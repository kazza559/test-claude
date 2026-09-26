#!/usr/bin/env python3
"""hedge-scan: pick the cheapest TradFi pair for a delta-neutral hedge between Variational (Omni) and Extended.

Usage:
  python3 scan.py                           # rank pairs at config size (default $15k/leg), hold 8h
  python3 scan.py --size 20000 --hold 24    # override size per leg / holding time (hours)
  python3 scan.py --only AAPL,TSLA,XAG      # restrict to these tickers (Variational symbols)
  python3 scan.py --all                     # also list pairs that are not tradable right now
  python3 scan.py --exit AAPL:short-var     # cost of closing an open hedge now (short-var = short on VAR, long on EXT)
  python3 scan.py --json                    # machine-readable output
  python3 scan.py --log spreads.csv         # append one row per pair (build your own time-of-day stats)

Public, unauthenticated endpoints only. Cost model and assumptions: README.md.
"""
import argparse
import concurrent.futures as cf
import csv
import datetime as dt
import json
import math
import os
import sys
import time
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
VAR_API = "https://omni-client-api.prod.ap-northeast-1.variational.io/metadata/stats"
EXT_API = "https://api.starknet.extended.exchange/api/v1"
UTC = dt.timezone.utc
ICT = dt.timezone(dt.timedelta(hours=7))
VAR_SIZES = (("size_1k", 1e3), ("size_100k", 1e5), ("size_1m", 1e6))
HARD = {"ext_inactive", "ext_closed", "ext_max_order", "ext_oi_cap", "var_stale", "ext_thin", "no_data"}
FLAG_TEXT = {
    "ext_inactive": "EXT không active", "ext_closed": "EXT đang đóng cửa", "ext_max_order": "vượt max lệnh market EXT",
    "ext_oi_cap": "EXT sát trần OI (reduce-only)", "var_stale": "quote VAR cũ", "ext_thin": "sổ lệnh EXT mỏng",
    "no_data": "thiếu dữ liệu", "var_illiquid": "VAR volume thấp", "vol_spike": "BIẾN ĐỘNG CAO",
    "proxy": "proxy (khác tài sản gốc)", "unverified_pts": "pts/$1M chưa xác minh",
}


def get(url, tries=3):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "hedge-scan/1.0", "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=20) as r:
                return json.loads(r.read())
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(1.5 * (i + 1))
    raise RuntimeError(f"fetch failed {url}: {last}")


def parse_ts(s):
    """ISO timestamp with 'Z' and any number of fractional digits (fromisoformat before 3.11 accepts only 3 or 6)."""
    head, _, frac = s.rstrip("Z").partition(".")
    return dt.datetime.fromisoformat(f"{head}.{(frac + '000000')[:6]}+00:00")


# ---------- market sessions ----------
def et_offset(t):
    """UTC offset (hours) of US Eastern time at UTC instant t (DST: 2nd Sun of Mar 07:00Z to 1st Sun of Nov 06:00Z)."""
    mar1, nov1 = dt.datetime(t.year, 3, 1, tzinfo=UTC), dt.datetime(t.year, 11, 1, tzinfo=UTC)
    start = mar1 + dt.timedelta(days=(6 - mar1.weekday()) % 7 + 7, hours=7)
    end = nov1 + dt.timedelta(days=(6 - nov1.weekday()) % 7, hours=6)
    return -4 if start <= t < end else -5


def sessions(now):
    off = et_offset(now)
    et = now + dt.timedelta(hours=off)
    wd, hm = et.weekday(), et.hour + et.minute / 60
    if wd == 5 or (wd == 6 and hm < 20) or (wd == 4 and hm >= 20):
        eq = "weekend"
    elif 9.5 <= hm < 16:
        eq = "rth"
    elif 4 <= hm < 9.5:
        eq = "pre"
    elif 16 <= hm < 20:
        eq = "post"
    else:
        eq = "overnight"
    if wd == 5 or (wd == 6 and hm < 18) or (wd == 4 and hm >= 17):
        cme = "weekend"
    elif 17 <= hm < 18:
        cme = "break"
    else:
        cme = "open"
    fx = "weekend" if wd == 5 or (wd == 6 and hm < 17) or (wd == 4 and hm >= 17) else "open"
    return dict(et_offset=off, equity=eq, cme=cme, fx=fx,
                near_bell=eq == "rth" and (hm < 9.75 or hm >= 15.75),
                rth_ict=((9.5 - off + 7) % 24, (16 - off + 7) % 24))


