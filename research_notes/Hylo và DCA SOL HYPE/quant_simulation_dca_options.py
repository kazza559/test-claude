#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
quant_simulation_dca_options.py  (reproducible; pure standard library)

Compares three ways of DCA-ing $4,000 into SOL or HYPE with a 3-level ladder
($1,200 per level, $400 kept in USDC):
  (1) spot buys,
  (2) Hylo-style leveraged x-token buys (xSOL / xHYPE),
  (3) long perpetual futures (Variational Omni margin rules) at 2x / 3x,
across stylized scenarios and historical backtests (Hyperliquid daily data).

Usage:
  python3 quant_simulation_dca_options.py            # uses/creates hl_daily_snapshot.csv next to this file
  python3 quant_simulation_dca_options.py --refresh  # re-download data from the Hyperliquid info API
Output: Markdown tables on stdout.

Every modelling assumption lives in the PARAMS block and in the class docstrings.
Mechanics sources:
  Hylo:        https://docs.hylo.so/technical-addendum/hylo-equations  (NAV, CR, zones, fees, borrow-rate curve)
               https://docs.hylo.so/protocol-overview/collateral-rebalancing (sell/buy zones)
  Variational: https://docs.variational.io/omni/trading/leverage  (IM = 1/leverage, MM = IM/2)
               https://docs.variational.io/omni/trading/liquidation (partial liquidation, 0.5% penalty)
               https://docs.variational.io/omni/trading/funding-rates (0.00125%/h interest baseline ~ 11% APR)
               https://docs.variational.io/omni/trading/fees (no trading fees; spread only)
