# Hylo (hylo.so) core mechanism: hyUSD, xSOL and the stability pool (sHYUSD, now called eHYUSD), as of 30 Sep 2026

Scope note for the report writer: Hylo changed its design in mid-2026. **V1** (public launch around July–August 2025, through mid-June 2026) had a SOL-only pool, a "stability mode" system (150% / 130%) and a **Stability Pool** (sHYUSD) that turned hyUSD into xSOL during stress. **V2** (early access late March 2026; full launch about 17 June 2026) has separate collateral pools (SOL, BTC, HYPE, USDC), six CR "rebalance zones", USDC-based collateral rebalancing, and an **Earn Pool**. In V2, sHYUSD was renamed **eHYUSD** (same mint) and no longer takes on xSOL. Unless marked "V1", everything below describes V2 as live on 30 Sep 2026.

"Live snapshot" means my own on-chain read on **2026-09-30 10:24:30 UTC** (Solana slot about 451.94M). I ran Hylo's open-source Rust SDK (hylo-quotes `RpcStateProvider` and hylo-stats `StatsClient`, v2.6.1, commit 1b1f90d of 14 Sep 2026) against the public mainnet RPC. Accounts read: the Hylo config PDA [9cd2sAfb…GcDND](https://solscan.io/account/9cd2sAfbBvKs4SX9YKo4dcjwP3TgTVQ8dT5koshGcDND), the mints for [hyUSD](https://solscan.io/token/5YMkXAYccHSGnHn9nob9xEvv6Pvka9DZWH7nTbotTu9E), [xSOL](https://solscan.io/token/4sWNB8zGWHkh6UnmwiEtzNxL4XrN7uK9tosbESbJFfVs) and [eHYUSD](https://solscan.io/token/HnnGv3HrSqjRpgdFmx7vQGjntNEoex1SU4e9Lxcxuihz), the LST vaults and the Pyth SOL/USD feed. SDK source: [github.com/hylo-so/sdk](https://github.com/hylo-so/sdk).

---

## Q1. How collateral value is split between hyUSD and xSOL: NAV, CR and leverage formulas, what backs the pool, who gets the staking yield

### Takeaway
One pool of SOL liquid staking tokens (LSTs: jitoSOL and hyloSOL) is split into two claims. The first is a $1-per-unit claim (vUSD_SOL, which backs hyUSD). The second, xSOL, takes everything left over, so it absorbs all SOL price moves. The formulas:
- xSOL NAV = (SOL-pool TVL − vUSD_SOL supply × $1) / xSOL supply
- CR = TVL / vUSD_SOL
- Effective leverage L = TVL / xSOL market cap = CR/(CR−1) = 1/(1−1/CR)

All staking yield goes to eHYUSD depositors, minus a 5% treasury cut. Plain hyUSD and xSOL earn nothing from it. xSOL holders therefore give up the LST yield an LST holder would earn. Above 165% CR they also pay extra, taken out of xSOL's own value.

