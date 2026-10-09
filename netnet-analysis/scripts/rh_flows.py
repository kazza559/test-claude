"""Robinhood Chain capital flows measured on chain, day by day (00:00 UTC):

* stablecoin supply on the chain: USDG (Paxos, issued natively), USDe (Ethena OFT, bridged in through LayerZero),
  U (United Stables) -> daily mint/burn = net new stablecoin money
* USDG parked in the Steakhouse USDG Morpho vault (yield deposits, Robinhood Earn) and WETH supply on L2
* activity proxy: user transactions per day, estimated by sampling blocks (minus the one ArbOS start-block tx per block)
* ETH locked in the canonical L1 bridge comes from rh_chain.py (data/market/rh_l1_bridge_eth.json)

* tokenized stocks (Robinhood stock/ETF tokens, roster from HoodScan): daily on-chain supply valued at today's prices
  -> net issuance (mint - burn) at constant prices, i.e. money moved into stock tokens on the chain
* Morpho Blue markets that lend USDG: total supplied / borrowed per day, borrow split by collateral (stablecoin loops, stock tokens, wsNET, ETH...)
  -> leverage demand on the chain

Writes data/market/rh_daily_flows.csv, rh_activity.csv, rh_stock_supply_daily.csv, rh_morpho_usdg_daily.csv.
"""
import csv, datetime, json, os, sys, time
import requests
from mc import multicall
from blocktime import block_at, _A
from paths import DATA, RAW
from rpc import get_logs, topic
import anchors

M = os.path.join(DATA, "market")
R = "https://robinhood.drpc.org"
TOK = {  # symbol: (address, decimals, call)
    "USDG": ("0x5fc5360d0400a0fd4f2af552add042d716f1d168", 6, "totalSupply()"),
    "USDe": ("0x5d3a1ff2b6bab83b63cd9ad0787074081a52ef34", 18, "totalSupply()"),
    "U": ("0xce24439f2d9c6a2289f741120fe202248b666666", 18, "totalSupply()"),
    "WETH": ("0x0bd7d308f8e1639fab988df18a8011f41eacad73", 18, "totalSupply()"),
    "steakUSDG": ("0xbeeff033f34c046626b8d0a041844c5d1a5409dd", 6, "totalAssets()"),  # vault assets are USDG units (6 decimals)
}


def day_ts(d):
    return int(datetime.datetime(d.year, d.month, d.day, tzinfo=datetime.timezone.utc).timestamp())


def head_block():
    return int(requests.post(R, json={"jsonrpc": "2.0", "id": 1, "method": "eth_blockNumber", "params": []}, timeout=30).json()["result"], 16)


def day_blocks(start=datetime.date(2026, 7, 1)):
    """[(label, block)] for every UTC midnight since `start`, plus ("head", head block)."""
    head = head_block()
    out, d = [], start
    today = datetime.datetime.now(datetime.timezone.utc).date()
    first_b, first_t = _A[0]
    while d <= today:
        if day_ts(d) < first_t:  # before the first anchor: binary search the exact midnight block
            b = anchors.block_at(day_ts(d), 1, first_b)
        else:
            b = block_at(day_ts(d))
        if b <= head:
            out.append((d.isoformat(), b))
        d += datetime.timedelta(days=1)
    return out + [("head", head)]


def mc_retry(calls, b, chunk=150):
    out = []
    for k in range(0, len(calls), chunk):
        res = None
        for i in range(4):
            try:
                res = multicall(calls[k:k + chunk], b)
                break
            except Exception:  # noqa: BLE001
                time.sleep(3 * (i + 1))
        if res is None:
            return None
        out += res
    return out


