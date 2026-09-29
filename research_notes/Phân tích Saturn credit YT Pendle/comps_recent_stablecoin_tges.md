# Recent stablecoin / yield-dollar TGE comps (mid-2025 → Sep 2026, excl. Ethena, Usual, OpenEden, Falcon, Resolv) and market-implied valuation of Saturn $STRN

Research date: 2026-09-29.

**How the data was gathered**
- "API pull" means Claude queried a public API on 2026-09-29:
  - DefiLlama coins/protocol/stablecoins
  - CoinGecko coins
  - Gate.io spot candles
  - Polymarket gamma
  - Whales Market
  - Hyperliquid and Aevo
- These are primary data, but Claude chose the snapshot dates and did the arithmetic.
- Binance, OKX and Bybit APIs were blocked from this environment, so Binance launch klines could not be pulled:
  - Binance returned "restricted location".
  - OKX returned 403.
  - Bybit returned a CloudFront country block.

**Price and supply conventions**
- **FDV** = price × max/total supply (stated per row). **MC** = price × circulating supply at TGE, where known.
- **"Day-1 close"** is the first Gate.io UTC daily close. Gate's first-candle "open" is often a seed placeholder, e.g., XPL "opened" at $0.075, so it is not used.
- **"DL-first"** is the first DefiLlama daily price, usually the morning after listing.
- **d30/d90/now drawdowns** are measured against DL-first, so the basis is the same for every token.
- "(search-summary only)" marks facts seen only in a search-engine summary, without reading the underlying page.

---

## Q1. Master comparison table: which projects actually TGE'd, launch valuation, float, venues, FDV/TVL

### Takeaway
Between Jul 2025 and Jun 2026 there were 12 relevant stablecoin-sector TGEs:
- 8 yield-dollar/stablecoin issuers
- 2 stablecoin L1s
- 2 adjacent yield protocols

**No stablecoin-protocol TGE was found in Q3 2026 (Jul–Sep).** Avant slipped past its mid-Sep target, Apyx postponed, and infiniFi guides Q4.

For the 8 issuer comps most similar to Saturn:
- **Day-1 FDV:** $72M–$612M, median about $235M.
- **FDV/TVL at TGE:** 0.36x–2.15x, median about 1.3x.

### Cited Findings

**Master table.** Prices come from API pulls on 2026-09-29 unless noted. All figures are verified API data except where a cell is marked as search-sourced.

