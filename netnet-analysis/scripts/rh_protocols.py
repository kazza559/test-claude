"""Where Robinhood Chain capital sits and where activity runs (DefiLlama):

* TVL by protocol on Robinhood Chain, with 1d / 7d / 30d change from each protocol's chain-specific history
* DEX volume by protocol, weekly
* fees by category (DEX, launchpad, trading app, perps, lending...), weekly

Writes data/market/rh_protocols.csv, rh_dex_by_protocol_weekly.csv, rh_fees_by_category_weekly.csv.
"""
import collections, csv, datetime, json, os, time
import requests
from paths import DATA, RAW

M = os.path.join(DATA, "market")
RM = os.path.join(RAW, "market")
CH = "Robinhood Chain"
S = requests.Session()


def get(url, tries=4):
    for i in range(tries):
        try:
            r = S.get(url, timeout=90)
            if r.status_code == 200:
                return r.json()
        except Exception:  # noqa: BLE001
            pass
        time.sleep(5 * (i + 1))
    return None


def day(ts):
    return datetime.datetime.utcfromtimestamp(int(ts)).strftime("%Y-%m-%d")


def weekly(daily, end):
    """Sum a {date: value} map into 7-day buckets ending on `end` (newest last)."""
    out = []
    for w in range(12, -1, -1):
        we = end - datetime.timedelta(days=7 * w)
        days = [(we - datetime.timedelta(days=i)).isoformat() for i in range(7)]
        out.append((we.isoformat(), sum(daily.get(d, 0) for d in days)))
    return out


def protocols():
    allp = get("https://api.llama.fi/protocols") or []
    on = [p for p in allp if CH in (p.get("chainTvls") or {})]
    on.sort(key=lambda p: -(p["chainTvls"].get(CH) or 0))
    rows = []
    for p in on[:20]:
        tvl = p["chainTvls"].get(CH) or 0
        hist = get(f"https://api.llama.fi/protocol/{p['slug']}")
        ser = {}
        if hist:
            for pt in ((hist.get("chainTvls") or {}).get(CH) or {}).get("tvl", []):
                ser[day(pt["date"])] = pt.get("totalLiquidityUSD") or 0
        ks = sorted(ser)

        def chg(n):
            if len(ks) <= n or not ser.get(ks[-1 - n]):
                return None
            return (ser[ks[-1]] / ser[ks[-1 - n]] - 1) * 100
        rows.append({"name": p["name"], "category": p.get("category"), "tvl": round(tvl), "chg_1d": chg(1), "chg_7d": chg(7), "chg_30d": chg(30),
                     "share_of_chain": None, "first_day": ks[0] if ks else None})
        print(rows[-1], flush=True)
    tot = sum(r["tvl"] for r in rows) or 1
    for r in rows:
        r["share_of_chain"] = round(r["tvl"] / tot * 100, 1)
    json.dump(on[:40], open(os.path.join(RM, "llama_protocols_rh.json"), "w"))
    return rows


def breakdown(kind):
    url = f"https://api.llama.fi/overview/{kind}/Robinhood%20Chain?excludeTotalDataChart=false&excludeTotalDataChartBreakdown=false"
    d = get(url) or {}
    json.dump(d, open(os.path.join(RM, f"llama_{kind}_breakdown.json"), "w"))
    cat = {p.get("name") or p.get("displayName"): p.get("category") for p in d.get("protocols", [])}
    per = collections.defaultdict(dict)
    for t, b in d.get("totalDataChartBreakdown", []):
        for name, v in b.items():
            per[name][day(t)] = (per[name].get(day(t), 0) or 0) + (v or 0)
    return per, cat


def write(fn, rows):
    if not rows:
        return
    with open(os.path.join(M, fn), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


if __name__ == "__main__":
    write("rh_protocols.csv", protocols())
    end = datetime.datetime.now(datetime.timezone.utc).date() - datetime.timedelta(days=1)
    dex, _ = breakdown("dexs")
    totals = {n: sum(v.values()) for n, v in dex.items()}
    top = [n for n, _ in sorted(totals.items(), key=lambda x: -x[1])[:8]]
    rows = []
    wk = {n: weekly(dex[n], end) for n in dex}
    for i, (we, _) in enumerate(wk[top[0]]):
        r = {"week_end": we}
        for n in top:
            r[n] = round(wk[n][i][1])
        r["Other"] = round(sum(wk[n][i][1] for n in dex if n not in top))
        rows.append(r)
    write("rh_dex_by_protocol_weekly.csv", rows)
    fees, cat = breakdown("fees")
    bycat = collections.defaultdict(dict)
    for n, ser in fees.items():
        c = cat.get(n) or "Other"
        for d, v in ser.items():
            bycat[c][d] = bycat[c].get(d, 0) + v
    cats = sorted(bycat, key=lambda c: -sum(bycat[c].values()))
    rows = []
    wk = {c: weekly(bycat[c], end) for c in cats}
    for i, (we, _) in enumerate(wk[cats[0]]):
        r = {"week_end": we}
        for c in cats[:7]:
            r[c] = round(wk[c][i][1])
        r["Other"] = round(sum(wk[c][i][1] for c in cats[7:]))
        rows.append(r)
    write("rh_fees_by_category_weekly.csv", rows)
    print("dex top:", top)
    print("fee categories:", cats[:8])
