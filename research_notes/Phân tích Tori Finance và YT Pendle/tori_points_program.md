# Tori Finance Points Program ("Cores"): Rates, Multipliers, Pendle YT Treatment, Supply of Points, and Token Conversion (as of 2026-09-28)

Research date: 2026-09-28 (all live figures pulled 2026-09-28 ~11:40-11:55 UTC unless stated otherwise).
How the data was gathered: official docs (docs.tori.finance, a Mintlify site that serves `.md` versions of each page), the Tori app's public JSON endpoints (`app.tori.finance/api/...`), the app's shipped JavaScript bundle (it contains the venue/multiplier config), Pendle's public API, on-chain `totalSupply`/`balanceOf` reads over a public Ethereum RPC, Ethplorer top holders, Morpho's API, and DefiLlama. The official X account (x.com/tori_finance) could not be read (login wall, mirrors blocked or returning 451/429). The Telegram handle `t.me/tori_finance` is NOT official: it is a squatted username that is listed for sale.

Terminology: "Nx" in Tori's app means **N Cores per $1 (or per 1 unit of the underlying) per day**. See the evidence in Q1.

---

## Q1. What are the exact point rates and multipliers per activity, especially for Pendle YT? Are they per $1 of underlying per day?

### Takeaway
The program is called **Cores**. Tori's app ships a per-venue "Cores multiplier" table, published at mainnet launch on Jul 27, 2026 and still live on 2026-09-28. Each "Nx" means N Cores per $1 per day. Key rates: **hold trUSD 25x, strUSD 5x, Ecosystem Vault (etrUSD) 35x, Pendle YT-trUSD 30x per YT, locked YT-trUSD 45x, Pendle LP-trUSD 45x on the SY portion only, YT-strUSD 6x, PT 0x.** Pendle's own points API confirms the YT and LP numbers as "points-per-asset" (Cores per 1 YT, meaning per 1 unit of underlying notional, per day). Pendle's docs say it takes 5% of all YT yield **including points**, and that the partner protocol deducts that fee when it allocates points. Neither Tori nor Pendle says whether the 30x figure is before or after that 5%.

### Cited Findings

