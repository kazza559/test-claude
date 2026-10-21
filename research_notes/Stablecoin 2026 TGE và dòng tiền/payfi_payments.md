# PayFi, stablecoin neobanks/cards, wallets and agentic (x402) payment tokens: project fact base as of 21 Oct 2026

Scope: payment-related stablecoin tokens that TGE'd in late 2025 to 2026 (and older payment tokens, for comparison), plus the pre-TGE pipeline and equity-only infrastructure as capital-flow context. Window: 1 Jan to 21 Oct 2026.

Research constraint: the shared web-search budget ran out partway through this task. Coverage after that point came from direct fetches of URLs already found and from structured data APIs: CoinGecko, DefiLlama and Polymarket. The items this affected are listed under Gaps.

## 1. Token-by-token performance after TGE: prices, circulating MC vs FDV, ATH, airdrops and unlocks

### Takeaway
Nearly every payment, neobank or x402 token that TGE'd between Sep 2025 and Feb 2026 is 85–99% below its ATH as of 21 Oct 2026:
- XPL: -95%
- AVICI: -96.5%
- TRIA: -95%
- OOB: -98.8%
- PING: -99.4%

That is far worse than BTC (-4.7% YTD). The median 2026 YTD return across 17 payment tokens with full-year data is about -50%. The notable 2026 gainers are:
- HUMA: +24% YTD
- KITE: +36% YTD
- ETHFI: +5% YTD, now essentially fully unlocked

The heaviest supply overhang is in two places:
- **XPL:** circulating supply is up 119% YTD, including a +63% jump in a single day on 26 Sep 2026.
- **HUMA:** the first team/investor unlock falls on 26 Nov 2026.

### Cited Findings

