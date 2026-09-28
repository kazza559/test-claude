# Saturn (saturn.credit) Points Program: Quantitative Detail (as of 2026-09-28)

Scope: this covers Saturn, the issuer of the USDat stablecoin and sUSDat (STRC-backed yield token), X handle @saturn_credit, docs at saturncredit.gitbook.io. It is not "Saturn Network" or Saturn.btc.
Data pull time: 2026-09-28, about 10:00–12:00 UTC. Most numbers below come from primary machine-readable sources: the Saturn app API and the Merkl API that the Saturn app itself queries. Estimates are labelled as estimates.

Method note (read first). The Saturn app reads points from its own endpoints `https://app.saturn.credit/api/points/snapshot?season=N` and `https://app.saturn.credit/api/points/{address}?season=N&snapshot=ID`. Both return Merkl-format objects: `{amount, pending, recipient}`, 18 decimals. The app JS hard-codes `CURRENT_POINTS_SEASON = 2`, `CURRENT_SEASON_LABEL = "SEASON 2"` and `POINTS_CREATOR_ADDRESS = 0x80c6a512B548229226C0676d6fdbAfF81d325990`. That address is the Merkl campaign creator (Merkl `creatorId: "saturn"`). Every Saturn points campaign lives on Merkl as a "POINT"-type reward token:
- Gravity Points (S1): `0xD223bbdd0421E394C0df9dFfe568f1dADfFd6f85`
- Orbital Points (S2): `0x10710501778b7FAf9e478f36FaE0B286C028eDE8`

The app's strategies page states it too: "Rates are reported by Merkl". I pulled all 183 campaigns, every leaderboard, per-campaign distributions and opportunity TVL/daily-reward records from `api.merkl.xyz`.

---

## Q1. Program name, seasons, start/end dates, snapshot

### Takeaway
Season 1 was "Gravity Points". It ran from a private beta on about 2026-03-15, went public on 2026-04-08 and ended 2026-08-08 at 23:59 ET (Merkl end 2026-08-09 03:59 UTC). Season 2, "Orbital Points", is live now. It runs from 2026-08-09 00:00 ET to 2026-12-08 23:59 ET, or until TVL reaches $1B. Saturn says TGE (ticker STRN) is planned for Q4 2026. If TGE comes before Dec 8, S2 ends early with a pro-rated allocation, and Season 3 starts right after the S2 snapshot.

