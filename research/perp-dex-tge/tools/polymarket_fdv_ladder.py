#!/usr/bin/env python3
"""Polymarket "FDV above ___ one day after launch" ladder tracker.

Fetches every threshold market of one event, rebuilds the implied FDV
distribution over time and prints the implied median (where P(FDV > X)
crosses 50%, log-interpolated between thresholds).

Usage:
    python3 polymarket_fdv_ladder.py <event-slug> [step_days] [launch_prob]

    event-slug   e.g. variational-fdv-above-one-day-after-launch
    step_days    spacing of the timeline rows (default 14)
    launch_prob  optional P(token launches before the market deadline).
                 When given, the current ladder is also shown conditional on
                 launch: P(FDV > X | launch) = P(FDV > X) / launch_prob.

Notes:
- Uses only public endpoints (gamma-api.polymarket.com, clob.polymarket.com)
  and the Python standard library.
- The raw ladder mixes two things: whether the token launches before the
  deadline and how high the FDV is. Lowest-threshold prices approximate the
  launch probability.
- Historical calibration (Lighter, edgeX, Backpack, GRVT, Paradex, 2025-2026):
  the median 30 days before TGE overstated the actual day-1 FDV in 4 of 5
  cases (median error about -40%); 2 days before TGE it still overstated in
  4 of 5 cases (median error about -30%).
"""
import json
import math
import re
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone

UA = {"User-Agent": "curl/8.5.0", "Accept": "*/*"}


def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.loads(r.read().decode())


def threshold_musd(label):
    s = label.strip().replace(">", "").replace("$", "").replace(",", "")
    m = re.match(r"([\d.]+)\s*([MBK]?)", s, re.I)
    if not m:
        return None
    v, unit = float(m.group(1)), m.group(2).upper()
    return v * 1000 if unit == "B" else (v / 1000 if unit == "K" else v)


def implied_median(points):
    pts = sorted((x, p) for x, p in points if p is not None)
    if not pts:
        return None
    if pts[0][1] < 0.5:
        return f"<{pts[0][0]:,.0f}"
    for (x1, p1), (x2, p2) in zip(pts, pts[1:]):
        if p1 >= 0.5 > p2:
            f = (p1 - 0.5) / (p1 - p2)
            return f"{math.exp(math.log(x1) + f * (math.log(x2) - math.log(x1))):,.0f}"
    return f">{pts[-1][0]:,.0f}"


def price_at(series, t):
    last = None
    for tt, p in series:
        if tt <= t:
            last = p
        else:
            break
    return last


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    slug = sys.argv[1]
    step = float(sys.argv[2]) if len(sys.argv) > 2 else 14.0
    launch_prob = float(sys.argv[3]) if len(sys.argv) > 3 else None

    events = get("https://gamma-api.polymarket.com/events?slug=" + urllib.parse.quote(slug))
    if not events:
        sys.exit(f"event not found: {slug}")
    ev = events[0]
    print(f"# {ev['title']}  (volume ${float(ev.get('volume') or 0):,.0f}, closed={ev.get('closed')})")

    ladder = []
    for m in ev.get("markets", []):
        label = m.get("groupItemTitle") or m.get("question") or ""
        thr = threshold_musd(label)
        tokens = json.loads(m.get("clobTokenIds") or "[]")
        if thr is None or not tokens:
            continue
        hist = get("https://clob.polymarket.com/prices-history?" + urllib.parse.urlencode(
            {"market": tokens[0], "interval": "max", "fidelity": 720})).get("history", [])
        series = sorted((h["t"], h["p"]) for h in hist)
        now_p = json.loads(m.get("outcomePrices") or "[null]")[0]
        ladder.append((thr, series, float(now_p) if now_p is not None else None))
        time.sleep(0.15)
    ladder.sort()

    t_all = [t for _, s, _ in ladder for t, _ in s]
    if not t_all:
        sys.exit("no price history")
    t0, t1 = min(t_all), max(t_all)
    header = " ".join(f"{(f'{x/1000:g}B' if x >= 1000 else f'{x:g}M'):>6}" for x, _, _ in ladder)
    print(f"date       | {header} | median $M")
    t = t0
    while t <= t1 + step * 86400:
        tt = min(t, t1)
        pts = [(x, price_at(s, tt)) for x, s, _ in ladder]
        cells = " ".join(f"{p*100:6.1f}" if p is not None else "     -" for _, p in pts)
        day = datetime.fromtimestamp(tt, timezone.utc).strftime("%Y-%m-%d")
        print(f"{day} | {cells} | {implied_median(pts)}")
        if tt == t1:
            break
        t += step * 86400

    now = [(x, p) for x, _, p in ladder]
    print("\nCurrent ladder P(FDV > X):", ", ".join(f"{x:g}M={p:.3f}" for x, p in now if p is not None))
    print("Implied median now ($M):", implied_median(now))
    if launch_prob:
        cond = [(x, min(1.0, p / launch_prob)) for x, p in now if p is not None]
        print(f"Conditional on launch (P={launch_prob:.2f}) median ($M):", implied_median(cond))


if __name__ == "__main__":
    main()
