# Axis (axis.to) Pendle YT markets: cost of YT, points per $, and break-even $/point

Data fetch window: **2026-09-28, 11:48:57–11:58:34 UTC**. Pendle market stats carry `dataUpdatedAt 2026-09-28T11:47:00Z` and token prices carry `priceUpdatedAt 2026-09-28T11:49:15Z`. Unless a row says otherwise, "now" means 2026-09-28 11:49 UTC. All raw numbers come from the Pendle public API (primary source); where I checked them against DefiLlama or on-chain data, I say so. Conventions: **B** is the unknown Season-1 base Coordinates rate per $1 per day. **M** is the multiplier. **0.95** is the share left after Pendle's 5% fee on YT points and yield. **T = 65.507 days**, the time from now to maturity (2026-12-03 00:00 UTC), so t = T/365 = 0.17947 years.

---

## Q1. Which project is "Axis", and what are its token tickers? (avoiding look-alikes)

### Takeaway
Axis (axis.to, X: @AxisFDN) issues **USDx** (the "Axis Dollar", a synthetic over-collateralized dollar that does not bear yield itself) and **sUSDx** (the "Axis Rewards Vault", an ERC-4626 staked USDx that bears yield). Both live on Ethereum. Its points are called **"Coordinates"**. Several unrelated projects share the "Axis" or "USDX" names and have to be filtered out.

