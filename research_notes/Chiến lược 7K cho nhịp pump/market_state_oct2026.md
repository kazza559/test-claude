# Crypto market state, macro backdrop (13–17 Oct 2026) and catalyst calendar to end-Q1 2027

Snapshot timing: all exchange/API figures were pulled ~03:10–03:30 UTC on Sat 17 Oct 2026 (weekend, thin liquidity; last US trading day was Fri 16 Oct). Raw outputs are saved in `/tmp/claude-0/-home-user-test-claude/8ec8a334-85ed-54af-babc-62d7e4c0704b/scratchpad/research/market_state/data/` (btc_check_output_20261017.txt, collect_output.txt, extra_output.txt, implied_output.txt). Anything older than 2 weeks is flagged **[STALE]**.

## 1. What happened to BTC and crypto, 10–17 Oct 2026, and does the price structure in the premise check out?

### Takeaway
BTC chopped lower in an $80–84K box. On 15 Oct, after the hot CPI, it wicked to $79,775, and it now sits at ~$81.5K. That is right on its 50-day SMA, the US-ETF cost basis and CryptoQuant's 365-day MA. The premise's structure is confirmed by OKX data: low $57.8K on 1 Jul, higher low $62.3K on 1 Aug, leg up to a $87.2–87.4K double top (21 Sep / 2 Oct). BTC is now in a ~6.7% pullback. Alts fell 2–4x harder than BTC in the pullback.