def session_of(ext_market):
    ref = ext_market.get("referenceMarket") or ""
    if ref in ("commodity_cme", "us_index_fut"):
        return "cme"
    if ref == "fx":
        return "fx"
    if ref == "always_open":
        return "always"
    return "equity" if ref == "us_equity" else "other"


# ---------- pricing ----------
def var_px(q, n, side, exp):
    """Estimated Variational fill price for notional n. side: 'ask' (buy) / 'bid' (sell).

    The public API quotes base, $1k, $100k (and $1M for majors). Between base and $1k we interpolate linearly;
    above $1k the extra cost grows as ((n - s0) / (s1 - s0)) ** exp (concave, exp from config)."""
    base = q["base"]
    mid = (float(base["bid"]) + float(base["ask"])) / 2
    sign = 1 if side == "ask" else -1
    pts = [(0.0, base)] + [(s, q[k]) for k, s in VAR_SIZES if q.get(k)]
    ex, hi = [], 0.0
    for s, p in pts:
        hi = max(hi, sign * (float(p[side]) - mid) / mid)
        ex.append((s, hi))
    e = ex[-1][1]
    for (s0, e0), (s1, e1) in zip(ex, ex[1:]):
        if n <= s1:
            f = (n - s0) / (s1 - s0)
            e = e0 + (e1 - e0) * (f if s0 == 0 else f ** exp)
            break
    else:
        if len(ex) >= 2:  # beyond the largest quoted size: extrapolate linearly
            (s0, e0), (s1, e1) = ex[-2], ex[-1]
            e = e1 + (e1 - e0) * (n - s1) / (s1 - s0)
    return mid * (1 + sign * e), mid


def walk(levels, n):
    """Average fill price for notional n through [(price, qty)] best-first; returns (avg_px, filled_fraction)."""
    got_n = got_q = 0.0
    for px, qty in levels:
        take = min(px * qty, n - got_n)
        got_n += take
        got_q += take / px
        if got_n >= n * (1 - 1e-9):
            break
    return (got_n / got_q if got_q else None), got_n / n


def vol_stats(candles, leg_delay_s):
    """Realized volatility from 5m mark-price candles (newest first from the API)."""
    closes = [float(c["c"]) for c in sorted(candles, key=lambda c: c["T"])]
    r = [math.log(b / a) for a, b in zip(closes, closes[1:]) if a > 0 and b > 0]
    if len(r) < 12:
        return None
    rms = lambda xs: math.sqrt(sum(x * x for x in xs) / len(xs)) * 1e4  # noqa: E731
    now, day = rms(r[-6:]), rms(r)
    return dict(sigma5m=now, sigma5m_day=day, ratio=now / day if day > 1e-6 else None,
                leg_risk=0.8 * now * math.sqrt(leg_delay_s / 300))


# ---------- data ----------
def load(cfg):
    var = {x["ticker"]: x for x in get(VAR_API)["listings"]}
    ext = [m for m in get(f"{EXT_API}/info/markets")["data"] if m.get("category") == "RWA"]
    pairs = []
    for m in ext:
        if m.get("status") in ("DELISTED", "PRELISTED"):
            continue
        base = m["name"].replace("-USD", "").replace("_24_5", "")
        proxy = base in cfg["proxies"]
        v = var.get(cfg["proxies"].get(base) or cfg["aliases"].get(base) or base)
        if not v or not (v.get("quotes") or {}).get("base"):
            continue
        ratio = float(m["marketStats"]["markPrice"] or 0) / float(v["mark_price"])
        if not proxy and abs(ratio - 1) > cfg["max_price_diff"]:
            continue  # same ticker, different asset (e.g. ON, QNT)
        pairs.append(dict(v=v, e=m, proxy=proxy))
    return pairs


def fetch_ext(pair):
    name = pair["e"]["name"]
    pair["bids"] = pair["asks"] = pair["candles"] = pair["funding_hist"] = []
    if pair.get("skip"):
        return pair
    try:
        ob = get(f"{EXT_API}/info/markets/{name}/orderbook")["data"]
        pair["bids"] = [(float(x["price"]), float(x["qty"])) for x in ob.get("bid", [])]
        pair["asks"] = [(float(x["price"]), float(x["qty"])) for x in ob.get("ask", [])]
    except RuntimeError:
        pair["bids"] = pair["asks"] = []
    try:
        pair["candles"] = get(f"{EXT_API}/info/candles/{name}/mark-prices?interval=PT5M&limit=288")["data"]
    except RuntimeError:
        pair["candles"] = []
    end = int(time.time() * 1000)
    try:
        h = get(f"{EXT_API}/info/{name}/funding?startTime={end - 8 * 3600 * 1000}&endTime={end}")["data"]
        pair["funding_hist"] = [float(x["f"]) for x in h]
    except (RuntimeError, KeyError, TypeError, ValueError):
        pair["funding_hist"] = []
    return pair


