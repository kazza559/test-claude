"""
Re Protocol (re.xyz) - Season 2 Pendle YT EV model.
Snapshot data: 2026-09-28 (Re public API, Pendle API, CoinGecko/DefiLlama).
Run: python3 yt_model.py
"""
from itertools import product

# ---------- Snapshot inputs (2026-09-28) ----------
S2_POINTS_SO_FAR = 686.85e9        # api.re.xyz leaderboard, snapshot 2026-09-27
DAILY_POINTS_NOW = 9.622e9         # api.re.xyz /public/opportunities (2026-09-27)
DAYS_TO_MATURITY = 72.5            # 2026-09-28 11:00 UTC -> 2026-12-10 00:00 UTC
DAYS_TO_DEC1 = 63.5
RE_PRICE_NOW = 0.46                # FDV ~ $460M
PENDLE_YIELD_FEE = 0.05            # Pendle takes 5% of YT yield

MARKETS = {
    # name: (yt_mid_price_usd, empirical pts per YT per day, nominal multiplier, underlying APY base, bear APY)
    "YT-reUSD 10DEC2026":  dict(px=0.021506, pts_emp=32.53, mult=30, apy=0.0675, apy_bear=0.060),
    "YT-reUSDe 10DEC2026": dict(px=0.033441, pts_emp=43.45, mult=40, apy=0.1200, apy_bear=0.100),
}
# Real Pendle SDK quotes (USDC in) -> effective price per YT
QUOTES = {
    "YT-reUSD 10DEC2026":  {1_000: 0.021989, 10_000: 0.022255, 50_000: 0.024110, 100_000: 0.025767},
    "YT-reUSDe 10DEC2026": {1_000: 0.034363, 10_000: 0.034825},
}

# ---------- Scenarios ----------
SCEN = {
    #            alloc(RE)  RE price  S2 total pts  days counted   pts/YT basis  realization(big wallet vested part)
    "Bull":      dict(alloc=45e6, p=0.55, T=1.30e12, days=DAYS_TO_MATURITY, emp=True,  vest_disc=0.70, apy="apy"),
    "Base":      dict(alloc=35e6, p=0.35, T=1.55e12, days=DAYS_TO_MATURITY, emp=True,  vest_disc=0.50, apy="apy"),
    "Bear":      dict(alloc=35e6, p=0.22, T=2.00e12, days=DAYS_TO_DEC1,     emp=False, vest_disc=0.35, apy="apy_bear"),
    "Super-bear":dict(alloc=35e6, p=0.15, T=2.50e12, days=DAYS_TO_DEC1,     emp=False, vest_disc=0.25, apy="apy_bear"),
}

def immediate_fraction(points):
    """S1 rule (assumed to carry over to S2): <=150M pts fully liquid, else (135M + 10% * total)/total."""
    if points <= 150e6:
        return 1.0
    return (135e6 + 0.10 * points) / points

def run(market, usd_in, scen_name, referral=False):
    m, s = MARKETS[market], SCEN[scen_name]
    px = QUOTES[market].get(usd_in, m["px"] * 1.03)
    n_yt = usd_in / px
    pts_day_per_yt = (m["pts_emp"] if s["emp"] else m["mult"]) * (1.06 if referral else 1.0)
    pts = n_yt * pts_day_per_yt * s["days"]
    yield_back = n_yt * m[s["apy"]] * (DAYS_TO_MATURITY / 365) * (1 - PENDLE_YIELD_FEE)
    usd_per_pt = s["alloc"] * s["p"] / s["T"]
    imm = immediate_fraction(pts)
    realization = imm + (1 - imm) * s["vest_disc"]
    airdrop = pts * usd_per_pt * realization
    total_back = yield_back + airdrop
    return dict(n_yt=n_yt, px=px, pts=pts, pts_day=n_yt * pts_day_per_yt, yield_back=yield_back,
                net_cost=usd_in - yield_back, usd_per_B=usd_per_pt * 1e9, imm=imm, realization=realization,
                airdrop=airdrop, total_back=total_back, pnl=total_back - usd_in, roi=(total_back / usd_in - 1))

if __name__ == "__main__":
    print("=== S2 point-supply projection ===")
    for name, s in SCEN.items():
        print(f"{name:11} T={s['T']/1e12:.2f}T  -> $/1B pts = {s['alloc']*s['p']/s['T']*1e9:,.0f}  (RE {s['p']}, alloc {s['alloc']/1e6:.0f}M)")
    print("\n=== Position table ===")
    for market in MARKETS:
        for usd_in in QUOTES[market]:
            for sc in SCEN:
                r = run(market, usd_in, sc)
                print(f"{market:20} ${usd_in:>7,} {sc:10} YT={r['n_yt']:>11,.0f} px={r['px']:.5f} pts/day={r['pts_day']/1e6:7.2f}M "
                      f"pts={r['pts']/1e6:8.1f}M yield_back=${r['yield_back']:>8,.0f} net_cost=${r['net_cost']:>8,.0f} "
                      f"$/B={r['usd_per_B']:>6,.0f} liquid%={r['imm']*100:5.1f} real%={r['realization']*100:5.1f} "
                      f"airdrop=${r['airdrop']:>8,.0f} ROI={r['roi']*100:+6.1f}%")
            print()
    print("=== Break-even RE FDV (Base T=1.55T, reUSD YT, $1k, no vesting) ===")
    r = run("YT-reUSD 10DEC2026", 1_000, "Base")
    need_per_pt = r["net_cost"] / r["pts"]
    for T in (1.3e12, 1.55e12, 2.0e12, 2.5e12):
        for alloc in (35e6, 45e6):
            print(f"T={T/1e12:.2f}T alloc={alloc/1e6:.0f}M -> break-even RE = ${need_per_pt*T/alloc:.3f} (FDV ${need_per_pt*T/alloc*1e3:.0f}M)")
    print("\n=== ROI grid: YT-reUSD $1k (liquid, no vesting), days=72.5, emp pts, base APY ===")
    prices = (0.15, 0.22, 0.30, 0.35, 0.46, 0.60)
    print("T \\ RE px " + "".join(f"{p:>9}" for p in prices))
    for T in (1.3e12, 1.55e12, 1.8e12, 2.0e12, 2.5e12):
        row = []
        for p in prices:
            SCEN["_g"] = dict(alloc=35e6, p=p, T=T, days=DAYS_TO_MATURITY, emp=True, vest_disc=0.5, apy="apy")
            row.append(run("YT-reUSD 10DEC2026", 1_000, "_g")["roi"] * 100)
        print(f"{T/1e12:>5.2f}T    " + "".join(f"{x:>+8.0f}%" for x in row))
    print("\n=== ROI grid: YT-reUSD $10k (vesting applies), days=72.5 ===")
    print("T \\ RE px " + "".join(f"{p:>9}" for p in prices))
    for T in (1.3e12, 1.55e12, 1.8e12, 2.0e12, 2.5e12):
        row = []
        for p in prices:
            SCEN["_g"] = dict(alloc=35e6, p=p, T=T, days=DAYS_TO_MATURITY, emp=True, vest_disc=0.5, apy="apy")
            row.append(run("YT-reUSD 10DEC2026", 10_000, "_g")["roi"] * 100)
        print(f"{T/1e12:>5.2f}T    " + "".join(f"{x:>+8.0f}%" for x in row))