### Cited Findings
- **Premise check (OKX BTC-USDT daily, UTC):** cycle intraday low $57,809 on 2026-07-01. Lowest daily close $58,628 on 2026-06-30. Higher low $62,268 on 2026-08-01. Aug–Oct high $87,399 on 2026-09-21, second high $87,238 on 2026-10-02. Last ~$81,520–81,565 on 2026-10-17 (−6.7% from the high, +41% from the low) — [OKX API daily candles](https://www.okx.com/api/v5/market/history-candles?instId=BTC-USDT&bar=1Dutc). The premise's Bitstamp low of $57.7K is consistent.
- **ATH:** $126,200 (OKX weekly, week of 6 Oct 2025); CoinGecko lists $126,080 on 2025-10-06. BTC is −35.4% from the ATH, and the 1 Jul low was −54% from it — [OKX API](https://www.okx.com/api/v5/market/candles?instId=BTC-USDT&bar=1Wutc), [CoinGecko markets API](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100). CryptoQuant cites $126,198 and K33 cites $126,272; the differences are venue effects — [Cointelegraph](https://cointelegraph.com/markets/bitcoin-bear-market-over-as-price-metric-copies-2023-recovery-cryptoquant-ceo), [Bitcoin.com/K33](https://news.bitcoin.com/k33-research-bitcoin-bear-market-bottom-60000-maximum-drawdown-2026/).
- **There was an earlier 2026 low near $60K in Feb.** Checkonchain describes two capitulations: ~$60K in Feb and ~$58K in Jun/Jul — [Bitget/Checkonchain](https://www.bitget.com/news/detail/12560605845575).
- **August breakout:** BTC went from $62,904 (16 Aug close) to $78,339 (21 Aug close), a weekly close jump of 62,904 → 77,743 (+23.6%) — [OKX API](https://www.okx.com/api/v5/market/history-candles?instId=BTC-USDT&bar=1Dutc). A second impulse ran from $76,419 (17 Sep close) to $86,618 (21 Sep close), right after the 16 Sep Fed hike — same source.
- **Daily path 9–17 Oct (OKX close):** 9 Oct $82,627 → 10 Oct $82,985 → 11 Oct $83,760 → 12 Oct $81,853 → 13 Oct $83,172 → 14 Oct (CPI) $81,683 (H 84,147 / L 81,453) → 15 Oct $82,232 (L **79,775**) → 16 Oct $81,618 → 17 Oct ~$81,520 (partial) — [btc_check output, OKX API](https://www.okx.com/api/v5/market/candles?instId=BTC-USDT&bar=1Dutc). Earlier swing low: $80,400 on 8 Oct.
- **Technicals (17 Oct):**
  - Moving averages: SMA20 $83,465 (price −2.3% vs it), SMA50 $81,358 (+0.2%), SMA100 $74,062 (+10.1%), SMA200 $72,465 (+12.5%).
  - Momentum: daily RSI14 46, weekly RSI14 56.5 (down from 63.3 two weeks earlier).
  - Bollinger (20): lower band $80,555, width 7.0%.
  - Source: [OKX API](https://www.okx.com/api/v5/market/candles?instId=BTC-USDT&bar=1Dutc)
- **Weekly closes (OKX):** 31 Aug wk $80,341; 7 Sep wk $76,836; 14 Sep wk $81,180; 21 Sep wk $84,479; 28 Sep wk $86,525; 5 Oct wk $83,760; current wk ~$81,520 (incomplete) — [OKX API](https://www.okx.com/api/v5/market/candles?instId=BTC-USDT&bar=1Wutc).
- **Price snapshots on 16 Oct:** Yahoo had BTC opening at $82,132; Fortune had ~$82,645 at 7:45am ET; CoinDesk had ~$81,310 at 12:08pm EDT. CoinDesk: "Bitcoin buyers snap up a brief drop below $80,000" — [Yahoo Finance](https://finance.yahoo.com/personal-finance/investing/article/bitcoin-and-ethereum-prices-today-friday-october-16-2026-bitcoin-ethereum-prices-firm-despite-two-strong-inflation-reports-113928147.html), [CoinDesk](https://www.coindesk.com/markets/2026/10/16/bitcoin-buyers-snap-up-a-brief-drop-below-usd80-000-as-asian-stocks-rebound).
- **Alt moves (OKX closes):**

  | Coin | 10 Oct → 17 Oct | 6 Oct → 17 Oct |
  |---|---|---|
  | BTC | −1.7% | −4.7% |
  | ETH | −3.2% | −10.0% |
  | SOL | −4.8% | −13.2% |
  | BNB | −3.8% | −7.4% |
  | LINK | −5.1% | −11.6% |
  | HYPE | −6.4% | −13.0% |
  | LIT | −11.6% | −15.7% |
  | XRP | −6.7% | −12.6% |
  | DOGE | −6.4% | −14.3% |

  Source: [OKX API](https://www.okx.com/api/v5/market/history-candles?instId=ETH-USDT&bar=1Dutc)
- **Total crypto market cap** $2.757T, BTC dominance 59.32% (CoinGecko, 03:24 UTC 17 Oct). CoinGecko showed a 24h change of −3.40%, which looks inconsistent with BTC's ~−0.6%; treat it with caution — [CoinGecko global API](https://api.coingecko.com/api/v3/global).

### Inferences
- **Retracement levels:**
  - The pullback has retraced only ~20% of the $57.8K→$87.4K leg.
  - Fibonacci levels for that full leg: 38.2% = ~$76.1K, 50% = ~$72.6K, 61.8% = ~$69.1K.
  - For the $62.3K→$87.4K leg: 38.2% = ~$77.8K, 50% = ~$74.8K, 61.8% = ~$71.9K.
  - A confluence zone sits at ~$72.5–75K: SMA200 $72.5K, SMA100 $74.1K, STH cost basis ~$74.4K (see §5), and the 50% retrace of the Aug leg.
- **Pattern:** two failed pushes at $87.2–87.4K (21 Sep, 2 Oct) with lower RSI on the second (74 → 63) form a short-term double top / bearish divergence. As long as $80K holds, the pullback is still a normal retest.

### Gaps
- I did not identify the specific catalyst for the 17–21 Aug +24% week. Time ran out; Glassnode Week 33–34 likely covers it.
- No Bitstamp-specific data was pulled; OKX was used as the reference venue.

## 2. Macro: CPI of 14 Oct, the Fed's 16 Sep decision, and pricing for the 28 Oct and Dec FOMC meetings; DXY, yields, equities, gold, oil

### Takeaway
The Fed **did hike** on 16 Sep 2026: +25 bp to 3.75–4.00%, a 12-0 vote, its first hike since July 2023, under Chair Kevin Warsh. September CPI came in hot: headline 3.7% y/y vs 3.6% expected, with energy/gasoline the main driver from the Iran-war oil shock. Core also beat on the month (0.3% vs 0.2%).
- **October meeting:** hike odds spiked to ~41–54%, then collapsed to ~13% after Warsh declined to signal a move.
- **December meeting:** a hike is the base case (~77% on Polymarket; ~71–89% across CME/Kalshi snapshots).

Macro is a headwind: US 10y ~5.1%, real 10y ~2.8%, Brent ~$127, DXY ~102. Equities are softening (Nasdaq −5% from its high), and gold is −26% from its January peak.

### Cited Findings
- **Fed, 16 Sep 2026:**
  - Target range raised to 3.75–4.00% by a 12-0 vote, the first hike since July 2023; the Fed had held at its first five meetings of 2026.
  - IORB 3.90%, effective 17 Sep; ON RRP 3.75%; standing repo 4.00%.
  - 16 of 18 participants expect at least one more 25 bp hike by year-end; the median year-end rate is ~4.1% (a 4.00–4.25% range).
  - Warsh said the standard for confidence on inflation "had not been satisfied."
  - Sources: [Fed implementation note PDF](https://www.federalreserve.gov/monetarypolicy/files/monetary20260916a1.pdf), [CNBC](https://www.cnbc.com/2026/09/16/fed-rate-decision-september-2026.html), [Fox Business](https://www.foxbusiness.com/economy/federal-reserve-interest-rate-decision-september-16-2026), [Advisor Perspectives](https://www.advisorperspectives.com/dshort/updates/2026/09/16/feds-interest-rate-decision-september-16-2026)
  - **This corrects nothing:** the earlier notes saying the Fed "hiked" are right.
- **Effective fed funds rate:** 3.88% (15 Oct) vs 3.63% before the hike — [FRED DFF](https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF).
- **September CPI (released Wed 14 Oct):**
  - Headline +0.6% m/m and **3.7% y/y** (Aug 3.4%; consensus ~3.6%).
  - Core +0.3% m/m (consensus 0.2%) and **2.6% y/y** (Aug 2.4%).
  - Gasoline +9.1% m/m, about half of the headline increase.
  - Sources: [CoinShares market update 16 Oct](https://coinshares.com/us/insights/research-data/market-update-16-10-2026/), [CBS News](https://www.cbsnews.com/news/september-cpi-report-inflation-energy-costs/), [CNBC](https://www.cnbc.com/2026/10/14/cpi-inflation-report-september-2026.html), [Kiplinger](https://www.kiplinger.com/investing/economy/cpi-report-september-2026-what-to-expect)
  - Yahoo notes PPI also came in strong ("two strong inflation reports") — [Yahoo Finance](https://finance.yahoo.com/personal-finance/investing/article/bitcoin-and-ethereum-prices-today-friday-october-16-2026-bitcoin-ethereum-prices-firm-despite-two-strong-inflation-reports-113928147.html).
- **September retail sales (15 Oct):** +0.8% vs ~0.3% expected, with August revised to +1.3%. Excluding gasoline, sales rose only 0.2% — [CoinShares](https://coinshares.com/us/insights/research-data/market-update-16-10-2026/).
- **Crypto reaction:**
  - BTC fell from >$83K before the release toward $80K. Peak liquidations came on 15 Oct: ~$948M in 24h across 177,440 traders, 90.6% of them longs (CoinGlass). ETH had the largest single-asset liquidations (~$283M) — [Crypto Adventure](https://cryptoadventure.com/bitcoin-and-ethereum-plunge-as-hot-u-s-cpi-sparks-nearly-1-billion-in-crypto-liquidations/), [Decrypt](https://decrypt.co/381044/bitcoin-whipsaws-crypto-liquidations-near-1-billion).
  - Another outlet reports a lower $483M — [Analytics Insight](https://www.analyticsinsight.net/news/bitcoin-and-ethereum-liquidations-hit-usd-483m-as-cpi-surges). A separate $771M flush happened as BTC lost $82K before the CPI release — [FinanceFeeds](https://financefeeds.com/771-million-liquidated-as-bitcoin-lost-82000-and-cpi-lands-wednesday/).
  - By 16 Oct BTC and ETH had stabilized near $82,000 and $2,445 — [Crypto Times](https://www.cryptotimes.io/2026/10/16/crypto-price-today-bitcoin-and-ethereum-recover-modestly-after-inflation-driven-dip/).
- **Odds of an October hike (FOMC decision 28 Oct, 2pm ET):**

  | Snapshot | Hike odds | Source |
  |---|---|---|
  | CME, before CPI | ~22% | [Investing.com](https://www.investing.com/analysis/fed-october-ratehike-odds-slide-below-22-ahead-of-minutes-200689107) |
  | CME, 12:20pm ET on 14 Oct | 41.5% | [FinanceFeeds](https://financefeeds.com/will-the-fed-hike-on-28-october-what-the-odds-did-after-a-3-7-cpi/), [Blockonomi](https://blockonomi.com/october-fed-rate-hike-odds-surge-to-43-as-u-s-cpi-inflation-hits-3-7) |
  | Intraday peaks, various sources | 41–54% | same as above |
  | Thursday 15 Oct | 27.7% | same as above |
  | Friday 16 Oct | 16.1% | same as above |
  | CME, 16 Oct | 12.7% hike / 87.3% hold | same as above |

  - The drop came after Warsh gave no sign of an imminent hike, and the dollar slid with it — [ActionForex](https://www.actionforex.com/action-insight/market-overview/657759-dollar-extends-slide-as-fed-warsh-refuses-to-revive-october-hike-bets/), [Invezz](https://invezz.com/news/2026/10/16/fed-rate-hold-odds-jump-to-85-even-as-warsh-offers-no-clues-on-policy-path).
  - **Conflict:** Mitrade reported 55–62% hike odds, which looks stale or wrong — [Mitrade](https://www.mitrade.com/insights/more/inflation/us-cpi-hot-core-266-october-hike-20261015J1352).
- **Prediction markets (API pull, 17 Oct ~03:20 UTC):**
  - Polymarket "Fed Decision in October?" ($44.7M volume): No change 86.5%, +25 bp 13.5%, +50 bp 0.35%.
  - Polymarket "Fed Decision in December?": +25 bp **76.5%**, no change 20.5%, +50 bp 2.65%.
  - Polymarket "Another Fed rate hike in 2026?": 79.5%. "How many hikes in 2026": 2 in total (Sep plus one more) 68%, 1 only 21.5%, 3 10.25%.
  - Source: [Polymarket gamma API](https://gamma-api.polymarket.com/public-search?q=Fed%20decision%20in%20October), [Polymarket](https://polymarket.com/event/fed-rate-hike-in-2026)
  - Kalshi October "Fed maintains rate": last 87¢ (bid 86 / ask 87), up from 71¢ the previous day — [Kalshi API](https://api.elections.kalshi.com/trade-api/v2/markets?event_ticker=KXFEDDECISION-26OCT). Polymarket was ~75/25 hold/hike on 15 Oct — [CoinShares](https://coinshares.com/us/insights/research-data/market-update-16-10-2026/).
- **Odds of a December hike (9 Dec), other venues:**
  - CME FedWatch: ~71% (Yahoo, ~15 Oct) and up to ~88.9% in another 16 Oct report.
  - Polymarket ~79% (Benzinga, 16 Oct); Kalshi ~70–75%.
  - Boston Fed's Susan Collins said rates should rise "a bit further" before year-end.
  - Sources: [Yahoo Finance](https://finance.yahoo.com/economy/policy/articles/fed-interest-rate-hike-seems-195052044.html), [Benzinga](https://www.benzinga.com/markets/prediction-markets/26/10/62408879/fed-rate-hike-odds-warsh-ai), [Kalshi](https://kalshi.com/markets/kxfeddecision/fed-meeting/kxfeddecision-26dec), [Yahoo/Collins](https://finance.yahoo.com/economy/policy/articles/susan-collins-says-rates-rise-180122241.html)
- **Rates:**
  - US 10y 5.10% (16 Oct) vs 4.48% on 1 Jul (+62 bp). 3-month high 5.31%; 5.28% on 7 Oct, so it eased ~18 bp this week.
  - US 2y 4.77% (vs 4.17% on 1 Jul). 10y real yield 2.78% (vs 2.25%; 3-month high 2.95%). 10y breakeven 2.35%.
  - Sources: [FRED DGS10](https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10), [FRED DGS2](https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS2), [FRED DFII10](https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFII10), [FRED T10YIE](https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10YIE), [Yahoo ^TNX](https://query1.finance.yahoo.com/v8/finance/chart/%5ETNX?range=3mo&interval=1d)
- **DXY:** 101.78 (16 Oct) vs 100.22 a month earlier and 100.73 in mid-July. The 3-month range is 98.77–102.58, with the high on 12 Oct — [Yahoo DX-Y.NYB](https://query1.finance.yahoo.com/v8/finance/chart/DX-Y.NYB?range=3mo&interval=1d). The broad trade-weighted USD index was 121.60 on 9 Oct vs 118.66 on 1 Sep — [FRED DTWEXBGS](https://fred.stlouisfed.org/graph/fredgraph.csv?id=DTWEXBGS).
- **Equities:**
  - S&P 500 7,659 (16 Oct), −2.0% from its 3-month high of 7,819.
  - Nasdaq Composite 26,140 (16 Oct), −5.3% from its 3-month high of 27,600, and −3.9% from 13 Oct (27,204) to 16 Oct.
  - VIX 16.5 (15 Oct). HY OAS 3.23% (15 Oct) vs 2.65% on 1 Sep.
  - Sources: [Yahoo ^GSPC](https://query1.finance.yahoo.com/v8/finance/chart/%5EGSPC?range=3mo&interval=1d), [Yahoo ^IXIC](https://query1.finance.yahoo.com/v8/finance/chart/%5EIXIC?range=3mo&interval=1d), [FRED VIXCLS](https://fred.stlouisfed.org/graph/fredgraph.csv?id=VIXCLS), [FRED BAMLH0A0HYM2](https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2)
- **Gold:** futures $4,186.70 (16 Oct) vs $4,399.70 on 17 Sep. The 3-month high is $4,697.80. PAXG peaked at $5,682.92 on 29 Jan 2026, so gold is ~−26% from that peak — [Yahoo GC=F](https://query1.finance.yahoo.com/v8/finance/chart/GC%3DF?range=3mo&interval=1d), [Coinbase PAXG-USD](https://api.exchange.coinbase.com/products/PAXG-USD/candles?granularity=86400).
- **Oil:**
  - Brent spot $126.55 (14 Oct) vs $69.24 on 1 Jul; 3-month peak $135.51; $130.80 on 15 Sep.
  - WTI spot $101.91 (14 Oct). WTI futures $99.04 (16 Oct), up from $88.28 on 7 Oct.
  - Sources: [FRED DCOILBRENTEU](https://fred.stlouisfed.org/graph/fredgraph.csv?id=DCOILBRENTEU), [FRED DCOILWTICO](https://fred.stlouisfed.org/graph/fredgraph.csv?id=DCOILWTICO), [Yahoo CL=F](https://query1.finance.yahoo.com/v8/finance/chart/CL%3DF?range=3mo&interval=1d)
  - The energy spike is tied to the US–Iran war and disruption in the Strait of Hormuz. Goldman warned Brent stays >$100 if the Hormuz closure drags on — [Yahoo/Goldman](https://finance.yahoo.com/sectors/energy/articles/brent-stay-above-100-2026-003121731.html), [Libnanews](https://live.libnanews.com/event/ev-1783897177759-427d).

### Inferences
- Crypto is fighting a **hiking** Fed (rate rising toward 4.00–4.25% by December), a 10y yield above 5%, real yields near cycle highs, and a renewed oil shock. In past cycles, new BTC uptrends came with easing liquidity, so a macro tailwind for a "next leg up" is absent in Q4 2026.
- The bull case therefore rests on crypto-native factors: exhausted sellers, on-chain cost-basis support and alt rotation. Macro is not supportive.
- The cleanest macro tailwind would be a peace deal or oil collapse that pulls headline CPI and December hike odds down.
- Post-CPI, BTC fell ~4% peak-to-trough and recovered within 24h, and the October hike scare faded quickly. This is mild resilience. With December now ~77% priced, a hike there is largely expected; a *hold* would be a positive surprise.

### Gaps
- Consensus for headline CPI m/m and core y/y was not found, nor the actual September PPI figures.
- No live CME FedWatch reading for December could be fetched directly; the numbers above are press snapshots.
- No direct October 2026 article on the state of the Iran war or Hormuz was found (latest found: August). Oil prices come from FRED/Yahoo.

## 3. ETF flows (BTC, ETH, SOL, XRP, HYPE) over the last 4–8 weeks, cumulative totals, and corporate treasury buyers

### Takeaway
US spot BTC ETFs took in nearly **$3B between 21 Sep and 6 Oct**, the fastest pace since Nov 2025. Since 7 Oct they have bled roughly **−$0.85B**. The cumulative total is ~$57.0B (SoSoValue, 15 Oct).
- ETH ETFs had a 9-day outflow streak totalling −$697M.
- SOL ETFs posted their first weekly outflow after 14 straight inflow weeks.
- XRP ETFs are flat; global crypto ETPs lost $434M in the CPI week.

Corporate buyers have essentially stalled: Strategy is buying only ~250–334 BTC a week with mNAV ~1.0x and is repurchasing preferreds instead, and Metaplanet is doing share buybacks.

### Cited Findings
- **BTC ETF flows, recent weeks:**
  - 21 Sep–6 Oct: "nearly $3B" net inflows, the fastest since Nov 2025. 7–12 Oct: ~−$760M — [Glassnode Week 41](https://research.glassnode.com/the-week-onchain-week-41-2026/).
  - Week of 5–9 Oct: −$678.9M, including −$484.9M on 7 Oct (Farside; SoSoValue shows −$487.07M) — [CryptoTicker](https://cryptoticker.io/en/crypto-etf-outflows-october-2026-bitcoin-ethereum/), [TokenPost](https://www.tokenpost.com/news/investing/27831).
- **BTC ETF daily flows, 12–16 Oct (Farside via press):**

  | Date | Net flow | Detail |
  |---|---|---|
  | 12 Oct | −$65.4M | |
  | 13 Oct | +$175.7M | FBTC +$103.1M, IBIT +$65.9M |
  | 14 Oct | −$261.4M | FBTC −$152.7M, IBIT −$110.9M |
  | 15 Oct | +$5.1M | IBIT +$16.8M |
  | 16 Oct | −$10.6M | partial, FBTC only |
  | **Week so far** | **≈ −$156.6M** | |

  Sources: [Farside](https://farside.co.uk/btc/), [Farside on X](https://x.com/FarsideUK/status/2110596559943430187), [The Coin Republic](https://www.thecoinrepublic.com/2026/10/15/bitcoin-etfs-bleed-262m-as-btc-sinks-below-81k-whats-next/), [Blockchain.news](https://blockchain.news/flashnews/bitcoin-etfs-261m-net-outflow-oct-14), [KuCoin flash](https://www.kucoin.com/news/flash/bitcoin-etfs-see-175-6m-inflows-on-october-13), [Crypto Economy](https://crypto-economy.com/bitcoin-etfs-add-5-1m-as-ether-funds-lose-60-3m/). Farside's site blocked direct fetching (Cloudflare), so these come from press citations of its table.
- **BTC ETF cumulative net inflows:**
  - **$56.96B** as of 15 Oct (SoSoValue) — [KuCoin/SoSoValue](https://www.kucoin.com/news/flash/bitcoin-spot-etfs-see-5-06m-net-inflow-blackrock-s-ibit-leads-with-16-79m), [TokenPost](https://www.tokenpost.com/news/investing/33082).
  - $57.68B as of 13 Oct (Alpha Finance/The Block) — [Crypto Briefing](https://cryptobriefing.com/spot-bitcoin-etfs-inflows-ether-etfs-october/).
  - **Conflict:** a SoSoValue-based TokenPost item shows $61.23B after 7 Oct and then $57.1B by 9 Oct. A $4B drop in two days is inconsistent with the daily flows, so treat $61.23B as erroneous — [TokenPost](https://www.tokenpost.com/news/investing/27831).
- **ETF cost basis:** Glassnode puts the US spot ETF cost basis at ~$81.5K. BTC dipped below it intraday on 8 and 13 Oct but closed back above — [Glassnode Week 41](https://research.glassnode.com/the-week-onchain-week-41-2026/). Checkonchain data via CoinDesk puts it at $82,300 (7 Oct) — [CoinDesk](https://www.coindesk.com/markets/2026/10/07/bitcoin-s-recovery-stalls-just-short-of-rescuing-its-last-underwater-cohort).
- **ETH ETFs:**
  - A 9-day outflow streak from 29 Sep totalled −$697.2M; October losses were ~−$635M at the time of reporting.
  - The streak broke on 13 Oct (+$24.8M). Outflows resumed with −$60.3M on 15 Oct.
  - Sources: [24/7 Wall St.](https://247wallst.com/investing/cryptocurrency/2026/10/14/ethereum-etfs-just-broke-a-ten-day-outflow-streak-solana-etfs-are-still-bleeding-which-one-turns-next/), [Crypto Economy](https://crypto-economy.com/bitcoin-etfs-add-5-1m-as-ether-funds-lose-60-3m/)
  - A weekly ETH ETF outflow of −$542.2M is reported (week not specified) — [TokenPost](https://www.tokenpost.com/news/investing/29615).
- **SOL ETFs:** five straight days of outflows; October net −$24.8M, the first weekly outflow after 14 consecutive inflow weeks — [24/7 Wall St.](https://247wallst.com/investing/cryptocurrency/2026/10/14/ethereum-etfs-just-broke-a-ten-day-outflow-streak-solana-etfs-are-still-bleeding-which-one-turns-next/), [The Token Press](https://www.thetokenpress.com/article/ether-and-solana-etfs-end-the-week-with-broad-outflows-99355229). A cumulative figure of $137.9M appears in a single aggregator post and is **unverified** (it looks low).
- **Combined alt ETFs on 15 Oct:** XRP, SOL and ETH ETFs lost −$71M combined while BTC took +$5.1M — [KuCoin flash](https://www.kucoin.com/news/flash/xrp-solana-and-ethereum-etfs-see-71m-outflow-bitcoin-etfs-attract-5-1m-inflow).
- **XRP ETFs:** cumulative net inflows $1.803B against net assets of $1.509B (SoSoValue, 14 Oct); demand has slowed sharply — [TokenPost](https://www.tokenpost.com/news/investing/32722), [24/7 Wall St.](https://247wallst.com/investing/cryptocurrency/2026/10/15/bitcoin-and-ethereum-etfs-lost-391-million-in-a-day-only-xrp-etfs-took-money-in/).
- **HYPE ETFs are live.** Grayscale HYPG was declared effective on 2 Jun 2026. As of 5 Jun, AUM was 21Shares $66M, Bitwise $88M and Grayscale $4.5M **[STALE: June]** — [CNBC](https://www.cnbc.com/2026/06/06/bitcoin-price-crash-crypto-hype-hyperliquid-etfs.html), [TradingView](https://www.tradingview.com/news/99Bitcoins:b56741d57094b:0-grayscale-hyperliquid-etf-imminent-per-new-filing/).
- **Global crypto ETPs (CoinShares):** −$434M of outflows in the week to 16 Oct, attributed to the hot CPI and hawkish repricing. CoinShares calls the setup "difficult rather than fundamentally bearish" — [CoinShares](https://coinshares.com/us/insights/research-data/market-update-16-10-2026/), [Crypto Briefing](https://cryptobriefing.com/coinshares-434m-outflows-cpi-rise/).
- **Strategy (MSTR):**
  - Bought 334 BTC ($28.7M) on 1–4 Oct and 250 BTC (~$21M, funded by MSTR stock sales plus cash) on 5–11 Oct.
  - Holds **848,250 BTC** at an average cost of **$75,444**, about $64B in total.
  - Over the same week it **repurchased $192.4M of STRC preferred stock**.
  - Sources: [SEC 8-K](https://www.sec.gov/Archives/edgar/data/0001050446/000119312526413164/mstr-20261005.htm), [SEC 8-K ex99](https://www.sec.gov/Archives/edgar/data/0001050446/000119312526419726/mstr-ex99_1.htm), [Yahoo Finance](https://finance.yahoo.com/markets/crypto/articles/strategy-acquires-250-bitcoin-repurchases-125404222.html)
- **Strategy mNAV:** ~**1.01x** on 15 Oct (52-week range 0.95–1.43x; stock ~$150) — [mnav.com](https://www.mnav.com/mnav/strategy). mNAV readings depend on the definition: basic 0.81x vs enterprise 1.09x on 8 Sep — [BitMEX](https://www.bitmex.com/blog/mstr-mnav-guide).
- **K33 on Strategy (13–14 Oct):**
  - STRC financing added only 4,947 BTC versus the counterfactual, but added $725M a year in dividends (~8,740 BTC at $83K). Total preferred dividend obligations are now $1.56B a year, up from $830M.
  - Cash covers ~42 months of dividends, which lowers the risk of forced sales.
  - Sources: [The Block](https://www.theblock.co/news/markets/2026-10-14-strategys-preferred-stock-financing-may-cost-it-bitcoin-k33-argues-418543), [Crypto Times](https://www.cryptotimes.io/2026/10/15/strategys-strc-bet-added-just-4947-bitcoin-k33-says-dividends-erase-gain-in-7-months/)
- **Metaplanet:**
  - Stock is ~−90% from its peak.
  - Bought back 73.98M shares for ¥19.3B (~$122M), filed 14 Oct. This is the first tranche of a ¥60B (~$379M) authorization.
  - Plans ~¥52B of zero-coupon convertible bonds due 2031 to repay BTC-backed loans. Those loans stood at 17.7% of BTC NAV, above its 10% guideline.
  - Sources: [Crypto Times](https://www.cryptotimes.io/2026/10/15/metaplanet-completes-122m-share-buyback-as-bitcoin-firm-issues-convertible-bond/), [CryptoSlate](https://cryptoslate.com/metaplanet-unveils-380-million-share-buyback-after-stock-crashes-nearly-90-from-peak/), [crypto.news](https://crypto.news/metaplanet-seeks-340m-to-repay-loans-buy-shares/)

### Inferences
- **Net ETF flow since 21 Sep is still positive.** My arithmetic: ~+$3B, minus ~$0.76B (7–12 Oct), minus ~$0.09B (13–16 Oct) ≈ **+$2.1B**. The ETF bid has turned from a tailwind into a mild headwind since 7 Oct, but there is no capitulation-type redemption wave.
- **The ETF cost basis matters.** At ~$81.5–82.3K it is the key "pain line": a sustained close below it puts the average ETF holder underwater.
- **The corporate bid is gone for now.** With mNAV ≈ 1.0x, issuing stock to buy BTC is not accretive. Strategy (~584 BTC in 2 weeks) and Metaplanet are spending on buybacks and debt management instead. The risk is not forced selling (42 months of dividend coverage), but there is no marginal treasury buyer.
- **ETH ETFs are a drag on ETH/BTC.** Persistent ETH ETF outflows match ETH/BTC falling from 0.0327 to 0.0298 (§7).

### Gaps
- Exact weekly BTC ETF totals for mid-Aug to 20 Sep, cumulative ETH and SOL ETF totals, and HYPE ETF flows since June could not be verified: Farside/SoSoValue are blocked or need an API key.

## 4. Stablecoin supply (total, USDT, USDC) over the last 90 days; exchange balances

### Takeaway
Stablecoin supply is **flat**:
- **Total:** $306.6B, +1.2% over 90 days and +0.7% over 30 days, but −2.5% from the May peak (~$316B).
- **USDT:** flat ($183.5B).
- **USDC:** shrinking ($72.7B, −1.4% over 30 days, −7.1% over 180 days).

This is not the expanding-liquidity backdrop that typically fuels a sustained alt leg. Exchange BTC reserves keep falling (~2.67M BTC, −1.7% since mid-September), which is mildly supportive.

### Cited Findings
- **Total stablecoins:**
  - **$306.58B** on 17 Oct.
  - Change over time: 7d −0.36% (−$1.1B); 30d +0.66% (+$2.0B); 60d +1.85%; 90d +1.24% (+$3.8B); 180d −2.48% (−$7.8B); 365d +0.36%.
  - Path: peak ~$316.4B (13 May) → trough ~$300.4B (5 Aug) → $308.0B (30 Sep) → $307.8B (14 Oct).
  - Source: [DefiLlama stablecoins API](https://stablecoins.llama.fi/stablecoincharts/all)
- **USDT:** **$183.45B** on 17 Oct; 30d +0.11%, 90d −0.32%, 180d −2.02%. Peak ~$189.7B in mid-May — [DefiLlama USDT](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=1).
- **USDC:** **$72.74B** on 17 Oct; 30d −1.41% (−$1.0B), 90d −0.87%, 180d −7.09% (−$5.5B), 365d −3.87% — [DefiLlama USDC](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=2).
- **Smaller stablecoins, 30-day changes:** USDS +8.7% ($7.05B), USDe −0.7% ($4.70B), USD1 −7.1% ($4.05B), PYUSD +1.2% ($2.83B), BUIDL −17.6% ($2.17B) — [DefiLlama list](https://stablecoins.llama.fi/stablecoins?includePrices=true).
- **Exchange BTC reserves (CryptoQuant):**
  - ~2.67M BTC on 12 Oct; ~2.68M per Cointelegraph (14 Oct).
  - −1.7% from ~2.726M on 20 Sep, and down ~130K BTC since Feb 2026 (~2.8M).
  - Sources: [CryptoQuant quicktake](https://cryptoquant.com/insights/quicktake/6accf67df987b352c7f6d479-BTC-Supply-on-Exchanges-Continues-to-Shrink), [Cointelegraph](https://cointelegraph.com/markets/cryptoquant-charts-bitcoin-uptober-thesis-valid), [BigGo/CryptoQuant](https://finance.biggo.com/news/1cd4dab0-1d3f-4342-a663-4de2ac1158b5)

### Inferences
- **Stablecoin "dry powder" has not grown with price.** BTC is +41% from its low while total stablecoins are +2% from their August trough. The rally has been driven more by repositioning (short covering, ETF flows) than by fresh fiat inflows.
- **USDC shrinkage hints at a weaker US bid.** USDC is the US-regulated rail, so its decline is consistent with a ~0% Coinbase premium (§6).
- **Exchange reserves:** falling balances reduce immediately sellable supply. The trend is gradual and does not offset weak new-money inflow.

### Gaps
- No exchange-balance data for stablecoins or ETH was obtained.
- The CryptoQuant figures come from secondary write-ups; the dashboard was not accessed directly.

## 5. On-chain valuation: realized price, STH cost basis, MVRV, percent of supply in profit — where does ~$81.5K sit?

### Takeaway
$81.5K sits in the **upper-middle of the on-chain bands**:
- About **+52% above realized price** (~$53.4K), so MVRV is ~1.5.
- About +3–5% above the True Market Mean (~$78–79K).
- About +9–10% above the STH cost basis (~$74.4K).
- **Right at** the ETF cost basis (~$81.5–82.3K) and CryptoQuant's 365-day MA (~$81.7K).
- About 7% below the overhead 2025-buyer / 6–12-month cost basis (~$88K).

About 68% of supply is in profit. Glassnode calls this "boxed in": support at $80–81.5K, then $78K; heavy supply at $88K and $100K.

### Cited Findings
- **bitcoin-data.com metrics (free tier, delayed; as of 10 Oct unless noted):**
  - Realized price **$53,420**; STH realized price **$74,398**; LTH realized price **$48,755**; True Market Mean **$79,161**.
  - MVRV **1.554**; STH-MVRV **1.115**; NUPL 0.357; SOPR 1.005; STH-SOPR 1.002; Puell 1.135.
  - Supply in profit **13.73M BTC** (16 Oct).
  - Source: [bitcoin-data.com API](https://bitcoin-data.com/v1/realized-price/last) (also /sth-realized-price, /mvrv, /supply-profit, /true-market-mean)
- **Percent of supply in profit ≈ 68.3%:** 13.73M ÷ 20.10M circulating supply (CoinGecko) — [CoinGecko markets API](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100). This is my derived figure.
- **Glassnode Week 41 (14 Oct; data as of 13 Oct):**
  - True Market Mean ~$78K; price has been above it, and above the STH cost basis, since 18 Sep.
  - US ETF cost basis ~$81.5K.
  - 6–12-month holder cost basis ~$88K (price rose to it in January, then fell more than a third).
  - 1–2-year holder cost basis ~$100K (met in May, then −25%).
  - The 30 Jun low close was "about a tenth above" realized price.
  - LTH realized loss peaked on 12 Aug and has since fallen ~85%. Profit-spent coins outnumber loss-spent ~4:1 since late August, versus 12:1 loss-dominant at the June low.
  - Liquidation clusters sit just under $80K and near $88K. The biggest Binance spot bid wall is at $80K.
  - Source: [Glassnode Week 41](https://research.glassnode.com/the-week-onchain-week-41-2026/)
- **Checkonchain cohort cost bases (via CoinDesk, 7 Oct):** 2025 buyers ~$88K (the only yearly cohort still underwater); ETF cost basis $82,300; 2023 cohort ~$65K (recurring support) — [CoinDesk](https://www.coindesk.com/markets/2026/10/07/bitcoin-s-recovery-stalls-just-short-of-rescuing-its-last-underwater-cohort).
- **CryptoQuant's 365-day MA** (its bull/bear dividing line) is ~**$81,700**; a sustained close above it "would confirm the new phase" — [Cointelegraph](https://cointelegraph.com/markets/bitcoin-bear-market-over-as-price-metric-copies-2023-recovery-cryptoquant-ceo), [CryptoBreaking](https://www.cryptobreaking.com/cryptoquant-ceo-says-bitcoin-bear/).
- **Older STH cost basis [STALE]:** Glassnode Week 33 (mid-Aug) had ~$68.5K and Week 32 ~$68.7K — [Glassnode Week 33](https://research.glassnode.com/the-week-onchain-week-33-2026/).

### Inferences
- **Distance from $81.5K to each level (my calc):**

  | Level | Price | $81.5K vs level |
  |---|---|---|
  | Realized price | $53.4K | +52.6% |
  | LTH realized price | $48.8K | +67% |
  | STH realized price | $74.4K | +9.5% |
  | True Market Mean | $78–79.2K | +3–4.5% |
  | ETF cost basis | $81.5–82.3K | ±0 / −1% |
  | 365-day MA | $81.7K | ±0 |
  | 6–12m / 2025 cohort cost basis | $88K | −7.4% |
  | 1–2y cohort cost basis | $100K | −18.5% |

- **Valuation is mid-cycle, not a bottom zone.** MVRV ~1.5 and NUPL ~0.36 compare with the July low, where MVRV was ~1.1, price was ~10% above realized price, and F&G was 12. BTC is no longer "cheap" on these metrics.
- **The bull case is that the cycle never closed below realized price**, which happened in 2015, 2018 and 2022. On that reading, the ~$58K low (MVRV ~1.1) may have been a shallower-than-usual bottom.
- **The STH cost basis (~$74.4K) is the classic bull-market line.** In bull phases, pullbacks typically hold above it; losing it on a closing basis would put recent buyers at a loss and has historically marked a failed recovery.
- **Overhead supply:** the $88K and $100K cohorts are break-even sellers above, which explains the twice-rejected $87.2–87.4K highs.

### Gaps
- Real-time (last-7-day) on-chain values need paid subscriptions; the bitcoin-data.com figures are lagged to 10 Oct, and CoinMetrics' community API returned 403.
- A CryptoQuant STH cost basis of ~$78.25K (7 Oct) appeared in a search summary without a traceable source, so it is not used. Methodologies differ: Glassnode and CryptoQuant cohort definitions vary.

## 6. Derivatives and sentiment: funding, open interest, options skew/DVOL, large expiries and max pain, Fear & Greed, Coinbase premium

### Takeaway
Positioning is **neutral-to-cautious, not washed out**:
- **Funding:** low but positive.
- **Open interest:** stayed near cycle highs through the pullback; the ~$1B in liquidations did not flush it.
- **Retail accounts:** increasingly long (OKX L/S 0.98 → 1.79), while takers are net sellers.
- **Options:** put skew is bid (25-delta RR −3.7 vol pts for 30 Oct), DVOL is rising (34.6 → 37.6), and max pain sits *below* spot for the big expiries ($79K on 30 Oct, $75K on 25 Dec).
- **Sentiment:** F&G is still "Greed" (55), with no fear reset.
- **Coinbase premium:** ~0%.
- **Market-implied odds:** options price only **~8% odds of BTC > $100K at the 25 Dec expiry** and ~18% at the 26 Mar 2027 expiry. Polymarket prices a $100K *touch* in 2026 at ~19.5%.

### Cited Findings
- **Funding:**
  - OKX BTC-USDT-SWAP: last 0.0100% per 8h; 3-day average 0.0060%; 7-day average 0.0033% (≈3.6% annualized); ~33-day average 0.0042%. 15 of the last 100 periods were negative — [OKX API funding](https://www.okx.com/api/v5/public/funding-rate-history?instId=BTC-USDT-SWAP&limit=100).
  - Hyperliquid BTC: 0.00125%/h now (= the 11% APR baseline); 7-day average 6.4% APR — [Hyperliquid API](https://api.hyperliquid.xyz/info).
  - ETH on OKX: 7-day average 0.0020% per 8h. SOL on OKX: last −0.0007%, with 29 of 100 periods negative — [OKX API](https://www.okx.com/api/v5/public/funding-rate-history?instId=ETH-USDT-SWAP&limit=100).
- **Hyperliquid watchlist (17 Oct):**

  | Coin | Funding now (APR) | 7-day avg funding (APR) | Open interest |
  |---|---|---|---|
  | HYPE | +8.3% | +9.8% | $1.59B |
  | LINK | +1.5% | +7.9% | $61M |
  | SOL | +0.4% | +5.9% | $569M |
  | ETH | +2.1% | +4.8% | $2.61B |
  | BNB | +8.0% | +4.6% | $46M |
  | LIT | **−10.6%** (shorts paying) | +0.2% | $133M |

  Total Hyperliquid perp OI is $11.33B. KNTQ is not a Hyperliquid perp. Source: [Hyperliquid API metaAndAssetCtxs/fundingHistory](https://api.hyperliquid.xyz/info)
- **Open interest:**
  - OKX BTC contract OI was $3.30B on 16 Oct, vs $3.40B on 22 Sep, a July trough of ~$2.49B (9 Jul) and $3.71B in early May. OI held at $3.2–3.36B through the 7–16 Oct decline — [OKX API OI](https://www.okx.com/api/v5/rubik/stat/contracts/open-interest-volume?ccy=BTC&period=1D).
  - Hyperliquid BTC OI 41,146 BTC (~$3.35B); premium −0.031% — [Hyperliquid API](https://api.hyperliquid.xyz/info).
- **Retail positioning and taker flow (OKX):**
  - Long/short account ratio rose from 0.98 (5 Oct) to 1.79 (16 Oct) — [OKX API L/S](https://www.okx.com/api/v5/rubik/stat/contracts/long-short-account-ratio?ccy=BTC&period=1D).
  - Taker buy/sell ratio was 0.94–0.97 on most days from 12–16 Oct, i.e. net taker selling — [OKX API taker volume](https://www.okx.com/api/v5/rubik/stat/taker-volume?ccy=BTC&instType=CONTRACTS&period=1D).
- **Futures basis (Deribit, annualized):** 30OCT26 7.0%; 6NOV26 6.3%; 27NOV26 5.8%; 25DEC26 5.7%; 26MAR27 5.4% — moderate contango, not frothy — [Deribit API](https://www.deribit.com/api/v2/public/get_book_summary_by_currency?currency=BTC&kind=future).
- **Implied volatility:**
  - BTC DVOL 37.6 on 17 Oct, up from 34.6 (25 Sep) and 34.8 (2 Oct). The 120-day range is 33.1–49.1; it hit 43.3 on 21 Aug. ETH DVOL 51.4 (up from 47.5 on 6 Oct).
  - Source: [Deribit DVOL API](https://www.deribit.com/api/v2/public/get_volatility_index_data?currency=BTC&resolution=1D)
- **Deribit BTC options, total OI 392,946 BTC (~$32.0B notional):**
  - **30OCT26** (Fri; the "31 Oct" expiry in the brief is actually Fri 30 Oct on Deribit): $12.20B notional; P/C OI 0.52; **max pain $79,000**. Largest call OI at 95K (25,571 BTC), 90K (15,250) and 100K (14,338). Largest put OI at 70K (4,142), 72K and 75K.
  - **27NOV26:** $2.18B; P/C 0.57; max pain $81,000.
  - **25DEC26** (Fri; the brief's "26 Dec" = Deribit's 25 Dec quarterly): $10.67B; P/C 0.61; **max pain $75,000**. Largest calls at 80K (8,684), 100K and 120K. Largest puts at 60K (6,794), 40K (5,032) and 55K.
  - **26MAR27:** $3.41B; P/C 0.64; max pain $76,000.
  - Source: [Deribit API book summary](https://www.deribit.com/api/v2/public/get_book_summary_by_currency?currency=BTC&kind=option)
- **25-delta risk reversal (call IV minus put IV, BTC):**

  | Expiry | 25d RR | ATM IV |
  |---|---|---|
  | 30 Oct | −3.7 vol pts | ~32.7 |
  | 27 Nov | −2.6 | n/a |
  | 25 Dec | −2.6 | ~36.2 |
  | 26 Mar 2027 | −1.6 | n/a |

  ETH 25d RR for 30 Oct is −2.7. ETH max pain is $2,500 for 30 Oct and $2,200 for 25 Dec. Source: [Deribit API ticker](https://www.deribit.com/api/v2/public/ticker?instrument_name=BTC-25DEC26-100000-C)
- **Options-implied (risk-neutral) probability that BTC is above each level *at expiry*** (call-spread digitals from Deribit marks, ~03:10 UTC 17 Oct):

  | Level | 30 Oct | 25 Dec | 26 Mar 2027 | 25 Jun 2027 |
  |---|---|---|---|---|
  | >$60K | n/a | 96% | 88% | n/a |
  | >$70K | n/a | 83% | 73% | n/a |
  | >$75K | 91% | n/a | n/a | n/a |
  | >$80K | 62% | 54% | n/a | n/a |
  | >$87K | 13% | 34% | n/a | n/a |
  | >$90K | 5% | 23% | 32% | n/a |
  | >$100K | ~0% | **8%** | **18%** | 23% |
  | >$110K | n/a | 2% | 9% | n/a |
  | >$126K | n/a | 1% | 3% | n/a |

  Source: [Deribit API](https://www.deribit.com/api/v2/public/get_book_summary_by_currency?currency=BTC&kind=option); computation in implied_output.txt.
- **Polymarket, BTC (17 Oct API pull):**
  - "What price will Bitcoin hit in 2026?" (touch by 31 Dec; $76M volume): ↑$95K 34.5%; ↑$100K **19.5%**; ↑$110K 10%; ↑$120K 5.5%.
  - Downside strikes (apparently newer markets measured from their creation date; resolution rules not verified): ↓$70K 39%, ↓$65K 22.5%, ↓$60K 16.5%.
  - "What price will Bitcoin hit in October?": ↑$87.5K 28.5%; ↑$90K 17.5%; ↑$95K 4%; ↓$77.5K 44.5%; ↓$75K 25.5%; ↓$70K 8%.
  - Source: [Polymarket gamma API](https://gamma-api.polymarket.com/public-search?q=What%20price%20will%20Bitcoin%20hit%20in%202026)
- **Fear & Greed (alternative.me):**
  - 17 Oct **55 ("Greed")**; 16 Oct 63; 15 Oct 53 ("Neutral"); 14 Oct 62; 12 Oct 69; 6 Oct 73.
  - 60-day min 46 (19 Aug), max 78 (22 Sep), average 66.5; 30-day average 67.
  - Around the cycle low: 12 on 29 Jun; 22 in early July; 25–30 through late Jul–early Aug (90-day min 25).
  - Source: [alternative.me API](https://api.alternative.me/fng/?limit=120)
- **Coinbase premium** (my proxy: Coinbase BTC-USD vs OKX BTC-USDT × USDT-USD, hourly): daily averages of −0.007% to +0.003% from 5–17 Oct, i.e. **~0%** — [Coinbase API](https://api.exchange.coinbase.com/products/BTC-USD/candles?granularity=3600), [OKX API](https://www.okx.com/api/v5/market/candles?instId=BTC-USDT&bar=1H&limit=300).

### Inferences
- **The pullback has not reset leverage or sentiment.** OI held up, retail long ratios rose, and F&G stayed in Greed. That leaves room for a deeper flush toward ~$75–78K (the True Market Mean / put-OI zone).
- **Options traders are hedging downside, not chasing upside.** Negative skew, max pain at $79K for 30 Oct and $75K for 25 Dec, and DVOL rising from lows all point the same way.
- **Pinning risk around 30 Oct:** with $12.2B expiring and the FOMC on 28 Oct two days earlier, a pull toward $79–80K is plausible.
- **Market-implied odds challenge the user's plan (sell above $100K by Q1 2027).** Options and Polymarket put $100K by 25 Dec at ~8% (terminal) / ~20% (touch), and by late March 2027 at ~18% (terminal). A rough rule is touch ≈ 2× terminal, which implies a ~30–35% chance of touching $100K by the end of March 2027. These are risk-neutral, not forecasts, but they are well below a "next leg is coming" base case.
- **Funding is not the main cost for longs right now.** Hyperliquid funding is near the 11% APR baseline for BTC/HYPE and lower for SOL/ETH. LIT's negative current funding means shorts are crowded there.

### Gaps
- No aggregated cross-exchange OI or liquidation heatmaps (CoinGlass needs an API key) and no CME basis or OI were obtained.
- The Coinbase premium is my own proxy, not CryptoQuant's index.
- A 60-day history of options skew was not pulled; only today's snapshot.

## 7. Market structure: BTC dominance, ETH/BTC, TOTAL2/TOTAL3, altcoin season, and alts vs BTC since the July low

### Takeaway
Alts behaved like high beta in the recovery:
- 74% of a 47-coin basket beat BTC over 90 days, just under the classic 75% "altseason" threshold.
- But the last 30 days are mixed (24 of 50 top alts beat BTC) and the 200-day picture is BTC-led (19 of 50).
- ETH/BTC peaked at 0.0327 (12 Sep) and is back to 0.0298.
- BTC dominance is 59.3% (CoinGecko).
- In the pullback, alts drew down 2–6x more than BTC from their Aug–Oct highs: SOL −16%, HYPE −18%, LINK −22%, LIT −42% vs BTC −6.7%.

### Cited Findings
- **Market caps (CoinGecko, 17 Oct 03:24 UTC):** total $2.757T. BTC dominance **59.32%**, ETH 10.72%, USDT 6.65%, BNB 3.48%, XRP 2.99%, USDC 2.63%, SOL 2.23%. Derived: TOTAL2 ≈ $1.122T, TOTAL3 ≈ $0.826T, TOTAL3 excluding USDT/USDC ≈ $0.570T — [CoinGecko global API](https://api.coingecko.com/api/v3/global).
- **ETH/BTC (OKX closes):** 0.02707 (20 Jun) → 0.02937 (1 Aug) → 0.03144 (22 Aug) → **0.03269 (12 Sep, peak)** → 0.03171 (3 Oct) → 0.03020 (10 Oct) → **0.02975 (17 Oct)** — [OKX API](https://www.okx.com/api/v5/market/history-candles?instId=ETH-USDT&bar=1Dutc).
- **Alt-season proxy (my calculation, OKX USDT pairs, 47 large alts):**
  - 90 days (19 Jul → 17 Oct): BTC +26.0%; **35 of 47 (74%)** beat BTC.
  - Since 1 Aug close: 34 of 47 beat BTC. Since 1 Jul close: 26 of 47.
  - Source: [OKX API](https://www.okx.com/api/v5/market/history-candles?instId=SOL-USDT&bar=1Dutc)
  - CoinGecko top-50 non-stable alts: 30 days, 24 of 50 beat BTC (+6.7%); 200 days, 19 of 50 beat BTC (+20.0%) — [CoinGecko markets API](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&price_change_percentage=7d,30d,200d,1y).
- **90-day leaders:** NEAR +165.5%, ENA +148.7%, PUMP +130.6%, ARB +112.5%, ZEC +110.7%, UNI +107.7%, TIA +104.9%, INJ +75.3%, AAVE +73.7%. **Laggards:** XLM −4.3%, TRX +2.6%, BONK +9.6%, DOGE +10.8%, XRP +19.1% — [OKX API](https://www.okx.com/api/v5/market/history-candles?instId=NEAR-USDT&bar=1Dutc).
- **Watchlist since the summer lows (OKX spot; HYPE/LIT also checked on Hyperliquid):**

  | Coin | Price (17 Oct) | Summer low (date) | Aug–Oct high (date) | From low | From high | vs BTC since 1 Jul | vs BTC since 1 Aug |
  |---|---|---|---|---|---|---|---|
  | SOL | $104.77 | $64.05 (25 Jun) | $124.96 (27 Sep) | +63.6% | −16.2% | −0.4% | +12.2% |
  | HYPE | $80.04 | $51.15 (2 Aug) | $98.04 (23 Sep) | +56.5% | −18.4% | −5.6% | +18.0% |
  | LIT | $3.217 | $1.474 (23 Jun) | $5.576 (24 Sep) | +118% | **−42.3%** | +14.2% | +22.6% |
  | BNB | $721.6 | $537.2 (1 Jul) | $810.1 (5 Oct) | +34.3% | −10.9% | −3.5% | −3.4% |
  | LINK | $12.34 | $7.01 (25 Jun) | $15.77 (29 Sep) | +76.1% | −21.7% | +23.5% | +17.8% |
  | ETH | $2,427 | $1,512 (26 Jun) | $2,808 (21 Sep) | +60.5% | −13.6% | +11.0% | +1.3% |

  - Sources: [OKX API](https://www.okx.com/api/v5/market/history-candles?instId=HYPE-USDT&bar=1Dutc), [Hyperliquid candleSnapshot](https://api.hyperliquid.xyz/info)
  - KNTQ is not a Hyperliquid perp, and its Hyperliquid spot pairs showed no usable volume — [Hyperliquid API](https://api.hyperliquid.xyz/info).
- **Glassnode on alts:** "coin froth" has been in its top fifth since 28 Sep, while global froth is low — [Glassnode Week 41](https://research.glassnode.com/the-week-onchain-week-41-2026/).
- **CoinGecko distance from ATH (17 Oct):** HYPE −18% (ATH $97.96 on 23 Sep 2026); SOL −64%; ETH −51%; BNB −47%; LINK −77% — [CoinGecko markets API](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100).

### Inferences
- **The August–September rally broadened** into a near-altseason by breadth (74% over 90 days), led by DeFi/old-cycle names (NEAR, UNI, AAVE, ARB, ENA) and perp-DEX tokens (LIT, HYPE).
- **The October pullback hit alts disproportionately.** That matches a market where the alt rally was leverage- and momentum-driven, not backed by stablecoin growth (§4) or ETF demand (ETH/SOL outflows, §3).
- **For the user's alt allocation:** alts have typically outperformed BTC on the way *up* and underperformed on the way *down* (beta ~2–3x in this sample).
- **Watchlist read-through:**
  - LIT's −42% from its high and HYPE being only −18% from its ATH reflect very different positioning.
  - BNB has underperformed BTC since July (low beta).
  - LINK has been the strongest large cap vs BTC.

### Gaps
- No historical BTC dominance / TOTAL2 / TOTAL3 series was obtained (TradingView/CMC need access), so the dominance *trend* is unmeasured.
- The official Blockchaincenter/CMC Altcoin Season Index value was not retrieved; my proxy uses a 47-coin OKX basket, not the official top 50.

## 8. Dated catalyst calendar, 17 Oct 2026 → 31 Mar 2027

### Takeaway
The near-term cluster runs **28 Oct FOMC → 30 Oct $12.2B Deribit expiry → 31 Oct Mt. Gox deadline → 3 Nov midterms → 6 Nov NFP → 10 Nov CPI**. After that come the **9 Dec FOMC** (hike ~77% priced), the **11 Dec government-funding deadline**, the **25 Dec $10.7B quarterly expiry**, and **LIT's first insider cliff (~27–30 Dec)**. The CLARITY Act is stalled after the failed 15 Sep cloture vote. Comprehensive market-structure law is unlikely before 2027, and no SEC catalysts are scheduled.

### Cited Findings
- **Macro dates:**
  - **FOMC 2026:** 27–28 Oct; 8–9 Dec (with SEP). **FOMC 2027:** 26–27 Jan; 16–17 Mar (with SEP); then 27–28 Apr. 2027 dates are tentative until confirmed. Minutes of the September meeting were released 7 Oct — [Federal Reserve calendar](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm).
  - **CPI (8:30 ET):** Oct data on **10 Nov 2026**; Nov data on **10 Dec 2026**; Dec data on **13 Jan 2027**; Jan data on 11 Feb 2027; Feb data on 10 Mar 2027 — [BLS CPI schedule](https://www.bls.gov/schedule/news_release/cpi.htm). Some third-party calendars list 12 Nov / 11 Dec, which conflicts with BLS.
  - **NFP / Employment Situation (8:30 ET):** **6 Nov 2026** (Oct); **4 Dec 2026** (Nov); 8 Jan 2027 (Dec); 5 Feb 2027 (Jan); 5 Mar 2027 (Feb) — [BLS Employment schedule](https://www.bls.gov/schedule/news_release/empsit.htm).
  - **US government funding:** the stopgap (H.R. 6500) funds the government through **11 Dec 2026**, so shutdown risk returns afterward and could delay data releases — [Fox News](https://www.foxnews.com/politics/trump-signs-government-funding-bill-avoiding-shutdown-ahead-midterms).
  - **US midterm elections:** 3 Nov 2026. The lame-duck session (5 Nov–18 Dec) is expected to be dominated by budget work — [CryptoTicker Q4 calendar](https://cryptoticker.io/en/crypto-dates-fourth-quarter-2026/).
- **Options expiries (Deribit, 08:00 UTC Fridays):** 23 Oct weekly ($1.2B); **30 Oct monthly ($12.2B, max pain $79K)**; 27 Nov monthly ($2.18B, max pain $81K); **25 Dec quarterly ($10.67B, max pain $75K)**; 26 Mar 2027 quarterly ($3.41B, max pain $76K) — [Deribit API](https://www.deribit.com/api/v2/public/get_book_summary_by_currency?currency=BTC&kind=option).
- **Mt. Gox:** the repayment deadline is **31 Oct 2026** (extended in Oct 2025 for the third time). Arkham showed 34,689 BTC still in Mt. Gox wallets as of Oct 2025 (~$2.8B at $81.5K) — [The Block](https://www.theblock.co/post/376205/mt-gox-postpones-repayment-deadline). Whether there has been another extension is unverified.
- **Token unlocks and supply events:**
  - Already passed: **ENA 5 Oct** (1.41B ENA, ~14% of supply, ~$381M; all remaining investor releases were pulled forward into this date, so no ENA unlocks remain in November); ARB 16 Oct (~92.7M, ~$20M); DBR 17 Oct (618.3M quarterly) — [CryptoTicker](https://cryptoticker.io/en/crypto-dates-fourth-quarter-2026/), [ChainCatcher](https://www.chaincatcher.com/en/article/2293219).
  - ZRO 20 Oct (~23.63M, insiders) — [CryptoTicker](https://cryptoticker.io/en/crypto-dates-fourth-quarter-2026/).
  - ALLO 11 Nov (160.2M, ~$41M, ~64% of circulating supply) — [CryptoTicker](https://cryptoticker.io/en/crypto-dates-fourth-quarter-2026/), [ChainCatcher](https://www.chaincatcher.com/en/article/2293219).
  - **Monad (MON) team cliff, 24 Nov:** ~10.7B MON by the article's estimate (~90% of the current 11.8B circulating supply); a third-party calendar says ~16.8B — [CryptoTicker](https://cryptoticker.io/en/crypto-dates-fourth-quarter-2026/).
  - HUMA 26 Nov (~332.5–479M); SAHARA team 26 Dec; 0G's first release moved to 22 Oct 2027 — [ChainCatcher](https://www.chaincatcher.com/en/article/2293219).
- **HYPE (watchlist) unlocks:**
  - Team unlocks fall on the **6th of each month** (next: 6 Nov, 6 Dec, 6 Jan) — [BeInCrypto](https://beincrypto.com/hyperliquid-hype-token-monthly-unlock-schedule/).
  - Actual distributions have been far below the whitepaper's ~9.92M HYPE a month (e.g. ~330K HYPE in April 2026) — [Tokenomist](https://tokenomist.ai/research/hype-tokenomics-330k-or-9-9m-hype-unlocks).
  - Hyperliquid cut monthly team unlocks by ~90% in Jan 2026 — [Yahoo Finance](https://finance.yahoo.com/news/hyperliquid-cuts-monthly-team-unlocks-120608785.html).
  - A single-source report (30 Sep 2026) says Hyperliquid Labs planned a ~$320M HYPE unlock for team distribution plus an institutional OTC sale. **Unverified** — [TokenPost](https://www.tokenpost.com/news/business/25891).
  - One tracker lists a 2.5%-of-market-cap HYPE unlock on 29 Nov (this conflicts with the 6th-of-month schedule) — [Tokenomics.com](https://app.tokenomics.com/tokenomics/hyperliquid/unlocks).
- **LIT (watchlist) unlock:**
  - The first insider cliff is **~27–30 Dec 2026**. Team (26%) and investors (24%) hold 500M LIT, vesting over ~3 years (~166.7M a year, ≈13.9M a month).
  - Some trackers show 30 Dec as the first tranche: 7.02M team + 6.48M investor tokens (13.5M LIT).
  - Lighter routes 100% of protocol fees to buybacks: trailing-year revenue was $57M, with ~$3.6M in fees in the 30 days to late August.
  - Sources: [FinanceFeeds (25 Aug)](https://financefeeds.com/lighter-lit-price-forecast-and-what-to-expect/), [Tokenomics.com](https://app.tokenomics.com/tokenomics/lighter/unlocks), [CryptoRank](https://cryptorank.io/price/lighter/vesting)
- **Protocol and industry events:**
  - Ethereum Glamsterdam activated on the Sepolia testnet on 6 Oct; the earliest mainnet window is December, with no date set.
  - Devcon 8 (Mumbai) runs 3–6 Nov. Solana Breakpoint (London) runs 15–17 Nov.
  - A possible SEC decision on crypto-ETF options on 11 Nov is **unverified**.
  - Source: [CryptoTicker](https://cryptoticker.io/en/crypto-dates-fourth-quarter-2026/)
- **Legislation (CLARITY Act):**
  - The House passed it on 17 Jul 2025 (294–134). Senate Banking advanced it 15–9 in May 2026.
  - The **Senate cloture vote failed on 15 Sep 2026**: 50–49 in favour per CNBC, far short of the 60 needed.
  - Tillis switched his vote to file a motion to reconsider, so the bill can technically be revived.
  - Passage odds are cited at 7–9%, and passage is seen as unlikely before 2027.
  - Sources: [CNBC](https://www.cnbc.com/2026/09/15/senate-cloture-vote-on-clarity-act-fails-dealing-regulatory-setback-to-crypto-industry.html), [DeFi Rate](https://defirate.com/clarity-act-fact-sheet/), [Troutman](https://www.troutmanfinancialservices.com/2026/05/senate-banking-committee-advances-clarity-act-in-bipartisan-vote/), [bit.com](https://www.bit.com/knowledge-hub/clarity-act-senate-vote)
- **SEC:** dozens of alt ETFs (SOL, XRP, DOGE, HYPE, etc.) are live under the Atkins SEC. In June 2026 the SEC opened a review of "novel ETF" rules. No October 2026 SEC actions were found — [The Block](https://theblock.co/post/406750/sec-opens-etf-rule-review-following-crypto-fund-surge-prediction-markets-push).

### Inferences
- **FOMC minutes dates (my calculation, minutes come ~3 weeks after each meeting):** 28 Oct meeting → ~18 Nov; 9 Dec meeting → ~30 Dec.
- **CLARITY Act dies with the 119th Congress on 3 Jan 2027 if not passed**, and would need reintroduction in the 120th Congress. This is a general constitutional fact, not from a crypto source.
- **Most volatile window: 28 Oct–10 Nov** (FOMC, expiry, Mt. Gox, midterms, NFP, CPI).
- **LIT supply overhang (my calc):** ~13.5–13.9M LIT a month ≈ $43–45M at $3.22, against fee-funded buybacks of ~$3.6M a month. That is roughly a 10:1 overhang from January 2027, unless the cliff is structured differently.
- **HYPE unlock risk** is uncertain but potentially large if the ~$320M report is accurate.

### Gaps
- A comprehensive list of >$50M large-cap unlocks for Jan–Mar 2027 was not found; trackers (Tokenomist, CryptoRank) need JS or an API.
- The SOL, BNB and LINK unlock schedules were not checked: SOL has no cliffs (inflation only), BNB has quarterly burns, and LINK's quarterly non-circulating releases were not verified for dates.
- No dates were found for Solana Alpenglow or Firedancer mainnet.
- Whether the Mt. Gox deadline has been extended again is unverified.

## 9. Analyst debate: bottom-in vs bear-market rally, key evidence, and invalidation levels

### Takeaway
Credible on-chain desks lean **"bottom likely in, but near term boxed in"**:
- CryptoQuant's CEO declared the bear over on 13 Oct.
- Checkonchain sees the bottom at ~$58K.
- Glassnode is constructive longer term but cautious near term.
- CoinShares sees a "difficult, not fundamentally bearish" range.

The **bear camp's calls are mostly stale** (June–August: Galaxy $40–46K floor, 10x $55K, Cowen's "October low"). Their core arguments still stand: macro tightening, the 4-year-cycle timing (12–13 months after the Oct 2025 ATH), ETF outflows and flat stablecoin liquidity.

Price sits *exactly* on the shared pivot ($80–82K: ETF cost basis and 365-day MA):
- **Bull confirmation:** daily close above $88K with ETF inflows.
- **First warning:** daily close below ~$80–81.5K.
- **Bull structure broken:** below the ~$74–78K STH cost basis / True Market Mean.
- **Thesis fully invalidated:** below the $62.3K higher low and the $57.8K cycle low.

### Cited Findings
- **Bull: CryptoQuant.**
  - CEO Ki Young Ju (13 Oct): the 2026 bear cycle is over; expects 12–24 months of upward or sideways action.
  - Research note "Whales Are Back" (13 Oct): large holders accumulating in an early bull market.
  - Framework line: 365-day MA ~$81.7K; sustained closes above it confirm the new phase.
  - Sources: [CryptoQuant research](https://cryptoquant.com/insights/research/6ace4fa1b3e204342cef8fb4-13-October-2026-Whales-Are-Back-Large-Holders-in-an-Early-Bull-Market-Supported-), [Cointelegraph](https://cointelegraph.com/markets/bitcoin-bear-market-over-as-price-metric-copies-2023-recovery-cryptoquant-ceo), [BigGo](https://finance.biggo.com/news/338becaf-d25d-45d8-9958-ee9ec3c3d06f), [CryptoBreaking](https://www.cryptobreaking.com/cryptoquant-ceo-says-bitcoin-bear/)
  - *Contrast:* CryptoQuant's head of research earlier called a rebound a "bear market rally" **[STALE: early 2026]**, and another CryptoQuant outlook had placed the bottom in Oct–Dec 2026 — [The Block](https://www.theblock.co/post/386021/bear-market-rally-cryptoquant-bitcoin-price-rebound).
- **Bull: Checkonchain (James Check).** The bottom is likely ~$58K after two capitulations (Feb ~$60K, Jun/Jul ~$58K). Seller exhaustion argues against a further major low in late 2026. Levels: $88K resistance (2025 cohort); $82.3K ETF cost-basis support; ~$65K for the 2023 cohort **[article ~4 weeks old]** — [Bitget](https://www.bitget.com/news/detail/12560605845575), [CoinTurk](https://en.coin-turk.com/checkonchain-analyst-says-bitcoin-cycle-bottom-likely-at-58000-not-october-2026/), [CoinDesk](https://www.coindesk.com/markets/2026/10/07/bitcoin-s-recovery-stalls-just-short-of-rescuing-its-last-underwater-cohort).
- **Mixed: Glassnode (14 Oct).**
  - "Boxed in between firm support below and heavy supply above." Near term cautious; longer term constructive, because loss-taking has dried up and the bear never closed below realized price.
  - **Bull confirmation:** daily close >$88K plus returning ETF inflows.
  - **Warning:** losing the $80K bids and ~$81.5K ETF cost basis brings the ~$78K True Market Mean into play.
  - Source: [Glassnode Week 41](https://research.glassnode.com/the-week-onchain-week-41-2026/)
- **Neutral: CoinShares (16 Oct).** Expects a "data-driven range rather than a trend"; the setup is "difficult rather than fundamentally bearish" — [CoinShares](https://coinshares.com/us/insights/research-data/market-update-16-10-2026/).
- **Bull: K33 (Vetle Lunde, 20 May 2026) [STALE].** Called the Feb ~$60K low the likely maximum drawdown, with a base case of a $60–75K consolidation. Evidence: 81 days of negative 30-day-average funding and LTH seller exhaustion. **The $57.8K low on 1 Jul marginally undercut that call (−3.6%)** — [Bitcoin.com](https://news.bitcoin.com/k33-research-bitcoin-bear-market-bottom-60000-maximum-drawdown-2026/).
- **Bull on timing: Bitwise (André Dragosch).** The consensus late-2026 bottom timeline may itself pull the turn earlier (date of piece unclear, likely mid-2026) — [DL News](https://www.dlnews.com/articles/markets/bitcoin-price-bottom-coming-sooner-than-expected/).
- **Bear: Galaxy Research (June 2026) [STALE].** The bottom is not in. Base-case floor $40–46K (tied to realized price), severe case $30–37K by late 2026; only 4 of 13 bottom indicators had triggered — [Blockonomi](https://blockonomi.com/galaxy-research-says-bitcoin-bottom-is-not-in-projects-40k-46k-base-case-floor-by-late-2026), [Coinpaper](https://coinpaper.com/17648/galaxy-research-warns-bitcoin-price-could-drop-to-40-000-by-2026-end-odds-at-32).
- **Bear: 10x Research (Markus Thielen) [STALE].**
  - 24 Jun: $55K as the "actionable low zone", with a bottom window of late Aug–Oct — [CoinDesk](https://www.coindesk.com/markets/2026/06/24/bitcoin-could-fall-to-usd55-000-before-finding-a-bottom-10x-research-says).
  - August: a new ATH is unlikely soon; downside drivers are ETF selling, a strong USD and the hawkish Warsh Fed — [Bitget](https://www.bitget.com/news/detail/12560605729457).
  - One report attributes a $46–47K scenario to Thielen — [Cryptonews](https://cryptonews.net/news/bitcoin/33099817/).
- **Bear: Benjamin Cowen.** Has repeatedly named October 2026 as a candidate for the major cycle low and said rallies would be temporary (article dates uncertain, likely late 2025 to early 2026) — [BeInCrypto](https://beincrypto.com/bitcoin-bear-market-not-over-benjamin-cowen-says/).
- **Macro evidence for the bear side (§2):**
  - Fed at 3.75–4.00% with a December hike ~77% priced; 10y 5.10%; real 10y 2.78%; Brent $126.55.
  - Weaker risk assets: Nasdaq −5.3% from its high; gold −26% from its January peak.
  - Sources: [Polymarket API](https://gamma-api.polymarket.com/public-search?q=Fed%20decision%20in%20December), [FRED](https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10)

### Inferences
- **Evidence for "bottom in":**
  - The cycle low ($57.8K) came with extreme fear (F&G 12), MVRV ~1.1 and 12:1 loss-dominant spending, then a clean higher low ($62.3K).
  - Price has held above the STH cost basis and True Market Mean since 18 Sep, and the LTH realized loss is down ~85%.
  - Breadth: 74% of alts beat BTC over 90 days.
  - Price has held $80K through a hot CPI and ~$1B of liquidations.
- **Evidence for "bear rally / not yet":**
  - The rally stalled exactly at the $88K overhead cohort cost basis (a double top).
  - ETF outflows since 7 Oct; corporate buying has stopped.
  - Stablecoin supply is flat (+1% over 90 days) and below its May peak.
  - The macro regime is tightening.
  - Options skew is put-bid and max pain sits below spot.
  - F&G never reset to fear in this pullback.
  - 4-year-cycle analogs: past bear lows (Dec 2018, Nov 2022) came ~12–13 months after the ATH, i.e. ~Oct–Nov 2026 this time. The July low came ~9 months after the ATH, and the drawdown (−54%) is far shallower than −77% (2022) or −84% (2018). Bears read this as "not enough capitulation"; bulls read it as "structurally shallower cycles" (the K33 argument).
- **Invalidation ladder for the premise "bottom in, next leg coming":**
  1. Daily close <$80K (Glassnode bid wall, below the ETF cost basis and 365-day MA): near-term bull case weakened, target $78K.
  2. Weekly close <~$74–75K (STH cost basis / SMA100 / 50% retrace of the August leg): bull structure broken; a retest of $65–70K becomes likely.
  3. Break of $62.3K (August higher low): premise seriously damaged.
  4. Break of $57.8K (cycle low): premise invalidated; the Galaxy/10x $40–55K targets come back into play.
- **Confirmation ladder:**
  1. Daily close >$88K with ETF inflows (Glassnode).
  2. >$100K (the 1–2y cohort cost basis) would put nearly all cohorts in profit. Markets currently price this at ~8–18% (terminal, Dec/Mar) or ~20% (touch by end-2026).

### Gaps
- No fresh (Oct 2026) published views were found from 10x Research, Galaxy, Bitwise, Kaiko or K33 on the cycle bottom; their latest cycle calls are June–August or earlier.
- Kaiko market-depth research for October 2026 was not found.
- CryptoQuant's 13 Oct research page returned 403 on direct fetch; its content is taken from press write-ups.
