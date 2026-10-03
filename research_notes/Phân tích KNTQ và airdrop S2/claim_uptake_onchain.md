# KNTQ Season-2 claim: measured uptake, claimer behaviour and the 2-hourly tracker

All numbers in this file were measured by the coordinator directly on-chain on 2026-10-03 between
23:15 and 23:40 UTC (read-only `eth_getLogs` / `eth_call` on HyperEVM via `rpc.purroofgroup.com` and
`hyperliquid-rpc.publicnode.com`, plus `api.hypurrscan.io/holders/KNTQ` and `api.hyperliquid.xyz/info`).
Provenance tag **[V-ME]** = verified by the coordinator here. Nothing was signed; no wallet was connected.

Contract set (cross-checked against two teammates' independent work):
claim proxy `0x435bb7ea4eb481cb686606d089ea4dee4c6cc03b`, KNTQ `0x000000000000780555bd0bca3791f89f9542c2d6`,
payment USDC `0xb88339cb7199b77e23db6e890353e22632ba630f`, pool funded with **exactly 50,000,000 KNTQ** in two
transfers from `0x5bd9e766c0151dcfbc4246e5f8b3193c4beeaae4` (100 test + 49,999,900), `start()` 2026-10-01
12:00:00Z, `end()` 2026-10-11 12:00:00Z, `quote(1e18)` = 0.261331 USDC. Tooling lives in
`/home/user/test-claude/kntq-s2-tracker/` (`tracker.py`, `series.py`, `README.md`).

## 1. Snapshot and the claim curve

### Takeaway
44.09% of the 50M pool was bought in the first 59.4 hours, but **38.6% of it went in the first 12 hours**
and the pace has since fallen by ~93%. Two independent snapshots 11 hours apart (43.788% → 44.093%)
show the claim is now a slow drip, not a wave. 27.95M KNTQ (55.9%) is still unclaimed with ~180 hours left.

### Cited Findings [V-ME]
Snapshots written to `kntq-s2-tracker/snapshots.csv`:

| UTC | block | wallets | claim txs | KNTQ claimed | % of 50M | left in contract | KNTQ price | premium vs 0.2613 |
|---|---|---|---|---|---|---|---|---|
| 2026-10-03 12:16 | 47,395,562 | 2,955 | 3,560 | 21,894,240 | 43.79% | 28,105,760 | $0.30225 | +15.7% |
| 2026-10-03 23:22 | 47,593,005 | 3,059 | 3,666 | 22,046,576 | 44.09% | 27,953,424 | $0.302835 | +15.9% |

- USDC collected by the contract: **$5,761,454**, exactly equal to the sum of `Claimed` costs, so the
  team has withdrawn none of the proceeds yet (`Withdrawn` events: none).
- Integrity check passes exactly: 50,000,000 − 22,046,576 − 27,953,424 = 0.
- Claim curve by hour (`kntq-s2-tracker/claim_series.json`), cumulative % of the 50M pool:

| Window (UTC) | KNTQ claimed | cumulative % | new wallets |
|---|---|---|---|
| Oct 1 12:00 (first hour) | 7,096,543 | 14.19% | 626 |
| Oct 1 12:00–16:00 | 15,519,158 | 31.04% | 1,189 |
| Oct 1 (12 h, to 24:00) | 19,289,818 | 38.58% | 1,918 |
| Oct 2 (full day) | +1,501,029 | 41.58% | +449 |
| Oct 3 (to 23:00) | +1,255,729 | 44.09% | +692 |

- Daily pace: 19.29M → 1.50M → 1.26M KNTQ. The Oct 3 total is dominated by **one 1.02M-KNTQ hour
  (09:00 UTC, 10 claims)**; excluding it, Oct 3 was ~0.24M.
- Oct 3 06:00–07:00 UTC saw 515 claims for only 48k KNTQ total (avg ~93 KNTQ) — a wave of dust wallets,
  not economically meaningful supply.

### Inferences
- Everyone with size and intent claimed on day one. What is left is mostly either small wallets or
  holders who do not plan to pay, so a linear extrapolation of the current pace (~0.26M/day ex-lumps)
  projects only **~48–52% claimed by the deadline**, not 100%.
- The remaining 27.95M is therefore better modelled as a **conditional** overhang: it only converts to
  supply while price is comfortably above 0.2613, and it is most likely to convert in a final rush in
  the last 24–48 hours before 2026-10-11 12:00 UTC (the pattern seen in most deadline-driven claims).
- Because the contract is a standing offer, it also caps rallies: anyone holding an unused allocation
  can create supply at 0.2613 at any time until expiry.

### Gaps
- The eligible-wallet denominator is not public (Kinetiq keeps the kPoints→KNTQ ratio private), so
  "% of wallets claimed" cannot be computed — only % of the pool. Aggregate implies ~1.3587 KNTQ/kPoint.

## 2. Who claimed, and how big

### Takeaway
The claim is as concentrated as the token: 3,059 wallets, median claim **305 KNTQ (~$80)**, mean 7,207,
largest 1.42M. The **top 10 wallets took 33.2%** of everything claimed, the top 100 took 68.5%.
Two of the three biggest claimants are known Season-1 whales.

### Cited Findings [V-ME]
- Concentration of the 22.05M claimed: top 10 = 33.2%, top 25 = 47.2%, top 50 = 57.8%,
  top 100 = 68.5%, top 500 = 91.4%.
- Claim-size buckets (wallets): <100 KNTQ: 1,147; 100–1k: 850; 1k–10k: 743; 10k–100k: 285;
  100k–1M: 32; >1M: 2.
- Largest claims: `0x9794bbbc…333b` 1,422,137 (one tx); `0x63af859d…4b36` 1,063,938;
  `0xbd8c75a0…971d` 996,418; `0x9f58a3c3…1dfb` 919,443; `0x0b83821b…3140` 612,531 (8 txs).
- Cross-reference with the flows research: `0x9794bbbc…333b` received a **12.77M genesis (S1) allocation**
  and `0x63af859d…4b36` bridged **20.32M** to HyperEVM in Dec 2025 — both are S1 whales that also took
  the maximum S2 allocation. The 30-day net-buying whale `0xaf0fdd39…1e92e` claimed 167,982 KNTQ.

### Inferences
- The same addresses that farmed S1 heavily also farmed kPoints S2 heavily. Allocation size tracks prior
  capital, not community breadth: 1,147 of 3,059 claimers bought less than $26 worth.
- The long tail cannot move price; the top ~50 wallets are the whole story of claim-driven supply.

## 3. Did claimants sell? (the key question)

### Takeaway
Yes — a clear majority of claimed size was disposed of almost immediately, but the three largest
claimants are still sitting on their tokens. Of the top 200 claimers (17.27M KNTQ = 78% of all claimed),
**151 wallets holding 9.82M KNTQ (56.8%) now show a zero or near-zero balance on both HyperEVM and
HyperCore**, while **33 wallets holding 5.95M (34.4%) still hold ≥90%**.

### Cited Findings [V-ME]
Classification of the top 200 claimers by (HyperEVM `balanceOf` + HyperCore balance) ÷ claimed:

| Class | wallets | KNTQ claimed | share of top-200 claimed |
|---|---|---|---|
| kept <10% ("disposed") | 151 | 9,815,000 | 56.8% |
| kept 10–90% (partial) | 16 | 1,511,437 | 8.8% |
| kept ≥90% ("still holding") | 33 | 5,947,005 | 34.4% |

- Still holding (full size, on HyperEVM, untouched): `0x9794bbbc…333b` 1.42M, `0x63af859d…4b36` 1.06M,
  `0xbd8c75a0…971d` 1.00M, `0x9f58a3c3…1dfb` 0.92M (this wallet holds 9.98M KNTQ in total).
- Fully disposed: `0x0b83821b…3140` 612k, `0xd507eeef…c948` 586k, `0xcc6bf6bf…7c75` 521k,
  `0x64b3bf0c…d0d4` 460k, `0x418769f7…c925` 362k, `0xd782059d…6ca7` 360k, `0xb2e27551…377c` 326k.
- **EVM→HyperCore bridge flow of KNTQ** (transfers to the system address `0x2000…007c`, the route a
  claimant must take to sell on the main `@334` book):

| Window (UTC) | KNTQ bridged to HyperCore | per hour |
|---|---|---|
| Sep 30 00:00 → Oct 1 12:00 (baseline) | 4,744,630 | ~132k/h |
| **Oct 1 12:00 → 24:00 (claim opens)** | **24,546,650** | **2,045k/h** |
| Oct 2 (full day) | 2,947,696 | 123k/h |
| Oct 3 00:00 → 23:00 | 977,468 | 44k/h |

### Inferences
- The 24.5M bridged in the first 12 hours against 19.3M claimed in the same window means **effectively
  all day-one claimed supply was moved to the order book**, together with pre-existing EVM balances.
  That is the mechanical explanation of the Oct 1 −35% candle, and it is now over: bridge-in has fallen
  to **one third of the pre-claim baseline**.
- Taking the two measures together, roughly **10–11M KNTQ of claimed supply has already been sold**
  (≈$3.0–3.3M at $0.29–0.30) and ~6M is held by a handful of large wallets that chose not to arbitrage.
  The marginal claim-driven seller has largely finished for now.
- The zero-balance wallets are a robust lower bound on selling (a wallet holding nothing cannot have
  kept its claim). The "still holding" bucket is an upper bound, since HyperCore balances can include
  tokens held before the claim.
- The 5.95M held by the big four is a different kind of overhang than the contract's 27.95M: it is
  unpriced, discretionary, and would hit the same thin book ($25k within ±2%).

### Gaps
- "Disposed" conflates selling with transfers to another wallet of the same owner, to a CEX, or into
  staking/LP positions (sKNTQ, Nest/Project X pools). Sales were not matched trade-by-trade to fills.
- Only the top 200 wallets were balance-checked (78% of claimed KNTQ); the remaining 2,859 wallets
  hold 22% and were not classified.

## 4. The 2-hourly tracker that is now running

### Takeaway
A read-only tracker is in place and scheduled every 2 hours (minute :07 UTC) until the window closes,
writing one row per run to `snapshots.csv` with deltas, claim pace, a linear projection of the final
claim share, price and the premium versus 0.2613.

### Cited Findings [V-ME]
- `tracker.py` runs incrementally from `state.json` (≈2 minutes, ~400 RPC calls per run), summing
  `Claimed(address,uint256,uint256)` events, then reads `balanceOf` of the claim contract for KNTQ and
  USDC, the HyperCore mid for `@334` and the HyperEVM pool price from `slot0()`.
- Alert thresholds wired into the schedule: premium <5% (price 0.262–0.275); any 2-hour window with
  >2M KNTQ claimed; loss of 0.287 or 0.278; and any print below 0.2613.
- Public RPC limits found in testing: `rpc.hyperliquid.xyz/evm`, `hyperliquid-rpc.publicnode.com` and
  `rpc.hypurrscan.io` cap `eth_getLogs` at 1,000 blocks; `rpc.purroofgroup.com` accepts 10,000.
  `hyperevmscan.io` is behind Cloudflare (403) from this environment, so no explorer was used.

### Inferences
- The two most informative series for timing an entry are **the claim pace** (how much of the 27.95M
  converts to supply, and when) and **the premium** (how much arbitrage incentive is left). A premium
  collapsing toward 0% with the pool still largely unclaimed is the bear case; the premium holding
  double digits while the pace stays near zero is the bull case.

## 5. Freshest market snapshot (2026-10-03 23:45 UTC) [V-ME]

- HyperCore `@334` mid **$0.30300** (bid 0.30296 / ask 0.30304), **premium over the 0.261331 claim price
  = +15.94%**. Depth near the touch is thin: ~$12.1k of bids within −2% and ~$22.6k of asks within +2%
  (full-precision book; the deeper $0.25–0.29 bid stack a teammate measured sits outside this window).
- Oct 3 hourly candles (UTC) show an unusually quiet, slightly upward grind while 44% of the pool was
  already claimed: 10:00 0.2999 → 23:00 close 0.3030, range 0.2949–0.3084 for the whole day, with
  **hourly volume falling from ~0.8M KNTQ to 0.08–0.46M**.
- Sequence worth noting: the day's low (0.2949) came at 10:00 UTC, *before* the 1.02M-KNTQ claim hour at
  09:00–10:00 was absorbed; price then closed the day near its high. Claim supply on Oct 3 was absorbed
  without a new low.

### Inferences
- Price is holding a tight 0.295–0.308 band at a ~16% premium to the claim price, three days into the
  window, with 44% claimed and ~10–11M claimed tokens already sold. The arbitrage has not closed the gap,
  which means real bids are absorbing it rather than the level being defended by claimants alone.
- The thin touch depth cuts both ways: a single $100–200k market sell still gaps price several percent,
  so the Oct 11 deadline rush remains the main mechanical risk even with the pace currently near zero.

## 6. What the two known buyers are doing right now (2026-10-03 23:50 UTC) [V-ME]

- **`0xaf0fdd39…1e92e`** (the 30-day net buyer, +5.1M KNTQ): **no fills and no TWAP slices at all since
  2026-10-03 12:00 UTC** — it stopped buying. Its resting ladder is unchanged from midday:
  **19 bids for 399,961 KNTQ between $0.2666 and $0.28656 (~$110k notional)** and
  **55 asks for 898,049 KNTQ between $0.36805 and $0.442 (~$369k)**.
- **`0x58f0bf43…0d20`** (TWAP-bought ≥1.09M on Oct 1): also **zero activity since Oct 3 12:00 UTC**.

### Inferences
- The visible marginal buyer has gone passive: it will buy on a dip into **$0.267–0.287** and sells into
  **$0.368–0.442**. That is an explicit, funded accumulation band below the market and a distribution
  band above it, from the one wallet with a demonstrated 30-day bid.
- With both whales idle, the day-three grind from 0.2949 to 0.3030 on falling volume is being done by
  small flow, not by whale accumulation. Thin liquidity cuts both ways, so neither the grind up nor the
  absence of whale bids above $0.287 should be read as strong demand at the current price.
