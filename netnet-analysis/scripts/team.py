"""Team-controlled flows: pTEAM exercises, where the minted NET went, the RWA Sleeve and its Morpho positions.

Needs raw/team_transfers_raw.json and raw/sleeve_transfers.json (run trace_addr.py for the Team Safe and the
Sleeve first) plus data/history_12h.json for prices. Writes data/team_pteam_to_desks.csv,
data/sleeve_net_buys_daily.csv and data/team_summary.json.
"""
import bisect, collections, csv, datetime, json, os
from eth_abi import decode
from mc import multicall
from rpc import eth_call, sel
from paths import DATA, RAW

ZERO = "0x0000000000000000000000000000000000000000"
TEAM = "0x3bb7a23316f82c0e984fa2e784846d8928a35f42"
SLEEVE = "0x498752d5fa0600cbd613074c151abe15b3fec7cb"
STAKING = "0xb078cc304a0b264c5f3680dc0488954accd02e87"
MORPHO = "0x9d53d5e3bd5e8d4cbfa6db1ca238aea02e651010"
DESKS = {
    "0x99b6ee6ede47d9a8a9bfd03f728a99b789df1961": "RwaDesk (listed)", "0xa84efc3136bf1bb89ade9e5be6ab32cb1a04f08d": "RwaDesk (unlisted 0xa84e)",
    "0x2f2f215b810fa692304cb0095804ab3c8e4cef78": "RwaDesk (unlisted 0x2f2f)", "0x70eaeec20c39df48509f1f3fab01f7dde207947b": "Desk (unlisted 0x70ea)",
    "0x7cf28d61d42352eb2fd68167e9b08f73cbbf21eb": "PackDesk (Superstore)",
}
MARKETS = {  # Morpho Blue stock-token markets (docs: /credit)
    "NVDA": ("0x8b16891f032a93b771347c9cb470a780e6699dd701553d3402aa3cdba6189c3e", "0xd0601ce157db5bdc3162bbac2a2c8af5320d9eec"),
    "SPCX": ("0x9b4b47cdf7e295341c6c6cdfd3efb9805c4a5b3d580dba0c0c39d3a4232b297b", "0x4a0e65a3eccec6dbe60ae065f2e7bb85fae35eea"),
    "AAPL": ("0xdeb4782d012d5fd3b24962538c2f6559049d70bda4dabd2e4212dacb96c28d45", "0xaf3d76f1834a1d425780943c99ea8a608f8a93f9"),
    "GOOGL": ("0x7fa81b10e5d21b2e4c571f862442bc11aff2ed14f02335868d0ff933fd40d0ba", "0x2e0847e8910a9732eb3fb1bb4b70a580adad4fe3"),
    "MSFT": ("0x2e1859aa8f143b7220088f80562c6dfe0bf8e52b87d9cedf8da8805f231994ce", "0xe93237c50d904957cf27e7b1133b510c669c2e74"),
    "COIN": ("0x3ebd43d91c3960a9fac32bedd5c60428e0e414de5bdd67fda770207afb0eb615", "0x6330d8c3178a418788df01a47479c0ce7ccf450b"),
}


def by_symbol(d):
    """Accept {symbol: {out, in}} or the older flat {out, in} layout."""
    if "out" not in d:
        return d
    from trace_addr import TOKENS
    res = collections.defaultdict(lambda: {"out": [], "in": []})
    for side in ("out", "in"):
        for l in d[side]:
            res[TOKENS.get(l["address"].lower(), l["address"].lower())][side].append(l)
    return res


from blocktime import ts_of


def price_fn():
    c = sorted(json.load(open(os.path.join(DATA, "gt_ohlcv_4h.json")))["data"]["attributes"]["ohlcv_list"])
    t, p = [x[0] for x in c], [x[4] for x in c]
    return lambda ts: p[max(bisect.bisect_right(t, ts) - 1, 0)]


def stock_prices():
    import requests
    st = requests.get("https://hoodscan.co/stocks-api", timeout=60).json()
    return {s["address"].lower(): s.get("price") or 0 for s in st.get("stocks", [])}