"""
import copy, csv, math, os, statistics as st, sys, time, datetime as dt, json

HERE = os.path.dirname(os.path.abspath(__file__))
SNAP = os.path.join(HERE, "hl_daily_snapshot.csv")
API = "https://api.hyperliquid.xyz/info"

# ----------------------------------------------------------------------------- PARAMS
class P:
    TOTAL = 4000.0            # account / budget (USDC)
    TRANCHE = 1200.0          # 30% per level; $400 stays in USDC
    SPOT_COST = 0.001         # 0.10% per spot buy/sell (fee + slippage) -- assumption
    PERP_HALF_SPREAD = 0.0002 # 2 bps paid on every perp open/close (Omni: 0 fees, spread only; quoted ~1-2.5 bps) -- assumption
    LIQ_PENALTY = 0.005       # Omni liquidation penalty 0.5% (docs)
    # Hylo x-token mint/redeem fees by rebalance zone (docs "example" bps): normal=Neutral&buy zones
    XFEES = {"normal": (0.01, 0.01), "sz1": (0.005, 0.04), "sz2": (0.0, 0.08)}
    SOL_LST_YIELD = 0.06      # hyloSOL APY 5-7% (docs) -> 6% used for the xSOL harvest multiplier
    SOL_MULT_CEIL = 2.0       # m_c "currently 2" (docs)
    HYPE_BORROW_BASE = 0.10   # xHYPE base borrow rate: NOT published -> 10%/yr assumption
    HYPE_BORROW_CEIL_MULT = 2.0  # ceiling "currently 2x the base" (docs)
    SUBSTEPS = 24             # intraday sub-steps per leg (open->low, low->close)
    FUND_BASE_APR = 0.11      # flat funding baseline (0.00125%/h * 8760 = 10.95%)

# ----------------------------------------------------------------------------- DATA
def _post(body):
    try:
        import requests
        for k in range(5):
            try:
                r = requests.post(API, json=body, timeout=30)
                r.raise_for_status()
                return r.json()
            except Exception:
                time.sleep(2 + 2 * k)
        raise RuntimeError("Hyperliquid API failed")
    except ImportError:
        import urllib.request
        req = urllib.request.Request(API, data=json.dumps(body).encode(),
                                     headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=30) as f:
            return json.load(f)

def _get(url, params):
    import requests
    for k in range(5):
        try:
            r = requests.get(url, params=params, timeout=30, headers={"User-Agent": "research-sim"})
            r.raise_for_status()
            return r.json()
        except Exception:
            time.sleep(2 + 2 * k)
    raise RuntimeError("GET failed: " + url)

def fetch_spot(coin):
    """Spot OHLC used as the main backtest price source (closer to the aggregated oracles that Hylo (Pyth)
    and Variational (index + fast EMA mark) use than Hyperliquid perp wicks).
    SOL: Coinbase Exchange SOL-USD daily candles; HYPE: Hyperliquid spot HYPE/USDC (pair @107)."""
    now = dt.datetime.now(dt.timezone.utc)
    rows = {}
    if coin == "SOL":
        s = dt.datetime(2023, 12, 1, tzinfo=dt.timezone.utc)
        while s < now:
            e = min(s + dt.timedelta(days=299), now)
            for k in _get("https://api.exchange.coinbase.com/products/SOL-USD/candles",
                          {"granularity": 86400, "start": s.isoformat(), "end": e.isoformat()}):
                day = dt.datetime.fromtimestamp(k[0], dt.timezone.utc).date().isoformat()
                rows[day] = (k[3], k[2], k[1], k[4])  # o, h, l, c
            s = e + dt.timedelta(days=1)
            time.sleep(0.4)
    else:
        start = int(dt.datetime(2024, 11, 29, tzinfo=dt.timezone.utc).timestamp() * 1000)
        cs = _post({"type": "candleSnapshot",
                    "req": {"coin": "@107", "interval": "1d", "startTime": start, "endTime": int(time.time() * 1000)}})
        for k in cs:
            day = dt.datetime.fromtimestamp(k["t"] / 1000, dt.timezone.utc).date().isoformat()
            rows[day] = (float(k["o"]), float(k["h"]), float(k["l"]), float(k["c"]))
    return rows

def fetch_snapshot(path=SNAP):
    now_ms = int(time.time() * 1000)
    mids = _post({"type": "allMids"})
    out = []
    for coin in ("SOL", "HYPE"):
        spot = fetch_spot(coin)
        start = int(dt.datetime(2023, 6, 1, tzinfo=dt.timezone.utc).timestamp() * 1000)
        cs = _post({"type": "candleSnapshot",
                    "req": {"coin": coin, "interval": "1d", "startTime": start, "endTime": now_ms}})
        fund = {}
        t = max(cs[0]["t"], int(dt.datetime(2024, 1, 1, tzinfo=dt.timezone.utc).timestamp() * 1000))
        while t < now_ms:
            f = _post({"type": "fundingHistory", "coin": coin, "startTime": t, "endTime": now_ms})
            if not f:
                break
            for x in f:
                day = dt.datetime.fromtimestamp(x["time"] / 1000, dt.timezone.utc).date().isoformat()
                fund[day] = fund.get(day, 0.0) + float(x["fundingRate"])
            nt = f[-1]["time"] + 1
            if nt <= t or len(f) < 2:
                break
            t = nt
        for c in cs:
            day = dt.datetime.fromtimestamp(c["t"] / 1000, dt.timezone.utc).date().isoformat()
            sp = spot.get(day, ("", "", "", ""))
            out.append([coin, day, c["o"], c["h"], c["l"], c["c"],
                        ("%.10f" % fund[day]) if day in fund else ""] + list(sp))
    with open(path, "w", newline="") as fh:
        fh.write("# fetched_utc=%s mid_SOL=%s mid_HYPE=%s source=api.hyperliquid.xyz/info candleSnapshot 1d + fundingHistory; "
                 "spot: Coinbase SOL-USD, Hyperliquid spot HYPE/USDC @107\n"
                 % (dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), mids["SOL"], mids["HYPE"]))
        w = csv.writer(fh)
        w.writerow(["coin", "date", "open", "high", "low", "close", "funding_daily_sum",
                    "spot_open", "spot_high", "spot_low", "spot_close"])
        w.writerows(out)

def load(path=SNAP, refresh=False):
    if refresh or not os.path.exists(path):
        fetch_snapshot(path)
    data, meta = {"SOL": [], "HYPE": []}, ""
    with open(path) as fh:
        lines = [l for l in fh]
    meta = lines[0].strip() if lines[0].startswith("#") else ""
    rdr = csv.DictReader([l for l in lines if not l.startswith("#")])
    fl = lambda x: float(x) if x not in (None, "") else None
    for r in rdr:
        data[r["coin"]].append(dict(date=r["date"], o=float(r["open"]), h=float(r["high"]),
                                    l=float(r["low"]), c=float(r["close"]),
                                    f=fl(r["funding_daily_sum"]),
                                    so=fl(r.get("spot_open")), sl=fl(r.get("spot_low")), sc=fl(r.get("spot_close"))))
    return data, meta

# ----------------------------------------------------------------------------- HELPERS
def geo(a, b, n):
    if a <= 0 or b <= 0 or abs(a - b) < 1e-12:
        return [b]
    return [a * (b / a) ** (i / n) for i in range(1, n + 1)]

def zone(cr):
    if cr < 1.0: return "destab"
    if cr < 1.20: return "sz2"
    if cr < 1.35: return "sz1"
    if cr < 1.65: return "neutral"
    if cr < 1.75: return "bz1"
    return "bz2"

def xfee(cr, side):  # side 0 = mint, 1 = redeem; None = blocked
    z = zone(cr)
    if z == "destab":
        return None
    key = z if z in ("sz1", "sz2") else "normal"
    return P.XFEES[key][side]

def ramp(cr):  # 0 below 165%, linear to 1 at 175% (buy zone 1 interpolation)
    return min(max((cr - 1.65) / 0.10, 0.0), 1.0)

def sol_mult(cr):  # LST-yield harvest multiplier m(CR)
    if cr < 1.35: return 0.0
    return 1.0 + (P.SOL_MULT_CEIL - 1.0) * ramp(cr)

def hype_rate(cr):  # annual borrow rate r(CR) on xHYPE market cap
    if cr < 1.35: return 0.0
    base = P.HYPE_BORROW_BASE
    return base + (P.HYPE_BORROW_CEIL_MULT * base - base) * ramp(cr)

# ----------------------------------------------------------------------------- PRODUCTS
class Spot:
    """Spot ladder: buy $TRANCHE at each level (0.10% cost); unfilled tranches + $400 stay in USDC.
    Optional staking APY (e.g. SOL LST) compounds daily on the token quantity."""
    def __init__(self, stake=0.0):
        self.cash, self.q, self.stake, self.fills = P.TOTAL, 0.0, stake, []
    def buy(self, k, p):
        px = p * (1 + P.SPOT_COST)
        self.q += P.TRANCHE / px; self.cash -= P.TRANCHE
        self.fills.append(dict(k=k, p=p))
    def on_price(self, p): pass
    def on_close(self, p, fund): self.q *= (1 + self.stake / 365)
    def value(self, p, exit=False):
        return self.cash + self.q * p * (1 - (P.SPOT_COST if exit else 0.0))
    def flag(self): return ""

class XToken:
    """Hylo-style x-token (xSOL/xHYPE). Pool state: collateral C (asset units), vUSD liabilities D ($),
    x-supply normalised to 1 (user is too small to move the pool).  NAV = C*P - D  (docs: (TVL - vUSD)/supply).
    CR = C*P/D ; effective leverage = CR/(CR-1).  Wiped when CR <= 100% (NAV -> 0, redemptions blocked).
    variant: 'static'  -> supplies fixed (value linear in P)
             'sell135' -> V2 sell zone: if CR < 135% at a daily close, sell collateral at spot to restore 135%
             'sell130' -> V1-style Stability Mode 2: restore 130% (hyUSD->x conversion; same effect on holders)
             'band'    -> V2 sell zone (135%) + buy zone (re-lever to 165% when CR > 165%)
    Carry: xSOL -> LST harvest multiplier m(CR) (y = 6%/yr); xHYPE -> borrow rate r(CR) on x market cap.
    Fees: zone-dependent mint/redeem (1%/1% normal, 0.5%/4% SZ1, 0%/8% SZ2) unless fees=False."""
    def __init__(self, asset, cr0, L1, variant="static", carry=True, fees=True):
        self.asset, self.variant, self.carry, self.fees = asset, variant, carry, fees
        self.C, self.D = 1.0, L1 / cr0
        self.s, self.cash, self.wiped, self.wipe_price = 0.0, P.TOTAL, False, None
        self.fills, self.blocked, self.rebal = [], 0, 0
    def cr(self, p): return self.C * p / self.D
    def nav(self, p): return 0.0 if self.wiped else max(self.C * p - self.D, 0.0)
    def lev(self, p):
        e = self.C * p - self.D
        return self.C * p / e if e > 0 else float("inf")
    def buy(self, k, p):
        cr = self.cr(p)
        if self.wiped or cr <= 1.0:
            self.blocked += 1; return
        fee = xfee(cr, 0) if self.fees else 0.0
        self.s += P.TRANCHE * (1 - fee) / self.nav(p); self.cash -= P.TRANCHE
        self.fills.append(dict(k=k, p=p, cr=cr, lev=self.lev(p), fee=fee, wipe=self.D / self.C))
    def on_price(self, p):
        if not self.wiped and self.C * p <= self.D:
            self.wiped, self.wipe_price = True, p
    def on_close(self, p, fund):
        if self.wiped: return
        cr = self.cr(p)
        if self.carry:
            if self.asset == "SOL":
                y = P.SOL_LST_YIELD / 365
                harvest = sol_mult(cr) * y * self.C * p     # hyUSD minted against the pool
                self.C *= (1 + y); self.D += harvest       # LST appreciation vs harvest
            else:
                self.D += hype_rate(cr) / 365 * max(self.C * p - self.D, 0.0)
        if self.C * p <= self.D:
            self.wiped, self.wipe_price = True, p; return
        floor = {"sell135": 1.35, "sell130": 1.30, "band": 1.35}.get(self.variant)
        cap = 1.65 if self.variant == "band" else None
        cr, tgt = self.cr(p), None
        if floor and cr < floor: tgt = floor
        elif cap and cr > cap: tgt = cap
        if tgt:
            E = self.C * p - self.D
            self.C = E * tgt / (p * (tgt - 1)); self.D = self.C * p - E
            self.rebal += 1
    def value(self, p, exit=False):
        v = self.s * self.nav(p)
        if exit and v > 0 and self.fees:
            fee = xfee(self.cr(p), 1)
            v = 0.0 if fee is None else v * (1 - fee)
        return self.cash + v
    def flag(self):
        return ("WIPED @%.4g" % self.wipe_price) if self.wiped else ""

class Perp:
    """Long perp ladder, cross margin, all $4,000 in the account.
    Variational Omni rules: IM = 1/leverage, MM = IM/2 (so 2x -> MM 25%, 3x -> MM 16.7%) unless mmr given.
    interp 'A': $1,200 margin per tranche (notional 1,200*lev);  'B': $1,200 notional per tranche.
    IM check (im_check=True): a new tranche is cut to what free margin allows:
        free = equity - IM% * (existing notional at mark)  -> max new notional = free / IM%.
    Liquidation: when equity < MM% * notional (marked every sub-step), partial liquidation closes just enough
    (at mark*(1 - spread - 0.5% penalty)) to bring equity back to MM.  Funding charged daily on notional."""
    def __init__(self, lev, interp, mmr=None, im_check=True):
        self.lev, self.interp = lev, interp
        self.imr = 1.0 / lev
        self.mmr = mmr if mmr is not None else 0.5 / lev
        self.planned = P.TRANCHE * lev if interp == "A" else P.TRANCHE
        self.cash, self.q, self.cost = P.TOTAL, 0.0, 0.0
        self.im_check, self.fills, self.liqs = im_check, [], []
        self.first_liq, self.q_max, self.funding_paid, self.wiped = None, 0.0, 0.0, False
    def equity(self, p): return self.cash + self.q * p - self.cost
    def liq_price(self):
        if self.q <= 0: return None
        x = (self.cost - self.cash) / (self.q * (1 - self.mmr))
        return x if x > 0 else None
    def buy(self, k, p):
        if self.wiped: return
        n = self.planned
        if self.im_check:
            free = self.equity(p) - self.imr * self.q * p
            n = min(n, max(free, 0.0) / self.imr)
        if n <= 1e-9:
            self.fills.append(dict(k=k, p=p, notional=0.0, liq=self.liq_price())); return
        px = p * (1 + P.PERP_HALF_SPREAD)
        dq = n / px
        self.q += dq; self.cost += dq * px; self.q_max = max(self.q_max, self.q)
        self.fills.append(dict(k=k, p=p, notional=n, liq=self.liq_price()))
    def _close(self, dq, px):
        avg = self.cost / self.q
        self.cash += dq * (px - avg); self.cost -= dq * avg; self.q -= dq
        if self.q < 1e-12: self.q, self.cost = 0.0, 0.0
    def on_price(self, p):
        if self.q <= 0 or self.wiped: return
        E = self.equity(p)
        if E >= self.mmr * self.q * p: return
        kk = P.PERP_HALF_SPREAD + P.LIQ_PENALTY
        if self.first_liq is None: self.first_liq = p
        qn = (E - self.q * p * kk) / (p * (self.mmr - kk))
        if qn <= 0:
            self._close(self.q, p * (1 - kk)); self.wiped = True
            self.cash = max(self.cash, 0.0)
        else:
            self._close(self.q - qn, p * (1 - kk))
        self.liqs.append(p)
    def on_close(self, p, fund):
        if self.q > 0:
            f = fund * self.q * p
            self.cash -= f; self.funding_paid += f
            self.on_price(p)
    def value(self, p, exit=False):
        return max(self.equity(p) - (self.q * p * P.PERP_HALF_SPREAD if exit else 0.0), 0.0)
    def flag(self):
        if self.first_liq is None: return ""
        closed = 1 - self.q / self.q_max if self.q_max > 0 else 1
        return "LIQ from %.4g (%.0f%% closed)" % (self.first_liq, 100 * closed)

class LETF:
    """Reference only: daily-rebalanced constant-leverage token (rebalanced at each daily close)."""
    def __init__(self, L):
        self.L, self.cash, self.v, self.ref, self.dead = L, P.TOTAL, 0.0, None, False
    def mark(self, p):
        if self.v <= 0: return 0.0
        return self.v * max(1 + self.L * (p / self.ref - 1), 0.0)
    def buy(self, k, p):
        self.v = self.mark(p) + P.TRANCHE if self.v > 0 else P.TRANCHE
        self.ref = p; self.cash -= P.TRANCHE
    def on_price(self, p):
        if self.v > 0 and 1 + self.L * (p / self.ref - 1) <= 0: self.v = 0.0; self.dead = True
    def on_close(self, p, fund):
        if self.v > 0: self.v, self.ref = self.mark(p), p
    def value(self, p, exit=False): return self.cash + self.mark(p)
    def flag(self): return "WIPED" if self.dead else ""

# ----------------------------------------------------------------------------- ENGINE
def breakeven(prod, p):
    """Price at which the whole $4,000 account is back to $4,000 (exit costs included), holding the
    post-last-fill state fixed (no further funding/carry/rebalancing)."""
    f = lambda x: prod.value(x, exit=True) - P.TOTAL
    lo, hi = p * 0.2, p * 5.0
    if f(hi) < 0: return None
    if f(lo) >= 0: return lo
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if f(mid) >= 0: hi = mid
        else: lo = mid
    return hi

def exposure(prod, p):  # $ gained per +1% move in the underlying (instantaneous)
    return prod.value(p * 1.005) - prod.value(p * 0.995)

def run(prod, bars, levels):
    """bars: list of (date, open, low, close, funding_daily_fraction). bars[0] = entry day (tranche 1 at levels[0]).
    Intraday path assumed open -> low -> close (worst case for longs); limit buys fill at their level."""
    prod.buy(0, levels[0])
    filled = [True] + [False] * (len(levels) - 1)
    snap = copy.deepcopy(prod) if all(filled) else None
    snap_p = levels[0]
    peak, mdd, vmin = P.TOTAL, 0.0, P.TOTAL
    def upd(v):
        nonlocal peak, mdd, vmin
        peak = max(peak, v); vmin = min(vmin, v)
        mdd = max(mdd, (peak - v) / peak if peak > 0 else 0.0)
    upd(prod.value(levels[0]))
    for d in range(1, len(bars)):
        _, o, l, c, fund = bars[d]
        pts = [o] + geo(o, l, P.SUBSTEPS) + [lv for k, lv in enumerate(levels) if not filled[k] and l <= lv < o]
        pts.sort(reverse=True)
        for p in pts:
            for k, lv in enumerate(levels):
                if not filled[k] and p <= lv:
                    prod.buy(k, p); filled[k] = True
                    if all(filled):
                        snap, snap_p = copy.deepcopy(prod), p
            prod.on_price(p)
        upd(prod.value(l))
        for p in geo(l, c, P.SUBSTEPS):
            prod.on_price(p)
        prod.on_close(c, fund)
        upd(prod.value(c))
    end = prod.value(bars[-1][3], exit=True)
    res = dict(end=end, pnl=end / P.TOTAL - 1, mdd=mdd, vmin=vmin, filled=sum(filled), flag=prod.flag(),
               be=None, exp=None, prod=prod)
    if snap is not None and sum(filled) == len(levels):
        res["be"], res["exp"], res["fill_p"] = breakeven(snap, snap_p), exposure(snap, snap_p), snap_p
    return res

def path_bars(wps, fund_apr):
    closes = []
    for (d0, p0), (d1, p1) in zip(wps, wps[1:]):
        for d in range(d0, d1):
            closes.append(p0 * (p1 / p0) ** ((d - d0) / (d1 - d0)))
    closes.append(wps[-1][1])
    bars = [("d0", closes[0], closes[0], closes[0], 0.0)]
    for i in range(1, len(closes)):
        o, c = closes[i - 1], closes[i]
        bars.append(("d%d" % i, o, min(o, c), c, fund_apr / 365))
    return bars

# ----------------------------------------------------------------------------- PRODUCT SETS
def product_set(asset, L1, full=True):
    X = "x" + asset
    ps = [("Spot ladder", lambda: Spot())]
    if asset == "SOL" and full:
        ps.append(("Spot ladder + 6% staking (LST)", lambda: Spot(stake=0.06)))
    for cr in (1.5, 2.0, 2.5, 3.0):
        ps.append(("%s static, CR0 %.1f (L0 %.2fx)" % (X, cr, cr / (cr - 1)),
                   (lambda cr=cr: XToken(asset, cr, L1, "static"))))
    for cr in (1.5, 2.0):
        ps.append(("%s sell-zone floor 135%%, CR0 %.1f" % (X, cr), (lambda cr=cr: XToken(asset, cr, L1, "sell135"))))
    ps.append(("%s V2 band 135-165%%, CR0 1.5" % X, lambda: XToken(asset, 1.5, L1, "band")))
    ps.append(("Perp A 2x ($1,200 margin/tranche)", lambda: Perp(2, "A")))
    ps.append(("Perp A 3x ($1,200 margin/tranche)", lambda: Perp(3, "A")))
    if full:
        ps.append(("Perp A 2x, full size (no IM cap)", lambda: Perp(2, "A", im_check=False)))
        ps.append(("Perp A 3x, full size (no IM cap)", lambda: Perp(3, "A", im_check=False)))
    ps.append(("Perp B ($1,200 notional/tranche, 2x or 3x)", lambda: Perp(2, "B")))
    return ps

# ----------------------------------------------------------------------------- OUTPUT
def md(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(x) for x in r) + " |")
    return "\n".join(out)

def fm(x, nd=0, pre="$"):
    if x is None: return "n/a"
    return ("%s%s" % (pre, format(x, ",.%df" % nd)))

def fp(x, nd=1):
    return "n/a" if x is None else ("%+.*f%%" % (nd, 100 * x))

def fpx(x):  # price formatting
    if x is None: return "n/a"
    return "$%.2f" % x if x < 1000 else "$%,.0f" % x

def scenarios(L):
    L1, L2, L3 = L
    zz = [(0, L1)]
    for i in range(6):
        zz += [(30 * i + 15, L3), (30 * i + 30, L1)]
    zz[-1] = (180, L2)
    return [
        ("(i) V-shape: L1->L2 (d20)->L3 (d40)->back to L1 (d90)", [(0, L1), (20, L2), (40, L3), (90, L1)]),
        ("(ii-a) all filled, then -30% below L3 (d90)", [(0, L1), (20, L2), (40, L3), (90, 0.7 * L3)]),
        ("(ii-b) all filled, then -50% below L3 (d90)", [(0, L1), (20, L2), (40, L3), (90, 0.5 * L3)]),
        ("(iii) only L1 filled, then +50% rally (d90)", [(0, L1), (90, 1.5 * L1)]),
        ("(iv) choppy L1<->L3 x6 cycles, ends at L2 (d180)", zz),
    ]

def stylized(asset, L, fund_apr=P.FUND_BASE_APR, full=True):
    out = []
    for sname, wps in scenarios(L):
        bars = path_bars(wps, fund_apr)
        rows = []
        for name, mk in product_set(asset, L[0], full):
            r = run(mk(), bars, L)
            rows.append((name, r))
        out.append((sname, bars[-1][3], rows))
    return out

def print_stylized(asset, L, res):
    print("\n#### %s ladder L1/L2/L3 = %s / %s / %s  (funding %.0f%% APR for perps)\n" %
          (asset, fpx(L[0]), fpx(L[1]), fpx(L[2]), 100 * P.FUND_BASE_APR))
    for sname, endp, rows in res:
        print("\n**%s** - end price %s\n" % (sname, fpx(endp)))
        tab = []
        for name, r in rows:
            tab.append([name, r["filled"], fm(r["end"]), fp(r["pnl"]), "%.1f%%" % (100 * r["mdd"]),
                        r["flag"] or "no", fpx(r["be"]) if r["be"] else ("n/a" if r["filled"] == 3 else "-"),
                        fm(r["exp"], 1) if r["exp"] is not None else "-"])
        print(md(["Option", "Fills", "End value", "P&L", "Max DD", "Liq / wipe", "Break-even after 3 fills",
                  "$ per 1% move after 3 fills"], tab))

# ----------------------------------------------------------------------------- MAIN
def main():
    refresh = "--refresh" in sys.argv
    data, meta = load(refresh=refresh)
    print("# DCA ladder simulation output\n")
    print("Data snapshot: `%s`\n" % meta)
    sol_now, hype_now = data["SOL"][-1]["c"], data["HYPE"][-1]["c"]
    print("Latest (partial-day) close: SOL %s, HYPE %s\n" % (fpx(sol_now), fpx(hype_now)))
    HYPE_L = [80.0, 70.0, 60.0]
    SOL_L = [120.0, 105.0, 90.0]
    HYPE_ALT = [round(hype_now * x, 2) for x in (0.9, 0.8, 0.7)]
    print("HYPE user levels vs current: " + ", ".join("%s = %+.1f%%" % (fpx(x), 100 * (x / hype_now - 1)) for x in HYPE_L))
    print("\nHYPE alt ladder (-10/-20/-30%% of current): %s" % ", ".join(fpx(x) for x in HYPE_ALT))
    print("\nSOL ladder: %s (L1 near current %s; L2 = -12.5%%, L3 = -25%%)" % (", ".join(fpx(x) for x in SOL_L), fpx(sol_now)))

    # ---- A. x-token wipe-out table
    print("\n## A. Hylo x-token: leverage and wipe-out under static supplies\n")
    rows = []
    for cr in (1.5, 2.0, 2.5, 3.0):
        L0 = cr / (cr - 1)
        cr2, cr3 = cr * 0.875, cr * 0.75
        rows.append(["%.1f" % cr, "%.2fx" % L0, "%.1f%%" % (100 * (1 - 1 / cr)),
                     "%.3f / %.2fx" % (cr2, cr2 / (cr2 - 1)), "%.3f / %.2fx" % (cr3, cr3 / (cr3 - 1)),
                     fpx(80 / cr), "%.1f%%" % (100 * (1 - (80 / cr) / 60)), fpx(120 / cr), "%.1f%%" % (100 * (1 - (120 / cr) / 90)),
                     "%.1f%%" % (100 * (sol_mult(cr) - 1) * P.SOL_LST_YIELD * L0 * (1 if cr >= 1.65 else 1)),
                     "%.1f%%" % (100 * hype_rate(cr))])
    print(md(["CR0 at L1", "Leverage at L1", "Underlying drop from L1 that wipes out", "CR / leverage at L2 (-12.5%)",
              "CR / leverage at L3 (-25%)", "HYPE wipe price (L1 $80)", "Further drop below $60 to wipe",
              "SOL wipe price (L1 $120)", "Further drop below $90 to wipe",
              "xSOL carry (%/yr of equity) at CR0", "xHYPE carry (%/yr of equity) at CR0"], rows))

    # ---- B. Perp liquidation prices after each tranche (analytic, no funding, planned full size)
    print("\n## B. Perp ladder: liquidation price after each tranche (cross margin, $4,000 account, no funding yet)\n")
    for asset, L in (("HYPE", HYPE_L), ("SOL", SOL_L)):
        rows = []
        for lev in (2, 3):
            for interp in ("A", "B"):
                for mmr_name, mmr in (("Variational MM=IM/2 (%.1f%%)" % (50 / lev), None), ("generic MM 3%", 0.03)):
                    pr = Perp(lev, interp, mmr=mmr, im_check=False)
                    liqs, nots = [], 0.0
                    for k, lv in enumerate(L):
                        pr.buy(k, lv)
                        lp = pr.liq_price()
                        liqs.append(fpx(lp) if lp else "none")
                    Ntot = sum(f["notional"] for f in pr.fills)
                    rows.append(["%s %dx" % (interp, lev), mmr_name, fm(Ntot), "%.2fx" % (Ntot / P.TOTAL)] + liqs +
                                ["%.1f%%" % (100 * (1 - pr.liq_price() / L[2])) if pr.liq_price() else "n/a"])
        print("\n**%s ladder %s**\n" % (asset, " / ".join(fpx(x) for x in L)))
        print(md(["Perp", "Maintenance margin", "Total notional after 3 fills", "Account leverage at entry",
                  "Liq. price after T1", "after T2", "after T3", "Further drop below L3 to liquidation"], rows))
    # IM check illustration
    print("\n**Initial-margin check at the 3rd tranche (Variational IM = 1/leverage), HYPE 80/70/60, no funding:**\n")
    rows = []
    for lev in (2, 3):
        pr = Perp(lev, "A", im_check=True)
        for k, lv in enumerate(HYPE_L):
            pr.buy(k, lv)
        f3 = pr.fills[-1]
        rows.append(["A %dx" % lev, fm(P.TRANCHE * lev), fm(f3["notional"]), "%.0f%%" % (100 * f3["notional"] / (P.TRANCHE * lev)),
                     fpx(pr.liq_price())])
    print(md(["Perp", "Planned T3 notional", "Max T3 notional allowed by free margin", "Share of plan", "Liq. price after capped T3"], rows))

    # ---- C. Stylized scenarios
    print("\n## C. Stylized scenarios\n")
    res_h = stylized("HYPE", HYPE_L)
    print_stylized("HYPE", HYPE_L, res_h)
    res_s = stylized("SOL", SOL_L)
    print_stylized("SOL", SOL_L, res_s)
    res_a = stylized("HYPE", HYPE_ALT, full=False)
    print_stylized("HYPE (alt ladder -10/-20/-30% of current)", HYPE_ALT, res_a)

    # funding sensitivity
    print("\n### C2. Perp funding sensitivity (HYPE 80/70/60; P&L on $4,000; IM-capped)\n")
    rows = []
    for sname, wps in scenarios(HYPE_L):
        row = [sname]
        for lev, interp in ((2, "A"), (3, "A"), (2, "B")):
            for apr in (0.05, 0.11, 0.20):
                r = run(Perp(lev, interp), path_bars(wps, apr), HYPE_L)
                row.append(fp(r["pnl"]) + (" L" if r["flag"] else ""))
        rows.append(row)
    print(md(["Scenario", "A2x 5%", "A2x 11%", "A2x 20%", "A3x 5%", "A3x 11%", "A3x 20%", "B 5%", "B 11%", "B 20%"], rows))
    print("\n(L = at least one partial liquidation)")

    # x-token variant sensitivity: V1 130% floor, carry off
    print("\n### C3. x-token sensitivity (HYPE 80/70/60): V1-style 130% floor; carry and fees switched off\n")
    rows = []
    for sname, wps in scenarios(HYPE_L):
        bars = path_bars(wps, P.FUND_BASE_APR)
        row = [sname]
        for mk in (lambda: XToken("HYPE", 1.5, 80, "sell135"), lambda: XToken("HYPE", 1.5, 80, "sell130"),
                   lambda: XToken("HYPE", 1.5, 80, "static", carry=False, fees=False),
                   lambda: XToken("HYPE", 2.0, 80, "static", carry=False, fees=False),
                   lambda: XToken("HYPE", 3.0, 80, "static", carry=False, fees=False)):
            r = run(mk(), bars, HYPE_L)
            row.append(fp(r["pnl"]) + (" W" if r["flag"] else ""))
        rows.append(row)
    print(md(["Scenario", "floor 135% CR0 1.5", "floor 130% CR0 1.5", "static 1.5 no carry/fees",
              "static 2.0 no carry/fees", "static 3.0 no carry/fees"], rows))

    # ---- D. Path dependence illustration: single $1,200 tranche at L1, no fees/carry/funding
    print("\n## D. Path dependence: one $1,200 tranche bought at $80, price returns to $80 (no fees, carry or funding)\n")
    paths = [("V: 80->60 (d45)->80 (d90)", [(0, 80), (45, 60), (90, 80)]),
             ("Zigzag 80<->60 x6, ends 80 (d180)", [(0, 80)] + sum([[(30 * i + 15, 60), (30 * i + 30, 80)] for i in range(6)], [])),
             ("Zigzag 80<->70 x12, ends 80 (d180)", [(0, 80)] + sum([[(15 * i + 7, 70), (15 * i + 15, 80)] for i in range(12)], []))]
    prods = [("Spot", lambda: Spot()),
             ("x-token static CR0 1.5 (3x at entry)", lambda: XToken("HYPE", 1.5, 80, "static", False, False)),
             ("x-token static CR0 2.0 (2x at entry)", lambda: XToken("HYPE", 2.0, 80, "static", False, False)),
             ("x-token V2 band 135-165%", lambda: XToken("HYPE", 1.5, 80, "band", False, False)),
             ("Daily-rebalanced 2x (LETF-style)", lambda: LETF(2)),
             ("Daily-rebalanced 3x (LETF-style)", lambda: LETF(3)),
             ("Perp 3x fixed size, $3,600 notional", lambda: Perp(3, "A"))]
    rows = []
    for pname, mk in prods:
        row = [pname]
        for nm, wps in paths:
            bars = path_bars(wps, 0.0)
            spt = P.SPOT_COST; P.SPOT_COST = 0.0; hs = P.PERP_HALF_SPREAD; P.PERP_HALF_SPREAD = 0.0
            r = run(mk(), bars, [80.0])
            P.SPOT_COST = spt; P.PERP_HALF_SPREAD = hs
            tv = r["end"] - (P.TOTAL - P.TRANCHE)
            row.append("%s (%s)" % (fm(tv), fp(tv / P.TRANCHE - 1)) + (" " + r["flag"] if r["flag"] else ""))
        rows.append(row)
    print(md(["Product (tranche value at end)"] + [p[0] for p in paths], rows))

    # ---- E. Historical backtests
    print("\n## E. Historical backtests (daily data; ladder L1 = start-day close, L2 = -12.5%, L3 = -25%; 180-day hold)\n")
    print("Main price source = spot OHLC (SOL: Coinbase SOL-USD; HYPE: Hyperliquid spot HYPE/USDC). Sensitivity = Hyperliquid perp OHLC "
          "(includes venue-specific wicks, e.g. SOL-PERP low $137.5 on 2025-10-10 vs Coinbase $176.9). Perp funding = Hyperliquid "
          "historical hourly funding summed per UTC day (proxy for Variational).\n")
    today = data["SOL"][-1]["date"]
    for asset in ("SOL", "HYPE"):
        rowsd = [r for r in data[asset] if r["date"] != today]  # drop partial day
        fall = [r["f"] for r in rowsd if r["f"] is not None]
        f25 = [r["f"] for r in rowsd if r["f"] is not None and r["date"] >= "2025-01-01"]
        first_f = next(r["date"] for r in rowsd if r["f"] is not None)
        print("\n### %s - Hyperliquid funding mean: %.1f%% APR (%s..%s), %.1f%% APR (2025-01-01..%s)\n" %
              (asset, 100 * 365 * st.mean(fall), first_f, rowsd[-1]["date"], 100 * 365 * st.mean(f25), rowsd[-1]["date"]))
        idx = {r["date"]: i for i, r in enumerate(rowsd)}
        starts, y, m = [], 2024, 1
        while True:
            dstr = "%04d-%02d-01" % (y, m)
            if dstr > "2026-04-01": break
            if dstr in idx and idx[dstr] + 180 < len(rowsd): starts.append(idx[dstr])
            m += 1
            if m == 13: y, m = y + 1, 1
        if asset == "HYPE":
            starts = [0] + starts
        names = [n for n, _ in product_set(asset, 1.0, full=False)] + ["Daily-rebal. 2x (ref)", "Daily-rebal. 3x (ref)"]
        short = {n: n.replace(" ($1,200 margin/tranche)", "").replace(" ($1,200 notional/tranche, 2x or 3x)", "")
                 .replace(" static, CR0", " st").replace(" sell-zone floor 135%, CR0", " fl135")
                 .replace(" V2 band 135-165%, CR0 1.5", " band").replace(" (L0 3.00x)", "").replace(" (L0 2.00x)", "")
                 .replace(" (L0 1.67x)", "").replace(" (L0 1.50x)", "") for n in names}
        summ = {}
        for srcname in ("spot", "perp"):
            allres = {n: [] for n in names}
            wrows = []
            for s in starts:
                win = rowsd[s:s + 181]
                if srcname == "spot":
                    if any(r["sc"] is None or r["sl"] is None or r["so"] is None for r in win): continue
                    O, Lo, C = [r["so"] for r in win], [r["sl"] for r in win], [r["sc"] for r in win]
                else:
                    O, Lo, C = [r["o"] for r in win], [r["l"] for r in win], [r["c"] for r in win]
                L1 = C[0]
                L = [L1, 0.875 * L1, 0.75 * L1]
                bars = [(win[i]["date"], O[i], Lo[i], C[i],
                         win[i]["f"] if win[i]["f"] is not None else P.FUND_BASE_APR / 365) for i in range(181)]
                rets = [math.log(C[i] / C[i - 1]) for i in range(1, len(C))]
                vol = st.pstdev(rets) * math.sqrt(365)
                fapr = 365 * st.mean([b[4] for b in bars[1:]])
                ps = product_set(asset, L1, full=False) + [("Daily-rebal. 2x (ref)", lambda: LETF(2)),
                                                           ("Daily-rebal. 3x (ref)", lambda: LETF(3))]
                wr = {}
                for n, mk in ps:
                    r = run(mk(), bars, L)
                    allres[n].append(r); wr[n] = r
                minp = min(Lo[1:])
                wrows.append([win[0]["date"], fpx(L1), fpx(C[-1]), fp(C[-1] / L1 - 1, 0), fp(minp / L1 - 1, 0),
                              "%.0f%%" % (100 * vol), "%.0f%%" % (100 * fapr), wr["Spot ladder"]["filled"]] +
                             [fp(wr[n]["pnl"], 0) + (" W" if "WIPED" in wr[n]["flag"] else "") +
                              (" L" if "LIQ" in wr[n]["flag"] else "") for n in names])
            summ[srcname] = allres
            if srcname == "spot":
                print(md(["Start", "L1", "End price (d180)", "End vs L1", "Min low vs L1", "Realized vol", "Funding APR (HL)", "Fills"] +
                         [short[n] for n in names], wrows))
                print("\n(W = x-token wiped out; L = perp partially/fully liquidated. P&L on the whole $4,000 incl. idle USDC.)\n")
        srows = []
        for n in names:
            rs, rp = summ["spot"][n], summ["perp"][n]
            pn, pp = [r["pnl"] for r in rs], [r["pnl"] for r in rp]
            srows.append([n, fp(st.median(pn)), fp(st.mean(pn)), fp(min(pn)), fp(max(pn)),
                          "%.0f%%" % (100 * sum(1 for x in pn if x < 0) / len(pn)),
                          "%d/%d" % (sum(1 for r in rs if r["flag"]), len(rs)),
                          "%.1f%%" % (100 * st.median([r["mdd"] for r in rs])), "%.1f%%" % (100 * max(r["mdd"] for r in rs)),
                          fp(st.median(pp)), "%d/%d" % (sum(1 for r in rp if r["flag"]), len(rp))])
        print(md(["Option", "Median P&L", "Mean P&L", "Worst", "Best", "% windows losing", "Liq/wipe windows",
                  "Median max DD", "Worst max DD", "Median P&L (perp prices)", "Liq/wipe (perp prices)"], srows))
        frows = []
        for lev, interp in ((2, "A"), (3, "A"), (2, "B")):
            pn_flat, nliq = [], 0
            for s in starts:
                win = rowsd[s:s + 181]
                if any(r["sc"] is None for r in win): continue
                L1 = win[0]["sc"]; L = [L1, 0.875 * L1, 0.75 * L1]
                bars_flat = [(r["date"], r["so"], r["sl"], r["sc"], P.FUND_BASE_APR / 365) for r in win]
                rr = run(Perp(lev, interp), bars_flat, L)
                pn_flat.append(rr["pnl"]); nliq += 1 if rr["flag"] else 0
            frows.append(["Perp A %dx" % lev if interp == "A" else "Perp B", fp(st.median(pn_flat)), fp(st.mean(pn_flat)),
                          "%d/%d" % (nliq, len(pn_flat))])
        print("\nPerps with a flat 11% APR funding (spot prices) instead of Hyperliquid historical funding:\n")
        print(md(["Option", "Median P&L", "Mean P&L", "Liq windows"], frows))

if __name__ == "__main__":
    main()
