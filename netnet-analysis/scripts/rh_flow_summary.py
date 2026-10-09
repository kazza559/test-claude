"""Weekly Robinhood Chain capital-flow table from the on-chain series (rh_flows.py) and the L1 bridge / DefiLlama
series (rh_chain.py): net new stablecoins by issuer, Robinhood Earn (Steakhouse USDG vault) deposits, Morpho USDG
borrowing, tokenized-stock issuance, ETH bridged from Ethereum, user transactions, DEX volume and fees.

Weeks match rh_chain_weekly.csv (DefiLlama days week_start .. week_end inclusive): on-chain deltas run from 00:00 UTC on
week_start to 00:00 UTC after week_end, or to the chain head for the current, still running week; the L1 bridge is
sampled daily at 13:12 UTC.
Writes data/market/rh_flow_weekly.csv and rh_flow_summary.json.
"""
import csv, datetime, json, os
from paths import DATA

M = os.path.join(DATA, "market")


def load(fn):
    return list(csv.DictReader(open(os.path.join(M, fn))))


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return 0.0


def by_date(rows):
    return {r["date"]: r for r in rows}


def peak(series):
    d, v = max(series.items(), key=lambda kv: kv[1])
    return {"date": d, "value": v}


def main():
    sup = by_date(load("rh_daily_flows.csv"))
    stk = by_date(load("rh_stock_supply_daily.csv"))
    mor = by_date(load("rh_morpho_usdg_daily.csv"))
    act = by_date(load("rh_activity.csv")) if os.path.exists(os.path.join(M, "rh_activity.csv")) else {}
    bridge = {x["time"][:10]: x["eth"] for x in json.load(open(os.path.join(M, "rh_l1_bridge_eth.json")))}
    chain = {r["week_end"]: r for r in load("rh_chain_weekly.csv")}
    snap = json.load(open(os.path.join(M, "market_snapshot.json")))
    eth_px = snap["ETH"]["price"]

    stables = lambda r: num(r["USDG"]) + num(r["USDe"]) + num(r["U"])
    rows = []
    for we in sorted(chain):
        s = chain[we]["week_start"]
        e = (datetime.date.fromisoformat(we) + datetime.timedelta(days=1)).isoformat()
        e = e if e in sup else "head"
        if s not in sup:
            continue
        a, b = sup[s], sup[e]
        days = [(datetime.date.fromisoformat(s) + datetime.timedelta(days=i)).isoformat() for i in range(7)]
        tx = [num(act[d]["user_tx_est"]) for d in days if d in act]
        bs, be = bridge.get((datetime.date.fromisoformat(s) - datetime.timedelta(days=1)).isoformat()), bridge.get(we)
        rows.append({
            "week_end": we, "partial": e == "head",
            "stables_end_musd": round(stables(b) / 1e6, 1),
            "stables_net_musd": round((stables(b) - stables(a)) / 1e6, 1),
            "usdg_net_musd": round((num(b["USDG"]) - num(a["USDG"])) / 1e6, 1),
            "usde_net_musd": round((num(b["USDe"]) - num(a["USDe"])) / 1e6, 1),
            "u_net_musd": round((num(b["U"]) - num(a["U"])) / 1e6, 1),
            "earn_vault_net_musd": round((num(b["steakUSDG"]) - num(a["steakUSDG"])) / 1e6, 1),
            "morpho_borrow_net_musd": round((num(mor[e]["borrow"]) - num(mor[s]["borrow"])) / 1e6, 1) if e in mor and s in mor else None,
            "stock_tokens_net_musd": round((num(stk[e]["usd_const_price"]) - num(stk[s]["usd_const_price"])) / 1e6, 1) if e in stk and s in stk else None,
            "bridge_eth_net": round(be - bs) if bs and be else None,
            "bridge_net_musd": round((be - bs) * eth_px / 1e6, 1) if bs and be else None,
            "user_tx_per_day_m": round(sum(tx) / len(tx) / 1e6, 2) if tx else None,
            "dex_volume_busd": round(num(chain[we]["dex_volume_musd"]) / 1e3, 2),
            "fees_musd": round(num(chain[we]["fees_musd"]), 1),
        })
    with open(os.path.join(M, "rh_flow_weekly.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    days = sorted(d for d in sup if d != "head")
    head = sup["head"]
    summ = {
        "eth_price": eth_px,
        "now": {"usdg": num(head["USDG"]), "usde": num(head["USDe"]), "u": num(head["U"]), "earn_vault": num(head["steakUSDG"]), "weth_l2": num(head["WETH"]),
                "stock_tokens_usd": num(stk["head"]["usd_const_price"]), "morpho_supply": num(mor["head"]["supply"]), "morpho_borrow": num(mor["head"]["borrow"]),
                "morpho_util_pct": num(mor["head"]["util_pct"]), "bridge_eth": bridge[max(bridge)]},
        "peak": {"stables": peak({d: stables(sup[d]) for d in days}), "usdg": peak({d: num(sup[d]["USDG"]) for d in days}),
                 "usde": peak({d: num(sup[d]["USDe"]) for d in days}), "earn_vault": peak({d: num(sup[d]["steakUSDG"]) for d in days}),
                 "stock_tokens_usd": peak({d: num(stk[d]["usd_const_price"]) for d in stk if d != "head"}),
                 "morpho_borrow": peak({d: num(mor[d]["borrow"]) for d in mor if d != "head"}), "bridge_eth": peak(bridge),
                 "user_tx_per_day": peak({d: num(r["user_tx_est"]) for d, r in act.items()}) if act else None},
        "morpho_borrow_by_collateral": json.load(open(os.path.join(M, "rh_morpho_usdg_borrow_by_collateral.json")))[:8],
    }
    summ["now"]["stables"] = summ["now"]["usdg"] + summ["now"]["usde"] + summ["now"]["u"]
    summ["earn_share_of_usdg_pct"] = round(summ["now"]["earn_vault"] / summ["now"]["usdg"] * 100, 1)
    json.dump(summ, open(os.path.join(M, "rh_flow_summary.json"), "w"), indent=1)
    for r in rows:
        print(r)
    print(json.dumps(summ, indent=1)[:2500])


if __name__ == "__main__":
    main()