### Cited Findings
- USDx contract `0xa1fA7777974312f7d801A8880714a218F76233f8` ("Axis Dollar (synthetic dollar token)") and StakedUSDx/sUSDx `0xEB892628D1E58BC475A6dCB7F5dBC4F591632AA4` ("Axis Rewards Vault") on Ethereum. The docs also list **V1 contracts on Plasma** (AxisUSD `0xA1FA77779e6866fa3eF48FC0720657E042158387`, StakedAxisUSDV2 `0x13A0…0012`) — [Axis docs: Contract Addresses](https://docs.axis.to/reference/contract-addresses)
- Pendle's own market metadata: "USDx does not accrue yield natively — yield is earned by staking USDx into sUSDx"; sUSDx is "the rewards vault of USDx… compounded via a market-neutral trading engine" — [Pendle API v2 markets/all](https://api-v2.pendle.finance/core/v2/markets/all?limit=100&skip=0) (field `marketInfo`)
- The Axis points program is named "Coordinates" ("the Axis rewards points") — [Axis docs: Brand](https://docs.axis.to/resources-and-legal/brand) ; [Axis docs: Origin Vault](https://docs.axis.to/origin-vault/origin-vault)
- Axis raised $5M in a round led by Galaxy Ventures for an "onchain yield protocol for USD, bitcoin and gold" — [The Block](https://www.theblock.co/post/381215/axis-5-million-usd-round-galaxy-ventures-onchain-yield-protocol-usd-bitcoin-gold)
- **Look-alikes to exclude:**
  - "Axis Robotics" ran a "1.5M Points pool… exclusively for Binance Wallet users" (a robot-trajectory task campaign on Base). This is a different project; airdrop newsletters call it "Axis launched a 1.5M Points campaign" — [airdrops_io Telegram #7796](https://t.me/airdrops_io/7796) ; [airdrops_io #7826](https://t.me/airdrops_io/7826)
  - The Pendle list also contains **"sUSDX" by usdx.money** on BNB Chain (chainId 56, market `0xe08fc305…fffc`, expired 2025-09-01) and **"ynUSDx" by YieldNest** (Ethereum, `0x261b2525…2ed9`, expired 2026-04-30). Neither is Axis — [Pendle API v2 markets/all](https://api-v2.pendle.finance/core/v2/markets/all?limit=100&skip=0)

### Inferences
- An analyst filtering by ticker alone ("USDX") will catch the wrong assets. Filter by `protocol == "Axis"` or by the underlying addresses above.

### Gaps
- The Axis API endpoint `https://api.axis.to/api/v1/susdx/apy` returned a **7-day APY of 0%** and rate 1.026745… for contract `0x24891F…c9bE`, which the Axis docs list as the **Plasma V1** `AxisUSDRateProvider`. It is not the Ethereum sUSDx (on-chain Ethereum rate is 1.02961, see Q3). I could not confirm which product that endpoint is meant to describe. — [Axis API](https://api.axis.to/api/v1/susdx/apy) ; [Axis docs: Contract Addresses](https://docs.axis.to/reference/contract-addresses)

---

## Q2. Which Pendle markets exist for Axis tokens, on which chains?

### Takeaway
There are **exactly two Axis markets on Pendle, both on Ethereum mainnet, both maturing 3 Dec 2026**: **USDx** (a pure points YT) and **sUSDx** (a yield-plus-points YT). I scanned all 803 Pendle markets across all chains, active and expired. No Axis market exists on Arbitrum, Base, BNB, Plasma, Sonic, HyperEVM or any other chain, and there is no expired Axis market.

### Cited Findings
- Full scan of `core/v2/markets/all` (803 markets, paginated, 2026-09-28 11:49 UTC): the only `protocol == "Axis"` entries are the two below. The active-market list `core/v1/markets/all?isActive=true` (79 active markets) returns the same two — [Pendle API v2 markets/all](https://api-v2.pendle.finance/core/v2/markets/all?limit=100&skip=0) ; [Pendle API v1 active](https://api-v2.pendle.finance/core/v1/markets/all?isActive=true)
- Pendle's launch post: "Introducing @AxisFDN USDx and sUSDx (3 Dec 2026 maturity)… now live as fixed income markets on Pendle – with the highest multiplier for Axis points" — [Pendle on X](https://x.com/pendle_fi/status/2095738643793207563). I saw this only as a search snippet; the page returned HTTP 402 when fetched.
- Both markets were created on 2026-09-02 (USDx 05:42:35 UTC, sUSDx 05:53:35 UTC). Meaningful trading began on 2026-09-04, when Coordinates Season 1 started — [Pendle API v1 market detail USDx](https://api-v2.pendle.finance/core/v1/1/markets/0x0bef762d2094ac80821c657dea6783fc43435292) ; [sUSDx](https://api-v2.pendle.finance/core/v1/1/markets/0x5e572498e9f83650f0ff24194999bddb4b390928) ; [historical-data](https://api-v2.pendle.finance/core/v2/1/markets/0x5e572498e9f83650f0ff24194999bddb4b390928/historical-data?time_frame=day)

**Market registry** (source: [Pendle API v1 market detail](https://api-v2.pendle.finance/core/v1/1/markets/0x5e572498e9f83650f0ff24194999bddb4b390928), [v2 /data](https://api-v2.pendle.finance/core/v2/1/markets/0x0bef762d2094ac80821c657dea6783fc43435292/data); stats as of 2026-09-28 11:47 UTC)

| | **USDx (3DEC2026)** | **sUSDx (3DEC2026)** |
|---|---|---|
| Chain | Ethereum (1) | Ethereum (1) |
| Market (LP) address | `0x0bef762d2094ac80821c657dea6783fc43435292` | `0x5e572498e9f83650f0ff24194999bddb4b390928` |
| PT | `0xa4b3a2eec53863fe2c9ab0041d480cf964942e84` (PT-USDx-3DEC2026) | `0x06ebad062fd573ca31a72d6dfb0f425da2153985` (PT-sUSDx-3DEC2026) |
| YT | `0xa91277e31f6be8c33850dde8dfacb27bad1be6fb` (YT-USDx-3DEC2026) | `0x96dcb9501bcc8128b7683980a63250448ea5334b` (YT-sUSDx-3DEC2026) |
| SY | `0xa7606952845269dc7377cba3c7c7bda133dd97f7` | `0x3b184870f40ca026341593cedb37ab09e611e928` |
| Underlying / accounting asset | USDx / USDx | sUSDx / USDx ("USDx staked in Axis") |
| Maturity | 2026-12-03 00:00 UTC | 2026-12-03 00:00 UTC |
| Days to maturity (from 11:49 UTC 28 Sep) | 65.51 | 65.51 |
| Pool liquidity (USD) | $2,244,572 | $5,861,693 |
| Total TVL (USD, incl. PT/YT outside pool) | $5,524,391 | $8,642,608 |
| 24h trading volume (USD) | $18,814 (−81% vs prior 24h) | $703,805 (+249% vs prior 24h) |
| AMM implied-APY range (`yieldRange`) | 6%–27% | 8%–30% |
| API `feeRate` | 0.2935% | 0.3341% |
| Pendle UI link (not fetched) | app.pendle.finance/trade/markets/0x0bef762d2094ac80821c657dea6783fc43435292 | app.pendle.finance/trade/markets/0x5e572498e9f83650f0ff24194999bddb4b390928 |

- DefiLlama cross-check (fetched 11:58:34 UTC): pendle-v2 "PT-USDx-03DEC2026" TVL $2,243,358 with fixed APY 15.00672%; "PT-sUSDx-03DEC2026" TVL $5,861,670 with fixed APY 19.27546%. It also shows Axis sUSDx vault TVL **$35,936,137**, Curve USDx-USDT $3.05M and Curve sUSDx-USDx $2.01M — [DefiLlama yields API](https://yields.llama.fi/pools)

### Inferences
- There is one maturity and one chain, so there is no cross-chain or cross-maturity arbitrage between Axis YTs. The only choice is **USDx YT versus sUSDx YT**.
- The USDx pool is small ($2.24M liquidity, about $19k of 24h volume). The sUSDx pool is the liquid one.

### Gaps
- I could not render the Pendle app UI (a JS app) to screenshot the displayed badges. Multipliers come from the Pendle API `points` field (Q3), which feeds the UI.

---

## Q3. Current pricing snapshot: YT/PT prices, implied and underlying APY, leverage, points multipliers, other incentives

### Takeaway
**YT-USDx costs ≈$0.0248 (about 40x yield/points exposure), receives zero underlying yield, and carries the 24x Axis multiplier**, the highest in Season 1. **YT-sUSDx costs ≈$0.0311 (about 32x exposure), receives the sUSDx vault yield (currently ≈21.6% APY against 19.3% implied), and carries only 6x.** YT holders earn no PENDLE incentives. There are no partner points other than Axis Coordinates.

### Cited Findings
**Prices and APYs** (Pendle API, 2026-09-28; prices at 11:49:15 UTC; USDx = $0.99991171, sUSDx = $1.0295155) — [v1 market USDx](https://api-v2.pendle.finance/core/v1/1/markets/0x0bef762d2094ac80821c657dea6783fc43435292) ; [v1 market sUSDx](https://api-v2.pendle.finance/core/v1/1/markets/0x5e572498e9f83650f0ff24194999bddb4b390928) ; [swapping-prices USDx](https://api-v2.pendle.finance/core/v1/sdk/1/markets/0x0bef762d2094ac80821c657dea6783fc43435292/swapping-prices) ; [swapping-prices sUSDx](https://api-v2.pendle.finance/core/v1/sdk/1/markets/0x5e572498e9f83650f0ff24194999bddb4b390928/swapping-prices) (fetched 11:51:31 UTC)

| | **YT-USDx** | **YT-sUSDx** |
|---|---|---|
| YT mid price (USD) | $0.024780 | $0.031137 |
| YT mid price (accounting asset USDx) = `ptDiscount` | 0.024782 USDx | 0.031140 USDx (= 0.030244 sUSDx) |
| Small-trade **buy** quote (fees included) | 39.5328 YT per USDx → 0.025295 USDx/YT | 32.4588 YT per sUSDx → 0.030808 sUSDx = 0.031720 USDx/YT |
| Small-trade **sell** quote | 0.024268 USDx/YT | 0.029680 sUSDx = 0.030559 USDx/YT |
| Buy/sell spread (small size) | 4.15% of mid | 3.73% of mid |
| PT price (USD) | $0.975132 | $0.968774 |
| Implied APY | 15.0067% | 19.2755% |
| Underlying APY (flows to YT) | **0%** (`underlyingApy 0`; YT floating APY −100%) | **21.6006%** (all "Protocol Yield", sourced from CONTRACT) |
| API field `impliedApyChange24h` (probably a relative change; field semantics not documented in what I read) | −0.0085 (≈ −0.85% relative) | +0.0720 (≈ +7.2% relative, i.e. from about 17.98%) |
| Leverage / "yield exposure" = 1 / YT price (USDx) | **40.35x** mid; 39.53x small buy | **32.11x** mid; 31.53x small buy |
| Pendle `ytRoi` (ROI if underlying APY holds) | −100% | +8.98% |
| Pendle `ytFloatingApy` | −100% | +61.49% |

- Check: YT price = 1 − (1+implied)^(−t) reproduces the API mid exactly. For USDx, 1 − 1.150067^(−0.17947) = 0.024782; for sUSDx, 1 − 1.192755^(−0.17947) = 0.031140 (my calculation from API fields).
- **On-chain sUSDx rate:** `convertToAssets(1e18)` = **1.029610411564866 USDx per sUSDx** at Ethereum block 26,075,797 (2026-09-28 11:56:59 UTC), queried via ethereum-rpc.publicnode.com. This matches Pendle's `conversionRate` 1.0296057623896737 — [Etherscan sUSDx](https://etherscan.io/address/0xEB892628D1E58BC475A6dCB7F5dBC4F591632AA4) ; [Pendle API marketInfo](https://api-v2.pendle.finance/core/v2/markets/all?limit=100&skip=0)
- DefiLlama shows the **Axis sUSDx** pool at current APY 26.377% with a **30-day mean of 22.697%** (fetched 11:58:34 UTC) — [DefiLlama yields API](https://yields.llama.fi/pools) (pool `edf44260-d78f-5dab-853a-f89c4f523169`)

**Points multipliers as served by Pendle** (field `points` in [Pendle API v2 markets/all](https://api-v2.pendle.finance/core/v2/markets/all?limit=100&skip=0)):
- USDx market: `{"key":"Axis","type":"multiplier","pendleAsset":"basic","value":24}` and `{"key":"Axis","type":"multiplier","pendleAsset":"lp","value":20}`, meaning **YT 24x, LP 20x**.
- sUSDx market: `{"key":"Axis","pendleAsset":"basic","value":6}` and `{"key":"Axis per $ LP","pendleAsset":"lp","value":5,"perDollarLp":true}`, meaning **YT 6x, LP 5x per $ of LP**.
- These match Axis's Season-1 multiplier list, as reported by airdrops.io from the Axis Season 1 announcement: **Pendle YT-USDx 24x**; Curve USDx/USDT LP 20x; Pendle LP USDx 20x; **Hold USDx 16x**; Origin/Ecosystem Vault (ogUSDx) 10x; Curve USDx/sUSDx LP 10x; **Pendle YT-sUSDx 6x**; Pendle LP sUSDx 5x; **Hold sUSDx 4x** — [airdrops.io/axis (updated 4 Sep 2026)](https://airdrops.io/axis/)
- Axis (official): "Coordinates accrue daily based on the eligible position and its corresponding multiplier. The same dollar counts in one position at a time, so venue multipliers do not stack… From September 4, the vault position moves to a flat 10x multiplier, while other USDx and sUSDx positions carry their own rates." — [Axis: What's Next for USDx and Coordinates (1 Sep 2026)](https://www.axis.to/insights/Whats-Next-for-USDx-and-Coordinates)

**Base rate (B):**
- Season 0 (Origin Vault): "You earn **10 Coordinates per day for every dollar deposited**. For example: deposit $10,000 on Day 1 and you earn 10000 x 10 x 30 x 2.0 multiplier = 6,000,000 Coordinates" — [Axis: How the Origin Vault Works (23 Jul 2026)](https://www.axis.to/insights/How-the-Origin-Vault-Works) ; docs: "~10 Coordinates/day + Multiplier (2x…first $50M, 1.75x…second $50M)" — [Axis docs: Origin Vault](https://docs.axis.to/origin-vault/origin-vault)
- For Season 1, Axis publishes the multipliers (4x–24x) but **not the base Coordinates per $ per day** in any page I could access — [Axis Season 1 post](https://www.axis.to/insights/Whats-Next-for-USDx-and-Coordinates)

**Pendle fee on points and yield:** "Pendle collects a 5% fee from all yield accrued (including points) by all YT… Since points are tracked off-chain, partner protocols deduct the 5% fee when allocating points to user wallets." — [Pendle docs: Fees](https://docs.pendle.finance/pendle-v2/ProtocolMechanics/Mechanisms/Fees)

**Other incentives:**
- PENDLE emissions go to **LPs only**: USDx LP `pendleApy` 0.752% (≈19.29 PENDLE/day to the pool at PENDLE = $2.386); sUSDx LP 0.299%. `pendleEmission.totalIncentive` is 164.24 (USDx) and 208.15 (sUSDx). Limit-order incentives also exist (`limitOrderIncentive`). The YT APY breakdown contains only "Protocol Yield" — [Pendle API v2 markets/all](https://api-v2.pendle.finance/core/v2/markets/all?limit=100&skip=0) ; [v2 /data](https://api-v2.pendle.finance/core/v2/1/markets/0x0bef762d2094ac80821c657dea6783fc43435292/data)
- LP APYs (DefiLlama): USDx LP 9.08% (8.32% base + 0.76% PENDLE); sUSDx LP 20.94% (20.63% + 0.30%) — [DefiLlama yields API](https://yields.llama.fi/pools)
- Referral: invitees' referrer earns 10% of their Coordinates; a referral code gives a "13% points boost" (airdrops.io's own code) — [airdrops.io/axis](https://airdrops.io/axis/)

### Inferences
- The Pendle "basic" multiplier applies to the YT holder's full underlying exposure. That means **1 YT ≈ $1 of USDx notional earns M × B Coordinates per day, before the 5% fee**. For YT-sUSDx, 1 YT corresponds to 1 USDx of accounting value, not 1 sUSDx (1 sUSDx = 1.0296 USDx). If Axis credits points per sUSDx unit, the result shifts by about 3%.
- I assume the 24x/6x shown are **gross**, with Axis deducting Pendle's 5% at allocation, which gives an effective 22.8x and 5.7x. This is the convention in Pendle's docs, but Axis has not confirmed it.
- Leverage-adjusted points per $ of capital (at $1k fills): YT-USDx is 24 × 38.78 = **~931x**, YT-sUSDx is 6 × 31.38 = **~188x**. Holding USDx gives 16x and holding sUSDx gives 4x. So YT-USDx earns about **4.9x more Coordinates per dollar than YT-sUSDx**, and about 58x more than holding USDx.

### Gaps
- **Season-1 base rate B is unpublished** in accessible sources. In Season 0 it was 10 Coordinates/$/day × a 2x boost. Season 1 describes a "flat 10x" for the vault, so B could be 1 (vault = 10/$/day) or 10 (vault = 100/$/day). All points below are therefore given in **"x-$-days"** (multiplier × $ notional × days, net of the 5% fee). Coordinates = x-$-days × B.
- Total Coordinates outstanding and any token conversion rate are unpublished. airdrops.io says "Axis has not published a conversion rate" — [airdrops.io/axis](https://airdrops.io/axis/). Without these, $/point cannot be turned into a token price.
- I could not read Pendle's launch tweet body (HTTP 402).

---

## Q4. Calculations: cost of YT, expected yield, net cost, points per $1,000, break-even $/point (base vs bearish)

### Takeaway
- **YT-USDx** is a pure points purchase. With 100% of capital at risk, **$1,000 buys about 38,782 YT and about 57.9M x-$-days (net of fee) by maturity**. Break-even is **≈ $1.73×10⁻⁵ per x-$-day**, which is **$17.3 per million Coordinates if B = 1, or $1.73 per million if B = 10**.
- **YT-sUSDx** yield roughly pays for the YT at today's 21.6% APY (net cost about −$65 per $1k, i.e. points come "free"). Its **break-even underlying APY is ≈20.2%** (at a $1k fill, after the 5% fee). At a bearish 10% APY, net cost is ≈$486 per $1k, or **≈$4.15×10⁻⁵ per x-$-day**. That is about 2.4x more expensive per point than YT-USDx.

### Cited Findings
Execution quotes from Pendle's Hosted SDK `POST /v3/sdk/1/convert` (USDx in, YT out, aggregator off, limit orders on; fetched 2026-09-28 11:52:34 and 11:53:05 UTC) — [Pendle Hosted SDK convert](https://api-v2.pendle.finance/core/v3/sdk/1/convert) ; [API docs](https://api-v2.pendle.finance/core/docs)

| Buy size (USDx) | YT-USDx received | Avg USDx/YT | Price impact | YT-sUSDx received | Avg USDx/YT | Price impact |
|---|---|---|---|---|---|---|
| 1,000 | 38,782.27 | 0.025785 | −3.89% | 31,375.45 | 0.031872 | −2.30% |
| 3,000 | 112,275.44 | 0.026720 | −7.26% | — | — | — |
| 5,000 | 181,163.24 | 0.027599 | −10.21% | — | — | — |
| 10,000 | 337,609.77 | 0.029620 | −16.34% | 307,359.26 | 0.032535 | −4.29% |
| 30,000 | — | — | — | 860,099.48 | 0.034880 | −10.73% |
| 50,000 | — | — | — | 1,336,712.91 | 0.037405 | −16.75% |
| 100,000 | **no route** | — | — | 2,260,194.63 | 0.044244 | −29.62% |
| 500,000 | no route | — | — | **no route** | — | — |

- Pendle fee on YT yield and points is 5% — [Pendle docs: Fees](https://docs.pendle.finance/pendle-v2/ProtocolMechanics/Mechanisms/Fees)
- sUSDx underlying APY: 21.6006% (Pendle, now); 22.697% 30-day mean (DefiLlama); Axis's own guidance is "10–20% net" ("a verifiable 10-20%… It is a net range") — [Pendle API](https://api-v2.pendle.finance/core/v1/1/markets/0x5e572498e9f83650f0ff24194999bddb4b390928) ; [DefiLlama](https://yields.llama.fi/pools) ; [Axis docs: Origin Vault FAQ](https://docs.axis.to/origin-vault/origin-vault)
- Other Axis yield data points: "As of July 9, 2026, APY stands at 10.7%" — [Axis Roadmap](https://www.axis.to/insights/The-Axis-Roadmap). The Origin vault "delivered 11.58% annualized on ogUSDx" since 5 Aug — [Axis Season 1 post](https://www.axis.to/insights/Whats-Next-for-USDx-and-Coordinates). sUSDx rewards are **"fully discretionary"**, "a signal of what the protocol is willing to pay for capital… not a mechanical redistribution of realized yield" — [Axis docs: Reward Distribution](https://docs.axis.to/susdx-the-rewards-vault/reward-distribution)

### Inferences (formulas and results; all my calculations from the cited inputs)

**Formulas**
- YT cost per $1 of underlying exposure = YT price in USDx (P). Leverage = 1/P.
- Expected yield to YT per YT to maturity (USDx) = Y = 0.95 × [(1 + APY)^t − 1], with t = 65.507/365 = 0.17947.
- Net cost per YT = P − Y. As % of price = (P − Y)/P. As % of notional = (P − Y)/$1.
- YT per $1,000 = 1000 / P. (USDx ≈ $0.99991, so USD and USDx are treated as 1:1; the error is under 0.01%.)
- Points per day per $1,000 spent = (1000 / P) × M × 0.95 × B. The "x-$-days/day" below equals (1000/P) × M × 0.95, so multiply by B for Coordinates.
- Total points to maturity = the above × 65.507 days. Season 1 = 4 Sep + 90 days = 3 Dec 2026 (Q6).
- Break-even $ per point = net cost per $1,000 / total points.
- Break-even underlying APY (sUSDx) = (1 + P/0.95)^(1/t) − 1.

**YT-USDx (M = 24, APY = 0)**

| Entry | P (USDx/YT) | YT per $1k | Net cost / $1k | Net cost % notional | x-$-days per day | x-$-days to maturity | Break-even $/x-$-day | $/Coordinate if B=1 | if B=10 |
|---|---|---|---|---|---|---|---|---|---|
| Mid (not executable) | 0.024782 | 40,352 | $1,000 | 2.478% | 920,033 | 60.27M | 1.659e-5 | $0.0000166 | $0.00000166 |
| $1k fill | 0.025785 | 38,782 | $1,000 | 2.578% | 884,236 | 57.92M | 1.726e-5 | $0.0000173 | $0.00000173 |
| $10k fill | 0.029620 | 33,761 | $1,000 | 2.962% | 769,750 | 50.42M | 1.983e-5 | $0.0000198 | $0.00000198 |

- If B = 1, $1,000 at a $1k fill earns ≈ **884k Coordinates/day and ≈ 57.9M by maturity**. If B = 10, it earns ≈ 8.84M/day and ≈ 579M.
- The YT goes to $0 at maturity and pays no yield, so net cost = 100% of the premium (2.58% of notional).

**YT-sUSDx (M = 6)**, $1k fill, P = 0.031872 USDx (31,375 YT per $1k; 178,840 x-$-days/day; 11.72M x-$-days to maturity)

| Underlying APY scenario | Yield per YT Y (after 5% fee) | Net cost per YT | Net cost % of price | Net cost / $1k | Break-even $/x-$-day |
|---|---|---|---|---|---|
| 22.70% (DefiLlama 30d mean) | 0.035523 | −0.003651 | −11.5% | −$114.55 | ≤0 (points free) |
| **21.60% (current, Pendle)** | 0.033937 | −0.002065 | −6.5% | **−$64.78** | ≤0 (points free) |
| **10% (bear: bottom of Axis's 10–20% guide)** | 0.016390 | 0.015482 | 48.6% | **$485.75** | **4.146e-5** |
| 5% (severe bear) | 0.008355 | 0.023517 | 73.8% | $737.85 | 6.298e-5 |
| 0% (rewards stop) | 0 | 0.031872 | 100% | $1,000 | 8.536e-5 |

- Break-even underlying APY for yield alone to repay the YT is **19.69% at mid and 20.19% at a $1k fill**. Current is 21.60%.
- The same analysis at other sizes: $10k fill (P = 0.032535) gives net −$43.08/$1k at 21.6% and $496.24 at 10%. $100k fill (P = 0.044244) gives **+$232.96/$1k at 21.6%** and $629.55 at 10%, because slippage wipes out the yield edge.
- Coordinates: if B = 1, ≈179k/day and 11.7M to maturity per $1k. If B = 10, ≈1.79M/day and 117M.

**Bearish points scenarios ($1k fills; break-even $/x-$-day)**

| Scenario | YT-USDx | YT-sUSDx @21.6% | YT-sUSDx @10% |
|---|---|---|---|
| Base (points to maturity, full multiplier) | 1.73e-5 | ≤0 | 4.15e-5 |
| Snapshot/season cut at day 45 from now (68.7% of points) | 2.51e-5 | ≤0 | 6.04e-5 |
| Snapshot at day 30 (45.8% of points) | 3.77e-5 | ≤0 | 9.05e-5 |
| Multiplier halved for the whole remaining period | 3.45e-5 | ≤0 | 8.29e-5 |

(For YT-USDx, this assumes the YT is worth about 0 once points stop. For YT-sUSDx, yield keeps accruing to maturity even if points stop.)

**Cross-checks and what the market is pricing**
- The price of YT-USDx means the market values one net x-$-day at **$1.659e-5** (0.024782 / (24 × 0.95 × 65.507)).
- Apply that value to YT-sUSDx's points (6 × 0.95 × 65.507 = 373.4 x-$-days per YT → $0.0062 per YT). The remaining $0.0249 of the sUSDx YT price then implies the market expects a **forward sUSDx APY of ≈15.5%**, well below the current 21.6%. In other words, the sUSDx YT prices in a yield decline, or the market values the 6x points at almost nothing.
- For comparison, holding $1k of USDx (16x, no Pendle fee) instead of sUSDx gives up ≈$35.72 of sUSDx yield over 65.5 days (at 21.6%). That is ≈3.41e-5 per x-$-day, roughly 2x the per-point cost of YT-USDx. The difference is that holding USDx keeps principal intact, while YT premium is lost.

### Gaps
- B (the Season-1 base rate) is unknown, so absolute Coordinates per $ carry a 10x uncertainty. Relative comparisons (x-$-days) are unaffected.
- The token/FDV per Coordinate is unknown. Break-even $/Coordinate cannot yet be compared against an expected airdrop value.
- Whether Axis applies the 5% Pendle deduction to the headline multiplier (24x → 22.8x) is unconfirmed.
- Fill quotes are snapshots. They depend on limit-order depth and can change minute to minute.

---

## Q5. Historical context: how implied APY and YT prices have moved (2 Sep to 28 Sep 2026)

### Takeaway
The markets are only about 26 days old. **YT prices fell about 25% (USDx) and about 21% (sUSDx) from the first trading day (4 Sep)**. For YT-USDx that drop is almost entirely **time decay**: implied APY is back to about 15%, the same as on 4 Sep, and the cost per day of exposure is flat at about $0.00037–0.00038 per YT-day. For YT-sUSDx, implied APY *rose* from 18.0% to 19.3%, so per-day exposure is about 7% more expensive than at launch, while underlying APY fell from a 26.5% peak to 18.7% and recovered to 21.6%. The market has **not** been marking the points down.

### Cited Findings
Daily data, 00:00 UTC snapshots except the 28 Sep row (≈11:00 UTC). YT price is the USD close from Pendle OHLCV; implied and underlying APY from historical-data. Sources: [historical-data USDx](https://api-v2.pendle.finance/core/v2/1/markets/0x0bef762d2094ac80821c657dea6783fc43435292/historical-data?time_frame=day&fields=ytPrice,ptPrice,impliedApy,underlyingApy,tvl,tradingVolume) ; [historical-data sUSDx](https://api-v2.pendle.finance/core/v2/1/markets/0x5e572498e9f83650f0ff24194999bddb4b390928/historical-data?time_frame=day&fields=ytPrice,ptPrice,impliedApy,underlyingApy,tvl,tradingVolume) ; [OHLCV YT-USDx](https://api-v2.pendle.finance/core/v4/1/prices/0xa91277e31f6be8c33850dde8dfacb27bad1be6fb/ohlcv?time_frame=day) ; [OHLCV YT-sUSDx](https://api-v2.pendle.finance/core/v4/1/prices/0x96dcb9501bcc8128b7683980a63250448ea5334b/ohlcv?time_frame=day)

| Date | YT-USDx close ($) | USDx implied | USDx pool liq ($M) | YT-sUSDx close ($) | sUSDx implied | sUSDx underlying | sUSDx pool liq ($M) |
|---|---|---|---|---|---|---|---|
| 09-02 (seed) | 0.0257 | 11.00% | 0.002 | 0.0342 | 15.00% | 21.22% | 0.002 |
| 09-04 (Season 1 start) | 0.0332 | 14.85% | 1.23 | 0.0395 | 17.97% | 21.16% | 2.28 |
| 09-07 | 0.0325 | 15.08% | 1.35 | 0.0415 | 19.69% | 21.42% | 2.62 |
| 09-10 | 0.0326 | 15.67% | 1.36 | 0.0413 | 20.41% | 25.93% | 2.72 |
| 09-14 | 0.0305 | 15.39% | 2.33 | 0.0387 | 20.00% | 26.48% (peak) | 4.25 |
| 09-17 | 0.0268 | 13.96% | 2.42 | 0.0341 | 18.15% | 22.09% | 5.70 |
| 09-21 | 0.0240 | 13.11% | 1.91 | 0.0319 | 17.88% | 20.10% | 5.75 |
| 09-23 | 0.0233 | 13.10% (low) | 2.39 | 0.0309 | 17.77% | 18.88% | 5.86 |
| 09-24 | 0.0273 | 15.78% | 2.26 | 0.0301 | 17.54% (low) | 18.71% (low) | 5.83 |
| 09-26 | 0.0256 | 15.20% | 2.28 | 0.0297 | 17.84% | 19.92% | 5.86 |
| 09-27 | 0.0252 | 15.13% | 2.29 | 0.0310 | 19.04% | 21.03% | 5.86 |
| 09-28 (~11:00) | 0.0248 | 15.01% | 2.24 | 0.0311 | 19.28% | 21.60% | 5.86 |

- Largest single-day volumes: USDx market $630,145 on 09-16 and $374,924 on 09-04. sUSDx market $1,085,391 on 09-17 and $725,958 on 09-04 — same historical-data sources.
- Axis says the Ecosystem Vault "will allocate capital into USDx and sUSDx positions, including… capital used to seed @pendle_fi markets" — [Axis Season 1 post](https://www.axis.to/insights/Whats-Next-for-USDx-and-Coordinates)

### Inferences
- Time-decay check (my calculation): at a constant 15% implied, YT-USDx would be worth 0.03387 at 90 days and 0.02477 at 65.5 days. The observed 0.0332 → 0.0248 path is therefore almost pure decay. Cost per YT-day: 0.0332/89 = 0.000373 on 4 Sep versus 0.024782/65.5 = 0.000378 now, essentially unchanged.
- YT-sUSDx: 0.0395/89 = 0.000444 per day on 4 Sep versus 0.000475 now (+7%). That is consistent with implied APY rising while underlying APY is volatile, from 18.7% to 26.5% within three weeks.
- The 09-24 jump in YT-USDx (implied 13.10% → 15.78%, YT 0.0233 → 0.0273) coincided with $330,663 of volume. I found no public catalyst, so treat it as unexplained.
- The sUSDx pool's liquidity rose from $2.3M to $5.9M by 17 Sep, then stayed flat. The USDx pool plateaued at $1.9–2.4M.

### Gaps
- History covers only 2–28 Sep 2026, because the markets launched 2 Sep. No multi-month history exists.
- I could not read X threads by Pendle YT analysts (x.com returns 402).
- Hourly or intraday data was not pulled.

---

## Q6. Differences between the two pools, and maturity versus the season/TGE timeline

### Takeaway
The two YTs are different products. **YT-USDx** is a leveraged Coordinates bet (24x, about 40x leverage, **no yield, so the premium is always 100% lost**). **YT-sUSDx** is mainly a leveraged bet on sUSDx's discretionary reward rate, with a small 6x points kicker. **Season 1 runs 90 days from 4 Sep 2026, i.e. to 3 Dec 2026, the same date as Pendle maturity**, so under current rules points accrue for the YT's full remaining life. No TGE or snapshot date has been announced.

### Cited Findings
- "Season 1 starts on September 4, 2026 and runs for 90 days… On Friday, September 4 at 2:00 PM UTC, the 30-day lock ends" — [Axis Season 1 post](https://www.axis.to/insights/Whats-Next-for-USDx-and-Coordinates). By my date arithmetic, 4 Sep + 90 days = **3 Dec 2026**. Pendle maturity is 2026-12-03 00:00 UTC — [Pendle API](https://api-v2.pendle.finance/core/v1/1/markets/0x5e572498e9f83650f0ff24194999bddb4b390928)
- "Origin was Season 0 of Coordinates… The pre-deposit boost used during Origin ends with Season 0" — [Axis Season 1 post](https://www.axis.to/insights/Whats-Next-for-USDx-and-Coordinates)
- USDx: "does not accrue yield natively". sUSDx important quirk: "There is a **7-day cooldown period** for unstaking sUSDx to USDx"; USDx market deposit/withdrawal is "Swap via LP, subject to liquidity" — [Pendle API marketInfo](https://api-v2.pendle.finance/core/v2/markets/all?limit=100&skip=0)
- sUSDx rewards "vest linearly over a configured window"; funding is "a decision, not a formula" — [Axis docs: Reward Distribution](https://docs.axis.to/susdx-the-rewards-vault/reward-distribution)
- Token status: "Axis has not confirmed a token… A public token sale is planned to follow" (airdrops.io, a secondary source; its FAQ elsewhere says "planned for early 2026", which contradicts the present date and looks stale) — [airdrops.io/axis](https://airdrops.io/axis/)

### Inferences
- If Season 1 is counted from 4 Sep 14:00 UTC, it ends about 3 Dec 14:00 UTC, roughly 14 hours after YT maturity. YT points therefore stop at maturity (00:00 UTC). After maturity, points on unredeemed SY go to Pendle's fee wallets ([Pendle docs: Fees](https://docs.pendle.finance/pendle-v2/ProtocolMechanics/Mechanisms/Fees)).
- If Axis ends the season early, snapshots early for a TGE, or cuts the 24x, YT-USDx loses value one-for-one with lost points, because it has no yield floor. YT-sUSDx keeps its yield leg.
- The market seems to treat YT-USDx points as the "real" points product. It prices YT-sUSDx close to yield-only fair value (a ~15.5% forward APY after stripping points at the USDx-implied rate).

### Gaps
- There is no official Season-1 end timestamp, no Season-2 plan, no TGE/snapshot date, and no token supply or conversion rate.
- I have no official statement on how Axis counts YT-sUSDx notional (per USDx accounting unit or per sUSDx).

---

## Q7. Risks: liquidity/slippage, YT decay to zero, early snapshot, multiplier changes, underlying risk

### Takeaway
**Liquidity is the binding constraint.** YT-USDx cannot absorb even $10k without about 16% impact, and has no route at $100k. YT-sUSDx takes about $10k at about 4% impact, but $100k costs about 30% on entry and about 30% on exit. Round-trip losses range from about 4% ($1k, sUSDx) to 34% ($10k, USDx) to about 51% ($100k, sUSDx).

### Cited Findings
Exit (sell) simulations via Pendle convert (2026-09-28 11:53:05 UTC; selling the exact YT amounts bought above) — [Pendle Hosted SDK convert](https://api-v2.pendle.finance/core/v3/sdk/1/convert):

| Position | Sell YT amount | Received | USD value | Price impact | Round-trip vs cost |
|---|---|---|---|---|---|
| YT-USDx from $1k | 38,782 | 921.44 USDx | $921.35 | −4.12% | −7.9% |
| YT-USDx from $10k | 337,610 | 6,599.05 USDx | $6,598.47 | −21.12% | **−34.0%** |
| YT-sUSDx from $1k | 31,375 | 931.28 sUSDx | $958.77 | −1.85% | −4.1% |
| YT-sUSDx from $10k | 307,359 | 8,926.99 sUSDx | $9,190.47 | −3.96% | −8.1% |
| YT-sUSDx from $100k | 2,260,195 | 47,567.31 sUSDx | $48,971.28 | −30.41% | **−51.0%** |

- Pool composition: USDx `extendedInfo.floatingSy` 271.27 versus floatingPt 3.36M; sUSDx floatingSy 1,348.59 versus floatingPt 2.87M. AMM implied-APY ranges are 6–27% (USDx) and 8–30% (sUSDx) — [Pendle API v1 market detail](https://api-v2.pendle.finance/core/v1/1/markets/0x0bef762d2094ac80821c657dea6783fc43435292)
- The Axis Ecosystem Vault seeds Pendle liquidity (it "will allocate capital… including… capital used to seed @pendle_fi markets"), so part of the LP depth is protocol-controlled — [Axis Season 1 post](https://www.axis.to/insights/Whats-Next-for-USDx-and-Coordinates)
- Underlying risks, per Pendle's market page: USDx "is not a hard-pegged stablecoin and can trade above or below $1… Exits may be delayed, expensive, or unavailable during market stress"; "Backing assets are held across multiple trading venues and off-chain custodians"; for sUSDx, "Negative yield may occur when market-neutral strategies underperform…" — [Pendle API marketInfo](https://api-v2.pendle.finance/core/v2/markets/all?limit=100&skip=0)
- sUSDx rewards are "fully discretionary… the reward rate is variable" — [Axis docs: Reward Distribution](https://docs.axis.to/susdx-the-rewards-vault/reward-distribution) ; [Axis docs: What is Axis](https://docs.axis.to/start-here/what-is-axis)

### Inferences
- **Price floors within the AMM range** (my calculation, YT = 1 − (1+r)^(−t) at t = 0.17947): YT-USDx is 0.01040 at 6% implied and 0.04199 at 27%. YT-sUSDx is 0.01372 at 8% and 0.04600 at 30%. If implied falls below the range floor (for example on news of an early snapshot or a multiplier cut), AMM liquidity disappears and exit depends on limit orders.
- **YT goes to zero at maturity.** For YT-USDx, 100% of the premium is spent by design. For YT-sUSDx, the loss depends on realized reward funding, which Axis controls at its discretion.
- **Multiplier or season-rule risk:** Axis sets and has already changed its multipliers (Season 0's 2x/1.75x boost was replaced by Season 1 flat rates). A cut to the 24x would reprice YT-USDx immediately.
- **Size guidance for the analyst:** realistic sizing is ≤$3–5k for YT-USDx (7–10% entry impact) and ≤$10–30k for YT-sUSDx (4–11% entry impact). Above these sizes, slippage dominates the economics.
- There is some platform risk from USDx peg or custody events. These would hit sUSDx yield (YT-sUSDx) and could also affect whether Coordinates are honored.

### Gaps
- Limit-order-book depth was not separately inspected. Convert quotes already include limit orders (`useLimitOrder: true`).
- I found no statement on whether Axis will exclude or adjust Pendle YT points on a sybil or post-hoc basis.
- There is no audit link in Pendle's `marketInfo.auditedUrl` (empty) for either market. Axis cites an OpenZeppelin audit of its own contracts — [Axis docs: Origin Vault](https://docs.axis.to/origin-vault/origin-vault)
