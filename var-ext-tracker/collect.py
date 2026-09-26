#!/usr/bin/env python3
"""Collect VAR (Variational) and EXT (Extended) pre-TGE metrics for the tracker dashboard.

Usage:
  python3 collect.py latest  OUT_DIR [SERIES_JSON]  # writes latest.json (state/latest) and row.json ({"rows": {date: row}})
  python3 collect.py history OUT_DIR   # writes series.json ({"rows": {...}}) rebuilt from public APIs (~185 days)

Sources: Variational omni API, Extended API, DefiLlama (OI, TVL, fees, prices),
CoinGecko (exchange volume, token markets), Polymarket gamma + CLOB, alternative.me (Fear & Greed).
Only public, unauthenticated endpoints are used.
"""
import datetime as dt
import json
import os
import statistics as st
import subprocess
import sys
import time

UTC = dt.timezone.utc

# D+1 calibration multiples (FDV 24h after listing / 30d-average metric before TGE),
# from LIT, EDGE, GRVT, BP. See README for derivation.
CALIB = {
    "oi": {"LIT": 3.2427, "EDGE": 0.6087, "GRVT": 0.7361},
    "tvl": {"LIT": 1.9737, "EDGE": 3.6504, "GRVT": 6.6983, "BP": 0.5811},
    "vol30": {"LIT": 0.0142, "EDGE": 0.0086, "GRVT": 0.0074, "BP": 0.0115},
    "fees": {"LIT": 19.6121, "EDGE": 2.5445},
}
PEERS = [  # symbol, coingecko id, supply used for FDV, TGE date, FDV 24h after listing (USD)
    ("HYPE", "hyperliquid", None, "2024-11-29", None),
    ("ASTER", "aster-2", 8e9, "2025-09-17", 4.325e9),
    ("LIT", "lighter", 1e9, "2025-12-30", 2.714e9),
    ("BP", "backpack", 1e9, "2026-03-23", 0.199e9),
    ("EDGE", "edgex", 1e9, "2026-03-31", 0.665e9),
    ("GRVT", "grvt", 1e9, "2026-07-30", 0.262e9),
]
PM = {
    "var_fdv": 103469, "ext_fdv": 91926,
    "var_launch": 73902, "ext_launch": 84920,
    "ext_listing": 881165,
    "fed_oct": 606422, "fed_dec": 770450,
}
VAR_API = "https://omni-client-api.prod.ap-northeast-1.variational.io/metadata/stats"
EXT_API = "https://api.starknet.extended.exchange/api/v1/info/markets"


def get(url, tries=4, wait=20, expect=None):
    last = None
    for i in range(tries):
        r = subprocess.run(["curl", "-s", "-m", "60", "-A", "var-ext-tracker", url],
                           capture_output=True, text=True).stdout
        try:
            d = json.loads(r)
            status = d.get("status") if isinstance(d, dict) else None
            if isinstance(status, dict) and status.get("error_code") == 429:
                raise ValueError("rate limited")
            if r.strip() == "Throttled":
                raise ValueError("throttled")
            if expect is not None and not isinstance(d, expect):
                raise ValueError(f"unexpected payload: {str(d)[:120]}")
            return d
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(wait * (i + 1))
    raise RuntimeError(f"fetch failed {url}: {last}")


def day(ts):
    return dt.datetime.fromtimestamp(ts, UTC).date()


def ds(d):
    return d.isoformat()


# ---------- helpers ----------
def btc_prices(days):
    start = int(time.time()) - (days + 2) * 86400
    d = get(f"https://coins.llama.fi/chart/coingecko:bitcoin?start={start}&span={min(days + 3, 499)}&period=1d")
    return {day(p["timestamp"]): p["price"] for p in d["coins"]["coingecko:bitcoin"]["prices"]}


def near(series, d, back=7):
    for i in range(back):
        k = d - dt.timedelta(days=i)
        if k in series:
            return series[k]
    return None


def cg_volume(exchange_id, days, btc, tries=6, wait=30):
    cache = os.environ.get("VOL_CACHE_DIR")
    if cache and os.path.exists(os.path.join(cache, f"vc365_{exchange_id}.json")):
        d = json.load(open(os.path.join(cache, f"vc365_{exchange_id}.json")))
        out = {}
        for t, v in d:
            k = day(t / 1000)
            p = near(btc, k)
            if p:
                out[k] = float(v) * p
        return out
    try:
        d = get(f"https://api.coingecko.com/api/v3/exchanges/{exchange_id}/volume_chart?days={days}", wait=wait, tries=tries, expect=list)
    except RuntimeError:
        return {}
    out = {}
    for t, v in d:
        k = day(t / 1000)
        p = near(btc, k)
        if p:
            out[k] = float(v) * p
    return out


