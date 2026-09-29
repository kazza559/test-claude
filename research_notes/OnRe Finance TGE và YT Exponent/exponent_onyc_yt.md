# Exponent Finance ONyc YT Markets: Live Data, Points Math, Costs (snapshot 2026-09-29 ~06:13–06:19 UTC)

Data provenance note (applies throughout): most numbers below were pulled LIVE on 2026-09-29 between 06:12 and 06:19 UTC from Exponent's own public JSON endpoints used by its web app (found by reading the app's JS bundle), from DefiLlama's yields API, from Jupiter's price API, and from an on-chain simulation using Exponent's published npm SDK (`@exponent-labs/exponent-sdk` + `@exponent-labs/market-three-math` v0.9.29) against Solana mainnet RPC. Endpoints to recompute:
- `https://app.exponent.finance/api/markets?include_frontend_hidden=true` (current v2 markets: ytPriceInAsset, ptPriceInAsset, impliedApy, underlyingApy*, liquidity, maturity, pointsBoost)
- `https://app.exponent.finance/api/implied-apy-chart?vaultAddress=<vault>&timeframeSeconds=31536000` (implied APY / PT / YT price history)
- `https://app.exponent.finance/api/underlying-apy-chart/<SY mint>?timeframeSeconds=31536000` (ONyc exchange-rate/NAV history)
- `https://app.exponent.finance/api/clmm` (CLMM pool balances, fee params), `https://app.exponent.finance/api/points/config` (points multipliers), `https://app.exponent.finance/api/tranching-markets` (srONyc/jrONyc tranche data)
- `https://web-api.exponent.finance/api/markets` (legacy v1 markets incl. expired ONyc maturities)
- `https://yields.llama.fi/pools` (filter project=onre / symbol ONYC)

Key identifiers: ONyc mint `5Y8NV33Vv7WbnLfq3zBcKSdYPrk7g2KoiQoe7M2tcxp5`; SY (wONyc) `G1qbuP11CdquJCzuDjruWqatQAHroajmxhLfeQVgHosF`; ONyc-10JAN27 vault `7f1PgxY3kGsPqLAKpwcduZkcBEhpjMz7U1iJ4pcCCzDy`, CLMM market `9cD4nKmLuM8FMj8Ur1ozbv7C1onZbeavQaJC7uM72eiq`, PT `HH7FiYbEfDwQoK2ZJpkMz1T6wG6TqPsWcxWCtEVgigrZ`, YT `GFpXWuDCm7QMjkYbMveNZoLzybqJaginDDvuX3bJqgLF`; srONyc-10JAN27 vault `y5UFEeB3LfUErLBjDMdZynAoqCwBgsMnDZSzth68aaH`, CLMM `BxyZMXUxxWQripMLR3QRH9FXeRMyGsWqpwj9kr3SGh2S`, YT `2yqH1TaR1zvpMTPAAvrKoAzYp6dJNwczSJ4X9Xqp5tMT`.

## Q1. Which Exponent markets have ONyc / OnRe-related underlying, and what are their live prices, APYs, liquidity?

### Takeaway
As of 2026-09-29 there are exactly two ACTIVE Exponent yield markets on OnRe assets, both maturing 10 Jan 2027 (~103.3 days away): **ONyc-10JAN27** (YT $0.0329 per $1 of principal, PT 0.9671, implied APY 12.55% vs ONyc 7d realized 11.02%, CLMM liquidity ~$3.0M, ~$20.3M of ONyc stripped) and **srONyc-10JAN27** on Exponent's senior-tranche ONyc (YT $0.0216, implied 8.04% vs underlying 7.11%, liquidity ~$0.30M). Three earlier v1 ONyc maturities (25JAN26, 13MAY26, 10SEP26) are expired.

