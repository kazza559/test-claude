# Hyperliquid quant screen: relative strength, beta, funding regimes and crash-wick risk (snapshot 2026-10-17 03:23 UTC)

Snapshot: `metaAndAssetCtxs` / `spotMetaAndAssetCtxs` fetched **2026-10-17 03:23:08 UTC**. Candles fetched 03:23–03:30 UTC; the last hourly candle opened 03:00 UTC, so "now" means the latest trade, about 03:25 UTC. Everything below is computed from the Hyperliquid public info API (`POST https://api.hyperliquid.xyz/info`). No OKX fallback was needed. Scripts (01_snapshot.py … 06_report.py), raw downloads (data/) and the machine-readable per-coin file are under `/tmp/claude-0/-home-user-test-claude/8ec8a334-85ed-54af-babc-62d7e4c0704b/scratchpad/research/hl_screen/`. The per-coin file is `summary.json`, with 52 coins and every metric below.

## Q1. Universe and market snapshot (OI ≥ $10M perps + watchlist + KNTQ spot)

### Takeaway
51 main-dex perps have OI notional ≥ $10M. All seven must-include coins clear the bar on their own. KNTQ trades on HL spot as **@334 (KNTQ/USDC)**, which confirms the earlier pair id. After ETH, the largest OI is in HYPE ($1.59B), SOL ($568M), ZEC ($534M) and NEAR ($313M). At the snapshot, 33 of the 51 perps were paying exactly HL's default funding of 0.00125%/h (10.95% APR).

