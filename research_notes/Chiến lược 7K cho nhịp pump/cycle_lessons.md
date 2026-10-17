# Past-cycle playbook for altcoin capital after BTC cycle bottoms (2015–16, Dec 2018–2019, Nov 2022–2024; Mar 2020–21 as contrast)

Method and labels (read first):
- **[computed]** = my own calculation. Sources: CoinMarketCap daily OHLC and market cap ([CMC historical API](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=1&convertId=2781&timeStart=1544832000&timeEnd=1592179200)), point-in-time top-N lists ([CMC historical listings API](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listings/historical?convertId=2781&date=2018-12-15&limit=200&start=1)), BTC dominance ([CMC global metrics API](https://api.coinmarketcap.com/data-api/v3/global-metrics/quotes/historical?format=chart&interval=1d&timeStart=1544832000&timeEnd=1545091200)), Hyperliquid daily candles and funding ([Hyperliquid info API](https://api.hyperliquid.xyz/info), POST `candleSnapshot` / `fundingHistory`), and OKX 1H candles ([OKX history-candles API](https://www.okx.com/api/v5/market/history-candles?instId=BTC-USDT&bar=1H&limit=100&after=1584144000000)). Scripts and raw data: `/tmp/claude-0/-home-user-test-claude/8ec8a334-85ed-54af-babc-62d7e4c0704b/scratchpad/research/cycles/` (`download.py`, `analyze.py`, `report.py`; results in `data/analysis.json`).
- **[quoted]** = a figure taken from the linked source.
- Returns are close-to-close on UTC daily closes unless marked "intraday". CMC prices are cross-exchange aggregates, so **CMC daily lows understate wicks on any single venue** (for example, Binance-only wicks on 2025-10-10). CMC's BTC dominance counts stablecoins in total market cap, which lowers the 2022–24 readings relative to ex-stablecoin measures (a method note).
- Cycle bottoms (lowest CMC daily close): 2015-01-14 (BTC $178), plus a secondary 2015-08-24 low ($210), the first bottom after ETH existed; 2018-12-15 ($3,237); 2020-03-12 ($4,971); 2022-11-21 ($15,787). Bitstamp intraday lows: $152.4 (2015-01-14), $3,122 (2018-12-15), $3,850 (2020-03-13), $15,479 (2022-11-21), $57,735 (2026-07-01) [computed from the local Bitstamp file].
- "Top-50 alts" means the 50 largest coins by CMC market cap on the bottom date, excluding BTC, stablecoins and wrapped or staked tokens. Membership is point-in-time, so there is no look-ahead. A coin whose CMC history ends before a horizon counts as −100%. **2015 caveat:** CMC no longer serves price history for 18–19 of the Jan-2015 top-50 (mostly dead micro-caps). They had to be dropped, so the 2015-01 alt statistics are biased upward, and the 2015 alt universe was made of sub-$50M coins anyway.

## 1. Cycle scoreboard: BTC returns, BTC dominance, ETH/BTC and top-50 alt breadth at +6/+12/+18 months

### Takeaway
In every cycle the median top-50 alt trailed BTC by month 12. Only 6–23% of top-50 alts beat BTC over 12 months (2% at 6 months in 2023). Alt breadth was briefly good right after the bottom in 2019 (70% beat BTC at +3 months), then collapsed as BTC dominance climbed (50%→71% in 2019; 38%→55% in 2022–24). Broad alt outperformance came only in 2020–21, after BTC broke its prior ATH; in that cycle dominance fell from 72% to 39%.

### Cited Findings
- Scoreboard [computed] — [CMC historical API](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=1&convertId=2781&timeStart=1544832000&timeEnd=1592179200); [CMC listings](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listings/historical?convertId=2781&date=2018-12-15&limit=200&start=1); [CMC global metrics](https://api.coinmarketcap.com/data-api/v3/global-metrics/quotes/historical?format=chart&interval=1d&timeStart=1544832000&timeEnd=1545091200)

| Cycle (bottom close) | Horizon (date) | BTC return | BTC dom. | ETH/BTC | Top-50 alt median | Top-50 75th pct | Equal-wt top-50 | % of top-50 beating BTC |
|---|---|---|---|---|---|---|---|---|
| 2015-08-24 ($210; dom 83.3%, ETH/BTC 0.0058) | +6m (2016-02-24) | +102% | 84.7% | 0.0147 | +20% | +64% | +63% | 17% |
| | +12m (2016-08-24) | +176% | 80.2% | 0.0190 | +18% | +168% | +288% | 23% |
| | +18m (2017-02-24) | +458% | 86.6% | 0.0111 | 0% | +67% | +380% | 17% |
| 2015-01-14 ($178; dom 80.1%) — survivorship-biased | +6m / +12m / +18m | +61% / +142% / +269% | 85.3 / 90.9 / 81.3% | – / 0.0028 / 0.0175 | +107% / +51% / +95% | +229% / +71% / +133% | – | 62% / 19% / 12% |
| 2018-12-15 ($3,237; dom 55.2%, ETH/BTC 0.0261) | +3m (2019-03-15) | +22% | 51.1% | 0.0348 | +38% | +70% | +51% | 70% |
| | +6m (2019-06-15) | +173% | 56.6% | 0.0304 | +99% | +156% | +142% | 22% |
| | +12m (2019-12-15) | +121% | 66.4% | 0.0200 | −19% | +37% | +23% | 8% |
| | +18m (2020-06-15) | +192% | 64.9% | 0.0243 | +22% | +83% | +82% | 8% |
| 2020-03-12 ($4,971; dom 64.6%, ETH/BTC 0.0226) — contrast | +3m | +91% | 65.1% | 0.0250 | +66% | +96% | +69% | 33% |
| | +6m (2020-09-12) | +110% | 56.7% | 0.0371 | +93% | +191% | +123% | 48% |
| | +12m (2021-03-12) | +1,053% | 61.5% | 0.0309 | +520% | +1,003% | +760% | 23% |
| | +18m (2021-09-12) | +827% | 41.2% | 0.0740 | +602% | +1,259% | +1,420% | 42% |
| 2022-11-21 ($15,787; dom 38.8%, ETH/BTC 0.0702) | +3m (2023-02-21) | +55% | 42.5% | 0.0679 | +35% | +56% | +40% | 28% |
| | +6m (2023-05-21) | +69% | 46.4% | 0.0674 | +4% | +16% | +5% | 2% |
| | +12m (2023-11-21) | +127% | 51.7% | 0.0541 | +1% | +32% | +17% | 6% |
| | +18m (2024-05-21) | +344% | 53.8% | 0.0540 | +55% | +152% | +112% | 8% |

- Even the 75th-percentile ("top-quartile") alt trailed BTC at +12 months in every cycle. Relative to BTC: −29% (2015-01), −3% (2015-08), −38% (2019), −4% (2020–21), −42% (2023). At +18 months: −37%, −70%, −37%, +47% (2020–21 only), −43% [computed] — [CMC](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=1&convertId=2781&timeStart=1544832000&timeEnd=1592179200)
- Dominance range from the bottom to +18m: 2018–20, 50.1% (2019-04-02) → 70.9% (2019-09-06); 2020–21, 71.8% (2021-01-03) → 39.3% (2021-05-19); 2022–24, 37.9% (2022-11-28) → 54.8% (2024-04-14); 2015–16, 76.4–91.7% [computed] — [CMC global metrics](https://api.coinmarketcap.com/data-api/v3/global-metrics/quotes/historical?format=chart&interval=1d&timeStart=1544832000&timeEnd=1545091200)
- Large caps vs the rest. In 2019 the top-10 alts led the first leg: their median was +213% at +6m and 60% of them beat BTC (BNB, LTC, BCH, EOS). In 2022–24, none of the top-10 alts at the bottom beat BTC at +6, +12 or +18 months [computed] — [CMC listings](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listings/historical?convertId=2781&date=2022-11-21&limit=200&start=1)
- Best top-50 performers [computed] — [CMC](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=1975&convertId=2781&timeStart=1544832000&timeEnd=1592179200):
  - 2019 at +6m: LINK +746%, BNB +619%, LTC +481%, BCH +447%, EOS +263%. At +12m: LINK +926%, XTZ +331%, BNB +218%.
  - 2023 at +12m: SOL +339%, OKB +188%, LINK +131%, MKR +117%. At +18m: SOL +1,404%, NEAR +401%, BCH +399%, MKR +382%, TON +268%.
  - 2016 at +12m from Aug-2015: XEM +6,111%, XMR +917%, ETH +796%.
  - 2020–21 at +18m: DOGE +16,203%, ADA +10,675%.
- K33 (June 2023): in previous alt seasons BTC dominance fell below 60%, and the low in dominance coincided with the top in total alt market cap. Alt rallies began only after BTC broke its prior ATH [quoted] — [Cointelegraph on K33](https://cointelegraph.com/markets/bitcoin-only-buy-and-hold-investment-strategy-outperforms-altcoins-over-the-long-term-analysis-shows)

### Inferences
- The +3-month window can flatter alts: 2019 had 70% of alts beating BTC at +3m but only 8% at +12m. Early breadth does not mean an alt season is under way.
- In both "BTC still below its prior ATH" cycles (2019 and 2023), a diversified alt book was close to a guaranteed underperformer against BTC over 6–18 months. The edge came from 1–3 leaders (LINK and BNB in 2019; SOL in 2023), not from breadth.

### Gaps
- No clean ex-stablecoin dominance series was built; CMC's series includes stablecoins. The 2015 alt statistics are unreliable because of missing dead coins.

## 2. Early-bull leaders: start price, peak multiple, timing, drawdowns along the way, and common traits

### Takeaway
Every early bull had a handful of leaders that beat BTC by 3–10x. Their common ingredients were forced demand or cash flow (BNB via Launchpad and burns; HYPE via fee buybacks; INJ via burns), a fresh narrative early in the cycle (AI, memes, the Solana revival), and exchange backing. **Every one of them fell 25–95% before peaking**, usually in the first correction, so leverage would have wiped out most holders of the eventual winners. The leaders were already visible in the top-5 by relative strength 3–6 months after the bottom.

### Cited Findings
- Leader statistics [computed; CMC closes; "max DD before peak" is the largest peak-to-trough fall between the start and the eventual peak] — [CMC historical API](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=5426&convertId=2781&timeStart=1669000000&timeEnd=1743379200)

| Coin (cycle) | Start (date, close) | Peak close (date) | Multiple / days | Max DD before peak (close / intraday, date) | BTC multiple, same window | What came after |
|---|---|---|---|---|---|---|
| BNB 2019 | 2018-12-15 $4.56 | $38.82 (2019-06-21) | 8.5x / 188d | −25% / −28% (2019-05-09) | 3.1x | −68% by 2019-12-17; −76% by 2020-03-16 |
| LINK 2019 | 2018-12-15 $0.203 | $3.70 (2019-06-29) | 18.2x / 196d | −34% / −42% (2019-06-04) | 3.7x | −58% by 2019-09-14; then $19.10 on 2020-08-15 (93.9x in 609d, despite −62% / −70% on 2020-03-16) |
| MATIC 2019 | 2019-04-28 $0.00442 (first CMC close after the IEO) | $0.0417 (2019-12-08) | 9.4x / 224d | −65% / −79% (2019-08-04) | 1.4x | −71% within days; 555x to 2021-05-18 (with −81% in Mar 2020) |
| XTZ 2019–20 | 2018-12-15 $0.389 | $4.41 (2020-08-12) | 11.3x (first-year max 4.7x) | −64% (2020-03-16) | 3.6x | |
| BTT / CELR / ONE (2019 Launchpad) | listing | BTT $0.00178 (2019-05-28); CELR and ONE peaked at or near listing | BTT 3.8x | BTT −40% | | BTT −85%, CELR −86%, ONE −95% afterwards |
| SOL 2023 | 2022-11-21 $11.85 (2022-12-29 low $9.65) | $261.87 (2025-01-18) | 22.1x / 789d (27.1x from Dec-29); first-year max 5.5x (12.6x from Dec-29) | −45% / −50% (2023-06-14) | 6.6x | −55% by 2025-03-10 |
| INJ 2023 | 2022-11-21 $1.57 | $52.04 (2024-03-12) | 33.2x / 477d | −40% / −46% (2023-03-09) | 4.5x | −83% by 2025-03-29 |
| FET (AI) | 2022-11-21 $0.055 | $3.26 (2024-03-28) | 59.4x / 493d | −67% / −71% (2023-06-14) | 4.5x | −86% |
| RNDR (AI) | 2022-11-21 $0.419 | $13.15 (2024-03-17) | 31.4x / 482d | −54% / −59% (2023-03-11) | 4.3x | −79% |
| AGIX (AI) | 2022-11-21 $0.041 | $1.39 (2024-03-28) | 34.2x | −73% (2023-10-19) | 4.5x | |
| LDO (liquid-staking tokens) | 2022-11-21 $1.11 | $3.78 (2024-01-10) | 3.4x (first-year max 2.9x) | −56% (2023-09-11) | 2.95x | barely beat BTC: the pre-Shanghai trade was short-lived |
| PEPE | 2023-04-17 $6.6e-8 (first CMC close) | $2.64e-5 (2024-12-09) | 398x / 602d (first-year max 150x) | −84% / −86% (2023-09-21) | 3.3x | −78% |
| BONK | 2022-12-30 $1.49e-7 | $5.36e-5 (2024-11-21) | 360x / 692d (first-year max 164x) | −95% / −96% (2023-10-13) | 5.9x | −82% |
| WIF | launched 2023-11-20 | $4.59 (2024-03-31) | multiple from launch price not meaningful | −71% close / −95% intraday in first days | | −91% by 2025-03-31 |
| HYPE | 2024-11-29 $6.08 (first CMC close) | $97.18 (2026-09-22) | 16.0x / 662d (first-year max 9.6x) | −68% / −73% (2025-04-06) | 0.88x (BTC lower) | 2026-10-16 close −17.5% from that peak |

- Other 2023–24 outcomes (peak multiple from 2022-11-21 or from launch) [computed] — [CMC](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=20396&convertId=2781&timeStart=1669000000&timeEnd=1743379200):
  - Steady multi-month runners: KAS 30.7x, STX 17.0x, RUNE 9.6x, OP 5.6x, TON 4.8x.
  - New launches that peaked fast, then fell 74–94%:
    - TIA: 8.7x within 100 days of launch, then −86%
    - APT: 4.5x in 65 days, then −74%
    - SEI: 5.9x, then −84%
    - WLD: 5.3x, then −94%
    - ENA: 1.9x in 8 days, then −86%
    - JUP: 2.7x, then −76%
    - ARB: 1.7x, roughly BTC's 1.6x over the same window, then −86%
  - SUI peaked at 3.8x in Jan 2025 but fell −74% (close) by 2024-08-05 on the way.
- 2020–21 contrast [computed]:
  - SOL: 333x from 2020-04-11 ($0.78) to 2021-11-06 ($259), with a −75% drawdown on the way.
  - Others: LUNA 382x, AXS 1,187x, FTM 1,081x, MATIC 264x, AVAX 33x (with −83% on the way).

  — [CMC](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=5426&convertId=2781&timeStart=1586563200&timeEnd=1638230400)
- Leaders showed up early. BNB (+230%) and LINK (+141%) were already top-5 among top-50 alts at +3m in 2019. SOL was #2 at both +3m (+111%) and +6m (+66%) in 2023 [computed] — [CMC listings](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listings/historical?convertId=2781&date=2023-02-21&limit=200&start=1)
- BNB 2019: all-time high of $39.68 on 2019-06-22, "a 566 percent increase". Launchpad sales had to be paid in BNB, which created buying pressure. The later lottery format required holding BNB for a set period. Quarterly burns of profits were ongoing (7 burns by then) [quoted] — [CryptoDaily](https://cryptodaily.co.uk/2019/09/bnb-performing-as-good-as-you-think); [Bitcoinist](https://bitcoinist.com/binance-coin-becomes-first-crypto-to-surpass-january-18-all-time-high/amp/); [CryptoPotato](https://cryptopotato.com/binance-coin-bnb-price-records-higher-high-with-every-ieo-in-2019-over-400-roi-already/)
- 2019 IEO returns, as of 2019-12-20 vs IEO price: BTT +101.7%, FET −15.3%, CELR −57.9%, MATIC +493.2%. Vs first exchange trade: −41.5%, −87.5%, −83.7%, +254.5%. On 2019-04-25 the same tokens had been +433.9% (BTT), +203.6% (FET) and +82.0% (CELR) vs IEO price [quoted] — [BitMEX Research](https://blog.bitmex.com/initial-exchange-offerings-part-2-investment-performance-update)
- CoinGecko's 2023 top gainers:
  - BONK +7,303% (from $0.0000002 to $0.0000146)
  - INJ +2,976% ($1.27→$39.07)
  - SOL +974% (#6)
  - Kaspa and Render also in the top 10
  - "All 10 of the top crypto gainers in 2023 were also among the most popular narratives": meme coins, L1s, AI, L2s [quoted]

  — [CoinGecko](https://coingecko.com/research/publications/top-crypto-gainers); [Finbold](https://finbold.com/top-3-cryptocurrencies-of-2023-with-the-biggest-gains-of-the-year/)
- June 2023 shock: the SEC's suits against Binance and Coinbase named SOL, ADA and MATIC as securities, and Robinhood delisted them on 2023-06-27. Over seven days SOL fell about 30%, MATIC 28% and ADA 29.5% [quoted] — [Fortune](https://fortune.com/crypto/2023/06/11/solano-cardano-and-polygon-plunge-nearly-30-as-big-firms-dump-holdings-after-sec-allegations); [Blockworks](https://blockworks.co/news/robinhood-nixes-ada-matic-sol)
- HYPE buybacks:
  - The Assistance Fund spent about $644.6M on HYPE buybacks in 2025 up to mid-October, 46% of all token-buyback spending that year. It bought at least 21.36M HYPE (about 2.1% of supply), averaging $65.5M a month and peaking at $110.6M in August 2025.
  - Estimates of the fee share sent to buybacks range from 90% to 99% depending on the source.
  - A later report cites more than $2B cumulative since January 2025.
  - The bought HYPE goes to an inaccessible address, recognised as a burn by an 85% validator vote in December 2025 [quoted]

  — [CryptoPotato](https://cryptopotato.com/hyperliquid-crushes-competition-with-46-of-all-token-buybacks-in-2025/); [CoinShares](https://coinshares.com/insights/research-data/hyperliquid-primer-and-5-year-valuation-framework/)

### Inferences
- Common traits of the winners:
  1. Mechanical demand or cash flow: BNB Launchpad participation and burns, HYPE buybacks, INJ burns.
  2. A new narrative that formed early in the cycle: AI in Jan–Feb 2023; memes; the Solana rebuild after FTX.
  3. Exchange or ecosystem backing: Binance Launchpad, Coinbase listings.
  4. Strength relative to BTC during the first 3–6 months.
- Low unlock overhang separates the persistent winners from the "peak-on-launch" tokens: SOL, LINK, BNB, INJ and HYPE did not face large scheduled unlocks the way APT, TIA, ARB, SEI and ENA did (see the unlock evidence in section 6).
- The eventual 20–60x winners of 2023 (SOL, INJ, FET, RNDR) all fell 40–71% between March and June 2023. A 2x isolated long liquidates at roughly −47% to −49%. Entered at the pre-drawdown local top, 2x would have been liquidated intraday on SOL (−50%), FET (−71%) and RNDR (−59%), and survived INJ (−46%) only marginally; a 3x long would have been liquidated on all four. Spot holders survived and captured the 20–60x.
- Launchpad/IEO tokens and low-float 2023–24 launches typically peaked within 0–10 months and then gave back 75–95%. In the early bull, "new listing hype" trades were short-duration trades, not holds.

### Gaps
- I did not compute unlock schedules or MC/FDV for each leader at its start date. The traits "low unlock overhang" and "relative strength during corrections" are only partly quantified here (see section 3).

## 3. The first major correction after the first leg: alt drawdowns vs BTC, recovery time, and whether resilient alts led the next leg

### Takeaway
In the modern cycles the median top-50 alt fell 1.3–2.3x as much as BTC in the first big correction: −64% vs −49% (2019); −37% vs −18% (Apr–Jun 2023); −30% vs −20% (Jul–Sep 2023); −60% vs −26% (Mar–Aug 2024). Only 8–30% of alts fell less than BTC. **Holding up best did not reliably predict leading the next leg.** The rank correlation between correction-period return and next-leg return was between −0.38 and +0.04 in all 9 corrections tested, and the best-holding quintile beat the worst-hit quintile in the next leg only once (2020). Next-leg leaders were usually high-beta names with a new catalyst: SOL 2023, SUI 2024, XRP in Nov 2024.

### Cited Findings
- Correction table [computed; universe = top-50 alts at the correction start; BTC peak and trough are daily closes; "ratio beta" = alt window return ÷ BTC window return] — [CMC historical API](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=1&convertId=2781&timeStart=1561507200&timeEnd=1576627200)

| Correction (BTC peak → trough close) | BTC close / intraday | Alt median (25th pct) | % alts falling less than BTC | Median ratio beta | BTC next leg (to) | Alt median next leg; % beating BTC | Spearman (corr. vs next) | Next-leg median: held-up quintile vs worst quintile | % alts back to pre-correction price within 180d |
|---|---|---|---|---|---|---|---|---|---|
| 2015-11-04 $412 → 11-11 $311 | −24% / −39% | −19% (−25%) | 72% | 0.77 | +50% (12-15) | +17%; 17% | −0.15 | −5% vs +15% | 92% |
| 2015-12-15 $465 → 2016-01-15 $364 | −22% / −22% | −13% (−22%) | 70% | 0.61 | +110% (06-16) | +35%; 30% | −0.36 | −11% vs +184% | 97% |
| 2016-06-16 $766 → 08-02 $547 | −29% / −32% | −15% (−33%) | 74% | 0.51 | +111% (2017-01-04) | +6%; 9% | +0.04 | −34% vs −1% | 68% |
| **2019-06-26 $13,016 → 12-17 $6,641** | −49% / −52% | **−64% (−73%)** | 20% | **1.31** | +56% (2020-02-12) | +102%; 82% | −0.22 | +74% vs +120% | 24% (55% within 365d) |
| 2020-08-17 $12,254 → 09-08 $10,132 (contrast) | −17% / −20% | −24% (−32%) | 35% | 1.41 | +303% (2021-01-08) | +30%; 6% | +0.02 | +83% vs +21% | 98% |
| 2021-04-13 $63,503 → 07-20 $29,807 (contrast) | −53% / −55% | −61% (−69%) | 24% | 1.16 | +127% (11-08) | +124%; 50% | −0.38 | +55% vs +187% | 60% |
| **2023-04-14 $30,486 → 06-14 $25,125** | −18% / −20% | **−37% (−46%)** | 8% | **2.11** | +25% (07-13) | +26%; 50% | −0.16 | +18% vs +26% | 58% |
| **2023-07-13 $31,476 → 09-11 $25,163** | −20% / −22% | **−30% (−36%)** | 30% | **1.48** | +190% (2024-03-13) | +183%; 46% | −0.14 | +165% vs +180% | 94% |
| **2024-03-13 $73,084 → 08-05 $53,991** | −26% / −33% | **−60% (−68%)** | 12% | **2.28** | +97% (12-17) | +97%; 50% | −0.17 | +61% vs +98% | 54% (54% within 365d) |

- Days until BTC itself regained its pre-correction close: 312 (2019), 9 (Apr–Jun 2023), 42 (Jul–Sep 2023) and 93 (2024). Median days for alts that did regain their pre-correction price: 252 (2019), 175 (Apr–Jun 2023), 58.5 (Jul–Sep 2023), 103 (2024) [computed] — [CMC](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=1&convertId=2781&timeStart=1561507200&timeEnd=1603497600)
- 2019 named examples [computed]:
  - LINK fell only −22% window-to-window (its worst point inside the window was −58%), then gained +129% in the next leg and went on to 93.9x by Aug 2020.
  - XTZ rose +42% during the correction, then +115% in the next leg.
  - BNB −65% → +114%. ETH −64% → +116%.
  - The best next-leg performers were the most crushed "dino" coins: BSV +353% (after −63%), LSK +337% (after −77%), ETC +253% (after −62%), DASH +223% (after −76%).

  — [CMC](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=1975&convertId=2781&timeStart=1561507200&timeEnd=1581465600)
- Apr–Jun 2023 [computed]:
  - Held up best: TRX +7%, LEO +2%, XRP −8% (then +70% after the 2023-07-13 Ripple ruling), XMR −17%, QNT −19%.
  - SOL −42% → +80%. MATIC −47% → +37%. LDO −36% → +35%.

  Jul–Sep 2023:
  - Held up best: TON +21% → +163%; MKR +17% → +168%; OP −7% → +245%.
  - Next-leg best: SOL (−32% in the correction) +824%, RNDR (−32%) +681%, STX (−37%) +623%, IMX +608%, NEAR +604%.
  - LINK −18% → +257%. BNB −20% → +206%.

  — [CMC](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=5426&convertId=2781&timeStart=1681430400&timeEnd=1710288000)
- Mar–Aug 2024 [computed]:
  - Held up best: TON +23% (but only +10% in the next leg), KAS +5% (−10% next), XMR −3%, LEO −5%, TRX −8% (+130% next).
  - Next-leg best: SUI (−67% in the correction) +767%, HBAR (−61%) +444%, XRP (−29%) +424%, XLM +387%, DOGE +317%.
  - SOL −21% → +72%. BNB −26% → +54%. ETH −40% → +61%. LINK −54% → +193%. INJ −68% → +75%. RNDR −64% and LDO −70% never regained their March 2024 price.

  — [CMC](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=20947&convertId=2781&timeStart=1710288000&timeEnd=1734393600)
- 2021 contrast: SOL held up (−14% vs a −61% alt median) and then led the next leg with +958%, the clearest case of "relative strength in the correction, then leadership". AVAX (−71% → +845%) and LUNA (−62% → +822%) did almost as well from far deeper drawdowns [computed] — [CMC](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=5426&convertId=2781&timeStart=1618272000&timeEnd=1636329600)
- 2015–16 behaved differently. Alts fell less than BTC (ratio beta 0.5–0.8) because the alt market was illiquid and idiosyncratic. ETH, however, fell −57% in Jun–Aug 2016 (the DAO hack) while BTC fell −29% [computed] — [CMC](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=1027&convertId=2781&timeStart=1466035200&timeEnd=1470096000)

### Inferences
- Rule of thumb from the modern cycles: during BTC's first real correction, expect the median large alt to fall about 1.5–2.3x as much as BTC. If BTC drops a further 15–25%, a typical top-50 alt drops 30–60%. Even the eventual leaders fell 32–45% (SOL 2023).
- "Buy what held up best" is not supported as a mechanical rule, and the next leg tended to reward beaten-down high-beta coins with a catalyst. The better use of relative strength is the 3–6 month relative strength off the cycle low (see section 2: BNB/LINK 2019, SOL 2023), sized so the coin can survive a 40–50% drawdown.
- After the 2024 correction, 46% of the top-50 never regained their pre-correction price within a year. Holding a loser through a correction carries real permanent-impairment risk, concentrated in the low-float 2023–24 launches (TIA, OP, SEI, ARB, STRK were the worst five, at −72% to −87%).

### Gaps
- The Dec 2024 → Apr 2025 correction, during which HYPE fell from about $35 to $9–10 and then led, was not run as a full top-50 table because the downloaded coin windows end in March 2025.

## 4. Leverage history: crash wicks, liquidations, funding/OI resets, ADL, and what share of 2x and 3x alt longs would have been liquidated

### Takeaway
In the big leverage flushes the median top-50 alt wicked about 50% below the prior day's close on aggregated CMC data: −52% (2020-03-12/13), −50% (2021-05-19), −49% (2025-10-10/11). Single venues were worse; the median Hyperliquid perp fell −70% on 2025-10-10. That put about 54–66% of 2x and 74–98% of 3x alt longs opened at the prior close below their liquidation level, while BTC at 2x survived every event except March 2020. The milder 2024-08-05 flush (median alt −19% to −21% from the prior close, but −39% to −43% from the 7-day high) still put most 3x longs opened during the prior week below their liquidation level.

### Cited Findings
- Liquidation thresholds for an isolated long [computed], using Hyperliquid-style margining where maintenance margin is half the initial margin at max leverage (formula assumption, not re-verified in this session):

| Coin max leverage | 2x long liquidates at | 3x long liquidates at |
|---|---|---|
| 40x (BTC) | −49.4% | −32.5% |
| 20x (SOL, XRP) | −48.7% | −31.6% |
| 10x (HYPE, BNB, LINK) | −47.4% | −29.8% |
| 5x | −44.4% | −25.9% |

  Funding paid and fees move these thresholds closer over time.
- Intraday crash wicks for majors [computed: OKX spot 1H candles; drop measured from the 24h high before the low, and from the prior UTC daily close] — [OKX history-candles](https://www.okx.com/api/v5/market/history-candles?instId=BTC-USDT&bar=1H&limit=100&after=1584144000000)

| Event (low, UTC) | BTC | ETH | SOL | BNB | LINK |
|---|---|---|---|---|---|
| 2020-03-13 02:00 | $3,792: −51% from 24h high / −21% from prior close | −54% / −19% | n/a (not listed) | n/a on OKX; CMC: −58% from 2020-03-11 close | −62% / −32% |
| 2021-05-19 12–13:00 | $29,000: −34% / −32% | −49% / −48% | −49% / −46% | n/a on OKX; CMC: −44% | −54% / −52% |
| 2022-06-13 to 06-18 (Celsius/3AC) | $17,618: −15% / −14% (06-18) | −20% / −19% | −13% / −10% | n/a | −26% / −16% |
| 2024-08-05 01–06:00 | $48,935: −20% / −16% | −29% / −22% | −24% / −21% | −25% / −20% | −32% / −26% |
| 2025-10-10 21:00 | $101,500: −17% / −17% | −23% / −23% | −35% / −34% | −32% / −31% | −65% / −64% |

- On Hyperliquid on 2025-10-10, measured as the drop from the prior daily close to the daily low [computed] — [Hyperliquid info API](https://api.hyperliquid.xyz/info):
  - Majors: BTC −17%, ETH −26%, SOL −38%, BNB −36%, LINK −65%, XRP −58%.
  - HYPE −28% (−38% from its 7-day high).
  - Other alts: AVAX −73%, DOGE −66%, AAVE −68%, ENA −77%, WIF −81%, SUI −83%.
  - Across 185 perps the median drop was −70% (25th percentile −78%); the worst wicks were TST −90%, IP −89%, DYDX −89%, ORDI −88%.
  - Share of perps whose daily low breached the coin's isolated liquidation level, for a long opened at the prior close: 96% at 3x and 94% at 2x. HL liquidations use the mark price, not trade prints, so these shares are upper bounds.
- On Hyperliquid on 2024-08-05 [computed] — [Hyperliquid info API](https://api.hyperliquid.xyz/info):
  - Majors from the prior close: BTC −16%, ETH −22%, SOL −21%, BNB −20%, LINK −25%. From the 7-day high: BTC −30%, ETH −38%, SOL −43%, LINK −42%.
  - Across 143 perps the median drop was −21% from the prior close; 31% breached the 3x level and 0.7% the 2x level.
  - Measured from the 7-day high, the median drop was −43%: 97% breached 3x and 50% breached 2x. This universe includes many low-max-leverage meme perps, which have tighter thresholds.
- Top-50 alts on CMC aggregated daily lows, drop from the prior close [computed] — [CMC listings](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listings/historical?convertId=2781&date=2025-10-09&limit=200&start=1):

| Event | BTC (from prior close; from 7d high) | Median alt (25th pct) | Share at/below 3x / 2x liquidation, entry at prior close | Same, entry at 7-day high | Named |
|---|---|---|---|---|---|
| 2020-03-12/13 | −48%; −55% | −52% (−57%) | 94% / 66% | 94% / 91% | ETH −51%, BNB −58%, LINK −61%, XRP −45%, ADA −52% |
| 2021-05-19 | −29%; −47% | −50% (−53%) | 98% / 56% | 100% / 88% | ETH −42%, BNB −44%, SOL −47%, LINK −50%, MATIC −56%, DOGE −54% |
| 2022-06-13→18 (6-day window) | −34%; −44% | −21% (−27%) | 16% / 0% | 90% / 20% | ETH −38%, MATIC −36%, BNB −28%, SOL −15%, LINK −15% |
| 2024-08-05 | −15%; −30% | −19% (−22%) | 0% / 0% | 84% / 8% | ETH −21%, SOL −20%, LINK −25%, PEPE −27% (−52% from 7d high) |
| 2025-10-10/11 | −14%; −17% | −49% (−62%) | 74% / 54% | 78% / 64% | ETH −21%, BNB −23%, SOL −21%, HYPE −40%, XRP −46%, LINK −54%, ADA −59%, AVAX −63%, DOT −65%, IP −82% |

- Hyperliquid funding [computed; 72-hour average annualized] — [Hyperliquid info API](https://api.hyperliquid.xyz/info):
  - Before 2025-10-10: BTC +9%, ETH +11%, SOL +13%, HYPE +15%, LINK +13%.
  - In the 72h after: SOL −116%, HYPE −32%, ETH −8.5%. The minimum hourly rates were SOL −0.205% and HYPE −0.187%.
  - 2024-08-05: before, BTC +12.7%, ETH +7.7%, SOL +8.5%; after, ETH −0.5%, SOL −7.9%.
  - This conflicts with The Defiant's claim of "70–80 bps per day for longs" on Hyperliquid before 10/10. My computed rates for majors were about 2.5–4 bps per day, so their figure may refer to specific alts.
- 2025-10-10/11 [quoted]:
  - Over $19B liquidated in under 24 hours across more than 1.6M accounts (Coinglass).
  - Hyperliquid open interest had peaked around $15.4B (Laevitas) and fell 60% (about $9B) by the end of the day. ADL was triggered on Hyperliquid.
  - Binance paid $283M in compensation for collateral mis-marked during 21:36–22:16 UTC; USDe traded at $0.65 on Binance but about $0.99 on Curve and Uniswap.

  — [The Defiant](https://thedefiant.io/newsletter/defi-daily/the-ultimate-10-10-crash-autopsy)
- 2025-10-10 ADL and venue wicks [quoted]:
  - Hyperliquid's cross-margin ADL fired for the first time in over two years [WuBlockchain](https://wublock.substack.com/p/hyperliquid-activates-cross-margin).
  - ADL closed about $2.1B of positions in 12 minutes; the production queue over-used ADL by about 28x relative to the optimal policy, imposing about $653M of unnecessary haircuts on winning traders [arXiv 2512.01112](https://arxiv.org/abs/2512.01112v2).
  - True liquidations may have reached $30–40B, with up to 90% of closures being longs [Forklog via search summary](https://forklog.com/en/wp-json/wp/v2/posts/92650).
  - On Binance, ATOM fell from $4 to $0.001 (−99.97%) and SUI from $3.40 to $0.56 (−83.5%) [RockawayX](https://rockawayx.com/insights/crypto-market-update-october-2025). On other venues ATOM fell only about 53% and IOTX about 46% [Pintu](https://pintu.co.id/en/news/216058-altcoins-on-binance-fall-to-zero-whats-really-happening-in-the-crypto-market/amp); [Cointelegraph](https://cointelegraph.com/markets/why-did-some-altcoins-on-binance-crash-to-zero).
- 2024-08-05: about $1.08B liquidated across nearly 300,000 traders (Coinglass); BTC went from about $65K to about $50K and ETH from about $2,760 to $2,172 [quoted] — [Unlock](https://www.unlock-bc.com/en/crypto-market-hit-by-1-08-billion-liquidation-amid-price-plunge). A KuCoin ranking puts it at about $1.2B — [KuCoin](https://www.kucoin.com/blog/top-10-largest-crypto-liquidation-events-of-all-time)
- 2021-05-19 [quoted]:
  - More than $8B of derivatives liquidations [CoinDesk](https://www.coindesk.com/bitcoin-plunge-40k-liquidations).
  - Bybt data: about $1.42B BTC and $1.6B ETH; Bybit was the largest venue at $534M, then Huobi at $521M [CryptoSlate](https://cryptoslate.com/bitcoin-dumps-to-38500-2-billion-in-crypto-liquidations-as-market-drops/).
  - About 700,000–900,000 traders were liquidated, and BTC rebounded from about $30K to about $40K within hours [GetBlock](https://www.publish0x.com/getblock/bitcoin-btc-went-under-dollar-30000-long-live-bitcoin-xgpkrde).
- 2020-03-12/13 "Black Thursday" [quoted]:
  - BitMEX liquidations were $1–1.6B (Skew), and total BTC futures open interest fell about 50% in a day [Decrypt](https://decrypt.co/26299/black-thursday-reshaped-bitcoin-futures-market-report?amp=1).
  - BitMEX had a 02:16–02:40 UTC outage, after which BTC rebounded from about $3,800 to $5,300 (Coin Metrics) [Unchained](https://unchainedcrypto.com/teetering-on-the-edge-how-black-thursday-exposed-the-flaws-in-the-crypto-markets/).
  - Funding stayed abnormally negative for an extended period afterwards [BlockTower](https://blocktower.substack.com/p/towerwatch-10-the-great-sell-off).

### Inferences
- BTC at 2x survived every flush in the sample except March 2020, when it fell −48% to −52% from the 2020-03-11 close (−48% on CMC, about −52% on OKX prints), right at or through the 2x level. ETH at 2x would have been liquidated in March 2020 (−51% from the prior close on CMC, −54% from the 24h high on OKX) and sat at the threshold in May 2021 (−42% on CMC, −48% to −49% on OKX). Alt longs at 3x were liquidated in most big flushes regardless of the coin. Alt longs at 2x survived the milder events (2022, 2024) but not the 2020, 2021 and 2025 cascades, in which roughly half or more of top-50 alts wicked through the −47% to −49% level from the prior close.
- On 10/10/2025, HYPE fell less than most alts on its own venue (−28% from the prior close). A 3x HYPE long opened at the prior close survived only barely (its threshold is −29.8%), and one opened at the weekly high did not (−38%). SOL and BNB 3x longs breached on OKX and HL prints; 2x survived. LINK breached even 2x (−64% to −65% on OKX/HL).
- Cascades happened during weekend or off-hours with thin liquidity: 2024-08-05 in Asian Monday hours, 2025-10-10 at 21:00 UTC on a Friday. Exchange-specific collateral and oracle failures (Binance's USDe marks) and ADL can close positions that would have survived on price alone. Cross-margining several 2x alt perps behaves like one levered basket in a correlated crash.

### Gaps
- No primary Coinglass time series of open interest and liquidations by event was retrieved; liquidation totals come from news coverage. Hyperliquid mark-price lows (the actual liquidation trigger) were not available, only trade-price candles. BNB has no OKX intraday data before 2024.

## 5. Concentrated vs diversified alt portfolios, and momentum/relative-strength evidence

### Takeaway
In my backtests, BTC beat every alt basket at +12 months in all three modern cycles, and at +18 months in 2019 and 2023. Equal-weight baskets beat BTC only at +18 months in 2020–21, after BTC's ATH break. Naive monthly "buy last month's top-3 gainers" momentum among the top-50 was the worst strategy in 2019, 2020 and 2023, with drawdowns of −59% to −99%. This matches the academic finding that crypto momentum is short-horizon (1–2 weeks) and reverses at a month or more. Concentration helped only when the pick was the cycle's leader.

### Cited Findings
- Backtests [computed]. Rules: start at the bottom close; monthly rebalancing; point-in-time top-50/top-20 universe each month; momentum ranks coins by trailing 30-day or 90-day return and holds the top 3 or top 5 equal-weighted for a month; no fees or slippage. Max DD covers 0–18m on daily equity. Each cell is +6m / +12m / +18m — [CMC historical API](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=1&convertId=2781&timeStart=1669000000&timeEnd=1716249600)

| Strategy | 2018-12 bottom | 2020-03 bottom (contrast) | 2022-11 bottom |
|---|---|---|---|
| BTC | +173% / +121% / +192% (max DD −62%, incl. Mar 2020) | +110% / +1,053% / +827% (−53%) | +69% / +127% / +344% (−20%) |
| ETH | +219% / +69% / +172% (−67%) | +245% / +1,477% / +2,935% (−57%) | +63% / +75% / +242% (−29%) |
| Equal-wt top-10, monthly rebalance | +202% / +31% / +46% (−71%) | +125% / +831% / +1,614% (−66%) | +18% / +34% / +161% (−34%) |
| Equal-wt top-20, monthly rebalance | +178% / +40% / +78% (−65%) | +131% / +610% / +1,148% (−69%) | +19% / +41% / +159% (−30%) |
| Equal-wt top-10, buy and hold | +222% / +39% / +87% (−71%) | +138% / +696% / +1,085% (−63%) | +23% / +21% / +106% (−33%) |
| Equal-wt top-20, buy and hold | +183% / +27% / +65% (−70%) | +154% / +771% / +1,384% (−60%) | +18% / +41% / +171% (−30%) |
| Top-3 by 30d return (from top-50) | +16% / −21% / −67% (−87%) | −38% / +30% / −8% (−86%) | −21% / −16% / −19% (−59%) |
| Top-3 by 90d return (from top-50) | +16% / −28% / −89% (−94%) | −89% / −60% / −34% (−99%) | +7% / −5% / +70% (−67%) |
| Top-5 by 30d return (from top-50) | +56% / −12% / −59% (−85%) | +9% / +222% / +143% (−67%) | 0% / +19% / +86% (−50%) |
| Top-3 by 30d return (from top-20) | +109% / −21% / −52% (−86%) | +64% / +186% / +188% (−71%) | +18% / +74% / +276% (−37%) |

- Single-coin dispersion at +12m [computed]:
  - 2023 top-20: median +13%, 75th percentile +60%, 10% beat BTC; best was SOL +339%.
  - 2019 top-20: median +20%, 75th percentile +49%, 10% beat BTC; best was LINK +926%.

  — [CMC](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=5426&convertId=2781&timeStart=1669000000&timeEnd=1700524800)
- Liu & Tsyvinski, "Risks and Returns of Cryptocurrency" (Review of Financial Studies 34(6), 2021, pp. 2689–2727; NBER w24877, 2018):
  - Crypto returns have no exposure to most stock-market and macro factors.
  - Time-series momentum is strong at daily and weekly frequencies (weaker for ETH than for BTC and XRP).
  - Investor-attention proxies forecast returns.
  - A secondary summary reports an average next-week BTC return of 11.2% vs 2.6% for the top vs bottom quintile of last-week returns [quoted] — [IDEAS/RePEc](https://ideas.repec.org/a/oup/rfinst/v34y2021i6p2689-2727..html); [NBER w24877](https://www.nber.org/system/files/working_papers/w24877/w24877.pdf); [CXO Advisory](https://www.cxoadvisory.com/currency-trading/crypto-asset-risks-and-returns/)
- Liu, Tsyvinski & Wu, "Common Risk Factors in Cryptocurrency" (NBER w25882, 2019; listed as Journal of Finance): three factors (market, size and momentum) capture the cross-section of expected crypto returns, built from weekly quintile sorts [quoted] — [NBER w25882](https://www.nber.org/papers/w25882.pdf); [SSRN](https://papers.ssrn.com/abstract=3379131); [CXO](https://cxoadvisory.com/size-effect/cryptocurrency-factor-model)
- Grobys & Sapkota, "Cryptocurrencies and momentum" (Economics Letters 180, 2019, pp. 6–10): 143 coins, 2014–2018, "do not indicate any evidence of significant momentum payoffs" using monthly returns [quoted] — [Univ. of Vaasa repository](https://osuva.uwasa.fi/handle/11111/2278)
- Dobrynskaya (HSE) studied about 2,000 coins with market cap above $1M over 2014–2020, with holding periods of 1–12 weeks. Per a blog summary of the paper, momentum is positive and significant up to 2 weeks, insignificant at 2–4 weeks, and significantly reversed from 4 weeks out to 2 years. I could not verify the original paper [quoted] — [HSE](https://www.hse.ru/en/news/research/559533243.html); [Arch blog summary](https://blog.arch.finance/momentum-investing-strategy-and-the-crypto-market)
- K33 (June 2023): $1 in each of 1,009 alts as they entered the top-100 since 2015 grew to about $7K, vs about $50K in BTC; about 1.5% of those alts beat BTC [quoted] — [Cointelegraph](https://cointelegraph.com/markets/bitcoin-only-buy-and-hold-investment-strategy-outperforms-altcoins-over-the-long-term-analysis-shows)

### Inferences
- Momentum works only at the horizon where the literature finds it, roughly 1–2 weeks. Monthly "chase the top gainers" rotations bought local tops in every modern cycle. A momentum rule restricted to large caps (top-20) was far less destructive: in 2023 it returned +74% at 12m with a −37% max drawdown, but it still trailed BTC at 12m in every modern cycle.
- For a $6.4K alt sleeve, history says a diversified alt basket has a lower expected return than BTC until BTC is through its prior ATH. Concentrating in one coin is a bet on picking the cycle's leader: the best top-20 coin did +339% to +926% at 12m, but the median did +13% to +20%. A middle path consistent with the data is 2–3 large-cap leaders chosen on 3–6 month relative strength, held spot.

### Gaps
- The backtests ignore fees, slippage and funding, and use only the top-50/top-20 universes. They therefore miss new listings such as SOL in 2020, which were outside the top-50 at the bottom. I found no published third-party backtest of equal-weight top-10/20 vs BTC specifically in early-bull windows.

## 6. What veteran traders and research consistently say about the early bull (sequencing, relative strength, unlocks, profit-taking, leverage)

### Takeaway
Sourced "veteran" material is thinner and more anecdotal than the price data, but it converges on four points:
1. BTC leads and alts follow in waves. Broad alt outperformance historically arrived only after BTC cleared its prior high and dominance broke lower.
2. Most alts lose to BTC over a full cycle, so alt exposure is a timing and selection bet, not a default.
3. Supply overhang (low-float/high-FDV tokens, team unlocks) is a measurable headwind.
4. Leverage in crypto is structurally fragile, because crashes are amplified by liquidation engines, ADL and thin weekend or overnight liquidity.

### Cited Findings
- **Sequencing / wave pattern (Arthur Hayes, written around early 2023 with BTC near $23K):** the reserve assets (BTC, ETH) rally first. That rally stalls and prices slip slightly while the "shitcoin complex" stages an aggressive rally. Then alts "rediscover gravity" and interest shifts back to BTC/ETH. The stair-step repeats until the secular bull ends [quoted, from a secondary write-up of his essay] — [The Informer Post summary of Hayes](https://theinformerpost.beehiiv.com/p/bitmex-founder-arthur-hayes-says-altcoins-could-go-vertical-in-next-bull-frenzy-heres-his-outlook)
- **Hayes after the 2025-10-10 crash (2025-12-19):** altcoins are "sickly"; "it will take time for the altcoin complex to heal"; those who preserved capital should "dumpster dive". Hedge-fund LP redemptions after October forced price-insensitive selling of alts. He expects leverage demand to return first through BTC and then spill into alts [quoted] — [DL News](https://www.dlnews.com/articles/markets/altcoins-are-sickly-but-its-time-to-buy-says-arthur-hayes/)
- **K33 Research (June 2023)** [quoted] — [Cointelegraph on K33, 2023-06-22](https://cointelegraph.com/markets/bitcoin-only-buy-and-hold-investment-strategy-outperforms-altcoins-over-the-long-term-analysis-shows):
  - $1 put into each of 1,009 altcoins as they entered CMC's top-100 since 2015 would be worth about $7,000, vs about $50,000 for the same dollars in BTC.
  - Over two-thirds of those alts became inactive; only 9.11% had positive returns, and about 1.5% beat BTC's roughly 50x.
  - Altcoin investing was profitable only in 2017 and 2021.
  - Alt rallies began only after BTC broke its prior ATH; the 2017 alt run started after BTC passed its 2013 peak in April 2017.
- K33's Anders Helseth: "You can create higher returns by trading market sentiment more aggressively," but it requires a lot of attention and is more risky. K33 analysts add that alt portfolios require "timing the market or picking the altcoin winners" [quoted] — [Cointelegraph](https://cointelegraph.com/markets/bitcoin-only-buy-and-hold-investment-strategy-outperforms-altcoins-over-the-long-term-analysis-shows)
- K33 on 2018–19: altcoins "continue[d] to hover around the lows for most of the duration of the bear market and only revers[ed] their trend after Bitcoin broke above its previous peak of $20,000" [quoted via a search summary of this article; exact wording not re-verified] — [Cointelegraph](https://cointelegraph.com/markets/bitcoin-only-buy-and-hold-investment-strategy-outperforms-altcoins-over-the-long-term-analysis-shows)
- **The altseason definition traders use:** Blockchain Center's Altcoin Season Index declares "altcoin season" when at least 75% of the top-50 coins (excluding stablecoins and asset-backed tokens) outperform BTC over a rolling 90 days. A reading of 25 or below means "Bitcoin season", and the index is backward-looking [quoted] — [CryptoSlate](https://cryptoslate.com/heres-why-alt-season-may-be-on-the-horizon/); [CoinGate](https://coingate.com/it/gift-cards/articles/article/altcoin-season-what-it-is-and-how-to-spot-one)
- **Relative strength on pullbacks:**
  - CryptoCred (secondary report): in past cycles BTC strength fed alts because crypto-native buyers roll profits into other coins, which "led to altcoin front running during Bitcoin pullbacks and consolidations" [quoted, secondary] — [Coinfomania](https://www.coinfomania.com/cryptocred-analyzes-bitcoin-trends-what-this-means-for-altcoins/)
  - Morpheus Trading (Deron Wagner) recommends building "a relative strength watchlist of emerging altcoin leadership" (coins near new ATHs while BTC is still below its high) and buying "valid pullbacks or consolidation patterns" [quoted] — [Morpheus Trading](https://morpheustrading.com/blog/4-leading-cryptos/)
- **Token unlocks (Keyrock, 16,000+ unlock events):**
  - About 90% of unlocks push prices down, regardless of size or type.
  - Price impact often starts about 30 days before the unlock, and larger unlocks bring 2.4x sharper drops.
  - Team unlocks are the worst (about −25%); investor unlocks are more controlled; ecosystem unlocks are slightly positive (+1.18% on average) [quoted]

  — [Keyrock](https://keyrock.com/from-locked-to-liquidity-what-16000-token-unlocks-teach-us/); [crypto.news summary](https://crypto.news/token-unlocks-almost-always-negative-for-price-keyrocks-study-reveals/)

  Caveat: The Tie's study of 12,350 priced unlocks found the median unlock was small relative to daily volume — [Streamflow](https://streamflow.finance/blog/token-unlock-report)
- **Low float / high FDV (Binance Research, May 2024):** about $155B of tokens were scheduled to unlock in 2024–2030. Tokens launched in 2024 had an average MC/FDV of just 12.3%, implying about $80B of new demand needed just to hold prices [quoted] — [Cointelegraph](https://cointelegraph.com/news/binance-urges-small-medium-projects-high-fdv-trend); [CryptoPotato](https://cryptopotato.com/binance-doubles-down-on-low-float-high-fdv-calls-for-action/); [Forklog](https://forklog.com/en/binance-highlights-155-billion-token-unlock-overhang/)
- **Leverage and exchange plumbing:**
  - On 2025-10-10, Binance paid $283M in compensation for collateral mis-marked during 21:36–22:16 UTC; USDe printed $0.65 on Binance while trading near $0.99 on Curve and Uniswap. Liquidations were triggered by venue-specific prices [quoted] — [The Defiant](https://thedefiant.io/newsletter/defi-daily/the-ultimate-10-10-crash-autopsy)
  - Hayes has said he personally uses little or no leverage and finds shorting hard [quoted, secondary] — [interview summary](https://ceointerviews.ai/interview/1076739/)

### Inferences
- The best-documented sequencing rule is K33's: broad alt outperformance arrived only after BTC cleared its prior ATH (2017, late 2020–21). In 2019 and 2023, with BTC still far below its prior ATH, breadth was poor except for narrative leaders, which matches my scoreboard. The 2026 setup (BTC around $81.5K vs a $126.2K ATH) is the "below prior ATH" regime, which historically favoured a few leaders rather than baskets.
- The unlock evidence argues for checking each watchlist coin's next-90-day unlock schedule and MC/FDV before sizing it. Team unlocks are the most damaging category.

### Gaps
- I could not retrieve primary, dated quotes from GCR, Hsaka, Pentoshi, Cobie or similar three-cycle traders; their material is mostly X posts that could not be fetched. Their often-cited rules (buy RS leaders on pullbacks, ladder out, avoid leverage on alts) are therefore not quoted here. I found no reliable published statistics on profit-taking ladders.

## 7. How the current setup (low $57.7K on 2026-07-01, first leg to about $87K, now a pullback) maps onto history

### Takeaway
On BTC magnitude and dominance, 2026 so far looks like the slow recoveries of 2015 and 2022–23, not 2019 or 2020. The relevant 2023 base rates: in each of the four 2023 pullback entries, the median top-20 alt fell to a 90-day return of −4% to −12%, and only 0–30% beat BTC. In 2019 and 2023–24, the first real correction cut the median alt 1.3–2.3x as hard as BTC.

### Cited Findings
- 2026 to date [computed] — [CMC historical API](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=1&convertId=2781&timeStart=1780272000&timeEnd=1792108800):
  - Lowest close $58,559 (2026-06-30); intraday low $57,748 (2026-07-01).
  - High close $86,603 (2026-09-21): a +47.9% leg in 83 days.
  - Close $81,501 on 2026-10-16: −5.9% from the high close and +35.8% from the 2026-07-01 close.
  - BTC dominance 57.7% → 59.9%, and rising. ETH/BTC 0.0268 → 0.0297.
- Historical comparison [computed] — [CMC](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=1&convertId=2781&timeStart=1416000000&timeEnd=1700524800):
  - BTC return 3.5 months after the bottom: +32% (2015-01), +97% (2015-08), +51% (2018-12), +84% (2020-03), +29% (2022-11).
  - First leg before the first 15% pullback: +96% in 72 days (Aug–Nov 2015), +302% in 193 days (2019), +147% in 158 days (2020), +57% in 91 days (Nov 2022 – Feb 2023, followed by a −21% dip into 2023-03-09/10).
  - The 2026 leg so far: +48% in 83 days, with no 15% pullback yet.
- Every time BTC first closed 7% below its 60-day closing high within 18 months of a bottom (24 events, 2018–2024), here is what followed over the next 90 days [computed]:

  | Measure | BTC | Median top-20 alt |
  |---|---|---|
  | Further max drawdown, median | −10% | −17% |
  | Further max drawdown, range | −1% to −56% | −2% to −64% |

  | Liquidation-level breach among top-20 alts | Median share | Mean share | Events with a large share |
  |---|---|---|---|
  | 3x | 15% | 28% | ≥40% in 9 of 24 events |
  | 2x | 0% | 14% | ≥35% in 4 of 24 (2019-06-27, 2020-02-25, 2021-03-25, 2021-04-24) |

  — [CMC](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=1&convertId=2781&timeStart=1544832000&timeEnd=1716249600)
- The four 2023 analog entries over the next 90 days [computed]:

  | Entry | BTC further drawdown | Median alt further drawdown | Share at 3x liquidation | Median alt 90-day return | Share of alts beating BTC |
  |---|---|---|---|---|---|
  | 2023-02-09 | −10% | −17% | 0% | −9% | 0% |
  | 2023-03-11 | −1% | −6% | 5% | −4% | 5% |
  | 2023-04-20 | −12% | −30% | 45% | −7% | 30% |
  | 2023-07-24 | −15% | −25% | 25% | −12% | 20% |

  No 2x positions were liquidated in any of the four.

  — [CMC](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=1&convertId=2781&timeStart=1675900800&timeEnd=1698105600)
- The 2019 analog, entering when BTC first closed 7% below its first-leg top (2019-06-27) [computed]:

  | Horizon | Share of top-20 alts at 2x liquidation | Share at 3x liquidation | Median unlevered return |
  |---|---|---|---|
  | 90 days | 60% | 100% | −50% |
  | 180 days | 95% | 100% | −56% |

  The 2024 analog (entry 2024-03-16):

  | Horizon | Share at 2x liquidation | Share at 3x liquidation | Median unlevered return | Median 2x return |
  |---|---|---|---|---|
  | 90 days | 5% | 45% | −18% | – |
  | 180 days | 50% | 75% | −32% | −83% |

  — [CMC](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=1&convertId=2781&timeStart=1561593600&timeEnd=1726444800)
- Holding 2x long from the bottom itself was survivable. Within 365 days, 2x liquidated 10% of top-20 alts (2019), 5% (2020) and 0% (2023), versus 25%, 5% and 15% at 3x [computed] — [CMC](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=1&convertId=2781&timeStart=1544832000&timeEnd=1700524800)
- HYPE is the current-cycle relative-strength outlier. It made a new closing high of $97.18 on 2026-09-22 while BTC was about 31% below its ATH, and closed 17.5% below that high on 2026-10-16 [computed] — [CMC](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=32196&convertId=2781&timeStart=1732838400&timeEnd=1792108800)

### Inferences
- The data favour spot over perps for this phase. Leverage was survivable when entered at the cycle bottom, but entries made after a first leg, during the pullback, were the ones wiped out (2019: 2x liquidations in 60–95% of top-20 alts; 2024: 50% within 180 days). Correlated wick events have taken out about half or more of 2x alt longs three times since 2020 (2020-03-12, 2021-05-19, 2025-10-10).
- If leverage is used at all, history supports 2x at most, on BTC/ETH-like volatility or the strongest large cap, sized so a −50% intraday wick plus a −30% to −60% correction cannot liquidate the account. 3x alt longs were breached in 74–98% of top-50 alts in each major flush, and by 15–28% of top-20 alts in a typical early-bull pullback.
- Base rates say a diversified alt basket is unlikely to beat simply holding more BTC until BTC reclaims its prior ATH ($126K). The historically rewarded alt bet in this regime is a concentrated position (1–3 coins) in leaders already showing 3–6 month relative strength (2019: LINK/BNB; 2023: SOL; 2026: HYPE), with deep spot drawdowns (−40% to −70%) budgeted for and profits laddered out into strength.