# ---------- model ----------
def evaluate(p, n, hold, cfg, now):
    v, e = p["v"], p["e"]
    ms, tc = e["marketStats"], e["tradingConfig"]
    flags = set()
    if p["proxy"]:
        flags.add("proxy")
    if not e.get("active") or e.get("status") != "ACTIVE":
        flags.add("ext_inactive")
    if e.get("isOffHours"):
        flags.add("ext_closed")
    if n > float(tc.get("maxMarketOrderValue") or 1e18):
        flags.add("ext_max_order")
    oi_lim = float(tc.get("openInterestLimit") or 0)
    if e.get("isRfq") and oi_lim and float(ms.get("openInterest") or 0) >= 0.95 * oi_lim:
        flags.add("ext_oi_cap")
    q = v["quotes"]
    age = (now - parse_ts(q["updated_at"])).total_seconds()
    if age > cfg["max_quote_age_s"]:
        flags.add("var_stale")
    if float(v["volume_24h"]) < cfg["min_var_volume_24h"]:
        flags.add("var_illiquid")
    if not p["bids"] or not p["asks"]:
        if not flags & HARD:  # books are not fetched for markets already known to be untradable
            flags.add("no_data")
        return dict(pair=p, flags=flags, n=n)

    exp, fee = cfg["var_size_curve_exp"], cfg["ext_taker_fee"] * 1e4
    v_ask, v_mid = var_px(q, n, "ask", exp)
    v_bid, _ = var_px(q, n, "bid", exp)
    e_ask, fa = walk(p["asks"], n)
    e_bid, fb = walk(p["bids"], n)
    if e_ask is None or e_bid is None:
        flags.add("no_data")
        return dict(pair=p, flags=flags, n=n)
    if min(fa, fb) < 1:
        flags.add("ext_thin")
    e_mid = (p["bids"][0][0] + p["asks"][0][0]) / 2
    k = e_mid / v_mid if p["proxy"] else 1.0  # proxies: compare on a normalized price, basis is meaningless
    e_ask, e_bid, e_mid = e_ask / k, e_bid / k, e_mid / k
    mid = (v_mid + e_mid) / 2
    var_rt = (v_ask - v_bid) / v_mid * 1e4
    ext_rt = (e_ask - e_bid) / e_mid * 1e4
    rt = var_rt + ext_rt + 2 * fee
    basis = (v_mid - e_mid) / mid * 1e4
    entry = {"long-var": (v_ask - e_bid) / mid * 1e4 + fee, "short-var": (e_ask - v_bid) / mid * 1e4 + fee}

    fv_h = float(v.get("funding_rate") or 0) / 8760  # VAR API: annualized decimal, >0 longs pay
    fe_now = float(ms.get("fundingRate") or 0)  # EXT: hourly decimal, >0 longs pay
    hist = p.get("funding_hist") or []
    fe_h = sum(hist) / len(hist) if hist else fe_now  # forecast = mean of the last 8 hourly payments
    fund_h = {"long-var": (fe_h - fv_h) * 1e4, "short-var": (fv_h - fe_h) * 1e4}  # bps/hour earned
    if abs(fund_h["long-var"]) * hold * 2 >= 0.25:
        side = max(fund_h, key=fund_h.get)
        why = "funding"
    else:
        side = min(entry, key=entry.get)
        why = "basis" if abs(basis) >= 0.3 else "spread"
    fund = fund_h[side] * hold
    cost_bps = rt - fund
    cost = n * cost_bps / 1e4
    ppm = cfg["var_points_per_m"].get(v["ticker"])
    if ppm is None:
        ppm = cfg["var_points_default"]
        flags.add("unverified_pts")
    pts = 2 * n / 1e6 * (ppm * (1 + cfg["points_boost"]) + cfg["ext_points_per_m"])
    vs = vol_stats(p["candles"], cfg["leg_delay_s"]) if p["candles"] else None
    if vs and vs["ratio"] and vs["ratio"] >= cfg["vol_spike_ratio"] and vs["sigma5m"] >= 3:
        flags.add("vol_spike")
    maker = None
    if not e.get("isRfq"):  # order-book market: EXT leg can rest as maker (0 fee), then hit VAR when filled
        maker = var_rt + 2 * cfg["ext_maker_fee"] * 1e4 - fund
    clips = {c: (var_px(q, c, "ask", exp)[0] - var_px(q, c, "bid", exp)[0]) / v_mid * 1e4 for c in (1e3, 5e3, 1e4, 2e4)}
    return dict(pair=p, flags=flags, n=n, side=side, why=why, var_rt=var_rt, ext_rt=ext_rt, fee=2 * fee, fund=fund,
                cost_bps=cost_bps, cost=cost, pts=pts, cpp=cost / pts if pts else None, basis=basis, entry=entry,
                fv_apr=fv_h * 8760 * 100, fe_h=fe_h * 100, fe_now=fe_now * 100, vol=vs, maker=maker, clips=clips, age=age,
                session=session_of(e), ppm=ppm)