### Cited Findings
**Active market 1: ONyc-10JAN27 (Exponent v2, platform "OnRe", interface "scope")** — all from [Exponent markets API](https://app.exponent.finance/api/markets?include_frontend_hidden=true), fetched 2026-09-29 06:13 UTC; UI page [app.exponent.finance/en/market/income/onyc-10JAN27](https://app.exponent.finance/en/market/income/onyc-10JAN27)
- Maturity: `maturityDateUnixTs` 1799586000 = **2027-01-10 13:00 UTC**; start 1787306400 (2026-08-21), release 2026-08-24. Days to maturity at snapshot: **103.28** (0.2830 yr).
- `ytPriceInAsset` **0.032912**; `ptPriceInAsset` **0.967088**; `impliedApy` **12.555%**; `yieldExposure` (=1/YT price) **30.38x**.
- The "asset" (accounting unit) is **USD** (`quoteAsset` = "US Dollar 9 Decimals"); `syExchangeRate` = **1.15055451 USD per ONyc** (ONyc NAV). So 1 PT redeems $1-worth of ONyc at maturity and 1 YT collects the yield on $1 of ONyc principal. YT price in USD ≈ **$0.03291**; in ONyc terms ≈ 0.02861 ONyc per YT.
- Underlying (ONyc) APY per Exponent: `underlyingApy`/7-epoch **11.020%**, 1-epoch 11.020%, 3-epoch 11.024%, 30-epoch **11.356%**.
- `liquidity` 2,998,283 (USD, 9-dec raw 2998283513997307) ; `clmmInRangeLiquidity` ~2,615,620; `orderbookExecutableDepth` ~11,039,675; `totalMarketSize` **20,277,661** (ONyc stripped into this vault, USD). `volume` field = 0 (not populated).
- CLMM pool (from [Exponent CLMM API](https://app.exponent.finance/api/clmm), 06:12 UTC): sy_balance 1,976,956 wONyc (~$2.27M), pt_balance 748,317 PT; `current_implied_apy` 0.125547; tick_space 2500; `ln_fee_rate_root` 0.001998; `treasury_fee_bps` 3500; LP `tradingFeeApy` (last 7d) 0.298%.
- Orderbook (Rate Order Book) `imv1h6xgX8GyiJjkBj5xvFxwWoB7sCyTGCi6yGK2bZt`, `last_seen_implied_apy` 117427 (≈11.74%), updated 2026-09-28 20:12 UTC — [Exponent orderbooks API](https://app.exponent.finance/api/orderbooks?is_active=true&vault_address=7f1PgxY3kGsPqLAKpwcduZkcBEhpjMz7U1iJ4pcCCzDy&include_frontend_hidden=true)
- Points boost object: platform onrefinance, season 1, points_name "Onre Points", `points_per_day` 1, **`yt_multiplier` 8, `lp_multiplier` 8**, type "sy", `is_external_tracking` true, updated 2026-09-21 — [Exponent markets API](https://app.exponent.finance/api/markets?include_frontend_hidden=true)
- `ytHolderRewardsApy` 0 and `ytHolderRewardCampaigns` [] (no extra Exponent token emissions to YT on this market) — same source.
- PT-ONyc-10JAN27 is also listed as collateral on Kamino ("OnRe Market"), TVL $1,044,509 — [DefiLlama yields](https://yields.llama.fi/pools) (pool 090c06f2-04f3-592a-aed9-da4152b4a73a).

**Active market 2: srONyc-10JAN27 (Exponent Senior Tranche of ONyc, interface "exponentTranching")** — [Exponent markets API](https://app.exponent.finance/api/markets?include_frontend_hidden=true), 06:13 UTC
- Underlying "Exponent Senior ONyc" (srONyc, mint `9J8VvigcjFTkN3jhZH2ieTi2hdGVBVpEXbcA1JDo7QpA`), NAV `syExchangeRate` 1.021746 USD.
- Maturity 1799578800 = **2027-01-10 11:00 UTC** (103.2 days). `ytPriceInAsset` **0.021619**, `ptPriceInAsset` 0.978381, `impliedApy` **8.037%**, yieldExposure 46.26x.
- Underlying APY 7-epoch **7.114%**, 1-epoch 7.227%, 30-epoch 7.407%.
- `liquidity` ~302,932 USD; `totalMarketSize` ~1,864,540; orderbook depth ~1,554,310.
- Points: "OnRe Points", **yt_multiplier 4, lp_multiplier 4**, points_per_day 1, updated 2026-09-23.
- CLMM has an LP farm emitting srONyc (token_rate 1512067, 2026-09-23 → 1792769004 ≈ 2026-10-23) — [Exponent CLMM API](https://app.exponent.finance/api/clmm).
- Tranche structure ([Exponent tranching-markets API](https://app.exponent.finance/api/tranching-markets)): tranching market `HM8iLNE2...` on ONyc started 1781705283 (2026-06-17); market size ~$7.91M; senior NAV $5.47M, junior NAV $2.44M; srLP price 1.021746, jrLP price 1.051171; coverage ratio 0.310 (min 0.2); utilization 64.4%. Junior tranche (jrONyc mint `71j6BZaUPaSG1f1Y3e12KvU66d23kHgzWXhMDHn23wyB`) has no PT/YT market.

**Expired v1 ONyc markets** — [Exponent legacy web-api](https://web-api.exponent.finance/api/markets)
- onyc-25Jan26: start 2025-08-27, maturity 2026-01-25 10:58 UTC; interestFeeBps 550.
- onyc-13May26: start 2026-01-12, maturity 2026-05-13.
- onyc-10Sep26: start 2026-05-03, maturity 2026-09-10 09:58 UTC; 4,706,084 wONyc deposited in vault at last read.
- Launch blog (4 Sep 2025) for the first market: PT "lock in 12%+ APY", LP "12.5%+ APY at launch", YT holders get "continuous yield distributions, boosted OnRe points" — [OnRe blog](https://www.onre.finance/blog/onyc-meets-exponent-real-world-yield-gets-a-defi-upgrade)

**Formulas verified against live data**
- YT price ≈ 1 − PT price (in asset/USD terms): 1 − 0.967088 = 0.032912 ✓.
- Implied APY = (1/PT)^(365/days) − 1 = (1/0.967088)^(1/0.2830) − 1 = 12.555% ✓ (matches API).
- Yield leverage = 1 / YT price = 30.38x (API `yieldExposure`) ✓.
- CLMM "spot price" = 1 + implied APY (1.12555) — [CLMM API](https://app.exponent.finance/api/clmm) and SDK comment "CLMM spot price (1 + decimal APY)" (`@exponent-labs/market-three-math` quote.d.ts).

### Inferences
- The YT on ONyc-10JAN27 is priced at an implied 12.55% vs 11.02% (7d) / 11.36% (30d) realized — i.e., the market pays a ~1.2–1.5pp premium over realized yield, which is the price of the 8x points boost.
- "TVL" for the report: use ~$20.3M ONyc stripped (market size) and ~$3.0M CLMM liquidity for tradability; orderbook adds depth (~$11M "executable depth" as reported by API, meaning unclear—treat cautiously).

### Gaps
- 24h volume: Exponent API `volume` field returns 0 for both v2 markets; DefiLlama has no Exponent project pools. No reliable 24h volume found.
- Birdeye/Solscan not queried; Jupiter price API returns no price for the YT/PT mints (YT "not tradable" on Jupiter).

## Q2. What points do YT holders get; does YT receive full underlying points (leverage = 1/YT price)? Caps?

### Takeaway
Exponent's live config shows ONyc YT (and LP) earn **8x OnRe Points** (srONyc YT: 4x), computed on the YT's notional exposure. That gives ≈ 8 × 30.4 ≈ **243 points per $1 of YT per day** (211 if points are counted per ONyc rather than per USD), vs 0.87 points per $1 per day for just holding ONyc, so roughly **240–280x more points per dollar**. OnRe's own docs still list a generic "Yield tokens 5x" tier — a conflict to flag. PT earns no points. No caps disclosed.

### Cited Findings
- OnRe base rate: "1 point per ONyc, per day"; tiers: wallet 1x, LP 2x, lending 3x–4x, **yield tokens 5x (Exponent YT named)**, leveraged looping 6x; "ONyc Points are not earned on PT tokens within fixed rate markets"; no caps disclosed ("certain campaigns or strategies may have limits"); points "do not represent any entitlement to tokens"; referral 10% / 5% bonus — [OnRe docs: Points Program](https://docs.onre.finance/onyc-in-defi/onre-points-program)
- Exponent live config: ONyc SY `G1qbuP11...` → `points_per_day` 1, `yt_multiplier` **8**, `lp_multiplier` **8**, type "sy", season 1, created 2026-08-24, updated 2026-09-21; srONyc SY `AojEeHMj...` → yt 4x, lp 4x, updated 2026-09-23 — [Exponent points config API](https://app.exponent.finance/api/points/config) and [markets API](https://app.exponent.finance/api/markets?include_frontend_hidden=true)
- The Exponent UI renders the rule as "{ticker} earns {yt_multiplier}x {points_name} per {quoteAsset} of exposure" → "ONyc earns 8x Onre Points per USD of exposure"; tooltip: points are "Non-transferable rewards issued by the underlying asset's protocol… may provide additional returns on top of the underlying APY earned from Yield Tokens" — Exponent app JS bundle (app.exponent.finance `_next/static/chunks`, fetched 2026-09-29)
- `is_external_tracking: true` for OnRe → OnRe (not Exponent) tracks/credits the points — [Exponent points config API](https://app.exponent.finance/api/points/config)
- Exponent docs: "1 YT collects the yield earned by 1 unit of principal"; "Buying YT gives leveraged exposure to future yield at a fraction of the notional cost" — [Exponent docs: Yield Trading Explained](https://docs.exponent.finance/user-documentation/yield-trading-explained)
- Comparable multipliers on other Exponent YTs (context): Re Points 30x, Solstice 15–30x, Apyx 128x, Hylo 2–25x, Dawn 2.4–3x — [Exponent points config API](https://app.exponent.finance/api/points/config)

**Points math (ONyc-10JAN27, spot YT $0.032912, 103.28 days left)**
- Per-USD-exposure basis (matches UI text): 8 pts/YT/day → **243.1 pts per $1 of YT per day**; 826 pts per YT over life; ~25,100 pts per $1 of YT to maturity.
- Per-ONyc basis (if OnRe applies 8x to ONyc-equivalent = 1/1.15055 ONyc per YT): 6.953 pts/YT/day → **211.3 pts per $1 of YT per day**; 718 pts per YT over life; ~21,800 pts per $1 of YT to maturity.
- Holding ONyc directly: 1 pt/ONyc/day = 0.869 pts per $1 per day. YT ≈ 243–280x more points per dollar than spot ONyc.
- srONyc-10JAN27 (YT $0.021619, 4x): 185.0 pts/$/day (USD basis) or 181.1 (per-token basis).

### Inferences
- Because Exponent's config (updated 2026-09-21) is newer and market-specific, the 8x figure is the operative YT multiplier; the OnRe docs' "5x" appears to be a generic/stale tier table. Recommend the report show both (5x as downside).
- Full points leverage holds: YT points are computed on notional principal exposure, so points per $ = multiplier × (1/YT price).

### Gaps
- Whether OnRe credits YT points per USD of exposure or per ONyc-equivalent is not documented publicly (≈13% difference); UI text says "per USD of exposure".
- No public OnRe statement on season 1 end date, caps, or points-to-token conversion.

## Q3. Does the YT holder receive ONyc's yield; how is it paid; how does ONyc yield accrue; realized APY?

### Takeaway
Yes: YT holders receive all ONyc yield on their notional until maturity (net of Exponent's 5.5% yield fee), accruing continuously and claimable as SY/ONyc. ONyc is non-rebasing — yield shows up as NAV/exchange-rate appreciation (1.0388 → 1.1506 USD from Oct-2025 to Sep-2026). Realized ONyc APY: 7d 11.02%, 30d 11.35%, 90d 11.83%, 180d 11.57%.

### Cited Findings
- "Yield Token (YT) – represents all the variable yield generated by the principal until maturity… 1 YT collects the yield earned by 1 unit of principal" — [Exponent docs](https://docs.exponent.finance/user-documentation/yield-trading-explained)
- "Yield traders will always receive their yield and emissions" regardless of liquidity; YT "upon expiry… become worthless" — [Exponent docs: Protocol Risks & Fees](https://docs.exponent.finance/user-documentation/protocol-risks-fees)
- YT yield is staged/claimed via `stage_yt_yield` / `ix-stage-yield` instructions (yield accrues to the YT position and is collected in SY) — [Exponent developer docs: raw-stage-yt-yield](https://docs.exponent.finance/developer-core/raw-instructions/raw-stage-yt-yield)
- OnRe: YT holders get "continuous yield distributions"; "Yield accrues to ONyc as the business generates premiums from underwriting reinsurance and interest from collateral assets" — [OnRe blog](https://www.onre.finance/blog/onyc-meets-exponent-real-world-yield-gets-a-defi-upgrade)
- ONyc exchange rate (USD per ONyc) daily series: 1.03878578 (2025-10-14) → 1.11925753 (2026-07-01) → 1.12947504 (2026-07-31) → 1.140432897 (2026-08-30) → 1.1482501 (2026-09-22) → **1.15055451 (2026-09-29)** — [Exponent underlying-apy-chart API](https://app.exponent.finance/api/underlying-apy-chart/G1qbuP11CdquJCzuDjruWqatQAHroajmxhLfeQVgHosF?timeframeSeconds=31536000)
- Realized APY computed from that series (compound; simple in brackets): 7d **11.02%** (10.46%); 30d **11.35%** (10.80%); 60d 11.91%; 90d **11.83%** (11.34%); 180d 11.57% (11.25%) — computed from [same API](https://app.exponent.finance/api/underlying-apy-chart/G1qbuP11CdquJCzuDjruWqatQAHroajmxhLfeQVgHosF?timeframeSeconds=31536000)
- DefiLlama: OnRe ONYC pool TVL **$290.3M**, APY 11.02%, 30d mean APY 11.36% — [DefiLlama yields](https://yields.llama.fi/pools) (pool 7083d6a5-e3cb-4eeb-8204-f1b735e4ecbb), 2026-09-29 06:12 UTC
- Jupiter market price ONyc **$1.14863** (vs NAV 1.15055; ~0.17% below NAV), 24h change +0.096% — [Jupiter price API v3](https://lite-api.jup.ag/price/v3?ids=5Y8NV33Vv7WbnLfq3zBcKSdYPrk7g2KoiQoe7M2tcxp5)

**Net cost of YT after yield flows back (ONyc-10JAN27, per YT, spot $0.032912, 103.28 days, 5.5% yield fee)**
Formula: net yield per YT = [(1+APY)^(days/365) − 1] × (1 − 0.055); net cost = YT price − net yield.
| Assumed ONyc APY | Gross yield/YT | Net yield/YT | Net cost/YT | Net cost as % of price |
|---|---|---|---|---|
| 11.02% (7d) | $0.03002 | $0.02837 | **$0.00454** | 13.8% |
| 11.36% (30d) | $0.03091 | $0.02921 | **$0.00371** | 11.3% |
| 11.83% (90d) | $0.03214 | $0.03038 | $0.00254 | 7.7% |
| 12.55% (implied) | $0.03403 | $0.03216 | $0.00075 | 2.3% |
- srONyc-10JAN27 (YT $0.021619): net cost/YT $0.00308 at 7.11% (14.2% of price); $0.00233 at 7.41% (10.8%).

**Breakeven value per OnRe point (spot price, no slippage)**: breakeven = net cost per YT / points per YT to maturity.
- ONyc YT, USD basis (826 pts/YT): $0.0000055/pt at 7d APY; $0.0000045/pt at 30d APY → i.e., **~$4.5–5.5 per 1M points**.
- ONyc YT, per-ONyc basis (718 pts/YT): $0.0000063/pt (7d) ; $0.0000052/pt (30d) → **~$5.2–6.3 per 1M points**.
- With $10k-size fill (avg $0.03356/YT): net cost $0.00519/YT → ~$6.3–7.2 per 1M pts; with $50k fill (avg ~$0.03589): net cost ~$0.00752/YT → ~$9.1–10.5 per 1M pts (7d APY).
- srONyc YT: ~$7.5–7.6 per 1M pts (7d APY), ~$5.7–5.8 (30d).
- Downside if OnRe applies only 5x (docs tier): multiply breakeven by 8/5 = 1.6.

### Inferences
- Most of the YT premium is recovered through yield; the "true" cost of the points is ~8–14% of the YT outlay at current realized APY (and would be larger if ONyc's APY falls). Total loss if ONyc yield went to 0 = entire YT price.
- ONyc is NAV-accreting (non-rebasing); yield flows to YT holders in SY/ONyc units.

### Gaps
- Exact claim UX (manual claim vs auto) for v2 markets not documented in text found; SDK has explicit stage/claim instructions, suggesting yield accrues and must be claimed.

## Q4. Exponent fees and slippage for $1k / $10k / $50k YT buys

### Takeaway
Exponent charges a **5.5% fee on YT yield** (on-chain `interestBpsFee` = 550 for both ONyc vaults) plus CLMM swap fees (ln fee rate root ≈ 0.2% in rate terms, 35% of which goes to treasury). On-chain simulation: ONyc YT costs +0.26% over spot for $1k, +2.0% for $10k, ~+9% for $50k (CLMM-only; orderbook depth may improve large fills). srONyc YT CLMM liquidity is exhausted around $2–3k.

### Cited Findings
- On-chain vault state loaded via Exponent SDK (`MarketThree.load`, Solana mainnet, 2026-09-29 06:18 UTC): ONyc vault `interestBpsFee` **550**, market `treasuryFeeBps` **3500**, `lnFeeRateRoot` 0.001998, tickSpace 2500; srONyc vault `interestBpsFee` 550, same fee params — [@exponent-labs/exponent-sdk on npm](https://www.npmjs.com/package/@exponent-labs/exponent-sdk)
- Legacy ONyc v1 vaults also `interestFeeBps` 550 — [Exponent legacy web-api](https://web-api.exponent.finance/api/markets)
- Exponent: "collects a 5.5% fee on yield distributed to Yield Tokens… with an average yield of 10%, traders would earn approximately 9.45%" — [Exponent docs: Protocol Fees (search snippet)](https://docs.exponent.finance/resources/protocol-fees) (page now 404; current page says trading fees vary by venue (Rate Order Book vs Rate CLMM) and "may decrease over time as the market nears expiry"; LPs share trading fees; no protocol fee on deposit/withdraw — [Exponent docs: Protocol Risks & Fees](https://docs.exponent.finance/user-documentation/protocol-risks-fees))
- YT buy mechanics: strip SY → PT+YT, sell PT to pool, net cost = SY stripped − SY from PT sale — [`@exponent-labs/market-three-math` ytTrades.d.ts](https://www.npmjs.com/package/@exponent-labs/market-three-math)

**Simulated YT buys (CLMM only, `simulateBuyYtWithSyIn` / `simulateBuyYt`, on-chain state 2026-09-29 06:18–06:19 UTC)**
| Market | Spend | YT received | Avg $/YT | Premium vs spot | Post-trade implied APY |
|---|---|---|---|---|---|
| ONyc-10JAN27 | $1,000 | 30,306 | $0.03300 | +0.26% | 12.61% |
| ONyc-10JAN27 | $10,000 | 297,966 | $0.03356 | +1.97% | 13.07% |
| ONyc-10JAN27 | ~$50,000 | ~1.393M (interp. between 1.2M YT=$42,517 and 1.5M YT=$54,146) | ~$0.0359 | ~+9.1% | ~15.1% |
| srONyc-10JAN27 | $1,000 | 45,456 | $0.02200 | +1.76% | 8.41% |
| srONyc-10JAN27 | ≥~$2.3k | — | — | CLMM liquidity exhausted (100k YT = $2,296 → 9.45%; beyond that price jumps to 17% cap) | — |
- Fees inside the $1k ONyc buy: LP fee 0.319 SY + protocol fee 0.172 SY (~$0.56 total, ~0.06%).

### Inferences
- Size sweet spot for ONyc YT via CLMM is ≤~$10–20k per trade; above that, use limit orders on the Rate Order Book or split over time. srONyc YT is effectively illiquid for anything but small tickets.

### Gaps
- The app's router may combine orderbook + CLMM; orderbook tick depth not simulated, so large-trade slippage above is conservative (upper bound).

## Q5. Historical implied APY trend (is YT getting more expensive?)

### Takeaway
No — YT has been getting **cheaper**: ONyc-10JAN27 implied APY fell from ~16.3% at launch (24 Aug 2026) to 12.55% now (YT 0.0556 → 0.0329); srONyc from ~12.9% to 8.0%. Part of the YT price decline is time decay; the implied-APY decline shows the points premium compressing toward realized yield.

### Cited Findings
Daily closes from [Exponent implied-apy-chart API](https://app.exponent.finance/api/implied-apy-chart?vaultAddress=7f1PgxY3kGsPqLAKpwcduZkcBEhpjMz7U1iJ4pcCCzDy&timeframeSeconds=31536000) (ONyc-10JAN27): date — implied APY / PT / YT / days left
- 2026-08-24: 16.25% / 0.9444 / 0.0556 / 138.5 (first trades at 14.3–15.5%)
- 2026-08-30: 15.21% / 0.9499 / 0.0501 / 132.5
- 2026-09-05: 15.25% / 0.9520 / 0.0480 / 126.5
- 2026-09-11: 14.00% / 0.9576 / 0.0424 / 120.6
- 2026-09-17: 13.86% / 0.9601 / 0.0399 / 114.5
- 2026-09-23: 12.54% / 0.9655 / 0.0345 / 108.5
- 2026-09-29: 12.55% / 0.9671 / 0.0329 / 103.3
srONyc-10JAN27 ([same API, vault y5UF...](https://app.exponent.finance/api/implied-apy-chart?vaultAddress=y5UFEeB3LfUErLBjDMdZynAoqCwBgsMnDZSzth68aaH&timeframeSeconds=31536000)): 08-24 12.85% (YT 0.0448) → 09-02 14.13% → 09-12 10.05% → 09-21 8.45% → 09-29 8.05% (YT 0.0217).

### Inferences
- The implied-minus-realized spread for ONyc YT compressed from ~5pp at launch to ~1.2–1.5pp now — the market is pricing OnRe points less richly (or more YT supply from LPs/PT buyers). Useful as a sentiment gauge for OnRe point value.

### Gaps
- Implied APY history for expired v1 markets (25JAN26/13MAY26/10SEP26) not pulled.

## Q6. Other Solana venues (RateX etc.) for ONyc YT; Exponent's own points/token; extra rewards

### Takeaway
Exponent is now the **only live venue** for ONyc YT: RateX ran three ONyc maturities (2601, 2605, 2609) with OnRe 5x + RateX 8x boosts, but its last one (ONyc-2609) matured on 2026-09-29 00:00 and no newer ONyc term is listed. Exponent pays **no token emissions to plain YT holders** on ONyc; the only extra rewards are **ONyc-denominated maker incentives for resting buyYT/sellYT limit orders** on the ONyc order book (~4,357 ONyc for 23 Sep–23 Oct, reward APY capped at 80%). Exponent Finance has no live token; claims about an "XPN" token appear to refer to a different project and are unverified.

### Cited Findings
**RateX** (queried via RateX's public API `POST https://api.rate-x.io/` `{"serverName":"AdminSvr","method":"querySymbol"}`, 2026-09-29 11:55 UTC; front end [app.rate-x.io](https://app.rate-x.io/))
- 91 symbols total; ONyc-related: **ONyc-2601** (due 2026-01-29), **ONyc-2605** (due 2026-05-29), **ONyc-2609** (due **2026-09-29 00:00**). All three show `expiration: "1"`. No ONyc-2612/2701 term listed → no live RateX ONyc market as of 2026-09-29.
- Each ONyc term: `partners` "OnRe Multiplier;RateX Multiplier", `partners_reward_boost` "5;8" (OnRe **5x**, RateX points **8x**), `protocol_fee_rate` 0.5, `trade_commission` 0.01, `earn_w` 0.95.
- RateX's front-end bundle lists ONYC under its "Points" and "Stablecoin" categories (app.rate-x.io main JS, fetched 2026-09-29).
- A search-engine summary claimed "ONyc… has $28 million in market activity on RateX" — no primary source found; treat as unverified ([search result context: solanacompass](https://solanacompass.com/projects/ratex)).

**Exponent emissions / own token**
- ONyc-10JAN27 and srONyc-10JAN27: `ytHolderRewardsApy` 0, `ytHolderRewardCampaigns` [] → no Exponent/partner token emissions to passive YT holders — [Exponent markets API](https://app.exponent.finance/api/markets?include_frontend_hidden=true)
- Orderbook maker campaigns ([Exponent orderbook-emissions API](https://app.exponent.finance/api/orderbook-emissions/campaigns), fetched 2026-09-29): 
  - ONyc book `imv1h6xg…`: campaign 2026-08-24→2026-09-23 funded **4,395.03 ONyc** (4,301.74 distributed); campaign 2026-09-23→2026-10-23 funded **4,356.98 ONyc** (617.11 distributed so far), `currentRewardsApy` 80 (i.e., at the 8000-bps cap), incentivized order types **buyYT / sellYT**, price band 600 bps around market (market implied 11.74%), weekly epochs (Thursdays 10:00 UTC).
  - srONyc book `ndAp6RJ1…`: 08-24→09-23 funded 4,930.44 srONyc (3,594.27 distributed); 09-23→10-23 funded 3,919.28 srONyc (138.68 distributed); same parameters.
- srONyc CLMM LP farm emits srONyc through ~2026-10-23 — [Exponent CLMM API](https://app.exponent.finance/api/clmm)
- Exponent v2 is live (app links to "exponent.finance/blog/exponent-v2-is-live"); a DL News roundup reports a v2 rewards campaign of ">$200,000" over 30 days after the late-May-2026 launch — [DL News](https://www.dlnews.com/articles/defi/five-upcoming-crypto-airdrops-to-watch-for-in-2026/) (seen as search snippet only)
- "XPN… ERC-20 governance token for Exponent… 1,000,000,000 supply… distribution over 48 months" — [docs.exponent.cx tokenomics](https://docs.exponent.cx/token/tokenomics). **Caution:** this is a different domain (exponent.cx) and an ERC-20; it is very likely a different project, not Exponent Finance on Solana. The claim that Exponent's "XPN token contract is finalized and awaiting audit, no TGE date" came from a search summary that seems to blend these; unverified.

**Live refresh (2026-09-29 11:55 UTC, [Exponent markets API](https://app.exponent.finance/api/markets?include_frontend_hidden=true))**
- ONyc-10JAN27: 103.04 days, YT **0.03274**, PT 0.96726, implied **12.516%**, underlying 7d 11.02% / 30d 11.356%, liquidity $2,998,408, market size $20,255,838, yt_multiplier 8. (Essentially unchanged from 06:13 UTC: YT 0.03291, implied 12.555%.)
- srONyc-10JAN27: 102.96 days, YT 0.02162, PT 0.97838, implied 8.057%, underlying 7.114% / 7.407%, liquidity $300,648, yt_multiplier 4.

### Inferences
- For points-per-dollar, Exponent ONyc YT (8x OnRe) is richer than RateX's past ONyc YT (5x OnRe + 8x RateX points). RateX's extra value came from RateX's own points; it's no longer available for ONyc.
- A YT buyer who enters through **limit orders on the Rate Order Book** (buyYT inside the ±6% band) can also earn the ONyc maker rewards, lowering effective cost; a market-order buyer via the CLMM gets none.
- No Exponent-native points are credited to ONyc YT buyers in the API data; any "Exponent airdrop" value is speculative and should be treated as zero in the base case.

### Gaps
- RateX ONyc historical YT prices/implied APYs not pulled (markets expired). RateX market-data method names exist (`queryMarketTrade` on "MDSvr") if needed.
- Whether Exponent Finance has a live points program for users (the app has `/api/points/user/` endpoints, but these seem to track partner points) — not confirmed.
- Exponent Finance token (name, TGE) — no primary-source confirmation found.