### Cited Findings
- **Market count:** the main perp dex lists 234 perps, 56 of them flagged delisted. **51** non-delisted perps have openInterest × markPx ≥ $10M — [HL API metaAndAssetCtxs](https://api.hyperliquid.xyz/info)
- **Watchlist OI is above the threshold in every case:** BNB $45.7M, LINK $60.9M, LIT $132.6M — [HL API metaAndAssetCtxs](https://api.hyperliquid.xyz/info)
- **Largest OI:**

  | Coin | OI notional |
  |---|---|
  | BTC | $3,353M |
  | ETH | $2,604M |
  | HYPE | $1,589M |
  | SOL | $568M |
  | ZEC | $534M |
  | NEAR | $313M |
  | XRP | $232M |
  | PUMP | $174M |
  | LIT | $133M |
  | DOGE | $98M |
  | ENA | $98M |

  [HL API metaAndAssetCtxs](https://api.hyperliquid.xyz/info)
- **BTC price check:** BTC markPx was **$81,494**, consistent with the premise (≈ $81,450) — [HL API metaAndAssetCtxs](https://api.hyperliquid.xyz/info)
- **KNTQ has two spot pairs:**
  - **@334 KNTQ/USDC:** mark 0.3113, mid 0.3114, 24h volume $1.67M. This is the active pair.
  - **@254 KNTQ/USDH:** mark 0.207, 24h volume $0.

  The API reports circulatingSupply = 999,999,999 (equal to total supply), so the implied cap of ≈ $311M is fully diluted, not float — [HL API spotMetaAndAssetCtxs](https://api.hyperliquid.xyz/info)
- **Technical pitfall:** in `spotMetaAndAssetCtxs`, the asset-context array is **not** positionally aligned with `universe` (261 of 1,117 rows mismatched). Contexts must be joined on their `coin` field. A naive zip mislabels @334 with another pair's price (35.95). — [HL API spotMetaAndAssetCtxs](https://api.hyperliquid.xyz/info)
- **Funding at the snapshot:**
  - **Default rate:** 33 of 51 universe perps were at exactly 0.0000125/h = 10.95% APR.
  - **Negative funding:** SOL −0.39%, LIT −13.59%, AAVE −2.31%, MON −9.07%, ADA −3.26%, ARB −35.33%, JUP −11.82% (APR).
  - **Others:** ETH 1.86%, HYPE 7.41%, BNB 7.47%, LINK 0.25%.

  [HL API metaAndAssetCtxs](https://api.hyperliquid.xyz/info)
- **Max leverage:**
  - BTC 40x, ETH 25x, SOL/XRP 20x, HYPE/BNB/LINK 10x.
  - LIT 5x.
  - Several trend coins are capped at 3x: VVV, AERO, GRASS, PONS, CASHCAT, PURR.

  [HL API metaAndAssetCtxs](https://api.hyperliquid.xyz/info)
- **Full universe snapshot** (sorted by OI; funding is the current hourly rate; "daily from" = first HL daily candle in a request starting 2023-01-01) — [HL API metaAndAssetCtxs / candleSnapshot](https://api.hyperliquid.xyz/info):

| Coin | Market | Mark px | OI $M | 24h vol $M | Funding /h | Funding APR | Max lev | Daily history from |
|---|---|---|---|---|---|---|---|---|
| BTC | perp | 81,494 | 3,353.3 | 2,840.6 | 0.00130% | 10.95% | 40x | 2023-01-01 |
| ETH | perp | 2,424 | 2,603.6 | 982.0 | 0.00020% | 1.86% | 25x | 2023-01-01 |
| HYPE | perp | 79.92 | 1,588.6 | 314.4 | 0.00080% | 7.41% | 10x | 2024-12-05 |
| SOL | perp | 104.62 | 568.1 | 325.6 | -0.00000% | -0.39% | 20x | 2023-01-01 |
| ZEC | perp | 1,151 | 534.0 | 299.3 | 0.00130% | 10.95% | 10x | 2023-01-07 |
| NEAR | perp | 5.071 | 313.3 | 173.5 | 0.00130% | 10.95% | 10x | 2023-01-01 |
| XRP | perp | 1.306 | 232.4 | 59.9 | 0.00000% | 0.24% | 20x | 2023-01-01 |
| PUMP | perp | 0.004612 | 174.4 | 115.4 | 0.00130% | 10.95% | 10x | 2025-07-10 |
| LIT | perp | 3.201 | 132.6 | 22.4 | -0.00160% | -13.59% | 5x | 2025-12-22 |
| DOGE | perp | 0.08018 | 98.4 | 4.6 | 0.00130% | 10.95% | 10x | 2023-01-01 |
| ENA | perp | 0.198 | 98.2 | 37.8 | 0.00040% | 3.71% | 10x | 2024-04-02 |
| WLD | perp | 0.5222 | 72.2 | 65.3 | 0.00130% | 10.95% | 10x | 2023-07-24 |
| ZRO | perp | 1.965 | 72.2 | 31.2 | 0.00130% | 10.95% | 5x | 2023-09-07 |
| UNI | perp | 7.289 | 68.6 | 13.3 | 0.00130% | 10.95% | 10x | 2023-01-01 |
| VVV | perp | 23.01 | 65.0 | 11.1 | 0.00130% | 10.95% | 3x | 2025-01-28 |
| XMR | perp | 555.95 | 64.6 | 22.3 | 0.00130% | 10.95% | 5x | 2023-04-22 |
| SUI | perp | 1.008 | 61.7 | 15.8 | 0.00130% | 10.95% | 10x | 2023-05-03 |
| AAVE | perp | 155.22 | 61.7 | 9.1 | -0.00030% | -2.31% | 10x | 2023-01-01 |
| XPL | perp | 0.08189 | 61.5 | 12.8 | 0.00130% | 10.95% | 10x | 2025-08-22 |
| LINK | perp | 12.31 | 60.9 | 6.5 | 0.00000% | 0.25% | 10x | 2023-01-01 |
| TAO | perp | 275.05 | 50.2 | 12.8 | 0.00130% | 10.95% | 5x | 2024-02-19 |
| STRK | perp | 0.07021 | 48.1 | 33.1 | 0.00130% | 10.95% | 5x | 2024-02-14 |
| BNB | perp | 721.07 | 45.7 | 3.0 | 0.00090% | 7.47% | 10x | 2023-01-01 |
| ONDO | perp | 0.4539 | 37.1 | 11.1 | 0.00120% | 10.11% | 10x | 2024-01-20 |
| MON | perp | 0.02271 | 37.1 | 2.5 | -0.00100% | -9.07% | 5x | 2025-10-08 |
| FARTCOIN | perp | 0.1528 | 36.4 | 6.5 | 0.00130% | 10.95% | 10x | 2024-12-20 |
| AERO | perp | 0.8804 | 34.1 | 6.5 | 0.00130% | 10.95% | 3x | 2024-12-04 |
| ADA | perp | 0.2243 | 34.0 | 3.6 | -0.00040% | -3.26% | 10x | 2023-01-01 |
| GRASS | perp | 0.6301 | 29.9 | 2.4 | 0.00130% | 10.95% | 3x | 2024-10-28 |
| PONS | perp | 0.3206 | 29.5 | 6.8 | 0.00130% | 10.95% | 3x | 2026-08-31 |
| GRAM | perp | 1.351 | 27.3 | 1.6 | 0.00130% | 10.95% | 5x | 2026-07-02 |
| LTC | perp | 59.76 | 26.2 | 2.3 | 0.00130% | 10.95% | 10x | 2023-01-01 |
| kPEPE | perp | 0.00401 | 26.1 | 26.0 | 0.00060% | 5.31% | 10x | 2023-05-05 |
| ASTER | perp | 0.7052 | 24.1 | 2.0 | 0.00130% | 10.95% | 5x | 2025-09-19 |
| CASHCAT | perp | 0.11 | 23.5 | 7.8 | 0.00130% | 10.95% | 3x | 2026-07-11 |
| PAXG | perp | 4,165 | 22.4 | 3.1 | 0.00130% | 10.95% | 10x | 2025-03-27 |
| AVAX | perp | 9.971 | 22.0 | 4.6 | 0.00030% | 2.27% | 10x | 2023-01-01 |
| ARB | perp | 0.1888 | 19.3 | 19.6 | -0.00400% | -35.33% | 10x | 2023-03-23 |
| CRV | perp | 0.3438 | 18.1 | 8.3 | 0.00030% | 2.80% | 10x | 2023-01-01 |
| TIA | perp | 0.712 | 16.9 | 26.2 | 0.00130% | 10.95% | 5x | 2023-10-19 |
| XLM | perp | 0.18 | 13.2 | 1.4 | 0.00130% | 10.95% | 5x | 2023-01-01 |
| HBAR | perp | 0.08403 | 13.1 | 1.3 | 0.00130% | 10.95% | 5x | 2023-01-01 |
| TRX | perp | 0.3356 | 12.6 | 1.5 | 0.00130% | 10.95% | 10x | 2023-01-01 |
| ETHFI | perp | 0.6899 | 11.4 | 2.5 | 0.00130% | 10.95% | 5x | 2024-03-18 |
| FIL | perp | 1.151 | 11.4 | 4.7 | 0.00130% | 10.95% | 5x | 2023-01-01 |
| FET | perp | 0.1946 | 10.9 | 1.9 | 0.00130% | 10.95% | 5x | 2023-01-17 |
| PENDLE | perp | 2.106 | 10.5 | 1.5 | 0.00130% | 10.95% | 5x | 2023-07-28 |
| WLFI | perp | 0.05695 | 10.4 | 0.4 | 0.00090% | 8.15% | 5x | 2025-08-23 |
| PURR | perp | 0.0987 | 10.4 | 1.1 | 0.00130% | 10.95% | 3x | 2024-11-04 |
| JUP | perp | 0.3025 | 10.2 | 3.0 | -0.00130% | -11.82% | 10x | 2023-12-03 |
| LDO | perp | 0.3988 | 10.1 | 1.7 | 0.00130% | 10.95% | 5x | 2023-01-01 |
| KNTQ | spot @334 | 0.3113 | n/a | 1.7 | spot | spot | spot | 2026-05-20 |

### Inferences
- **Default funding:** 10.95% APR equals 0.01% per 8h. It is the interest-rate component of HL's documented funding formula, which applies when the premium is small ([HL docs: funding](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/funding); mechanism not re-fetched this session). In practice, a 2x perp long in a quiet market costs about 0.9% of notional, or 1.8% of equity, per 30 days.
- **HL liquidity for BNB and LINK is thin relative to OI:** 24h volume was $3.0M (BNB) and $6.5M (LINK) against $45.7M and $60.9M OI. KNTQ's only liquid venue on HL is the @334 spot book at about $1.7M/day. Size and slippage matter even for a ~$6.4K account if orders are placed in a burst.

### Gaps
- HIP-3 builder-deployed perp dexes were not queried; the universe is the main dex only.
- KNTQ's true circulating float is not available from this endpoint.

## Q2. Relative strength vs BTC since the July 2026 low and through the current pullback

### Takeaway
BTC anchors on HL match the premise:

| Point | Date and hour (UTC) | BTC price |
|---|---|---|
| Cycle low | 2026-07-01 01:00 | $57,768 |
| Higher low | 2026-08-01 18:00 | $62,237 |
| First-leg top | 2026-09-21 20:00 | $87,471 |
| Retest | 2026-10-02 | $87,235 |
| Now | 2026-10-17 | $81,499 (−6.4% from the top) |

- **RS leaders since the August low:** KNTQ (spot), NEAR, STRK, CASHCAT, ZRO, ZEC, ENA, ARB, TIA and PUMP (top 10 by coin/BTC ratio). Of these, NEAR, STRK, ZRO, TIA and PUMP also rose during the pullback. KNTQ fell only 3% and ENA moved in line with BTC.
- **Watchlist:**
  - LINK is the only perp that beat BTC in the rally (+19% vs BTC since the August low) and kept pace in the pullback.
  - LIT, HYPE and SOL beat BTC in the rally but are giving it back in the pullback.
  - BNB lags.

### Cited Findings
- **BTC anchors** (HL BTC perp, hourly candles; the hour shown is the candle open time) — [HL API candleSnapshot 1h](https://api.hyperliquid.xyz/info):

  | Anchor | Hour (UTC) | Extreme | Hourly close (used for returns) |
  |---|---|---|---|
  | July low | 2026-07-01 01:00 | low $57,768 | $58,739 |
  | August low | 2026-08-01 18:00 | low $62,237 | $62,550 |
  | Leg top | 2026-09-21 20:00 | high $87,471 | $87,047 |
  | Retest | 2026-10-02 12:00 | high $87,235 | $86,801 |

  Two reference highs from daily candles: the high since 2023 is **$126,297 (2025-10-06)** and the 2026 high is **$97,949 (2026-01-14)** — [HL API candleSnapshot 1d](https://api.hyperliquid.xyz/info)
- **BTC returns to now ($81,499):**

  | Window | BTC return |
  |---|---|
  | Since July low | +38.7% |
  | Since August low | +30.3% |
  | August low → leg top | +39.2% |
  | Leg top → now | −6.4% |
  | Retest → now | −6.1% |
  | 7d | −1.3% |
  | 30d | +6.7% |
  | From 2023+ high | −35.5% |
  | From 2026 high | −16.8% |

  [HL API candleSnapshot](https://api.hyperliquid.xyz/info)
- **Method:** each coin's return is measured from its own hourly close at BTC's extreme hour. "vs BTC (diff)" = coin return − BTC return. "vs BTC (ratio)" = (1+coin)/(1+BTC) − 1, i.e. the coin/BTC pair return. Fifty coins have data at the August-low hour; PONS listed 2026-08-31 and is excluded from the ranking. GRAM and CASHCAT listed after the July low, so they have no since-July value.
- **Table (a), RS leaderboard:** top 25 by return vs BTC since the August low, then BTC and watchlist coins outside the top 25 with their overall rank. "Pullback resid vs β" = log(1 + leg-top→now move) − β × log(1 + BTC move); it is positive when the coin did better in the pullback than its beta implies — [HL API candleSnapshot 1h/1d + metaAndAssetCtxs](https://api.hyperliquid.xyz/info):

| # | Coin | Price | OI $M | 24h vol $M | Since Jul low | Since Aug low | vs BTC since Aug (diff) | vs BTC since Aug (ratio) | Aug low→Top | Top→Now (pullback) | Pullback vs BTC (ratio) | 7d | 30d | From 2026 high | β (1h) | Pullback resid vs β |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | KNTQ (spot @334) | 0.3128 | n/a | 1.7 | +97.8% | +244.1% | +213.8% | +164.1% | +255.3% | -3.2% | +3.4% | +8.0% | +56.1% | -31.4% | 0.66 | +1.2% |
| 2 | NEAR | 5.079 | 313.3 | 173.5 | +186.2% | +206.1% | +175.8% | +134.9% | +145.9% | +24.5% | +32.9% | +2.6% | +88.2% | -15.5% | 1.53 | +31.9% |
| 3 | STRK | 0.07041 | 48.1 | 33.1 | +143.2% | +183.8% | +153.5% | +117.8% | +78.3% | +59.2% | +70.0% | -4.9% | +149.1% | -44.6% | 1.38 | +55.6% |
| 4 | CASHCAT | 0.1104 | 23.5 | 7.8 | n/a | +173.5% | +143.3% | +109.9% | +346.3% | -38.7% | -34.5% | -4.7% | -42.5% | -65.3% | 3.08 | -28.6% |
| 5 | ZRO | 1.964 | 72.2 | 31.2 | +137.1% | +171.8% | +141.5% | +108.6% | +63.3% | +66.4% | +77.7% | +0.3% | +93.9% | -24.0% | 1.20 | +58.9% |
| 6 | ZEC | 1,151 | 534.0 | 299.3 | +190.5% | +148.4% | +118.1% | +90.7% | +214.0% | -20.9% | -15.5% | -5.3% | -16.5% | -32.1% | 1.50 | -13.6% |
| 7 | ENA | 0.1983 | 98.2 | 37.8 | +175.9% | +146.5% | +116.2% | +89.2% | +162.4% | -6.1% | +0.3% | -9.4% | +31.1% | -32.7% | 1.69 | +4.9% |
| 8 | ARB | 0.1892 | 19.3 | 19.6 | +147.1% | +142.8% | +112.5% | +86.3% | +185.3% | -14.9% | -9.1% | +3.2% | +14.2% | -26.1% | 1.49 | -6.3% |
| 9 | TIA | 0.7395 | 16.9 | 26.2 | +109.6% | +132.3% | +102.0% | +78.3% | +35.3% | +71.6% | +83.3% | +55.3% | +112.9% | -3.3% | 1.39 | +63.2% |
| 10 | PUMP | 0.00461 | 174.4 | 115.4 | +231.4% | +122.6% | +92.3% | +70.8% | +109.3% | +6.4% | +13.6% | -15.2% | +20.3% | -32.4% | 1.51 | +16.1% |
| 11 | AERO | 0.8833 | 34.1 | 6.5 | +84.2% | +118.8% | +88.5% | +67.9% | +70.5% | +28.3% | +37.0% | +9.3% | +60.4% | -11.2% | 1.57 | +35.2% |
| 12 | GRASS | 0.6311 | 29.9 | 2.4 | +35.2% | +106.2% | +75.9% | +58.3% | +41.4% | +45.9% | +55.8% | -3.2% | +90.1% | -29.2% | 1.39 | +46.9% |
| 13 | VVV | 23.05 | 65.0 | 11.1 | +86.3% | +95.6% | +65.3% | +50.1% | +164.7% | -26.1% | -21.1% | +3.2% | -7.2% | -33.6% | 1.49 | -20.5% |
| 14 | UNI | 7.296 | 68.6 | 13.3 | +161.0% | +79.3% | +49.0% | +37.6% | +117.2% | -17.4% | -11.8% | -0.6% | +7.4% | -33.4% | 1.50 | -9.3% |
| 15 | ETHFI | 0.6937 | 11.4 | 2.5 | +117.2% | +76.9% | +46.6% | +35.8% | +85.4% | -4.6% | +1.9% | +3.1% | +16.3% | -16.6% | 1.44 | +4.8% |
| 16 | WLD | 0.5234 | 72.2 | 65.3 | +28.5% | +73.7% | +43.4% | +33.3% | +54.1% | +12.7% | +20.4% | +0.4% | +40.5% | -27.8% | 1.56 | +22.2% |
| 17 | AAVE | 155.61 | 61.7 | 9.1 | +80.7% | +73.2% | +42.9% | +32.9% | +62.7% | +6.5% | +13.7% | -9.0% | +27.8% | -17.1% | 1.30 | +14.8% |
| 18 | CRV | 0.3453 | 18.1 | 8.3 | +86.4% | +72.3% | +42.0% | +32.2% | +82.4% | -5.5% | +0.9% | -3.4% | +7.5% | -24.6% | 1.15 | +1.9% |
| 19 | PURR | 0.09874 | 10.4 | 1.1 | +15.2% | +67.2% | +36.9% | +28.3% | +114.3% | -22.0% | -16.7% | -13.6% | -6.2% | -46.3% | 1.62 | -14.1% |
| 20 | FIL | 1.161 | 11.4 | 4.7 | +61.8% | +66.9% | +36.6% | +28.1% | +39.9% | +19.3% | +27.4% | -3.0% | +45.1% | -31.1% | 1.25 | +25.9% |
| 21 | AVAX | 9.989 | 22.0 | 4.6 | +52.1% | +63.8% | +33.5% | +25.7% | +82.9% | -10.4% | -4.3% | -3.9% | +32.4% | -33.2% | 1.24 | -2.9% |
| 22 | JUP | 0.3037 | 10.2 | 3.0 | +43.5% | +60.8% | +30.5% | +23.4% | +57.9% | +1.8% | +8.8% | -18.2% | +39.4% | -21.7% | 1.50 | +11.7% |
| 23 | LIT | 3.204 | 132.6 | 22.4 | +74.8% | +58.2% | +27.9% | +21.4% | +135.6% | -32.9% | -28.3% | -9.8% | -33.9% | -42.6% | 1.38 | -30.8% |
| 24 | LINK | 12.35 | 60.9 | 6.5 | +71.2% | +55.1% | +24.8% | +19.0% | +65.5% | -6.3% | +0.1% | -3.6% | +10.9% | -21.8% | 1.31 | +2.1% |
| 25 | PENDLE | 2.118 | 10.5 | 1.5 | +60.2% | +54.3% | +24.0% | +18.4% | +84.2% | -16.2% | -10.5% | -0.3% | -7.0% | -24.4% | 1.45 | -8.1% |
| ref | BTC | 81,499 | 3,353.3 | 2,840.6 | +38.7% | +30.3% | +0.0% | +0.0% | +39.2% | -6.4% | +0.0% | -1.3% | +6.7% | -16.8% | 1.00 | +0.0% |
| 29 (watchlist) | SOL | 104.68 | 568.1 | 325.6 | +41.6% | +47.3% | +17.0% | +13.1% | +67.8% | -12.2% | -6.3% | -4.5% | +4.8% | -29.6% | 1.20 | -5.1% |
| 26 (watchlist) | HYPE | 79.91 | 1,588.6 | 314.4 | +23.8% | +53.3% | +23.0% | +17.7% | +79.3% | -14.5% | -8.7% | -4.7% | +0.7% | -18.5% | 1.13 | -8.2% |
| 36 (watchlist) | BNB | 721.43 | 45.7 | 3.0 | +31.7% | +25.2% | -5.1% | -3.9% | +39.8% | -10.5% | -4.4% | -3.1% | -0.6% | -24.8% | 0.77 | -6.0% |

- **Watchlist detail** (BTC as reference; KNTQ = spot @334) — [HL API candleSnapshot / metaAndAssetCtxs / spotMetaAndAssetCtxs](https://api.hyperliquid.xyz/info):

| Metric | BTC | SOL | HYPE | LIT | BNB | LINK | KNTQ (spot) |
|---|---|---|---|---|---|---|---|
| Price (last close, 03:00 UTC candle) | 81,499 | 104.68 | 79.91 | 3.204 | 721.43 | 12.35 | 0.3128 |
| OI notional $M | 3,353.3 | 568.1 | 1,588.6 | 132.6 | 45.7 | 60.9 | n/a |
| 24h notional volume $M | 2,840.6 | 325.6 | 314.4 | 22.4 | 3.0 | 6.5 | 1.7 |
| Funding now (APR) | 10.95% | -0.39% | 7.41% | -13.59% | 7.47% | 0.25% | spot |
| Max leverage | 40x | 20x | 10x | 5x | 10x | 10x | spot |
| Since BTC Jul low (07-01 01:00) | +38.7% | +41.6% | +23.8% | +74.8% | +31.7% | +71.2% | +97.8% |
| Since BTC Aug low (08-01 18:00) | +30.3% | +47.3% | +53.3% | +58.2% | +25.2% | +55.1% | +244.1% |
|   vs BTC (ratio) | +0.0% | +13.1% | +17.7% | +21.4% | -3.9% | +19.0% | +164.1% |
| Aug low → leg top (09-21 20:00) | +39.2% | +67.8% | +79.3% | +135.6% | +39.8% | +65.5% | +255.3% |
| Leg top → now | -6.4% | -12.2% | -14.5% | -32.9% | -10.5% | -6.3% | -3.2% |
|   vs BTC (ratio) | +0.0% | -6.3% | -8.7% | -28.3% | -4.4% | +0.1% | +3.4% |
| Retest top (10-02 12:00) → now | -6.1% | -14.6% | -12.1% | -15.5% | -7.6% | -14.5% | -0.9% |
| 7d / 30d | -1.3% / +6.7% | -4.5% / +4.8% | -4.7% / +0.7% | -9.8% / -33.9% | -3.1% / -0.6% | -3.6% / +10.9% | +8.0% / +56.1% |
| From high since 2023 (date) | -35.5% (2025-10-06) | -64.6% (2025-01-19) | -18.5% (2026-09-23) | -42.6% (2026-09-24) | -47.5% (2025-10-13) | -60.1% (2024-12-13) | -31.4% (2026-10-01) |
| From 2026 high (date) | -16.8% (2026-01-14) | -29.6% (2026-01-13) | -18.5% (2026-09-23) | -42.6% (2026-09-24) | -24.8% (2026-01-17) | -21.8% (2026-09-29) | -31.4% (2026-10-01) |
| β 1h all / down / up | 1.00 / 1.00 / 1.00 | 1.20 / 1.33 / 1.03 | 1.13 / 1.24 / 0.84 | 1.38 / 1.55 / 0.96 | 0.77 / 0.91 / 0.64 | 1.31 / 1.56 / 0.99 | 0.66 / 0.82 / 0.55 |
| R² (1h) | 1.00 | 0.61 | 0.32 | 0.14 | 0.56 | 0.48 | 0.03 |
| β 4h / β 1d | 1.00 / 1.00 | 1.22 / 1.23 | 1.05 / 1.26 | 1.33 / 1.52 | 0.76 / 0.67 | 1.26 / 1.26 | 0.64 / 1.22 |
| Swing ratio up / down | 1.00 / 1.00 | 1.73 / 1.92 | 2.03 / 2.28 | 3.46 / 5.16 | 1.02 / 1.65 | 1.67 / 0.99 | 6.52 / 0.49 |
| Ann. vol (1h, since Jul) | 35% | 54% | 70% | 130% | 36% | 66% | 135% |
| Worst daily wick since 2025 (date) | -17.1% (2025-10-10) | -37.8% (2025-10-10) | -27.7% (2025-10-10) | -32.1% (2025-12-30) | -35.5% (2025-10-10) | -65.4% (2025-10-10) | -36.6% (2026-06-04) |
| 2025-10-10 wick (low vs prev close) | -17.1% | -37.8% | -27.7% | n/a | -35.5% | -65.4% | n/a |
| Worst 7d close→low (start) | -28.8% (2026-01-30) | -42.6% (2026-01-30) | -35.7% (2025-10-03) | -42.5% (2026-01-08) | -38.1% (2025-10-08) | -67.4% (2025-10-06) | -45.2% (2026-06-01) |
| Approx. drop to liquidate 2x isolated long | -49.4% | -48.7% | -47.4% | -44.4% | -47.4% | -47.4% | n/a (spot) |

- **Best pullback performers** (leg top → now): TIA +71.6%, ZRO +66.4%, STRK +59.2%, GRASS +45.9%, AERO +28.3%, NEAR +24.5%, FIL +19.3%, WLD +12.7%, AAVE +6.5%, PUMP +6.4%.
- **Worst pullback performers:** PONS −46.0%, CASHCAT −38.7%, LIT −32.9%, VVV −26.1%, PURR −22.0%, ZEC −20.9%, DOGE −20.1%, FARTCOIN −19.6%, kPEPE −18.4%, UNI −17.4%, XPL −17.0%.

  [HL API candleSnapshot 1h](https://api.hyperliquid.xyz/info)
- **New highs during this leg:**
  - HYPE set its highest daily high since listing on **2026-09-23** (≈ $98) and is now −18.5% from it.
  - LIT peaked at **5.5858 on 2026-09-24** and is now −42.6% from it (−33.9% over 30d).
  - KNTQ peaked at **0.4557 on 2026-10-01** and is now −31.4% from it.

  [HL API candleSnapshot 1d](https://api.hyperliquid.xyz/info)
- **NEAR** is the largest-OI leader ($313M OI):

  | Window | NEAR |
  |---|---|
  | Since July low | +186.2% |
  | Since August low | +206.1% (+134.9% vs BTC) |
  | August low → top | +145.9% |
  | Leg top → now | +24.5% |
  | 30d | +88.2% |
  | From 2026 high | −15.5% |

  [HL API candleSnapshot](https://api.hyperliquid.xyz/info)
- **ZEC** ($534M OI) had the biggest rally among large-OI alts but is now giving back:

  | Window | ZEC |
  |---|---|
  | August low → top | +214.0% |
  | Leg top → now | −20.9% |
  | 30d | −16.5% |

  [HL API candleSnapshot](https://api.hyperliquid.xyz/info)

### Inferences
- **The rally had two kinds of winners.**
  - *Persistent leaders* outperformed both in the rally and in the pullback: NEAR, ZRO, STRK, TIA, GRASS, AERO, WLD, AAVE, PUMP, FIL; and LINK, which kept pace in the pullback.
  - *Rally-only winners* outperformed into the top and are now underperforming: ZEC, LIT, HYPE, SOL, VVV, CASHCAT, PURR, UNI, ARB.

  For "trend coins," the first group shows current RS. The second group is what you would buy on the premise that the next BTC leg revives last leg's winners.
- **Watchlist ranking by RS since the August low** (out of 50):

  | Coin | Rank |
  |---|---|
  | KNTQ | #1 |
  | LIT | #23 |
  | LINK | #24 |
  | HYPE | #26 |
  | SOL | #29 |
  | BNB | #36 |

  Only KNTQ and LINK were not lagging BTC in the pullback.

### Gaps
- "ATH" here means the highest HL daily high since 2023-01-01 or listing. Older coins' true all-time highs (e.g., LINK 2021) are outside this window.
- Returns are anchored on BTC's extreme hours, not each coin's own low or high.

## Q3. Beta to BTC (overall / upside / downside), R² and swing ratios

### Takeaway
The recomputed hourly OLS betas since 2026-07-01 are lower than the earlier work's mid values:

| Coin | Earlier work (mid) | Hourly OLS β | Downside β | Rally swing ratio |
|---|---|---|---|---|
| HYPE | 1.45 | 1.13 | 1.24 | 2.03 |
| SOL | 1.6 | 1.20 | 1.33 | 1.73 |
| LIT | 2.0 | 1.38 | 1.55 | 3.46 |

The earlier figures fall between the OLS/downside betas and the realized rally swing ratios. Two patterns hold across the universe:
- **Asymmetry:** every coin has downside β > upside β (medians 1.67 vs 1.01).
- **Trend amplitude:** realized swing ratios usually exceed OLS β (median swing-up 1.52 vs median β 1.39), so hourly β understates how far alts move over a trend leg.

### Cited Findings
- **Method:**
  - OLS of consecutive-hour log returns on BTC log returns, 2026-07-01 00:00 UTC → 2026-10-17 03:00 UTC: about 2,595 hours (fewer for coins listed later).
  - Downside / upside β = OLS within hours with BTC return < 0 / > 0 (with intercept).
  - 4h and 1d betas use resampled closes.
  - Swing ratio = coin % move ÷ BTC % move between BTC's extreme hours. Up = August low → leg top (BTC +39.2%); down = leg top → now (BTC −6.4%).

  [HL API candleSnapshot 1h/1d](https://api.hyperliquid.xyz/info)
- **Cross-section (51 non-BTC series):**
  - Median β 1.39; median downside β 1.67; median upside β 1.01. Downside β > upside β for **all 51** coins.
  - Median R² 0.25.
  - Median swing-up 1.52; median swing-down 1.11.
  - Across coins, the correlation of β with swing-up is 0.52 and with swing-down is 0.21.

  [HL API candleSnapshot 1h](https://api.hyperliquid.xyz/info)
- **Watchlist β (all / down / up, R²):**

  | Coin | β all | β down | β up | R² | β 4h | β 1d | Swing up | Swing down |
  |---|---|---|---|---|---|---|---|---|
  | SOL | 1.20 | 1.33 | 1.03 | 0.61 | 1.22 | 1.23 | 1.73 | 1.92 |
  | HYPE | 1.13 | 1.24 | 0.84 | 0.32 | 1.05 | 1.26 | 2.03 | 2.28 |
  | LIT | 1.38 | 1.55 | 0.96 | 0.14 | 1.33 | 1.52 | 3.46 | 5.16 |
  | LINK | 1.31 | 1.56 | 0.99 | 0.48 | 1.26 | 1.26 | 1.67 | 0.99 |
  | BNB | 0.77 | 0.91 | 0.64 | 0.56 | 0.76 | 0.67 | 1.02 | 1.65 |
  | KNTQ (spot) | 0.66 | 0.82 | 0.55 | 0.03 | 0.64 | 1.22 | 6.52 | 0.49 |
  | ETH | 1.15 | 1.25 | 1.08 | 0.73 | — | — | 1.32 | 2.04 |

  [HL API candleSnapshot](https://api.hyperliquid.xyz/info)
- **Flag rule:**
  - `rally>>beta`: swing-up > 1.6β and swing-up − β > 1.
  - `rally<<beta`: swing-up < 0.5β, or swing-up − β < −1.
  - `UP in pullback`: swing-down < 0.
  - `pullback>>beta`: swing-down − β > 2.
  - `pullback<<beta`: swing-down < 0.4β.

  **Coins flagged:**

  | Flag | Coins |
  |---|---|
  | rally>>beta | KNTQ, NEAR, CASHCAT, ZEC, ENA, ARB, PUMP, VVV, UNI, PURR, LIT, XMR |
  | rally<<beta | ONDO, MON, WLFI, GRAM |
  | UP in pullback | NEAR, STRK, ZRO, TIA, PUMP, AERO, GRASS, WLD, AAVE, FIL, JUP, ONDO |
  | pullback>>beta | CASHCAT, VVV, LIT, PONS |
  | pullback<<beta | SUI, FET, WLFI |

  [HL API candleSnapshot 1h](https://api.hyperliquid.xyz/info)
- **Table (b), beta table for all universe coins** (sorted by β; residuals are log moves net of β × BTC's log move) — [HL API candleSnapshot 1h/1d](https://api.hyperliquid.xyz/info):

| Coin | N hours | β (1h OLS) | β down | β up | R² | β 4h | β 1d | Ann. vol | Swing ratio up (Aug low→top) | Swing ratio down (top→now) | Rally resid vs β | Pullback resid vs β | Flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CASHCAT | 2351 | 3.08 | 3.52 | 2.70 | 0.08 | 3.36 | 2.43 | 372% | 8.84 | 6.07 | +47.6% | -28.6% | rally>>beta,pullback>>beta |
| PONS | 1128 | 2.45 | 2.28 | 1.44 | 0.12 | 2.11 | 2.11 | 247% | n/a | 7.22 | n/a | -45.4% | pullback>>beta |
| FARTCOIN | 2595 | 1.81 | 2.25 | 1.28 | 0.32 | 1.90 | 2.07 | 113% | 1.28 | 3.08 | -19.4% | -9.9% |  |
| ENA | 2595 | 1.69 | 1.94 | 1.36 | 0.25 | 1.74 | 1.86 | 119% | 4.15 | 0.95 | +40.5% | +4.9% | rally>>beta |
| kPEPE | 2595 | 1.66 | 2.02 | 1.42 | 0.40 | 1.70 | 2.02 | 91% | 2.01 | 2.88 | +3.2% | -9.3% |  |
| PURR | 2595 | 1.62 | 2.04 | 1.16 | 0.14 | 1.80 | 2.56 | 154% | 2.92 | 3.45 | +22.6% | -14.1% | rally>>beta |
| FET | 2595 | 1.58 | 1.91 | 1.26 | 0.34 | 1.56 | 1.75 | 95% | 1.19 | 0.54 | -14.0% | +6.9% | pullback<<beta |
| AERO | 2595 | 1.57 | 1.88 | 1.22 | 0.29 | 1.46 | 1.24 | 102% | 1.80 | -4.44 | +1.6% | +35.2% | UP in pullback |
| WLD | 2595 | 1.56 | 1.98 | 1.03 | 0.25 | 1.48 | 1.45 | 109% | 1.38 | -1.99 | -8.4% | +22.2% | UP in pullback |
| ONDO | 2595 | 1.55 | 1.82 | 1.17 | 0.33 | 1.58 | 1.33 | 95% | 0.48 | -0.10 | -34.0% | +10.8% | rally<<beta,UP in pullback |
| NEAR | 2595 | 1.53 | 1.85 | 1.11 | 0.23 | 1.53 | 1.33 | 112% | 3.73 | -3.84 | +39.5% | +31.9% | rally>>beta,UP in pullback |
| SUI | 2595 | 1.52 | 1.92 | 1.16 | 0.41 | 1.44 | 1.55 | 82% | 1.35 | 0.17 | -7.8% | +8.9% | pullback<<beta |
| XPL | 2595 | 1.51 | 2.05 | 1.01 | 0.22 | 1.54 | 1.65 | 113% | 0.86 | 2.67 | -21.0% | -8.7% |  |
| ADA | 2595 | 1.51 | 1.83 | 1.20 | 0.43 | 1.50 | 1.57 | 80% | 1.12 | 1.37 | -13.6% | +0.8% |  |
| PUMP | 2595 | 1.51 | 1.50 | 0.89 | 0.15 | 1.24 | 1.03 | 137% | 2.79 | -1.00 | +24.0% | +16.1% | rally>>beta,UP in pullback |
| JUP | 2595 | 1.50 | 1.81 | 1.09 | 0.28 | 1.36 | 1.28 | 99% | 1.48 | -0.29 | -4.1% | +11.7% | UP in pullback |
| ZEC | 2595 | 1.50 | 1.62 | 1.19 | 0.27 | 1.87 | 1.80 | 102% | 5.46 | 3.28 | +64.8% | -13.6% | rally>>beta |
| UNI | 2595 | 1.50 | 1.87 | 1.13 | 0.25 | 1.36 | 1.44 | 105% | 2.99 | 2.74 | +28.1% | -9.3% | rally>>beta |
| ARB | 2595 | 1.49 | 1.91 | 1.13 | 0.19 | 1.46 | 1.64 | 118% | 4.73 | 2.34 | +55.4% | -6.3% | rally>>beta |
| VVV | 2595 | 1.49 | 1.67 | 1.01 | 0.15 | 1.54 | 1.05 | 135% | 4.20 | 4.10 | +48.1% | -20.5% | rally>>beta,pullback>>beta |
| LDO | 2595 | 1.48 | 1.83 | 1.11 | 0.27 | 1.26 | 1.09 | 99% | 0.90 | 1.21 | -18.6% | +1.7% |  |
| MON | 2595 | 1.46 | 2.07 | 0.90 | 0.23 | 1.46 | 1.52 | 107% | 0.68 | 1.95 | -24.8% | -3.7% | rally<<beta |
| PENDLE | 2595 | 1.45 | 1.67 | 1.11 | 0.30 | 1.43 | 1.11 | 92% | 2.15 | 2.55 | +13.1% | -8.1% |  |
| ETHFI | 2595 | 1.44 | 1.70 | 0.92 | 0.19 | 1.48 | 1.33 | 117% | 2.18 | 0.72 | +14.0% | +4.8% |  |
| TAO | 2595 | 1.40 | 1.86 | 0.98 | 0.36 | 1.36 | 1.54 | 81% | 1.56 | 1.62 | +1.4% | -1.6% |  |
| GRASS | 2595 | 1.39 | 2.11 | 0.74 | 0.11 | 1.30 | 1.35 | 144% | 1.06 | -7.20 | -11.3% | +46.9% | UP in pullback |
| TIA | 2595 | 1.39 | 1.90 | 0.89 | 0.21 | 1.36 | 1.31 | 105% | 0.90 | -11.24 | -15.6% | +63.2% | UP in pullback |
| LIT | 2595 | 1.38 | 1.55 | 0.96 | 0.14 | 1.33 | 1.52 | 130% | 3.46 | 5.16 | +40.1% | -30.8% | rally>>beta,pullback>>beta |
| STRK | 2595 | 1.38 | 1.72 | 0.93 | 0.11 | 1.40 | 1.92 | 142% | 2.00 | -9.29 | +12.4% | +55.6% | UP in pullback |
| XRP | 2595 | 1.34 | 1.49 | 1.26 | 0.52 | 1.33 | 1.54 | 65% | 1.17 | 2.34 | -6.5% | -7.3% |  |
| XLM | 2595 | 1.32 | 1.61 | 1.04 | 0.42 | 1.31 | 1.33 | 71% | 0.68 | 2.52 | -20.1% | -8.8% |  |
| LINK | 2595 | 1.31 | 1.56 | 0.99 | 0.48 | 1.26 | 1.26 | 66% | 1.67 | 0.99 | +7.1% | +2.1% |  |
| AAVE | 2595 | 1.30 | 1.53 | 1.02 | 0.33 | 1.23 | 1.53 | 79% | 1.60 | -1.02 | +5.7% | +14.8% | UP in pullback |
| DOGE | 2595 | 1.28 | 1.64 | 0.98 | 0.51 | 1.26 | 1.41 | 63% | 1.19 | 3.15 | -4.2% | -14.0% |  |
| FIL | 2595 | 1.25 | 1.72 | 0.94 | 0.22 | 1.18 | 1.25 | 93% | 1.02 | -3.02 | -7.8% | +25.9% | UP in pullback |
| AVAX | 2595 | 1.24 | 1.51 | 0.95 | 0.35 | 1.26 | 1.09 | 73% | 2.12 | 1.64 | +19.5% | -2.9% |  |
| ZRO | 2595 | 1.20 | 1.34 | 0.85 | 0.11 | 1.13 | 0.81 | 128% | 1.62 | -10.42 | +9.2% | +58.9% | UP in pullback |
| SOL | 2595 | 1.20 | 1.33 | 1.03 | 0.61 | 1.22 | 1.23 | 54% | 1.73 | 1.92 | +12.1% | -5.1% |  |
| ETH | 2595 | 1.15 | 1.25 | 1.08 | 0.73 | 1.19 | 1.24 | 47% | 1.32 | 2.04 | +3.6% | -6.3% |  |
| CRV | 2595 | 1.15 | 1.58 | 0.83 | 0.17 | 1.13 | 1.11 | 96% | 2.10 | 0.87 | +22.0% | +1.9% |  |
| HYPE | 2595 | 1.13 | 1.24 | 0.84 | 0.32 | 1.05 | 1.26 | 70% | 2.03 | 2.28 | +20.9% | -8.2% |  |
| HBAR | 2595 | 1.06 | 1.34 | 0.78 | 0.27 | 1.07 | 0.93 | 71% | 0.85 | 1.35 | -6.6% | -2.0% |  |
| BTC | 2595 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 35% | 1.00 | 1.00 | -0.0% | +0.0% |  |
| LTC | 2595 | 0.94 | 1.11 | 0.75 | 0.32 | 0.87 | 0.94 | 58% | 1.08 | 0.66 | +4.4% | +1.9% |  |
| ASTER | 2595 | 0.84 | 1.24 | 0.60 | 0.23 | 0.72 | 0.63 | 61% | 0.61 | 0.80 | -6.2% | +0.3% |  |
| GRAM | 2562 | 0.82 | 1.21 | 0.52 | 0.19 | 0.82 | 0.89 | 66% | 0.13 | 1.11 | -22.2% | -1.9% | rally<<beta |
| BNB | 2595 | 0.77 | 0.91 | 0.64 | 0.56 | 0.76 | 0.67 | 36% | 1.02 | 1.65 | +7.9% | -6.0% |  |
| KNTQ (spot @334) | 2595 | 0.66 | 0.82 | 0.55 | 0.03 | 0.64 | 1.22 | 135% | 6.52 | 0.49 | +104.9% | +1.2% | rally>>beta |
| WLFI | 2595 | 0.57 | 0.68 | 0.42 | 0.09 | 0.41 | 0.25 | 67% | 0.11 | 0.08 | -14.7% | +3.3% | rally<<beta,pullback<<beta |
| XMR | 2595 | 0.57 | 0.81 | 0.28 | 0.07 | 0.56 | 0.49 | 74% | 1.59 | 0.89 | +29.5% | -2.1% | rally>>beta |
| PAXG | 2595 | 0.19 | 0.26 | 0.13 | 0.10 | 0.22 | 0.34 | 21% | 0.19 | 0.63 | +0.9% | -2.8% |  |
| TRX | 2595 | 0.14 | 0.23 | 0.10 | 0.09 | 0.17 | 0.17 | 16% | 0.13 | 0.41 | +0.3% | -1.7% |  |

### Inferences
- **For scenario modeling, use a band rather than a single β.** The low end is OLS β or 1d β. The high end is the realized August-low→top swing ratio.

  | Coin | Upside band | Downside guidance |
  |---|---|---|
  | SOL | ≈ 1.2–1.75× | ≈ 1.3–1.9× (downside β, pullback swing) |
  | HYPE | ≈ 1.1–2.0× | ≈ 1.25–2.3× |
  | LIT | ≈ 1.4–3.5× | ≈ 1.55–5× |
  | LINK | ≈ 1.3–1.7× | — |
  | BNB | ≈ 0.75–1.0× | — |
  | KNTQ | idiosyncratic (R² 0.03) | — |

- **The β asymmetry (down > up for every coin) makes leveraged alt longs structurally convex the wrong way at short horizons.** Alts' rally outperformance came from drift concentrated in the trend phase, not from hourly co-movement. That drift can reverse quickly, as with LIT: +135.6% into the top, then −32.9% after.
- **Low R² names have unreliable betas.** These include LIT 0.14, STRK/ZRO 0.11, CASHCAT 0.08, KNTQ 0.03. They should be modeled as BTC beta plus a large idiosyncratic volatility term (the annualized vol column in table (b)), not as levered BTC.

### Gaps
- The earlier work's method and window for its 1.45 / 1.6 / 2.0 betas are unknown, so the gap cannot be attributed precisely.
- Swing ratios are single-episode estimates. The pullback denominator (BTC −6.4%) is small, so swing-down ratios are very noisy.
- PONS (since 2026-08-31), CASHCAT (since 2026-07-11) and GRAM (since 2026-07-02) have short samples.

## Q4. Funding cost of holding longs: rally windows vs calm periods

### Takeaway
On HL, funding sits at the 10.95% APR default most of the time: the median hourly rate equals 0.0000125 in every regime for every coin tested. The averages are driven by tails.

| Regime | Average funding (APR) | Cost per 30 days (% of notional) |
|---|---|---|
| Nov–Dec 2024 mania (W1) | BTC 37%, ETH 44%, SOL 47%, LINK 50%, kPEPE 78%; HYPE 143% (partial window) | 3–4% for majors |
| Mid-2025 legs (W2/W3) | ≈ 8–20% for most coins (ENA lower; ZEC's 4-day W3 sample 58%) | ≈ 0.7–1.6% |
| 2026 Aug-low → leg-top rally (W4) | BTC 8.5%, SOL 7.6%, HYPE 10.7%, LIT 13.8%, ZEC 14.9% | ≈ 0.6–1.2% |

The 2026 leg was not a funding-expensive rally.

### Cited Findings
- **Method:**
  - Hourly `fundingRate` from `fundingHistory`, 2024-10-01 → 2026-10-17, paginated at 500 rows per call: 17,908 rows for BTC.
  - Annualized = rate × 24 × 365. "%/30d" = mean hourly rate × 720 = % of notional paid per 30 days by a long.
  - Windows are UTC dates, inclusive.
  - **Calm** = days with |BTC 30-day close-to-close return| < 5% (271 days since 2024-10-01). **Bull30d** = BTC 30-day return > +15% (102 days).

  [HL API fundingHistory](https://api.hyperliquid.xyz/info)
- **Alt selection:** BTC, ETH, SOL, HYPE, the watchlist perps BNB/LINK/LIT, and five high-β alts with long or large-OI history (ZEC, ENA, kPEPE, WLD, SUI).
- **Coverage limits:**
  - HYPE funding starts 2024-12-05, so W1 covers only 302 hours (Dec 5–17).
  - LIT starts 2025-12-22.
  - ZEC funding history starts 2025-10-02, even though its candles go back to 2023.

  [HL API fundingHistory](https://api.hyperliquid.xyz/info)
- **Table (c1), average annualized funding (in brackets: % of notional per 30 days)** — [HL API fundingHistory](https://api.hyperliquid.xyz/info). Regime days since 2024-10-01: calm=271, bull30d=102. W1 = 2024-11-05→12-17; W2 = 2025-06-22→08-14; W3 = 2025-09-01→10-06; W4 = 2026-08-01→09-21 (BTC August low → leg top):

| Coin | W1 | W2 | W3 | W4 | Calm | Bull30d | All | Last30d |
|---|---|---|---|---|---|---|---|---|
| BTC | 37.1% (3.05%) | 15.4% (1.26%) | 10.7% (0.88%) | 8.5% (0.70%) | 7.9% (0.65%) | 21.6% (1.78%) | 10.2% (0.84%) | 8.9% (0.73%) |
| ETH | 43.6% (3.59%) | 16.1% (1.33%) | 8.4% (0.69%) | 9.1% (0.74%) | 7.2% (0.59%) | 24.1% (1.98%) | 9.6% (0.79%) | 9.3% (0.77%) |
| SOL | 46.7% (3.84%) | 15.6% (1.28%) | 10.4% (0.86%) | 7.6% (0.62%) | 3.7% (0.31%) | 24.8% (2.04%) | 6.4% (0.52%) | 8.4% (0.69%) |
| HYPE | 142.5% (11.71%) | 19.7% (1.62%) | 18.5% (1.52%) | 10.7% (0.88%) | 17.9% (1.47%) | 35.2% (2.89%) | 20.4% (1.67%) | 10.2% (0.83%) |
| BNB | 43.8% (3.60%) | 13.6% (1.12%) | 9.0% (0.74%) | 11.0% (0.90%) | 2.8% (0.23%) | 24.0% (1.97%) | 6.2% (0.51%) | 8.9% (0.73%) |
| LINK | 49.6% (4.07%) | 19.7% (1.62%) | 11.7% (0.97%) | 12.4% (1.02%) | 10.7% (0.88%) | 27.8% (2.28%) | 13.2% (1.08%) | 10.1% (0.83%) |
| LIT | n/a | n/a | n/a | 13.8% (1.14%) | 9.0% (0.74%) | 15.4% (1.26%) | 10.8% (0.89%) | 10.6% (0.87%) |
| ZEC | n/a | n/a | 57.9% (4.76%) | 14.9% (1.23%) | 6.8% (0.56%) | 17.7% (1.45%) | 4.3% (0.36%) | 12.8% (1.06%) |
| ENA | 13.3% (1.09%) | 8.0% (0.66%) | 0.1% (0.01%) | 14.9% (1.22%) | -3.0% (-0.25%) | 14.7% (1.21%) | -1.2% (-0.10%) | 14.8% (1.22%) |
| kPEPE | 78.0% (6.41%) | 18.6% (1.53%) | 13.5% (1.11%) | 13.9% (1.14%) | 6.8% (0.56%) | 42.8% (3.52%) | 13.3% (1.09%) | 14.2% (1.17%) |
| WLD | 46.7% (3.84%) | 15.7% (1.29%) | 13.5% (1.11%) | 8.6% (0.71%) | 6.8% (0.56%) | 25.2% (2.07%) | 9.2% (0.75%) | 17.3% (1.42%) |
| SUI | 39.0% (3.21%) | 17.5% (1.44%) | 11.0% (0.90%) | 12.7% (1.04%) | 5.5% (0.45%) | 24.3% (2.00%) | 8.0% (0.66%) | 13.3% (1.09%) |

- **Table (c2), 90th-percentile annualized hourly funding** (11.0% = the default rate) — [HL API fundingHistory](https://api.hyperliquid.xyz/info):

| Coin | W1 | W2 | W3 | W4 | Calm | Bull30d | All | Last30d |
|---|---|---|---|---|---|---|---|---|
| BTC | 68.5% | 32.6% | 11.0% | 11.0% | 11.0% | 52.8% | 13.6% | 11.0% |
| ETH | 80.5% | 41.4% | 11.0% | 11.0% | 11.0% | 62.3% | 11.0% | 11.0% |
| SOL | 87.0% | 41.9% | 13.4% | 11.0% | 11.0% | 67.9% | 14.0% | 11.0% |
| HYPE | 300.1% | 49.0% | 45.0% | 11.0% | 37.0% | 104.1% | 44.5% | 11.0% |
| BNB | 95.1% | 42.9% | 11.0% | 11.0% | 11.0% | 72.7% | 11.0% | 11.0% |
| LINK | 101.0% | 47.5% | 11.0% | 12.2% | 11.0% | 72.5% | 12.0% | 11.0% |
| LIT | n/a | n/a | n/a | 28.9% | 11.0% | 32.2% | 11.0% | 11.0% |
| ZEC | n/a | n/a | 116.1% | 26.0% | 11.0% | 37.6% | 11.0% | 12.8% |
| ENA | 47.9% | 55.5% | 18.8% | 21.6% | 11.0% | 39.9% | 11.0% | 27.2% |
| kPEPE | 150.0% | 55.0% | 26.3% | 22.0% | 11.0% | 115.6% | 33.2% | 25.2% |
| WLD | 111.8% | 43.3% | 26.4% | 11.7% | 11.0% | 77.8% | 21.1% | 40.1% |
| SUI | 90.4% | 47.0% | 11.0% | 13.6% | 11.0% | 72.1% | 11.0% | 22.1% |

- **Table (c3), share of hours at exactly the default 0.0000125/h / share of hours negative** — [HL API fundingHistory](https://api.hyperliquid.xyz/info):

| Coin | W1 | W2 | W3 | W4 | Calm | Bull30d | All | Last30d |
|---|---|---|---|---|---|---|---|---|
| BTC | 21%/0% | 57%/5% | 83%/2% | 60%/9% | 61%/14% | 45%/5% | 56%/13% | 61%/7% |
| ETH | 17%/0% | 47%/11% | 67%/11% | 67%/6% | 56%/17% | 45%/6% | 53%/16% | 73%/6% |
| SOL | 19%/0% | 51%/10% | 68%/5% | 53%/12% | 50%/24% | 38%/11% | 44%/26% | 64%/9% |
| HYPE | 15%/1% | 61%/6% | 60%/6% | 68%/10% | 68%/8% | 55%/7% | 67%/7% | 82%/7% |
| BNB | 33%/0% | 52%/18% | 70%/11% | 66%/10% | 53%/28% | 51%/9% | 52%/25% | 65%/11% |
| LINK | 22%/0% | 68%/1% | 85%/1% | 65%/9% | 76%/6% | 51%/3% | 72%/6% | 67%/8% |
| LIT | n/a/n/a | n/a/n/a | n/a/n/a | 71%/9% | 76%/11% | 75%/6% | 78%/9% | 73%/11% |
| ZEC | n/a/n/a | n/a/n/a | 33%/0% | 71%/6% | 65%/18% | 71%/3% | 66%/18% | 85%/2% |
| ENA | 58%/14% | 39%/25% | 49%/28% | 77%/5% | 55%/29% | 68%/9% | 55%/28% | 80%/2% |
| kPEPE | 15%/1% | 51%/9% | 67%/6% | 72%/8% | 65%/16% | 47%/4% | 59%/15% | 67%/9% |
| WLD | 30%/0% | 56%/11% | 75%/3% | 64%/17% | 67%/16% | 48%/10% | 62%/17% | 70%/2% |
| SUI | 37%/2% | 59%/9% | 86%/2% | 73%/6% | 58%/22% | 53%/9% | 54%/22% | 71%/3% |

- **Extreme hourly prints (annualized max since 2024-10):**

  | Coin | Max |
  |---|---|
  | BTC | 297% |
  | HYPE | 776% |
  | ZEC | 1,885% (a single hour inside the calm regime) |
  | LIT | 249% (during W4) |

  The 99th percentile in the 2026 W4 rally was BTC 24.7%, SOL 22.2%, HYPE 71.5%, LIT 108.2%, ZEC 125.9% — [HL API fundingHistory](https://api.hyperliquid.xyz/info)
- **Last 30 days:**

  | Coin | Average funding (APR) |
  |---|---|
  | BTC | 8.9% |
  | ETH | 9.3% |
  | SOL | 8.4% |
  | HYPE | 10.2% |
  | BNB | 8.9% |
  | LINK | 10.1% |
  | LIT | 10.6% |
  | ZEC | 12.8% |
  | ENA | 14.8% |
  | kPEPE | 14.2% |
  | WLD | 17.3% |
  | SUI | 13.3% |

  [HL API fundingHistory](https://api.hyperliquid.xyz/info)

### Inferences
- **Cost of a 2x perp long, as % of equity per 30 days** (double the %-of-notional figure; ignores trading fees):

  | Scenario | Cost per 30 days |
  |---|---|
  | Default rate | ≈ 1.8% |
  | W4-style rally (SOL 0.62%/30d notional) | ≈ 1.2% |
  | Bull30d regime | ≈ 3.6–4.1% for BTC/SOL; ≈ 5.8% for HYPE |
  | 2024-style mania (W1) | ≈ 6–8% for SOL/BNB/LINK; ≈ 23% for HYPE |

  Over a 2–3 month hold in a hot market, funding can consume a meaningful share of the 2x advantage over spot. In a W4-like market it is minor.
- **HYPE carries a structural premium:** calm-regime average 17.9% APR (p90 37%) and all-history average 20.4%, against BTC's 7.9% / 10.2%. Holding HYPE via perps costs roughly double the majors outside of manias.
- **SOL and BNB longs pay less than the default in calm markets** (averages 3.7% and 2.8%) because 24–28% of calm hours had negative funding.

### Gaps
- ZEC history before 2025-10-02 and LIT before 2025-12-22 are missing, so W1–W3 cannot be compared for them.
- HYPE's W1 window is only its first two weeks of trading.
- Funding regime definitions (named windows, ±5% calm band) are judgment calls. A different calm definition would shift the averages modestly, since medians stay at the default.

## Q5. Crash-wick risk: worst daily wicks, the 2025-10-10/11 event, worst 3-day and 7-day drawdowns

### Takeaway
The 2025-10-10 crash is the worst daily wick since 2025 for almost every perp on HL:

| Coin | 2025-10-10 wick (low vs prior close) |
|---|---|
| BTC | −17.1% |
| ETH | −25.8% |
| HYPE | −27.7% |
| BNB | −35.5% |
| SOL | −37.8% |
| LINK | −65.4% |
| Most alts | −58% to −86% |

At 2x isolated (liquidation ≈ 44–49% adverse move), BTC, ETH, SOL, HYPE and BNB would have survived that day on candle lows. LINK and most alts would not. LIT had not listed yet. Its worst 7-day close-to-low (−42.5%) sits just inside its ≈ −44% 2x threshold.

### Cited Findings
- **Method:** daily UTC candles since 2025-01-01 (or listing).
  - Wick = low_t / close_{t−1} − 1.
  - N-day close→low = min(low over t+1..t+N) / close_t − 1.
  - N-day close→close = close_{t+N} / close_t − 1.

  [HL API candleSnapshot 1d](https://api.hyperliquid.xyz/info)
- **Table (d1), 10 worst daily wicks** (low vs previous close) for the named coins — [HL API candleSnapshot 1d](https://api.hyperliquid.xyz/info):

| Rank | BTC | ETH | SOL | HYPE | BNB | LINK | LIT |
|---|---|---|---|---|---|---|---|
| 1 | -17.1% (2025-10-10) | -26.9% (2025-02-03) | -37.8% (2025-10-10) | -27.7% (2025-10-10) | -35.5% (2025-10-10) | -65.4% (2025-10-10) | -32.1% (2025-12-30) |
| 2 | -15.0% (2026-02-05) | -25.8% (2025-10-10) | -22.1% (2025-03-03) | -22.1% (2025-03-26) | -18.8% (2025-02-03) | -24.4% (2025-02-03) | -24.1% (2026-08-22) |
| 3 | -10.6% (2026-01-31) | -18.7% (2026-01-31) | -19.4% (2026-01-31) | -17.0% (2025-01-18) | -16.0% (2025-11-03) | -18.0% (2025-11-03) | -21.7% (2026-01-29) |
| 4 | -9.7% (2025-03-03) | -16.7% (2025-03-03) | -18.1% (2025-02-24) | -17.0% (2025-04-06) | -13.5% (2026-02-05) | -17.4% (2025-03-03) | -21.6% (2026-01-31) |
| 5 | -7.7% (2025-04-06) | -15.4% (2026-02-05) | -15.7% (2026-02-05) | -16.1% (2025-02-01) | -12.8% (2026-01-31) | -17.0% (2026-01-31) | -21.5% (2026-06-04) |
| 6 | -7.6% (2025-02-28) | -15.1% (2025-11-04) | -15.6% (2025-11-03) | -16.1% (2025-01-09) | -11.6% (2025-10-14) | -16.1% (2025-02-02) | -19.7% (2026-01-12) |
| 7 | -7.4% (2026-06-05) | -14.9% (2025-04-06) | -13.8% (2025-02-03) | -15.8% (2025-11-21) | -11.4% (2025-11-04) | -15.1% (2025-02-24) | -19.5% (2026-05-22) |
| 8 | -7.4% (2025-11-21) | -13.0% (2026-06-05) | -13.7% (2026-02-06) | -15.5% (2026-06-04) | -10.8% (2025-10-17) | -15.0% (2026-02-05) | -19.4% (2026-01-15) |
| 9 | -7.4% (2026-02-03) | -12.3% (2025-02-24) | -13.7% (2025-04-06) | -15.1% (2025-03-03) | -9.6% (2025-02-04) | -14.3% (2025-04-06) | -18.6% (2026-09-29) |
| 10 | -7.3% (2026-06-02) | -12.1% (2025-09-22) | -12.2% (2025-11-04) | -14.5% (2025-01-02) | -9.3% (2026-05-23) | -12.5% (2025-08-14) | -15.6% (2026-05-26) |

- **Table (d2), 2025-10-10/11 event and worst 3d/7d drawdowns** for the named coins — [HL API candleSnapshot 1d](https://api.hyperliquid.xyz/info). The 2x liquidation column is approximate, using an isolated long with maintenance margin = 1/(2 × maxLeverage), per [HL docs: margining](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/margining) (not re-fetched this session):

| Coin | History since | 2025-10-10 prev close → low (drop) | 2025-10-10 close vs prev | 2025-10-11 drop (low vs prev close) | Worst 3d close→low (start) | Worst 7d close→low (start) | Worst 3d close→close | Worst 7d close→close | Approx. 2x isolated liq. drop |
|---|---|---|---|---|---|---|---|---|---|
| BTC | 2025-01-01 | 121,615 → 100,837 (-17.1%) | -7.3% | -2.9% | -21.0% (2026-02-02) | -28.8% (2026-01-30) | -20.1% | -25.7% | -49.4% |
| ETH | 2025-01-01 | 4,369 → 3,241 (-25.8%) | -12.5% | -4.7% | -36.5% (2025-01-31) | -36.5% (2025-01-31) | -22.1% | -35.3% | -49.0% |
| SOL | 2025-01-01 | 221.00 → 137.51 (-37.8%) | -15.1% | -8.1% | -40.0% (2025-10-08) | -42.6% (2026-01-30) | -25.1% | -33.5% | -48.7% |
| HYPE | 2025-01-01 | 43.98 → 31.80 (-27.7%) | -15.0% | -5.9% | -31.9% (2025-10-08) | -35.7% (2025-10-03) | -24.2% | -31.1% | -47.4% |
| BNB | 2025-01-01 | 1,256 → 809.51 (-35.5%) | -12.1% | -2.5% | -38.1% (2025-10-08) | -38.1% (2025-10-08) | -21.4% | -30.0% | -47.4% |
| LINK | 2025-01-01 | 22.01 → 7.615 (-65.4%) | -21.4% | -4.1% | -66.4% (2025-10-08) | -67.4% (2025-10-06) | -24.1% | -28.8% | -47.4% |
| LIT | 2025-12-23 | not listed | n/a | n/a | -39.1% (2025-12-28) | -42.5% (2026-01-08) | -33.1% | -38.4% | -44.4% |

- On 2025-10-10, **38 of 47** universe perps then listed printed a daily wick deeper than their approximate 2x isolated liquidation move (at today's max leverage). Those that did not: ZEC -41.9%, SOL -37.8%, BNB -35.5%, HYPE -27.7%, ETH -25.8%, PAXG -23.6%, XMR -22.5%, BTC -17.1%, TRX -15.4%. Median 10-10 wick across the 47 perps: -66.3%; range for the 39 alts excluding BTC/ETH/SOL/BNB/HYPE/PAXG/TRX/XMR: -86.1% to -41.9%. — [HL API candleSnapshot 1d + metaAndAssetCtxs](https://api.hyperliquid.xyz/info)
- **Table (d3), crash-risk summary for the whole universe** (sorted by worst 7-day close→low). "Breached at 2x?" asks whether the worst 7-day close→low exceeded the approximate 2x isolated liquidation move at today's max leverage — [HL API candleSnapshot 1d + metaAndAssetCtxs](https://api.hyperliquid.xyz/info):

| Coin | History since | Worst daily wick (date) | 2025-10-10 wick | Worst 3d close→low | Worst 7d close→low (start) | Worst 7d close→close | 2x iso liq. drop | Breached at 2x? |
|---|---|---|---|---|---|---|---|---|
| FARTCOIN | 2025-01-01 | -86.1% (2025-10-10) | -86.1% | -87.0% | -88.0% (2025-10-06) | -62.6% | -47.4% | YES |
| TIA | 2025-01-01 | -83.9% (2025-10-10) | -83.9% | -84.4% | -85.1% (2025-10-04) | -40.4% | -44.4% | YES |
| SUI | 2025-01-01 | -82.9% (2025-10-10) | -82.9% | -83.5% | -84.0% (2025-10-04) | -33.2% | -47.4% | YES |
| ETHFI | 2025-01-01 | -81.0% (2025-10-10) | -81.0% | -82.8% | -83.1% (2025-10-04) | -39.1% | -44.4% | YES |
| STRK | 2025-01-01 | -80.3% (2025-10-10) | -80.3% | -81.9% | -82.9% (2025-10-06) | -39.1% | -44.4% | YES |
| FET | 2025-01-01 | -77.6% (2025-10-10) | -77.6% | -80.3% | -81.6% (2025-10-03) | -47.7% | -44.4% | YES |
| WLD | 2025-01-01 | -78.5% (2025-10-10) | -78.5% | -79.9% | -80.7% (2025-10-03) | -35.1% | -47.4% | YES |
| AERO | 2025-01-01 | -78.2% (2025-10-10) | -78.2% | -78.7% | -80.4% (2025-10-06) | -34.7% | -40.0% | YES |
| LDO | 2025-01-01 | -78.7% (2025-10-10) | -78.7% | -79.4% | -80.3% (2025-10-06) | -32.9% | -44.4% | YES |
| PUMP | 2025-07-11 | -75.4% (2025-10-10) | -75.4% | -78.9% | -80.3% (2025-10-03) | -47.6% | -47.4% | YES |
| GRASS | 2025-01-01 | -77.2% (2025-10-10) | -77.2% | -79.1% | -80.2% (2025-10-03) | -44.0% | -40.0% | YES |
| ENA | 2025-01-01 | -76.9% (2025-10-10) | -76.9% | -78.1% | -79.5% (2025-10-03) | -37.9% | -47.4% | YES |
| FIL | 2025-01-01 | -77.9% (2025-10-10) | -77.9% | -78.5% | -78.9% (2025-10-06) | -40.8% | -44.4% | YES |
| ARB | 2025-01-01 | -75.6% (2025-10-10) | -75.6% | -76.5% | -77.7% (2025-10-06) | -34.3% | -47.4% | YES |
| CRV | 2025-01-01 | -75.7% (2025-10-10) | -75.7% | -76.2% | -77.4% (2025-10-03) | -40.1% | -47.4% | YES |
| XPL | 2025-08-23 | -68.1% (2025-10-10) | -68.1% | -74.3% | -77.2% (2025-10-06) | -55.4% | -47.4% | YES |
| JUP | 2025-01-01 | -74.7% (2025-10-10) | -74.7% | -75.8% | -76.9% (2025-10-06) | -41.3% | -47.4% | YES |
| CASHCAT | 2026-07-12 | -70.7% (2026-08-22) | n/a | -76.5% | -76.5% (2026-07-14) | -58.2% | -40.0% | YES |
| AVAX | 2025-01-01 | -73.1% (2025-10-10) | -73.1% | -73.5% | -75.6% (2025-10-03) | -34.3% | -47.4% | YES |
| VVV | 2025-01-29 | -47.0% (2025-10-10) | -47.0% | -59.7% | -75.5% (2025-01-29) | -41.2% | -40.0% | YES |
| ONDO | 2025-01-01 | -72.6% (2025-10-10) | -72.6% | -73.7% | -74.8% (2025-10-06) | -28.9% | -47.4% | YES |
| UNI | 2025-01-01 | -73.0% (2025-10-10) | -73.0% | -73.7% | -74.6% (2025-10-06) | -29.2% | -47.4% | YES |
| kPEPE | 2025-01-01 | -69.6% (2025-10-10) | -69.6% | -70.6% | -72.4% (2025-10-06) | -35.6% | -47.4% | YES |
| AAVE | 2025-01-01 | -68.5% (2025-10-10) | -68.5% | -69.8% | -71.0% (2025-10-06) | -31.4% | -47.4% | YES |
| WLFI | 2025-08-24 | -66.3% (2025-10-10) | -66.3% | -67.5% | -69.9% (2025-10-03) | -40.6% | -44.4% | YES |
| ADA | 2025-01-01 | -66.9% (2025-10-10) | -66.9% | -67.8% | -69.0% (2025-10-06) | -36.6% | -47.4% | YES |
| PENDLE | 2025-01-01 | -65.4% (2025-10-10) | -65.4% | -67.3% | -68.7% (2025-10-06) | -40.9% | -44.4% | YES |
| DOGE | 2025-01-01 | -65.8% (2025-10-10) | -65.8% | -66.7% | -68.0% (2025-10-06) | -29.8% | -47.4% | YES |
| LINK | 2025-01-01 | -65.4% (2025-10-10) | -65.4% | -66.4% | -67.4% (2025-10-06) | -28.8% | -47.4% | YES |
| HBAR | 2025-01-01 | -64.2% (2025-10-10) | -64.2% | -65.3% | -66.9% (2025-10-06) | -27.7% | -44.4% | YES |
| ZRO | 2025-01-01 | -64.3% (2025-10-10) | -64.3% | -66.6% | -66.6% (2025-10-08) | -37.1% | -44.4% | YES |
| XLM | 2025-01-01 | -63.7% (2025-10-10) | -63.7% | -64.6% | -66.3% (2025-10-06) | -26.1% | -44.4% | YES |
| TAO | 2025-01-01 | -65.4% (2025-10-10) | -65.4% | -65.4% | -65.4% (2025-10-09) | -31.1% | -44.4% | YES |
| ASTER | 2025-09-20 | -54.4% (2025-10-10) | -54.4% | -62.6% | -63.2% (2025-10-03) | -41.8% | -44.4% | YES |
| XRP | 2025-01-01 | -58.1% (2025-10-10) | -58.1% | -59.2% | -61.4% (2025-10-03) | -32.8% | -48.7% | YES |
| LTC | 2025-01-01 | -61.3% (2025-10-10) | -61.3% | -61.3% | -61.3% (2025-10-09) | -27.2% | -47.4% | YES |
| ZEC | 2025-01-01 | -46.3% (2026-06-05) | -41.9% | -60.2% | -60.2% (2026-06-03) | -41.9% | -47.4% | YES |
| PURR | 2025-01-01 | -48.2% (2025-10-10) | -48.2% | -52.9% | -58.6% (2025-10-03) | -48.1% | -40.0% | YES |
| MON | 2025-10-09 | -49.8% (2025-10-10) | -49.8% | -49.8% | -53.5% (2025-10-09) | -46.7% | -44.4% | YES |
| NEAR | 2025-01-01 | -47.9% (2025-10-10) | -47.9% | -49.4% | -50.9% (2025-10-06) | -31.8% | -47.4% | YES |
| KNTQ (spot @334) | 2026-05-21 | -36.6% (2026-06-04) | n/a | -45.2% | -45.2% (2026-06-01) | -34.8% | n/a | spot |
| SOL | 2025-01-01 | -37.8% (2025-10-10) | -37.8% | -40.0% | -42.6% (2026-01-30) | -33.5% | -48.7% | no |
| LIT | 2025-12-23 | -32.1% (2025-12-30) | n/a | -39.1% | -42.5% (2026-01-08) | -38.4% | -44.4% | no |
| PONS | 2026-09-01 | -22.4% (2026-09-10) | n/a | -32.8% | -42.3% (2026-09-05) | -35.8% | -40.0% | YES |
| XMR | 2025-01-01 | -23.5% (2026-02-05) | -22.5% | -27.8% | -40.7% (2026-01-31) | -36.3% | -44.4% | no |
| BNB | 2025-01-01 | -35.5% (2025-10-10) | -35.5% | -38.1% | -38.1% (2025-10-08) | -30.0% | -47.4% | no |
| ETH | 2025-01-01 | -26.9% (2025-02-03) | -25.8% | -36.5% | -36.5% (2025-01-31) | -35.3% | -49.0% | no |
| HYPE | 2025-01-01 | -27.7% (2025-10-10) | -27.7% | -31.9% | -35.7% (2025-10-03) | -31.1% | -47.4% | no |
| BTC | 2025-01-01 | -17.1% (2025-10-10) | -17.1% | -21.0% | -28.8% (2026-01-30) | -25.7% | -49.4% | no |
| PAXG | 2025-03-28 | -23.6% (2025-10-10) | -23.6% | -24.1% | -24.1% (2025-10-08) | -14.2% | -47.4% | no |
| TRX | 2025-01-01 | -15.4% (2025-10-10) | -15.4% | -21.3% | -21.3% (2025-01-31) | -17.0% | -47.4% | no |
| GRAM | 2026-07-03 | -10.3% (2026-07-17) | n/a | -15.9% | -17.3% (2026-07-10) | -12.3% | -44.4% | no |


### Inferences
- **2x on BTC, ETH, SOL, HYPE or BNB survived every daily wick since 2025, measured on trade-price lows.** The closest call is SOL's 7-day −42.6% (from 2026-01-30) against a ≈ −48.7% threshold.
- **LINK and nearly all mid- and small-cap alts would have been liquidated at 2x isolated on 2025-10-10.** For trend coins, either run lower effective leverage (≤ 1.3–1.5x), use spot, or keep a cross-margin buffer.
- **LIT's 5x max leverage means a higher maintenance margin, so its 2x liquidation is nearer (≈ −44%).** Its realized worst 7-day close→low (−42.5%) leaves almost no buffer.

### Gaps
- Candle lows are HL trade prices; liquidations use HL's mark price (oracle and book-based), which may not have reached the same lows on 2025-10-10. Mark-price history is not available from candleSnapshot.
- Liquidation estimates use today's max leverage; tiers, fees and funding are ignored.
- KNTQ (spot since 2026-05-20) and LIT (since 2025-12-22) have no history through a 10-10-type event.

## Q6. Interpretation: leaders, high-beta laggards, caveats

### Takeaway
- **Leaders:** NEAR is the standout: large OI, the strongest RS through both the rally and the pullback, and a beta-adjusted residual of +31.9% in the pullback. ZRO, STRK, TIA, GRASS and AERO are strong but thinner, with histories of −62% to −98% drawdowns from their 2023+ highs and −64% to −84% wicks on 2025-10-10.
- **Watchlist:** LINK has the cleanest "beta plus modest alpha" profile. KNTQ is a strong idiosyncratic spot trend, uncorrelated with BTC hour to hour.
- **High-beta laggards:** FARTCOIN, XPL, MON, ONDO, LDO, ADA, DOGE, XLM and kPEPE.
- **Rally-only winners now giving back:** LIT, ZEC, HYPE and SOL.

### Cited Findings
- **Leaders** (beat BTC both since the August low and in the pullback; coin/BTC ratios in %, OI): KNTQ +164/+3 (spot), NEAR +135/+33 ($313M), STRK +118/+70 ($48M), ZRO +109/+78 ($72M), ENA +89/+0 ($98M), TIA +78/+83 ($17M), PUMP +71/+14 ($174M), AERO +68/+37 ($34M), GRASS +58/+56 ($30M), ETHFI +36/+2, WLD +33/+20 ($72M), AAVE +33/+14 ($62M), CRV +32/+1, FIL +28/+27, JUP +23/+9, LINK +19/+0 ($61M), XMR +17/+1, SUI +16/+6 ($62M), FET +9/+3, LTC +5/+2 — [HL API candleSnapshot + metaAndAssetCtxs](https://api.hyperliquid.xyz/info)
- **High-beta laggards** (β ≥ 1.4 with a negative beta-adjusted return since the August low; β, return since the August low, residual):

  | Coin | β | Since Aug low | Residual |
  |---|---|---|---|
  | XPL | 1.51 | +11% | −30% |
  | FARTCOIN | 1.81 | +21% | −29% |
  | MON | 1.46 | +11% | −28% |
  | ONDO | 1.55 | +20% | −23% |
  | LDO | 1.48 | +25% | −17% |
  | ADA | 1.51 | +31% | −13% |
  | FET | 1.58 | +42% | −7% |
  | kPEPE | 1.66 | +46% | −6% |
  | TAO | 1.40 | +45% | ≈ 0% |

  Lower-β laggards include DOGE (β 1.28: +17.1% since the August low, −20.1% in the pullback) and XLM (β 1.32: +6.1%, −16.1%) — [HL API candleSnapshot](https://api.hyperliquid.xyz/info)
- **Rally winners giving back** (beat BTC since the August low, but the pullback is worse than BTC by >5%; coin/BTC ratios in %): CASHCAT +110/−35, LIT +21/−28, VVV +50/−21, PURR +28/−17, ZEC +91/−16, kPEPE +12/−13, UNI +38/−12, PENDLE +18/−11, ARB +86/−9, HYPE +18/−9, ETH +1/−7, SOL +13/−6 — [HL API candleSnapshot](https://api.hyperliquid.xyz/info)
- **Defensive / low beta:** BNB (β 0.77; +25.2% since the August low, −3.9% vs BTC), TRX (0.14), PAXG (0.19), XMR (0.57; +53% since the August low on idiosyncratic strength) — [HL API candleSnapshot](https://api.hyperliquid.xyz/info)

### Inferences
- **Watchlist read-through:**
  - **SOL:** the most "index-like" alt (R² 0.61, β ≈ 1.2), with mild RS and the lowest idiosyncratic risk.
  - **HYPE:** β ≈ 1.1–1.3 but a 2.0 rally swing. It set an ATH on 2026-09-23 and so leads on a cycle basis. Its perp funding is structurally expensive.
  - **LIT:** the highest-amplitude watchlist coin (rally swing 3.5×, pullback swing 5.2×, 130% annualized vol). It is in a deep pullback (−42.6% from its 2026-09-24 high, −33.9% over 30d). Max leverage is 5x and the 2x liquidation buffer is thin.
  - **BNB:** low beta and lagging; it suits stability, not upside.
  - **LINK:** steady RS with a clean beta.
  - **KNTQ:** spot only, idiosyncratic, $1.7M/day liquidity, ATH 2026-10-01.
- **Candidate trend coins by RS persistence plus liquidity:** NEAR first; then WLD, AAVE and PUMP (OI $62–174M, positive in the pullback). TIA, ZRO, STRK, GRASS and AERO show stronger RS but have thin OI or volume, 3x caps (AERO, GRASS) and extreme historical wick and drawdown profiles.
- **Caveats:**
  - Single-episode swing ratios.
  - Very short histories: PONS, CASHCAT, GRAM, KNTQ, LIT, MON, ASTER, XPL, WLFI, PUMP.
  - "ATH" means high since 2023 or listing.
  - Momentum leaders after a +100–200% run are also the most exposed to mean reversion.
  - Trade-price wicks are not mark-price liquidations.

### Gaps
- No order-book depth or slippage analysis was done for the smaller leaders (TIA, GRASS, AERO, STRK) or KNTQ spot.
- No fundamental or catalyst check on why the leaders are leading (outside this quant scope).
- Betas were not recomputed on the August-low-onward window alone. All betas use the 2026-07-01 → now sample.
