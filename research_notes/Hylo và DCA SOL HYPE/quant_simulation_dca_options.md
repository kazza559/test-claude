# Quantitative simulation: DCA-ing $4,000 into SOL or HYPE via spot ladder vs Hylo x-token ladder vs perp ladder

> STATUS: PRELIMINARY (first full run done; final run with spot-price backtests and 2 bps perp spread in progress; numbers below will be replaced).

## Q1. How is each option modelled (formulas, parameters, assumptions)?

### Takeaway
Spot is linear with no leverage. A Hylo x-token with static supplies is a fixed-size leveraged long whose leverage rises as the price falls, and it is wiped out when the price reaches liabilities ÷ collateral. On Variational, a perp's maintenance margin is half the initial margin (25% at 2x, 16.7% at 3x), so a "2x/3x" ladder that puts $1,200 margin into each tranche becomes a 1.8x/2.7x account, which is liquidated 32% or 13% below the third level.

### Cited Findings
- xASSET NAV = (ASSET TVL − vUSD supply) / xASSET supply; CR = collateral × price / vUSD supply; effective leverage = TVL / xASSET market cap — [Hylo Equations](https://docs.hylo.so/technical-addendum/hylo-equations)
- Variational: MM is generally half of IM; 5x = 20% IM / 10% MM — [Variational Leverage](https://docs.variational.io/omni/trading/leverage)
- Partial liquidation, 0.5% penalty — [Variational Liquidation](https://docs.variational.io/omni/trading/liquidation)

### Inferences
- (preliminary) HYPE 80/70/60, interpretation A (margin $1,200/tranche): liquidation after 3rd fill ≈ $40.9 (2x) / $52.2 (3x); interpretation B never liquidates.

### Gaps
- xHYPE base borrow rate not published (assumed 10%/yr).