### Cited Findings
- Gravity Points campaign "started on April 8th, following a one-month private beta period". "Season 1 will end on August 8th or until Saturn's Total Value Locked (TVL) reaches $500M USD – whichever occurs first." — [Saturn docs: Gravity Points – Season 1](https://saturncredit.gitbook.io/saturn-docs/overview/gravity-points-season-1)
- On Merkl, the earliest Gravity campaigns start 2026-03-15 16:00 UTC (the private beta) and the S1 base campaigns end 2026-08-09 03:59 UTC. — [Merkl API, campaigns by Saturn creator](https://api.merkl.xyz/v4/campaigns?creatorAddress=0x80c6a512B548229226C0676d6fdbAfF81d325990&items=100&page=0) (also `&page=1`, `&page=2`)
- "Season 2 points will be called Orbital Points". "Season 2 will begin at 12:00 AM ET on August 9, 2026, and end at 11:59 PM ET on December 8, 2026, or when Saturn's total value locked reaches $1 billion, whichever occurs first." — [Saturn docs: Orbital Points – Season 2](https://saturncredit.gitbook.io/saturn-docs/overview/orbital-points-season-2)
- On Merkl, S2 base campaigns run 2026-08-09 04:00 UTC to 2026-12-09 04:59 UTC. — [Merkl API](https://api.merkl.xyz/v4/campaigns?creatorAddress=0x80c6a512B548229226C0676d6fdbAfF81d325990&items=100&page=0)
- Season 1 ended on time, not on the TVL trigger: "Saturn's total value locked peaked at approximately $248 million before heightened STRC volatility. TVL subsequently stabilized at approximately $180 million". The same passage reports >5,000 users with ≥$10 positions and lending markets around $23.74M. — [Orbital Points – Season 2 docs](https://saturncredit.gitbook.io/saturn-docs/overview/orbital-points-season-2)
- Saturn app live snapshot API on 2026-09-28: S1 `{"calculatedAt":"2026-09-28T10:17:23.769Z","snapshotId":"805","status":"ready"}`, S2 `{"calculatedAt":"2026-09-28T10:17:37.182Z","snapshotId":"806","status":"ready"}`. — [app.saturn.credit/api/points/snapshot?season=2](https://app.saturn.credit/api/points/snapshot?season=2)
- The TGE announcement of 2026-09-25 (reported via MarsBit, ChainCatcher and KuCoin) has these parts:
  - Token ticker STRN, TGE in Q4 2026.
  - "up to 5% of the total token supply reserved for allocation during Season 2".
  - "If the second season ends early, the TGE allocation will be proportionally reduced based on the actual duration… any unallocated portion will be returned to the Saturn ecosystem allocation for future seasons". Worked example: 75% of the duration gives 75% of the allocation.
  - Season 3 begins immediately after the S2 snapshot. Eligible positions keep earning S2 points until the snapshot, and no user action is required.
  - Tokenomics and claim details "will be disclosed in future announcements".
  - Sources: [ChainCatcher, 2026-09-25](https://www.chaincatcher.com/en/article/2292229); [KuCoin flash, 2026-09-25](https://www.kucoin.com/news/flash/saturn-plans-tge-in-q4-2026-allocates-up-to-5-supply-for-second-season)
- KOL reading of the TGE announcement (DEFI Kadic, 2026-09-25):
  - "Plan 1 (TGE on/after Dec 8): full 5%".
  - "Plan 2 (TGE before Dec 8): S2 ends early; allocation reduced by running days / total days".
  - Source: [KuCoin insight – DEFI Kadic](https://www.kucoin.com/news/insight/PENDLE/6ab625c874fd460007c54ed9)

### Inferences
- Nominal S2 length is 122.04 days (Aug 9 04:00 UTC to Dec 9 04:59 UTC). On 2026-09-28 12:00 UTC, 50.3 days had elapsed and about 71.7 remain.
- Because of the pro-rata rule, tokens per S2 point stay roughly the same whatever the TGE date, as long as the daily emission rate stays roughly constant. An earlier TGE shrinks both the allocation and the points supply in proportion. See Q4.
- Some sources say "TGE scheduled before December 8", but the official wording as reported only says "Q4 2026" plus the early-end pro-rata clause. The exact TGE date is not public.

### Gaps
- There is no exact TGE date and no S2 snapshot date beyond "Q4 2026". Season 3 terms (rates, allocation) are unknown.
- The original X/Discord announcements could not be reached. X mirrors (xcancel, nitter) were down or blocked, so the TGE announcement is taken from media relays.

---

## Q2. Exact earning rates: points per $1 per day, full multiplier tables and history

### Takeaway
1× equals 1 point per $1 of position value per day, time-weighted and computed hourly by Merkl. Merkl stores each campaign as a "FIX_APR" of 365% × multiplier, so APR 365 = 1×, 1825 = 5×, 10950 = 30×. I checked this against live Merkl daily-reward records:
- Hold sUSDat on Ethereum: $45.28M TVL earns 45.28M points/day (1.00×).
- Hold USDat: $55.05M earns 275.3M/day (5.00×).
- Curve USDC/USDat: $9.47M earns 236.9M/day (25.0×).

For Pendle YT the "$1" is one YT unit, i.e. $1 of underlying notional, not the YT market price. See Q3.

### Cited Findings: unit calibration
- Opportunity records timestamped 2026-09-28 00:00 UTC:
  - "Hold Staked USDat (sUSDat)": TVL 45,277,082, daily Orbital amount 45,277,082 (= 1×). — [Merkl opportunity 7327235486235463977](https://api.merkl.xyz/v4/opportunities/7327235486235463977)
  - "Hold USDat": TVL 55,054,607, daily 275,273,035 (= 5×). — [Merkl opportunity 2416353277329385508](https://api.merkl.xyz/v4/opportunities/2416353277329385508)
  - "Provide liquidity to Curve USDC-USDat": TVL 9,474,168, daily 236,854,197 (= 25×). — [Merkl opportunity 11602167019406774224](https://api.merkl.xyz/v4/opportunities/11602167019406774224)
- The campaign parameters use `distributionMethod: FIX_APR` with `apr` values of 365 (1×), 1825 (5×), 3650 (10×), 5475 (15×), 9125 (25×) and 10950 (30×), `rewardTokenPricing: false` and `computeMethod: genericTimeWeighted`. — [Merkl API campaigns](https://api.merkl.xyz/v4/campaigns?creatorAddress=0x80c6a512B548229226C0676d6fdbAfF81d325990&items=100&page=0)

### Cited Findings: Season 2 (Orbital) official table
Source: [Orbital Points – Season 2 docs](https://saturncredit.gitbook.io/saturn-docs/overview/orbital-points-season-2) and [Allocations](https://saturncredit.gitbook.io/saturn-docs/overview/allocations). Points are per $1 per day and the table is valid from 2026-08-09. The Merkl APR confirming each row is in brackets.

| Activity | Orbital pts/$/day | Chains |
|---|---|---|
| Hold USDat | 5× [1825] | ETH, BNB, Monad |
| Hold sUSDat | 1× [365] | ETH, BNB, Monad |
| Curve LP USDC/USDat | 25× [9125] | ETH, Monad |
| Curve LP USDC/sUSDat | 25× [9125] | ETH, Monad |
| PancakeSwap USDT/USDat, active range | 25× | BNB |
| PancakeSwap USDT/sUSDat, active range | 25× | BNB |
| Pendle LP USDat | 15× [5475] | ETH, BNB, Monad |
| Pendle YT-USDat | 30× [10950] | ETH, BNB, Monad |
| Pendle LP sUSDat | 5× [1825] | ETH, BNB, Monad |
| Pendle YT-sUSDat | 10× [3650] | ETH, BNB, Monad |
| Strata srUSDat (senior) | 1× [365] | ETH |
| Strata jrUSDat (junior) | 5× [1825] | ETH |
| Pendle LP srUSDat | 7.5× [2737.5] | ETH (Merkl also has a Monad campaign) |
| Pendle YT-srUSDat | 15× [5475] | ETH (Merkl also Monad) |
| Pendle LP jrUSDat | 5× | ETH |
| Pendle YT-jrUSDat | 10× | ETH |
| Lend USDC in Saturn Morpho vault (satUSDC) | 1× [365] | ETH, Monad |
| Lend AUSD in Flowdesk AUSD RWA strategy (fAUSDe) | 1× [365] | ETH |
| Borrow AUSD against sUSDat collateral (Morpho) | 2× [730, MORPHOBORROW] | ETH |

- The docs add: "Orbital Points will remain consistent across Ethereum, BNB Chain, and Monad." "Saturn may also introduce temporary campaigns or boosts". "PancakeSwap positions must remain within the active liquidity range". — [S2 docs](https://saturncredit.gitbook.io/saturn-docs/overview/orbital-points-season-2)
- The app strategies page (Season 2) shows "Max Points 25×" across 15 non-Pendle routes: Hold USDat 5×, Hold sUSDat 1×, Curve 25×, Morpho borrow 2×, lend 1×, srUSDat 1×, jrUSDat 5×. Pendle routes are not listed on that page. — [app.saturn.credit/strategies](https://app.saturn.credit/strategies)
- The Pendle YT-jrUSDat and LP-jrUSDat campaigns on Merkl only exist for the 27AUG2026 expiry, which ended 2026-08-27. No 14JAN2027 jrUSDat market campaign exists. — [Merkl API](https://api.merkl.xyz/v4/campaigns?creatorAddress=0x80c6a512B548229226C0676d6fdbAfF81d325990&items=100&page=1)

### Cited Findings: Season 1 (Gravity) official table
Points are per $1 per day, valid 2026-04-08 to 2026-08-08. Source: [Gravity Points – Season 1 docs](https://saturncredit.gitbook.io/saturn-docs/overview/gravity-points-season-1), [Allocations](https://saturncredit.gitbook.io/saturn-docs/overview/allocations). The Merkl start date for each campaign is in brackets.
- **Ethereum**
  - Hold USDat 7× [2555; from 03-15]. Hold sUSDat 1× [from 03-15].
  - Curve USDC/USDat 20× [7300]. Curve USDC/sUSDat 18×.
  - Pendle LP USDat 15×. YT-USDat 30×. LP sUSDat 5×. YT-sUSDat 10×.
  - Morpho sUSDat collateral (Flowdesk) 2× [MORPHOCOLLATERAL 730]. Morpho Saturn USDC vault 1× [satUSDC from 06-15]. Flowdesk AUSD 1× [fAUSDe from 04-23].
  - Strata srUSDat 1× and jrUSDat 3× [1095] [both from 04-16].
  - Pendle LP srUSDat 7.5×, YT-srUSDat 15×, LP jrUSDat 5×, YT-jrUSDat 10× [all from 05-06].
- **BNB Chain** (from 05-20; Pendle from 05-25)
  - Hold USDat 9× [3285]. Stake/hold sUSDat 1.2× [438].
  - PancakeSwap USDT/USDat and USDT/sUSDat 24× in range.
  - Pendle LP USDat 18× [6570], YT-USDat 36× [13140], LP sUSDat 6× [2190], YT-sUSDat 12× [4380].
- **Monad** (from 07-14)
  - Hold USDat 9× [3285]. Stake 1.2× [438].
  - Curve USDC/USDat 20× [from 07-17].
  - Pendle LP USDat 19× [6935], YT-USDat 38× [13870], LP sUSDat 6.5× [2372.5], YT-sUSDat 13× [4745].
  - The docs label two Monad rows as "LP USDat 6.5x" and "yt-USDat 13x". Merkl shows these are sUSDat LP and YT-sUSDat, so the docs rows are typos.
- The S1 docs also say: "Incentives are subject to change during Season 1, but will be transparently communicated with forward guidance." — [S1 docs](https://saturncredit.gitbook.io/saturn-docs/overview/gravity-points-season-1)

### Cited Findings: rate changes S1 → S2 (dated)
All changes took effect on 2026-08-09.

| Activity | S1 | S2 |
|---|---|---|
| Hold USDat, Ethereum | 7× | 5× |
| Hold USDat, BNB/Monad | 9× | 5× |
| Stake sUSDat, BNB/Monad | 1.2× | 1× |
| Curve USDC/USDat | 20× | 25× |
| Curve USDC/sUSDat | 18× | 25× |
| PancakeSwap | 24× | 25× |
| jrUSDat | 3× | 5× |
| BNB Pendle rates | LP USDat 18×, YT-USDat 36× | 15× / 30× (unified across chains) |
| Monad Pendle rates | LP USDat 19×, YT-USDat 38× | 15× / 30× (unified across chains) |

Unchanged: Ethereum Pendle YT-USDat 30×, LP USDat 15×, YT-sUSDat 10×, LP sUSDat 5×. — [Allocations page (both tables)](https://saturncredit.gitbook.io/saturn-docs/overview/allocations)

### Cited Findings: temporary boosts on Merkl (not in the docs tables)
All are dated campaigns from the [Merkl API](https://api.merkl.xyz/v4/campaigns?creatorAddress=0x80c6a512B548229226C0676d6fdbAfF81d325990&items=100&page=0). An extra campaign on the same token stacks on top of the base campaign.
- **S1, 2026-05-06 to 05-11 (Strata Pendle launch):** a duplicate YT-srUSDat 15× and YT-jrUSDat 10× campaign, so effectively 2× (30× and 20×).
- **S1 "Gravity Accelerate" (ended 2026-06-06 09:00 EST):** 2× boost. Ethereum LP 30× and YT 60×; BNB LP 36× and YT 72×. — [Today in DeFi, 2026-06-03](https://news.todayindefi.com/p/airdrop-alpha-saturn-and-apyx-boosted). I could not identify this boost as a distinct Merkl FIX_APR campaign. It may sit inside the "INVALID"/manual-type campaigns.
- **S1, 2026-06-15 to 08-09:** a second Ethereum YT-USDat-27AUG2026 30× campaign (94.09B budget) ran alongside the original 30× campaign (97B budget, 03-15 to 08-15). Both were fully exhausted (see Q3 on budget caps).
- **S1 Monad, 2026-08-04 to 08-09:** extra campaigns for YT-USDat-14JAN2027 at 34.2× (plus the 38× base; the split budget suggests top-up campaigns), YT-sUSDat 13× ×2, and LP 19× / 6.5× duplicates.
- **S2 Monad launch boost, 2026-08-09 to 08-14:** duplicates of YT-USDat 30×, YT-sUSDat 10×, LP-USDat 15× and LP-sUSDat 5×, so 2× on Monad Pendle for 5 days.
- **S2, 2026-08-14 to 08-28:**
  - Ethereum and Monad YT-USDat-14JAN2027 +15× (total 45×). YT-sUSDat +5× (total 15×).
  - Ethereum LP-USDat +15× (total 30×). Monad LP-USDat +7.5× (total 22.5×).
  - LP-sUSDat +2.5× on both chains (total 7.5×).
- **S2, 2026-08-27 to 09-27:** Ethereum PT-USDat-14JAN2027 1.5× (APR 547.5), the only PT points campaign found. srUSDat +2× (total 3×). A small Pendle LP-USDat DUTCH_AUCTION campaign (0.91M budget).
- **Manual "JSON_AIRDROP" credits:**
  - Gravity: 652.6M on 2026-08-15 to 547 users; 10.3M on 2026-09-19.
  - Orbital: 79.3M on 2026-09-19; 62k on 2026-09-21.
- The PancakeSwap rate appears in Merkl as whitelisted USDat/sUSDat balance campaigns at 48× (S1) and 50× (S2) of the USDat or sUSDat side. Each is whitelisted to one address (0xF80Ab3Cc…, 0xf3396a9a…) with forwarding enabled. There are also PANCAKESWAP DUTCH_AUCTION campaigns. — [Merkl API](https://api.merkl.xyz/v4/campaigns?creatorAddress=0x80c6a512B548229226C0676d6fdbAfF81d325990&items=100&page=0)

### Cited Findings: referral and early-user boosts
- Referral: the referrer gets "10% of the qualifying Gravity Points earned by each eligible Referred User directly referred", and the referred user "may receive a 5% bonus on their own qualifying Gravity Points". There is "one referral layer only". The terms are effective 05/11/2026. — [Gravity Points Referral Program Terms](https://saturn.credit/legal/gravity-program)
- On-chain config matches: every Merkl campaign carries hook `gravity-saturn` with `valueForBoostForReferrer: 100000000` and `valueForBoostForInvited: 50000000`, i.e. 10% and 5% at 1e9 scale, `cumulativeBoost: true`. — [Merkl API](https://api.merkl.xyz/v4/campaigns?creatorAddress=0x80c6a512B548229226C0676d6fdbAfF81d325990&items=100&page=0)
- S1 participant boost: "Users who earned more than 1,000,000 Gravity Points during Season 1 will receive a 20% Orbital Points boost during Season 2." — [S2 docs](https://saturncredit.gitbook.io/saturn-docs/overview/orbital-points-season-2). This is implemented as Merkl hook `saturn-gravity-s1-boosts` (`boostingFunction: multiply`) on the S2 base campaigns.
- 3,480 of 8,100 S1 addresses hold more than 1M Gravity Points, so they qualify. — computed from the full [Merkl Gravity leaderboard](https://api.merkl.xyz/v4/rewards/token/?chainId=1&address=0xD223bbdd0421E394C0df9dFfe568f1dADfFd6f85&items=100&page=0)
- No NFTs, badges or quest programs (Galxe, Zealy) were found for Saturn points.

### Inferences
- Maximum stackable S2 rate per $1 per day for a referred user in the >1M S1 cohort: base × 1.20 (S1 boost) × 1.05 (referee bonus), about 1.26× base. Whether the two multiply or add is unconfirmed; Merkl `cumulativeBoost: true` suggests additive. For YT-USDat that gives about 36–37.8 points per YT per day. Referrers additionally receive 10% of their referees' points, which adds new points on top rather than taking them from the referee.
- PancakeSwap: 48× or 50× on the USDat side of a roughly 50/50 pool works out to about 24× or 25× per $ of LP. This matches the docs, which supports reading the whitelisted address as the pool.

### Gaps
- The Gravity Accelerate boost could not be matched to a specific Merkl campaign. The contents of the "INVALID"-type S1 campaigns (about 16.5B points, 3.3% of S1) are unknown and may be manual boosts or corrections.
- No official announcement text was found for the S2 temporary boosts (Aug 14–28, Aug 27–Sep 27). They are inferred from Merkl campaign data only.

---

## Q3. Pendle specifics: YT, LP, PT, SY, and how YT points are computed

### Takeaway
Pendle YT-USDat earns 30 Orbital points per YT unit per day in S2, on all chains. That is 30× the underlying $1 notional, not 30× the YT market value. YT-sUSDat earns 10× and YT-srUSDat 15×. Pendle LP earns 15× (USDat), 5× (sUSDat) and 7.5× (srUSDat) per $1 of LP value. PT normally earns 0; the one exception was a PT-USDat 1.5× campaign on Ethereum from Aug 27 to Sep 27, 2026. Points are paid directly to YT holders by Merkl's time-weighted balance tracker. This is the standard Pendle-style convention of points per YT = multiplier × underlying units.

YT campaigns have finite Merkl budgets. When YT supply exceeds what the budget supports, the effective multiplier falls below nominal. This has already happened to the Ethereum YT-USDat-27AUG2026 campaigns.

### Cited Findings
- **Merkl parameters for S2 YT campaigns:**
  - Ethereum YT-USDat-14JAN2027 (`0x480C3c94…`): `apr: 10950` (30×), `priceData: {YT → 0x23238f20… (USDat token)}`, `targetTokenPricing: true`, budget 97B Orbital, 2026-08-09 16:00 to 12-09 04:59 UTC.
  - Monad YT-USDat-14JAN2027 (`0x5aff25c8…`): same 30×, priced as Monad USDat (`0x0Bb150DF…`), budget 194B.
  - The S1 YT-USDat-27AUG2026 campaign used `targetTokenPricing: false`, meaning per token unit.
  - Source: [Merkl API](https://api.merkl.xyz/v4/campaigns?creatorAddress=0x80c6a512B548229226C0676d6fdbAfF81d325990&items=100&page=0)
- **On-chain YT supplies, 2026-09-28** (`totalSupply()`, 6 decimals):
  - [Ethereum YT-USDat-14JAN2027](https://etherscan.io/token/0x480c3c9470fa4bbda030f6396fa4b17adefc1ce0): 20,132,267
  - [Monad YT-USDat-14JAN2027](https://monadscan.com/token/0x5aff25c86c7cb739e554be8904b32047738b7440): 43,021,394
  - BNB YT-USDat-14JAN2027 (`0x99010c74…`): 70,825
  - Ethereum YT-sUSDat-14JAN2027 (`0xc38901aa…`): 5,346,340
  - Monad YT-sUSDat (`0x3ebb9764…`): 4,539,882
  - Ethereum YT-srUSDat (`0xf26e7953…`): 809,418
  - Monad YT-srUSDat (`0x0435a599…`): 986,296
  - Addresses come from the [Pendle API](https://api-v2.pendle.finance/core/v1/1/markets/active)
- **Evidence that YT is valued at $1 underlying for distribution:**
  - Merkl's opportunity TVL for "Hold YT USDat 14JAN2027" is $503,654. That equals 20.13M YT × the YT market price of $0.02502, and its displayed daily reward of 15.1M is 30 × that value. — [Merkl opportunity 13354597549279540508](https://api.merkl.xyz/v4/opportunities/13354597549279540508); YT price from [Pendle market API](https://api-v2.pendle.finance/core/v1/1/markets/0x4ccf6deb3d1895373f604b418ff55d8adae8b846)
  - But actual distributions are about 30 per YT unit. The Monad YT-USDat-14JAN2027 S2 campaign has already paid 41.49B points to 1,021 addresses in 50.3 days. At market-price valuation (about $0.03–0.05 per YT × 43M YT × 30) it could have paid only about 2–3B.
  - A holder of 3,235,216 ETH YT-USDat (0x3763a100…) has 647.9M points in that campaign with 18.19M pending. That pending amount is about 4.5 h of 30 × 3.235M = 97M/day, versus about 7.5 days at YT-price valuation. — [Merkl campaign rewards list](https://api.merkl.xyz/v4/rewards/?chainId=1&campaignId=0xc1e3cc5480ae78be877d38dc1058a6b2cbc0d82d074e71f4ded2122df849eb81&items=5), balance via Ethereum RPC `balanceOf`
- **Budget caps:**
  - FIX_APR campaigns have a fixed `amount`. Unused budget accrues to the creator address, which held 2.953e12 Gravity and 9.325e11 Orbital "leftover" points. — [Merkl token total](https://api.merkl.xyz/v4/rewards/token/total?chainId=1&address=0x10710501778b7FAf9e478f36FaE0B286C028eDE8), [leaderboard](https://api.merkl.xyz/v4/rewards/token/?chainId=1&address=0x10710501778b7FAf9e478f36FaE0B286C028eDE8&items=15)
  - Three campaigns paid users exactly 100% of their budget, which means they were capped:
    - S1 Ethereum YT-USDat-27AUG2026 (97B over 03-15 to 08-15, cap 634M/day)
    - S1 Ethereum YT-USDat-27AUG2026 top-up (94.09B over 06-15 to 08-09, cap 1.706B/day)
    - S2 Ethereum YT-USDat-27AUG2026 (19.4B over 08-09 to 08-27, cap 1.078B/day)
  - Source: per-campaign sums from [Merkl rewards endpoint](https://api.merkl.xyz/v4/rewards/?chainId=1&campaignId=0x0b114cad59943478ddc9425cf2cefaec7606632b4fc3f5acadb6c46437e95433&items=100)
- **Pendle LP:** Merkl TVL for "LP in Pendle USDat 14JAN2027" (Ethereum) is $1,958,359, the same as Pendle market liquidity of $1,957,470. The daily reward is 29.4M (15×). So LP points are per $ of full LP value. — [Merkl opportunity 6928984681703931525](https://api.merkl.xyz/v4/opportunities/6928984681703931525), [Pendle market data](https://api-v2.pendle.finance/core/v2/1/markets/0x4ccf6deb3d1895373f604b418ff55d8adae8b846/data)
- **PT:** the only PT campaign found is Ethereum PT-USDat-14JAN2027, APR 547.5 (1.5×), 2026-08-27 to 09-27. It paid only 33.9M points to users. The docs list no PT rate. KOL DEFI Kadic wrote: "Holding Pendle PT-USDat also grants more Saturn points multiplier". — [Merkl API](https://api.merkl.xyz/v4/campaigns?creatorAddress=0x80c6a512B548229226C0676d6fdbAfF81d325990&items=100&page=0); [KuCoin insight – DEFI Kadic, 2026-09-24](https://www.kucoin.com/news/insight/STRC/6ab4e07874fd460007c529d3)
- **SY:** Pendle SY campaigns existed only as small DUTCH_AUCTION campaigns in Mar–May and Jul 2026 (S1). They paid negligible amounts.
- **Pendle market data, Ethereum USDat 14JAN2027, 2026-09-28:**
  - impliedApy 8.98%, YT price $0.02502, ptDiscount 2.50%, ytRoi −66.4%.
  - underlyingApy 3% (an "EXTERNAL_REWARD" in USDC; underlyingInterestApy 0).
  - Market liquidity $1.96M, total market TVL $20.45M.
  - Other markets: Monad USDat impliedApy 9.10%; Ethereum sUSDat 12.92%; Monad sUSDat 17.41%.
  - Sources: [Pendle API v2 data](https://api-v2.pendle.finance/core/v2/1/markets/0x4ccf6deb3d1895373f604b418ff55d8adae8b846/data); [Pendle active markets Monad](https://api-v2.pendle.finance/core/v1/143/markets/active)
- **Pendle UI points badge:** the Pendle API market object had `points: null`. I could not confirm the badge text from the Pendle UI.

### Inferences
- **Current S2 accrual per YT-USDat-14JAN2027:**
  - Base: 30 points/day.
  - With the S1-holder boost: 36/day. Adding the 5% referee bonus: about 37.5/day.
  - From 2026-09-28 12:00 UTC to S2 end (2026-12-09 04:59 UTC, 71.7 days): about 2,151 base points per YT (about 2,580 with the 20% boost).
  - YT-sUSDat: about 717 points. YT-srUSDat: about 1,076 points.
- **Cap headroom** (cap/day ÷ 30 = maximum YT supply that still earns the full 30×):
  - Ethereum YT-USDat campaign: 97B / 121.54 d = 798M/day, which supports about 26.6M YT at 30×. Current supply is 20.1M (76% of cap).
  - Monad YT-USDat campaign: 194B / 122.04 d = 1.590B/day, which supports about 53.0M YT. Current supply is 43.0M (81% of cap).
  - If boosts are applied inside the budget, the effective cap is lower.
  - If YT supply keeps growing past these levels, points per YT will fall below 30 unless Saturn tops up the budget, as it did in S1 on 06-15.
- Merkl's own UI "TVL" and APR for YT opportunities value YT at market price. This understates true YT point emissions by about 40×. Anyone reading Merkl dashboards should correct for this.
- After the S2 snapshot, YT-14JAN2027 holders will presumably earn Season 3 points until expiry on Jan 14, 2027, about 36 days if S2 runs to Dec 8. S3 rates and allocation are unknown.

### Gaps
- There is no official statement that YT points are computed on underlying notional. That conclusion is inferred from Merkl `priceData` (YT → USDat) and realized distributions, which I consider high confidence.
- Merkl's exact cap logic and whether boosts are paid inside or outside the campaign budget are not documented in what I could access.
- Spectra, Euler and Aave have no Saturn points campaigns on Merkl. The app strategies page mentions "Morpho and Euler", but no Euler points rate was found.

---

## Q4. Total points outstanding, daily emission, projections and inflation

### Takeaway
- **S1 (final):** about 474–497 billion Gravity Points across 8,100 addresses. The top 10 hold 39.7% and the top 100 hold 70.6%.
- **S2 to date (2026-09-28):** about 150–156 billion Orbital Points across 8,002 addresses.
- **Current S2 emission:** about 2.8B Orbital/day at base rates, with YT valued at underlying. That is roughly 2.8–3.4B/day once the 20% S1 boost and referral bonuses are included. YT-USDat holders on Ethereum and Monad receive about 68% of base daily emission.
- **Projected S2 total at the Dec 8 end:** about 350–400B.
- **Implied inflation:** the S2 stock grows about 1.9–2.3% per day now and will roughly 2.3–2.6× from today to Dec 8.

### Cited Findings
- **Totals:**
  - Merkl token total for Gravity Points is 3.4277e12, of which the creator address holds 2.9532e12 (unallocated or returned budget). Users therefore hold **4.7445e11**.
  - Orbital total is 1.0824e12 with creator 9.3252e11, so users hold **1.5017e11**, including 2.92e8 pending.
  - Sources: [Gravity total](https://api.merkl.xyz/v4/rewards/token/total?chainId=1&address=0xD223bbdd0421E394C0df9dFfe568f1dADfFd6f85); [Orbital total](https://api.merkl.xyz/v4/rewards/token/total?chainId=1&address=0x10710501778b7FAf9e478f36FaE0B286C028eDE8); [Gravity leaderboard](https://api.merkl.xyz/v4/rewards/token/?chainId=1&address=0xD223bbdd0421E394C0df9dFfe568f1dADfFd6f85&items=15); [Orbital leaderboard](https://api.merkl.xyz/v4/rewards/token/?chainId=1&address=0x10710501778b7FAf9e478f36FaE0B286C028eDE8&items=15)
  - Cross-check by summing per-campaign recipient lists: S1 users 4.967e11, S2 users 1.561e11. That is about 4% higher than the token-level totals, possibly because of reallocations or forwarding. This is the reason for giving ranges. — [Merkl rewards per campaign](https://api.merkl.xyz/v4/rewards/?chainId=1&campaignId=0xc1e3cc5480ae78be877d38dc1058a6b2cbc0d82d074e71f4ded2122df849eb81&items=100)
  - The Saturn app's creator-address call returns the same figures: S1 amount 2953224539939617291906846722068 (2.953e12) and S2 932518048324901460433516300868 (9.325e11). — [app.saturn.credit/api/points/0x80c6…?season=2&snapshot=806](https://app.saturn.credit/api/points/0x80c6a512B548229226C0676d6fdbAfF81d325990?season=2&snapshot=806)
- **Distribution statistics** (computed from the full leaderboards, about 81 pages each):
  - S1: median holder 408k points; 3,480 holders above 1M; 61 above 1B. Top 1 holds 8.0%, top 10 39.7%, top 50 62.2%, top 100 70.6%, top 1,000 95.2%.
  - S2: median 47.8k; 2,068 holders above 1M; 28 above 1B. Top 1 holds 12.5%, top 10 41.4%, top 100 77.4%, top 1,000 97.7%.
  - The largest wallet in both seasons is 0x2843dff4…: 38.0B Gravity and 18.7B Orbital. It currently holds 614,729 YT-USDat on Ethereum.
  - Source: [Merkl leaderboard pages](https://api.merkl.xyz/v4/rewards/token/?chainId=1&address=0x10710501778b7FAf9e478f36FaE0B286C028eDE8&items=100&page=0)
- **S1 points by activity** (users only, sum of per-campaign lists, 4.967e11 total):

| Activity | Share of S1 |
|---|---|
| Pendle YT-USDat (all chains) | 56.1% (278.8B) |
| Curve LP/gauge | 10.5% |
| Hold USDat | 8.9% |
| Pendle YT-sUSDat | 6.4% |
| Pendle LP-USDat | 5.9% |
| Manual "INVALID" campaigns | 3.3% |
| PancakeSwap | 2.5% |
| YT-srUSDat | 2.0% |
| Morpho/lending | 1.3% |
| LP-sUSDat | 1.2% |
| Hold sUSDat | 0.8% |

  By chain: Ethereum 368B, BNB 104B, Monad 25B. — derived from [Merkl per-campaign rewards](https://api.merkl.xyz/v4/rewards/?chainId=1&campaignId=0x0b114cad59943478ddc9425cf2cefaec7606632b4fc3f5acadb6c46437e95433&items=100)
- **S2 points by activity to date** (1.561e11 total):

| Activity | Share of S2 so far |
|---|---|
| Pendle YT-USDat | 60.7% (94.8B) |
| Curve LP/gauge | 11.6% |
| Hold USDat | 9.9% |
| YT-sUSDat | 5.6% |
| LP-USDat | 4.3% |
| PancakeSwap | 2.3% |
| Hold sUSDat | 1.6% |
| YT-srUSDat | 1.5% |
| LP-sUSDat | 1.0% |
| Morpho | 0.7% |
| PT-USDat | 0.02% |

  By chain: Ethereum 77.5B, Monad 66.4B, BNB 12.2B.
  The largest single S2 campaigns are Monad YT-USDat-14JAN2027 30× (41.5B, 1,021 users), Ethereum YT-USDat-27AUG2026 (19.4B, capped), Ethereum YT-USDat-14JAN2027 (14.9B), Ethereum Curve USDC/USDat (12.5B) and Ethereum Hold USDat (11.8B). — same Merkl source
- **Live S2 daily emission, Merkl rewardsRecord at 2026-09-28 00:00 UTC** (38 live opportunities, 18-dec amounts): the Merkl-displayed total is 828.5M Orbital/day over $144M of tracked TVL. Selected lines:

| Opportunity | TVL | Orbital/day |
|---|---|---|
| Hold USDat, Ethereum | $55.05M | 275.3M |
| Curve USDC-USDat, Ethereum | $9.47M | 236.9M |
| Curve USDat-USDC, Monad | $2.33M | 58.3M |
| Hold sUSDat, Ethereum | $45.28M | 45.3M |
| Curve gauge, Ethereum | $1.42M | 42.5M |
| Pendle LP USDat, Ethereum | $1.96M | 29.4M |
| Pendle LP USDat, Monad | $1.47M | 22.0M |
| Morpho AUSD borrow | $5.68M | 11.4M |
| jrUSDat | $1.98M | 9.9M |
| Pendle LP sUSDat, Monad | $1.62M | 8.1M |
| Pendle LP sUSDat, Ethereum | $1.35M | 6.8M |
| srUSDat | $4.99M | 5.0M |
| Flowdesk AUSD | $4.98M | 5.0M |
| PancakeSwap USDat-USDT | $0.125M | 3.8M |
| Saturn USDC vault, Monad | $1.93M | 1.9M |
| Saturn USDC vault, Ethereum | $0.92M | 0.9M |

  - YT lines at YT market price: ETH YT-USDat $0.50M → 15.1M/day; Monad YT-USDat $1.09M → 32.7M/day.
  - Sources: [Merkl opportunities](https://api.merkl.xyz/v4/opportunities/11602167019406774224), e.g. [7327235486235463977](https://api.merkl.xyz/v4/opportunities/7327235486235463977), [12559560247831882498](https://api.merkl.xyz/v4/opportunities/12559560247831882498)
- **Other TVL context:**
  - 2026-09-24: TVL $138M, split USDat $70.8M and sUSDat $69.8M; sUSDat APY about 13.8%. — [KuCoin insight – TECA, 2026-09-24](https://www.kucoin.com/news/insight/STRC/6ab5320974fd460007c533d6)
  - S1 peak about $248M, then about $180M. — [S2 docs](https://saturncredit.gitbook.io/saturn-docs/overview/orbital-points-season-2)
  - May 2026: TVL above $125M. — [Phemex news on seed round](https://phemex.com/news/article/saturn-credit-secures-2m-in-seed-funding-led-by-the-spartan-group-79735)

### Inferences (estimates; method shown)
- **Corrected current base S2 emission.** Take the non-YT Merkl rewards (828.5M − 52.6M YT lines = 776.0M/day) and add YT at $1 underlying:

| Line | Calculation | Orbital/day |
|---|---|---|
| ETH YT-USDat | 20.132M × 30 | 604.0M |
| Monad YT-USDat | 43.021M × 30 | 1,290.6M |
| BNB YT-USDat | 0.071M × 30 | 2.1M |
| ETH YT-sUSDat | 5.346M × 10 | 53.5M |
| Monad YT-sUSDat | 4.540M × 10 | 45.4M |
| ETH YT-srUSDat | 0.809M × 15 | 12.1M |
| Monad YT-srUSDat | 0.986M × 15 | 14.8M |
| **YT subtotal** | | **2,022.5M** |
| **Base total** | 776.0M + 2,022.5M | **≈2.80B** |

  Add the S1 boost (+20% for >1M-point holders, who likely hold most TVL given S1 top-1,000 = 95% of points) and referral (+5% referee, +10% to referrer). **Effective emission ≈ 2.8–3.4B Orbital/day** (assumption: a 0–20% uplift in aggregate).
- **Cross-check:** S2 users hold 150–156B after 50.3 days, an average of about 3.0–3.1B/day. The average includes the Aug 9–27 expiring markets and the Aug 14–28 and Aug 27–Sep 27 boosts, and is consistent with the estimate above.
- **Projected S2 outstanding** (range from 150–156B today plus 2.8–3.4B/day). At constant YT supply; emissions rise if TVL or YT supply grows, subject to the campaign caps in Q3.

| Date | Days from now | Added | S2 total | Share of full S2 duration |
|---|---|---|---|---|
| 2026-10-31 | +32.7 | +92–111B | ≈242–267B | 68.0% |
| 2026-11-15 | +47.7 | +134–162B | ≈284–318B | 80.3% (so about 4.02% of supply) |
| 2026-12-01 | +63.7 | +178–217B | ≈328–373B | 93.4% |
| 2026-12-08 end | +71.7 | +201–244B | ≈351–400B | 100% |

- **Inflation:** 2.8–3.4B/day on a 150B stock is about 1.9–2.3% per day now, falling to about 0.8% per day by December as the stock grows. S1 Gravity stock is essentially fixed at about 474–497B; small manual credits are still appearing, such as +10.3M on 2026-09-19.
- **Points per token (the season allocation is from Q5):**
  - S1: 5% of supply ÷ about 485B Gravity gives $/Gravity point ≈ 0.05 × FDV / 4.85e11 ≈ **1.03e-13 × FDV**. At $100M FDV that is $1.03e-5 per point ($10.3 per 1M points); at $300M, $3.1e-5.
  - S2: 5% × (days run / 122.04) ÷ S2 points at snapshot. With full-term S2 of about 375B, $/Orbital point ≈ **1.33e-13 × FDV**, or $1.33e-5 at $100M FDV.
  - Under the pro-rata rule an earlier TGE gives nearly the same ratio. For a Nov 15 TGE: 4.02% / about 301B ≈ 1.34e-13 × FDV.
  - An Orbital point is therefore worth about 1.3× a Gravity point if both seasons get 5%.
- **Illustrative YT-USDat value from S2 points only** (no S3, no boosts): 2,151 points × 1.33e-13 × FDV ≈ **2.9e-10 × FDV per YT**. That is $0.029 at $100M FDV, $0.058 at $200M and $0.145 at $500M.
  - Compare the Ethereum YT price of $0.025 on 2026-09-28. Of that, about $0.009 is the 3% underlying yield on $1 for 108 days.
  - The market therefore implies a points-breakeven FDV of about $55M for non-boosted holders, before S3 accrual (Dec 9–Jan 14) and before any dilution from YT supply growth.
  - These are inferences on unconfirmed FDV and supply, for the report writer to stress-test.

### Gaps
- Total STRN supply and FDV are unannounced. Nothing public says whether referral points or S1-boost points come out of the same 5% (presumably yes, since they are just points).
- The aggregate uplift from boosts and referrals on daily emission could not be measured directly. Merkl's historical-diff endpoint needs an API key.
- Some leaderboard recipients may be contracts. I did not filter them.

---

## Q5. Official token allocation to points, multiple seasons, dilution

### Takeaway
- S1 (Gravity): up to 5% of initial STRN supply, pro-rata to S1 points.
- S2 (Orbital): up to 5% of supply, pro-rated if S2 ends early.
- Season 3 is confirmed to follow immediately.

Seasons have separate allocations, so S2 points do not dilute S1 tokens in the stated framework. Within a season, all points share that season's fixed allocation. No total community or airdrop percentage, total supply or vesting has been disclosed.

### Cited Findings
- "The Saturn Foundation may allocate up to 5% of the initial token supply to Season 1 participants… distributed proportionally based on the Gravity points held at the end of Season 1". It is conditioned on launch of the governance token. The Bitget article calls the token "STRC", which is an error; STRC is Strategy's preferred stock. — [Bitget News](https://www.bitget.com/news/detail/12560605400930); also quoted in [2lambroz Substack, 2026-05-20](https://2lambroz.substack.com/p/11-yield-with-zero-strc-risk-i-had)
- "The Saturn Foundation may allocate up to 5% of the initial token supply to Season 2 participants, conditioned on the launch of the Saturn governance token." — [S2 docs](https://saturncredit.gitbook.io/saturn-docs/overview/orbital-points-season-2)
- "They confer no rights to any future token or airdrop, except Season 1, which is conditioned on the launch of the Saturn governance token – the timing, terms, and existence of which are not committed or guaranteed." — [S2 docs](https://saturncredit.gitbook.io/saturn-docs/overview/orbital-points-season-2)
- TGE announcement (2026-09-25): STRN, Q4 2026, S2 up to 5% pro-rata. Unallocated S2 tokens return "to the Saturn ecosystem allocation pool for future seasons". Season 3 starts immediately after the snapshot. — [ChainCatcher](https://www.chaincatcher.com/en/article/2292229); [KuCoin flash](https://www.kucoin.com/news/flash/saturn-plans-tge-in-q4-2026-allocates-up-to-5-supply-for-second-season)
- Funding context: $2M seed (May 2026) led by The Spartan Group with Anchorage and Susquehanna Crypto, plus an $800K angel round (Jan 2026), for $2.8M total. — [airdrops.io, updated 2026-09-25](https://airdrops.io/saturn-credit/); [Phemex](https://phemex.com/news/article/saturn-credit-secures-2m-in-seed-funding-led-by-the-spartan-group-79735)

### Inferences
- Combined S1+S2 is up to 10% of initial supply. S3 has an unknown allocation, possibly funded partly by pro-rata leftovers from S2.
- A low raise ($2.8M) with a 5%+5% points allocation means the $/point outcome depends heavily on the TGE FDV. No official FDV anchor exists.

### Gaps
- No total supply, no full tokenomics and no Season 3 allocation. No statement on whether the 5% figures are "initial supply" or "total supply": the docs say "initial token supply" while the TGE news says "total token supply".

---

## Q6. Anti-sybil rules, lockups/vesting, claim conditions, eligibility

### Takeaway
Eligibility rules are strict: geofencing and KYC or permissioning. Referral anti-abuse terms are extensive. Saturn keeps full discretion to adjust, reverse or claw back points. No vesting or lockup schedule for the airdrop has been announced; it is "to be disclosed".

### Cited Findings
- S2 docs: "Not available to persons in the United States, the EEA, the UK, or any sanctioned jurisdiction." — [S2 docs](https://saturncredit.gitbook.io/saturn-docs/overview/orbital-points-season-2). The S1 docs say US and EEA users "will be geofenced and blocked". — [S1 docs](https://saturncredit.gitbook.io/saturn-docs/overview/gravity-points-season-1)
- "USDat is a permissioned token. Only addresses that have completed Saturn's onboarding process can mint, redeem, or hold USDat." — [USDat Overview docs](https://saturncredit.gitbook.io/saturn-docs/solution/usdat-overview)
- Referral terms (effective 2026-05-11):
  - Excluded jurisdictions: US, EEA, UK, Canada, Singapore, Hong Kong, PRC and sanctioned jurisdictions.
  - KYC, AML and sanctions screening may be required for both referrer and referee.
  - Bans self-referral, duplicate, Sybil, bot, nominee and coordinated accounts, and VPN or proxy evasion.
  - Caps may apply per referrer, per user and at device, IP, wallet or household level.
  - Points "may be modified, reduced, reversed, suspended… or cancelled". "No participant may rely on any Gravity Points balance as final, vested… unless and until Saturn expressly states otherwise in writing."
  - Source: [Gravity Points Referral Program Terms](https://saturn.credit/legal/gravity-program)
- Merkl campaigns carry blacklists: for example 5 addresses on the AUSD borrow campaign and 4 on the USDat hold campaigns, presumably protocol contracts. — [Merkl API](https://api.merkl.xyz/v4/campaigns?creatorAddress=0x80c6a512B548229226C0676d6fdbAfF81d325990&items=100&page=0)
- TGE announcement: "specific token economic model, distribution, and claiming arrangements will be disclosed in subsequent announcements"; "no action is required from users at this time". — [ChainCatcher](https://www.chaincatcher.com/en/article/2292229); [KuCoin flash](https://www.kucoin.com/news/flash/saturn-plans-tge-in-q4-2026-allocates-up-to-5-supply-for-second-season)

### Inferences
- Allocation claims will probably need non-restricted-jurisdiction status and perhaps KYC, since USDat itself is permissioned. Farmers in excluded jurisdictions face forfeiture risk.
- The referral terms reserve heavy discretion, so a post-hoc sybil filter at TGE is possible, though nothing specific has been announced.

### Gaps
- There is no information on vesting or partial TGE unlock (Ethena, Usual or Falcon-style), claim windows, or a minimum points threshold.

---

## Q7. Community sentiment, farming strategies and $/point estimates

### Takeaway
Public commentary is mostly neutral how-to content: KOL "playbooks" pushing YT-USDat at 30× as "the fastest way to stack Saturn Points", Curve 25× and Morpho looping. I found **no explicit published $/point estimate** from any KOL. The only valuation anchor is an illustrative "$100M FDV × 5% to S1" assumption. I found no public dilution complaints; Discord, Telegram and X were not reachable.

### Cited Findings
- DEFI Kadic (2026-09-24) lists five strategies:
  1. Hold USDat, 3% APR, "upgraded in September".
  2. sUSDat at 13.85% APY.
  3. Pendle PT up to 17.41% fixed (Monad PT-sUSDat).
  4. "Pendle YT-USDat/YT-sUSDat… the fastest way to stack Saturn Points".
  5. Morpho looping "50% to over 100%" APY.
  - The same author also claims "Holding Pendle PT-USDat also grants more Saturn points multiplier".
  - Source: [KuCoin insight – DEFI Kadic](https://www.kucoin.com/news/insight/STRC/6ab4e07874fd460007c529d3)
- DEFI Kadic (2026-09-25) summarizes S2: "Up to 5% of $STRN is set aside for the Season 2 alone". Multipliers: Hold USDat 5×, "LP on Pendle (buy PT assets) 15×", LP on Curve 25×, YT 30×. "The amount of points on Season 2 directly affect the $STRN allocation for each user". — [KuCoin insight](https://www.kucoin.com/news/insight/PENDLE/6ab625c874fd460007c54ed9)
- TECA (2026-09-24) gives TVL $138M, sUSDat about 13.8% APY and STRC backing 96.7%. Multiplier table: USDat 5×, Curve 25×, sUSDat 1×, YT-USDat 30×, jrUSDat 5×. It describes a PT carry trade ("~6.7% PT yield vs ~4.8% Morpho borrowing"). — [KuCoin insight – TECA](https://www.kucoin.com/news/insight/STRC/6ab5320974fd460007c533d6)
- 2lambroz.eth (2026-05-20) gives an illustrative "$100M FDV with 5% allocation to S1". The author criticizes Saturn's opacity ("Token doesn't exist yet with no name, supply, or TGE date announced") versus Apyx ("100M fixed supply, 5% to S1, 4% to S2"). — [2lambroz Substack](https://2lambroz.substack.com/p/11-yield-with-zero-strc-risk-i-had)
- Today in DeFi (2026-06-03) recommends bridging sUSDat to BNB for higher multipliers during Gravity Accelerate (YT 72×), noting "every day of the campaign counts". — [Today in DeFi](https://news.todayindefi.com/p/airdrop-alpha-saturn-and-apyx-boosted)
- airdrops.io (updated 2026-09-25) rates farming "Medium" difficulty and "Medium" cost. It states "No conversion formula from Orbital Points to STRN tokens has been published yet". — [airdrops.io](https://airdrops.io/saturn-credit/)
- Errors in third-party sources, to flag:
  - airdrops.io labels S1 rates (Curve 20×/18×, USDat 7×) as "Orbital" multipliers. — [airdrops.io](https://airdrops.io/saturn-credit/)
  - 2lambroz lists "Pendle sUSDat LP 7.5x" (7.5× is srUSDat LP) and "PT-USDat… 30x". — [2lambroz](https://2lambroz.substack.com/p/11-yield-with-zero-strc-risk-i-had)
  - The official docs and Merkl data contradict both. — [Allocations docs](https://saturncredit.gitbook.io/saturn-docs/overview/allocations)
- CryptoRank has a Saturn drophunting page, but it returned HTTP 403 to the fetcher. — [CryptoRank](https://cryptorank.io/drophunting/saturn-protocol-activity1153)

### Inferences
- With no community $/point estimates, the report writer should use the FDV-parametric formulas in Q4: $/Gravity pt ≈ 1.03e-13 × FDV and $/Orbital pt ≈ 1.33e-13 × FDV. The only published FDV anchor is 2lambroz's illustrative $100M.
- Points are highly concentrated: the top 10 hold about 40% in each season, and YT-USDat accounts for about 56–61% of all points. The YT-USDat market is effectively where the points economy is decided. Pricing of YT therefore reflects the market's implied STRN FDV; see the Q4 inference of about $55M breakeven for Ethereum YT at $0.025.

### Gaps
- I could not access X (mirrors down), Discord or Telegram. No dilution complaints, no KOL $/point numbers and no community spreadsheets were found in indexed sources. I found no Dune dashboard or DefiLlama airdrop entry for Saturn points.
