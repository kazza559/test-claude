# Pendle YT Markets for USD.AI Assets (USDai / sUSDai): Live Data, YT Economics, History, Points Rules

Fetch metadata: all Pendle API data below was pulled with curl on **2026-09-28 between 11:48 and 11:53 UTC**. The Pendle `dataUpdatedAt` field for the live figures was `2026-09-28T11:49:00Z`, and token prices had `priceUpdatedAt 2026-09-28T11:49:15Z`. The v2 `/data` snapshot timestamp was `2026-09-28T11:00:00Z`. The USD.AI rewards page (Allo rates), USD.AI docs (llms-full.txt), CoinGecko (CHIP) and DefiLlama were fetched in the same window. Raw JSON is saved in the session scratchpad (`/tmp/claude-0/-home-user-test-claude/33116665-e8e5-5567-9073-c111e217db02/scratchpad/`): `detail_v1_*.json`, `data_v2_*.json`, `hist_*.json`, `histx_*.json`, `usdai_markets_v2all.json`, `usdai_opportunities.json`.

Conventions used in every calculation:
- `now = 2026-09-28 11:49 UTC`. `days = (maturity 00:00 UTC − now)`, which gives 16.5076 d for 15-Oct-2026 and 149.5076 d for 25-Feb-2027.
- USDai price = $1.0002727 (Pendle API). YT and PT prices "in USDai" = USD price ÷ 1.0002727.
- For the sUSDai markets, Pendle's accounting unit (`pyUnit`) is **"USDai staked in USD.AI"**. 1 PT + 1 YT = 1 USDai of staked value, **not** 1 sUSDai. 1 YT receives the growth of the sUSDai/USDai exchange rate on 1 USDai notional. Check: PT 0.994753 + YT 0.005247 = 1.000000 USDai.
- Implied APY check: `(1/PT_in_USDai)^(365/days) − 1`. It reproduces the API value exactly for all 4 markets.
- Pendle takes **5% of all YT yield and points** (Pendle docs; the USD.AI docs say the same). The YT yield and points below are multiplied by 0.95.
- "Point unit" = 1 unit of underlying (1 USDai notional) × 1x multiplier × 1 day, called a "1x-$-day". This avoids assuming the absolute Allo unit, which I could not confirm.

---

## Q1. Which USDai/sUSDai Pendle markets exist right now (all chains), with live numbers?

### Takeaway
There are exactly **4 active USD.AI markets, all on Arbitrum (42161)**: USDai and sUSDai expiring **15-Oct-2026** and USDai and sUSDai expiring **25-Feb-2027**. Liquidity is concentrated in the Oct-2026 pools ($50.3M USDai, $11.4M sUSDai). The Feb-2027 USDai pool is nearly empty ($57K liquidity, $0 24h volume). No USD.AI market is active on Ethereum, Plasma, Base, BNB, Sonic, HyperEVM, Monad, Mantle, Berachain or Optimism. The 2 Plasma markets (19-Mar-2026) and 6 other Arbitrum markets have expired.

