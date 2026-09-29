# OnRe Finance Points Program (ONyc, Solana): mechanics, multipliers, supply of points (as of 2026-09-29)

Research date: 2026-09-29 (UTC ~06:15). The main data sources are OnRe's own GitBook docs and OnRe's **public, keyless rewards API** (`rewards.api.onre.finance/api/v1`). I pulled the full leaderboard (23,899 wallets) plus the official 30-day points-growth series from that API. So the totals below are **measured, not estimated**. Only the pre-2026-08-30 history and the forward projections are modelled.

---

## 1. What is the program called, when did it start, and are there seasons, an end date or a snapshot?

### Takeaway
The program is called **"OnRe Points"**. The docs page title is "OnRe Points Program" and Exponent labels it "OnRe Points", season 1. It went live publicly on **2025-09-11**, and ONyc activity before that date was tracked in the background and credited retroactively. As of 2026-09-29 I found no announced end date, season length, TGE snapshot or cap. There is a daily snapshot at 00:00 UTC, and it is used only for leaderboard ranking.

### Cited Findings
- **Launch:** OnRe press release/blog dated **September 11, 2025**: "today launched OnRe Points… OnRe Points are live today across all supported strategies." — [OnRe blog, 2025-09-11](https://www.onre.finance/blog/onre-introduces-points-program-rewarding-onyc-participation-across-defi); same release also on [GlobeNewswire 2025-09-11](https://www.globenewswire.com/news-release/2025/9/11/3148615/0/en/OnRe-Launches-Points-Program-Turn-Your-DeFi-Activity-into-Rewards.html).
- **Retroactive tracking before launch:** Exponent integration post (2025-09-04): "OnRe points are currently being tracked in the background and will be retroactively credited when the OnRe Rewards Program launches." — [OnRe blog, 2025-09-04](https://www.onre.finance/blog/onyc-meets-exponent-real-world-yield-gets-a-defi-upgrade). The API leaderboard still carries an Exponent market bucket named "AUG-2025", which is consistent with pre-launch accrual. — [OnRe rewards API leaderboard](https://rewards.api.onre.finance/api/v1/points/leaderboard?page=0&size=20)
- **Season label:** Exponent's points config lists OnRe with `"points_name": "OnRe Points"` and `"season": 1` (entries created 2026-08-24 and updated 2026-09-21 and 2026-09-23). — [Exponent points config API](https://app.exponent.finance/api/points/config)
- **"Pilot season":** the Referral & Ambassador doc says "The pilot season focuses on deepening engagement with ONyc…" and that "All point structures, multipliers, and seasonal criteria are listed on the Rewards Dashboard." — [OnRe docs: Referral and Ambassador Program](https://docs.onre.finance/onyc-in-defi/referral-and-ambassador-program)
- **Snapshot and update cadence:** "Every position you hold is measured once a day." Balances are "recalculated continuously… the leaderboard's official daily ranking is captured at 00:00 UTC", and points are "typically updated on an hourly basis". — [OnRe docs: OnRe Points Program](https://docs.onre.finance/onyc-in-defi/onre-points-program)
- **No cap:** "There is no fixed global cap, but certain campaigns or strategies may have limits. Any caps are disclosed in advance." — [OnRe docs](https://docs.onre.finance/onyc-in-defi/onre-points-program)
- **Separate "Season 1" of a different program:** a secondary news source (2026-09-17) says an "ONyc Compounding Interest Rewards Season 1" was "scheduled to begin September 27, 2026", with a 60-day holding qualification ("Positions maintained for 60 days or more qualify…"). It adds that "Full mechanics and reward rates for Season 1 are expected in the lead-up to the start date." — [Solana Compass, 2026-09-17](https://solanacompass.com/news/onre-surpasses-300m-aum-as-onyc-compounding-interest-rewards-season-1-opens-september-27)

### Inferences
- The points program has run continuously for about 383 days (2025-09-11 to 2026-09-29) with no season break. Counting retroactive accrual from the August 2025 Kamino, Loopscale and Exponent integrations, it has run about 13.5 months.
- The "Compounding Interest Rewards Season 1" that started 2026-09-27 may be a new reward layer, such as a yield or interest bonus for 60-day holders, and not a reset of OnRe Points. The rewards API shows no reset or new season bucket as of 2026-09-29, and points kept accruing normally on 09-27, 09-28 and 09-29.

### Gaps
- I found no official end date, TGE snapshot date or "Season 1 ends" date for OnRe Points.
- I could not reach a primary OnRe source (X post or docs) for "Compounding Interest Rewards Season 1". The only source is a secondary news summary with garbled wording ("qualify for interest rates"). Its mechanics, and whether it changes points accrual, are unknown. A follow-up search was blocked by a tool rate limit.

---

## 2. What is the base earning rate?

### Takeaway
The base rate is **1 point per ONyc per day**, measured on ONyc units (ONyc-equivalent exposure) and not on USD value. Price or NAV changes do not change points. Some stablecoin legs, such as USDC, USDG or USDS supplied to the OnRe lending markets, also earn points. Points are never clawed back.

### Cited Findings
- "The base rate is simple: **1 point per ONyc, per day.**" — [OnRe docs](https://docs.onre.finance/onyc-in-defi/onre-points-program)
- Official per-position formula: `position_points = onyc_equivalent_balance × duration_days × base_points_per_onyc_day (1) × venue_multiplier × personal_multiplier`. Wallet total = wallet + lending + looping + liquidity + yield_token + vault + campaign_boost + referral_bonus points, and `user_points = floor(total_points)`. — [OnRe docs](https://docs.onre.finance/onyc-in-defi/onre-points-program)
- "Accrual is based solely on ONyc exposure, not the market value of the position." "Once points are earned, they remain permanently associated with your wallet." — [OnRe docs](https://docs.onre.finance/onyc-in-defi/onre-points-program)
- "On automated market-maker pools, points are earned only on the ONyc side. Some lending and vault products do reward a supplied stablecoin leg." — [OnRe docs](https://docs.onre.finance/onyc-in-defi/onre-points-program)
- ONyc NAV on 2026-09-29 was **$1.150554** and circulating supply was **252.32M ONyc**, giving AUM of **$290.31M**. — [OnRe core API /data/nav](https://core.api.onre.finance/data/nav); [OnRe rewards API capital reconciliation](https://rewards.api.onre.finance/api/v1/analytics/capital/reconciliation)
- The API breakdown fields show the other assets that earn points: `kamino.usdg`, `kamino.usdc`, `kamino.usds`, `loopscale.usdc`, `kamino.onycJitosol`, `orca.onycUsdc`, `orca.onycJitosol`, `exponent.tranching.senior` and `junior` (srONyc and jrONyc), `carrot`, `elemental`, `exponentVault` and `ratex`. — [OnRe rewards API leaderboard](https://rewards.api.onre.finance/api/v1/points/leaderboard?page=0&size=20)

### Inferences
- Because accrual is per ONyc and NAV was $1.1506 on 2026-09-29, holding ONyc pays about 0.869 points per $1 per day at 1x.
- Cumulatively, stablecoin supply legs are material: loopscale.usdc is 7.9% of all points, kamino.usdc 3.2% and kamino.usdg 2.9%, so about 14% of points in total. Points are therefore not strictly "per ONyc of supply".

### Gaps
- The docs do not say how stablecoin legs convert into "ONyc-equivalent", whether per $1 or divided by NAV.

---

## 3. What multiplier does each integration or DeFi venue get? Do PT holders get zero points, and do YT holders get the points of the underlying?

### Takeaway
The current official tiers are: **Hodl 1x · LP 2x · Lend/Deposit 3–4x · Yield Tokens 5x · Loop/Leverage 6x**. Kamino loops earn "6x + Leverage", meaning 6x on the gross, levered ONyc collateral. **PT earns no points.** YT holders earn points on the underlying ONyc their YT represents, at the YT multiplier. Exponent LPs earn only on the YT portion of the LP. Exponent's live config (2026-09-21) shows **8x YT and 8x LP for the wONyc SY** and **4x for srONyc**. The 8x is above the documented 5x and looks like a limited-time maturity boost.

### Cited Findings
- **Tier table (OnRe docs, current):** Hodl, holding in wallet = 1x. Provide Liquidity, DEX pools = 2x. Lend and Deposit, supplying ONyc or stablecoins to lending markets, vaults and structured yield = 3x–4x. Yield Tokens, holding ONyc YTs in fixed-rate markets = 5x. Loop and Leverage, leveraged ONyc looping = 6x. "Unless otherwise stated, campaign boosts stack on top of standard venue multipliers." — [OnRe docs](https://docs.onre.finance/onyc-in-defi/onre-points-program)
- **Venue table (Referral & Ambassador doc):**

  | Activity | Venue | Asset or pair | Multiplier |
  |---|---|---|---|
  | Yield Trading | Exponent | ONyc | 5x |
  | Yield Trading | RateX | ONyc | 5x |
  | Looping | Kamino | ONyc/USDG, ONyc/USDC, ONyc/USDS | **6x + Leverage** |
  | Looping | Loopscale | ONyc/USDC, ONyc/USDT, ONyc/USX | 6x |
  | Looping | Elemental | ONyc/USDC | 4x |
  | Lending | Kamino | ONyc, USDG, USDC, USDS | 3x |
  | Lending | Loopscale | USDC | 3x |
  | LP | Kamino | ONyc/USDG, ONyc/JitoSOL | 2x |
  | LP | Orca | ONyc/USDC, ONyc/JitoSOL | 2x |
  | LP | Raydium | ONyc/USDG | 2x |

  — [OnRe docs: Referral and Ambassador Program](https://docs.onre.finance/onyc-in-defi/referral-and-ambassador-program)
- **PT = 0 points:** "No. ONyc Points are not earned on PT tokens within fixed rate markets… PT tokens… do not currently qualify for point accrual." — [OnRe docs](https://docs.onre.finance/onyc-in-defi/onre-points-program). The yield-trading page's comparison table reads ONyc "Regular points", PT-ONyc/PT-srONyc "No points", YT-ONyc/YT-srONyc "High points". — [OnRe docs: Yield Trading](https://docs.onre.finance/onyc-in-defi/defi-opportunities/yield-trading)
- **YT and LP:** YTs are "Eligible to earn OnRe Points, and users providing liquidity to supported PT/YT markets earn Points on the Yield Token (YT) portion of their LP position." "Eligible YT balances are calculated and updated hourly." — [OnRe docs: Yield Trading](https://docs.onre.finance/onyc-in-defi/defi-opportunities/yield-trading)
- **YT anti-churn rule:** "For strategies such as Exponent Yield Tokens that trade through an order book, points are calculated against the highest balance held during the accrual period and are floored at the value recorded at the time of any accounting change." — [OnRe docs](https://docs.onre.finance/onyc-in-defi/onre-points-program)
- **Exponent live config (fetched 2026-09-29):**
  - SY `G1qbuP11…` (wONyc, "Exponent Wrapped ONyc"): `points_per_day: 1`, **`yt_multiplier: 8`, `lp_multiplier: 8`**, updated 2026-09-21.
  - SY `AojEeHMj…` (wsrONyc, the senior tranche): **`yt_multiplier: 4`, `lp_multiplier: 4`**, updated 2026-09-23.
  - Both entries have `is_external_tracking: true`, meaning OnRe computes the points.
  - Sources: [Exponent points config API](https://app.exponent.finance/api/points/config); SY-to-asset mapping from [Exponent sy-tokens API](https://app.exponent.finance/api/sy-tokens).
- **Exponent markets tracked by OnRe (API buckets):** AUG-2025, JAN-2026, SEP-2026, SRONYC-SEP2026, ONYC-JAN2027 and SRONYC-JAN2027, plus Exponent tranching (senior and junior) and exponentVault. — [OnRe rewards API](https://rewards.api.onre.finance/api/v1/points/leaderboard?page=0&size=20)
- **Limited-time boost on new maturities:** "New maturities for ONyc and srONyc went live with limited-time points boosts." — [OnRe in Review: August 2026 (2026-09-01)](https://www.onre.finance/blog/onre-in-review-august-2026)
- **Earlier Exponent boost (community source):** "LPs providing ONyc liquidity on Exponent can receive 8x OnRe points rewards until January 31st, after which it will revert to the regular 5x multiplier." — [Odaily "Lazy Investor's Guide"](https://www.odaily.news/en/post/5208939). This is secondary and not verified against an OnRe primary source.
- **Historical multipliers at launch (2025-09-11):** Base 1x; LP on Kamino, Orca and Raydium 2x; lending collateral on Kamino and Loopscale 3x, "with scalable multipliers for looping"; Exponent YT and LP 4x ("Maximum rewards"). — [OnRe blog 2025-09-11](https://www.onre.finance/blog/onre-introduces-points-program-rewarding-onyc-participation-across-defi)
- **Loopscale (2025-08-20):** "3x OnRe points on all ONyc deposited"; a 4x loop turns "$50K" into "$200K of supplied ONyc, all earning 3x OnRe points… effective 12x multiplier on your original deposit." — [OnRe blog 2025-08-20](https://www.onre.finance/blog/onyc-launches-vault-on-loopscale-to-unlock-leveraged-usdc-strategies)
- **RateX (2025-10-16):** "For a limited time, ONyc participants can earn 8x RateX Points and 5x OnRe Points as part of a launch promotion." — [OnRe blog 2025-10-16](https://www.onre.finance/blog/trade-and-earn-real-world-yield-with-onyc-on-ratex)
- **Kamino ONyc/JitoSOL vault (2025-10-20):** "10x OnRe Points" for a limited time. — [OnRe blog 2025-10-20](https://www.onre.finance/blog/jitosol-x-onyc-where-solanas-native-yield-meets-real-world-income)
- **Carrot Boost loops (2025-12-31):** "users can earn 6x OnRe Points". — [OnRe blog 2025-12-31](https://www.onre.finance/blog/onyc-looping-is-now-live-on-carrot-boost)
- **Elemental vault (2026-02-11):** "Vault depositors earn OnRe Points" (the multiplier is not stated there; the docs table gives Elemental 4x). — [OnRe blog 2026-02-11](https://www.onre.finance/blog/the-elemental-edge)
- **Ethereum / RockawayX "OnRe Core Vault" on Accountable (2026-06-03):** "rewards 4x OnRe Points". — [OnRe blog 2026-06-03](https://www.onre.finance/blog/onres-uncorrelated-reinsurance-backed-yield-is-now-available-on-ethereum-for-the-first-time)
- **Exponent v2 (2026-05-29):** "coordinated incentives and boosted OnRe Points are now live across multiple Exponent v2 participation flows." — [OnRe blog 2026-05-29](https://www.onre.finance/blog/onyc-expands-across-exponent-v2-with-new-yield-strategies-fixed-rate-markets-and-automated-vault-infrastructure)
- **Venues not in the current tables:** I found no OnRe points integration for Drift, Jupiter Lend or Meteora. Jupiter is named only as a secondary-liquidity venue ("Secondary liquidity is available 24/7 via Orca, Raydium, Jupiter"). — [OnRe docs FAQ](https://docs.onre.finance/technical-resources/frequently-asked-questions)
- **Leverage earns more:** "Leveraged strategies can earn more points because they increase effective ONyc exposure." — [OnRe docs](https://docs.onre.finance/onyc-in-defi/onre-points-program)

### Inferences
- **YT points per $:** a YT on 1 ONyc earns 5–8 points/day, depending on whether the base 5x or the current 8x Exponent setting applies, while costing only the YT price, roughly a few % of NAV. Points per dollar are therefore very high on YT. For example, if YT-ONyc (JAN-2027) costs about 3–4% of ONyc, 8x/day on about $0.035 of capital is about 200+ points per $ per day. That compares with 0.87 points per $ per day for plain holding. This needs the live YT price from the Exponent researcher.
- **Kamino loop per equity dollar:** at 6x on gross collateral with 2.5–2.9x leverage (typical per OnRe's Kamino review), a loop earns roughly 15–17 points per ONyc of equity per day.
- **Conflicting YT multipliers:** 4x at launch, 5x in the docs today, 8x in the Exponent config for wONyc. The multiplier appears to change per maturity and campaign. The 8x on wONyc (updated 2026-09-21) is most likely the "limited-time points boost" for the new ONYC-JAN2027 maturity. Its expiry is not published.

### Gaps
- There is no published per-market schedule, for example a start and end date for the 8x on ONYC-JAN2027.
- The exact leverage-counting rule for Kamino "6x + Leverage" is not documented, for example whether borrowed stablecoins are netted.
- Current RateX multiplier: docs say 5x, but the RateX bucket is only 0.65% of total points, so this matters little.
- Drift, Jupiter Lend and Meteora: no evidence of any points integration.

---

## 4. Referral bonuses, boosts, campaigns, badges, early-user or tier multipliers, decay

### Takeaway
Referrals pay the referrer **+10% of the referee's points** and give the referee **+5%**. They activate only once the referee holds **≥100 ONyc** and have no cap. Time-limited campaigns (10x, 3x, 5x, 6x, 8x, 10x) have stacked on top of venue multipliers. There is **no decay**: points are never clawed back and earlier entry simply means more days of accrual. Ambassador tiers are Discord roles only, and I found no NFT or badge multipliers.

### Cited Findings
- **Referral terms:** "Referrers receive a bonus equal to 10% of the points earned by the referred wallet. Referred users receive an additional 5% bonus on their own point accrual." Activation requires "the minimum qualifying ONyc exposure threshold, currently set at 100 ONyc"; "Any points earned prior to activation are excluded". There is no limit on the number of referrals and no cap on referral rewards. Self-referral is not allowed, and each wallet can have only one referrer. — [OnRe docs](https://docs.onre.finance/onyc-in-defi/onre-points-program)
- The referral doc also describes the referrer's 10% as coming from the referee's "ONyc wallet exposure points, calculated from their verified ONyc balance", and says "Referral relationships are permanent." — [OnRe docs: Referral and Ambassador Program](https://docs.onre.finance/onyc-in-defi/referral-and-ambassador-program)
- **Referral points issued in aggregate:** 6.508B cumulative as of 2026-09-29, 2.70% of all points. The recent rate is about 50–51M per day, roughly 4% of base issuance. — [OnRe rewards API analytics/overview](https://rewards.api.onre.finance/api/v1/analytics/overview); [points/growth](https://rewards.api.onre.finance/api/v1/analytics/points/growth)
- **Global Access launch campaign:**
  - 2025-10-01 "Day-One Super Boost": 10x on ONyc acquired through the Global Access flow. Example given: 1,000 ONyc bought 2025-10-01 = 140,000 points by 10-16.
  - 2025-10-02 to 10-16: "3x daily multiplier" on newly acquired ONyc. Example given: 1,000 ONyc = 42,000 points.
  - Both require a 14-day holding period.
  - Source: [OnRe blog 2025-10-01](https://www.onre.finance/blog/introducing-onyc-global-access-the-permissionless-path-to-onchain-institutional-yield)
  - Results: "12,325,124 points earned through the 10x Launch campaign" and "151,431,377 points earned through the 3x Daily Multiplier". — [OnRe in Review: October 2025](https://www.onre.finance/blog/onre-in-review-october-2025)
- **Per-wallet global multiplier seen in the API:** one leaderboard wallet, rank 23, shows `activeMultipliers: [{"sourceType":"GLOBAL","multiplier":1.1,"effectiveFromDate":"2026-09-18","effectiveToDate":null}]`. All other wallets show null or empty. — [OnRe rewards API leaderboard](https://rewards.api.onre.finance/api/v1/points/leaderboard?page=0&size=1000)
- **No decay:** "Selling, transferring, or withdrawing ONyc only impacts future accrual and never reduces points already accumulated." — [OnRe docs](https://docs.onre.finance/onyc-in-defi/onre-points-program)
- **Ambassador program:** Discord roles (Observer, Analyst, Builder, Yield Seeker, Connector, Catalyst) giving "visible Discord roles and leaderboard recognition". No points multiplier is stated. — [OnRe docs: Referral and Ambassador Program](https://docs.onre.finance/onyc-in-defi/referral-and-ambassador-program)
- The API field `permissionlessBoost` totals only 18.45M across all wallets. That is far below the 163.8M the October 2025 review reports for the two launch campaigns, so the campaign points were probably folded into other buckets. — [OnRe rewards API](https://rewards.api.onre.finance/api/v1/points/leaderboard?page=0&size=1000)

### Inferences
- In a model, referral adds about 2.7–4% on top of base issuance. Campaign boosts are episodic and small in aggregate (the October 2025 campaigns were about 0.16B points, under 0.1% of today's total).
- Early-user advantage is only time in market. There is no explicit early-user multiplier except the 2025-10-01 and 10-02 to 10-16 campaigns.

### Gaps
- The meaning and eligibility of the 1.1x "GLOBAL" personal multiplier (from 2026-09-18) are undocumented.
- I found no badges or NFTs, and no tier multipliers based on holding size or duration.

---

## 5. Total points issued so far and the current daily issuance rate, with a historical estimate

### Takeaway
**Total OnRe Points issued as of 2026-09-29 is about 240.90B** (234.39B base plus 6.51B referral) across **23,899 wallets**. This figure comes from OnRe's official API. **The current issuance rate is about 1.32–1.33B points per day** (about 1.275B base plus about 0.051B referral). That equals about **5.0 base points per circulating ONyc per day** (about 5.2 including referral), or about 4.4 points per $ of AUM per day. At a flat rate, total points reach about **364B by 2026-12-31** and about **483B by 2027-03-31**.

### Cited Findings
- **Official totals** (`/analytics/overview`, asOfDate 2026-09-29):
  - totalBasePointsIssued = 234,389,729,691
  - totalReferralBonusIssued = 6,508,471,694
  - **totalPointsIssued = 240,898,201,385**
  - walletCount = 23,899
  - Source: [OnRe rewards API analytics/overview](https://rewards.api.onre.finance/api/v1/analytics/overview)
- My own sum of `totalPoints` over all 23,899 leaderboard rows, pulled 2026-09-29 06:13 UTC in 24 pages of 1,000, is **240,898,189,696**, which matches the overview. — [OnRe rewards API leaderboard](https://rewards.api.onre.finance/api/v1/points/leaderboard?page=0&size=1000)
- **Official daily series** (`/analytics/points/growth`, last 31 days only):

  | Date | Total issued (cumulative) | Daily total growth | Daily base | Daily referral |
  |---|---|---|---|---|
  | 2026-08-30 | 189.49B | — | — | — |
  | 2026-09-01 | 192.67B | 1.53B | 1.45B | 0.075B |
  | 2026-09-10 | 217.22B | 5.99B (spike) | 5.59B | 0.40B |
  | 2026-09-15 | 219.48B | **−3.76B** (correction) | −3.62B | −0.14B |
  | 2026-09-19 | 225.62B | 2.21B | 2.69B | −0.49B (referral correction) |
  | 2026-09-23 | 231.89B | 1.33B | 1.28B | 0.049B |
  | 2026-09-26 | 235.87B | 1.32B | 1.27B | 0.051B |
  | 2026-09-29 | **239.85B** | **1.324B** | **1.274B** | **0.051B** |

  - Mean daily growth over 2026-08-31 to 09-29 is about 1.68B, inflated by backfill spikes.
  - The steady state over 2026-09-20 to 09-29 is **1.32–1.67B per day, and 1.32–1.33B per day over the last 7 days**.
  - Source: [OnRe rewards API analytics/points/growth](https://rewards.api.onre.finance/api/v1/analytics/points/growth)
- **Points per ONyc per day,** computed as daily base ÷ previous-day circulating supply. The last 7 days are steady at **4.88–5.03 base (5.07–5.23 total)** with supply of about 253–262M ONyc. The 30-day average, including backfills, is 6.44. — computed from [points/growth](https://rewards.api.onre.finance/api/v1/analytics/points/growth) and [core API NAV/supply](https://core.api.onre.finance/data/nav)
- **Capital distribution by protocol** (2026-09-29, `/analytics/capital/distribution`):

  | Protocol | Capital | Share |
  |---|---|---|
  | Kamino | $184.5M | 63.6% |
  | Loopscale | $61.1M | 21.0% |
  | Exponent | $36.1M | 12.4% |
  | Orca | $9.7M | 3.3% |
  | Elemental | $6.9M | 2.4% |
  | Carrot | $0.1M | 0.04% |
  | **Total AUM** | **$290.3M** | |

  — [OnRe rewards API analytics/overview](https://rewards.api.onre.finance/api/v1/analytics/overview)
- **Cumulative points by source bucket** (sum over all wallets, 2026-09-29; the Exponent YT and LP totals include all maturities):

  | Bucket | Points | Share |
  |---|---|---|
  | Kamino ONyc | 71.19B | 29.6% |
  | Loopscale ONyc | 59.11B | 24.5% |
  | Exponent YT | 39.21B | 16.3% |
  | Loopscale USDC | 19.01B | 7.9% |
  | Wallet (hodl) | 12.33B | 5.1% |
  | Kamino USDC | 7.68B | 3.2% |
  | Kamino USDG | 7.05B | 2.9% |
  | Referral | 6.51B | 2.7% |
  | Elemental | 4.78B | 2.0% |
  | Carrot | 4.31B | 1.8% |
  | Exponent LP | 3.21B | 1.3% |
  | Orca ONyc/USDC | 2.16B | 0.9% |
  | RateX | 1.57B | 0.65% |
  | Exponent vault | 1.51B | 0.63% |
  | Exponent tranching junior | 0.58B | |
  | Exponent tranching senior | 0.24B | |
  | Kamino ONyc/JitoSOL | 0.42B | |

  - Exponent YT by maturity: SEP-2026 24.80B, AUG-2025 6.00B, ONYC-JAN2027 4.24B, JAN-2026 3.08B, SRONYC-JAN2027 0.19B, SRONYC-SEP2026 0.15B.
  - Source: [OnRe rewards API leaderboard](https://rewards.api.onre.finance/api/v1/points/leaderboard?page=0&size=1000)
- **Concentration** (2026-09-29): top 1 wallet = 8.10% of all points (19.50B). Top 10 = 27.4%, top 50 = 43.5%, top 100 = 52.3%, top 500 = 75.2%, top 1,000 = 84.75% and top 5,000 = 98.4%. Median wallet = 72,095 points. 6,236 wallets hold >1M points, 345 hold >100M and 23 hold >1B. — computed from [OnRe rewards API leaderboard](https://rewards.api.onre.finance/api/v1/points/leaderboard?page=0&size=1000)
- **ONyc supply and AUM history** (OnRe core API):

  | Date | Supply | AUM |
  |---|---|---|
  | 2025-09-11 (launch) | 25.3M ONyc | $26.1M |
  | 2025-12-01 | 40.6M | |
  | 2026-01-01 | 69.1M | |
  | 2026-03-01 | 107.7M | |
  | 2026-05-01 | 143.2M | |
  | 2026-07-01 | 184.0M | |
  | 2026-09-01 | 245.6M | |
  | 2026-09-29 | 252.3M | $290.3M |

  NAV rose from 1.0299 to 1.1506 over the same period. — [OnRe core API /data/nav](https://core.api.onre.finance/data/nav)
- **Community tracker:** onre.xpoints.io ("community-built · unofficial") mirrors the same API. It shows #1 at 19,502,759,963 points, identical to the official API. — [ONRE Points Leaderboard (xpoints)](https://onre.xpoints.io/)

### Inferences (historical reconstruction and projections; these are estimates)
- **History before 2026-08-30 (model).** The official series gives 185.01B base points accrued before 2026-08-30. I spread that over daily circulating supply from 2025-09-11 to 2026-08-29, which totals 3.976e10 ONyc-days. That implies a lifetime average of **about 4.65 base points per ONyc per day** (4.55 if accrual is assumed to start 2025-08-01). Assuming a constant ratio, estimated base points per month are:

  | Month | Est. base points | Cumulative |
  |---|---|---|
  | Sep 2025 (from 09-11) | 2.5B | 2.5B |
  | Oct 2025 | 4.5B | 7.0B |
  | Nov 2025 | 4.7B | 11.7B |
  | Dec 2025 | 7.6B | 19.4B |
  | Jan 2026 | 11.6B | 31.0B |
  | Feb 2026 | 11.9B | 42.9B |
  | Mar 2026 | 17.7B | 60.6B |
  | Apr 2026 | 17.7B | 78.3B |
  | May 2026 | 22.8B | 101.0B |
  | Jun 2026 | 23.9B | 124.9B |
  | Jul 2026 | 29.2B | 154.2B |
  | Aug 2026 | 30.8B | 185.0B (calibrated to the official figure) |
  | Aug 30 – Sep 29 2026 | +49.4B base (official) | 234.4B base / 240.9B total |

  The ratio probably rose over time as looping share grew, so the true early months were likely somewhat lower and recent months higher. The model is anchored on the official 185.0B and 234.4B figures.
- **Cross-check against the multiplier mix.** On 2026-09-29, Kamino holds 63.6% of capital, much of it looped at 6x on gross collateral, and Loopscale holds 21% at 6x plus a 3x stablecoin leg. Exponent holds 12.4%, but its YT points go only to YT holders; PT and the SY/PT side earn nothing. That mix plausibly yields the observed weighted average of about 5x base per circulating ONyc. So "supply × about 5 points per day" is a reasonable modelling rule for now.
- **Forward projections of total points,** starting at 240.9B on 2026-09-29 with 1.3244B per day now:

  | Date | Flat rate | +3% per month | +8% per month |
  |---|---|---|---|
  | 2026-10-31 | 283B | 284B | 285B |
  | 2026-12-31 | 364B | 370B | 380B |
  | 2027-03-31 | 483B | 506B | 550B |
  | 2027-06-30 | 604B | 657B | 767B |

  For reference, supply grew about +8% per month through H1 2026 but was flat to slightly down over 2026-09-15 to 09-29 (262M falling to 252M ONyc).
- **Rule of thumb for per-user share:** a user earning X points per day gets X / 1.32B of current daily issuance. For example, 1,000 ONyc held idle earns 1,000 per day, which is 7.6e-7 of daily issuance.
- **Negative days (2026-09-15, 2026-09-19 referral) conflict with "never clawed back".** They suggest occasional recalculations, sybil or blacklist removals, or bug fixes at aggregate level. The app bundle references an `/accounts/blacklist-stats` endpoint, which is not public. This is an inference only.

### Gaps
- The public API exposes only the last 30 days of the issuance series. The pre-2026-08-30 path is my model, not official data.
- I found no Dune dashboard or community spreadsheet with a longer points history. archive.org had no snapshots of the rewards API.
- The spikes (e.g., +5.99B on 2026-09-10 and +2.93B on 09-04) are unexplained. They are likely backfills when new markets or campaigns are tracked; the docs say "Eligible activity from that initial period is still accounted for once tracking begins".

---

## 6. What does OnRe say about the share of token supply that points convert to, or give any conversion hints?

### Takeaway
There is **no official token, TGE date, airdrop allocation or points-to-token ratio** as of 2026-09-29. The docs explicitly say points carry no entitlement to tokens. The only official hint of a token is a **May 2025** OnRe launch post referring to "the $ONRE protocol token". Third-party airdrop sites treat $ONRE as speculative.

### Cited Findings
- "Points have no monetary value, are not transferable, and do not represent any entitlement to tokens, assets, or financial rewards. They exist to measure participation and to power the leaderboard… where your standing may influence future benefits, incentives, and program rewards at OnRe's discretion." — [OnRe docs](https://docs.onre.finance/onyc-in-defi/onre-points-program)
- An official OnRe post (2025-05-21, launching the earlier "ONe" token) says: "token incentives from sUSDe and the **$ONRE protocol token** offer meaningful upside potential." It also said ONe offered "projected returns of up to 40.35% consisting of reinsurance performance, collateral yield, and token incentives." — [OnRe blog 2025-05-21](https://www.onre.finance/blog/onre-backed-by-ethena-solana-ventures-and-rockawayx-launches-structured-yield-product-combining-real-world-stability-and-on-chain-upside)
- MEXC blog (2026-05-12): "No official $ONRE token launch details, total supply, or TGE timeline have been announced as of April 2026". The same article speculatively says "$ONRE token incentives are active on all pools and integrations" and cites Exponent YT as offering "up to 27x point multipliers", which is effective leverage and not an official multiplier. — [MEXC blog 2026-05-12](https://blog.mexc.com/token-reviews/onre-airdrop-2026-how-to-earn-onre-by-depositing-into-the-worlds-first-on-chain-reinsurance-protocol-on-solana/)
- An aggregated search snippet claimed the "OnRe Finance airdrop ends December 31, 2026". This comes from third-party airdrop listings such as [airdrops.io](https://airdrops.io/onre/), [AirdropBee](https://airdropbee.com/onre-airdrop/) and [Airdrops.sh](https://www.airdrops.sh/airdrop/onre-finance). Treat it as an unverified placeholder; no OnRe source confirms it.

### Inferences
- Any points-to-token model needs assumed airdrop percentages, since OnRe has given no guidance. The measured inputs are 240.9B points now and about 1.32B per day.
- The "$ONRE protocol token" wording (May 2025) and the "future benefits, incentives, and program rewards at OnRe's discretion" language point to an eventual token-linked reward, but nothing is committed.

### Gaps
- OnRe has published no tokenomics, TGE date, airdrop percentage, vesting or points-conversion formula. A final search for recent (Sept 2026) token news was blocked by a tool rate limit, so an announcement in the last days before 2026-09-29 cannot be fully ruled out.

---

## 7. Sybil and eligibility rules, KYC, geographic restrictions, minimum holdings

### Takeaway
Points are wallet-based, and multiple wallets per user are explicitly allowed. The only anti-gaming rules are: no self-referral, one referrer per wallet, a 100 ONyc minimum for referral activation, a 14-day hold on launch campaigns, and max-balance or floor accounting for order-book YTs. **Open Access (permissionless) ONyc needs no KYC**, but ONyc is **excluded for US persons and about 65 jurisdictions, including the UK, South Korea, Vietnam, Australia, Russia and Nigeria**. Direct mint and redeem through the regulated route needs Sumsub KYC and Bermuda "Qualified Acquirer" status.

### Cited Findings
- "Can multiple wallets owned by the same user participate? Yes, leaderboard rankings are based on wallet addresses." — [OnRe docs](https://docs.onre.finance/onyc-in-defi/onre-points-program)
- "Wallets with fewer than 1 total accrued point may not yet appear on the leaderboard." A referral activates at 100 ONyc. — [OnRe docs](https://docs.onre.finance/onyc-in-defi/onre-points-program)
- **Open Access:** "No onboarding or approvals required… Permissionless participation with no minimums… Broad global availability, subject to jurisdictional restrictions". **Institutional Access:** "requires KYC/KYB". — [OnRe docs: Open Access vs Institutional Access](https://docs.onre.finance/for-capital-providers/open-access-vs-institutional-access)
- **KYC for direct mint and redeem:** "To mint or redeem directly through the OnRe app, all capital providers must complete identity verification through… Sumsub." Participants must be Qualified Acquirers under Bermuda law, meeting one of:
  - income of $200k per year (or $300k joint);
  - net worth of $1M or more;
  - for corporations, about $5M in assets.
  - Source: [OnRe docs: KYC and AML Policy](https://docs.onre.finance/legal/kyc-and-aml-policy)
- **Excluded jurisdictions (full list):** Afghanistan, Algeria, Angola, Australia, Belarus, Bolivia, Bosnia & Herzegovina, British Virgin Islands, Bulgaria, Burkina Faso, Burundi, Cameroon, Central African Republic, Côte d'Ivoire, Crimea, Croatia, Cuba, Democratic Republic of Congo, Ethiopia, Guinea-Bissau, Haiti, Iran, Iraq, Kenya, Kosovo, Kuwait, Laos, Lebanon, Liberia, Libya, Mali, Monaco, Montenegro, Mozambique, Myanmar, Namibia, Nepal, Nicaragua, Nigeria, North Korea, North Macedonia, Papua New Guinea, Northern Cyprus, Romania, Russia, Serbia, Slovenia, Somalia, Somaliland, South Africa, **South Korea**, South Ossetia, South Sudan, Sudan, Syria, Ukraine (Donetsk, Kherson, Luhansk and Zaporizhzhia oblasts), **United Kingdom, United States**, Venezuela, **Vietnam**, West Bank, Yemen and Zimbabwe. — [OnRe docs: ONyc Excluded Jurisdictions](https://docs.onre.finance/legal/onyc-excluded-jurisdictions)
- October 2025: "Anyone outside the U.S. can now mint ONyc permissionlessly". — [OnRe in Review: October 2025](https://www.onre.finance/blog/onre-in-review-october-2025)
- The Open Access route "is operated independently" by On Technologies Corporation, separate from the regulated On Re SAC Ltd, and is used "at users' own risk". — [OnRe blog 2025-10-01](https://www.onre.finance/blog/introducing-onyc-global-access-the-permissionless-path-to-onchain-institutional-yield)
- The app front-end has geoblocking enabled (`VITE_ENABLE_GEOBLOCK: true` in the production bundle). — [app.onre.finance](https://app.onre.finance/earn/leaderboard) (observed in the JS bundle on 2026-09-29)

### Inferences
- Points accrue on-chain by wallet, whatever the holder's jurisdiction. However, a future token distribution could impose KYC or geo-exclusion; there is no information either way. Users in excluded jurisdictions, including Vietnam, the US, the UK and South Korea, face terms-of-use risk and possible exclusion at any TGE.
- Sybil splitting across wallets gives no advantage, since accrual is linear per ONyc. It matters only for referral self-dealing, which is prohibited.

### Gaps
- There are no published sybil-filtering criteria for any future airdrop.
- It is unknown whether points earned by wallets in excluded jurisdictions will be honoured.