def rank_key(r):
    return (bool(r["flags"] & HARD), "vol_spike" in r["flags"], r.get("cpp") if r.get("cpp") is not None else 1e9)


# ---------- output ----------
def label(r):
    return f"{r['pair']['v']['ticker']}/{r['pair']['e']['name'].replace('-USD', '')}"


def side_txt(side, short=False):
    if short:
        return "L.VAR S.EXT" if side == "long-var" else "S.VAR L.EXT"
    return "LONG Variational + SHORT Extended" if side == "long-var" else "SHORT Variational + LONG Extended"


def fmt_hours(h):
    return f"{int(h):02d}:{int(round(h % 1 * 60)):02d}"


def print_report(rows, skipped, s, now, cfg, n, hold, show_all):
    sess_vn = {"weekend": "CUỐI TUẦN (đóng)", "rth": "PHIÊN CHÍNH", "pre": "pre-market", "post": "after-hours",
               "overnight": "overnight", "open": "mở", "break": "nghỉ 1h"}
    print(f"hedge-scan · {now.astimezone(ICT):%Y-%m-%d %H:%M} ICT ({now.astimezone(ICT):%a}) · ${n:,.0f}/chân · giữ {hold:g}h"
          f" · pts: {cfg['var_points_default']}/$1M mặc định, boost +{cfg['points_boost'] * 100:.0f}%")
    a, b = s["rth_ict"]
    print(f"Phiên: Cổ phiếu Mỹ = {sess_vn[s['equity']]} (phiên chính {fmt_hours(a)}–{fmt_hours(b)} ICT, T2–T6)"
          f" · Hàng hoá CME = {sess_vn[s['cme']]} · FX = {sess_vn[s['fx']]}")
    if s["equity"] != "rth":
        print("⚠ Ngoài phiên chính Mỹ: spread cổ phiếu/ETF trên Variational thường rộng gấp nhiều lần → nếu không gấp, chờ phiên chính.")
    if s["near_bell"]:
        print("⚠ Đang trong 15 phút đầu/cuối phiên: biến động & spread cao, nên đợi.")
    print()
    hdr = f"{'#':>2}  {'Cặp VAR/EXT':<22}{'Chiều':<12}{'VAR':>6}{'EXT':>6}{'phí':>5}{'fund':>6}{'=bps':>6}{'$/vòng':>8}{'pts':>6}{'$/pt':>7}{'basis':>7}  Ghi chú"
    print(hdr)
    print("-" * len(hdr))
    shown = [r for r in rows if show_all or not (r["flags"] & HARD)][: cfg["top"] if not show_all else None]
    for i, r in enumerate(shown, 1):
        star = "★ " if r["pair"]["v"]["ticker"] in cfg["var_points_per_m"] else ""
        notes = star + ", ".join(FLAG_TEXT[f] for f in sorted(r["flags"]) if f != "unverified_pts")
        if "cost" not in r:
            print(f"{i:>2}  {label(r):<22}{'-':<12}{'':>6}{'':>6}{'':>5}{'':>6}{'':>6}{'':>8}{'':>6}{'':>7}{'':>7}  {notes}")
            continue
        print(f"{i:>2}  {label(r):<22}{side_txt(r['side'], True):<12}{r['var_rt']:>6.1f}{r['ext_rt']:>6.1f}{r['fee']:>5.1f}"
              f"{r['fund']:>+6.1f}{r['cost_bps']:>6.1f}{r['cost']:>8.2f}{r['pts']:>6.2f}{r['cpp']:>7.2f}{r['basis']:>+7.1f}  {notes}")
    print("\nCột: VAR/EXT = spread round-trip (mở+đóng) ở size này, bps · phí = 2×taker EXT · fund = funding nhận được trong thời gian giữ"
          " (+ là nhận) · =bps = tổng chi phí · basis = giá VAR − EXT (+ nghĩa là VAR đắt hơn) · ★ = cặp có trong list pts đã xác minh")
    if skipped:
        agg = {}
        for r in skipped:
            for f in r["flags"] & HARD:
                agg[FLAG_TEXT[f]] = agg.get(FLAG_TEXT[f], 0) + 1
        print(f"Bỏ qua {len(skipped)} cặp chưa giao dịch được lúc này ({', '.join(f'{k}: {v}' for k, v in sorted(agg.items()))}); --all để xem.")

    picks = [r for r in rows if not (r["flags"] & HARD) and "cost" in r][:3]
    if not picks:
        print("\nKhông có cặp nào giao dịch được ngay lúc này.")
        return
    print("\nGỢI Ý")
    for i, r in enumerate(picks, 1):
        p, v, e = r["pair"], r["pair"]["v"], r["pair"]["e"]
        other = "short-var" if r["side"] == "long-var" else "long-var"
        why = {"funding": "theo funding", "basis": "theo basis (vào giá tốt hơn)", "spread": "chiều vào rẻ hơn"}[r["why"]]
        print(f"{i}) {v['ticker']}: {side_txt(r['side'])} ({e['name']}), ${n:,.0f} mỗi chân — chọn chiều {why}")
        print(f"   1 vòng mở+đóng ≈ ${r['cost']:.2f} ({r['cost_bps']:.1f} bps) → +{r['pts']:.2f} pts VAR"
              f" ({r['ppm']:g}/$1M{'' if 'unverified_pts' not in r['flags'] else ', CHƯA xác minh'}) → ${r['cpp']:.2f}/pt")
        print(f"   Vào ngay: {r['entry'][r['side']]:.1f} bps (chiều ngược {r['entry'][other]:.1f}) · basis {r['basis']:+.1f} bps"
              + ("" if p["proxy"] else " → khi đóng, đợi basis đảo chiều/về 0 để đóng rẻ hơn (--exit)"))
        print(f"   Funding: VAR {r['fv_apr']:+.2f}% APR · EXT {r['fe_h']:+.4f}%/h (TB 8h; hiện tại {r['fe_now']:+.4f}%/h)"
              f" → chiều này {r['fund']:+.2f} bps/{hold:g}h")
        c = r["clips"]
        print(f"   VAR spread theo size (round-trip bps, ước tính): 1k {c[1e3]:.1f} · 5k {c[5e3]:.1f} · 10k {c[1e4]:.1f} · 20k {c[2e4]:.1f}"
              f" · quote cách đây {r['age']:.0f}s")
        if r["maker"] is not None:
            print(f"   EXT là sổ lệnh: đặt limit maker (0 phí) bên EXT, khớp rồi mới market bên VAR → ≈ {r['maker']:.1f} bps"
                  f" (${n * r['maker'] / 1e4:.2f}/vòng)")
        vs = r["vol"]
        if vs:
            ratio = f" (x{vs['ratio']:.1f} so với TB 24h)" if vs["ratio"] else ""
            print(f"   Biến động: σ5m {vs['sigma5m']:.1f} bps{ratio} · rủi ro lệch chân ~{vs['leg_risk']:.1f} bps/{cfg['leg_delay_s']}s")
        oi = sum(float(x) for x in v["open_interest"].values())
        print(f"   Thanh khoản: VAR vol24h ${float(v['volume_24h']) / 1e6:.2f}M, OI ${oi / 1e6:.2f}M · EXT vol24h"
              f" ${float(e['marketStats']['dailyVolume'] or 0) / 1e6:.2f}M, OI ${float(e['marketStats']['openInterest'] or 0) / 1e6:.2f}M"
              f"{' (RFQ)' if e.get('isRfq') else ' (orderbook)'}")
    print("\nLưu ý: spread VAR ở size 10–20k là nội suy từ quote $1k/$100k public → so với quote thật trên UI Omni trước khi bấm;"
          " nếu UI xấu hơn đáng kể, chia nhỏ lệnh hoặc bỏ qua.")


