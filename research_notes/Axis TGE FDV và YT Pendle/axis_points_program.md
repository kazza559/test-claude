# Axis (AxisFDN, axis.to) "Coordinates" Points Program: Structure, Earning Rates, Issuance, and Implied $/Point

Research date: 2026-09-28 (all "now" values captured 2026-09-28 11:50–12:00 UTC unless stated otherwise).

**Identity check (to avoid confusion with other projects named Axis).** The project here is Axis Foundation (X: @AxisFDN, site axis.to, app app.axis.to, docs docs.axis.to). It issues **USDx**, a synthetic dollar, and **sUSDx**, its staked yield-bearing ERC-4626 vault. Yield comes from a delta-neutral, cross-venue arbitrage engine. It is NOT any of these:
- **Axis Robotics** (@axisrobotics): a physical-AI data project on Base. It runs its own "Axis Points", an Aug 2026 Binance Wallet campaign with 1.5M "Axis Points", and a Kaito creator program with a "$AXIS" ticker ([airdrops.io Telegram, 2026-08-20 / 2026-08-26](https://t.me/s/airdrops_io?before=7827); [X / CryptoLakhan](https://x.com/CryptoLakhan/status/2092520653333123391)). Anything mentioning "$AXIS airdrop", "Axis Points", "Kaito" or "1.5M Points campaign" refers to Axis Robotics, not AxisFDN.
- **Stables Labs USDX**: a different protocol on DefiLlama ([DefiLlama API](https://api.llama.fi/protocols)).
- **yAxis**: also unrelated ([DefiLlama API](https://api.llama.fi/protocols)).

---

## 1. Program structure: name, seasons, dates, and token/airdrop status

### Takeaway
The points are called **"Coordinates"** (the leaderboard is called "the Grid"). The seasons so far:
- **Season 0 ("Origin")**: the Origin Vault pre-deposit, deposits from Jul 29, 2026, with accrual through the 30-day lock ending Sep 4, 2026.
- **Season 1**: started **Sep 4, 2026** and runs **90 days**, which by calculation ends about **Dec 3, 2026**. That is the same day the Axis Pendle markets mature.

No token, TGE date, airdrop allocation % or conversion rate has been announced. Official copy says Coordinates "confer no entitlement to any token, allocation, or reward". The only token hints are Dec 2025 press coverage of a "governance token allocation program" and a "public token sale", which was then planned for "early 2026" and has already slipped.

### Cited Findings
- **Name and branding.** The program is named "Coordinates". The docs describe it as "your position on the Grid, the map of every depositor's standing in Axis Origin. You accrue them on your deposited balance over time, scaled by your Multiplier." — [Axis Docs – Origin Vault](https://docs.axis.to/origin-vault/origin-vault.md)
- **Where users see it.** The program lives at app.axis.to/coordinates: "where you can see your Coordinates, create an invite link and set what you share with the people you invite". — [Axis Docs – Origin Vault](https://docs.axis.to/origin-vault/origin-vault.md)
- **Season 0 (Origin).** The pre-deposit opened Jul 29, 2026 at 10:00 AM New York time. The window was "about a week, closing on August 5 or when the $50M cap fills". Deposits were USDT/USDC on Ethereum via Upshift, and the position token is ogUSDx. — [AxisFDN X article "Axis Origin: What You're Depositing Into", 2026-07-27](https://x.com/AxisFDN/status/2081726383240126870)
- **The 30-day lock.** "The 30 days run from August 5 regardless of when the cap fills, so the lock ends on September 4." At vault close, "the vault mints USDx with the full balance and stakes half of it as sUSDx". — [AxisFDN X article, 2026-07-27](https://x.com/AxisFDN/status/2081726383240126870)
- **First tranche filled fast.** "$50M deposited in 22 hours. Positions locked at base yield + 2x Coordinates multiplier. The Origin Vault is now closed." — [AxisFDN on X, 2026-07-30](https://x.com/AxisFDN/status/2082805356820906485)
- **Final Origin size.** "We closed the Origin Vault on August 5 with $67,248,750 deposited across 1,857 wallets." ogUSDx has delivered "11.58% annualized" since close. — [AxisFDN X article "The Origin Vault: What's Next for USDx and Coordinates", 2026-09-01](https://x.com/AxisFDN/status/2094772784002154737)
  - The Jul 30 tweet said "closed" at $50M, yet the final figure was $67.25M. This suggests a second tranche at 1.75x was opened afterward.
- **Season 1 announcement.** "Origin was Season 0 of Coordinates... Season 1 starts on September 4, 2026 and runs for 90 days. From that point, Coordinates reflect where USDx is being put to work across the ecosystem." — [AxisFDN X article, 2026-09-01](https://x.com/AxisFDN/status/2094772784002154737)
- **Docs are stale on seasons.** The docs page still calls the Origin pre-deposit "Season 1" ("Season 1 opened July 29 and the deposit window closes August 5") with an "Initial cap. $100M". The Sep 1 X article calls Origin "Season 0" and says Season 1 starts Sep 4. — [Axis Docs – Origin Vault](https://docs.axis.to/origin-vault/origin-vault.md) vs [AxisFDN X article, 2026-09-01](https://x.com/AxisFDN/status/2094772784002154737)
  - The Jul 15 launch tweet gave "The cap is $50m", while the docs give $100M. — [AxisFDN on X, 2026-07-15](https://x.com/AxisFDN/status/2077377662780047641)
- **Official disclaimer.** "Coordinates are non-transferable, have no monetary value, and confer no entitlement to any token, allocation, or reward. Program terms remain subject to final published rules." — [AxisFDN X article, 2026-07-27](https://x.com/AxisFDN/status/2081726383240126870)
  - Another article says Coordinates carry "no cash value on their own". — [AxisFDN X article "How the Origin Vault Works", 2026-07-22](https://x.com/AxisFDN/status/2079919958713077866)
- **Token plans in Dec 2025 press.** At the seed announcement, Axis would open the Origin Vault "offering early adopters ... the opportunity to participate in the governance token allocation program". The vault "aims to gather up to $1 billion in deposits, followed by a public token sale and the full launch of the protocol scheduled for early 2026". — [The Cryptonomist, 2025-12-03](https://en.cryptonomist.ch/2025/12/03/axis-revolutionizes-institutional-yield-5-million-raised-to-bring-transparent-yield-on-usd-bitcoin-and-gold/)
  - The Block's wording: "a target of up to $1 billion in deposits ahead of a public token sale and full protocol launch early next year". The seed round was $5M, led by Galaxy Ventures, with OKX Ventures, CMT Digital, FalconX, GSR, Maven 11, CMS Holdings and Marc Zeller. — [The Block, 2025-12-03](https://www.theblock.co/post/381215/axis-5-million-usd-round-galaxy-ventures-onchain-yield-protocol-usd-bitcoin-gold)
- **Docs on governance.** The docs' own Q&A endpoint answered that there is "no mention of an Axis governance token, a TGE date, or any allocation for Coordinates holders". It also said Axis "has no formal onchain governance today". — [Axis Docs (GitBook ask endpoint, Protocol Administration)](https://docs.axis.to/technical-and-architecture/governance.md)
- **Third-party status checks.** airdrops.io (updated 2026-09-04): "Axis has not confirmed a token or airdrop... no conversion rate has been published". — [airdrops.io/axis](https://airdrops.io/axis/)
  - The airdrops.io 2026 tier list ranked AxisFDN in **C tier**: "No token is confirmed, no conversion rate has been published... Real capital, real lockup, unconfirmed everything." — [AIRDROPS.IO X article, 2026-08-19](https://x.com/airdrops_io/status/2090032492401095159)
- **Geo-restrictions.** Axis app pages return "Axis isn't available in your region" from a US IP. — [app.axis.to/origin](https://app.axis.to/origin)
  - The docs list "No US persons" plus sanctions screening. — [Axis Docs – Eligibility & Onboarding](https://docs.axis.to/resources-and-legal/eligibility-and-onboarding.md)

### Inferences
- **Season 1 end date.** 90 days from Sep 4, 2026 is Dec 3, 2026. This lines up exactly with the Pendle USDx/sUSDx market maturity of 3 Dec 2026, so a YT held to maturity captures essentially all remaining Season 1 accrual.
- **When a TGE could come.** A TGE is unlikely before the end of Season 1 (Dec 3, 2026). Given the stated "public token sale" intent, a Season 2 or a token sale step before any airdrop is plausible. Each of these would add more points or more buyers before any conversion, which is a dilution risk.
- **Allocation is unknown.** No airdrop % exists. Any $/point figure therefore depends entirely on an assumed allocation % and FDV (see Section 6).

### Gaps
- No official airdrop allocation %, TGE date, token ticker, vesting or claim conditions, or points-to-token conversion rule was found in the docs, Telegram or official X articles.
- The full "final published rules" referenced in the disclaimer could not be located.
- Axis's X timeline after Sep 4, 2026 could not be read in full: syndication was rate-limited and the Telegram channel only reposts bare links. There may be later posts (e.g., new integrations or multiplier changes) that were not captured.

---

## 2. Earning rates: Coordinates per $ per day by activity

### Takeaway
**Season 0 (Origin):** base 10 Coordinates/$/day.
- × 2.0 for the first $50M, i.e. **20/$/day**.
- × 1.75 for the second tranche, i.e. **17.5/$/day**.

**Season 1 (from Sep 4, 2026):** position-specific multipliers, where "Nx" works out to about **N Coordinates per $ per day**. This is inferred from leaderboard data, since a 10x vault position accrues about 9.93–10.1/$/day.

| Where your USDx sits | Multiplier | Coordinates per $1 per day |
|---|---|---|
| Stay in the Origin / Ecosystem Vault (ogUSDx) | 10x | ≈10 |
| Hold USDx | 16x | 16 |
| Hold sUSDx | 4x | 4 |
| Curve USDx/USDT LP | 20x | 20 |
| Curve USDx/sUSDx LP | 10x | 10 |
| Pendle YT-USDx | 24x | 24 |
| Pendle YT-sUSDx | 6x | 6 |
| Pendle LP, USDx market | 20x | 20 |
| Pendle LP, sUSDx market | 5x | 5 |

Other rules:
- **No stacking.** Multipliers do not stack across venues.
- **Pendle fee.** Pendle takes a 5% fee on YT points.
- **YT basis.** YT points apply to the underlying amount each YT represents: 1 YT is treated as 1 USDx of underlying.
- **Other integrations.** No Morpho, Euler, Aave or CEX integrations with Coordinates were found.

### Cited Findings
- **Season 0 base and boost.** "Every dollar deposited earns 10 Coordinates per day. For the Origin Vault a one-time 2x launch boost applies on top, so eligible pre-deposits accrue 20 Coordinates per dollar per day from July 29." — [AxisFDN X article, 2026-07-27](https://x.com/AxisFDN/status/2081726383240126870)
  - The Jul 22 article gives a worked example: "deposit $10,000 on Day 1 and you earn 10000 x 10 x 30 x 2.0 multiplier = 6,000,000 Coordinates over the course of the 30-day lock-up". — [AxisFDN X article, 2026-07-22](https://x.com/AxisFDN/status/2079919958713077866)
- **Season 0 tranches.** "Depositors in the first $50M are set at a 2x multiplier for all their deposits in the Origin Vault. Depositors in the second $50M are set at a 1.75x multiplier." — [Axis Docs – Origin Vault](https://docs.axis.to/origin-vault/origin-vault.md)
  - Also: "After Origin ends, all users earn Coordinates under the same asset and duration based rules, regardless of when they enter." — [AxisFDN X article, 2026-07-27](https://x.com/AxisFDN/status/2081726383240126870)
- **Season 1 accrual rules.** "Coordinates accrue daily based on the eligible position and its corresponding multiplier. The same dollar counts in one position at a time, so venue multipliers do not stack." — [AxisFDN X article, 2026-09-01](https://x.com/AxisFDN/status/2094772784002154737)
  - Also: "The pre-deposit boost used during Origin ends with Season 0. From September 4, the vault position moves to a flat 10x multiplier, while other USDx and sUSDx positions carry their own rates." — same article.
- **Season 1 multiplier table.** The official image embedded in the Sep 1 article gives the values in the table above: ogUSDx vault 10x; hold USDx 16x; hold sUSDx 4x; Curve USDx/USDT LP 20x; Curve USDx/sUSDx LP 10x; Pendle YT-USDx 24x; Pendle YT-sUSDx 6x; Pendle LP USDx market 20x; Pendle LP sUSDx market 5x. — [AxisFDN X article image, 2026-09-01](https://pbs.twimg.com/media/HRIeu4WbcAAgBU6.png) (from [article](https://x.com/AxisFDN/status/2094772784002154737))
  - airdrops.io reproduced these numbers (24x, 20x, 16x, 10x, "4x–6x"). — [airdrops.io/axis](https://airdrops.io/axis/)
- **Pendle's framing.** "Introducing @AxisFDN USDx and sUSDx (3 Dec 2026 maturity)... with the highest multiplier for Axis points". — [Pendle on X, 2026-09-04](https://x.com/pendle_fi/status/2095738643793207563)
- **Pendle market data (Pendle API, 2026-09-28 ~11:00–11:52 UTC).** Both markets expire 2026-12-03 00:00 UTC. — [Pendle API USDx market](https://api-v2.pendle.finance/core/v1/1/markets/0x0bef762d2094ac80821c657dea6783fc43435292); [Pendle API sUSDx market](https://api-v2.pendle.finance/core/v1/1/markets/0x5e572498e9f83650f0ff24194999bddb4b390928)

  | | USDx market (0x0bef…5292) | sUSDx market (0x5e57…0928) |
  |---|---|---|
  | Pool liquidity | $2.24M | $5.99M |
  | Total TVL | $5.52M | $8.77M |
  | Underlying APY | 0% | 21.6% |
  | Implied APY | 15.0% | 19.3% |
  | PT price | $0.9751 | $0.9688 |
  | YT price | $0.02478 | $0.03114 |
  | SY price | — | $1.0295 |
  | 24h volume | $18.8K | $704K |

- **On-chain supplies (Ethereum RPC eth_call, 2026-09-28 ~12:00 UTC).**
  - USDx totalSupply = 56,358,179 — [Etherscan USDx](https://etherscan.io/address/0xa1fA7777974312f7d801A8880714a218F76233f8)
  - sUSDx totalSupply = 35,042,058 shares, totalAssets = 36,079,594 USDx, so 1 sUSDx = 1.02961 USDx — [Etherscan sUSDx](https://etherscan.io/address/0xEB892628D1E58BC475A6dCB7F5dBC4F591632AA4)
  - YT-USDx (= PT-USDx) supply = 4,362,434 — [Etherscan YT-USDx](https://etherscan.io/address/0xa91277e31f6be8c33850dde8dfacb27bad1be6fb)
  - YT-sUSDx (= PT-sUSDx) supply = 6,088,209 — [Etherscan YT-sUSDx](https://etherscan.io/address/0x96dcb9501bcc8128b7683980a63250448ea5334b)
  - SY-USDx holds 5,633,248 USDx; SY-sUSDx holds 8,730,421 sUSDx.
- **Curve pools (Curve API, 2026-09-28).** — [Curve API](https://api.curve.finance/v1/getPools/all/ethereum)
  - USDx/USDT pool 0xE521…6C45: TVL $3.05M (1.74M USDx + 1.31M USDT).
  - sUSDx/USDx pool 0x1C9A…81eE: TVL $2.01M (0.97M sUSDx + 1.02M USDx).
- **Pendle YT points mechanics.** "Pendle collects a 5% fee from all yield accrued (including points) by all YT in existence". Also: "Fees on points are applied similarly as Pendle treats points as a form of yield". Partner protocols deduct the 5% when allocating points. — [Pendle Docs – Fees](https://docs.pendle.finance/pendle-v2/ProtocolMechanics/Mechanisms/Fees)
  - "1 YT earns the same points as 1 unit of the underlying asset". — [Pendle Docs – YT](https://docs.pendle.finance/pendle-v2/ProtocolMechanics/YieldTokenization/YT)
  - PT holders forgo points; LPs keep points on their SY/YT exposure. — [Pendle Academy – Points Trading](https://pendle.gitbook.io/pendle-academy/ecosystem-and-resources/points-trading)
  - An older Pendle Academy page cites "3% YT fees". The current Fees doc says 5%, so use 5%.
- **Evidence that "10x" ≈ 10 Coordinates/$/day (Axis points API, sampled 9 times 2026-09-28 11:50:51–11:59:02 UTC).** — [Axis points leaderboard API](https://api.axis.to/api/v1/points/leaderboard)
  - Several wallets accrue exactly 993,092/day, 1,191,7xx/day, 1,241,3xx/day and 1,986,185/day. These are clean multiples of about 9.93 Coordinates/$/day on round deposits ($100K, $120K, $125K, $200K).
  - Rank-1 wallet 0xBdfB…23d4 accrues about 141.6–142.6M/day. That is consistent with roughly a $14M ogUSDx position at 10x. Its 13.68B total is also consistent with about $14M × 20/$/day through Season 0 plus about 24 days at 10/$/day.
- **Community farming commentary.** Axis pre-deposits became withdrawable Sep 4, 2026 14:00 UTC, with a "7 day cooldown for free withdrawals or 30 bps fee for instant withdrawals". — [coinfoin on X, 2026-09-03](https://x.com/coinfoin_/status/2095495871769219348)
  - Same post: "For yield + points, the $sUSDx LP looks quite attractive. However, if your goal is to maximize points, $USDx LP could be the better option... YT sUSDx... is yield-bearing and could potentially get free points."
  - Pendle-focused commentary described the USDx market as "a pure points play". — [WebSearch summary of Pendle/X coverage](https://x.com/pendle_fi/status/2095738643793207563)

### Inferences
**Per-$10,000 Season 1 accrual** (before referral bonus; Coordinates/day, and cumulative to Dec 3, 2026 ≈ 65.5 days from 2026-09-28 12:00 UTC):

| Position | Coordinates/day | Cumulative to Dec 3 |
|---|---|---|
| ogUSDx vault (10x) | 100,000 | ~6.55M |
| Hold USDx (16x) | 160,000 | ~10.48M |
| Hold sUSDx (4x) | 40,000 | ~2.62M |
| Curve USDx/USDT LP (20x) | 200,000 | ~13.1M |
| Curve USDx/sUSDx LP (10x) | 100,000 | ~6.55M |
| Pendle LP USDx (20x) | 200,000 | ~13.1M |
| Pendle LP sUSDx (5x) | 50,000 | ~3.28M |
| Pendle YT-USDx (24x): $10K buys ≈403,550 YT at $0.02478 | ≈9.20M net of 5% Pendle fee | ≈603M |
| Pendle YT-sUSDx (6x): $10K buys ≈321,160 YT at $0.03114 | ≈1.83M net | ≈120M |

The YT rows are the largest per dollar, which is the standard YT-leverage effect.

**Per-YT, held to maturity (65.5 days, net of 5% fee):**
- **YT-USDx** earns 24 × 65.5 × 0.95 ≈ **1,493 Coordinates**. Price is $0.02478 and USDx has 0% underlying yield, so the cost is **≈$1.66e-5 per Coordinate (≈$16.6 per million)**. This is the market-implied break-even $/point.
- **YT-sUSDx** earns 6 × 65.5 × 0.95 ≈ **373 Coordinates** plus sUSDx yield. At the trailing 21.6% APY, yield is worth ≈0.216 × 65.5/365 × 0.95 ≈ $0.0368 per YT, which is above the $0.0311 price. The points are therefore roughly "free" if the APY holds. If APY drops sharply, the break-even is ≈$8.3e-5/pt treating the whole price as a points cost.

**Opportunity-cost view for non-Pendle routes:**
- Holding USDx (16x) instead of sUSDx (4x) gives up ~21.6% APY for 12 extra Coordinates/$/day. That is about $0.039 per $ over 65.5 days for about 786 extra points, or ≈$4.9e-5/pt.
- YT-USDx is the cheapest points source per dollar, followed by Curve and Pendle LPs.

**Relative weighting.** sUSDx positions carry exactly 1/4 of the equivalent USDx multipliers (4x vs 16x, 6x vs 24x, 5x vs 20x). The program deliberately pays points to unstaked or LP'd USDx and gives little to sUSDx, which already earns yield.

### Gaps
- **"Nx" vs N per $ per day.** Axis has not published that "Nx" equals N Coordinates/$/day in Season 1. This is inferred from leaderboard accrual on vault positions only. The per-unit basis for YT and LP positions is unconfirmed: YT amount vs underlying, and full LP value vs SY portion.
- **Other boosts.** No lock-duration boosts, NFTs/badges or tier systems were found for Season 1. The Jul 22 article hinted that a "Multiplier schedule rewards the capital that arrives first and commits longest", but no duration-based schedule was published.
- **Other integrations.** No Coordinates integrations with Morpho, Euler, Aave, Uniswap or CEXs were found as of 2026-09-28. The Sep 1 article names only the Ecosystem Vault, direct holdings, Curve and Pendle. New integrations with higher multipliers during Season 1 would dilute existing earners.
- **Pendle's live display.** The Pendle app's own points-multiplier display could not be fetched, because the app UI is JS-rendered and the API has no points field.

---

## 3. Total points issued, daily issuance rate, time series, and concentration

### Takeaway
As of **2026-09-28 11:59 UTC**, the public Axis API reports **68.80 billion Coordinates** across **2,325 wallets**. Live issuance measured over an 8.2-minute window is **≈260M Coordinates/day**.

About 93% of that live accrual goes to top-100 wallets, and about 55% to the single rank-1 wallet (a vault position). Distribution is highly concentrated:

| Group | Share of all Coordinates |
|---|---|
| Top 1 | 19.9% |
| Top 10 | 45.6% |
| Top 100 | 88.1% |

66 of the top-100 wallets show zero live accrual. This suggests that Season 1 points from DeFi positions (Pendle, Curve, and possibly wallet holdings) are **not reflected live** in the total and may be credited later. That is a hidden-inflation risk.

### Cited Findings
- **Public endpoint.** `GET https://api.axis.to/api/v1/points/leaderboard` returns `totalWallets`, `totalPoints` and the top 100 addresses (truncated) with points, share and referralCount. Other guessed routes return 403. — [Axis points leaderboard API](https://api.axis.to/api/v1/points/leaderboard)
- **Snapshots** — [Axis points leaderboard API](https://api.axis.to/api/v1/points/leaderboard)

  | UTC timestamp (2026-09-28) | totalPoints | Wallets |
  |---|---|---|
  | 11:50:17 | 68,799,248,467.72 | 2,325 |
  | 11:50:51 | 68,799,347,820.59 | 2,325 |
  | 11:59:02 | 68,800,826,070.94 | 2,325 |
  | 12:01:05 | 68,801,196,386.20 | 2,325 |

  - Rate over the 11 samples from 11:50:51 to 12:01:05 (10.2 minutes): **260.07M/day**. Minute-by-minute rates ranged 258.1M–260.0M/day.
- **Top holders.** — [Axis points leaderboard API](https://api.axis.to/api/v1/points/leaderboard)

  | Rank | Wallet | Coordinates | Share | Live accrual |
  |---|---|---|---|---|
  | 1 | 0xBdfB…23d4 | 13.684B | 19.8–19.9% | ~142M/day |
  | 2 | 0x6b28…bE5b | 2.664B | 3.8% | ~0 |
  | 3 | 0x030f…2a9D | 2.323B | 3.3% | 0 |
  | 4 | 0xC039…ea41 | 2.161B | 3.1% | 0 |
  | 5 | 0x2732…4800 | 2.006B | 2.9% | 0 |

  - Cumulative concentration: top-5 33.2%, top-10 45.6%, top-20 60.8%, top-50 78.8%, top-100 88.1%.
  - Only 34 of the top 100 wallets had any live accrual (>1,000/day). The top 100 together accrued 242.8M/day, about 93% of total live issuance.
- **Scale of Season 0.** Origin closed with $67,248,750 from 1,857 wallets. — [AxisFDN X article, 2026-09-01](https://x.com/AxisFDN/status/2094772784002154737)
  - Wallet count has since risen to 2,325. — [Axis points leaderboard API](https://api.axis.to/api/v1/points/leaderboard)
- **Axis TVL (DefiLlama "Axis" = USDx-based TVL).** — [DefiLlama Axis](https://defillama.com/protocol/axis) / [API](https://api.llama.fi/protocol/axis)

  | Date (2026) | TVL |
  |---|---|
  | Aug 20 | $67.55M |
  | Sep 3 | $67.78M |
  | Sep 4 | $66.28M |
  | Sep 11 | $66.73M |
  | Sep 15 | $60.75M |
  | Sep 17 | $56.32M |
  | Sep 21 | $54.33M (low) |
  | Sep 28 | $56.33M |

  - So there were net outflows of about 17% after the Sep 4 unlock, partly recovering since.
- **axis.to homepage figures (unverified, likely live/stale mix).** TVL $56.4M; Net APY 21.6%; "USDx Supply Snapshot: $26,616,774". — [axis.to](https://www.axis.to/)
  - The last figure conflicts with the on-chain USDx totalSupply of 56.36M on 2026-09-28. It may refer to unstaked supply or be stale.

### Inferences
**Decomposing the 68.8B total (estimate).**
- **Season 0 estimate ≈ 47–56B**, based on these assumptions:
  - First $50M at 20/$/day for ≈36.5 days (Jul 29 14:00 UTC to Sep 4 14:00 UTC, minus average fill time): ≈36.5B.
  - Second ≈$17.25M at 17.5/$/day for ≈33 days: ≈10B.
  - Referral uplift of 0–20%.
- **Season 1 to date (≈23.9 days, Sep 4 14:00 to Sep 28 12:00 UTC)**: the remaining ≈13–22B, i.e. ≈0.5–0.9B/day on average.
  - This is plausible: the vault held about $67M at 10x (≈670M/day) at Season 1 start, falling as users redeemed. The live rate is now 260M/day.
  - Season 0 is roughly 70–80% of all points issued so far.

**Why the live rate likely understates true Season 1 issuance.** Estimated full-rate Season 1 issuance if every eligible position accrued per the multiplier table (using 2026-09-28 supplies):

| Position | Estimated Coordinates/day |
|---|---|
| YT-USDx: 4.36M × 24 | ≈105M |
| YT-sUSDx: 6.09M × 6 | ≈37M |
| Pendle LP USDx: $1.3–2.2M × 20 | ≈25–45M |
| Pendle LP sUSDx: $2.9–6.0M × 5 | ≈14–30M |
| Curve USDx/USDT: $1.7–3.05M × 20 | ≈35–61M |
| Curve sUSDx/USDx: $2.0M × 10 | ≈20M |
| **Pendle + Curve subtotal** | **≈235–300M** |
| Vault (10x) | ≈ the observed 260M |
| Direct USDx (16x) and sUSDx (4x) holdings | tens of millions to ~100M+ |
| **Plausible total** | **≈0.5–0.65B/day** |

The observed live rate is 0.26B/day, and 66/100 top wallets (many of which presumably moved to Pendle/Curve) show zero accrual. The most likely explanation is that off-vault Season 1 Coordinates are computed off-chain and credited later. This is unconfirmed.

**Projection of total Coordinates at the end of Season 1 (Dec 3, 2026 = 65.5 days after the snapshot):**

| Case | Assumption | Total at Dec 3, 2026 |
|---|---|---|
| Low (only live-tracked accrual continues) | 68.8B + 0.26B × 65.5 | ≈ **86B** |
| Base (DeFi positions credited retroactively for all 90 days at ~0.25–0.35B/day extra) | + ≈22–32B | ≈ **108–118B** |
| Bear/dilutive | USDx supply grows (e.g., Ecosystem Vault seeding, new integrations), high-multiplier venues (20–24x) take a bigger share, or a Season 2 is added before TGE | **150B+** |

- **YT-USDx share.** YT-USDx holders collectively would earn ≈4.36M × 1,493 ≈ **6.5B** Coordinates by maturity, about 6–7.5% of the end-S1 total. More if YT supply grows.

### Gaps
- **No historical time series.** There is no public dashboard, Dune query or archived API snapshot. Wayback CDX requests failed with connection resets, so only same-day (2026-09-28) samples exist. Re-sampling the endpoint on later dates would give the true growth rate.
- **What the total includes is unconfirmed:**
  - whether `totalPoints` includes Pendle/Curve/direct-holding Coordinates;
  - whether it includes referral bonuses;
  - how often DeFi positions are credited.
  The docs Q&A found no documented crediting cadence. — [Axis Docs ask endpoint](https://docs.axis.to/readme.md)
- **Top holders unidentified.** The rank-1 holder (0xBdfB…23d4, ~20%) is not identified. It could be an institution, a team-affiliated wallet or a market maker, which matters for "effective float" of the airdrop. Addresses are truncated in the API.
- **No Dune dashboard or community tracker for Coordinates was found.**

---

## 4. Referral mechanics and inflationary bonuses

### Takeaway
- **Referee:** gets a fixed +10% on their own Coordinates, and up to +15% if the referrer shares back up to 5%.
- **Referrer:** earns 10% of referees' eligible Coordinates, minus whatever they share back.
- **Overhead:** total referral issuance is ≈20% of referred users' base points. Referral points are additive and not taken from referees.
- **KOL codes:** at least one KOL advertises a 20% boost, which suggests custom terms.

Referral is therefore a material, up to 20%+, inflation layer on top of base accrual.

### Cited Findings
- **Rules.** "Your referral... earns a fixed 10% bonus on the Coordinates they accrue... If you choose to share part of your reward back to them, they can earn up to 15%. You, the referrer, earn 10% of the eligible Coordinates your referrals accrue while they hold. You can share up to 5% of that back to them, keeping between 5% and 10%." — [AxisFDN X article, 2026-07-27](https://x.com/AxisFDN/status/2081726383240126870)
- **Worked example.** "if someone who joined through you accrues 1,000 Coordinates. If you share the full 5%, they receive an extra 150... and you keep 50... Their own Coordinates are never reduced to pay yours; referral rewards are always additional." — [AxisFDN X article, 2026-07-27](https://x.com/AxisFDN/status/2081726383240126870) (image: [referral graphic](https://pbs.twimg.com/media/HOPFsDYWkAA2bPk.jpg))
- **Lock-in.** "Each person has one referrer locked in at their first deposit, and the terms that apply when someone joins are fixed for them and do not change afterward." Every account gets a referral code automatically. — [AxisFDN X article, 2026-07-27](https://x.com/AxisFDN/status/2081726383240126870)
- **Pre-launch status.** On Jul 22, referral mechanics were "being finalized" (Beacon/Triangulate branding). — [AxisFDN X article, 2026-07-22](https://x.com/AxisFDN/status/2079919958713077866)
- **KOL boost claim.** "you can use my referral link below to activate 20% points boost instead of the regular 10% referral boost". — [coinfoin on X, 2026-09-03](https://x.com/coinfoin_/status/2095495871769219348)
  - This exceeds the official 15% maximum for referees, so KOL codes appear to carry custom terms. Unverified.
- **Referrers on the leaderboard (2026-09-28).** 14 of the top-100 wallets have ≥1 referral. — [Axis points leaderboard API](https://api.axis.to/api/v1/points/leaderboard)
  - 0x4f2d…A104 has **325 referrals** (rank 32, 433M Coordinates).
  - 0x8816…7401 has 28 referrals.
  - 0x9808…ca5B has 27 referrals.

### Inferences
- **Maximum overhead.** Referral overhead on referred users' base accrual is at most ≈20% (10% fixed to referee + 10% split between referrer and referee), or higher under KOL deals.
- **Likely share of total.** If 30–70% of base points come from referred wallets, referral issuance would add ≈6–14% to totals. The share of referred deposits is unknown.
- **Why this matters for valuation.** Referral Coordinates count toward the denominator for any airdrop split. When valuing a YT position, use the network-wide total, which already includes referrals, rather than just base accrual.

### Gaps
- No official statistic exists for the share of Coordinates from referrals, or the number of referred wallets.
- It is unconfirmed whether referral bonuses apply to Season 1 DeFi positions (Pendle YT/LP, Curve). "Eligible Coordinates" is not defined.

---

## 5. Rule changes over time, sybil rules, thresholds, and disclaimers

### Takeaway
There has already been one effective **rate cut**: vault positions went from 20/$/day (Season 0, 2x) to 10/$/day (Season 1, "flat 10x"). At the same time, high multipliers (16–24x) were introduced for unlocked, LP'd or Pendle USDx, shifting points toward liquidity venues.

No sybil policy, minimum threshold, vesting or claim conditions for Coordinates have been published. Official language repeatedly states that there is no entitlement.

### Cited Findings
- **Season 0 → Season 1 cut.** "The pre-deposit boost used during Origin ends with Season 0. From September 4, the vault position moves to a flat 10x multiplier". The rationale: "Origin was about growing USDx supply. Season 1 is about giving that supply more places to go and rewarding the liquidity that makes those markets useful." — [AxisFDN X article, 2026-09-01](https://x.com/AxisFDN/status/2094772784002154737)
- **Ecosystem Vault mandate.** The Ecosystem Vault "will allocate capital into USDx and sUSDx positions, including liquidity on @CurveFinance and capital used to seed @pendle_fi markets". — [AxisFDN X article, 2026-09-01](https://x.com/AxisFDN/status/2094772784002154737)
  - This implies protocol-controlled capital also sits in high-multiplier venues. Whether the vault's Coordinates pass through to ogUSDx holders at 10x or earn venue rates is not stated.
- **Redemption terms after unlock.** Standard redemption takes 7 days and is free, and "continues earning while the request is being processed". Instant redemption costs about 30 bps. — [AxisFDN X article, 2026-09-01](https://x.com/AxisFDN/status/2094772784002154737)
- **No sybil or referral-abuse rules in docs.** The docs contain no published referral rules or sybil-resistance restrictions for Coordinates. There are only product-level eligibility controls (no US persons, sanctions screening, on-chain blacklisting). — [Axis Docs – Eligibility & Onboarding](https://docs.axis.to/resources-and-legal/eligibility-and-onboarding.md); [Axis Docs – Core Contracts](https://docs.axis.to/reference/core-contracts.md)
- **No minimum deposit.** "Is there a minimum deposit size? No, there is no minimum deposit size." — [Axis Docs – Origin Vault](https://docs.axis.to/origin-vault/origin-vault.md)
- **Disclaimer.** "Coordinates are non-transferable, have no monetary value, and confer no entitlement to any token, allocation, or reward. Program terms remain subject to final published rules." — [AxisFDN X article, 2026-07-27](https://x.com/AxisFDN/status/2081726383240126870)

### Inferences
- **Signal from the rate cut.** Halving vault accrual while offering 16–24x elsewhere means the team is willing to re-weight multipliers mid-program. Further changes during Season 1 (new venues or boosted markets) would dilute holders of earlier points.
- **Why dilution risk is high.** Season 1 multipliers are 5–12x the Season 0 "per $ per day" economics for some venues, relative to the post-boost 10/day. With no issuance cap, total issuance scales linearly with USDx deployed in DeFi.
- **Regulatory filter risk.** The US-person exclusion suggests an eventual token distribution may require KYC or geo-filtering. This could either shrink the eligible denominator or add friction and claim-condition risk.

### Gaps
- Sybil filtering, minimum points thresholds for eligibility, airdrop vesting and cliff, and claim windows are all unannounced.
- The treatment of team, insider or market-maker wallets on the leaderboard is unknown.

---

## 6. Community valuation, pre-market pricing, and implied $/point

### Takeaway
No Whales Market points market for AxisFDN exists, and no community $/point estimate was found. The only liquid price signals are:
- **Pendle YT-USDx:** the market implies ≈**$16.6 per million Coordinates**. At 86–118B total Coordinates, that prices the entire Coordinates airdrop at only ≈**$1.4–2.0M**.
- **Polymarket:** ≈**21.5%** probability of an Axis token launch by Dec 31, 2026, with thin volume.

For $/point, apply: $/point = FDV × airdrop% ÷ total points at TGE (matrix below).

### Cited Findings
- **Polymarket event "Will Axis launch a token by ___?"** Created 2026-07-29. It resolves on an official Axis token that is "actively and publicly tradable", with source x.com/AxisFDN, and excludes stablecoins and synthetic tokens. Prices as of 2026-09-28:

  | Market | Yes price | Notes | Volume |
  |---|---|---|---|
  | By Dec 31, 2026 | 0.215 | last 0.20, bid 0.21 / ask 0.22 | ~$6.6K |
  | By Jun 30, 2027 | 0.585 | last 0.44, bid 0.48 / ask 0.69 (thin) | ~$1.1K |
  | By Dec 31, 2027 | 0.615 | last 0.44, bid 0.44 / ask 0.78 (very thin) | ~$1.0K |

  — [Polymarket event](https://polymarket.com/event/will-axis-launch-a-token-by-20260729144519159) (via [Gamma API](https://gamma-api.polymarket.com/public-search?q=axis&limit_per_type=20))
- **Whales Market.** Scanning the token list (442 entries, 2026-09-28) found no AxisFDN / Coordinates pre-market. — [Whales Market API](https://api.whales.market/v2/tokens?keyword=axis)
- **No perp pre-launch venue listings found.** No Hyperliquid or Aevo pre-launch market for Axis was found in searches.
- **Farming guides do not price points.** airdrops.io explicitly provides "No per-point value or total points estimate". — [airdrops.io/axis](https://airdrops.io/axis/)
  - Its tier list rated AxisFDN C tier ("unconfirmed everything"). — [AIRDROPS.IO X article, 2026-08-19](https://x.com/airdrops_io/status/2090032492401095159)
- **Pendle pricing inputs.** YT-USDx price $0.02478, 0% underlying yield, 24x, maturity Dec 3, 2026. YT-sUSDx price $0.03114, 21.6% underlying APY, 6x. — [Pendle API](https://api-v2.pendle.finance/core/v1/1/markets/0x0bef762d2094ac80821c657dea6783fc43435292); [Pendle API](https://api-v2.pendle.finance/core/v1/1/markets/0x5e572498e9f83650f0ff24194999bddb4b390928)

### Inferences
**Market-implied $/point from YT-USDx.** $0.02478 ÷ (24 × 65.5 days × 0.95) ≈ **$1.66e-5 per Coordinate** ($16.6/M).
- Multiplied by the projected end-of-Season-1 supply, the market values the whole Coordinates pool at:
  - ≈$1.43M at 86B points;
  - ≈$1.82M at 110B;
  - ≈$2.49M at 150B.
- Implied FDV at a 5% airdrop allocation:
  - ≈$28.5M at 86B points;
  - ≈$36.5M at 110B;
  - ≈$49.8M at 150B.
- At a 2% allocation, the implied FDV at 86B points is ≈$71M.

**Interpretation.** The YT market prices in a heavy discount for:
- no token (Polymarket ~21.5% by end-2026, ~60% by end-2027);
- long time-to-TGE;
- dilution;
- possible exclusion of Pendle positions or sybil filtering.

It is also illiquid: YT-USDx pool $2.24M liquidity, ~$19K daily volume.

**Scenario matrix: $ per 1 million Coordinates** (= FDV × allocation ÷ total points × 1e6):

| FDV | Alloc 2% @86B | 5% @86B | 10% @86B | 2% @110B | 5% @110B | 10% @110B | 2% @150B | 5% @150B | 10% @150B |
|---|---|---|---|---|---|---|---|---|---|
| $50M | $11.6 | $29.1 | $58.1 | $9.1 | $22.7 | $45.5 | $6.7 | $16.7 | $33.3 |
| $100M | $23.3 | $58.1 | $116.3 | $18.2 | $45.5 | $90.9 | $13.3 | $33.3 | $66.7 |
| $250M | $58.1 | $145.3 | $290.7 | $45.5 | $113.6 | $227.3 | $33.3 | $83.3 | $166.7 |
| $500M | $116.3 | $290.7 | $581.4 | $90.9 | $227.3 | $454.5 | $66.7 | $166.7 | $333.3 |
| $1B | $232.6 | $581.4 | $1,162.8 | $181.8 | $454.5 | $909.1 | $133.3 | $333.3 | $666.7 |

**YT-USDx break-even (ignoring token-existence probability and time value):** $16.6/M. That break-even is reached, for example, at:
- FDV $50M with 3% allocation at 86B points;
- FDV $100M with ≈1.8% allocation at 110B;
- FDV $250M with 1% allocation at 150B.

Adjust for token probability as expected value = P(token by TGE) × value. For example, at 60% probability the break-even value needed is ≈$27.7/M.

**Worked example.** $10,000 of YT-USDx bought 2026-09-28 earns ≈603M net Coordinates by Dec 3. That is ≈0.70% of an 86B total, or ≈0.51% of 118B. Payoff:
- ≈$17.5K–35K if FDV is $100M with a 5% allocation, depending on the denominator;
- $0 if no token, or if the conversion excludes or discounts Pendle positions.

**Bearish/dilution flags for the report writer:**
1. No token or allocation is confirmed, and the official text says "no entitlement".
2. About 70–80% of points already sit with Season 0 depositors, and the top-10 wallets hold ~46%.
3. Off-vault Season 1 accrual appears not yet reflected in the public total. The true denominator is likely 25–40% higher than the live figure implies by Dec 3.
4. Issuance has no cap and scales with USDx deployed at 16–24x.
5. Multipliers have already been re-weighted once, and Season 2 or token-sale sequencing could extend the farm.
6. Referral overhead of up to ~20%+, with KOL codes possibly higher.
7. Pendle takes a 5% fee on YT points.
8. US persons are excluded, so eligibility filtering is possible.

### Gaps
- No community X threads, Telegram alpha posts, Medium or Substack pieces were found that estimate $/Coordinate or project total points. Searches returned only generic Pendle and airdrop content, plus Axis Robotics noise.
- No Whales Market, Hyperliquid pre-launch or Aevo market exists as of 2026-09-28, so there is no direct secondary price for Coordinates.
- Polymarket volumes are tiny ($1–7K per market), so its probabilities are weak signals.
- The official AxisFDN Discord could not be located or accessed. The Telegram channel (t.me/AxisFDN) only reposts X links; its latest post is 2026-09-01. — [Telegram preview](https://t.me/s/AxisFDN)
