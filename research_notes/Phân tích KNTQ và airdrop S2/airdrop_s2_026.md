# Kinetiq final kPoints distribution ("Season 2") — the $0.26 paid KNTQ claim, and whether $0.26 is a floor

**Research cut-off: 2026-10-03 ~23:25 UTC.** All on-chain figures below were measured by me directly at HyperEVM block **47,593,106 (2026-10-03 23:18:16 UTC)** and are labelled `[own on-chain measurement]`. Official facts, press reports and inference are kept separate.

**Three corrections to the working summary, up front:**
1. **The real on-chain price is 0.261331 USDC per KNTQ, not $0.26.** Official copy says "fixed $0.26" and even gives the example "an account allocated 1,000 KNTQ can acquire all 1,000 for 260 USDC" — the contract actually charges **261.331 USDC** for 1,000 KNTQ (+0.51%). Confirmed uniform across all 3,666 claims. ([official post](https://kinetiq.xyz/blog/kntq-kpoints-claim); contract `quote()` via [rpc.hypurrscan.io](https://rpc.hypurrscan.io))
2. **"Season 2" is not Kinetiq's wording.** Official framing is "the final kPoints have now been distributed" / "KNTQ claim is now open" — a terminal event, not a new season. No official use of "Season 2" found anywhere. ([official blog index](https://kinetiq.xyz/blog))
3. **A running total IS obtainable**, contrary to "no running total": `totalClaimed()` reverts, but the claim contract's KNTQ balance gives it exactly — `50,000,000 − balanceOf(claimContract)`. This is how I measured participation (and it independently confirms the pool is exactly 50,000,000 KNTQ).

---

## Official terms: allocation formula, caps, eligibility, window, claim URL

### Takeaway
The official post is unusually explicit about mechanics (pro-rata-by-kPoints allocation, partial claims allowed, USDC on HyperEVM, no lockup, claim at kinetiq.xyz/kntq) and unusually silent about the two things traders need: the exact points→KNTQ ratio (the kPoints formula is *deliberately secret per Kinetiq's own docs*) and any sybil/clawback rule. There is **no free airdrop component** — the entire final distribution is a paid right to buy.

### Cited Findings
- Official post "KNTQ claim is now open: kPoints holders can acquire KNTQ at $0.26", `dateModified` **2026-10-01T11:37:04Z** — i.e. published ~23 minutes before the window opened — [kinetiq.xyz/blog/kntq-kpoints-claim](https://kinetiq.xyz/blog/kntq-kpoints-claim)
- Verbatim allocation rule: **"Your final kPoints balance determines the amount of KNTQ allocated to your account. That allocation gives you the right to acquire up to that amount of KNTQ at the fixed $0.26 price during the 10-day window."** — [official post](https://kinetiq.xyz/blog/kntq-kpoints-claim)
- Verbatim worked example: **"an account allocated 1,000 KNTQ can acquire all 1,000 for 260 USDC"** — [official post](https://kinetiq.xyz/blog/kntq-kpoints-claim)
- Partial claims explicitly allowed: **"You do not have to claim the full allocation. The interface allows you to select how much USDC you want to use, up to your account's maximum allocation."** — [official post](https://kinetiq.xyz/blog/kntq-kpoints-claim)
- Price is static, not oracle/TWAP-linked: **"The claim price does not change with the KNTQ market price."** — [official post](https://kinetiq.xyz/blog/kntq-kpoints-claim)
- Program totals: **"A total of 36.8M kPoints were distributed during the program, with participating kPoints holders allocated a combined 50M KNTQ"**, after **46 weeks** of distributions — [official post](https://kinetiq.xyz/blog/kntq-kpoints-claim); 46 weeks / 800k points per week in the later phase also reported by [Crypto Briefing](https://cryptobriefing.com/kinetiq-ends-kpoints-kntq-price-drop/)
- No lockup: **"the KNTQ received has no lockup or vesting period"** — [official post](https://kinetiq.xyz/blog/kntq-kpoints-claim)
- Payment rail and claim URL: **"The claim is executed using USDC on HyperEVM"**; claim at **kinetiq.xyz/kntq**, "connect the account that participated"; login by wallet, email (recommended), Google or passkey; **"Apple login is not recommended for this claim flow"**; Markets.xyz mobile users can export their account private key and import it into a desktop wallet — [official post](https://kinetiq.xyz/blog/kntq-kpoints-claim)
- No extension: **"There is no additional claim period announced after the 10-day window, so eligible participants should complete the process before the deadline."** — [official post](https://kinetiq.xyz/blog/kntq-kpoints-claim)
- Unclaimed: **"Any portion of the 50M KNTQ allocation that has not been claimed when the period ends will be returned to the Kinetiq Foundation"** and "allocated toward ecosystem and growth initiatives" — [official post](https://kinetiq.xyz/blog/kntq-kpoints-claim)
- The kPoints earning formula is secret by policy: Kinetiq docs state **"Details around the kPoints program are kept entirely private, regardless of anyone's strategy or usage"** and that **"Repeated questions about the formula in Discord will result in: muting, timeouts and potential bans for repeat offenders."** Docs do confirm the cadence: **"Snapshots: Taken every Tuesday. Distributions: Occur every Thursday. Weekly distributions: 800,000 kPoints"** — [kinetiq.xyz/docs/kpoints](https://kinetiq.xyz/docs/kpoints)
- `[own on-chain measurement]` Exact window from the claim contract `0x435bb7ea4eb481cb686606d089ea4dee4c6cc03b`: `start()` = 1790856000 = **2026-10-01T12:00:00Z**; `end()` = 1791720000 = **2026-10-11T12:00:00Z** (exactly 864,000 s = 10 days) — queried via [rpc.hypurrscan.io](https://rpc.hypurrscan.io)
- `[own on-chain measurement]` `quote()` is linear and uniform: quote(1e18)=261,331; quote(2e18)=522,662; quote(1000e18)=261,331,000 → **0.261331 USDC/KNTQ at every size**. Payment token `usdc()` = `0xb88339cb7199b77e23db6e890353e22632ba630f` (native USDC). `owner()` = `0x18a82c968b992d28d4d812920eb7b4305306f8f1`. `merkleRoot()`, `paused()`, `totalClaimed()`, `price()`, `minPurchase()`, `cap()` all revert (not public getters).
- `[own on-chain measurement]` Pool size independently verified: claim contract holds **27,953,424.46 KNTQ** remaining; plus 22,046,576 claimed = **50,000,000 KNTQ exactly**. KNTQ token on HyperEVM = `0x000000000000780555bd0bca3791f89f9542c2d6` (symbol `KNTQ`), `totalSupply()` = **1,000,000,000** → the pool is **5.0% of total supply**.
- Claim-UI mechanics recovered verbatim from the kinetiq.xyz/kntq app bundle (i18n strings): banner "Your allocation lets you claim KNTQ with USDC"; stats shown are **"Claimable" / "Opens" / "Closes" / "Your price"**; error states include **"invalid_proof": "This wallet's allocation could not be verified"** (→ allocation is a fixed per-wallet Merkle entry), **"exceeded": "This is more than your remaining allocation"** (→ remaining allocation tracked), **"below_min": "This amount costs less than the minimum purchase. Increase it or claim your full remaining amount."** (→ a minimum purchase exists), **"paused": "Claiming is paused. Try again later."** (→ claiming is pausable), "expired": "The claim window has closed." — read-only fetch of [kinetiq.xyz/kntq](https://kinetiq.xyz/kntq) (no wallet connected, nothing signed)
- `[own on-chain measurement]` Smallest observed claim = **0.130 KNTQ (~$0.034)**, so the minimum purchase is economically negligible.

### Inferences
- **Aggregate ratio is 1.3587 KNTQ per kPoint** (50,000,000 / 36,800,000). The official post never states a ratio; it only says the final kPoints balance "determines" the allocation. Because the formula is secret by policy, a strictly linear pro-rata split is a reasonable but **unconfirmed** assumption — the aggregate arithmetic is consistent with it, and the implied cost is ~$0.355 per kPoint at $0.261331.
- Allocation is a **Merkle-proof snapshot** fixed before 2026-10-01 12:00 UTC (from `invalid_proof` wording plus the contract deploy on 2026-09-30 19:27 UTC). There is therefore nothing left for a user to "farm", and no way to grow an allocation during the window.
- **Per-wallet cap = the wallet's own allocation; there is no separate global or absolute cap** mentioned anywhere, and the uniform `quote()` plus the exactly-uniform realised price across 3,666 claims (below) shows the "Your price" label is UI phrasing, **not** per-wallet differentiated pricing.
- No sybil filter, clawback, KYC gate, HyperCore-vs-HyperEVM distinction, or per-category breakdown (kHYPE / LP / referral / Ascend) is disclosed in any official text I could reach. Any sybil filtering would have had to happen silently inside the secret allocation formula.

### Gaps
- **The exact points→KNTQ formula is not public and will not be made public** (explicit Kinetiq policy). Cannot confirm linear pro-rata vs tiered/curved.
- Could not read the **@Kinetiq_xyz X thread or its replies** (x.com returns HTTP 402 from this environment), so any extra terms, clarifications or team replies posted only on X are unverified. Same for Discord/Telegram announcement mirrors (not indexed/reachable).
- Official **Terms of Use for this claim** not located (the S1 claim required accepting Foundation Terms of Use; whether this one does is unknown).
- Why the contract charges **0.261331** rather than a round 0.260000 is unexplained in any source — no official statement ties it to a TWAP, a fee, or a rounding convention.
- **Safety flag for the report:** a search result titled "KNTQ Season 2 Claim" at `kntq-claim.vercel.app` is **not** an official Kinetiq domain (official is kinetiq.xyz/kntq). I did not interact with it. Treat as a likely phishing clone.

---

## Why $0.26: justification, implied valuation, and any price-defense commitment

### Takeaway
Kinetiq justified the price **only** as a discount to spot ("roughly 35% below spot" with KNTQ ~$0.40 at publication) and never published a valuation rationale, TWAP methodology, or seed-round/TGE comparison. $0.26 implies a **$260M FDV** (1B supply) — i.e. the team sold the final 5% of supply at a ~14% discount to current spot, and made **no commitment to defend the price**; the only live supply-reduction lever is the pre-existing buyback program plus governance proposal KIP-5.

### Cited Findings
- The only official framing of the price level: **"At the time of publication, KNTQ is trading around $0.40, making the $0.26 fixed price roughly 35% below spot."** — [official post](https://kinetiq.xyz/blog/kntq-kpoints-claim)
- Reported raise: **~$13 million if fully claimed** — [Crypto Briefing](https://cryptobriefing.com/kinetiq-ends-kpoints-kntq-price-drop/), [KuCoin/The Defiant flash](https://www.kucoin.com/news/flash/kinetiq-ends-kpoints-program-switches-to-paid-kntq-claims-token-dips-over-30), [ChainCatcher EN](https://www.chaincatcher.com/en/article/2293658)
- Supply/valuation anchors: max supply **1 billion KNTQ**; the 50M pool is **5% of max supply**; circulating supply reported in a **280–335M** range — [Crypto Briefing](https://cryptobriefing.com/kinetiq-ends-kpoints-kntq-price-drop/)
- Buyback machinery that exists independently of the claim: protocol revenue → **"70% is used for buybacks. The remaining 30% funds treasury operations"**; 100% of validator-commission share, 100% of Markets.xyz disposable income, 100% of Launch deployer-share revenue, all KNTQ trading fees, and 50% of future Elysium sequencer revenue go to buybacks — [kinetiq.xyz/docs/kntq](https://kinetiq.xyz/docs/kntq)
- Governance proposal **KIP-5 ("Redirect All Purchased KNTQ to the Hyperliquid Assistance Fund", 2026-09-16)** directs revenue-funded buybacks to the Hyperliquid Assistance Fund to reduce KNTQ supply permanently; **prior buybacks acquired 5.39M+ KNTQ at a ~$0.15 average** — [Crypto Briefing](https://cryptobriefing.com/kinetiq-ends-kpoints-kntq-price-drop/), proposal listed at [kinetiq.xyz/blog](https://kinetiq.xyz/blog/kip-5-kntq-buybacks-assistance-fund)
- Price context at announcement (multiple outlets, broadly consistent, small differences): ATH **~$0.448 on 2026-10-01**, then **−20%+ to ~$0.33** by the time of writing — [Crypto Briefing](https://cryptobriefing.com/kinetiq-ends-kpoints-kntq-price-drop/); pre-announcement **~$0.422**, low **$0.281 (−33%)**, recovery **~$0.325 (−23%)** — [KuCoin flash](https://www.kucoin.com/news/flash/kinetiq-ends-kpoints-program-switches-to-paid-kntq-claims-token-dips-over-30), [PANews](https://panews.io/articles/01a0fadf-a2e6-7703-97f5-9d43f1a3f6e7), [Odaily](https://www.odaily.news/zh-CN/newsflash/522068), [WuBlock](https://www.wublock123.com/news/kinetiq-kpoints-program-ends-kntq-falls-23-percent-69415)
- Price as of **2026-10-03 14:23 UTC: $0.3049**, 24h change **+5.82%**, 24h volume **$3.88M (−67.65%)**; the analysis frames **$0.30 as the critical support** — "If KNTQ holds the $0.30 support, it could rebound with a market recovery; a break below risks a test of $0.28" — and attributes the decline to a "market-wide risk-off move" — [CoinMarketCap CMC-AI price analysis](https://coinmarketcap.com/cmc-ai/kinetiq/price-analysis/)

### Inferences
- **$0.261331 ⇒ FDV ≈ $261.3M** at 1B supply (vs ~$305M at $0.3049 on Oct 3 and ~$448M at the Oct 1 ATH). Against a reported 280–335M circulating, $0.26 implies a **$73–87M market cap**. The "~$302M FDV at $0.3022" figure in the brief is consistent with the same FDV convention.
- The discount has compressed hard: **~35% below spot at announcement → ~14.3% below spot at $0.3049**. The option's moneyness, not the headline price, is what has changed.
- I found **no statement of any kind** from Kinetiq about defending $0.26, buying back during the window, or about claimant arbitrage. The buyback program is revenue-driven and mechanical, not a price-defense pledge; KIP-5 would change its *destination*, not its size.
- Note an internal tension worth flagging in the report: the docs say buybacks are sent to the **sKNTQ staking contract** for stakers, while KIP-5 would redirect purchased KNTQ to the **Hyperliquid Assistance Fund**. If KIP-5 passes, sKNTQ's yield source changes — relevant to whether claimants are incentivised to stake rather than sell.

### Gaps
- **No source ties $0.26 to a seed round (~$17.5M pre-money), to a ~$0.11 TGE price, or to any TWAP.** I could not verify the seed valuation or the $0.11 TGE price from any source — both should be treated as unconfirmed in the final report.
- No official explanation exists for *why* this level; the only published anchor is "~35% below spot".
- No team statement on arbitrage, price defense, or buyback timing around the claim.

---

## Participation: how much of the 50M has actually been claimed

### Takeaway
**No official dashboard, API or statement on claim progress exists**, and I found no third-party (Dune/analyst) count. I therefore measured it directly from the contract's `Claimed` logs: as of **2026-10-03 23:18 UTC, 44.09% of the 50M pool (22,046,576 KNTQ) has been claimed by 3,059 wallets for $5,761,454 USDC** — and the take-up is extremely front-loaded, with 38.6% of the entire pool claimed on day one and the daily pace now down ~93% from day one.

### Cited Findings
- `[own on-chain measurement]` Method: all `Claimed(address,uint256,uint256)` logs (topic0 `0x987d620f...a2f9a`) on `0x435bb7ea4eb481cb686606d089ea4dee4c6cc03b` from the window-open block 47,376,135 (2026-10-01T12:00:00Z) to block 47,593,106 (2026-10-03T23:18:16Z), via [hyperliquid-rpc.publicnode.com](https://hyperliquid-rpc.publicnode.com) and [rpc.hypurrscan.io](https://rpc.hypurrscan.io). Event decodes as (claimer, KNTQ 18dp, USDC 6dp).
- `[own on-chain measurement]` **Totals: 3,666 claim events; 3,059 unique wallets; 22,046,576 KNTQ claimed = 44.093% of the 50M pool; 5,761,454 USDC paid; realised price exactly 0.261331 for every claim** (no per-wallet price variation).
- `[own on-chain measurement]` **Cross-check:** contract KNTQ balance 27,953,424.46 (= 55.91% unclaimed) and contract USDC balance **5,761,453.63** — the USDC balance equals the collected amount, i.e. **the team has not withdrawn any proceeds yet** (no `Withdrawn` effect visible).
- `[own on-chain measurement]` **Pace, UTC days:**
  - 2026-10-01 (12:00–24:00): 2,458 claims, **19,289,818 KNTQ (38.58% of pool)**, $5,041,027
  - 2026-10-02: 495 claims, **1,501,029 KNTQ (+3.00%)**, $392,265
  - 2026-10-03 (to 23:18): 713 claims, **1,255,729 KNTQ (+2.51%)**, $328,161
- `[own on-chain measurement]` **First hour (2026-10-01 12:00–13:00 UTC): 801 claims, 7,096,543 KNTQ = 14.2% of the entire pool.** Hours 2–4 added ~8.4M more; by 16:00 UTC on day one ~15.4M (30.8%) was already claimed.
- `[own on-chain measurement]` **Concentration:** per-wallet claimed KNTQ — min 0.13, p25 28.4, **median 305.2**, p75 2,493, p95 20,052, **max 1,422,137**. **Top 10 wallets = 33.18% of all KNTQ claimed.** Largest five: `0x9794bb…333b` (1,422,137), `0x63af85…4b36` (1,063,938), `0xbd8c75…971d` (996,418), `0x9f58a3…1dfb` (919,443), `0x0b8382…3140` (612,531).
- Officially published participation stats: none found on [kinetiq.xyz/kntq](https://kinetiq.xyz/kntq), [kinetiq.xyz/blog/kntq-kpoints-claim](https://kinetiq.xyz/blog/kntq-kpoints-claim) or [kinetiq.xyz/docs/kpoints](https://kinetiq.xyz/docs/kpoints); the claim app exposes no public stats endpoint (only an on-page "Claimable / Opens / Closes / Your price" panel scoped to the connected wallet).
- Press coverage through 2026-10-03 reports no claim-rate figure, only that take-up matters: "the key variable is how much of the 50 million tokens actually gets claimed and sold" — [KuCoin flash, 2026-10-02](https://www.kucoin.com/news/flash/kinetiq-ends-kpoints-program-kntq-price-drops-23-after-token-sale-launch)

### Inferences
- **The marginal claimer is now a much smaller wallet.** Day-one average claim was ~7,848 KNTQ; Oct 3's average is ~1,761. The large, price-insensitive allocations went first, which is exactly the behaviour of claimants who intended to monetise immediately.
- **Straight-line projection to expiry is ~31–32M (62–64%)** at the current ~1.26M/day pace over the remaining 7.5 days — but deadline-driven claiming is normally bimodal, so a final-48-hour spike toward 2026-10-11 12:00 UTC should be expected. Anything from ~60% to ~85% final take-up is consistent with the data so far; **full 100% take-up now looks unlikely** given 56% is still outstanding with the discount down to ~14%.
- **Aggregate claimant P&L is thin: $5.76M paid, worth ~$6.72M at $0.3049 — about +$0.96M (+16.7%) gross, unhedged.** That is small relative to the slippage of selling 22M tokens into a $3.88M/day market, which is a strong reason to expect claimants to drip-sell rather than dump, and an equally strong reason why the marginal claimant quits as spot approaches $0.26.
- **Liquidity is the binding constraint, not the pool size.** 24h volume was $3.88M on Oct 3; already-claimed tokens are ~$6.7M notional (≈1.7x daily volume) and the unclaimed remainder is ~$8.5M notional (≈2.2x daily volume). A $0.26 "floor" has to absorb sell flow several times larger than daily turnover.

### Gaps
- No Dune dashboard for Kinetiq claims found via search; no analyst/X thread counts located (X inaccessible, HTTP 402).
- I did not attribute wallets to CEX deposit addresses or trace post-claim selling (teammates cover flows), so **claimed ≠ sold** here; the 22.05M figure is an upper bound on realised sell pressure to date.
- `Withdrawn`/`Bridged` event counts were not separately enumerated (a broader unfiltered log pull was rejected 403 by the public RPC); the USDC-balance identity is the evidence that nothing has been withdrawn.

---

## Season 1 precedent

### Takeaway
Season 1 was the opposite structure — a **free** airdrop of **24% of supply** to kPoints holders at the November 2025 TGE — which is precisely why the paid S2 terms landed badly. I could **not** verify an S1 claim rate, sell-through data, or any team post-mortem; the only hard S1 facts I could source are the allocation and claim-deadline terms.

### Cited Findings
- Announced **2025-10-22**, article published **2025-10-23**: the initial airdrop covered **25% of the 1B supply — 24% to kPoints holders and 1% to Hypurr holders**; remaining allocations 30% protocol growth/rewards, 23.5% core contributors, 10% foundation, 7.5% investors, 4% liquidity — [blocmates](https://www.blocmates.com/news-posts/kinetiq-foundation-announces-kntq-token-launch-allocating-24-to-kpoints-holders)
- S1 claim condition and deadline: **claim by 2025-11-21 20:00 UTC**, with participants required to **accept the Kinetiq Foundation's Terms of Use** to be eligible — [blocmates](https://www.blocmates.com/news-posts/kinetiq-foundation-announces-kntq-token-launch-allocating-24-to-kpoints-holders)
- Core contributors and investors: **3-year vesting, 1-year cliff**, then monthly linear over 2 years — [blocmates](https://www.blocmates.com/news-posts/kinetiq-foundation-announces-kntq-token-launch-allocating-24-to-kpoints-holders), [kinetiq.xyz/docs/kntq](https://kinetiq.xyz/docs/kntq)
- Genesis/TGE: KNTQ launched **2025-11-27 on Hyperliquid**, described as the first major Hyperliquid ecosystem token launch; Kinetiq had ~$1.6B TVL at the time of the token announcement — [kinetiq.xyz/docs/kntq](https://kinetiq.xyz/docs/kntq), [blocmates](https://www.blocmates.com/news-posts/kinetiq-foundation-announces-kntq-token-launch-allocating-24-to-kpoints-holders)
- An institutional S1 recipient disclosed receipt publicly (useful for sizing S1 recipients): Hyperion DeFi (NASDAQ: HYPD) press release announcing **receipt of the Kinetiq airdrop** — [ir.hyperiondefi.com](https://ir.hyperiondefi.com/news-events/press-releases/detail/300/hyperion-defi-announces-receipt-of-kinetiq-airdrop-partnership-with-native-markets-and-purchase-of-150-000-additional-hype)
- S2 contrast is the core of the press narrative: the shift is "from a free points-based model to a paid subscription model" — [WuBlock](https://www.wublock123.com/news/kinetiq-kpoints-program-ends-kntq-falls-23-percent-69415), [KuCoin/MarsBit flash](https://www.kucoin.com/news/flash/kinetiq-ends-kpoints-program-kntq-price-drops-23-after-token-sale-launch)

### Inferences
- The S1 free allocation (**240M KNTQ**) is ~**10.9x** the KNTQ claimed in S2 so far and ~4.8x the entire S2 pool. S2's 50M is a second-order supply event by comparison — its importance is **informational** (a hard, public reservation price plus a known expiry) rather than raw supply.
- The brief's S1 price path (**−76% to $0.0358 by 2025-12-17**) is teammate-verified and I could not independently corroborate it from any source I reached; if used in the report, keep it attributed to the teammate's verification, not to a published source here. Note the obvious implication if true: **$0.26 today is ~7.3x the December 2025 low**, so "the claim price is the floor" is a claim about a level the token traded *far* below less than a year ago.
- The S1 claim deadline (2025-11-21) preceding the stated TGE (2025-11-27) means S1's "claim" was an **eligibility acceptance** step, not a market-priced decision — structurally nothing like S2's paid option.

### Gaps
- **No S1 claim rate, no S1 unclaimed/forfeited figure, no sell-through data, and no team post-mortem** found in any reachable source.
- S1 TGE price and opening FDV not verified (no source found); the ~$0.11 TGE figure in the brief remains unconfirmed.

---

## Arbitrage mechanics and what happens at expiry (2026-10-11 12:00 UTC)

### Takeaway
The "no hedge" premise checks out: I verified there is **no KNTQ perpetual anywhere on Hyperliquid** — not in the 234-market main perp universe nor in any of the 10 builder-deployed (HIP-3) perp dexes. With no lockup, no perp and a hard expiry, a claimant's only monetisation is spot selling above $0.261331, which makes $0.26 a **reservation price that is self-enforcing only while the window is open** — it is a feature of the *option*, not of the *market*, and it disappears at 12:00 UTC on Oct 11.

### Cited Findings
- `[own on-chain measurement, 2026-10-03 ~23:25 UTC]` Hyperliquid `meta` returns **234 perp markets, none containing "KNTQ"**; `perpDexs` returns 10 builder dexes (`xyz`, `flx`, `vntl`, `hyna`, `km`, `abcd`, `cash`, `para`, `mkts`, `io`) totalling 299 further markets, **none containing "KNTQ"** — queried via [api.hyperliquid.xyz/info](https://api.hyperliquid.xyz/info)
- The published floor/ceiling framing: "If sell pressure from the claim event subsides after the window closes … KNTQ could find support near $0.26; a sustained break below that level risks a deeper correction toward $0.24. For points holders, the claim only makes sense as long as KNTQ trades above $0.26, and the 10-day window caps how long anyone can wait to decide." — [KuCoin flash](https://www.kucoin.com/news/flash/kinetiq-ends-kpoints-program-kntq-price-drops-23-after-token-sale-launch)
- The arbitrage channel stated explicitly in coverage: with spot at **$0.293 when the window opened**, the gap "created an immediate arbitrage incentive for claimants to sell for a quick profit, driving the price down toward the claim price" — [KuCoin flash](https://www.kucoin.com/news/flash/kinetiq-ends-kpoints-program-shifts-to-paid-token-allocation-as-kntq-drops-23)
- Near-term technical frame on Oct 3: **$0.30 support, break risks $0.28** — [CMC-AI](https://coinmarketcap.com/cmc-ai/kinetiq/price-analysis/)
- Foundation's stated use of unclaimed tokens is **"ecosystem and growth initiatives"** — [official post](https://kinetiq.xyz/blog/kntq-kpoints-claim); press repeats "ecosystem and growth initiatives" with no further detail — [Crypto Briefing](https://cryptobriefing.com/kinetiq-ends-kpoints-kntq-price-drop/), [KuCoin](https://www.kucoin.com/news/flash/kinetiq-ends-kpoints-program-switches-to-paid-kntq-claims-token-dips-over-30)
- The only supply-reduction commitment in play is buyback-based (KIP-5 → Hyperliquid Assistance Fund, "to reduce KNTQ supply permanently"; prior buybacks 5.39M+ KNTQ at ~$0.15 avg) — [Crypto Briefing](https://cryptobriefing.com/kinetiq-ends-kpoints-kntq-price-drop/)

### Inferences
- **$0.26 behaves as a magnet, not a floor, while the window is open.** Any claimant who still wants the tokens is indifferent between buying at 0.261331 from the contract and buying on-market below that, so **market bids above $0.26 are structurally cannibalised by the contract**: the contract is an infinitely-deep offer at 0.261331 for 27.95M tokens to anyone with an allocation. That caps rallies for allocation holders and removes a natural buyer base — a mechanism that looks like support but acts like a ceiling on claimant demand.
- **The real asymmetry is below $0.26, and it is stabilising.** If spot trades under 0.261331, remaining claims stop being rational, so up to 27.95M tokens of latent supply is switched off and reverts to the Foundation. That is the genuine floor-like property: **sub-$0.26 kills the supply, so the supply overhang is self-limiting, not self-reinforcing.**
- **Expiry is a supply-cliff *end*, not a supply cliff.** At 2026-10-11 12:00 UTC the forced-decision pressure ends and no new claimant supply can be created. Mechanically that is bullish-at-the-margin; the offsetting risk is that claimants who bought purely for the arbitrage still hold unsold inventory after the catalyst that justified it has passed.
- **A "$0.26 floor" has no enforcement mechanism after Oct 11.** Nothing in any official document commits the Foundation or treasury to bid at $0.26; the buyback is sized by revenue, and KIP-5 historically bought at ~$0.15 — far below the claim price. Treat $0.26 post-expiry as a **psychological/reference level with a cost-basis cluster behind it**, not a bid.
- The Foundation receiving ~28M unclaimed KNTQ (if take-up stalls near 44–60%) **re-centralises 2.8–3.1% of supply into a discretionary bucket** with no stated lockup, which is a mild medium-term overhang the report should name — the opposite of a burn.

### Gaps
- **No official statement on whether unclaimed KNTQ will be burned, locked, vested or sold** — only "ecosystem and growth initiatives". No timeline, no commitment not to sell.
- No statement about whether proceeds (USDC, $5.76M and counting, still sitting in the claim contract) will fund buybacks, treasury, or anything else.
- No analyst modelling of the expiry event found; the only published forward view is the KuCoin "support near $0.26 / break risks $0.24" line.

---

## Sentiment: how the community reacted

### Takeaway
The only *named*, citable reaction I could source is **DeFi Dad**, who liked the structure but panned the communication. Everything else in indexed English/Chinese media is newswire reprint with no community colour — and the single most informative sentiment datapoint is behavioural, not verbal: **44% of the pool was claimed in under three days, 38.6% of it on day one**, which is not the behaviour of a community that refused to pay.

### Cited Findings
- **DeFi Dad** (DeFi educator/podcast host) supported the purchase-option approach but criticised the communication: **"I wish more teams offered up these call options instead"**, adding that the team should have stated upfront that users would receive an option to buy discounted $KNTQ — [cryptonews.net](https://cryptonews.net/news/defi/33528205/), [Crypto Briefing](https://cryptobriefing.com/kinetiq-ends-kpoints-kntq-price-drop/)
- The expectation-gap framing: "Some farmers who spent 46 weeks accumulating points may have expected a free allocation" — [Crypto Briefing](https://cryptobriefing.com/kinetiq-ends-kpoints-kntq-price-drop/)
- Chinese-language coverage exists but is pure newswire with no community commentary: [ChainCatcher CN](https://www.chaincatcher.com/article/2293658), [Odaily](https://www.odaily.news/zh-CN/newsflash/522068), [WuBlock](https://www.wublock123.com/news/kinetiq-kpoints-program-ends-kntq-falls-23-percent-69415), [PANews](https://panews.io/articles/01a0fadf-a2e6-7703-97f5-9d43f1a3f6e7)
- Airdrop-aggregator framing calls it out as "a paid token allocation, not a free claim" (2026-10-03) — [AirdropAlert](https://airdropalert.com/blogs/pons-rev-down-90-crypto-airdrop-update/)
- Note for the report: [airdrops.io/kinetiq](https://airdrops.io/kinetiq/) still carries the headline "Claim free KNTQ tokens", i.e. aggregator pages are stale/misleading versus the actual paid terms.

### Gaps
- **X/Twitter is inaccessible from this environment (HTTP 402 on x.com)**, so I could not read the Oct 1 announcement replies, quote-tweets, or any KOL calls with dates. This is the single biggest gap in this section — **no Vietnamese, Korean, or substantive Chinese community sentiment was obtainable**, and I found no Discord/Telegram mirrors indexed.
- No dated KOL price calls (bullish or bearish) located beyond DeFi Dad's structural comment.
- No evidence either way on claimants' intent to stake into sKNTQ rather than sell.

---

## Historical analogs: did a fixed claim price become support, a ceiling, or break?

### Takeaway
I found **no documented precedent for this exact structure** (points holders granted a short-dated, unlockable right to buy at a fixed price) in reachable sources — the model is genuinely unusual, which is itself a finding. What I could source is a strong **2026 base rate for claimant behaviour and post-claim price paths**, and it is bearish: three in four 2026 airdrop tokens trade below their first-week price, with a median −48%.

### Cited Findings
- **Bitquery study of 51 major 2026 airdrops (2026-01-01 to 2026-09-29; Ethereum, BNB Chain, Base, Arbitrum; each ≥5,000 wallets and ≥$1M), $809.4M distributed at claim-day prices** — [Bitquery](https://bitquery.io/investigations/crypto-airdrops-2026):
  - **35 of 46 tokens (76%) trade below their first-week median price; median price change −48%**
  - **73% of claimers moved tokens within one day** in the median drop
  - **Only 23% still held at least half their allocation after 30 days; 8% at 90 days**
  - **Top 10% of claimers received 73% of tokens** in the median drop; **top 1% ≈ 34%**
  - Named cases: **Brevis (BREV)** — seven in ten claimers moved tokens within one hour, now ~78% below first week; **ROBO** — one farming group claimed 87% via 11,204 linked wallets; exceptions: **Bitway (BTW) ~93x**, **ENA/sENA doubled**
  - 25 of 51 launches spawned counterfeit tokens pushed into wallets 5.4 million times
- Scale comparison for the Hyperliquid ecosystem: **Lighter's December 2025 airdrop distributed 250M LIT worth ~$675M on day one** — [AirdropAlert](https://airdropalert.com/blogs/lighter-review)
- General presale/fixed-price structure context (not a specific analog): presales sell at a fixed price below the planned listing, typically with immediate staking availability; "lockups" are what prevent immediate selling, and tokens only stabilise once transfer restrictions expire — [a16z crypto](https://a16zcrypto.com/posts/article/airdrops-safe-legal-frequent/), [DappRadar](https://dappradar.com/rewards)

### Inferences
- **The closest structural kin to this claim is a short-dated covered call / rights issue, not an airdrop.** Kinetiq's own supportive critic framed it exactly that way ("these call options"). The useful analogy set is therefore *rights issues and ICO/presale cost-basis clusters*, where the standard result is that the subscription price acts as a reference level that holds while the offer is live and is frequently broken afterwards — but I could not source a crypto-specific, named, dated example of that outcome, so **the report should not assert a precedent it cannot cite.**
- **Applying the 2026 base rate with the one structural difference that matters:** in a free airdrop the claimant's cost basis is zero, so 73% sell within a day and median drawdown is −48%. Here every claimant paid 0.261331, so the marginal seller's reservation price is a real number rather than zero. That is a genuine reason to expect **shallower, slower selling than the base rate** — the mechanism that produced 76%-below-first-week outcomes (costless supply) is partly disabled.
- **But the base rate's concentration finding transfers directly and is confirmed here:** the top 10% of claimers taking ~73% of tokens in the median 2026 drop matches my measured 33.18% in just the top 10 wallets. Concentrated, sophisticated claimants are precisely the cohort that hedges or exits fastest — and with **no KNTQ perp to hedge into**, their only exit is spot.
- **Verdict framing for the report (my inference, clearly labelled):** $0.26 is best described as **a magnet until 2026-10-11 12:00 UTC and a reference level afterwards, not a floor.** It is magnet-like because the contract's standing offer at 0.261331 caps claimant bids above it; it is floor-*like* only in the narrow mechanical sense that sub-$0.26 trading switches off the remaining 27.95M of claimable supply; and it is a potential cliff edge because nothing — no lockup, no perp, no buyback pledge, no Foundation commitment — enforces the level once the window shuts, and a 2026 base rate of −48% median post-claim drawdown argues against treating any claim price as structural support.

### Gaps
- **No named crypto precedent located** for "points holders get the right to buy at a fixed price, no lockup, short window" — I could not source Legion, Echo/Sonar, Kaito-style community-sale outcomes, nor a Hyperliquid-ecosystem equivalent, from any reachable indexed source. Multiple query formulations returned only generic airdrop/presale/tax content.
- Bitquery's universe is **Ethereum/BNB/Base/Arbitrum and free airdrops** — it does not cover HyperEVM or paid claims, so it is a base rate, not a like-for-like comparison.
- No study found on how ICO/presale prices behaved as support, with magnitudes and dates.

---

## Appendix: reusable method for monitoring claim take-up (for the 2-hourly tracking task)

`[own on-chain measurement]` Two independent reads, both cheap and wallet-free:

1. **Remaining pool (single call, exact):** `eth_call` → `balanceOf(0x435bb7ea4eb481cb686606d089ea4dee4c6cc03b)` on KNTQ `0x000000000000780555bd0bca3791f89f9542c2d6`; claimed = `50,000,000 − balance`. Baseline: balance **27,953,424.46** at block 47,593,106 (2026-10-03 23:18:16 UTC).
2. **Wallet count + pace:** `eth_getLogs` on the claim contract, topic0 `0x987d620f307ff6b94d58743cb7a7509f24071586a77759b77c2d4e29f75a2f9a` (`Claimed(address,uint256,uint256)`), decoding topics[1]=claimer, data word0=KNTQ (18dp), word1=USDC (6dp). Baseline: **3,666 events / 3,059 wallets / 22,046,576 KNTQ / 5,761,454 USDC**.
   - RPC limits observed: [rpc.hypurrscan.io](https://rpc.hypurrscan.io) caps `eth_getLogs` at **1,000 blocks**; [hyperliquid-rpc.publicnode.com](https://hyperliquid-rpc.publicnode.com) accepted **50,000-block** spans *with* a topic filter but returned **403** for unfiltered pulls. Window-open block = **47,376,135**; expiry (2026-10-11 12:00:00 UTC) will land near block **~48.1M** (≈1 block/s observed).
3. **Proceeds check:** USDC `0xb88339cb7199b77e23db6e890353e22632ba630f` `balanceOf(claimContract)` = **5,761,453.63** — equals collected, so a divergence signals the team withdrawing proceeds.