**Official docs (base program)**
- Cores are "points you earn for contributing to the growth of the protocol… by holding trUSD, staking strUSD, and participating in integrated DeFi protocols." — [Tori Docs: Cores](https://docs.tori.finance/resources/cores)
- "Emission rates are set per season. During Season 1's pre-deposit phase, the rate was 30 Cores per dollar per day." "During the pre-deposit phase, Cores earned a 2x boost, the highest planned for the program. The phase has ended." — [Tori Docs: Cores](https://docs.tori.finance/resources/cores) (page lastmod 2026-08-25 per [sitemap](https://docs.tori.finance/sitemap.xml))
- Pre-deposit vault table: cap $50M; USDC/USDT; Ethereum; LP token etrUSD; fees waived; "Cores: 2x boost, 30 Cores per dollar per day"; 30-day hard lock-up. After the phase it became the Ecosystem Vault with a soft lock-up and a 7-day withdrawal period. — [Tori Docs: Pre-Deposit Vault](https://docs.tori.finance/resources/pre-deposit)
- Referral: "you receive 10% of the Cores they earn. They keep all of their Cores, and you get a bonus on top." There is no cap. — [Tori Docs: Referral](https://docs.tori.finance/resources/referral); [Tori Docs: Cores](https://docs.tori.finance/resources/cores)
- FAQ: "During Season 1's pre-deposit phase, the rate was 30 Cores per dollar per day." — [Tori Docs: General FAQ](https://docs.tori.finance/faq/general)
- **Conflict or ambiguity about the pre-deposit rate.** Third-party guides read the docs as "30 per dollar per day, doubled during pre-deposit", i.e. an effective **60**/$/day ([usethebitcoin, updated Jul 2, 2026](https://usethebitcoin.com/airdrop/tori-finance/); [airdrops.io, updated Jul 24, 2026](https://airdrops.io/tori-finance/)). The official pre-deposit table says "2x boost, 30 Cores per dollar per day", which reads as **30 including the 2x** ([Tori Docs](https://docs.tori.finance/resources/pre-deposit)). See the Q3 inferences: the total points on the leaderboard fit 30/day effective much better than 60/day.

**Live per-venue multiplier table.** Source: the Tori app's DeFi page config, field `rewards_multiplier`, extracted from the app JS bundle [app.tori.finance/_next/static/immutable/chunks/2k0jyeo_ewi3n.js](https://app.tori.finance/_next/static/immutable/chunks/2k0jyeo_ewi3n.js) that serves [app.tori.finance/defi](https://app.tori.finance/defi). The app's UI text describes the column as "Cores multipliers: Tori points, per dollar deployed". An earlier note in the same UI said "Cores multipliers are illustrative until the table publishes Jul 27" ([app.tori.finance/defi](https://app.tori.finance/defi)). Values as of 2026-09-28:

| Activity (app slug) | Cores multiplier (Cores per $ per day) | Notes from app text |
|---|---|---|
| Stake trUSD → strUSD (`stake-strusd`) | **5x** | "5x cores while you hold" |
| Hold trUSD (`hold-trusd`) | **25x** | "No rewards yet, Cores accrue while you decide" (trUSD itself pays no yield) |
| Tori Ecosystem Vault, Upshift/etrUSD, ex-pre-deposit (`tori-ecosystem-vault`) | **35x** | "The pre-deposit vault, now deploying across Tori strategies and DeFi" |
| Monad Tori ecosystem vault (AUSD, Accountable) | 15x | |
| RockawayX Morpho USDC vault (`rockawayx-tori-vault`) | 10x | Lend USDC |
| Morpho lend USDC into strUSD/trUSD/etrUSD/PT-strUSD/PT-trUSD markets | 10x each | |
| Morpho strUSD collateral (borrow USDC) / Spiral loop / Tenor borrow | 5x | Spiral: "Cores accrue to the proxy Spiral opens for you" |
| Morpho trUSD collateral | 25x | |
| Morpho etrUSD collateral | 35x | |
| Morpho PT-strUSD or PT-trUSD collateral | **0x** | "No Cores on PT" |
| Tenor lend USDC (fixed rate vs strUSD) | 10x | |
| Curve trUSD/USDC, Fluid trUSD/USDC, Curve frxUSD/trUSD (+ Convex / Stake DAO / Beefy wrappers) | 30x | Beefy: "Same points as holding the LP" |
| Curve strUSD/trUSD (+ Convex / Stake DAO) | 15x | |
| **Pendle YT-trUSD (26 Nov 2026)** | **30x** | "Cores on your YT balance" |
| **Pendle LP trUSD** | **45x** | "Cores accrue on the SY portion of your Pendle LP only" |
| **Locked YT-trUSD (Tori "YT Lock")** | **45x** | "Lock Pendle YT-trUSD for boosted Cores" |
| Pendle YT-strUSD (26 Nov 2026) | 6x | "Cores on your YT balance" |
| Pendle LP strUSD | 9x | SY portion only |
| Locked YT-strUSD | 9x | |
| Royco senior / junior strUSD tranches | 5x each | |
| Monad: Morpho lend AUSD 10x; strUSD collateral 5x; SharpByte AUSD vault 10x | | |

**Pendle-side confirmation (per YT, per day).** Pendle's points API lists, for the trUSD market `0xfcf009cb…c947`, `{key: "Cores", type: "points-per-asset", pendleAsset: "basic", value: 30}` and `{pendleAsset: "lp", value: 45, perDollarLp: false}`. For the strUSD market `0xac0283…eaddb` it lists basic 6 and lp 9. — [Pendle API points-market](https://api-v2.pendle.finance/core/v1/markets/points-market?chainId=1)
- On Pendle, trUSD's `pyUnit` is "trUSD on Tori" with `ptEqualsPyUnit: true`. 1 YT therefore represents 1 trUSD of underlying notional, so **YT-trUSD earns 30 Cores per YT per day**, which is the full underlying-notional rate. — [Pendle API market trUSD](https://api-v2.pendle.finance/core/v1/1/markets/0xfcf009cb3135da12a6eb1f73f3ee05392a7bc947)
- YT-trUSD gets **more** Cores per unit (30) than holding the underlying (25). Relative to the underlying rate: YT = 1.2x, LP-SY = 1.8x, locked YT = 1.8x. The strUSD venues follow the same pattern (5 → 6 → 9 → 9). — derived from the [app bundle](https://app.tori.finance/_next/static/immutable/chunks/2k0jyeo_ewi3n.js) and the [Pendle API](https://api-v2.pendle.finance/core/v1/markets/points-market?chainId=1)
- **YT Lock mechanics** (from app UI strings): "Lock Pendle YT-trUSD for boosted Cores"; "**Once locked, YT cannot be withdrawn.**" Locked holders keep a "Claimable Yield" function that syncs yield from Pendle. The lock tokens are `lYT-trUSD` (0x10b2487173d9f7087c8bdce9e70fd135212a8d7d) and `lYT-strUSD` (0x6569c554cbf71dfcc32aec48b0edd2582f5c4a96). — [app.tori.finance (activities page strings)](https://app.tori.finance/activities); on-chain symbols read via RPC, see [Etherscan lYT-trUSD](https://etherscan.io/token/0x10b2487173d9f7087c8bdce9e70fd135212a8d7d)
- **Pendle fee on points:** "Pendle collects a 5% fee from all yield accrued (including points) by all YT… Since points are tracked off-chain, partner protocols deduct the 5% fee when allocating points to user wallets." — [Pendle Docs: Fees](https://docs.pendle.finance/pendle-v2/ProtocolMechanics/Mechanisms/Fees). Some secondary sources cite 3% instead ([search summary of Pendle docs/vePENDLE pages](https://docs.pendle.finance/ProtocolMechanics/Mechanisms/vePENDLE)). The current Fees page says 5%.
- Pendle states it "does NOT give nor generate additional points" for YT leverage. It streams the underlying's points to YT holders. — [Pendle Docs (points trading)](https://pendle.gitbook.io/pendle-academy/ecosystem-and-resources/points-trading)

**Other boosts in the app**
- The Activities page has "Wallet Boost" and rule-based boosts ("Hold X+ …", "Campaign Boost", "{source} Boost") and a named boost `b5` = "Pre-Deposit Boost". The mock data in the bundle shows the structure (multipliers such as 1.1x, 1.15x, 1.2x, 1.5x). That data is **placeholder**, not live. — [app bundle chunk 2nm0z435-x6e1.js](https://app.tori.finance/_next/static/immutable/chunks/2nm0z435-x6e1.js); [app.tori.finance/activities](https://app.tori.finance/activities)
- The app supports linking an X account and has "Private invitation" and "Country of residence" sign-in flows. These are possible inputs to eligibility or boosts; no rules are published. — [app.tori.finance/activities](https://app.tori.finance/activities)

### Inferences
- **Formula for points per day:** Cores/day = Σ (position USD or underlying units × venue multiplier) × (any wallet/rule boost) + 10% of referees' Cores for the referrer.
- **Pendle YT-trUSD:** Cores/day = 30 × (number of YT-trUSD). If Tori applies Pendle's 5% fee it is 28.5. Locked YT: 45 (or 42.75 after the fee). The multiplier is on the full underlying notional, not on the dollars spent.
- **Pendle LP:** Cores/day = 45 × (your share of the pool's SY). On 2026-09-28 the trUSD pool held 2.064M SY out of $2.573M of liquidity (about 80% SY), so the effective rate is about **36 Cores per $1 of LP per day**. For the strUSD pool (5.378M SY, about $5.52M, out of $7.20M) it is about **6.7-6.9 Cores per $1 of LP per day**. Pool figures: [Pendle API trUSD](https://api-v2.pendle.finance/core/v1/1/markets/0xfcf009cb3135da12a6eb1f73f3ee05392a7bc947), [Pendle API strUSD](https://api-v2.pendle.finance/core/v1/1/markets/0xac028348c46d3455899a2b9b50077c11960eaddb)
- **Worked example with the YT-trUSD price on 2026-09-28** ($0.013730/YT; 58.5 days to the 26 Nov 2026 maturity; trUSD underlying APY = 0, so YT-trUSD is essentially a pure Cores instrument):
  - $1 of YT buys about 72.8 YT, which earns about **2,185 Cores/day** (2,076 after a 5% fee).
  - Locked YT: about **3,277 Cores/day per $1** (3,114 after the fee). Locking is irreversible.
  - Cores per YT to maturity: 1,755 (30x) or 2,633 (45x locked).
  - Market-implied price: about **$7.8 per 1M Cores** (unlocked YT, gross) or about $5.2 per 1M Cores (locked).
  - For comparison, holding $1 of trUSD earns 25 Cores/day and the Ecosystem Vault earns 35 Cores/day.
- **YT-strUSD** ($0.017173) earns only 6 Cores/day/YT, about **349 Cores/day per $1**. Most of its price reflects the strUSD yield (about 11.2% underlying APY, worth roughly $0.0179/YT to maturity before the fee).
- **Cross-check on the value of a Core.** RockawayX's vault disclosure put Phase-1 "Points APY" at 8.73% ([RockawayX](https://www.rockawayx.com/insights/rockawayx-tori-ecosystem-vault-investment-thesis-risk-disclosure)). At 30 Cores/$/day that implies about **$7.97 per 1M Cores**, almost identical to the YT-implied $7.8/1M. At 60/day it would imply $3.99/1M. This is another hint that 30/day was the effective pre-deposit rate.

### Gaps
- Tori has not said whether the 30x/45x Pendle figures are gross or net of Pendle's 5% points fee.
- There is no official documentation of the YT Lock contract: lock duration, whether lYT is transferable, or what happens at the 26 Nov 2026 maturity. The only evidence is the UI string "Once locked, YT cannot be withdrawn."
- For LPs on Curve, Fluid and Convex, it is unclear whether the multiplier applies to the whole LP dollar value or only the trUSD/strUSD leg.
- The rules and sizes of live wallet/rule boosts are not public. The only examples in the bundle are placeholders.
- The pre-deposit rate is ambiguous: 30/day effective or 60/day. Official wording is ambiguous; aggregators say 60.

---

## Q2. When did the program start, what season is running now, and when does it end?

### Takeaway
**Season 1 started June 23, 2026** with the pre-deposit vault. As of 2026-09-28, **Season 1 is still the current (and only) season**. The pre-deposit phase is over: the vault filled to $50M in about 7 days, mainnet and the multiplier table launched Jul 27, 2026, and the vault became the Ecosystem Vault. **No official Season 1 end date, Season 2 announcement, or TGE date has been published.**

### Cited Findings
- "Season 1 began June 23, 2026 with the pre-deposit phase… That phase is complete: the vault has converted to the Ecosystem Vault." — [Tori Docs: Cores](https://docs.tori.finance/resources/cores)
- The pre-deposit vault filled $50M in 7 days; the press release is dated July 27, 2026. — [The Defiant (press release)](https://thedefiant.io/news/press-releases/tori-brings-institutional-trades-on-chain-fills-50m-before-launch)
- The app's DeFi page says multipliers were "illustrative until the table publishes Jul 27"; the Pendle PT card said "Opens Jul 27." — [app.tori.finance/defi](https://app.tori.finance/defi)
- Pendle markets for trUSD and strUSD were created around 2026-07-19 per the market `timestamp` field, and both mature **26 Nov 2026**. — [Pendle API trUSD](https://api-v2.pendle.finance/core/v1/1/markets/0xfcf009cb3135da12a6eb1f73f3ee05392a7bc947), [Pendle API strUSD](https://api-v2.pendle.finance/core/v1/1/markets/0xac028348c46d3455899a2b9b50077c11960eaddb)
- RockawayX's vault document describes Phase 1 as a target of about 30 days with about a $50M cap, and a Phase 2 transition threshold of "$25M (of $50M cap)". Phase 2 allocations are indicative: strUSD-trUSD Curve LP 32.5%, trUSD-USDC Curve LP 27.5%, strUSD Pendle LP 20%, trUSD Pendle LP 20%. — [RockawayX](https://www.rockawayx.com/insights/rockawayx-tori-ecosystem-vault-investment-thesis-risk-disclosure)
- The FAQ says "future seasons will define how the protocol recognizes" Cores, which implies more seasons are planned but gives no dates. — [Tori Docs: General FAQ](https://docs.tori.finance/faq/general)
- Third-party trackers agree: "Tori has not announced a token or a TGE date." — [usethebitcoin](https://usethebitcoin.com/airdrop/tori-finance/); [airdrops.io](https://airdrops.io/tori-finance/); [AirdropAlert](https://airdropalert.com/airdrops/tori-finance/)

### Inferences
- The only hard date inside the points system is the **Pendle maturity on 26 Nov 2026**. The YT/LP Cores streams end there unless new maturities are listed. The market may treat it as a natural checkpoint, but nothing links it officially to the end of Season 1.
- Season 1 has run about 97.5 days as of 2026-09-28.

### Gaps
- No official or credibly sourced rumored end date for Season 1 was found. The X account could not be read, so any announcements made only on X may be missed.

---

## Q3. How many Cores have been issued so far, and what is the current daily issuance?

### Takeaway
The app's public leaderboard API reports **157,501,782,271.6 Cores (about 157.5B) across 6,467 wallets as of 2026-09-28 ~11:44 UTC**. The lifetime average is about **1.62B Cores/day**. No public figure for daily issuance exists. A bottom-up estimate from on-chain venue sizes × multipliers gives about **2.0-2.5B Cores/day currently** (about 2.43B/day before double-count adjustments). Holdings are highly concentrated: top 10 wallets hold 34%, top 100 hold 62%.

### Cited Findings

**Official leaderboard.** Public, no auth: `GET https://app.tori.finance/api/leaderboard`. It returns the top 100 plus `totalWallets` and `totalPoints`; `?address=0x…` adds `myRank/myPoints/myPercentile`. Pagination parameters are ignored. — [Tori leaderboard API](https://app.tori.finance/api/leaderboard)
- 2026-09-28 11:44 UTC: `totalPoints` = 157,501,782,271.602; `totalWallets` = 6,467. — [Tori leaderboard API](https://app.tori.finance/api/leaderboard)
- Top wallets:

  | Rank | Wallet | Cores | Share |
  |---|---|---|---|
  | 1 | 0x2e3dc205… | 16.92B | 10.7% |
  | 2 | 0xfecfc331… | 10.20B | 6.5% |
  | 3 | 0xd93e7ab3… | 5.71B | 3.6% |
  | 4 | 0x0068b5d7… | 3.96B | 2.5% |
  | 5 | 0x645e0dbd… | 3.88B | 2.5% |
  | 100 | — | 114.3M | — |

  — [Tori leaderboard API](https://app.tori.finance/api/leaderboard)
- Cumulative share of total Cores (computed from the API): top 1 = 10.74%, top 3 = 20.84%, top 5 = 25.82%, top 10 = 34.04%, top 20 = 44.83%, top 50 = 56.10%, top 100 = 62.38%. The other ~6,367 wallets share about 37.6%. — [Tori leaderboard API](https://app.tori.finance/api/leaderboard)
- Referral counts in the top 100 are small. The largest is 75 (rank 94); others are 28, 24 and 15. — [Tori leaderboard API](https://app.tori.finance/api/leaderboard)
- The leaderboard total did not change across polls between 11:46 and 11:52 UTC. It is a periodic snapshot, not real-time. The front end interpolates a user's own balance with `pointsPerSecond` from an authenticated endpoint (`/api/points/rewards` returns 401 without a session). — [app bundle 2n8jy38tg1jyz.js](https://app.tori.finance/_next/static/immutable/chunks/2n8jy38tg1jyz.js)
- The top wallet (rank 1, an EOA) currently holds 4.95M strUSD directly (10.8% of strUSD supply). — [Ethplorer top holders strUSD](https://api.ethplorer.io/getTopTokenHolders/0x280839980a7ed0d7717f64125fe241012e5f5815?apiKey=freekey&limit=25)
- EOA 0xa8a697…a60e holds 5.05M trUSD, 6.34M strUSD and 531.7k YT-trUSD (15% of YT-trUSD supply) but is **not** in the top 100. This suggests protocol/vault wallets are excluded from Cores. — [Ethplorer trUSD holders](https://api.ethplorer.io/getTopTokenHolders/0xd0580192e98ea6ceb9c7b6191ed2e27560911697?apiKey=freekey&limit=25); [Ethplorer YT-trUSD holders](https://api.ethplorer.io/getTopTokenHolders/0x1fcdb1e747419bb8d1a029c4d1f83b41e8afe8ce?apiKey=freekey&limit=10); [Tori leaderboard API](https://app.tori.finance/api/leaderboard)
- **YT holder distribution (2026-09-28):**
  - YT-trUSD: 54.3% sits in the YT Lock contract (1.924M). 0xa8a697 holds 15.0%. 0x6b28fb12… holds 499.5k (14.1%) and is leaderboard rank 28 with 0.816B Cores.
  - Largest lYT-trUSD lockers: 0x3b561a4e… 301.7k (15.7%, rank 30, 0.67B Cores); 0x649c037b… 165.5k (rank 51); 0x32d820c6… 131.3k (rank 61). At 45x the largest locker earns about 13.6M Cores/day.

  — [Ethplorer lYT-trUSD holders](https://api.ethplorer.io/getTopTokenHolders/0x10b2487173d9f7087c8bdce9e70fd135212a8d7d?apiKey=freekey&limit=10); [Tori leaderboard API](https://app.tori.finance/api/leaderboard)

**Inputs for a bottom-up estimate of daily issuance (all on 2026-09-28)**
- **Supplies:**
  - trUSD: 75.19M
  - strUSD: 45.88M, at a share price of 1.026297 (≈$47.09M)
  - YT-trUSD: 3,544,668; of which locked (lYT-trUSD): 1,923,817 (54%)
  - YT-strUSD: 3,419,921; of which locked (lYT-strUSD): 566,103 (16.6%)
  - SY-trUSD: 5.609M
  - SY-strUSD: 8.722M

  Read on-chain via `totalSupply`: [trUSD](https://etherscan.io/token/0xd0580192E98eA6CEB9c7b6191Ed2E27560911697), [strUSD](https://etherscan.io/token/0x280839980a7eD0D7717F64125fE241012E5F5815), [YT-trUSD](https://etherscan.io/token/0x1fcdb1e747419bb8d1a029c4d1f83b41e8afe8ce), [lYT-trUSD](https://etherscan.io/token/0x10b2487173d9f7087c8bdce9e70fd135212a8d7d); share price from [Tori /api/apy](https://app.tori.finance/api/apy)
- **Ecosystem Vault (etrUSD):**
  - totalAssets 44,652,682 against a deposit cap of 75,000,000
  - 7-day withdrawal lag
  - apy7d 5.96%

  — [Tori /api/vault/info](https://app.tori.finance/api/vault/info)
- **Proof of reserves:** reserves $75.32M vs supply 74.89M (100.58% collateralized). — [Tori /api/solvency](https://app.tori.finance/api/solvency)
- **Pendle pools:**
  - trUSD: liquidity $2.57M (SY 2.064M, PT 0.516M)
  - strUSD: liquidity $7.20M (SY 5.378M, PT 1.711M)
  - Implied APY: 9.01% (trUSD) and 11.41% (strUSD)
  - YT price: $0.013730 (YT-trUSD) and $0.017173 (YT-strUSD)

  — [Pendle API trUSD](https://api-v2.pendle.finance/core/v1/1/markets/0xfcf009cb3135da12a6eb1f73f3ee05392a7bc947), [Pendle API strUSD](https://api-v2.pendle.finance/core/v1/1/markets/0xac028348c46d3455899a2b9b50077c11960eaddb)
- **Morpho (Ethereum):**
  - strUSD/USDC market: supply $13.39M, borrow $12.10M, collateral $15.96M
  - PT-trUSD/USDC: supply $2.55M
  - PT-strUSD/USDC: supply $0.68M

  — [Morpho API](https://blue-api.morpho.org/graphql)
- **Other large strUSD holders:** Morpho Blue 15.55M; SY-strUSD 8.72M; CCIP token pool (bridged to Monad/Pharos) 6.15M; Curve strUSD/trUSD pool 2.04M. — [Ethplorer strUSD holders](https://api.ethplorer.io/getTopTokenHolders/0x280839980a7ed0d7717f64125fe241012e5f5815?apiKey=freekey&limit=25)
- **Other large trUSD holders:**
  - strUSD contract 47.09M
  - trUSD Silo (unstake cooldown) 10.77M
  - SY-trUSD 5.61M
  - Fluid liquidity layer 2.40M
  - Curve str/trUSD 1.985M
  - Curve frxUSD/trUSD 1.138M (plus 1.921M frxUSD)
  - The Curve trUSD/USDC pool is negligible (about $2k)

  — [Ethplorer trUSD holders](https://api.ethplorer.io/getTopTokenHolders/0xd0580192e98ea6ceb9c7b6191ed2e27560911697?apiKey=freekey&limit=25)
- **DefiLlama TVL history:** 2026-07-01 $49.87M; 07-22 $50.11M; 08-01 $54.8M; 08-15 $63.93M; 09-01 $66.23M; 09-15 $67.82M; 09-28 $73.06M. — [DefiLlama Tori Finance](https://defillama.com/protocol/tori-finance)

### Inferences
- **Bottom-up current issuance** (venue size × multiplier, in Cores/day). All inputs are from the Q3 findings above.

  | Venue | Size × multiplier | Cores/day |
  |---|---|---|
  | Ecosystem Vault | $44.65M × 35 | 1,563M |
  | Morpho USDC lenders | $16.6M × 10 | 166M |
  | Morpho strUSD collateral | $15.96M × 5 | 80M |
  | Pendle trUSD: YT unlocked | 1.62M × 30 | 48.6M |
  | Pendle trUSD: YT locked | 1.92M × 45 | 86.6M |
  | Pendle trUSD: LP SY | 2.06M × 45 | 92.9M |
  | Pendle trUSD subtotal | | ≈228M |
  | Pendle strUSD (YT 17.1M + lYT 5.1M + LP 48.4M) | | ≈71M |
  | Curve strUSD/trUSD | $4.08M × 15 | 61M |
  | Curve frxUSD/trUSD | $3.06M × 30 | 92M |
  | Fluid trUSD/USDC | ~$2.73M × 30 | 82M |
  | Direct strUSD holders | ~$7.3M × 5 | 36M |
  | Direct trUSD holders | ~$0.4M × 25 | 9M |
  | Bridged strUSD on Monad/Pharos | ~$6.3M × ~6.5 | 41M |
  | **Total** | | **≈2.43B/day** |

  - Referral bonuses add up to +10% of referred users' Cores; the realistic uplift is probably a few percent.
  - Because the Ecosystem Vault deploys into Curve and Pendle LPs, some LP Cores probably overlap with vault Cores. If vault-owned positions are excluded, as the absence of 0xa8a697 from the leaderboard suggests, the true figure is lower.
  - The 0xa8a697 wallet, which appears to be excluded, holds 531.7k unlocked YT-trUSD. That removes about 16M/day from the Pendle line.
  - **Working estimate: about 2.0-2.5B Cores/day (central ~2.2B/day) as of late Sep 2026.**
- **Historical consistency check (supports 30/day effective in pre-deposit):**
  - Pre-deposit, about Jun 23 to Jul 27: ~$50M × 30 × ~30-34 days ≈ 45-51B.
  - The remaining ~106-112B over the ~63 days after launch averages about 1.7B/day, which is consistent with TVL rising from $50M to $73M.
  - If pre-deposit had paid 60/day (≈90-102B), the post-launch average would be only about 0.9-1.1B/day. That is below what the 35x vault alone would emit (~1.56-1.75B/day). The 60/day reading is therefore hard to reconcile with the leaderboard total.
- **Projection of total Cores outstanding** (157.5B on 2026-09-28 + rate × days):

  | Assumed rate | By 26 Nov 2026 (+58.5 d, Pendle maturity) | By 31 Dec 2026 | By 31 Mar 2027 |
  |---|---|---|---|
  | 1.8B/day | ≈263B | ≈326B | ≈488B |
  | 2.1B/day | ≈280B | ≈354B | ≈543B |
  | 2.4B/day | ≈298B | ≈382B | ≈598B |
  | 2.7B/day | ≈315B | ≈410B | ≈653B |

  These assume TVL and multipliers stay constant. Growth in TVL or new high-multiplier venues would push the numbers up.
- **Share of a position.** At about 2.2B/day, $1M in the Ecosystem Vault (35M/day) is about 1.6% of daily issuance. 1M YT-trUSD (30M/day, costing about $13.7k on 2026-09-28) is about 1.4% of daily issuance.

### Gaps
- No official number for daily issuance, and no historical time series (no Dune dashboard found; the Wayback Machine was blocked from this environment). The leaderboard did not update during the ~6-minute polling window observed before these notes were written, so a direct delta measurement was not possible.
- Whether vault, protocol, Pendle and Morpho contract addresses are excluded from the Cores total is not documented. It is inferred only from the absence of 0xa8a697 from the leaderboard.
- The multiplier table that applied between Jul 23 and Jul 27 (vault conversion to launch), and any mid-season changes, are not documented.

---

## Q4. Has Tori disclosed what % of token supply goes to Cores holders, and are there hints about TGE timing?

### Takeaway
**No.** Tori explicitly says Cores "are not a promise of any token or payment". It has published no token, no TGE date, no % allocation, no conversion rate, and no vesting or claim mechanics. The only hint is that "future seasons will define how the protocol recognizes" Cores.

### Cited Findings
- "Cores represent your contribution to Tori. As the protocol evolves, they will factor into how early supporters are recognized. The form that takes has not been decided, and Cores are not a promise of any token or payment." — [Tori Docs: Cores](https://docs.tori.finance/resources/cores)
- "What will Cores be used for? That has not been announced yet. Cores record your contribution, and future seasons will define how the protocol recognizes it. They are not a promise of any token or payment." — [Tori Docs: General FAQ](https://docs.tori.finance/faq/general)
- Aggregators say: "Token confirmed: No"; "allocation formula remains unannounced"; "TGE date: Not announced." — [usethebitcoin](https://usethebitcoin.com/airdrop/tori-finance/); [airdrops.io](https://airdrops.io/tori-finance/); [AirdropAlert](https://airdropalert.com/airdrops/tori-finance/)
- Funding: seed round in March 2026 led by Delphi Ventures, with ScaleX Ventures and QInvest; amount undisclosed. — [usethebitcoin](https://usethebitcoin.com/airdrop/tori-finance/); [The Defiant](https://thedefiant.io/news/press-releases/tori-brings-institutional-trades-on-chain-fills-50m-before-launch)
- The Terms of Service reserve the Company's "absolute right, in its sole and unfettered discretion" to modify, limit or terminate access, and prohibit bots and automation. These are general clauses, not points-specific. — [Tori Docs: Terms](https://docs.tori.finance/legal/terms)
- Eligibility: users attest they are 18 or older and not a Restricted Person or in a Prohibited Jurisdiction. The app collects "Country of residence" and a signed agreement at sign-in. — [AirdropAlert](https://airdropalert.com/airdrops/tori-finance/); [app.tori.finance/activities](https://app.tori.finance/activities)

### Inferences
- Any % of supply for Season 1 must be an assumption, for example taken from comparable synthetic-dollar or points programs; nothing official exists.
- **Market-implied value of Cores:** YT-trUSD prices Cores at about $7.8 per 1M (Q1). At ~280-300B Cores by 26 Nov 2026, the market implicitly values all Season 1 Cores at only about **$2.2-2.3M**. That suggests either heavy skepticism, or that YT buyers price in a large discount for token risk and the possible 5% fee. Treat this as an inference, not an official figure.
- Geo-restriction and sign-in or KYC-like flows (country, agreement signature) suggest distribution eligibility could be restricted by jurisdiction.

### Gaps
- No official or credible leaked tokenomics, airdrop % or vesting schedule.
- No explicit anti-sybil policy for Cores beyond the general ToS.

---

## Q5. Have there been retroactive changes, dilution events, boost endings, or controversies?

### Takeaway
The only documented change is the planned **end of the 2x pre-deposit boost** when the pre-deposit phase ended (late July 2026). This was followed by the Jul 27 publication of the per-venue multiplier table, which had been "illustrative" before that. No evidence was found of multiplier cuts, sybil purges or other controversies. Coverage is limited because X could not be read.

### Cited Findings
- The 2x pre-deposit boost "was the highest planned for the program. The phase has ended." — [Tori Docs: Cores](https://docs.tori.finance/resources/cores); [Tori Docs: General FAQ](https://docs.tori.finance/faq/general)
- "Cores multipliers are illustrative until the table publishes Jul 27 — the final multiplier table publishes at launch." — [app.tori.finance/defi](https://app.tori.finance/defi)
- The docs pages on Cores, pre-deposit and referral were last modified 2026-08-25 (FAQ 2026-09-20), so no recent rule changes appear in the docs. — [Tori Docs sitemap](https://docs.tori.finance/sitemap.xml)
- Web searches on "Tori Finance" with sybil, leaderboard, Season 2 or multiplier-cut terms returned only airdrop-guide rehashes. There were no reports of purges or changes. — e.g., [AirdropAlert](https://airdropalert.com/airdrops/tori-finance/), [airdrops.io](https://airdrops.io/tori-finance/)
- Dilution vector: new venues (Monad vaults, Royco tranches, YT Lock at 45x) and rising TVL ($50M in July to $73M on Sep 28) raise daily issuance. The 45x YT Lock is higher than the 30x ex-pre-deposit rate. — [app bundle](https://app.tori.finance/_next/static/immutable/chunks/2k0jyeo_ewi3n.js); [DefiLlama](https://defillama.com/protocol/tori-finance)

### Inferences
- The pre-deposit boost was "the highest planned", yet the Ecosystem Vault (35x), Pendle LP/locked YT-trUSD (45x) and Curve/Fluid (30x) now exceed the 30/day pre-deposit rate. The per-dollar rate therefore effectively rose after launch. Either the post-launch "Nx" scale differs from the pre-deposit base, or "highest boost" refers to the multiplier (2x) and not the absolute rate. This is a source of ambiguity worth flagging.

### Gaps
- Official X announcements (possible changes to multipliers, new seasons, snapshots) could not be verified.
- No Discord (discord.gg/torifinance) or Telegram announcement archive is accessible; the Telegram handle t.me/tori_finance is a squatted, for-sale username, not Tori's.