def llama_series(kind, slug, data_type=None):
    url = f"https://api.llama.fi/summary/{kind}/{slug}"
    if data_type:
        url += f"?dataType={data_type}"
    d = get(url)
    return {day(t): v for t, v in (d.get("totalDataChart") or [])}


def llama_tvl(slug):
    d = get(f"https://api.llama.fi/protocol/{slug}")
    return {day(x["date"]): x["totalLiquidityUSD"] for x in d.get("tvl", [])}


def last(series, d, back=5):
    """Most recent value on or before d (DefiLlama's current day often lags)."""
    for i in range(back):
        k = d - dt.timedelta(days=i)
        if series.get(k) is not None:
            return series[k]
    return None


def trailing(series, d, n=30, how="avg"):
    v = [series[k] for k in series if 0 <= (d - k).days < n]
    if not v:
        return None
    return sum(v) / len(v) if how == "avg" else sum(v) * n / len(v)


def interp_median(points, target=0.5):
    """points: [(threshold_usd, P(FDV>threshold))]; linear interpolation of the survival curve."""
    pts = sorted((x, p) for x, p in points if p is not None)
    # enforce monotone non-increasing survival
    mono, lo = [], 1.0
    for x, p in pts:
        lo = min(lo, p)
        mono.append((x, lo))
    for (x1, p1), (x2, p2) in zip(mono, mono[1:]):
        if p1 >= target >= p2 and p1 != p2:
            return x1 + (p1 - target) / (p1 - p2) * (x2 - x1)
    return None


def parse_usd(label):
    s = label.replace("$", "").replace(">", "").replace(",", "").strip().upper()
    num = float("".join(ch for ch in s if ch.isdigit() or ch == "."))
    return num * (1e9 if "B" in s else 1e6 if "M" in s else 1)


def pm_event(eid):
    return get(f"https://gamma-api.polymarket.com/events/{eid}")


def pm_markets(eid, include_closed=True):
    e = pm_event(eid)
    out = []
    for m in e.get("markets", []):
        if not include_closed and m.get("closed"):
            continue
        try:
            yes = float(json.loads(m.get("outcomePrices") or "[]")[0])
        except Exception:  # noqa: BLE001
            yes = None
        tok = json.loads(m.get("clobTokenIds") or "[]")
        out.append(dict(label=(m.get("groupItemTitle") or m.get("question") or "").strip(),
                        yes=yes, token=tok[0] if tok else None, closed=bool(m.get("closed"))))
    return e, out


def pm_history(token):
    h = get(f"https://clob.polymarket.com/prices-history?market={token}&interval=max&fidelity=1440").get("history", [])
    return {day(p["t"]): p["p"] for p in h}


def model_fdv(metrics):
    """metrics: dict method->value. Returns per-method (low, median, high) and median of medians."""
    per = {}
    for k, v in metrics.items():
        if not v:
            continue
        mult = list(CALIB[k].values())
        per[k] = dict(low=min(mult) * v, mid=st.median(mult) * v, high=max(mult) * v, value=v)
    mids = [x["mid"] for x in per.values()]
    return dict(methods=per, median=st.median(mids) if mids else None)