| # | Project (token) — type | TGE date | Supply used for FDV | Day-1 FDV (price) | Initial float / MC | TVL at TGE → FDV/TVL | Venues at launch | FDV d30 / d90 / now (2026-09-29) | Now vs DL-first |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Treehouse (TREE) — tETH/DOR fixed-income (not a stablecoin) | 2025-07-29 | 1B | $668M ($0.668 Gate close); ATH $1.36 intraday day 1 | 15.61% (156.1M) → MC ≈ $104M | $560M → 1.2x | Binance (HODLer #29), OKX, Coinbase | $314M / $188M / $45M | -93% |
| 2 | Reservoir (DAM) — rUSD/srUSD CDP stablecoin | 2025-08-18 | 1B | $89M (DL-first $0.089, 08-19); peak $149M on 2025-09-18 | n/a (277.5M circ now) | $54M (DefiLlama) → 1.65x. The project claimed about $250M TVL, which would be about 0.36x | Binance Alpha + Binance DAMUSDT perp (50x) | $69M / $30M / $2.4M | -97% |
| 3 | River (RIVER) — satUSD omni-CDP stablecoin | 2025-09-22 | 100M | $201M (DL-first $2.01, 09-23); ATH $87.73 on 2026-01-26 = $8.8B FDV | 19.6M circ now; initial float n/a | $553M → 0.36x | Binance Alpha/perps and others (not verified per venue) | $476M / $400M / $110M | -46% (-99% from ATH) |
| 4 | Plasma (XPL) — stablecoin L1 (pre-deposit) | 2025-09-25 | 10B | $12.75B ($1.275 Gate close); Polymarket 1-day FDV resolved >$8B | 1.8B (18%) → MC ≈ $2.3B | $3.89B stablecoins on chain (09-26) → 3.3x ("> $2B" per The Block → up to 6.4x) | Binance (HODLer #44), most CEXs | $3.67B / $1.25B / $962M | -93% |
| 5 | YieldBasis (YB) — Curve BTC-LP (crvUSD-based; adjacent, no points) | 2025-10-15 | 1B max | $671M ($0.671 Gate close); Polymarket 1-day FDV resolved $500M–$1B | 87.9M (8.8%) → MC ≈ $59M | $153M → 4.4x | Binance (HODLer #53) | $467M / $426M / $83M (CoinGecko shows $63M on 753M total) | -88% |
| 6 | Stable (STABLE) — USDT stablecoin L1 (pre-deposit) | 2025-12-08 | 100B | $2.15B ($0.0215 Gate close); Polymarket 1-day FDV resolved <$2B | n/a (26.7B circ now) | $0.48B stablecoins on chain (12-10) → 4.5x. Pre-deposits: $825M in Phase 1, "$2.6B" across two phases | Bybit, Bitget, Gate and others | $1.52B / $2.88B / $2.80B | +73% |
| 7 | Yala (YALA) — BTC-backed YU stablecoin (cautionary) | 2025-07-23 | 1B | $262M (DL-first $0.2625) | n/a | $213M → 1.2x | Binance Alpha and others (not verified) | $182M / $85M / ≈$0 | -100% |
| 8 | Unitas (UP) — USDu JLP delta-neutral yield dollar (Solana) | 2026-03-13 (Binance Wallet Exclusive TGE #44) | 1B | $72M (DL-first $0.0722, 03-14); Polymarket 1-day FDV resolved $50–100M | n/a (216M = 21.6% circ now) | $81M → 0.9x | Binance Wallet/Alpha | $197M / $333M / $241M (ATH $523M on 2026-08-31) | +224% |
| 9 | USD.AI (CHIP) — USDai GPU-credit yield dollar | 2026-04-21/22 | 10B | $612M ($0.0612 Gate close 04-21); $1.13B at 04-22 close; Polymarket 1-day FDV resolved $1B–$2B; ATH $1.40B on 04-23 | 2B (20%) → MC ≈ $122M | $284M → 2.2x (4.0x at the $1.13B day-2 FDV) | Binance, Coinbase, Upbit, Bithumb, Bybit, KuCoin; perps on Binance, OKX, Bitget, Hyperliquid, Lighter | $478M / $308M / $433M | -30% |
| 10 | Solstice (SLX) — USX synthetic dollar (Solana) | 2026-05-25 | 1B | $207M ($0.207 Gate close); "debuted near $0.37" per MEXC News (conflict) | n/a (242.8M circ now) | $398M (MEXC News) → 0.5x | Binance Alpha, Gate, Bitget, OKX, MEXC, BitMart, Kraken | $198M / $76M / $64M (ATH $658M on 06-27) | -61% |
| 11 | Re (RE) — reUSD reinsurance-backed yield dollar | 2026-06-18 | 1B | $437M ($0.437 Gate close); ATH $1.08B on 06-20 | 159.6M (16%) → MC ≈ $70M | $258M → 1.7x | Binance, Robinhood, OKX, Bybit, KuCoin | $472M / $431M / $463M | +1% |
| 12 | Cap (CAP) — cUSD covered-credit dollar | 2026-06-26 | 10B | $289M (DL-first $0.0289, 06-27); Polymarket 1-day FDV resolved $250–300M; auction cleared at $0.011 (≈$106–110M FDV) | 15.6% (1.56B) → MC ≈ $45M | $221M → 1.3x | Uniswap CCA auction, then CEXs (venues not verified) | $234M / $499M / $558M (ATL $155M on 07-12; ATH $783M on 08-14) | +93% |

Two boundary cases from May–Jun 2025, used for context only:
- **Huma (HUMA), 2025-05-26:** day-1 FDV $669M ($0.0669 Gate close, 10B supply), 17.3% float. Now $283M, -54% from DL-first.
- **Spark (SPK), 2025-06-17:** day-1 FDV $576M ($0.0576 Gate close, 10B). Now $225M, -62%.

**Sources for the table**
- Prices, all rows: [DefiLlama coins chart API](https://coins.llama.fi/chart/coingecko:cap-4) (ids: treehouse, reservoir, river, plasma, yield-basis, stable-2, yala, unitas, chip-2, solstice, re, cap-4, huma-finance, spark-2); [Gate.io candles API](https://api.gateio.ws/api/v4/spot/candlesticks?currency_pair=XPL_USDT&interval=1d); [CoinGecko coins API](https://api.coingecko.com/api/v3/coins/cap-4) (supply, ATH/ATL)
- TVL at TGE: [DefiLlama protocol API](https://api.llama.fi/protocol/cap) (slugs: treehouse-protocol, reservoir-protocol, river-omni-cdp, yield-basis, unitas-usdu, usd-ai, cap, re, yala); [DefiLlama stablecoins by chain](https://stablecoins.llama.fi/stablecoincharts/Plasma)
- Polymarket 1-day FDV resolutions: [Polymarket gamma API](https://gamma-api.polymarket.com/public-search?q=Cap%20FDV&keep_closed_markets=1)
- Treehouse: [ChainCatcher](https://www.chaincatcher.com/en/article/2193825); [PR Newswire](https://www.prnewswire.com/news-releases/treehouse-launches-tree-token-across-binance-okx-coinbase-and-top-exchanges-following-token-generation-event-302517520.html)
- Reservoir: [ChainCatcher](https://www.chaincatcher.com/en/article/2198259); [Chainplay](https://chainplay.gg/blog/binance-alpha-launch-reservoir-dam-aug-18/)
- River: [River docs, tokenomics](https://docs.river.inc/tokenomics/tokenomics)
- Plasma: [The Block](https://www.theblock.co/post/372300/stablecoin-layer-1-plasma-goes-live-introducing-xpl-token-and-defi-integrations); [CryptoNinjas](https://www.cryptoninjas.net/news/binance-unveils-plasma-xpl-with-75m-airdrop-and-10b-supply-ahead/)
- YieldBasis: [ChainCatcher](https://www.chaincatcher.com/en/article/2212384)
- Stable: [The Block, Phase 1](https://www.theblock.co/post/376022/stables-phase-1-hits-cap); [Yield Network case study](https://www.yieldnetwork.io/blog/stable-predeposit-case-study)
- Unitas: [PANews](https://www.panewslab.com/en/articles/019cdbd7-3251-72b7-8df5-b95b83c655b2)
- USD.AI: [usd.ai "$CHIP Is Live"](https://usd.ai/insights/chip-is-live)
- Solstice: [MEXC News](https://www.mexc.com/news/1112452); [Bitget News](https://www.bitget.com/news/detail/12560605428009)
- Re: [re.xyz TGE post](https://re.xyz/insights/re-tge-launch)
- Cap: [Bitget News](https://www.bitget.com/news/detail/12560605474641); [The Defiant](https://thedefiant.io/news/defi/cap-labs-cap-token-auction-106m-fdv-oversubscription)

**Additional cited facts**
- **YieldBasis float conflict:** YB's initial circulating supply is quoted as both "12.56%" and 87,916,667 YB. 87.9M is 8.8% of 1B, so the sources conflict — [search summary of Binance/ChainCatcher](https://www.chaincatcher.com/en/article/2212384)
- **Plasma public sale:** $0.05/XPL, i.e., a $500M FDV. Oversubscribed; the sale is described as "$300 million" — [search summary of ICO Drops](https://icodrops.com/plasma/)
- **Cap tokenomics:**
  - The ICO was 5% (500M CAP).
  - The auction had 1,002 bids and $16.4M of commitments, and cleared at $0.011. The Defiant gives a $106M FDV; DefiLlama records $110M — [The Defiant](https://thedefiant.io/news/defi/cap-labs-cap-token-auction-106m-fdv-oversubscription)
  - Initial float of 15.6% = ICO 5% + ecosystem 10% + market makers 0.6%. Investors and team have a 12-month cliff — [Bitget News](https://www.bitget.com/news/detail/12560605474641)
- **USD.AI tokenomics:**
  - ICO: 7% (700M CHIP) at a $300M FDV via CoinList, 100% unlocked at TGE.
  - Airdrop: 3% (300M CHIP), fully unlocked (search-summary only) — [ICO Drops](https://icodrops.com/usd-ai/)
  - "Protected CHIP" for ICO buyers settles at $270M / $190M FDV floors, with a USDC top-up — [usd.ai](https://usd.ai/insights/chip-is-live)
- **Re float:** 159.6M RE liquid at TGE, from the Ecosystem allocation — [re.xyz](https://re.xyz/insights/re-tge-launch)

### Inferences
- **Launch valuations of issuer comps:** the 8 yield-dollar issuers most similar to Saturn (DAM, RIVER, YALA, UP, CHIP, SLX, RE, CAP) launched at:
  - FDV: $72M–$612M, median ≈ $235M.
  - FDV/TVL: 0.36x–2.15x, median ≈ 1.27x.
  - Claude's arithmetic from the table above.
- **Floats were small:** initial circulating supply was typically 9–20% of total, so launch market caps ran from about $45M (Cap) to $122M (USD.AI).
- **Polymarket calibration:** the six resolved "FDV one day after launch" markets (Plasma, Stable, YB, Unitas, USD.AI, Cap) all settled in the bracket that matched the Gate/DefiLlama day-1 prints. For small issuers, the 1-day FDV settles close to FDV/TVL ≈ 1x.
- **Pre-market forecasts can miss badly.** USD.AI printed $1–2B at 1 day and then fell to about $0.48B by day 30. A Whales Market blog had predicted "$270M–$320M one day after launch" ([Whales Market blog](https://whales.market/blog/usd-ai-chip-fdv-prediction/)), and the actual day-1 FDV was 3–5x that.

### Gaps
- Initial float at TGE is missing for DAM, RIVER, STABLE, YALA, UP and SLX. The CoinGecko circulating figures are current, not at-TGE.
- Exact listing venues for River, Yala and Cap were not verified.
- Launch-minute (opening) FDVs were not obtainable because the Binance, OKX and Bybit APIs were geo-blocked. Day-1 closes are used instead.
- DefiLlama TVL for Reservoir at TGE ($54M) conflicts with the project's claim of about $250M.
- Plasma's and Stable's "TVL" is on-chain stablecoin supply, which is not strictly comparable.

---

## Q2. Airdrop economics: % to points holders, points duration, $/point, and evidence on Pendle YT outcomes

### Takeaway
Season-1 points pools for these TGEs were typically **3–10% of supply**; the median of the disclosed ones is about 9%. River's dynamic 30% is an outlier.

The 2026 cohort increasingly used protective designs:
- tiered or vested claims for large wallets (Re, Solstice)
- stablecoin-denominated "stabledrops" in place of tokens (Cap)
- protected ICOs (USD.AI)

Direct YT-buyer PnL for these comps is essentially unpublished.

### Cited Findings
- **Treehouse:**
  - 10% "Community Airdrop" plus a 5.75% "Future Airdrop" — [Tokenomist](https://tokenomist.ai/treehouse) (search-summary only)
  - Binance HODLer got 12.5M (1.25%) — [ChainCatcher](https://www.chaincatcher.com/en/article/2193825)
  - The Nuts snapshot was 2025-05-29, with a 100-Nuts minimum — [Treehouse blog](https://www.treehouse.finance/blog/tree-airdrop-checker)
- **Reservoir:**
  - Season 1 points (20B) = 10% of supply (100M DAM), claimable in four phases from 2025-08-18 to 10-17 — [CoinCarp](https://www.coincarp.com/currencies/reservoir-dam/project-info/); [Reservoir on X](https://x.com/reservoir_xyz/status/1929636144125563386) (search-summary only)
  - Binance Alpha also airdropped 320 DAM per eligible Alpha user — [ChainCatcher](https://www.chaincatcher.com/en/article/2198259)
  - **Implied $/point:** 0.005 DAM/pt × $0.089 = **≈ $0.00045 per point (≈ $446 per 1M points)** at DL-first. At today's $0.0024 that is ≈ $12 per 1M points (Claude's arithmetic).
- **River (dynamic airdrop):**
  - 1B River Pts convert into up to 30M staked RIVER (≈30% of supply, "Community Airdrop + Community Reserve").
  - Converting on day 1 yields close to zero; the full rate applies on day 180, a 270x difference — [River docs](https://docs.river.inc/tokenomics/airdrop); [BingX](https://bingx.com/en/learn/article/river-dynamic-airdrop-starts-22-september-how-to-claim-river-tokens)
  - Max value: 0.03 RIVER/pt × $2.01 = $0.06/pt at TGE (Claude's arithmetic). The actual value depended on conversion timing.
- **Plasma:**
  - 25M XPL (0.25%) was split *equally* across eligible pre-deposit/sale participants, about 9,304 XPL each — [PANews](https://www.panewslab.com/en/articles/1237e3c6-812c-46b4-b0f8-8a30a3ddc7dc); [BingX](https://bingx.com/en/learn/article/plasma-xpl-token-launch-airdrop-bonus-set-for-sep-25)
  - Binance HODLer got 75M (0.75%) — [CryptoNinjas](https://www.cryptoninjas.net/news/binance-unveils-plasma-xpl-with-75m-airdrop-and-10b-supply-ahead/)
  - The deposit vault cap was raised from $250M to $1B and filled in about 30 minutes — [Yahoo/Plasma](https://finance.yahoo.com/news/bitcoin-based-stablecoin-network-plasma-072622816.html)
- **Stable:**
  - 10% genesis airdrop (10B STABLE) to pre-deposit vault-receipt holders, including receipts deployed on Morpho, **Pendle** and Uniswap. Claims ran until 2026-03-02 — [Stable blog](https://blog.stable.xyz/the-stable-airdrop); [The Block tokenomics](https://www.theblock.co/post/381171/stable-unveils-tokenomics)
  - Phase 1 ($825M) was controversial: about $600M came from ten large wallets pre-announcement — [The Block](https://www.theblock.co/post/376022/stables-phase-1-hits-cap)
- **YieldBasis:** no points program. Binance HODLer got 10M YB (1%). The pre-launch target FDV was $200M (search-summary only) — [ChainCatcher](https://www.chaincatcher.com/en/article/2212384)
- **Unitas:**
  - Binance Wallet Alpha users (≥61 Alpha points) shared 30M UP (3%) — [BingX flash](https://bingx.com/en/flash-news/post/binance-wallet-launches-unitas-up-booster-and-tge-with-up-airdrop) (search-summary only)
  - Season 1 points ran until TVL hit $100M; Season 2 "Units" started 2026-03-24 — [CoinMarketCap AI updates](https://coinmarketcap.com/cmc-ai/unitas/latest-updates/) (search-summary only)
  - The S1 points-holder % was not found.
- **USD.AI:**
  - 3% airdrop (300M CHIP), fully unlocked at TGE (search-summary only) — [ICO Drops](https://icodrops.com/usd-ai/)
  - The USDai farm ran from about May 2025 (DefiLlama TVL start 2025-05-19) to the Apr-2026 TGE, about 11 months — [DefiLlama](https://api.llama.fi/protocol/usd-ai)
- **Solstice:**
  - About 7.5–8% of supply went to Flares holders.
  - Tiered unlock: regular users got 25% on day 1; top wallets got only 5–20% immediately; the remainder unlocks linearly over 3 or 9 months, subject to TVL maintenance — [MEXC News](https://www.mexc.com/news/1112452); [Bitget News](https://www.bitget.com/news/detail/12560605428009)
  - SLX fell more than 40% within hours "as airdrop claimers flooded the market", with complaints about "lower-than-expected unlock allocations" — [MEXC News](https://www.mexc.com/news/1112452)
- **Re:**
  - S1 wallets with ≤150M points (95% of participants) were fully unlocked on 2026-06-18.
  - Larger wallets got 150M points' worth immediately; the rest comes in 6 semiannual tranches over 3 years, contingent on keeping their average S1 TVL.
  - The total % was not disclosed — [re.xyz](https://re.xyz/insights/re-tge-launch)
- **Cap (unusual design):**
  - Homestead "caps" points (2026-01-29 → 07-23): 20x for holding cUSD, 40x for YT-cUSD/LP.
  - Points were paid as a **cUSD "stabledrop"**, not in CAP. Rates were 0.000027772 cUSD per cap (≈ **$27.8 per 1M caps**) and 0.000021267 cUSD per COG, calibrated to "5% of Cap's value at $250M FDV" (search-summary only) — [Cap blog](https://www.cap.app/blog/cap-stabledrop); [Today in DeFi](https://news.todayindefi.com/p/grvt-claim-live-cap-stabledrop-open)
  - Cap **cut the stabledrop from $12M to $4.2M** after backlash. The founder said he had committed "before the funding to back it was fully secured" — [The Defiant](https://thedefiant.io/news/defi/cap-cuts-its-stabledrop-airdrop-to-usd4-2m-from-usd12m-as-backlash-mounts)
  - No confirmed link was found between Homestead caps and CAP tokens (search-summary only).
- **Boundary cases:**
  - Huma S1: 5% (500M HUMA) — [Huma blog](https://blog.huma.finance/huma-airdrop-payfi-decentralized)
  - Spark Ignition: 300M SPK (3%) — [Spark docs](https://docs.spark.fi/airdrop/ignition)
- **Pipeline references:**
  - Apyx: 5% S1 and an S2 pool raised from 6% to 9% (see other notes) — [ChainCatcher](https://www.chaincatcher.com/en/article/2291854)
  - Saturn: up to 5% for S1 plus up to 5% for S2 — [ChainCatcher](https://www.chaincatcher.com/en/article/2292229)

### Inferences
- **Typical season-1 pool:** 3–10% of supply. Disclosed: CHIP 3, SPK 3, HUMA 5, SLX ≈7.75, TREE 10, DAM 10, STABLE 10, RIVER 30 (max). The median is about 9% (Claude's arithmetic). Saturn's 5% + 5% (10% across two seasons) is in line; Apyx's 5% + 9% is richer.
- **Post-2025 designs shift value away from mercenary and whale farmers**, which lowers realized $/point for large YT wallets:
  - Re: whale tranches over 3 years
  - Solstice: 5–20% up-front for top wallets
  - Cap: a stabledrop that was cut by 65%
  - River: time-decay conversion
- **Pendle YT evidence (weak):**
  - Stable explicitly credited Pendle-held receipts, and STABLE is one of the few tokens above DL-first (+73%).
  - Cap YT-cUSD holders (40x caps) were paid in cUSD, and the pool was cut from $12M to $4.2M. Any YT priced on the original $12M likely realized only about 35% of expected value (Claude's inference).
  - Solstice/Unitas/Re YT outcomes were not found.

### Gaps
- No published total-points figures or realized $/point were found for Treehouse, Unitas, USD.AI, Solstice or Re.
- No per-market Pendle YT PnL studies were found for any of these comps.
- The Unitas S1 airdrop % is unknown. The Re total airdrop % is undisclosed.
- The Cap stabledrop article date was not visible, and the per-cap rate after the cut was not found.

---

## Q3. Post-TGE performance (1-month and current drawdowns)

### Takeaway
The H2-2025 cohort collapsed: 5 of 7 are down 88–100% from DL-first. The H1-2026 cohort is roughly flat: median ≈ +1% now, with Unitas (+224%) and Cap (+93%) as winners and Solstice (-61%) and USD.AI (-30%) as losers.

The newer cohort also has had less time to decay (3–6 months since TGE vs 9–14 months).

### Cited Findings
All figures are API pulls from DefiLlama coins daily prices on 2026-09-29, measured against DL-first. Columns are d7 / d30 / d90 / now.

| Token | d7 | d30 | d90 | Now |
|---|---|---|---|---|
| XPL | -36% | -74% | -91% | -93% |
| TREE | -30% | -50% | -70% | -93% |
| DAM | -44% | -22% | -67% | -97% |
| RIVER | +16% | +137% | +99% | -46% |
| YB | -40% | -32% | -38% | -88% |
| STABLE | -7% | -6% | +79% | +73% |
| YALA | -31% | -31% | -68% | ≈-100% |
| UP | +55% | +173% | +361% | +224% |
| CHIP | +36% | -22% | -50% | -30% |
| SLX | +115% | +22% | -53% | -61% |
| RE | +57% | +2% | -7% | +1% |
| CAP | -18% | -19% | +72% | +93% |

Source: [DefiLlama coins chart API](https://coins.llama.fi/chart/coingecko:unitas)

- **Measured from intraday or day-2 peaks the losses are larger:**
  - CHIP: ATH $0.140 on 2026-04-23 → -69%
  - RE: ATH $1.079 on 06-20 → -57%
  - SLX: ATH $0.658 on 06-27 → -90%
  - TREE: ATH $1.36 on launch day → -97%
  - Source: [CoinGecko API](https://api.coingecko.com/api/v3/coins/re)
- **Mercenary TVL outflows after TGE (DefiLlama):**
  - Reservoir: $54M → $25M at +30d. It peaked at $390M in 2025-10 and is $72M now.
  - USD.AI: $679M 90 days before TGE vs $284M at TGE (peak $702M on 2025-11-22) → $231M now.
  - Solstice: peak $523M (2026-07-17) → $215M now.
  - Unitas: $81M → $102M at +30d → $46M now.
  - Cap: $221M → $252M at +30d → $289M now.
  - Re: $258M → $390M now.
  - Source: [DefiLlama protocol API](https://api.llama.fi/protocol/reservoir-protocol)
- **Yala:** YU was exploited in Sep 2025, when 120M YU was minted without authorization and fell to $0.20. It depegged again in Nov 2025 (-53% to $0.44), and YALA went to about $0 — [The Block](https://www.theblock.co/post/370547/yalas-bitcoin-backed-stablecoin-yu-depegs-after-security-breach-leads-to-unauthorized-mint); [CCN](https://www.ccn.com/news/crypto/yala-stablecoin-second-depeg/)

### Inferences
- Across all 12 comps the median d30 is about **-20%** (Claude's arithmetic).
- For the 8 issuer comps the median d30 is about -9%. The median now is about -38%, with a very wide range from -100% to +224%.
- **2026 launches that held up shared these features:**
  - low FDV (UP $72M)
  - small float (Cap 15.6%, Re 16%)
  - vesting or protection for sale buyers (Cap's auction; Re's tiering)
  - TVL that kept growing after TGE (Cap, Re)
- **Launches that failed had high launch FDV/TVL, a big day-1 pump, or protocol-risk events:**
  - CHIP: 4x FDV/TVL at day 2
  - SLX: +115% in the first week, then -90% from ATH
  - YALA and DAM

### Gaps
- There is no Q3-2026 cohort to measure, because no stablecoin TGE was found in Jul–Sep 2026.
- d30/d90 are measured from DL-first (morning after listing), not from the listing-open price.

---

## Q4. Sector synthesis: medians by cohort, is the trend cooling, and the typical season-1 airdrop

### Takeaway
**Launch FDVs compressed:** the all-comps median fell from about $668M (H2 2025) to about $289M (H1 2026). FDV/TVL eased from about 1.65x to about 1.3x, and post-TGE outcomes improved.

**Q3 2026 had zero stablecoin TGEs found.** Avant and Apyx delayed, and the pipeline is pushed into Q4 2026 (infiniFi, Apyx, Saturn). So issuance is cooling while launched valuations have become more conservative.

### Cited Findings
Cohort medians below are Claude's arithmetic from the Q1 and Q3 tables (API pulls, 2026-09-29).

**Cohort medians**

| Cohort | n | Median day-1 FDV | Median FDV/TVL | Median d30 | Median d90 | Median now |
|---|---|---|---|---|---|---|
| H2 2025, all (TREE, DAM, YALA, RIVER, XPL, YB, STABLE) | 7 | ≈ $668M | ≈ 1.65x | ≈ -31% | ≈ -67% | ≈ -93% |
| H2 2025, issuers only (DAM, YALA, RIVER) | 3 | ≈ $201M | ≈ 1.2x | ≈ -22% | ≈ -67% | ≈ -97% |
| H1 2026 (UP, CHIP, SLX, RE, CAP; all are issuers) | 5 | ≈ $289M | ≈ 1.3x | ≈ +2% | ≈ -7% | ≈ +1% |
| Q3 2026 | 0 | n/a | n/a | n/a | n/a | n/a |

Across all 12 comps: median day-1 FDV ≈ $363M and median FDV/TVL ≈ 1.5x. Across the 8 issuers: median FDV ≈ $235M and median FDV/TVL ≈ 1.27x.

**Q3 2026 pipeline status (none TGE'd)**
- **Avant:**
  - Postponed its TGE to "mid-September", saying "DeFi tokens as a whole are currently under pressure". Points stopped 2026-05-15 — [Bitget News](https://www.bitget.com/news/detail/12560605409666)
  - Its docs still say "TGE is currently targeted for September" — [Avant docs](https://docs.avantprotocol.com/rewards-program/avant-season-1-airdrop)
  - ChainCatcher shows no newer Avant news after 2026-05-13 — [ChainCatcher tag](https://www.chaincatcher.com/en/tags/avant)
  - CoinGecko lists "avant" with no market data (API pull 2026-09-29), so it is treated as not launched — [CoinGecko API](https://api.coingecko.com/api/v3/coins/avant)
- **Apyx:**
  - Postponed from Oct 13 2026, and the airdrop pool was raised from 6% to 9% — [ChainCatcher](https://www.chaincatcher.com/en/article/2291854)
  - Its Polymarket FDV market is still open (2026-09-29). Yes-prices: >$100M 0.63, >$200M 0.305, >$500M 0.09 (thin and internally inconsistent: >$300M is priced at 0.355) — [Polymarket gamma](https://gamma-api.polymarket.com/public-search?q=Apyx%20FDV)
- **infiniFi:** raised $3M+ and plans a Q4 2026 TGE. S1 and earned S2 points carry fixed, undiluted allocations — [PR Newswire](https://www.prnewswire.com/news-releases/infinifi-raises-3m-ahead-of-q4-tge-302887464.html); [Alea Research](https://alearesearch.substack.com/p/infinifi-season-1-points-and-2026)
- **Theo Network:** Polymarket FDV market still open. Yes-prices: >$100M 0.405, >$300M 0.30. Theo Network TVL ≈ $134M.
  - The "THEO" token that launched on 2026-08-20 belongs to **Autheo**, a different project — [Polymarket gamma](https://gamma-api.polymarket.com/public-search?q=Theo%20FDV); [CoinGabbar](https://www.coingabbar.com/en/crypto-currency-news/autheo-tge-update); [DefiLlama](https://api.llama.fi/protocols)
- **Neutrl:** Polymarket >$20M is only 0.22 "Yes", implying a low probability of launch before the deadline — [Polymarket gamma](https://gamma-api.polymarket.com/public-search?q=Neutrl%20FDV)
- **Strata:** "expected April 2026" (search-summary only), but no traded token was found — [AirdropAlert](https://airdropalert.com/airdrops/strata-markets/)
- **Noon:** no token found. Noon's TVL is $39M — [DefiLlama](https://api.llama.fi/protocols)
- **Other stablecoin-adjacent names with open Polymarket FDV markets (2026-09-29):**
  - Multipli.fi: >$250M 0.56, >$300M 0.485
  - 3Jane: >$100M 0.565, >$200M 0.28
  - Tori Finance: >$50M 0.375
  - Perena: >$100M 0.245
  - Felix: >$100M 0.08
  - Source: [Polymarket gamma](https://gamma-api.polymarket.com/public-search?q=FDV%20one%20day%20after%20launch&events_status=active)
- **Cautionary cases:**
  - Elixir: deUSD collapsed about 98% after Stream Finance's roughly $93M loss (Nov 2025) — [Pharos](https://pharos.watch/learn/case-studies/stream-elixir-contagion-2025/)
  - Level: wound down in Sep–Oct 2025 with no token — [Bitget News](https://www.bitget.com/news/detail/12560604988048)
  - Yala: collapsed (Q3 above)

### Inferences
- **Is the trend cooling?**
  - Yes in *volume*: no stablecoin-sector TGEs in Q3 2026, and several delays that explicitly cite market conditions.
  - Valuations have *reset lower* rather than collapsed: the H1-2026 issuer median is ≈ $289M FDV at ≈ 1.3x TVL.
  - The H1-2026 cohort has held up better on the same d30/d90 horizon: median d90 ≈ -7% vs ≈ -67% for H2 2025.
- **Rule of thumb for a small yield-dollar TGE in Q4 2026:** day-1 FDV ≈ 0.5–2x TVL, centered around 1.3x. Expect -20% to -50% within 90 days unless TVL keeps growing post-TGE.
- **Typical season-1 airdrop** is 3–10% of supply (median ≈ 9%), increasingly with whale vesting or tiering.

### Gaps
- The sample is small (3–7 per cohort), and the H2-2025 "all" cohort mixes L1 pre-deposit chains and non-stablecoin yield protocols.
- Selection bias: projects that never TGE'd (Level) or whose tokens were delisted are only partly captured.
- The H1-2026 "now" figures cover only 3–6 months of post-TGE life.

---

## Q5. $STRN (Saturn, saturn.credit) market-implied valuation: pre-market, points markets and prediction markets

### Takeaway
The only live price signal found is **Polymarket**. As of 2026-09-29 about 06:00 UTC it implies:
- about 74% odds of an STRN launch by 2026-12-31, and about 89% by end-2027
- conditional on launch, a **median 1-day FDV ≈ $205M** (interquartile ≈ $95M–$330M; mean ≈ $250–265M)

Liquidity is very thin, at about $21.6K lifetime volume.

No STRN pre-market or points market was found on Whales Market, Hyperliquid (main plus all HIP-3 dexes), or Aevo. Bybit and Binance could not be checked because of geo-blocks.

### Cited Findings
- **Identity check:**
  - Polymarket's Saturn markets resolve on "Saturn (https://x.com/saturn_credit)", i.e., saturn.credit. Stablecoins such as USDat do not count as a token launch — [Polymarket gamma API](https://gamma-api.polymarket.com/public-search?q=saturn); event page slugs "saturn-fdv-above-one-day-after-launch-20260623191408697" and "will-saturn-launch-a-token-by" at [Polymarket](https://polymarket.com/event/saturn-fdv-above-one-day-after-launch-20260623191408697)
  - The unrelated "Saturn Classic DAO Token (STRN)" is a different, dead token ($0, no volume) — [BitDegree](https://www.bitdegree.org/cryptocurrency-prices/saturn-classic-dao-token-strn-price)
  - CoinGecko "saturn-dollar" (USDAT) is Saturn's stablecoin, not the governance token — [CoinGecko search API](https://api.coingecko.com/api/v3/search?query=saturn)
- **Polymarket "Saturn FDV above ___ one day after launch?"**
  - Created 2026-06-23. Event volume ≈ $21.6K; liquidity ≈ $97.9K, of which ≈ $63K sits on the $800M strike.
  - FDV is defined as total supply × price at 4:00 PM ET on the day after launch. If there is no launch by 2028-01-01 the market resolves No.
  - Mid "Yes" prices at 2026-09-29 06:00 UTC:

| Strike | Yes mid | Bid / ask |
|---|---|---|
| >$50M | 0.885 | 0.88 / 0.89 |
| >$100M | 0.65 | 0.63 / 0.67 |
| >$200M | 0.46 | 0.45 / 0.47 |
| >$300M | 0.26 | — |
| >$400M | 0.14 | — |
| >$500M | 0.075 | — |
| >$600M | 0.0425 | — |
| >$700M | 0.036 | — |
| >$800M | 0.0265 | — |
| >$1B | 0.024 | — |

  - 1-month changes: >$200M -0.06, >$300M -0.12, >$50M +0.045.
  - Source: [Polymarket gamma API](https://gamma-api.polymarket.com/public-search?q=saturn)
- **Polymarket "Will Saturn launch a token by ___?"**
  - Created 2026-06-05; volume ≈ $16.2K.
  - Yes-prices: by 2026-12-31 **0.74** (1-month change +0.545, i.e., about 0.20 a month ago, before the 2026-09-25 TGE announcement); by 2027-06-30 0.90; by 2027-12-31 0.89.
  - Source: [Polymarket gamma API](https://gamma-api.polymarket.com/public-search?q=saturn)
- **Whales Market:** all 467 tokens were paginated on 2026-09-29, including pre-market and points markets. There is **no Saturn/STRN listing**.
  - Peers that are listed: USD.AI CHIP (ended, last $0.039), Solstice SLX (ended, last $0.25), 3Jane (pending, no trades), Multipli (active, no trades).
  - Source: [Whales Market API](https://api.whales.market/v2/tokens)
- **Hyperliquid:** no STRN or SATURN perp in the main universe (234 perps), in any HIP-3 dex (xyz, flx, vntl, hyna, km, abcd, cash, para, mkts, io), or in spot. CHIP and RESOLV perps exist — [Hyperliquid info API](https://api.hyperliquid.xyz/info)
- **Aevo:** 102 perpetual markets checked, with no pre-launch STRN market — [Aevo API](https://api.aevo.xyz/markets?instrument_type=PERPETUAL)
- **Bybit/Binance pre-market:** not checkable. The Bybit API returned a CloudFront country block and Binance returned "restricted location". No web mention of an STRN pre-market on either exchange was found.
- **Saturn context:**
  - DefiLlama TVL is $146.4M on 2026-09-29, with a peak of $214M on 2026-06-09.
  - DefiLlama-listed raises: $0.8M (2026-01-15) and a $2M seed (2026-05-07), plus an undisclosed strategic round (2026-08-13) — [DefiLlama protocol API](https://api.llama.fi/protocol/saturn)
  - The TGE was announced 2026-09-25: STRN in Q4 2026, with up to 5% of supply for Season 2 — [ChainCatcher](https://www.chaincatcher.com/en/article/2292229)
  - An analyst example used "$100M FDV with 5% to S1" — [2lambroz Substack](https://2lambroz.substack.com/p/11-yield-with-zero-strc-risk-i-had)
  - The Pendle-YT-implied points break-even is about $55M FDV, per the sibling note `saturn_points_program.md` (Q4).

### Inferences
- **Conditional FDV distribution** (Claude's arithmetic): dividing each Yes-price by P(launch by 2028) ≈ 0.89 gives P(FDV > X | launch):

| X | P(FDV > X \| launch) |
|---|---|
| $50M | ≈ 0.99 |
| $100M | ≈ 0.73 |
| $200M | ≈ 0.52 |
| $300M | ≈ 0.29 |
| $400M | ≈ 0.16 |
| $500M | ≈ 0.08 |
| $1B | ≈ 0.03 |

  - Median ≈ **$207M**; 25th–75th percentile ≈ $96M–$331M.
  - Mean ≈ $250M, truncated at $1B, or about $264M with a linear tail to $2B.
  - This is a thin market: a few thousand dollars can move strikes by 5–10 points.
- **Cross-check against the comps:**
  - $146M TVL × issuer-median FDV/TVL 1.27–1.31x gives **≈ $186–192M**. The comp range of 0.36–2.15x gives ≈ $53M–$315M.
  - The Polymarket median (~$207M) is therefore consistent with 2026 comps. It sits about 4x above the ≈ $55M Pendle-YT break-even, which suggests YT is cheap relative to Polymarket's view.
  - Caveats: the Season-2 pool shrinks pro-rata if TGE comes before Dec 8, and 2026 whale-tiering designs could cut realized value.
- **Calibration:** Polymarket's resolved 1-day FDVs for peers matched realized prints (Cap $250–300M; Unitas $50–100M). The market has been a reasonable, if noisy, guide to day-1 FDV. Day-30 FDVs then ran a median of about 20% lower.

### Gaps
- No Polymarket price history (time series) could be retrieved: the CLOB prices-history endpoint returned 403 via the proxy. Only the current mid-prices and 1d/1w/1m changes are available.
- No Kalshi market was checked. No analyst-published Pendle-implied STRN FDV was found beyond the sibling note's ≈ $55M break-even.
- Binance/Bybit/OKX pre-market listings could not be queried because of geo-blocks. Their absence is inferred only from the lack of any news mention.
- STRN total supply, initial float and listing venues are unannounced, so FDV-to-price conversion is impossible.
