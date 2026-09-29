# Market Environment and Solana/Reinsurance Comps for an OnRe (ONyc) TGE — as of 2026-09-29

Method note: Hard numbers below were pulled live on 2026-09-29 from public APIs (CoinGecko `/global`, `/simple/price`, `/market_chart`; DefiLlama `api.llama.fi` chain/protocol/fees endpoints; `stablecoins.llama.fi`; `coins.llama.fi` price charts; CoinPaprika tickers for supply/ATH). CoinGecko rate-limited and then blocked after several calls, so some token supply/ATH data comes from CoinPaprika and some prices from DefiLlama's coin-price API (they differ by 1–3% intraday). Where I use DefiLlama "first price" as a proxy for listing price, it is the first daily/2-day data point after listing, not an official listing price, so treat it as ±20% on launch day, when tokens are very volatile.

## 1. Macro/crypto market state (Jul–Sep 2026): bull, range or bear?

### Takeaway
Crypto is in an **early recovery after a deep H1-2026 bear market**, not a confirmed bull. BTC/ETH/SOL are +40–70% off their June 2026 lows after three straight monthly gains, but they are still 33–49% below their Oct-2025 highs. DeFi TVL (-45% from its Oct-2025 peak) and Solana TVL (-51% from its Sep-2025 peak) are well below 2025 levels, and total stablecoin supply has been flat since May (~$306–320B). A bearish-leaning base case should treat this as a relief rally that is vulnerable to reversal, with Fed rate-hike risk in focus.

