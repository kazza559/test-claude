"""Turn raw/flows.json + data/*.json into the small CSV tables the report cites, plus data/summary.json."""
import collections, csv, datetime, json, os
from flows import POOLS, label
from paths import DATA, RAW


def w_csv(name, header, rows):
    with open(os.path.join(DATA, name), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


def main():
    hist = json.load(open(os.path.join(DATA, "history_12h.json")))
    keys = ["time", "block", "spot", "twap", "nav", "premium", "rate", "supply", "staked", "index", "rfv", "liquid", "morpho", "pool_net", "pool_usdg", "pteam_ex", "pteam_now", "bd_net", "inv_price", "inv_cap", "ps_active"]
    w_csv("protocol_history_12h.csv", keys, [[r.get(k) for k in keys] for r in hist])

    f = json.load(open(os.path.join(RAW, "flows.json")))
    days, wallets = f["days"], f["wallets"]
    close = {datetime.datetime.utcfromtimestamp(x[0]).strftime("%Y-%m-%d"): x[4]
             for x in json.load(open(os.path.join(DATA, "gt_ohlcv_day.json")))["data"]["attributes"]["ohlcv_list"]}
    dk = ["mint_rebase", "mint_bond", "mint_pteam", "mint_premium", "mint_genesis", "burn", "bond_claim", "desk_claim", "desk_fill", "stake", "unstake",
          "tax_in", "tax_sell", "inverse_bond", "pool_out", "pool_in", "users_buy_usd", "users_sell_usd", "buyers", "sellers"]
    w_csv("daily_flows.csv", ["date", "close_usd"] + dk, [[d, close.get(d)] + [round(v.get(k, 0), 4) for k in dk] for d, v in days.items()])

    g = lambda w, k: w.get(k, 0.0)
    for win in ("7", "30"):
        rows = sorted(wallets.items(), key=lambda x: g(x[1], "buy_usd" + win) - g(x[1], "sell_usd" + win))
        pick = rows[:50] + rows[::-1][:50]
        w_csv(f"top_traders_{win}d.csv", ["address", "label", "buy_usd", "sell_usd", "net_usd", "bond_claim_net", "transfers_in_net", "transfers_out_net", "tx_count_all_time"],
              [[a, label(a) or "", round(g(w, "buy_usd" + win)), round(g(w, "sell_usd" + win)), round(g(w, "buy_usd" + win) - g(w, "sell_usd" + win)),
                round(g(w, "bondclaim_" + win), 3), round(g(w, "xfer_in_" + win), 3), round(g(w, "xfer_out_" + win), 3), int(g(w, "n"))] for a, w in pick])

    # 30-day net DEX flow by wallet category
    cat = collections.defaultdict(lambda: [0, 0.0])
    for a, w in wallets.items():
        net = g(w, "buy_usd30") - g(w, "sell_usd30")
        if not (g(w, "buy_usd30") or g(w, "sell_usd30")):
            continue
        if a == "0x498752d5fa0600cbd613074c151abe15b3fec7cb":
            c = "team_rwa_sleeve"
        elif g(w, "bondclaim_30") > 1:
            c = "bond_claimers"
        else:
            c = "other_wallets"
        side = "net_buyers" if net > 0 else "net_sellers"
        cat[(c, side)][0] += 1
        cat[(c, side)][1] += net
    w_csv("net_flow_by_category_30d.csv", ["category", "side", "wallets", "net_usd"], [[c, s, n, round(v)] for (c, s), (n, v) in sorted(cat.items())])

    # weekly supply table (weeks starting Friday so the last full week ends on Thursday)
    wk = collections.defaultdict(lambda: collections.defaultdict(float))
    for d, v in days.items():
        dt = datetime.date.fromisoformat(d)
        k = (dt - datetime.timedelta(days=(dt.weekday() - 4) % 7)).isoformat()
        for kk, vv in v.items():
            wk[k][kk] += vv
        wk[k]["days"] += 1
        if close.get(d):
            wk[k]["close"] = close[d]
    w_csv("weekly_supply_flows.csv", ["week_from", "days", "close_usd", "mint_rebase", "mint_bond", "mint_pteam", "mint_premium", "bond_claim", "desk_claim", "stake", "unstake", "pool_net_in"],
          [[k, int(v["days"]), v.get("close"), round(v["mint_rebase"]), round(v["mint_bond"]), round(v["mint_pteam"]), round(v["mint_premium"]),
            round(v["bond_claim"]), round(v["desk_claim"]), round(v["stake"]), round(v["unstake"]), round(v["pool_in"] - v["pool_out"])] for k, v in sorted(wk.items())])

    ds = json.load(open(os.path.join(DATA, "ds_token.json")))["pairs"]
    w_csv("pools.csv", ["dex", "version", "pair", "base", "quote", "liquidity_usd", "volume_24h_usd", "txns_24h_buys", "txns_24h_sells", "price_usd", "created"],
          [[p["dexId"], ",".join(p.get("labels") or []), p["pairAddress"], p["baseToken"]["symbol"], p["quoteToken"]["symbol"], (p.get("liquidity") or {}).get("usd"),
            p["volume"].get("h24"), p["txns"]["h24"]["buys"], p["txns"]["h24"]["sells"], p["priceUsd"],
            datetime.datetime.utcfromtimestamp(p["pairCreatedAt"] / 1000).strftime("%Y-%m-%d") if p.get("pairCreatedAt") else ""]
           for p in sorted(ds, key=lambda p: -((p.get("liquidity") or {}).get("usd") or 0))])

    summary = {"mint_sources_all_time": f["mint_src"], "transactions": f["ntx"], "wallets": len(wallets),
               "net_flow_by_category_30d": {f"{c}/{s}": {"wallets": n, "net_usd": round(v)} for (c, s), (n, v) in cat.items()}}
    for win in ("7", "30"):
        summary[f"dex_user_flows_{win}d"] = {"buy_usd": round(sum(g(w, "buy_usd" + win) for w in wallets.values())),
                                            "sell_usd": round(sum(g(w, "sell_usd" + win) for w in wallets.values())),
                                            "bond_claims_net": round(sum(g(w, "bondclaim_" + win) for w in wallets.values()), 1)}
    json.dump(summary, open(os.path.join(DATA, "summary.json"), "w"), indent=1)
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
