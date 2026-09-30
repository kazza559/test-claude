# Quantitative simulation: DCA-ing $4,000 into SOL or HYPE (spot ladder vs Hylo x-token ladder vs 2x/3x perp ladder)

As of 2026-09-30. All simulation numbers come from `quant_simulation_dca_options.py` in this folder. It is pure standard-library Python and reproduces this output exactly from the data snapshot `hl_daily_snapshot.csv`, fetched 2026-09-30 10:24 UTC; `--refresh` re-downloads the data. Everything here is mechanics and numbers only, not an investment recommendation. Unless a line says otherwise, "P&L" is measured on the whole $4,000, including the $400 USDC reserve and any unfilled tranches held as cash.

## 1. How is each option modelled, and what do the Hylo and Variational docs specify?

### Takeaway
- **Spot:** fixed 1x.
- **Hylo x-token with static supplies:** holds a fixed amount of collateral financed by fixed stablecoin debt. Its value is linear in the price, its leverage rises as the price falls, and it is wiped out at the pool's liabilities ÷ collateral price.
- **Hylo V2 x-token:** V2 replaced the old "stability pool converts hyUSD into xSOL below 130% CR" with sell/buy-zone collateral rebalancing at CR <135% and >165%. For a holder, that behaves like a band-rebalanced leveraged token.
- **Variational perps:** fixed-size. The maintenance margin (MM) is half the initial margin (IM): 25% of notional at a 2x setting and 16.7% at 3x. The leverage setting therefore also sets the liquidation threshold.