### Cited Findings
- Active-markets endpoint per chain: `core/v1/{chainId}/markets/active`. For 42161 it returned 4 USD.AI markets. The endpoints for 1, 9745, 8453, 56 and 999 returned markets but none for USDai/sUSDai. The endpoints for 146, 5000, 80094 and 10 returned an empty list. The endpoint for 143 returned markets but none for USD.AI. — [Pendle API Arbitrum active](https://api-v2.pendle.finance/core/v1/42161/markets/active); [Ethereum](https://api-v2.pendle.finance/core/v1/1/markets/active); [Plasma](https://api-v2.pendle.finance/core/v1/9745/markets/active)
- A cross-check of all 803 Pendle markets (`core/v2/markets/all`, paginated) filtered by name or protocol "USD.AI" found only 12 markets: 10 on Arbitrum and 2 on Plasma. — [Pendle API v2 markets/all](https://api-v2.pendle.finance/core/v2/markets/all?limit=100&skip=0)

**Live snapshot table (Arbitrum, 2026-09-28 11:49 UTC)** — [v1 market detail, e.g. sUSDai-Oct](https://api-v2.pendle.finance/core/v1/42161/markets/0xcbf629c8d396b1261f81f55175afa010e94787d8); [v2 /data](https://api-v2.pendle.finance/core/v2/42161/markets/0xcbf629c8d396b1261f81f55175afa010e94787d8/data)

| Field | USDai 15-OCT-2026 | sUSDai 15-OCT-2026 | sUSDai 25-FEB-2027 | USDai 25-FEB-2027 |
|---|---|---|---|---|
| Market (LP) address | 0xa8a0dea40174cfc30fea9e3a77f182ab33f46e25 | 0xcbf629c8d396b1261f81f55175afa010e94787d8 | 0xf86119a39f8654f38acbbd5488bd83f3f51983c8 | 0x46f545683d8494ef4c54b7ea40ca762c620846ef |
| YT address | 0xaf67341456151ab8c270e0962966092181c2eb80 | 0x11456849c38ea4af212ab8d4324b39983716516a | 0x9adc5ff64705ccedf6ba61cdac124a720c0ff902 | 0x82533d15d76f498de4f50858f9a86ad3b22c752d |
| PT address | 0xc9d24ad0bb25f34098e226a8c5192dea7bacccae | 0xb459db106f645d698e74027eef6019a26a0675cc | 0xe9d07c2a3588b9a25edd55664be44ecfe5f92fce | 0xfaf260b16d3fa1609c74799089ad3cedfcd703fc |
| SY | SY-USDai 0x5edcbc20…5b82 | SY-sUSDai 0x30ccf4bb…2f62 | SY-sUSDai 0x30ccf4bb…2f62 | SY-USDai 0x5edcbc20…5b82 |
| Maturity (UTC) | 2026-10-15 00:00 | 2026-10-15 00:00 | 2027-02-25 00:00 | 2027-02-25 00:00 |
| Days to expiry | 16.51 | 16.51 | 149.51 | 149.51 |
| YT price USD | $0.0043264 | $0.0052481 | $0.0411358 | $0.0291476 |
| YT price in USDai | 0.0043252 | 0.0052467 | 0.0411250 | 0.0291396 |
| PT price USD | $0.9959463 | $0.9950245 | $0.9591368 | $0.9711251 |
| Implied APY | 10.058% | 12.335% | 10.796% | 7.487% |
| Underlying APY (Pendle) | 0% | 7.575% | 7.575% | 0% |
| Implied − underlying | +10.058 pp | +4.760 pp | +3.221 pp | +7.487 pp |
| Pool liquidity | $50,348,682 | $11,407,000 | $3,990,126 | $56,933 |
| Total TVL (incl. floating PT) | $89,703,295 | $63,641,078 | $6,779,012 | $1,944,018 |
| 24h volume | $181,217 | $463,029 | $697,004 | $0 |
| Points shown on Pendle (`points` field) | USD.AI multiplier **25** | USD.AI multiplier **12** | USD.AI multiplier **12** | USD.AI multiplier **25** |
| YT gets underlying yield? | **No** (USDai has 0 yield; `ytApyBreakdown` Protocol Yield = 0) | **Yes**, sUSDai staking yield 7.575% | **Yes**, 7.575% | **No** |
| Pendle `ytRoi` (API) | −1.000 | −0.4011 | −0.2986 | −1.000 |
| Pendle yieldRange (AMM range) | 4%–32% | 4%–38% | 3%–13% | 3%–15% |
| isPrime | true | true | false | false |
| LP aggregatedApy | 2.34% | 8.83% | 10.92% | 2.77% |
| totalPt / totalSy in pool | 11.30M / 39.08M | 2.75M / 7.77M | 3.17M / 0.85M | 21.2K / 36.4K |
| Output token on exit | USDai or PYUSD | **sUSDai only** | **sUSDai only** | USDai or PYUSD |

- Pendle's own market text for USDai markets: "USDai … does not earn any yield from loans originated by the protocol but earns additional points". Its `ytApyBreakdown` "Protocol Yield" is 0 for both USDai markets and 0.07575 for both sUSDai markets. — [Pendle API v2 markets/all](https://api-v2.pendle.finance/core/v2/markets/all?limit=100&skip=0)
- sUSDai market `conversionRate`: 1 sUSDai = 1.1153153902 "USDai staked in USD.AI". — [Pendle API v2 markets/all](https://api-v2.pendle.finance/core/v2/markets/all?limit=100&skip=0)
- The 24h change fields show activity moving to the Feb-2027 sUSDai market. For sUSDai-Feb: `tradingVolumeChange24h` = +16.0 (i.e. +1,600%), `impliedApyChange24h` = +0.0894 (relative, ≈ 9.91% → 10.80%), `liquidityChange24h` = +3.1%. For sUSDai-Oct: `impliedApyChange24h` = +0.49% relative. For USDai-Oct: `tradingVolumeChange24h` = −90%. — [Pendle v1 detail sUSDai-Feb](https://api-v2.pendle.finance/core/v1/42161/markets/0xf86119a39f8654f38acbbd5488bd83f3f51983c8)
- DefiLlama cross-check (same time): PT-USDai-15OCT2026 at 10.10% (30d mean 9.06%); PT-sUSDai-15OCT2026 at 12.33% (30d mean 11.48%); PT-sUSDai-25FEB2027 at 10.87% (30d mean 10.00%). The sUSDai vault itself (Arbitrum) shows TVL $509.6M, APY 7.49%, 30d mean 7.11%, labelled "30d unlock". — [DefiLlama yields pools](https://yields.llama.fi/pools)

**Expired USD.AI markets (all show impliedApy 0 or −1 now)** — [Pendle API inactive Arbitrum](https://api-v2.pendle.finance/core/v1/42161/markets/inactive); [v2 markets/all](https://api-v2.pendle.finance/core/v2/markets/all?limit=100&skip=0)

| Market | Chain | Address | Maturity | Pendle points value |
|---|---|---|---|---|
| USDai | Arbitrum | 0x8e101c690390de722163d4dc3f76043bebbbcadd | 2025-11-20 | 25 |
| sUSDai | Arbitrum | 0x43023675c804a759cbf900da83dbcc97ee2afbe7 | 2025-11-20 | 12 |
| USDai | Arbitrum | 0x3308574370f19ea639f4671838e01cfb77d8db70 | 2026-02-19 | 15 |
| sUSDai | Arbitrum | 0x2092fa5d02276b3136a50f3c2c3a6ed45413183e | 2026-02-19 | 12 |
| USDai | Plasma | 0x15735f2f53c5cd25a57dff83b11c93eceaf72073 | 2026-03-19 | 15 |
| sUSDai | Plasma | 0x0d7d9abee602c7f0a242ea7e200e47c372acba84 | 2026-03-19 | 12 |
| USDai | Arbitrum | 0x8a8a557b90ec79496a18a1f9c9da8bbd7db86fd3 | 2026-06-18 | 25 |
| sUSDai | Arbitrum | 0x299674f6da858f903d77486fba50bc9f2e0db24d | 2026-06-18 | 12 |

### Inferences
- A points farmer realistically has only the two Oct-2026 markets (deep liquidity) and sUSDai-Feb-2027 ($4M liquidity) to choose from. USDai-Feb-2027 ($57K liquidity, $0 volume) is usable only for very small tickets; a $1,000 trade is probably fine, but price impact was not measured.
- For the sUSDai markets, YT redemption and the exit token are sUSDai only. Converting back to stablecoins then needs the 30-day unstake epoch or a DEX swap.

### Gaps
- The Pendle app UI was not rendered (JS app). The multiplier "as shown on Pendle" comes from the API `points` field that feeds the UI, not from a screenshot.
- Price impact for a $1,000 buy in each YT was not simulated. The Pendle SDK/route quote endpoint was not called.

---

## Q2. YT economics per market: leverage, net cost of points, implied points premium, per-$1,000 outcome

### Takeaway
At current prices the market charges almost the **same price per point-unit in both Oct-2026 markets: about $1.10–1.12 × 10⁻⁵ per 1x-$-day**. USDai-YT is 100% points cost. sUSDai-YT gets back ~60% of its price as yield, so its net cost is about 40%. Per $1,000:
- **YT-USDai-Oct**: all $1,000 is spent on about 90.6M point-units.
- **YT-sUSDai-Oct**: about $599 of yield comes back and about $401 buys about 35.9M point-units.
- **Feb-2027 YTs**: priced cheaply per point **only if** points keep accruing after Season 2 ends (Oct 14, 2026). If points stop at Season 2's end, the Feb-2027 YTs are about 6–7x more expensive per point than the Oct YTs.

### Cited Findings
- Price, APY and day inputs are from the Pendle API snapshot in Q1. — [Pendle v1 market detail](https://api-v2.pendle.finance/core/v1/42161/markets/0xa8a0dea40174cfc30fea9e3a77f182ab33f46e25)
- Multipliers: USD.AI app "Buy YT" rates are 25 (USDai-14OCT and 24FEB) and 12 (sUSDai-14OCT and 24FEB). These match Pendle's `points` values. — [USD.AI rewards page (SSR data)](https://app.usd.ai/rewards); [Pendle API v2](https://api-v2.pendle.finance/core/v2/markets/all?limit=100&skip=0)
- 5% Pendle fee on YT yield and points: "5% of yield / points from Pendle YT markets go to the Pendle Treasury, which is standard across all Pendle markets." — [USD.AI docs, Pendle FAQ (llms-full)](https://docs.usd.ai/llms-full.txt)
- Pendle's API `ytRoi` for sUSDai-Oct is −0.40106 and for sUSDai-Feb is −0.29865. These match my fee-inclusive yield calculation below (−40.1% and −29.9%), so Pendle's ytRoi already includes the 5% fee and assumes a constant underlying APY. — [Pendle v1 detail](https://api-v2.pendle.finance/core/v1/42161/markets/0xcbf629c8d396b1261f81f55175afa010e94787d8)

**Formulas**
- Leverage (underlying exposure per $1) = 1 / YT_in_USDai
- Expected yield per YT to maturity (compounded) = (1 + underlyingAPY)^(days/365) − 1. After the Pendle fee: × 0.95. (Simple version: APY × days/365.)
- Net cost of points per YT = YT_in_USDai − net yield per YT
- Points premium = impliedAPY − underlyingAPY
- Point-units per YT = multiplier × days × 0.95
- Breakeven value per point-unit = net cost per YT / point-units per YT

**Per-market calculations**

1) **YT-USDai-15OCT2026** (25x, no yield)
- YT = 0.0043264 / 1.0002727 = 0.0043252 USDai. Leverage = 1/0.0043252 = **231.2x**
- Yield = 0. Net cost = 0.0043252 (100% of the price). Premium = 10.058 − 0 = **10.058 pp**
- Point-units per YT = 25 × 16.5076 × 0.95 = 392.06. Breakeven = 0.0043252 / 392.06 = **$1.103e-5 per 1x-$-day** (= 249 CHIP per 1M units at CHIP $0.044279)
- Per $1,000: 1000 / 0.0043264 = **231,141 YT** (notional $231,204). Yield $0. Loss excluding points −$1,000 (−100%). Points = 231,141 × 392.06 = **90.62M units**. Holding $1,000 USDai at 8x for 16.51 d gives 132,061 units, so the YT gives **~686x** more points.

2) **YT-sUSDai-15OCT2026** (12x, sUSDai yield flows to YT)
- YT = 0.0052467 USDai. Leverage = **190.6x**
- Yield per YT: simple 0.07575 × 16.5076/365 = 0.003426; compounded (1.07575)^(16.5076/365) − 1 = 0.003308; after fee = **0.003142**
- Net cost = 0.0052467 − 0.003142 = **0.002104 USDai** (40.1% of price). Premium = 12.335 − 7.575 = **4.760 pp**
- Point-units per YT = 12 × 16.5076 × 0.95 = 188.19. Breakeven = 0.002104 / 188.19 = **$1.118e-5 per unit** (= 252.5 CHIP per 1M units)
- Per $1,000: **190,546 YT** (notional $190,598). Expected yield **$598.94**. Loss excluding points **−$401.06 (−40.1%)**. Points = **35.86M units**. Holding $1,000 sUSDai at 2x gives 33,015 units, so the YT gives **~1,086x** more.
- Breakeven underlying APY with zero value for points: (1 + YT/0.95)^(365/days) − 1 = **12.95%**. Current is 7.575%.
- Sensitivity of the per-$1,000 yield to sUSDai APY:

| sUSDai APY | Yield | Loss excluding points |
|---|---|---|
| 5% | $399.98 | −$600.02 |
| 6% | $477.79 | −$522.21 |
| 7.575% | $598.94 | −$401.06 |
| 9% | $707.09 | −$292.91 |
| 10% | $782.18 | −$217.82 |

3) **YT-sUSDai-25FEB2027** (12x)
- YT = 0.0411250 USDai. Leverage = **24.3x**
- Yield: simple 0.031028; compounded 0.030361; after fee **0.028843**
- Net cost = 0.041125 − 0.028843 = **0.012282** (29.9% of price). Premium = 10.796 − 7.575 = **3.221 pp**
- Point-units per YT, if points accrue only to the end of Season 2 (16.51 d): 188.19. Breakeven = **$6.526e-5 per unit** (1,474 CHIP per 1M units)
- If points continue at 12x to maturity (149.51 d): 1,704.39 units. Breakeven = **$7.206e-6 per unit**
- Per $1,000: **24,310 YT**. Yield **$701.35**. Loss excluding points **−$298.65 (−29.9%)**. Points: 4.57M units (Season 2 only) or 41.43M units (to maturity).
- Breakeven underlying APY with zero value for points: **10.90%**
- Sensitivity of the per-$1,000 yield to sUSDai APY:

| sUSDai APY | Yield | Loss excluding points |
|---|---|---|
| 5% | $466.31 | −$533.69 |
| 6% | $557.98 | −$442.02 |
| 9% | $829.99 | −$170.01 |
| 10% | $919.68 | −$80.32 |

4) **YT-USDai-25FEB2027** (25x)
- YT = 0.0291396 USDai. Leverage = **34.3x**. Yield 0. Net cost = 100%. Premium = **7.487 pp**
- Point-units per YT: 392.06 (Season 2 only) or 3,550.81 (to maturity). Breakeven = **$7.433e-5** (Season 2 only) or **$8.206e-6** (to maturity)
- Per $1,000: **34,308 YT**. Yield $0. Points: 13.45M units (Season 2 only) or 121.82M units (to maturity).

**The "Lock YT" option on USD.AI raises the multiplier.** The USD.AI app lists these Lock YT rates — [USD.AI rewards page](https://app.usd.ai/rewards):

| YT | Buy-and-hold rate | Lock rate |
|---|---|---|
| USDai-14OCT | 25 | 30 |
| sUSDai-14OCT | 12 | 15 |
| USDai-24FEB | 25 | 40 |
| sUSDai-24FEB | 12 | 20 |

Breakeven per unit if locked (scaled by old/new multiplier):

| YT | Breakeven if locked |
|---|---|
| USDai-Oct | 9.19e-6 |
| sUSDai-Oct | 8.94e-6 |
| USDai-Feb | 5.13e-6 (to maturity) or 4.65e-5 (Season 2 only) |
| sUSDai-Feb | 4.32e-6 (to maturity) or 3.92e-5 (Season 2 only) |

### Inferences
- The market is efficient between the Oct pairs. The implied price per point-unit is $1.103e-5 for USDai-YT and $1.118e-5 for sUSDai-YT, within 1.4%, so neither Oct YT is clearly "cheaper" for points. USDai-YT has no yield risk but gives zero residual value. sUSDai-YT returns ~60% as yield but carries sUSDai APY and loan-default risk; a ±1.5 pp APY swing moves the per-$1,000 result by about ±$110.
- The Feb-2027 YTs price points at ~$7.2–8.2e-6 per unit *if* accrual continues after Oct 14. That is ~26–35% cheaper than the Oct YTs, which is consistent with the market pricing some probability that a post-Season-2 program continues at similar rates. If Season 2 is the last program, Feb YT buyers overpay by ~6–7x per point.
- A buyer is profitable only if the realized Allo → CHIP value exceeds ~$1.1e-5 per 1x-$-day (Oct YTs). At CHIP = $0.04428 that means about **250 CHIP per 1M point-units**. Holding $1,000 of USDai at 8x for 16.5 d earns only ~132K units, so this threshold is equivalent to plain USDai holders earning ~33 CHIP (~$1.46) per $1,000 over the same 16.5 days, i.e. ~3.2% annualized in CHIP. That annualization is derived here, not sourced.

### Gaps
- **Allo points → CHIP conversion is unknown.** No official Season 2 pool size (CHIP amount) or total Allo supply was found, so the fair value per point-unit cannot be computed. Only the market-implied breakeven above is available.
- It is unconfirmed whether USD.AI's "25x/12x" means Allo per YT unit (1 USDai notional) per day. That is Pendle's standard convention and consistent with USD.AI's "APR = rewards / YT notional" guidance, but the absolute Allo unit per $1-day at 1x was not confirmed.
- It is unconfirmed whether the 5% Pendle fee is already netted out of USD.AI's displayed 25x/12x. I applied it (×0.95) conservatively.
- Lock YT terms were not fully verified: whether a lock is reversible, and the exact decay schedule. The docs say only "rates decrease over time" and "rate is locked per deposit".

---

## Q3. Historical moves (past ~1–4 months) and outcomes of expired USDai/sUSDai maturities

### Takeaway
Over June–September 2026, implied APY in the Oct-2026 markets **rose** as maturity approached:
- USDai-Oct: 6.2–7.2% → 10.06%
- sUSDai-Oct: ~9.5% → 12.33%

Meanwhile sUSDai's underlying APY stayed at 7.1–9.0%. The implied cost per point-unit in the Oct markets therefore **rose from ~2–8e-6 to ~1.04–1.07e-5**: late-season buying is paying more per point. For expired markets, every USDai-YT went to 0 (a pure points purchase). sUSDai-YT buyers typically lost **~23–60% before points** because implied APYs (7.7–30%) exceeded realized sUSDai yield (6.1–11.4%). The one near-breakeven case was an entry 90 days before the Jun-2026 expiry.

### Cited Findings
Source for all rows: Pendle historical-data v3 (daily, fields impliedApy, underlyingApy, ytPrice, ptPrice, syPrice, tvl, totalTvl, tradingVolume) — [sUSDai-Oct history](https://api-v2.pendle.finance/core/v3/42161/markets/0xcbf629c8d396b1261f81f55175afa010e94787d8/historical-data?time_frame=day&timestamp_start=2026-06-01T00:00:00Z&timestamp_end=2026-09-28T12:00:00Z&fields=timestamp,impliedApy,underlyingApy,ytPrice,ptPrice,syPrice,tvl,totalTvl,tradingVolume,ytFloatingApy); same pattern for other addresses.

**USDai-15OCT2026** (implied %, YT $, pool TVL $M):

| Date | Implied | YT $ | Pool TVL $M |
|---|---|---|---|
| 06-01 | 6.76% | 0.02392 | 0.78 |
| 06-22 | 6.27% | 0.01881 | 50.51 (pool jumped from $0.35M to $50.5M around 06-22) |
| 07-13 | 6.34% | 0.01553 | 50.38 |
| 08-03 | 6.56% | 0.01245 | 50.38 |
| 08-24 | 7.11% | 0.00955 | 50.29 |
| 09-07 | 8.75% | 0.00846 | 50.30 |
| 09-14 | 8.82% | 0.00692 | 50.31 |
| 09-21 | 10.00% | 0.00599 | 50.31 |
| 09-28 | 10.06% | 0.00433 | 50.35 |

- USDai-15OCT2026 had a 24h-volume spike of $13.95M on 2026-09-21. Total TVL grew from $61.6M (Jul) to $89.7M (Sep 28).

**sUSDai-15OCT2026** (implied / underlying %, YT $):

| Date | Implied | Underlying | YT $ |
|---|---|---|---|
| 06-01 | 9.49% | 6.56% | 0.03298 |
| 06-29 | 9.01% | 8.39% | 0.02498 |
| 07-27 | 9.80% | 7.94% | 0.02004 |
| 08-24 | 10.31% | 8.12% | 0.01362 |
| 09-07 | 11.49% | 7.53% | 0.01096 |
| 09-21 | 12.12% | 7.17% | 0.00719 |
| 09-28 | 12.33% | 7.58% | 0.00525 |

- sUSDai-15OCT2026 pool TVL was stable at $11–14.6M.

**sUSDai-25FEB2027** (launched 2026-06-16; implied / underlying %, YT $):

| Date | Implied | Underlying | YT $ |
|---|---|---|---|
| 06-16 | 9.70% | 1.21% (launch artifact) | 0.06214 |
| 07-07 | 9.66% | 8.16% | 0.05693 |
| 08-04 | 9.28% | 8.60% | 0.04836 |
| 09-01 | 9.64% | 8.50% | 0.04339 |
| 09-15 | 9.89% | 7.22% | 0.04099 |
| 09-22 | 9.86% | 7.18% | 0.03916 |
| 09-28 | 10.80% | 7.58% | 0.04114 |

- sUSDai-25FEB2027 pool TVL grew from $0.05M to $3.99M.

**USDai-25FEB2027**: implied 6.7–7.6% the whole time. YT fell from $0.04582 (06-16) to $0.02915 (09-28). Pool TVL stayed at ~$0.06M.

**Implied cost per point-unit over time** (my calculation: (YT − 0.95 × expected yield) / (mult × days × 0.95), assuming constant 25x/12x; historical multipliers were not verified):

| Market | Series |
|---|---|
| USDai-Oct | 7.87e-6 (06-16) → 6.81e-6 (07-01) → 7.16e-6 (08-01) → 8.85e-6 (09-01) → 9.40e-6 (09-14) → 1.05e-5 (09-21) → 1.07e-5 (09-28) |
| sUSDai-Oct | 5.59e-6 (06-16) → 2.13e-6 (07-01) → 3.14e-6 (08-01) → 5.58e-6 (09-01) → 8.48e-6 (09-14) → 1.04e-5 (09-21/28) |
| USDai-Feb (to-maturity basis) | flat 7.3–8.2e-6 |
| sUSDai-Feb (to-maturity basis) | 0.6–2.8e-6 in Jul–Aug → 6.1–7.1e-6 in mid/late Sep |

**Expired markets: realized outcome of buying YT at 90 / 60 / 30 days before expiry.** Yield is measured with the sUSDai/USDai exchange rate = sUSDai syPrice ÷ USDai syPrice. This avoids the USDai premium distortion of Sep–Oct 2025, when USDai traded up to $1.033. Net yield = 0.95 × rate growth. Source: [sUSDai-Nov-2025 history](https://api-v2.pendle.finance/core/v3/42161/markets/0x43023675c804a759cbf900da83dbcc97ee2afbe7/historical-data?time_frame=day&timestamp_start=2025-06-01T00:00:00Z&timestamp_end=2026-09-28T12:00:00Z&fields=timestamp,impliedApy,underlyingApy,ytPrice,ptPrice,syPrice,tvl,totalTvl,tradingVolume) and the equivalent URLs for the other expired addresses.

| Market | Entry | Implied at entry | Realized sUSDai APY | YT (USDai) | Net yield / YT | ROI excluding points |
|---|---|---|---|---|---|---|
| sUSDai-20NOV2025 | 90d (08-22) | 15.27% | 10.37% | 0.03406 | 0.02313 | −32.1% |
| sUSDai-20NOV2025 | 60d (09-21) | 22.08% | 11.41% | 0.03174 | 0.01674 | −47.3% |
| sUSDai-20NOV2025 | 30d (10-21) | 30.06% | 11.35% | 0.02067 | 0.00815 | −60.6% |
| sUSDai-19FEB2026 | 90d | 17.68% | 7.23% | 0.03892 | 0.01630 | −58.1% |
| sUSDai-19FEB2026 | 60d | 12.99% | 6.51% | 0.01955 | 0.00974 | −50.2% |
| sUSDai-19FEB2026 | 30d | 12.55% | 6.15% | 0.00935 | 0.00451 | −51.7% |
| sUSDai-19MAR2026 (Plasma) | 90d | 13.41% | 6.44% | 0.03022 | 0.01457 | −51.8% |
| sUSDai-19MAR2026 (Plasma) | 60d | 10.75% | 6.18% | 0.01638 | 0.00925 | −43.5% |
| sUSDai-19MAR2026 (Plasma) | 30d | 7.72% | 6.17% | 0.00589 | 0.00453 | −23.1% |
| sUSDai-18JUN2026 | 90d (03-20) | 6.54% | 6.63% | 0.01533 | 0.01499 | **−2.2%** |
| sUSDai-18JUN2026 | 60d | 9.91% | 6.99% | 0.01516 | 0.01044 | −31.2% |
| sUSDai-18JUN2026 | 30d | 9.53% | 7.05% | 0.00721 | 0.00515 | −28.5% |
| All USDai-YT markets (Nov-25, Feb-26, Mar-26 Plasma, Jun-26) | any | 5.0–33.7% | 0 | — | 0 | −100% (all value from points) |

- Peak sizes of the expired markets:

| Market | Pool TVL peak | Total TVL peak | Implied APY at peak |
|---|---|---|---|
| USDai-Nov-2025 | $141.8M | $264.3M | up to 42.4% (2025-10-14) |
| sUSDai-Nov-2025 | $77.5M | — | up to 35.9% |
| USDai-Feb-2026 | $83.6M | — | 7.6–13% |
| sUSDai-Feb-2026 | $92.0M | $238.8M | 12.5–19% |

- Pendle multipliers on expired markets: USDai-Nov-25 = 25, Feb-26 = 15, Plasma Mar-26 = 15, Jun-26 = 25; sUSDai = 12 throughout. Pendle's market notes say "USD.AI points for this pool has been updated to 15x [USDai] / 12x [sUSDai] since 19 Nov 2025", and older USDai notes say "10x since 19 Nov 2025". These notes appear stale or inconsistent with the `points.value` field. — [Pendle API v2 markets/all (marketInfo.importantQuirks)](https://api-v2.pendle.finance/core/v2/markets/all?limit=100&skip=0)

### Inferences
- Pattern: implied APY in USD.AI YT markets **rises into maturity**. This is partly a mechanical small-denominator effect and partly late-season demand for points, so late buyers pay the most per point. The current Oct-2026 price per unit (~1.1e-5) is the highest in the Jun–Sep window. For USDai-Oct it is ~50–57% above July–August (6.8–7.2e-6). For sUSDai-Oct it is ~2.4–4.9x July–August (2.1–4.4e-6).
- Across 12 sUSDai-YT entry points in 4 expired maturities, 11 lost 23–61% before points. The realized sUSDai APY (6.1–11.4%) was consistently below the implied APY at entry, so YT buyers were systematically paying for points.
- Realized sUSDai APY has drifted down from ~10–11% (Aug–Nov 2025) to ~6.2–7.1% (Dec 2025 – Jun 2026), then back up to ~7.6–7.8% (Jun–Sep 2026).

### Gaps
- Season 1 Pendle multipliers were not verified historically beyond Pendle's current `points` field and the stale quirk notes.
- The realized CHIP value that Season 1 YT holders received per point (i.e. whether points justified the ~50% pre-points losses) could not be computed: Season 1 total Allo and per-wallet conversion were not found.
- The OHLCV endpoint (`/v4/{chainId}/prices/{address}/ohlcv`) was not pulled; daily historical-data was used instead.

---

## Q4. What do Pendle and USD.AI say about points multipliers for YT and LP, LP dilution by PT, caps, and the points program timeline?

### Takeaway
Points are USD.AI **Allo** points, in **Season 2 ("Flatiron") running through October 14, 2026**. Rewards are distributed as **$CHIP airdrops**. Current Allo rates from the USD.AI app:
- Buy YT: USDai **25x**, sUSDai **12x**
- Lock YT: USDai-Oct **30x**, USDai-Feb **40x**, sUSDai-Oct **15x**, sUSDai-Feb **20x**
- Pendle LP: **16x**
- Plain holding: USDai **8x**, sUSDai **2x**

Pendle streams points to YT; PT earns none, so LP earns only on its non-PT (SY) share. Pendle keeps 5%. No explicit point cap was found. Nothing official was found about a program after October 14, 2026, which is critical for the Feb-2027 YTs.

### Cited Findings
- **Season 2 timing**: "Allo Game Season 2 (Flatiron) … runs through October 14, 2026". All rewards are distributed via $CHIP airdrops, multipliers range from 1x to 40x depending on strategy, and users can "buy or lock YTs and LPTs on Pendle". — [USD.AI "$CHIP Is Live" (Apr 22, 2026)](https://usd.ai/insights/chip-is-live)
- Season 2 "ends October 14, 2026". — [USD.AI insights listing / search summary](https://usd.ai/insights)
- **Current Allo rates** (`alloRate` field in the rewards-page data, fetched 2026-09-28) — [USD.AI rewards](https://app.usd.ai/rewards):

| Strategy | Allo rate |
|---|---|
| Buy YT-USDai-14OCT | 25 |
| Buy YT-USDai-24FEB | 25 |
| Buy YT-sUSDai-14OCT | 12 |
| Buy YT-sUSDai-24FEB | 12 |
| Lock YT-USDai-14OCT | 30 |
| Lock YT-USDai-24FEB | 40 |
| Lock YT-sUSDai-14OCT | 15 |
| Lock YT-sUSDai-24FEB | 20 |
| Buy LPT (all four Pendle markets) | 16 |
| Hold USDai (Arbitrum/Base/Ethereum/Plasma) | 8 |
| Hold sUSDai | 2 |
| Curve/Fluid/Aerodrome LPs | 16 |
| Gamma USDai-USDC | 20 |
| CHIP-USDC LP | 30 |
| sCHIP | 10 |
| Expired 17-JUN and Plasma 18-MAR entries | 0 |

- USD.AI labels the Pendle maturities as 14-OCT / 24-FEB, while Pendle uses 15-OCT / 25-FEB 00:00 UTC.
- **Pendle side**: the `points` field for each market is `{key: "USD.AI", type: "multiplier", pendleAsset: "basic", value: 25 or 12}`; some entries add `perDollarLp: false`. — [Pendle API v2 markets/all](https://api-v2.pendle.finance/core/v2/markets/all?limit=100&skip=0)
- Pendle doc wording: "Pendle streams the points and yields to YT holders"; "LPs consist of PT and its underlying" and "PT does not earn points". Also: "Pendle does NOT give nor generate additional points to enable YT's leverage. Pendle simply streams points from the underlying to YT holders." — [Pendle Points Support Page](https://docs.pendle.finance/pendle-academy/ecosystem-and-resources/points-trading/points-support-page)
- Pendle collects a 5% fee from all yield (including points) accrued by YT. — [Pendle Fees docs (via search summary)](https://docs.pendle.finance/pendle-v2/ProtocolMechanics/Mechanisms/Fees); USD.AI confirms "5% of yield / points from Pendle YT markets go to the Pendle Treasury". — [USD.AI docs (llms-full)](https://docs.usd.ai/llms-full.txt)
- **Lock YT mechanics**: locked-YT Allo rates **decay over time**; each deposit uses the current rate, and wallet-level rates are blended by weighted average (example: 500k YT at 22x + 500k at 20x = 21x), and "once blended, it does not revert". Locked YTs stop receiving yield on Pendle; yield accumulates in USD.AI's Lock YT contract and is "automatically distributed … in batches (about every 20 days)". The "Allo rate IS locked per deposit". — [USD.AI docs Pendle FAQ (llms-full)](https://docs.usd.ai/llms-full.txt)
- USD.AI guidance on YT APR: "APR = rewards / YT notional"; "What matters is IY (Implied Yield), true economic cost of entering YT"; "YT goes to zero at maturity". — [USD.AI docs Pendle FAQ (llms-full)](https://docs.usd.ai/llms-full.txt)
- Allo points update ~hourly. They are wallet-based and non-transferable. They **stop accruing once you submit an sUSDai unstake request**, while yield continues until the scheduled unstake date. Multipliers "are adjusted … always announced publicly ahead of time". — [USD.AI docs Allo FAQ (llms-full)](https://docs.usd.ai/llms-full.txt)
- Earlier Allo structure (Season 1): USDai = "ICO" alignment (5x base, KYC and purchase required, 70% of the sale allocation), sUSDai = "Airdrop" alignment (2x base, free, 30%). Strategy tiers were Basic < Auto/Boost (Pendle LP) < Max/Lock (YT). — [USD.AI docs allo-points.md](https://docs.usd.ai/app-guide/depositor/allo-points.md)
- Pendle's market notes for the current markets still say: USDai-market points "entitle you to allocation to purchase USD.AI tokens during TGE… KYC is required", and sUSDai-market points "entitle you to airdrop … No KYC is required". — [Pendle API v2 markets/all (marketInfo)](https://api-v2.pendle.finance/core/v2/markets/all?limit=100&skip=0). This conflicts with the post-TGE statement that all Season 2 rewards are $CHIP airdrops — [USD.AI "$CHIP Is Live"](https://usd.ai/insights/chip-is-live). The Pendle notes look like stale Season 1 text.
- **CHIP token**: TGE was April 21, 2026, per USD.AI's own post — [USD.AI "$CHIP Is Live"](https://usd.ai/insights/chip-is-live). This contradicts an aggregator's "March 30, 2026" — [MEXC Learn](https://www.mexc.com/learn/article/what-is-usd-ai-crypto-usdai-susdai-chip-token-and-allo-points-explained/1).
- Level Up ICO participants had protected CHIP unlocking at YT maturities June 17, 2026 and October 14, 2026, settled at $270M / $190M FDV. — [USD.AI "$CHIP Is Live"](https://usd.ai/insights/chip-is-live)
- CHIP price on 2026-09-28 11:51 UTC:

| Metric | Value |
|---|---|
| Price | $0.04427893 |
| Market cap | $88.6M |
| FDV | $442.8M |
| Circulating supply | 2.0B |
| Total supply | 10B |
| 30d change | +7.7% |
| 7d change | −10.8% |
| ATH | $0.1402 (2026-04-23) |

  Source: [CoinGecko API chip-2](https://api.coingecko.com/api/v3/coins/chip-2). An aggregator states a total supply of 1B — [MEXC Learn](https://www.mexc.com/learn/article/what-is-usd-ai-crypto-usdai-susdai-chip-token-and-allo-points-explained/1). This conflicts with CoinGecko's 10B; CoinGecko's figure is consistent with the $270M/$300M FDV figures.
- Tokenomics: 27.5% of CHIP is for ecosystem bootstrapping. "The first 10% was distributed during Season 1 (The Allo Game)"; the remainder funds "airdrops, upcoming incentive programs". — [USD.AI docs Tokenomics (llms-full)](https://docs.usd.ai/llms-full.txt)
- May 2026: USD.AI "launches the Allo Points API and completes a full Season 2 XP audit. Six fixes made. Net +10.2% gain." — [USD.AI insights](https://usd.ai/insights)

### Inferences
- **LP vs YT**: on the Pendle side, LP earns points only on the SY (underlying) share, not the PT share. USD.AI sets a flat 16x for Pendle LPT. The base it applies 16x to (LP $ value vs. SY share) is not stated; `perDollarLp: false` in Pendle's API suggests it is *not* per dollar of LP. In the USDai-Oct pool the SY share is 39.08M SY vs 11.30M PT, so ~78% of pool assets earn points. In sUSDai-Feb only ~21% (0.85M SY vs 3.17M PT). Treat this as an interpretation, not a confirmed formula.
- **Critical timing risk**: Season 2 ends October 14, 2026, effectively the same day the Oct YTs mature. Oct-YT buyers today get ~16.5 days of Season 2 points. Feb-2027 YT buyers get the same 16.5 days of Season 2 points, plus whatever a later season pays (unannounced).
- No explicit cap on Pendle points or per-wallet points was found. The practical constraint is the unknown total Allo supply that the Season 2 CHIP pool is divided among.

### Gaps
- No official Season 2 CHIP pool size and no Season 3 announcement were found. The Medium article "Season 2 Points" returned HTTP 403. The Allo Google Sheet (master multiplier sheet) was not accessible.
- The exact Allo unit (Allo per $ per day at 1x) was not confirmed.
- It is unknown whether Season 2 points are claimable/airdropped immediately after October 14 or vest.

---

## Q5. sUSDai mechanics relevant to YT (exchange-rate growth, APY variability, redemption queue)

### Takeaway
sUSDai is a price-accruing vault token: yield flows through the sUSDai→USDai exchange rate, currently 1.11532. Its APY is **variable**: Pendle's underlying APY ranged 7.14–9.03% since June 30 and averaged 7.57% over the last 30 days. It is funded by GPU-backed loans at 7–15% APR, T-bills and a 4.5% PayPal PYUSD incentive. Exits use a **30-day global epoch with a FIFO queue** limited by cash. Points stop once an unstake is requested. YT-sUSDai holders are exposed to APY changes and to loan-default risk (negative yield possible), and redeem into sUSDai, not stables.

### Cited Findings
- Exchange-rate growth measured from Pendle history: sUSDai USD price 1.08877 (06-01) → 1.11562 (09-28), i.e. +2.466% in 119 d (**7.76% APY**). Over 90 d (06-30 → 09-28): +1.867% (**7.79% APY**). Over 30 d (08-29 → 09-28): +0.601% (**7.56% APY**). Pendle underlyingApy averaged 7.85% since 06-30 (min 7.14%, max 9.03%) and 7.57% over the last 30 d. — [Pendle sUSDai-Oct history](https://api-v2.pendle.finance/core/v3/42161/markets/0xcbf629c8d396b1261f81f55175afa010e94787d8/historical-data?time_frame=day&timestamp_start=2026-06-01T00:00:00Z&timestamp_end=2026-09-28T12:00:00Z&fields=timestamp,impliedApy,underlyingApy,ytPrice,ptPrice,syPrice,tvl,totalTvl,tradingVolume,ytFloatingApy)
- DefiLlama sUSDai (Arbitrum): APY 7.49%, 30d mean 7.11%, TVL $509.6M. — [DefiLlama yields](https://yields.llama.fi/pools)
- Historical exchange rates (sUSDai/USDai, from Pendle syPrice ratios):

| Date | Rate |
|---|---|
| 2025-08-22 | 1.02614 |
| 2025-11-19 | 1.05113 |
| 2026-02-18 | 1.06975 |
| 2026-06-17 | 1.09198 |
| 2026-09-28 | 1.11532 |

  Source: [Pendle history endpoints](https://api-v2.pendle.finance/core/v3/42161/markets/0x2092fa5d02276b3136a50f3c2c3a6ed45413183e/historical-data?time_frame=day&timestamp_start=2025-06-01T00:00:00Z&timestamp_end=2026-09-28T12:00:00Z&fields=timestamp,impliedApy,underlyingApy,ytPrice,ptPrice,syPrice,tvl,totalTvl,tradingVolume)
- Yield delivery: "Yield accrues via the exchange ratio between sUSDai and USDai"; sUSDai uses "rebasing-by-price". The loan rates are "Variable based on LTV and offtake type, ranging from 7-15% APR". Idle capital sits in T-bills as a "yield floor". — [USD.AI docs sUSDai (llms-full)](https://docs.usd.ai/llms-full.txt)
- PayPal provides "a 4.5% annual incentive on PYUSD held in the protocol, on up to $1 billion in loan backing for 2026", which "flows through to sUSDai yield". — [USD.AI docs Partners (llms-full)](https://docs.usd.ai/llms-full.txt)
- **Redemption**: "Redemptions operate on a global 30-day epoch cycle … FIFO queue". The queue closes on day 29 and redemptions are processed on day 30 from available cash. Unfulfilled requests roll to the next epoch. "The protocol does not prematurely terminate or liquidate active GPU loans to satisfy redemptions." QEV auction-based priority is "planned but not yet implemented". — [USD.AI docs sUSDai Redemption (llms-full)](https://docs.usd.ai/llms-full.txt)
- Two price feeds exist: a "Redemption Share Price" (settled repayments) and a "Deposit Share Price" (prorates expected repayments), to prevent yield sniping. — [USD.AI docs sUSDai Withdrawal Estimates (llms-full)](https://docs.usd.ai/llms-full.txt)
- Pendle risk note on the sUSDai pools: "The pool could generate negative yield if the loan that has been originated has defaulted…". The note on the USDai pools says "minimal risk of generating negative yield". — [Pendle API v2 markets/all](https://api-v2.pendle.finance/core/v2/markets/all?limit=100&skip=0)
- USDai is "backed 1:1 by US Treasuries and cash equivalents", minted and redeemed via PYUSD. Direct mint/redeem at contract level moves to whitelisted, KYC-verified market makers from Q2 2026. Pendle's sUSDai market notes say the USDai minting cap was reached, so the Pendle router swaps via DEX (price impact warning). — [USD.AI docs (llms-full)](https://docs.usd.ai/llms-full.txt); [Pendle API v2 marketInfo](https://api-v2.pendle.finance/core/v2/markets/all?limit=100&skip=0)
- The USD.AI Pendle FAQ explains that Pendle's underlying APY is backward-looking ("realized yield over a sample period") while the USD.AI dashboard shows real-time yield, so the two differ. — [USD.AI docs (llms-full)](https://docs.usd.ai/llms-full.txt)

### Inferences
- For YT-sUSDai-Oct (16.5 d), realized yield depends on the few loan repayments that land before Oct 15. Because the vault prorates repayments in deposit pricing and settles in steps, short-window realized APY can deviate noticeably from the 7.575% headline. The history shows day-to-day underlying APY swings of 7.1–9.0%.
- YT-sUSDai redeems and exits into sUSDai. A holder who wants stablecoins either waits one or more 30-day epochs (points stop at request, but that is irrelevant after Season 2 ends) or sells sUSDai on Curve/Fluid at market price.

### Gaps
- Current redemption queue length and epoch position, i.e. how many USDai are queued vs. available cash, were not found.
- The realized share of yield from the PayPal incentive vs. loan interest vs. T-bills was not quantified.
