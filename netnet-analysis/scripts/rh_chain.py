"""Robinhood Chain capital-flow snapshot: DefiLlama TVL / stablecoins / DEX volume / fees, ETH locked in the
canonical L1 bridge (Ethereum archive RPC), plus BTC/ETH and Fear & Greed for context.

Raw API answers go to raw/market/ (git-ignored); data/market/ gets rh_chain_weekly.csv, rh_chain_summary.json,
rh_l1_bridge_eth.json, rh_stables_breakdown.json and market_snapshot.json.
Run with --cached to rebuild the summaries from files already in raw/market/.
"""
import collections, csv, datetime, json, os, statistics, sys, time
import requests
from paths import DATA, RAW

M = os.path.join(DATA, "market")
RM = os.path.join(RAW, "market")
os.makedirs(M, exist_ok=True)
os.makedirs(RM, exist_ok=True)
CHAIN = "Robinhood%20Chain"
L1_RPC = "https://eth.drpc.org"
L1_BRIDGE = "0xDf8755334ce7A73cCF6b581C02eA649AE3E864b3"  # docs.robinhood.com/chain/protocol-contracts
SOURCES = {
    "llama_tvl_hist.json": f"https://api.llama.fi/v2/historicalChainTvl/{CHAIN}",
    "llama_stables_hist.json": f"https://stablecoins.llama.fi/stablecoincharts/{CHAIN}",
    "llama_dex.json": f"https://api.llama.fi/overview/dexs/{CHAIN}?excludeTotalDataChart=false&excludeTotalDataChartBreakdown=true",
    "llama_fees.json": f"https://api.llama.fi/overview/fees/{CHAIN}?excludeTotalDataChart=false&excludeTotalDataChartBreakdown=true",
    "llama_stables_all.json": "https://stablecoins.llama.fi/stablecoins?includePrices=true",
    "fng.json": "https://api.alternative.me/fng/?limit=60",
    "cg_btc_90d.json": "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=90&interval=daily",
    "cg_eth_90d.json": "https://api.coingecko.com/api/v3/coins/ethereum/market_chart?vs_currency=usd&days=90&interval=daily",
    "cg_global.json": "https://api.coingecko.com/api/v3/global",
    "cg_rh_eco.json": "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&category=robinhood-ecosystem&order=market_cap_desc&per_page=30&page=1&price_change_percentage=24h,7d,30d",
    "hs_stocks.json": "https://hoodscan.co/stocks-api",
    "hs_memes.json": "https://hoodscan.co/meme-stocks-api",
}


def day(ts):
    return datetime.datetime.utcfromtimestamp(int(ts)).strftime("%Y-%m-%d")


def fetch():
    for fn, url in SOURCES.items():
        for i in range(3):
            r = requests.get(url, timeout=60)
            if r.status_code == 200:
                open(os.path.join(RM, fn), "w").write(r.text)
                break
            time.sleep(10 * (i + 1))


def l1_bridge_eth(days=98):
    s = requests.Session()

    def rpc(m, p):
        for _ in range(4):
            try:
                r = s.post(L1_RPC, json={"jsonrpc": "2.0", "id": 1, "method": m, "params": p}, timeout=40).json()
                if "result" in r:
                    return r["result"]
            except Exception:  # noqa: BLE001
                time.sleep(2)
        return None

    head = int(rpc("eth_blockNumber", []), 16)
    hts = int(rpc("eth_getBlockByNumber", [hex(head), False])["timestamp"], 16)
    out = []
    for d in range(days + 1):
        ts = hts - d * 86400
        b = head - int((hts - ts) / 12)
        for _ in range(3):  # refine on 12s slots
            t = int(rpc("eth_getBlockByNumber", [hex(b), False])["timestamp"], 16)
            b += int((ts - t) / 12)
        bal = rpc("eth_getBalance", [L1_BRIDGE, hex(b)])
        out.append({"time": datetime.datetime.utcfromtimestamp(ts).strftime("%Y-%m-%d %H:%M"), "block": b, "eth": int(bal, 16) / 1e18 if bal else None})
    out.reverse()
    json.dump(out, open(os.path.join(M, "rh_l1_bridge_eth.json"), "w"), indent=1)
    return out