def supply_series(start=datetime.date(2026, 7, 1)):
    rows = []
    for d, b in day_blocks(start):
        calls = [(a, sig, [], [], ["uint256"]) for a, dec, sig in TOK.values()]
        res = mc_retry(calls, b)
        if res is None:
            continue
        row = {"date": d, "block": b}
        for (sym, (a, dec, sig)), v in zip(TOK.items(), res):
            row[sym] = (v / 10 ** dec) if v is not None else None
        rows.append(row)
        print(row["date"], {k: (round(v / 1e6, 2) if isinstance(v, float) and k != "WETH" else (round(v, 1) if isinstance(v, float) else v)) for k, v in row.items() if k not in ("date", "block")}, flush=True)
    return rows


ACT_RPC = "https://rpc.mainnet.chain.robinhood.com"  # drpc's free plan caps JSON-RPC batches at 3 requests


def activity(start=datetime.date(2026, 7, 1), per_day=100):
    """User tx per day ~= mean(tx in sampled blocks - 1 ArbOS start tx) x blocks that day."""
    s = requests.Session()
    out = []
    mids = [(d, b) for d, b in day_blocks(start) if d != "head"]
    for (d, b0), (_, b1) in zip(mids, mids[1:]):
        nums = [b0 + int((b1 - b0) * (i + 0.5) / per_day) for i in range(per_day)]
        batch = [{"jsonrpc": "2.0", "id": i, "method": "eth_getBlockByNumber", "params": [hex(n), False]} for i, n in enumerate(nums)]
        res = None
        for i in range(4):
            try:
                r = s.post(ACT_RPC, json=batch, timeout=60).json()
                if isinstance(r, list) and all("result" in x for x in r):
                    res = r
                    break
            except Exception:  # noqa: BLE001
                pass
            time.sleep(3 * (i + 1))
        if not res:
            continue
        txs = [max(0, len(x["result"]["transactions"]) - 1) for x in res if x.get("result")]
        gas = [int(x["result"]["gasUsed"], 16) for x in res if x.get("result")]
        blocks = b1 - b0
        out.append({"date": d, "blocks": blocks, "user_tx_est": round(sum(txs) / len(txs) * blocks), "avg_tx_per_block": round(sum(txs) / len(txs), 3),
                    "gas_used_est": round(sum(gas) / len(gas) * blocks)})
        print(out[-1], flush=True)
    return out


