# Kinetiq (KNTQ) — Fundamentals, Intrinsic Growth and Tokenomics (as of 2026-10-03)

**Convention used below:** `[V]` = verified by me this session (direct API/RPC call, output inspected); `[R]` = reported by a secondary source, not independently verified. All "as of" timestamps are UTC. Snapshot taken 2026-10-03 ~23:10–23:30 UTC.

**Headline price/valuation anchors used throughout** `[V]`: KNTQ $0.303325; mcap $85,075,857; FDV $303,326,377; circulating 280,476,290; total/max supply 1,000,000,000; ATH $0.452145 on 2026-10-01T06:18:50Z; ATL $0.03578 on 2025-12-17; +53.8% 30d, +206.7% 60d, +99.2% 200d; CG `last_updated` 2026-10-03T23:12:40Z — [CoinGecko API /coins/kinetiq](https://api.coingecko.com/api/v3/coins/kinetiq). HYPE = $89.36 `[V]` ([CoinGecko simple/price](https://api.coingecko.com/api/v3/simple/price?ids=hyperliquid&vs_currencies=usd)); HyperCore HYPE mid = $87.99 `[V]` ([Hyperliquid info API, allMids](https://api.hyperliquid.xyz/info)).

---

## Q1. Protocol metrics: kHYPE supply, TVL, market share, rank vs other Hyperliquid LSTs, and the 30/90/180-day trend

### Takeaway
Kinetiq is unambiguously the dominant Hyperliquid LST — ~83% of all Hyperliquid LST TVL, >5x the #2 (stHYPE) — but **the business is shrinking in HYPE terms, hard and continuously**: staked HYPE fell from a 50.07M peak (2025-10-04) to 29.69M at TGE (2025-11-27) to **12.47M on 2026-10-03** (−58% since TGE, −75% from peak). USD TVL has been flat-to-down (~$1.1–1.3B) only because HYPE's price rose. Market share is stable because the *entire* Hyperliquid LST category more than halved alongside it, not because Kinetiq is winning.

### Cited Findings

**TVL in USD (DefiLlama parent protocol, Hyperliquid L1)** `[V]` — [api.llama.fi/protocol/kinetiq](https://api.llama.fi/protocol/kinetiq):
| Date | TVL (USD) |
|---|---|
| 2025-10-04 (all-time peak) | $2,653,266,457 |
| 2025-11-27 (TGE) | $1,130,549,762 |
| 2026-01-01 | $696,774,636 |
| 2026-04-05 (180d ago) | $792,783,650 |
| 2026-07-05 (90d ago) | $1,124,019,756 |
| 2026-09-05 (30d ago) | $1,264,676,407 |
| 2026-09-20 | $1,301,054,975 |
| 2026-10-03 (latest) | $1,112,975,403 |

→ USD TVL: **−12.0% over 30d, −1.0% over 90d, +40.4% over 180d** (the 180d gain is HYPE price, not inflows).

**TVL in HYPE units — the real growth metric** `[V]` — same endpoint, `tokens` series (HYPE + WHYPE):
| Date | HYPE | WHYPE | Total HYPE-equivalent |
|---|---|---|---|
| 2025-10-04 (peak) | — | — | **50,068,715** |
| 2025-11-27 (TGE) | 28,107,844 | 1,579,280 | 29,687,124 |
| 2026-01-01 | 25,215,786 | 1,902,966 | 27,118,753 |
| 2026-04-05 (−180d) | 20,583,656 | 1,203,566 | 21,787,222 |
| 2026-07-05 (−90d) | 15,460,080 | 685,644 | 16,145,724 |
| 2026-09-05 (−30d) | 14,289,920 | 698,045 | 14,987,965 |
| 2026-10-03 | 12,004,188 | 466,143 | **12,470,331** |

→ **−16.8% (30d), −22.8% (90d), −42.8% (180d), −58.0% since TGE, −75.1% from peak.** The decline is monotonic month over month with no inflection in any 30-day window since TGE. `[V]`

**On-chain LST token supplies, HyperEVM, read directly 2026-10-03 ~23:20 UTC** `[V]` (eth_call `totalSupply()` via `https://hyperliquid-rpc.publicnode.com`; token addresses from [Kinetiq docs — Contracts and audits](https://kinetiq.xyz/docs/contracts-and-audits)):
- kHYPE `0xfD739d4e423301CE9385c1fb8850539D657C296D`: **10,718,476.27**
- kmHYPE `0x360C140E5344A1A0593D44B4ea6Fc7C3DAf0C473`: **511,244.64**
- GhostLST `0x74323CD0Db2FD826CadCc90153995F1E2b1d0801`: 564,209.91
- HiHYPE (Hyperion, via Kinetiq Launch) `0x4f322145aBedb2b39f69e7d4531AB4B2e6483154`: 398,804.11
- hylqHYPE: 147.16 | flowHYPE: 0.01 | asxnHYPE: 0.03 → **three of the four named "institutional"/Launch LSTs are effectively dead**
- stHYPE (competitor, Valantis/Thunderhead) `0xfFaa4a3D97fE9107Cef8a3F48c069F577Ff76cC1`: **2,291,855.73**

→ Implied kHYPE NAV: DefiLlama kHYPE TVL of 11,404,710 HYPE ÷ 10,718,476 kHYPE = **~1.064 HYPE per kHYPE** `[V]` (inference from two verified figures).

**Hyperliquid LST league table, 2026-10-03** `[V]` — [api.llama.fi/protocols](https://api.llama.fi/protocols) + per-protocol endpoints:
| # | Protocol | TVL USD | HYPE units | 7d chg |
|---|---|---|---|---|
| 1 | Kinetiq kHYPE | $1,020,605,499 | 11,404,710 | −9.2% |
| 2 | stHYPE | $205,148,488 | 2,291,853 | −5.9% |
| 3 | Kinetiq kmHYPE (Markets) | $46,856,609 | 523,907 | −11.6% |
| 4 | Hyperbeat LST (beHYPE) | $13,876,963 | 155,029 | −9.0% |
| 5 | Kinetiq Launch (all LSTs) | $6,596,431 | 73,712 | −3.9% |
| 6 | Kintsu | $2,691,181 | 800 | +6.2% |
| 7 | SpinUp Liquid Staking | $233,685 | — | −9.4% |
| 8 | Stratium HYPE Staking | $4,054 | — | −4.0% |

- **Kinetiq total (kHYPE + kmHYPE + Launch) = $1,074,058,539 = 83.1% of the $1.29B Hyperliquid LST category; kHYPE alone = 79.0%.** `[V]`
- LoopedHYPE (LHYPE) is classified by DefiLlama as *Yield*, not Liquid Staking: mcap $8.21M, TVL $8.20M — a wrapper, not a peer base LST. `[V]`

**Market-share trend (Kinetiq share of Hyperliquid LST HYPE units)** `[V]` — computed from per-protocol `tokens` series:
| Date | kHYPE | kmHYPE | Launch | stHYPE | Hyperbeat | Kintsu | Kinetiq share |
|---|---|---|---|---|---|---|---|
| 2025-11-27 | 28,107,844 | 0 | 0 | 1,328,310 | 931,880 | 0 | **92.6%** |
| 2026-01-01 | 24,319,707 | 896,079 | 0 | 3,523,769 | 563,557 | 3,739 | 86.0% |
| 2026-04-05 | 19,785,702 | 797,954 | 0 | 3,564,405 | 469,448 | 1,612 | 83.6% |
| 2026-07-05 | 14,784,466 | 620,821 | 54,794 | 2,811,781 | 188,062 | 900 | 83.8% |
| 2026-09-05 | 13,652,199 | 588,919 | 48,803 | 2,570,832 | 161,507 | 789 | 83.9% |
| 2026-10-03 | 11,404,710 | 523,907 | 73,712 | 2,291,853 | 155,029 | 800 | **83.1%** |

→ Share lost 9.5pp in the first 4 months post-TGE, then has been **flat at 83–84% for six months**. Category total HYPE went 30.4M → 14.45M (−52%) over the same period. `[V]`

**Share of ALL staked HYPE (not just LSTs)** `[V]` — [Hyperliquid info API `validatorSummaries`](https://api.hyperliquid.xyz/info), 35 validators, read 2026-10-03:
- Total staked HYPE on Hyperliquid: **437,160,014** (active set 437,101,487) ≈ $39.1B at $89.36.
- Kinetiq's 12,470,331 HYPE = **2.85% of all staked HYPE.** `[V]`
- Validator predicted APR (week): median **2.18%**, range 0.00–2.24%. `[V]`
- Kinetiq runs one named validator: "Kinetiq x Hyperion", 6,129,152 HYPE staked, 4% commission, active. `[V]`

### Inferences
- The gross staking-yield pool Kinetiq sits on is ~2.18% APR × 12.47M HYPE ≈ 272k HYPE/yr ≈ $24.3M/yr — which matches DefiLlama's annualized "Fees" of $25.8M almost exactly, a good cross-check that the fee data is real. `[V]`
- Kinetiq's moat is *category* dominance in a category that is contracting. The bull case cannot rest on share gains (share is pinned) — it must rest on (a) HYPE price, (b) the whole LST category re-growing, or (c) non-LST products. (a) is the only one currently working.
- The 83% share being *stable* while absolute HYPE halves suggests the outflow is category-wide (users unstaking/rotating out of Hyperliquid LSTs generally), not Kinetiq-specific churn.

### Gaps
- I could not find a Kinetiq- or ASXN-published dashboard giving kHYPE supply/HYPE-staked directly from the protocol, to cross-check DefiLlama's token series. The on-chain `totalSupply()` reads above are the independent check I was able to make.
- Reason for the 180-day HYPE outflow (unstaking to sell HYPE, rotation into native staking/HLP, or competitive loss to off-DefiLlama venues) is not established.

---

## Q2. Revenue: fees, take rate, and the other products (Ascend, Markets, Elysium, Launch)

### Takeaway
**This is the one genuinely bullish data series.** Kinetiq's *revenue* has more than doubled since the April 2026 fee switch — $199.8k (Apr) → $410.6k (Sep 2026), ~$4.9M annualized — even while HYPE TVL fell 43%. The growth is from a higher take rate and new products, not from growth in the staking base. But the new products are tiny in absolute terms, Elysium is **still a testnet** today, and only ~36% of revenue currently routes to the token.

### Cited Findings

**Fee/revenue architecture — primary source** `[V]` — [Kinetiq docs, KNTQ page](https://kinetiq.xyz/docs/kntq) ("Last updated September 16, 2026") and DefiLlama adapter methodology `[V]` ([api.llama.fi/summary/fees/kinetiq](https://api.llama.fi/summary/fees/kinetiq)):
- kHYPE: **0.1% unstaking fee only, before 2026-04-09; 10% performance fee on staking rewards from 2026-04-09.** Of that performance fee, **70% → KNTQ buybacks, 30% → treasury** (KIP-2). 90% of staking rewards stay with stakers.
- Validator commissions: active-set validators share **50% of the commission they charge on Kinetiq's stake, in perpetuity, as a condition of opting in** (`invoice_rate_bps = 5000`). Docs: "100% of Kinetiq's share is used for buybacks"; DefiLlama adapter says 70% buyback / 30% treasury — **direct conflict, see Q4.**
- Kinetiq Earn (vkHYPE, Veda strategy vault): **20% performance fee on vault profits**, profit-only, no management or entry/exit fee. 0% to holders.
- Kinetiq Markets (HIP-3 `km`/`mkts`): Kinetiq's deployer-fee cut; docs say 100% of "disposable Markets income (minimum 10% of deployer share plus builder code revenue)" → buybacks.
- Kinetiq Launch: 10% performance fee on partner-LST staking rewards; 70% buyback / 30% treasury default.
- KNTQ spot trading fees: `deployerTradingFeeShare = 1.0` `[V]` (verified in Hyperliquid `spotMeta` for token index 124) → Kinetiq keeps the entire KNTQ-denominated spot fee; docs say **100% is sent directly to the Assistance Fund**.
- Elysium: **50% of sequencer revenue programmatically buys KNTQ on the open market.**

**Consolidated P&L, DefiLlama, 2026-10-03** `[V]`:
| Window | Fees (gross, incl. pass-through yield) | Revenue (Kinetiq's cut) | Protocol Revenue (treasury) | Holders Revenue (buybacks) |
|---|---|---|---|---|
| 24h | $64,948 | $8,777 | $4,356 | $4,422 |
| 7d | $488,310 | $82,526 | $48,740 | $33,786 |
| 30d | $2,121,444 | $403,674 | $257,627 | $146,045 |
| 90d | $5,946,613 | $1,030,729 | $634,267 | $396,454 |
| 180d | $11,610,229 | $1,832,691 | $1,294,612 | $1,291,524 |
| 1y | $27,919,405 | $4,239,972 | $3,707,898 | $1,285,521 |
| all-time | $38,727,184 | $5,071,911 | $4,533,833 | $1,291,524 |
| **annualized (30d)** | **$25,810,902** | **$4,911,367** | **$3,134,462** | **$1,776,881** |
| annualized (90d) | $24,116,820 | $4,180,179 | $2,572,303 | $1,607,841 |

**Monthly revenue series — the growth story** `[V]`:
| Month | Fees | Revenue | Protocol Rev | Holders Rev |
|---|---|---|---|---|
| 2025-09 | $6,310,128 | $604,899 | $604,899 | $0 |
| 2025-10 | $6,334,554 | **$1,209,780** | $1,209,780 | $0 |
| 2025-11 (TGE) | $3,707,587 | $635,682 | $635,682 | $0 |
| 2025-12 | $1,743,586 | $259,716 | $259,716 | $0 |
| 2026-01 | $1,427,471 | **$94,002** (trough) | $94,002 | $0 |
| 2026-02 | $1,511,918 | $112,997 | $112,997 | $0 |
| 2026-03 | $1,828,938 | $152,360 | $152,360 | $0 |
| **2026-04** (fee switch 04-09) | $1,630,559 | $199,782 | $344,964 | $608,277 ← anomalous, see Gaps |
| 2026-05 | $1,902,181 | $273,426 | $149,179 | $124,244 |
| 2026-06 | $2,109,408 | $310,171 | $169,798 | $140,376 |
| 2026-07 | $1,907,980 | $291,965 | $166,022 | $125,939 |
| 2026-08 | $2,029,916 | $346,255 | $214,846 | $131,399 |
| **2026-09** | $2,117,079 | **$410,597** | $264,618 | $145,979 |
| 2026-10 (3 days) | $230,301 | $30,818 | $15,509 | $15,310 |

→ Revenue **Apr→Sep 2026: +105.5%**; last three months Jul→Sep: +40.6%. Gross Fees are flat (~$1.9–2.1M/mo) — **all the revenue growth is take-rate and mix, none of it is volume.** `[V]`

**Revenue by product, 2026-10-03** `[V]` (per-child-protocol DefiLlama summaries):
| Product | Fees 30d | Revenue 30d | Revenue 1y | Rev. share of 30d | Live since |
|---|---|---|---|---|---|
| Kinetiq kHYPE | $1,875,637 | $187,567 | $2,524,802 | 46% | 2025-07-18 |
| Kinetiq Markets Perps (builder codes) | $157,774 | **$157,774** | $484,905 | 39% | 2025-12-17 |
| Kinetiq KNTQ (spot deployer fees) | $19,598 | $19,598 | $126,586 | 4.8% | 2025-11-29 |
| Kinetiq Validators (invoiced commission) | $38,205 | $19,100 | $101,928 | 4.7% | 2026-04-09 |
| Kinetiq Markets (HIP-3 deployer cut) | $83,852 | $12,169 | $96,678 | 3.0% | 2026-01-12 |
| Kinetiq Earn (vkHYPE vault) | **−$68,963** | $11,575 | $902,745 | 2.8% | 2025-07-24 |
| Kinetiq Launch | $8,672 | $865 | $2,328 | 0.2% | 2026-06-15 |

- **Kinetiq Earn is losing money for depositors**: gross vault "Fees" (= yield) were **−$68,963 over 30d and −$9,232 over 7d** — the vkHYPE strategy vault produced *negative* yield in Sept 2026, down from $4.39M of yield over the trailing year. `[V]`
- Launch has essentially no traction: $865 of revenue in 30 days, $2,328 in its life. `[V]`

**Markets by Kinetiq ("Markets.xyz") — HIP-3 traction, read on-chain 2026-10-03** `[V]` ([Hyperliquid info API, `perpDexs` + `meta` per dex](https://api.hyperliquid.xyz/info)):
- Two HIP-3 dexes share deployer `0x71f0019cc7fa79e4f42587fb7b9a817d8d2429ec` and fee recipient `0xbcd4071d023bf2aae484d724c130b5af6f0ca0d2`: **`km` "Markets by Kinetiq"** and **`mkts` "Markets By Kinetiq"** — the deployer address is also the kmHYPE `StakingManager` per the docs.
- **`km`: all 23 markets are `isDelisted: true`** — the original dex is fully wound down / migrated to `mkts`.
- **`mkts`: 24 markets, only 5 live** — `mkts:US500`, `mkts:USBOND`, `mkts:SMALL2000`, `mkts:USTECH`, `mkts:BVIV`. 19 delisted (BABA, EUR, TSLA, GOLD, SILVER, AAPL, GOOGL, NVDA, PLTR, JPN225, XIAOMI, RTX, MU, TENCENT, SEMI, GLDMINE, USOIL, USENERGY).
- Live-market 24h notional volume: US500 $1.38M + USBOND $1.42M + USTECH $1.66M + BVIV $0.487M + SMALL2000 $0.163M = **≈$5.11M/day**. Open interest ≈ **$8.95M** (computed from contract OI × mark). `deployerFeeScale = 1.0` on all live markets. `[V]`
- Context: Kinetiq is one of 10 HIP-3 perp dexes on Hyperliquid (xyz, flx/Felix, vntl/Ventuals, hyna/HyENA, km, abcd, cash/dreamcash, para/Paragon, mkts, io/EntropyIO). `[V]`

**Elysium — NOT LIVE as of 2026-10-03** `[V]`:
- I fetched `https://elysium.kinetiq.xyz` directly on 2026-10-03 ~23:18 UTC. The page renders as **"Elysium testnet explorer"** with a **"Testnet"** badge, live blocks and HYPE-denominated test transactions. **Elysium contributes $0 revenue today.** `[V]`
- Public testnet began **2026-09-22**; mainnet is scheduled for **2026-10-20** (4 weeks later) `[R]` — [TradingView/CoinMarketCal](https://www.tradingview.com/news/coinmarketcal:ab9da4724094b:0-kinetiq-elysium-mainnet-launch-brings-its-hyperliquid-l2-live-by-20-oct-2026/); [KuCoin flash](https://www.kucoin.com/news/flash/kinetiq-launches-elysium-l2-to-boost-hype-ecosystem).
- Fee split `[R]`: **50% of sequencer revenue → buy-and-burn KNTQ via the Assistance Fund; 25% → app developers using Elysium blockspace; 25% → Kinetiq treasury** — [crypto.news](https://crypto.news/kinetiq-unveils-elysium-l2-with-hype-gas/); the 50%-to-KNTQ figure is **confirmed by the primary source** (Kinetiq docs, [kinetiq.xyz/docs/kntq](https://kinetiq.xyz/docs/kntq): "Elysium: 50% of sequencer revenue programmatically buys KNTQ on the open market") `[V]`.
- **Conflicting technical descriptions**: "built on the OP Stack to settle on HyperEVM" vs "an Arbitrum Orbit chain... targeting 300 million gas per second with blocks every 100–200 ms" — [chainstack.com/what-is-elysium](https://chainstack.com/what-is-elysium/) and [crypto.news](https://crypto.news/kinetiq-unveils-elysium-l2-with-hype-gas/) disagree. Both secondary. HYPE is the gas token in all accounts.
- Elysium strategy was announced **2026-07-27** `[R]` — [CoinMarketCap AI timeline](https://coinmarketcap.com/cmc-ai/kinetiq/latest-updates/).

**Other dated 2026 product events** `[R]` — [CoinMarketCap AI timeline](https://coinmarketcap.com/cmc-ai/kinetiq/latest-updates/):
- **2026-06-11**: Launch goes live — "$KNTQ stakers can now back perpetual market deployers to earn a permanent share of their trading fees."
- **2026-06-30**: "Kinetiq has bought back about $322K of $KNTQ to date... funded entirely by protocol revenue."
- **2026-09-24**: partnership with DoubleZero Edge to bring Hyperliquid order-book data to institutional desks.
- "HIP-4 Protocol Development coming soon... to enable novel markets like sportsbooks and esports betting" — forward-looking, unshipped.

### Inferences
- Take rate on staking rewards is **10%**, of which Kinetiq keeps 30% (3% of gross rewards) for the treasury and spends 70% (7% of gross rewards) on buybacks. Revenue/Fees = 403,674/2,121,444 = **19.0%** blended — above 10% because Markets Perps builder-code fees and KNTQ spot deployer fees are 100%-margin revenue.
- **Revenue growth is mix-shift, and it is running out of room.** The fee switch (Apr 2026) was a one-time step from ~0% to 10%; the second-largest line (Markets Perps builder codes, 39% of revenue) runs on ~$5M/day of HIP-3 volume with only 5 live markets and 19 delisted. There is no evident volume engine behind the revenue curve.
- At $5.11M/day volume and $157.8k/30d builder-code fees, implied builder take ≈ 10bp of notional. If `mkts` volume stalls, 39% of revenue stops growing.
- Elysium is the entire forward-looking value-accrual case, and on 2026-10-03 it had **zero** mainnet revenue, 17 days before its scheduled launch. Treat any "Elysium adds X to buybacks" estimate as unbacked.

### Gaps
- **The April 2026 HoldersRevenue figure ($608,277) is anomalous** — ~4.5x every subsequent month, and larger than April's total Revenue ($199,782). This is almost certainly an adapter backfill/catch-up at the 2026-04-09 switchover, not a real month of buybacks. I could not reconcile it. Exclude April from any buyback-rate estimate.
- No primary Kinetiq revenue dashboard was reachable: `api.kinetiq.xyz/v1/*` returns **401 "API key required"** `[V]`, and `kinetiq.xyz/kntq` is client-rendered so its live Buybacks/Burned/Staked panels came back empty to a raw fetch `[V]`.
- "Kinetiq Ascend" / @AscendLaunch: I could not establish from any primary source whether this is a Kinetiq product, a Kinetiq Launch partner, or an independent protocol. Its buyback reallocation (see Q4) does **not** appear in DefiLlama's Kinetiq adapter, which suggests it is *not* Kinetiq protocol revenue. Treat Ascend buybacks as separate from the $1.78M/yr figure.
- `kinetiq.xyz/blog` and the governance forum / KIP archive were unreachable from this sandbox (TLS connection reset on repeated attempts). KIP texts below are therefore secondary.

---

## Q3. Valuation multiples vs peers

### Takeaway
On market cap against *Kinetiq's own* revenue, KNTQ at ~17x is defensible and cheaper than Jito (40x) or Hyperliquid (29x). On **FDV** (62x revenue) and on **holders revenue** (48x mcap / 171x FDV) it is expensive, and on mcap/TVL it is ~5x Lido and ~2.5x Rocket Pool. The whole case rests on whether you use mcap or FDV — and with a 31%-of-supply insider cliff 55 days out (Q5), FDV is the honest denominator.

### Cited Findings

**KNTQ multiples, 2026-10-03** `[V]` (computed from the verified numbers above):
| Metric | On mcap ($85.08M) | On FDV ($303.33M) |
|---|---|---|
| / annualized Revenue ($4.91M) | **17.3x** | **61.8x** |
| / annualized Revenue (90d, $4.18M) | 20.4x | 72.6x |
| / annualized Holders Revenue ($1.78M) | **47.9x** | 170.7x |
| / annualized Protocol Revenue ($3.13M) | 27.1x | 96.8x |
| / annualized gross Fees ($25.81M) | 3.30x | 11.75x |
| / TVL ($1.074B Kinetiq LSTs) | **0.0792** | 0.2824 |

CoinGecko's own computed ratios agree: `mcap_to_tvl_ratio` 0.07, `fdv_to_tvl_ratio` 0.26 `[V]` ([CoinGecko](https://api.coingecko.com/api/v3/coins/kinetiq)).

**Peer table, 2026-10-03** `[V]` (mcap from [CoinGecko simple/price](https://api.coingecko.com/api/v3/simple/price?ids=lido-dao,jito-governance-token,rocket-pool,ether-fi,hyperliquid,marinade&vs_currencies=usd&include_market_cap=true); TVL + 30d fees/revenue annualized from DefiLlama per-protocol summaries):
| Protocol | mcap | TVL | ann. Fees | ann. Revenue | mcap/Rev | mcap/TVL |
|---|---|---|---|---|---|---|
| Lido (LDO) | $387,426,047 | $26,449,496,605 | $625,486,460 | $38,789,085 | **10.0x** | **0.0146** |
| ether.fi (ETHFI) | $703,455,436 | $5,167,225,123 | $159,992,981 | $46,502,132 | 15.1x | 0.1361 |
| **Kinetiq (KNTQ)** | **$85,075,857** | **$1,074,058,539** | **$25,810,902** | **$4,911,367** | **17.3x** | **0.0792** |
| Hyperliquid (HYPE) | $19,877,264,719 | — | $885,274,200 | $685,767,962 | 29.0x | — |
| Jito (JTO) | $299,129,089 | $1,243,108,006 | $124,831,910 | $7,507,989 | 39.8x | 0.2406 |
| Rocket Pool (RPL) | $44,318,812 | $1,395,590,066 | $35,108,571 | $0 | n/a | 0.0318 |
| Marinade (MNDE) | $13,342,823 | $273,123,682 | — | — | n/a | 0.0489 |

Lido's annualized holders revenue is $27.3M → LDO at **14.2x** holders revenue, vs **KNTQ at 47.9x**. `[V]`

**Hyperliquid LST competitors' economics for reference** `[V]`: stHYPE ann. fees $5.02M / revenue $502k (10% take rate, no token); Hyperbeat ann. fees $2.27M / revenue $447k.

**Other Hyperliquid-ecosystem tokens with mcap on DefiLlama, 2026-10-03** `[V]`: Gate GT $1.168B, Backpack BP $321.0M, SwissBorg BORG $171.6M, Hyperlane HYPER $24.0M, Equilibria EQB $13.1M, LoopedHype LHYPE $8.21M, TermMax TMX $1.83M, Wrapped HLP wHLP $1.40M. **KNTQ at $85.1M mcap is the largest pure HyperEVM-native DeFi token in that set** (the larger entries are CEX tokens and cross-chain infra, not Hyperliquid-native).

### Inferences
- The gap between mcap/Rev (17x) and FDV/Rev (62x) is the entire debate. With 72% of supply non-circulating and the insider cliff 55 days away, a buyer at $0.30 is paying ~62x revenue for the fully-diluted claim.
- Revenue would need to roughly **3.6x to ~$17.5M/yr** for FDV/Rev to reach Lido's 10x at today's price — i.e., the market is pricing in Elysium working *and* the LST base stabilizing.
- mcap/TVL of 0.079 is 5.4x Lido's 0.0146. Lido is a fair comparison on business model (ETH LST, fee switch, governance token) and *cheaper on every revenue multiple too*, which is a hard problem for the KNTQ bull case. The Jito comparison (39.8x) is the only peer that makes KNTQ look cheap, and Jito's mcap/TVL is 3x KNTQ's.
- "mcap/Fees = 3.3x" is the number bulls will quote. It is misleading: gross "Fees" here is ~90% pass-through staking yield owned by kHYPE holders, not Kinetiq.

### Gaps
- Token Terminal and Messari were not consulted (not reachable / not needed given DefiLlama's per-product adapter detail was richer).
- No peer has a directly comparable "LST governance token on a perp DEX L1" profile; Jito is the nearest (Solana LST + MEV/block-engine + perp-adjacent revenue) and trades at 2.3x KNTQ's revenue multiple, so the comp is a genuine valuation argument in both directions.

---

## Q4. Value accrual: buybacks, burns, sKNTQ, treasury, governance

### Takeaway
Buybacks are real but small — **~$1.78M/yr annualized, ~$4.4–6.0k/day** — and since **KIP-5 (~2026-09-15) they no longer pay sKNTQ holders anything**: 100% is routed to the Hyperliquid Assistance Fund as a supply sink. The protocol's own live docs (updated 2026-09-16) and its own KNTQ product page contradict each other on this. Cumulative supply removed to date: **3,988,286 KNTQ = 0.40% of supply.**

### Cited Findings

**Current mechanics — primary source, Kinetiq docs "Last updated September 16, 2026"** `[V]` — [kinetiq.xyz/docs/kntq](https://kinetiq.xyz/docs/kntq), quoted verbatim:
> "Kinetiq routes revenue from every product into KNTQ buybacks. Purchased tokens, along with any fees already paid in KNTQ, are sent to the Hyperliquid Assistance Fund, permanently removing them from supply.
> - Protocol revenue (KIP-2): 70% is used for buybacks. The remaining 30% funds treasury operations.
> - Validator commissions (KIP-2): 100% of Kinetiq's share is used for buybacks. Active-set validators share 50% of the commission they charge on protocol stake, in perpetuity, as a condition of opting in.
> - KNTQ trading fees: 100% is sent directly to the Assistance Fund.
> - Markets.xyz: 100% of Kinetiq's disposable Markets income (minimum 10% of deployer share plus builder code revenue) is used for buybacks.
> - Launch: 100% of Kinetiq's share of Launch revenue (10% of deployer share) is used for buybacks.
> - Elysium: 50% of sequencer revenue programmatically buys KNTQ on the open market."

**sKNTQ — governance only, per the same primary source** `[V]`:
> "KNTQ can be staked for sKNTQ, which is used for governance. Unstaking sKNTQ features a 7-day withdrawal period."

sKNTQ tiers (utility, not yield) `[V]`: Markets referral share 6% @ 50,000 sKNTQ → 7% @ 100k → 8% @ 500k → 10% @ 1.25M → 15% @ 2.5M. kmHYPE minting allocation: up to 1,111 @ 50k sKNTQ → 11,111 @ 100k → 111,111 @ 500k → 222,222 @ 1.25M → uncapped @ 2.5M.

**Three documented contradictions on where buyback value goes** — flag these prominently:
1. Docs (2026-09-16) `[V]`: buybacks → Assistance Fund, "permanently removing them from supply"; sKNTQ is "used for governance" with **no fee share stated**.
2. Kinetiq's own live KNTQ product page FAQ, fetched 2026-10-03 `[V]` ([kinetiq.xyz/kntq](https://kinetiq.xyz/kntq)): "All acquired KNTQ from these mechanisms is **distributed to stakers**" and "Kinetiq generates revenue... and **distributes returns to sKNTQ holders**." This is a **stale pre-KIP-5 page that contradicts the docs**.
3. DefiLlama's adapter methodology `[V]` ([api.llama.fi/summary/fees/kinetiq](https://api.llama.fi/summary/fees/kinetiq)) describes validator commissions as "70% of the invoiced amount, used to buy back KNTQ **for sKNTQ holders**" and 30% to treasury — vs docs' "100% of Kinetiq's share is used for buybacks." DefiLlama's split is what the *numbers* follow (Validators 30d: revenue $19,100 = $5,731 proto + $13,371 holders, exactly 30/70) `[V]`.

**KIP-5, ~2026-09-15** `[R]`: redirected **100% of KNTQ buybacks to the Hyperliquid Assistance Fund**; at announcement **5.39M KNTQ had been bought with protocol revenue at an average ~$0.15** (~0.53% of total supply, ~2.15% of circulating) — [@VikingoDigital_ on X](https://x.com/VikingoDigital_/status/2099908097401602439), echoed by [cryptobriefing](https://cryptobriefing.com/kinetiq-ends-kpoints-kntq-price-drop/) ("more than 5.39 million KNTQ at an average price of $0.15").
**KIP-2** `[R]`: established the 70/30 buyback/treasury split and 100% of validator-commission share to buybacks — [CoinMarketCap AI](https://coinmarketcap.com/cmc-ai/kinetiq/what-is/).

**Supply actually removed — verified on-chain** `[V]`:
- Hyperliquid Assistance Fund `0xfefefefefefefefefefefefefefefefefefefefe` holds **3,988,286.19 KNTQ = 0.399% of supply** ([api.hypurrscan.io/holders/KNTQ](https://api.hypurrscan.io/holders/KNTQ), `lastUpdate` 1791069081 = 2026-10-03T23:11Z).
- sKNTQ staking contract `0x696238e0Ca31c94e24ca4CBe7921754E172E4d0F` holds **75,829,511.38 KNTQ** = 7.58% of total supply and **27.0% of the 280.48M circulating** (eth_call `balanceOf` on `0x000000000000780555bd0bca3791f89f9542c2d6`, HyperEVM, 2026-10-03 ~23:20 UTC).
- Buyback bot `0xaa3b7392052d62928cc87701e3ca6fb6630bb6e2` holds **0 KNTQ** on HyperEVM (pass-through, no accumulation).
- KNTQ ERC-20 `totalSupply()` = **1,000,000,000.000000** exactly, 18 decimals — **no on-chain burns have reduced supply; "burn" means transfer to the Assistance Fund, not `_burn()`.**

**Observed buyback run-rate** `[V]`: daily Holders Revenue, 2026-09-24 → 2026-10-03: $4,872 / $4,697 / $5,601 / $4,617 / $4,597 / $962 / $8,702 / $4,885 / $4,422 / $6,003. → **$4.4–6.0k/day typical, ≈$150k/month, ≈$1.78M/yr**, consistent with the reported $3–8k/day bot. Note **no step-up after 2026-09-30** (the Ascend reallocation date), reinforcing that Ascend flows are outside Kinetiq's adapter.

**Reconciliation problem on cumulative buybacks** — flag: DefiLlama's all-time Holders Revenue is **$1,291,524** (all of it post-2026-04-09) `[V]`. Against the reported 5.39M KNTQ at ~$0.15 (= ~$808k) `[R]`, and the 3.99M KNTQ now in the Assistance Fund `[V]`, the three figures do not reconcile cleanly. Most likely causes: the anomalous $608k April adapter entry, and ~1.4M KNTQ distributed to sKNTQ stakers pre-KIP-5 rather than sent to the Assistance Fund. The 2026-06-30 Kinetiq statement of "$322K bought back to date" `[R]` is also inconsistent with the adapter's ~$1.07M cumulative by that date. **Do not present a single cumulative-buyback number as fact.**

**Ascend buyback reallocation, 2026-09-30** `[R]` — [TradingView/CoinMarketCal](https://www.tradingview.com/news/coinmarketcal:0115aaccb094b:0-kinetiq-ascend-buyback-allocation-shifts-to-50-hype-50-kntq-30-sep-2026/): split moved **from 90% HYPE / 10% KNTQ to 50% / 50%**; of the KNTQ bought, **60% burned, 20% to kHYPE/KNTQ liquidity, 20% to the Ascend points program**. The 50/50, 60/20/20 terms are confirmed by two independent secondary sources but **I found no primary Kinetiq source** and no corresponding step-up in on-chain/adapter buyback flow. KNTQ rose ~28% in 24h and printed its $0.45 ATH around this announcement `[R]` ([KuCoin](https://www.kucoin.com/news/insight/HYPE/6abf1f5d38a2640007922a32)).

**Treasury** `[V]`: DefiLlama's treasury tracker for Kinetiq reports only **$18,631 total / $4,954 own-tokens** on 2026-10-03 ([api.llama.fi/treasury/kinetiq](https://api.llama.fi/treasury/kinetiq)) — this is clearly tracking a near-empty address and **must not be used as the treasury figure.** No reliable treasury/runway number was obtainable.

**Audits — 8 reports, primary source** `[V]` ([kinetiq.xyz/docs/contracts-and-audits](https://kinetiq.xyz/docs/contracts-and-audits), page "Last updated April 28, 2026"): 2026-01-15 Spearbit (sKNTQ); 2025-11-27 Spearbit (kmHYPE); 2025-11-24 Zenith (kmHYPE); 2025-11-23 Pashov (kHYPE instant unstake); 2025-06-24 Spearbit (kHYPE LST); 2025-04-16 Code4rena (kHYPE LST); 2025-03-17 Zenith; 2025-03-06 Pashov. All at `audits.kinetiq.xyz`. Live bug bounty on Cantina: `https://cantina.xyz/bounties/a98129d7-dd15-4c16-b2cb-d8cc42f87de4`. **Note: no audit published since 2026-01-15 — Elysium (mainnet in 17 days) has no listed audit.**

### Inferences
- **Buybacks are economically irrelevant at current scale.** $1.78M/yr against an $85M mcap is a 2.1% annual "yield" on circulating, and 0.59% on FDV. Against the insider vesting stream starting in November (Q5), it offsets roughly **3.8% of monthly unlock value**.
- **KIP-5 removed the only direct cash-flow right a KNTQ holder had.** Post-KIP-5, KNTQ is a pure supply-sink/governance token: holders benefit only via reduced dilution, not distribution. The fact that Kinetiq's own front page still advertises the old model is a disclosure problem and a reason to distrust marketing-sourced "real yield" claims.
- Routing buybacks to Hyperliquid's Assistance Fund is a political/alignment choice that transfers optionality to the Hyperliquid ecosystem rather than to KNTQ stakers. It is good for HYPE-ecosystem standing and neutral-to-negative for a KNTQ cash-flow valuation.
- 27% of circulating supply sitting in sKNTQ with a 7-day unstaking queue is meaningful float suppression *and* a latent overhang: those holders are earning tier benefits, not yield, so their stickiness is weaker than a yield-bearing stake would be.

### Gaps
- Governance: I could not reach the KIP forum/archive (TLS resets on `kinetiq.xyz/blog`), so I cannot list the KIP pipeline, vote turnout, quorum, or whether KIP-5 was actually voted on versus team-implemented. KIP-1, KIP-3, KIP-4 contents are unknown to me; KIP-6+ could not be confirmed to exist. Only KIP-2 and KIP-5 are documented, both via secondary sources plus the docs' KIP-2 citation.
- No audit of Elysium, sKNTQ post-Jan-2026, or the S2 claim contract was found. Absence of a published audit is not proof one doesn't exist.
- Treasury size, stablecoin holdings and runway: **unknown and unobtainable** from public sources this session.

---

## Q5. Token supply, distribution and the unlock schedule

### Takeaway
The allocation reconciles exactly with the on-chain genesis split. **The dominant fact is a 310M-token (31% of supply) insider cliff at ~2026-11-27 — 55 days from the $0.26 Season 2 claim price.** On the docs' literal wording that releases ~12.9M KNTQ/month (~4.6% of current circulating, ~$3.9M/month at $0.30) for 24 months starting late November 2026. Sources also disagree on circulating supply by 55M tokens (280M vs 335M).

### Cited Findings

**Allocation — reconciles exactly to on-chain genesis** `[R]` for the table, `[V]` for the reconciliation — [blocmates, Kinetiq Foundation announcement](https://www.blocmates.com/news-posts/kinetiq-foundation-announces-kntq-token-launch-allocating-24-to-kpoints-holders):
| Bucket | % | Tokens | Genesis location |
|---|---|---|---|
| Initial airdrop — kPoints holders | 24.0% | 240,000,000 | distributed at TGE |
| Initial airdrop — Hypurr holders | 1.0% | 10,000,000 | distributed at TGE |
| Protocol growth & rewards | 30.0% | 300,000,000 | deployer |
| Core contributors | 23.5% | 235,000,000 | deployer, vesting |
| Foundation | 10.0% | 100,000,000 | deployer |
| Investors | 7.5% | 75,000,000 | deployer, vesting |
| Liquidity | 4.0% | 40,000,000 | ~20M at TGE / ~20M deployer |
| **Total** | **100%** | **1,000,000,000** | |

→ **Reconciliation check** `[V]` (inference from verified genesis split): deployer's 730M = 300M growth + 235M contributors + 100M foundation + 75M investors + 20M liquidity = **730M exactly**; the 270M to 9,999 addresses = 240M kPoints + 10M Hypurr + 20M liquidity = **270M exactly**. The allocation table is therefore internally consistent with the on-chain genesis and can be treated as reliable.

**Vesting — primary source, verbatim** `[V]` — [kinetiq.xyz/docs/kntq](https://kinetiq.xyz/docs/kntq):
> "All core contributors and investors share the same vesting schedule: **Total duration: 3 years. Cliff: 1 year. Vesting: 2-year monthly linear vesting following the cliff.**"

Genesis/TGE = **2025-11-27** `[V]` (same page) → **cliff date ≈ 2026-11-27**, i.e. **55 days after 2026-10-03**.

**Two readings of the cliff — present both** `[V]` (arithmetic on verified inputs; 310M = 235M + 75M):
| Reading | At cliff (2026-11-27) | Monthly thereafter | First-year total | Monthly as % of 280.5M circ |
|---|---|---|---|---|
| **Docs-literal** (nothing in yr 1; 310M over 24 monthly tranches) | 0 (or first tranche) | **12.92M (~$3.92M @ $0.30)** | **155.0M (~$47.0M)** | **4.61%** |
| Alternative (1/3 at cliff, 2/3 over 24mo) | 103.33M (~$31.3M) | 8.61M (~$2.61M) | 103.3M (~$31.3M) | 3.07% |

The docs' phrase "2-year monthly linear vesting **following** the cliff" with "total duration: 3 years" supports the **docs-literal** reading. Either way: **buybacks at $1.78M/yr offset only 3.8% (docs-literal) to 5.7% (alternative) of the dollar value of monthly insider unlocks.** `[V]`

**Nothing material unlocks on a published schedule in Oct–Dec 2026 except the Nov-27 cliff** `[V]` (inference from the single published schedule): the only scheduled, contractual unlock in the next 6 months is the contributor/investor cliff at ~2026-11-27 and monthly tranches thereafter (~2026-12-27, ~2027-01-27, ~2027-02-27, ~2027-03-27 at ~12.92M each on the docs-literal reading).

**The 300M "protocol growth & rewards", 100M foundation and ~20M residual liquidity have NO published vesting schedule** `[V]` (absence confirmed on the docs page, which details only contributor/investor vesting) — they are **discretionary, releasable at will**. The Season 2 sale (50M = 5% of supply, $0.2613, window 2026-10-01 12:00 → 2026-10-11 12:00 UTC, unclaimed reverts to the Kinetiq Foundation) `[R]` is the first visible drawdown from these buckets; which bucket it came from is not stated anywhere I could find.

**Where the non-circulating ~720M actually sits — on-chain, 2026-10-03** `[V]`:
| Location | KNTQ | % supply |
|---|---|---|
| HyperCore system escrow `0x200000000000000000000000000000000000007c` (= the HyperEVM-side balance of spot token index 124) | **857,384,167.90** | 85.74% |
| …of which: sKNTQ staking `0x696238e0Ca31c94e24ca4CBe7921754E172E4d0F` | 75,829,511.38 | 7.58% |
| …of which: Season 2 claim contract `0x435bb7ea4eb481cb686606d089ea4dee4c6cc03b` | 27,953,424.46 | 2.80% |
| …remaining on HyperEVM, holders not identifiable (see Gaps) | ~753,601,232 | ~75.4% |
| HyperCore spot, 11,795 other addresses | ~142,615,811 | 14.26% |
| …of which: Hyperliquid Assistance Fund `0xfefe…fe` | 3,988,286.19 | 0.399% |
| **Total on HyperCore (all addresses)** | **999,999,979** | 100% |

- **The genesis deployer `0x51172933b60847085e2a959e860e2ec9e240ac09` now holds 0 KNTQ on HyperEVM** `[V]` — the 730M has been moved to other HyperEVM addresses.
- Largest *unlabelled* HyperCore holders `[V]`: `0xaf0fdd39e5d92499b0ed9f68693da99c0ec1e92e` 18,673,243 (1.87%), `0xa9b95f2a2e7ef219021efc5c04c32761b8553bbd` 11,004,428 (1.10%), `0x77375a8c9d13bf79afb2a87f1b0ac1dfd5f5bf66` 3,229,207, `0xbf66cb8b987fee1f6526bb6ee04345d36405f913` 2,850,744, `0xfeb63b9e4a871b644816d94a1d19517a87ce5fa0` 2,799,772. None hold any KNTQ on HyperEVM `[V]`, so these are HyperCore-native positions (plausibly market makers / exchange wallets). Flows are a teammate's scope.
- Season 2 claim contract at 27,953,424 of 50,000,000 implies **~22.0M (≈44%) claimed** in the first ~2.4 days of the 10-day window `[V]` — a single data point; teammates own this series.

**Circulating supply: sources conflict by 55M tokens** — flag:
- CoinGecko: **280,476,290** circulating, mcap $85.08M `[V]` ([CoinGecko](https://api.coingecko.com/api/v3/coins/kinetiq), 2026-10-03T23:12Z)
- DropsTab: **335.48M** circulating (33.55%), mcap **$101.75M**, same FDV $303.30M `[V]` (fetched 2026-10-03, [dropstab.com/coins/kinetiq](https://dropstab.com/coins/kinetiq/vesting))
- cryptobriefing: "circulating supply ranges between **280–335 million** tokens" `[R]` — [cryptobriefing](https://cryptobriefing.com/kinetiq-ends-kpoints-kntq-price-drop/)
- DefiLlama parent protocol mcap: $85,915,010 `[V]` (consistent with CoinGecko)

→ The 55M delta ≈ the 50M Season 2 allocation plus liquidity. **Effective float is somewhere in 280–336M; mcap is therefore $85–102M depending on treatment.** Multiples in Q3 use the conservative (CoinGecko) basis; on the DropsTab basis mcap/Revenue = 20.7x.

**KNTQ token identifiers, re-verified** `[V]` ([Hyperliquid info API `spotMeta`](https://api.hyperliquid.xyz/info)): `name KNTQ`, `fullName Kinetiq`, `index 124`, `tokenId 0xbd31bd605c0a1b82c72aae3587f9061f`, `szDecimals 2`, `weiDecimals 8`, `isCanonical false`, `evmContract 0x000000000000780555bd0bca3791f89f9542c2d6` with `evm_extra_wei_decimals 10` (→ 18 ERC-20 decimals, confirmed by `decimals()` = 18 `[V]`), `deployerTradingFeeShare 1.0`. Spot mid `@334` = $0.302765 `[V]`.

### Inferences
- **This is the central risk to buying at $0.26–0.30.** A new buyer at the S2 price is 55 days ahead of the start of a 24-month insider distribution worth ~$3.9M/month at today's price, from holders whose cost basis is ~$0.0175–0.0233 (Q6) — i.e. a 13–17x gain, with no lockup after vest. Buybacks absorb <4% of it.
- The 400M of discretionary foundation + growth tokens is arguably a *larger* risk than the contractual 310M, because its release is unscheduled and unannounced. The S2 sale is the template: 5% of supply monetized at $0.26 with no lockup, ~$13.07M of potential proceeds, announced 1 day before the window opened.
- Supply-sink progress to date (3.99M = 0.40%) is ~1/32nd of a single year's docs-literal insider vest. On current mechanics, **net supply grows for at least the next two years regardless of buyback performance.**
- Because S2 tokens have no lockup and S1 recipients are already liquid, the airdrop buckets are fully reflected in float; the overhang is purely insider + foundation.

### Gaps
- **I could not enumerate HyperEVM KNTQ holders**, so I cannot name the vesting/treasury contracts holding the ~753.6M. Every holder API I tried failed: `hyperevmscan.io` (Cloudflare 403 per the brief), `www.hyperscan.com/api/v2` (301 → Cloudflare), `hyperscan.com`/`explorer.hyperliquid.xyz` (redirect to hl.eco), `api.hl.eco/api/v2/tokens/.../holders` (404), `api.hypurrscan.io/evmHolders|tokenHolders` (404), `api.routescan.io/.../999/...` ("chain not supported" / "NO_BLOCKCHAINS_FOR_PARAMS"), `999.routescan.io` (403). Enumerating them would require `eth_getLogs` over ~26M blocks at 10k/range — not feasible in budget. **This is the single biggest open item: whether the 310M is in a verifiable on-chain vesting contract or a multisig the team can move at will is unknown.**
- No dated unlock *calendar* from Tokenomist / TokenUnlocks / CryptoRank was obtainable (cryptorank.io returns 403; dropstab's vesting tab served no schedule). The Nov-27 cliff date is my inference from TGE + the docs' "1 year", not a tracker-published date.
- Which bucket funds the 50M Season 2 sale (growth 30% vs foundation 10%) is not disclosed in any source I found.
- Whether the Assistance Fund's 3.99M KNTQ is excluded from CoinGecko's circulating figure is not stated.

---

## Q6. Investors, rounds and cost basis

### Takeaway
One disclosed round only: a **$1.75M seed closed 2025-10-22 at ~$17.5M pre-money**, led by Maven 11. Implied cost basis is **$0.0175–0.0233/KNTQ**, i.e. insiders are up **13–17x** at $0.30 and **11–15x** against the Season 2 price of $0.2613. Their tokens begin unlocking ~2026-11-27.

### Cited Findings
- **Seed, 2025-10-22, $1.75M** `[V]` — [api.llama.fi/protocol/kinetiq](https://api.llama.fi/protocol/kinetiq) `raises` field, `date 1761091200` (= 2025-10-22), `round "Seed"`, `amount 1.75` ($M), `valuation: null`, `leadInvestors: []`, `otherInvestors: ["Maven 11","Pier Two","Chorus One Ventures","IMC Crypto","Infinite Field","Flowdesk","Susquehanna"]`. DefiLlama lists no `source` URL and no valuation.
- **Valuation ~$17.5M pre-money; Maven 11 lead; additional investors Alpen Capital (formerly Comfy Capital) and DeFi Dad** `[R]` — [CryptoRank /ico/kinetiq](https://cryptorank.io/ico/kinetiq) (page itself returned 403 to direct fetch; figures via search-result extraction, so **secondary and unconfirmed**).
- **Implied per-token cost** `[V]` (arithmetic on the above):
| Basis | $/KNTQ | Multiple at $0.3033 | vs S2 $0.2613 |
|---|---|---|---|
| $17.5M pre-money FDV ÷ 1B | **$0.0175** | **17.3x** | 14.9x |
| $1.75M for the full 7.5% investor bucket (75M) | **$0.0233** | **13.0x** | 11.2x |
| $1.75M = 9.09% of $19.25M post-money | $0.0193 | 15.8x | 13.6x |
- Three of the named seed investors are **operationally embedded**, not passive: **Flowdesk** (flowHYPE institutional LST deployment), **Chorus One** and **Infinite Field** both run Hyperliquid validators that appear in Kinetiq's own validator directory (`kinetiq.xyz/validators/falconx-chorus-one-14`, `kinetiq.xyz/validators/infinitefieldxyz-14`) `[V]` ([kinetiq.xyz/sitemap.xml](https://kinetiq.xyz/sitemap.xml), [contracts-and-audits](https://kinetiq.xyz/docs/contracts-and-audits)). **Pier Two** is also a professional staking operator.
- Stale aggregator figures to avoid: alphadrops/chainbroker show "FDV $129.64M, mcap $35.00M" `[R]` — these are historical, not current.

### Inferences
- $1.75M raised against a 23.5% team + 7.5% investor allocation means the cap table is overwhelmingly **team**, not VC: 235M contributor tokens (~$71M at $0.30) vs 75M investor tokens (~$23M). Team supply is 3.1x investor supply — team vesting, not VC vesting, is the dominant unlock.
- The investor roster's operational overlap (validators, Flowdesk LST) is a genuine distribution advantage and also a conflict-of-interest vector: seed investors who run validators sit on both sides of the "validators share 50% of commission with Kinetiq" arrangement.
- Note the sequencing: the seed closed **2025-10-22**, ~5 weeks before the 2025-11-27 TGE. This was effectively a pre-TGE round at ~1/17th of today's price, not an early-stage venture bet.

### Gaps
- No Series A or strategic round found; whether one exists undisclosed is unknown. PitchBook has two separate Kinetiq profiles (818779-60, 229525-93) that I could not access.
- No primary announcement (Kinetiq blog/X post) for the seed was reachable, so the $17.5M valuation and the Maven 11 "lead" designation rest entirely on CryptoRank, whose page I could not load directly. DefiLlama leaves `leadInvestors` empty and `valuation` null — **the two sources do not corroborate each other on the valuation.**
- Team/foundation entity: "Kinetiq Research" is the copyright holder on the site and "Kinetiq Foundation" issues the token `[V]`; no named founders were found in any source I reached.

---

## Q7. Execution and risk: promised vs shipped, audits, incidents

### Takeaway
Execution on *shipping* is good — Launch (Jun 2026), Markets/HIP-3 (Jan 2026), Earn, institutional LSTs, Elysium testnet (Sep 2026) all landed. Execution on *traction* is poor: most shipped products have near-zero revenue, 19 of 24 Markets products are delisted, and three of four institutional LSTs have ~zero supply. No exploit has occurred; there was one kHYPE depeg (Sept 2025, pre-TGE).

### Cited Findings

**Shipped, with dates** `[V]` where noted:
| Date | Item | Status today |
|---|---|---|
| 2025-07-18 | kHYPE live (DefiLlama fee data starts) `[V]` | Live, $1.02B, shrinking in HYPE terms |
| 2025-07-24 | Kinetiq Earn / vkHYPE vault `[V]` | Live; **negative 30d yield (−$68,963)** `[V]` |
| 2025-11-27 | KNTQ TGE; kmHYPE audited & launched `[V]` | Live |
| 2026-01-12 | Kinetiq Markets HIP-3 (`km`) `[V]` | **All 23 `km` markets delisted**; migrated to `mkts`, 5 of 24 live `[V]` |
| 2026-04-09 | Fee switch: 10% performance fee; Validators revenue line begins `[V]` | Live; doubled revenue |
| 2026-06-11 | Launch by Kinetiq `[R]` | Live; **$865 revenue in 30d** `[V]`; 3 of 4 partner LSTs ~zero supply `[V]` |
| 2026-07-27 | Elysium L2 announced `[R]` | Testnet only |
| 2026-09-15 | KIP-5 `[R]` | Live |
| 2026-09-22 | Elysium public testnet `[R]` | **Still testnet on 2026-10-03** `[V]` |
| 2026-09-24 | DoubleZero Edge data partnership `[R]` | Announced |
| 2026-09-30 | Ascend buyback 50/50 reallocation `[R]` | No adapter/on-chain confirmation `[V]` |
| 2026-10-01 | kPoints program ends; S2 paid claim opens `[R]` | Open until 2026-10-11 |
| **2026-10-20** | **Elysium mainnet (scheduled)** `[R]` | **Not shipped — 17 days out** |

**Promised but not shipped** `[R]` — [CoinMarketCap AI](https://coinmarketcap.com/cmc-ai/kinetiq/latest-updates/): Elysium mainnet (2026-10-20); "HIP-4 Protocol Development coming soon... to enable novel markets like sportsbooks and esports betting" — no date, no code.

**Incidents**
- **kHYPE depeg, 2025-09-24 to 2025-09-27**: kHYPE fell to **0.8802** vs peg (−11.98%); peg restored within days. Attributed to liquidity fragmentation during a Hyperliquid NFT drop, **not protocol failure**; kHYPE/USDT DEX volume +25% to >$500k on 2025-09-26 18:00 UTC `[R]` — [blockchain.news](https://blockchain.news/flashnews/khype-depeg-alert-kinetiq-staked-hype-dropped-to-0-8802-sept-24-27-before-peg-restored-trading-risks-and-liquidity-signals). This predates TGE.
- **No hacks on record** `[V]`: DefiLlama's `hacks` array for Kinetiq is **empty** ([api.llama.fi/protocol/kinetiq](https://api.llama.fi/protocol/kinetiq)). I found no exploit, slashing event, or validator failure in any source.
- **Governance friction, 2026-10-01**: ending the 46-week kPoints program (36.8M points distributed, 800k/week in later phases) and replacing a free airdrop with a **paid** $0.26 claim coincided with KNTQ giving back **>20% from its $0.448 ATH to ~$0.33** `[R]` — [cryptobriefing](https://cryptobriefing.com/kinetiq-ends-kpoints-kntq-price-drop/); [KuCoin](https://www.kucoin.com/news/flash/kinetiq-ends-kpoints-program-shifts-to-paid-token-allocation-as-kntq-drops-23) headlines it as "KNTQ Drops 23%". cryptobriefing reports no official team statement and no community reaction.

**Audit posture** `[V]`: 8 audits by 5 firms (Spearbit ×3, Pashov ×2, Zenith ×2, Code4rena ×1) plus a live Cantina bug bounty — strong for an LST. **But the most recent is 2026-01-15, and the contracts-and-audits page itself was last updated 2026-04-28**, so kmHYPE/`mkts` changes, the S2 claim contract, and Elysium are all unaudited as far as public disclosure shows. Code4rena's April 2025 contest repo is public: `https://github.com/code-423n4/2025-04-kinetiq`.

### Inferences
- Pattern: Kinetiq **ships fast and prunes fast**. 19 delisted HIP-3 markets and 3 dead institutional LSTs in under a year is either healthy iteration or product-market-fit failure depending on charity; either way it means **none of the post-kHYPE products has yet become a second revenue leg**, except builder-code fees (which are an interface business, not a product).
- The single largest execution risk in the next 30 days is Elysium: it carries the only large prospective value-accrual mechanism (50% of sequencer revenue), is scheduled to ship 2026-10-20, is still testnet, has no published audit, and has conflicting public descriptions of its own stack (OP Stack vs Arbitrum Orbit). A slip or a thin launch removes the main justification for a 62x FDV/revenue multiple.
- The kPoints→paid-claim switch is a tell on treasury intent: the foundation chose to **raise cash from its own community at $0.26** rather than distribute. That is a bearish signal on runway and a bearish signal on the foundation's own view of fair value — and $0.2613 is a credible ceiling-anchor, since the issuer itself was a willing seller there.
- Zero exploits across 15 months and ~$1–2.6B of TVL with 8 audits is a real, underrated positive. The depeg was a liquidity event, not a solvency event, and the current ~1.064 kHYPE NAV `[V]` shows the redemption mechanism is intact.

### Gaps
- Kinetiq's blog, governance forum and status page were all unreachable from this sandbox (`kinetiq.xyz/blog` → TLS `Recv failure: Connection reset by peer`; `elysium.kinetiq.xyz/docs` → `SSL_ERROR_SYSCALL`). I therefore have **no primary-source roadmap document** to score "promised vs shipped" against, only the CMC AI timeline (a secondary aggregator).
- No evidence either way on whether Elysium mainnet is on track for 2026-10-20.
- No information found on team size, hiring/attrition, or legal/regulatory matters.
- kHYPE's current secondary-market peg could not be verified: kHYPE does not trade on HyperCore spot (not in `allMids` `[V]`) and I did not query HyperEVM DEX pools. NAV (1.064) is verified; market price vs NAV is not.