### Cited Findings
- **Core invariant (per pool):** "ASSET TVL = vUSD Supply · $1 + xASSET Supply · xASSET Price". vUSD is an internal accounting unit that cannot be traded; users only hold hyUSD, xASSETs and collateral — [Hylo docs, Core Mechanism](https://docs.hylo.so/protocol-overview/core-mechanism)
- **xSOL NAV formula:** "xASSET NAV_USD = (ASSET TVL (USD) − vUSD Supply) / xASSET Supply"; if xASSET supply is 0, NAV defaults to $1 — [Hylo Equations](https://docs.hylo.so/technical-addendum/hylo-equations). The SDK computes it the same way: `free_collateral = n_collateral·p_collateral − n_stable·p_stable; nav = free_collateral / n_lever` — [hylo-core exchange_math.rs](https://github.com/hylo-so/sdk/blob/main/hylo-core/src/exchange_math.rs)
- **Mint and redeem NAV differ by the Pyth confidence band:** minting xSOL uses the *upper* Pyth price (price + confidence) and redeeming uses the *lower* one. This works like a built-in bid/ask spread. Live snapshot: mint NAV $0.092399 vs redeem NAV $0.092323 (≈0.08% apart) with Pyth SOL/USD at $119.5836 ± $0.0202 — [exchange_math.rs `next_levercoin_mint_nav` / `next_levercoin_redeem_nav`](https://github.com/hylo-so/sdk/blob/main/hylo-core/src/exchange_math.rs); [pyth/oracle.rs `PriceRange::from_conf`](https://github.com/hylo-so/sdk/blob/main/hylo-core/src/pyth/oracle.rs); live on-chain read (see scope note)
- **CR definition:** "CR = Total Collateral × Collateral Price / vUSD Supply" (per pool); system CR = Σ pool TVLs / Σ vASSET supplies — [Hylo Equations](https://docs.hylo.so/technical-addendum/hylo-equations); [Risk Management](https://docs.hylo.so/protocol-overview/risk-management)
- **Leverage definition:** "xASSET Effective Leverage = ASSET TVL / xASSET Market Cap"; it "approaches infinity as CR approaches 100%, and approaches 1 as CR increases" — [Hylo Equations](https://docs.hylo.so/technical-addendum/hylo-equations). Leverage rises when vUSD is minted or xASSET is redeemed, and falls when vUSD is burned or xASSET is minted — [docs, xASSETs](https://docs.hylo.so/protocol-overview/xassets)
- **Target:** each pair targets a CR of **150%**, i.e. **3x** structural leverage in normal conditions — [docs, xASSETs](https://docs.hylo.so/protocol-overview/xassets). The 150% target comes from SOL's 1-day 99.9% VaR of −32.95% (data from 10 Apr 2020 to 2026) — [Value-at-Risk Analysis](https://docs.hylo.so/technical-addendum/value-at-risk-analysis)
- **Worked example from the docs:** 1 SOL at $100 backs 50 vUSD plus 50 xSOL at $1. If SOL goes to $200, xSOL is worth $3. If SOL goes to $75, xSOL is worth $0.50 — [docs, xASSETs](https://docs.hylo.so/protocol-overview/xassets)
- **Backing assets (SOL pool):** LSTs in Hylo's registry, "currently consisting of jitoSOL and hyloSOL". LSTs are valued at "true" stake-pool value using Sanctum's SOL value calculator (SOL in stake pool / LST supply), then converted to USD with Pyth SOL/USD — [Multi-Asset Architecture](https://docs.hylo.so/protocol-overview/multi-asset-architecture); [Hylo Equations](https://docs.hylo.so/technical-addendum/hylo-equations)
- **Live SOL-pool composition (2026-09-30 10:24 UTC):** 211,474.80 jitoSOL and 22,339.03 hyloSOL, worth 299,543.17 SOL in total. TVL $35,814,403; vUSD_SOL 20,977,193.70; xSOL supply 160,708,971.61; CR **170.73%** (BuyZone1); xSOL market cap ≈ $14.84M; **effective leverage ≈ 2.41x** — live on-chain read (scope note). DefiLlama's 30 Sep 2026 breakdown matches: JITOSOL 210,473 ($32.32M) and HYLOSOL 22,314 ($2.85M) in the protocol — [DefiLlama API, Hylo](https://api.llama.fi/protocol/hylo)
- **hyUSD = sum of all pools' vUSD (V2):** "hyUSD Supply = Σ(vUSD_i Supply · vUSD_i NAV)". Live check: vUSD_SOL 20,977,194 + vUSD_BTC 2,129,110 + vUSD_HYPE 1,585,701 + vUSD_USDC ≈0.002 ≈ 24,692,004, against a hyUSD mint supply of 24,691,985.08 — [Multi-Asset Architecture](https://docs.hylo.so/protocol-overview/multi-asset-architecture); live on-chain read
- **Who receives LST yield (V2):** "This yield flows to hyUSD stakers and protocol revenue, making leverage effectively free for xSOL holders while the pool's CR is in the Neutral zone" — [Multi-Asset Architecture](https://docs.hylo.so/protocol-overview/multi-asset-architecture). Each epoch the yield is harvested by a permissionless crank, turned into newly minted hyUSD and added to the Earn Pool — [Earn Pool](https://docs.hylo.so/protocol-overview/earn-pool)
- **Treasury cut of the harvest:** on-chain `yield_harvest_config.fee` = 500 bps (**5%**); the code caps it at 10% (1000 bps) — live read of the [Hylo config account](https://solscan.io/account/9cd2sAfbBvKs4SX9YKo4dcjwP3TgTVQ8dT5koshGcDND); [hylo-core yields.rs](https://github.com/hylo-so/sdk/blob/main/hylo-core/src/yields.rs). Docs: "The protocol bounds r_c at about 30% annualized, and the treasury fee taken from the harvest at 10%" — [Hylo Equations](https://docs.hylo.so/technical-addendum/hylo-equations)
- **xSOL forgoes the yield:** "Leverage is effectively free from ongoing costs besides the forfeited yield" — [docs, xASSETs](https://docs.hylo.so/protocol-overview/xassets)
- **Extra cost above 165% CR (xSOL "borrow rate"):** the LST harvest is scaled by m(CR). m = 0 below 135%; 1 from 135–165%; linear from 1 up to m_c for 165–175%; m_c at 175% and above. m_c is configurable in [1, 5] and "currently 2". "The excess over 1× comes out of xSOL equity": xSOL rate on exposure = (m(CR) − 1) × LST yield — [Hylo Equations](https://docs.hylo.so/technical-addendum/hylo-equations). On-chain `yield_harvest_config.ceil_mult` = 2.0 (live read of the [Hylo config account](https://solscan.io/account/9cd2sAfbBvKs4SX9YKo4dcjwP3TgTVQ8dT5koshGcDND))
- **Reference staking yield:** hyloSOL APY 5.85% (30-day mean 5.62%) on DefiLlama, 30 Sep 2026 — [DefiLlama yields API](https://yields.llama.fi/pools) (pool 1b94ffcc-…, project "hylo-lsts"). Docs quote hyloSOL at "5–7%" — [Liquid Staking Tokens](https://docs.hylo.so/product-guide/liquid-staking-tokens). The CEO's late-2025 estimate: if all hyUSD were staked, holders "would only earn roughly the 6-7% base return" — [Solana Compass, Lightspeed podcast notes](https://solanacompass.com/learn/Lightspeed/how-hylo-is-accelerating-solana-defi-in-2026-plish)
- **V1 was the same idea with a single pool:** "Hylo V1 supported only SOL with xSOL and hyUSD as synthetic tokens built on top of the protocol's LST pool" — [Multi-Asset Architecture](https://docs.hylo.so/protocol-overview/multi-asset-architecture)
- **Design lineage (f(x) Protocol on Ethereum):** f(x) v1 split ETH collateral "into a lower-volatility component (β < 1) called fractional ETH (fETH) and a higher-volatility (β > 1) one called leveraged ETH (xETH)". xETH is "essentially a long perpetual future contract with zero funding costs and variable leverage". fETH had β = 0.1 — [Aladdin/f(x) docs](https://docs.aladdin.club/f-x-protocol). Hylo uses the same split-the-collateral design, but its stable leg is fixed at $1 (β = 0) and the xASSET takes 100% of the price move.

### Inferences
- **What a retail xSOL holder actually owns:** a pro-rata claim on "SOL collateral minus a fixed dollar debt". At the live snapshot, each xSOL is ≈ 0.0018639 SOL of collateral (299,543.17 / 160.709M) minus ≈ $0.13053 of zero-interest dollar debt (20.977M / 160.709M). NAV = 0.0018639 × $119.58 − $0.13053 ≈ $0.0923.
- **Cost of the leverage compared with other holdings:**
  - Versus plain (unstaked) SOL, xSOL has no explicit carry while CR is 135–165%.
  - Versus an LST, the holder gives up about 5.6–6% a year on their own capital. Economically, they also give up the yield on the "borrowed" part, and that is what pays eHYUSD.
  - At the live CR of 170.7%, m ≈ 1.573. The explicit extra cost is (m−1) × y × L ≈ 0.573 × 5.85% × 2.41 ≈ **8.1% per year of xSOL value** (7.8–8.3% for y = 5.6–6%), as long as CR stays there.
  - At CR ≥ 175% (m = 2, L ≈ 2.33) it would be ≈ 13–14% per year.
  - These are derived from the docs' formulas plus the live snapshot. They are not a published Hylo number.
- The Pyth confidence band acts like a tiny hidden spread. In calm markets it is about 0.02% of the SOL price, so about 0.08% on xSOL (conf × L).

### Gaps
- I could not confirm the exact m(CR) used in the last harvest (epoch 1046). The harvest took place at an unknown intra-epoch CR.
- jitoSOL's own APY on 30 Sep 2026 was not separately verified. I used hyloSOL's 5.85% as a proxy.

---

## Q2. How effective leverage drifts as SOL moves; whether xSOL is linear in SOL with static supplies; the SOL drawdown that wipes xSOL out

### Takeaway
If token supplies stay fixed, xSOL NAV is a straight-line (affine) function of the SOL price. It behaves like a fixed-size long of N/X SOL, financed with zero-interest dollar debt. That means no volatility decay, and the return from any starting point is exactly L₀ × the SOL % move until NAV hits zero. Instantaneous leverage L = CR/(CR−1) rises as SOL falls and falls as SOL rises. xSOL is wiped out when SOL falls 1 − 1/CR: −33.3% from CR 150%, and −41.4% from the live CR of 170.7% (SOL ≈ $70.0). Path dependence, and so decay, only comes from supply changes:
- hyUSD mints and redeems by other users
- V1 stability-pool conversions
- V2 sell/buy-zone rebalancing
- fees and the harvest multiplier

### Cited Findings
- The docs describe NAV as the "variable reserve, the excess value not backing the virtual stablecoin", and give the $100 → $200 → $3/xSOL example — [docs, xASSETs](https://docs.hylo.so/protocol-overview/xassets)
- The docs *also* warn: "Volatility decay causes leveraged tokens to lose value over time in sideways markets. When holding an xASSET through multiple rebalancing cycles, the break-even price of a user's position may increase". Their example: SOL −20% then back to $100, while xSOL at 2x goes $100 → $60 → $90 — [docs, xASSETs](https://docs.hylo.so/protocol-overview/xassets)
- The late-2025 CEO podcast contrasted xSOL with daily-rebalanced leveraged ETFs: "xSOL's leverage varies with market conditions, avoiding this constant rebalancing cost". It said leverage varies "between approximately 2x to 4x, though it rarely exceeds 3.2x in practice" (V1) — [Solana Compass, Lightspeed notes](https://solanacompass.com/learn/Lightspeed/how-hylo-is-accelerating-solana-defi-in-2026-plish)
- In V2 the protocol *does* rebalance. Sell zone (CR < 135%): it sells collateral for USDC, "de-leveraging the xASSET and raising the pool's CR toward 135%". Buy zone (CR > 165%): it buys collateral with USDC, "re-leveraging the xASSET" toward 165% — [Collateral Rebalancing](https://docs.hylo.so/protocol-overview/collateral-rebalancing)
- The DefiLlama Research note (30 Jul 2026) says the loss in V1 ended up as **dilution**. "Between October 2025 and June 2026, the supply of xSOL grew from a modest 8.4 million to 235 million, a 28-fold increase", partly from users minting fresh xSOL and partly from the stability pool "burn[ing] a reserve of hyUSD tokens and issu[ing] new xSOL in its place" — [DefiLlama Research newsletter](https://research-newsletters.defillama.com/p/leverage-without-liquidation)
- Live snapshot, 2026-09-30 10:24 UTC: CR 170.73%, L 2.414x, SOL $119.58 — live on-chain read (scope note)

### Inferences (computed; static supplies unless noted)
- **Algebra:** NAV(P) = (N·P − V)/X, where N = SOL in the pool, V = vUSD, X = xSOL supply. So d(NAV)/dP = N/X, a constant.
  - Return from time 0: NAV(P)/NAV(P₀) − 1 = L₀ × (P/P₀ − 1), where L₀ = CR₀/(CR₀−1).
  - Instantaneous leverage is L(P) = N·P/(N·P − V): it rises when P falls and falls when P rises.
- **Leverage drift from CR 150% (L = 3x) with fixed supplies:**

| SOL move | CR | Instantaneous leverage | xSOL move |
|---|---|---|---|
| −30% | 105% | 21x | −90% |
| −20% | 120% | 6x | −60% |
| −10% | 135% | 3.86x | −30% |
| +20% | 180% | 2.25x | +60% |
| +50% | 225% | 1.8x | +150% |
| +100% | 300% | 1.5x | +300% |

  Note that this "3x" never compounds the way daily-reset 3x ETFs do. On the way up, xSOL's % gain is *less* than a daily-reset 3x product would give in a steady rally. On the way down, its % loss is *larger*: it reaches zero at −33%, while a daily-reset 3x only asymptotically approaches zero.
- **Wipeout thresholds** (SOL drop that takes NAV to 0, i.e. 1 − 1/CR):

| Starting CR | Leverage | SOL drop to wipe out xSOL |
|---|---|---|
| 120% | 6x | 16.7% |
| 130% | 4.33x | 23.1% |
| 135% | 3.86x | 25.9% |
| 150% | 3x | 33.3% |
| 165% | 2.54x | 39.4% |
| **170.7% (live)** | **2.41x** | **41.4% (SOL ≈ $70.0)** |
| 175% | 2.33x | 42.9% |
| 200% | 2x | 50% |

- **Live SOL prices at the V2 zone boundaries** (static supplies from the 30 Sep 2026 snapshot; P = CR × V / N with V = 20.977M, N = 299,543 SOL):
  - CR 175% (borrow multiplier maxes at 2x): ≈ $122.6 (+2.5%)
  - CR 165%: ≈ $115.6 (−3.4%)
  - CR 135% (sell-zone rebalancing starts, xSOL redeem fee jumps to 4%): ≈ $94.5 (−20.9%)
  - CR 120% (sell zone 2, redeem fee 8%): ≈ $84.0 (−29.7%)
  - CR 100% (xSOL NAV = 0, mint/redeem blocked): ≈ $70.0 (−41.4%)
  - In practice, other users' hyUSD mint/redeem flows and rebalancing will move these levels.
- **How "linear" becomes path-dependent:**
  1. Another user's hyUSD mint at NAV adds SOL and vUSD in equal dollar amounts. xSOL NAV is unchanged, but each xSOL now carries more SOL exposure (more leverage). A hyUSD redemption does the opposite. Dynamic fees deliberately route hyUSD mints into high-CR pools and redemptions out of low-CR pools, which *re-leverages* after rallies and *de-leverages* after drops.
  2. V2 sell-zone rebalancing sells SOL after drops (de-leveraging and locking in losses); buy-zone rebalancing buys after rallies. That is the classic leveraged-ETF rebalancing pattern that causes volatility decay.
  3. V1 stability-pool conversions minted new xSOL at depressed NAV (see Q3). No value moved at that instant, but leverage was cut at the bottom, so a later SOL recovery lifted xSOL far less.
- **Break-even arithmetic at live supplies:** xSOL = $1 needs SOL ≈ (X + V)/N = (160.709M + 20.977M)/299,543 ≈ **$607**. xSOL's all-time high of $2.08 would need SOL ≈ $1,186. This matches DefiLlama Research's June/July 2026 estimate of "$630–$719" for xSOL to regain $1.

### Gaps
- There is no official Hylo statement on how large rebalancing-driven decay is in V2. The V2 rebalancing history (volumes, dates) is not published in the docs.

---

## Q3. Low-CR behavior: stability thresholds, dynamic fees, mint/redeem restrictions, the stability pool, liquidation and funding

### Takeaway
- **V1** (to about mid-June 2026):
  - Below 150% CR, "Stability Mode 1" nudged fees (cheaper xSOL mints and hyUSD redemptions).
  - Below 130%, "Stability Mode 2" switched on the Stability Pool. It burned sHYUSD's hyUSD and minted xSOL to push CR back above 130%. That xSOL was later sold back into hyUSD once CR recovered above 150%.
- **V2** (live on 30 Sep 2026) replaces the modes with six zones. Neutral is 135–165% (target 150%). Below 135% the protocol:
  - sells collateral for USDC, at up to a 0.2% discount (subsidy) for SOL
  - raises the xSOL redeem fee (4% in 120–135%, 8% in 100–120%) and lowers the xSOL mint fee
  - blocks hyUSD mints from that pool below the 150% mint threshold
  - below 100%, sets xSOL NAV to 0, halts minting and redemption, and burns Earn Pool hyUSD as first-loss capital
- xSOL is never liquidated and pays no funding. The costs show up instead as NAV loss, dilution/deleveraging, higher exit fees, and (above 165% CR) a yield-multiplier "borrow rate".

### Cited Findings
**V1 (historical)**
- The CEO described three levels on the Lightspeed podcast (notes on Solana Compass):
  - Normal threshold is 150% CR.
  - Stability Mode One below 150%: "it becomes cheaper to mint xSOL and cheaper to redeem high USD".
  - 130% "triggers Stability Mode Two and activates the stability pool … some of their high USD may be converted to xSOL to restore the collateral ratio above 130%". "Once the collateral ratio recovers above 150%, the xSOL converted from stability pool participants gets returned to high USD."
  - Source: [Solana Compass, Lightspeed notes](https://solanacompass.com/learn/Lightspeed/how-hylo-is-accelerating-solana-defi-in-2026-plish). The page metadata says 16 Dec 2024, but the content covers the 10 Oct 2025 crash and ~$100M TVL, so it was recorded around late 2025. The notes are AI-generated.
- Another write-up from 29 Jul 2025 gives a "150%" target for hyUSD minting and a "130%" circuit breaker for sHYUSD conversion — [lavneet.wtf blog](https://lavneet.wtf/blog/hylo-a-monetary-system-built-on-yield/)
- On-chain remnants support these thresholds. The live Hylo config account still has a deprecated `_unused_1` field = **1.30** (bits 130, exp −2) and `stablecoin_mint_threshold` = **1.50**. It also has deprecated V1 hyUSD fee fields: "normal" mint 0.10% / redeem 0.30%, and "mode_1" mint 0.50% / redeem 0.30% — live read of the [Hylo config account](https://solscan.io/account/9cd2sAfbBvKs4SX9YKo4dcjwP3TgTVQ8dT5koshGcDND), decoded with [hylo_exchange IDL](https://github.com/hylo-so/sdk/blob/main/hylo-idl/idls/hylo_exchange.json). The SDK marks the `StablecoinFees` struct "Deprecated — retained only for Hylo account deserialization" — [fees/controller.rs](https://github.com/hylo-so/sdk/blob/main/hylo-core/src/fees/controller.rs)
- V1 xSOL fee: a "flat 1% fee" on xSOL entries and exits — [Solana Compass, Lightspeed notes](https://solanacompass.com/learn/Lightspeed/how-hylo-is-accelerating-solana-defi-in-2026-plish)
- How the Stability Pool worked, per Pine Analytics: "Hylo starts actively burning the hyUSD that backs sHYUSD and replacing that backing with xSOL … as the protocol's numbers normalize, the stability pool … slowly sells off its xSOL to return to full stablecoin backing". Until then "sHYUSD is no longer a stable asset and fluctuates based on the price of SOL" — [Pine Analytics Q1 2026 (15 Apr 2026)](https://pineanalytics.substack.com/p/hylo-quarterly-operations-overview)
- DefiLlama Research: the stability pool "automatically burned a reserve of hyUSD tokens and issued new xSOL in its place … they came at a cost to people who already held xSOL. The dramatic increase in token supply … meant there were far more claimants" — [DefiLlama Research newsletter, 30 Jul 2026](https://research-newsletters.defillama.com/p/leverage-without-liquidation)
- V1 audit scope: OtterSec audited the "stability-pool" program as "a liquidity pool where users deposit hyUSD to earn yield while supporting the rebalancing of the exchange's collateral ratio" — [OtterSec report, 5 May 2025](https://hylo-audits.s3.us-east-2.amazonaws.com/OtterSec-Exchange-Stability-Pool-20250513.pdf)

**V2 (current)**
- **Zones** (lower bound inclusive; "These zones replace the former 'stability mode' thresholds"):

| CR range | Zone |
|---|---|
| < 100% | Destabilized: "xASSET NAV → 0; rebalancing, P&L settlement, and minting halt" |
| 100–120% | Sell Zone 2 |
| 120–135% | Sell Zone 1 |
| 135–165% | Neutral |
| 165–175% | Buy Zone 1 |
| ≥ 175% | Buy Zone 2 |

  Sources: [Hylo Equations](https://docs.hylo.so/technical-addendum/hylo-equations) and the same boundaries hard-coded in [rebalance/mode.rs](https://github.com/hylo-so/sdk/blob/main/hylo-core/src/rebalance/mode.rs)
- **xSOL fee table, live on-chain (bps, mint/redeem):**
  - Neutral and both buy zones: **100 / 100**
  - Sell Zone 1: **50 / 400**
  - Sell Zone 2: **0 / 800**
  - Destabilized: mint and redeem blocked (the SDK returns `NoValidLevercoinMintFee` / `NoValidLevercoinRedeemFee`)
  - The code caps any levercoin fee at 1000 bps.
  - Sources: live on-chain read; [fees/controller.rs](https://github.com/hylo-so/sdk/blob/main/hylo-core/src/fees/controller.rs); the docs list the same table as an "example" — [Additional Risk Management](https://docs.hylo.so/technical-addendum/additional-risk-management)
- The docs call this an "anti-destabilization backstop, not a routine cost … In normal conditions, autonomous rebalancing keeps CR inside the Neutral band, so these elevated fees almost never apply" — [Additional Risk Management](https://docs.hylo.so/technical-addendum/additional-risk-management)
- **Minting hyUSD from a pool is blocked below the 150% mint threshold.** The threshold is constrained on-chain to 150–170% and is 1.50 live. Hyusd redemptions from a pool are only quoted while that pool's projected CR stays ≤ 150% — [Dynamic Collateral Routing](https://docs.hylo.so/protocol-overview/dynamic-collateral-routing); [Hylo Equations](https://docs.hylo.so/technical-addendum/hylo-equations); live on-chain read
- **Rebalance pricing (live SOL-pool config):**
  - Sell curve: floor 0.2% / ceiling 0.1%. The price runs linearly from spot × (1 − 0.2%) at CR 120% (a subsidy) to spot × (1 + 0.1%) at CR 135% (a profit), and is clamped below 120%.
  - Buy curve: floor 0.1% / ceiling 0.1%. It runs from spot × (1 − 0.1%) at 165% to spot × (1 + 0.1%) at 175%.
  - Code caps: sell ≤ 5%/5%, buy ≤ 5%/2%.
  - Sources: live on-chain read; [rebalance/pricing.rs](https://github.com/hylo-so/sdk/blob/main/hylo-core/src/rebalance/pricing.rs)
- **Rebalance P&L goes to the Earn Pool.** Profitable rebalances mint hyUSD into it; subsidized ones burn hyUSD from it — [Collateral Rebalancing](https://docs.hylo.so/protocol-overview/collateral-rebalancing)
- **Destabilized (< 100%):** "The protocol burns Earn Pool hyUSD to retire the unbacked virtual-stablecoin overhang … The burn is capped at the Earn Pool's balance, and the amount retired is recorded as debt on a pool drawdown ledger". While a drawdown is outstanding, stablecoin minting is frozen for that pool, harvesting pauses, and future yield repays the drawdown first — [Additional Risk Management](https://docs.hylo.so/technical-addendum/additional-risk-management). Live `pool_drawdown` ledger on 30 Sep 2026 = 0 — live on-chain read
- **If Earn Pool hyUSD runs out:** the SDK has a "depeg" path where hyUSD NAV = total collateral × price / supply, i.e. hyUSD would trade below $1 — [exchange_math.rs `depeg_stablecoin_nav`](https://github.com/hylo-so/sdk/blob/main/hylo-core/src/exchange_math.rs)
- **Pine on V2:** "sHYUSD no longer takes on xSOL exposure … replaced with a market-driven system where the exchange automatically creates MEV opportunities for searchers to buy away fading collateral for USDC, and vice versa" — [Pine Analytics Q1 2026](https://pineanalytics.substack.com/p/hylo-quarterly-operations-overview)
- **No liquidation, no funding:** "Nobody holding xSOL was ever forced out of a position … nobody paid an ongoing fee to hold leveraged SOL exposure" (about V1). Listed trade-offs: "dynamic fees to mint and redeem hyUSD, volatility decay, and variable leverage" — [DefiLlama Research newsletter](https://research-newsletters.defillama.com/p/leverage-without-liquidation)
- **USDC pool is empty (live):** vault holds 0.001832 USDC. Mint fee 0%, redeem fee 0.20%. USDC routes need Pyth USDC within ≤ $0.001 of par — live on-chain read; [Dynamic Collateral Routing](https://docs.hylo.so/protocol-overview/dynamic-collateral-routing)

### Inferences
- **V1 stability pool, effect on xSOL holders:** conversion happened at the exchange's NAV, so there was no instant value transfer. But it cut leverage right at the low. For example, CR 129% means L ≈ 4.4x; pushing CR back to ≥130% lowered L. It also multiplied the xSOL supply, so later SOL recoveries raised xSOL NAV much less. On-chain supply confirms this: xSOL supply went from about 98M (1 Jun 2026) to about 224–237M (7–8 Jun 2026) while hyUSD supply fell from about 14.9M to about 10.8M (CoinGecko market caps/prices; see Q6). That is "deleveraging at the bottom" and is the main hidden cost V1 xSOL holders paid in 2026.
- **V1 stability pool, effect on sHYUSD holders:** they became automatic dip-buyers of leveraged SOL. It paid off in Q1 2026 (52.4% APY) because xSOL bounced from its conversion levels. It could have lost money had SOL kept falling.
- **V2 changes who absorbs losses:**
  - Arbitrageurs are paid a small spread (≤0.2% for SOL) to take collateral for USDC when CR is below 135%.
  - xSOL holders get de-leveraged (sell after drops) instead of diluted.
  - eHYUSD absorbs rebalancing subsidies and, if CR goes below 100%, is burned.
  - The sell route needs arbitrageurs willing to bring USDC at about the oracle price. In a fast gap-down, a pool can skip past 135% → 100% before enough flow arrives.
- **Right now (30 Sep 2026, CR 170.7%, BuyZone1):**
  - The buy route (USDC → SOL, re-leveraging) is formally open, but the USDC pool holds only $0.0018, so the protocol has no USDC to re-leverage with. Leverage stays at 2.41x instead of the 3x target, and xSOL pays the m ≈ 1.57 harvest multiplier.
  - Re-leveraging now depends on new hyUSD mints from the SOL pool. Up to about 8.70M hyUSD could be minted before CR falls to 150% (live `max_mintable_stablecoin`).
- **A retail holder faces no margin call.** The practical "liquidation equivalent" is NAV → 0 below CR 100%, plus fees in stress: redeem fee 4–8% in the sell zones, and redemptions blocked at < 100%.

### Gaps
- The complete V1 xSOL fee schedule by stability mode (Mode 1/Mode 2 numbers) is not published. Only the "flat 1%" normal fee and the deprecated hyUSD fee fields were verified.
- The exact V1 conversion instruction (price used, and any bonus/discount) could not be checked. V1 source code is not public; audits reference a private repo, github.com/hylo-so/protocol. I infer the conversion was at NAV from the SDK's `convert_stable_to_lever_lst` path and the secondary descriptions.

---

## Q4. sHYUSD / eHYUSD: current and historical yield, where it comes from, risks, and whether it is a sensible place to park stablecoins before DCA entries

### Takeaway
eHYUSD (formerly sHYUSD, same mint) earns the protocol's harvested yield:
- LST staking yield across the whole SOL pool, times m(CR)
- xBTC and xHYPE borrow rates
- net profit or loss from rebalancing
- minus a 5% treasury cut

The yield is concentrated because only the Earn Pool's share of hyUSD earns it. The live projected APY on 30 Sep 2026 is about **14.8–14.9%**. Realized returns:
- about +34% over the last 12 months
- Q1 2026 about 52–56% annualized, and Q2 2026 about 53% annualized, both boosted by V1 xSOL exposure
- Q3 2026 about 20% annualized, and September 2026 about 14%

In V2, eHYUSD no longer holds xSOL. It is still first-loss capital: its hyUSD is burned if a pool falls below 100% CR, it pays rebalancing subsidies, and withdrawals are rate-limited (1M hyUSD per epoch) with a 0.10% fee. It is a reasonable but not risk-free place to park stablecoins. Its main risk is correlated with a sharp SOL crash — exactly when a DCA buyer would want to deploy.

### Cited Findings
- **Rename:** "eHYUSD is the same token as sHYUSD: same mint address, only the ticker has changed for Hylo V2. No migration or action of any kind is needed from holders" — [Earn Pool](https://docs.hylo.so/protocol-overview/earn-pool)
- **Yield sources:** SOL pool native staking rewards; BTC and HYPE pool borrow rates. Yield is harvested each epoch by a permissionless crank and turned into hyUSD, which raises eHYUSD NAV. "US Treasury yield on USDC will be added in the coming weeks, adding a base yield of 4% APY" (forward-looking, not verified as live) — [Earn Pool](https://docs.hylo.so/protocol-overview/earn-pool)
- **APY formula in the docs:** (1 + Epoch Rate)^182.5 − 1 — [Earn Pool](https://docs.hylo.so/protocol-overview/earn-pool). The SDK instead *measures* epochs per year from chain timing: 272.94 on 30 Sep 2026. Solana slots were about 0.271 s over 16–30 Sep 2026 (slot 447,625,876 at 2026-09-16 21:34:38 UTC to slot 451,937,430 at about 2026-09-30 10:27 UTC, from RPC `getBlockTime`), so "182.5" is outdated — [hylo-stats client.rs `measure_epochs_per_year`](https://github.com/hylo-so/sdk/blob/main/hylo-stats/src/client.rs); live RPC read
- **Live Earn Pool stats (2026-09-30 10:24 UTC; SDK `StatsClient::earn_pool_stats`):**
  - eHYUSD NAV **1.494787 hyUSD**; 21,599,128.60 hyUSD in the pool; eHYUSD supply 14,449,639.20
  - Current epoch 1046
  - Last-epoch harvest: LST stream 9,634.35 hyUSD, cbBTC borrow-rate stream 1,388.95 hyUSD
  - Last-epoch rate 0.0510%; **"naive" APY 14.94%; projected APY 14.77%**
  - Outstanding drawdown 0
  - Note: the SDK's stats client only includes the cbBTC exo pair, not HYPE, so the HYPE borrow-rate stream is missing and APY may be slightly understated.
  - Sources: live on-chain read; [hylo-stats types.rs / client.rs](https://github.com/hylo-so/sdk/blob/main/hylo-stats/src/client.rs)
- **Share of hyUSD in the Earn Pool:** 21.60M of 24.69M (≈87.5%) on 30 Sep 2026 — live on-chain read
- **Earn Pool limits (live PoolConfig):** withdrawal fee **0.10%** (applied to the hyUSD part); withdrawal limiter **1,000,000 hyUSD per epoch** across all users (5,071.57 used so far in epoch 1046); deposit cap **25,000,000 hyUSD**; paused = false. The pool's legacy xSOL account ([4GPXVX…rhk1](https://solscan.io/account/4GPXVXuzk8ABAUkoXeBJg8r9kccEXQjoi5vqSxE9rhk1)) holds **0 xSOL** — live on-chain read. Docs on withdrawals: "Pro-rata share of both hyUSD and any xASSET in the pool, with a configurable withdrawal fee applied to the hyUSD portion" — [Hylo Equations](https://docs.hylo.so/technical-addendum/hylo-equations)
- **Realized eHYUSD/hyUSD path** (DefiLlama coins API, market prices near 12:00 UTC; eHYUSD/hyUSD ratio):

| Date | Ratio |
|---|---|
| 1 Oct 2025 | 1.1159 |
| 1 Nov 2025 | 1.1298 |
| 1 Dec 2025 | 1.1414 |
| 1 Jan 2026 | 1.1527 |
| 1 Feb 2026 | 1.1653 |
| 1 Mar 2026 | 1.2279 |
| 1 Apr 2026 | 1.2866 |
| 1 May 2026 | 1.3258 |
| 1 Jun 2026 | 1.3579 |
| 1 Jul 2026 | 1.4296 |
| 1 Sep 2026 | 1.4792 |
| 29 Sep 2026 | 1.4940 |

  Sources: [DefiLlama coins API](https://coins.llama.fi/prices/historical/1790683200/solana:HnnGv3HrSqjRpgdFmx7vQGjntNEoex1SU4e9Lxcxuihz) (per-date queries). The last point matches the on-chain NAV of 1.4948.
- **Pine, Q1 2026:** "sHYUSD delivered its strongest quarter on record at 52.4% APY as xSOL recovered from lows". Stability pool activations "deployed $7.9M in hyUSD". About 10% of sHYUSD backing was still xSOL at the time of the report, pending reconversion — [Pine Analytics Q1 2026](https://pineanalytics.substack.com/p/hylo-quarterly-operations-overview)
- **KuCoin summary of the V2 launch (17 Jun 2026):** the stability pool "deployed ~$8M into xSOL over 3 months" in 59 transactions and "generated $763K in profits" for sHYUSD holders — [KuCoin news](https://www.kucoin.com/news/flash/hylo-launches-v2-expands-on-chain-leverage-to-stocks-and-multi-asset-collateral)
- **Earlier quoted yields:**
  - "~18% APY" in a 29 Jul 2025 write-up — [lavneet.wtf](https://lavneet.wtf/blog/hylo-a-monetary-system-built-on-yield/)
  - "trailing yields around 15%" in the late-2025 podcast notes — [Solana Compass](https://solanacompass.com/learn/Lightspeed/how-hylo-is-accelerating-solana-defi-in-2026-plish)
  - "19–22% APY" in undated secondary reviews, surfaced by search summaries of Medium reviews — low reliability
- **Why the yield is amplified:** yield on the whole pool's collateral is concentrated on staked hyUSD. The docs' example is 11.8% when 70% of hyUSD is staked — [Earn Pool](https://docs.hylo.so/protocol-overview/earn-pool)
- **Earn Pool is first-loss capital:** "Earn Pool depositors [are] the protocol's first-loss capital: they earn the system's aggregate yield in calm conditions and have their hyUSD burned to recollateralize a pool when one falls below 100% backing" — [Additional Risk Management](https://docs.hylo.so/technical-addendum/additional-risk-management)
- **V2 audit, Accretion (8 Jul 2026), relevant to eHYUSD:**
  - ACC-M13, "LP Accounting Ignores Drawdown Debt and Misprices sHYUSD" (Medium, **ACKNOWLEDGED**, not fixed): "New depositors may receive too many LP tokens, and users withdrawing during drawdown may lose their share of the future repayment"
  - ACC-L1, "Oracle Freeze Locks out Settlement While Allowing Users To Exit Earn Pool" (Low, FIXED). The auditor called this "an inherent issue with the earn pool: Users can exit the pool whenever losses are predictable … They can earn a risk premium while cutting off their tail risk almost entirely". Hylo's response mentioned a possible "per-epoch liquidity window allowing users to withdraw X% of a pool"
  - Source: [Accretion V2 report](https://hylo-audits.s3.us-east-2.amazonaws.com/Accretion-HyloV2-July2026.pdf)
- **Pine on why sHYUSD holders left in Q1 2026:** sHYUSD holders "wanted stable yield, but the volatility profile introduced by the stability pool activations made the asset less appropriate for looping strategies and less comfortable to hold" — [Pine Analytics Q1 2026](https://pineanalytics.substack.com/p/hylo-quarterly-operations-overview)

### Inferences
- **As a parking spot before DCA entries:**
  - At about 14.8% projected APY it pays well above USDC lending rates. Part of that comes from xSOL holders paying the m > 1 multiplier while CR > 165%. That component would shrink if CR falls back into Neutral, or rise if SOL rallies further.
  - Its tail risk is concentrated in the SOL-crash scenario: sell-zone subsidies and a < 100% CR burn. A DCA buyer waiting for dips holds a stablecoin that is weakest exactly when they want to spend it.
  - Exiting at scale is rate-limited (1M hyUSD per epoch for everyone) and costs 0.10%. After that, selling hyUSD → USDC relies on DEX depth, since the protocol's direct hyUSD redemption routes are currently closed (Q5).
  - For amounts of $1k–$4k, the costs are small (0.10% withdrawal fee + about 0.1% hyUSD → USDC; see Q5).
- The realized ~34% one-year return (Oct 2025 → Sep 2026) is **not** a clean stablecoin yield. About half came in Q1–Q2 2026 from V1's xSOL exposure paying off after conversions near the lows. Under V2 rules, eHYUSD would not have had that exposure.
- The 12-month path is based on market prices (DefiLlama), not NAV snapshots. It could differ slightly from true NAV at each date.

### Gaps
- There is no official eHYUSD APY history series; the DefiLlama yields API has no eHYUSD pool. The quarterly figures above are my own calculations from market prices.
- The current "pool allocation" (Earn Pool vs treasury) of borrow-rate harvests for BTC/HYPE was not read. The LST harvest fee is 5%.
- The USDC Treasury-yield addition ("4% APY … coming weeks") was not verified as live. The USDC pool is currently empty.

---

## Q5. Fees and execution: xSOL and hyUSD mint/redeem fees (and how they vary with CR), Hylo app vs DEXes, liquidity for $1k–$4k, NAV vs market price

### Takeaway
Protocol fees:
- **xSOL:** 1% to mint and 1% to redeem in the Neutral and buy zones. Redeem rises to 4% (CR 120–135%) and 8% (CR 100–120%); mint falls to 0.5% and then 0%. Both are blocked below 100%.
- **hyUSD from volatile pools:** mint fee runs from 0.20% at CR 150% down to 0.005% at ≥170%. Redeem fee runs from 0% at ≤130% up to 0.20% at 150%, and redemption is refused above 150%.
- **USDC pool:** 0% to mint, 0.20% to redeem.

In practice on 30 Sep 2026, buying $1k–$4k of xSOL through Jupiter's DEX routes cost about 0.17–0.26% in price impact, at about 0.6–0.7% *below* the protocol mint NAV. Minting in the app costs about 1% more. Selling routed through Hylo's own redeem cost about 1% below NAV. xSOL's market price is kept in a band of about NAV ± 1% by mint/redeem arbitrage.

### Cited Findings
- **hyUSD mint fee curve** (volatile pools; fee in N5 units; control points from the SDK): 150% → 0.200%, 151% → 0.180%, 152% → 0.150%, 155% → 0.110%, 160% → 0.060%, 165% → 0.030%, 170% → 0.005%. Minting is blocked below the domain — [hylo-core fees/curves.rs `MINT_FEE_INV`](https://github.com/hylo-so/sdk/blob/main/hylo-core/src/fees/curves.rs); [Dynamic Collateral Routing](https://docs.hylo.so/protocol-overview/dynamic-collateral-routing)
- **hyUSD redeem fee curve:** 130% → 0%, 135% → 0.091%, 140% → 0.140%, 145% → 0.174%, 150% → 0.200%. Redemption is rejected above the domain, i.e. when the projected CR > 150% — [fees/curves.rs `REDEEM_FEE_LN`](https://github.com/hylo-so/sdk/blob/main/hylo-core/src/fees/curves.rs). Fees are evaluated at the *projected* post-trade CR — [Hylo Equations](https://docs.hylo.so/technical-addendum/hylo-equations)
- **USDC pool:** mint 0%, redeem 0.2%; "the redeem fee matches the top of the volatile pools' redeem fee curve" — [Dynamic Collateral Routing](https://docs.hylo.so/protocol-overview/dynamic-collateral-routing); the live on-chain values are the same (live read)
- **xSOL fees:** live on-chain 100/100 bps in Neutral/Buy zones, 50/400 in Sell Zone 1, 0/800 in Sell Zone 2, blocked when Destabilized. Swapping hyUSD ↔ xSOL inside a pool uses the same table (hyUSD → xSOL uses the mint fee; xSOL → hyUSD uses the redeem fee and is disallowed in Sell Zone 2) — [fees/controller.rs](https://github.com/hylo-so/sdk/blob/main/hylo-core/src/fees/controller.rs); live on-chain read
- **Other live fees:** swapping between LSTs inside the pool 0.10% (`lst_swap_fee`); Earn Pool withdrawal 0.10% — live on-chain read
- **Routing:** "The DEX router (e.g. Titan, Jupiter) evaluates the proposed fee from each available pool and selects the cheapest path" — [Dynamic Collateral Routing](https://docs.hylo.so/protocol-overview/dynamic-collateral-routing). The SDK ships a Jupiter AMM integration crate (`hylo-jupiter`) — [SDK README](https://github.com/hylo-so/sdk)
- **Live Jupiter quotes** (2026-09-30 ≈10:27 UTC, 50 bps slippage):
  - **Buy $1,000 USDC → xSOL:** 10,896.0 xSOL, effective price **$0.091777**, price impact **0.17%**, routed via Kipseli + Orca Whirlpool
  - **Buy $4,000:** 43,547.9 xSOL, **$0.091853**, impact **0.26%**, routed via Manifest/BisonFi/Kipseli/Whirlpool
  - **Sell about $1,000 of xSOL:** 10,929.0 xSOL → 1,001.70 USDC (**$0.091655**), routed through **"Hylo Exchange"** redeem then LST → USDC
  - **Sell about $4,000:** 43,715.8 xSOL → 4,006.45 USDC (**$0.091648**), Hylo Exchange 100%
  - **hyUSD → USDC $4,000:** 3,995.41 USDC out (−0.11%), via Orca Whirlpool 97% / Meteora 3%
  - **USDC → hyUSD $4,000:** 4,003.74 hyUSD
  - Source: [Jupiter quote API](https://lite-api.jup.ag/swap/v1/quote) (queried 2026-09-30)
- **At the same time:** protocol NAV was $0.092399 (mint) / $0.092323 (redeem) (live on-chain read, 10:24 UTC). CoinGecko showed $0.091344 at 10:20 UTC — [CoinGecko xSOL](https://www.coingecko.com/en/coins/hylo-leveraged-sol)
- **DEX liquidity (GeckoTerminal, 30 Sep 2026):**
  - Main xSOL pool: Orca xSOL/SOL with **$504.9k** reserves and $1.55M 24h volume
  - Other xSOL pools: Meteora xSOL/SOL $76.6k; Meteora xSOL/USDC $42.4k; Orca xSOL/SOL (second pool) $30.5k; plus several small meme-pair pools
  - hyUSD: Orca hyUSD/USDC **$2.73M** reserves ($1.40M 24h volume); Orca hyUSD/JitoSOL $124k
  - Source: [GeckoTerminal xSOL pools API](https://api.geckoterminal.com/api/v2/networks/solana/tokens/4sWNB8zGWHkh6UnmwiEtzNxL4XrN7uK9tosbESbJFfVs/pools); [Orca xSOL/SOL pool page](https://www.geckoterminal.com/solana/pools/coj59LYbLc6DhMwnxxfPc9mUiknjFSsW4XcuYw4DMPk); [Orca hyUSD/USDC pool](https://www.geckoterminal.com/solana/pools/4tJW2axbTxtT6nKbjB5pZwePtW84cB7E1B6tdCCLGfrC)
- **xSOL is used elsewhere in DeFi:** a Loopscale xSOL lending market (TVL $704k, 3.79% supply APY, 30 Sep 2026) — [DefiLlama yields API](https://yields.llama.fi/pools)
- **Live protocol-level routes:**
  - Max hyUSD redeemable from the SOL pool = **0**, because CR 170.7% > 150%. The BTC pool (CR 168.3%) and HYPE pool (CR 158.3%) are also above 150%.
  - The USDC pool holds 0.0018 USDC.
  - Max hyUSD mintable from the SOL pool before CR hits 150% ≈ 8.70M.
  - Source: live on-chain read (SDK `max_redeemable_stablecoin`, `max_mintable_stablecoin`)

### Inferences
- **For a $1k–$4k xSOL buy:**
  - Jupiter's DEX route beat minting in the app by about **1.7%** that morning: $0.09178 vs NAV/(1 − 1%) ≈ $0.09333.
  - Exits routed through Hylo's redeem landed about 0.8% below mint NAV. The sell leg is effectively capped at NAV × (1 − 1% redeem fee) minus the LST → USDC hop.
  - A round trip at unchanged prices cost only about 0.1–0.3% because the DEX price sat near the redeem-arbitrage floor. In NAV terms the frictions are roughly: entry discount about 0.7%, exit about 1% below NAV.
  - This will not always hold. After strong buying, the DEX price can go up to about NAV × 1.01, the mint-arbitrage ceiling.
- **Rule of thumb for price vs NAV in Neutral/Buy zones:** market price stays within about ±1% of NAV (plus the LST ↔ SOL/USDC swap cost and the Pyth confidence band). In sell zones the lower bound can drop to about NAV × 0.96 or NAV × 0.92 because redeem fees rise.
- **hyUSD exits are currently a secondary-market affair.** With every volatile pool above 150% and the USDC pool empty, hyUSD cannot be redeemed at the protocol for collateral. The fallback is hyUSD → xSOL (1%) → redeem (1%), about 2%. At $4k, Orca's hyUSD/USDC pool costs only about 0.1%.

### Gaps
- There are no historical order-book or slippage statistics beyond the single live quote snapshot.
- The Hylo app's own swap UI (which may route through Titan/Jupiter) was not tested. hylo.so returned HTTP 429 to automated fetches.

---

## Q6. History from launch (2025) to Sep 2026: xSOL vs SOL, CR and leverage ranges, big drawdowns (10 Oct 2025, 2026), hyUSD peg, TVL, incidents

### Takeaway
- xSOL went through a brutal cycle. It traded about $1.95–2.08 in mid/late October 2025 (SOL about $190–200) and hit a daily low of $0.0165 on 7 Jun 2026 (SOL $62.18).
- On 30 Sep 2026 it traded about $0.091 (SOL about $119.5). That is **−95.3% vs SOL −41.0%** from 15 Oct 2025.
- Leverage was about 2.2x in November 2025, about 3.1x in January 2026, about 3.4–3.9x from February to June 2026, and 2.41x live now.
- **On 10 Oct 2025 the stability pool did not trigger.** hyUSD dipped only to about $0.992.
- In **Q1 2026 (SOL −33%)** and **early June 2026 (SOL $82 → $62)**, the V1 stability pool converted hyUSD into xSOL, multiplying xSOL supply (8.3M → about 237M).
- hyUSD kept its peg on DefiLlama data (daily range $0.9922–1.0044).
- TVL:
  - DefiLlama parent total (including hyloSOL LSTs) peaked at $107.6M (15 Jan 2026) and was $65.2M on 30 Sep 2026.
  - The protocol alone is $41.2M.
  - The SOL pool alone is about $35.8M.
- No hacks are recorded.

### Cited Findings
- **Launch timing:** DefiLlama's TVL series starts 29 Jul 2025 at $8.45M — [DefiLlama API](https://api.llama.fi/protocol/hylo). The CEO said the protocol "operated independently for only a few months after launch in July-August" — [Solana Compass](https://solanacompass.com/learn/Lightspeed/how-hylo-is-accelerating-solana-defi-in-2026-plish). An OtterSec audit of the V1 programs ran 10–27 Feb 2025 (follow-up 2–30 Apr 2025), which points to a pre-launch or private-beta period — [OtterSec report](https://hylo-audits.s3.us-east-2.amazonaws.com/OtterSec-Exchange-Stability-Pool-20250513.pdf). IQ.wiki lists "public launch" as "1 Jun 2025", but its dates are rounded to the month and it is low reliability — [IQ.wiki milestones](https://iq.wiki/wiki/hylo-protocol/milestones)
- **TVL (DefiLlama parent "Hylo", which includes the "Hylo LSTs" child):**

| Date | TVL |
|---|---|
| 1 Aug 2025 | $8.97M |
| 1 Sep 2025 | $23.8M |
| 1 Oct 2025 | $68.9M |
| 1 Nov 2025 | $102.9M |
| 1 Dec 2025 | $87.2M |
| 1 Jan 2026 | $82.4M |
| **15 Jan 2026 (peak)** | **$107.6M** |
| 1 Feb 2026 | $73.1M |
| 1 Mar 2026 | $43.8M |
| 1 Apr 2026 | $40.7M |
| 1 Jun 2026 | $36.9M |
| 1 Jul 2026 | $30.6M |
| 1 Aug 2026 | $29.7M |
| 1 Sep 2026 | $48.9M |
| **30 Sep 2026** | **$65.2M** |

  On 30 Sep 2026 the child split was "Hylo Protocol" $41.23M and "Hylo LSTs" $23.99M — [DefiLlama API, Hylo](https://api.llama.fi/protocol/hylo); [DefiLlama protocols API](https://api.llama.fi/protocols); [DefiLlama Hylo page](https://defillama.com/protocol/hylo)
- **Pine's protocol-only TVL:** "Protocol TVL fell 58% from $52M to $22.8M" in Q1 2026, with $13M of net user withdrawals — [Pine Analytics Q1 2026](https://pineanalytics.substack.com/p/hylo-quarterly-operations-overview). This is a different basis from DefiLlama's parent total, which includes hyloSOL.
- **Q4 2025:** "the protocol absorbed SOL's 40% decline without triggering stability mechanisms" because new xSOL buyers entered. Q1 2026 "broke that pattern … forced the stability pool activations" — [Pine Analytics Q1 2026](https://pineanalytics.substack.com/p/hylo-quarterly-operations-overview)
- **10 Oct 2025 crash:** "Hylo emerged from this period without any stability pool activations, with market forces alone being sufficient". Around that period CR reached about 145% (Stability Mode One) and then went back to about 160% as users bought xSOL at the bottom — [Solana Compass, Lightspeed notes](https://solanacompass.com/learn/Lightspeed/how-hylo-is-accelerating-solana-defi-in-2026-plish)
- **hyUSD on 10–11 Oct 2025 (DefiLlama 4-hour prices):** $0.9996 at 10 Oct 12:00 UTC → $0.9922 at 10 Oct 24:00 → $0.9906 at 11 Oct 04:00 → $0.9972 by end of 11 Oct. SOL went $221.3 → $184.5 over the same window — [DefiLlama coins chart API](https://coins.llama.fi/chart/solana:5YMkXAYccHSGnHn9nob9xEvv6Pvka9DZWH7nTbotTu9E)
- **hyUSD peg over the whole period (DefiLlama daily, 18 Sep 2025 → 29 Sep 2026):**
  - Minimum $0.9922 (10 Oct 2025), maximum $1.0044 (26 Dec 2025)
  - The only day below $0.995 was 10 Oct 2025
  - Monthly averages $0.9990–1.0011
  - Source: [DefiLlama coins API](https://coins.llama.fi/chart/solana:5YMkXAYccHSGnHn9nob9xEvv6Pvka9DZWH7nTbotTu9E); [DefiLlama stablecoin page](https://defillama.com/stablecoin/hylo-hyusd)
  - **Conflict:** CoinGecko's daily hyUSD series shows many prints of $0.97–0.99 from January to May 2026 and $0.93–0.97 in late June 2026 (low $0.9307 on 30 Jun 2026; "ATL" $0.927 on 29 Jun 2026; plus an obviously bad "ATH" of $100.36) — [CoinGecko hyUSD](https://www.coingecko.com/en/coins/hylo-usd). DefiLlama shows about $0.998–1.001 on those same days, and CoinGecko's xSOL series in the same window (16–26 Jun 2026) is frozen at $0.0286. I treat the CoinGecko hyUSD dips as a data-quality problem, not a depeg. DefiLlama Research also states "hyUSD held its peg" — [DefiLlama Research newsletter](https://research-newsletters.defillama.com/p/leverage-without-liquidation)
- **xSOL price vs SOL (CoinGecko daily; the xSOL series starts 15 Oct 2025):**

| Date | SOL | xSOL | Note |
|---|---|---|---|
| 15 Oct 2025 | $202.58 | $1.9506 | |
| 26 Oct 2025 | $193.93 | $1.80 | CoinGecko ATH $2.08 that day, intraday |
| 1 Nov 2025 | $187.17 | $1.6849 | |
| 1 Dec 2025 | $133.83 | $0.6598 | |
| 1 Jan 2026 | $124.52 | $0.5037 | |
| 15 Jan 2026 | $146.51 | $0.7978 | |
| 1 Feb 2026 | $105.49 | $0.2580 | |
| 1 Mar 2026 | $84.67 | $0.0748 | |
| 1 Apr 2026 | $83.04 | $0.0639 | |
| 1 Jun 2026 | $82.34 | $0.0536 | |
| **7 Jun 2026** | **$62.18** | **$0.0165** | daily low; CoinGecko ATL $0.01486 on 6 Jun 2026, intraday |
| 1 Jul 2026 | $73.56 | $0.0276 | |
| 1 Aug 2026 | $72.79 | $0.0263 | |
| 1 Sep 2026 | $103.01 | $0.0658 | |
| **30 Sep 2026** | **$119.47** | **$0.0913** | |

  Source: [CoinGecko market_chart API, xSOL](https://api.coingecko.com/api/v3/coins/hylo-leveraged-sol/market_chart?vs_currency=usd&days=365&interval=daily); [CoinGecko SOL](https://api.coingecko.com/api/v3/coins/solana/market_chart?vs_currency=usd&days=365&interval=daily)
- **Daily xSOL/SOL return ratios on days SOL moved more than 6%:**
  - November 2025: about 2.1–2.8x
  - February 2026: about 3.0–4.3x
  - June 2026: about 3.7–4.0x
  - August–September 2026: about 2.5–2.8x
  - Examples: 6 Feb 2026 SOL −14.8% / xSOL −49.1%; 6 Jun 2026 SOL −7.5% / xSOL −30.1%; 19 Sep 2026 SOL +11.0% / xSOL +29.4%
  - Source: calculated from the CoinGecko series above
- **xSOL supply dilution:** "from a modest 8.4 million [Oct 2025] to 235 million [Jun 2026]" — [DefiLlama Research newsletter](https://research-newsletters.defillama.com/p/leverage-without-liquidation). CoinGecko market cap/price gives about 8.3M (16 Oct 2025), 24.1M (15 Nov 2025), 32.9M (1 Jan 2026), 94.6M (15 Feb 2026), 98.4M (1 Jun 2026), 224.0M (7 Jun 2026), 236.7M (8 Jun 2026), about 150M (early Jul 2026), 180.6M (15 Aug 2026), and 160.8M (30 Sep 2026). On-chain supply on 30 Sep 2026 was 160,708,971.6 — [CoinGecko API](https://api.coingecko.com/api/v3/coins/hylo-leveraged-sol/market_chart?vs_currency=usd&days=365&interval=daily); live on-chain read
- **hyUSD supply (DefiLlama stablecoins):**

| Date | hyUSD supply |
|---|---|
| 1 Oct 2025 | 21.27M |
| 1 Nov 2025 | 37.51M |
| 1 Jan 2026 | 35.18M |
| 1 Feb 2026 | 30.48M |
| 1 Mar 2026 | 16.82M |
| 1 Jun 2026 | 14.92M |
| 1 Jul 2026 | 11.19M |
| 1 Sep 2026 | 17.02M |
| 30 Sep 2026 | 24.39M (on-chain 24.69M) |

  Source: [DefiLlama stablecoin API](https://stablecoins.llama.fi/stablecoin/302)
- **Stability-pool activations:** $7.9M in Q1 2026 — [Pine](https://pineanalytics.substack.com/p/hylo-quarterly-operations-overview); about $8M over 3 months in 59 transactions, with a $763K profit — [KuCoin news](https://www.kucoin.com/news/flash/hylo-launches-v2-expands-on-chain-leverage-to-stocks-and-multi-asset-collateral). The late-2025 podcast mentioned "two instances where the stability pool has been activated in Hylo's history", both profitable for stakers — [Solana Compass](https://solanacompass.com/learn/Lightspeed/how-hylo-is-accelerating-solana-defi-in-2026-plish)
- **V2 timeline:**
  - "Late March brought … the V2 beta launch at v2.hylo.so/early-access" — [Pine](https://pineanalytics.substack.com/p/hylo-quarterly-operations-overview)
  - A KuCoin flash item dated 17 Jun 2026 reports "Hylo Launches V2" — [KuCoin](https://www.kucoin.com/news/flash/hylo-launches-v2-expands-on-chain-leverage-to-stocks-and-multi-asset-collateral)
  - Solana's June 2026 roundup: "Hylo shipped V2 with its xAsset Engine … and crossed $500M in volume across $hyUSD, $sHYUSD, and $xSOL" — [Solana Ecosystem Roundup, June 2026](https://solana.com/news/solana-ecosystem-roundup-june-2026)
- **Incidents:** DefiLlama's Hylo entry has an empty `hacks` list — [DefiLlama API](https://api.llama.fi/protocol/hylo). I found no reports of exploits.

### Inferences
- **Estimated SOL-pool CR and leverage before V2** (TVL = hyUSD supply + xSOL market cap, from DefiLlama hyUSD supply and CoinGecko xSOL market cap):

| Date | CR | Leverage |
|---|---|---|
| 1 Nov 2025 | 181% | 2.23x |
| 1 Dec 2025 | 154% | 2.84x |
| 1 Jan 2026 | 147% | 3.12x |
| 1 Feb 2026 | 136% | 3.75x |
| 1 Mar 2026 | 142% | 3.40x |
| 1 Apr 2026 | 135% | 3.84x |
| 1 May 2026 | 141% | 3.42x |
| 1 Jun 2026 | 135% | 3.83x |
| 7 Jun 2026 | 134% | 3.93x |

  The implied SOL-pool TVL ($51.8M on 1 Jan 2026 → $22.1M on 1 Apr 2026) matches Pine's "$52M → $22.8M", which supports this method. These are daily snapshots. Intraday CR clearly fell below 130% during activations, because the stability pool triggered.
- **Performance by window:**
  - 1 Nov 2025 → 1 Feb 2026: SOL −43.6%, xSOL −84.7%
  - 1 Jan → 1 Apr 2026: SOL −33.3%, xSOL −87.3%
  - 7 Jun → 30 Sep 2026: SOL +92.1%, xSOL +452%
  - 1 Aug → 30 Sep 2026: SOL +64.1%, xSOL +247.6%
- **The rally recovered more than a fixed-supply model predicts.** At a CR of about 134% on 7 Jun (L ≈ 3.93x) a static-supply model gives about +362%, yet xSOL rose about 452%. hyUSD supply more than doubled (11.2M on 1 Jul → 24.7M on 30 Sep), and minting hyUSD from the SOL pool re-levers xSOL. Path dependence can help as well as hurt.
- Losses were far larger than "3x SOL" suggests because deleveraging and dilution happened near the lows. A holder from 15 Oct 2025 lost 95% while SOL lost 41%.

### Gaps
- There is no free, reliable xSOL price source for 10 Oct 2025 itself: the CoinGecko series starts 15 Oct 2025, GeckoTerminal's free API only covers 180 days, and DefiLlama coins has no earlier xSOL data. xSOL's exact move during the crash is unverified.
- Exact dates and sizes of each stability-pool activation are not published.
- **Conflict:** the podcast says "two instances" of activation before the recording (late 2025), while Pine says Q4 2025 triggered no stability mechanisms. Those two activations may have been before Q4 2025; this is unresolved.
- Exact on-chain CR history (intraday) and V2-era CR history (June–September 2026) could not be rebuilt without an archival node or indexer.

---

## Q7. Security and governance: audits, oracle, admin keys and upgradeability, team and funding, tail risks, points/airdrop

### Takeaway
Audits:
- OtterSec (Feb–Apr 2025, V1): 2 critical findings, both resolved
- Accretion (Sep–Nov 2025, V1.2): 1 high finding, remediated
- Accretion (Feb–Jul 2026, V2): 0 critical/high, 16 medium, 3 medium acknowledged and not fixed. The deployed build was marked "unverified" in the report.

Pricing uses Pyth SOL/USD (10 s staleness limit, 1% confidence tolerance) plus Sanctum stake-pool "true" LST value.

The exchange, Earn Pool and router programs are upgradeable. Their upgrade authority is a Squads v4 vault controlled by a multisig: threshold 3, 8 members, 4 of whom can vote, 6-hour timelock. The exchange was last upgraded 16 Sep 2026.

Funding and team: a $1.5M seed in August 2025 led by Robot Ventures. The CEO is "Narek (Plish)". An XP points program (xSOL earns 20 XP per $ per day) runs with no announced token.

Main tail risks:
- a fast SOL gap-down through CR 100%
- oracle freeze or failure
- contract or upgrade risk
- LST stake-pool loss
- exit-liquidity limits (Earn Pool 1M/epoch, empty USDC pool)
- admin-tunable parameters

### Cited Findings
- **Audits listed by Hylo:** OtterSec (V1.1 Exchange & Stability Pool, "Feb 2025"); Accretion (V1.2, Dec 2025); Accretion (V2 Exchange, Earn Pool & Router, Jul 2026) — [docs, Audits](https://docs.hylo.so/security/audits)
- **OtterSec report dated 5 May 2025:**
  - Engagement 10–27 Feb 2025, follow-up 2–30 Apr 2025
  - 7 findings: 2 Critical (collateral-ratio manipulation via unvalidated LST registry accounts; EMA-price arbitrage), 1 Medium (xSOL mint-fee bypass), 2 Low, 2 Info
  - The criticals are marked RESOLVED
  - Code lives in the private repo github.com/hylo-so/protocol
  - Source: [OtterSec PDF](https://hylo-audits.s3.us-east-2.amazonaws.com/OtterSec-Exchange-Stability-Pool-20250513.pdf)
- **Accretion (8 Dec 2025):** engagement 1 Sep – 26 Nov 2025; 16 findings; top one a high-severity "price manipulation through non-canonical price feeds". Mediums included fees using the wrong stability mode, missing slippage protection, and yield miscalculation. "All immediately relevant findings were fully remediated" — [Accretion PDF](https://hylo-audits.s3.us-east-2.amazonaws.com/Accretion-Hylo-Dec2025.pdf)
- **Accretion V2 (8 Jul 2026):**
  - Engagement 23 Feb – 2 Jul 2026
  - "51 findings …: 16 medium, 25 low, and 10 informational; no critical or high … 44 were fixed, 6 accepted or acknowledged"
  - Acknowledged mediums: ACC-M1 (LST-USDC swaps ignore SPL stake-pool withdrawal fees and misprice rebalance trades), ACC-M13 (LP accounting ignores drawdown debt and misprices sHYUSD), ACC-M14 (mint fee uses pre-fee amount and overcharges users)
  - The exchange program's audit result reads "Status: unverified … not verified" against build hash 958348f…
  - Source: [Accretion V2 PDF](https://hylo-audits.s3.us-east-2.amazonaws.com/Accretion-HyloV2-July2026.pdf)
- **Oracles:** Pyth SOL/USD, BTC/USD, HYPE/USD, and USDC/USD (par check only). LSTs are priced with "the Sanctum SOL value calculator program … avoiding market manipulation risks" — [Hylo Equations](https://docs.hylo.so/technical-addendum/hylo-equations). Live config: `oracle_interval_secs` = 10, `oracle_conf_tolerance` = 0.01 (1%). SOL/USD oracle account [7AviUf9n…HmyE](https://solscan.io/account/7AviUf9nL62mcxNbQGKm4nKDQnPjswo6c5MX4D57HmyE) — live read of the [Hylo config account](https://solscan.io/account/9cd2sAfbBvKs4SX9YKo4dcjwP3TgTVQ8dT5koshGcDND). Code bounds: interval 1–60 s, confidence tolerance ≤ 5%, and a Pythnet verification-level check — [pyth/oracle.rs](https://github.com/hylo-so/sdk/blob/main/hylo-core/src/pyth/oracle.rs)
- **Upgradeability and admin:**
  - The [Exchange](https://solscan.io/account/HYEXCHtHkBagdStcJCp3xbbb9B7sdMdWXFNj6mdsG4hn), [Earn Pool](https://solscan.io/account/HysTabVUfmQBFcmzu1ctRd1Y1fxd66RBpboy1bmtDSQQ) and [Router](https://solscan.io/account/hyRouTRDAgn65xyyJ3L5c4k5SFmSdr3NxDV8Euzjy3f) programs are upgradeable, all with upgrade authority [GzyhwK4y…MiNP](https://solscan.io/account/GzyhwK4y7EKPEevAMc2TEpgi1Y3znwj14FUzkHmCMiNP). That is a system-owned, data-less account (a Squads vault PDA).
  - Its latest transactions (24 Sep 2026) call the Squads v4 program with multisig [14Ajz35n…5NJm](https://solscan.io/account/14Ajz35nKp4KUkHaLxucKfwCEKUeXaRCCuDYXqzK5NJm). Decoded: **threshold 3, 8 members (4 with full vote/execute permissions, 3 initiate-only, 1 none), time lock 21,600 s (6 h)**, config authority = none (autonomous).
  - Last deploys: Exchange at slot 447,625,876 (**16 Sep 2026 21:34 UTC**), Router at slot 439,863,765 (17 Aug 2026), Earn Pool at slot 434,128,362 (20 Jul 2026).
  - Source: my RPC reads (`getAccountInfo`, `getSignaturesForAddress`, `getBlockTime`) on 30 Sep 2026
- **Admin-tunable parameters** (exchange IDL instructions): levercoin fees, hyUSD mint threshold, LST buy/sell curves, the yield harvest config, oracle interval and confidence tolerance, the SOL/USD oracle account, USDC fees, exo borrow-rate curves and market-cap limits, plus `pause_protocol`/`pause_lst_pair` and a two-step `propose/approve/accept_address_update`. Earn Pool: `update_withdrawal_fee`, `update_withdrawal_limit`, `update_deposit_limit`, `pause_earn_pool`, `absorb_loss` — [hylo_exchange IDL](https://github.com/hylo-so/sdk/blob/main/hylo-idl/idls/hylo_exchange.json); [hylo_earn_pool IDL](https://github.com/hylo-so/sdk/blob/main/hylo-idl/idls/hylo_earn_pool.json)
- **Code-level bounds on those parameters:** levercoin fee ≤ 10%; harvest multiplier ceiling 1–5x; harvest fee ≤ 10%; mint threshold within 150–170%; exo levercoin market-cap limit $1M–$100M — [fees/controller.rs](https://github.com/hylo-so/sdk/blob/main/hylo-core/src/fees/controller.rs); [yields.rs](https://github.com/hylo-so/sdk/blob/main/hylo-core/src/yields.rs); [mode.rs](https://github.com/hylo-so/sdk/blob/main/hylo-core/src/rebalance/mode.rs); [limiter/levercoin.rs](https://github.com/hylo-so/sdk/blob/main/hylo-core/src/limiter/levercoin.rs)
- **Live admin keys** in the config account: admin [12DAP8y5…y4Ce](https://solscan.io/account/12DAP8y5XemtK1pJFNMVVnQugt3PUAbZZr9SmyVvy4Ce), pause authority [H6qRPNvL…pCC5](https://solscan.io/account/H6qRPNvLnuQSZHAWzKDwv2bokBBupC99aJMV4u5FpCC5), treasury mAQQ9Bph…gVyV. Both admin and pause keys are system accounts with no data. The pause authority's last transaction (30 Jul 2026) invoked the Squads program — live RPC reads
- **Funding:** $1.5M seed announced August 2025, led by Robot Ventures, with Solana Ventures, YTWO and Colosseum — [DefiLlama raises (API)](https://api.llama.fi/protocol/hylo); [Hylo on X, seed announcement](https://x.com/hylo_so/status/1953488827516915765); [crypto-fundraising.info](https://crypto-fundraising.info/blog/hylo-raised-1-5m-in-a-seed-funding-round/)
- **Team:** "Hylo CEO Narek (known as Plish)" — [Solana Compass, Lightspeed notes](https://solanacompass.com/learn/Lightspeed/how-hylo-is-accelerating-solana-defi-in-2026-plish). The hyloSOL validator is run "in partnership with Sentinel and Phase Labs" — [Liquid Staking Tokens](https://docs.hylo.so/product-guide/liquid-staking-tokens)
  - **Warning:** a search-engine summary named "Edward West, Aaron Post, Gavin McDermott, Mike Gagnon, and Ray Marceau" as founders, with Edward West "Co-Founder of Impact Hub Oakland". Those names belong to a *different* "Hylo" (the hylo.com community-coordination platform), not hylo.so. Do not use them.
- **XP program:**
  - XP per $ per day: xSOL/xBTC **20**; hyUSD 5; hyloSOL+ 5; eHYUSD 1; hyloSOL 1
  - Referrals earn 10% of referees' XP; referees get a 5% boost
  - "The XP program runs in seasons"
  - Source: [docs, XP System](https://docs.hylo.so/product-guide/xp-system)
  - Airdrop trackers say "No token has been confirmed" — [AirdropAlert](https://airdropalert.com/airdrops/hylo/). A search summary claims Season 1 started 5 Dec 2025, but I did not verify this against a primary source.
  - **Status on 23 Sep 2026:** a KuCoin explainer describes **Season 1** as live with xSOL 20 / hyUSD and hyloSOL+ 5 / eHYUSD and hyloSOL 1 XP per $ per day. It says "Points ≠ confirmed airdrop or tokens" and "TGE has not been officially announced", and that crowns and boosts from Season 0 carry forward — [KuCoin insight, 23 Sep 2026](https://www.kucoin.com/news/insight/SOL/6ab3dc5174fd460007c501cf)
  - Search-engine summaries of news items (Bitget/edgecap results, not opened) said eHYUSD launched with a "$15M initial cap and 30-day Genesis Boost", and that holding eHYUSD gave a "5% to 25%" boost on Season 1 points. Neither was verified against a primary Hylo source. The live Earn Pool deposit cap on 30 Sep 2026 is 25M hyUSD (on-chain PoolConfig).
- **VaR framing:** SOL 1-day 99.9% VaR −32.95%; "the 150% target ensures the SOL pool can withstand a price drop corresponding to the 0.1% worst day" — [Value-at-Risk Analysis](https://docs.hylo.so/technical-addendum/value-at-risk-analysis)

### Inferences — main tail risks for an xSOL buyer
1. **Market gap-down.** At the live CR, a 41% SOL drop zeroes xSOL. At the 150% target, 33% does. Even in a slower decline, V2's sell zone de-leverages after the drop (locking in losses), and exits then cost 4–8%.
2. **Oracle.** A stale Pyth feed (> 10 s) or one with a wide confidence band (> 1%) makes transactions fail. That can freeze mint/redeem during a crash. ACC-L1 describes exactly this scenario for settlement.
3. **Contract and upgrade risk.** Code changes after the audit are possible: the exchange was upgraded 16 Sep 2026, after the 8 Jul 2026 report. The protocol repo is private, so the SDK's open-source math is the only public code. A 3-of-4-voter Squads multisig with a 6 h timelock limits single-key risk, but a 6-hour window gives users little time to react.
4. **LST risk.** Collateral is about 90% jitoSOL. It is priced at stake-pool value, not market price, so a market depeg of jitoSOL does not hit NAV. A real stake-pool loss (slashing, or a stake-pool program bug) would, and would hit xSOL first, amplified by L.
5. **hyUSD run / exit liquidity.** Direct protocol redemption is closed while pools are above 150% CR and the USDC pool is empty. Earn Pool withdrawals are capped at 1M hyUSD per epoch. In a panic, hyUSD exits depend on about $2.7M of Orca depth.
6. **Governance-tunable economics.** Fees, the harvest multiplier (up to 5x) and thresholds can change within code bounds. For example, a higher m_c would raise xSOL's carry above 165% CR.

### Gaps
- I did not identify the multisig members. I could not confirm that the `admin` config key (12DAP8y5…) is itself a Squads vault; its latest transaction touched the shadow/test exchange program.
- The V2 "unverified build" status may have been fixed later. There is no public verifiable-build attestation.
- No token or TGE has been announced by the team, and I found no primary source for an XP season calendar in 2026.
