# Base rates, market regime, mechanisms and methodological traps: do newly launched tokens (especially perp DEX tokens) trade above their TGE valuation at some point after launch? (TGEs Oct 2023 – Oct 2026)

Scope note: this file covers the broad reference class, sector context, market regime, mechanisms and method traps. Per-token perp DEX data (TGE FDV, peak FDV, dates) is being built by other researchers. Today is 27 Oct 2026. "Secondary" means I could only reach press coverage of a study, not the study itself. Where I could not open a page, the claim rests on search-result summaries, and I say so.

---

## Q1. Base rates: how do 2024–2026 token launches perform vs their TGE price/valuation, how often do they EVER exceed it, when do they peak, and does a lower launch FDV predict a better outcome?

### Takeaway
Every large 2024–2026 study finds that about 80–93% of new tokens trade below their TGE or listing price months later (medians of roughly −70% to −96%). Peaks come early: 37% of 2024 CEX listings set their all-time high on listing day and never beat it. The only study with launch-FDV buckets (Memento Research, 2025 launches) shows a steep, consistent gradient. Launches at $25–200M FDV were 40% green with a median of −26%; launches at ≥$1B FDV were 0% green. Perp DEX was the best category in that sample (N=3, 33% green), and HYPE is the single best performer among 113 large 2024+ launches (+1,519%). However, **no study I found measures the user's metric, the MAXIMUM post-TGE FDV vs TGE FDV, by launch-FDV bucket**. All published base rates measure the end-point value, which is only a lower bound for "ever above TGE."

### Cited Findings

#### A. General token-launch evidence (all sectors)

