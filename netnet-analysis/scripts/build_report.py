"""Bundle the analysis outputs (data/*.csv|json, data/market/*) into one JSON blob and inject it into
report.template.html -> report.html (the HTML version of README.md, with charts)."""
import csv, datetime, json, os
from paths import DATA, ROOT

M = os.path.join(DATA, "market")


def rows(fn):
    return list(csv.DictReader(open(os.path.join(DATA, fn))))


def f(x, nd=2):
    try:
        return round(float(x), nd)
    except (TypeError, ValueError):
        return None


def main():
    st = json.load(open(os.path.join(DATA, "latest_state.json")))
    hist = [r for r in json.load(open(os.path.join(DATA, "history_12h.json"))) if r.get("nav") and r.get("spot") and r["time"] != "latest"]
    history = [{"t": r["time"][:16], "price": f(r["spot"]), "nav": f(r["nav"]), "premium": f(r["premium"], 3), "supply": f(r["supply"], 0)} for r in hist]
    history.append({"t": datetime.datetime.utcfromtimestamp(st["ts"]).strftime("%Y-%m-%dT%H:%M"), "price": f(st["spot"]), "nav": f(st["nav"]), "premium": f(st["premium"], 3), "supply": f(st["supply"], 0)})

    weekly = [{"week": r["week_from"], "days": int(r["days"]), "rebase": f(r["mint_rebase"], 0), "bond": f(r["mint_bond"], 0),
               "pteam": f(r["mint_pteam"], 0), "premium": f(r["mint_premium"], 0), "bond_claim": f(r["bond_claim"], 0)}
              for r in rows("weekly_supply_flows.csv") if int(r["days"]) > 1]

    cat = {}
    for r in rows("net_flow_by_category_30d.csv"):
        c = cat.setdefault(r["category"], {"buy": 0, "sell": 0, "wallets_buy": 0, "wallets_sell": 0})
        if r["side"] == "net_buyers":
            c["buy"] += float(r["net_usd"]); c["wallets_buy"] += int(r["wallets"])
        else:
            c["sell"] += float(r["net_usd"]); c["wallets_sell"] += int(r["wallets"])
    categories = [{"key": k, "net": round(v["buy"] + v["sell"]), "buy": round(v["buy"]), "sell": round(v["sell"]),
                   "wallets_buy": v["wallets_buy"], "wallets_sell": v["wallets_sell"]} for k, v in cat.items()]

    sleeve = [{"date": r["date"], "net": f(r["net_bought"], 1), "usd": f(r["usd_at_4h_close"], 0)} for r in rows("sleeve_net_buys_daily.csv")]
    team = json.load(open(os.path.join(DATA, "team_summary.json")))
    s = team["sleeve"]
    sleeve_book = {"net": s["net"], "wsnet": s["wsnet"], "index": st["index"], "usdg": s["usdg"],
                   "wallet_stocks_usd": sum(v["usd"] for v in s["wallet_stocks"].values()),
                   "morpho_collateral_usd": s["morpho_collateral_usd"], "morpho_debt_usd": s["morpho_debt_usd"],
                   "markets": {k: {"collateral_usd": v["collateral_usd"], "debt_usd": v["debt_usd"],
                                   "util": (v["market_borrow_usd"] / v["market_supply_usd"]) if v["market_supply_usd"] else None}
                               for k, v in s["morpho"].items() if v["collateral"]},
                   "bought_net": team["sleeve_net_bought"], "bought_usd": team["sleeve_net_bought_usd"],
                   "pteam_exercised": team["pteam_exercised_net"], "pteam_now": team["pteam_exercisable_now_net"],
                   "pteam_same_tx": team["pteam_txs_mint_and_desk_same_tx"], "pteam_txs": team["pteam_txs_total"],
                   "desk_sale_est_usd": team["est_desk_sale_usd"], "owners": team["safe_owners"]}
    desks = [{"addr": r["desk"], "name": r["name"], "usdg_in": f(r["usdg_in"], 0), "to_treasury": f(r["to_treasury"], 0), "to_router": f(r["to_router_0xc941"], 0)}
             for r in rows("desk_usdg_flows.csv")]

    def traders(fn):
        t = rows(fn)
        pick = lambda part: [{"addr": r["address"], "label": r["label"], "net": f(r["net_usd"], 0), "buy": f(r["buy_usd"], 0), "sell": f(r["sell_usd"], 0),
                              "bond_claim": f(r["bond_claim_net"], 1)} for r in part]
        return {"sellers": pick(t[:8]), "buyers": pick(t[50:58])}

    chain = [{"week_start": r["week_start"], "week_end": r["week_end"], "dex": f(r["dex_volume_musd"], 1), "fees": f(r["fees_musd"], 2),
              "tvl": f(r["tvl_end_musd"], 1), "stables": f(r["stablecoins_end_musd"], 1), "eth": f(r["l1_bridge_eth_end"], 0), "btc": f(r["btc_usd_end"], 0)}
             for r in csv.DictReader(open(os.path.join(M, "rh_chain_weekly.csv")))]
    chain_sum = json.load(open(os.path.join(M, "rh_chain_summary.json")))
    snap = json.load(open(os.path.join(M, "market_snapshot.json")))
    cg = json.load(open(os.path.join(DATA, "cg_coin.json")))["market_data"]
    eco = [{"symbol": "NET", "chg30": cg["price_change_percentage_30d"], "chg7": cg["price_change_percentage_7d"], "mcap": None}]
    eco += [{"symbol": x["symbol"].upper(), "chg30": x["chg_30d_pct"], "chg7": x["chg_7d_pct"], "mcap": x["mcap"]} for x in snap["rh_ecosystem_tokens"]]
    eco += [{"symbol": k, "chg30": snap[k]["chg_30d_pct"], "chg7": snap[k]["chg_7d_pct"], "mcap": None} for k in ("BTC", "ETH")]

    # Robinhood Chain capital flows (rh_flows.py, rh_flow_summary.py, rh_protocols.py)
    mrows = lambda fn: list(csv.DictReader(open(os.path.join(M, fn))))
    rh_weekly = [{k: (v if k == "week_end" else (v == "True") if k == "partial" else f(v, 2)) for k, v in r.items()} for r in mrows("rh_flow_weekly.csv")]
    sup = {r["date"]: r for r in mrows("rh_daily_flows.csv")}
    stk = {r["date"]: r for r in mrows("rh_stock_supply_daily.csv")}
    mor = {r["date"]: r for r in mrows("rh_morpho_usdg_daily.csv")}
    act = {r["date"]: r for r in mrows("rh_activity.csv")}
    bridge = {x["time"][:10]: x["eth"] for x in json.load(open(os.path.join(M, "rh_l1_bridge_eth.json")))}
    rh_daily = [{"d": d, "usdg": f(float(r["USDG"]) / 1e6, 1), "usde": f(float(r["USDe"]) / 1e6, 1), "u": f(float(r["U"] or 0) / 1e6, 1),
                 "earn": f(float(r["steakUSDG"]) / 1e6, 1), "stocks": f(float(stk[d]["usd_const_price"]) / 1e6, 2) if d in stk else None,
                 "m_supply": f(float(mor[d]["supply"]) / 1e6, 1) if d in mor else None, "m_borrow": f(float(mor[d]["borrow"]) / 1e6, 1) if d in mor else None,
                 "tx": f(float(act[d]["user_tx_est"]) / 1e6, 2) if d in act else None, "eth": f(bridge.get(d), 0)}
                for d, r in sup.items() if d != "head"]
    rh_sum = json.load(open(os.path.join(M, "rh_flow_summary.json")))
    by = dict(json.load(open(os.path.join(M, "rh_morpho_usdg_borrow_by_collateral.json"))))
    morpho_coll = [[k, by.get(k, 0)] for k in ("USDe", "syrupUSDG", "mGLO", "spUSDG")]
    morpho_coll += [["Cổ phiếu token hoá", float(mor["head"]["borrow_stock_tokens"])], ["wsNET (NetNet)", by.get("wsNET", 0)]]
    morpho_coll.append(["Khác", float(mor["head"]["borrow"]) - sum(v for _, v in morpho_coll)])
    rh_proto = [{"name": r["name"], "cat": r["category"], "tvl": f(r["tvl"], 0), "chg7": f(r["chg_7d"], 1), "chg30": f(r["chg_30d"], 1)} for r in mrows("rh_protocols.csv")[:14]]
    fees_cat = [{k: (v if k == "week_end" else f(v, 0)) for k, v in r.items()} for r in mrows("rh_fees_by_category_weekly.csv")]
    dex_proto = [{k: (v if k == "week_end" else f(v, 0)) for k, v in r.items()} for r in mrows("rh_dex_by_protocol_weekly.csv")]
    loop = json.load(open(os.path.join(DATA, "loopback_summary.json")))

    hs = json.load(open(os.path.join(DATA, "hs_get_token.json")))["market"]
    ev = json.load(open(os.path.join(DATA, "hs_evidence_24h.json")))["item"]
    pools = [{"dex": r["dex"], "ver": r["version"], "pair": r["pair"], "quote": r["quote"], "liq": f(r["liquidity_usd"], 0), "vol": f(r["volume_24h_usd"], 0)}
             for r in rows("pools.csv")[:8]]
    holders = rows("holders_top100.csv")

    data = {
        "asof": datetime.datetime.utcfromtimestamp(st["ts"]).strftime("%Y-%m-%d %H:%M UTC"),
        "state": {k: st[k] for k in ("spot", "twap", "nav", "premium", "rate", "supply", "staked", "rfv", "liquid", "morpho", "pteam_ex", "pteam_now",
                                     "inv_price", "inv_cap", "bd_net", "pool_net", "pool_usdg", "index")},
        "history": history, "weekly_mints": weekly, "categories": categories, "sleeve_daily": sleeve, "sleeve": sleeve_book,
        "desks": desks, "traders7": traders("top_traders_7d.csv"), "traders30": traders("top_traders_30d.csv"),
        "chain_weekly": chain, "chain": chain_sum, "macro": {k: snap[k] for k in ("BTC", "ETH", "fear_greed", "global")},
        "stock_tokens": {k: snap["stock_tokens"][k] for k in ("count", "marketCap", "volume24", "liquidity")}, "memes": snap["meme_coins"],
        "eco": eco, "net_cg": {"chg7": cg["price_change_percentage_7d"], "chg30": cg["price_change_percentage_30d"], "ath": cg["ath"]["usd"]},
        "hoodscan": {"h24": hs["h24"], "d7": hs["d7"], "mix": {k: v for k, v in ev["participantMix"].items() if isinstance(v, dict)}, "net24": ev["metrics"]["netFlowUsd"]},
        "pools": pools, "holders_top": [{"addr": r["address"], "eq": f(r["net_equivalent"], 1), "label": r["label"]} for r in holders[:12]],
        "rh_weekly": rh_weekly, "rh_daily": rh_daily, "rh_sum": rh_sum, "morpho_coll": morpho_coll, "rh_proto": rh_proto, "fees_cat": fees_cat, "dex_proto": dex_proto,
        "loopback": {k: loop[k] for k in ("supply_usdg", "borrow_usdg", "util_pct", "borrow_apr_pct", "oracle_net_usd", "collateral_net_eq", "borrowers",
                                          "aggregate_ltv", "ladder", "sleeve")},
    }
    tpl = open(os.path.join(ROOT, "report.template.html")).read()
    html = tpl.replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False, separators=(",", ":")))
    out = os.path.join(ROOT, "report.html")
    open(out, "w").write(html)
    print(out, len(html), "bytes;", len(history), "history points,", len(chain), "chain weeks")


if __name__ == "__main__":
    main()
