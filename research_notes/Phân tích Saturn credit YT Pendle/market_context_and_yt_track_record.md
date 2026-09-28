# Market backdrop (Sep 2026) for a stablecoin-protocol TGE, and the Pendle YT points-farming track record

Research date: 2026-09-28. All figures are date-stamped; figures from before 2026 are labelled as older data. "API pull" means Claude queried a public data API on 2026-09-28 (DefiLlama, Pendle, FRED, OKX, Hyperliquid). Those raw numbers are primary data, but Claude chose the snapshot dates and did the arithmetic. Other sources are cited inline. Anything taken only from a search-engine summary, without Claude reading the underlying page, is marked "(search-summary only, unverified)".

---

## Q1. Crypto price backdrop: BTC, ETH, total market cap, 3–6 month trend (as of late Sep 2026)

### Takeaway
Crypto is in a sharp relief rally inside a bear-ish year. BTC bottomed near $60k in late June 2026 and is now about $83–84k (+~40% in three months), but it is still about 22% lower year on year and about 30%+ below the Oct-2025 ATH. ETH shows the same pattern (~$1.57k in late June, ~$2.67–2.71k now). Total market cap is back near $2.8–3.0T after falling to about $2.4T at end-Q1 2026. Bitcoin dominance is still high and a broad altseason has not been confirmed.