**Memento Research, 2025 launches (the key study for the user's hypothesis)**
- Sample and metric: 118 token launches in 2025. The metric is the % change from "TGE opening" to the data date (20 Dec 2025), measured on FDV and market cap. Exchange or inclusion criteria and the exact "opening" timestamp are not stated. The page metadata shows 19 Jul 2026, but the data is as of 20 Dec 2025. — [Memento Research, "State of 2025 Token Launches: Year-in Review"](https://mementoresearch.com/state-of-2025-token-launches-year-in-review)
- Headline results: 84.7% (100/118) were below their TGE valuation and 15.3% (18/118) were green. Median FDV change was −71.1% and median market-cap change −66.8%. An equal-weighted FDV basket returned about −33.3%, while an FDV-weighted basket returned −61.5%. The median green token was +109.7% (~2.1x) and the median red token −76.8%. 65% of launches were down ≥50%. — [Memento Research](https://mementoresearch.com/state-of-2025-token-launches-year-in-review)
- **Launch-FDV buckets (Memento calls them "quartiles," but they are uneven):**

  | Starting FDV bucket | N | Median starting FDV | Median FDV change (to 20 Dec 2025) | % green |
  |---|---|---|---|---|
  | $25m – $200m | 35 | ~$126m | −26% | 40% |
  | $210m – $489.1m | 24 | ~$335m | −73% | 13% |
  | $500m – $940m | 29 | ~$680m | −82% | 3% |
  | $957.6m – $28.1b | 30 | ~$1.58b | −83% | 0.0% |

  Launches with starting FDV ≥$1B: 28, of which 0% were green, with a median of about −81%. — [Memento Research](https://mementoresearch.com/state-of-2025-token-launches-year-in-review)
- By category (N / median FDV change / % green): Infra 46 / −72% / 9%; AI 23 / −82% / 13%; DeFi 19 / −52% / 32%; Consumer 14 / −61% / 14%; Gaming 6 / −86% / 17%; Stablecoin 4 / −77% / 0%; **Perp DEX 3 / −31% / 33%, with an average of +213%**; Data 2 / +0.7% / 50%. — [Memento Research](https://mementoresearch.com/state-of-2025-token-launches-year-in-review)
- Ash (@ahboyash, Memento Research) first posted the study on X on 20 Dec 2025 ("2025 token launches have mostly been a bloodbath"). Examples of start FDV → FDV around 20 Dec 2025: Berachain $4.46B → $305M (−93.2%); Plasma XPL $12.97B → $1.31B (−89.9%); Falcon Finance $6.7B → $949.7M (−85.8%); Mira $1.4B → $125.4M (−91.1%); Syndicate $940M → $59.8M (−93.6%). — [crypto.news, 21 Dec 2025](https://crypto.news/new-crypto-tokens-failing-in-2025-85-below-tge-prices/); [original X post](https://x.com/ahboyash/status/2002363360327704834)
- The Defiant headlined the study "Token Launches With Low FDVs Vastly Outperformed Hyped Debuts in 2025." The article body would not load for me. — [The Defiant](https://thedefiant.io/news/research-and-opinion/token-launches-with-low-fdvs-vastly-outperformed-hyped-debuts-in-2025-memento-research)

**Other 2025-launch studies**
- DWF Labs used Memento Research data and found that more than 80% of 2025 launches trade below their TGE price. Typical drawdowns were 50–70% within about 90 days of listing. Managing partner Andrei Grachev said "most tokens reach a price peak within the first month." The report's date is not confirmed; coverage dates from early 2026. — [Whale Alert summary of DWF Labs report](https://whale-alert.io/stories/ca8d01157f6a5c/DWF-Labs-80-of-2025-Tokens-Trade-Below-TGE-Institutional-Capital-Rotating-into-Public-Crypto-Stocks-and-Infrastructure)
- Airdrops.com (18 Feb 2026) credits Galaxy Research with the claim that "roughly 85% of tokens launched in 2025 are now trading below their TGE price." It links only to Galaxy's general insights index and gives no sample, so I treat this as unverified and probably an echo of Memento. — [Airdrops.com](https://airdrops.com/news/85-of-2025-crypto-tokens-now-trade-below-tge-as-sell-off-deepens)
- Messari simulated buying $100 of each of the 92 non-stablecoin tokens listed on Binance spot in 2025 at the day-one close. The $9,200 portfolio was worth about $2,600 by March 2026 (−71% at portfolio level). Temporary recoveries during stronger market periods faded later in 2025. — [AMBCrypto, 10 Mar 2026](https://ambcrypto.com/messari-data-shows-binances-2025-listings-down-71-on-average/)
- A separate analyst review of 27 Binance listings from 2025 found only 3 with positive returns (FORM, RED, LAYER). The other 24 averaged −44%, with BIO at −90.9% and COOKIE at −82.0%. Measurement date not captured. — [BeInCrypto](https://beincrypto.com/binance-listed-tokens-negative-return)

**Studies extending into 2026**
- **Delphi Digital, "State of Token Markets," reported 13 Jun 2026.** The French article calls the author "Delphi Consulting" but links to members.delphidigital.io.
  - Sample: 652 listings on five CEXs from Jan 2025 to end-May 2026: Binance 51, Kraken 111, Coinbase 41, Bybit 101, Gate.io 348.
  - Method: $1,000 per token on listing day, using CoinGecko daily closes, fees included, measured to 29 May 2026.
  - Results: median −82%; 52% lost >80%; **only 12% in profit**.
  - Portfolio returns by exchange: Binance −74%, Kraken −59%, Coinbase and Bybit about −56 to −57%, Gate.io −42% (but 88% of Gate tokens lost money).
  - Only 26 Gate.io listings had data through the end date. The rest dropped out when data stopped after a collapse or illiquidity, which is survivorship in reverse.
  - Source: [Journal du Coin](https://journalducoin.com/exchanges/listings-crypto-cex-2025-investisseurs-particuliers-50-cents-dollar-investi/)
  - Per ChainCatcher's summary, the same study blames unlocks, poor routing of revenue to holders, and airdrops used as exit liquidity. It also says a revenue-weighted basket of top protocol tokens with fee switches rose about 30% over the same period. — [ChainCatcher](https://www.chaincatcher.com/en/article/2270245)
- **CryptoRank, published 21 Jul 2026.** Sample: 113 tokens launched since 2024, **restricted to projects with market cap >$100M as of 21 Jul 2026**. Results: only 8 (7.1%) above TGE price, with a reported median return of −95.7%. Named winners: HYPE +1,519%, ONDO +101.4%, EVA +20.3%, NIGHT +16.5%. The other four winners were not named. Causes cited: "sell-offs, thin liquidity, and regulatory uncertainty." — [CryptoPotato](https://cryptopotato.com/the-harsh-reality-of-new-crypto-just-7-of-major-tokens-beat-their-launch-price/); [Cryptoast](https://cryptoast.fr/seules-8-cryptos-lancees-depuis-2024-restent-rentables-pour-les-premiers-acheteurs/)
- **CoinGecko 2026 spot CEX report (secondary; summary dated 9 Apr 2026).**
  - Across the top 12 CEXs, about 32% of new listings were positive after 30 days.
  - After 12 months, "fewer than 10%" were above their initial listing price on most top exchanges.
  - Upbit had 67% green at 30 days, but every Upbit listing was below its listing price by days 300–329.
  - Coinbase listings "caught a second wind" after month 6.
  - Source: [CoinSpectator](https://coinspectator.com/mainstream/2026/04/09/90-of-tokens-listed-on-major-cexs-fell-below-their-listing-price-within-1-year-the-odds-are-heavily-against-buying-new-tokens/)

**When does the peak happen? (closest available evidence on "ATH on or near listing day")**
- **CryptoNinjas × Storible, 389 tokens listed in 2024.** Exchanges: Binance, Bybit, OKX, Coinbase, Bithumb, Upbit. Prices as of 4 Feb 2025.
  - All exchanges: average short-term rise after listing +54%, followed by an average −52% drop; 89% below their listing-phase peak; **37% hit their ATH on listing day and never exceeded it**.
  - Binance: average listing-phase gain +87%; 46% ATH on listing day; 98% "dumped"; average −70% from peak.
  - Bybit: +61%; **60% ATH on listing day**; −63% from peak.
  - Coinbase: +41%; 23% ATH on listing day; −28% from peak.
  - Sources: [Cryptonomist, 31 Mar 2025](https://en.cryptonomist.ch/2025/03/31/the-98-of-new-tokens-listed-on-cex-experience-a-price-crash/); [CryptoNinjas](https://www.cryptoninjas.net/exchange/study-cex-listing-effects/)
- **CoinGecko, 50 biggest airdrops, 1 Jan 2020 – 20 Feb 2024.** 23/50 (46%) peaked within the first 14 days. 7/50 (14%) peaked on airdrop day and "were subsequently unable to recover." Counting from the table, about 22/50 peaked more than a month later. — [CoinGecko, "When Is the Best Time to Sell Airdrops?"](https://www.coingecko.com/research/publications/when-to-sell-airdrops)
- **Keyrock, "Airdrops in the Barren Desert" (2024 airdrops; reported 25 Sep 2024).**
  - 88% of tokens launched with airdrops that year declined, most within 15 days. Keyrock: "The majority of price movement occurs in the earliest days following the airdrop."
  - FDV and liquidity were the main drivers; "FDV management is more important" than airdrop size.
  - Sources: [DL News](https://www.dlnews.com/articles/snapshot/keyrock-study-says-most-token-airdrops-crash-after-launch); [BeInCrypto (88.7%, 62 airdrops, crash within 15 days)](https://beincrypto.com/majority-airdrop-tokens-crash-within-15-days/)
  - Only 8 of the 62 airdrops were positive after 90 days, an "11% success rate." — [Cryptopolitan](https://www.cryptopolitan.com/airdrops-record-11-success-rate/)

**Structural background (low float / high FDV)**
- Binance Research published "Low Float & High FDV: How Did We Get Here?" on 17 May 2024.
  - About $155B of tokens were due to unlock between 2024 and 2030.
  - Recent launches circulated only "6–20% of the projected issuance."
  - It recommended judging tokens by FDV-to-revenue and FDV-to-TVL.
  - Source: [ForkLog](https://forklog.com/en/binance-highlights-155-billion-token-unlock-overhang/)
- The researchers noted that only a couple of months into 2024, the FDV of that year's launches was already nearing the full-year 2023 total. — [DL News](https://dlnews.com/articles/defi/why-crypto-cant-stop-talking-about-fdv/)
- Binance said it would favour projects with "small to medium valuation relative to competitors in their respective sectors" for listings. — [The Informer Post](https://theinformerpost.beehiiv.com/p/binance-warns-against-low-float-high-valuation-coins-puts-out-call-for-small-projects-with-strong-fu)

#### B. Perp-DEX-specific evidence at the base-rate level
- In Memento's 2025 sample, the 3 perp DEX tokens had an average FDV change of +213%, a median of −31%, and 33% green, against 15.3% green for all 118. Memento names Hyperliquid and Aster as sector leaders but gives no per-token figures and does not list the three tokens. — [Memento Research](https://mementoresearch.com/state-of-2025-token-launches-year-in-review)
- In CryptoRank's 113-token sample (2024+ launches, data 21 Jul 2026), HYPE is the best performer at +1,519% vs its TGE price. No other perp DEX token is named among the 8 winners. — [CryptoPotato](https://cryptopotato.com/the-harsh-reality-of-new-crypto-just-7-of-major-tokens-beat-their-launch-price/)
- Keyrock's 2024 airdrop study names Drift, a Solana trading platform, as the top performer and credits its "modest launch value." It blames ZkLend's high launch value for its failure. — [DL News](https://www.dlnews.com/articles/snapshot/keyrock-study-says-most-token-airdrops-crash-after-launch)
- dYdX's airdrop (2021, outside the window) peaked in week 4 at +113%. — [CoinGecko](https://www.coingecko.com/research/publications/when-to-sell-airdrops)
- **Lighter (LIT), a counter-example to "low FDV at TGE".**
  - Before launch, pre-market trading put LIT near $3.20, implying FDV above $3B. Polymarket gave roughly even odds that FDV one day after launch would exceed $3B. — [FXStreet](https://www.fxstreet.com/cryptocurrencies/news/traders-split-over-whether-lighters-lit-clears-3-billion-fdv-after-launch-202512301124)
  - After the 30 Dec 2025 TGE (250M LIT, 25% of supply, airdropped), LIT hit an all-time low of $2.33 on 1 Jan 2026 as "many airdrop recipients cashed out." It then rose 37% by 6 Jan 2026 as fee-funded buybacks began and whales bought; a wallet believed to belong to Justin Sun held about 13.2M LIT. — [DL News, 6 Jan 2026](https://dlnews.com/articles/markets/lighter-token-rebounds-as-protocol-begins-buybacks-and-whales-buy-in)
- **Failures in the perp DEX cohort.**
  - On 8 Jul 2025 Vertex announced it would sunset VRTX. Staking, rewards and buybacks would cease, and VRTX holders would receive an airdrop of 1% of Ink's genesis supply. — [The Block](https://www.theblock.co/post/361570/vertex-to-sunset-vrtx-token-move-perp-dex-onto-kraken-backed-ink-layer-2)
  - KiloEx suffered a ~$7.5M oracle exploit and halted operations on 14 Apr 2025. KILO reportedly fell 31.5% in a day to $0.0366, 77.8% below its 27 Mar peak of $0.1648. These price figures come from one outlet citing CoinGecko and were not cross-checked. — [ForkLog](https://forklog.com/en/kiloex-halts-operations-following-7-5-million-hack/); [Cointelegraph](https://cointelegraph.com/news/kiloex-compensation-plan-7-million-hack-april)

### Inferences
- **Reported base rates are lower bounds for the user's metric.** At a 6–20 month horizon, the share of new tokens above their TGE price is about 7% (CryptoRank, large 2024+ launches), 12% (Delphi, CEX listings 2025–May 2026), about 15% (Memento, 2025 launches) and about 40% (Memento's $25–200M FDV bucket). Any token that is green at the end was necessarily above TGE at some point, so the "ever above" share must be at least these levels and is probably much higher. See the Q5 simulation.
- **Peaks are front-loaded.** In the 2024 CEX cohort, 37% set their ATH on listing day itself. 46% of large airdrops peaked within 2 weeks, and DWF says most tokens peak within the first month. For many tokens, the "maximum FDV after TGE" is therefore the listing-day wick. Whether such a token counts as "pushed above TGE" depends entirely on the TGE price definition (first print vs open vs day-0 close).
- **The direction of the user's hypothesis is supported, but it is not the same claim.** Memento's gradient (40% → 13% → 3% → 0% green across FDV buckets) and Keyrock's emphasis on FDV and modest launch values (Drift) support "lower launch FDV → better outcome." But that evidence is about end-point returns, not peak multiples. Low-FDV buckets also hold smaller, more volatile tokens, which mechanically raises the odds of a higher later maximum.
- **The perp DEX category result is outlier-driven.** An average of +213% against a median of −31% with N=3 is arithmetically possible only if the best token was about +700% to +770% at 20 Dec 2025. That follows from a median of −31% and a worst token no lower than −100%. This fits ASTER being the outlier, but Memento does not name it, so this is my inference. One mega-winner (HYPE in 2024, likely ASTER in 2025) can make the sector look different from the overall base rate.
- The CryptoRank "−95.7% median" looks extreme for a sample of tokens still above $100M market cap. It may be mis-transcribed in coverage, so I'd treat it as "as reported."

### Gaps
- I found no study, from any desk, that reports the share of tokens whose post-TGE maximum FDV exceeded TGE FDV, or the distribution of peak multiples by launch-FDV bucket. This is the core empirical gap for the user's hypothesis; the per-token perp DEX dataset has to fill it.
- Memento does not name its three perp DEX tokens. It also does not define "TGE opening" precisely or give its inclusion criteria.
- I could not open the primaries for Keyrock's airdrop report, CoinGecko's 2026 CEX report, Delphi's report, CryptoRank's post or DWF Labs' report. Figures come from secondary coverage.
- Coverage of Memento says Plasma's FDV briefly reached about $17B after TGE before collapsing. I could not tie this to a page I opened.
- I found no TGE-performance base-rate studies for this window from Kaiko, Tokenomist, Blockworks Research, The Block Research or Animoca. I did not search Messari for anything beyond the Binance-listings simulation.

---

## Q2. Perp DEX sector context, 2023–2026: volume growth, Hyperliquid's rise and "HYPE comps," the 2025 perp DEX wars, Binance/CZ support for Aster, and fee-funded buybacks

### Takeaway
On-chain perps went from a niche (2.1% of derivatives volume in Jan 2023) to about $7.9T of volume in 2025 and more than $1T per month from Oct 2025. Hyperliquid's ~70% share and fee-funded buybacks (97–99% of fees, over $1.3B cumulative by May 2026) made HYPE the sector's valuation anchor: +1,519% from TGE by Jul 2026, still priced at about 61x FDV/earnings in Jun 2026. That anchor fed a "next Hyperliquid" launch wave in H2 2025 (Aster, Lighter, Avantis, edgeX), driven by points and airdrops and, for Aster, by Binance/CZ-adjacent backing. Much of the challengers' volume was incentive-driven or of questionable integrity, so FDV/volume "comps" overstate their fundamentals.

### Cited Findings

**Volume growth**
- Daily perp DEX volume exceeded $100B by the first week of Oct 2025, up from "a few billion" in early 2024. Perp DEXs captured about 10% of CEX perp volume. — [21Shares, 6 Oct 2025](https://www.21shares.com/research/the-perpetual-dex-wars-hyperliquid-aster-and-lighter-in-focus)
- **DefiLlama data via Cointelegraph (31 Dec 2025):**
  - Cumulative perp DEX volume reached $12.09T, up from $4.1T at the start of 2025.
  - 2025 volume was about $7.9T: about $2.1T in H1 and about $5.74T (73%) in H2.
  - Oct 2025 was the first month above $1T; Dec 2025 was also about $1T.
  - Hyperliquid did $175–248B per month in H1 2025. Aster did $259B in each of Oct and Nov 2025. Lighter was consistently above $100B per month by Q3 2025.
  - Source: [Cointelegraph](https://cointelegraph.com/news/perpetuals-dex-volume-2025-onchain-derivatives-growth)
- Oct 2025 perp DEX volume was about $1.3T, nearly double September. The Block's analysts credited incentive programs tied to expected airdrops plus liquidation-driven trading. — [ForkLog](https://forklog.com/en/news/monthly-perp-dex-volume-tops-1trn)
- Per CoinGecko data, perp DEXs' share of derivatives volume rose from 2.1% (Jan 2023) to a record 11.7% (Nov 2025). — [Cointelegraph](https://cointelegraph.com/news/dex-adoption-hip-3-hype-200-hyperliquid)

**Market share (shares conflict because dates and metrics differ)**
- 21Shares: Hyperliquid held about 70% share for most of the 12 months to Sep 2025, then about 10% in Sep 2025, when Aster held about 70% and Lighter about 15%. Hyperliquid's open interest was still $13.5B vs Aster's $3B. Aster's volume/TVL ratio was above 70:1, against a typical 3–7 elsewhere in DeFi. — [21Shares](https://www.21shares.com/research/the-perpetual-dex-wars-hyperliquid-aster-and-lighter-in-focus)
- CF Benchmarks: Hyperliquid's share of on-chain perp volume was about 71% in May 2025 and about one-third in Apr 2026. — [CF Benchmarks, 10 Jun 2026](https://www.cfbenchmarks.com/blog/pricing-the-perp-dex-leader-a-valuation-framework-for-hyperliquid)
- A Cantor report (Dec 2025) said rivals had cut Hyperliquid's share to 17%, down from 60% in May. — [MEXC repost](https://www.mexc.com/news/289675)
- Another late-2025 analysis put Hyperliquid at about 20% by Nov 2025, with Lighter at 27.7%, Aster 19.3% and edgeX 14.6%. — [MEXC repost](https://www.mexc.com/news/196770)
- A DefiLlama peer-set dashboard (mid-2026) shows Hyperliquid at about 68.5% of 30-day derivatives volume among tracked peers, Aster about 15.0% and Lighter about 13.1%. These are peer-set shares, not sector-wide. — [DefiLlama](https://defillama.com/pro/q4twtf7glc8ivq8)
- VanEck: Hyperliquid did $181.7B of 30-day volume in Apr 2026, about 32% of on-chain perp volume. VanEck is an issuer, so this is promotional. — [VanEck](https://www.vaneck.com/lu/en/blog/digital-assets/exploring-hyperliquid-redefining-derivatives-trading/)

**Hyperliquid as the valuation anchor ("HYPE comps") and fee-funded buybacks**
- Historically 97% of protocol fees go to the Assistance Fund, which buys HYPE on the open market. Cumulative buybacks exceeded $1.1B by end-Apr 2026. A Dec 2025 governance vote formally recognized Assistance Fund HYPE as burned. — [VanEck](https://www.vaneck.com/lu/en/blog/digital-assets/exploring-hyperliquid-redefining-derivatives-trading/)
- Amina puts the share at 97–99% of perp and spot fees, with over $1.3B deployed and about 28.5M HYPE held by May 2026, and about $857M of fees in 2025. This conflicts with VanEck's figure of 44M HYPE accumulated. — [Amina Group](https://aminagroup.com/research/hyperliquid-hype-etf-buyback-staking-yield-institutional-access-2026/)
- **CF Benchmarks (10 Jun 2026):**
  - HYPE at $56.19: FDV about $53.7B (~956M tokens); circulating value about $12.5B (~222M tokens).
  - Annualized fees about $1.06B and earnings about $0.88B.
  - **FDV/earnings about 61x; circulating/earnings about 14x.** It uses a normalized mature-venue exit multiple of about 25x (Coinbase about 38x trailing, ICE about 22x).
  - 2025 buybacks averaged about $65M per month, buying about 21M HYPE at an average near $30.
  - Source: [CF Benchmarks](https://www.cfbenchmarks.com/blog/pricing-the-perp-dex-leader-a-valuation-framework-for-hyperliquid)
- 21Shares (Oct 2025): Hyperliquid's annualized revenue was over $800M, HYPE buybacks exceeded $715M, and there were no VC allocations. — [21Shares](https://www.21shares.com/research/the-perpetual-dex-wars-hyperliquid-aster-and-lighter-in-focus)
- A Blockworks analyst said Hyperliquid's FDV-to-fees ratio is higher than Drift's and dYdX's. This is search-snippet level only; the article returned 403. — [Blockworks](https://blockworks.com/news/hyperliquid-hype-valued-l1-perps-dex)
- Commentary describes traders hunting for "the next Hyperliquid" after HYPE's run, with rivals offering zero fees and airdrop incentives. These are low-quality commentary sources. — [We The Ivy](https://en-wetheivy.beehiiv.com/p/problems-that-open-the-door-to-opportunity-hyperliquid); [Netcoins (ASTER, APEX, Avantis named as incentive-driven challengers)](https://netcoins.com/blog/the-rise-of-the-perp-dex-meta---hyperliquid-leads-the-charge-amid-new-challengers)

**The 2025 "perp DEX wars": Aster and Binance/CZ**
- Aster's reported volume briefly exceeded Hyperliquid's after its token launch in Sep 2025, running at roughly 8x its open interest. — [CF Benchmarks](https://www.cfbenchmarks.com/blog/pricing-the-perp-dex-leader-a-valuation-framework-for-hyperliquid)
- After the APX Finance merger the token surged "over 2,000%." Aster offers up to 1,001x leverage in Simple Mode and runs a points-based rewards system. — [21Shares](https://www.21shares.com/research/the-perpetual-dex-wars-hyperliquid-aster-and-lighter-in-focus)
- U.Today reported a gain of more than 8,000% in a week; the base price differs from other sources. — [U.Today via TradingView](https://vn.tradingview.com/news/u_today:81455d534094b:0-8-000-in-week-binance-founder-ends-speculations-on-his-affiliation-with-next-bnb)
- CZ disclosed a wallet holding over $2.5M of ASTER. The token jumped from $0.91 to $1.26 and 24h volume rose from $224M to over $2B. — [Cointelegraph](https://cointelegraph.com/news/aster-token-surges-after-cz-buys-two-million-tokens); [Unchained](https://unchainedcrypto.com/aster-jumps-30-after-cz-discloses-2-5-million-holdings/)
- CZ calls himself an "advisor." YZi Labs (formerly Binance Labs) is listed as a backer on Aster's X profile, and some posts say Aster's API looks almost identical to Binance's. — [Cointelegraph](https://cointelegraph.com/news/defillama-delist-aster-perp-data-integrity)
- See also coverage of CZ championing Aster around its debut. — [CryptoSlate](https://cryptoslate.com/binance-founder-cz-champions-aster-amid-impressive-token-debut/)
- On 5 Oct 2025 DefiLlama delisted Aster's perp volume. Its founder 0xngmi showed volumes "mirroring Binance Perp volumes almost exactly" (correlation about 1) and said Aster exposes no order-level data to check for wash trading. ASTER fell about 10% after the news. DefiLlama had earlier delisted "Lighter and many other perp DEXs" for "blatant wash trading." — [Cointelegraph](https://cointelegraph.com/news/defillama-delist-aster-perp-data-integrity); [Unchained](https://unchainedcrypto.com/defillama-delists-aster-perp-volume-over-data-integrity-concerns/)
- **Aster tokenomics shift (provisional):**
  - A KuCoin headline: "Aster Overhauls ASTER Tokenomics: 99% of Fees to Buybacks, Supply Cut to 3B." — [KuCoin](https://www.kucoin.com/news/flash/aster-overhauls-aster-tokenomics-99-of-fees-to-buybacks-supply-cut-to-3b)
  - Tokenomist reported that insider unlocks stay inactive until Sep 2026. — [Tokenomist](https://www.tokenomist.ai/research/deep-dive-aster-dex-aster-tokenomics-emissions-buybacks-burn-cycles)
  - Sources conflict on the fee share going to buybacks (60–90% vs 99%).

**Lighter, edgeX and others**
- Lighter launched mainnet on 2 Oct 2025, charges zero fees for retail, and its LLP pool averaged about 60% APY. — [21Shares](https://www.21shares.com/research/the-perpetual-dex-wars-hyperliquid-aster-and-lighter-in-focus)
- Lighter processed $232B of 30-day volume before its Dec 2025 TGE. In early 2026 Aster held about 20% of perp DEX share, and StarkWare tech powered about 16% of volume across Paradex, Extended and edgeX. — [BlockEden, 29 Jan 2026](https://blockeden.xyz/blog/2026/01/29/perp-dex-wars-2026-hyperliquid-lighter-aster-edgex-paradex-decentralized-derivatives/)
- LIT tokenomics: 25% airdropped from points seasons 1–2. Team (26%) and investors (24%) are locked for one year, then vest linearly over three years. — [BTC-Echo](https://www.btc-echo.de/schlagzeilen/lighter-launcht-lit-token-das-naechste-hyperliquid-222495/); [Coin Academy](https://coinacademy.fr/actu/lighter-lance-token-lit-airdrop/)
- Tokenomist flags Lighter's "December 2026 cliff." — [Tokenomist](https://tokenomist.ai/research/lighter-lit-tokenomics-robinhood-hype-a-real-burn-and-the-december-2026-cliff-2)
- Vertex's CEO on its exit: "competition in the perp space has ramped up exponentially." — [The Block](https://www.theblock.co/post/361570/vertex-to-sunset-vrtx-token-move-perp-dex-onto-kraken-backed-ink-layer-2)

### Inferences
- **Perp DEX tokens differ structurally from the average 2024–2026 launch.**
  - Many have real fee revenue and fee-funded buybacks.
  - The sector anchor (HYPE) rose more than 15x after TGE and still trades at about 61x FDV/earnings. Against that comp, a challenger launching at a few hundred million to a few billion of FDV can be marketed as "cheap vs HYPE," which is a plausible driver of post-TGE re-ratings.
  - This fits the sector's better showing in Memento's 2025 sample and HYPE topping CryptoRank's list.
- **Volume-based comps were unreliable at the peak of the wars.** Signs include Aster's volume/TVL above 70:1, the DefiLlama delisting, earlier wash-trading delistings of Lighter, and zero-fee retail models where volume earns no fees. "Low FDV relative to volume" was often low only relative to inflated or unmonetized volume.
- **Timing clustered at the sector top.** The H2 2025 challengers launched as the hype peaked (Oct 2025 was the first >$1T month), right around the 10 Oct 2025 crash (see Q3). Launch timing within the regime is a confounder for any "low FDV → higher peak" test.

### Gaps
- I found no reliable FDV/fees or FDV/earnings multiples for Aster, Lighter, edgeX, Paradex or Avantis, and no time series of sector multiples.
- I found no systematic study of the "HYPE comps" effect, i.e. whether peer perp DEX tokens re-rate after HYPE moves; the evidence is narrative only.
- Claims of consecutive month-over-month declines in 2026 sector volume appeared only in unverified commentary.
- The sources do not agree on whether Aster's buybacks are currently burned, sent to reserves or distributed to veASTER stakers.

---

## Q3. Market regime timeline, Oct 2023 – Oct 2026 (for placing each TGE in a bull or bear window)

### Takeaway
The window splits into four broadly bullish phases:
- Oct 2023 – mid-Mar 2024: ETF-driven, BTC ATH $73,098.
- Nov – Dec 2024: election rally, BTC $108,135 on 17 Dec 2024.
- Mid-Apr – early Oct 2025: BTC above $126k, ETH ATH $4,946.
- Aug – Oct 2026: a partial recovery to about $80–85k BTC.

And three bearish or bleeding phases:
- Mid-Mar – early Nov 2024: Q2 2024 −14.4%, plus the 5 Aug 2024 crash.
- Feb – early Apr 2025: BTC down to $74.4k.
- 10 Oct 2025 through mid-2026: about $19B liquidated on 10–11 Oct 2025; BTC about $60k in Feb 2026 and about $59k on 5 Jun 2026, roughly −53% from the peak.

Altcoins underperformed BTC in most of these windows.

### Cited Findings

**Oct 2023 – Mar 2024: bull**
- Total crypto market cap rose 54.3% (+$607B) in Q4 2023, and 108.1% for 2023 as a whole to $1.72T. CoinGecko credits optimism about US spot BTC ETF approval. — [CoinGecko 2023 Annual Report (PDF)](https://assets.coingecko.com/reports/2023/CoinGecko-2023-Annual-Crypto-Industry-Report.pdf)
- BTC went from about $26.9k to about $42.2k in Q4 2023. This figure comes from a republishing site. — [Unlock-bc](https://www.unlock-bc.com/en/q4-dominates-70-of-market-gains-adds-607b-to-total-market-cap-2023-annual-crypto-industry-report-shows)
- **Q1 2024:** total market cap rose about 64.5% to $2.9T (13 Mar 2024). BTC gained 68.8%, falling first to a quarterly low of $39,505 after the January ETF approval, then rebounding 85% to an ATH of $73,098. Memecoins were the most profitable narrative. — [CoinGecko 2024 Q1 Report](https://coingecko.com/research/publications/2024-q1-crypto-report); [Cointelegraph](https://cointelegraph.com/markets/memecoins-were-most-profitable-crypto-narrative-in-q1-2024-coingecko)

**Apr – Oct 2024: altcoin bleed and chop**
- **Q2 2024:** total market cap fell 14.4% (−$408.8B) to $2.43T. BTC fell 11.9%, trading between $58k and $72k, and never set a new ATH in the quarter. — [CoinGecko 2024 Q2 Report](https://www.coingecko.com/research/publications/2024-q2-crypto-report)
- **5 Aug 2024 crash:** over $1B of crypto futures were liquidated in 24h (about 200k traders), and ether had its steepest one-day drop since May 2021. — [CoinDesk](https://coindesk.com/markets/2024/08/05/crypto-futures-witness-840m-in-liquidations-as-bitcoin-nosedives-ether-records-biggest-fall-since-2021)
  - The trigger was the yen carry-trade unwind after the Bank of Japan's 31 Jul hike; the Nikkei fell 12.4% that day. — [Cointelegraph opinion](https://cointelegraph.com/opinion/how-the-yen-carry-trade-wiped-out-crypto)
  - BTC fell about 18% to about $51.1k and ETH about 23% to about $2.2k, per secondary summaries; intraday lows vary by venue. — [Young Platform](https://youngplatform.com/en/blog/news/bitcoin-crash-causes/)
- CoinGecko's annual report calls Q3 2024 the year's most tumultuous quarter. Fed rate cuts began on 18 Sep 2024. — [Coin Bureau summary of CoinGecko 2024 Annual Report](https://coinbureau.com/press-release/coingecko-2024-crypto-industry-report); [Cryptopolitan](https://www.cryptopolitan.com/coingecko-crypto-market-cap-nearly-doubled-in-2024-btc-dominance-cemented/)

**Nov 2024 – Jan 2025: bull**
- Total market cap rose 45.7% in Q4 2024. BTC hit about $108,135 on 17 Dec 2024, and total market cap set a record of $3.91T. 2024 overall was +97.7%. CoinGecko cites Trump's election as a major trigger. — [Coin Bureau summary of CoinGecko 2024 Annual Report](https://coinbureau.com/press-release/coingecko-2024-crypto-industry-report); [CoinGecko 2024 Annual Report (PDF)](https://assets.coingecko.com/reports/2024/CoinGecko-2024-Annual-Crypto-Industry-Report.pdf)

**Feb – early Apr 2025: drawdown**
- BTC fell as low as $74,400 in April 2025 after Trump's initial tariff plan. — [Bloomberg (video page, 18 Nov 2025)](https://www.bloomberg.com/news/videos/2025-11-18/bitcoin-falls-nearly-30-from-2025-peak-video)
- The CoinMarketCap Altcoin Season Index stood at 21 on 15 Mar 2025, far below the altseason threshold of 75. — [KuCoin flash](https://www.kucoin.com/news/flash/altcoin-season-index-at-21-signals-bitcoin-dominance-in-march-2025-crypto-market)
- Kaiko/Blockhead (Mar 2025): the top 10 altcoins made up 64% of altcoin volume, up from 32% at end-2021, which favours selective rather than broad altcoin rallies. — [Bitcoin.com (ES)](https://news.bitcoin.com/es/fin-de-la-temporada-de-altcoins-informe-predice-ganancias-especificas-en-lugar-de-un-aumento-generalizado-en-criptomonedas/)

**Mid-Apr – early Oct 2025: bull led by BTC and ETH**
- **Q3 2025:** total market cap rose 16.4% (+$563.6B) to about $4T, the highest since late 2021. ETH went from $2,502 to an ATH of $4,946, driven by ETF inflows and treasury-company buying. — [Cryptonews (CoinGecko Q3 2025 report)](https://cryptonews.com/news/q3-2025-bitcoin-surged-to-ath-but-with-notable-laggard-as-ethereum-led-the-quarter/); [Blockchain.news](https://blockchain.news/news/crypto-market-reaches-4-trillion-eth-bnb-record-highs-q3-2025)
- BTC set a record above $126,000 in early October 2025. — [Bloomberg](https://www.bloomberg.com/news/videos/2025-11-18/bitcoin-falls-nearly-30-from-2025-peak-video)

**10–11 Oct 2025 crash and the bear phase after it**
- After Trump threatened 100% tariffs on Chinese imports, BTC fell from about $122k to about $114k on 10 Oct and to as low as about $104k overnight. — [ts2.tech](https://ts2.tech/en/crypto-market-carnage-bitcoin-crashes-from-record-highs-as-tariff-bombshell-wipes-out-20b/)
- **Scale (figures vary by source):**
  - CoinGlass: $19.13B liquidated across 1,618,240 traders, with a true scale possibly $30–40B because of late disclosure.
  - Total market cap fell from about $4.15T to $3.74T.
  - Some small altcoins fell more than 99% intraday.
  - USDe briefly traded at about $0.66 on Binance, and Binance reimbursed $283M.
  - Sources: [CoinGecko Learn](https://www.coingecko.com/learn/october-10-crypto-crash-explained); [Decrypt](https://decrypt.co/343941/bitcoin-ethereum-dogecoin-down-record-19-billion-crypto-liquidations)
- By 18 Nov 2025 BTC was below $90k, erasing its 2025 gains. — [Bloomberg](https://www.bloomberg.com/news/videos/2025-11-18/bitcoin-falls-nearly-30-from-2025-peak-video)
- **2025 full year:** total market cap fell 10.4% to about $3T, the first annual decline since 2022. BTC fell 6.4% while gold rose 62.6%. Stablecoins grew 48.9% to $311B. — [CoinGecko 2025 Annual Report (PDF)](https://assets.coingecko.com/reports/2025/CoinGecko-2025-Annual-Crypto-Industry-Report.pdf); [HTX summary](https://www.htx.com/en-in/news/coingecko-2025-cryptocurrency-industry-report-total-market-c-4WRFl9O9/)
  - Q4 2025 alone was −23.7% (−$946B). This appears only in a headline. — [TechFlow](https://techflowpost.com/en-US/article/29977)
- **Early Feb 2026:** BTC hit about $60k, about −52% from the $126k peak, then recovered to about $69k. Analysts disagreed on whether this was the bottom (Fidelity, Bernstein, K33). — [AMBCrypto](https://ambcrypto.com/bitcoins-weakest-bear-market-ever-bernstein-predicts-150k-in-2026/); [Fidelity](https://www.fidelity.com/learning-center/trading-investing/decode-crypto-chart-of-the-month)
- **June 2026:** BTC hit about $59.0–59.1k on 5 Jun 2026, its lowest since Oct 2024 and roughly half the Oct 2025 ATH.
  - Strategy sold 32 BTC, its first sale, to fund preferred dividends.
  - Spot BTC ETFs had a 12–13-day outflow streak and $3.61B of outflows in June (SoSoValue). ETF assets were about $72.6B, about −57% from the Oct 2025 peak.
  - BTC fell below $60k again around 26 Jun 2026.
  - Sources: [Cointelegraph](https://cointelegraph.com/news/bitcoin-etfs-biggest-outflows-june-btc-below-60k); [The Block](https://www.theblock.co/post/403659)

**Aug – Oct 2026: partial recovery**
- The crypto market had its biggest 3-day rally since 2023, more than 20%, with over $4B of bearish positions liquidated in a short squeeze. Coverage ties it to the US Treasury doubling purchases of longer-dated bonds, and spot BTC ETFs took in $1.92B of net inflows in a week. BTC briefly topped $81k on 25 Aug 2026. These are search-snippet level; the CNBC pages returned 403. — [CNBC, 24 Aug 2026](https://www.cnbc.com/2026/08/24/crypto-extends-gains-after-biggest-3-day-rally-since-2023.html); [CNBC, 25 Aug 2026](https://www.cnbc.com/2026/08/25/bitcoin-price-near-80000-cryptocurrency-ether-us-treasuries.html)
- Total crypto market cap climbed back above $3T on 22 Sep 2026 as leveraged bets surged. — [Cryptonomist, 22 Sep 2026](https://en.cryptonomist.ch/2026/09/22/bitcoin-crypto-market-rally/)
- BTC rose as much as 2.4% to $84,737 on 21 Oct 2026. Coverage puts it about 45% above the June low and about 32% below the Oct 2025 peak. — [Bloomberg, 21 Oct 2026](https://www.bloomberg.com/news/articles/2026-10-21/bitcoin-rallies-back-as-tech-rebound-sparks-speculative-appetite)
- On 26 Oct 2026, BTC was about $79.6k, ETH about $2,300 and SOL about $100. Spot BTC ETFs saw about $773.5M of outflows on 22–23 Oct, and the Fear & Greed index read a neutral 50. Most large altcoins fell, while some memecoins rose. — [KuCoin daily report](https://www.kucoin.com/news/articles/crypto-daily-market-report-october-26-2026); [crypto.news](https://crypto.news/crypto-market-watch-worst-altcoins-bitcoin-price-80k/)

### Inferences
- **Proposed regime windows for tagging each TGE.** This classification is mine, built from the cited anchors.

  | Window | Regime | Anchor evidence |
  |---|---|---|
  | Oct 2023 – mid-Mar 2024 | Bull (ETF anticipation and approval; memecoins) | Q4 2023 +54.3%; Q1 2024 +64.5%; BTC ATH $73,098 |
  | Mid-Mar 2024 – early Nov 2024 | Bear/chop, altcoin bleed | Q2 2024 −14.4%; 5 Aug 2024 crash; "tumultuous" Q3 |
  | Early Nov 2024 – Jan 2025 | Bull | Q4 2024 +45.7%; BTC $108,135 (17 Dec 2024) |
  | Feb – early Apr 2025 | Bear/drawdown | BTC low $74.4k (Apr 2025); Altseason Index 21 |
  | Mid-Apr – early Oct 2025 | Bull (BTC/ETH-led, selective alts) | Q3 2025 +16.4% to $4T; ETH ATH $4,946; BTC >$126k |
  | 10 Oct 2025 – Jul 2026 | Bear | $19B liquidation; Q4 2025 −23.7%; BTC ~$60k (Feb 2026) and ~$59k (Jun 2026) |
  | Aug – Oct 2026 | Partial recovery / range ($79–85k BTC) | Aug 3-day +20%; >$3T total cap (Sep); altcoins uneven |

- **Consequences for the hypothesis.**
  - A TGE in a bull window gets a tailwind that makes a higher post-TGE maximum more likely regardless of launch FDV.
  - A TGE in the last weeks before 10 Oct 2025 (e.g., Aster in Sep 2025) had a short runway before a market-wide deleveraging.
  - A TGE in the Oct 2025 – Jul 2026 bear (e.g., Lighter, 30 Dec 2025) faced a persistent headwind; any later peak above TGE there is better evidence of token-specific strength.
- **Horizon bias in Memento's data.** Memento's 2025 cohort was measured on 20 Dec 2025, i.e. after the Oct 2025 crash. Its "below TGE" rates are partly a regime artefact, especially for H2 2025 launches.

### Gaps
- I found no authoritative source for an exact Jan 2025 BTC high, the exact 7 Apr 2025 low, or the exact July/Aug 2025 BTC records. These are well known but not sourced here.
- Coverage conflicts on the 2026 low: early-Feb ~$60k vs 5 Jun ~$59k vs a claimed early-Aug $62–64k range from promotional blogs. The cited reporting puts the cycle low in June 2026.
- I found no altcoin-index series (e.g., TOTAL3 or OTHERS) with dated values. The altcoin-vs-BTC claims rest on the Altseason Index and the Kaiko concentration data.

---

## Q4. Mechanisms behind post-TGE pumps of low-FDV/low-float tokens, and behind failures

### Takeaway
Post-TGE re-ratings in this period came mainly from five sources:
- fee-funded buybacks (HYPE, then copied by LIT and ASTER);
- exchange listings and endorsements ("Binance effect," CZ disclosures);
- short squeezes and coordinated flows on perp markets with a small, concentrated float (MYX is the clearest alleged case);
- airdrop-season incentives that pull in volume and attention;
- whale accumulation.

Failures came from:
- airdrop recipients dumping;
- unlock overhang (90% of unlocks are price-negative);
- perp listings that make hedged spot dumping easy;
- hacks (KiloEx), shutdowns (Vertex) and data-integrity shocks (Aster's DefiLlama delisting);
- market-wide liquidation cascades (Oct 2025).

### Cited Findings

**Pump mechanisms**
- **Fee-funded buybacks.**
  - Hyperliquid routes 97–99% of fees to open-market HYPE buybacks, more than $1.1–1.3B cumulative by Apr–May 2026. — [VanEck](https://www.vaneck.com/lu/en/blog/digital-assets/exploring-hyperliquid-redefining-derivatives-trading/); [Amina Group](https://aminagroup.com/research/hyperliquid-hype-etf-buyback-staking-yield-institutional-access-2026/)
  - HYPE is +1,519% vs its TGE price (Jul 2026). — [CryptoPotato](https://cryptopotato.com/the-harsh-reality-of-new-crypto-just-7-of-major-tokens-beat-their-launch-price/)
  - LIT rebounded 37% from its low as buybacks from exchange revenue began. — [DL News](https://dlnews.com/articles/markets/lighter-token-rebounds-as-protocol-begins-buybacks-and-whales-buy-in)
  - The Delphi study notes that a revenue-weighted basket of fee-switch tokens rose about 30% while the median listing fell 82%. — [ChainCatcher](https://www.chaincatcher.com/en/article/2270245)
- **CEX listings.**
  - The "Binance effect": newly listed tokens spiked 41% on average (CoinDesk, Jan 2023, a pre-window baseline). — [CoinDesk](https://www.coindesk.com/markets/2023/01/06/binance-effect-means-41-price-spike-for-newly-listed-tokens)
  - In the 2024 cohort, the average listing-phase gain was +87% on Binance and +54% across six exchanges, followed by deep drawdowns. — [Cryptonomist](https://en.cryptonomist.ch/2025/03/31/the-98-of-new-tokens-listed-on-cex-experience-a-price-crash/)
  - Binance Alpha announces new tokens, sometimes with Alpha-Points airdrops, and perps can follow weeks later. This comes from a promotional source. — [AAP/Cision press release](https://aapnews.aap.com.au/news/cision20251112AE21149)
- **Founder/exchange endorsement.** CZ's disclosure of more than $2.5M of ASTER lifted it from $0.91 to $1.26, and volume rose about 9x in 24h. — [Cointelegraph](https://cointelegraph.com/news/aster-token-surges-after-cz-buys-two-million-tokens)
- **Short squeezes and coordinated flows on small-float perps (MYX Finance, Sep 2025; allegations, not established facts).**
  - MYX ran from a low of $0.133 in Aug 2025 to a record near $20; commentators argued there was no news behind it. — [Invezz, 12 Sep 2025](https://invezz.com/news/2025/09/12/heres-why-the-myx-finance-price-surged-and-why-it-may-crash-soon/)
  - Cointelegraph linked the move to forced short liquidations and suspected whale coordination across Binance futures, Bitget spot and PancakeSwap. It also noted that a 39M-token unlock coincided with the surge, raising fears of insiders exiting into retail demand. — [Cointelegraph](https://cointelegraph.com/news/what-is-myx-finance-why-is-it-up-1-400-percent)
  - Bubblemaps flagged one entity allegedly claiming more than $170M of the airdrop through about 100 new accounts, which MYX denied. — [crypto.news](https://crypto.news/myx-finance-price-surges-insider-manipulation-2025/); [BeInCrypto](https://beincrypto.com/myx-price-explosive-rally-or-manipulation/)
  - An advocacy piece calls it "a deliberately orchestrated exit-liquidity game." — [Wu Blockchain Substack](https://wublock.substack.com/p/the-myx-affair-a-deliberately-orchestrated)
- **Low-float squeeze mechanics.** The circulating supply is small and a large share sits with a few wallets. Carry traders short the perp against spot, then float holders push spot up, which can margin-call the short leg. — [HackerNoon](https://hackernoon.com/that-300percent-funding-apr-is-not-free-money-screening-for-squeeze-traps-on-binance-perpetuals)
- **ASTER manipulation allegations (unverified).**
  - An opinion Substack alleges insider farming, wash trading and Binance ties, citing Elementus. — [Amologoko Substack](https://amologoko.substack.com/p/aster-hyperliquid-killer-or-binances)
  - The verified part is DefiLlama's delisting over volume integrity, with volumes mirroring Binance perps at a correlation of about 1. — [Cointelegraph](https://cointelegraph.com/news/defillama-delist-aster-perp-data-integrity)
- **Airdrop seasons and points as attention and volume engines.**
  - The record Oct 2025 perp DEX volume was credited to incentive programs tied to expected airdrops. — [ForkLog](https://forklog.com/en/news/monthly-perp-dex-volume-tops-1trn)
  - Lighter's TGE airdrop drew on points seasons 1–2. — [Coin Academy](https://coinacademy.fr/actu/lighter-lance-token-lit-airdrop/)
  - Analysts saw much of Lighter's and Aster's volume as incentive-driven rather than organic. — [MEXC repost of Cantor-based analysis](https://www.mexc.com/news/289675)
- **Whale accumulation.** After LIT's launch, several large holders bought millions of dollars' worth; a wallet believed to belong to Justin Sun held about 13.2M LIT. — [DL News](https://dlnews.com/articles/markets/lighter-token-rebounds-as-protocol-begins-buybacks-and-whales-buy-in)

**Failure mechanisms**
- **Airdrop recipients dumping.**
  - 88% of 2024 airdrop tokens declined, most within 15 days; airdrops smaller than 5% of supply often saw "massive sell-offs." — [BeInCrypto](https://beincrypto.com/majority-airdrop-tokens-crash-within-15-days/)
  - LIT hit its all-time low of $2.33 two days after TGE as recipients sold. — [DL News](https://dlnews.com/articles/markets/lighter-token-rebounds-as-protocol-begins-buybacks-and-whales-buy-in)
  - The Delphi study describes airdrops as exit liquidity. — [ChainCatcher](https://www.chaincatcher.com/en/article/2270245)
- **Unlock overhang.**
  - Keyrock studied 16,000+ unlock events across 40 tokens (page assets dated Dec 2024). 90% of unlocks created negative price pressure. Weakness often starts about 30 days before an unlock and prices stabilize about 14 days after. Team unlocks are the worst (about −25%); investor unlocks are "controlled" (106 events); ecosystem unlocks average +1.18%. Larger unlocks produce drops 2.4x sharper. — [Keyrock](https://keyrock.com/from-locked-to-liquidity-what-16000-token-unlocks-teach-us/)
  - Binance Research counted about $155B of unlocks due 2024–2030. — [ForkLog](https://forklog.com/en/binance-highlights-155-billion-token-unlock-overhang/)
  - Perp-DEX-specific: Lighter's team and investor cliff is due Dec 2026 — [Tokenomist](https://tokenomist.ai/research/lighter-lit-tokenomics-robinhood-hype-a-real-burn-and-the-december-2026-cliff-2) — and Aster insider unlocks are inactive until Sep 2026. — [Tokenomist](https://www.tokenomist.ai/research/deep-dive-aster-dex-aster-tokenomics-emissions-buybacks-burn-cycles)
- **Perp listings as "death traps."** ai16z fell 84% and VVV 67% after their Binance perp listings. An Arete Capital partner argued perp listings let traders short aggressively while dumping spot (Feb 2025). — [The Block](https://www.theblock.co/news/defi/2025-02-06-ai16z-and-vvv-see-double-digit-price-drops-since-death-trap-perps-listings-analyst-says-339220)
- **Liquidity.** "Without sufficient liquidity, prices become highly sensitive to sell pressure," and high-FDV tokens often lack the liquidity to support their valuations. — [DL News (Keyrock)](https://www.dlnews.com/articles/snapshot/keyrock-study-says-most-token-airdrops-crash-after-launch)
- **High launch FDV.** In Memento's sample, launches at ≥$1B FDV were 0% green. — [Memento Research](https://mementoresearch.com/state-of-2025-token-launches-year-in-review)
- **Hacks.** KiloEx: ~$7.5M exploit and operations halted on 14 Apr 2025; KILO fell sharply. — [ForkLog](https://forklog.com/en/kiloex-halts-operations-following-7-5-million-hack/)
- **Shutdowns and pivots.** Vertex sunset VRTX in Jul 2025, ending staking, rewards and buybacks. — [The Block](https://www.theblock.co/post/361570/vertex-to-sunset-vrtx-token-move-perp-dex-onto-kraken-backed-ink-layer-2)
- **Data-integrity shocks.** ASTER fell about 10% after the DefiLlama delisting. — [Cointelegraph](https://cointelegraph.com/news/defillama-delist-aster-perp-data-integrity)
- **Market-wide deleveraging.** On 10–11 Oct 2025 about $19B was liquidated and some small altcoins fell more than 99% intraday. — [CoinGecko Learn](https://www.coingecko.com/learn/october-10-crypto-crash-explained)

### Inferences
- **Low float plus perp listings cuts both ways.** It can manufacture a higher post-TGE maximum through squeezes and coordinated flows (MYX), or crush the price through hedged spot dumping (ai16z, VVV). For the user's "max FDV" metric, a low float raises the odds of a spike above TGE FDV, but such spikes may be manipulation-driven and short-lived. They say little about fundamental under-valuation at launch.
- **Buybacks are the one mechanism tied to fundamentals.** Fee-funded buybacks link FDV to revenue. They are the most plausible reason a perp DEX that launches at low FDV relative to fees gets pushed higher over time (HYPE, and partly LIT after launch). They only work if fees are real, unlike zero-fee or wash-traded volume.
- **Insider unlocks fall outside most measurement windows.** Many perp DEX tokens schedule insider unlocks 9–12 months after TGE (Aster Sep 2026, Lighter Dec 2026). Peaks measured within the first year therefore often occur before the overhang hits.

### Gaps
- I found no systematic study of how often perp listings or Binance Alpha listings cause pumps vs dumps; the evidence is anecdotal.
- MYX and ASTER manipulation claims come from analysts, on-chain sleuths and advocacy pieces, not regulators or court findings.
- I found no reliable figures on Aster's airdrop stages (e.g., a "Stage 6" from Feb 2026) or on the exact fee share going to Aster buybacks; the reports conflict.

---

## Q5. Methodological pitfalls in testing "low-FDV perp DEX launches mostly get pushed to a higher FDV after TGE"

### Takeaway
Results hinge on definitions:
- Which "TGE price": pre-market, first print, open, day-0 close, or FDV 24h after launch?
- Which threshold: any print above TGE, or ≥1.5x / ≥2x?
- Which sample: survivors only, or every launch?
- What "low FDV" means: absolute dollars, or relative to fees, to HYPE comps, or to the last private round?

Because new tokens are extremely volatile, "the maximum after TGE exceeded TGE" is nearly guaranteed at a 1.0x threshold unless the token dumps from the first print. My simulation shows about 83–92% of random paths do so within a year, even with a −70% median drift. The hypothesis is only informative with a strict TGE definition, a higher threshold and a null benchmark.

### Cited Findings
- **Definitions differ across the studies cited:**
  - Memento: "TGE opening." — [Memento Research](https://mementoresearch.com/state-of-2025-token-launches-year-in-review)
  - Messari: "day-one closing price." — [AMBCrypto](https://ambcrypto.com/messari-data-shows-binances-2025-listings-down-71-on-average/)
  - Delphi: listing day, using CoinGecko daily closes. — [Journal du Coin](https://journalducoin.com/exchanges/listings-crypto-cex-2025-investisseurs-particuliers-50-cents-dollar-investi/)
  - CoinGecko's airdrop study: first trading price, inferred from its Jupiter example. — [CoinGecko](https://www.coingecko.com/research/publications/when-to-sell-airdrops)
  - CryptoNinjas: "price at listing" plus the listing-phase ATH. — [Cryptonomist](https://en.cryptonomist.ch/2025/03/31/the-98-of-new-tokens-listed-on-cex-experience-a-price-crash/)
  - Prediction markets use FDV "one day after launch," and pre-market trading prices tokens before TGE (LIT about $3.20, FDV >$3B). — [FXStreet](https://www.fxstreet.com/cryptocurrencies/news/traders-split-over-whether-lighters-lit-clears-3-billion-fdv-after-launch-202512301124)
- **Listing-day wicks.** 37% of 2024 CEX listings set their ATH on listing day and never beat it (46% on Binance, 60% on Bybit), after average listing-phase gains of +54% (+87% on Binance). If TGE price is the first print or open, a large share of tokens will have their "max after TGE" inside the TGE day itself. — [Cryptonomist](https://en.cryptonomist.ch/2025/03/31/the-98-of-new-tokens-listed-on-cex-experience-a-price-crash/)
- **Survivorship and selection.**
  - CryptoRank keeps only tokens with market cap >$100M on the measurement date. — [CryptoPotato](https://cryptopotato.com/the-harsh-reality-of-new-crypto-just-7-of-major-tokens-beat-their-launch-price/)
  - Delphi kept only 26 of 348 Gate.io listings to the end; the rest dropped out after collapse or illiquidity. — [Journal du Coin](https://journalducoin.com/exchanges/listings-crypto-cex-2025-investisseurs-particuliers-50-cents-dollar-investi/)
  - A perp DEX list built today will under-represent dead or sunset tokens such as VRTX unless they are added deliberately. — [The Block](https://www.theblock.co/post/361570/vertex-to-sunset-vrtx-token-move-perp-dex-onto-kraken-backed-ink-layer-2)
- **Averages vs medians, and weighting.**
  - Memento: equal-weighted −33.3% vs FDV-weighted −61.5% vs median −71.1%.
  - The perp DEX category: average +213% vs median −31% at N=3.
  - Source: [Memento Research](https://mementoresearch.com/state-of-2025-token-launches-year-in-review)
- **"Low FDV" in absolute vs relative terms.**
  - Memento's buckets are absolute dollars ($25–200M is the lowest). — [Memento Research](https://mementoresearch.com/state-of-2025-token-launches-year-in-review)
  - Binance Research recommends FDV-to-revenue and FDV-to-TVL instead. — [ForkLog](https://forklog.com/en/binance-highlights-155-billion-token-unlock-overhang/)
  - Binance's listing team judges valuation "relative to competitors in their respective sectors." — [The Informer Post](https://theinformerpost.beehiiv.com/p/binance-warns-against-low-float-high-valuation-coins-puts-out-call-for-small-projects-with-strong-fu)
  - The sector comp itself is expensive: HYPE at about 61x FDV/earnings vs about 25x for mature venues. — [CF Benchmarks](https://www.cfbenchmarks.com/blog/pricing-the-perp-dex-leader-a-valuation-framework-for-hyperliquid)
  - Volume-based comps can be contaminated by wash or incentive volume (Aster volume/TVL above 70:1; DefiLlama delistings). — [21Shares](https://www.21shares.com/research/the-perpetual-dex-wars-hyperliquid-aster-and-lighter-in-focus); [Cointelegraph](https://cointelegraph.com/news/defillama-delist-aster-perp-data-integrity)
- **Horizon and regime.** Memento measured 2025 launches at 20 Dec 2025, so each token had a different horizon, and all were measured after the Oct 2025 crash. CryptoRank and Delphi measured into a mid-2026 bear market. — [Memento Research](https://mementoresearch.com/state-of-2025-token-launches-year-in-review); [Cointelegraph (Jun 2026 low)](https://cointelegraph.com/news/bitcoin-etfs-biggest-outflows-june-btc-below-60k)

### Inferences
- **Monte Carlo null benchmark (my own calculation; not from any source).**
  - Setup: geometric random walk on daily closes, 200,000 paths, measured relative to the day-0 close. Drift is set so the median 180-day return is 0%, −50% or −70%; −70% is close to Memento's −71% median FDV change. Daily volatility is assumed at 5%, 8% or 12% (about 95–230% annualized). The volatility levels are assumptions, not sourced. Script: /tmp/claude-0/-home-user-test-claude/2ad751b0-58d6-5348-a96a-1b74151bb386/scratchpad/sim/maxsim.py
  - Results with a −70% median 180-day drift:

    | Daily vol | Any close >1.0x TGE close within 30d / 90d / 365d | Max ≥1.5x within 365d | Max ≥2x within 365d | Never closes above day 0 in 365d |
    |---|---|---|---|---|
    | 5% | 79% / 82% / 83% | 10% | 2% | 17% |
    | 8% | 84% / 87% / 89% | 38% | 20% | 11% |
    | 12% | 86% / 90% / 92% | 62% | 46% | 8% |

  - With zero drift and 8% vol: 97% exceed 1.0x, 77% reach 1.5x and 63% reach 2x within a year.
  - Implication: "max FDV after TGE > TGE FDV" at a 1.0x threshold, measured against the day-0 close, will come out "true" for most tokens even when they are steadily losing value. It cannot by itself distinguish low-FDV from high-FDV launches.
- **Front-loading beyond random-walk levels.** In the random walk, the 365-day ATH falls within the first 7 days for only about 14–29% of paths under negative drift. Empirically, 37% of 2024 CEX listings peaked on listing day alone. This suggests real launches front-load their peaks more than a random walk, through listing-day pumps. The comparison is approximate, since that study likely used intraday highs while my simulation uses daily closes.
- **Recommended operationalization for the perp DEX dataset.**
  1. Fix TGE FDV as the first-hour VWAP or the day-0 daily close on the main venue, and report the first-print open separately.
  2. Measure the maximum daily close (not intraday wick) from day 1 to day N (e.g., 30/90/180/365, and to today).
  3. Report the share reaching ≥1.0x, ≥1.5x, ≥2x and ≥3x of TGE FDV.
  4. Compare low-FDV vs high-FDV perp DEX launches, and both against the random-walk null and the Memento all-sector buckets.
  5. Tag each TGE with the Q3 regime window.
  6. Define "low FDV" both absolutely (e.g., below $200M, matching Memento's lowest bucket) and relatively: FDV/annualized fees vs HYPE's multiple at the time, and TGE FDV vs last private-round valuation.
  7. Include dead or sunset tokens (e.g., VRTX).
- **Recurring circulating supply.** Max FDV uses total supply, while market cap uses circulating supply. As tokens unlock, market cap can exceed its TGE level while FDV does not, or the reverse if supply is burned (e.g., Aster's reported supply cut, Hyperliquid's Assistance Fund HYPE treated as burned). The dataset should state which measure it uses.

### Gaps
- I found no published empirical distribution of daily volatility for newly launched perp DEX tokens, so the simulation's volatility parameters are assumptions.
- I found no source quantifying how often TGE-day intraday highs exceed the eventual post-TGE maximum daily close, for perp DEX tokens specifically.
- I found no source systematically comparing TGE FDV with last private-round valuations for perp DEX launches; the per-token team would have to collect this from fundraising announcements.
