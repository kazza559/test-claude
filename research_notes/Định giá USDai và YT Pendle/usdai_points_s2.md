# USD.AI points program (Allo / "Flatiron" = Allo Game Season 2): mechanics, rates, issuance, conversion to CHIP — as of 2026-09-28

Research date: 2026-09-28 (all live API / on-chain snapshots taken 2026-09-28 11:40–12:10 UTC unless stated otherwise).
Convention used below: **"Nx" = N Allo points per $1 (or per 1 YT of underlying notional) per day** — this unit was verified empirically (see Q2 "Unit verification").
Labels: **[OFFICIAL]** = USD.AI docs/blog/API; **[COMMUNITY]** = third-party/analyst; **[DERIVED]** = my calculation (formula shown).

Source-quality warning: the Medium account "@USD-ai" ("USD.AI Airdrop: CHIP Rewards, Yield & Season 2 Points", 2026-04-08) that ranks high in search links every CTA to `referal-l439.pages.dev` (not a usd.ai domain) and invents the name "Flatiron Points" as a separate framework. Treat it as **unofficial / likely phishing**; it is NOT used as a source for any number below. — [Medium article](https://medium.com/@USD-ai/usd-ai-airdrop-%EF%B8%8Fstaking-flatiron-points-and-chip-rewards-ca5706942aa2)

---

## Q1. Program name, Season 1 history, Season 2 dates, Season 3

### Takeaway
The points are called **Allo™** ("Allo points"; API calls them "XP"). Season 1 = "The Allo Game" (Aug 2025 → **2026-02-18**), which converted into 10% of CHIP supply (7% ICO rights at $0.03 + 3% free airdrop). Season 2 = **"Flatiron" (Allo Game S2)**: accrual started **2026-02-19 00:00 UTC**, rewards 100% as a CHIP airdrop, official end **2026-10-14** (Oct-maturity Pendle rates drop to 0 at 2026-10-15 00:00 UTC). **No Season 3 has been announced**, but the 24-FEB-2027 Pendle markets already carry open-ended Allo rates with no end date.

### Cited Findings
**Name / system**
- "Allo™ is the rewards system for the USD.AI protocol"; earned via Deposits (alignment/strategy/amount) and Team (10% of referred members' activity). [OFFICIAL] — [docs: Allo (Points)](https://docs.usd.ai/app-guide/depositor/allo-points)
- API internally names points "xp" (e.g. `xpState.totalXp`, `inviteXp`); public endpoints `/usdai/public/total-allo?season=N`, `/usdai/wallets/leaderboard?season=N`. [OFFICIAL] — [API total-allo S2](https://api.usd.ai/usdai/public/total-allo?season=2)

**Season 1 ("The Allo Game")**
- Launched publicly with blog of 2025-08-20. Two "alignments": USDai → ICO alignment; sUSDai → Airdrop alignment. Game ends when $20M total yield paid or 6 months pass. At end "10% of the total supply is allocated to Allo Game participants, of which 70% flows to ICO Alignment and 30% to Airdrop Alignment… ICO participants will be able to purchase 7% of the total token supply at a $300m FDV. Airdrop Alignment will receive 3% of the total supply." Tokens fully unlocked at TGE. KYC for ICO side. [OFFICIAL] — [The Allo Game (2025-08-20)](https://usd.ai/insights/the-allo-game)
- S1 base rates: ICO/USDai base 5x Allo; Airdrop/sUSDai base 2x Allo; airdrop requires Airdrop Alignment higher than the protocol average; you cannot get both ICO and airdrop from one wallet. [OFFICIAL] — [docs: Allo (Points)](https://docs.usd.ai/app-guide/depositor/allo-points)
- S1 multiplier history: AutoUSDai vault 15x for a 30-day lock, ending 2025-11-07, then standard 10x. [OFFICIAL] — [Sunsetting Auto Strategy Vaults (2025-10-29)](https://usd.ai/insights/sunsetting-auto-strategy-vaults). Pendle YT-USDai Allo multiplier cut from 30x to 15x on 2025-11-18; YTs had 12–15x base Allo but 25–30x alignment multiplier (search-snippet summary of Dune blog; not fully verified) — [Dune blog "The Pendle Effect"](https://dune.com/blog/the-pendle-effect). In S1 YT-sUSDai = 12x vs YT-USDai = 25x (Sep 2025) — [PendleIntern (2025-09-03)](https://x.com/PendleIntern/status/1963062355316899892)
- Final week of S1: "Alignment multipliers for YTs for both USDai and sUSDai are being increased to 60x." [OFFICIAL] — [Season 1 Finale: Level Up (2026-02-12)](https://usd.ai/insights/level-up-finale)
- S1 end date **2026-02-18**; ICO on CoinList 2026-02-22 23:00 UTC → 2026-02-27 23:00 UTC at **$0.03/CHIP, $300M FDV, 700,000,000 CHIP (7%)**, 100% unlocked, min $100. Airdrop: CHIP sent to default wallet at TGE, no minimum. "If you have no alignment when the Allo Game ends, your Allo points will be burned." [OFFICIAL] — [CHIP ICO, Airdrop, and What's Next (2026-02-09)](https://usd.ai/insights/chip-ico-airdrop)
- S1 totals (live API, 2026-09-28): total S1 Allo = **1,771,968,655,930 (≈1.772T)**; ICO-aligned = **922,906,625,709 (20,023 wallets)**; Airdrop-aligned = **755,060,221,630 (25,444 wallets)**. [OFFICIAL API] — [total-allo S1](https://api.usd.ai/usdai/public/total-allo?season=1); [alignment-leaderboards S1](https://api.usd.ai/usdai/wallets/alignment-leaderboards?season=1)
- "Level Up" bridge (Feb 18–25, 2026): lock Pendle YTs to a "Level Up Score" derived from S1 allocation (per 1 CHIP: ~0.18 YT-USDai or ~0.40 YT-sUSDai). ICO path: Boost Own (4-mo, refund right at $300M, discount to $270M FDV at maturity) / Max Own (8-mo, $190M FDV). Airdrop path: Boost Earn ($350M implied buyout) / Max Earn ($420M) — irreversible, "burning your points for a fixed payout." All Level Up paths "Earn S2 points." [OFFICIAL] — [Level Up finale (2026-02-12)](https://usd.ai/insights/level-up-finale); [Level Up Guide (2026-02-26)](https://usd.ai/insights/allo-game-to-flatiron-level-up-guide)
- TGE / listing: CHIP went live 2026-04-21 (article dated 2026-04-22); total supply 10,000,000,000; contract 0x0c1c1c109fe34733fca54b82d7b46b75cfb71f6e; claim deadline 2026-05-30; Level Up airdrop buyout USDC sent 2026-04-20; protected ICO CHIP unlocks at YT maturity (2026-06-17 and/or 2026-10-14). [OFFICIAL] — [$CHIP Is Live](https://usd.ai/insights/chip-is-live)

**Season 2 ("Flatiron")**
- "Chapter 2: Flatiron moves to a single points system with rewards distributed entirely through airdrops. There is no ICO path or alignment. Points earned from Level Up YT locks carry forward… deposit caps are removed, and looping strategies… will be fully supported. Looping will be the thematic points goal for Flatiron." [OFFICIAL] — [Level Up Guide (2026-02-26)](https://usd.ai/insights/allo-game-to-flatiron-level-up-guide)
- "Flatiron is live… all rewards will be distributed through $CHIP airdrops… Multipliers range from 1x to 40x… **Flatiron runs through Oct 14, 2026.**" [OFFICIAL] — [$CHIP Is Live (2026-04-22)](https://usd.ai/insights/chip-is-live); reiterated "Earn points through October 14, 2026 for the S2 $CHIP airdrop" — [July recap (2026-08-05)](https://usd.ai/insights/usdai-july-recap-81m-deployed-loans)
- S2 accrual start: every S2 integration's rate schedule begins at `startTimestamp 1771459200` = **2026-02-19 00:00 UTC**; Oct-2026 Pendle integrations switch to rate 0 at **2026-10-15 00:00 UTC**. [OFFICIAL API] — [integration-rates](https://api.usd.ai/usdai/public/integration-rates)
- The app has a Season 1 / Season 2 dropdown with status labels (active vs ended). [OFFICIAL] — [Product updates Apr 21–May 1 2026](https://usd.ai/insights/product-updates-april-21-may-1-2026)

**Season 3**
- No official S3 announcement found (searched usd.ai/insights index through Sep 2026, docs, X search). The Pendle 24-FEB-2027 markets (USDai/sUSDai LP 16x, YT 25x/12x, locked YT 40x/20x) have rate schedules with **no end timestamp**, unlike the Oct-2026 markets. [OFFICIAL API] — [integration-rates](https://api.usd.ai/usdai/public/integration-rates); [app opportunities list](https://app.usd.ai/rewards?tab=opportunities)

### Inferences
- The open-ended rates on Feb-2027 Pendle markets strongly suggest points will keep accruing after 2026-10-14 (either S2 extension or an S3), but nothing is announced; the YT-USDai-24FEB27 price is consistent with the market pricing post-Oct-14 accrual (see Q5).
- S2 elapsed ≈ 221.5 days at 2026-09-28 12:00 UTC; remaining ≈ 16.5 days to 2026-10-15 00:00 UTC [DERIVED].

### Gaps
- Exact S1 start date for accrual (public launch/"Allo Game" blog 2025-08-20; Pendle boost vaults 2025-08-25 per Dune snippet) — not pinned to an official timestamp.
- No official S3 or S2-extension statement found as of 2026-09-28.

---

## Q2. Season 2 earning rules: rates per $/day, multipliers, Pendle YT/LP, DEX/lending, referrals, queue, boosts, caps

### Takeaway
Current S2 rates (live app/API 2026-09-28): hold USDai **8x**, hold sUSDai **2x**, lending supply USDai/sUSDai **8x**, DEX LP / Fluid "double" / Pendle LP **16x** (Gamma USDai-USDC 20x), **YT-USDai 25x**, **YT-sUSDai 12x**, **locked YT-USDai 30x (Oct-26) / 40x (Feb-27)**, **locked YT-sUSDai 15x (Oct-26) / 20x (Feb-27)**, sCHIP/locked CHIP **10x**, CHIP-USDC LP **30x** (±10% range), third-party USDC/USDT lending **0–1x**. YT holders are credited per YT on full underlying notional (1 YT = 1 USDai of accounting asset), **net of Pendle's 5% fee** (gross 26.32x → 25x). sUSDai YT earns **less than half** the USDai YT rate (12x vs 25x). Referral: referrer earns +10% of referees' points (creators up to +20%). No deposit caps in S2.

### Cited Findings
**Current rate table (app HTML RSC payload + `/usdai/wallet/adjusted-rates`, 2026-09-28)** [OFFICIAL] — [app.usd.ai opportunities](https://app.usd.ai/rewards?tab=opportunities); [adjusted-rates API](https://api.usd.ai/usdai/wallet/adjusted-rates?address=0x0000000000000000000000000000000000000001); [integration-rates API](https://api.usd.ai/usdai/public/integration-rates)

| Activity (chain) | Rate now | Notes |
|---|---|---|
| Lock YT-USDai-24FEB2027 (Arb) | **40x** | USD.AI lock vault |
| Lock YT-USDai-14OCT2026 (Arb) | **30x** | 20x from 02-19, 30x from 04-07 17:00 UTC |
| Buy YT-USDai-14OCT2026 / 24FEB2027 (Arb) | **25x** | 20x→25x on 04-07; gross (pre-Pendle-fee) 26.316x |
| CHIP-USDC LP Uniswap (Arb, Eth), Aerodrome (Base) | **30x** | "Must be +/- 10% of current price" |
| Lock YT-sUSDai-24FEB2027 | **20x** | |
| Gamma USDai-USDC LP (Arb) | **20x** | 20x→16x (04-07)→20x (06-01) |
| Pendle LP USDai & sUSDai (14OCT26, 24FEB27) | **16x** | USDai-LP 8x→16x (04-07); sUSDai-LP 5x→16x (06-01); per $ of LP value |
| Curve (LP & staked), Aerodrome CL, Balancer, Maverick V2, Fluid "double"/smart LP, Jupiter Lend LP | **16x** | USDai-side 12x→16x on 04-07 |
| Lock YT-sUSDai-14OCT2026 | **15x** | 12x→15x on 04-07 |
| Buy YT-sUSDai-14OCT2026 / 24FEB2027 | **12x** | gross 12.63x |
| sCHIP (Arb/Base/Eth), locked CHIP 4-mo/8-mo (Level Up) | **10x** | "Per $1 of sCHIP"; sCHIP from 2026-04-26 |
| Hold USDai (Arb/Base/Plasma/Eth), Euler/Silo/Fluid single supply, Morpho/Kamino/Jupiter sUSDai collateral, queued USDai deposit | **8x** | USDai hold 5x (Eth 4x) → 8x on 04-07 |
| Hold sUSDai (all chains), queued sUSDai deposit | **2x** | unchanged since 02-19 |
| Lend USDC/USDT/USDe to USDai/PT markets (Euler, Morpho, Silo, Gearbox, Euler Earn) | **1x** ("0–1x") | Pendlend Euler USDT → 0x from 2026-09-26 |
| Expired Jun-2026 & Mar-2026 (Plasma) Pendle markets, Penpie/Equilibria, Spectra | 0x | ended |

- Rate-change history (all from API `rateSchedule`): 2026-02-19 00:00 UTC S2 start; **2026-04-07 17:00 UTC** broad increase (USDai hold 5→8, YT-USDai 20→25, locked YT-USDai-Oct 20→30, locked YT-sUSDai-Oct 12→15, USDai LPs 12→16, Pendle LP-USDai-Oct 8→16, LP-USDai-Jun 8→10, Fluid single 5→8, Gamma 20→16); **2026-04-26** sCHIP 0→10; **2026-06-01** Pendle LP-sUSDai 5→16, Gamma USDai 16→20; **2026-06-18** Jun-2026 markets → 0; **2026-09-26** Pendlend Euler → 0; **2026-10-15** Oct-2026 markets → 0. Feb-2027 markets were added with flat rates (launched on Pendle ~2026-06-15). [OFFICIAL API] — [integration-rates](https://api.usd.ai/usdai/public/integration-rates); Pendle market timestamps — [Pendle API active markets](https://api-v2.pendle.finance/core/v1/42161/markets/active)
- Caveat: the 2026-06-03 audit **retroactively rewrote** some schedules (e.g. "Euler sUSDai supply was earning at 2x. It has been raised to 8x"; all sUSDai venues equalized to Fluid baseline 8x single / 16x LP; sUSDai now valued at live NAV ≈ $1.063 then instead of $1.00). So the API schedule shows post-audit history, not necessarily what the UI displayed at the time. [OFFICIAL] — [Allo Points API and Audit (2026-06-03)](https://usd.ai/insights/allo-points-api-audit)
- Official rate snapshot at 2026-06-03: 30x (3 integrations: CHIP/USDC Uniswap Arb+Mainnet, CHIP/ETH Aerodrome), 16x (18: Fluid double vaults, Curve staked, Maverick V2, Aerodrome CL), 10x (5: locked CHIP, sCHIP), 8x (17: USDai direct, Euler, Fluid single, Morpho collateral), 2x (6: sUSDai direct incl. queued), 1x (17: USDC/USDT integrators). [OFFICIAL] — [Allo Points API and Audit](https://usd.ai/insights/allo-points-api-audit)
- Official range statement: "Multipliers range from 1x to 40x." [OFFICIAL] — [$CHIP Is Live](https://usd.ai/insights/chip-is-live)

**Unit verification (empirical, [DERIVED] from official API)** — wallet 0x4a74…33bf3 (S2 rank #1) between two API refreshes (2026-09-28 ~11:51 → ~12:01 UTC): USDai balance 19,796.54 earned +1,435.25 XP; Pendle LP-USDai-14OCT (19,827,207 LP × $2.5217 = $49.998M) earned +7,247,700 XP; YT-USDai-14OCT (3,020,523 YT) earned +684,337 XP. Per-unit accrual ÷ rate gives the same elapsed time for all three (0.00906 day ≈ 13.0 min): 1,435.25/19,796.54/8 = 7,247,700/49.998M/16 = 684,337/3,020,523/25 = 0.00906. ⇒ **Rate = Allo per $1 (or per 1 YT) per day; LP rate applies to LP market value in USD; YT rate applies per YT unit (full underlying notional), and the 25x is net of Pendle's 5% fee.** — [wallet API](https://api.usd.ai/usdai/wallet/0x4a74c93dfcb24354131b8149100f428624833bf3?season=2); [integrations-data API](https://api.usd.ai/usdai/wallet/integrations-data?address=0x4a74c93dfcb24354131b8149100f428624833bf3&chainId=42161)
- `/usdai/wallet/rates` shows YT gross rates 26.3158 (=25/0.95) and 12.6316 (=12/0.95), locked 31.58/42.11/15.79/21.05; `/adjusted-rates` shows 25/12/30/40/15/20. [OFFICIAL API] — [rates API](https://api.usd.ai/usdai/wallet/rates?address=0x4a74c93dfcb24354131b8149100f428624833bf3). Docs: "5% of yield / points from Pendle YT markets go to the Pendle Treasury." — [docs: Pendle (Yield, YT, Locks)](https://docs.usd.ai/depositor/faq/pendle-yield-yt-locks)
- Pendle markets for sUSDai use **USDai as accounting asset** (1 YT-sUSDai = yield on 1 USDai-worth of sUSDai; sUSDai NAV 1.1153 on 2026-09-28). [OFFICIAL Pendle API] — [Pendle market sUSDai-14OCT](https://api-v2.pendle.finance/core/v1/42161/markets/0xcbf629c8d396b1261f81f55175afa010e94787d8); sUSDai convertToAssets(1e18) = 1.11532 on-chain (Arbitrum, [sUSDai contract](https://arbiscan.io/address/0x0b2b2b2076d95dda7817e785989fe353fe955ef9))

**Locked-YT mechanics**
- Locked YT rates **decay over time**; each deposit gets the current rate; wallet multiplier = amount-weighted blend, "once blended, it does not revert"; transfers of locked YT to a new wallet take the current rate. Allo rate is locked per deposit. Locked-YT yield is paid out in batches ~every 20 days; locked YTs stop receiving Pendle-side yield. [OFFICIAL] — [docs: Allo Points & Alignment](https://docs.usd.ai/depositor/faq/allo-points-and-alignment); [docs: Pendle](https://docs.usd.ai/depositor/faq/pendle-yield-yt-locks)
- Level Up "Overlock Bonus": locking YTs beyond the Level Up Score gives "a Flatiron point multiplier (kicking in at 100% your score)" plus first priority on unsold ICO CHIP; "all YTs of all maturities and types will get a 20% bonus up to 2x of your Level Up Score." [OFFICIAL] — [Level Up Guide](https://usd.ai/insights/allo-game-to-flatiron-level-up-guide). (Exact current magnitude not visible in API; `adjusted-rates` for the top-40 S2 wallets showed no wallet-specific deviations.)

**Other rules**
- Points update "every ~1 hour"; transfer → old wallet stops, new wallet starts next cycle; points non-transferable. [OFFICIAL] — [docs FAQ](https://docs.usd.ai/depositor/faq/allo-points-and-alignment)
- Allo points **stop accruing once an sUSDai unstake request is submitted** (yield continues until unstake date). [OFFICIAL] — same
- Queued deposits earn: USDAI_QUEUED_DEPOSIT_ARBITRUM 8x (4x before 04-07), SUSDAI_QUEUED_DEPOSIT 2x. [OFFICIAL API] — [integration-rates](https://api.usd.ai/usdai/public/integration-rates). No separate "GPU-loan/Allocator" points track exists in the S2 integration list.
- Referral: "every active participant earns a 10% point bonus on their referred wallets"; creators can apply for up to "100% bonus (20% effective bonus rate)"; assignments permanent for the season. [OFFICIAL] — [Flatiron Referral Boost (2026-04-16)](https://usd.ai/insights/flatiron-referral-boost-program). API wallet object shows `invite.percentage: 10`, `inviteXp` counted inside `totalXp`. — [wallet API](https://api.usd.ai/usdai/wallet/0x4a74c93dfcb24354131b8149100f428624833bf3?season=2)
- Community claim that using a referral link "gets you the max +20% boost on every point you earn" (i.e., referee-side boost) — [COMMUNITY, x256xx 2026-04-23](https://x.com/x256xx/status/2047406439409529147); **not confirmed** by official docs (official text describes the bonus accruing to the referrer).
- S2 removed deposit caps and targets looping (Fluid). [OFFICIAL] — [Level Up Guide](https://usd.ai/insights/allo-game-to-flatiron-level-up-guide)
- Discrepancy: Pendle Intern / x256xx (2026-04-23/24) quote "LP USDai | 25x multiplier" and "LP sUSDai | 12x" (likely Pendle-UI display or "keep YT" zap), whereas USD.AI API credits Pendle LP at 16x per $ LP value (USDai-LP since 04-07; sUSDai-LP 5x until 06-01). [COMMUNITY] — [PendleIntern](https://x.com/PendleIntern/status/2047483461024559539); [OFFICIAL API](https://api.usd.ai/usdai/public/integration-rates)

### Inferences
- Points per $ of capital at risk (at 2026-09-28 prices, [DERIVED]): YT-USDai-14OCT: 25 Allo/day ÷ $0.004326 = **~5,780 Allo per $ per day**; YT-sUSDai-14OCT: 12 ÷ $0.005258 = ~2,280 Allo/$/day (+ sUSDai yield); YT-USDai-24FEB27: 25 ÷ $0.02915 = ~858 Allo/$/day; LP 16 Allo/$/day; hold USDai 8; hold sUSDai 2.
- Looping: a Fluid sUSDai supply position (8x on supplied collateral) looped L× gives ≈8·L Allo per $ equity/day (+ net carry); Fluid vaults dominate top-wallet points (see Q3).
- sUSDai YT vs USDai YT: 12x vs 25x per unit; sUSDai YT also carries real yield (~7.6% underlying APY), so its points price is lower-leverage.

### Gaps
- Exact current Overlock-bonus multiplier and whether it is reflected in the API `totalXp`.
- Official statement of the lock-rate "decay" schedule for Feb-2027 lock vaults (current 40x/20x displayed; decay parameters not published).
- Whether YT-sUSDai points use USDai notional (1.00) or sUSDai NAV (1.115) per YT — Pendle accounting asset is USDai, so most likely $1 notional; not officially stated.

---

## Q3. Total points issued, dashboards/API, daily issuance and trend

### Takeaway
S2 cumulative Allo = **1,054,527,779,846 (≈1.0545T)** as of 2026-09-28 ~11:50 UTC; S1 total = **1,771,968,655,930 (≈1.772T)**; all seasons ≈ **2.83T**. S2 issuance averaged **~3.57B/day** (Feb 19 → Jun 3) and **~5.83B/day** (Jun 3 → Sep 28); lifetime S2 average 4.76B/day. Bottom-up, Pendle YTs alone issue ~2.2B/day and Pendle LPs ~1.05B/day. Projected final S2 total ≈ **1.13–1.16T** if current pace holds to Oct 15. Points are highly concentrated (top-10 wallets = 45%, top-100 = 78% of S2).

### Cited Findings
- Public API endpoints (no auth): `GET https://api.usd.ai/usdai/public/total-allo?season=2` → `{"total":1054527779846.0443}`; `?season=1` → `{"total":1771968655930.1465}` (queried 2026-09-28 11:50–12:01 UTC). [OFFICIAL API] — [S2](https://api.usd.ai/usdai/public/total-allo?season=2); [S1](https://api.usd.ai/usdai/public/total-allo?season=1)
- `GET /usdai/wallets/totalWallets?season=2` → 77,283 (same value returned for season=1 — appears to be total registered wallets, not season-specific). — [API](https://api.usd.ai/usdai/wallets/totalWallets?season=2)
- Leaderboard API (top 100): S2 #1 = 132.55B XP (12.6% of S2), top-10 sum 476.3B (45.2%), top-100 sum 825.0B (78.2%), #100 = 1.42B. S1 top-100 = 937.8B (52.9%). — [S2 leaderboard](https://api.usd.ai/usdai/wallets/leaderboard?season=2); [S1 leaderboard](https://api.usd.ai/usdai/wallets/leaderboard?season=1)
- Official Allo Points API launched 2026-06-03: `GET https://api.usd.ai/usdai/public/integration-rates` returns all integrations, contract addresses and rate schedules. Audit: "Season 2 total XP increases from 338.1 billion to 372.7 billion (+34.6B, +10.2%)"; 6B "ghost" points removed and redistributed to Pendle YT holders (then 139.4B XP across 12 YT integrations); S1/S2 boundary fix removed up to 7x inflation for some managed-vault/YT accounts; Concrete-lock decimal and post-maturity accrual bugs fixed. [OFFICIAL] — [Allo Points API and Audit (2026-06-03)](https://usd.ai/insights/allo-points-api-audit)
- App UI: /allo page shows "Total Allo", total wallets, Leaderboard tab, Season 1/2 toggle; Portfolio shows per-position "Allo earned [rate per token per day]". [OFFICIAL] — [docs Portfolio (+Team)](https://docs.usd.ai/app-guide/depositor/portfolio-+team); [Product updates May 4–15](https://usd.ai/insights/product-updates-may-4-may-15)
- Protocol TVL: **$619.9M** (app metrics, fetchedAt 2026-09-28 11:41 UTC; gross APY 8.74%, net 7.49%) — [app.usd.ai](https://app.usd.ai/rewards?tab=opportunities); $492.1M at end-Aug 2026, sUSDai supply > $400M — [August recap (2026-09-01)](https://usd.ai/insights/august-recap-100m-facility-susdai-ath); $436.8M TVL, sUSDai $349.5M (2026-08-05) — [July recap](https://usd.ai/insights/usdai-july-recap-81m-deployed-loans); $398M TVL (June 2026) — [Lighthouse YTD report](https://usd.ai/insights/usdai-2026-ytd-report-lighthouse); x256xx cited $261M sUSDai supply on 2026-04-23 — [x256xx](https://x.com/x256xx/status/2047406439409529147). S1 peak USDai supply ~$698M (2025-11-21) — [Dune blog](https://dune.com/blog/the-pendle-effect)
- On-chain (Arbitrum, 2026-09-28 ~12:00 UTC, eth_call totalSupply/balanceOf): YT-USDai-14OCT supply 50,818,223 (13,164,721 in USD.AI lock vaults); YT-sUSDai-14OCT 55,245,785 (17,684,674 locked); YT-USDai-24FEB27 1,964,374 (219,738 locked); YT-sUSDai-24FEB27 6,075,414 (4,089,575 locked); USDai (Arb) 217.6M; sUSDai (Arb) 316.8M shares; sCHIP (Arb) 53.55M. — [YT-USDai-14OCT](https://arbiscan.io/token/0xaf67341456151ab8c270e0962966092181c2eb80); [YT-sUSDai-14OCT](https://arbiscan.io/token/0x11456849c38ea4af212ab8d4324b39983716516a); lock-vault addresses from [integration-rates](https://api.usd.ai/usdai/public/integration-rates)
- Pendle pool liquidity (2026-09-28): LP-USDai-14OCT $50.35M, LP-sUSDai-14OCT $11.41M, LP-sUSDai-24FEB27 $3.99M, LP-USDai-24FEB27 $0.057M. — [Pendle API](https://api-v2.pendle.finance/core/v1/42161/markets/active)
- The S2 #1 wallet (0x4a74…33bf3) holds 19.83M of 19.97M LP-USDai-14OCT tokens (~$50M, ~99% of that pool) + 3.02M YT-USDai-14OCT. — [integrations-data API](https://api.usd.ai/usdai/wallet/integrations-data?address=0x4a74c93dfcb24354131b8149100f428624833bf3&chainId=42161); [Pendle market](https://api-v2.pendle.finance/core/v1/42161/markets/0xa8a0dea40174cfc30fea9e3a77f182ab33f46e25)
- Top-40 S2 wallets' XP by source (sum 666B): Fluid sUSDai vaults (double Plasma 112.9B, double Arb 78.9B, single Arb 77.4B, single Plasma 69.8B) ≈ 350B (~53%); Pendle LP-USDai-Oct 81.2B; locked YT-sUSDai-Oct 37.6B; YT-sUSDai-Oct 33.9B; locked YT-USDai-Oct 33.7B; YT-USDai-Oct 23.3B; hold USDai 20.1B; hold sUSDai 13.1B; locked CHIP-8mo 4.6B. — [wallet API per address](https://api.usd.ai/usdai/wallet/0x4a74c93dfcb24354131b8149100f428624833bf3?season=2) (aggregated over leaderboard top-40)

### Inferences ([DERIVED])
- Average issuance: S2 start 2026-02-19 00:00 → 2026-06-03 (≈104.5 d): 372.7B ⇒ **3.57B/day**; 2026-06-03 → 2026-09-28 12:00 (117 d): (1,054.5 − 372.7)B ⇒ **5.83B/day**; full S2 (221.5 d) ⇒ 4.76B/day. Growth driven by TVL growth ($398M Jun → $620M Sep) and the 06-01 sUSDai-LP increase (5x→16x).
- Bottom-up current issuance (rate × on-chain size): YT (unlocked × 25/12 + locked × 30/15/40/20) = 941M + 395M + 451M + 265M + 44M + 9M + 24M + 82M ≈ **2.21B/day**; Pendle LP ≈ (50.35+11.41+3.99+0.06)M × 16 ≈ **1.05B/day**; sCHIP (Arb only) ≈ 53.55M × $0.0443 × 10 ≈ 24M/day; remainder (plain sUSDai at 2x, USDai 8x, Fluid loops 8–16x, Curve/Gamma etc., +10% referral) ≈ 2–3B/day ⇒ total ≈ **5–6B/day**, consistent with the 5.83B/day average. Caveat: locked-YT blended rates may be below displayed rates (decay/blending).
- Point inflation: at ~5.5–6B/day, S2 total grows ~0.55%/day (≈ 5.5B/1,054.5B); remaining 16.5 days add ≈ 83–99B (+8–9%) ⇒ **final S2 ≈ 1.137–1.154T** (assuming no rule changes and Oct-2026 rates ending 2026-10-15 00:00 UTC).
- Also note after 10-15 the Oct-2026 YT/LP positions (≈ 2.1B/day of issuance by the bottom-up estimate) stop earning; if accrual continues on Feb-2027 markets, the post-Oct issuance rate would drop sharply unless capital rolls.

### Gaps
- Point-in-time snapshot of the protocol total changed only hourly-or-slower; my 5-min polls of `total-allo` 11:50–12:10 UTC did not capture a refresh, so no directly measured instantaneous rate (see poll note appended at end if captured).
- No Dune dashboard dedicated to Allo points was verified (search surfaced [dune.com/entropy_advisors/usdai-usdai](https://dune.com/entropy_advisors/usdai-usdai) for USDai supply, not points).
- Historical daily S2 totals (time series) not publicly archived (Wayback CDX blocked from this environment).

---

## Q4. Token allocation to points (S1 realized, S2 stated/estimated)

### Takeaway
S1 officially received **10% of supply (1.0B CHIP)**: 7% as ICO purchase rights at $0.03 and 3% (300M CHIP) free airdrop, all unlocked at TGE. **The S2 (Flatiron) CHIP pool has NOT been disclosed.** It must come from the "Ecosystem Bootstrapping" bucket (27.5% of supply, of which 10% was used in S1 → **17.5% remaining** for "airdrops, upcoming incentive programs, and other targeted incentives"). Community base case: **3–5% of supply**.

### Cited Findings
- Tokenomics: Ecosystem Bootstrapping **27.5%** ("The first 10% was distributed during Season 1 (The Allo Game). The remaining allocation will fund USD.AI growth initiatives, including airdrops, upcoming incentive programs…"), Reserve 19.8%, Core contributors 23.1%, Investors 29.6% (both 12-month cliff, 33% at month 12, rest monthly over 24 months). Total supply 10B. [OFFICIAL] — [docs Tokenomics](https://docs.usd.ai/governance/tokenomics) (Messari lists 23.5% core / 19.5% reserves — minor discrepancy — [Messari, 2026-03-02](https://messari.io/report/a-valuation-of-usdai-chip))
- Official unlock chart (docs image): ecosystem bucket ≈2.0B unlocked at TGE (Q2'26), rising slowly to ≈2.2B by Q1'27, a step to ≈2.45B in Q2'27, then linear to 2.75B by Q1'29 (my reading of the chart; values approximate). [OFFICIAL chart] — [docs Tokenomics](https://docs.usd.ai/governance/tokenomics)
- "In this new season of Allo Game, all rewards will be distributed through $CHIP airdrops." No size given. [OFFICIAL] — [$CHIP Is Live](https://usd.ai/insights/chip-is-live)
- Buybacks: Permian Labs bought back 338,806,273 CHIP from investor allocations in May 2026; with the prior "airdrop buyback" of 31,731,287 CHIP (Level Up airdrop buyout), cumulative buybacks = 3.71% of supply. [OFFICIAL] — [May 2026 recap](https://usd.ai/insights/usdai-may-2026-recap)
- Community estimate (x256xx, 2026-04-23): one S2 airdrop "likely 3–5% of FDV": Bear 3% × $300M = $9M; Base 4% × $500M = $20M (most likely); Bull 5% × $1B = $50M. [COMMUNITY] — [x256xx article](https://x.com/x256xx/status/2047406439409529147), amplified by [PendleIntern](https://x.com/PendleIntern/status/2047483461024559539) and [Pendle Print #111 (2026-04-27)](https://pendlefi.substack.com/p/pendle-print-111)

### Inferences ([DERIVED])
- The unlock chart's ecosystem line (≈+0.2B over Q2'26–Q1'27 and a ≈+0.25B step in Q2'27) is consistent with an S2 airdrop of roughly 2–4.5% of supply being scheduled around/after season end, but this is an interpretation of a chart, not a stated allocation.
- CHIP per S2 Allo for a given pool X% and final S2 ≈ 1.14T: CHIP/Allo = X% × 10B / 1.14T → 1% ⇒ 8.77e-5; 2% ⇒ 1.75e-4; 3% ⇒ 2.63e-4; 4% ⇒ 3.51e-4; 5% ⇒ 4.39e-4 CHIP per Allo.

### Gaps
- No official S2 pool size, no official split between Pendle/partners, no statement on whether S1 Level Up "S2 points" are a separate sub-pool.

---

## Q5. Point value estimates ($/Allo): S1 realized, Pendle-YT implied, community

### Takeaway
**S1 realized:** airdrop side received **0.000397 CHIP per aligned Allo** ⇒ ≈ **$1.19e-5/Allo at $0.03 (ICO)**, **$2.44e-5 at TGE-day close ($0.0613)**, **$1.76e-5 at today's $0.0443**. **S2 market-implied (Pendle YT-USDai-14OCT, pure-points YT): ≈ $1.05e-5 per Allo**, cross-checked by YT-sUSDai-14OCT ≈ $1.01e-5. At final S2 ≈ 1.14T, that implies a **~$12M S2 pool ≈ 270M CHIP ≈ 2.7% of supply** at $0.0443. No OTC/pre-market point trading venue was found.

### Cited Findings
- CHIP price 2026-09-28: $0.0443 (Uniswap Arbitrum CHIP/USDC, liquidity $0.96M; FDV ≈ $443M, mcap ≈ $88.6M). [MARKET] — [DexScreener API](https://api.dexscreener.com/latest/dex/tokens/0x0c1c1c109fe34733fca54b82d7b46b75cfb71f6e)
- CHIP daily closes (Arbitrum Uniswap pool): 2026-04-21 open 0.0618 / close **0.0613** (high 0.1097); 04-22 close 0.1133; 04-23 high 0.2519, close 0.1038; 05-25 0.0461; 06-08 0.0332; 07-20 0.0299; 08-03 0.0246; 08-31 0.0387; 09-14 0.0419; 09-26 0.0487; 09-28 0.0443. [MARKET] — [GeckoTerminal OHLCV](https://api.geckoterminal.com/api/v2/networks/arbitrum/pools/0x560093b297e9c149e8566f329122c1790b4da306/ohlcv/day?limit=170). Aggregator figures differ: ATH $0.1383 on 2026-04-23 (CMC) vs $0.1189 on 04-22 (CoinGabbar); CEX first-day +103% vs $0.03 ICO. — [CoinMarketCap](https://coinmarketcap.com/currencies/usd-ai/); [CoinGabbar](https://www.coingabbar.com/en/price-prediction/chip-price-prediction-usdai-list-binance-bybit-kucoin-mexc-upbit)
- Pendle (2026-09-28 ~11:53 UTC): YT-USDai-14OCT **$0.004326**, implied APY 10.06%, underlying APY **0** (USDai non-yield-bearing); YT-sUSDai-14OCT **$0.005258**, implied 12.36%, underlying 7.575%; YT-USDai-24FEB27 **$0.02915**, implied 7.49%; YT-sUSDai-24FEB27 **$0.04114**, implied 10.80%. [MARKET] — [Pendle USDai-14OCT](https://api-v2.pendle.finance/core/v1/42161/markets/0xa8a0dea40174cfc30fea9e3a77f182ab33f46e25); [sUSDai-14OCT](https://api-v2.pendle.finance/core/v1/42161/markets/0xcbf629c8d396b1261f81f55175afa010e94787d8); [USDai-24FEB27](https://api-v2.pendle.finance/core/v1/42161/markets/0x46f545683d8494ef4c54b7ea40ca762c620846ef); [sUSDai-24FEB27](https://api-v2.pendle.finance/core/v1/42161/markets/0xf86119a39f8654f38acbbd5488bd83f3f51983c8)
- Community scenario returns (2026-04-23, x256xx): LPT-USDai-14OCT APY bear 18% / base 39% / bull 98%; LPT-sUSDai-14OCT 15/26/54%; $1k YT-USDai-17JUN → $2,680/$5,960/$14,940; $1k YT-sUSDai → $1,690/$2,850/$6,020 (assumed pool $9M/$20M/$50M). [COMMUNITY] — [x256xx](https://x.com/x256xx/status/2047406439409529147)
- Pre-TGE FDV prediction $270M–$320M (central ~$290M). [COMMUNITY] — [Whales Market blog](https://whales.market/blog/usd-ai-chip-fdv-prediction/)
- S1 guide: "$1,000 principal… farm 26m Allo Points" via YT-sUSDai (Sep 2025). [COMMUNITY] — [PendleIntern](https://x.com/PendleIntern/status/1963062355316899892)

### Inferences ([DERIVED], formulas)
- **S1 realized, airdrop side:** CHIP/Allo = 300,000,000 / 755,060,221,630 = **3.973e-4**. $/Allo = 3.973e-4 × P: P=$0.03 → **$1.19e-5**; P=$0.0613 (04-21 close) → **$2.44e-5**; P=$0.1133 (04-22 close) → $4.50e-5; P=$0.0443 (now) → **$1.76e-5**.
- **S1 realized, ICO side** (value of the right to buy at $0.03): 700,000,000 / 922,906,625,709 = 7.585e-4 CHIP-rights/Allo; value = 7.585e-4 × (P − 0.03): at $0.0613 → $2.37e-5; at $0.0443 → $1.08e-5 (ignores ICO subscription/pro-rata and Level Up extras).
- **Coordinator's metric** (3% ÷ ALL S1 points): 300M / 1.772T = 1.693e-4 CHIP/Allo ⇒ $5.1e-6 (at $0.03), $1.04e-5 (at $0.0613), $7.5e-6 (at $0.0443). Using full 10% ÷ all S1 points: 5.64e-4 CHIP/Allo ⇒ $3.46e-5 (TGE close) / $2.50e-5 (now) — but this mixes free airdrop with paid ICO rights.
- **S2 implied from YT-USDai-14OCT** (no underlying yield, expires at season end): Allo remaining per YT = 25 × 16.5 d = 412.5 ⇒ $/Allo = 0.004326 / 412.5 = **$1.049e-5**.
- **Cross-check YT-sUSDai-14OCT:** yield value = 0.07575 × 16.5/365 × 0.95 = $0.003253; points value = 0.005258 − 0.003253 = $0.002005 for 12 × 16.5 = 198 Allo ⇒ **$1.013e-5/Allo**.
- **YT-USDai-24FEB27:** if only S2 accrual (412.5 Allo) counted ⇒ $7.07e-5/Allo (7× the Oct YT ⇒ inconsistent) ; if all 149.5 days at 25x count (3,737 Allo) ⇒ **$7.8e-6/Allo** ⇒ the market is pricing continued (S3/extension) accrual at a ~25% discount to S2 points.
- **Implied S2 pool:** final S2 ≈ 1.137–1.154T × $1.05e-5 ≈ **$11.9–12.1M** ⇒ ÷ $0.0443 ≈ **269–273M CHIP ≈ 2.7% of supply** (market-implied; embeds risk discount and time value to an unknown distribution date).
- Break-even check vs S1: S2 implied $/Allo ($1.05e-5) ≈ 60% of S1 airdrop-side realized value at today's price ($1.76e-5).
- For a user: value of a position = rate × days × $/Allo; e.g. $1 in LP-USDai for remaining 16.5 d = 16 × 16.5 × 1.05e-5 ≈ $0.00277 (≈6.1% annualized) on top of PT/LP yield.

### Gaps
- No OTC/pre-market Allo trading (Whales Market etc.) found for S2 points; Pendle YT is the only observable market price.
- CHIP "price at TGE" is not uniquely defined (CEX vs DEX, intraday range $0.05–0.25 in first 3 days); I report DEX daily closes.

---

## Q6. Anti-sybil, vesting/claim terms, loyalty boosts

### Takeaway
S1: airdrop and ICO tokens **100% unlocked** (no vesting), auto-distributed/claimable in-app with deadline 2026-05-30; unaligned S1 points were **burned**; Level Up offered lock-based refund/discount/buyout options. **S2 claim/vesting/anti-sybil terms have not been published.** The only "loyalty" mechanics in S2 are locked-YT multipliers (rate locked per deposit, decaying for new deposits), the Level Up Overlock bonus, sCHIP 10x, and permanent referral teams.

### Cited Findings
- ICO: "Unlock: 100% at TGE (no vesting for ICO tokens)"; Airdrop: distributed on TGE date to default wallet, no minimum, "no separate claim process." [OFFICIAL] — [CHIP ICO, Airdrop (2026-02-09)](https://usd.ai/insights/chip-ico-airdrop)
- Post-TGE: "If you have not claimed your tokens, head to the USD.AI app and complete the claim first. The deadline to claim is May 30, 2026." [OFFICIAL] — [$CHIP Is Live](https://usd.ai/insights/chip-is-live)
- Airdrop tokens unlocked at TGE "with U.S. accredited investor exceptions subject to one-year lock-up." [SECONDARY] — [MEXC blog (2026-04-02)](https://blog.mexc.com/usdai-airdrop-guide-chip-eligibility-yield-strategies-and-season-2-opportunities/)
- S1 gating: no alignment at game end ⇒ points burned; "Even minimal participation in a qualifying strategy is sufficient." [OFFICIAL] — [CHIP ICO, Airdrop](https://usd.ai/insights/chip-ico-airdrop)
- Level Up ICO protected CHIP: refund at $300M any time (forfeits CHIP); early unlock forfeits discount right; hold to maturity ⇒ discount to $270M/$190M FDV paid in USDC. Airdrop buyout irreversible. [OFFICIAL] — [Level Up finale](https://usd.ai/insights/level-up-finale); [$CHIP Is Live](https://usd.ai/insights/chip-is-live)
- Points are wallet-based (email irrelevant); points cannot be moved between wallets. [OFFICIAL] — [docs FAQ](https://docs.usd.ai/depositor/faq/allo-points-and-alignment)
- "USD.AI reserves the right to modify the program at any time" (referral boost terms); multiplier changes "are always announced publicly ahead of time." [OFFICIAL] — [Referral Boost](https://usd.ai/insights/flatiron-referral-boost-program); [docs FAQ](https://docs.usd.ai/depositor/faq/allo-points-and-alignment)
- Audit precedent: team retroactively removed 6B "ghost" points and corrected inflated balances (S1/S2 boundary, Concrete lock decimal bug) — shows willingness to adjust balances pre-distribution. [OFFICIAL] — [Allo Points API and Audit](https://usd.ai/insights/allo-points-api-audit)

### Inferences
- Given S1 precedent (fully unlocked airdrop, in-app claim), an S2 airdrop without vesting is plausible but unconfirmed; modelers should include a scenario with vesting/cliff or a stake-to-claim (sCHIP) requirement since sCHIP is an explicit 10x S2 activity and CHIP has a staking/backstop module.
- Referral bonus (+10–20%) and possible retroactive audits add to total points (dilution) beyond the per-$ rates.

### Gaps
- No official S2 snapshot date, distribution date, claim window, vesting, minimum threshold or sybil filter found as of 2026-09-28.
- No explicit "hold-through-TGE" loyalty multiplier for S2 found.