def write(fn, rows):
    if not rows:
        return
    keys = list(rows[0].keys())
    with open(os.path.join(M, fn), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        w.writerows(rows)


def stock_supply(start=datetime.date(2026, 7, 1), top=10):
    """Daily on-chain supply of every Robinhood stock/ETF token, valued at today's price (constant-price issuance)."""
    st = json.load(open(os.path.join(RAW, "market", "hs_stocks.json")))["stocks"]
    toks = [(x["symbol"], x["address"], x.get("price") or 0) for x in st if x.get("address")]
    dec = mc_retry([(a, "decimals()", [], [], ["uint8"]) for _, a, _ in toks], "latest")
    toks = [(sym, a, px, dc if dc is not None else 18) for (sym, a, px), dc in zip(toks, dec)]
    rows = []
    for d, b in day_blocks(start):
        res = mc_retry([(a, "totalSupply()", [], [], ["uint256"]) for _, a, _, _ in toks], b)
        if res is None:
            continue
        usd = {sym: (v / 10 ** dc) * px if v else 0.0 for (sym, a, px, dc), v in zip(toks, res)}
        rows.append({"date": d, "block": b, "tokens_live": sum(1 for v in res if v), "usd_const_price": round(sum(usd.values())), "usd": usd})
        print(d, rows[-1]["tokens_live"], round(rows[-1]["usd_const_price"] / 1e6, 2), flush=True)
    last = rows[-1]["usd"]
    lead = [sym for sym, _ in sorted(last.items(), key=lambda x: -x[1])[:top]]
    out = []
    for r in rows:
        o = {k: r[k] for k in ("date", "block", "tokens_live", "usd_const_price")}
        for sym in lead:
            o[sym] = round(r["usd"].get(sym, 0))
        o["other"] = round(r["usd_const_price"] - sum(o[sym] for sym in lead))
        out.append(o)
    return out


MORPHO = "0x9d53d5e3bd5e8d4cbfa6db1ca238aea02e651010"
USDG = TOK["USDG"][0]
WSNET = "0x63c12667638f2ae6fc6ae09b43d98ec84a8586ea"


def morpho_usdg(start=datetime.date(2026, 7, 1)):
    """Morpho Blue markets lending USDG: daily total supply / borrow, borrow split by collateral class."""
    head = head_block()
    logs = get_logs(MORPHO, [topic("CreateMarket(bytes32,(address,address,address,address,uint256))")], 1, head)
    mk = []
    for lg in logs:
        w = lg["data"][2:]
        loan, coll = "0x" + w[24:64], "0x" + w[64 + 24:128]
        if loan.lower() == USDG:
            mk.append((lg["topics"][1], coll.lower(), int(w[256:320], 16) / 1e18))
    stocks = {x["address"].lower(): x["symbol"] for x in json.load(open(os.path.join(RAW, "market", "hs_stocks.json")))["stocks"]}
    syms = mc_retry([(c, "symbol()", [], [], ["string"]) for _, c, _ in mk], "latest")

    def cls(c, sym):
        if c in stocks:
            return "stock_tokens"
        if c == WSNET:
            return "wsNET"
        if sym and "USD" in sym.upper():  # USDe, sUSDe, syrupUSDG, spUSDG...: stablecoin loops
            return "stables"
        if sym and "ETH" in sym.upper():
            return "ETH"
        return "other"
    kinds = [cls(c, sym) for (_, c, _), sym in zip(mk, syms)]
    print(len(logs), "markets,", len(mk), "lend USDG:", {k: kinds.count(k) for k in set(kinds)}, flush=True)
    rows = []
    for d, b in day_blocks(start):
        res = mc_retry([(MORPHO, "market(bytes32)", ["bytes32"], [bytes.fromhex(i[2:])], ["uint128"] * 6) for i, _, _ in mk], b)
        if res is None:
            continue
        row = {"date": d, "block": b, "supply": 0.0, "borrow": 0.0, "borrow_stables": 0.0, "borrow_stock_tokens": 0.0, "borrow_wsNET": 0.0, "borrow_ETH": 0.0, "borrow_other": 0.0, "markets_live": 0}
        for v, k in zip(res, kinds):
            if not v or not v[0]:
                continue
            row["markets_live"] += 1
            row["supply"] += v[0] / 1e6
            row["borrow"] += v[2] / 1e6
            row["borrow_" + k] += v[2] / 1e6
        row = {k: (round(v) if isinstance(v, float) else v) for k, v in row.items()}
        row["util_pct"] = round(row["borrow"] / row["supply"] * 100, 1) if row["supply"] else None
        rows.append(row)
        print(row, flush=True)
    by = {}
    for (i, c, lltv), sym, k, v in zip(mk, syms, kinds, mc_retry([(MORPHO, "market(bytes32)", ["bytes32"], [bytes.fromhex(i[2:])], ["uint128"] * 6) for i, _, _ in mk], head)):
        if v and v[2]:
            by[sym or c] = by.get(sym or c, 0) + v[2] / 1e6
    json.dump(sorted(by.items(), key=lambda x: -x[1]), open(os.path.join(M, "rh_morpho_usdg_borrow_by_collateral.json"), "w"), indent=1)
    return rows


if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "all"
    if what in ("all", "supply"):
        write("rh_daily_flows.csv", supply_series())
    if what in ("all", "activity"):
        write("rh_activity.csv", activity())
    if what in ("all", "stocks"):
        write("rh_stock_supply_daily.csv", stock_supply())
    if what in ("all", "morpho"):
        write("rh_morpho_usdg_daily.csv", morpho_usdg())