### Cited Findings
- **Spot prices on 2026-09-29:** BTC $83,727, ETH $2,688, SOL $118.91. Total crypto market cap is $2.87T — [CoinGecko API /simple/price & /global](https://api.coingecko.com/api/v3/global)
- **BTC path (daily closes):** 2025-09-30 $114,327 → 2025-11-29 $90,905 → 2026-02-27 $67,497 → 2026-03-29 $66,389 → 2026-06-27 $60,022 → 2026-07-27 $65,344 → 2026-08-26 $78,511 → 2026-09-29 $83,727. The 365-day high was $124,740 and the 365-day/180-day low was $58,566 (June 2026). BTC is +39% over 3 months (from Jun 27), +26% over 6 months (from Mar 29) and ~-33% from the 365-day high — [CoinGecko market_chart API](https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=365&interval=daily)
- **ETH path:** 2025-09-30 $4,215 → 2026-03-29 $2,000 → 2026-06-27 $1,577 (365-day low $1,566) → 2026-09-29 $2,689. ETH is +70% over 3 months, +34% over 6 months and ~-43% from the 365-day high of $4,691 — [CoinGecko market_chart API](https://api.coingecko.com/api/v3/coins/ethereum/market_chart?vs_currency=usd&days=365&interval=daily)
- **SOL path:** 2025-09-30 $212.9 → 2025-12-29 $125.2 → 2026-03-29 $82.1 → 2026-06-27 $71.8 (365-day low $62.18) → 2026-09-25 $117.0 → 2026-09-29 $118.9. SOL is +66% over 3 months, +45% over 6 months and ~-49% from the 365-day high of $234.8 — [CoinGecko market_chart API](https://api.coingecko.com/api/v3/coins/solana/market_chart?vs_currency=usd&days=365&interval=daily)
- **Total DeFi TVL (all chains):** the 400-day peak was $171.1B on 2025-10-07 → 2025-11-24 $112.2B → 2026-02-22 $91.5B → 2026-05-23 $79.6B → trough $68.2B on 2026-07-01 → 2026-08-21 $83.2B → 2026-09-29 $94.4B. That is -45% from the peak and +38% from the trough (includes the price effect) — [DefiLlama historicalChainTvl](https://api.llama.fi/v2/historicalChainTvl)
- **Solana DeFi TVL:** the 400-day peak was $13.24B on 2025-09-14 → 2025-10-25 $11.49B → 2026-02-22 $6.55B → trough $4.45B on 2026-06-11 → 2026-09-29 $6.44B. That is -51% from the peak and +45% from the trough. Solana is still #2 chain by TVL ($6.44B vs Base $6.23B, BSC $5.70B) — [DefiLlama chain TVL](https://api.llama.fi/v2/historicalChainTvl/Solana); [DefiLlama chains](https://api.llama.fi/v2/chains)
- **Total stablecoin supply:** 2025-09-25 $293.9B → 2026-03-24 $313.2B → 2026-05-23 $320.3B (peak area) → 2026-07-22 $306.4B → 2026-09-29 $311.3B. It has been flat to slightly down since May 2026. USDT is $183.8B and USDC $74.8B (2026-09-29) — [DefiLlama stablecoins](https://stablecoins.llama.fi/stablecoincharts/all)
- CEX.IO data (via CMC) shows total stablecoin supply dipped from $315B (Q1) to $312B (Q2 2026) — [CoinMarketCap Academy, 2026-07-02](https://coinmarketcap.com/academy/article/yield-bearing-stablecoin-supply-falls-q2-2026-treasury-backed-growth)
- BTC is up ~10% in September 2026 and on track for 3 straight monthly gains (July up, August sharp rebound, September green). It briefly printed 8-month highs above $87K. Near-$1B ETF inflow days are underwriting the rally — [Crowdfund Insider, Sep 2026](https://www.crowdfundinsider.com/2026/09/312293-bitcoins-september-2026-rally-puts-3-month-positive-btc-price-streak-within-reach-analysis/)
- Fed rate-hike bets and rising Treasury yields are the main headwind flagged for September 2026. Analysts see a break below ~$77.2K as invalidating the recovery — [Analytics Insight](https://www.analyticsinsight.net/cryptocurrency-analytics-insight/crypto-market-september-2026-why-fed-rate-hike-bets-are-back-in-focus); [CoinDesk 2026-09-01](https://www.coindesk.com/markets/2026/09/01/bitcoin-enters-rektember-as-rate-hike-risks-threaten-its-august-rally)
- A secondary source states total crypto market cap fell 20.4% in Q1 2026 and CEX spot volume fell 39.1% (low-quality Medium source; not independently verified) — [Medium/Coinmonks](https://medium.com/coinmonks/why-2026-token-launches-are-being-built-for-surviving-after-tge-70ff9361fdbf)
- DeFi TVL "slid every month in 2026" from ~$115B in January to ~$70B, consistent with the DefiLlama data above — [Yahoo Finance](https://finance.yahoo.com/markets/crypto/articles/defi-total-value-locked-slides-072657247.html)
- Two major 2026 DeFi exploits hit sentiment. Drift (Solana perps) lost ~$285M on 2026-04-01 (suspected DPRK), and its TVL fell from ~$550M to <$250M — [CoinDesk](https://www.coindesk.com/business/2026/04/02/north-koreans-hackers-likely-behind-the-usd286-million-drift-protocol-exploit-elliptic); [TRM Labs](https://www.trmlabs.com/resources/blog/north-korean-hackers-attack-drift-protocol-in-285-million-heist). Resolv's USR yield-dollar was exploited in March 2026: 80M unbacked USR were minted and ~$23–25M extracted, and USR crashed ~70%+ — [The Block](https://www.theblock.co/post/394582/resolvs-usr-stablecoin-depegs-after-attacker-mints-80-million-unbacked-tokens-extracts-roughly-25-million); [CoinDesk 2026-03-23](https://www.coindesk.com/markets/2026/03/23/resolv-stablecoin-drops-70-after-usd80-million-exploit-after-attacker-mints-usr)

### Inferences
- **Phase call:** this is an "early recovery / range" regime. Prices have momentum (Jul–Sep) but sit far below 2025 highs. On-chain capital (TVL, stablecoins) has recovered much less than prices, which suggests the rebound is price-driven more than new-money-driven.
- **Bearish-leaning assumption for a Q4-2026 TGE:** assume BTC could revisit the $70–77K range, with alts/SOL-beta tokens falling 25–40% in that case. Solana DeFi tokens in particular rebounded 50–300% off June lows (see Section 3), so they have room to give back.
- The Drift hack hurts Solana DeFi's security reputation, and the Resolv hack hurts the "yield dollar" category directly. Diligence on custody, mint controls and multisigs will be a larger part of how the market prices an RWA/yield token like ONyc.

### Gaps
- There is no historical total crypto market cap series: the CoinGecko `/global/market_cap_chart` endpoint is paid, so only the spot figure ($2.87T) is reported.
- No Kaiko/Glassnode/Coinbase Institutional September 2026 outlook was retrieved, so a standardized "cycle phase" label from a primary research house is missing.

## 2. Airdrop/TGE climate in 2025–2026 and whether the stablecoin/yield-dollar narrative is cooling

### Takeaway
The TGE climate is poor. 85% of 2025 TGEs trade below launch (median >70% drawdown), and public token sales hit a 5-year low in Q2 2026 ($58M, 37 sales). Binance Alpha/HODLer distribution is still the default listing path but no longer protects price. The yield-dollar narrative has **clearly cooled**:
- USDe supply is -67% from its Oct-2025 peak.
- Yield-bearing stablecoin supply shrank 15% in Q2 2026, the first contraction since Q3 2023.
- Every 2025-cohort yield-dollar governance token (ENA, USUAL, FF, RESOLV, EDEN, HUMA, SLX) is down 58–98% from ATH.
- Capital is rotating toward Treasury/RWA-backed yield, which is a relative positive for a real-world, non-crypto-correlated yield source like reinsurance.

### Cited Findings
**TGE performance statistics**
- Memento Research tracked 118 TGEs in 2025: ~85% were trading below their TGE valuation, and the median token was down >70%. Tokens that debuted on major CEXs "including Binance, often sold off almost immediately." Examples: Plasma (XPL) went from $2.00 to <$0.20, and Monad was down ~40% since its November launch — [CoinDesk, 2026-01-06](https://www.coindesk.com/business/2026/01/06/why-crypto-s-new-token-issues-are-falling-flat-and-what-comes-next)
- DWF Labs: >80% of 2025 launches are below listing price, with typical 50–70% drawdowns within 90 days — [CoinMarketCap Academy](https://coinmarketcap.com/academy/article/over-80percent-of-2025-token-launches-are-trading-below-listing-price-reports-dwf-labs)
- CryptoRank: public token sales (ICO/IEO/IDO) raised just $58M across 37 sales in Q2 2026. That is -85% QoQ (Q1 2026: ~$390M across 105 sales) and the weakest quarter in five years. May 2026 had only 13 sales, the lowest since late 2020 — [CryptoRank insight](https://cryptorank.io/insights/analytics/q2-2026-the-worst-ico-quarter); [BeInCrypto](https://beincrypto.com/crypto-ico-ido-sales-q2-low/)
- Binance Alpha remains the dominant listing/airdrop funnel. In 2025 it ran 100+ airdrop events and 221 tokens launched via airdrops/TGEs/Boosters. It is still active in Sep 2026: Canopy (CNPY) was listed 2026-09-07 with an Alpha-points airdrop — [CMC Academy](https://coinmarketcap.com/academy/article/binance-alpha-2025-crypto-airdrops-token-launches); [NFT Plazas](https://nftplazas.com/binance-alpha-lists-canopy-token-cnpy-airdrop/)
- Binance HODLer Airdrops in 2026 include Brevis (2026-01-06) and Gensyn (2026-05-14). The HODLer-airdrop category holds 47 coins with a combined ~$2.4B market cap — [Cryptowire](https://www.cryptowire.in/crypto/binance-new-listings/); [CoinGecko category](https://www.coingecko.com/en/categories/binance-hodler-airdrops)
- MetaDAO "ownership coin" launches on Solana are the counter-trend. They have raised $624.7M across 23 sales, use low starting FDVs and have performance-gated team unlocks (tranches at 2x–32x ICO price). The reported average ATH ROI for 2025 launches is 8.6x (promotional source) — [KuCoin news](https://www.kucoin.com/news/flash/metadao-raises-625m-in-23-sales-faces-challenge-of-filtering-quality-projects); [Alea Research](https://alearesearch.substack.com/p/metadao)

**Yield-dollar supply trends** (DefiLlama stablecoins, 2026-09-29)

| Asset | Peak supply (date) | Supply 2026-09-29 | Change / note |
|---|---|---|---|
| Ethena USDe | $14.82B (2025-10-04) | $4.90B (low $3.93B, 2026-08-11) | -67% from peak; ~+20% MoM from $4.07B |
| Falcon USDf | $2.15B (2025-10-15) | $1.21B | -44% |
| Usual USD0 | $1.86B (Jan 2025) | $0.55B | — |
| Resolv USR | $0.59B (Jan 2025) | ~$0.01B | Effectively dead after March-2026 exploit |
| USD.AI USDai | $0.66B (2026-01-20) | $0.23B | -65% |
| Solstice USX (Solana) | $0.52B (2026-07-31) | $0.22B | -58% in ~2 months (prev month $0.25B) |
| Re Protocol reUSD | — | ~$0.25–0.28B | Counter-trend grower: ~$0.11B Jan 2026; prev month $0.22B |

Sources: [DefiLlama stablecoin 146](https://stablecoins.llama.fi/stablecoin/146), [DefiLlama stablecoins list](https://stablecoins.llama.fi/stablecoins)

**Other evidence of cooling**
- Yield-bearing stablecoin supply fell >$3.5B (-15%) in Q2 2026, the first quarterly contraction since Q3 2023. sUSDe lost 52% of supply (~$2B) and Sky's sUSDS fell 16%. Treasury-backed products grew: Ondo USDY +66%, Circle USYC +16%, BlackRock BUIDL +2% — [CMC Academy citing CEX.IO, 2026-07-02](https://coinmarketcap.com/academy/article/yield-bearing-stablecoin-supply-falls-q2-2026-treasury-backed-growth); [Cointelegraph via TradingView](https://www.tradingview.com/news/cointelegraph:e004e2781094b:0-yield-bearing-stablecoin-slowdown-ends-3-year-run-for-crypto-native-products/)
- sUSDe 7-day trailing APY was 7.1% in June 2026, down from 9.4% in April, as perp funding compressed (secondary source) — [RWATimes](https://rwatimes.substack.com/p/yield-bearing-stablecoins-lose-35b)

**Yield-dollar governance token drawdowns** (prices from DefiLlama coins API as of 2026-09-28/29; ATH from CoinPaprika; supply from CoinPaprika)

| Token | Price now | Drawdown from ATH / listing | FDV / mcap | Recent move |
|---|---|---|---|---|
| ENA | $0.253–0.257 | -83% from ATH $1.52 (Apr 2024) | FDV ~$3.8B, mcap $2.55B | +256% over 90 days (bounce from ~$0.07 in late June 2026) |
| USUAL | $0.0142 | -98% from ATH $0.71 (2025-01-10) | mcap ~$27.6M (CoinGecko) | — |
| FF (Falcon) | $0.117–0.123 | -85% from day-1 ATH $0.797 (TGE 2025-09-29); -57% vs first DefiLlama print $0.284 | FDV ~$1.2B, mcap $274–368M | — |
| RESOLV | $0.0187 | -95% from $0.34–0.41 (TGE 2025-06-11) | FDV ~$19M | — |
| EDEN (OpenEden) | $0.060 | -96% from ATH $1.53 (2025-09-30); -84% vs $0.385 print (2025-10-02) | FDV ~$60M | — |
| HUMA | $0.0283 | -77% from ATH $0.122; -58% vs first print $0.067 (TGE 2025-05-26) | FDV ~$283M, mcap $49M | — |
| SLX (Solstice) | $0.064 | -90% from ATH ~$0.65 (2026-06-29) | FDV ~$64M, mcap $15.5M | — |

Sources: [DefiLlama coins API](https://coins.llama.fi/chart/coingecko:ethena?start=1735689600&span=330&period=2d); [CoinPaprika tickers](https://api.coinpaprika.com/v1/tickers/ena-ethena)

### Inferences
- **Base-rate for OnRe's post-TGE path:** across the nine yield/DeFi-adjacent TGEs listed in Section 3 (2025–2026), the median change from first-print price to today is about **-57%**. Only 2 of 9 are above first print, and both are June-2026 launches (RE +7%, CAP +93%) that benefited from the Jul–Sep relief rally. A bearish-leaning model should assume a 40–60% decline from listing within 90 days unless float is very low and there are no airdrop-cliff sellers.
- The narrative has bifurcated. "Crypto-native basis-trade yield dollars" (USDe, USDf, USR, USX) are shrinking. "Real-world-cash-flow yield" (T-bills, reinsurance: reUSD +2.5x YTD, ONyc TVL +3.8x YTD) is growing. OnRe should be positioned in the second bucket. Token-market multiples for the whole "stablecoin/yield" sector are still depressed, so the narrative premium is small.
- Low public-sale volume in Q2 2026 means retail liquidity for new tokens is thin. Binance Alpha listing is achievable but, per Memento, is not price-supportive.

### Gaps
- There is no 2026-specific aggregate TGE-performance study (e.g., Memento 2026 H1) with average % down from listing. The 2025 figures and my own sample are the best available.
- The cause of Solstice USX's ~58% supply drop in Aug–Sep 2026 was not found. A CMC-AI page mentions a 75M SLX (7.5%) Foundation release in September 2026, but that is not a primary source — [CMC AI Solstice updates](https://coinmarketcap.com/cmc-ai/solstice/latest-updates/)
- There are no reliable current sUSDe APY figures for Jul–Sep 2026.

## 3. Solana DeFi/RWA TGE comps (2025–2026): launch FDV vs TVL

### Takeaway
Recent Solana yield/RWA TGEs launched at roughly **$230–670M FDV**. Most now trade at **0.3–1.0x FDV/TVL**: Solstice 0.30x, Kamino ~0.30x, Huma ~0.74x, Meteora ~1.0x. The closest comps are Solstice (Solana yield-dollar, Binance Alpha, May 2026), which lost ~70% from its first print and ~90% from ATH, and Huma (Solana PayFi/RWA, May 2025), which is -58% from its first print. Across the broader DeFi comp set, the median FDV/TVL is about 1.0x and the lower quartile about 0.3x. Exponent, Loopscale and Perena have no confirmed token yet.

### Cited Findings
**Comp table** (TVL from [DefiLlama protocols API](https://api.llama.fi/protocols), 2026-09-29; prices from [DefiLlama coins API](https://coins.llama.fi/prices/current/coingecko:re,coingecko:solstice,coingecko:huma-finance); supply from [CoinPaprika](https://api.coinpaprika.com/v1/tickers/slx-solstice)). "Launch FDV" is approximated from the first DefiLlama price print × total supply unless a press figure is cited. **Bold** marks the direct comps.

| Token | Chain / sector | TGE | Launch FDV (approx.) | FDV now | TVL now | FDV/TVL | Price vs first print |
|---|---|---|---|---|---|---|---|
| **SLX (Solstice)** | Solana yield-dollar | 2026-05-25 | $207M–350M | ~$64M | $215M (peak $523M, 2026-07-17) | **0.30x** | **-68%** |
| **HUMA** | Solana PayFi/RWA | 2025-05-26 | ~$670M | ~$283M | $381.5M | **0.74x** | **-58%** |
| **RE (Re Protocol)** | ETH reinsurance | 2026-06-18 | ~$430–480M | ~$462M | $390M (DefiLlama; $560M self-reported June) | **1.18x** (~0.83x on self-reported) | **+7%** |
| KMNO (Kamino) | Solana lending | 2024 | n/a | ~$430M | ~$1.47B (Lend $1.39B + Liquidity $75M; peak $3.37B, Oct-2025) | ~0.30x | — |
| MET (Meteora) | Solana DEX | 2025-10-23 | ~$552M | ~$320–330M | ~$320M (all modules) | ~1.0x | -40% |
| CLOUD (Sanctum) | Solana LST | 2024 | n/a | ~$70M (assumes 1B supply, unverified) | $2.2B (LST TVL) | ~0.03x | — |
| CAP | ETH credit / stablecoin | ~2026-06-27 | ~$294M | ~$555M | $289M | ~1.9x | +93% |
| CHIP (USD.AI) | ETH GPU-backed yield dollar | 2026-04-21/22 | ~$608M | ~$436M | USDai $0.23B | ~1.9x | -28% |
| FF (Falcon) | ETH synthetic dollar | 2025-09-29 | ~$2.8B (first print; ATH $7.97B) | ~$1.2B | $1.21B | ~1.0x | -57% |
| ENA (Ethena) | ETH synthetic dollar | 2024 | n/a | ~$3.8B | USDe $4.9B + USDtb $0.49B | ~0.7x | — |

- **Solstice (SLX) detail:**
  - Launched 2026-05-25 on Binance Alpha, Gate, Bitget, OKX, MEXC and BitMart, at an initial FDV "just under $230M" (other reports ~$350M at $0.355). It lost >40% within hours as airdrop claimers sold. Farmers were angered by surprise vesting of the "Flares" airdrop — [MEXC news](https://www.mexc.com/news/1112452); [SolanaFloor](https://solanafloor.com/news/solstice-slx-launch-sparks-backlash-from-airdrop-farmers-over-surprise-vesting)
  - DefiLlama price path: first print $0.207 (2026-05-25), ATH ~$0.576–0.654 (2026-06-28/29), then $0.064–0.066 (2026-09-28) — [DefiLlama coins API](https://coins.llama.fi/chart/coingecko:solstice?start=1735689600&span=330&period=2d); [CoinPaprika](https://api.coinpaprika.com/v1/tickers/slx-solstice)
  - TVL: $171.8M (2025-10-01) → $523.0M peak (2026-07-17) → $215.1M (2026-09-29) — [DefiLlama protocol/solstice](https://api.llama.fi/protocol/solstice)
- **Huma (HUMA) detail:** TGE 2025-05-26 via Binance Alpha/Launchpool. Supply is 10B, and 5% went to the Season-1 airdrop — [CryptoRank news](https://cryptorank.io/news/feed/af757-huma-token-to-debut-on-binance-alpha-with-airdrop-on-may-26); [Huma blog](https://blog.huma.finance/huma-airdrop-payfi-decentralized). Huma TVL grew $167.6M (2026-05-27) → $381.5M (2026-09-29) while the token stayed ~58% below its first print, showing that TVL growth did not rescue the token — [DefiLlama protocol/huma](https://api.llama.fi/protocol/huma)
- **Drift (DRIFT):** $0.019–0.020, -98.6% since Jan 2025 after the 2026-04-01 $285M exploit. FDV is ~$20M, and the Drift Trade TVL module is ~$0.6M; Drift Staked SOL still holds $333M — [DefiLlama](https://api.llama.fi/protocols); [Halborn](https://www.halborn.com/blog/post/explained-the-drift-hack-april-2026)
- **Jupiter (JUP):** $0.326, CoinGecko market cap $1.08B. Jupiter Lend TVL is $1.16B and Jupiter Perps $805M. 30-day revenue annualizes to ~$84M, so mcap/revenue is ~13x — [CoinGecko API](https://api.coingecko.com/api/v3/simple/price?ids=jupiter-exchange-solana&vs_currencies=usd&include_market_cap=true); [DefiLlama fees](https://api.llama.fi/summary/fees/jupiter?dataType=dailyRevenue)
- **Exponent (OnRe's YT/PT venue):** no token found on CoinGecko search. DefiLlama TVL: Yield Exchange $67.4M (2026-09-29; peak $132.8M in Jul 2025; $115.6M on 2026-07-28), Risk Tranching $14.0M, Strategy Vaults $12.1M. Exponent's risk-tranching launched with OnRe's ONyc reinsurance yield — [DefiLlama protocol/exponent-yield-exchange](https://api.llama.fi/protocol/exponent-yield-exchange); [Solana ecosystem roundup](https://solana.com/news/solana-ecosystem-roundup-may-2026)
- **Loopscale:** TVL $91.5M (peak $107.8M, 2026-01-29); no token found — [DefiLlama protocol/loopscale](https://api.llama.fi/protocol/loopscale). **RateX:** TVL $4.0M; DefiLlama lists symbol "RTX" (token status unverified). **Perena:** Vaults $13.3M, DEX $0.6M; no token found — [DefiLlama protocols](https://api.llama.fi/protocols)
- **Solana DeFi token bounce off the June 2026 lows** (90-day price change to 2026-09-29): KMNO +133%, CLOUD +315%, MET +104%, JUP +55%, HUMA +26%, DRIFT +22%, JTO -21%, SLX -89% — [DefiLlama coins API](https://coins.llama.fi/chart/coingecko:kamino?start=1735689600&span=330&period=2d)
- **OnRe itself (for scaling):**
  - DefiLlama TVL rose from $16.2M (2025-07-14) to $77.2M (2026-01-12), $136.7M (2026-03-17), $224.7M (2026-07-15), $295.7M (2026-09-13) and $294.8M (2026-09-29) — [DefiLlama protocol/onre](https://api.llama.fi/protocol/onre)
  - OnRe docs (via search snippet) report $281.75M total asset value and ~9,300 holders as of 2026-09-26 — [OnRe docs](https://docs.onre.finance/introduction/onre-tokenized-reinsurance-onyc)
  - ONyc NAV went from $1.008 (2025-07-06) to $1.148 (2026-09-28). The 90-day change is +2.8% and the 180-day change +5.5%, which is ~11–12% annualized — [DefiLlama coins API](https://coins.llama.fi/chart/coingecko:onyc?start=1735689600&span=330&period=2d)
  - DefiLlama 30-day fees are $2.66M (~$32.4M annualized). Tracked "revenue" is only ~$0.9M annualized, which is likely methodology-dependent — [DefiLlama fees/onre](https://api.llama.fi/summary/fees/onre?dataType=dailyFees)

### Inferences
- **Mechanical OnRe FDV ranges at TVL ≈ $295M:**
  - 0.3x (Solstice/Kamino, bear case) → ~$90M
  - 0.74x (Huma) → ~$220M
  - 1.0x (sector median) → ~$295M
  - 1.18x (RE, the closest sector comp) → ~$350M
  - A bearish-leaning launch FDV range of roughly **$120–250M** is consistent with the comps. RE's launch FDV of ~$430–480M was set on a larger reported book ($500–560M self-reported) and Binance spot listing, and should be treated as the upper bound rather than the base.
- Solstice is the cautionary analogue: same chain, yield-dollar, Binance Alpha, airdrop with surprise vesting. It launched at ~$230M FDV and now sits at ~$64M with TVL down 59% from peak. It shows that TVL is mercenary once points end, which is a risk for ONyc TVL post-TGE if much of it is points-farming capital (e.g., via Exponent YT).
- Huma shows that even strong post-TGE TVL growth (+128% in 4 months) does not re-rate a token trading below its launch FDV when unlock supply keeps coming.

### Gaps
- Exact official listing prices/FDVs for HUMA, MET, CAP and CHIP were not verified from primary sources; the first DefiLlama price print was used.
- There is no verified token/TGE data for Exponent, Loopscale, Perena or RateX (RTX status unclear). The Kamino, Sanctum and Jupiter TGE-date FDVs (2024) were not retrieved.
- Circulating supply for RE after June 2026 (post-launch unlocks) was not verified. The ~$74M mcap figure assumes 159.6M circulating.

## 4. On-chain reinsurance / insurance-linked yield competitors

### Takeaway
**Re Protocol is the only direct, liquid, token-bearing comp.** Its $RE token was launched on 2026-06-18 with Binance, OKX, Bybit, Robinhood and KuCoin listings. It opened at ~$0.43–0.48 (FDV ~$430–480M), spiked to ~$1.04–1.08 (FDV ~$1.05B) within 2 days, and trades at $0.462 (FDV ~$462M), which is ~1.2x DefiLlama TVL and ~24x annualized fees. Legacy on-chain insurance (Nexus Mutual, Ensuro, Nayms, Neptune) is small ($0–114M TVL) and has low token valuations. It is not a growth comp, but it anchors the "insurance token" multiple near 1x TVL.

### Cited Findings
**Re Protocol (re.xyz)**
- RE TGE was 2026-06-18. Supply is 1B fixed (ERC-20). Allocation: Ecosystem 50%, Core contributors 20% (12-month cliff, 36-month vest), Investors 17% (12-month cliff, 36-month vest), Ecosystem Development Reserve 13%. Initial circulating supply was ~159.6M (16%). Listed on Binance, Robinhood, OKX, Bybit, KuCoin and others. Season-1 points holders ≤150M points claimed all tokens at TGE; larger holders got 150M points' worth plus 10%, with the rest vesting in 6 tranches over 3 years — [Re: RE TGE launch](https://re.xyz/insights/re-tge-launch)
- June 2026 update (Re-reported):
  - TVL $560M, underwriting portfolio $510.5M, on-chain capital $70.97M, off-chain reserves $177.67M, contracted premium receivable $318.93M.
  - 48 programs across 49 US states, 700K+ policyholders.
  - 10,000+ RE holders within 48 hours and 27 trading venues (16 spot, 11 perp).
  - reUSDe redemption window: requests 2026-07-09 to 07-22.
  - Source: [Re June performance update](https://re.xyz/insights/june-performance-update)
- Cover Re SPC has written ~$500M in premiums since inception ($310M in 2026) across 40+ insurance partners — [GlobeNewswire 2026-05-26](https://www.globenewswire.com/news-release/2026/05/26/3300870/0/en/Resilience-Foundation-to-Launch-The-RE-Governance-Token.html); [Re TGE post](https://re.xyz/insights/re-tge-launch)
- RE price path (DefiLlama 4-hour data): $0.476 (2026-06-18 19:00 UTC) → $0.431 → $0.80 (06-19) → $1.04 (06-20 20:00) → $0.72 (06-24) → $0.462 (2026-09-28). That is -54% from the peak, -24% over 90 days and +7% vs the first print. CoinGecko shows an ATH of $1.08 on 2026-06-20 and an FDV of $463.8M — [DefiLlama coins API](https://coins.llama.fi/chart/coingecko:re?start=1781740800&span=40&period=4h); [CoinGecko RE](https://www.coingecko.com/en/coins/re)
- Re TVL on DefiLlama (on-chain tracked): $85.8M (2025-12-01) → $165.8M (2026-03-31) → $282.1M (2026-05-30) → $257.6M (2026-07-29, post-redemption window) → $390.3M (2026-09-29, ATH). reUSD supply is ~$0.25–0.28B (prev month $0.22B) — [DefiLlama protocol/re](https://api.llama.fi/protocol/re); [DefiLlama stablecoins](https://stablecoins.llama.fi/stablecoins)
- Re fees are $1.59M over 30 days (~$19.3M annualized). FDV/annualized fees is therefore ~24x — [DefiLlama fees/re](https://api.llama.fi/summary/fees/re?dataType=dailyFees)

**Legacy on-chain insurance**
- **Nexus Mutual (NXM):** TVL/capital pool $113.8M (2026-09-29), down from $205.3M on 2025-10-01 (ATH $780.6M in Nov 2021). DefiLlama mcap is $112.8M, so mcap/TVL is ~1.0x. NXM is $67.95, -39% from its Aug-2025 high. Annualized 30-day fees are ~$1.1M — [DefiLlama protocol/nexus-mutual](https://api.llama.fi/protocol/nexus-mutual); [DefiLlama coins API](https://coins.llama.fi/chart/coingecko:nxm?start=1735689600&span=330&period=2d)
- **Ensuro:** TVL $2.3M. **Nayms:** TVL ~$0 (mcap ~$14K). **Neptune Mutual:** TVL ~$0. **Unslashed** $4.0M, **Ease** $5.2M, **InsurAce** $0.1M — [DefiLlama protocols](https://api.llama.fi/protocols)

### Inferences
- The RE listing is the single best pricing anchor for OnRe. Same thesis (stablecoin capital → quota-share/short-tail reinsurance), similar on-chain TVL (Re $390M vs OnRe $295M), and it launched only ~3 months before OnRe's likely window. Scaling RE's current FDV/TVL (1.18x) to OnRe gives ~$350M. Scaling RE's launch FDV/on-chain TVL (~$450M / $282M ≈ 1.6x) gives ~$470M. Both are optimistic because RE had tier-1 CEX spot listings from day 1 and a larger reported premium book, and because RE itself is -24% over the last 90 days despite a market rally. A bearish-leaning haircut of 30–50% to the RE-implied value gives **~$175–245M**.
- RE's pattern (flat open → 2.4x pump in 48 hours → -55% over 3 months) matches the generic 2025–26 TGE decay curve. OnRe should model a similar post-listing retrace.
- Legacy insurance tokens (NXM ~1x TVL, tiny fees) show that the market does not pay a large premium for "insurance" per se; growth and yield scale are what re-rate.

### Gaps
- No token/valuation data was found for Arbol, Relm or tokenized cat-bond platforms, which were not searched in depth.
- Re's private-round valuation was not found. No official RE listing price was found; the ~$0.43–0.48 open is inferred from DefiLlama 4-hour data.

## 5. Seasonality and event timing (Breakpoint, Q4 TGE activity, hurricane season)

### Takeaway
- **Breakpoint 2026** is **Nov 15–17, 2026 at Olympia London**, the natural Solana catalyst.
- The **2026 Atlantic hurricane season has been historically benign**: 8 named storms and 0 hurricanes through late September, the first season since 1914 without a hurricane this late, under a very strong El Niño. With the season ending Nov 30, a TGE in late Nov/early Dec would come after peak-season cat risk has passed. The benign year strengthens OnRe's "uncorrelated yield, no losses" story but may soften 1/1/2027 reinsurance pricing (inference).

### Cited Findings
- Solana Breakpoint 2026 runs Nov 15–17, 2026 at Olympia London. It is the first UK edition, with 8,000+ expected attendees — [Solana Compass](https://solanacompass.com/news/solana-breakpoint-2026-comes-to-london-for-the-first-time-november-15-17-at-olympia); [solana.com/breakpoint](https://solana.com/breakpoint)
- 2026 Atlantic hurricane season:
  - 8 named storms, 0 hurricanes, 0 major hurricanes, ACE ~9.9 at the latest update.
  - On 2026-09-21 it became "the first since 1914 to not have a hurricane so late into the season," due to a very strong El Niño.
  - US tropical-storm damage is ~$1.02B+ in total (TS Arthur, Jun 17–18: >$1B; Bertha and Edouard: tens of millions each).
  - Tropical Storms Fay and Hanna are active on Sep 28–29.
  - Forecasts: NOAA (May 21) called for 8–14 named storms and 3–6 hurricanes; CSU (Jul 8) called for 9 named storms, 4 hurricanes and 1 major.
  - Source: [Wikipedia: 2026 Atlantic hurricane season](https://en.wikipedia.org/wiki/2026_Atlantic_hurricane_season)
- NOAA maintained a below-normal Atlantic outlook in its 2026 update — [NOAA](https://www.noaa.gov/news-release/noaa-maintains-prediction-for-below-normal-atlantic-hurricane-season). Swiss Re Institute describes H1-2026 insured cat losses as "below trend" — [Swiss Re Institute](https://www.swissre.com/institute/research/topics-and-risk-dialogues/climate-and-natural-catastrophe-risk/first-half-2026-insured-catastrophe-losses.html)
- The Atlantic season officially ends Nov 30 — [NOAA](https://www.noaa.gov/news-release/noaa-maintains-prediction-for-below-normal-atlantic-hurricane-season)
- Q4 TGE pipeline: large unlocks are due, e.g. SUI's Oct 1 unlock (~$61M) and a Monad unlock in November 2026 — [Tokenomist/CryptoRank via search](https://tokenomist.ai/); [BSC News](https://x.com/BSCNews/article/2099457787445313684)

### Inferences
- **Timing logic (bearish-leaning):**
  - Launching **before** Nov 30 exposes the token to headline cat risk. A late-season Gulf/Florida landfall could hit ONyc NAV sentiment right at listing, even though October climatology is lower in an El Niño year.
  - Launching **around or just after Breakpoint (mid/late Nov) to early Dec** lets OnRe cite a "full hurricane season, zero hurricanes" track record plus Breakpoint visibility.
  - Launching in **late Q4** runs into holiday liquidity and the usual December de-risking.
  - The Jan 1 reinsurance renewal is a natural follow-on catalyst (renewal yields).
- A benign cat year typically softens reinsurance rates at renewal (general market dynamic; not sourced here). ONyc's forward yield (~11–12% trailing) could compress in 2027, which matters for token-multiple assumptions.
- Macro timing risk: the rally is only 3 months old. If BTC loses the $77K support flagged by analysts, a Nov/Dec TGE would hit a weaker tape; a bearish base case should price that possibility.

### Gaps
- No source quantifying typical Q4 TGE volumes/performance vs other quarters was found.
- October 2026 hurricane forecasts and live activity after Sep 29 are unknown.

## 6. Analyst frameworks for FDV from TVL/revenue for yield protocols (2026)

### Takeaway
No published 2026 standard framework was found. In practice the market prices yield/stablecoin protocols at **~0.3–1.2x FDV/TVL**, and at **~10–25x FDV/annualized gross fees** for the healthier names (HUMA ~9.5x, ENA ~16x, RE ~24x). DeFi blue chips with real protocol revenue trade at ~7–13x revenue (Meteora, Jupiter), while low-take-rate lenders trade much higher on revenue (Kamino ~60x). For OnRe, FDV/TVL is the most defensible because DefiLlama shows OnRe's tracked protocol revenue as tiny.

### Cited Findings
Derived multiples, computed from DefiLlama fees/revenue API 30-day totals × (365/30) as of 2026-09-29 and the FDVs above:

| Token | Annualized fees | Annualized revenue | Multiple |
|---|---|---|---|
| RE | $19.3M | $0.1M | FDV/fees ≈ 24x |
| HUMA | $29.9M | — | FDV/fees ≈ 9.5x |
| ENA | $244M | — | FDV/fees ≈ 16x |
| KMNO | $55.7M | $7.3M | FDV/revenue ≈ 60x |
| MET | $368M | $43.3M | FDV/revenue ≈ 7.5x |
| JUP | $229M | $84M | mcap/revenue ≈ 13x |
| Maple | $112M | $16.6M | — |
| **OnRe** | **$32.4M** | **$0.9M** | — |

- Source: [DefiLlama fees API](https://api.llama.fi/summary/fees/re?dataType=dailyFees) (same endpoint per slug)
- Revenue per unit of TVL ("real yield") is cited in 2026 as the key discriminator between protocols (e.g., Hyperliquid) — [DeFi Intel/eco.com summary via search](https://defi-intel.com/best-yield-protocols/)
- MetaDAO-style launches use deliberately low starting FDVs with performance-gated team unlocks, as a market response to high-FDV/low-float failures — [Alea Research](https://alearesearch.substack.com/p/metadao)

### Inferences
- Applying the fee multiple to OnRe's gross fees of ~$32.4M gives: 9.5x (Huma) ≈ $310M; 16x (ENA) ≈ $520M; 24x (RE) ≈ $780M. These overstate token value because fees are mostly passed to ONyc holders as yield. Unless OnRe discloses a protocol take-rate or a fee switch, the writer should rely on FDV/TVL (~$90–350M range) and haircut fee-based figures heavily.
- **Suggested bearish-leaning triangulation for the writer:**
  - Floor: Solstice 0.3x TVL → ~$90M.
  - Base: ~0.5–0.8x TVL → ~$150–240M. This sits between Huma and Solstice and reflects RE's -24% over 90 days and the cooled yield-dollar narrative.
  - Upside: RE 1.18x TVL → ~$350M.
  - Launch-day spikes (RE hit 2.4x its open) should not be used as valuation anchors.

### Gaps
- No Messari/Delphi/Blockworks 2026 valuation framework document with explicit FDV/TVL or P/F benchmarks for yield protocols was retrieved.
- OnRe's actual protocol take-rate (management/performance fee) was not verified here and is needed to make fee-multiple valuation meaningful.