# ---------- latest ----------
def collect_latest(series_path=None):
    now = dt.datetime.now(UTC)
    today = now.date()
    btc = btc_prices(40)

    # Variational
    v = get(VAR_API)
    L = v["listings"]
    tv = sum(float(x["volume_24h"]) for x in L) or 1
    tradfi = sum(float(x["volume_24h"]) for x in L if float(x["funding_rate"]) == 0)
    spread = 0.0
    for x in L:
        q = (x.get("quotes") or {}).get("base") or {}
        if not q.get("bid") or not q.get("ask"):
            continue
        b, a = float(q["bid"]), float(q["ask"])
        m = (a + b) / 2
        if m > 0:
            spread += float(x["volume_24h"]) * (a - b) / m * 1e4
    top = sorted(L, key=lambda x: -float(x["volume_24h"]))[:6]
    var_oi_s = llama_series("open-interest", "variational")
    stored = {}
    if series_path and os.path.exists(series_path):
        stored = (json.load(open(series_path)).get("rows") or {})

    def from_stored(key):
        return {dt.date.fromisoformat(k): r[key] for k, r in stored.items() if r.get(key)}

    var_vol_s = cg_volume("variational-omni", 60, btc, tries=2, wait=8) or from_stored("v_vol")
    var = dict(
        vol24=float(v["total_volume_24h"]), cumVol=float(v["cumulative_volume"]), tvl=float(v["tvl"]),
        oiApi=float(v["open_interest"]), markets=int(v["num_markets"]),
        oi=last(var_oi_s, today) or (float(v["open_interest"]) / 2),
        oi30=trailing(var_oi_s, today), vol30=trailing(var_vol_s, today, 30, "sum"),
        vol30prev=trailing({k: val for k, val in var_vol_s.items() if (today - k).days >= 30}, today - dt.timedelta(days=30), 30, "sum"),
        tradfiShare=tradfi / tv, spreadBps=spread / tv,
        top=[dict(t=x["ticker"], v=float(x["volume_24h"])) for x in top],
    )
    var["model"] = model_fdv({"oi": var["oi30"], "tvl": var["tvl"], "vol30": var["vol30"]})

    # Extended
    e = get(EXT_API)["data"]
    evol = sum(float(x["marketStats"].get("dailyVolume") or 0) for x in e) or 1
    rwa = sum(float(x["marketStats"].get("dailyVolume") or 0) for x in e if x.get("category") == "RWA")
    ext_oi_s = llama_series("open-interest", "extended-perps")
    ext_fee_s = llama_series("fees", "extended-perps")
    ext_tvl_s = llama_tvl("extended-perps")
    ext_vol_s = cg_volume("extended", 60, btc, tries=2, wait=8) or from_stored("e_vol")
    ext = dict(
        vol24=evol, oiApi=sum(float(x["marketStats"].get("openInterest") or 0) for x in e),
        markets=sum(1 for x in e if x.get("active")), rwaShare=rwa / evol,
        oi=last(ext_oi_s, today), oi30=trailing(ext_oi_s, today),
        tvl=last(ext_tvl_s, today), vol30=trailing(ext_vol_s, today, 30, "sum"),
        vol30prev=trailing({k: val for k, val in ext_vol_s.items() if (today - k).days >= 30}, today - dt.timedelta(days=30), 30, "sum"),
        fees30=trailing(ext_fee_s, today, 30, "sum"),
    )
    ext["feesAnn"] = ext["fees30"] * 365 / 30 if ext["fees30"] else None
    ext["model"] = model_fdv({"oi": ext["oi30"], "tvl": ext["tvl"], "vol30": ext["vol30"], "fees": ext["feesAnn"]})

    # Polymarket
    def fdv_block(eid):
        ev, ms = pm_markets(eid, include_closed=False)
        pts = [(parse_usd(m["label"]), m["yes"]) for m in ms if m["yes"] is not None]
        pts.sort()
        return dict(points=pts, median=interp_median(pts), p25=interp_median(pts, 0.75), p75=interp_median(pts, 0.25),
                    volume=float(ev.get("volume") or 0))

    def launch_block(eid):
        _, ms = pm_markets(eid)
        return [dict(label=m["label"], p=m["yes"], closed=m["closed"]) for m in ms]

    var["pm"] = fdv_block(PM["var_fdv"])
    ext["pm"] = fdv_block(PM["ext_fdv"])
    var["launch"] = launch_block(PM["var_launch"])
    ext["launch"] = launch_block(PM["ext_launch"])
    ext["listing"] = [dict(label=m["label"], p=m["yes"]) for m in pm_markets(PM["ext_listing"], False)[1]]
    fed = {}
    for k in ("fed_oct", "fed_dec"):
        _, ms = pm_markets(PM[k], False)
        fed[k] = {m["label"]: m["yes"] for m in ms}

    # Market
    fng = get("https://api.alternative.me/fng/?limit=31&format=json")["data"]
    btc_now = near(btc, today)
    btc_30 = near(btc, today - dt.timedelta(days=30))
    peers = []
    ids = ",".join("coingecko:" + p[1] for p in PEERS)
    cur = get(f"https://coins.llama.fi/prices/current/{ids}")["coins"]
    pct = get(f"https://coins.llama.fi/percentage/{ids}?period=30d").get("coins", {})
    for sym, cid, sup, tge, d1 in PEERS:
        price = (cur.get("coingecko:" + cid) or {}).get("price")
        supply = sup or 1e9
        peers.append(dict(sym=sym, tge=tge, d1=d1, price=price, fdv=price * supply if price else None,
                          ch30=pct.get("coingecko:" + cid)))
    hype = (cur.get("coingecko:hyperliquid") or {}).get("price")

    latest = dict(
        updatedAt=now.isoformat(timespec="minutes"), date=ds(today),
        var=var, ext=ext, calib=CALIB,
        mkt=dict(btc=btc_now, btc30=(btc_now / btc_30 - 1) if btc_now and btc_30 else None,
                 fng=int(fng[0]["value"]), fngLabel=fng[0]["value_classification"],
                 fng30=sum(int(x["value"]) for x in fng[:30]) / min(30, len(fng)),
                 hype=hype, fed=fed),
        peers=peers,
    )
    row = {ds(today): dict(
        v_vol=var_vol_s.get(today - dt.timedelta(days=1)) or var["vol24"], v_oi=var["oi"], v_tvl=var["tvl"],
        v_pm=var["pm"]["median"], v_p1b=dict(var["pm"]["points"]).get(1e9),
        v_model=var["model"]["median"],
        e_vol=ext_vol_s.get(today - dt.timedelta(days=1)) or ext["vol24"], e_oi=ext["oi"], e_tvl=ext["tvl"],
        e_fee=last(ext_fee_s, today), e_pm=ext["pm"]["median"], e_p300=dict(ext["pm"]["points"]).get(3e8),
        e_model=ext["model"]["median"],
        btc=btc_now, fng=int(fng[0]["value"]), hype=hype,
    )}
    return latest, row