def summarize(bridge):
    tvl = {day(x["date"]): x["tvl"] for x in json.load(open(os.path.join(RM, "llama_tvl_hist.json")))}
    st = {day(x["date"]): x["totalCirculatingUSD"].get("peggedUSD", 0) for x in json.load(open(os.path.join(RM, "llama_stables_hist.json")))}
    dex = {day(t): v for t, v in json.load(open(os.path.join(RM, "llama_dex.json"))).get("totalDataChart", [])}
    fees = {day(t): v for t, v in json.load(open(os.path.join(RM, "llama_fees.json"))).get("totalDataChart", [])}
    eth = {x["time"][:10]: x["eth"] for x in bridge if x["eth"] is not None}
    btc = {datetime.datetime.utcfromtimestamp(t / 1000).strftime("%Y-%m-%d"): p for t, p in json.load(open(os.path.join(RM, "cg_btc_90d.json")))["prices"]}
    # weeks ending on the latest day with data
    last = max(dex)
    end = datetime.date.fromisoformat(last)
    rows = []
    for w in range(12, -1, -1):
        we = end - datetime.timedelta(days=7 * w)
        ws = we - datetime.timedelta(days=6)
        days = [(ws + datetime.timedelta(days=i)).isoformat() for i in range(7)]
        k = we.isoformat()
        rows.append([ws.isoformat(), k,
                     round(sum(dex.get(d, 0) for d in days) / 1e6, 1), round(sum(fees.get(d, 0) for d in days) / 1e6, 2),
                     round(tvl.get(k, 0) / 1e6, 1), round(st.get(k, 0) / 1e6, 1), round(eth.get(k) or 0), round(btc.get(k) or 0)])
    with open(os.path.join(M, "rh_chain_weekly.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["week_start", "week_end", "dex_volume_musd", "fees_musd", "tvl_end_musd", "stablecoins_end_musd", "l1_bridge_eth_end", "btc_usd_end"])
        w.writerows(rows)
    stab = []
    for s_ in json.load(open(os.path.join(RM, "llama_stables_all.json"))).get("peggedAssets", []):
        cc = s_.get("chainCirculating", {}).get("Robinhood Chain")
        if cc:
            stab.append({"symbol": s_["symbol"], "now": cc.get("current", {}).get("peggedUSD", 0),
                         "prev_week": cc.get("circulatingPrevWeek", {}).get("peggedUSD", 0), "prev_month": cc.get("circulatingPrevMonth", {}).get("peggedUSD", 0)})
    stab.sort(key=lambda x: -x["now"])
    dx = json.load(open(os.path.join(RM, "llama_dex.json")))
    fe = json.load(open(os.path.join(RM, "llama_fees.json")))
    peak_day = max(dex, key=dex.get)
    summary = {
        "asof": last,
        "tvl": tvl[max(tvl)], "stablecoins": st[max(st)], "stablecoin_breakdown": stab[:6],
        "dex_24h": dx.get("total24h"), "dex_7d": dx.get("total7d"), "dex_30d": dx.get("total30d"), "dex_change_7d_pct": dx.get("change_7d"),
        "dex_peak_day": peak_day, "dex_peak_usd": dex[peak_day],
        "fees_24h": fe.get("total24h"), "fees_7d": fe.get("total7d"), "fees_change_7d_pct": fe.get("change_7d"),
        "top_dexs_24h": [(p.get("name"), p.get("total24h")) for p in sorted(dx.get("protocols", []), key=lambda p: -(p.get("total24h") or 0))[:8]],
        "l1_bridge_eth_now": bridge[-1]["eth"], "l1_bridge_eth_peak": max(x["eth"] or 0 for x in bridge),
        "l1_bridge_eth_peak_day": max(bridge, key=lambda x: x["eth"] or 0)["time"][:10],
    }
    json.dump(summary, open(os.path.join(M, "rh_chain_summary.json"), "w"), indent=1)
    json.dump(stab, open(os.path.join(M, "rh_stables_breakdown.json"), "w"), indent=1)
    json.dump(market_snapshot(), open(os.path.join(M, "market_snapshot.json"), "w"), indent=1)
    return summary, rows


def market_snapshot():
    """Macro + Robinhood-ecosystem context: BTC/ETH trend, Fear & Greed, ecosystem tokens, stock tokens, meme coins."""
    out = {}
    for sym, fn in (("BTC", "cg_btc_90d.json"), ("ETH", "cg_eth_90d.json")):
        p = [x[1] for x in json.load(open(os.path.join(RM, fn)))["prices"]]
        out[sym] = {"price": p[-1], "chg_7d_pct": (p[-1] / p[-8] - 1) * 100, "chg_30d_pct": (p[-1] / p[-31] - 1) * 100,
                    "chg_90d_pct": (p[-1] / p[0] - 1) * 100, "high_90d": max(p), "low_90d": min(p)}
    f = [int(x["value"]) for x in json.load(open(os.path.join(RM, "fng.json")))["data"]]
    out["fear_greed"] = {"now": f[0], "avg_7d": sum(f[:7]) / 7, "avg_30d": sum(f[:30]) / 30}
    g = json.load(open(os.path.join(RM, "cg_global.json"))).get("data", {})
    out["global"] = {"mcap_usd": g.get("total_market_cap", {}).get("usd"), "mcap_chg_24h_pct": g.get("market_cap_change_percentage_24h_usd"),
                     "btc_dominance": g.get("market_cap_percentage", {}).get("btc")}
    eco = json.load(open(os.path.join(RM, "cg_rh_eco.json")))
    native = ("pons", "ai", "cashcat", "npc", "lit", "net")
    out["rh_ecosystem_tokens"] = [{"symbol": x["symbol"], "price": x["current_price"], "mcap": x.get("market_cap"),
                                   "chg_7d_pct": x.get("price_change_percentage_7d_in_currency"), "chg_30d_pct": x.get("price_change_percentage_30d_in_currency")}
                                  for x in eco if x["symbol"] in native]
    st = json.load(open(os.path.join(RM, "hs_stocks.json")))
    out["stock_tokens"] = {**st.get("stats", {}), "top_volume": [(x["symbol"], x.get("volume24")) for x in sorted(st.get("stocks", []), key=lambda x: -(x.get("volume24") or 0))[:8]]}
    mm = json.load(open(os.path.join(RM, "hs_memes.json")))
    # SUSD pairs carry wash volume (hundreds of $M from ~100 trades a day) and cbBTC pairs are not memes: keep both out
    wash = lambda c: "SUSD" in ((c.get("anchorSymbol") or "").upper(), (c.get("symbol") or "").upper())
    coins = [c for c in mm.get("coins", []) if (c.get("anchorSymbol") or "") != "cbBTC" and not wash(c)]
    washed = [c for c in mm.get("coins", []) if wash(c)]
    ch = [c["change24"] for c in coins if c.get("change24") is not None and (c.get("vol24") or 0) > 50000]
    out["meme_coins"] = {"tracked": len(coins), "vol24": sum(c.get("vol24") or 0 for c in coins), "liquidity": sum(c.get("liquidity") or 0 for c in coins),
                         "net_flow_24h": sum((c.get("flow") or {}).get("net24h") or 0 for c in coins),
                         "median_change_24h_pct": statistics.median(ch) if ch else None,
                         "share_up_24h_pct": round(sum(1 for x in ch if x > 0) / len(ch) * 100, 1) if ch else None,
                         "new_launches_24h": len(mm.get("launches") or []),
                         "excluded_wash": {"coins": len(washed), "vol24": sum(c.get("vol24") or 0 for c in washed),
                                           "trades24h": sum((c.get("flow") or {}).get("trades24h") or 0 for c in washed)}}
    return out


if __name__ == "__main__":
    cached = "--cached" in sys.argv
    if not cached:
        fetch()
    bfn = os.path.join(M, "rh_l1_bridge_eth.json")
    bridge = json.load(open(bfn)) if cached and os.path.exists(bfn) and isinstance(json.load(open(bfn))[0], dict) else l1_bridge_eth()
    summary, rows = summarize(bridge)
    for r in rows:
        print(r)
    print(json.dumps({k: v for k, v in summary.items() if k not in ("stablecoin_breakdown", "top_dexs_24h")}, indent=1))
    print(json.dumps(json.load(open(os.path.join(M, "market_snapshot.json"))), indent=1)[:2500])
