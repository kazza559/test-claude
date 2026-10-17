# HYPE, LIT, KNTQ and Variational: fundamentals, tokenomics and catalysts (as of 2026-10-17)

Data conventions: "snapshot" means live API pulls on **2026-10-17 between 03:22 and 03:31 UTC**. These are a Saturday-morning UTC window, so the 24h figures mostly cover Friday 2026-10-16. Mids at pull time were HYPE 79.92, LIT 3.198, KNTQ 0.3108–0.3114, SOL 104.6 and BTC 81,490 ([Hyperliquid info API, allMids](https://api.hyperliquid.xyz/info)). Rolling-window figures (30d/90d) come from DefiLlama daily series that end 2026-10-16 or 2026-10-17. Older figures are flagged as STALE. Scripts and raw data are in `/tmp/claude-0/-home-user-test-claude/8ec8a334-85ed-54af-babc-62d7e4c0704b/scratchpad/research/hl_eco/` (`pull_hl.py`, `analyze1.py`, `pull_venues.py`, `kntq_onchain.py`, `derive.py`, raw files in `data/`).

## Q1. HYPE: protocol fees/revenue, Assistance Fund buybacks and staking

### Takeaway
Hyperliquid had its best fee month since Nov 2025 in **September 2026 ($91.3M)**. Fee momentum has since faded: **30-day fees are $88.2M, −15% vs the prior 30 days**, while **90-day fees are $235.4M, +20% vs the prior 90 days**. Almost all revenue (~$2.37M/day) buys HYPE into the Assistance Fund, which now holds **48.10M HYPE (4.8% of total supply, ≈$3.84B)**. The buyback is real but small in supply terms, about **0.8M HYPE/month (≈0.26–0.36% of circulating per month)**. At about $864M annualized revenue, HYPE trades at roughly **21x mcap/revenue and 88x FDV/revenue**.

### Cited Findings
- **Fees.** DefiLlama Hyperliquid fees:
  - Windows: **30d $88.23M** vs prior 30d $103.74M (−15.0%). **90d $235.37M** vs prior 90d $196.20M (+20.0%). Last 7d $20.36M (~$2.91M/day). Last full day (2026-10-16) $3.14M.
  - Monthly 2026: Jan $77.3M, Feb $70.7M, Mar $69.5M, Apr $58.7M, May $62.2M, Jun $81.0M, Jul $55.1M, Aug $77.8M, **Sep $91.3M**, Oct 1–16 $44.3M (pace ≈$86M/month).
  - Nov 2025 was $101.4M and Oct 2025 $124.8M.
  - Source: [DefiLlama fees API – hyperliquid](https://api.llama.fi/summary/fees/hyperliquid?dataType=dailyFees).
- **Revenue.** DefiLlama Hyperliquid revenue, which equals "holders revenue" (the buyback):
  - **30d $71.05M** vs prior 30d $84.46M (−15.9%). **90d $186.00M** vs prior 90d $144.10M (+29.1%). Sep 2026 $74.19M. Last 7d $16.16M. All-time $1.35B.
  - Annualized from the 30d figure: **≈$864M**.
  - Source: [DefiLlama fees API – hyperliquid revenue](https://api.llama.fi/summary/fees/hyperliquid?dataType=dailyRevenue).
- **Perps vs spot.** Perps account for nearly all of it: 30d perp fees $85.08M and perp revenue $69.04M — [DefiLlama fees API – hyperliquid-perps](https://api.llama.fi/summary/fees/hyperliquid-perps?dataType=dailyFees).
- **Assistance Fund balance.** `0xfefe…fefe` holds **48,095,596 HYPE**, with recorded entry notional $1,372.5M (average cost ≈$28.54). The fund also holds 4,222,452 KNTQ. HL's `tokenDetails` lists the AF's 48.10M HYPE as non-circulating — [Hyperliquid info API, spotClearinghouseState + tokenDetails, snapshot](https://api.hyperliquid.xyz/info).
- **Older AF figure (STALE).** Netcoins (undated) put the AF at "~29.8M HYPE worth over $1.5B" and said "97–99% of fees … flow into the Assistance Fund" — [Netcoins](https://netcoins.com/blog/hyperliquids-hype-token-unlocks).
- **Buyback in HYPE terms (calculation).** $71.05M over 30d is ≈**$2.37M/day**. At the 30d HL VWAP of $88.78 that is ≈**26.7k HYPE/day ≈ 0.80M HYPE/month**. That equals ≈0.26%/month of HL-reported circulating supply (302.07M) or ≈0.36%/month of CoinGecko circulating (222.45M) — [DefiLlama](https://api.llama.fi/summary/fees/hyperliquid?dataType=dailyHoldersRevenue); [Hyperliquid info API candleSnapshot](https://api.hyperliquid.xyz/info).
- **Supply per HL.** Circulating 302.07M, total 998.85M, futureEmissions 410.70M. Non-circulating balances: `0x43e9abea…a251` with **237,986,771 HYPE** and the AF with 48.10M — [Hyperliquid info API, tokenDetails](https://api.hyperliquid.xyz/info).
- **Supply per CoinGecko.** Circulating 222.45M, total 955.3M, mcap $17.78B, FDV $76.37B — [CoinGecko API](https://api.coingecko.com/api/v3/coins/hyperliquid). The two circulating figures differ by ~80M HYPE.
- **Valuation (calculation).**
  - CoinGecko mcap / annualized revenue ≈ **20.6x**.
  - FDV / revenue ≈ **88x**.
  - On HL's circulating supply (302M × $79.9 = $24.1B) ≈ 27.9x.
- **Staking.**
  - **441.31M HYPE staked** across 35 validators (27 active). Predicted APR ≈2.17% on the Foundation validators.
  - Largest validators: Hyper Foundation 1–5 ≈208.1M combined. **"Hyperliquid Strategies x Unit" 38.0M.** Anchorage by Figment 28.2M. Hypurrscanning 23.2M. Nansen x HypurrCollective 21.9M.
  - Source: [Hyperliquid info API, validatorSummaries, snapshot](https://api.hyperliquid.xyz/info).
- **HYPE perp positioning (snapshot).**
  - OI 19.88M HYPE (**$1.59B**); 24h perp volume $314M plus spot (@107) $44.5M.
  - Funding +0.00082%/h (≈+7.2% APR). The 30d average is +10.3% APR and the 7d average +7.9% APR.
  - Source: [Hyperliquid info API, metaAndAssetCtxs + fundingHistory](https://api.hyperliquid.xyz/info).

### Inferences
- The buyback supports price but does not offset large unlocks. One month of buybacks (~0.8M HYPE) is about 1/12 of the nominal 9.92M monthly core-contributor tranche (see Q2). The October team payout of 3.75M HYPE equals ≈140 days of buybacks.
- Fee trend for the 3–6-month window: the 90-day trend is up and September was the cycle-best month, but the last 30 days rolled over (−15%) as volatility fell. Fees are pro-cyclical, so in a renewed BTC leg up the $2.5–3.0M/day buyback could plausibly return to $3–4M/day. That is an inference from the Sep 2026 and Oct–Nov 2025 levels, not a forecast from any source.
- Staked supply (441M) is larger than HL's own circulating figure (302M), so team and Foundation tokens are a large part of stake. That makes the staking ratio a weak signal of retail conviction.

### Gaps
- No independent time series of AF HYPE holdings (e.g., month-end 2025 vs now) was pulled, so the cumulative buyback since a fixed date is not computed. Only current holdings (48.10M) and cost basis ($1.37B) are verified.
- DefiLlama does not split spot vs perp fees cleanly (the `hyperliquid-spot` slug returned HTTP 400).

## Q2. HYPE: team unlocks, ETF flows and treasury companies (supply vs. demand)

### Takeaway
The core-contributor vesting started around late Nov 2025. **Actual distributions have run far below the nominal ~9.9M HYPE/month**, typically 0.14–0.53M per month. October 2026 was the exception: **3.75M HYPE was unstaked and sold OTC to institutional buyers**, with half delivered to five wallets by Oct 7. On the demand side, **Hyperliquid Strategies (PURR) is still a large net buyer (≈38.5M HYPE, +~5M since Sep 8)**. The two US spot ETFs (21Shares THYP, Bitwise BHYP) hold about $430M but saw **net outflows in Aug–Sep**. No October ETF flow data was found.

### Cited Findings
- **Schedule.** Core contributors hold 23.8% of supply, locked for one year after the 2024-11-29 genesis and "vested on a rolling basis" since around Nov 2025, with most vesting completing 2027–2028. CryptoEconomy (2026-09-30) listed **9.92M HYPE (~$856M) for 2026-10-06**. Tokenomist-based price reactions after earlier unlocks: June ≈+1%, July ≈−7% (14d), August ≈−3% (14d). Source: [Bitrue, 2026-10-01](https://www.bitrue.com/blog/hype-token-unlock-october).
- **Nominal tranche (older source, STALE).** "a 29 November cliff of 9.92M HYPE … then ~9.9M HYPE per month linearly for 24 months"; the article was not year-stamped — [Netcoins](https://netcoins.com/blog/hyperliquids-hype-token-unlocks).
- **First payouts.** The Block headline (2025-12-29): "Hyperliquid Labs set for next HYPE token payout as 1.2 million tokens unstake"; the URL slug refers to the "first allocation" — [The Block](https://www.theblock.co/news/defi/2025-12-29-hype-tokens-unstaked-for-hyperliquid-labs-first-allocation-383880). Only the headline was retrieved.
- **October 2026 OTC.** Per [CryptoBriefing, 2026-10-07](https://cryptobriefing.com/hyperliquid-labs-hype-otc-distribution/):
  - **3.75M HYPE (~$330M)** began unbonding 2026-09-30 and finished unstaking 2026-10-07.
  - **1.875M was sent to five OTC buyer wallets at 375,000 each**. The other half had not moved by Oct 7.
  - Co-founder iliensinc confirmed an OTC agreement with an undisclosed institution, and the team says the tokens will not enter public markets (paraphrased).
  - Prior monthly distributions were "140,000 to 534,000 HYPE"; the October schedule nominally listed 9.9M.
- **Conflicting accounts of the October deal.**
  - Earlier reports said one institutional buyer — [BeInCrypto via search](https://beincrypto.com/hyperliquid-token-unlock-320-million-price-impact/).
  - CryptoBriefing reports five wallets.
  - Crypto.news says HYPE "drops 4% to $87 as team starts $330M token deal" — [crypto.news](https://crypto.news/hype-drops-4-to-87-as-team-starts-330m-token-deal/). CryptoBriefing instead says the initial reaction was positive.
- **Team-allocation-sized holding (on-chain).** HL lists `0x43e9abea1910387c4292bca4b94de81462f8a251` as non-circulating with **237.99M HYPE**, which matches the 23.8% (238M) core-contributor allocation almost exactly — [Hyperliquid info API, tokenDetails](https://api.hyperliquid.xyz/info). The wallet label is my inference; it is not officially confirmed.
- **ETFs.** Per [CryptoBriefing, 2026-09-14](https://cryptobriefing.com/hype-etf-outflows-26-million-september-2026/):
  - THYP (21Shares) launched 2026-05-12.
  - Week of Sep 7–11: **−$26.4M** combined (BHYP −$20.1M, THYP −$6.3M). The 12 sessions to Aug 3 saw −$29.8M.
  - **Cumulative net inflows ≈$330M; net assets $430M ≈2.40% of HYPE mcap.**
- **BHYP.** Bitwise BHYP launched 2026-05-15, took ~$19M in one day and overtook THYP as the largest HYPE ETF — [Whale Alert story via search](https://whale-alert.io/stories/82ba01cb9e0690/Bitwise-HYPE-ETF-becomes-worlds-largest-after-19M-inflow).
- **Hyperliquid Strategies (Nasdaq: PURR), holdings and buying.**
  - DefiLlama's treasury tracker shows **38.52M HYPE as of 2026-10-08**, with purchases almost every week from late Aug into Oct — [DefiLlama DAT – PURR, via search](https://defillama.com/digital-asset-treasury/PURR).
  - It bought **494,200 HYPE (~$45.8M) on 2026-09-25** (~35.1M held then) — [Crypto Economy](https://crypto-economy.com/hyperliquid-strategies-buys-45-8m-in-hype/).
  - A September filing showed ~33.2M HYPE as of Sep 8 — [crypto.news](https://crypto.news/hype-whales-move-to-exchanges-as-a-treasury-keeps-buying/).
  - On-chain cross-check: the "Hyperliquid Strategies x Unit" validator has 38.0M HYPE delegated (snapshot) — [Hyperliquid info API](https://api.hyperliquid.xyz/info).
- **PURR funding and earlier history.**
  - Aug 27 earnings: raised $646.6M at an average $8.70/share and bought ~16.5M HYPE at an average $46.77.
  - A Sep 1 amendment lifted the equity sale facility from $1B to **$2.5B**.
  - Source: [CoinTurk](https://en.coin-turk.com/hyperliquid-strategies-raises-stock-sale-program-to-2-5-billion-for-hype-accumulation/).
  - A Dec 2025 $30M share buyback was authorized — [The Block](https://www.theblock.co/post/381780/hype-token-treasury-hyperliquid-strategies-stock-repurchase).
- **Lion Group (LGHL).** On 2026-09-29 it sold its entire SOL position and part of its BTC to buy ~38,102 HYPE, and now holds ~232,900 HYPE (~$20.1M) — [PR Newswire](https://www.prnewswire.com/news-releases/lion-group-holding-ltd-announces-strategic-treasury-reallocation-toward-hyperliquid-hype-302893878.html).
- **Robinhood listing.** Robinhood announced on **2026-09-30** that US perps via Bitstamp will include **HYPE (up to 3x)**, alongside BTC, ETH, SOL, XRP, DOGE, ADA and LINK. This is a new US retail access channel for HYPE exposure, with no launch date given — [KuCoin/Odaily, 2026-09-30](https://www.kucoin.com/news/flash/lighter-s-token-dips-20-as-robinhood-announces-bitstamp-futures-expansion).

### Inferences
- The unlock risk has changed character. The nominal schedule implies ~$790M/month of supply at $79.9, but the team is paying out mostly small amounts and placing larger tranches OTC. The OTC buyers' resale terms are undisclosed, so the 1.875M HYPE not yet delivered (and the five buyer wallets) are the overhang to watch.
- If `0x43e9…a251` really is the team allocation, almost the whole 238M is still non-circulating. That caps realized dilution so far, but it also means the full overhang still exists.
- The marginal structural bid is PURR (≈+5M HYPE from Sep 8 to Oct 8, ≈ six months of AF buybacks in one month). ETF demand turned negative in Aug–Sep. A pause in PURR's buying, for example if its share price falls below NAV and shuts the ATM, would remove the largest discretionary buyer. That is an inference: PURR's NAV premium was not checked.

### Gaps
- No October 2026 ETF flow data was found (Farside and SoSoValue were not reachable in this pass).
- No new data on Hyperion DeFi (HYPD) HYPE holdings or activity.
- No reconciled month-by-month record of team distributions (sold vs staked) since Nov 2025 beyond the 140k–534k range, the Dec 2025 1.2M headline and the Oct 3.75M OTC. Tokenomist and ASXN were not fetched.
- PURR's mNAV and share price were not checked.

## Q3. HYPE: HIP-3, HyperEVM/USDH, market share, incidents, performance vs BTC, bull/bear

### Takeaway
**HIP-3 is now ~36% of Hyperliquid perp volume ($3.21B/24h, OI $3.85B), but it is effectively one venue: trade.xyz (`xyz`) has ≈97.5% of HIP-3 volume.** Several other builder dexes (Felix, Ventuals, HyENA, dreamcash, Kinetiq `km`) now show every market delisted. Hyperliquid's share of on-chain perps is stable-to-up (≈57% of on-chain OI per Castle Labs on 10-14; ≈57% of 24h volume across six venues in my snapshot, including HIP-3). HYPE is **+214% YTD vs BTC −7%**, but it **lagged BTC since the July 1 cycle low (+28% vs +36%)** and is −18% from its 2026-09-23 ATH.

### Cited Findings
- **HIP-3 snapshot (24h), per [Hyperliquid info API, perpDexs + metaAndAssetCtxs per dex](https://api.hyperliquid.xyz/info):**
  - Total volume **$3.212B vs main-dex perps $5.682B**, so HIP-3 is **36.1%** of HL perp volume. HIP-3 OI is **$3.85B**; main-dex OI is $11.31B.
  - **`xyz` (trade.xyz, deployer 0x8880…0888)**: $3.13B volume, $3.76B OI, 115 live of 136 markets. Top markets: XYZ100 $329M, SP500 $269M, CL (oil) $230M, BRENTOIL $219M, SKHX $206M, TSLA $200M.
  - Smaller live dexes: `io` (EntropyIO) $66.8M; `para` (Paragon) $6.5M; `mkts` (Markets by Kinetiq) $6.4M.
  - **`flx` (Felix), `vntl` (Ventuals), `hyna` (HyENA), `cash` (dreamcash), `km`, `abcd`: every market flagged delisted, zero volume.**
- **Polymarket on HIP-3.** "HIP-3 OI hit $5B in 2026?" trades at **36.6%**; $6B at 13% — [Polymarket gamma API](https://gamma-api.polymarket.com/public-search?q=hyperliquid).
- **USDH on HL spot.** USDH/USDC volume was **$4,350/24h**. The HYPE/USDH, UBTC/USDH and KNTQ/USDH pairs have no live mid (dormant). The AF holds 43,220 USDH — [Hyperliquid info API, spotMetaAndAssetCtxs](https://api.hyperliquid.xyz/info).
- **Market share, my 24h venue snapshot (from each venue's API):**
  - Volumes: Hyperliquid main + HIP-3 $8.89B; **Variational $3.02B**; Lighter $1.85B; Aster $1.42B; Extended $0.49B; Paradex $0.014B.
  - Shares of that $15.69B: **HL 56.7%, Variational 19.3%, Lighter 11.8%, Aster 9.1%, Extended 3.1%, Paradex 0.1%**.
  - edgeX's API returned 503 and Binance returned 451 (geo-blocked). For CEX context, OKX swaps did ≈$21.1B/24h (estimate).
  - Sources: [Variational stats API](https://omni-client-api.prod.ap-northeast-1.variational.io/metadata/stats); [Lighter API](https://mainnet.zklighter.elliot.ai/api/v1/orderBookDetails); [Aster API](https://fapi.asterdex.com/fapi/v1/ticker/24hr); [Extended API](https://api.starknet.extended.exchange/api/v1/info/markets); [Paradex API](https://api.prod.paradex.trade/v1/markets/summary?market=ALL); [OKX API](https://www.okx.com/api/v5/market/tickers?instType=SWAP).
- **Castle Labs (2026-10-14).** Hyperliquid had **≈57% of on-chain perp OI ($7.77B)**, Aster 9.6%, Variational 7.9%, Lighter 5.4% (including Robinhood Chain perps). By 24h volume: HL ≈36%, Variational 16%, Lighter 11%, Aster 8.5% — [Castle Labs, via search](https://castlelabs.io/research/perp-dex-rankings). The HL volume share differs from mine because of methodology (HIP-3 inclusion and venue set).
- **Share trend over 2025–2026.**
  - HL went above 40% volume share in June 2026, for the first time since Sep 2025. Its 30d volume was ~$203B vs Aster and Variational ~$63B each and Lighter ~$55B — [Blockonomi, via search](https://blockonomi.com/dex-statistics-2026-volume-market-share-and-perp-data).
  - August 2026: HL had 58% of the top-8 perp DEXs — [CryptoBriefing, via search](https://cryptobriefing.com/hyperliquid-perp-dex-market-share/).
  - Late 2025: Aster reportedly took ~70% in Sep 2025 (disputed as incentive-driven), and by Nov 2025 HL was ~20% vs Lighter 27.7% — [search summary of BlockEden and others](https://blockeden.xyz/blog/2026/01/29/perp-dex-wars-2026-hyperliquid-lighter-aster-edgex-paradex-decentralized-derivatives/).
- **Incidents in 2026.**
  - **2026-04-09 Fartcoin self-liquidation attack.** About $15M notional was built across 4 wallets and force-liquidated into HLP via auto-deleveraging. HLP took ≈$1.5M realized loss (≈$3M book) within 24h. PeckShield links the actor to an earlier XPL manipulation. Sources: [Journal du Coin](https://journalducoin.com/defi/hyperliquid-vault-hlp-part-en-fumee-sur-le-fartcoin-15-million-sevaporent/); [CoinAcademy](https://coinacademy.fr/actu/hyperliquid-1-5-million-dollars-perdus-attaque-suicide-fartcoin/).
  - HLP TVL fell from $603.9M (Sep 2025) to ~$268.6M (Jun 2026) per CoinGecko; another snapshot says $420M (conflict) — [CoinGecko Learn, via search](https://www.coingecko.com/learn/hyperliquid-hlp-vault-analysis).
  - No 2026 validator outage was found.
- **Price performance (HL daily closes, [Hyperliquid info API candleSnapshot](https://api.hyperliquid.xyz/info)):**
  - HYPE: 2025-12-31 close 25.45; 2026 low **20.46 (2026-01-21)**; 2026-07-01 close 62.34; Aug 2 low 51.08; **ATH 97.999 (2026-09-23)**; 30d low 77.44 (2026-10-15); now 79.86.
  - YTD: **HYPE +213.8% vs BTC −7.0%, SOL −16.1%, ETH −18.4%**.
  - Since 2026-07-01: **HYPE +28.1% vs BTC +35.8%, ETH +50.7%, SOL +35.0%, LIT +54.6%**.
  - Since 2026-09-24: HYPE −13.3% vs BTC −3.4%.
  - CoinGecko ATH is $97.96 (2026-09-23 05:16 UTC) — [CoinGecko API](https://api.coingecko.com/api/v3/coins/hyperliquid).
- **Polymarket HYPE ladder (by 2026-12-31, snapshot), from [Polymarket gamma API](https://gamma-api.polymarket.com/public-search?q=hyperliquid):**
  - Reach $100: **45%** ($720k volume); a second market ("hit $100 by Dec 31") shows 38.5%. Reach $110: 24.5%; $120: 13%; $150: 6.5%; $200: 3.2%.
  - Dip to $75: 75.7% (wide bid/ask 0.668/0.845); **$70: 54.5%; $65: 48.5%; $60: 35.5%**; $50: 11.5%; $40: 5.1%.
- **Bull vs bear evidence (from the data above).**
  - Bull: record-level September fees, buyback ≈$2.4M/day, PURR accumulation, Robinhood US perps listing HYPE, HIP-3 ≈36% of volume, and on-chain OI share ≈57%.
  - Bear: 30d fees −15%, team OTC tranche plus a nominal 9.9M/month schedule, ETF outflows, HIP-3 concentration in one deployer, FDV/revenue ≈88x, and underperformance vs BTC since July.

### Inferences
- **The trader's resting bids.**
  - HYPE 30@74 is about 4.4% below the 30d low (77.44). Polymarket prices a dip to $75 before year-end at ~76% and to $70 at ~55%, so the 74 bid has a better-than-even chance of filling by year-end and the 69 bid is roughly a coin flip.
  - Both are 2x cross perps. The 69 level is about 35% above the August swing low (51.08), which is where a bear scenario could take price (Polymarket: 11.5% for $50).
- **HIP-3 risk concentration.** HIP-3 is a real growth leg, now mostly equity-index and commodity perps, but the dependency on one deployer (trade.xyz) is extreme. The wave of fully delisted builder dexes implies the long tail of HIP-3 builders has not been economically viable.
- **Allocation implication.** On fundamentals and liquidity HYPE is the only "core-able" asset of the four. HYPE has been a high-beta follower of BTC since July rather than a leader, so a core position mainly depends on the BTC leg up resuming and fees re-accelerating.

### Gaps
- No named, dated sell-side or analyst bull/bear pieces on HYPE were retrieved this pass. A DefiLlama "HYPE metrics bullish/bearish thesis" dashboard exists but was not opened — [DefiLlama](https://defillama.com/pro/hype-metrics-bullish-bearish-thesis-ps8lt0).
- HyperEVM activity (TVL, gas) was not pulled.
- Why Felix, Ventuals, HyENA and dreamcash were delisted was not researched.
- No 30/90-day DefiLlama derivatives-volume series: the API returned **HTTP 402**, so the share trend relies on third-party snapshots.

## Q4. LIT (Lighter): business trend, revenue/buyback, supply and the cliff, the Robinhood shock, catalysts

### Takeaway
LIT is a **~$800M-mcap / $3.2B-FDV** token with only 25% of supply circulating. The business recovered from a spring trough: **fees 90d +51%** vs the prior 90 days, but **30d fees are flat at $5.9M** and **30d buybacks are $2.77M (−16%) ≈0.35% of mcap**. The insider 50% (500M LIT) unlocks over 3 years after a 1-year cliff. **500M/156 weeks = 3.2M LIT/week (≈13.9M/month ≈5.6% of today's circulating supply per month), about 20x the current monthly buyback.** The first post-cliff date is **2026-12-27 per Tokenomist, or 2027-01-28 (13.5M) per Tokenomics.com**. Robinhood choosing Bitstamp for US perps (2026-09-30) knocked ~20% off LIT within a day. LIT is now **−42.6% from its 2026 high of $5.59** and −36.7% from the Sep 24 close.

### Cited Findings
- **What Lighter is.** An Ethereum-based perp DEX; DefiLlama TVL is **$629.6M on Ethereum + $111.5M on "Robinhood Chain"** (+$2.1k on Arbitrum) — [DefiLlama protocol API – lighter](https://api.llama.fi/protocol/lighter).
  - Robinhood joined Lighter's **$68M Series B (2025)**. In mid-2026 Lighter integrated with **Robinhood Wallet** for perps and stock tokens, mainly for non-US users — [KuCoin/Odaily, 2026-09-30](https://www.kucoin.com/news/flash/lighter-s-token-dips-20-as-robinhood-announces-bitstamp-futures-expansion).
  - LIT ("Lighter Infrastructure Token") was announced on 2025-12-30 — [search summary](https://iranbroker.net/news/decentralized-exchange-lighter-introduces-lit-token/).
- **Volume and OI now.** Lighter API snapshot:
  - 239 markets, **24h volume $1.854B**, OI ≈$534M (sum of OI × last price). BTC $886M and ETH $425M dominate.
  - The LIT market itself: $17.8M volume, $34.4M OI.
  - Source: [Lighter API orderBookDetails](https://mainnet.zklighter.elliot.ai/api/v1/orderBookDetails).
  - Castle Labs (10-14) shares: **11% of 24h on-chain perp volume, 5.4% of OI** — [Castle Labs](https://castlelabs.io/research/perp-dex-rankings). My snapshot: 11.8% (Q3).
  - Mid-2026 30d volume ≈$55B — [Blockonomi](https://blockonomi.com/dex-statistics-2026-volume-market-share-and-perp-data).
- **Fees and revenue trend (DefiLlama):**
  - Monthly fees: Nov 2025 $18.09M (peak); Jan 2026 $9.00M; Mar $3.83M; Apr $2.81M; May $2.85M; Jun $3.90M; Jul $2.83M; **Aug $4.33M; Sep $5.29M**; Oct 1–16 $3.23M (pace ≈$6M).
  - **30d fees $5.94M vs $5.97M prior; 90d $14.13M vs $9.34M (+51%).**
  - **Revenue 30d $4.90M**, prior 30d $4.58M.
  - Source: [DefiLlama fees API – lighter](https://api.llama.fi/summary/fees/lighter?dataType=dailyFees).
- **Buyback.** DefiLlama "holders revenue" (the buyback):
  - **30d $2.77M** (prior 30d $3.28M); Sep $2.66M; Oct 1–16 $1.47M; Jan 2026 $6.71M; **cumulative since Jan 2026 $30.5M**.
  - At the 30d LIT VWAP of $4.13, 30d buybacks ≈ **0.67M LIT = 0.35% of mcap (~4.2% annualized)**.
  - Source: [DefiLlama fees API – lighter holders revenue](https://api.llama.fi/summary/fees/lighter?dataType=dailyHoldersRevenue).
  - The Tokenomist article title calls it "a real burn", but its body was not retrievable (HTTP 403) — [Tokenomist](https://tokenomist.ai/research/lighter-lit-tokenomics-robinhood-hype-a-real-burn-and-the-december-2026-cliff-2).
- **Supply and valuation.**
  - Circulating **250M / total 1B**; price $3.20; **mcap $801M; FDV $3.205B**; 24h volume $75.8M; 30d −32.7%; 60d +39.7%.
  - CoinGecko ATH **$7.86 on 2025-12-30 (TGE day)**; ATL $0.779 on 2026-03-31.
  - Source: [CoinGecko API – lighter](https://api.coingecko.com/api/v3/coins/lighter).
  - Multiples (calculation): mcap/annualized revenue ≈13.4x; FDV/revenue ≈53.7x.
- **Unlock schedule.**
  - Team 26% + investors 24% (500M LIT) have "a 1-year unlock and 3-year linear vesting after" (Lighter, quoted) — [Cointelegraph, via search](https://cointelegraph.com/news/lighter-lit-tokenomics-split-community-reaction).
  - Tokenomist: **cliff 2026-12-27**, vesting to about late Dec 2029 — [Tokenomist, via search](https://tokenomist.ai/research/lighter-lit-tokenomics-robinhood-hype-a-real-burn-and-the-december-2026-cliff-2).
  - **Conflict:** Tokenomics.com lists TGE 2025-12-30 and a **next unlock on 2027-01-28 of ≈13.5M LIT**, with 36 unlock events to 2030-01-28 — [Tokenomics.com, via search](https://app.tokenomics.com/tokenomics/lighter/unlocks).
  - The 25% ecosystem/reserve bucket has **no published schedule** (same sources).
- **Unlock math (calculation).** 500M/156 weeks = **3.205M LIT/week**, matching the "~3.2M/week" in the brief. On a monthly cadence that is 500M/36 = **13.9M LIT/month ≈5.6% of circulating per month**, ≈$44M/month at $3.20. The current buyback covers ≈4.8% of that.
- **The Robinhood shock (2026-09-30).** Per [KuCoin/Odaily](https://www.kucoin.com/news/flash/lighter-s-token-dips-20-as-robinhood-announces-bitstamp-futures-expansion):
  - At its annual event, Robinhood said US perps will go through **Bitstamp** (acquired in 2025 for $200M): BTC, ETH, SOL, XRP, DOGE, ADA, LINK and HYPE, at 10x for BTC/ETH and 3x for the rest. No launch date was given.
  - **LIT fell "nearly 20%"** short term.
  - Lighter still powers Robinhood Wallet perps and no termination has been announced. Lighter lacks the US licenses it would need; a DCM designation would be key; founder Vladimir Novakovski has discussed pursuing US approvals.
  - Other tallies: −22% over 7 days ([The Defiant](https://thedefiant.io/news/defi/lighter-token-drops-after-robinhood-perps-plan)) and −26% over 7 days ([CoinStats](https://coinstats.app/news/862f635adac703612bded0657740285faa38ad367870d8db4dda80ca6f1cd7c3_Lighter-crypto-price-drop-reaches-26-as-Robinhood-turns-to-Bitstamp-for-US-perps)).
- **Price path (HL LIT perp daily, [Hyperliquid info API](https://api.hyperliquid.xyz/info)):**
  - **2026 high 5.5858 (intraday 2026-09-24)**; Sep 24 close 5.068; Sep 29 close 3.934; Oct 3 close 3.566; Oct 5 close 4.022 (bounce); **30d low 2.8947 (2026-10-15)**; now 3.207.
  - **−42.6% from the high; −36.7% from the Sep 24 close**; YTD +28.6%; since Jul 1 +54.6%.
  - The "$5.59 ATH" is the HL-perp/2026 high. CoinGecko's ATH is $7.86 (TGE day).
- **LIT perp positioning on HL (snapshot).**
  - OI 41.46M LIT (**$133M**). Funding −12.7% APR at the snapshot; 30d average +14.1% APR, 7d average +10.9%. 24h volume $22.5M; max leverage 5x.
  - Book within ±2% (aggregated): bid $693k / ask $997k.
  - Source: [Hyperliquid info API](https://api.hyperliquid.xyz/info).
- **Polymarket LIT (before 2027, snapshot):** reach $6: **32%**; $8: 9.2%; $10: 6.3% ($149k volume); $12: 3.65%. **Dip to $2.5: 51.5%; dip to $2: 24.5%** — [Polymarket gamma API](https://gamma-api.polymarket.com/public-search?q=lighter).
- **Analyst view.** The KuCoin/Odaily author calls buying now "catching a falling knife" and suggests waiting for regulatory progress or a deeper Robinhood collaboration. The same author says concluding that Robinhood will abandon Lighter is an overinterpretation — [KuCoin/Odaily](https://www.kucoin.com/news/flash/lighter-s-token-dips-20-as-robinhood-announces-bitstamp-futures-expansion).

### Inferences
- **The trader's LIT 550@2.6999 bid.** It sits about 7% below the 30d low (2.8947). Polymarket prices a dip to $2.5 before 2027 at ~51.5%, so a fill before year-end is better than a coin flip. The order is a 2x cross perp on a token with a dated supply event roughly 10 weeks away (Dec 27 or Jan 28), so the window to hold it is short.
- **Dilution vs buyback.** Post-cliff dilution of ~5.6% of float per month dwarfs the ~0.35%/month buyback. The pre-cliff window (now to about Dec 20) is where LIT can trade on beta and catalysts. Holding through the cliff needs a demand story (US licensing, a Robinhood Chain expansion) that is not on any public calendar.
- **Sizing.** LIT looks like a satellite or tactical position (high beta, positive 90d business trend, Robinhood optionality) with a time stop before the cliff, not a core position.

### Gaps
- **No LIT catalysts dated for Oct 2026–Q1 2027** (listings, product launches, fee changes) were found. A news search returned nothing newer than the Sep 30 Robinhood story.
- The exact cliff date and cadence (Dec 27 weekly vs Jan 28 monthly) are unresolved, and the official Lighter docs were not fetched.
- Aug–Oct 2026 daily volume and OI series for Lighter were unavailable (the DefiLlama derivatives API is paywalled). Only the current snapshot and the fee trend (a proxy) are available.
- Lighter's role on "Robinhood Chain" was not verified beyond DefiLlama's chain TVL and Castle Labs' note.

## Q5. KNTQ (Kinetiq): update of the 2026-10-03 report

### Takeaway
**The S2 claim ended at 67.4% take-up** (33.71M of 50M KNTQ, ≈$8.81M USDC). This is at the top of the earlier report's 55–70% range; the tracker's ~50% linear projection was too low because the deadline rush happened. On **2026-10-12** the Foundation swept the **16.29M unclaimed KNTQ back to the growth wallet** and the **$8.81M USDC to an unlabeled contract**. Price spiked to **0.385 intraday / 0.3717 close on 10-11**, hitting the report's T1 and T2 zones, then faded to **0.311**. The fundamental base kept shrinking: **Kinetiq HYPE −8.7% in 14 days to 11.33M HYPE (TVL $940M)**, sKNTQ −9.7%, and October revenue running at ~60% of September's pace. Team and investor wallets (310M) are still untouched, about 6 weeks before the 2026-11-27 cliff.

### Cited Findings
- **S2 claim result (on-chain, read 2026-10-17 03:30 UTC, block 48,750,364).**
  - The claim contract `0x435b…c03b` now holds 0 KNTQ and 0 USDC.
  - `Withdrawn` events moved 100 + **16,289,438.96 KNTQ to growth wallet `0x5bd9…aae4`** (blocks 48,301,608 and 48,302,749, **2026-10-12 00:54 and 01:12 UTC**).
  - They also moved 100 + **8,809,488.50 USDC to `0x64bd77698ab7c3fd0a1f54497b228ed7a02098e3`** (a contract, not an EOA) at **01:35 and 01:53 UTC**.
  - Implied claimed amount: **33,710,461 KNTQ = 67.42%**. Cross-check: 33.71M × 0.261331 = $8.8096M, which matches the USDC swept.
  - Source: [HyperEVM RPC (rpc.purroofgroup.com)](https://rpc.purroofgroup.com).
  - The last tracker row (2026-10-04 08:08 UTC) showed 22,171,333 claimed (44.34%), so **≈11.54M KNTQ (≈$3.0M) was claimed in the final ~7 days** — [local tracker `/home/user/test-claude/kntq-s2-tracker/snapshots.csv`](https://rpc.purroofgroup.com).
- **Allocation wallets (same read).**
  - **Team 235,000,000; investors 75,000,000; foundation 100,000,000 — unchanged since TGE.**
  - Growth **265,539,538.96**. That is 250M + 16.29M returned − **exactly 750,000 moved out** to an unidentified destination.
  - Liquidity 9,476,666.43, up from 4,523,810 on Oct 3.
  - Source: [HyperEVM RPC](https://rpc.purroofgroup.com).
- **Price.**
  - HL @334 mid **0.3114** (snapshot). Daily closes: Oct 3 0.3046; **Oct 8 0.2868** (lowest close); Oct 10 0.2988; **Oct 11 0.3717** (deadline day, +24%); Oct 12 0.3333; Oct 14 0.3061; Oct 17 0.3115.
  - **Intraday range since Oct 4: 0.26771–0.385.** 30d VWAP 0.3195.
  - Source: [Hyperliquid info API candleSnapshot @334](https://api.hyperliquid.xyz/info).
  - CoinGecko: mcap **$98.0M** (circulating 315.0M, up from 280.5M on Oct 3 as claimed tokens entered circulation), **FDV $311M**, 24h volume $2.27M, 7d +7.5%, 30d +56% — [CoinGecko API – kinetiq](https://api.coingecko.com/api/v3/coins/kinetiq).
- **Kinetiq TVL and staking (DefiLlama tokens).**
  - **HYPE 11,332,364 + WHYPE 455,207 on 2026-10-17**, vs 12,407,459 + 466,131 on Oct 3 and 15,096,683 + 671,184 on Jul 17. That is **−8.7% in 14 days and −24.9% in 90 days** in HYPE terms. TVL is **$939.8M**.
  - sKNTQ staked: **68.44M KNTQ** vs 75.8M on Oct 3 (−9.7%).
  - Source: [DefiLlama protocol API – kinetiq](https://api.llama.fi/protocol/kinetiq).
- **Revenue (DefiLlama).**
  - Fees 30d **$1.91M** vs prior 30d $2.36M (−19%). **Revenue 30d $332.5k** vs $424.8k (−22%). Holders revenue 30d $135.7k.
  - **Oct 1–17 revenue $138.7k vs September $424.2k**, a ~$250k/month pace (partial month, so flag as provisional).
  - Source: [DefiLlama fees API – kinetiq](https://api.llama.fi/summary/fees/kinetiq?dataType=dailyRevenue).
- **Buybacks.** The Assistance Fund holds **4,222,452 KNTQ** (entry notional $913k, average ≈$0.216), vs 3,988,286 on Oct 3. That is +234k KNTQ in ~13 days ≈ **17.7k KNTQ/day (~$5.5k/day)**, and 0.42% of supply cumulatively — [Hyperliquid info API spotClearinghouseState](https://api.hyperliquid.xyz/info).
- **HIP-3 "exchange-as-a-service" (Markets by Kinetiq, `mkts`).** **5 live of 24 markets**, 24h volume **$6.44M** (USBOND $3.50M, USTECH $2.02M, US500 $0.54M), OI $9.40M. The older `km` dex has every market delisted — [Hyperliquid info API](https://api.hyperliquid.xyz/info).
- **HL spot liquidity (KNTQ/USDC @334, snapshot).**
  - Within ±2% (aggregated book): **bid $59.2k / ask $53.1k**. Within ±5%: $125k / $111k. Within ±10%: $220k / $205k.
  - Top 20 full-precision levels: $26.3k bid / $23.8k ask within 0.5%.
  - 24h HL spot volume $1.67M.
  - Source: [Hyperliquid info API l2Book](https://api.hyperliquid.xyz/info).
  - For comparison, Oct 3 depth within ±2% was $12.1k bid / $22.6k ask (earlier report, `/home/user/test-claude/reports/Phân tích KNTQ và airdrop S2.md`).
- **Elysium (the key catalyst).**
  - Scheduled for 2026-10-20 per CoinMarketCal — [TradingView/CoinMarketCal](https://www.tradingview.com/news/coinmarketcal:ab9da4724094b:0-kinetiq-elysium-mainnet-launch-brings-its-hyperliquid-l2-live-by-20-oct-2026/).
  - As of ~Oct 2, mainnet was "pre-launch" with no date in Kinetiq's docs, and Chainstack will add mainnet support once Kinetiq confirms the chain ID and date — [Chainstack](https://chainstack.com/what-is-elysium/amp/).
  - Parameters are "still being refined" — [CryptoBriefing](https://cryptobriefing.com/kinetiq-elysium-testnet-hyperliquid/). Launch is described as "imminent" — [Bankless](https://www.bankless.com/read/news/kinetiq-unveils-elysium-l2-for-hyperliquid.md).
- **Unlocks.** The docs state a 1-year cliff and then 2-year monthly linear vesting for core contributors (235M) and investors (75M). Read literally, that implies **≈12.9M KNTQ/month from ~2026-11-27**, held in EOAs with no vesting contract (earlier report).

### Inferences
- **Status vs the earlier report's plan.**
  - The claim overhang is gone (the expiry itself was mechanically positive), and T1/T2 (0.335–0.377) traded on Oct 11.
  - The hard stop (daily close < 0.2550) was not triggered.
  - Two fundamental invalidation lines are now close: Kinetiq TVL ($940M vs the $900M line) and HYPE staked (11.33M vs the ~11M line).
  - The Foundation now holds the $8.81M raise plus the returned 16.29M KNTQ, and has already moved 750k KNTQ out of the growth wallet. That is discretionary supply.
- **Allocation.** KNTQ is not a core or satellite candidate for a 3–6-month plan. At most it is a small event trade around Elysium (Oct 20, unconfirmed), with a mandatory exit before the 2026-11-27 cliff. Depth has improved but is still only about $55–60k within ±2%.

### Gaps
- Elysium mainnet status after Oct 2 is unknown; no confirmation was found.
- The identity of the USDC recipient contract `0x64bd…98e3` and the destination of the 750k KNTQ moved out of the growth wallet were not traced.
- I found no new Kinetiq announcements (Discord/X) for Oct 4–17.

## Q6. Variational: points, TGE timing, valuation, farmability and platform risk

### Takeaway
Variational has announced **VAR for Q4 2026 with no date**:
- **32% to points holders, fully unlocked at TGE.**
- 18% ecosystem.
- 50% team and investors (12-month lock, then ≥3-year linear).
- 100% of treasury revenue to buyback and burn.

**Polymarket's median launch FDV is now ≈$1.2–1.3B**, down slightly from ~$1.34B earlier, with a mean of ≈$1.7B. It prices launch by Nov 30 at 30% and by Dec 31 at ~87% (thin market). Omni is now the **#2 on-chain perp venue by 24h volume ($3.0B, 16–19% share)**, but **57% of that volume is synthetic index and commodity markets**. Points are volume-based (150k/week). At the Polymarket median FDV, my estimate is about **$350 of airdrop per $1M of volume (≈3.5 bps)**, so a $7K trader can farm a few hundred to low-thousands of dollars, with real risk.

### Cited Findings
- **Tokenomics.** Per [CryptoBriefing, 2026-09-23](https://cryptobriefing.com/variational-var-token-launch-airdrop/):
  - TGE in **Q4 2026**, no exact date.
  - **32% airdrop to points holders, fully unlocked at TGE, no cliffs.** Eligibility needs at least 1 point; unclaimed tokens are burned.
  - **50% team and investors**: 12-month lockup, then linear vesting over at least 3 years.
  - **18% ecosystem** (Variational Foundation).
  - **100% of treasury revenue to VAR buybacks and burns.**
  - **150,000 points per week until TGE.**
  - Omni is a zero-fee perps platform on Arbitrum, in private beta, with a public mainnet planned before the token.
  - Funding: **$50M Series A (May 2026, led by Dragonfly; Bain Capital Crypto, Coinbase Ventures)** plus a $10.3M seed.
- **Points timeline.** The program was originally set to end by Q3 2026 (Sep 30). It was extended "because of major strategic partnerships", with weekly 150k distributions continuing to TGE — [Bitrue, via search](https://www.bitrue.com/blog/variational-var-tge). Points distributions began in Dec 2025 — [Medium guide, via search](https://medium.com/@variational-io/variational-airdrop-farm-omni-points-before-var-b369e4724b6f).
- **How points accrue (secondary guides only).**
  - Weekly, by trading volume. Tiers boost multipliers. Referrals count 0.2× referred volume. One guide says swaps earn double — [Medium guide](https://medium.com/@variational-io/variational-airdrop-farm-omni-points-before-var-b369e4724b6f); [Cryptoast](https://cryptoast.fr/variational-comment-etre-eligible-airdrop-crypto/).
  - No source describes OI- or PnL-based points.
- **Loss refunds.** A refund pool is funded from OLP spread revenue. Sources conflict on the share: ~10% of trading revenue vs one-sixth of OLP spread income — [Cryptoast](https://cryptoast.fr/variational-comment-etre-eligible-airdrop-crypto/); [search summary](https://alearesearch.substack.com/p/variational).
  - **The live API shows `loss_refund.pool_size = 0` and `refunded_24h = 0`** — [Variational stats API, snapshot](https://omni-client-api.prod.ap-northeast-1.variational.io/metadata/stats).
- **Platform metrics (snapshot, same API).**
  - 24h volume **$3.023B**, cumulative $419.1B, TVL **$238.5M**, OI **$1.99B**, 575 markets.
  - Top markets by 24h volume: US100S $940M, BTC $468M, ETH $393M, US500S $318M, US30S $262M, XAUS $129M. Synthetic index/commodity tickers are **57.0% of 24h volume**.
  - Quoted base spreads: BTC 1.48 bps, ETH 1.12 bps, HYPE 0.91 bps, SOL 2.69 bps.
- **Market position.** Castle Labs (10-14): **16% of on-chain perp volume and 7.9% of OI** — [Castle Labs](https://castlelabs.io/research/perp-dex-rankings). My 6-venue snapshot: 19.3% (Q3).
- **Polymarket "Variational FDV above X one day after launch" (snapshot, $3.55M total volume).**
  - Thresholds: $100M **98.35%**; $200M 98.1%; $300M 93.1%; **$500M 86.5%; $800M 72.5%; $1B 58.5%; $2B 27.75%**; $3B 13.6%; $4B 6.85%; $5B 3.0%.
  - Source: [Polymarket gamma API](https://gamma-api.polymarket.com/events?slug=variational-fdv-above-one-day-after-launch).
  - Implied **median ≈$1.21B (log-linear) to $1.28B (linear); mean ≈$1.69B** (trapezoid, crude tail). These are calculations.
- **Polymarket launch-timing markets.**
  - By Oct 31, 2026: **4.75%**. By Nov 30: **30%** (bid 0.29 / ask 0.31). By Dec 31: **86.55%** (bid 0.831 / ask 0.90; only $1.7k liquidity).
  - Source: [Polymarket gamma API search](https://gamma-api.polymarket.com/public-search?q=variational).
- **Peer multiples (calculation, CoinGecko FDV / 24h volume).** Lighter $3.20B FDV / $1.85B ≈ 1.7x; Aster $5.50B / $1.42B ≈ 3.9x. Variational at a $1.25B FDV / $3.02B ≈ 0.4x — [CoinGecko API](https://api.coingecko.com/api/v3/coins/lighter).
- **Farming math (my estimate, assumptions stated).**
  - Weekly volume ≈ 7 × $3.02B ≈ $21.2B, so 150k points/week ≈ **7.1 points per $1M of volume**, assuming points are pro-rata to volume.
  - Assumed total points by TGE ≈ 54 weeks × 150k ≈ 8.1M, with 32% of supply to points.
  - Airdrop value per $1M of volume: **$197 at the earlier $705M model FDV**, **$350 at the $1.25B Polymarket median**, $476 at the $1.7B mean.
  - Cost side: crossing a ~1.1–1.5 bp BTC/ETH spread once per round trip costs ≈$55–75 per $1M of volume (calculation from the API spreads).

### Inferences
- **Farmability for a ~$7K account at 2x.**
  - $14k notional means a round trip is about $28k of volume, so $1M takes about 36 round trips.
  - Over a plausible 6–10 weeks to TGE, $1–3M of volume could yield roughly $350–1,000 at the median FDV, net of a few hundred dollars of spread.
  - That is meaningful relative to $7K but not transformative. Directional PnL variance and the possibility that tiers, referrals or sybil filters dilute pro-rata math dominate the outcome.
  - The empty loss-refund pool removes the cushion that guides advertise.
- **Valuation vs Polymarket.** Variational's volume share has run well ahead of its OI and TVL. The heavy synthetic-index volume looks partly incentive-driven, so post-TGE volume could normalize, as happened at Aster and Lighter. That argues for treating the Polymarket median (~$1.2B) as optimistic relative to the earlier $705M model. The gap has narrowed from ~1.9x to ~1.7x because Polymarket's median fell.
- **Timing.** Nov 30 at 30% vs Dec 31 at ~87% implies the market expects a December TGE.
- **Sizing.** Variational is a small farming sleeve at most, not an allocation. A $7K account should not lock collateral it needs for the HYPE/LIT plan.

### Gaps
- The official points formula (volume vs OI/PnL weighting, tiers, sybil rules) was not verified from Variational docs. All accrual detail comes from secondary guides.
- **Platform-risk items from earlier work on this account were not re-verified this pass:** OLP as sole counterparty is supported by guides, but the all-or-nothing limit fills and order expiry were not checked.
- No pre-market (e.g., Aevo/Whales/Hyperliquid pre-launch) price for VAR was found.
- Total VAR supply has not been published.

## Q7. Other perp-DEX tokens and airdrops (Aster, edgeX, Paradex, Extended): status relevant to a 3–6-month plan

### Takeaway
None of these looks like an aggressive-plan buy on current data.
- **ASTER** is a large ($1.9B mcap / $5.5B FDV) range-bound token with fees down 28% over 30 days.
- **EDGE** (edgeX) is −50% in 30 days with fees collapsing.
- **DIME** (Paradex) is a micro-cap whose exchange volume has almost vanished.
- **Extended** has real volume (~$0.5B/day) and no token found, which makes it the only airdrop-optionality name. Its status is unverified.

### Cited Findings
- **ASTER.**
  - $0.705, mcap **$1.91B**, FDV **$5.50B**, 30d −1.3%, 1y −44.5%, ATH $2.41 (2025-09-24) — [CoinGecko API – aster-2](https://api.coingecko.com/api/v3/coins/aster-2).
  - HL perp YTD +1.8%; 2026 range 0.404–0.870 — [Hyperliquid info API](https://api.hyperliquid.xyz/info).
  - Fees 30d **$4.79M vs $6.69M prior (−28%)**; holders revenue 30d $3.13M — [DefiLlama fees API – aster](https://api.llama.fi/summary/fees/aster?dataType=dailyFees).
  - 24h volume $1.42B — [Aster API](https://fapi.asterdex.com/fapi/v1/ticker/24hr). OI share 9.6% — [Castle Labs](https://castlelabs.io/research/perp-dex-rankings).
- **edgeX (EDGE).**
  - $0.306, mcap $107M, FDV $305M, **ATH $1.54 (2026-05-22)**, ATL $0.237 (2026-07-05), 7d −19%, **30d −49.9%** — [CoinGecko API – edgex](https://api.coingecko.com/api/v3/coins/edgex).
  - Fees 30d $3.22M vs $5.09M prior; 90d $11.4M vs $27.7M — [DefiLlama fees API – edgex](https://api.llama.fi/summary/fees/edgex?dataType=dailyFees).
  - The edgeX public API returned 503 at the snapshot.
- **Paradex (DIME).**
  - $0.0525, mcap $9.8M, FDV $52.5M, ATH $0.102 (2026-10-11), 30d +216%, 24h volume $35k — [CoinGecko API – paradex](https://api.coingecko.com/api/v3/coins/paradex).
  - Exchange 24h volume **$14.2M** — [Paradex API](https://api.prod.paradex.trade/v1/markets/summary?market=ALL). Fees 30d $54.8k — [DefiLlama](https://api.llama.fi/summary/fees/paradex?dataType=dailyFees).
- **Extended.**
  - 24h volume **$487M**, OI $188M, 407 markets — [Extended API](https://api.starknet.extended.exchange/api/v1/info/markets).
  - Fees 30d $1.49M (−19%); monthly fees ~$1.6M since July — [DefiLlama fees API – extended](https://api.llama.fi/summary/fees/extended?dataType=dailyFees).
  - No token on CoinGecko was checked or found.

### Inferences
- For a ~$6.4K altcoin sleeve, the perp-DEX token set ranks roughly HYPE > LIT (tactical, pre-cliff) > Variational farm (small) > KNTQ (event-only) > others (skip). The alternative-airdrop slot, if any, is Extended. That is a lead to verify, not a recommendation.

### Gaps
- No current status was gathered on Extended, GRVT or edgeX points/TGE programs, or on ASTER's buyback and unlock schedule. These were skipped as lower priority under the time budget.
