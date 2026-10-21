# Stablechains (stablecoin-specialised L1/L2s) and their tokens — TGE'd vs pre-TGE, fact base as of 21 Oct 2026

## Q1. Token status: TGE dates, venues, sale/listing/ATH/current prices, circulating MC vs FDV, and % changes

### Takeaway
Only two "pure" stablechain tokens actually trade: Plasma's XPL and Stable's STABLE. Both are far below where they opened. XPL is −95% from its Sept 2025 ATH and −51% YTD in 2026, while its circulating MC is ~$369M against an FDV of ~$815M. STABLE is +88% YTD, but that is a rebound from a post-TGE crash: it is still −25% versus its ~$0.036 open and −38% from its May 2026 ATH, and its FDV of ~$2.7B is ~5.6x its circulating MC. Adjacent "payments/stablecoin" tokens are also deep under their 2026 highs: MEGA −79% from ATH, KITE −62%, CC −45%, CELO near cycle lows. The best performer in the peer set is the incumbent TRX (+16.5% YTD). Circle's ARC exists only as a private presale ($0.30, $3B FDV) plus a genesis mint, with nothing tradable, and Stripe's Tempo has no token.

### Cited Findings

#### Data notes (read first)
- Current prices, MC, FDV, ATH/ATL dates and supply come from the CoinGecko API, pulled 2026-10-21 between 13:23 and 13:32 UTC. 2026 price paths are daily (00:00 UTC) points from the DefiLlama coins API, so daily highs and lows differ slightly from intraday ATH/ATL — [CoinGecko API (XPL example)](https://api.coingecko.com/api/v3/coins/plasma); [DefiLlama coins API (XPL example)](https://coins.llama.fi/chart/coingecko:plasma?start=1767225600&span=294&period=1d)
- The web-search budget ran out late in this research. The few items that could not be re-checked are listed under Gaps.

#### Plasma (XPL) — Tether/Bitfinex-aligned stablechain, TGE'd
- Mainnet beta and TGE happened on 25 Sep 2025 with an initial supply of 10B XPL — [Plasma docs: XPL tokenomics](https://www.plasma.org/docs/get-started/xpl/tokenomics) [High]
- The public sale ran 17–28 Jul 2025 on Sonar (Echo) and offered 10% of supply (1B XPL) at a "$500M valuation". It required KYC, and US buyers had to be accredited — [Plasma blog, 14 Jul 2025](https://www.plasma.org/company/blog/xpl-the-public-sale-and-its-role-in-the-plasma-ecosystem) [High]
- Sale price was $0.05/XPL, i.e. $500M FDV. The size of demand differs by source: "~$50M raised, oversubscribed by $323M", "$373M in commitments", or "$300M at $500M FDV" — [ICO Drops](https://icodrops.com/plasma/); [BingX Learn](https://bingx.com/en/learn/article/plasma-xpl-token-launch-airdrop-bonus-set-for-sep-25) [Medium; amounts conflict]
- Launch venues on day one were Binance, OKX and Bybit, with a Korean Upbit listing as well. XPL traded up to ~$1.54 early on, then settled around ~$1.20, roughly a ~$12B FDV — [Yahoo Finance](https://finance.yahoo.com/news/plasma-xpl-explodes-beginning-end-092024923.html) [Medium]
- ATH was $1.68 on 2025-09-27 17:31 UTC. ATL was $0.060147 on 2026-06-10 — [CoinGecko API](https://api.coingecko.com/api/v3/coins/plasma) [High]
- Current, as of 2026-10-21 13:23 UTC:
  - Price $0.08147.
  - **Circulating MC $369.2M; FDV $814.5M.**
  - Circulating supply 4.533B (45.3% of 10B).
  - 24h volume $26.9M.
  - Change: 1-year −79.2%, 200-day −31.5%, 30-day −21.6%.
  - Source: [CoinGecko API](https://api.coingecko.com/api/v3/coins/plasma) [High]
- Cross-check: XPL was $0.077 on 20 Oct 2026 at 12:36 EDT, with 24h volume of $31.1M — [CoinDesk price page](https://www.coindesk.com/price/plasma) [Medium]
- 2026 path (daily closes):
  - $0.1613 on 31 Dec 2025.
  - 2026 high $0.2096 on 6 Jan.
  - 2026 low $0.0613 on 10 Jun.
  - $0.0783 on 20 Oct, which is **−51.5% YTD**.
  - Month-ends: Jan 0.1227, Feb 0.0917, Mar 0.0883, Apr 0.0930, May 0.0890, Jun 0.1050, Jul 0.0780, Aug 0.0840, Sep 0.0959.
  - Source: [DefiLlama coins API](https://coins.llama.fi/chart/coingecko:plasma?start=1767225600&span=294&period=1d) [High]
- Messari lists 1-year performance of −88.38% and a cycle low of $0.0606 on 10 Jun 2026 — [Messari Plasma profile](https://messari.io/project/plasma) [Medium]
- Returns (my calculations from the figures above): **+63% vs the $0.05 sale price; ~−93% vs the ~$1.20 day-1 level (−94.7% vs $1.54); −95.2% vs ATH.**
- XPL now trades on 70 markets, including Binance, OKX, MEXC, Bybit, Bitstamp by Robinhood, Gate and Bitget — [CoinGecko page](https://www.coingecko.com/en/coins/plasma) [High]

#### Stable (STABLE) — Tether/Bitfinex-backed "USDT-as-gas" chain, TGE'd
- Mainnet and TGE were on 8 Dec 2025 at 13:00 UTC. Backpack listed STABLE/USD and a STABLE perp — [Backpack](https://learn.backpack.exchange/blog/stable-listed-on-backpack); [Bankless](https://www.bankless.com/read/news/stablechain-mainnet-launches-with-stable-token) [High]
- At TGE, Bitget, Backpack and Bybit announced spot trading. Binance, Coinbase and the Korean exchanges had not — [Bitget News](https://www.bitget.com/amp/news/detail/12560605101314) [Medium]
- I found no public token sale. STABLE traded pre-market on Whales Market, and WEEX listed it pre-market on 7 Nov 2025 — [Whales Market](https://whales.market/en/premarket/STABLE); [WEEX](https://www.weex.com/wiki/article/what-is-stablestable-the-stablecoin-public-chain-31460) [Medium]
- Launch trading: the token opened at ~$0.036 and hit ~$0.046 before falling >60% to ~$0.015 — [PANews](https://www.panewslab.com/en/articles/2050e827-52be-412e-9b7a-5cf172897c6b); [Bitget News](https://www.bitget.com/amp/news/detail/12560605101314) [Medium]
  - My calculation: FDV at the ~$0.036 open was ≈$3.6B on 100B supply.
- ATL was $0.0092214 on 2025-12-23. ATH was **$0.04324 on 2026-05-14** — [CoinGecko API](https://api.coingecko.com/api/v3/coins/stable-2) [High]
  - This conflicts with the "~$0.046 day-1 high" press report. CoinGecko's series does not show it.
- Current, as of 2026-10-21 13:23 UTC:
  - Price $0.02699.
  - **Circulating MC $486.1M; FDV $2.701B.**
  - Circulating supply 18.0B (18%).
  - 24h volume $10.6M.
  - Source: [CoinGecko API](https://api.coingecko.com/api/v3/coins/stable-2) [High]
- Conflicting snapshots:
  - CoinPaprika (19 Oct 2026): $0.024136 and MC $424.79M — [CoinPaprika](https://coinpaprika.com/coin/stable-stable) [Medium]
  - Messari (25 Sep 2026): circulating MC $700.9M and FDV $2.63B, which implies ~26.6B circulating before the "Universal Lock" relock covered in Q2 — [Messari report](https://messari.io/report/understanding-stable-a-comprehensive-overview) [Medium; via search summary, page returned 429]
- 2026 path (daily closes):
  - $0.0140 on 31 Dec 2025.
  - $0.0411 on 14 May.
  - $0.0264 on 20 Oct, which is **+88% YTD**.
  - Month-ends: Jan 0.0247, Feb 0.0327, Mar 0.0241, Apr 0.0332, May 0.0379, Jun 0.0382, Jul 0.0339, Aug 0.0262, Sep 0.0276.
  - Source: [DefiLlama coins API](https://coins.llama.fi/chart/coingecko:stable-2?start=1767225600&span=294&period=1d) [High]
- Returns (my calculations): **−25% vs the ~$0.036 open; −37.6% vs ATH; +193% vs ATL.** No sale price exists to compare against.
- STABLE trades on 28 markets: Bybit, Gate, Bitget, LBank, PancakeSwap v3 (BSC), MEXC, Hotcoin, BingX, Kraken and KCEX. There is no Binance spot or Coinbase market in the list — [CoinGecko page](https://www.coingecko.com/en/coins/stable-2) [High]
- Coinbase added STABLE to its listing roadmap on 19 Oct 2026. Trading is not live — [Crypto Briefing](https://cryptobriefing.com/coinbase-adds-axis-pearl-stable-roadmap/) [Medium]

#### MegaETH (MEGA) — adjacent: real-time Ethereum L2 with native stablecoin USDm (Ethena-powered)
- The public sale in Oct 2025 was priced at $0.0999, roughly a $999M FDV — [ICO Drops](https://icodrops.com/megaeth/) [Medium]
- TGE was **30 Apr 2026**, after the first KPI (10 ecosystem apps live) was met. Binance opened spot trading at 11:00 UTC with a Seed Tag, without taking an allocation or a listing fee — [The Block](https://www.theblock.co/amp/post/399563/megaeth-token-goes-live-as-major-exchanges-open-mega-trading); [crypto.news](https://crypto.news/megaeth-launches-mega-token-as-major-exchanges-open-trading/); [Parameter](https://parameter.io/megaeth-mega-debuts-across-major-exchanges-without-paying-listing-fees/) [High]
  - The CoinGecko page says "TGE November 2025". That conflicts with these reports, and with the API's ATH date and the DefiLlama price series, both of which start on 30 Apr 2026.
- Opening price was ~$0.16 (FDV ~$1.7B) per [Parameter](https://parameter.io/megaeth-mega-debuts-across-major-exchanges-without-paying-listing-fees/), or ~$0.183 (FDV $1.82B) per [CoinCentral](https://coincentral.com/megaeth-mega-price-token-launches-on-binance-and-major-exchanges-with-no-listing-fees-paid/). It then fell ~38% in 72 hours to ~$0.128 [Medium]
- ATH was $0.2177 on 2026-04-30 (TGE day). ATL was $0.0301 on 2026-08-14 — [CoinGecko API](https://api.coingecko.com/api/v3/coins/megaeth) [High]
- Current, as of 2026-10-21: $0.04637; **circulating MC $52.4M; FDV $463.8M**; circulating supply 1.13B (11.3%) — [CoinGecko API](https://api.coingecko.com/api/v3/coins/megaeth) [High]
- Returns (my calculations): **−53.6% vs sale; −71% to −75% vs open; −78.7% vs ATH.**

#### Kite AI (KITE) — adjacent: "agentic stablecoin payments" L1
- TGE was 3 Nov 2025 on Binance with a Seed Tag — [CoinMarketCap AI](https://coinmarketcap.com/cmc-ai/kite/price-analysis/) [Medium]
- KITE opened at ~$0.11 and slid to $0.095 within hours — [Bitget News](https://www.bitget.com/news/detail/12560605059352) [Medium]
- In its first hours it carried a $159M MC and an $883M FDV — [CoinDesk, 3 Nov 2025](https://www.coindesk.com/business/2025/11/03/ai-payments-startup-kite-debuts-token-with-usd263m-trading-volume-in-first-two-hours) [High]
- ATL was $0.0618 on 2025-11-04. ATH was $0.3197 on 2026-03-06 — [CoinGecko API](https://api.coingecko.com/api/v3/coins/kite-2) [High]
- Current, as of 2026-10-21: $0.1224; **circulating MC $292.7M; FDV $1.224B**; circulating supply 2.391B (23.9%) — [CoinGecko API](https://api.coingecko.com/api/v3/coins/kite-2) [High]
- 2026 path: $0.0897 on 31 Dec, peaking at $0.3008 on 9 Mar (daily), then $0.1214 on 20 Oct, which is **+35% YTD** — [DefiLlama coins API](https://coins.llama.fi/chart/coingecko:kite-2?start=1767225600&span=294&period=1d) [High]
- Returns (my calculations): ~+11% vs the ~$0.11 open; −61.7% vs ATH.

#### Canton Network (CC) — adjacent: institutional privacy L1 used for settlement and tokenized collateral
- There was no ICO. Supply is emission-based: circulating equals total at 39.887B, and max supply is unlimited — [CoinGecko API](https://api.coingecko.com/api/v3/coins/canton-network) [High]
- ATL was $0.0590 on 2025-12-06. ATH was $0.1942 on 2026-02-03 — [CoinGecko API](https://api.coingecko.com/api/v3/coins/canton-network) [High]
- Current, as of 2026-10-21: $0.1072; **MC = FDV = $4.276B**; 200-day −22.9% — [CoinGecko API](https://api.coingecko.com/api/v3/coins/canton-network) [High]
- 2026 path: $0.1523 on 31 Dec, $0.188 on 3 Feb, low $0.0906 on 17 Aug, $0.1049 on 20 Oct, which is −31% YTD — [DefiLlama coins API](https://coins.llama.fi/chart/coingecko:canton-network?start=1767225600&span=294&period=1d) [High]
- Venues include Temple Digital Group (CC/USDCx), Bybit, Gate, Bitget, OKX, Kraken, MEXC and KuCoin — [CoinGecko page](https://www.coingecko.com/en/coins/canton) [High]

#### Celo (CELO) — Ethereum L2 since 2025 with a stablecoin/payments pivot
- Current, as of 2026-10-21: $0.08585; MC $52.2M; FDV $85.9M; circulating supply 608.4M of 1B — [CoinGecko API](https://api.coingecko.com/api/v3/coins/celo) [High]
- ATL was $0.0557 on 2026-06-30, and 1-year change is −64.6% — [CoinGecko API](https://api.coingecko.com/api/v3/coins/celo) [High]
- YTD 2026 is −23.8% ($0.1112 → $0.0847) — [DefiLlama coins API](https://coins.llama.fi/chart/coingecko:celo?start=1767225600&span=294&period=1d) [High]

#### Benchmarks
- TRX: $0.3313 with **MC = FDV = $31.48B**, rank #8 — [CoinGecko TRX page](https://www.coingecko.com/en/coins/tron) [High]
  - YTD +16.5% ($0.2843 → $0.3312), with a 2026 high of $0.3754 on 26 May — [DefiLlama coins API](https://coins.llama.fi/chart/coingecko:tron?start=1767225600&span=294&period=1d) [High]
- SOL: $107.29 on 21 Oct. YTD −14.5% ($124.49 → $106.39), with a 2026 low of $62.16 on 6 Jun — [DefiLlama coins API](https://coins.llama.fi/chart/coingecko:solana?start=1767225600&span=294&period=1d) [High]
  - Circulating supply is ~589.55M — [MetaMask price page](https://metamask.io/price/solana) [Medium]
- Macro context, 2026 YTD:
  - BTC −5.2% ($87,515 → $82,944), 2026 low $58,558 on 1 Jul — [DefiLlama coins API](https://coins.llama.fi/chart/coingecko:bitcoin?start=1767225600&span=294&period=1d) [High]
  - ETH −17.6% ($2,967 → $2,446), 2026 low $1,565 on 25 Jun — [DefiLlama coins API](https://coins.llama.fi/chart/coingecko:ethereum?start=1767225600&span=294&period=1d) [High]

#### Not tradable / no token (status check of the seed list)
- **Arc (Circle):** all 10B ARC were genesis-minted in the US in the week of the 16 Sep 2026 mainnet launch. ARC is not tradable, and Circle calls the mint "not a commitment to publicly launch or distribute ARC" — [The Block, 16 Sep 2026](https://www.theblock.co/news/ecosystems/2026-09-16-circle-launches-arc-mainnet-with-blackrock-and-visa-among-validators-mints-10-billion-arc-tokens-415250); [Stablecoin Insider](https://stablecoininsider.org/circle-arc-mainnet-launch/) [High]
- **Tempo (Stripe/Paradigm):** no native token. Fees are paid in USD stablecoins through a Fee AMM, defaulting to pathUSD — [Datawallet](https://www.datawallet.com/crypto/tempo-explained); [Dwellir](https://www.dwellir.com/blog/stablechain-rpc-guide) [Medium]
- **Noble:** a CoinGecko search for "noble" returns only bridged USDC.n, so there is no traded NOBLE token — [CoinGecko search API](https://api.coingecko.com/api/v3/search?query=noble) [Medium]
- **1Money:** no native token per the CEO. An unexplained "1MNT" entry appears on its explorer — see Q5 — [The Block](https://www.theblock.co/news/business/2025-03-10-1money-ceo-brian-shroder-on-building-l1-for-stablecoins-with-no-native-token-and-flat-gas-fees-345455) [Medium]
- **Codex and Converge:** I found no token for either. Converge's validators stake ENA — see Q5.

### Inferences
- Every TGE'd stablechain or payments token in this cohort trades below its listing-day valuation. XPL is ~−93%, STABLE −25%, MEGA ~−72%. KITE is the exception at ~+11% vs its open, but it is −62% from its 2026 ATH.
- XPL's 2026 drawdown (−51.5% YTD) is roughly 3–10x worse than BTC (−5%), SOL (−15%) and ETH (−18%). That points to project-specific causes beyond market beta: the unlock calendar, falling TVL and near-zero fee capture (see Q2 and Q3).
- STABLE's +88% YTD is mostly a mean-reversion from the post-TGE capitulation (ATL 23 Dec 2025). Its circulating-MC drop from ~$701M on 25 Sep to ~$486M on 21 Oct 2026 is largely mechanical: circulating supply went from ~26.6B to 18.0B after the relock, rather than price alone.
- The only peer token with positive 2026 returns and a large stablecoin base is the incumbent TRX. Its MC is roughly 85x XPL's.

### Gaps
- I could not find exact first-trade prices by venue for XPL or STABLE, or for Hyperliquid/Aevo pre-market marks.
- No public data on STABLE's seed-round valuation or token price was found. Exact circulating supply at STABLE's TGE was not found either.
- I could not identify the driver of STABLE's 14 May 2026 ATH. Search returned only low-quality or promotional items, such as a [HokaNews piece](https://www.hokanews.com/2026/05/stable-outpaces-xpl-as-investors-focus.html) claiming "STABLE outpaces XPL".
- I could not verify whether KITE was a Binance Launchpool project or had any public sale price.
- Whether Binance spot ever listed STABLE is unresolved: CoinGecko's market list shows no Binance spot pair.

## Q2. Tokenomics: circulating %, airdrops, unlock schedules, notable past unlocks and their price impact, and the next 6 months of unlocks

### Takeaway
XPL has the heaviest near-term overhang in the cohort. After the 25 Sep 2026 cliff, which added ~63% to float, 227.8M XPL unlock every month. That is ~1.37B XPL from 25 Oct 2026 to 25 Mar 2027, or **~30% of current circulating supply**, and there is still no staking sink. STABLE moved 82% of supply into a "Universal Lock" with no release before 8 Dec 2027, which pushes the overhang into 2027–2029 behind a $0.025 VWAP gate. KITE faces a single 640M cliff on 3 Nov 2026, equal to ~27% of its float.

### Cited Findings

#### Plasma (XPL)
- Allocation:
  - Public sale 10% (1B).
  - Ecosystem & Growth 40% (4B): 0.8B unlocked at launch, the remaining 3.2B monthly over 3 years to 25 Sep 2028.
  - Team 25% (2.5B): one-third on a 1-year cliff on 25 Sep 2026, the rest monthly over 2 years.
  - Investors 25%: same schedule as the team.
  - Non-US sale buyers unlocked at launch. US buyers unlocked on 28 Jul 2026.
  - Source: [Plasma docs](https://www.plasma.org/docs/get-started/xpl/tokenomics) [High]
- Staking and inflation (5%/yr, falling 0.5%/yr to a 3% floor) activate only when external validators and delegation go live. Neither is live. Locked team and investor XPL earns no rewards, and base fees are burned (EIP-1559) — [Plasma docs](https://www.plasma.org/docs/get-started/xpl/tokenomics) [High]
  - Delegation, once expected in Q1 2026, has no fixed timeline — [Datawallet](https://www.datawallet.com/crypto/what-is-plasma-chain); [CoinMarketCap latest updates](https://coinmarketcap.com/cmc-ai/plasma-xpl/latest-updates/) [Medium]
- Airdrop:
  - About 1% of supply (100M XPL), including an equal ~9,304 XPL to each eligible pre-depositor, worth ~$8,390 at debut — [BingX Learn](https://bingx.com/en/learn/article/plasma-xpl-token-launch-airdrop-bonus-set-for-sep-25); [PANews](https://www.panewslab.com/en/articles/1237e3c6-812c-46b4-b0f8-8a30a3ddc7dc) [Medium]
  - XPL was also a Binance HODLer Airdrops asset — [Yahoo Finance](https://finance.yahoo.com/news/binance-adds-plasma-xpl-hodler-093724491.html) [Medium]
- Current circulating supply of 4.533B reconciles exactly to the schedule (my calculation): 1B sale + 0.8B ecosystem at launch + 12 × 88.89M monthly ecosystem tranches + 1.667B team/investor cliff = 4.533B. This matches [CoinGecko API](https://api.coingecko.com/api/v3/coins/plasma).
- **US public-sale unlock, 28 Jul 2026:** the amount actually claimed was not disclosed. XPL traded near $0.084 on 28 Jul after bouncing off ~$0.079 — [AMBCrypto, 28 Jul 2026](https://ambcrypto.com/xpl-crypto-price-prediction-2030-can-plasma-adoption-outpace-token-dilution/) [Medium]
  - Daily closes went from $0.1050 at end-June to $0.0780 at end-July, about −26% across the unlock month — [DefiLlama coins API](https://coins.llama.fi/chart/coingecko:plasma?start=1767225600&span=294&period=1d) [High]
- **Team/investor cliff, 25 Sep 2026:** ~1.76B XPL, equal to 17.6% of initial supply and +63.2% of circulating, worth $144–198M. There is no data on how much was sold — [Pluang/Tokenpost, 25 Sep 2026](https://pluang.com/en/news-feed/plasma-buat-1-76-miliar-xpl-bisa-diperdagangkan-dalam-pembukaan-terjadwal) [Medium]
  - It breaks down as 833.3M team plus 833.3M investors, with an 88.9M ecosystem tranche the same day — [CryptoTicker, 15 Oct 2026](https://cryptoticker.io/en/plasma-xpl-unlock-monthly-schedule/) [Medium]
  - Price went from $0.0959 at end-September to $0.0783 on 20 Oct, about −18%; CoinGecko's 30-day change is −21.6% — [DefiLlama coins API](https://coins.llama.fi/chart/coingecko:plasma?start=1767225600&span=294&period=1d); [CoinGecko API](https://api.coingecko.com/api/v3/coins/plasma) [High]
- **Monthly unlocks from 25 Oct 2026:** 227,777,777 XPL (69.44M team + 69.44M investors + 88.89M ecosystem), ≈5.0% of circulating, ~$17.6M at $0.077 — [CryptoTicker](https://cryptoticker.io/en/plasma-xpl-unlock-monthly-schedule/) [Medium]
  - CoinGecko also flags the next unlock as 25 Oct — [CoinGecko page](https://www.coingecko.com/en/coins/plasma) [High]
- **Next 6 months, 25 Oct 2026 – 25 Mar 2027 (my calculation):** 6 × 227.8M = **1.367B XPL**. That is ≈30.1% of today's 4.533B float, 13.7% of total supply, and ~$111M at $0.0815.
  - Projected circulating supply: ~5.9B by end-March 2027 and ~7.27B by 25 Oct 2027. All 10B are out by 25 Sep 2028 — [CryptoTicker](https://cryptoticker.io/en/plasma-xpl-unlock-monthly-schedule/) [Medium]
- Conflict: one CoinMarketCap AI page framed a "2.5B-token July 2026 unlock", which contradicts the docs — [CoinMarketCap AI](https://coinmarketcap.com/cmc-ai/plasma-xpl/price-prediction/) [Low]
- Named investors include Founders Fund, Framework, Bitfinex/Tether and DRW Cumberland — [GitHub deep-dive](https://github.com/Ricosworks1/blockchain-payment-flow-analysis/releases/tag/deep-dive-plasma-xpl-1-81b-cliff-unlock-sept-2026) [Low]

#### Stable (STABLE)
- Supply is a fixed 100B. A "Genesis Distribution" of 10% was fully unlocked at mainnet — [EGW News](https://egw.news/crypto/news/30966/stable-launches-mainnet-and-tge-on-december-8-pJpu-XC9t) [Medium]
- **Universal Lock (whitepaper update, reported 22 Aug 2026):**
  - Covers 82B STABLE: ~25B team, ~25B investors/advisers and ~32B ecosystem/Foundation. About 18B sit outside the lock.
  - Releases are a percentage of the 82B pool, and each phase vests daily over ~180 days:

    | Date | Share | Tokens |
    |---|---|---|
    | 8 Dec 2027 | 5% | 4.1B |
    | 8 Mar 2028 | 5% | 4.1B |
    | 8 Jun 2028 | 10% | 8.2B |
    | 8 Sep 2028 | 15% | 12.3B |
    | 8 Dec 2028 | 15% | 12.3B |
    | 8 Mar 2029 | 20% | 16.4B |
    | 8 Jun 2029 | 30% | 24.6B |

  - The framework ends on 8 Dec 2029.
  - VWAP gate: if the 30-day VWAP is below **$0.025**, a stage is postponed by 3 months, with a 9-month cumulative cap. This is a delay mechanism, not a price floor.
  - Foundation tokens that had already unlocked under the old model get relocked. More than 25B STABLE were circulating before the change.
  - Source: [KuCoin blog, 22 Aug 2026](https://www.kucoin.com/blog/stable-whitepaper-update-82-of-stable-supply-enters-universal-lock-with-unlocks-through-2029) [Medium]
- The effective date was reported as 5 Oct 2026 — [ChainCatcher Q4 2026 unlocks](https://www.chaincatcher.com/en/article/2293219) [Low]
  - CoinGecko's current circulating supply of 18.0B is consistent with the lock being in force — [CoinGecko API](https://api.coingecko.com/api/v3/coins/stable-2) [High]
- Conflicting unlock data:
  - RootData, via ChainCatcher on 1 Oct 2026, flagged an 8 Oct unlock of ~$24.9M on the legacy ~888.9M monthly ecosystem pattern — [ChainCatcher](https://www.chaincatcher.com/en/article/2293485) [Low]
  - DropsTab still lists the next unlock as 888.89M STABLE — [DropsTab vesting](https://dropstab.com/coins/stable-2/vesting) [Low]
  - Another tracker flagged an 8 Dec 2026 unlock — [CoinMarketCap AI](https://coinmarketcap.com/cmc-ai/stable/price-prediction/) [Low]
- **Next 6 months (my calculation):** ≈0% of float if the Universal Lock is in force, since no release is due before 8 Dec 2027. Under the legacy schedule it would be ~0.89B a month (≈4.9% of the 18B float), roughly 30% over 6 months. Which applies is unresolved.
- STABLE at $0.027 sits only ~8% above the $0.025 VWAP gate (my calculation).
- Airdrop: I found no confirmed STABLE airdrop to pre-depositors. Pre-deposit "rewards" were Morpho yield and Pendle receipt-token markets — [Yield Network](https://www.yieldnetwork.io/blog/stable-predeposit-case-study) [Medium]

#### Kite AI (KITE)
- Supply is capped at 10B. The whitepaper allocates 48% to community, 12% to investors and 20% to team/early contributors — [CoinDesk](https://www.coindesk.com/business/2025/11/03/ai-payments-startup-kite-debuts-token-with-usd263m-trading-volume-in-first-two-hours) [High]
- **Next unlock is 3 Nov 2026: 640M KITE** (240M investors + 400M team/advisors/early contributors), about $78.3M — [CoinGecko page](https://www.coingecko.com/en/coins/kite-ai) [Medium]
  - My calculation: that is ≈26.8% of the 2.391B float.

#### MegaETH (MEGA)
- Circulating supply is 1.13B of 10B (11.3%) — [CoinGecko API](https://api.coingecko.com/api/v3/coins/megaeth) [High]
- The forward unlock schedule was not found (see Gaps).

#### Canton (CC)
- CC has no vesting cliffs. Supply is emission-driven and unlimited, with circulating equal to total at 39.887B — [CoinGecko API](https://api.coingecko.com/api/v3/coins/canton-network) [High]

#### Arc (ARC, not trading)
- The 10B genesis supply is split 60% ecosystem, 25% Circle and 15% long-term reserve. Initial issuance is expected at 2–3% a year, targeting "inflation neutrality" — [Yahoo Finance/Decrypt](https://finance.yahoo.com/news/arc-stablecoin-blockchain-usdc-issuer-150103906.html) [High]
- Presale buyers hold ~740M ARC (≈7.4%) and are locked for at least 1 year after Arc moves to PoS or dPoS — [Cointelegraph via TradingView](https://www.tradingview.com/news/cointelegraph:ad4cbe069094b:0-usdc-issuer-circle-raises-222m-in-arc-token-presale-valued-at-3b/) [Medium]
- Buyers have repayment rights if tokens are not delivered, or the PoS transition is not completed, by 8 May 2028 — [KuCoin News](https://www.kucoin.com/news/flash/circle-s-arc-secures-222m-pre-sale-network-valued-at-3b) [Medium]

#### TRX (benchmark)
- Q3 2026 issuance was 360.2M TRX generated against 234.5M burned, for net issuance of +125.8M. About 48.16% of supply is staked — [crypto.news, 19 Oct 2026](https://crypto.news/tron-handles-trillions-in-stablecoin-transfers-how-much-does-the-network-earn/) [Medium]

### Inferences
- XPL's float grows ~30% in six months, plus another ~1.37B by Sept 2027, with no staking yield or burn large enough to absorb it. Chain fees are ~$16K a month (see Q3). Continued supply pressure is the base case, and it is probably the main reason the post-cliff bounce failed.
- STABLE's re-lock turned a 2026 overhang problem into a 2027–2029 one. It looks bullish near-term, but the $0.025 VWAP gate means price weakness defers rather than cancels supply. Holders face a large, uncertain release wall starting Dec 2027.
- KITE's 3 Nov 2026 cliff (~27% of float) is the largest single dated unlock among adjacent names in the next month.

### Gaps
- I could not establish how much US public-sale XPL was claimed on 28 Jul 2026, or whether team/investor wallets sold after 25 Sep 2026.
- The official effective date of STABLE's Universal Lock is unconfirmed: I could not reach a primary Stable Foundation post. The 8 Oct and 8 Dec 2026 tracker entries are also unexplained.
- I did not find MegaETH's unlock schedule or KITE's monthly unlocks after 3 Nov 2026. Search budget ran out.

## Q3. Fundamentals: 2026 stablecoin supply (peak vs now), TVL, DEX volume, activity, fees/revenue, incentive vs organic share, key integrations, and pre-deposit retention

### Takeaway
On-chain traction did not hold for the TGE'd stablechains.
- **Plasma** fell from a $6.35B stablecoin peak in Oct 2025 to ~$1.3B, of which ~43% is yield-seeking USDe. DeFi TVL fell from $6.36B to $0.57B, and the chain earned only ~$73K in gas fees in 2026.
- **Stable** turned >$2B of pre-deposits into just ~$20–24M of on-chain stablecoins.
- **MegaETH's** USDm/USDe base collapsed from ~$811M in May to ~$18M.

Meanwhile, the tokenless corporate chains (Circle's Arc at ~$0.69–0.77B after 5 weeks, Stripe's Tempo at ~$0.72B) and exchange/fintech chains (Robinhood Chain ~$1.05B, OKX's X Layer ~$1.5B) are adding stablecoins quickly. Tron added ~$12.4B in 2026 to reach ~$94B. All four stablechains together hold <1% of the ~$301B stablecoin market.

### Cited Findings

#### Market context
- Total USD-pegged supply summed across chains was **$300.83B** on 21 Oct 2026.
  - Ethereum $143.24B, Tron $94.07B, Solana $15.64B, BSC $13.64B, Hyperliquid $7.03B, Base $5.08B, Arbitrum $3.64B, Polygon $2.82B, X Layer $1.50B, Avalanche $1.34B.
  - **Plasma $1.288B (#11)**, Robinhood Chain $1.053B (#12), XRPL $1.009B, Aptos $0.852B.
  - **Arc $0.755B (#15)**, TON $0.730B, **Tempo $0.724B (#17)**, Monad $0.697B.
  - Celo $113.8M, Noble $84.1M, Pharos $63.9M, **Stable $19.9M (#60)**, MegaETH $18.2M, Codex $5.2M.
  - Source: [DefiLlama stablecoin chains API](https://stablecoins.llama.fi/stablecoinchains) [High]
- By asset: USDT $182.7B, USDC $72.2B, USDe $4.66B, USDG $3.07B, OUSD $0.83B — [DefiLlama stablecoins API](https://stablecoins.llama.fi/stablecoins?includePrices=false) [High]
- Total stablecoins were $308.0B on 13 Aug 2026 — [Eco, citing DefiLlama](https://eco.com/support/en/articles/15192015-what-is-usdt0-tether-s-omnichain-stablecoin-explained-2026) [Medium]
- Stablechain share (my calculation): Plasma + Arc + Tempo + Stable = $2.79B, or **0.93%** of $300.8B.
  - Dwellir also states these four held "<1% of stablecoin supply on 7 Oct 2026" — [Dwellir](https://www.dwellir.com/blog/stablechain-rpc-guide) [Medium]
- Different DefiLlama endpoints give slightly different chain totals: Plasma $1.29–1.35B, Arc $0.69–0.77B, Stable $19.9–23.8M. I cite the chains endpoint as the headline figure.

#### Plasma
- Stablecoins: ATH **$6,354M on 9 Oct 2025** → $1,924M on 1 Jan 2026 → 2026 peak $2,199M on 14 Jan → 2026 low **$760M on 12 Aug** → **$1,346M on 21 Oct 2026**.
  - My calculations: −79% from ATH and −30% YTD.
  - Source: [DefiLlama stablecoin chart](https://stablecoins.llama.fi/stablecoincharts/Plasma) [High]
  - Stablecoin Insider gives a similar picture: ~$6.35B down to ~$1.31B on 16 Oct 2026 (−79%) — [Stablecoin Insider](https://stablecoininsider.org/paul-faecks-plasma/) [Medium]
- Composition on 21 Oct: **USDT $714.4M; USDe $579.4M (≈43%)**; YZUSD $58.2M — [DefiLlama stablecoins API](https://stablecoins.llama.fi/stablecoins?includePrices=false) [High]
  - USDT on Plasma: ATH $5,349M on 18 Oct 2025 → $1,377M on 1 Jan 2026 → low $614M on 3 Sep 2026 → $708M — [DefiLlama USDT](https://stablecoins.llama.fi/stablecoin/1) [High]
  - USDe on Plasma: ATH $1,102M on 28 Sep 2025 → $401M on 1 Jan → low $62.5M on 24 Apr → **$580M** on 21 Oct 2026. Month-ends: Jul $101M, Aug $199M, Sep $530M — [DefiLlama USDe](https://stablecoins.llama.fi/stablecoin/146) [High]
  - Native Circle USDC has been live on Plasma since late Aug 2026 — [Dwellir](https://www.dwellir.com/blog/stablechain-rpc-guide) [Medium]. It does not appear among Plasma assets ≥$0.1M in DefiLlama.
- DeFi TVL: ATH **$6,360M on 9 Oct 2025** → $1,293M on 1 Jan 2026 → 2026 peak $2,651M on 16 Jan → **$572M on 21 Oct 2026** (−91% from ATH) — [DefiLlama TVL API](https://api.llama.fi/v2/historicalChainTvl/Plasma) [High]
- Protocol TVL on Plasma (CEX wallets and curators included, so these overlap):
  - **Aave V3 $486.9M**, about 85% of DeFi TVL.
  - CEX wallets: Binance $267.0M, Bybit $71.6M, Gate $53.4M.
  - Yuzu Money $65.7M, Fluid $37.4M, Plasma Saving Vaults $31.8M, **Plasma One $31.2M**.
  - Source: [DefiLlama protocols API](https://api.llama.fi/protocols) [High]
- DEX volume:
  - 2026 YTD $2.76B; last 30 days $241M.
  - Monthly: Jan $690M, Feb $350M, Mar $167M, Apr $322M, May $142M, Jun $327M, Jul $181M, Aug $167M, Sep $300M, Oct (1–21) $119M.
  - Source: [DefiLlama DEX API](https://api.llama.fi/overview/dexs/Plasma) [High]
- Fees:
  - Chain gas fees (= burned revenue): **2026 YTD ~$73K**, last 30 days ~$16K, all-time ~$268K — [DefiLlama fees API](https://api.llama.fi/summary/fees/plasma?dataType=dailyFees) [High]
  - App-level fees on Plasma, mostly lending interest: 2026 YTD $58.3M, falling from $11.7M in January to ~$4M a month since May — [DefiLlama app fees](https://api.llama.fi/overview/fees/Plasma) [High]
  - AMBCrypto, citing DefiLlama in July 2026, gave >932K daily transactions and ~$159 a day of chain revenue — [AMBCrypto](https://ambcrypto.com/xpl-crypto-price-prediction-2030-can-plasma-adoption-outpace-token-dilution/) [Medium]
- Incentive evidence from launch:
  - Aave on Plasma reached ~$6.6B TVL by mid-Oct 2025, with "~$160 of TVL per $1 of incentives" in its first 8 weeks — [Plasma insights](https://www.plasma.to/insights/aave-plasma-global-credit-layer) [Medium; self-reported]
  - $4B of DeFi deposits arrived on day one as users chased XPL rewards — [DL News](https://www.dlnews.com/articles/defi/plasma-defi-deposits-soar-as-users-chase-xpl-token-rewards/) [High]
  - About 65% of Plasma stablecoins sat in lending markets chasing rewards — [Datawallet](https://www.datawallet.com/crypto/what-is-plasma-chain) [Low]
  - A 7-day launch incentive program ran through 2 Oct 2025 — [Bitget News](https://www.bitget.com/news/detail/12560604989972) [Low]
- Pre-deposit campaign (2025): more than 4,000 wallets participated, with a median deposit of ~$12K. The Veda vault was locked until mainnet beta — [Plasma blog](https://www.plasma.org/company/blog/xpl-the-public-sale-and-its-role-in-the-plasma-ecosystem) [High]
  - Plasma launched with ~$2B of stablecoin liquidity across 100+ DeFi partners — [Eco](https://eco.com/support/en/articles/15010646-best-stablecoin-l1-chains-in-2026-the-new-wave-of-dollar-native-blockchains) [Medium]
  - DefiLlama's first print was $1,022M on 24 Sep 2025 — [DefiLlama stablecoin chart](https://stablecoins.llama.fi/stablecoincharts/Plasma) [High]
- **Plasma One** (consumer neobank) launched publicly on 17 Jun 2026:
  - Visa card usable in 180+ countries, with cashback paid in XPL.
  - Tiers: Lite (free), Core (10,000 XPL lock or $120/yr) and Platinum (100,000 XPL lock).
  - The private beta had 5,000 weekly active users before launch.
  - Sources: [Yahoo Finance](https://finance.yahoo.com/markets/crypto/articles/plasma-one-neobank-goes-live-162135847.html); [BusinessWire, 19 Jun 2026](https://www.businesswire.com/news/home/20260619440985/en/Plasma-One-Launches-to-Herald-a-New-Era-of-Stablecoin-Banking) [High]
  - Crypto card volume passed $8M (date unclear) — [CoinGape](https://coingape.com/block-of-fame/pulse/stablecoin-neobank-plasma-one-goes-live-crossing-8m-crypto-card-volume/) [Low]
  - Plasma One holds $31.2M of TVL — [DefiLlama protocols API](https://api.llama.fi/protocols) [High]

#### Stable
- Pre-deposits:
  - **Phase 1:** an $825M cap filled in ~22 minutes on 23–24 Oct 2025. One entity supplied more than $500M (over 60%), and about 194–274 wallets took part. At least $540M was deposited before the public announcement.
  - **Phase 2** (opened 6 Nov 2025): a $500M cap drew more than $1.1B of eligible deposits from over 10,000 KYC'd wallets. About 45% was allocated above a guaranteed $1K, and ~55% was refunded.
  - Total: ~$2.6B from more than 26,000 wallets.
  - Source: [Yield Network case study, 10 Nov 2025](https://www.yieldnetwork.io/blog/stable-predeposit-case-study) [Medium]
  - Bankless gives ">$2B from >24,000 wallets" — [Bankless](https://www.bankless.com/read/news/stablechain-mainnet-launches-with-stable-token) [High]
- **Post-TGE retention:** on-chain stablecoins were $483M on 10 Dec 2025 → ATH $706M on 16 Dec → **$161M on 1 Jan 2026** → low **$10.1M on 19 May** → **$23.8M on 21 Oct 2026** — [DefiLlama stablecoin chart](https://stablecoincharts.llama.fi/stablecoincharts/Stable) [High]
  - Composition: USDT $19.8M and frxUSD $3.9M — [DefiLlama stablecoins API](https://stablecoins.llama.fi/stablecoins?includePrices=false) [High]
  - My calculation: retained supply is ≈1% of the $2–2.6B pre-deposits and ≈3.4% of the Dec-2025 on-chain peak.
- DeFi TVL: ATH $100.0M on 14 Dec 2025 → 2026 peak $38.7M on 3 Aug → $28.5M on 21 Oct — [DefiLlama TVL API](https://api.llama.fi/v2/historicalChainTvl/Stable) [High]
  - DefiLlama's chain page on 18 Oct showed $29.33M of TVL and $20.58M of stablecoins — [DefiLlama chain page](https://defillama.com/chain/stable) [High]
- Top protocols: Concrete $66.3M (vault allocator), Morpho Blue $27.0M, Bybit $22.4M, Gauntlet $20.8M, LayerZero $19.8M — [DefiLlama protocols API](https://api.llama.fi/protocols) [High]
- Activity and fees: DEX volume was **$8.06M for all of 2026 YTD** and ~$16K over the last 30 days. App fees were $3.8M YTD. Chain gas fees are not tracked by DefiLlama — [DefiLlama DEX API](https://api.llama.fi/overview/dexs/Stable); [DefiLlama app fees](https://api.llama.fi/overview/fees/Stable) [High]
- Technical design:
  - Native USDT0 has been the gas token since Feb 2026, when v1.2.0 replaced gUSDT.
  - Consensus is DPoS with 11 validators on StableBFT, a CometBFT derivative.
  - Source: [Dwellir](https://www.dwellir.com/blog/stablechain-rpc-guide) [Medium]
- Validators may share USDT gas fees with STABLE delegators — [Messari](https://messari.io/report/understanding-stable-a-comprehensive-overview) [Medium]

#### Arc (Circle) — public mainnet 16 Sep 2026
- Testnet launched in Oct 2025 and processed more than 700M transactions in under a year — [The Block](https://www.theblock.co/news/ecosystems/2026-09-16-circle-launches-arc-mainnet-with-blackrock-and-visa-among-validators-mints-10-billion-arc-tokens-415250) [High]
- Launch-day figures: 7.76M transactions, ~$280K of fees and ~$650M of on-chain USDC, per Dune — [KuCoin/Odaily](https://www.kucoin.com/news/flash/arc-mainnet-records-7-76m-transactions-and-100m-usdc-transfers-on-launch-day) [Medium; its transfer-volume figures conflict]
- Stablecoins: $649M on 17 Sep → low $452M on 28 Sep → $772M on 21 Oct (chart), or $755M on the chains endpoint — [DefiLlama stablecoin chart](https://stablecoins.llama.fi/stablecoincharts/Arc) [High]
  - Composition: USDC $677.8M, EURC $8.7M, GBPA $0.8M — [DefiLlama stablecoins API](https://stablecoins.llama.fi/stablecoins?includePrices=false) [High]
- DeFi TVL: ATH $566M on 12 Oct, $532M on 21 Oct — [DefiLlama TVL API](https://api.llama.fi/v2/historicalChainTvl/Arc) [High]
  - Top protocols: Morpho $303.8M, Aave V4 $183.1M, Galaxy Curation $90.4M, Keyrock $75.1M, Uniswap V3 $23.3M, Circle Gateway $12.7M — [DefiLlama protocols API](https://api.llama.fi/protocols) [High]
- DEX volume was $1.04B in September and $735M for 1–21 October. App fees were $5.9M over 30 days, down 70% month on month — [DefiLlama DEX API](https://api.llama.fi/overview/dexs/Arc); [DefiLlama app fees](https://api.llama.fi/overview/fees/Arc) [High]
- Integrations:
  - Aave V4, Morpho and Uniswap from day one. StableFX supports USDC, EURC, GBPA, JPYC and KRW1. BlackRock BUIDL and USYC can be used as collateral. Circle and DTCC plan tokenization of DTC assets on Arc from H2 2027 — [The Block](https://www.theblock.co/news/ecosystems/2026-09-16-circle-launches-arc-mainnet-with-blackrock-and-visa-among-validators-mints-10-billion-arc-tokens-415250) [High]
  - BNY, HSBC, Société Générale and State Street have access — [Yahoo Finance/Decrypt](https://finance.yahoo.com/news/arc-stablecoin-blockchain-usdc-issuer-150103906.html) [High]

#### Tempo (Stripe + Paradigm) — mainnet 18 Mar 2026
- Mainnet launched with the Machine Payments Protocol (MPP), after a public testnet in Dec 2025 — [crypto.news](https://crypto.news/stripe-and-paradigms-tempo-mainnet-goes-live-for-machine-payments/); [Finextra](https://www.finextra.com/newsarticle/47462/stripe-backed-tempo-blockchain-goes-live-with-machine-payments-protocol) [High]
- Validators are permissioned:
  - Stripe, Visa and Zodia Custody joined in April 2026, and MoneyGram in May — [Everstake](https://everstake.com/resources/blog/what-is-tempo-stripe-and-paradigms-stablecoin-payments-blockchain-explained) [Medium]
  - zerohash joined on 6 Oct 2026 — [Tempo blog](https://tempo.xyz/blog/zerohash-joins-tempo-as-a-validator-and-infrastructure-partner/) [High]
- Stablecoins: $6.2M on 28 Apr → ATH $759M on 8 Oct → **$723M** on 21 Oct — [DefiLlama stablecoin chart](https://stablecoins.llama.fi/stablecoincharts/Tempo) [High]
  - Composition:
    - **OUSD $529.4M (≈73%; $0 a month earlier)**.
    - Bridge's USDB $100.7M, pathUSD $54.0M.
    - USDC $26.0M (down from $83.6M a month earlier), USDT $9.9M.
  - Source: [DefiLlama stablecoins API](https://stablecoins.llama.fi/stablecoins?includePrices=false) [High]
- **OUSD (Open USD)** launched on 30 Sep 2026 with $400M+ of launch liquidity on Tempo:
  - Issuer Open Standard, backed by Coinbase, Mastercard, Stripe and Visa. Mint and burn at no cost through Coinbase, Stripe and Visa, with Mastercard "soon" — [Tempo blog, 30 Sep 2026](https://tempo.xyz/blog/ousd-is-live-on-tempo/) [High]
  - Issued by Bridge, with reserves at BlackRock, Lead Bank and BNY. Also launched on Ethereum, Solana and Base — [PrimeXBT](https://primexbt.com/news/coinbase-backed-ousd-stablecoin-launches-on-ethereum-solana-base-and-tempo/); [Crypto Briefing](https://cryptobriefing.com/tempo-integrates-open-usd-enterprise/) [Medium]
  - OUSD on Tempo: $424.5M on 30 Sep → $529.7M on 21 Oct — [DefiLlama OUSD](https://stablecoins.llama.fi/stablecoin/443) [High]
- DeFi TVL was $107M on 21 Oct (ATH) — [DefiLlama TVL API](https://api.llama.fi/v2/historicalChainTvl/Tempo) [High]
  - Top protocols: Morpho $66.0M, Sentora curator $65.6M (overlaps Morpho), Uniswap V4 $25.1M, Tempo Stablecoin DEX $15.8M — [DefiLlama protocols API](https://api.llama.fi/protocols) [High]
- Activity and fees:
  - DEX volume was $94.5M YTD, including $41M in September — [DefiLlama DEX API](https://api.llama.fi/overview/dexs/Tempo) [High]
  - Chain fees were ~$53K YTD, with DefiLlama showing ~$0 since August — [DefiLlama fees API](https://api.llama.fi/summary/fees/tempo?dataType=dailyFees) [High]
  - Dune counted 3.9M transactions and 177K addresses in the first 10 weeks. DefiLlama showed ~40K transactions and ~4.7K active addresses in a 24h window (date unclear) — [Dune Tempo](https://dune.com/blockchains/tempo); [DefiLlama chain page](https://defillama.com/chain/tempo) [Medium]
- Klarna announced KlarnaUSD on Tempo on 25 Nov 2025 for a 2026 mainnet launch — [The Block](https://www.theblock.co/news/markets/2025-11-25-bnpl-firm-klarna-announces-usd-stablecoin-on-stripe-paradigms-tempo-blockchain-to-cut-payment-costs-380365) [High]. KlarnaUSD does not appear among Tempo assets ≥$0.1M in DefiLlama.

#### MegaETH (USDm)
- Stablecoins: ATH **$811M on 7 May 2026** → **$18.2M** on 21 Oct — [DefiLlama stablecoin chart](https://stablecoins.llama.fi/stablecoincharts/MegaETH) [High]
  - USDm: ATH $562M on 3 May → $228M at end-June → $18M at end-July → $16.1M now — [DefiLlama USDm](https://stablecoins.llama.fi/stablecoin/342) [High]
  - USDe on MegaETH: $441M on 11 Jun → ~$0.1M by 21 Jul — [DefiLlama USDe](https://stablecoins.llama.fi/stablecoin/146) [High]
- TVL: ATH $246M on 12 May → $12.5M — [DefiLlama TVL API](https://api.llama.fi/v2/historicalChainTvl/MegaETH) [High]
- DEX volume peaked at $244M in May and was $14M for 1–21 October — [DefiLlama DEX API](https://api.llama.fi/overview/dexs/MegaETH) [High]

#### Kite AI
- DefiLlama tracks ~$0 of stablecoins on the KiteAI chain since 7 Jul 2026 — [DefiLlama stablecoin chart](https://stablecoins.llama.fi/stablecoincharts/KiteAI) [High]
- CoinGecko shows a headline that Kite halted Ethereum transfers after a security alert with no losses (~3 months ago). It also dates mainnet to "212 days ago", which would be around late March 2026 — [CoinGecko page](https://www.coingecko.com/en/coins/kite-ai) [Low]

#### Celo
- Stablecoins: $177.5M on 1 Jan 2026 → low $106.9M on 27 Jul → $112.4M on 21 Oct. The ATH was $341.2M in Sep 2024 — [DefiLlama stablecoin chart](https://stablecoins.llama.fi/stablecoincharts/Celo) [High]
  - Composition: USDT $83.8M, BRLA $28.7M, USDC $16.1M, USDm $13.7M — [DefiLlama stablecoins API](https://stablecoins.llama.fi/stablecoins?includePrices=false) [High]
- DeFi TVL is $13.7M — [DefiLlama TVL API](https://api.llama.fi/v2/historicalChainTvl/Celo) [High]
- A vendor-reported claim (≈Apr 2026) gives 840K DAU and >$65B of stablecoin volume since the L2 migration — [Bitget](https://www.bitget.com/news/detail/12560605349931) [Low]

#### Noble (Cosmos USDC issuance hub)
- Circle announced on 10 Sep 2026 that it is ending USDC on Noble:
  - New minting stopped on 13 Oct 2026.
  - The contract and CCTP routes pause on 12 Jan 2027, with redemptions from 13 Jan 2027.
  - Injective becomes the Cosmos USDC source.
  - Coinbase ended Noble USDC support on 17 Aug 2026.
  - Sources: [CoinPaprika](https://coinpaprika.com/news/circle-pulls-usdc-noble-forcing-cosmos/); [KuCoin](https://www.kucoin.com/news/insight/USDC/6ad2b649c31ba8000731dee5); [Crypto Briefing](https://cryptobriefing.com/coinbase-ends-usdc-noble-network-support/) [Medium]
- Stablecoins: ATH $815M on 21 Jul 2025 → $277.5M on 1 Jan 2026 → **$86.6M** on 21 Oct 2026 — [DefiLlama stablecoin chart](https://stablecoins.llama.fi/stablecoincharts/Noble) [High]

#### Codex (stablecoin L2)
- Stablecoins: $51.1M on 11 Apr 2026 → peak $53.2M on 21 Apr → **$4.7M** on 21 Oct. USDC alone fell from $51.0M a month earlier to $5.2M — [DefiLlama stablecoin chart](https://stablecoins.llama.fi/stablecoincharts/Codex); [DefiLlama stablecoins API](https://stablecoins.llama.fi/stablecoins?includePrices=false) [High]
- A competitor's guide says Codex rebranded toward "Codex FX", focused on off-chain FX — [Eco](https://eco.com/support/en/articles/13052727-what-is-codex-blockchain-2026-guide) [Low]

#### New exchange/fintech chains in 2026 (not stablechains in name, but competing for stablecoin float)
- **Robinhood Chain** (Arbitrum-based L2):
  - Public testnet 10 Feb 2026, public mainnet **1 Jul 2026**. Dollar liquidity comes from Paxos' USDG — [CoinDesk](https://www.coindesk.com/business/2026/07/01/robinhood-rolls-out-public-blockchain-as-it-expands-deeper-into-crypto); [ArbitrumDAO factsheet](https://forum.arbitrum.foundation/t/arbitrumdao-factsheet-robinhood-chain-mainnet-launch/31041) [High]
  - Stablecoins: $241M on 7 Jul → ATH $1,113M on 6 Oct → $1,087M (USDG $686.5M, USDe $362.6M) — [DefiLlama](https://stablecoins.llama.fi/stablecoincharts/Robinhood%20Chain) [High]
  - TVL is $1,146M — [DefiLlama TVL](https://api.llama.fi/v2/historicalChainTvl/Robinhood%20Chain) [High]
  - DEX volume is $111B YTD, starting in July — [DefiLlama DEX](https://api.llama.fi/overview/dexs/Robinhood%20Chain) [High]
  - Much of the early activity was memecoins — [CryptoTicker](https://cryptoticker.io/en/robinhood-chain-memecoins-explained/) [Medium]
- **X Layer (OKX):** stablecoins went from $33M on 1 Jan 2026 to an ATH of $2,093M on 9 Aug, and are $1,494M now (USDG $1,318.5M) — [DefiLlama](https://stablecoins.llama.fi/stablecoincharts/X%20Layer) [High]

#### Tron (incumbent)
- Stablecoins: $81.69B on 1 Jan 2026 → ATH **$95.03B on 10 Oct** → $94.14B on 21 Oct (+15.2% YTD, about +$12.4B). USDT is $92.53B and USDD $1.28B — [DefiLlama stablecoin chart](https://stablecoins.llama.fi/stablecoincharts/Tron); [DefiLlama stablecoins API](https://stablecoins.llama.fi/stablecoins?includePrices=false) [High]
- TRON DAO Q3 2026 figures, from [crypto.news, 19 Oct 2026](https://crypto.news/tron-handles-trillions-in-stablecoin-transfers-how-much-does-the-network-earn/) [Medium; self-reported]:
  - Stablecoin settlement of $2.21T ($24.05B a day).
  - **Network fees of $701.4M** (~$7.62M a day).
  - 1.10B transactions.
  - 4.41M daily active accounts (30-day average to 4 Oct).
  - Tron added $4.8B of stablecoins in the 90 days to 21 Sep, against $2.59B for the other nine top-10 chains combined.
- DefiLlama counts Tron chain fees far lower: $266M for 2026 YTD and ~$24M a month — [DefiLlama fees API](https://api.llama.fi/summary/fees/tron?dataType=dailyFees) [High]. That is a methodology gap against TRON DAO's ~$234M a month.
- On 29 Aug 2025 Tron cut its energy price by 60% (210 → 100 sun), and daily fee revenue fell from $13.9M to ~$5M — [TradingView/cryptonews](https://www.tradingview.com/news/cryptonews:313497305094b:0-tron-votes-to-slash-network-fees-60-to-defend-stablecoin-dominance/); [Blockworks](https://blockworks.com/news/tron-fee-gamble) [Medium]

#### Solana
- Stablecoins: $14.25B on 1 Jan 2026 → ATH $17.45B on 25 Sep → $15.93B on 21 Oct. The top assets are USDC $6.91B and USDT $2.69B — [DefiLlama stablecoin chart](https://stablecoins.llama.fi/stablecoincharts/Solana) [High]
- TVL fell from $8.16B to $5.98B — [DefiLlama TVL API](https://api.llama.fi/v2/historicalChainTvl/Solana) [High]
- Chain fees were $190.9M YTD ($27.7M over 30 days). App fees were $2.87B YTD — [DefiLlama fees API](https://api.llama.fi/summary/fees/solana?dataType=dailyFees); [DefiLlama app fees](https://api.llama.fi/overview/fees/Solana) [High]

### Inferences
- **Incentive-driven vs organic, Plasma (my estimate):**
  - About 43% of its stablecoins are USDe, a yield instrument. The Aug–Oct 2026 rebound in Plasma stablecoins (+$586M from the 12 Aug low) came almost entirely from USDe (+~$480M since end-July), while USDT on Plasma kept falling.
  - About 85% of DeFi TVL is a single lending market (Aave).
  - Directly payments-linked balances are small: roughly ~$392M in CEX wallets and $31M in Plasma One.
  - Organic payment activity is probably a small minority of balances. The token captures almost none of it, because USDT transfers are gas-free (2026 gas fees ~$73K).
- **Stable** is the clearest case of pre-deposit capital that never became usage. Roughly $2–2.6B was committed, yet ~$24M is on-chain ten months after TGE, and 2026 DEX volume was ~$8M.
- **MegaETH** shows the same pattern. Its USDm and USDe balances rose and fell within about 10 weeks around the April TGE.
- **Capital is migrating to chains without tradable tokens.** In five weeks Arc's stablecoin supply passed half of Plasma's, and its DeFi TVL ($532M) is roughly level with Plasma's ($572M). Tempo grew mostly through one consortium stablecoin (OUSD). Robinhood Chain and X Layer each passed $1B quickly.
- Arc's and Tempo's balances are also concentrated and partly launch-liquidity driven: Morpho plus Aave make up ~91% of Arc's TVL, and OUSD is ~73% of Tempo's stablecoins. Their "organic payments" share is unproven too.
- Noble's decline after Circle's exit shows the platform risk of issuer-dependent chains. Arc's rise is partly the mirror image of that decline.

### Gaps
- I did not find the cause of the Aug–Oct 2026 USDe inflow to Plasma (a new Ethena/Pendle/Aave incentive program?), or of MegaETH's July 2026 USDm/USDe exit. Search budget was exhausted.
- I found no reliable split of Plasma transactions into payments, DeFi and bots, and no Plasma One user or card-volume figure dated after its June launch.
- Tempo has no organic payments metric (merchant or Klarna volume). KlarnaUSD's live status is unverified.
- I have no Canton on-chain stablecoin metrics (Canton is not on DefiLlama), apart from the existence of a CC/USDCx pair.
- Arc and Tempo transaction and active-address counts for October 2026 come only from secondary or undated sources.

## Q4. Valuation comparison: MC and FDV relative to stablecoin supply, TVL and fees — stablechains vs Tron and Solana

### Takeaway
On a "dollars hosted" basis, XPL trades at a discount to Tron: FDV/stablecoins is ~0.6x against Tron's 0.33x MC (TRX has no locked supply). On fee capture, however, it is effectively unvalued-to-infinite, with FDV ~4,000x annualized gas fees against Tron's ~11x on TRON DAO's fee data or ~108x on DefiLlama's. STABLE is the outlier: an FDV of ~$2.7B on ~$20–24M of stablecoins is ~110–136x, roughly 400x Tron's ratio. Arc's private presale ($3B FDV) implies ~4x its stablecoin base and ~5.6x its TVL, which is between XPL and STABLE.

### Cited Findings
- All inputs are as of 21 Oct 2026:
  - Prices, MC and FDV: [CoinGecko API](https://api.coingecko.com/api/v3/coins/plasma).
  - Stablecoins: [DefiLlama chains endpoint](https://stablecoins.llama.fi/stablecoinchains).
  - TVL: [DefiLlama TVL API](https://api.llama.fi/v2/historicalChainTvl/Plasma).
  - Fees, annualized from trailing 30 days: [DefiLlama fees API](https://api.llama.fi/summary/fees/plasma?dataType=dailyFees) and [DefiLlama app fees](https://api.llama.fi/overview/fees/Plasma).
  - TRX MC: [CoinGecko](https://www.coingecko.com/en/coins/tron). TRON DAO fees: [crypto.news](https://crypto.news/tron-handles-trillions-in-stablecoin-transfers-how-much-does-the-network-earn/).
  - SOL MC is my calculation: $107.29 × ~589.55M circulating from [MetaMask](https://metamask.io/price/solana).
  - All ratios below are my calculations.

| Chain/token | Circ MC | FDV | Stablecoins | DeFi TVL | MC/Stables | FDV/Stables | FDV/TVL | Annualized chain fees | FDV/chain fees |
|---|---|---|---|---|---|---|---|---|---|
| Plasma XPL | $369M | $815M | $1,288M | $572M | 0.29x | 0.63x | 1.4x | ~$0.2M | ~4,200x |
| Stable STABLE | $486M | $2,701M | $19.9M ($23.8M alt.) | $28.5M | 20–24x | 113–136x | 95x | n/a (not tracked) | n/a |
| MegaETH MEGA | $52M | $464M | $18.2M | $12.5M | 2.9x | 25.5x | 37x | ~$0.85M | ~545x |
| Kite KITE | $293M | $1,224M | ~$0 | n/a | n/a | n/a | n/a | n/a | n/a |
| Celo CELO | $52M | $86M | $113.8M | $13.7M | 0.46x | 0.75x | 6.3x | ~$1.0M | ~85x |
| Canton CC | $4,276M | $4,276M | not tracked | not tracked | n/a | n/a | n/a | n/a | n/a |
| Arc (ARC presale) | none (not trading) | $3,000M | $755M | $532M | n/a | 3.97x | 5.6x | n/a | n/a |
| Tempo (equity $5B) | none (no token) | $5,000M (equity) | $724M | $107M | n/a | 6.9x | 47x | ~$0 | n/a |
| Tron TRX | $31,479M | $31,479M | $94,074M | $5,542M | 0.33x | 0.33x | 5.7x | ~$291M (DefiLlama) / ~$2.8B (TRON DAO) | 108x / 11x |
| Solana SOL | ~$63,250M | n/a | $15,640M | $5,978M | 4.0x | n/a | n/a | ~$337M | ~188x (MC) |

- Notes on the table:
  - Celo's chain fees are annualized from YTD, not trailing 30 days.
  - Tempo's "FDV" row is an equity valuation, not a token FDV.
- App-level fees (lending interest etc.) accrue to apps, not to the L1 token.
  - On that basis, FDV is ~16.7x Plasma's annualized app fees ($48.7M), ~352x Stable's ($7.7M) and ~42x Arc's ($71.8M, launch-inflated).
  - Sources: [DefiLlama app fees Plasma](https://api.llama.fi/overview/fees/Plasma); [Stable](https://api.llama.fi/overview/fees/Stable); [Arc](https://api.llama.fi/overview/fees/Arc) [High]
- Peak valuations (my calculations):
  - XPL at ATH: $1.68 × 1.8B circulating = ~$3.0B MC, ~$16.8B FDV, against ~$6.35B of peak stablecoins (FDV/stables ~2.6x).
  - XPL today: $0.37B MC and $0.81B FDV.
  - Sources: [CoinGecko API](https://api.coingecko.com/api/v3/coins/plasma); [DefiLlama](https://stablecoins.llama.fi/stablecoincharts/Plasma)
- Tron's fee data depends on the source: TRON DAO/Messari give ~$700M a quarter, while DefiLlama's adapter shows ~$24–32M a month — [crypto.news](https://crypto.news/tron-handles-trillions-in-stablecoin-transfers-how-much-does-the-network-earn/); [DefiLlama fees API](https://api.llama.fi/summary/fees/tron?dataType=dailyFees) [High; definitional conflict]

### Inferences
- The market now prices XPL roughly like a "Tron-lite" on deposits: FDV is 0.6x stablecoins against TRX at 0.33x. The difference is that Tron's stablecoins are sticky, payment-driven USDT that pays meaningful fees, while ~43% of Plasma's base is mercenary USDe. On fees XPL is still expensive; on hosted dollars it is cheap.
- STABLE's valuation is disconnected from on-chain fundamentals. An FDV of ~$2.7B against ~$24M of stablecoins and ~$8M of 2026 DEX volume is held up by the Tether/Bitfinex narrative, a small float (18%) and the deferred-unlock structure. It does not reflect usage, so it is vulnerable if the narrative fades or Coinbase listing demand disappoints.
- The ARC presale's $3B FDV against ~$0.76B of stablecoins (≈4x) sets a reference point well above where XPL trades (0.63x). Either institutions are paying a "Circle premium", or XPL/STABLE public prices imply a public ARC would list below presale. This is a key uncertainty for a future ARC TGE.
- Tron is the only chain in the set where token value is clearly backed by fees. Even there, the 2025 fee cut shows the pressure to cut fees to defend share against zero-fee stablechains.

### Gaps
- Stable's gas-fee revenue (USDT0) is not tracked by DefiLlama.
- Tempo's DefiLlama chain fees read ~$0 after August, which may be an adapter issue.
- Canton has no comparable stablecoin, TVL or fee data.
- Solana revenue definitions vary: one source cites 21Shares' H1 2026 network revenue of $141M, down 87.1% — [SQ Magazine/aggregated](https://sqmagazine.co.uk/solana-statistics/) [Low]

## Q5. Pre-TGE pipeline: funding, investors, valuation, points/airdrops, token confirmed vs rumored, expected TGE timing (Polymarket) and expected FDV

### Takeaway
The two heavyweight pipeline chains are run by public or near-public corporates and are deliberately tokenless or token-optional. **Arc** has a real token: ARC was presold at $0.30 for a $3B FDV, and all 10B were genesis-minted. But Circle has made no commitment to a public launch. PoS exploration is slated for 2027, and Polymarket prices only **9%** for an Arc token by 31 Dec 2026, 43% by 30 Jun 2027 and 68% by 31 Dec 2027. **Tempo** ($5B equity valuation) has no token and no public token signal. The second tier is fading or tokenless: Converge uses ENA, 1Money says it has no native token, Codex has shrunk, and Noble is being deprecated by Circle.

### Cited Findings

#### Arc (Circle) — token exists privately; public TGE unconfirmed [confidence the token eventually lists: Medium; by end-2026: Low]
- Presale details:
  - Announced with Q1 2026 results around 8–11 May 2026: **$222M for ~740M ARC at $0.30, a $3B FDV.**
  - a16z crypto led with $75M. Other buyers included BlackRock, Apollo Funds, ICE, ARK Invest, SBI Group and Standard Chartered Ventures.
  - Sources: [KuCoin News](https://www.kucoin.com/news/flash/circle-s-arc-secures-222m-pre-sale-network-valued-at-3b); [Quartz](https://qz.com/circle-arc-token-presale-222-million-blackrock-a16z-051126) [Medium]
  - CoinDesk's investor list also includes Bullish and Haun Ventures, describes ARC as a "native coordination asset" closer to ETH or SOL than to USDC, and notes the whitepaper was published on 11 May — [CoinDesk, 11 May 2026](https://www.coindesk.com/business/2026/05/11/circle-raises-usd222-million-for-arc-blockchain-token-sale-at-usd3-billion-valuation) [High]
- Lock-up and refund terms: presale buyers are locked for at least 1 year after the PoS or dPoS switch, with repayment rights if delivery or the transition is not done by 8 May 2028 — [Cointelegraph via TradingView](https://www.tradingview.com/news/cointelegraph:ad4cbe069094b:0-usdc-issuer-circle-raises-222m-in-arc-token-presale-valued-at-3b/); [KuCoin News](https://www.kucoin.com/news/flash/circle-s-arc-secures-222m-pre-sale-network-valued-at-3b) [Medium]
- Effect on Circle's results: Circle roughly doubled its FY "other revenue" guidance to $310–330M in Q2 2026, partly because of presale revenue recognition — [Yahoo Finance/Decrypt](https://finance.yahoo.com/news/arc-stablecoin-blockchain-usdc-issuer-150103906.html) [High]
- Mainnet and token status:
  - Public mainnet opened on 16 Sep 2026.
  - Validators: Circle, BlackRock, DTCC, Galaxy, ICE, Mastercard, MoneyGram, SBI, Standard Chartered, Sumitomo, Visa and Worldpay.
  - The network runs proof-of-authority on Malachite BFT, with PoS being explored for 2027.
  - The 10B ARC genesis mint is "not a commitment to publicly launch ARC".
  - Sources: [Yahoo Finance/Decrypt](https://finance.yahoo.com/news/arc-stablecoin-blockchain-usdc-issuer-150103906.html); [The Block](https://www.theblock.co/news/ecosystems/2026-09-16-circle-launches-arc-mainnet-with-blackrock-and-visa-among-validators-mints-10-billion-arc-tokens-415250) [High]
- **Polymarket "Will Arc launch a token by…?"** (read on 21 Oct 2026; resolution source x.com/arc):
  - 31 Dec 2026: **9%**.
  - 30 Jun 2027: **43%**.
  - 31 Dec 2027: **68%**.
  - Total volume $617,770.
  - Source: [Polymarket](https://polymarket.com/event/will-arc-launch-a-token-by) [High]
  - An earlier snapshot on 7 Sep 2026 read 13%, 43% and 89% for the same dates — [PredictMarketCap](https://predictmarketcap.com/events/will-arc-launch-a-token-by) [Medium]
- Airdrop and points: no airdrop has been confirmed. "Arc House" community points have been referenced by airdrop sites — [Cryptonomist](https://en.cryptonomist.ch/2026/09/17/arc-network-airdrop-guide/); [99airdrops](https://99airdrops.com/airdrops/arc/) [Low]
- Expected FDV: the only hard anchor is the $3B presale FDV. Retail price predictions of $0.25–0.90 per ARC ($2.5–9B FDV) are unsupported speculation — [CoinGabbar](https://www.coingabbar.com/en/price-prediction/arc-price-prediction-circle-arc-mainnet-launch-16-september-2026) [Low]

#### Tempo (Stripe + Paradigm) — no token [token in 2026: very low; long-term: speculative]
- Funding: a $500M Series A at a **$5B valuation** in Oct 2025, led by Thrive Capital and Greenoaks with Sequoia, Ribbit and SV Angel. Stripe and Paradigm did not put in capital — [Yahoo Finance/Fortune](https://finance.yahoo.com/news/exclusive-stripe-backed-blockchain-startup-161642558.html); [Cointelegraph](https://cointelegraph.com/news/tempo-stripe-blockchain-5b-valuation-funding-round) [High]
- I found no 2026 Tempo funding round in search. Stripe was valued at ~$159B in Feb 2026 — [Everstake](https://everstake.com/resources/blog/what-is-tempo-stripe-and-paradigms-stablecoin-payments-blockchain-explained) [Medium]
- Token status:
  - No native token, and no TGE announced as of July 2026 — [Everstake](https://everstake.com/resources/blog/what-is-tempo-stripe-and-paradigms-stablecoin-payments-blockchain-explained) [Medium]
  - A future move to permissionless validation "could eventually require a staked asset", but there is no commitment — [Datawallet](https://www.datawallet.com/crypto/tempo-explained) [Low; speculative]
  - Tempo's own OUSD launch post mentions no token — [Tempo blog](https://tempo.xyz/blog/ousd-is-live-on-tempo/) [High]
- Polymarket: I found no Tempo token market. The search returned only Polymarket's own POLY token speculation.

#### Converge (Ethena + Securitize) — no separate token [status: unverified]
- Announced in Mar 2025 as an institutional RWA chain targeting a Q2 2025 mainnet. Gas is paid in USDe/USDtb, and validators stake ENA — [CoinDesk, 16 Apr 2025](https://www.coindesk.com/tech/2025/04/16/ethena-securitize-target-q2-mainnet-launch-for-rwa-focused-blockchain-tap-arbitrum-celestia); [The Block](https://www.theblock.co/post/346665/ethena-securitize-launch-converge-new-institutional-grade-evm-tokenization); [Eco](https://eco.com/support/en/articles/15010654-what-is-converge-blockchain) [Medium]
- Converge does not appear in DefiLlama's stablecoin-by-chain list as of 21 Oct 2026 — [DefiLlama](https://stablecoins.llama.fi/stablecoinchains) [High]

#### 1Money Network — "no native token" [Medium]
- The CEO said in Mar 2025 that the L1 has no native token and flat fees, and the Aug 2025 testnet post repeated that the native token was eliminated — [The Block](https://www.theblock.co/news/business/2025-03-10-1money-ceo-brian-shroder-on-building-l1-for-stablecoins-with-no-native-token-and-flat-gas-fees-345455); [1Money blog](https://www.1money.com/blog/testnet-launch) [High]
- Conflicting signal: the explorer lists a "1Money Network Token (1MNT)" with 8,000,050,000 supply and 0 holders, created in Apr 2026 — [1Money explorer](https://www.1moneynetwork.com/explorer/token) [Low; unexplained]
- Other facts:
  - Mainnet is listed with chain ID 21210 — [Chainlist](https://chainlist.org/chain/21210)
  - 1Money announced an M0 issuance partnership on 27 Jan 2026 — [BusinessWire](https://www.businesswire.com/news/home/20260127522384/en/1Money-Partners-With-M0-to-Launch-1Money-Issuance)
  - It raised $20M — [Causeartist](https://www.causeartist.com/blog/1money-launches-with-20m-in-funding-to-revolutionize-stablecoin-payments) [Medium]

#### Codex — no token found
- Stablecoin L2 backed by Dragonfly. Mainnet went live on 24 Jun 2025 with USDC gas — [Eco](https://eco.com/support/en/articles/13052727-what-is-codex-blockchain-2026-guide) [Medium]
- Stablecoins collapsed to $4.7M (see Q3).

#### Noble — no token; USDC being deprecated by Circle (see Q3)
- One source says a standalone EVM L1 mainnet launched on 18 Mar 2026 — [KuCoin blog](https://www.kucoin.com/blog/noble-blockchain) [Low]

#### Others (adjacent, no token signal found in this research)
- Robinhood Chain (mainnet 1 Jul 2026) and OKX's X Layer — see Q3 — [CoinDesk](https://www.coindesk.com/business/2026/07/01/robinhood-rolls-out-public-blockchain-as-it-expands-deeper-into-crypto)
- Pharos, an RWA L1: stablecoins of $51.0M and TVL of $73.0M on 21 Oct 2026 — [DefiLlama](https://stablecoins.llama.fi/stablecoincharts/Pharos) [High]
- Bank consortium: 21 banks and asset managers, including Bank of America, Citi, Goldman Sachs, Wells Fargo and Fidelity, are reported to be formalising a USD stablecoin consortium targeting H1 2027 — [FinanceX Magazine](https://www.financexmagazine.com/post/the-week-stablecoins-stopped-being-a-side-project-how-september-2026-rebuilt-the-payments-stack) [Low; the search snippet's attribution was unclear]
- Pearl (PEARL), added to Coinbase's roadmap alongside STABLE, is a proof-of-useful-work AI L1, not a stablechain — [Crypto Briefing](https://cryptobriefing.com/coinbase-adds-axis-pearl-stable-roadmap/) [Medium]

### Inferences
- The pipeline that could restart the narrative effectively comes down to ARC. Its timing is gated by Circle's PoS work (2027), and the market prices a 2026 TGE at under 10%.
- If ARC lists, the presale anchor ($3B FDV) and Arc's growing USDC base give it a fundamentally stronger setup than XPL or STABLE had. Lock-ups keep presale supply off the market until at least a year after PoS.
- Tempo looks designed to stay tokenless. Its network effects (OUSD, Visa, Mastercard, Coinbase, Stripe, zerohash) accrue to Stripe's equity rather than to a token, so there is no likely token catalyst there in 2026–27.
- Smaller stablechains (Codex, Noble, 1Money, Converge) are losing relevance as issuers concentrate supply on their own chains: Circle on Arc, Stripe/Bridge on Tempo, Paxos/Robinhood on USDG chains.

### Gaps
- I could not confirm whether Converge's mainnet is live in 2026, or whether 1Money's mainnet is live and what 1MNT is.
- There is no pre-market (Hyperliquid or Aevo) quote for ARC. I found no Polymarket market for Tempo, Converge or 1Money tokens.
- I found no points programs for Tempo or 1Money.

## Q6. Narrative assessment: has the stablechain thesis delivered for token holders? Analyst views, and competition among Tether-aligned chains, Circle, Stripe and incumbents

### Takeaway
For token holders, no. The stablechain thesis delivered big pre-deposits and launch-day TVL in 2025, then mostly round-tripped:
- XPL is −95% from ATH and −51% in 2026, with stablecoins down 79% and TVL down 91% from peak.
- STABLE's chain is nearly empty (~$24M).
- MEGA is −79%.

The underlying "stablecoins grow" thesis did deliver, but the gains went to incumbents (Tron +$12.4B YTD), to issuer-owned chains without public tokens (Arc, Tempo) and to exchange/fintech chains (Robinhood Chain, X Layer). Research houses were bullish going in (Delphi, Messari, Galaxy's macro calls). I found no 2026 research-house post-mortem, so analyst conclusions on token value capture remain mostly implicit.

### Cited Findings
- **Delphi Digital:**
  - Published "Plasma: Taking Aim at a Trillion Dollar Opportunity" — [Delphi](https://members.delphidigital.io/reports/plasma-taking-aim-at-a-trillion-dollar-opportunity) and "The Case for Plasma One: Stablecoins Are Eating the World" — [Delphi](https://members.delphidigital.io/reports/the-case-for-plasma-one-stablecoins-are-eating-the-world) [Medium; paywalled, titles only]
  - Its Tempo piece highlights the enshrined Fee AMM, which lets fees be paid in any stablecoin and converted for validators, and warns that more chains mean more liquidity fragmentation — [Delphi on X](https://x.com/Delphi_Digital/article/2031063065744073128) [Medium]
  - A summary of Delphi-related material frames Arc, Codex and Tempo as "issuer-aligned & compliance-heavy; risk siloing usage", and neutrality (Plasma) as the possibly stronger foundation — [Delphi report page via search summary](https://members.delphidigital.io/reports/plasma-taking-aim-at-a-trillion-dollar-opportunity) [Low; attribution uncertain]
- **Messari:**
  - Published "The Rise of Stablechains" on 22 Aug 2025. Its Stable overview notes that validators can share USDT fee-vault income with delegators, which is meant to create STABLE demand. Its Plasma profile shows XPL at −88% over 1 year — [Messari Stable report](https://messari.io/report/understanding-stable-a-comprehensive-overview); [Messari Plasma](https://messari.io/project/plasma) [Medium]
- **Galaxy Research (Dec 2025):** predicted stablecoins would overtake ACH transaction volume in 2026, with 30–40% annual supply growth, and expected one or two dollar stablecoins to dominate. I found no Galaxy report specific to stablechain tokens — [Cointelegraph](https://cointelegraph.com/news/galaxy-stablecoins-ach-transaction-volume-2026) [High]
- **Blockworks** covered Tron's 60% fee cut as a "fee gamble" to defend stablecoin dominance — [Blockworks](https://blockworks.com/news/tron-fee-gamble) [Medium]. I found no Blockworks Research note on stablechain token value accrual.
- **The Block** mostly provided news coverage (Arc mainnet, MegaETH TGE, Klarna on Tempo). I found no Block Research valuation note.
- **Value-accrual critiques:**
  - "StableChain's product is Tether's dollar, but its native token does none of that", so value depends on governance, not usage — [Chain Tech Daily, 25 Jul 2026](https://chaintechdaily.com/2026/07/25/what-is-the-stable-token-for-the-value-accrual-test/) [Low; page returned 404 on fetch, content via search summary]
  - XPL's value case is "weaker and more contested": it is used for validator staking and incentives, not end-user gas — [Eco](https://eco.com/support/en/articles/11802920-what-is-plasma-xpl-stablecoin-l1-in-2026) [Low]
- **Competitive scorecard, stablecoins on 21 Oct 2026** — [DefiLlama](https://stablecoins.llama.fi/stablecoinchains) [High]:
  - Tether-aligned: Plasma $1.29B (−79% from peak) and Stable $0.02B (−97% from peak).
  - Circle: Arc $0.76B after 5 weeks.
  - Stripe: Tempo $0.72B after 7 months, ~73% OUSD.
  - Exchange/fintech: Robinhood Chain $1.05B, X Layer $1.50B.
  - Incumbents: Tron $94.1B (+15% YTD), Solana $15.6B (+12% YTD), Ethereum $143.2B.
- Validator and control models:
  - Arc and Tempo use permissioned institutional validators, and Plasma a trusted launch set. Stable runs DPoS with 11 validators — [Dwellir](https://www.dwellir.com/blog/stablechain-rpc-guide) [Medium]
  - A comparison piece matches chains to users: Plasma for retail/emerging-market payments, Arc for institutions/capital markets, Tempo for fintechs and merchants — [Chainstack](https://chainstack.com/stablecoin-l1-comparison/) [Low]
- Tron's response to the threat was to cut its energy price by 60% in Aug 2025. It still took the largest share of 2026 stablecoin growth among top-10 chains: +$4.8B in 90 days against +$2.59B for the other nine combined — [crypto.news](https://crypto.news/tron-handles-trillions-in-stablecoin-transfers-how-much-does-the-network-earn/); [TradingView/cryptonews](https://www.tradingview.com/news/cryptonews:313497305094b:0-tron-votes-to-slash-network-fees-60-to-defend-stablecoin-dominance/) [Medium]
- Issuer-chain risk cuts both ways: Circle is withdrawing USDC from Noble, with minting stopped on 13 Oct 2026 — [CoinPaprika](https://coinpaprika.com/news/circle-pulls-usdc-noble-forcing-cosmos/) [Medium]

### Inferences
- The thesis "stablecoin supply grows, so stablechain tokens accrue value" failed in 2026 for three structural reasons:
  - The flagship apps make payments gas-free or charge gas in stablecoins, so the native token does not capture flows.
  - TVL was rented with token incentives and pre-deposit yield, and left when emissions became worth less.
  - Heavy unlock calendars hit thin, declining fundamentals.
- Within the Tether camp, Tether's own distribution (USDT0 everywhere, Tron's entrenched rails) appears to compete with Plasma and Stable rather than funnel to them. USDT on Plasma (~$0.7B) is <1% of Tron's USDT ($92.5B).
- Circle (Arc) and Stripe (Tempo) are winning share of new institutional and fintech flows by controlling issuance (USDC, OUSD/Bridge) and distribution (Visa, Mastercard, Coinbase). They have not offered public tokens yet, which forces speculative capital either to wait for ARC or to buy weaker proxies.
- Arc's genuinely strong start (~$0.76B stablecoins, ~$0.53B TVL in 5 weeks) is the best evidence that the demand exists. The bottleneck is token design and access, not the stablecoin market.

### Gaps
- I found no 2026 Messari, Delphi, Galaxy, Blockworks Research or The Block Research report that explicitly reviews stablechain token performance. The pieces found are 2025 bullish theses, macro predictions or news. A follow-up search would be needed once the web-search budget is restored.

## Q7. Implications for capital flows into stablechain tokens and remaining upside of the sub-narrative; catalysts that could restart it

### Takeaway
Speculative capital in stablechain tokens has shrunk sharply.
- XPL went from ~$3.0B circulating MC (~$16.8B FDV) at its Sept 2025 ATH to ~$0.37B MC ($0.81B FDV) now.
- Together, XPL and STABLE are ~$0.86B circulating MC and ~$3.5B FDV.

At the same time, "real" stablecoin capital keeps flowing to tokenless issuer chains and to Tron. The remaining upside depends on a few discrete catalysts: a public ARC TGE (Polymarket: 9% in 2026, 43% by mid-2027), STABLE's Coinbase listing, and Plasma activating staking and delegation. Supply headwinds dominate the next 6 months: XPL adds ~30% to its float, and KITE unlocks 27% of float on 3 Nov. The base case is that the sub-narrative stays dormant until ARC, or a first-party Tether or Stripe token event, gives investors a credible way to own a winning stablechain.

### Cited Findings
- Capital lost and remaining:
  - XPL at its Sept 2025 ATH: $1.68 × 1.8B circulating ≈ $3.0B MC and $16.8B FDV, against $369M MC and $815M FDV now — [CoinGecko API](https://api.coingecko.com/api/v3/coins/plasma) [High; MC/FDV at ATH are my calculations]
  - STABLE: $486M MC and $2.7B FDV — [CoinGecko API](https://api.coingecko.com/api/v3/coins/stable-2) [High]
- Primary capital raised by the leading stablechain projects:
  - Arc presale, May 2026: $222M at $3B FDV — [CoinDesk](https://www.coindesk.com/business/2026/05/11/circle-raises-usd222-million-for-arc-blockchain-token-sale-at-usd3-billion-valuation) [High]
  - Tempo equity, Oct 2025: $500M at $5B — [Yahoo Finance/Fortune](https://finance.yahoo.com/news/exclusive-stripe-backed-blockchain-startup-161642558.html) [High]
  - Stable seed: $28M — [Bankless](https://www.bankless.com/read/news/stablechain-mainnet-launches-with-stable-token) [High]
- Dated supply catalysts over the next 6 months:
  - XPL: 227.8M on the 25th of every month (Oct 2026 – Mar 2027), ~1.37B in total — [CryptoTicker](https://cryptoticker.io/en/plasma-xpl-unlock-monthly-schedule/) [Medium]
  - KITE: 640M on 3 Nov 2026 — [CoinGecko](https://www.coingecko.com/en/coins/kite-ai) [Medium]
  - STABLE: nothing before 8 Dec 2027 if the Universal Lock is in force, with a $0.025 VWAP gate — [KuCoin blog](https://www.kucoin.com/blog/stable-whitepaper-update-82-of-stable-supply-enters-universal-lock-with-unlocks-through-2029) [Medium]
- Potential demand and narrative catalysts:
  - STABLE on Coinbase's listing roadmap (19 Oct 2026) — [Crypto Briefing](https://cryptobriefing.com/coinbase-adds-axis-pearl-stable-roadmap/) [Medium]
  - ARC TGE odds of 9%, 43% and 68% for end-2026, mid-2027 and end-2027 — [Polymarket](https://polymarket.com/event/will-arc-launch-a-token-by) [High]
  - Arc's PoS exploration in 2027 — [The Block](https://www.theblock.co/news/ecosystems/2026-09-16-circle-launches-arc-mainnet-with-blackrock-and-visa-among-validators-mints-10-billion-arc-tokens-415250) [High]
  - Plasma staking, delegation and 5% inflation, with no fixed date — [Plasma docs](https://www.plasma.org/docs/get-started/xpl/tokenomics) [High]
  - Plasma One adoption — [BusinessWire](https://www.businesswire.com/news/home/20260619440985/en/Plasma-One-Launches-to-Herald-a-New-Era-of-Stablecoin-Banking) [High]
  - DTCC tokenization on Canton (pilot reported 15 Jul 2026, commercial service in Oct 2026) — [Phemex](https://phemex.com/academy/canton-price-analysis-dtcc-tokenization-pilot); [CryptoTicker](https://cryptoticker.io/en/dtcc-tokenization-canton-launch/) [Low–Medium; secondary]
  - Circle and DTCC on Arc from H2 2027 — [The Block](https://www.theblock.co/news/ecosystems/2026-09-16-circle-launches-arc-mainnet-with-blackrock-and-visa-among-validators-mints-10-billion-arc-tokens-415250) [High]
  - Noble's USDC shutdown on 12 Jan 2027, a migration flow toward Injective and Arc — [KuCoin](https://www.kucoin.com/news/insight/USDC/6ad2b649c31ba8000731dee5) [Medium]
- CC rose ~27% after DTCC revealed its tokenization plans on Canton in Dec 2025, an example of how institutional-adoption headlines can move these tokens — [CoinMarketCap Academy](https://coinmarketcap.com/academy/article/canton-coin-token-surges-dtcc-tokenization-plans) [Medium]

### Inferences
- **Capital-flow read:** stablechain tokens have not been a 2026 destination for net new speculative capital. The cohort's 2026 returns trail BTC, ETH, SOL and TRX, apart from STABLE's rebound off its lows. On-chain dollars left the TGE'd chains as incentives decayed, while new dollars (USDC on Arc, OUSD on Tempo, USDG on Robinhood Chain and X Layer, USDT on Tron) went to chains whose upside accrues to Circle, Stripe, Robinhood, OKX or TRX holders.
- **Remaining upside, scenario view (my judgment):**
  - **Bull case (low–medium probability within 12 months):** Circle commits to a public ARC distribution or airdrop for the 2027 PoS transition. ARC lists near or above its $0.30 presale ($3B+ FDV) on a ~$1B+ USDC base. That would re-rate the "blue-chip stablechain" category, probably benefiting XPL and STABLE only briefly unless their own fundamentals turn.
  - **Base case:** no ARC or Tempo token before mid-2027. XPL keeps absorbing ~228M tokens a month. STABLE trades on listing headlines and the $0.025 VWAP gate. The sub-narrative stays dormant.
  - **Bear case:** USDe-driven balances leave Plasma again, as happened in 2026, and Tron and issuer chains keep taking share. XPL tests or breaks its $0.060 ATL during the unlock months, and STABLE's FDV compresses toward fundamentals: ~$24M of stablecoins, no meaningful fees.
- **What would change the assessment:**
  - Evidence of fee-sharing or buybacks funded by stablecoin fees: Stable's USDT fee vault to delegators, Plasma burns at scale.
  - Sustained growth of USDT (not USDe) on Plasma.
  - Plasma One user and volume disclosures.
  - An official ARC TGE date.
  - Any Tempo token or staking announcement.

### Gaps
- I found no flow data (exchange net flows, ETF/treasury holdings, whale accumulation) for XPL or STABLE in 2026.
- I found no sell-side or research-house price targets.
- There is no Polymarket or pre-market pricing for a Tempo token or for Plasma staking timing.
- Several checks could not be done because the session's web-search budget ran out. Re-run searches once it is restored:
  - drivers of the Aug–Oct 2026 USDe inflow to Plasma;
  - MegaETH's July 2026 USDm exit;
  - Converge and 1Money mainnet status;
  - Kite mainnet date;
  - the driver of STABLE's May 2026 ATH.