# ---------- history ----------
def collect_history(days=185):
    today = dt.datetime.now(UTC).date()
    start = today - dt.timedelta(days=days)
    btc = btc_prices(days + 40)
    var_vol = cg_volume("variational-omni", days + 40, btc)
    time.sleep(15)
    ext_vol = cg_volume("extended", days + 40, btc)
    var_oi = llama_series("open-interest", "variational")
    ext_oi = llama_series("open-interest", "extended-perps")
    ext_fee = llama_series("fees", "extended-perps")
    ext_tvl = llama_tvl("extended-perps")
    fng = {day(int(x["timestamp"])): int(x["value"]) for x in get(f"https://api.alternative.me/fng/?limit={days + 5}&format=json")["data"]}
    hs = int(time.time()) - (days + 2) * 86400
    hype = {day(p["timestamp"]): p["price"] for p in get(
        f"https://coins.llama.fi/chart/coingecko:hyperliquid?start={hs}&span={days + 3}&period=1d")["coins"]["coingecko:hyperliquid"]["prices"]}

    def pm_hist(eid):
        _, ms = pm_markets(eid)
        hist = {}
        for m in ms:
            if not m["token"]:
                continue
            try:
                hist[parse_usd(m["label"])] = pm_history(m["token"])
            except Exception:  # noqa: BLE001
                continue
        return hist

    var_pm = pm_hist(PM["var_fdv"])
    ext_pm = pm_hist(PM["ext_fdv"])

    rows = {}
    d = start
    while d < today:
        def pmv(h, thr=None):
            pts = [(x, near(s, d, 3)) for x, s in h.items()]
            if thr is not None:
                return dict(pts).get(thr)
            return interp_median([p for p in pts if p[1] is not None])
        v30 = trailing(var_vol, d, 30, "sum")
        e30 = trailing(ext_vol, d, 30, "sum")
        efa = trailing(ext_fee, d, 30, "sum")
        rows[ds(d)] = dict(
            v_vol=var_vol.get(d), v_oi=var_oi.get(d), v_pm=pmv(var_pm), v_p1b=pmv(var_pm, 1e9),
            v_model=model_fdv({"oi": trailing(var_oi, d), "vol30": v30})["median"],
            e_vol=ext_vol.get(d), e_oi=ext_oi.get(d), e_tvl=ext_tvl.get(d), e_fee=ext_fee.get(d),
            e_pm=pmv(ext_pm), e_p300=pmv(ext_pm, 3e8),
            e_model=model_fdv({"oi": trailing(ext_oi, d), "tvl": ext_tvl.get(d), "vol30": e30,
                               "fees": efa * 365 / 30 if efa else None})["median"],
            btc=near(btc, d), fng=fng.get(d), hype=near(hype, d),
        )
        rows[ds(d)] = {k: (round(v, 6) if isinstance(v, float) else v) for k, v in rows[ds(d)].items() if v is not None}
        d += dt.timedelta(days=1)
    return {"rows": rows}


def main():
    mode, out = sys.argv[1], sys.argv[2]
    os.makedirs(out, exist_ok=True)
    if mode == "latest":
        latest, row = collect_latest(sys.argv[3] if len(sys.argv) > 3 else None)
        json.dump(latest, open(os.path.join(out, "latest.json"), "w"))
        json.dump({"rows": row}, open(os.path.join(out, "row.json"), "w"))
        print(json.dumps({"date": latest["date"], "var_vol24": latest["var"]["vol24"], "var_pm": latest["var"]["pm"]["median"],
                          "var_model": latest["var"]["model"]["median"], "ext_pm": latest["ext"]["pm"]["median"],
                          "ext_model": latest["ext"]["model"]["median"]}, indent=1))
    elif mode == "history":
        s = collect_history(int(sys.argv[3]) if len(sys.argv) > 3 else 185)
        json.dump(s, open(os.path.join(out, "series.json"), "w"))
        print("rows", len(s["rows"]), "bytes", len(json.dumps(s)))
    else:
        raise SystemExit(__doc__)


if __name__ == "__main__":
    main()