### Cited Findings
- BTC $84,413 and ETH $2,712.99 at 9am ET on 2026-09-25. BTC is -22.58% YoY (it was $109,040 a year earlier) and +5.89% over one month ($79,715 in late Aug 2026). The article says BTC closed 2025 "roughly 30% below the all-time high it hit that very October" — [Fortune, 2026-09-25](https://fortune.com/article/price-of-bitcoin-09-25-2026/)
- DefiLlama/CoinGecko daily price path (API pull), BTC / ETH: 2026-03-28 $66,328 / $1,991; 2026-06-28 $59,943 / $1,572; 2026-07-28 $63,712 / $1,890; 2026-08-28 $80,268 / $2,511; 2026-09-27 $84,417 / $2,696; current (2026-09-28) $83,062 / $2,666 — [DefiLlama coins API](https://coins.llama.fi/prices/current/coingecko:bitcoin,coingecko:ethereum)
- BTC rose 24.95% in August 2026 and was still 9.62% below its start-of-year level. US spot BTC ETFs took in $3.52B in August 2026 — [Yahoo Finance, Sep 2026](https://finance.yahoo.com/markets/crypto/articles/bitcoin-price-prediction-september-2026-080209568.html). The same article gives BTC market cap as "$1.33T", which does not match an ~$84k price; treat that figure as stale or erroneous.
- Q1 2026: total crypto market cap fell 20.4% to about $2.4T by end-March 2026, about 45% below the Oct-2025 peak, and CEX spot volume fell 39.1% QoQ to $2.7T (search-summary only, unverified; likely from a CoinGecko Q1-2026 report) — [search result context: CryptoRank/CoinGecko coverage](https://cryptorank.io/news/feed/91205-crypto-tokens-trade-below-launch-price)
- Total crypto market cap was about $2.98T on 2026-09-26 and back above $2.8T on 2026-09-19. TOTAL2 (ex-BTC) was about $1.17–1.23T. The altcoin market has added about $371B since June 2026, and 87% of Binance-listed alts are above their 200-DMA. The Altcoin Season Index was 34 on 2026-09-02, so BTC still dominates (search-summary only, unverified) — [cryptonews.net](https://cryptonews.net/news/analytics/33503259/); [OKX Orbit](https://www.okx.com/en-us/orbit/insight/87968812308864); [OneBullEx](https://www.onebullex.com/news/articles/altcoin-season-index-holds-at-34-points-on-september-2-keeping-bitcoin-dominant-2)
- HYPE is about $90 (2026-09-28; it was $63.2 on 2026-06-28) and PENDLE about $2.39–2.64 (it was $1.07 on 2026-04-12) — [DefiLlama coins API](https://coins.llama.fi/prices/current/coingecko:hyperliquid,coingecko:pendle)

### Inferences
- The TGE window is better than in Q2 2026, which was the trough (BTC about $60k, DeFi TVL about $68B). It is still a selective, BTC-led market rather than an altseason. A stablecoin-protocol TGE in Q4 2026 would list into a recovering but fragile tape, where a new Fed hiking cycle (Q3) is a live macro headwind.
- The three-month momentum is strongly positive. Anyone rumoring TGE FDVs off the June lows would be too low, and anyone rumoring off the 2025 peak would be far too high. The sensible reference is today's multiples, discounted for the risk that the rally reverses.

### Gaps
- No primary total-market-cap time series was obtained (the CoinGecko global API was rate-limited). The Q1-2026 figure ($2.4T) and the Sep-2026 figure (~$2.98T) come only from search summaries.
- K33, Glassnode and CoinShares weekly reports were not retrieved.

---

## Q2. Stablecoin supply and DeFi TVL trend

### Takeaway
Total stablecoin supply has been flat at about $300–318B since Oct 2025. In June 2026 it had its biggest monthly contraction in four years, and it has since recovered to about $311B. Growth is now in payments and volume, not supply. DeFi TVL fell from about $155B (Oct 2025) to about $68B (Jul 2026) and has rebounded to about $94B. Yield-bearing and synthetic stablecoins have shrunk far more than fiat-backed ones.

### Cited Findings
- DefiLlama total USD-pegged stablecoin supply (API pull, first of each month, $B): 2025-01 204.8 → 2025-07 252.3 → 2025-10 297.5 → 2025-11 306.0 → 2026-01 305.9 → 2026-04 313.9 → 2026-05 318.0 (peak) → 2026-06 317.4 → 2026-07 308.8 → 2026-08 303.9 → 2026-09 307.3 → 2026-09-28 311.5 — [DefiLlama stablecoins API](https://stablecoins.llama.fi/stablecoincharts/all)
- CoinDesk (2026-07-12): stablecoin market cap fell about $10B from its May 2026 peak (~$310B), including $7.7B in June alone, and has been stalled around $300B since Oct 2025. USDT went from $190B (May) to about $184B; USDC from $80B (Mar 2026 peak) to about $73B — [CoinDesk](https://www.coindesk.com/markets/2026/07/12/stablecoin-market-cap-has-shrunk-by-usd10-billion-since-may-but-analyst-sees-no-reason-to-panic)
- June 2026 saw the biggest monthly drop in four years ($7.7B). The GENIUS Act's yield prohibition "pushed idle capital into tokenized Treasuries". Adjusted volume was a record $1.79T (search-summary only) — [KuCoin](https://www.kucoin.com/blog/stablecoin-market-cap-drops-in-june-2026-largest-decline-in-4-years); [PYMNTS](https://www.pymnts.com/cryptocurrency/2026/stablecoin-market-cap-suffers-biggest-decline-in-4-years/)
- Allium (Sep 2026 report): supply was $303B in Aug 2026, up 6% YoY from $285B. Tether and Circle hold 85%. Exchange-held supply is $89B and DeFi-held supply $26B. Identified payments were $401–527B Jan–Aug 2026, up 42–63% YoY — [CryptoDaily/Allium, Sep 2026](https://cryptodaily.co.uk/2026/09/stablecoin-supply-303b-payments-401b-allium). The data sources disagree on the base: another summary gives $269.4B→$308.0B (+14.3% YoY).
- Current supplies (DefiLlama API pull, 2026-09-28; previous month in brackets): USDT $183.7B ($183.3B); USDC $75.2B ($74.2B); USDS $6.68B; **USDe $4.94B ($4.08B, +21% m/m)**; USD1 $4.43B; USDf (Falcon) $1.21B; USD0 (Usual) $0.55B; apxUSD (Apyx) $0.31B; reUSD $0.28B; USDai $0.22B; avUSD $0.125B; **USDat (Saturn Dollar) $0.085B ($0.080B)**; USR (Resolv) ~$0.001B — [DefiLlama stablecoins API](https://stablecoins.llama.fi/stablecoins?includePrices=true)
- Supply histories of yield and synthetic stablecoins (DefiLlama API pull, $B):
  - USDe: 5.88 (Jan-25), 14.71 (Oct-25 peak), 6.30 (Jan-26), 3.90 (May-26), 4.95 (Sep-28-26).
  - USDf: 2.06 (Jan-26 peak), 1.21 (now).
  - USD0: 1.63 (Jan-25), 0.55 (now).
  - Cap cUSD: 0.348 (Jan-26), 0.087 (now).
  - apxUSD: 0.52 (Jun-26 peak), 0.32 (now).
  - USDat: 0.11 (Jul/Aug-26), 0.07–0.08 (Sep-26).
  - Source: [DefiLlama stablecoin endpoints](https://stablecoins.llama.fi/stablecoins)
- Ethena: USDe peaked at about $15B (Oct 2025) and was below $5B by late Aug 2026 (a >65% contraction). ENA incentives for USDe go to zero after Sep 2026 (about an 85% reduction since 2024; >$750M distributed in total). A Sep-2026 governance proposal ties ENA buybacks to USDe supply above $7.5B — [CryptoBriefing, 2026-09-26](https://cryptobriefing.com/ethena-ends-usde-token-incentives/); [Ethena on X](https://x.com/ethena/status/2103758327142641925)
- DefiLlama total DeFi TVL (API pull, first of month, $B): 2025-08 135.8, 2025-09 150.7, **2025-10 155.3 (peak)**, 2025-12 115.7, 2026-01 114.4, 2026-03 90.3, 2026-05 82.3, 2026-06 79.1, **2026-07 68.2 (trough)**, 2026-08 72.9, 2026-09 86.9, 2026-09-28 94.0 — [DefiLlama API](https://api.llama.fi/v2/historicalChainTvl)
- On 2026-09-21 DefiLlama showed $93.9B TVL: Ethereum $52.7B, Solana $6.2B, Base $5.9B; Lido $26.0B, Aave $19.2B, Morpho $10.7B (search-summary only) — [DefiLlama](https://defillama.com/)
- Solana stablecoin supply hit a record $17.3B on 2026-09-25 — [Solana Compass](https://solanacompass.com/news/solana-stablecoin-supply-hits-new-all-time-high-of-173b)

### Inferences
- A new yield stablecoin does not have a rising tide behind it. The aggregate is flat, and share is concentrating in USDT/USDC plus a few bank or fintech issuers. Most 2025-vintage synthetic or yield stablecoins have lost 40–100% of their peak supply: USDe -66%, USD0 -66%, USDf -41%, cUSD -75%, USR ~-100%, lvlUSD ~-100%, deUSD wound down. This context matters for the FDV a small stablecoin (e.g., USDat, ~$85M supply) can command.
- USDe's +21% m/m rebound and the DeFi TVL recovery since July are early signs that carry demand is returning, but they are not yet a trend.

### Gaps
- DeFi TVL by category (e.g., yield-stablecoin category TVL) was not pulled.
- Allium ($303B) and DefiLlama ($311B) measure different stablecoin universes, so the exact supply depends on methodology.

---

## Q3. Yield drivers: perp funding/basis (Ethena-style) and Fed/T-bill rates (RWA-style)

### Takeaway
Crypto-native carry is low: BTC/ETH perp funding runs about 5% annualized (30-day, OKX) and sUSDe yields about 4.8%. Risk-free USD rates are rising again. The Fed hiked 25bp on 2026-09-16 to 3.75–4.00% and signalled more hikes. The 3M T-bill is 4.24% and the 10Y is 5.18%. RWA- and T-bill-backed stablecoins therefore now out-yield basis-trade stablecoins. Rising rates are also a headwind for crypto risk appetite and token FDVs.

### Cited Findings
- FOMC, 2026-09-16: the Fed funds target was **raised** 25bp to 3.75–4.00%, 12-0. Statement: "Inflation remains elevated. Today's policy action will support a timelier return to the Committee's 2 percent goal" — [Federal Reserve press release](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm)
- Dot plot: 16 of 18 participants expect another hike and four see two more possible. Markets price one more 25bp hike in 2026, with hikes continuing into 2027 (search-summary only) — [CNBC, 2026-09-16](https://www.cnbc.com/2026/09/16/fed-rate-decision-september-2026.html)
- FRED (API pull):
  - Effective Fed funds: 3.63% (Aug 2026) → 3.88% (2026-09-24). A year earlier (Sep 2025, older data) it was 4.33%.
  - 3M T-bill (DGS3MO): 3.65% (Jan 2026 low) → 3.92% (2026-09-01) → 4.24% (2026-09-24).
  - 10Y (DGS10): 4.19% (Jan 2026) → 4.79% (2026-09-01) → 5.18% (2026-09-24).
  - Sources: [FRED DGS3MO](https://fred.stlouisfed.org/series/DGS3MO); [FRED DFF](https://fred.stlouisfed.org/series/DFF); [FRED DGS10](https://fred.stlouisfed.org/series/DGS10)
- Perp funding (API pulls, 2026-09-28): OKX BTC-USDT-SWAP averaged 5.45% annualized and ETH-USDT-SWAP 4.92% (2026-08-29 → 2026-09-28). Hyperliquid BTC 7-day funding was about 9.96% annualized, close to Hyperliquid's built-in baseline interest component, so it does not signal strong long demand — [OKX API](https://www.okx.com/api/v5/public/funding-rate-history?instId=BTC-USDT-SWAP); [Hyperliquid info API](https://api.hyperliquid.xyz/info)
- sUSDe 7-day APY was 7.1% in June 2026, down from 9.4% in April as funding compressed. Perps now make up only about 11% of USDe backing as Ethena pivots to institutional lending, RWAs and basis trades — [Eco support article](https://eco.com/support/en/articles/15254002-ethena-usde-and-susde-2026-delta-neutral-yield); [Unchained](https://unchainedcrypto.com/ethena-overhauls-usde-reserves-with-institutional-lending-and-real-world-assets/)
- Pendle's sUSDe underlying APY was 4.8% on 2026-09-28, with implied APY 5.1–5.3% on Oct/Nov-2026 maturities — [Pendle API](https://api-v2.pendle.finance/core/v2/markets/all?isActive=true)

### Inferences
- With T-bills at about 4.2% and rising, and basis at about 5%, a stablecoin's "native" yield has little room above risk-free unless it takes credit or duration risk (e.g., STRC-style digital credit at 12%). Points-driven YT premia therefore make up a large share of the total "APY" that farmers see.
- Hawkish Fed repricing (10Y above 5%) is the main macro risk to the current crypto rally and hence to Q4-2026 TGE FDVs.

### Gaps
- No aggregated, OI-weighted funding series (Glassnode, The Block, Coinglass) was retrieved. Hyperliquid 30/90-day pulls were rate-limited.
- Ethena's current (Sep 2026) sUSDe APY comes from the Pendle feed only, not Ethena's own dashboard.

---

## Q4. Strategy (MSTR) STRC / digital-credit status (relevant to BTC-backed yield stablecoins)

### Takeaway
STRC still pays 12.00% a year, semi-monthly. It fell to an intraday low of $71.25 in June 2026, its deepest drawdown since launch. It has recovered to about $97 on $635M of buybacks but remains below its $100 par, so the STRC ATM is paused. Apyx, an STRC-backed stablecoin, postponed its Oct-2026 TGE explicitly because of this drawdown. Strive's SATA (13%) is holding par better.

### Cited Findings
- STRC dividend is 12.00% a year ($0.50 semi-monthly), payable 2026-09-30. Management will keep 12.00% "until STRC has demonstrated sustained, healthy trading near $100 per share." Q3 dividends on the other preferreds: STRF 10%, STRK 8%, STRD 10%, STRE 10% (€) — [SEC 8-K, 2026-08-31](https://www.sec.gov/Archives/edgar/data/0001050446/000119312526377583/mstr-20260831.htm)
- STRC hit an intraday low of $71.25 in June 2026, the deepest on record since its July-2025 launch. Strategy later sold 3,588 BTC for $216M to fund dividends (search-summary only) — [CoinDesk, 2026-06-18](https://www.coindesk.com/markets/2026/06/18/strategy-s-strc-preferred-stock-hits-a-record-low-below-par); [Blockhead, 2026-06-23](https://www.blockhead.co/2026/06/23/strcs-slide-below-par-puts-strategys-funding-machine-to-the-test/)
- As of 2026-09-01: STRC was $97.34 after $635.2M of buybacks (latest $151.8M at an average of $97.48). Strategy holds 845,050 BTC and bought 4,603 BTC at about $80k, its first purchase in two months. Strive's SATA pays 13% daily and holds about $100 par. MSTR is -15% YTD — [CoinDesk, 2026-09-01](https://www.coindesk.com/markets/2026/09/01/strategy-spends-usd635m-buying-back-strc-as-perpetual-preferred-stock-lags-usd100-par)
- STRC's ATM is paused while it trades below par (search-summary only) — [CoinDesk, 2026-09-01](https://www.coindesk.com/markets/2026/09/01/strategy-spends-usd635m-buying-back-strc-as-perpetual-preferred-stock-lags-usd100-par)
- Apyx (apyUSD, with STRC as core reserve) postponed its TGE from 2026-10-13 to TBA on 2026-09-23. Reasons given: STRC's "deepest and longest drawdown in its brief history" and institutional expansion. The Season-2 airdrop was raised from 6% to 9% of supply to reflect the longer accrual; Pendle and Curve positions keep scoring — [ChainCatcher](https://www.chaincatcher.com/en/article/2291854)
- Pendle (2026-09-28): apyUSD (Nov-26) has TVL $67M, implied 15.1% vs underlying 14.0%, with 32–52x "Pips". apxUSD has TVL $18.5M, implied 14.8%, with 100–128x Pips. STRCx (xStocks) has TVL $32M, implied 20.2% vs underlying 12.3% — [Pendle API](https://api-v2.pendle.finance/core/v2/markets/all?isActive=true)

### Inferences
- For any STRC/digital-credit-backed stablecoin, including Saturn's USDat/sUSDat, the June-2026 STRC drawdown is both a proven risk and a TGE-timing risk. The closest comparable (Apyx) chose to delay its TGE and **increase** the airdrop pool, which dilutes the points of existing farmers relative to the original plan (per-point value moves ambiguously: the pool is 1.5x larger but accrual runs longer). YT pricing for this sector should assume similar delays.

### Gaps
- STRC's exact price on 2026-09-28 and the current ATM status were not verified beyond 2026-09-01.

---

## Q5. Altcoin/TGE environment 2025–2026: post-listing performance, delays, regulation

### Takeaway
New-token outcomes are poor across every dataset:
- Memento: 84.7% of 2025 TGEs were below their TGE valuation, with a median of -71%. Launches above $1B FDV had a 0% green rate.
- CryptoRank (Jul 2026): 92.9% of 2024–2026 launches still above $100M market cap trade below TGE price, with a median of -95.7%.
- Stablecoin projects were among the worst categories in 2025, averaging -70%.

Several DeFi and stablecoin protocols (Avant, Apyx, OpenSea, Zetarium) delayed TGEs in 2026, citing market conditions. On regulation, the GENIUS Act's yield ban stands and the CLARITY Act's yield compromise failed. That is a headwind for passive-yield stablecoins, not a tailwind.

### Cited Findings
- Memento Research, 118 TGEs in 2025 (data as of 2025-12-20; older data):
  - 84.7% below TGE valuation; median -71.1% FDV and -66.8% MC.
  - 65% fell ≥50% and 51% fell ≥70%.
  - By FDV bucket: $25–200M median -26% (40% green); $210–489M -73% (13% green); $500–940M -82% (3% green); ≥$957M -83% (0% green).
  - Source: [Memento Research](https://mementoresearch.com/state-of-2025-token-launches-year-in-review)
- In the same study, stablecoin projects averaged -70% and DeSci -93%, while perp DEXs averaged +200% — [The Defiant](https://thedefiant.io/news/research-and-opinion/token-launches-with-low-fdvs-vastly-outperformed-hyped-debuts-in-2025-memento-research)
- CryptoRank (2026-07-21): of 113 tokens launched 2024–2026 with market cap above $100M, 92.9% trade below TGE price and the median return is -95.7%. Only 8 are above, e.g., HYPE +1,519%, ONDO +101%, EVA +20%, NIGHT +16.5% — [Bitget/CryptoRank](https://www.bitget.com/news/detail/12560605525394); [Crypto Economy](https://crypto-economy.com/only-8-crypto-tokens-launched-since-2024-remain-profitable-as-most-collapse-below-tge-prices/)
- Keyrock, 62 airdrops (older data, 2024): 88% of airdropped tokens declined, mostly within the first 15 days. Only 8 of 62 were positive at 90 days. High FDV was "the single most damaging factor" — [Keyrock](https://keyrock.com/airdrops-in-the-barren-desert/); [DL News](https://www.dlnews.com/articles/snapshot/keyrock-study-says-most-token-airdrops-crash-after-launch/)
- About 32% of new listings on the top 12 CEXs were positive 30 days after listing (search-summary only; original source not identified).
- Farmed-protocol tokens, day-1 → day-30 / day-90 / now (2026-09-28), from DefiLlama/CoinGecko daily closes (API pull). "Day 1" is the first daily close, which can differ from the opening print.
  - 2024 (older data):
    - ENA $0.78 → +9% / -34% / -66%
    - ETHFI $3.12 → +13% / +28% / -78%
    - REZ $0.160 → -14% / -62% / -97%
    - EIGEN $3.99 (Oct-2024 transferability) → -37% / -12% / -94%
    - SWELL $0.038 → +30% / -69% / -98%
    - PUFFER $0.71 → -61% / +11% / -97%
    - USUAL $1.07 → -7% / -77% / -99%
    - SOLV (Jan 2025) $0.13 → -74% / -82% / -97%
  - 2025:
    - RESOLV $0.35 → -48% / -56% / -95%
    - SPK $0.057 → -42% / +4% / -60%
    - HUMA $0.067 → -53% / -60% / -60%
    - TREE $0.67 → -47% / -73% / -93%
    - MITO $0.21 → -29% / -58% / -93%
    - BARD $1.06 → -41% / -24% / -87%
    - XPL $1.28 → -70% / -90% / -92%
    - FF $0.284 → -47% / -69% / -54%
    - STABLE $0.0215 → -32% / +23% / +26%
  - Source: [DefiLlama coins chart API](https://coins.llama.fi/chart/coingecko:ethena)
- Delays:
  - OpenSea delayed its SEA TGE beyond Q1 2026, citing market conditions, and offered fee refunds — [Bankless](https://www.bankless.com/read/news/opensea-foundation-delays-q1-2026-tge-target)
  - Avant (avUSD) postponed its TGE to mid-September, saying "DeFi tokens as a whole are currently under pressure" and pointing to recent exploits. Points accrual stopped May 15 (year presumed 2026; not confirmed on the retrieved page) — [Bitget News](https://www.bitget.com/news/detail/12560605409666)
  - Zetarium delayed to Q2 2026 on exchange-partner advice — [CoinGabbar](https://www.coingabbar.com/en/crypto-currency-news/zetarium-airdrop-tge-listing-update-delay-q2-2026)
  - Apyx postponed its Oct-13-2026 TGE (see Q4) — [ChainCatcher](https://www.chaincatcher.com/en/article/2291854)
- Regulation: the GENIUS Act (signed July 2025) bars payment-stablecoin issuers from paying yield. The CLARITY Act's yield compromise (Tillis–Alsobrooks, May 2026) did not pass, so "the GENIUS Act is now the primary law governing stablecoin rewards." On 2026-09-24 the Fed proposed GENIUS implementing rules in which certain third-party arrangements are "presumed to be prohibited payments of interest or yield", leaving a narrow credit-card-style rewards path. Regulators are past the July-2026 statutory deadline — [CoinDesk, 2026-09-24](https://www.coindesk.com/policy/2026/09/24/u-s-federal-reserve-moves-on-proposals-to-implement-genius-act-for-stablecoins); [CoinDesk, 2026-05-02](https://www.coindesk.com/policy/2026/05/02/crypto-industry-backs-clarity-act-yield-compromise-pushes-senate-banking-for-markup)
- Binance HODLer Airdrops category market cap was about $2.3B (undated snapshot). Gensyn was the 64th HODLer project (May 2026) and Brevis the 60th (Jan 2026). No systematic performance statistics were found — [CoinGecko category](https://www.coingecko.com/en/categories/binance-hodler-airdrops)

### Inferences
- Base rates for a stablecoin-protocol TGE in late 2026: about 85–93% chance of trading below TGE price within months, and a median day-30 drawdown of about -40% in the farmed-token sample above (14 of 17 negative at day 30; median roughly -41%). Launching above $500M FDV has historically had a ≤3% chance of being green.
- The "stablecoin narrative" is split. Payments and bank or fintech stablecoins have tailwinds from GENIUS implementation, the Fed rules and Allium payment growth. Yield-bearing DeFi stablecoin protocols face regulatory friction on yield, a history of blow-ups, and a -70% category average in 2025.

### Gaps
- No 2026-specific TGE cohort statistics were found (e.g., a share of 2026 TGEs below listing at 30/90 days). The CryptoRank set mixes 2024–2026.
- No systematic Binance HODLer 2026 performance study was found.
- Avant's actual TGE outcome (mid-Sep 2026) was not found.

---

## Q6. Pendle's current state: TVL, points-market share, mechanics and fees

### Takeaway
Pendle v2 TVL is about $1.15–1.26B, down about 88–91% from its Sep-2025 peak ($10.6B DefiLlama month-start; $13.4B per Pendle). On 2026-09-28, points-bearing markets were about 69% of Pendle's active TVL and about 90% of its 24h volume, so points farming is still Pendle's core retail use case. Emissions are down 93% YTD and buybacks exceed emissions. No change to YT points mechanics was found; the YT fee on yield and points has historically been 3%.

### Cited Findings
- Pendle TVL from DefiLlama (API pull, first of month, $B):
  - 2024: Jun 6.22 (peak), Oct 1.97.
  - 2025: Feb 5.49, **Sep 10.61**, Dec 3.41.
  - 2026: Jan 3.69, Mar 2.27, May 1.50, **Jul 0.96**, Sep 1.19; 2026-09-28 1.26.
  - Source: [DefiLlama protocol API](https://api.llama.fi/protocol/pendle)
- Pendle's 2025 review: average TVL $5.8B (+79% YoY), peak $13.4B, volume $47.8B; 85% of TVL in stablecoins — [Phemex](https://phemex.com/news/article/pendles-tvl-soars-to-58-billion-in-2025-up-79-yearonyear-42499); [Lookonchain](https://www.lookonchain.com/feeds/39375)
- Q1-2026 average TVL was $2.57B (-48% QoQ). TVL fell from $1.44B (May 2026) to $1.02B (2026-06-23). H1-2026 average daily TVL was about $1.3B. Boros cumulative volume passed $14B in H1-2026 — [Token Terminal dashboard](https://tokenterminal.com/explorer/studio/dashboards/1539e4ad-107b-4947-9948-0fbb8e82e2d3); [Bitget, 2026-07-23](https://www.bitget.com/news/detail/12560605533510)
- Revenue: $44.6M in 2025. Monthly revenue fell from $4.44M (Aug 2025) to $0.55M (Mar 2026). Up to 80% of revenue now goes to buybacks. PENDLE was $1.07 on 2026-04-12 (-85.8% from ATH) — [LiveBitcoinNews, 2026-04-12](https://www.livebitcoinnews.com/pendle-drops-85-as-revenue-slumps-buyback-shift-signals-turnaround/)
- Pendle Print #126 (2026-09-28): "Emission is down 93% YTD" and buybacks outpace new supply 10.4x. PT-looping fees are now dynamic (about 10% of loop APY, capped at 10bps). New points campaigns include Asseto NGI+ (40x Reale points) — [Pendle Print #126](https://pendlefi.substack.com/p/pendle-print-126)
- Weekly incentives cut from about 90k to about 21k PENDLE; about 2M PENDLE bought back (H2-2026 roadmap) — [Bitget, 2026-07-23](https://www.bitget.com/news/detail/12560605533510)
- Active-market snapshot (Pendle API pull, 2026-09-28; 79 markets across 9 chains):
  - Total TVL $1,149M and 24h volume $13.3M.
  - Markets carrying points: 50 of 79, **$787.5M TVL (69%)** and **$12.0M 24h volume (90%)**.
  - Largest: reUSD (re.xyz) $216M TVL, implied 11.6% vs underlying 7.0%, 30x Re + 5x Sats. AUSD $115M. sUSDS $99M. USDai $90M, implied 10.1%, 25x.
  - Saturn: USDat (Monad) $42.8M, implied 9.1% vs underlying 3.0%, 30x Saturn points. USDat (ETH) $20.4M, implied 9.0%. sUSDat (ETH / Monad) $6.1M / $4.7M, 10x.
  - Source: [Pendle API](https://api-v2.pendle.finance/core/v2/markets/all?isActive=true)
- Points and fees:
  - "Pendle does NOT give nor generate additional points … simply streams points from the underlying to YT holders" — [Pendle docs, Points Support](https://docs.pendle.finance/pendle-academy/ecosystem-and-resources/points-trading/points-support-page)
  - Pendle applies a 3% fee to yield and points earned through YT — [DeFi Sentinel, 2026-06-27](https://defisentinel.org/research/introduction-to-point-farming-2026). The Usual campaign also stated "Pendle's DAO takes a 3% fee on all YT Pills" (2024; older data) — [Usual blog](https://usual.money/blog/pendle)
  - Pendle's dashboard assumes points are worth $0, so YT PnL shows deeply negative until an airdrop is added — [Pendle docs](https://docs.pendle.finance/pendle-academy/ecosystem-and-resources/points-trading/points-support-page)

### Inferences
- Pendle's liquidity in points markets is thin: $13M of 24h volume across all markets. Size limits and price impact matter for any YT position sizing.
- On 2026-09-28 the market-implied "points premium" (implied APY minus underlying APY) was about 6.1pp/yr on USDat and 4.6pp/yr on reUSD. On sUSDe it was only about 0.3–0.5pp, consistent with Ethena ending ENA incentives. This premium is what YT buyers pay for points.

### Gaps
- No Dune breakdown of YT-only volume was found. The 69%/90% figures are a single-day snapshot and include PT/LP flows in points markets.
- The current (2026) YT fee rate was not confirmed on Pendle's own fee docs page. The 3% figure is from a secondary 2026 source and a 2024 partner blog.

---

## Q7. Case studies: Pendle YT points-farming outcomes (2024–2026)

### Takeaway
The record splits sharply by vintage:
- **Early and novel farms paid out** when bought early: EtherFi S1, Ethena S1, Usual S1/Pills, and Plasma/Stable-style pre-deposits.
- **Later seasons, crowded farms and small stablecoins mostly lost**: Ethena S2, S4 and S5; Renzo; EigenLayer via Pendle; Swell and Puffer; Resolv; Falcon; Level; Elixir.
- The loss drivers were lower-than-expected FDV or token price at claim, points dilution, delayed or restricted claims, and protocol failure.

Precise per-wallet YT ROI is rarely published. Most "wins" are anecdotal, while the losses can be inferred from price data.

### Cited Findings

**EtherFi / LRT restaking era (2024; older data)**
- Traders who used YT-eETH to farm EigenLayer points recouped their whole YT cost from the ETHFI airdrop, which made the EIGEN exposure effectively free. ETHFI's first daily close was $3.12 (2024-03-18) and it was +13% at day 30 and +28% at day 90 — [Tencent/Lianpr repost of analysis, 2025-05-26](https://news.qq.com/rain/a/20250526A0465200); [DefiLlama coins API](https://coins.llama.fi/chart/coingecko:ether-fi). The ROI claim is qualitative and anecdotal.
- YT-eETH in the Karak pool earned 31x Karak, 62x EtherFi and 21x EigenLayer multipliers. Renzo YT gave up to 117x Renzo points vs spot — [OnchainTimes, Apr 2024](https://www.onchaintimes.com/5-insane-roi-pointsairdrop-strategies/)
- **Renzo:** OTC and secondary markets valued points at **$0.45 per point** (Apr 2024). The realized airdrop value was about **$0.12 per ezPoint** (0.36 REZ × $0.34). REZ TGE was 2024-04-30 with 5% to users; ezETH depegged to 0.93 ETH — [OnchainTimes](https://www.onchaintimes.com/5-insane-roi-pointsairdrop-strategies/); [Ouroboros Research](https://ouroborosresearch.substack.com/p/ouroboros-market-update-3-renzo-airdrop). REZ was -62% at day 90 and is -97% now — [DefiLlama](https://coins.llama.fi/chart/coingecko:renzo)
- **EigenLayer:** pre-TGE estimates were about $0.10–0.14 per point — [Metaverse Post](https://mpost.io/eigenlayer-points-post-eigen-airdrop-could-reach-1b-potentially-yielding-0-1-to-users/); [AiCoin](https://www.aicoin.com/en/article/389227)
  - Only 5% went to the first round. The first season was limited to direct stakers and LRT holders, and Pendle/DeFi users were pushed to phase 2. PENDLE fell >50% within a month — [Bitget News](https://www.bitget.com/news/detail/12560603983274); [PANews](https://panews.io/articles/m0ngi707vao3)
  - Pendle lost about $3B TVL (-40%) in one week in June 2024 as LRT markets expired and airdrops faded — [DL News, 2024-07-01](https://www.dlnews.com/articles/defi/pendle-hit-with-3bn-drawdown-as-restaking-airdrops-fade/)
  - EIGEN's first transferable close was $3.99 (Oct 2024), -37% at day 30 — [DefiLlama](https://coins.llama.fi/chart/coingecko:eigenlayer)
- **Swell / Puffer:** SWELL was -69% at day 90 and PUFFER -61% at day 30 after TGE. Puffer points were quoted at about $0.0089 pre-TGE — [DefiLlama](https://coins.llama.fi/chart/coingecko:swell-network); [OnchainTimes](https://www.onchaintimes.com/5-insane-roi-pointsairdrop-strategies/)

**Ethena seasons (USDe/sUSDe YT)**
- **S1 (shards → ENA, Apr 2024):** ENA launched at about a $1B market cap. Pendle YT gave about 7x leveraged shard exposure — [The Defiant](https://thedefiant.io/news/defi/ethena-labs-ena-launches-at-usd1-billion-post-airdrop-as-sats-campaign-kicks-off); [Dune, "The Pendle Effect"](https://x.com/Dune/article/2051286497974980686). ENA was $0.616 on 2024-04-02 and $0.897 on 2024-06-01 — [DefiLlama](https://coins.llama.fi/prices/historical/1712059200/coingecko:ethena)
- **S2 (sats, Apr → Sep 2, 2024):** ENA fell from $0.897 (2024-06-01) to $0.236 at season end (2024-09-02), about -74% — [DefiLlama](https://coins.llama.fi/chart/coingecko:ethena). An Aug-2024 analysis said early YT-sUSDe buyers "may face large losses" because of the falling ENA price — [PANews](https://panews.io/articles/m0ngi707vao3). A rule change requiring YT-sUSDe holders to meet extra conditions drew controversy (search-summary only) — [Binance Square / TheMerkleNews](https://www.binance.com/en/square/post/13159005718425). ENA later jumped from $0.28 to $0.42 after the S2 claim — [AirdropAlert](https://airdropalert.com/blogs/ethena-ena-price-surge-after-airdrop/)
- **S3 (Sep 2, 2024 → Mar 23, 2025):** 3.5% of supply, about $178.5M at the 2025-05-01 claim — [X, Airdrop_Adv](https://x.com/Airdrop_Adv/status/1917709309632471225). ENA was $1.14 in mid-Dec 2024, $0.396 at season end and $0.333 at claim — [DefiLlama](https://coins.llama.fi/chart/coingecko:ethena). The Pendle sUSDe multipliers were 20x (3-month) and 25x (6-month) — [BlockBeats/Bitget](https://www.bitget.com/news/detail/12560604188138)
- **S4 (Mar → Sep 24, 2025):**
  - Ex-ante model (2025-05-26): YT-sUSDe at 0.0161 USDe (62x) with 66 days to maturity, ENA $0.359, a 3.5% pool and 168.6B sats per day gave an estimated "393% APY". The author noted that without points the YT "basically" returns nothing — [LianPR](https://www.lianpr.com/en/news/detail/304729)
  - Realized: 3.5% nominal, but only 1.5% was instantly claimable. Another 1% was vested for the top 2,000 wallets, and the last 1% is contingent on Hyena Trade going live. ENA was about $0.33 at claim — [AirdropAlert S4](https://airdropalert.com/airdrops/ethena-season-4/); [The Defiant](https://thedefiant.io/news/defi/ethena-season-4-rewards-go-live)
  - Rewards went live more than a month after the season ended — [The Defiant](https://thedefiant.io/news/defi/ethena-season-4-rewards-go-live)
  - USDe supply rose from $5.3B (2025-07-01) to $14.7B (2025-10-01) during S4 — [DefiLlama](https://stablecoins.llama.fi/stablecoins)
- **S5 (Sep 25, 2025 → Mar 25, 2026):** 2% of supply (about 300M ENA), claim opened 2026-05-05 — [KuCoin](https://www.kucoin.com/blog/how-to-claim-ethena-season-5-airdrop). ENA was $0.097 at season end and $0.107 at claim, vs $0.607 at the S4 end — [DefiLlama](https://coins.llama.fi/chart/coingecko:ethena)
- **S6** began 2026-03-26 — [MEXC blog](https://blog.mexc.com/news/ethena-airdrop-guide-before-the-season-5-deadline/). Ethena says USDe-related token incentives go to zero at the end of Sep 2026 — [Ethena on X](https://x.com/ethena/status/2103758327142641925)

**Usual (USD0++ YT, Pills → USUAL, Nov 2024; older data)**
- 7.5% of USUAL went to Pills holders, and YT-USD0++ earned 3 Pills per day per YT — [Usual blog](https://usual.money/blog/golden-yt-winners); [Usual blog](https://usual.money/blog/pendle)
- YT buyers reportedly made "over 10x" (other reports say about 5x vs 3–4x expected in "moonsheets") (search-summary only, anecdotal) — [ChainCatcher](https://www.chaincatcher.com/en/article/2196073); [Tencent repost](https://news.qq.com/rain/a/20250526A0465200)
- USUAL's first daily close was $1.07 (2024-11-18). It was -7% at day 30, -77% at day 90 and is -99% now — [DefiLlama](https://coins.llama.fi/chart/coingecko:usual)
- On 2025-01-10 Usual changed USD0++ redemption to a $0.87 floor, and USD0++ fell to $0.89. About one third of Usual TVL sat in Pendle, where PT holders took substantial losses and Morpho liquidations failed — [The Block](https://www.theblock.co/post/333995/usual-money-protocol-update); [Leviathan News](https://leviathannews.substack.com/p/collateral-damage-usd0-depeg-leaves)
- USD0 supply went from $1.63B (Jan 2025) to $0.55B (Sep 2026) — [DefiLlama](https://stablecoins.llama.fi/stablecoins)

**Resolv (USR / wstUSR / RLP YT)**
- Season 1 ran nine months and ended in the May-2025 Genesis airdrop (10% of supply). YT earned points on the full underlying notional — [Resolv docs / CryptoRank drophunting](https://docs.resolv.xyz/litepaper/using-resolv/resolv-points/seasons/season-1)
- RESOLV's first close was $0.35 (2025-06-11): -48% at day 30, -56% at day 90, -95% now — [DefiLlama](https://coins.llama.fi/chart/coingecko:resolv)
- On 2026-03-22 a compromised key minted $80M of unbacked USR and about $25M was extracted. USR traded as low as $0.025 on Curve. Morpho took $6.2M of bad debt — [CoinDesk](https://www.coindesk.com/markets/2026/03/23/resolv-stablecoin-drops-70-after-usd80-million-exploit-after-attacker-mints-usr); [Chainalysis](https://www.chainalysis.com/blog/lessons-from-the-resolv-hack/)
- USR supply went from $0.40B (Feb 2026) to about $0.01B (Jun–Sep 2026) — [DefiLlama](https://stablecoins.llama.fi/stablecoins)

**Spark (SPK, Jun 2025)**
- SPK's first close was $0.057: -42% at day 30, -60% now — [DefiLlama](https://coins.llama.fi/chart/coingecko:spark-2)
- One farmer reported an 86% loss on a YT position before counting points, partly offset by a 5,295 SPK airdrop (search-summary only, anecdotal; attribution unclear — possibly the [FIP Crypto thread](https://x.com/fipcrypto/status/1956731358073569415))

**Falcon (USDf/sUSDf YT, Miles → FF, Sep 2025)**
- FF's first close was $0.284 (2025-09-29): -47% at day 30, -69% at day 90, $0.13 now — [DefiLlama](https://coins.llama.fi/chart/coingecko:falcon-finance-ff)
- Pendle claimed 2.32M FF worth about $294K from Miles Season 1 (2025-10-10), which implies about $0.127 per FF — [Phemex](https://phemex.com/news/article/pendle-claims-294k-in-falcon-finance-airdrop-25424)
- Later Pendle pools (Jan-2026 maturity) offered 36x to 72x Miles to YT-sUSDf — [search summary of Falcon materials](https://docs.falcon.finance/falcon-miles)
- USDf supply went from $2.06B (Jan 2026) to $1.21B now — [DefiLlama](https://stablecoins.llama.fi/stablecoins)

**Level (lvlUSD / slvlUSD YT)**
- Pendle launch (Feb 2025): 40x XP plus Symbiotic points for lvlUSD YT and LP, and 20x for slvlUSD — [Level on X](https://x.com/levelusd/status/1894557798857416768)
- On 2025-09-26 Level announced its acquisition by an unnamed DeFi protocol and a wind-down. The last yield distribution was 2025-10-02. No token or XP compensation was mentioned — [Bitget News](https://www.bitget.com/news/detail/12560604988048); [Level docs](https://level-money.gitbook.io/level-documentation)
- lvlUSD supply went from $0.169B (May 2025) to about $0 — [DefiLlama](https://stablecoins.llama.fi/stablecoins)

**Elixir (deUSD)**
- After Stream Finance disclosed about $93M in losses (2025-11-04), deUSD (about 65% backed by loans to Stream) fell about 98% to roughly $0.015–0.025 and was wound down. About $1B left DeFi yield products in a week — [Pharos](https://pharos.watch/learn/case-studies/stream-elixir-contagion-2025/); [The Block](https://www.theblock.co/post/377961/elixir-sunsets-deusd-synthetic-stablecoin-following-stream-finance-unwinding-aims-full-redemptions)

**Plasma / Stable (stablecoin-chain pre-deposits, late 2025)**
- **Plasma:** because 25M XPL was split equally across depositors, a $1 pre-deposit received 9,304 XPL, about $10,000 at launch — [KuCoin](https://www.kucoin.com/square/post/content_6ab808fc003e86000766b240); [PANews](https://www.panewslab.com/en/articles/1237e3c6-812c-46b4-b0f8-8a30a3ddc7dc)
  - XPL's first close was $1.28 (2025-09-26): -70% at day 30, -90% at day 90 — [DefiLlama](https://coins.llama.fi/chart/coingecko:plasma)
  - Pendle on Plasma ran 5 markets with $900K a week in XPL incentives — [Bitget](https://www.bitget.com/news/detail/12560604997882)
- **Stable:** pre-deposit receipts held on Pendle were eligible for the airdrop (2025-12-08) — [Stable blog](https://blog.stable.xyz/the-stable-airdrop)
  - Prediction markets gave more than 85% odds of a listing-day FDV above $2B — [Bitget](https://www.bitget.com/amp/news/detail/12560605101314)
  - STABLE's first close was $0.0215: -32% at day 30, +26% now (one of the few above day 1) — [DefiLlama](https://coins.llama.fi/chart/coingecko:stable-2)

**2026 stablecoin farms**
- **USD.AI (USDai YT → CHIP):**
  - ICO at $0.03 (Feb 2026); 3% airdrop (300M CHIP) fully unlocked. CHIP was about $0.042, a $416M FDV (undated CoinGecko snapshot) — [search summary of CoinGecko / ICO Drops](https://icodrops.com/usd-ai/)
  - "Protected CHIP" for ICO participants settles at $270M / $190M FDV floors, with a USDC refund if below — [USD.AI](https://usd.ai/insights/chip-is-live)
  - A Pendle-affiliated account called USDai YTs "generational wealth" (biased and anecdotal) — [Pendle Intern on X](https://x.com/PendleIntern/status/2047152449350414840)
- **Re (reUSD → $RE, claims 2026-06-18):** wallets with up to 150M points (95% of participants) were fully unlocked. Larger wallets got 10% up front plus 6 tranches over 3 years — [Re](https://re.xyz/insights/re-tge-launch). Season-2 points (30x) are still live on Pendle with $216M TVL — [Pendle API](https://api-v2.pendle.finance/core/v2/markets/all?isActive=true)
- **Apyx:** TGE postponed and the S2 pool raised from 6% to 9% (see Q4) — [ChainCatcher](https://www.chaincatcher.com/en/article/2291854)
- **Terminal Finance (Ethena-incubated):** $280M pre-launch TVL (Oct 2025), with up to 10% of supply to sENA holders — [Chainwire](https://chainwire.org/2025/10/28/ethena-incubated-dex-terminal-finance-tops-280m-tvl-before-launch/)

### Inferences
- Clearly positive for YT buyers (per available evidence): EtherFi S1 (early), Ethena S1 (early), Usual Pills (S1, if sold by early Dec 2024), Plasma pre-deposit (equal-split quirk, not YT), and possibly USD.AI (anecdotal).
- Clearly negative or likely negative:
  - Renzo: points realized at about 27% of the pre-TGE secondary price.
  - EigenLayer via Pendle: exclusion, delay and a small first tranche.
  - Ethena S2: -74% ENA during the season.
  - Ethena S5: ENA -84% from S4 claim to S5 end, and the pool cut from 3.5% to 2%.
  - Resolv S2/S3: exploit, and token -95%.
  - Level: shutdown with no token.
  - Elixir: collapse.
  - Falcon late-season 36–72x farms: FF -54% to -69% from day 1.
- Ethena S3 and S4 are ambiguous. Value depended on purchase date and ENA path, and S4 was diluted by a 2.8x USDe supply surge and a partly vested or contingent pool.
- The Ethena pool value per season fell from about $175M (S3, 3.5% × 15B × $0.333) to about $32M (S5, 300M × $0.107), a drop of about 82% (Claude's arithmetic from cited prices and allocations). Average USDe supply in S5 was higher than in S3, so value per sat fell even more.

### Gaps
- No Dune dashboard or published dataset was found that computes realized YT buyer PnL per market or season. The Dune "Pendle Effect" blog URL returned 404.
- No reliable $/sat for Ethena S2–S5 was found, because total sats per season were not published in retrieved sources. The S2 allocation percentage was not found.
- No per-point realized values were found for Falcon Miles, Resolv points, Level XP or Karak XP. Karak's KAR outcome was not found.
- Outcomes for Kelp (KERNEL), Swell YT, Cap (TGE status unknown), Ethereal, Terminal (no TGE found as of Sep 2026), Hyperliquid-ecosystem farms and the Avant TGE were not found.

---

## Q8. Patterns: how often YT buyers lost, why, implied-APY levels, points inflation, TGE slippage

### Takeaway
Systematic YT PnL data does not exist publicly. Across the case set, though, most post-2024 points farms (roughly 2 in 3 or more) appear to have lost money for YT buyers who entered at market-implied prices, and nearly all stablecoin-protocol farms after the Usual S1 era did. The dominant loss drivers, in order, were:
1. The token price or FDV at claim was far below what farmers had priced (-40% median at day 30; -70% median across 2025 launches).
2. Points dilution from TVL surges, extra seasons and larger pools over longer accrual.
3. Delayed, vested or contingent claims.
4. Protocol failure (exploit, depeg, shutdown), which zeroes the points.
5. Rule changes that disadvantage Pendle/YT holders.

### Cited Findings
- Stated failure mode: projects that delay issuance "infinitely dilute" point value. A YT bought at 8% implied APY on Aave USDT that realizes 4% loses about half its principal — [Tencent/Lianpr analysis, 2025-05-26](https://news.qq.com/rain/a/20250526A0465200)
- A YT bought at 0.10 implying 25% APY over 6 months loses money if realized yield is below 25%. Points are "not a guaranteed claim on future token" and multipliers change — [Eco support article, 2026](https://eco.com/support/en/articles/15253995-what-is-pendle-pt-and-yt-tokens-explained-2026); [airdrops.io, 2026-09-04](https://airdrops.io/blog/xstocks-yt-farm-strategy/)
- Many YTs showed "-100% Long Yield APY" when priced above expected income (Pendle UI, 2024) — [PANews](https://panews.io/articles/m0ngi707vao3)
- FDV / price at claim below expectations: Renzo realized $0.12 vs $0.45 per point pre-TGE — [Ouroboros](https://ouroborosresearch.substack.com/p/ouroboros-market-update-3-renzo-airdrop); [OnchainTimes](https://www.onchaintimes.com/5-insane-roi-pointsairdrop-strategies/). Median day-30 return for the 17-token farmed sample was about -41% (14/17 negative) and median day-90 about -58% (13/17 negative) (Claude's calculation from [DefiLlama](https://coins.llama.fi/chart/coingecko:ethena) daily closes).
- Points inflation and dilution:
  - Ethena S4's USDe supply was up 2.8x during the season — [DefiLlama](https://stablecoins.llama.fi/stablecoins)
  - Apyx extended accrual (pool 6%→9%) — [ChainCatcher](https://www.chaincatcher.com/en/article/2291854)
  - Late-season multiplier escalation: Falcon went from 36x to 72x Miles — [Falcon materials](https://docs.falcon.finance/falcon-miles). Apyx Pips are at 100–128x — [Pendle API](https://api-v2.pendle.finance/core/v2/markets/all?isActive=true)
  - Teams can "conjure insider positions" that dilute honest farmers — [DeFi Sentinel](https://defisentinel.org/research/introduction-to-point-farming-2026)
- Delays and slippage:
  - EIGEN was announced and claimed in Apr/May 2024 but untradeable until about 2024-10-01 (first price in the DefiLlama series is 2024-10-02) — [DefiLlama](https://coins.llama.fi/chart/coingecko:eigenlayer)
  - Ethena S4 rewards arrived more than a month after the season ended — [The Defiant](https://thedefiant.io/news/defi/ethena-season-4-rewards-go-live). The S5 claim came about 6 weeks after the season ended (Mar 25 → May 5, 2026) — [KuCoin](https://www.kucoin.com/blog/how-to-claim-ethena-season-5-airdrop)
  - Avant pushed its TGE to mid-September (about 4 months after points stopped). Apyx is postponed indefinitely from Oct 13, 2026. OpenSea slipped beyond Q1 2026 — sources in Q5
- Structural vesting at claim: Ethena S4 had only 1.5% of 3.5% instantly liquid — [AirdropAlert](https://airdropalert.com/airdrops/ethena-season-4/). Re gave large wallets 10% up front with the rest over 3 years — [Re](https://re.xyz/insights/re-tge-launch)
- Rule changes and exclusion: Pendle/DeFi users were excluded from EigenLayer's first season — [Bitget](https://www.bitget.com/news/detail/12560603983274). There was controversy over Ethena conditions for YT-sUSDe holders (search-summary only) — [Binance Square](https://www.binance.com/en/square/post/13159005718425)
- Protocol failure: Resolv exploit (Mar 2026), Elixir deUSD collapse (Nov 2025), USD0++ floor-price depeg (Jan 2025) and Level shutdown (Sep 2025) — sources in Q7
- Crowd exit when incentives end: Pendle TVL dropped 40% in one week at LRT expiries (Jun 2024) — [DL News](https://www.dlnews.com/articles/defi/pendle-hit-with-3bn-drawdown-as-restaking-airdrops-fade/). TVL was -74% from its Sep-2025 peak by Jan 2026 as carry turned negative — [DeFi Sentinel / search summary](https://defisentinel.org/research/introduction-to-point-farming-2026)

### Inferences
- **Win rate:** in the approximately 15 farms Claude could characterize, only about 4–5 were clearly profitable for YT buyers, and all of them were early or first-season, novel farms in bull tapes (H1 2024 and Q4 2024). Every 2025–2026 stablecoin-protocol farm with a known outcome (Resolv, Falcon, Level, Elixir, Ethena S5, Spark) appears negative for buyers at typical implied prices. USD.AI is the only possible exception, and the evidence is anecdotal.
- **Implied-APY level before losses:** directly comparable data is lacking. Qualitatively, losses followed periods of very high multipliers (36–128x) and implied APYs well above underlying (e.g., 5–10pp of points premium) late in a campaign, when TVL was surging, which is exactly when dilution is greatest.
- **Size of the dilution effect:** in Ethena's case, falling token price explains most of the per-season value collapse (ENA $0.607 at S4 end → $0.097 at S5 end, -84%). The allocation cut (3.5%→2%, -43%) compounds it, and so does TVL growth in S4 (2.8x). For small stablecoins, protocol-failure risk dominates (Level, Resolv and Elixir were effectively total losses on points).
- **Typical timeline slippage:** 1–2 months from season end to claim is routine (Ethena S4, S5). TGE postponements of 3–6+ months happened repeatedly in 2026 when markets were weak (Avant, Apyx, OpenSea, Zetarium). EigenLayer's transferability was delayed about 5 months.

### Gaps
- There is no base rate on the share of all Pendle YT buyers who lost money; the counts above are Claude's qualitative tally of a non-random case set.
- No data was found that links entry implied APY (or implied $/point) to ex-post outcomes per market.

---

## Q9. Rules of thumb used by experienced farmers (and evidence-based calibration)

### Takeaway
Published rules of thumb are sparse and qualitative:
- Value points off a conservative FDV, anchored to the last VC round or a pre-market.
- Assume that FDVs above $500M–$1B rarely hold.
- Require that yield plus points exceed YT cost with a margin.
- Expect dilution and delays.

The evidence supports a heavy haircut for a small, STRC-exposed stablecoin TGE in Q4 2026: roughly 40–60% below the "rumored" FDV, a 3–6 month delay with continued dilution, and a meaningful probability of zero.

### Cited Findings
- YT only makes sense if future yield plus points exceed the YT principal, because YT has no principal redemption — [Tencent/Lianpr](https://news.qq.com/rain/a/20250526A0465200)
- Heuristics from DeFi Sentinel (2026-06-27):
  - About 10% community allocation at TGE is standard; 20–30% is "very, very good".
  - The last VC round valuation is a rough floor for the opening FDV ("if VCs came in at a $300M valuation … the token won't open below $300M").
  - Source: [DeFi Sentinel](https://defisentinel.org/research/introduction-to-point-farming-2026)
- $/point method: (total points at airdrop ÷ (airdrop % × TGE FDV)), with explicit assumptions for points growth — [search summary referencing LianPR/Chinese analyses](https://www.lianpr.com/en/news/detail/304729). "Many early YT farmers break even only at 3x+ launch FDV" (search-summary only, unverified; primary source not identified).
- FDV is the key determinant of post-airdrop performance (Keyrock). Launches under $200M FDV had a 40% green rate vs 0% above about $1B (Memento) — [Keyrock](https://keyrock.com/airdrops-in-the-barren-desert/); [Memento](https://mementoresearch.com/state-of-2025-token-launches-year-in-review)
- 2026 innovation: some teams now offer downside protection (e.g., USD.AI's "Protected CHIP" FDV floors for ICO participants) — [USD.AI](https://usd.ai/insights/chip-is-live)
- Pendle UI treats points as $0 in PnL, so farmers must track airdrops manually — [Pendle docs](https://docs.pendle.finance/pendle-academy/ecosystem-and-resources/points-trading/points-support-page)

### Inferences
These are Claude's calibration suggestions for a bearish-leaning YT valuation, derived from the cited evidence above. They are not sourced rules.
- **FDV haircut:** apply a 40–60% haircut to the "rumored" or pre-market FDV to get the expected claim-date FDV. Evidence: median day-30 of -41% across the farmed-token sample; Renzo points realized at 27% of the pre-TGE price; 2025 stablecoin category average -70%. For a sub-$100M-supply stablecoin, base FDV scenarios should sit in the $50–250M range where Memento shows better survival, not $500M+.
- **Delay:** assume the TGE comes 3–6 months after the rumored date. While points keep accruing to everyone, including cheaper late YTs and higher multipliers, model a 30–100% increase in total points by TGE (Ethena S4's TVL rose 2.8x; Apyx's pool rose 1.5x with a longer accrual).
- **Liquidity at claim:** assume 30–60% of the allocation is immediately liquid (Ethena S4 was 43% instant; Re vests large wallets). Value the rest at a further discount.
- **Tail risk:** assign 20–35% probability to a zero or near-zero points outcome for a small yield-stablecoin protocol within a 12-month horizon. Precedents: Level shutdown, Resolv exploit, Elixir collapse, USD0++ depeg. The STRC-specific risk adds to this: its June-2026 drawdown to $71 led Apyx to postpone its TGE.
- **Market beta:** the Q4-2026 backdrop (Fed hiking, 10Y above 5%, BTC -22% YoY despite the rebound) argues against assuming TGE multiples above current comparables. CHIP at about $416M FDV (on a ~$0.2B-supply stablecoin) and FF at about $1.3B FDV (on $1.2B USDf) are the most relevant 2025–26 comparables. Claude computed FF's FDV as $0.13 × 10B supply; the 10B FF supply figure is not cited in these notes.

### Gaps
- No primary-sourced, widely cited farmer rulebook (e.g., "use a 30–50% FDV discount") was found. The numeric heuristics above are Claude's inferences from the case evidence.
- FF total supply (10B) and CHIP supply-to-TVL ratios were not verified in this session. Confirm before using them as valuation multiples.