#### Data notes and benchmarks
- **How the figures were pulled.**
  - "Now" prices, circulating MC and FDV come from the CoinGecko public API (/coins/markets), pulled 21 Oct 2026 between 13:17 and 13:28 UTC.
  - The 1 Jan 2026 prices and the 2026 highs and lows are daily closes from /coins/{id}/market_chart?days=365. That window runs from 22 Oct 2025 to 21 Oct 2026.
  - "First CoinGecko daily price" means the first daily close in that window. I use it as a proxy for the listing price.
  - Implied FDVs are my own calculation: price × total supply.
  - Circulating-supply paths are also my own calculation: market cap ÷ price, per day.
  - Sources: [CoinGecko API markets endpoint](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=huma-finance,plasma,ether-fi,avici,tria,oobit-2,kite-2,ping,payai-network-2); [CoinGecko market_chart (example: XPL)](https://api.coingecko.com/api/v3/coins/plasma/market_chart?vs_currency=usd&days=365&interval=daily)
- **Benchmarks, 21 Oct 2026.**
  - BTC: $83,431. It was $87,575 on 1 Jan 2026, so -4.7% YTD. The 2026 low was $58,566 (1 Jul) and the high $96,899 (15 Jan).
  - ETH: $2,468, -16.9% YTD. The 2026 low was $1,566 (26 Jun).
  - SOL: $106.6, -14.4% YTD. The 2026 low was $62.18 (7 Jun).
  - Sources: [CoinGecko BTC](https://www.coingecko.com/en/coins/bitcoin); [CoinGecko ETH](https://www.coingecko.com/en/coins/ethereum); [CoinGecko SOL](https://www.coingecko.com/en/coins/solana)
- **Total USD stablecoin supply.** Supply was roughly flat through 2026, after growing 49% in 2025. Source: [DefiLlama stablecoins](https://defillama.com/stablecoins) (API: https://stablecoins.llama.fi/stablecoincharts/all)

  | Date | Supply |
  |---|---|
  | 1 Jan 2025 | $203.2B |
  | 1 Oct 2025 | $296.0B |
  | 1 Jan 2026 | $303.7B |
  | 1 Apr 2026 | $309.2B |
  | 1 Jul 2026 | $303.4B |
  | 1 Oct 2026 | $305.8B |
  | 21 Oct 2026 | $303.4B |

- **CoinGecko sector caps, 21 Oct 2026.**
  - "Neobank": $2.90B. Most of it is MNT ($1.81B), ETHFI ($0.70B) and XPL ($0.37B). Source: [CoinGecko Neobank category](https://www.coingecko.com/en/categories/neobank)
  - "Crypto Card Issuer": $3.80B. Most of it is CRO ($2.97B) and NEXO ($0.82B). Source: [CoinGecko Crypto Card Issuer](https://www.coingecko.com/en/categories/crypto-card-issuer)
  - "Payment Solutions": $2.14B. Source: [CoinGecko Payment Solutions](https://www.coingecko.com/en/categories/payment-solutions)
  - "x402 Ecosystem": $10.56B. LINK alone accounts for $9.58B, so the headline overstates "x402" tokens. Source: [CoinGecko x402 Ecosystem](https://www.coingecko.com/en/categories/x402-ecosystem)
  - "AI Agents": $3.73B.
- **2026 YTD returns.** These are 1 Jan to 21 Oct 2026, from CoinGecko daily closes. The median of these 17 tokens is -49.8%. Pages for each token are linked in the source list below the summary table.

  | Token | YTD |
  |---|---|
  | KITE | +36.4% |
  | HUMA | +24.3% |
  | WLD | +21.2% |
  | ETHFI | +4.9% |
  | ZBCN | +0.2% |
  | GNO | -10.7% |
  | ACH | -25.4% |
  | PAYAI | -32.4% |
  | XPL | -49.8% |
  | REQ | -50.3% |
  | PUNDIX | -56.5% |
  | OOB | -59.5% |
  | LAYER | -60.1% |
  | TEL (legacy) | -62.3% |
  | KTA | -66.4% |
  | AVICI | -88.9% |
  | PING | -89.4% |

#### Summary table (CoinGecko, 21 Oct 2026, unless noted)

| Token (project) | TGE / first trade | Sale price and FDV | First CG daily price → implied FDV | ATH (date) → implied FDV | Price 21 Oct 26 | Circulating MC | FDV | vs sale or first price | vs ATH | YTD | Circulating % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| HUMA (Huma Finance) | 26 May 2025 (ATH set on TGE day) | n/a | outside window | $0.1156 (26 May 25) → ~$1.16B | $0.0307 | $53.3M | $307.4M | n/a | -73.4% | +24.3% | 17.3% (1.733B of 10B) |
| XPL (Plasma / Plasma One) | Sep 2025 (ATH 27 Sep 25) | public sale at $500M valuation ($50M raised) → $0.05/XPL | outside window | $1.68 (27 Sep 25) → ~$16.8B | $0.0816 | $370.0M | $816.1M | +63% vs sale | -95.1% | -49.8% | 45.3% (4.53B of 10B) |
| ETHFI (ether.fi, incl. Cash) | Mar 2024 | – | – | $8.53 (27 Mar 24) | $0.724 | $698.3M | $698.3M | – | -91.5% | +4.9% | ~100% of 965M total (1B max) |
| AVICI (Avici) | MetaDAO ICO, Oct 2025 | $0.35; ~$4.5M FDV; $3.5M raised | $0.752 (22 Oct 25, first in window) | $7.56 (26 Nov 25) → ~$97.5M | $0.265 | $3.42M | $3.42M | -24% vs ICO | -96.5% | -88.9% | 100% (12.9M) |
| TRIA (Tria) | 3 Feb 2026 | none found | $0.0157 → ~$157M (MC ~$34M) | $0.0500 (15 May 26) → ~$500M | $0.00249 | $5.35M | $24.8M | -84% | -95.0% | n/a | 21.6% (2.158B of 10B) |
| OOB (Oobit) | 12 Nov 2025 (Kraken) | VCI Global $100M token-treasury deal | $0.736 → ~$730M | $0.736 (12 Nov 25) | $0.00895 | $5.18M | $8.86M | -98.8% | -98.8% | -59.5% | 58.5% (579M of 990M) |
| KITE (Kite AI) | 3 Nov 2025 (first CG price) | n/a | $0.118 → ~$1.18B | $0.3197 (6 Mar 26) → ~$3.2B | $0.1226 | $293.2M | $1,226M | +3.7% | -61.7% | +36.4% | 23.9% (2.39B of 10B) |
| PING (x402 mint token) | ~24 Oct 2025 | n/a | $0.0341 → ~$34M | $0.0786 (25 Oct 25) → ~$79M | $0.000447 | $0.45M | $0.45M | -98.7% | -99.4% | -89.4% | 100% |
| PAYAI (PayAI Network) | CG series from 19 Nov 2025 | n/a | $0.0124 | $0.01895 (21 Dec 25) → ~$19M | $0.00813 | $7.98M | $7.98M | -34% | -57% | -32.4% | 100% |
| TEL (Telcoin, new 18-decimal token) | migration from 24 Sep 2026 | – | $0.00165 (24 Sep 26) | $0.00248 (28 Sep 26) | $0.001485 | CG does not populate it (~$140M inferred from legacy supply) | $148.6M | -10% | -40% | legacy TEL -62.3% | ~95% (legacy data) |
| ACH (Alchemy Pay) | 2020 | – | – | $0.1987 (6 Aug 21) | $0.00558 | CG does not populate it ($73.0M on 1 Jan 26) | $85.6M* | – | -97.2% | -25.4% | unreliable* |
| REQ (Request) | 2017 | – | – | $1.059 (5 Jan 18) | $0.0514 | $41.0M | $51.4M | – | -95.1% | -50.3% | 80% |
| PUNDIX (Pundi X) | older | – | – | – | $0.1015 | $26.2M | $26.2M | – | – | -56.5% | ~100% |
| GNO (Gnosis / Gnosis Pay) | 2017 | – | – | $644 (8 Nov 21) | $114.27 | $301.6M | $342.8M | – | -82.3% | -10.7% | 88% |
| ZBCN (Zebec, PayFi) | older | – | – | $0.0070 (29 May 25) | $0.00241 | $240.8M | $240.8M | – | -65.6% | +0.2% | ~100% |
| LAYER (Solayer / Emerald card) | 2025 | – | – | $3.39 (4 May 25) | $0.0672 | $14.1M | $67.2M | – | -98.0% | -60.1% | 21% |
| WLD (World) | 2023 | – | – | $11.74 (9 Mar 24) | $0.586 | $2.24B | $5.86B | – | -95.0% | +21.2% | 38% |
| STABLE (Stable chain; context only) | ~8 Dec 2025 | – | $0.0268 → ~$2.68B | $0.0432 (14 May 26) | $0.0270 | $485.7M | $2.70B | +0.7% | -37.6% | +94.7% | 18% |
| UP (Superform; CG "neobank" tag) | 10 Feb 2026 | – | $0.0623 | $0.2877 (13 May 26) | $0.0581 | $14.0M | $58.1M | -6.9% | -79.8% | n/a | ~24% |
| KTA (Keeta, payments L1) | 2025 | – | – | $1.68 (9 Jun 25) | $0.0713 | $44.4M | $71.3M | – | -95.8% | -66.4% | 62% |

\*ACH: CoinGecko reports a total supply of 15.35B, which conflicts with ACH's historical 10B maximum. Its circulating-supply field has read 0 since May 2026, so the FDV and supply figures are unreliable.

Row sources:
- [CoinGecko HUMA](https://www.coingecko.com/en/coins/huma-finance)
- [CoinGecko XPL](https://www.coingecko.com/en/coins/plasma)
- [CoinGecko ETHFI](https://www.coingecko.com/en/coins/ether-fi)
- [CoinGecko AVICI](https://www.coingecko.com/en/coins/avici)
- [CoinGecko TRIA](https://www.coingecko.com/en/coins/tria)
- [CoinGecko OOB](https://www.coingecko.com/en/coins/oobit-2)
- [CoinGecko KITE](https://www.coingecko.com/en/coins/kite-2)
- [CoinGecko PING](https://www.coingecko.com/en/coins/ping)
- [CoinGecko PAYAI](https://www.coingecko.com/en/coins/payai-network-2)
- [CoinGecko TEL (new)](https://www.coingecko.com/en/coins/telcoin-2); [CoinGecko Telcoin (legacy)](https://www.coingecko.com/en/coins/telcoin)
- [CoinGecko ACH](https://www.coingecko.com/en/coins/alchemy-pay)
- [CoinGecko REQ](https://www.coingecko.com/en/coins/request-network)
- [CoinGecko PUNDIX](https://www.coingecko.com/en/coins/pundi-x-2)
- [CoinGecko GNO](https://www.coingecko.com/en/coins/gnosis)
- [CoinGecko ZBCN](https://www.coingecko.com/en/coins/zebec-network)
- [CoinGecko LAYER](https://www.coingecko.com/en/coins/solayer)
- [CoinGecko WLD](https://www.coingecko.com/en/coins/worldcoin-wld)
- [CoinGecko STABLE](https://www.coingecko.com/en/coins/stable-2)
- [CoinGecko UP](https://www.coingecko.com/en/coins/superform)
- [CoinGecko KTA](https://www.coingecko.com/en/coins/keeta)

Sale, ICO and listing details are cited in the project bullets below.

#### Project details: PayFi and credit

**Huma Finance (HUMA)**
- **2026 price path.**
  - 1 Jan: $0.0246.
  - Daily-close low: $0.0129 (3 Apr 2026). The intraday ATL was $0.01108 on 26 Feb 2026.
  - 2026 high: $0.0355 (5 Oct 2026), 139% above the April low. The current price is 13.8% below that high.
  - 30-day change: +24.8%.
  - Source: [CoinGecko HUMA](https://www.coingecko.com/en/coins/huma-finance)
- **Supply and staking.** Circulating supply held at exactly 1,733,333,333 every day of H1 2026, with no unlock. Net staked HUMA rose from 268.2M to 523.1M, which took the staked share of the float from 15.5% to 30.2%. Gross H1 staking was 380.9M against 126.0M unstaked. Q2 2026 net staking was negative, about -4%. Source: [Blockworks Advisory, Huma H1 2026 report](https://blockworks.com/api/investor-report/huma-finance-protocol-report-h1-2026/pdf)
- **Unlock extension.** On 17 Apr 2026, Huma announced that the team, advisors and major investors would extend their initial unlock by six months. The first unlock moved from 26 May 2026 to 26 Nov 2026. Source: [Tokenomist weekly unlock digest, May 25–31, 2026](https://tokenomist.ai/research/weekly-unlock-digest-may-25-31-2026-humas-lockup-extension). I saw this content in a search snippet; the page returned 403 when fetched directly.
- **Unlock schedule, conflicting data.**
  - Tokenomics.com, as of Jul 2026, listed an unlock of 157.11M HUMA (1.6% of total supply) on 26 Aug 2026. It also called 26 Nov 2026 the largest upcoming unlock, "13.4% of market cap" worth of tokens.
  - CoinGecko shows circulating supply rising only from 1.733B to 1.739B by 21 Oct 2026, so the August unlock either is not reflected or did not happen.
  - Sources: [Tokenomics.com HUMA unlocks](https://app.tokenomics.com/tokenomics/huma-finance/unlocks); contradicted in part by [CoinGecko HUMA](https://www.coingecko.com/en/coins/huma-finance)
- **Circulating supply, conflicting data.** CoinMarketCap lists about 3.26B HUMA circulating, against 1.733B at CoinGecko, Tokenomist and Blockworks. Source: [CoinMarketCap HUMA](https://coinmarketcap.com/currencies/huma-finance/)

**Zebec (ZBCN)**
- PayFi/payroll and card token. ATH $0.0070 (29 May 2025). 2026 high $0.0038 (28 Apr); 2026 low $0.00157 (13 Aug). Flat YTD at +0.2%; about 100% circulating. Source: [CoinGecko ZBCN](https://www.coingecko.com/en/coins/zebec-network)

**Request Network (REQ)**
- 2026 low $0.0485 (30 Jun). Down 50% YTD. Source: [CoinGecko REQ](https://www.coingecko.com/en/coins/request-network)

**Alchemy Pay (ACH)**
- 2026 high $0.01324 (25 Jan); 2026 low $0.00409 (25 Jul). Source: [CoinGecko ACH](https://www.coingecko.com/en/coins/alchemy-pay)

**Pundi X (PUNDIX)**
- 2026 low $0.073 (17 Aug). Source: [CoinGecko PUNDIX](https://www.coingecko.com/en/coins/pundi-x-2)

**Telcoin (TEL)**
- **Token migration.** The legacy two-decimal TEL is moving to a new 18-decimal TEL, called "TEL3" during the transition.
  - Starts 24 Sep 2026; converts 1:1.
  - One-way, with a 12-month primary window and a 12-month extended period.
  - Same contract address planned on Ethereum, Polygon and Base.
  - Max supply 100B. The approved 2026 "Year 3" allocation authorizes 900M TEL.
  - Source: [Securities.io, updated 5 Sep 2026](https://www.securities.io/investing-in-telcoin-tel-everything-you-need-to-know-2/)
- **Network and ownership.** Telcoin Network mainnet was not live as of 5 Sep 2026 because the validator quorum had not been reached. TEL confers no ownership in Telcoin Inc. or Telcoin Digital Asset Bank, and no claim on eUSD reserves. Source: [Securities.io](https://www.securities.io/investing-in-telcoin-tel-everything-you-need-to-know-2/)
- **Legacy TEL prices.** 1 Jan 2026: $0.003916 (MC $372.3M). 2026 low: $0.00140 (18 Aug). 365-day high: $0.00673 (19 Nov 2025). Source: [CoinGecko Telcoin (legacy)](https://www.coingecko.com/en/coins/telcoin)
- **New TEL.** The new token is about 40% below its post-migration high of $0.00248 (28 Sep 2026). Source: [CoinGecko TEL (new)](https://www.coingecko.com/en/coins/telcoin-2)

#### Project details: stablecoin neobanks and card programs

**Plasma (XPL) / Plasma One**
- **Funding.** The XPL public sale raised $50M (per CryptoRank) at a $500M valuation, led by Bitfinex and Framework. Earlier rounds raised $24M. Source: [Yahoo Finance, Plasma One announcement, 22 Sep 2025](https://finance.yahoo.com/news/plasma-launches-revolutionary-usdt-native-172446155.html)
- **Price extremes.** ATL $0.0601 (10 Jun 2026). 2026 high $0.208 (7 Jan). Source: [CoinGecko XPL](https://www.coingecko.com/en/coins/plasma)
- **Circulating supply.** The table below is derived from [CoinGecko XPL market_chart](https://api.coingecko.com/api/v3/coins/plasma/market_chart?vs_currency=usd&days=365&interval=daily). About 89M XPL was added on roughly the 25th to 27th of each month, and about 131M per month in Mar–May 2026. On 26 Sep 2026 a single step added 1.755B (+63%).

  | Date | Circulating XPL |
  |---|---|
  | 22 Oct 2025 | 1.80B |
  | 1 Jan 2026 | 2.07B |
  | 25 Sep 2026 | 2.78B |
  | 26 Sep 2026 | 4.53B |

- **Cashback in XPL.** A third-party guide says Plasma One cashback of 2–4%, depending on tier, is paid in XPL. Source: [blocmates](https://www.blocmates.com/articles/why-use-the-plasma-card-features-benefits-explained)

**ether.fi (ETHFI)**
- **Supply.** 965.35M circulating, equal to total supply. Circulating rose from 653M (1 Jan 2026) to 965M (+48%) through monthly steps on the 17th or 18th. That implies essentially all supply is now unlocked. Derived from [CoinGecko ETHFI](https://www.coingecko.com/en/coins/ether-fi)
- **Price.** ATL $0.2665 (5 Jun 2026); the price is 171% above it now. Source: [CoinGecko ETHFI](https://www.coingecko.com/en/coins/ether-fi)
- **Buybacks, conflicting data.**
  - A Feb 2026 write-up describes the buyback design as 25% of monthly revenue plus 100% of withdrawal fees weekly. Source: [Tokenomics.com](https://tokenomics.com/articles/etherfi-tokenomics-how-the-dual-buyback-engine-returns-16-24m-to-ethfi-stakers)
  - A DefiLlama Pro dashboard says buybacks fell from about 13–16% of monthly gross revenue (Nov–Dec 2025) to about $0 in May–Jul 2026, even though the DAO passed a $50M buyback program in Oct 2025. I could not verify this against a primary source. Source: [DefiLlama dashboard](https://defillama.com/pro/ethfi-follow-the-money-ms7xy3)

**Avici (AVICI)**
- **MetaDAO ICO.** Price $0.35; $3.5M raised; 10M AVICI offered; pre-valuation $4.51M. Launch was reported on 14 Oct 2025 and the sale concluded around 18 Oct 2025. A Substack analysis said the sale drew "tens of millions" in deposits; that is a single source. Source: [ICO Drops](https://icodrops.com/avici)
- **Supply and price.** The 12.9M supply is fully circulating; it stepped from 10M to 12.9M on 26 Oct 2025. The ATH of $7.56 (26 Nov 2025) was 21.6x the ICO price. On 1 Jan 2026 the price was $2.39 (MC $30.9M), and the 2026 high was $4.61 (12 Jan). The ATL was $0.2175 on 28 Aug 2026, the day of the hack. Source: [CoinGecko AVICI](https://www.coingecko.com/en/coins/avici)
- **Hack, 28 Aug 2026.** Source: [Tech Insider, 31 Aug 2026](https://tech-insider.org/?p=18646)
  - **Cause:** a privilege-escalation bug in an outdated Solana card-collateral contract linked to the card issuer Rain.
  - **Losses:** $500,859.22 in confirmed card-balance losses by Avici's own reconciliation; the on-chain laundering trail traced by others is about $1–1.1M.
  - **Response:** 1,685 accounts affected, all to be refunded automatically.
  - **Token impact:** AVICI fell as much as 49% intraday; other outlets reported 27–40%.

**Tria (TRIA)**
- **TGE.** First public trading on 3 Feb 2026, with Binance Alpha as the initial platform. Source: [MEXC News](https://www.mexc.com/news/623032). I saw this in a search snippet; the page returned 410 on a later fetch. CoinGecko's first price, on 3 Feb 2026, corroborates the date.
- **Tokenomics.** Source: [Tria Medium, "Tria Tokenomics"](https://usetria.medium.com/tria-tokenomics-3f4773d417d3), via search snippet; the page returned 403 when fetched.
  - 10B supply, no inflation.
  - Genesis circulating supply: 2,157,756,000 (21.58%).

  | Allocation | Share |
  |---|---|
  | Community | 41.04% |
  | Foundation | 18% |
  | Ecosystem & Liquidity | 15% |
  | Investors | 13.96% |
  | Core Contributors | 12% |

- **Airdrop.** Points-based: Tria Points were earned through spending, trading and referrals and converted to TRIA after TGE. "Season 1" rewards were separate from "loyalty token rewards." Sources: [Bitrue guide](https://www.bitrue.com/blog/tria-airdrop-guide); [CommunityOne post](https://communityone.io/servers/943112063914508308/tria/news/tria-token-live-airdrop-staking-utility)
- **Price and supply.** ATL $0.00232 (18 Oct 2026); -39% over the last 30 days. CoinGecko shows circulating supply unchanged at 2.158B since TGE. Source: [CoinGecko TRIA](https://www.coingecko.com/en/coins/tria)

**Oobit (OOB)**
- **Launch.** OOB debuted on Kraken on 12 Nov 2025 at 10am ET. VCI Global (Nasdaq: VCIG) announced a US$100M acquisition of OOB and serves as treasury manager. Tether is described as a strategic shareholder in Oobit. Source: [Finviz / press release](https://finviz.com/news/227200/oob-token-debuts-on-kraken-following-vcigs-us100-million-acquisition)
- **Launch-day numbers.** GMGN data, as cited by MEXC:
  - OOB briefly traded above $0.8; it was reported at $0.56 with a market cap of about $560M, +342% in 24h.
  - VCI acquired $50M of OOB by issuing restricted shares, and planned another $50M of secondary-market buys.
  - Source: [MEXC News](https://www.mexc.com/news/226731)
- **Earlier rebrand.** The OBT/OOBIT ticker was swapped 1:1 to OOB. Source: [MEXC announcement](https://www.mexc.com/he-IL/announcements/article/mexc-to-support-the-oobit-oobit-token-swap-and-rebranding-to-oobit-oob-17827791531640)
- **Post-launch.** The price fell to $0.0221 by 1 Jan 2026, about -97% in seven weeks. Circulating supply jumped from 77M to 250M on 16 Nov 2025, then +40.6% on 24 Feb 2026 and +67.6% on 5 Aug 2026, reaching 579M. Derived from [CoinGecko OOB](https://www.coingecko.com/en/coins/oobit-2)

**Gnosis (GNO)**
- 2026 high $178.89 (2 Jul 2026). Source: [CoinGecko GNO](https://www.coingecko.com/en/coins/gnosis)

**Solayer (LAYER)**
- ATL $0.0576 (29 Jul 2026). Source: [CoinGecko LAYER](https://www.coingecko.com/en/coins/solayer)

**Cypher (CYPR)**
- A card-wallet token in CoinGecko's neobank category. ATH $0.4686 (5 Oct 2025); now $0.000117, about -100%. Source: [CoinGecko Neobank category](https://www.coingecko.com/en/categories/neobank)

**Thor Wallet (TITN) and other neobank-tagged micro-caps**
- These are under $1M MC and mostly 90–99% below their ATH. Source: [CoinGecko Neobank category](https://www.coingecko.com/en/categories/neobank)

#### Project details: wallets with a payment angle

**World (WLD)**
- ATL $0.230 (18 May 2026). Circulating supply rose 43% YTD, from 2.67B to 3.82B. Derived from [CoinGecko WLD](https://www.coingecko.com/en/coins/worldcoin-wld)

#### Project details: agentic and x402 tokens

**Kite AI (KITE)**
- **Price.** First daily price $0.118 (3 Nov 2025). ATL $0.0618 (4 Nov 2025). ATH $0.3197 (6 Mar 2026). Source: [CoinGecko KITE](https://www.coingecko.com/en/coins/kite-2)
- **Circulating supply.** 1.80B through Apr 2026; 2.27B after a +26% step on 8 May 2026; 2.33B in Jun; 2.39B in Jul; flat since. Derived from [CoinGecko KITE](https://www.coingecko.com/en/coins/kite-2)

**PAYAI**
- ATL $0.00207 (30 Apr 2026); the price is about 293% above it now. Source: [CoinGecko PAYAI](https://www.coingecko.com/en/coins/payai-network-2)

**Other x402-tagged tokens (21 Oct 2026).** Source: [CoinGecko x402 Ecosystem](https://www.coingecko.com/en/categories/x402-ecosystem)

| Token | MC | FDV | ATH date | vs ATH | YTD | Note |
|---|---|---|---|---|---|---|
| DREAMS (Daydreams) | $3.3M | – | 7 Nov 2025 | -91.5% | -59.7% | – |
| ANY (AnySpend) | $6.5M | $29.3M | 12 Nov 2025 | -88.8% | -56.9% | – |
| ZAUTH | $1.5M | – | 14 Feb 2026 | -80% | – | – |
| BNKR (Bankr) | $33.4M | – | 10 Feb 2026 | -72% | – | – |
| ACU (Acurast) | $43.5M | $107M | 23 Jan 2026 | -67% | – | – |
| UB (Unibase) | $330M | $1.32B | 15 May 2026 | – | +276% | AI-memory project that CoinGecko tags as x402 |

#### Unlocks over the next six months (Oct 2026 – Apr 2027): cited facts
- **HUMA:** the first team/advisor/investor unlock is on 26 Nov 2026. Source: [Tokenomist](https://tokenomist.ai/research/weekly-unlock-digest-may-25-31-2026-humas-lockup-extension). The size is unverified; see Inferences.
- **XPL:** monthly releases are visible in CoinGecko data, about 89–131M per month, plus the 26 Sep 2026 cliff-sized step. Derived from [CoinGecko](https://www.coingecko.com/en/coins/plasma)
- **Fully or nearly fully circulating, so little or no unlock overhang:** ETHFI, AVICI, PING, PAYAI, ZBCN, PUNDIX. Source: [CoinGecko markets data](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=ether-fi,avici,ping,payai-network-2,zebec-network,pundi-x-2)
- **Low float:** KITE 23.9%, TRIA 21.6%, STABLE 18%, HUMA 17.3%, OOB 58.5%, LAYER 21%. Source: [CoinGecko markets data](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=kite-2,tria,stable-2,huma-finance,oobit-2,solayer)

### Inferences
- **XPL unlock size.** The 26 Sep 2026 step of 1.755B XPL is about one-third of the combined team (25%) and investor (25%) allocations, which is 1.667B, plus one ~89M ecosystem tranche. This matches the schedule Plasma published at launch, which I know from prior knowledge and did not re-verify this session:
  - Team and investors: one-third unlocks at a one-year cliff after mainnet beta; the rest unlocks monthly over 24 months.
  - Ecosystem: 32% unlocks monthly over 36 months, which is 88.9M per month.
  - If that holds, about 228M XPL unlocks per month (about 139M insider plus 89M ecosystem). Over the next six months that is about 1.37B XPL, roughly 30% of current circulating supply and about $112M at today's price.
  - Confidence: medium-high on the cadence, medium on the exact amounts.
- **HUMA unlock size.** If "13.4% of market cap" is right, the 26 Nov 2026 unlock is about 230M HUMA, or about 13% of circulating supply, worth about $7M at today's price. Confidence: low; the size has not been verified.
- **KITE and TRIA anniversaries.** Both have their one-year TGE anniversary inside the window: 3 Nov 2026 for KITE and 3 Feb 2027 for TRIA. Many 2025-vintage tokens use 12-month insider cliffs. Speculative; check Tokenomist or the projects' docs.
  - For TRIA, investors (13.96%) and core contributors (12%) together hold 26% of supply, against a 21.6% float. A cliff could therefore more than double circulating supply.
- **Launch pattern.** Tokens listed at hype-peak valuations and then fell 85–99%. Implied peak FDVs:

  | Token | Implied peak FDV |
  |---|---|
  | XPL | ~$16.8B |
  | KITE | ~$3.2B |
  | OOB | ~$730M |
  | TRIA | ~$500M |
  | AVICI | ~$97.5M |
  | PING | ~$79M |

  AVICI shows that even a tiny ICO valuation ($4.5M) does not protect holders. It is now below its ICO price after a 21.6x run.
- **Why the 2026 outperformers held up.** HUMA combined growing fees, locked insider supply and 30% of the float staked. KITE had a low float and the agentic narrative. ETHFI had no remaining unlocks and growing Cash revenue. Cheap or no new supply combined with measurable fundamentals is the common factor.

### Gaps
- **Listing data outside the window.** Exact TGE listing prices and FDVs for HUMA (May 2025) and XPL (Sep 2025) fall outside the 365-day API window and were not re-verified.
- **Unverified venue and airdrop details.** TGE venues and airdrop details for HUMA, XPL, KITE, PING and PAYAI were not verified. The following is unverified background from prior knowledge:
  - HUMA listed on Binance on 26 May 2025 with a HODLer Airdrop.
  - KITE launched via Binance Launchpool on 3 Nov 2025.
  - PING was a fair-mint token paid via x402 on Base.
- **No forward unlock calendars.** Tokenomist and CryptoRank pages returned 403, so there is no authoritative unlock calendar for KITE, TRIA, OOB, STABLE or HUMA. The Nov 2026 HUMA unlock size is unconfirmed.
- **Broken CoinGecko supply fields.** ACH's circulating supply has not been reported since May 2026. The new TEL token's circulating MC is not populated; I estimated about $140M from the legacy supply of about 95.1B.
- **Funding not collected.** Funding rounds for Tria and Kite AI were not collected.
- **PAYAI series.** The PAYAI CoinGecko ID "payai-network-2" starts on 19 Nov 2025, which suggests a migration or relisting. The original token's history was not checked.

## 2. Real usage versus incentive-driven activity: card spend, TPV, users, revenue and regions in 2026

### Takeaway
Card spend that can be tracked on-chain is real, sizeable and concentrated. In the last 30 days, the 20 card programs DefiLlama tracks did $886M:
- RedotPay: $463M
- Nexo: $168M
- ether.fi Cash: $134M
- Karta: $53M
- Plasma One: $29M

The leaders grew through the 2026 bear market:
- ether.fi Cash monthly spend rose 2.4x from Jan to Sep.
- Plasma One went from about $0 to $25.6M per month after launch.
- Huma's H1 volume rose 56% half-on-half.

Token-incentivized programs show the opposite pattern:
- Tria Card fees are about 97% below their pre-TGE peak.
- DefiLlama-tracked x402 volume is about 94% below its Dec 2025 level.

Little of this value reaches tokens:
- Huma's fees go to liquidity providers, so its protocol revenue is zero by design.
- ether.fi Cash took about $12.8M in revenue over the last year, roughly 1.4% of spend.

### Cited Findings

#### Industry level
- **Artemis report, 15 Jan 2026.** Sources: [The Defiant](https://thedefiant.io/crypto-cards-rival-stablecoin-transfers-as-spending-tops-usd18-billion-artemis); [Forklog](https://forklog.com/en/crypto-card-market-surges-1400-in-two-years-to-18bn/). One outlet dates the $1.5B month to Aug 2025.
  - Crypto card monthly volume grew from about $100M in early 2023 to more than $1.5B in late 2025. That is a 106% CAGR and an annualized rate above $18B.
  - P2P stablecoin transfers run at about $19B annualized but grew only 5% over the same period.
  - Visa stablecoin-linked card spend reached a $3.5B annualized rate in late 2025, up about 460% YoY. Visa handles more than 90% of on-chain crypto card volume.
  - USDC and USDT make up about 96% of the collateral on Rain-issued cards.
- **DefiLlama "Crypto Card Issuer" category, as of 21 Oct 2026.** This covers only on-chain settlement flows. DefiLlama files card spend under its "dexs/volume" dimension.
  - 20 programs have volume data. Combined: $885.8M over the last 30 days and $6.65B over the last 365 days.
  - Sources: [DefiLlama API overview (Crypto Card Issuer volume)](https://api.llama.fi/overview/dexs?excludeTotalDataChart=true&dataType=dailyVolume); for example, [DefiLlama RedotPay Card](https://defillama.com/protocol/redotpay-card)

  | Program | 30d | 365d | All-time | 30d vs prior 30d |
  |---|---|---|---|---|
  | RedotPay | $463.1M | $1.93B | $2.28B | +2.2% |
  | Nexo | $168.3M | $2.69B | $6.62B | – |
  | ether.fi Cash | $133.9M | $934.4M | $1.02B | +9.6% |
  | Karta | $53.1M | $338.0M | – | +14.5% |
  | Plasma One | $29.1M | $94.5M | – | +30% |
  | Kolo | $15.3M | $109.5M | – | – |
  | Gnosis Pay | $6.6M | $101.8M | $178.6M | -15% |
  | Bleap | $5.0M | $37.8M | – | – |
  | Spritz | $3.4M | $56.7M | – | – |
  | MetaMask Card | $2.3M | $49.3M | $72.9M | – |
  | Tuyo | $2.1M | – | – | – |
  | Exa | $1.7M | $16.0M | – | – |
  | Solayer Card | $0.57M | $14.3M | – | – |
  | Bitget Wallet Card | $0.43M | $36.8M | – | – |
  | Avici | $0.37M | $6.3M | – | -37% |
  | SafePal | $0.28M | – | – | – |
  | KAST Card | $0.20M | $52.9M | – | – |
  | Cypher | $0.09M | $74.2M | – | – |
  | Holyheld | $0 | $40.7M | – | – |
  | Ready | $0 | $33.1M | – | – |

  A further ten programs listed in the category had no volume data: Avalanche, Coinbase, Kraken and Revolut cards, plus VaultLeap, Wirex One, Ethena Pay, Ruvo and PayitFast. Source: [DefiLlama protocols API](https://api.llama.fi/protocols)

#### Monthly on-chain card volume, $M (DefiLlama summary/dexs API; Oct 2026 covers 1–21 Oct only)

| Program | Jul25 | Aug25 | Sep25 | Oct25 | Nov25 | Dec25 | Jan26 | Feb26 | Mar26 | Apr26 | May26 | Jun26 | Jul26 | Aug26 | Sep26 | Oct26* |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RedotPay | 34.3 | 42.4 | 35.6 | 34.0 | 29.6 | 32.9 | 43.5 | 48.7 | 55.4 | 54.1 | 58.9 | 63.3 | 296.1 | 467.5 | 461.7 | 320.5 |
| ether.fi Cash | 10.6 | 13.8 | 23.6 | 33.1 | 36.8 | 55.8 | 54.3 | 53.2 | 62.5 | 64.9 | 79.8 | 83.5 | 102.7 | 109.4 | 128.4 | 95.6 |
| Nexo | 184.8 | 230.9 | 153.8 | 249.3 | 386.2 | 160.5 | 161.7 | 325.4 | 314.9 | 226.1 | 145.5 | 386.3 | 100.5 | 123.7 | 188.5 | 109.7 |
| Karta | 1.8 | 2.8 | 3.1 | 4.0 | 6.5 | 7.2 | 9.2 | 8.1 | 17.2 | 27.6 | 34.3 | 39.1 | 58.4 | 43.7 | 49.5 | 36.6 |
| Plasma One | 0 | 0 | 0 | 0 | 0 | 0 | 0.13 | 0.26 | 1.10 | 0.77 | 3.41 | 8.96 | 15.16 | 19.89 | 25.63 | 19.99 |
| KAST Card | 0 | 0 | 0 | 0 | 0 | 0.04 | 11.91 | 11.44 | 13.91 | 10.94 | 2.83 | 0.69 | 0.56 | 0.21 | 0.21 | 0.15 |
| Gnosis Pay | 11.2 | 11.0 | 11.2 | 12.0 | 10.9 | 9.9 | 9.6 | 8.3 | 9.5 | 9.7 | 10.2 | 1.4 | 8.4 | 8.2 | 7.6 | 4.3 |
| Bleap | 0.90 | 1.14 | 1.10 | 1.18 | 2.19 | 2.76 | 1.45 | 1.94 | 2.83 | 2.88 | 3.01 | 3.40 | 4.29 | 4.55 | 4.67 | 3.55 |
| MetaMask Card | 3.11 | 3.87 | 4.30 | 5.31 | 5.08 | 4.79 | 4.85 | 4.26 | 5.14 | 5.14 | 4.25 | 3.55 | 3.30 | 2.85 | 2.53 | 1.63 |
| Exa | 1.33 | 1.16 | 1.01 | 0.94 | 0.84 | 0.83 | 1.12 | 1.13 | 1.00 | 1.18 | 1.29 | 1.49 | 2.27 | 1.63 | 1.71 | 1.21 |
| Holyheld | 8.37 | 7.22 | 7.87 | 5.48 | 5.89 | 6.87 | 4.20 | 4.72 | 5.43 | 4.21 | 4.19 | 3.62 | 0 | 0 | 0 | 0 |
| Cypher | 8.76 | 9.56 | 9.48 | 10.69 | 9.12 | 9.13 | 9.08 | 6.81 | 8.44 | 7.65 | 8.27 | 7.88 | 3.83 | 0.16 | 0.14 | 0.03 |
| Solayer Card | 1.85 | 1.88 | 1.92 | 2.22 | 1.85 | 1.71 | 1.76 | 1.10 | 1.29 | 1.45 | 0.98 | 0.76 | 0.86 | 0.75 | 0.60 | 0.34 |
| Avici | 0 | 0 | 0 | 0 | 0 | 0.09 | 0.73 | 0.66 | 0.70 | 0.74 | 0.83 | 0.55 | 0.70 | 0.69 | 0.36 | 0.25 |

Sources:
- [DefiLlama RedotPay Card](https://defillama.com/protocol/redotpay-card)
- [DefiLlama EtherFi Cash](https://defillama.com/protocol/etherfi-cash-liquid)
- [DefiLlama Nexo Card](https://defillama.com/protocol/nexo-card)
- [DefiLlama Karta Card](https://defillama.com/protocol/karta-card)
- [DefiLlama Plasma One](https://defillama.com/protocol/plasma-one)
- [DefiLlama KAST Card](https://defillama.com/protocol/kast-card)
- [DefiLlama Gnosis Pay](https://defillama.com/protocol/gnosis-pay)
- [DefiLlama Bleap Card](https://defillama.com/protocol/bleap-card)
- [DefiLlama MetaMask Card](https://defillama.com/protocol/metamask-card)
- [DefiLlama Exa Card](https://defillama.com/protocol/exa-card)
- [DefiLlama Holyheld Card](https://defillama.com/protocol/holyheld-card)
- [DefiLlama Cypher Card](https://defillama.com/protocol/cypher-card)
- [DefiLlama Solayer Card](https://defillama.com/protocol/solayer-card)
- [DefiLlama Avici](https://defillama.com/protocol/avici)
- API pattern: https://api.llama.fi/summary/dexs/{slug}?dataType=dailyVolume

#### Monthly fees, revenue and x402 volume, $M (DefiLlama; Oct 2026 covers 1–21 Oct only)

| Metric | Jul25 | Aug25 | Sep25 | Oct25 | Nov25 | Dec25 | Jan26 | Feb26 | Mar26 | Apr26 | May26 | Jun26 | Jul26 | Aug26 | Sep26 | Oct26* |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tria Card fees | 0.02 | 0.04 | 0.06 | 0.76 | 0.39 | 0.33 | 0.43 | 0.22 | 0.18 | 0.18 | 0.19 | 0.09 | 0.04 | 0.01 | 0.02 | 0.02 |
| ether.fi Cash revenue | 0.15 | 0.19 | 0.33 | 0.46 | 0.51 | 0.77 | 0.75 | 0.69 | 0.86 | 0.89 | 1.10 | 1.14 | 1.39 | 1.50 | 1.76 | 1.32 |
| Huma fees | 0.00 | 0.59 | 0.69 | 1.05 | 0.72 | 1.01 | 1.03 | 0.95 | 1.18 | 1.18 | 1.20 | 1.15 | 1.48 | 1.70 | 2.50 | 1.97 |
| x402 volume | 0.00 | 0.00 | 0.00 | 3.88 | 6.06 | 10.76 | 2.03 | 2.29 | 2.39 | 1.99 | 1.03 | 0.76 | 0.57 | 1.12 | 0.66 | 0.77 |
| b402 fees | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.01 | 0.46 | 0.32 | 0.12 | 0.08 | 0.04 | 0 | 0 | 0 |
| MetaMask mUSD fees | 0 | 0 | 0.10 | 0.21 | 0.08 | 0.07 | 0.07 | 0.06 | 0.07 | 0.09 | 0.09 | 0.09 | 0.07 | 0.05 | 0.04 | 0.03 |

Sources:
- [DefiLlama Tria Card](https://defillama.com/protocol/tria-card)
- [DefiLlama EtherFi Cash](https://defillama.com/protocol/etherfi-cash-liquid)
- [DefiLlama Huma](https://defillama.com/protocol/huma)
- [DefiLlama x402](https://defillama.com/protocol/x402)
- [DefiLlama b402](https://defillama.com/protocol/b402)
- [DefiLlama MetaMask USD](https://defillama.com/protocol/metamask-usd)

#### Neobanks and card issuers

**RedotPay**
- 6M users and about $10B of annualized payment volume, per the company website, as cited on 24 Feb 2026. Source: [Cointelegraph](https://cointelegraph.com/news/redotpay-eyes-us-ipo-1b-4b-valuation)
- More than $150M of annualized revenue, operating profitably, reported with the Dec 2025 Series B. Another report cites $158M of revenue from investor materials. Source: [The Block](https://www.theblock.co/post/382729), via search snippet.
- Hong Kong-based; 100+ markets. Sources: [Cointelegraph](https://cointelegraph.com/news/redotpay-eyes-us-ipo-1b-4b-valuation); search snippet.
- On-chain-tracked RedotPay volume ran at about $43–63M per month in Jan–Jun 2026, then $296M (Jul), $467M (Aug) and $462M (Sep). Source: [DefiLlama RedotPay Card](https://defillama.com/protocol/redotpay-card)

**ether.fi Cash.** Source for this list: [Crypto Briefing, 4 Sep 2026](https://cryptobriefing.com/ether-fi-cash-exceeds-800m-spend/)
- **Spend:**
  - More than $800M cumulative, about $600M of it in 2026.
  - Q1 2026: $170M, +35% QoQ. Cumulative spend passed $400M by late Apr, and monthly volume regularly exceeded $50M.
- **Base:** about 70,000 active cards, about 300,000 accounts, nearly 10M transactions, average transaction under $100.
- **Revenue share:** Cash was 26% of ether.fi revenue in Q1 2026, up from 14.2% in Q4 2025. Revenue comes from interchange, FX and lending.
- **Rewards and chain:** up to 3% cashback, credited to user vaults. Cash migrated to OP Mainnet in Feb 2026.

**ether.fi Cash: DefiLlama cross-check**
- Q1 2026 on-chain volume = $54.3M + $53.2M + $62.5M = $170.0M, matching Crypto Briefing.
- Revenue over the last 365 days: $12.79M. Fees: $33.1M. TVL: $248M.
- Source: [DefiLlama EtherFi Cash](https://defillama.com/protocol/etherfi-cash-liquid)
- A proposal to move Cash to Aave V4 on Optimism reached temp check on 1 Jul 2026; the outcome is unconfirmed. Source: [DefiLlama dashboard](https://defillama.com/pro/ethfi-follow-the-money-ms7xy3), via search snippet.

**Plasma One**
- **Announcement, 22 Sep 2025.** 4% cashback, "10%+ yields" and card coverage in 150 countries. The team gathered user and merchant feedback in Istanbul, Dubai and Buenos Aires. Source: [Yahoo Finance](https://finance.yahoo.com/news/plasma-launches-revolutionary-usdt-native-172446155.html)
- **Full launch, 23 Jun 2026.** Confidence: medium. Source: [Business Wire China press release](https://www.businesswirechina.com/en/news/63301.html), seen via search snippet and not fetched. DefiLlama's volume inflection in May–Jun 2026 corroborates the timing. The release describes:
  - Zero fees.
  - Up to 4% cashback, with 5% and 10% on eligible AI spend for higher tiers.
  - XPL rose about 20% on the news but stayed about 94% below its ATH.
- **Vendor claims.** Privy, the wallet infrastructure vendor, says Plasma One was the fastest stablecoin card to reach $1M of verifiable on-chain spend, in 45 days. Privy also says 90% of first-time card users spend again. The private beta reportedly had 5,000 weekly active users. Source: [Privy blog](https://privy.io/blog/building-a-stablecoin-native-neobank-from-the-ground-up-with-plasma-one)
- **DefiLlama.**
  - Plasma One monthly spend went from $0.13M (Jan 2026) to $8.96M (Jun) and $25.63M (Sep). TVL is $31.2M.
  - Plasma Saving Vaults: TVL $31.8M, $5.43M of fees over the past year.
  - The Plasma chain itself earned only $154k of fees over the past year.
  - Sources: [DefiLlama Plasma One](https://defillama.com/protocol/plasma-one); [DefiLlama Plasma Saving Vaults](https://defillama.com/protocol/plasma-saving-vaults); [DefiLlama fees overview](https://api.llama.fi/overview/fees?excludeTotalDataChart=true)

**KAST**
- **Series A, 9 Mar 2026.** Source: [Pulse 2.0](https://pulse2.com/kast-80-million-series-a-raised-by-stablecoin-neobank-to-expand-global-financial-platform)
  - **Scale:** more than 1M users and nearly $5B of annualized transaction volume.
  - **Growth:** revenue had doubled since end-Sep 2025, and users and revenue were growing 15–20% month on month. KAST expects a $100M annual revenue run rate in 2026.
  - **Expansion:** expanding in Latin America, North America and the Middle East; pay-ins and payouts in more than 190 countries.
- **DefiLlama on-chain card volume:** $11.9M (Jan), $11.4M (Feb), $13.9M (Mar), $10.9M (Apr), then $2.8M (May), $0.7M (Jun) and about $0.2M per month in Aug–Oct. Source: [DefiLlama KAST Card](https://defillama.com/protocol/kast-card)

**Rain**
- In Jan 2026 the CEO said the active card base had grown 30x and annualized payment volume 38x over the prior year. Rain issues cards in 150+ countries. Source: [The Block](https://www.theblock.co/post/384910/rain-valuation-nears-2-billion-usd-series-c-250-million-raise)
- $3B of annualized payment volume; ranked #8 on the Fortune Crypto 100 (2026). Source: [Fortune](https://fortune.com/ranking/crypto/2026/rain/)
- Rain is the issuing partner whose outdated contract was exploited in the Avici hack. Source: [Tech Insider](https://tech-insider.org/?p=18646)

**Telcoin**
- US-resident users can open on-chain bank accounts as of 23 Jun 2026. ACH or wire deposits mint eUSD 1:1 on Ethereum, Base, Solana and Polygon. Yield on eUSD and debit cards are planned. Source: [Telcoin newsroom](https://telco.in/newsroom/2026-06-23/telcoin-launches-first-regulated-on-chain-bank-accounts-in-the-us)
- The Nebraska Digital Asset Depository Institution (DADI) charter received final approval in Nov 2025. The bank is not FDIC insured. Sources: [Securities.io](https://www.securities.io/investing-in-telcoin-tel-everything-you-need-to-know-2/); [Crowdfund Insider](https://www.crowdfundinsider.com/2026/06/287418-telcoin-enables-regulated-on-chain-bank-accounts-for-us-consumers/)

#### PayFi: Huma Finance
Source for this list: [Blockworks Advisory, Huma H1 2026 report](https://blockworks.com/api/investor-report/huma-finance-protocol-report-h1-2026/pdf). Blockworks Advisory reports are typically commissioned by the protocol.
- **Volume:**
  - Cumulative PayFi volume reached $14.96B at 30 Jun 2026, up from $8.96B at year-end 2025.
  - H1 2026 volume was $6.00B, against $3.85B in H2 2025 (+56%) and $2.41B in H1 2025 (+149%).
- **Fees:**
  - $6.68M in H1 (Q1 $3.15M, Q2 $3.53M). Monthly fees held at $1.15–1.20M from March; June annualizes to about $13.8M.
  - The take rate was about 11 bps of throughput in Q2, down from 13 bps in Q4 2025.
  - Protocol revenue is zero by design: fees accrue to PST liquidity providers, not to the protocol.
- **PST** (the PayFi Strategy Token):
  - Supply grew from $116.1M to $181.8M "without the deposit campaigns that drove late-2025 inflows."
  - Yield is about 8%. Gross fee capture was 8.3–9.1% annualized, and NAV per share rose from 1.0718 to 1.1135.
- **Arf** (Huma's financing arm):
  - The credit facility grew from $70.5M to $150M, and turnover rose from 4.46 to 4.53 cycles.
  - Cumulative Arf loans reached $7.56B.
- **Retail incentives wound down:**
  - Maxi Mode was sunset: mPST fell from $7.68M to $0.76M, and mPST holders dropped 39%.
  - PST holders fell 13% to 4,443 while the average position grew 81% to $40,926. The report calls this "less dependency on incentive-driven deposits."
- **Management quote:** "Despite the bear market and an overall shrinking DeFi ecosystem…"

DefiLlama shows Huma fees of $1.48M (Jul), $1.70M (Aug), $2.50M (Sep) and $1.97M for 1–21 Oct. That is $2.94M over the last 30 days and $16.36M over the last 365 days, with TVL of $378.6M. DefiLlama's Q1 total ($3.16M) and Q2 total ($3.53M) match Blockworks. Source: [DefiLlama Huma](https://defillama.com/protocol/huma)

#### Wallet stablecoins and wallet revenue

**Phantom**
- CASH supply: $127.7M on 21 Oct 2026, against $127.6M a month earlier. Source: [DefiLlama stablecoins](https://defillama.com/stablecoins)
- Phantom launched CASH through Bridge's Open Issuance platform and was its first issuer, in Sep 2025. Phantom Card, built on Stripe Issuing and Bridge, rolled out to all users in spring 2026. "Thousands" of cards were issued after general availability. Source: [Stripe case study](https://stripe.com/us/customers/phantom-spotlight)

**MetaMask**
- mUSD supply: $33.8M on 21 Oct 2026, against $30.1M a month earlier. In Jan 2026 it was cited at more than $53M, so it shrank during 2026.
- mUSD earned $857k of fees over 365 days.
- Sources: [DefiLlama stablecoins](https://defillama.com/stablecoins); [BlockEden](https://blockeden.xyz/blog/2026/01/26/metamask-mask-token-consensys-wallet-tokenization/); [DefiLlama MetaMask USD](https://defillama.com/protocol/metamask-usd)

**Wallet fees over the last 365 days (DefiLlama)**
- Phantom Wallet $88.7M, plus Phantom Perps $19.0M.
- MetaMask Wallet $33.0M, plus MetaMask Perps $11.8M.
- Sources: [DefiLlama Phantom Wallet](https://defillama.com/protocol/phantom-wallet); [DefiLlama MetaMask Wallet](https://defillama.com/protocol/metamask-wallet)

**Other stablecoin supplies, 21 Oct 2026**
- Telcoin eUSD: $10.2M.
- Western Union USDPT: $17.4M, against $15.4M a month earlier. CoinGecko's price series for USDPT starts 8 Jul 2026.
- Comparison: PYUSD $2.86B and USDG $3.07B.
- Sources: [DefiLlama stablecoins](https://defillama.com/stablecoins); [CoinGecko USDPT](https://www.coingecko.com/en/coins/usdpt-western-union)

#### x402 usage
- **Phemex, 5 Apr 2026, citing WuBlockchain.** The transaction count fell 98%, from a 20M peak in Nov 2025 to 420K in Mar 2026. Volume was about $15M in March; the article labels it weekly, but it may be monthly. The average transaction size rose from $0.04 to $26. Source: [Phemex](https://phemex.com/news/article/x402-protocol-sees-surge-in-weekly-volume-to-15-million-amid-transaction-drop-70999)
- **AiCoin/Odaily, Nov 2025.** Daily volume fell 90% from its peak, and fewer than 2,000 new daily additions were recorded after November. Source: [AiCoin](https://www.aicoin.com/en/news-flash/2614356)
- **Visa/Artemis analysis (undated).** Visa's Sheffield put adjusted x402 volume at $19M. About 4,000 wallets drive roughly 90% of adjusted spending, mostly on Base. Source: [The Defiant](https://thedefiant.io/converge/infrastructure)
- **DefiLlama x402 adapter.** Monthly figures are in the table above. All-time volume is $34.3M; the last 30 days $1.0M; the last 24 hours $143k. This contradicts Phemex's $15M figure; DefiLlama's coverage of facilitators is probably partial. Source: [DefiLlama x402](https://defillama.com/protocol/x402)

### Inferences
- **Real vs incentive-driven:**
  - **Tria:** the fee collapse right after its Feb 2026 TGE is the clearest case of points-farming demand. Fees peaked in Oct 2025 during the points season, are about 97% lower by Sep 2026, and the token fell 95%.
  - **x402:** the late-2025 spike, with a $0.04 average transaction, looks like bot, mint or test traffic. The later profile of fewer but larger payments (about $26 average) looks more like real API commerce, but at a tiny absolute size of about $1M per month on DefiLlama. The fact that Visa/Artemis needed an "adjusted" volume measure supports this reading.
- **Organic-looking growth among leaders:** ether.fi Cash, RedotPay, Karta, Bleap and Huma all grew through a market where BTC fell to $58.6K by 1 Jul 2026. But part of this is subsidized:
  - Plasma One pays 2–4% cashback in XPL, which is effectively selling pressure on XPL. At current monthly spend of about $25M, that implies roughly $0.5–1M per month of XPL rewards (my estimate).
  - ether.fi Cash offers up to 3% cashback, which is large relative to its roughly 1.4% revenue take (revenue $12.79M ÷ spend $934M over 365 days).
- **On-chain tracker breaks are not real-world declines.** Several DefiLlama series likely break for methodology reasons:
  - **KAST:** the drop after Apr 2026 contradicts its self-reported growth. A move to a different issuer or settlement address is likely.
  - **Holyheld:** zero from Jul 2026, likely a tracking break.
  - **RedotPay:** the 4.7x jump in Jul 2026 likely reflects added coverage.
  - **Cypher:** the collapse to about $0 coincides with its token going to about zero, so the program may have ended.

  Treat month-on-month changes for these four with caution.
- **Concentration.** RedotPay alone accounts for 52% of tracked 30-day card volume. RedotPay, Nexo and ether.fi together account for 86%. The neobanks with tokens (Plasma One, Avici, Tria) together account for less than 4%.
- **Regions.** Available evidence points to emerging markets:
  - KAST: Latin America and the Middle East.
  - Plasma One: user research in Istanbul, Dubai and Buenos Aires.
  - RedotPay: Hong Kong-based, 100+ markets.
  - Rain: licensing in South America, Asia and Africa.

  Telcoin's bank product is US-only. There is no quantitative regional split.
- **Run rates.** Tracked card volume for the last 30 days annualizes to about $10.6B. That is in line with Artemis's late-2025 run rate above $18B, given that DefiLlama misses off-chain and Visa-direct flows.

### Gaps
- **Missing user numbers:** no user or cardholder counts for Plasma One (beyond the beta WAU), Bleap, Exa, Holyheld, Gnosis Pay, MetaMask Card or Avici. No country-level split for any program.
- **Unknown series breaks:** the causes of the KAST, Holyheld, RedotPay and Cypher breaks are unconfirmed.
- **Not covered at all:** Kontigo (LatAm/Venezuela) and Payy.
- **Plasma One launch date:** the 23 Jun 2026 date is medium confidence; the press release was not fetched directly.
- **Data sources not accessed:** Dune card dashboards and x402scan (the page was not machine-readable). There is no authoritative 2026 x402 volume series beyond DefiLlama's partial adapter and the press figures, which conflict.
- **Unverified buyback data:** ether.fi's 2026 buyback amounts rest on a single unverified DefiLlama dashboard claim.
- **No incentive-spend totals:** not found for XPL cashback, KAST points or MetaMask Rewards.
- **World App:** its 2026 stablecoin and payments metrics were not collected.

## 3. Pre-TGE pipeline: points and cashback programs, funding and valuations, token odds, airdrop expectations, and equity-only infrastructure

### Takeaway
The large payment names without tokens either show no near-term plan or are taking the equity route.

Prediction markets, as of 21 Oct 2026, give low odds of a token by 31 Dec 2026:

| Project | Odds of token by 31 Dec 2026 |
|---|---|
| MetaMask | 6% |
| Phantom | 4% |
| Rabby | 9% |
| Base | 5.5% |
| Stripe's Tempo | 4% |
| KAST | 16.5% (thin market) |

The equity route:
- **RedotPay:** IPO talk at a valuation above $4B.
- **Rain:** $1.95B valuation.
- **KAST:** $80M Series A, token unconfirmed.

M&A is repricing payment infrastructure:
- Mastercard agreed to buy BVNK for up to $1.8B.
- Zerohash is seeking a valuation of $1.5B or more.

In 2026 the private equity stack, not tokens, captured most of the value created in stablecoin payments.

### Cited Findings

#### Prediction-market odds (Polymarket, 21 Oct 2026; pulled via gamma-api.polymarket.com)

**MetaMask and Consensys**
- MetaMask token by 31 Dec 2026: 6%. The event has traded $8.72M; the "by 30 Sep 2026" market resolved No. Source: [Polymarket MetaMask token](https://polymarket.com/event/will-metamask-launch-a-token-in-2025)
- MetaMask FDV above $100M one day after launch: 4.5%; above $1B: 4.5%; above $3B: 2.25% (event volume $3.36M). Source: [Polymarket MetaMask FDV](https://polymarket.com/event/metamask-fdv-above-one-day-after-launch)
- Consensys IPO by 31 Dec 2026: 3.85%. Source: [Polymarket Consensys IPO](https://polymarket.com/event/will-consensys-ipo-by-december-31-2025)
- Consensys IPO closing market cap above $1B: 7.45%. Source: [Polymarket Consensys IPO market cap](https://polymarket.com/event/consensys-ipo-closing-market-cap-above)

**Other wallets and chains**
- **Phantom token:** 4.15% by 31 Dec 2026; 21% by 31 Dec 2027. The quarterly markets through 30 Sep 2026 resolved No. Source: [Polymarket Phantom](https://polymarket.com/event/will-phantom-launch-a-token-by)
- **Rabby token:** 9% by 31 Dec 2026; 29.5% by 31 Dec 2027. Source: [Polymarket Rabby](https://polymarket.com/event/will-rabby-launch-a-token-by)
- **Base token:** 5.5% by 31 Dec 2026; 20.5% by 30 Jun 2027; 41.5% by 31 Dec 2027 (event volume $8.05M). Source: [Polymarket Base](https://polymarket.com/event/will-base-launch-a-token-in-2025-341)
- **Tempo token** (Stripe's payments chain): 4.05% by 31 Dec 2026; 22.5% by 31 Dec 2027 (volume $924K). Source: [Polymarket Tempo](https://polymarket.com/event/will-tempo-launch-a-token-by)

**KAST**
- KAST token odds by date: Source: [Polymarket KAST](https://polymarket.com/event/will-kast-launch-a-token-by)

  | By | Odds |
  |---|---|
  | 31 Dec 2026 | 16.5% |
  | 31 Mar 2027 | 23% |
  | 30 Jun 2027 | 34% |
  | 30 Sep 2027 | 36.5% |
  | 31 Dec 2027 | 38% |

  The market is very thin, with only $15.6K traded.

**Stripe IPO**
- Stripe IPO before 2027: 2.2%. Source: [Polymarket IPOs before 2027](https://polymarket.com/event/ipos-before-2027)

#### MetaMask: token status and programs
Source for this list: [BlockEden, 26 Jan 2026 (updated 22 Feb 2026)](https://blockeden.xyz/blog/2026/01/26/metamask-mask-token-consensys-wallet-tokenization/)
- **Token signals:**
  - In Sep 2025, Joe Lubin said MetaMask's token "may come sooner than you would expect."
  - A claim portal, claims.metamask.io, appeared in Oct 2025 behind a password and later redirected to the homepage.
- **MetaMask Rewards:** launched Oct 2025 with more than $30M of LINEA. Season 1 ran 90 days, and points came from swaps, perps, bridging and referrals.
- **mUSD:** launched Aug 2025 with Bridge and M0, on Ethereum and Linea.
- **Users:** more than 30M MAU.
- **Consensys IPO:** reportedly being worked on with JPMorgan and Goldman for mid-2026; it has not happened.

Fake "MASK airdrop" announcements appeared in Mar 2026 on unaffiliated, low-credibility domains. Treat them as phishing. Example: [woollyfelt.com page (not credible)](https://nepal.woollyfelt.com/?p=11365)

#### Neobank and card companies: funding, valuation, token status

**KAST**
- Series A of $80M on 9 Mar 2026, co-led by QED Investors and Left Lane Capital. Peak XV, HSG and DST Global Partners returned. Source: [Pulse 2.0](https://pulse2.com/kast-80-million-series-a-raised-by-stablecoin-neobank-to-expand-global-financial-platform)
  - The valuation was not disclosed.
  - Founded Jul 2024 by former Circle executive Raagulan Pathy.
  - The press release does not mention a token, points or an airdrop.
- CoinLaunch, a promotional aggregator, claims a points-farming campaign with a "confirmed $KAST airdrop" of 15–25% of supply. It lists a TBA date (plus an unclear "02 May 2026 retrodrop") and a $90M total raise. Source: [CoinLaunch](https://coinlaunch.space/projects/kast/). Confidence: low.

**RedotPay**
- **2025 funding:** $194M across three rounds. Source: [Cointelegraph, 24 Feb 2026](https://cointelegraph.com/news/redotpay-eyes-us-ipo-1b-4b-valuation)

  | Round | Date | Amount | Investors |
  |---|---|---|---|
  | Series A | Mar 2025 | $40M | Lightspeed (lead); HSG; Galaxy Ventures |
  | Strategic | Sep 2025 | $47M | Coinbase Ventures; Galaxy; Vertex |
  | Series B | Dec 2025 | $107M | Goodwater (lead); Pantera; Blockchain Capital; Circle Ventures; HSG |

  The strategic round made RedotPay a unicorn, valued above $1B.
- **IPO talks.** On 24 Feb 2026, Bloomberg reported that RedotPay was weighing a US IPO that could raise more than $1B at a valuation above $4B. JPMorgan, Goldman Sachs and Jefferies were involved, and a listing "may occur as early as this year." RedotPay declined to comment.
- No token plans were mentioned.

**Rain**
- Series C of $250M at a $1.95B valuation in Jan 2026, led by ICONIQ. Total raised: about $338M. Source: [The Block](https://www.theblock.co/post/384910/rain-valuation-nears-2-billion-usd-series-c-250-million-raise)
- Other participants: Sapphire, Dragonfly, Bessemer, Galaxy Ventures, FirstMark, Lightspeed, Norwest and Endeavor Catalyst.
- Prior rounds: a $58M Series B (Aug 2025, Sapphire) and $24.5M (Mar 2025).
- Rain has no token.

**Plasma**
- Plasma already has a token (XPL), so it is not part of the pipeline. Its rewards program is cashback in XPL. Source: [blocmates](https://www.blocmates.com/articles/why-use-the-plasma-card-features-benefits-explained)

#### Equity-only payment infrastructure: capital-flow context

**Mastercard–BVNK**
- Definitive agreement signed 17 Mar 2026 for up to $1.8B, including $300M contingent on milestones. Completion is expected by end-2026, subject to regulatory approvals. Source: [Coin360](https://coin360.com/news/mastercard-bvnk-1-8b-stablecoin-acquisition)
- BVNK was valued at about $750M in its 2024 Series B and operates in 130+ countries.
- Mastercard cited at least $350B of stablecoin payment volume in 2025. Its chief product officer said buying was faster than building.

**Coinbase–BVNK**
- Exclusive talks at about $2B ended on 11 Nov 2025, per Bloomberg and Fortune. Source: [Acquiry deal analysis](https://www.acquiry.com/deal-analysis/coinbase-bvnk-deal-collapse/), via search snippet.

**Zerohash**
- Mastercard explored buying Zerohash at $1.5–2B but dropped the plan after the BVNK deal. Zerohash is reportedly raising at a higher valuation; an earlier round sought $250M at $1.5B. Source: [crypto.news](https://crypto.news/zerohash-seeks-1-5b-valuation-after-mastercard-exit/). Coin360 also notes the Zerohash exploration.

**Stripe–Bridge**
- Stripe paid $1.1B for Bridge in 2025, which serves as the benchmark. Source: [Coin360](https://coin360.com/news/mastercard-bvnk-1-8b-stablecoin-acquisition)

### Inferences
- **Probability of a big wallet airdrop.** Markets assign at most about 10% to any major wallet or app-chain airdrop (MetaMask, Phantom, Rabby, Base, Tempo) before 2027. Even by end-2027, the highest is Base at 41.5%. The pipeline of large, liquid payment-adjacent TGEs is mostly a 2027+ story.
- **MetaMask's likely valuation.** The FDV ladder (about 4.5% for any FDV above $100M) suggests conditional expectations of a multi-billion FDV if it ever launches. With the Consensys IPO stalled (3.85%), the token appears tied to corporate-finance decisions.
- **Strongest neobanks prefer equity.** RedotPay and Rain are on venture/IPO tracks with nine- to ten-figure revenue or volume. KAST raised an institutional Series A. For users of these firms, airdrop expectations should be heavily discounted: about 16.5% for KAST in 2026, and nothing confirmed for RedotPay or Rain.
- **Airdrop farmers have been burned.** The Tria precedent (a 41% community allocation that collapsed 95%) and Avici (below its ICO price) suggest the next neobank TGEs (KAST, possibly Bleap or Holyheld) will face skeptical buyers. That is likely to push teams toward low-float, low-FDV listings or toward delaying.
- **Price signals for public listings.** M&A and late-stage rounds are setting high marks: BVNK at about 2.4x its 2024 valuation, Rain at $1.95B, and RedotPay above $1B, targeting above $4B. These may serve as reference prices for any future tokenized or public listing of payment companies.

### Gaps
- **Other neobanks' funding and token plans.** Not gathered for Bleap, Holyheld, Exa, Kontigo, Payy and Gnosis Pay (beyond the GNO token). Only their DefiLlama volumes are available.
- **Infrastructure rounds.** 2026 rounds and valuations for Mesh, Conduit, Borderless and Orbital were not gathered because the search budget was exhausted.
- **RedotPay after Feb 2026.** Its IPO status since the Bloomberg report (filed, paused or priced) is unknown.
- **KAST valuation and points.** KAST's Series A valuation and official points terms are unknown.
- **Wallet token statements.** No 2026 official statements on token plans from Phantom or Rabby were collected.
- **Agentic-payments companies, Skyfire and Catena Labs.** No 2026 funding data was collected. Unverified background from prior knowledge, to be checked:
  - Skyfire raised a $9.5M seed (Aug 2024; a16z CSX, Coinbase Ventures).
  - Catena Labs raised $18M (May 2025; a16z crypto; founder Sean Neville).
  - Kite AI raised about $33M, including an $18M Series A in Sep 2025 led by PayPal Ventures and General Catalyst.
- **Ignored Polymarket market.** The XPL price ladder ("Will Plasma reach $X by 31 Dec 2026") has internally inconsistent prices, with $1.80 at 15.5% but $1.40 at 2.65%. It looks illiquid or stale and should not be used. Source: [Polymarket Plasma price](https://polymarket.com/event/what-price-will-plasma-hit-before-2027)

## 4. Sub-narratives: when PayFi, "stablecoin neobank" and x402/agentic payments peaked, what came after, and current sentiment

### Takeaway
All three sub-narratives peaked in price before or at the very start of 2026:
- **PayFi:** in May–Jun 2025.
- **Stablecoin chain and neobank:** in Sep–Dec 2025, with an echo in mid-Jan 2026 and a brief relief rally in mid-May 2026.
- **x402:** in late Oct–Dec 2025.

By Oct 2026, sentiment toward the tokens is poor: post-TGE drawdowns of 85–99%, the Avici hack and the Tria collapse. Sentiment toward the underlying businesses is strong among TradFi buyers and VCs (Rain, RedotPay, KAST, BVNK).

x402 has turned from a meme-mint mania into a small but higher-value payments rail. Large networks (Visa, Block/Lightning) are paying attention, but its tokens have not benefited.

### Cited Findings

#### Price peaks by sub-narrative (CoinGecko ATH dates)

| Sub-narrative | Token | Peak date | Peak type |
|---|---|---|---|
| PayFi | LAYER | 4 May 2025 | ATH |
| PayFi | HUMA | 26 May 2025 | ATH (TGE day) |
| PayFi | ZBCN | 29 May 2025 | ATH |
| PayFi | KTA | 9 Jun 2025 | ATH |
| Stablecoin chain / neobank | XPL | 27 Sep 2025 | ATH |
| Stablecoin chain / neobank | CYPR | 5 Oct 2025 | ATH |
| Stablecoin chain / neobank | MNT | 8 Oct 2025 | ATH |
| Stablecoin chain / neobank | OOB | 12 Nov 2025 | ATH |
| Stablecoin chain / neobank | AVICI | 26 Nov 2025 | ATH ($7.56) |
| Stablecoin chain / neobank | AVICI | 4 Dec 2025 | 365-day max |
| x402 | PING | 25 Oct 2025 | ATH |
| x402 | DREAMS | 7 Nov 2025 | ATH |
| x402 | ANY | 12 Nov 2025 | ATH |
| x402 | PAYAI | 21 Dec 2025 | ATH |

Sources: [CoinGecko Neobank](https://www.coingecko.com/en/categories/neobank); [CoinGecko Payment Solutions](https://www.coingecko.com/en/categories/payment-solutions); [CoinGecko x402 Ecosystem](https://www.coingecko.com/en/categories/x402-ecosystem)

#### Echo rallies and second waves
- **Mid-Jan 2026:** XPL 2026 high on 7 Jan; AVICI $4.61 on 12 Jan; LAYER 12 Jan; ETHFI 14 Jan; BTC 2026 high on 15 Jan.
- **x402 second wave:** ACU 23 Jan; BNKR 10 Feb; ZAUTH 14–15 Feb; KITE ATH 6 Mar 2026.
- **Mid-May 2026 relief rally:** Superform 13–14 May; STABLE 14 May; TRIA ATH 15 May; UB 15–16 May.
- Sources: CoinGecko market_chart and category data — [CoinGecko Neobank](https://www.coingecko.com/en/categories/neobank); [CoinGecko x402 Ecosystem](https://www.coingecko.com/en/categories/x402-ecosystem)

#### Mid-2026 trough and recovery
- **Lows:**
  - PAYAI ATL 30 Apr 2026.
  - WLD ATL 18 May.
  - ETHFI ATL 5 Jun.
  - SOL 2026 low 7 Jun.
  - XPL ATL 10 Jun.
  - ETH 2026 low 26 Jun.
  - BTC 2026 low ($58.6K) 1 Jul.
- **Recoveries to 21 Oct:**
  - ETHFI +171% from its ATL.
  - HUMA +139% from its 3 Apr low to its 5 Oct high.
  - PAYAI +293% from its ATL.
  - XPL +36% from its ATL.
- Sources: [CoinGecko](https://www.coingecko.com/en/coins/bitcoin) and the token pages cited in section 1.

#### x402 activity curve
- The transaction count peaked at 20M in Nov 2025 and was down 98% by Mar 2026. The average transaction grew from $0.04 to $26. Source: [Phemex](https://phemex.com/news/article/x402-protocol-sees-surge-in-weekly-volume-to-15-million-amid-transaction-drop-70999)
- DefiLlama-tracked volume peaked at $10.76M in Dec 2025, fell to about $0.6–1.1M per month in Jun–Oct 2026, and sits at $34.3M all-time. Source: [DefiLlama x402](https://defillama.com/protocol/x402)
- b402, the BNB Chain variant, peaked in Mar 2026 and was at about zero by Aug 2026. Source: [DefiLlama b402](https://defillama.com/protocol/b402)
- A Lightning payment spec was merged into the x402 repository (Block). Visa and Artemis produced an "adjusted volume" analysis of x402. Source: [The Defiant](https://thedefiant.io/converge/infrastructure)

#### Sector market caps today, 21 Oct 2026
- "Neobank": $2.90B. Excluding MNT, ETHFI and XPL, it is under $0.1B.
- Native x402 tokens are mostly under $10M each, apart from KITE ($293M MC) and UB.
- Sources: [CoinGecko categories](https://www.coingecko.com/en/categories/neobank); [CoinGecko x402 Ecosystem](https://www.coingecko.com/en/categories/x402-ecosystem)

#### Sentiment markers in 2026
- **Positive (business side):**
  - Huma management cited "the bear market and an overall shrinking DeFi ecosystem" while reporting record PayFi volume. Source: [Blockworks Advisory](https://blockworks.com/api/investor-report/huma-finance-protocol-report-h1-2026/pdf)
  - Mastercard said buying BVNK was faster than building. Source: [Coin360](https://coin360.com/news/mastercard-bvnk-1-8b-stablecoin-acquisition)
  - The Rain, RedotPay and KAST mega-rounds — see section 3.
- **Negative (token side):**
  - The Avici hack via a Rain card contract. Source: [Tech Insider](https://tech-insider.org/?p=18646)
  - The TRIA collapse (-39% over 30 days, ATL on 18 Oct 2026). Source: [CoinGecko TRIA](https://www.coingecko.com/en/coins/tria)
  - The XPL insider cliff. Derived from [CoinGecko XPL](https://www.coingecko.com/en/coins/plasma)

### Inferences
- **PayFi**
  - **Peak:** mid-2025, around the HUMA TGE and the Solayer and Zebec card launches.
  - **2026:** the label has largely merged into "stablecoin payments," while Huma's fundamentals compounded. HUMA has decoupled positively in H2 2026 (+24% YTD), reflecting real fee growth and locked supply. It remains 73% below its TGE-day ATH, and the 26 Nov 2026 insider unlock is the near-term test.
  - **Current sentiment:** cautiously constructive on fundamentals, wary of supply.
- **Stablecoin neobank**
  - **Peak:** mindshare and price peaked Sep–Dec 2025: the XPL TGE, the Plasma One announcement, the Oobit/VCIG treasury listing and the Avici ICO run.
  - **Echoes:** a mid-Jan 2026 echo and a speculative TRIA/Superform pop in mid-May 2026.
  - **After the peak:**
    - Unlock-driven bleed (XPL circulating +119% YTD).
    - Points-farmer exits (Tria).
    - Security incidents (Avici, Aug 2026).
    - Equity capital capturing the real winners off-chain (RedotPay, Rain, KAST).
  - **Current sentiment** toward neobank tokens: bearish or apathetic. Toward neobank businesses: bullish.
- **x402 / agentic payments**
  - **Peak:** the x402 mini-narrative peaked from late Oct to Dec 2025, driven by meme-mint activity on Base (PING) and a cluster of small-cap "facilitator" and agent tokens.
  - **After the peak:** activity fell about 95–98% by spring 2026 while value per transaction rose. Institutional infrastructure adoption continued (Visa analytics, Lightning spec), but token prices did not follow, apart from the low-float KITE, which peaked in Mar 2026.
  - **Current sentiment:** "real but tiny." The rail is credible but volumes are too small, about $1M per month tracked on-chain, to support token valuations beyond KITE's.
- **Timing pattern.** Each wave peaked within days to weeks of its headline TGE (XPL, HUMA, OOB, PING) or of a broad market top (BTC's mid-Jan 2026 high). That suggests flows were narrative and liquidity-driven rather than usage-driven.

### Gaps
- **Mindshare data.** No Kaito mindshare series, Google Trends or social-volume data was collected, so "mindshare" peaks are inferred from price and on-chain activity only.
- **Narrative research.** No Messari, Delphi or a16z 2026 narrative pieces were collected.
- **Agentic payments protocols.** No 2026 adoption data was collected for Stripe ACP, Google AP2, Visa Intelligent Commerce, the Visa Trusted Agent Protocol or Mastercard Agent Pay, nor any x402 Foundation or V2 updates. The search budget was exhausted. Unverified background from prior knowledge, to be checked:
  - Coinbase launched x402 in May 2025 and set up an x402 Foundation with Cloudflare in Sep 2025.
  - Google's AP2 (Sep 2025) included an A2A x402 extension.
  - OpenAI and Stripe launched ACP and ChatGPT Instant Checkout on 29 Sep 2025.
  - Visa launched Intelligent Commerce in Apr 2025 and the Trusted Agent Protocol in Oct 2025.
  - Mastercard launched Agent Pay in Apr 2025.

## 5. Implications for capital flows into payment-related stablecoin tokens and their remaining upside

### Takeaway
The 2026 evidence shows capital flowing to stablecoin payments as a business, not into payment tokens.

The business side:
- Equity rounds: Rain $1.95B, RedotPay above $1B with an IPO target above $4B, KAST $80M.
- M&A: BVNK up to $1.8B.
- Growing card spend.

The token side:
- The median payment token is about -50% YTD and more than 90% below its ATH, against BTC at -5% YTD.
- Stablecoin supply is flat at about $303B.

Remaining upside is likely confined to a few tokens that combine three things:
1. Measurable fee growth.
2. Explicit value accrual (buybacks or a fee share).
3. A manageable unlock overhang.

On those criteria the candidates are:
- **HUMA:** fees are rising, but they go to liquidity providers, and an insider unlock is due 26 Nov.
- **ETHFI:** fully unlocked and Cash revenue is growing, but buyback execution is unclear.
- **KITE:** the agentic narrative and the best price holder, but 76% of supply is still locked.

New neobank TGEs face a buyer base burned by Tria, Avici, Oobit and PING.

### Cited Findings

#### Equity and M&A side
- Rain: $250M at $1.95B. Source: [The Block](https://www.theblock.co/post/384910/rain-valuation-nears-2-billion-usd-series-c-250-million-raise)
- RedotPay: $194M raised in 2025; IPO talks at more than $1B raised and a valuation above $4B. Source: [Cointelegraph](https://cointelegraph.com/news/redotpay-eyes-us-ipo-1b-4b-valuation)
- KAST: $80M Series A. Source: [Pulse 2.0](https://pulse2.com/kast-80-million-series-a-raised-by-stablecoin-neobank-to-expand-global-financial-platform)
- Mastercard–BVNK: up to $1.8B. Source: [Coin360](https://coin360.com/news/mastercard-bvnk-1-8b-stablecoin-acquisition)
- Zerohash: seeking $1.5B or more. Source: [crypto.news](https://crypto.news/zerohash-seeks-1-5b-valuation-after-mastercard-exit/)

#### Token side
- The CoinGecko Neobank category totals $2.90B and Payment Solutions $2.14B. Native x402 tokens are a few tens of millions of dollars combined, plus KITE at $293M MC / $1.23B FDV. Sources: [CoinGecko Neobank](https://www.coingecko.com/en/categories/neobank); [CoinGecko Payment Solutions](https://www.coingecko.com/en/categories/payment-solutions); [CoinGecko KITE](https://www.coingecko.com/en/coins/kite-2)
- The median 2026 YTD for 17 payment tokens is -49.8%, against BTC -4.7% and ETH -16.9%. Source: CoinGecko (computed; see section 1)

#### Usage and revenue bases versus valuations
These figures come from DefiLlama for the past 365 days unless noted, and the multiples are my own calculations.

**ETHFI**
- FDV: $698M.
- Total ether.fi revenue: about $43.7M, made up of Stake $29.45M, Cash $12.79M and Liquid $1.42M.
- Multiples: about 16x total revenue, and about 55x on Cash revenue alone.
- Sources: [DefiLlama fees overview (revenue)](https://api.llama.fi/overview/fees?excludeTotalDataChart=true&dataType=dailyRevenue); [CoinGecko ETHFI](https://www.coingecko.com/en/coins/ether-fi)

**HUMA**
- FDV: $307M.
- Fees: the Sep 2026 run rate is about $30M per year ($2.50M × 12), about 10x. Protocol revenue is $0 by design.
- Sources: [DefiLlama Huma](https://defillama.com/protocol/huma); [Blockworks Advisory](https://blockworks.com/api/investor-report/huma-finance-protocol-report-h1-2026/pdf)

**XPL**
- FDV: $816M.
- Plasma One spend: about $308M per year at the Sep run rate.
- Plasma chain fees: $154k over 365 days.
- Sources: [DefiLlama Plasma One](https://defillama.com/protocol/plasma-one); [CoinGecko XPL](https://www.coingecko.com/en/coins/plasma)

**TRIA**
- FDV: $24.8M.
- Tria Card fees: about $0.26M per year at the current 30-day rate, down from $2.36M over the past year.
- Source: [DefiLlama Tria Card](https://defillama.com/protocol/tria-card)

**AVICI**
- FDV: $3.4M.
- Card fees: $72k per year.
- Card volume: about $3–4M per year at the current rate.
- Source: [DefiLlama Avici](https://defillama.com/protocol/avici)

**KITE**
- FDV: $1.23B.
- Total DefiLlama-tracked x402 volume: about $12M per year at the current rate. That covers the whole ecosystem, not Kite specifically.
- Source: [DefiLlama x402](https://defillama.com/protocol/x402)

#### Stablecoin base
- Total stablecoin supply is flat in 2026: $303.7B on 1 Jan and $303.4B on 21 Oct. Wallet-issued stablecoins are small: Phantom CASH $127.7M and MetaMask mUSD $33.8M. Source: [DefiLlama stablecoins](https://defillama.com/stablecoins)

### Inferences
- **Equity captures the value.** The highest-quality payment businesses (RedotPay, Rain, KAST, BVNK, Zerohash) are financed by equity at rising valuations. Token holders get exposure mainly to the second tier and to chain-level stories (XPL, STABLE). This structurally limits how much capital can flow into "payment tokens." Investors wanting the stablecoin-payments theme can get it through equity, IPOs (RedotPay, Consensys) or M&A rather than tokens.
- **Supply, not demand, is the binding constraint.** Unlock schedules (XPL about 30% of float over the next six months by inference; the HUMA first insider unlock; KITE and TRIA anniversaries) will absorb inflows. Cashback paid in native tokens (XPL) adds continuous sell pressure. Positive price drift needs fee-funded buybacks larger than emissions; none of the neobank tokens has demonstrated this in 2026, and ETHFI's buyback status is disputed.
- **Usage does not equal token value.** Huma (volume up 149% YoY but token revenue zero by design) and ether.fi Cash (spend up 2.4x but only about 1.4% take and uncertain buybacks) show that strong real usage translates weakly into token value. Tokens that get explicit fee switches or buybacks could re-rate if market beta turns.
- **Remaining upside by bucket:**
  - **Mid-caps with fundamentals.** ETHFI and HUMA have the most defensible bull cases: fee growth, high staking or full unlock. Both need a value-accrual catalyst. For HUMA, the catalyst is a fee switch or staking rewards from fees; for ETHFI, verified buybacks. Both need to clear supply events, chiefly the HUMA unlock on 26 Nov 2026.
  - **Chain-level payment tokens.** XPL and STABLE trade on chain narratives more than card usage. XPL's FDV ($816M) is about 5,300x its chain fees, and its float is still growing about 5% per month by inference, which caps upside absent a demand shock.
  - **x402 and agentic.** KITE is the only liquid vehicle. Its FDV of $1.23B is far ahead of measurable x402 usage (about $1M per month tracked), so it is a narrative or beta trade, exposed to the Nov 2026 anniversary-cliff risk (speculative).
  - **Micro-caps** (TRIA, AVICI, OOB, PING, PAYAI and other x402 or neobank tags). These are option-like and illiquid, with demonstrated post-TGE usage collapse in Tria's case and security risk in Avici's. They are unlikely to attract institutional flows.
- **Pipeline flows.** With MetaMask, Phantom, Rabby, Base and Tempo all at 4–9% odds for 2026, the next major payments-related airdrop catalyst is likely 2027 or later. KAST (16.5% by end-2026) is the most plausible near-term neobank TGE, and its reception will be judged against the Tria and Avici precedents.
- **Capital flows toward winning card issuers through their partners.** Rain's model shows that card-issuing infrastructure accrues value regardless of which neobank token wins, but it also concentrates counterparty and security risk (Avici hack). Card spend is also concentrated in RedotPay, Nexo and ether.fi (86% of tracked 30-day volume). Token investors should expect value to accrue to issuers and processors (Visa had more than 90% of on-chain card volume per Artemis), not to app tokens.

### Gaps
- **Fund-flow data.** No direct data on exchange inflows, wallet cohorts or holder concentration for these tokens. "Capital flow" is inferred from price, market cap, supply and equity deal data.
- **Buyback and fee-switch roadmaps.** No verified 2026 buyback numbers for ETHFI, and no fee-switch roadmap for HUMA. No public data on XPL cashback emissions.
- **Unverified unlock sizes.** The Nov 2026 HUMA unlock size, the KITE and TRIA cliff structures, and the XPL post-cliff schedule were inferred or unverified, because Tokenomist and CryptoRank were blocked.
- **No mindshare or sentiment data.** No Kaito, LunarCrush or funding-rate data, so current sentiment is inferred from price behavior and news tone.