### Cited Findings
**Hylo (primary docs)**
- xASSET NAV = (ASSET TVL − vUSD supply) / xASSET supply, and NAV defaults to $1 if the supply is zero. Per-asset CR = total collateral × collateral price / vUSD supply. Effective leverage = ASSET TVL / xASSET market cap, which "approaches infinity as CR approaches 100%, and approaches 1 as CR increases" — [Hylo Equations](https://docs.hylo.so/technical-addendum/hylo-equations)
- Each xASSET–vUSD pair targets a CR of 150%, "implying structural leverage at 3x". Leverage "increases when vUSD is minted or xASSET is redeemed" and "decreases when vUSD is burned or xASSET is minted" — [Hylo xASSETs](https://docs.hylo.so/protocol-overview/xassets)
- There are six rebalance zones: <100% Destabilized (xASSET NAV → 0; rebalancing, P&L settlement and minting halt), 100–120% Sell Zone 2, 120–135% Sell Zone 1, 135–165% Neutral, 165–175% Buy Zone 1, ≥175% Buy Zone 2. "These zones replace the former 'stability mode' thresholds" — [Hylo Equations](https://docs.hylo.so/technical-addendum/hylo-equations)
- **Sell zone:** the protocol opens an ASSET→USDC route, "de-leveraging the xASSET and raising the pool's CR toward 135%", capped so it does not overshoot. **Buy zone:** a USDC→ASSET route for arbitrageurs, "re-leveraging the xASSET and bringing the pool's CR down toward 165%". Rebalance prices carry a spread: a protocol profit near the inner bound and a subsidy near the outer bound, settled against the Earn Pool by minting or burning hyUSD — [Hylo Collateral Rebalancing](https://docs.hylo.so/protocol-overview/collateral-rebalancing)
- The xASSET mint/redeem fee schedule by zone (labelled "example") is: Neutral and buy zones 100/100 bps; Sell Zone 1 50/400 bps; Sell Zone 2 0/800 bps; Destabilized, minting and redemption blocked — [Hylo Additional Risk Management](https://docs.hylo.so/technical-addendum/additional-risk-management)
- Below 100% CR the protocol burns Earn Pool hyUSD to retire the unbacked overhang, lifting CR back toward 100%. The burn is capped at the Earn Pool balance. While a drawdown is outstanding, stablecoin minting is frozen and yield harvesting pauses — [Hylo Additional Risk Management](https://docs.hylo.so/technical-addendum/additional-risk-management)
- **Borrow-rate curve (BTC and HYPE pools):**
  - The rate is 0 below 135%, the base rate r_f in 135–165%, and rises linearly to the ceiling r_c at 175%.
  - r_c is "currently 2× the floor rate", and the protocol bounds r_c at about 30% annualized.
  - The rate is charged on the xASSET market cap and lowers the xASSET NAV.
  - Source: [Hylo Equations](https://docs.hylo.so/technical-addendum/hylo-equations). xHYPE pays a borrow rate "with the same mechanism as xBTC" — [Hylo Multi-Asset Architecture](https://docs.hylo.so/protocol-overview/multi-asset-architecture)
- **xSOL carry:**
  - The SOL pool has no floor rate. Instead, a multiplier m(CR) applies to the harvested LST yield: 0 below 135%, 1× in 135–165%, rising to m_c (currently 2) at ≥175%. The amount above 1× comes out of xSOL equity: xSOL rate on exposure = (m − 1) × LST yield — [Hylo Equations](https://docs.hylo.so/technical-addendum/hylo-equations)
  - xSOL leverage is "effectively free from ongoing costs besides the forfeited yield" — [Hylo xASSETs](https://docs.hylo.so/protocol-overview/xassets)
- hyloSOL APY is 5–7% — [Hylo Liquid Staking Tokens](https://docs.hylo.so/product-guide/liquid-staking-tokens). The SOL pool holds jitoSOL/hyloSOL. The HYPE pool holds HYPE on Solana priced by Pyth HYPE/USD — [Hylo Multi-Asset Architecture](https://docs.hylo.so/protocol-overview/multi-asset-architecture). SOL/USD is priced by Pyth — [Hylo Equations](https://docs.hylo.so/technical-addendum/hylo-equations)
- The 150% target is based on SOL's 99.9% one-day VaR of −32.95% — [Hylo VaR Analysis](https://docs.hylo.so/technical-addendum/value-at-risk-analysis)
- eHYUSD is the same token as the former sHYUSD (stability pool); only the ticker changed in V2 — [Hylo Earn Pool](https://docs.hylo.so/protocol-overview/earn-pool)
- In V1, Stability Mode 2 triggered at CR < 130%. Stability-pool hyUSD was converted into xSOL, burning hyUSD and minting xSOL, to restore CR — secondary sources surfaced via web search, not re-read in full: [Donoba](https://donoba.substack.com/p/hylo-enhancing-capital-efficiency), [lavneet.wtf](https://lavneet.wtf/blog/hylo-a-monetary-system-built-on-yield/)

**Variational Omni (primary docs)**
- Leverage = 1 / initial margin %. "The maintenance margin requirement will be half that of the initial margin requirement." Example given: "5x leverage = 20% initial margin requirement and 10% maintenance margin requirement." Also: "Decreasing your leverage may move your estimated liquidation price closer" — [Variational Leverage](https://docs.variational.io/omni/trading/leverage)
- In cross margin, the USDC balance collateralizes every cross position, and liquidations can hit any of them once maintenance-margin usage crosses 100% — [Variational Margin](https://docs.variational.io/omni/trading/margin)
- The liquidation trigger is maintenance margin ≥ 100%, computed with "a very fast EMA of the mark price". Liquidations are partial, and a long is force-closed at bid − 0.5% — [Variational Liquidation](https://docs.variational.io/omni/trading/liquidation)
- There are no trading fees; the protocol earns the spread — [Variational Fees](https://docs.variational.io/omni/trading/fees)
- Funding: F = average premium + clamp(interest − premium, ±0.05%). The interest rate is fixed at 0.00125%/hour (≈10.95%/yr), funding is capped at 2%/hour, and the window runs 1–8h — [Variational Funding Rates](https://docs.variational.io/omni/trading/funding-rates)
- The mark price, derived from an index aggregated across exchanges, is the reference for UPnL, margin and liquidations — [Variational Quoted, Index and Mark Prices](https://docs.variational.io/omni/trading/quoted-index-and-mark-prices)

**Data**
- Hyperliquid `allMids` on 2026-09-30 10:24 UTC: SOL $119.555, HYPE $86.389. The same API supplied daily candles (SOL-PERP from 2023-06-01, HYPE-PERP from 2024-12-05), hourly funding history, and HYPE/USDC spot candles (pair @107) — [Hyperliquid info API](https://api.hyperliquid.xyz/info)
- SOL spot daily OHLC from Coinbase Exchange SOL-USD — [Coinbase Exchange API](https://api.exchange.coinbase.com/products/SOL-USD/candles)

### Inferences (model specification = the stated assumptions)
**Ladders**
- **HYPE:** $1,200 at each of $80, $70 and $60, plus $400 kept in USDC. These levels sit −7.4%, −18.9% and −30.5% from $86.39.
- **HYPE alternative:** 10/20/30% below the current price, i.e. $77.73, $69.09 and $60.46. It was also run; results are within a few points of the main ladder (section 3).
- **SOL:** $120, $105 and $90. The first level is near spot at $119.6; the others are −12.5% and −25%, the same percentage steps as 80/70/60. Because the geometry is identical, spot and perp results in % are exactly equal for SOL and HYPE in the stylized tests; only the x-token carry differs.

**Spot**
- Each buy costs 0.10% (fee plus slippage), and so does the exit. There is an optional 6% staking row for SOL, representing the forgone LST yield.

**Hylo x-token, static baseline**
- The pool starts at CR0 = 1.5, 2.0, 2.5 or 3.0 (≈3x, 2x, 1.67x, 1.5x) when the price is at L1. Supplies are fixed and the user is too small to move the pool.
- The user's value is V(P) = Σk T·(1−f_k)·(P − W)/(L_k − W), where W = D/C = L1/CR0. That is linear in P, so the position is equivalent to a fixed number of "collateral units" financed by fixed debt. Effective leverage at price P is P/(P − W).
- Wipe-out happens when CR ≤ 100% (P ≤ W). The position is then treated as terminal: value 0, redemption blocked.
- Fees are the docs' example zone fees: mint 1% / 0.5% / 0% and redeem 1% / 4% / 8% (Neutral / SZ1 / SZ2).
- **Carry, applied daily at the pool level:**
  - xSOL: LST yield y = 6%/yr with the m(CR) multiplier per the docs. Its cost is (m − 1)·y on TVL, which is 0 in the Neutral zone and +y·TVL (a gain) below 135%.
  - xHYPE: base borrow rate assumed at 10%/yr, ceiling 20%, applied on the x market cap per the docs' curve.

**Hylo x-token, intervention variants**
- **"Sell-zone floor 135%":** at each daily close, if CR < 135%, the pool sells collateral at spot so that CR returns to 135%, keeping the NAV unchanged:
  - C' = E·CR*/(P·(CR* − 1))
  - D' = C'·P − E
  - This caps leverage at ≈3.86x. A V1-style 130% floor (cap 4.33x) was also run.
- **Equivalence of V1 and V2 for a holder:** converting hyUSD into x-tokens at NAV (V1) gives exactly the same per-holder value and exposure as selling collateral to reach the same CR (V2), so both deleverage the holder identically.
- **"V2 band 135–165%":** adds buy-zone re-levering to 165% (≈2.54x) when CR > 165%. It is only meaningful for CR0 = 1.5.
- **Idealisation:** rebalancing is instant, at oracle spot, once per day, with the subsidy borne by the Earn Pool rather than the x-token NAV.

**Perps (Variational rules)**
- Cross margin with the whole $4,000 in the account. IM = 1/leverage and MM = IM/2, i.e. 25% of notional at 2x and 16.7% at 3x.
- **Interpretation A:** $1,200 margin per tranche, i.e. $2,400 notional at 2x or $3,600 at 3x.
- **Interpretation B:** $1,200 notional per tranche.
- **Initial-margin check:** a new tranche is cut to (equity − IM%·existing notional at mark)/IM%. "Full size (no IM cap)" rows show the plan if the venue or extra collateral allowed it.
- **Costs:** 2 bps per open and per close (zero fees plus spread). Funding is 11% APR on notional in the stylized tests, with 5% and 20% as sensitivities. Backtests use Hyperliquid's historical funding as a proxy, with flat 11% as a sensitivity.
- **Liquidation:** partial, whenever equity < MM·notional, checked on intraday sub-steps. Just enough is closed at mark·(1 − 0.02% − 0.5%) to restore equity to MM.
- After the trigger, continuous partial liquidation shrinks the position as q ∝ P^k, with k = (1 − MM)/(MM − 0.52%). Equity therefore behaves like P^4.06 at MM 25% and P^6.16 at MM 16.7%, i.e. a ~4x or ~6x constant-leverage wind-down.

**Price paths**
- Stylized paths are daily, log-linear between waypoints. Backtest days are traversed open → low → close in 24 geometric sub-steps per leg, and limit buys fill at their level (or at the open on a gap).

### Gaps
- The xHYPE base borrow rate is not published in the docs, so 10%/yr was assumed. Carry scales linearly; see the carry column in section 2.
- The live CR of the Hylo SOL and HYPE pools was not retrieved: the docs' OpenAPI file is a Mintlify sandbox placeholder. Starting CR is therefore a scenario parameter, not today's value.
- The rebalance "crossover" points and endpoint spreads are "configurable per asset" and unpublished. Real rebalancing needs arbitrageurs and can lag, so actual leverage could exceed the modelled 3.86x cap during fast drops.
- Variational does not document whether unrealized losses reduce the margin available for new orders; the standard cross-margin behavior was assumed. Per-asset maximum leverage and HYPE-specific spreads were not verified.
- V1 stability-mode details come only from secondary sources.
- The x-token fee values are labelled "example" in the docs.

## 2. What are the liquidation/wipe thresholds, break-even prices and exposures once all tranches are filled?

### Takeaway
**Wipe and liquidation points, HYPE 80/70/60 ladder:**

| Option | Wipe / liquidation price | Distance below the last level ($60) |
|---|---|---|
| Static x-token, CR0 1.5 | $53.3 | −11% |
| Static x-token, CR0 2.0 | $40.0 | −33% |
| Static x-token, CR0 2.5 | $32.0 | −47% |
| Static x-token, CR0 3.0 | $26.7 | −56% |
| Perp A 2x, full size | ≈$40.9 | −32% |
| Perp A 3x, full size | ≈$52.2 | −13% |
| Perp A 2x, third tranche cut by the IM check | ≈$40.0 | −33% |
| Perp A 3x, third tranche cut by the IM check | ≈$48.0 | −20% |
| Perp B, spot ladder | never | — |

**Break-evens** cluster at $66–72.

**Exposure after three fills**, in $ per 1% move at $60: about $31 for spot and perp B, $60–94 for perp A, and $52–179 for static x-tokens.

### Cited Findings
- The formulas used are the NAV, CR and leverage definitions ([Hylo Equations](https://docs.hylo.so/technical-addendum/hylo-equations)) and Variational's MM = IM/2 rule ([Variational Leverage](https://docs.variational.io/omni/trading/leverage)).

### Inferences (own computation)
**A. Static x-token: leverage and wipe-out by starting CR** (the ladder's L2/L3 are −12.5%/−25% from L1)

| CR0 at L1 | Leverage at L1 | Drop from L1 that wipes out | CR / leverage at L2 | CR / leverage at L3 | HYPE wipe price (L1 $80) | Further drop below $60 to wipe | SOL wipe price (L1 $120) | Further drop below $90 | xSOL carry at CR0 (%/yr of equity) | xHYPE carry at CR0 (%/yr, assumed rate) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1.5 | 3.00x | 33.3% | 1.31 / 4.20x | 1.13 / 9.00x | $53.33 | 11.1% | $80.00 | 11.1% | 0% | 10% |
| 2.0 | 2.00x | 50.0% | 1.75 / 2.33x | 1.50 / 3.00x | $40.00 | 33.3% | $60.00 | 33.3% | 12% | 20% |
| 2.5 | 1.67x | 60.0% | 2.19 / 1.84x | 1.88 / 2.14x | $32.00 | 46.7% | $48.00 | 46.7% | 10% | 20% |
| 3.0 | 1.50x | 66.7% | 2.63 / 1.62x | 2.25 / 1.80x | $26.67 | 55.6% | $40.00 | 55.6% | 9% | 20% |

- **Wipe price does not move when you ladder.** It is set by the pool, at W = L1/CR0 under static supplies. Tranches bought lower therefore sit closer to W and carry far more leverage, e.g. 9x at L3 for CR0 1.5.
- **A perp ladder is the reverse:** each extra tranche raises the account's liquidation price.
- **High starting CR costs carry.** Under the docs' curves, a high CR (≥175%) makes xSOL pay 1× the LST yield on TVL, i.e. 9–12%/yr of equity, and xHYPE pay the ceiling rate.

**B. Perp ladder: liquidation price after each tranche** (planned full size; before funding)

| Ladder | Perp | Maintenance margin | Total notional | Account leverage at entry | Liq. after T1 | after T2 | after T3 | Drop below L3 to liq. |
|---|---|---|---|---|---|---|---|---|
| HYPE 80/70/60 | A 2x | 25% (Variational) | $7,200 | 1.80x | none | $16.60 | $40.92 | 31.8% |
| HYPE 80/70/60 | A 3x | 16.7% (Variational) | $10,800 | 2.70x | none | $39.83 | $52.17 | 13.0% |
| HYPE 80/70/60 | A 2x | 3% (generic venue) | $7,200 | 1.80x | none | $12.83 | $31.64 | 47.3% |
| HYPE 80/70/60 | A 3x | 3% (generic venue) | $10,800 | 2.70x | none | $34.22 | $44.82 | 25.3% |
| HYPE 80/70/60 | B (2x or 3x) | 25% / 16.7% | $3,600 | 0.90x | none | none | none | never |
| SOL 120/105/90 | A 2x | 25% | $7,200 | 1.80x | none | $24.89 | $61.38 | 31.8% |
| SOL 120/105/90 | A 3x | 16.7% | $10,800 | 2.70x | none | $59.75 | $78.26 | 13.0% |
| SOL 120/105/90 | B | — | $3,600 | 0.90x | none | none | none | never |

- **Liquidation formula** (cross margin, one asset): P_liq = (Σ q_i·entry_i − cash)/(Q·(1 − MM)). Funding paid raises P_liq by about APR/12 × P/(1 − MM) per month: ≈$0.7/month at $60 with 11% APR.
- **Why B never liquidates:** account equity always exceeds the position value by at least $400, so equity can never fall below any MM fraction of notional. For B, choosing "2x" or "3x" changes nothing.
- **Why a higher MM loosens the plan:** Variational's high MM (25% or 16.7%) moves liquidation up by about $9 (2x) or $7 (3x) versus a 3% MM venue.

**IM check at the third tranche** (HYPE, no funding)

| Perp | Planned T3 notional | Max T3 notional allowed | Share of plan | Liq. after capped T3 |
|---|---|---|---|---|
| A 2x | $2,400 | $2,256 | 94% | $40.00 |
| A 3x | $3,600 | $1,969 | 55% | $48.00 |

- The losses on T1 and T2 by the time price reaches $60 ($943 at 2x, $1,414 at 3x) consume free margin. Under interpretation A the third tranche cannot be placed in full unless more collateral is added.

**Break-even and exposure right after the third fill** (stylized V path, filled on day 40; perps include 40 days of 11% funding; x-token break-evens include the redeem fee of the zone at the break-even price)

| Option | HYPE break-even | HYPE $ per 1% move at $60 | SOL break-even | SOL $ per 1% at $90 |
|---|---|---|---|---|
| Spot ladder | $69.18 | $31.3 | $103.77 | $31.3 |
| Spot ladder + 6% staking (SOL) | — | — | $103.47 | $31.3 |
| x static CR0 1.5 | $65.96 | $179.5 | $98.98 | $175.6 |
| x static CR0 2.0 | $68.33 | $78.5 | $102.37 | $78.5 |
| x static CR0 2.5 | $69.14 | $60.0 | $103.53 | $60.0 |
| x static CR0 3.0 | $69.54 | $52.0 | $104.07 | $52.0 |
| x sell-zone floor 135%, CR0 1.5 | $69.32 | $88.9 | $103.71 | $89.6 |
| x V2 band 135–165%, CR0 1.5 | $69.32 | $88.9 | $103.71 | $89.6 |
| Perp A 2x (IM-capped) | $69.78 | $60.4 | $104.67 | $60.4 |
| Perp A 3x (IM-capped) | $71.67 | $75.8 | $107.51 | $75.8 |
| Perp A 2x/3x full size | $69.43 | $62.6 / $93.8 | $104.15 | $62.6 / $93.8 |
| Perp B | $69.43 | $31.3 | $104.15 | $31.3 |

- **Break-even for the equal-dollar ladder:** $69.04 before costs, the harmonic mean of $80/$70/$60 (3 ÷ (1/80 + 1/70 + 1/60)).
- **Capped perp A 3x has the highest break-even,** because the cheapest tranche was cut to 55%.
- **Static CR 1.5 has the lowest break-even,** because the 9x third tranche dominates.
- **Perp break-evens drift up with funding,** by ≈0.9%/month at 11% APR (≈$0.64/month at $70).

### Gaps
- Break-evens assume the post-fill state is frozen (no further carry, funding or rebalancing).
- Liquidation prices assume the whole $4,000 stays in the account.

## 3. How do the options compare in stylized scenarios?

### Takeaway
- **V-shape:** more leverage wins. Static CR0 1.5 made +106%, perps +23–37%, spot +14%.
- **Continued decline of −30% or −50% below L3:** a −90% result means only the $400 USDC reserve survived.

| Option | −30% below L3 | −50% below L3 |
|---|---|---|
| Static x-token, CR0 1.5 | −90% (wiped) | −90% (wiped) |
| Static x-token, CR0 2.0 | −86% | −90% (wiped) |
| Static x-token, CR0 2.5 | −69% | −90% (wiped) |
| Static x-token, CR0 3.0 | −60% | −86% |
| Perp A 3x (partial liquidation) | −90% | −99% |
| Perp A 2x | −72% | −93% (partially liquidated) |
| Rebalanced x-tokens (never wiped) | −74% to −76% | −86% |
| Spot and perp B | −35% to −37% | −51% to −52% |
- **Rally with only one fill:** gains scale with the leverage of that single tranche, from +14% (spot) to +52% (V2 band).
- **Six-month chop ending at L2:** funding and rebalancing decay turn most leveraged variants negative (perp A 3x −15%, V2 band −44%). Static x-tokens depend only on the end price and carry.

### Cited Findings
- The funding baseline of 0.00125%/h (~11%/yr) is the reference for the 11% case — [Variational Funding Rates](https://docs.variational.io/omni/trading/funding-rates)

### Inferences (own simulation)
**Paths** (daily, log-linear between waypoints; L1/L2/L3 = $80/$70/$60 for HYPE and $120/$105/$90 for SOL):
- **(i)** L1 → L2 on day 20 → L3 on day 40 → back to L1 on day 90.
- **(ii-a)** L1 → L2 → L3 on day 40 → 0.7·L3 on day 90 (HYPE $42, SOL $63).
- **(ii-b)** The same, ending at 0.5·L3 on day 90 (HYPE $30, SOL $45).
- **(iii)** L1 → 1.5·L1 on day 90; only T1 fills.
- **(iv)** Zigzag L1 ↔ L3 six times (15 days per leg), ending at L2 on day 180.

**3a. HYPE 80/70/60: P&L on $4,000 (ending value)** — perp funding 11% APR

| Option | (i) V back to $80 | (ii-a) to $42 | (ii-b) to $30 | (iii) rally to $120 (1 fill) | (iv) choppy, end $70 |
|---|---|---|---|---|---|
| Spot ladder | +14.1% ($4,563) | −35.4% ($2,586) | −51.0% ($1,961) | +14.9% ($4,596) | +1.1% ($4,043) |
| xHYPE static CR0 1.5 | +105.9% ($8,235) | −90.0% ($400), wiped @ $53.4 | −90.0% ($400), wiped @ $53.4 | +41.3% ($5,654) | +26.2% ($5,049) |
| xHYPE static CR0 2.0 | +35.7% ($5,428) | −85.7% ($571) | −90.0% ($400), wiped @ $40.5 | +26.7% ($5,069) | −0.7% ($3,974) |
| xHYPE static CR0 2.5 | +24.4% ($4,975) | −68.6% ($1,256) | −90.0% ($400), wiped @ $32.9 | +21.9% ($4,877) | −5.4% ($3,784) |
| xHYPE static CR0 3.0 | +19.9% ($4,798) | −60.2% ($1,590) | −85.8% ($568) | +19.5% ($4,781) | −6.5% ($3,742) |
| xHYPE sell-zone floor 135%, CR0 1.5 | +36.0% ($5,441) | −76.1% ($956) | −86.4% ($546) | +41.3% ($5,654) | −6.2% ($3,753) |
| xHYPE sell-zone floor 135%, CR0 2.0 | +35.7% ($5,428) | −73.7% ($1,053) | −85.7% ($572) | +26.7% ($5,069) | −0.7% ($3,974) |
| xHYPE V2 band 135–165%, CR0 1.5 | +37.6% ($5,505) | −76.1% ($956) | −86.4% ($546) | +51.7% ($6,067) | −43.6% ($2,256) |
| Perp A 2x (IM-capped) | +23.0% ($4,921) | −71.8% ($1,128) | −92.7% ($290); liq. from $40.6, 61% closed | +28.0% ($5,118) | −7.4% ($3,704) |
| Perp A 3x (IM-capped) | +22.9% ($4,917) | −90.0% ($400); liq. from $48.6, 55% closed | −98.7% ($50); liq. from $48.3, 92% closed | +41.9% ($5,677) | −15.0% ($3,400) |
| Perp A 2x full size | +24.8% ($4,990) | −73.5% ($1,059); liq. from $42.4, 3% closed | −93.2% ($271); liq. from $41.9, 65% closed | +28.0% ($5,118) | −6.9% ($3,723) |
| Perp A 3x full size | +37.1% ($5,485) | −92.3% ($310); liq. from $53.0, 72% closed | −99.0% ($39); liq. from $52.8, 95% closed | +41.9% ($5,677) | −10.4% ($3,584) |
| Perp B (2x or 3x setting) | +12.4% ($4,495) | −36.8% ($2,530) | −52.3% ($1,910) | +14.0% ($4,559) | −3.5% ($3,861) |

**3b. HYPE: maximum drawdown of the $4,000 account**

| Option | (i) | (ii-a) | (ii-b) | (iii) | (iv) |
|---|---|---|---|---|---|
| Spot ladder | 11.9% | 35.3% | 50.9% | 0.0% | 22.8% |
| x static 1.5 | 40.8% | 90.0% | 90.0% | 0.3% | 72.6% |
| x static 2.0 | 26.3% | 85.4% | 90.0% | 0.3% | 50.6% |
| x static 2.5 | 22.0% | 67.7% | 90.0% | 0.3% | 44.0% |
| x static 3.0 | 19.8% | 59.9% | 85.4% | 0.3% | 40.1% |
| x floor 135%, CR0 1.5 | 33.6% | 76.0% | 86.3% | 0.3% | 55.2% |
| x V2 band, CR0 1.5 | 33.6% | 76.0% | 86.3% | 0.3% | 72.2% |
| Perp A 2x (capped) | 24.6% | 71.8% | 92.7% | 0.0% | 46.0% |
| Perp A 3x (capped) | 36.9% | 90.0% | 98.7% | 0.0% | 57.5% |
| Perp A 3x full | 36.9% | 92.2% | 99.0% | 0.0% | 63.3% |
| Perp B | 12.3% | 36.7% | 52.2% | 0.0% | 26.2% |

**3c. SOL 120/105/90: P&L** (spot and perp rows are identical in % to HYPE; only the x-token carry model differs)

| Option | (i) V back to $120 | (ii-a) to $63 | (ii-b) to $45 | (iii) rally to $180 | (iv) choppy, end $105 |
|---|---|---|---|---|---|
| Spot ladder | +14.1% | −35.4% | −51.0% | +14.9% | +1.1% |
| Spot ladder + 6% staking | +15.3% | −34.7% | −50.5% | +15.6% | +3.7% |
| xSOL static CR0 1.5 | +107.4% ($8,295) | −90.0%, wiped @ $79.5 | −90.0%, wiped @ $79.6 | +42.7% | +37.0% |
| xSOL static CR0 2.0 | +37.3% | −84.7% | −90.0%, wiped @ $60.5 | +28.0% | +2.8% |
| xSOL static CR0 2.5 | +26.0% | −67.9% | −90.0%, wiped @ $49.0 | +23.2% | −2.1% |
| xSOL static CR0 3.0 | +21.7% | −59.5% | −85.2% | +20.8% | −2.6% |
| xSOL floor 135%, CR0 1.5 | +38.4% | −75.5% | −86.2% | +42.7% | −1.6% |
| xSOL floor 135%, CR0 2.0 | +37.3% | −73.1% | −85.5% | +28.0% | +2.8% |
| xSOL V2 band, CR0 1.5 | +40.3% | −75.5% | −86.2% | +53.6% | −40.8% |
| Perp A 2x / A 3x (capped) / B | +23.0% / +22.9% / +12.4% | −71.8% / −90.0% (liq.) / −36.8% | −92.7% (liq.) / −98.7% (liq.) / −52.3% | +28.0% / +41.9% / +14.0% | −7.4% / −15.0% / −3.5% |

- xSOL does slightly better than xHYPE because xSOL pays no carry in the Neutral zone and gains the LST yield below 135% CR, whereas xHYPE pays the assumed 10–20% borrow rate.

**3d. HYPE alternative ladder $77.73/$69.09/$60.46 (−10/−20/−30% of current): P&L**

| Option | (i) to $77.73 | (ii-a) to $42.32 | (ii-b) to $30.23 | (iii) to $116.59 | (iv) end $69.09 |
|---|---|---|---|---|---|
| Spot | +12.1% | −34.4% | −50.3% | +14.9% | +0.8% |
| x static 1.5 | +72.7% | −90.0% (wiped @ $51.9) | −90.0% (wiped) | +41.3% | +13.1% |
| x static 2.0 | +28.1% | −81.7% | −90.0% (wiped @ $39.5) | +26.7% | −2.9% |
| x static 3.0 | +16.0% | −58.3% | −83.9% | +19.5% | −7.3% |
| x floor 135%, CR0 1.5 | +32.1% | −75.4% | −86.2% | +41.3% | −5.5% |
| x V2 band | +32.6% | −75.4% | −86.2% | +51.7% | −29.7% |
| Perp A 2x | +20.1% | −70.8% | −92.5% (liq.) | +28.0% | −7.7% |
| Perp A 3x | +21.3% | −89.3% (liq.) | −98.7% (liq.) | +41.9% | −14.2% |
| Perp B | +10.4% | −35.8% | −51.6% | +14.0% | −3.8% |

**3e. Perp funding sensitivity (HYPE 80/70/60, IM-capped; "L" = at least one partial liquidation)**

| Scenario | A2x 5% | A2x 11% | A2x 20% | A3x 5% | A3x 11% | A3x 20% | B 5% | B 11% | B 20% |
|---|---|---|---|---|---|---|---|---|---|
| (i) V-shape | +25.3% | +23.0% | +19.6% | +26.3% | +22.9% | +17.9% | +13.4% | +12.4% | +10.8% |
| (ii-a) −30% below L3 | −70.5% | −71.8% | −73.7% | −89.3% L | −90.0% L | −91.0% L | −35.9% | −36.8% | −38.0% |
| (ii-b) −50% below L3 | −92.4% L | −92.7% L | −93.2% L | −98.7% L | −98.7% L | −98.9% L | −51.5% | −52.3% | −53.4% |
| (iii) +50% rally | +29.0% | +28.0% | +26.3% | +43.6% | +41.9% | +39.5% | +14.5% | +14.0% | +13.2% |
| (iv) 6-month chop | −2.4% | −7.4% | −14.9% | −8.6% | −15.0% | −24.6% | −0.9% | −3.5% | −7.3% |

- In the 6-month chop, each extra 10 percentage points of funding APR costs about 8 points of the $4,000 for A 2x (notional ≈$7k), about 11 points for A 3x, and about 4 points for B. These are the table's slopes between 5% and 20%.

**3f. x-token sensitivity (HYPE)**

| Scenario | Floor 135%, CR0 1.5 | Floor 130% (V1-style), CR0 1.5 | Static 1.5, no carry/fees | Static 2.0, no carry/fees | Static 3.0, no carry/fees |
|---|---|---|---|---|---|
| (i) | +36.0% | +40.4% | +108.0% | +40.0% | +24.9% |
| (ii-a) | −76.1% | −79.1% | −90.0% (wiped) | −83.5% | −57.0% |
| (ii-b) | −86.4% | −87.6% | −90.0% (wiped) | −90.0% (wiped) | −82.8% |
| (iii) | +41.3% | +41.3% | +45.0% | +30.0% | +22.5% |
| (iv) | −6.2% | −4.1% | +33.8% | +7.5% | +3.4% |

- In the choppy path, fees and carry cost static x-tokens 8–10 points of the $4,000 (e.g. static 3.0: −6.5% with vs +3.4% without). That includes the 4–8% redeem fees when exiting in sell zones.

### Gaps
- The stylized paths are smooth (≈1.4–1.9% daily moves), which is well below HYPE/SOL realized volatility of 55–130%/yr. Real chop would add more decay to the rebalanced variants.
- Scenario horizons (90/180 days) and the timing of waypoints are arbitrary choices.

## 4. What do historical backtests (2024–2026) show?

### Takeaway
- **SOL (28 monthly-start windows, 180-day hold, Jan 2024 – Apr 2026 starts):**
  - Spot median P&L was −0.8% (worst −51%).
  - Leverage widened outcomes without raising the median: perp A 3x median −20% with liquidation in 10/28 windows; static xSOL CR0 1.5 wiped in 14/28.
- **HYPE (17 windows, Dec 2024 – Apr 2026 starts; HYPE rose from $12.7 to $86):**
  - Leverage raised medians: perp A 2x +72%, x floor 135% CR0 2.0 +73%, spot +47%.
  - It also produced liquidation or wipe-out in 6–9 of 17 windows for A 2x, A 3x and static CR0 1.5.
- **Spot and perp B were never liquidated** in any window.

### Cited Findings
- Price sources: Hyperliquid info API (candles, funding, HYPE/USDC spot) — [Hyperliquid info API](https://api.hyperliquid.xyz/info); Coinbase SOL-USD daily candles — [Coinbase Exchange API](https://api.exchange.coinbase.com/products/SOL-USD/candles)
- **Venue-specific wicks:**
  - SOL: On 2025-10-10, Hyperliquid SOL-PERP printed a low of $137.51, 37.8% below the prior close of $221.00. Coinbase SOL-USD's low that day was $176.85, 20.0% below its $221.03 open.
  - HYPE: HYPE-PERP's low was $31.80 (−27.7%); Hyperliquid spot HYPE/USDC's low was $34.49 (−21.6%).
  - On 2024-01-03, SOL-PERP's low was $61.00 against Coinbase's $85.50.
  - Source for all of the above: [Hyperliquid info API](https://api.hyperliquid.xyz/info), [Coinbase Exchange API](https://api.exchange.coinbase.com/products/SOL-USD/candles)
  - For comparison, CoinGecko's aggregated 4-day OHLC low around 2025-10-10 was $176.73 — [CoinGecko API](https://api.coingecko.com/api/v3/coins/solana/ohlc?vs_currency=usd&days=365)
- Hylo prices collateral with Pyth oracles ([Hylo Equations](https://docs.hylo.so/technical-addendum/hylo-equations)). Variational liquidates on a fast EMA of a mark price built from an aggregated index ([Variational Liquidation](https://docs.variational.io/omni/trading/liquidation)). For both, spot/aggregated prices are closer to the relevant price than perp wicks, which is why spot OHLC is the main backtest source.
- Hyperliquid funding, mean over each period (computed from hourly history):

| Asset | Full available history | 2025-01-01 to 2026-09-29 |
|---|---|---|
| SOL | 12.2% APR (2024-01-01 to 2026-09-29) | 3.0% APR |
| HYPE | 20.6% APR (2024-12-05 to 2026-09-29) | 16.6% APR |

  Source: [Hyperliquid info API](https://api.hyperliquid.xyz/info)

### Inferences (own simulation)
**Setup**
- Ladder: L1 = the start-day spot close, L2 = −12.5%, L3 = −25%, with the same $1,200/$1,200/$1,200 + $400 split.
- Windows start on the 1st of each month (plus 2024-12-05 for HYPE, its first data day) and are held for 180 days. Perp funding uses Hyperliquid's daily historical funding.
- Windows overlap and are not independent, and HYPE's period was dominated by one uptrend. Treat the medians as descriptive, not predictive.

**4a. SOL summary (spot prices; last two columns use Hyperliquid perp prices, including wicks)**

| Option | Median P&L | Mean | Worst | Best | % windows losing | Liq/wipe windows | Median max DD | Worst max DD | Median P&L (perp px) | Liq/wipe (perp px) |
|---|---|---|---|---|---|---|---|---|---|---|
| Spot ladder | −0.8% | +7.6% | −51.4% | +65.4% | 50% | 0/28 | 33.7% | 59.0% | −0.9% | 0/28 |
| xSOL static CR0 1.5 | −59.5% | +3.9% | −90.0% | +396.1% | 64% | 14/28 | 84.5% | 96.4% | −90.0% | 15/28 |
| xSOL static CR0 2.0 | −2.6% | +11.8% | −90.0% | +161.2% | 50% | 7/28 | 56.3% | 94.0% | −2.6% | 7/28 |
| xSOL static CR0 2.5 | −3.9% | +9.2% | −90.0% | +121.0% | 50% | 4/28 | 51.1% | 93.3% | −3.8% | 4/28 |
| xSOL static CR0 3.0 | −4.2% | +8.2% | −90.0% | +103.9% | 50% | 2/28 | 48.1% | 91.0% | −4.4% | 2/28 |
| xSOL floor 135%, CR0 1.5 | −19.9% | +17.9% | −87.7% | +177.9% | 54% | 0/28 | 69.7% | 92.5% | −20.7% | 2/28 |
| xSOL floor 135%, CR0 2.0 | −14.1% | +14.9% | −87.1% | +161.2% | 54% | 0/28 | 56.3% | 91.7% | −14.3% | 0/28 |
| xSOL V2 band, CR0 1.5 | −30.0% | +0.9% | −87.8% | +233.1% | 61% | 0/28 | 77.5% | 93.1% | −34.2% | 7/28 |
| Perp A 2x | −7.8% | +5.7% | −93.5% | +119.0% | 54% | 7/28 | 59.0% | 96.8% | −7.8% | 7/28 |
| Perp A 3x | −20.0% | +3.0% | −99.1% | +146.1% | 54% | 10/28 | 69.4% | 99.7% | −19.9% | 11/28 |
| Perp B | −3.3% | +3.8% | −50.5% | +60.9% | 50% | 0/28 | 36.9% | 59.6% | −3.2% | 0/28 |
| Daily-rebalanced 2x (reference) | −14.8% | +6.3% | −77.0% | +143.3% | 61% | 0/28 | 59.7% | 84.0% | −14.8% | 0/28 |
| Daily-rebalanced 3x (reference) | −33.3% | −3.4% | −86.6% | +235.3% | 61% | 0/28 | 76.2% | 91.9% | −37.6% | 4/28 |

- With a flat 11% funding instead of the historical rate, SOL medians are: A 2x −8.1%, A 3x −22.0%, B −3.7%. Liquidation counts are unchanged at 7, 11 and 0.

**4b. SOL per-window P&L (spot prices; W = wiped, L = liquidated)**

| Start | L1 | End vs L1 | Min vs L1 | Fills | Spot | x st 1.5 | x st 2.0 | x st 3.0 | x fl135 1.5 | x band | Perp A 2x | Perp A 3x | Perp B | Daily 3x |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2024-01-01 | $110.11 | +27% | −29% | 3 | +42% | +247% | +98% | +63% | +109% | +11% | +36% | +38% | +20% | +18% |
| 2024-02-01 | $97.78 | +83% | −5% | 1 | +25% | +70% | +46% | +34% | +70% | +30% | +35% | +52% | +17% | +31% |
| 2024-03-01 | $129.53 | +11% | −15% | 2 | +11% | +37% | +19% | +13% | +37% | −27% | +3% | +5% | +2% | −31% |
| 2024-04-01 | $192.35 | −18% | −43% | 3 | −5% | −90% W | −10% | −12% | −30% | −57% | −21% | −57% L | −10% | −62% |
| 2024-05-01 | $134.46 | +33% | −18% | 2 | +25% | +97% | +53% | +37% | +97% | +91% | +44% | +66% | +22% | +39% |
| 2024-06-01 | $165.99 | +43% | −34% | 3 | +59% | −90% W | +148% | +94% | +157% | +127% | +96% | +115% | +50% | +91% |
| 2024-07-01 | $146.52 | +33% | −25% | 2 | +25% | +90% | +50% | +35% | +72% | +16% | +34% | +51% | +17% | +13% |
| 2024-08-01 | $167.22 | +36% | −34% | 3 | +51% | −90% W | +124% | +79% | +134% | +89% | +77% | +92% | +40% | +60% |
| 2024-09-01 | $128.50 | +15% | −6% | 1 | +5% | +9% | +5% | +4% | +9% | −19% | +0% | +0% | +0% | −13% |
| 2024-10-01 | $145.10 | −14% | −23% | 2 | −5% | −20% | −14% | −11% | −20% | −33% | −17% | −25% | −8% | −40% |
| 2024-11-01 | $166.02 | −11% | −43% | 3 | +3% | −90% W | +11% | +2% | −26% | −35% | −2% | −25% L | +0% | −35% |
| 2024-12-01 | $236.95 | −34% | −60% | 3 | −21% | −90% W | −90% W | −38% | −77% | −82% | −67% L | −91% L | −24% | −80% |
| 2025-01-01 | $193.84 | −20% | −51% | 3 | −7% | −90% W | −90% W | −15% | −58% | −69% | −19% L | −66% L | −8% | −67% |
| 2025-02-01 | $212.94 | −19% | −55% | 3 | −6% | −90% W | −90% W | −12% | −65% | −72% | −35% L | −77% L | −8% | −67% |
| 2025-03-01 | $143.59 | +49% | −34% | 3 | +65% | −90% W | +161% | +104% | +148% | +133% | +119% | +146% | +61% | +130% |
| 2025-04-01 | $126.69 | +66% | −25% | 2 | +47% | +164% | +96% | +68% | +121% | +95% | +85% | +128% | +43% | +99% |
| 2025-05-01 | $150.89 | +29% | −16% | 2 | +23% | +80% | +45% | +31% | +69% | +33% | +39% | +59% | +20% | +15% |
| 2025-06-01 | $157.76 | −13% | −23% | 2 | −4% | −20% | −14% | −11% | −21% | −40% | −13% | −20% | −7% | −40% |
| 2025-07-01 | $146.92 | −15% | −20% | 2 | −5% | −21% | −15% | −12% | −20% | −27% | −13% | −20% | −7% | −27% |
| 2025-08-01 | $162.66 | −23% | −28% | 3 | −10% | −29% | −24% | −20% | −30% | −34% | −22% | −34% | −11% | −42% |
| 2025-09-01 | $197.32 | −57% | −66% | 3 | −45% | −90% W | −90% W | −90% W | −86% | −86% | −89% L | −98% L | −45% | −84% |
| 2025-10-01 | $222.15 | −63% | −70% | 3 | −51% | −90% W | −90% W | −90% W | −88% | −88% | −94% L | −99% L | −50% | −87% |
| 2025-11-01 | $186.26 | −55% | −64% | 3 | −44% | −90% W | −90% W | −73% | −85% | −85% | −87% L | −97% L | −43% | −84% |
| 2025-12-01 | $126.66 | −35% | −47% | 3 | −22% | −90% W | −52% | −40% | −66% | −67% | −41% | −70% L | −21% | −65% |
| 2026-01-01 | $126.73 | −42% | −53% | 3 | −30% | −90% W | −90% W | −52% | −77% | −78% | −57% L | −84% L | −28% | −74% |
| 2026-02-01 | $100.66 | −28% | −40% | 3 | −15% | −90% W | −35% | −29% | −53% | −55% | −27% | −39% | −13% | −58% |
| 2026-03-01 | $83.60 | +25% | −28% | 3 | +40% | +271% | +107% | +66% | +102% | +120% | +76% | +92% | +39% | +127% |
| 2026-04-01 | $81.17 | +46% | −26% | 3 | +62% | +396% | +161% | +102% | +178% | +233% | +117% | +143% | +60% | +235% |

**4c. HYPE summary (spot prices = Hyperliquid spot HYPE/USDC; last two columns = HYPE-PERP prices)**

| Option | Median P&L | Mean | Worst | Best | % windows losing | Liq/wipe windows | Median max DD | Worst max DD | Median P&L (perp px) | Liq/wipe (perp px) |
|---|---|---|---|---|---|---|---|---|---|---|
| Spot ladder | +46.8% | +70.7% | −18.5% | +278.9% | 18% | 0/17 | 38.2% | 60.2% | +46.9% | 0/17 |
| xHYPE static CR0 1.5 | −90.0% | +270.4% | −90.0% | +2,992.6% | 53% | 9/17 | 91.1% | 95.6% | −90.0% | 9/17 |
| xHYPE static CR0 2.0 | +17.5% | +93.2% | −90.0% | +633.5% | 41% | 6/17 | 67.2% | 93.2% | +16.1% | 6/17 |
| xHYPE static CR0 2.5 | +60.1% | +96.6% | −90.0% | +481.0% | 29% | 2/17 | 60.3% | 92.5% | +60.0% | 2/17 |
| xHYPE static CR0 3.0 | +62.8% | +106.0% | −36.4% | +415.1% | 18% | 0/17 | 56.5% | 92.2% | +62.9% | 0/17 |
| xHYPE floor 135%, CR0 1.5 | +52.9% | +123.4% | −68.6% | +718.5% | 41% | 0/17 | 76.6% | 92.2% | +53.4% | 0/17 |
| xHYPE floor 135%, CR0 2.0 | +72.8% | +112.8% | −64.3% | +633.5% | 41% | 0/17 | 67.2% | 91.6% | +72.7% | 0/17 |
| xHYPE V2 band, CR0 1.5 | +67.0% | +210.6% | −75.7% | +1,310.6% | 41% | 0/17 | 81.0% | 92.7% | +65.0% | 0/17 |
| Perp A 2x | +71.6% | +92.6% | −50.8% | +486.6% | 29% | 6/17 | 68.0% | 97.0% | +71.4% | 6/17 |
| Perp A 3x | +17.1% | +95.1% | −90.5% | +609.8% | 41% | 8/17 | 85.0% | 99.6% | +17.4% | 8/17 |
| Perp B | +44.4% | +63.0% | −21.5% | +250.3% | 18% | 0/17 | 40.0% | 65.1% | +44.5% | 0/17 |
| Daily-rebalanced 2x (reference) | +83.0% | +159.9% | −46.7% | +877.9% | 29% | 0/17 | 64.1% | 84.4% | +83.1% | 0/17 |
| Daily-rebalanced 3x (reference) | +71.2% | +236.8% | −73.8% | +1,564.1% | 41% | 0/17 | 77.7% | 91.0% | +71.3% | 0/17 |

- With a flat 11% funding instead of the historical rate, HYPE medians are: A 2x +77.0%, A 3x +30.2%, B +44.2%. Liquidation counts are unchanged at 6, 8 and 0.

**4d. HYPE per-window P&L (spot prices; W = wiped, L = liquidated)**

| Start | L1 | End vs L1 | Min vs L1 | Fills | Spot | x st 1.5 | x st 2.0 | x st 3.0 | x fl135 1.5 | x band | Perp A 2x | Perp A 3x | Perp B | Daily 3x |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2024-12-05 | $12.71 | +184% | −27% | 3 | +205% | +2993% | +626% | +376% | +634% | +1246% | +271% | +324% | +188% | +1351% |
| 2025-01-01 | $26.32 | +50% | −65% | 3 | +67% | −90% W | −90% W | +99% | −56% | −40% | −50% L | −91% L | +54% | −23% |
| 2025-02-01 | $23.19 | +76% | −60% | 3 | +93% | −90% W | −90% W | +139% | −27% | +15% | +17% L | −68% L | +79% | +47% |
| 2025-03-01 | $19.61 | +132% | −53% | 3 | +152% | −90% W | −90% W | +227% | +53% | +185% | +184% L | +17% L | +135% | +261% |
| 2025-04-01 | $13.32 | +254% | −30% | 3 | +279% | +1485% | +633% | +415% | +718% | +1311% | +487% | +610% | +250% | +1564% |
| 2025-05-01 | $19.93 | +139% | −3% | 1 | +42% | +111% | +73% | +54% | +111% | +67% | +72% | +107% | +36% | +78% |
| 2025-06-01 | $34.19 | +2% | −14% | 2 | +6% | +24% | +10% | +5% | +12% | −4% | +5% | +7% | +2% | −5% |
| 2025-07-01 | $36.88 | −31% | −40% | 3 | −18% | −90% W | −51% | −36% | −59% | −61% | −42% | −59% L | −22% | −57% |
| 2025-08-01 | $37.59 | −8% | −45% | 3 | +5% | −90% W | +17% | +6% | −41% | −46% | +3% | −40% L | +2% | −34% |
| 2025-09-01 | $43.10 | −28% | −52% | 3 | −15% | −90% W | −90% W | −29% | −68% | −75% | −45% L | −80% L | −18% | −72% |
| 2025-10-01 | $47.26 | −22% | −57% | 3 | −9% | −90% W | −90% W | −20% | −69% | −76% | −51% L | −85% L | −12% | −74% |
| 2025-11-01 | $43.27 | −8% | −53% | 3 | +6% | −90% W | −90% W | +3% | −57% | −61% | −15% L | −67% L | +2% | −57% |
| 2025-12-01 | $31.00 | +120% | −34% | 3 | +139% | −90% W | +333% | +215% | +225% | +391% | +262% | +325% | +135% | +391% |
| 2026-01-01 | $24.23 | +168% | −15% | 2 | +112% | +384% | +226% | +160% | +335% | +379% | +215% | +323% | +108% | +326% |
| 2026-02-01 | $30.56 | +72% | −16% | 2 | +50% | +164% | +95% | +66% | +140% | +79% | +92% | +138% | +46% | +71% |
| 2026-03-01 | $31.56 | +156% | −7% | 1 | +47% | +129% | +85% | +63% | +129% | +147% | +89% | +133% | +44% | +141% |
| 2026-04-01 | $36.02 | +143% | −4% | 1 | +43% | +117% | +77% | +57% | +117% | +121% | +81% | +121% | +40% | +120% |

**Observations**
- **Ladder cost only matters on liquidation or wipe-out.** A deep dip followed by a strong recovery is the typical "ladder works" path, e.g. HYPE 2025-01 to 2025-03: min −53% to −65%, end +50% to +132%. On that path spot made +67% to +152%, but perp A 3x was liquidated (−91% to +17%) and static CR0 ≤ 2.0 was wiped (−90%). The ladder's value comes from buying the dip, and leverage forfeits it whenever the dip exceeds the wipe or liquidation distance.
- **Rebalanced x-tokens replace wipe-out with deleverage-then-lag.** The floor and band variants were never wiped on spot prices, but in the same dip-and-recovery windows they recovered much less than spot (e.g. HYPE 2025-01: floor 135% −56% vs spot +67%). That is the cost of deleveraging near the bottom.
- **Funding matters for perps, and was lower recently.**
  - SOL's realized Hyperliquid funding was 25–36% APR in windows starting Jan–Mar 2024 but −1% to −4% APR in windows starting Sep 2025 – Feb 2026.
  - Perp B trailed spot by about 2.5 points on the median in SOL and about 2.4 points in HYPE over 180 days.
- **The 2024-12-05 HYPE window is an outlier:** static CR0 1.5 made +2,993%. The third tranche was bought at 9x leverage just above the wipe price before a +184% move. It illustrates the unbounded convexity of static supplies near W.
- **Wick sensitivity:**
  - Using Hyperliquid perp OHLC instead of spot mostly changes the rebalanced SOL variants and the daily 3x reference: xSOL V2 band wipes go from 0/28 to 7/28, floor 135% from 0/28 to 2/28, daily 3x from 0/28 to 4/28, mainly because of the 2025-10-10 SOL-PERP wick.
  - Static x-tokens and perps are barely affected. For the SOL 2024-01-01 window, static CR0 1.5 flips from +247% (spot low −29%) to −90% (perp wick −45%).

### Gaps
- Variational's own historical funding and prices were not available; Hyperliquid is the proxy.
- Only 17 HYPE windows (one regime: a +580% rise from $12.7 to $86 overall) and 28 SOL windows exist, and they overlap.
- Hylo's actual pool CR history was not used; the static CR is a parameter.

## 5. How does path dependence differ across fixed-size perps, daily-rebalanced tokens and Hylo x-tokens?

### Takeaway
- **Price-path independent (no volatility decay):** a static-supply Hylo x-token and a fixed-size perp. Their value depends only on the current price, but each carries a hard threshold: the pool-wide wipe price for the x-token, the liquidation price for the perp. The perp also pays funding.
- **Volatility decay:** products that re-target leverage. That covers daily-rebalanced 2x/3x, and Hylo V2 in practice, since its sell/buy zones deleverage low and re-lever high. In the tests they lost 0.4–58% of a tranche's value when the price simply returned to its start: daily 3x lost up to 18%, and the V2 band up to 58% in ±25% swings.

### Cited Findings
- Hylo warns that "Volatility decay causes leveraged tokens to lose value over time in sideways markets" and that xASSET value is path-dependent. Its example: SOL $100 → $80 → $100 takes a 2x xSOL from $100 → $60 → $90 — [Hylo xASSETs](https://docs.hylo.so/protocol-overview/xassets)
- xASSET leverage "fluctuates dynamically with protocol activity". It increases when vUSD is minted or xASSET redeemed, and decreases when vUSD is burned or xASSET minted. The docs' example: a pool of $100 SOL backing $50 vUSD and $50 xSOL is 2x; +$50 vUSD makes it 3x; −$25 vUSD makes it 1.5x — [Hylo xASSETs](https://docs.hylo.so/protocol-overview/xassets)
- Leveraged ETFs that rebalance daily have value that depends on realized volatility; with high volatility, "the median investor will experience a long-run erosion in value" — Cheng & Madhavan (2009), [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1539120) (summary via search; paper not re-read)
- Variational liquidations are partial — [Variational Liquidation](https://docs.variational.io/omni/trading/liquidation)

### Inferences (own simulation and derivations)
**Single $1,200 tranche bought at $80; price returns to $80; no fees, carry or funding**

| Product | V: 80 → 60 → 80 (90 days) | Zigzag 80 ↔ 60 ×6 (180 days) | Zigzag 80 ↔ 70 ×12 (180 days) |
|---|---|---|---|
| Spot | $1,200 (0.0%) | $1,200 (0.0%) | $1,200 (0.0%) |
| x-token static CR0 1.5 (3x at entry) | $1,200 (0.0%) | $1,200 (0.0%) | $1,200 (0.0%) |
| x-token static CR0 2.0 (2x at entry) | $1,200 (0.0%) | $1,200 (0.0%) | $1,200 (0.0%) |
| x-token V2 band 135–165% | $956 (−20.3%) | $499 (−58.4%) | $1,166 (−2.9%) |
| Daily-rebalanced 2x | $1,196 (−0.4%) | $1,123 (−6.4%) | $1,133 (−5.6%) |
| Daily-rebalanced 3x | $1,187 (−1.1%) | $984 (−18.0%) | $1,010 (−15.9%) |
| Perp 3x, fixed $3,600 notional | $1,200 (0.0%) | $1,200 (0.0%) | $1,200 (0.0%) |

- **Hylo's own decay example assumes rebalancing.** With static supplies at CR 2, the docs' path gives xSOL $100 → $60 → $100 (TVL 200 → 160 → 200 against vUSD 100). The docs' $90 requires the leverage to be reset to 2x at $80 (60 × 1.5 = 90). So xSOL decays only through supply changes: V2 zone rebalancing, the V1 stability-pool conversion, or other users' flows.
- **Static x-token equals a perp with no maintenance margin or liquidation engine:** V = u·P − d. Equity goes to zero at the pool's W rather than being liquidated early. But W is shared by all holders and does not depend on your own entries. Under V2, a sub-100% CR is handled by burning Earn Pool hyUSD, and x-token NAV → 0 while redemptions are blocked.
- **Other users' flows change your leverage with no action from you.** Worked example (docs' equations):
  - Starting pool: TVL $150, vUSD $100, x market cap $50 (CR 1.5, 3x).
  - Others mint $50 of hyUSD → TVL $200, vUSD $150 → CR 1.33, leverage 4x.
  - Others instead mint $50 of x-tokens → TVL $200, vUSD $100 → CR 2.0, leverage 2x.
- **The two intervention mechanisms treat holders identically.** V1's hyUSD→x conversion and V2's collateral sale both keep NAV unchanged at the moment of intervention and cut the holder's exposure to CR*/(CR* − 1) times their equity. That deleveraging is what caps losses in a slide (−76% instead of wiped out in the −30% scenario). It also produces the decay seen above and the weaker recoveries after deep dips (section 4).
- **Fixed-size perps have no decay,** but carry two costs:
  - Funding: ≈0.9% of notional per month at 11% APR.
  - Liquidation: after the MM trigger, partial liquidation turns the account into a shrinking ~4x (MM 25%) or ~6x (MM 16.7%) constant-leverage position (equity ∝ P^4.06 or P^6.16). Losses below the trigger therefore accelerate rather than stopping at a single liquidation.

### Gaps
- Real Hylo leverage paths depend on unobserved protocol-wide mint/redeem flows and arbitrage timing. None of these were simulated beyond the idealized zone rules.
- The LETF literature was consulted only via a search summary.
