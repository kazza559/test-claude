import math, datetime
# ---------- INPUTS (2026-09-29 snapshot) ----------
YT_SPOT=0.032912        # USD per YT (1 YT = yield on $1 principal)
DAYS=103.28             # to 2027-01-10 13:00 UTC
T=DAYS/365
FEE=0.055               # Exponent fee on YT yield
NAV=1.15055451
tickets={1000:0.03300,10000:0.03356,50000:0.0359}  # avg fill price from on-chain sim
P0=240.898e9            # total points 2026-09-29
D0=1.3244e9             # points/day steady state
def pts_total(date, g_month):
    """cumulative points at date, daily issuance growing g per month (compounded daily)"""
    n=(datetime.date.fromisoformat(date)-datetime.date(2026,9,29)).days
    if g_month==0: return P0+D0*n
    r=(1+g_month)**(12/365)-1
    return P0+D0*((1+r)**n-1)/r
for d in ['2026-12-31','2027-01-10','2027-03-31','2027-06-30','2027-09-30']:
    print(d,[round(pts_total(d,g)/1e9) for g in (0,0.03,0.08)], 'at 1.68B/d flat', round((P0+1.68e9*(datetime.date.fromisoformat(d)-datetime.date(2026,9,29)).days)/1e9))
def net_yield(apy): return ((1+apy)**T-1)*(1-FEE)
print('\nnet yield per YT', {a:round(net_yield(a),6) for a in (0.09,0.10,0.1102,0.1136,0.1255)})
print('\n== per-ticket economics (USD-exposure basis) ==')
for tk,px in tickets.items():
    n_yt=tk/px
    for apy in (0.1102,0.10):
        ny=n_yt*net_yield(apy); cost=tk-ny
        for m in (8,5):
            pts=n_yt*m*DAYS
            print(f"ticket ${tk:>6} APY {apy:.4f} m={m}: YT={n_yt:,.0f} yield_back=${ny:,.0f} net_cost=${cost:,.0f} ({cost/tk*100:.1f}%) pts={pts/1e6:,.2f}M  BE=${cost/pts*1e6:.2f}/1M pts  pts/$/day={m/px:.1f}")
# ---------- scenarios ----------
sc={
 'Bull': dict(snap='2026-12-31', g=0.00, fdv=350e6, A=0.07, h=0.20, p=0.10),
 'Base': dict(snap='2027-03-31', g=0.03, fdv=200e6, A=0.05, h=0.30, p=0.35),
 'Bear': dict(snap='2027-06-30', g=0.08, fdv=100e6, A=0.03, h=0.40, p=0.25),
 'Zero': dict(snap=None, p=0.30),
}
print('\n== scenario value per point ==')
vals={}
for k,s in sc.items():
    if s.get('snap') is None: vals[k]=0; print(k,'value 0'); continue
    P=pts_total(s['snap'],s['g'])
    v=s['fdv']*s['A']*(1-s['h'])/P
    vals[k]=v
    print(f"{k}: snapshot {s['snap']} P={P/1e9:.0f}B pool=${s['fdv']*s['A']/1e6:.1f}M after haircut ${s['fdv']*s['A']*(1-s['h'])/1e6:.2f}M -> ${v*1e6:.2f} per 1M pts")
print('\n== P&L per ticket by scenario (APY 11.02%) ==')
for tk,px in tickets.items():
    n_yt=tk/px; ny=n_yt*net_yield(0.1102)
    for m in (8,5):
        # bull snapshot before maturity -> points only to 2026-12-31
        out=[]; ev=0
        for k,s in sc.items():
            days=DAYS
            if s.get('snap')=='2026-12-31': days=(datetime.datetime(2026,12,31)-datetime.datetime(2026,9,29,6)).total_seconds()/86400
            pts=n_yt*m*days
            val=pts*vals[k]
            pnl=val+ny-tk
            ev+=s['p']*pnl
            out.append(f"{k}: airdrop ${val:,.0f} PnL ${pnl:,.0f} ({pnl/tk*100:+.0f}%)")
        print(f"${tk} m={m}: "+' | '.join(out)+f" || EV ${ev:,.0f} ({ev/tk*100:+.1f}%)")
# ---------- sensitivity grid: $ per 1M pts (pre-haircut) ----------
print('\n== $ per 1M points, pre-haircut ==')
Ps=[364e9,483e9,606e9,767e9]
for fdv in (80e6,100e6,150e6,200e6,300e6,400e6,500e6):
    for A in (0.03,0.05,0.07):
        print(f"FDV {fdv/1e6:.0f}M A {A*100:.0f}%: "+'  '.join(f"{fdv*A/P*1e6:6.1f}" for P in Ps))
# ---------- breakeven FDV ----------
print('\n== breakeven FDV (net cost only, $1k ticket, APY 11.02%) ==')
for m,be in ((8,None),(5,None)):
    px=tickets[1000]; n_yt=1000/px; cost=1000-n_yt*net_yield(0.1102); pts=n_yt*m*DAYS; BE=cost/pts
    for P in Ps:
        for A,h in ((0.05,0.30),(0.03,0.40),(0.07,0.20)):
            print(f"m={m} P={P/1e9:.0f}B A={A} h={h}: FDV_BE=${BE*P/(A*(1-h))/1e6:.0f}M")
# ---- market-implied FDV from YT price
BEspot=(YT_SPOT-net_yield(0.1102))/(8*DAYS)
print('\nmarket-implied $/1M pts at spot 8x', BEspot*1e6)
for P in (377e9,506e9):
    print('implied pool after haircut', BEspot*P/1e6, 'M ; implied FDV at 5%/30%', BEspot*P/(0.05*0.7)/1e6)
# opportunity cost
print('\nopp cost $1k at 11% avg outstanding', ((1000+140)/2)*0.1102*T, ' full', 1000*0.1102*T)

print('\n== EV grid ($1k & $10k tickets) ==')
for tk in (1000,10000):
    px=tickets[tk]; n_yt=tk/px
    for apy in (0.1102,0.10):
        ny=n_yt*net_yield(apy)
        for m in (8,5):
            for elig in (1.0,0.7):
                ev=0
                for k,s in sc.items():
                    days=DAYS
                    if s.get('snap')=='2026-12-31': days=(datetime.datetime(2026,12,31)-datetime.datetime(2026,9,29,6)).total_seconds()/86400
                    val=n_yt*m*days*vals[k]*elig
                    ev+=s['p']*(val+ny-tk)
                print(f"tk {tk} APY {apy} m {m} elig {elig}: EV ${ev:,.0f} ({ev/tk*100:+.1f}%)")
# historical-median comp upside: $0.44 per $1k TVL-day
tvl_days=53.4e9+183*290e6
pool=0.44*tvl_days/1000
print('\nhist median pool',pool/1e6,'M; per 1M pts at 506B',pool/506e9*1e6, '; $1k YT value', 25.04e6*pool/506e9)
print('base pool per $1k TVL-day', 10e6/(tvl_days/1000), 'APR eq', 10e6/290e6/(0.5+183/365)*100)
tvl_days_dec=53.4e9+93*290e6
print('bull pool per $1k-day', 24.5e6/(tvl_days_dec/1000))
# cat tail: NAV shock after 50 days, yield stops
n_yt=1000/0.033
earned=n_yt*((1.1102)**(50/365)-1)*(1-FEE)
print('cat after 50d: yield kept',earned,'loss',1000-earned)
print('share of points at maturity for $1k 8x', 25.04e6/377e9*100,'%')
print('cost per point-day now vs launch', 0.032912/103.28, 0.0556/138.5)