def main():
    px = price_fn()
    d = by_symbol(json.load(open(os.path.join(RAW, "team_transfers_raw.json"))))
    by_tx = collections.defaultdict(list)
    for side in ("in", "out"):
        for l in d["NET"][side]:
            by_tx[l["transactionHash"]].append((int(l["blockNumber"], 16), "0x" + l["topics"][1][-40:], "0x" + l["topics"][2][-40:], int(l["data"], 16) / 1e9))
    rows, same_tx = [], 0
    for tx, ls in by_tx.items():
        minted = sum(a for b, fr, to, a in ls if fr == ZERO)
        to_desk = [(DESKS.get(to, to), a) for b, fr, to, a in ls if fr == TEAM and to != STAKING]
        if minted and to_desk:
            same_tx += 1
        b = ls[0][0]
        t = ts_of(b)
        for dest, a in to_desk:
            rows.append([datetime.datetime.utcfromtimestamp(t).strftime("%Y-%m-%d %H:%M"), tx, round(minted, 4), dest, round(a, 4), round(px(t), 2), round(a * px(t) * 0.935, 2)])
    rows.sort()
    with open(os.path.join(DATA, "team_pteam_to_desks.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["time_utc", "tx", "net_minted_by_pteam_in_tx", "destination", "net_sent", "twap_usd", "est_desk_sale_usd(twap*0.935)"])
        w.writerows(rows)
    # Sleeve: NET bought on the market (NET received from anything but Staking / Team Safe)
    sv = by_symbol(json.load(open(os.path.join(RAW, "sleeve_transfers.json"))))
    daily = collections.defaultdict(lambda: [0.0, 0.0])
    for l in sv["NET"]["in"]:
        fr = "0x" + l["topics"][1][-40:]
        if fr in (STAKING, TEAM):
            continue
        b = int(l["blockNumber"], 16)
        a = int(l["data"], 16) / 1e9
        t = ts_of(b)
        k = datetime.datetime.utcfromtimestamp(t).strftime("%Y-%m-%d")
        daily[k][0] += a
        daily[k][1] += a * px(t)
    with open(os.path.join(DATA, "sleeve_net_buys_daily.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["date", "net_bought", "usd_at_4h_close"])
        for k in sorted(daily):
            w.writerow([k, round(daily[k][0], 4), round(daily[k][1], 2)])
    # Safe owners, Sleeve holdings and Morpho positions
    owners = {}
    for name, s in (("TeamSafe", TEAM), ("RWASleeve", SLEEVE)):
        o = eth_call(s, sel("getOwners()"))
        th = eth_call(s, sel("getThreshold()"))
        owners[name] = {"owners": list(decode(["address[]"], bytes.fromhex(o[2:]))[0]), "threshold": int(th, 16)}
    sp = stock_prices()
    calls = []
    for sym, (mid, tok) in MARKETS.items():
        ib = bytes.fromhex(mid[2:])
        calls += [(MORPHO, "position(bytes32,address)", ["bytes32", "address"], [ib, SLEEVE], ["uint256", "uint128", "uint128"]),
                  (MORPHO, "market(bytes32)", ["bytes32"], [ib], ["uint128"] * 6),
                  (tok, "balanceOf(address)", ["address"], [SLEEVE], ["uint256"])]
    calls += [("0xca9c78dd337a67f6e0077f65f5e9218719d30edf", "balanceOf(address)", ["address"], [SLEEVE], ["uint256"]),
              ("0x63c12667638f2ae6fc6ae09b43d98ec84a8586ea", "balanceOf(address)", ["address"], [SLEEVE], ["uint256"]),
              ("0x5fc5360d0400a0fd4f2af552add042d716f1d168", "balanceOf(address)", ["address"], [SLEEVE], ["uint256"]),
              ("0x650f58079daa17ee28928c2f92d22291d038b2b0", "exercised()", [], [], ["uint256"]),
              ("0x650f58079daa17ee28928c2f92d22291d038b2b0", "exercisableNow()", [], [], ["uint256"])]
    res = multicall(calls, "latest")
    morpho, wallet_stocks = {}, {}
    for i, (sym, (mid, tok)) in enumerate(MARKETS.items()):
        pos, mkt, bal = res[3 * i], res[3 * i + 1], res[3 * i + 2]
        p = sp.get(tok, 0)
        col = pos[2] / 1e18 if pos else 0
        debt = pos[1] * mkt[2] / mkt[3] / 1e6 if pos and mkt and mkt[3] else 0
        morpho[sym] = {"collateral": col, "collateral_usd": col * p, "debt_usd": debt, "market_borrow_usd": (mkt[2] / 1e6 if mkt else 0), "market_supply_usd": (mkt[0] / 1e6 if mkt else 0)}
        wallet_stocks[sym] = {"qty": (bal or 0) / 1e18, "usd": (bal or 0) / 1e18 * p}
    k = 3 * len(MARKETS)
    summary = {
        "safe_owners": owners,
        "pteam_exercised_net": res[k + 3] / 1e9, "pteam_exercisable_now_net": res[k + 4] / 1e9,
        "pteam_txs_mint_and_desk_same_tx": same_tx, "pteam_txs_total": len(by_tx),
        "net_sent_to_desks": round(sum(r[4] for r in rows), 4), "est_desk_sale_usd": round(sum(r[6] for r in rows), 2),
        "sleeve": {"net": res[k] / 1e9, "wsnet": res[k + 1] / 1e18, "usdg": res[k + 2] / 1e6, "wallet_stocks": wallet_stocks, "morpho": morpho,
                   "morpho_collateral_usd": sum(m["collateral_usd"] for m in morpho.values()), "morpho_debt_usd": sum(m["debt_usd"] for m in morpho.values())},
        "sleeve_net_bought": round(sum(v[0] for v in daily.values()), 4), "sleeve_net_bought_usd": round(sum(v[1] for v in daily.values()), 2),
    }
    json.dump(summary, open(os.path.join(DATA, "team_summary.json"), "w"), indent=1)
    print(json.dumps({k: v for k, v in summary.items() if k != "sleeve"}, indent=1))
    print("sleeve morpho collateral", round(summary["sleeve"]["morpho_collateral_usd"]), "debt", round(summary["sleeve"]["morpho_debt_usd"]))


if __name__ == "__main__":
    main()