def exit_report(results, specs, n, cfg):
    for spec in specs:
        tick, _, side = spec.partition(":")
        side = side.strip().lower() or "long-var"
        r = next((x for x in results if x["pair"]["v"]["ticker"].upper() == tick.upper() and "cost" in x), None)
        if not r:
            print(f"{spec}: không tìm thấy cặp / thiếu dữ liệu")
            continue
        close_as = "short-var" if side == "long-var" else "long-var"  # closing = opposite trades
        now_bps = r["entry"][close_as]
        neutral = (r["var_rt"] + r["ext_rt"]) / 2 + r["fee"] / 2
        print(f"{r['pair']['v']['ticker']} (đang {side}): đóng ngay tốn {now_bps:.1f} bps (${n * now_bps / 1e4:.2f} cho ${n:,.0f}/chân);"
              f" mức trung tính {neutral:.1f} bps → {'ĐÓNG NGAY, basis đang có lợi' if now_bps <= neutral else 'basis đang bất lợi, có thể chờ'}"
              f" (basis {r['basis']:+.1f} bps)")


def log_rows(path, results, now):
    new = not os.path.exists(path)
    with open(path, "a", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["ts_utc", "var", "ext", "size", "var_rt_bps", "ext_rt_bps", "basis_bps", "var_fund_apr", "ext_fund_h_pct", "flags"])
        for r in results:
            if "cost" in r:
                w.writerow([now.isoformat(timespec="seconds"), r["pair"]["v"]["ticker"], r["pair"]["e"]["name"], r["n"],
                            round(r["var_rt"], 3), round(r["ext_rt"], 3), round(r["basis"], 3), round(r["fv_apr"], 4),
                            round(r["fe_h"], 6), "|".join(sorted(r["flags"]))])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--size", type=float, help="notional per leg in USD (leverage included)")
    ap.add_argument("--hold", type=float, help="expected holding time in hours (for funding)")
    ap.add_argument("--top", type=int)
    ap.add_argument("--only", help="comma-separated tickers")
    ap.add_argument("--all", action="store_true", help="also show pairs that are not tradable now")
    ap.add_argument("--exit", help="TICKER:long-var|short-var[,...] cost of closing an open hedge now")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--log", help="append a CSV snapshot to this file")
    ap.add_argument("--config", default=os.path.join(HERE, "config.json"))
    a = ap.parse_args()
    cfg = json.load(open(a.config))
    n = a.size or cfg["size_usd"]
    hold = a.hold if a.hold is not None else cfg["hold_hours"]
    if a.top:
        cfg["top"] = a.top
    now = dt.datetime.now(UTC)

    pairs = load(cfg)
    only = {t.strip().upper() for t in (a.only or "").split(",") if t.strip()}
    if a.exit:
        only |= {s.split(":")[0].strip().upper() for s in a.exit.split(",")}
    excl = {t.upper() for t in cfg["exclude"]}
    pairs = [p for p in pairs if p["v"]["ticker"].upper() not in excl
             and (not only or p["v"]["ticker"].upper() in only or p["e"]["name"].upper().split("-")[0] in only)]
    for p in pairs:  # no need to pull books for markets that cannot trade now
        p["skip"] = not a.all and (p["e"].get("isOffHours") or p["e"].get("status") != "ACTIVE")
    with cf.ThreadPoolExecutor(max_workers=12) as ex:
        pairs = list(ex.map(fetch_ext, pairs))
    results = sorted((evaluate(p, n, hold, cfg, now) for p in pairs), key=rank_key)
    if a.log:
        log_rows(a.log, results, now)
    if a.exit:
        exit_report(results, [s.strip() for s in a.exit.split(",")], n, cfg)
        return
    if a.json:
        out = []
        for r in results:
            d = {k: v for k, v in r.items() if k not in ("pair", "flags")}
            d.update(var=r["pair"]["v"]["ticker"], ext=r["pair"]["e"]["name"], flags=sorted(r["flags"]),
                     tradable=not (r["flags"] & HARD))
            d["clips"] = {str(int(k)): v for k, v in (r.get("clips") or {}).items()}
            out.append(d)
        json.dump(dict(time=now.isoformat(), size=n, hold=hold, sessions={k: v for k, v in sessions(now).items()}, pairs=out),
                  sys.stdout, indent=1, default=str)
        return
    skipped = [r for r in results if r["flags"] & HARD]
    print_report(results, skipped if not a.all else [], sessions(now), now, cfg, n, hold, a.all)


if __name__ == "__main__":
    main()
