# RWA/T-bill-backed, credit-backed and CDP stablecoins and stablecoin-issuer tokens: 2026 fact base (as of 21 Oct 2026)

Scope and method notes (read first):
- Most numbers come from public APIs pulled on **21 Oct 2026, about 13:20–13:40 UTC**. Each figure links to the exact API endpoint.
  - **CoinGecko** `coins/markets` snapshot, last_updated 2026-10-21T13:24:53Z: price, circulating market cap (MC), fully diluted valuation (FDV), all-time high (ATH), circulating and total supply.
  - **DefiLlama coins API**: first recorded price (used as a proxy for the listing price), the 1 Jan 2026 price (timestamp 1767225600), and the 2026 daily high and low.
  - **DefiLlama stablecoins API**: supply histories.
  - **DefiLlama protocol API**: TVL histories.
  - **DefiLlama fees/revenue overview**: trailing 1-year and 30-day fees, revenue and holders revenue.
  - **DefiLlama yields**: current APYs.
- "First print" means DefiLlama's first recorded price. It is a proxy for the listing price, not an official listing price.
- **MC is circulating market cap. FDV is total or max supply × price.** The two are reported separately throughout.
- The shared web-search budget for this session ran out partway through. After that I only fetched specific, already-known URLs and public data APIs; I ran no further searches. Some qualitative items therefore stay unverified and are listed under Gaps.
- Huma is excluded per the brief. Ethena (ENA, USDe) and Falcon (FF, USDf) appear only as benchmarks.

## Q1. Token-level facts: TGE, sale and listing price/FDV, ATH, current price, MC vs FDV, YTD 2026, % vs listing and ATH, airdrops, unlocks

### Takeaway
Only one of the 12 late-2025/2026 TGEs tracked here trades above its first print: CAP (+150%). The median is about −81% below first print.

Among the 21 older tokens that existed on 1 Jan 2026, the median YTD return is −44%, and only six are positive:
- SKY +33%
- ONDO +29%
- PLUME +10%
- FXN +10%
- CRV +9%
- AAVE +7%

Small-cap CDP and yield-protocol governance tokens fell 45–90%. Examples are RIVER, DAM, YB, AVL, INV, FRAX, USUAL, RSUP and LISTA.

### Cited Findings

#### 1A. Status check of the seed list (verified vs not)
- **WLFI**: tradable since 1 Sep 2025. First print $0.2811 on 2025-09-01 ([DefiLlama first](https://coins.llama.fi/prices/first/coingecko:world-liberty-financial)). CoinGecko learn cited an "initial launch price of $0.31" ([CoinGecko Learn](https://www.coingecko.com/learn/world-liberty-financial-buyback-proposal-underway)). [High]
- **USUAL**: first print $1.096 on 2024-11-18 ([DefiLlama first](https://coins.llama.fi/prices/first/coingecko:usual)). USD0++ was renamed bUSD0 via UIP-12 on 10 Dec 2025 ([Usual blog index](https://usual.money/blog)). [High]
- **EDEN (OpenEden)**: first print $0.5358 on 2025-09-30 ([DefiLlama first](https://coins.llama.fi/prices/first/coingecko:openeden)). Exchange guides describe an airdrop "live (Sept 30)" ([BingX](https://bingx.com/en/learn/article/openeden-airdrop-guide-how-to-claim-eden-tokens)). [High]
- **DAM (Reservoir)**: first print $0.1196 on 2025-08-18 ([DefiLlama first](https://coins.llama.fi/prices/first/coingecko:reservoir)). [High]
- **CAP (Cap)**: TGE 26 Jun 2026. About 15.6% of supply circulated at launch, and CAP traded more than $355M in volume in its first 7 days ([Bitget/CryptoBriefing, 7 Jul 2026](https://www.bitget.com/news/detail/12560605494177)). [High]
- **CHIP (USD.AI)**: USD.AI's 22 Apr 2026 post says CHIP "went live yesterday" (about 21 Apr 2026) ([USD.AI](https://usd.ai/insights/chip-is-live)). DefiLlama's first print is also 2026-04-21 ([DefiLlama first](https://coins.llama.fi/prices/first/coingecko:chip-2)). ICO Drops instead says the TGE "concluded on Mar 30, 2026", which conflicts ([ICO Drops](https://icodrops.com/usd-ai/)). [High that trading began ~21 Apr]
- **RE (Re, reinsurance)**: TGE 18 Jun 2026 on Binance, Robinhood, OKX, Bybit, KuCoin and others ([re.xyz](https://re.xyz/insights/re-tge-launch)). [High]
- **GROVE (Sky Star)**: distribution via Sky Ecosystem Rewards started 6–7 Jul 2026 ([Sky blog, 7 Jul 2026](https://sky.money/blog/grove-sky-ecosystem-rewards)). First print 2026-07-06 ([DefiLlama first](https://coins.llama.fi/prices/first/coingecko:grove-2)). [High]
- **SPK (Spark)**: first print $0.0571 on 2025-06-17 ([DefiLlama first](https://coins.llama.fi/prices/first/coingecko:spark-2)). [High]
- **Keel and Obex (Sky Stars)**: Keel's own 2026 post mentions no Keel token ([Keel Substack, 23 Feb 2026](https://keelfi.substack.com/p/keel-in-2026-expanding-the-mandate)).
  - CoinGecko ids "keel" (MC $7.5k) and "obex" (MC $5k) exist but are almost certainly unrelated microcaps ([CoinGecko](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=keel,obex)). [Medium]
- **M0, Agora, Midas**: I found no tradable governance token for any of them.
  - CoinGecko search for "midas" returns only Midas yield tokens (mTBILL, mF-ONE, etc.).
  - Agora's only listing is AUSD ([CoinGecko markets](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=agora-dollar)). [Medium]
- **infiniFi (INFI) and 3Jane (JANE)**: still pre-TGE (details in Q5).
- **Apyx (APYX)**: CoinGecko shows a "preview listing" with 100M total supply and no price as of 21 Oct 2026 ([CoinGecko coin API](https://api.coingecko.com/api/v3/coins/apyx)). A planned 13 Oct 2026 TGE was announced ([Today in DeFi, 27 May 2026](https://news.todayindefi.com/p/airdrop-alpha-re-protocol-announced)). Live trading is unverified.
- **Avant**: a CoinGecko id exists with no market data ([CoinGecko](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=avant)). Treat as pre-TGE.
- **Name collision**: "reUSD" is both Re's reinsurance-backed token ([CoinGecko re-protocol-reusd](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=re-protocol-reusd)) and Resupply's CDP stablecoin ([DefiLlama id 256](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=256)).
- **Frax**: FXS was renamed FRAX. The governance token is CoinGecko id `frax-share` (symbol FRAX), while id `frax` is the legacy FRAX stablecoin ([CoinGecko](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=frax,frax-share)).

#### 1B. Recently TGE'd tokens (late 2025 – 2026)

Prices, MC and FDV are as of 21 Oct 2026 13:24 UTC (CoinGecko). First print and 1 Jan prices are from DefiLlama.

| Token (project) | First print (date) → FDV at first print | Sale / ICO terms | ATH (date) | Price 21-Oct-26 | Circ MC / FDV | YTD 2026 | vs first print | vs ATH | Sources |
|---|---|---|---|---|---|---|---|---|---|
| WLFI (World Liberty; USD1) | $0.2811 (2025-09-01) → $28.1B (100B supply) | n/a (presale prices not verified) | $0.3313 (2025-09-01) | $0.05648 | $1,795M / $5,647M (circ 31.78B of 100B) | −60.6% (1-Jan $0.1433) | −79.9% | −83.0% | [CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=world-liberty-financial) · [first](https://coins.llama.fi/prices/first/coingecko:world-liberty-financial) · [1-Jan](https://coins.llama.fi/prices/historical/1767225600/coingecko:world-liberty-financial) |
| EDEN (OpenEden) | $0.5358 (2025-09-30) → $536M; next-day close $0.4016 | n/a | $1.31 (2025-09-30) | $0.0600 | $26.2M / $60.0M (circ 435.9M of 1B) | −8.4% (1-Jan $0.0655) | −88.8% | −95.4% | [CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=openeden) · [first](https://coins.llama.fi/prices/first/coingecko:openeden) · [1-Jan](https://coins.llama.fi/prices/historical/1767225600/coingecko:openeden) |
| DAM (Reservoir) | $0.1196 (2025-08-18) → $120M | n/a | $0.1489 (2025-09-18) | $0.003604 | $1.0M / $3.6M (circ 277.5M of 1B) | −85.4% (1-Jan $0.0248) | −97.0% | −97.6% | [CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=reservoir) · [first](https://coins.llama.fi/prices/first/coingecko:reservoir) |
| RIVER (River; satUSD Omni-CDP) | $1.87 (2025-09-22) → $187M | n/a | $87.73 (2026-01-26) | $1.11 | $21.8M / $111.1M (circ 19.6M of 100M) | −90.6% (1-Jan $11.81) | −40.6% | −98.7% | [CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=river) · [first](https://coins.llama.fi/prices/first/coingecko:river) |
| YB (Yield Basis; crvUSD-levered) | $0.6928 (2025-10-15) → $693M (1B max) | n/a | $0.8185 (2025-10-15) | $0.06448 | $17.7M / $48.8M | −83.9% (1-Jan $0.4001) | −90.7% | −92.1% | [CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=yield-basis) · [first](https://coins.llama.fi/prices/first/coingecko:yield-basis) |
| GAIB (GAIB; AID) | $0.1504 (2025-11-19) → $150M | n/a | $0.2494 (2025-11-19) | $0.01988 | $4.1M / $19.9M | −28.2% (1-Jan $0.0277) | −86.8% | −92.0% | [CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=gaib) · [first](https://coins.llama.fi/prices/first/coingecko:gaib) |
| MEZO (Mezo; MUSD BTC-CDP) | $0.0662 (2026-04-01) → $66M | n/a | $0.1485 (2026-04-13) | $0.002848 | $1.4M / $2.8M (circ 500M of 1B) | n/a | −95.7% | −98.1% | [CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=mezo) · [first](https://coins.llama.fi/prices/first/coingecko:mezo) |
| CHIP (USD.AI; USDai) | $0.0609 (2026-04-21) → $609M; day-2 close $0.1152 | CoinList ICO 22–27 Feb 2026 at $0.03 (FDV $300M), 700M CHIP = 7% of supply, 100% unlocked at TGE; raised $19.4M | $0.1402 (2026-04-23) | $0.04567 | $91.4M / $457.1M (circ 2.0B of 10B) | n/a | −24.9% (vs ICO +52%) | −67.4% | [CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=chip-2) · [first](https://coins.llama.fi/prices/first/coingecko:chip-2) · [USD.AI ICO](https://usd.ai/insights/chip-ico-airdrop) · [ICO Drops](https://icodrops.com/usd-ai/) |
| SLX (Solstice; USX) | $0.2900 (2026-05-25) → $290M | n/a | $0.6582 (2026-06-27) | $0.05036 | $12.2M / $50.3M (circ 242.8M of 1B) | n/a | −82.6% | −92.3% | [CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=solstice) · [first](https://coins.llama.fi/prices/first/coingecko:solstice) |
| RE (Re; reUSD) | $0.4748 (2026-06-18) → $475M (1B supply) | not disclosed | ~$0.9985 daily high (2026-06-21) | $0.3944 | MC not on CoinGecko; ≥159.6M liquid at TGE (≥~$63M at today's price) / FDV ~$394M | n/a | −17.0% | ~−60% | [DL price](https://coins.llama.fi/prices/current/ethereum:0x526526528f35ac738177003b8773b402b8df8143) · [DL first](https://coins.llama.fi/prices/first/ethereum:0x526526528f35ac738177003b8773b402b8df8143) · [re.xyz](https://re.xyz/insights/re-tge-launch) |
| CAP (Cap; cUSD) | $0.02718 (2026-06-26) → $272M; ~15.6% circulating at launch ≈ $42M MC | Uniswap ICO ended 16 Feb 2026 at $0.01065 (400M CAP = 4%, $4.22M raised, implied FDV $106.5M); auction ended 17 Jun 2026 with floor FDV $75M (ICO Drops) | $0.1208 (2026-10-12) | $0.0680 | $106.1M / $679.9M (circ 1.56B of 10B) | n/a | +150.2% (vs Feb ICO +538%) | −43.7% | [CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=cap-4) · [first](https://coins.llama.fi/prices/first/coingecko:cap-4) · [ICO Drops](https://icodrops.com/cap-3/) |
| GROVE (Grove, Sky Star) | $0.01679 (2026-07-06) → $168M | none (emitted to USDS suppliers) | $0.04463 (2026-07-06) | $0.005027 | $4.4M / $50.3M (circ 873.9M of 10B) | n/a | −70.1% | −88.7% | [CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=grove-2) · [first](https://coins.llama.fi/prices/first/coingecko:grove-2) |
| Benchmark: FF (Falcon) | $0.649 (2025-09-29) → $6.49B; next-day close $0.189 | — | $0.7708 (2025-09-29) | $0.1091 | $364.9M / $1,091M | +26.6% | −83.2% | −85.8% | [CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=falcon-finance-ff) |

Other sale and launch details:
- **CHIP refund protection.** Before the token went live, "Protected $CHIP" was set to unlock at YT maturity (17 Jun and/or 14 Oct 2026) and "settle at $270M / $190M FDV", with the price difference refunded in USDC. A refund at $300M FDV was available at any time, forfeiting the CHIP ([USD.AI](https://usd.ai/insights/chip-is-live)).
- **CHIP venues.** Spot listings included Upbit, Binance, Bybit, Bithumb, Robinhood, Coinbase, Bitvavo, KuCoin, MEXC, HTX and Gate. Perps listed on Binance, OKX, Bitget, Hyperliquid and Lighter ([USD.AI](https://usd.ai/insights/chip-is-live)).
- **CHIP airdrop.** 300M CHIP (3% of supply), sent automatically at TGE. Allo points were burned for wallets with no "alignment" when Season 1 ended on 18 Feb 2026 ([search summary of USD.AI/CoinList materials](https://usd.ai/insights/chip-ico-airdrop); [USD.AI](https://usd.ai/insights/chip-ico-airdrop)).
  - The 3% figure comes from search-result summaries; the USD.AI page I opened does not state the airdrop percentage. [Medium]
- **CAP's earlier sale plan.** The Defiant reported a planned token sale at a "$250 million valuation" for 10% of supply, which was supposed to fund the cUSD "Stabledrop" ([The Defiant](https://thedefiant.io/news/defi/cap-cuts-its-stabledrop-airdrop-to-usd4-2m-from-usd12m-as-backlash-mounts)).
  - This conflicts with ICO Drops' figures ($0.01065 Uniswap ICO; $75M floor-FDV auction). Treat the sale terms as [Medium/Low].
- **CAP Stabledrop.** Cap ended its "Frontier" phase on 4 Feb 2026 by distributing 12M cUSD ([The Defiant](https://thedefiant.io/news/defi/cap-airdrops-usd12-million-in-stablecoins-to-early-users)).
  - It was later cut to $4.2M. The founder apologized for committing to a figure "before the funding to back it was fully secured" ([The Defiant](https://thedefiant.io/news/defi/cap-cuts-its-stabledrop-airdrop-to-usd4-2m-from-usd12m-as-backlash-mounts)).
  - Caps points were "expected to convert to a future Cap token at TGE" ([Today in DeFi, 27 May 2026](https://news.todayindefi.com/p/airdrop-alpha-re-protocol-announced)).
- **RE tokenomics.** 1B fixed supply ([re.xyz](https://re.xyz/insights/re-tge-launch)):
  - Ecosystem 50%: 159.6M liquid at TGE, remainder linear over 48 months.
  - Ecosystem Development Reserve 13%.
  - Investors 17%: 12-month cliff, then 36 months linear.
  - Core Contributors 20%: 12-month cliff, then 36 months linear.
- **RE Season 1 airdrop.** Wallets with up to 150M points claimed everything on 18 Jun 2026. Larger wallets got the first 150M plus 10% of the remainder, with the rest in six six-monthly tranches over 3 years. Full first-tranche claims require keeping the Season 1 TVL baseline, and shortfalls are prorated ([re.xyz](https://re.xyz/insights/re-tge-launch)).
  - Yearn counts about 10,170 holders at launch and about 16% circulating ([Yearn risk report](https://github.com/yearn/risk-score/blob/master/reports/report/re-reusd.md)).
- **GROVE.** Fixed supply of 10B. Allocation is 70% Sky Ecosystem, 25% team and contributors, 5% Grove Foundation. It listed on Coinbase, Bybit, KuCoin and Bitvavo on 7 Jul (search summary citing Messari/Blockworks: [Messari](https://messari.io/project/sky-protocol), [Blockworks filing](https://blockworks.com/token-transparency/filing/grove-finance)). [Medium]
  - GROVE is not available in the US ([Sky blog](https://sky.money/blog/grove-sky-ecosystem-rewards)).
- **WLFI price context.** WLFI fell nearly 6% to about $0.054 on 20 Oct 2026 as USD1 supply shrank by $401M ([Coinpaper](https://coinpaper.com/37601/wlfi-price-falls-6-as-trump-linked-usd-1-stablecoin-sees-401-m-in-redemptions)). CoinGecko's WLFI ATL is $0.04828 on 2026-09-11 ([CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=world-liberty-financial)).

2026 daily high and low, from DefiLlama charts ([example WLFI](https://coins.llama.fi/chart/coingecko:world-liberty-financial?start=1767225600&span=294&period=1d); same endpoint pattern for each id):

| Token | 2026 high | 2026 low |
|---|---|---|
| WLFI | $0.1803 (13 Jan) | $0.0513 (9 Aug) |
| EDEN | $0.1227 (21 May) | $0.0260 (29 Mar) |
| DAM | $0.0621 (12 Apr) | $0.00154 (8 Sep) |
| RIVER | $85.53 (27 Jan) | $1.02 (18 Oct) |
| CHIP | $0.1128 (23 Apr) | $0.0217 (9 Aug) |
| CAP | $0.0971 (12 Oct) | $0.0160 (12 Jul) |
| SLX | $0.576 (28 Jun) | $0.0477 (18 Oct) |
| GROVE | $0.0318 (6 Jul) | $0.0052 (20 Oct) |
| MEZO | $0.1027 (13 Apr) | $0.0028 (16 Oct) |

#### 1C. Established tokens in scope (as of 21 Oct 2026, CoinGecko; YTD uses DefiLlama 1-Jan prices)

| Token | Price | Circ MC / FDV | ATH (date) | vs ATH | 1-Jan-26 price | YTD | 2026 high / low (DefiLlama daily) | Sources |
|---|---|---|---|---|---|---|---|---|
| SKY | $0.07664 | $1,796M / $1,797M | $0.10087 (2026-10-05) | −24.0% | $0.05761 | **+33.0%** | $0.0973 (5 Oct) / $0.0493 (27 Jun) | [CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=sky) · [1-Jan](https://coins.llama.fi/prices/historical/1767225600/coingecko:sky) |
| ONDO | $0.4624 | $2,252M / $4,624M (circ 4.87B of 10B) | $2.14 (2024-12-15) | −78.4% | $0.3586 | **+29.0%** | $0.5877 (28 Sep) / $0.2252 (6 Feb) | [CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=ondo-finance) · [1-Jan](https://coins.llama.fi/prices/historical/1767225600/coingecko:ondo-finance) |
| PLUME | $0.01816 | $123.9M / $181.7M | $0.2475 (2025-03-19) | −92.7% | $0.01655 | +9.8% | $0.0227 (12 Oct) / $0.0090 (1 Mar) | [CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=plume) |
| FXN (f(x)) | $26.01 | $4.3M / $32.2M (CG circ 164k of 1.24M total; likely excludes locked veFXN) | $219.95 (2024-03-13) | −88.2% | $23.71 | +9.7% | $34.71 (4 Oct) / $10.24 (31 Jul) | [CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=fxn-token) |
| CRV (crvUSD) | $0.3913 | $618.4M / $950.0M | $15.37 (2020) | −97.5% | $0.3588 | +9.1% | $0.4372 (16 Jan) / $0.1815 (5 Jun) | [CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=curve-dao-token) |
| AAVE (GHO) | $156.14 | $2,410M / $2,498M | $661.69 (2021) | −76.4% | $146.17 | +6.8% | $184.06 (6 Oct) / $60.88 (7 Jun) | [CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=aave) |
| SPK (Spark) | $0.01977 | $66.7M / $197.8M (circ 3.37B of 10B) | $0.1845 (2025-07-23) | −89.3% | $0.02099 | −5.8% | $0.0520 (24 Apr) / $0.0132 (18 Aug) | [CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=spark-2) |
| SYRUP (Maple) | $0.2043 | $238.5M / $259.1M | $0.6532 (2025-06-25) | −68.7% | $0.3219 | −36.5% | $0.3995 (12 Jan) / $0.1212 (25 Jun) | [CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=syrup) |
| LQTY (Liquity) | $0.2105 | $20.8M / $21.0M | $146.94 (2021) | −99.9% | $0.3784 | −44.4% | $0.4240 (16 Jan) / $0.1575 (20 Jul) | [CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=liquity) |
| LISTA | $0.0794 | $34.2M / $63.2M | $0.8428 (2024-06-20) | −90.6% | $0.1717 | −53.7% | $0.1835 (6 Jan) / $0.0442 (24 Jul) | [CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=lista) |
| RSUP (Resupply) | $0.1042 | $3.0M / $8.1M | $4.59 (2025-03-20) | −97.7% | $0.2291 | −54.5% | $0.3167 (3 Jan) / $0.0573 (18 Jul) | [CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=resupply) |
| USUAL | $0.01096 | $21.6M / $21.7M (circ 1.975B; CG max 3B) | $1.61 (2024-12-19) | −99.3% | $0.02454 | −55.3% | $0.0308 (17 Jan) / $0.0076 (30 Jul) | [CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=usual) |
| FRAX (ex-FXS, id frax-share) | $0.2614 | $24.5M / $26.1M | $42.8 (2022, as FXS) | −99.4% | $0.6427 | −59.3% | $1.253 (19 Jan) / $0.228 (30 Jun) | [CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=frax-share) |
| INV (Inverse; DOLA) | $11.39 | $8.1M / $8.3M | $2,075 (2021) | −99.5% | $28.24 | −59.7% | $30.44 (6 Jan) / $8.37 (10 Aug) | [CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=inverse-finance) |
| AVL (Avalon; USDa) | $0.01958 | $8.8M / $19.6M | $0.787 (2025-03-07) | −97.5% | $0.0760 | −74.2% | $0.0884 (6 Jan) / $0.0152 (18 Aug) | [CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=avalon-2) |
| Benchmark: ENA | $0.2078 | $2,786M / $3,118M | $1.52 (2024) | −86.3% | $0.1997 | +4.1% | $0.2722 (28 Sep) / $0.0712 (1 Jul) | [CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=ethena) |

#### 1D. Supply overhang and known unlocks
- **Locked or uncirculated supply as % of circulating** (CoinGecko total-or-max minus circulating, as of 21 Oct 2026; [CG snapshot](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=world-liberty-financial,cap-4,chip-2,grove-2,spark-2,ondo-finance,openeden,plume,syrup,sky)):

| Overhang | Tokens |
|---|---|
| Under 10% (fully or nearly fully circulating) | SKY ~0.1%, LQTY ~1.2%, AAVE ~3.6%, FRAX (gov) ~6.5%, SYRUP ~8.6% |
| Moderate | PLUME ~47%, CRV ~54% vs total (2.43B) |
| Around 100–130% | MEZO 100%, ONDO ~105%, EDEN ~129% |
| Around 200% | SPK ~196%, WLFI ~215% |
| Around 260–410% | DAM ~260%, SLX ~312%, GAIB ~388%, CHIP 400%, RIVER ~410% |
| Above 500% | CAP ~541%, GROVE ~1,044% |

- **SKY emissions.** The Feb 2026 executive created a new staking-reward vest stream of **838,182,330 SKY over 180 days** ([Sky executive, 26 Feb 2026](https://vote.sky.money/executive/template-executive-vote-launch-agent-onboardings-january-monthly-settlement-cycle-and-treasury-management-function-sky-staking-rewards-normalization-prime-agent-proxy-spells-february-26-2026)). That is about 3.6% of the 23.43B circulating supply ([CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=sky)).
- **RE.** Investor and contributor cliffs (12 months from 18 Jun 2026) fall outside the next six months. The Ecosystem allocation unlocks linearly, and the first Season 1 vesting tranche falls about 6 months after TGE, around mid-Dec 2026 ([re.xyz](https://re.xyz/insights/re-tge-launch)).
- **CHIP.** "Protected" CHIP from the Level Up program unlocked at the 17 Jun and 14 Oct 2026 YT maturities ([USD.AI](https://usd.ai/insights/chip-is-live)). Search summaries say US accredited ICO buyers have a 1-year lock from TGE (around Mar–Apr 2027) ([ICO Drops](https://icodrops.com/usd-ai/)). [Medium]
- **GROVE.** Distribution "follows a schedule set by Sky Governance", with continuous emission to USDS suppliers ([Sky blog](https://sky.money/blog/grove-sky-ecosystem-rewards)).

### Inferences
- The tape for 2026 TGEs was poor. Of the six 2026 TGEs (MEZO, CHIP, SLX, RE, CAP, GROVE), the median is about −48% vs first print; across all 12 late-2025/2026 TGEs it is about −81%.
  - Tokens sold to ICO buyers at a low FDV (CHIP at $300M, CAP at about $75–107M) are the only ones where early public buyers are in profit. CHIP is +52% vs its ICO price and CAP is +538%.
  - This suggests the sale structure (low FDV, refund protection, auctions) mattered more than sub-sector.
- CAP's rally from a $0.0155 low (12 Jul) to a $0.1208 ATH (12 Oct) came while cUSD supply was shrinking (Q2). Only about 15.6% of CAP circulates, so this looks like a float- and liquidity-driven move rather than a fundamentals re-rating. [Medium]
- Many tokens bottomed together between 5 Jun and 31 Jul 2026 (AAVE, CRV, ENA, SKY, SYRUP, CAP, FF) and peaked again in Sep–Oct. This points to a market-wide drawdown in mid-2026; the cross-section is not purely idiosyncratic.

### Gaps
- No unlock calendars (Tokenomist, CryptoRank, DefiLlama unlocks) could be retrieved: they returned 403 or require a paid plan. So I cannot give exact 21 Oct 2026 – 21 Apr 2027 unlock amounts as % of circulating for WLFI, ONDO, SPK, PLUME, EDEN, CHIP, CAP, SYRUP, FF or LISTA.
  - Unverified memory: WLFI's remaining early-supporter tokens are subject to a governance vote, and ONDO unlocks annually in January. Both need confirmation.
- WLFI presale prices, USUAL/EDEN/DAM exchange venues, and EDEN/DAM airdrop sizes could not be verified after the search budget ran out.
- RE's current circulating supply and market cap are not on CoinGecko.
- The cause of RIVER's ~47× run to $87.73 (26 Jan 2026) and its −98.7% collapse is unknown.
- The cause of the FRAX governance token's −59% YTD (after doubling to $1.25 in January) is unknown.
- CoinGecko's `frax-share` id may track the Ethereum-bridged FRAX rather than Fraxtal-native FRAX. [Medium-Low]

## Q2. Stablecoin supply and TVL: 1 Jan 2026, 2026 peak, latest; yields; depeg and redemption episodes

### Takeaway
Total stablecoin supply was flat in 2026: $305.0B on 1 Jan and $305.2B on 21 Oct, with a $317.1B peak on 17 May and a $299.9B low on 11 Aug. Growth was therefore a reshuffle of share between issuers.

Inside this scope:
- **Grew:** USD1 (+19.5%, but −25.5% from its Feb peak), USDS+DAI (+10.6%), GHO (+41%), fxUSD (+142%), Maple TVL (+17.5%).
- **Shrank 60–80% from peaks:** credit-backed or points-driven coins (cUSD −76% YTD, USDai −60%, iUSD −62%) and several RWA/T-bill issuers (USDO −81%, M −76%, Plume pUSD −76%).
- **Grew fastest:** new token-less issuers, such as United Stables U ($1.59B), USDGO ($1.30B) and Open USD ($0.83B).

### Cited Findings

#### 2A. Market backdrop (DefiLlama, USD terms)
- **Total stablecoins**: $305.03B (1 Jan 2026) → peak $317.09B (17 May) → low $299.87B (11 Aug) → $305.16B (21 Oct 2026), +0.04% YTD ([DefiLlama all](https://stablecoins.llama.fi/stablecoincharts/all)).
- **USDT**: $187.26B → peak $190.43B (20 May) → $182.91B, −2.3% ([DL id 1](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=1)).
- **USDC**: $75.31B → peak $79.63B (18 Mar) → $72.25B, −4.1% ([DL id 2](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=2)).
- **Token-less issuers that won share (1 Jan → 2026 peak → now):**

| Stablecoin | 1 Jan 2026 | 2026 peak (date) | 21 Oct 2026 | YTD | Source |
|---|---|---|---|---|---|
| USDG | $1.23B | $3.44B (12 May) | $3.06B | +149% | [DL 286](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=286) |
| RLUSD | $1.28B | $2.53B (8 Oct) | $2.40B | +88% | [DL 250](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=250) |
| BUIDL | $1.48B | $2.88B (15 Jul) | $2.19B | +47% | [DL 173](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=173) |
| YLDS | $0.33B | $0.69B (24 Aug) | $0.50B | +51% | [DL 272](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=272) |
| PYUSD | $3.60B | $4.21B (5 Mar) | $2.86B | −20.5% | [DL 120](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=120) |

- **CoinGecko sector market caps** (21 Oct 2026 13:17 UTC; [CoinGecko categories](https://api.coingecko.com/api/v3/coins/categories)):

| CoinGecko category | Market cap |
|---|---|
| Stablecoins | $297.8B |
| Tokenized Treasuries | $9.32B |
| Stablecoin Issuer (tokens) | $9.86B |
| RWA Protocol | $13.22B |
| Synthetic Dollar | $6.78B |
| Crypto-backed Stablecoin | $5.11B |
| Yield-Bearing Stablecoin | $3.05B |
| US Treasury-backed Stablecoin | $2.37B |
| Midas Liquid Yield Tokens | $0.26B |

#### 2B. Fiat/T-bill/RWA issuers (DefiLlama supply unless noted)

| Stablecoin (issuer token) | 1 Jan 2026 | 2026 peak (date) | 21 Oct 2026 | YTD | Notes | Source |
|---|---|---|---|---|---|---|
| USD1 (WLFI) | $3,361M | **$5,389M (11 Feb)** | $4,016M | +19.5% (−25.5% from peak) | Chain mix: Solana $115M→$1,398M; BSC $1,916M→$1,192M; Ethereum $1,224M→$1,377M | [DL 262](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=262) · [chains](https://stablecoins.llama.fi/stablecoin/262) |
| USD0 (USUAL) | $547.5M | $599.4M (18 Jan) | $542.0M | −1.0% | ATH $1,862M (7 Jan 2025). bUSD0 pool $502.9M, APY 5.23% (all USUAL rewards). Usual USD0 TVL $149.6M→$83.1M | [DL 195](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=195) · [yields](https://yields.llama.fi/pools) · [TVL](https://api.llama.fi/protocol/usual-usd0) |
| USDO (EDEN) | $77.1M | $77.1M (4 Jan) | $14.5M | **−81.1%** | ATH $298.8M (21 Jul 2025). USDO APY 3.45%. TBILL pool $20.8M at 3.59% | [DL 241](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=241) · [yields](https://yields.llama.fi/pools) |
| M by M0 (no token found) | $872.8M | $874.3M (20 Jan) | $206.9M | **−76.3%** | M on Arbitrum $690.7M→$0.2M; Ethereum $125.3M→$171.8M; Noble $39.7M→$1.4M; Monad $0→$17.7M. M0 TVL $879M→$212M | [DL 213](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=213) · [chains](https://stablecoins.llama.fi/stablecoin/213) · [TVL](https://api.llama.fi/protocol/m0) |
| mUSD (MetaMask, on M0) | $23.4M | $40.0M (13 Oct) | $32.2M | +37.6% | ATH $89.4M (15 Oct 2025). Issued by Bridge (Stripe) via M0 | [DL 313](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=313) · [Pharos](https://pharos.watch/stablecoin/musd-metamask/) |
| USDN (Noble, on M0) | $39.7M | $39.7M (3 Jan) | $1.4M | −96.3% | effectively wound down (cause not verified) | [DL 282](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=282) |
| AUSD (Agora, no token) | $216.1M | $296.9M (5 Sep) | $213.7M | −1.1% | ATH $359.5M (28 Nov 2025) | [DL 205](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=205) |
| USDY (ONDO) | n/a | n/a | MC $2,357M (2.051B tokens × $1.15) | n/a | APY 3.71%. Pool TVLs: Ethereum $1,261M, Stellar $538M, Sei $260M | [CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=ondo-us-dollar-yield) · [yields](https://yields.llama.fi/pools) |
| USDon (Ondo) | $0 | $90.4M (25 Aug) | $64.8M | new | — | [DL 408](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=408) |
| rUSD / srUSD (DAM) | Reservoir TVL $81.9M | **TVL $237.5M (12 Apr)** | TVL $70.4M | −14% | TVL low $20.1M (1 Sep). ATH TVL $389.8M (26 Oct 2025). DefiLlama tracks only $0.2M "circulating" rUSD (likely unstaked only). wsrUSD pool $113.1M at 6.00% | [TVL](https://api.llama.fi/protocol/reservoir-protocol) · [DL 217](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=217) · [yields](https://yields.llama.fi/pools) |
| pUSD (PLUME) | $8.7M | $17.5M (21 Feb) | $2.1M | −75.7% | ATH $50.6M (Jun 2025). Plume Vaults TVL $44.3M→$227.7M (+415%) | [DL 266](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=266) · [TVL](https://api.llama.fi/protocol/plume-vaults) |
| United Stables U (new, no token) | $0 | $1,587M (21 Oct) | $1,587M | new | Launched 18 Dec 2025 on BNB Chain and Ethereum. Backed by USDT, USDC and USD1. Binance listed U on 13 Jan 2026. BSC $1,078M, Ethereum $425M | [DL 336](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=336) · [BNB Chain](https://www.bnbchain.org/en/blog/united-stables-launches-u-as-a-native-stablecoin-on-bnb-chain) · [AltcoinBuzz](https://www.altcoinbuzz.io/binance-lists-united-stables-u-with-new-pairs) |
| Other 2026 newcomers | USDGO $0 | USDGO $1,418M (25 Sep) | USDGO $1,298M | new | Open USD $831M (21 Oct, ATH). Polymarket USD peaked $627M (13 Jul), now $484M. Multipli rwaUSDi $487M. Theo thUSD TVL $132M (since 10 Sep) | [DL 347](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=347) · [DL 443](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=443) · [DL 406](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=406) · [DL 340](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=340) · [TVL](https://api.llama.fi/protocol/theo-network-thusd) |

More detail on USD1's October redemptions ([FinanceFeeds, 19 Oct 2026](https://financefeeds.com/world-libertys-usd1-supply-falls-9-1-after-heavy-ethereum-bnb-burns/)):
- USD1 market cap fell from $4.43B (6 Oct) to $4.02B (19 Oct), −9.1%.
- Net burns between 6 and 15 Oct were $385.0M: Ethereum $184.6M across 63 burns, BNB Chain $200.4M across 12 burns.
- About $200M came from one unidentified BNB address, roughly 52% of the drop. More than 99% of Ethereum redemptions passed through a BitGo-labelled wallet.
- The price held between $0.998 and $1.000, so the peg did not break.
- A February FinanceFeeds report said Binance-linked wallets held about 87% of USD1 supply.
- Issuance is moving from BitGo to World Liberty Trust Company, which received preliminary conditional OCC approval on 14 Aug.

#### 2C. Credit-backed and yield stablecoins

| Product | 1 Jan 2026 | 2026 peak (date) | 21 Oct 2026 | YTD | Yield (21 Oct) | Source |
|---|---|---|---|---|---|---|
| Maple syrupUSDC/USDT (TVL) | $2,357M | $3,138M (3 Jan) | $2,769M | **+17.5%** | Low $1,555M (20 Apr). ATH $3,246M (30 Oct 2025). Main syrup pool APY not exposed in DefiLlama yields | [TVL](https://api.llama.fi/protocol/maple) |
| Cap cUSD | $348.5M | $443.2M (28 Jan) | $82.8M | **−76.2%** | Low $61.1M (16 Jul). Cap TVL $381.7M→$232.9M. stcUSD 4.98% | [DL 296](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=296) · [TVL](https://api.llama.fi/protocol/cap) · [yields](https://yields.llama.fi/pools) |
| USD.AI USDai | $653.5M | $663.2M (20 Jan) | $262.0M | **−59.9%** | Low $153.6M (21 Jul). Arbitrum $506M→$261M; Plasma $147M→$0.9M. sUSDai 6.23% | [DL 309](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=309) · [chains](https://stablecoins.llama.fi/stablecoin/309) · [yields](https://yields.llama.fi/pools) |
| infiniFi iUSD | $178.5M | $190.5M (7 Jan) | $68.3M | **−61.7%** | Low $43.8M (2 Oct). siUSD 6.15% | [DL 298](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=298) · [yields](https://yields.llama.fi/pools) |
| 3Jane USD3 | DefiLlama net TVL $42.4M | $49.9M (28 Jan) | net TVL $11.7M; USD3 MC $102.4M (85.7M × $1.20) | n/a | USD3 6.69%, sUSD3 13.84% (USD3 pool TVL $93.1M) | [TVL](https://api.llama.fi/protocol/3jane-lending) · [CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=3jane-usd3) · [yields](https://yields.llama.fi/pools) |
| Re reUSD (+reUSDe) | n/a | n/a | reUSD MC $344.2M (310.5M × $1.11) | n/a | reUSD 6.76%, reUSDe 11.80% | [CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=re-protocol-reusd) · [yields](https://yields.llama.fi/pools) |
| Avant avUSD | $101.0M | $134.4M (29 Aug) | $120.2M | +19.0% | savUSD 7.95% | [DL 271](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=271) · [yields](https://yields.llama.fi/pools) |
| Solstice USX | $306.1M | $523.2M (31 Jul) | $209.4M | −31.6% | — | [DL 310](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=310) |
| Apyx apxUSD (pre-TGE) | $0 | $524.7M (28 May) | $291.7M | −44% from peak | — | [DL 354](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=354) |
| Benchmarks | USDe $6.30B; USDf $2.06B | — | USDe $4.67B; USDf $1.73B | USDe −25.9%; USDf −16.0% | sUSDe 5.17%; sUSDf 3.84% | [DL 146](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=146) · [DL 246](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=246) |

Re structure and backing:
- Re states reUSD's yield as the higher of two benchmarks: SOFR + 250 bps for capital deployed as reinsurance collateral, or 7-day trailing sUSDe yield + 250 bps for capital held onchain ([Solana Compass](https://solanacompass.com/news/re-protocol-launches-reusd-on-solana-backed-by-5105m-reinsurance-portfolio)).
- Yearn's 7 Sep 2026 review gives a different picture ([Yearn risk report](https://github.com/yearn/risk-score/blob/master/reports/report/re-reusd.md)):
  - It describes a blended formula, not a "higher-of" floor.
  - About 99.5% of onchain reserves are sUSDe.
  - The first-loss Re Capital buffer is about $73M.
  - Instant redemptions come from a vault holding only about $9.09M.
  - Score: 3.45/5 (Medium risk).

#### 2D. CDP and decentralized stablecoins

| Stablecoin | 1 Jan 2026 | 2026 peak (date) | 21 Oct 2026 | YTD | Yield / notes | Source |
|---|---|---|---|---|---|---|
| USDS (Sky) | $5,860M | **$8,950M (1 Apr)** | $6,714M | +14.6% | sUSDS 3.80% (30-day mean 3.69%) on $4.83B (Ethereum) + $364M (Arbitrum). stUSDS 5.64% | [DL 209](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=209) · [yields](https://yields.llama.fi/pools) |
| DAI (Sky) | $4,497M | $4,877M (23 Jun) | $4,743M | +5.5% | sDAI (Sky Lending) 1.25%. USDS+DAI combined $10.36B→$11.46B (+10.6%) | [DL 5](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=5) |
| Sky/Spark/Grove TVL | Sky Lending $5,786M; SparkLend $3,334M; Spark Liquidity Layer $2,009M; Spark Savings $2,176M | Sky $7,490M (19 Mar); SparkLend $5,832M (22 Sep); SLL $2,823M (13 Oct); Savings $2,999M (4 May); Grove $3,386M (17 Apr) | Sky $5,691M; SparkLend $5,175M (+55%); SLL $2,723M (+36%); Savings $1,618M (−26%); Grove $1,405M | — | Grove tracked from 23 Jan 2026 | [Sky](https://api.llama.fi/protocol/sky-lending) · [SparkLend](https://api.llama.fi/protocol/sparklend) · [SLL](https://api.llama.fi/protocol/spark-liquidity-layer) · [Savings](https://api.llama.fi/protocol/spark-savings) · [Grove](https://api.llama.fi/protocol/grove-finance) |
| GHO (Aave) | $495.2M | **$699.0M (6 Aug, ATH)** | $699.0M | **+41.1%** | sGHO 4.50% on $235.3M | [DL 118](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=118) · [yields](https://yields.llama.fi/pools) |
| crvUSD (Curve) | $348.6M | $369.0M (6 Jan) | $243.8M | −30.1% | Low $186.3M (29 Jun). scrvUSD 2.59%. crvUSD market TVL $134.4M→$139.0M | [DL 110](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=110) · [TVL](https://api.llama.fi/protocol/crvusd) |
| frxUSD (Frax) | $111.9M | $138.8M (9 May) | $98.6M | −11.9% | Legacy FRAX $210.1M→$150.8M. sfrxUSD 4.90%. Frax USD TVL $60.7M→$103.2M | [DL 235](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=235) · [DL 6](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=6) · [TVL](https://api.llama.fi/protocol/frax-usd) |
| BOLD (Liquity V2) | $40.4M | $40.4M (2 Jan) | $38.3M | −5.2% | Low $29.0M (11 Jul). LUSD $35.1M→$25.7M. Liquity V2 TVL $126.6M→$98.1M. sBOLD (Pendle) ~5% | [DL 269](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=269) · [TVL](https://api.llama.fi/protocol/liquity-v2) |
| Liquity forks | feUSD $19.6M; USDaf V2 $2.0M; USND $1.6M; Mezo MUSD $21.0M | MUSD $31.8M (17 Jul) | feUSD $9.4M (−52%); USDaf $0.2M; USND ~$0; Quill USDQ $0.1M; ebUSD ~$0; Orki USDK ~$0; MUSD $29.5M (+40%) | — | Felix CDP TVL $39.6M→$25.9M. Mezo Borrow TVL $29.2M (20 Jan)→$1.4M | [DL 251](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=251) · [DL 295](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=295) · [DL 287](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=287) · [DL 303](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=303) · [Felix](https://api.llama.fi/protocol/felix-cdp) |
| fxUSD (f(x)) | $32.8M | $91.8M (15 Oct) | $79.5M | **+142.3%** | fx TVL $56.1M→$115.4M. fxSAVE 6.35% | [DL 168](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=168) · [TVL](https://api.llama.fi/protocol/fx-protocol) |
| DOLA (Inverse) | $175.7M | $185.9M (6 Jan) | $113.1M | −35.6% | Low $77.0M (23 Apr). sDOLA 5.42%. FiRM TVL $68.8M→$33.4M | [DL 15](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=15) · [TVL](https://api.llama.fi/protocol/inverse-finance-firm) |
| reUSD (Resupply) | $51.6M | $53.0M (11 Jan) | $52.8M | +2.3% | Low $31.8M (11 Mar). sreUSD 1.63% | [DL 256](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=256) |
| lisUSD (Lista) | $74.5M | $94.2M (30 Sep) | $75.9M | +1.9% | Lista CDP TVL $659.7M→$81.6M (−88%). Lista Lending TVL $990M. USD1 on Lista Lending $138M at 1.43% | [DL 79](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=79) · [TVL](https://api.llama.fi/protocol/lista-cdp) |
| satUSD (River) | $159.1M | $159.6M (26 Jan) | $125.4M | −21.2% | River Omni-CDP TVL $153.9M→$104.2M | [DL 218](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=218) · [TVL](https://api.llama.fi/protocol/river-omni-cdp) |
| USDa (Avalon) | $272.4M | $272.4M (4 Jan) | $145.6M | −46.6% | — | [DL 220](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=220) |
| USDH (Native Markets, Hyperliquid) | $62.9M | $106.4M (8 May) | $6.5M | −89.6% | — | [DL 321](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=321) |
| Yield Basis (TVL) | $203.1M | $247.3M (15 Jan) | $125.0M | −38.5% | — | [TVL](https://api.llama.fi/protocol/yield-basis) |

Sky milestones during 2026:
- **Mid-March:** USDS was about $7.9B, up more than 22% over 30 days, per DL News on 13 Mar 2026 ([DL News](https://www.dlnews.com/articles/defi/sky-slashes-buybacks-to-boost-reserves-of-usds-stablecoin/)).
- **End of May:** Spark reported $6.4B in Savings TVL, $3.6B in SparkLend and $2.6B in the Spark Liquidity Layer ([CryptoBriefing](https://cryptobriefing.com/spark-may-savings-sparklend-tvl/)).
- **27 May newsletter:** the Sky Savings Rate had been cut to 3.60%, per a headline only ([Today in DeFi](https://news.todayindefi.com/p/airdrop-alpha-re-protocol-announced)).

#### 2E. Depeg, redemption and incident episodes (2026)
- **USD1:** about $401M was redeemed in two weeks (6–19 Oct 2026), concentrated in a few wallets. The peg held between $0.998 and $1.000 ([FinanceFeeds](https://financefeeds.com/world-libertys-usd1-supply-falls-9-1-after-heavy-ethereum-bnb-burns/)). [High]
- **Re:** on 25 Aug 2026, TWAP manipulation of the Pendle PT-reUSD market caused about $36.4M in Morpho liquidations. Re's own contracts were not compromised, and reUSD never depegged; its share price rose from $1.00 to about $1.099 since 12 Jun 2025 ([Yearn](https://github.com/yearn/risk-score/blob/master/reports/report/re-reusd.md)). [High]
- **Usual bUSD0 (formerly USD0++):**
  - It now matures on 11 Jun 2028 and redeems 1:1 for USD0 at maturity.
  - The DAO-set early-exit floor was reported at $0.92 in mid-2026, up from $0.87 in January 2025.
  - UIP-15 (Dec 2025) moved the protocol to full DAO ownership.
  - Source: search-result summary of Usual materials ([Usual blog index](https://usual.money/blog); [Cointelegraph, Jan 2025](https://cointelegraph.com/news/usd0-stablecoin-depeg-revenue-switch)). [Medium]
- **Adjacent incidents** ([DefiLlama hacks](https://api.llama.fi/hacks)): the Resolv USR infrastructure key leak (21 Mar 2026, $24.5M) and the Kelp cross-chain exploit (18 Apr 2026, $293M). These are synthetic or LST incidents, but they are part of the 2026 yield-stablecoin risk backdrop. I found no DefiLlama-listed 2026 hack for any seed-list protocol.
- **CoinGecko price prints to treat with caution:**
  - iUSD shows an ATL of $0.2431 on 2026-01-04 and an ATH of $1.38 on 2026-01-10.
  - Legacy FRAX shows an ATH of $1.66 on 2026-03-30 and an ATL of $0.2498 on 2026-06-24.
  - These look like thin-pool artifacts, not verified depegs ([CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=infinifi-usd,frax)). [Low]

### Inferences
- The stablecoin market as a whole did not grow in 2026. Gains for any coin therefore came from rotation:
  - into US-regulated, token-less issuers (USDG, RLUSD) and Binance-adjacent products (U, USD1);
  - out of USDT, USDC, PYUSD and yield or synthetic dollars (USDe, USDtb, USDf).
- Two scope coins grew organically without points: Sky (+10.6%) and GHO (+41%). Both offer a savings-rate wrapper (sUSDS 3.80%, sGHO 4.50%) and deep lending integrations.
- M0's collapse looks mechanical. The M supply on Arbitrum fell from $690.7M to $0.2M, roughly matching USDai's own decline on Arbitrum. A likely explanation is that USD.AI moved USDai's backing off $M, or that USDai redemptions removed most of the M on Arbitrum. [Medium-Low; not confirmed by a primary source]
- USD1 remains highly concentrated: one BNB wallet alone redeemed about $200M, and an 87% Binance-linked share was reported in February. The 2026 peak of $5.39B (11 Feb) was probably driven by a few large holders rather than broad adoption. [Medium]

### Gaps
- No 1 Jan 2026 baseline for USDY, OUSG, TBILL, Midas mTBILL/mF-ONE, Ondo's total RWA AUM, or syrupUSDC/syrupUSDT split supplies. These are not in DefiLlama's stablecoin set, CoinGecko throttled further calls, and rwa.xyz was not fetched.
- Causes are unverified for:
  - USDO's −81%;
  - Noble USDN's wind-down;
  - DOLA's January–April contraction (from $185.9M to $77.0M);
  - Reservoir's April-peak-to-September collapse in TVL;
  - Lista CDP TVL's −88% while lisUSD supply stayed flat;
  - USDH's −94% from peak.
- DefiLlama's reported USDS supply on L2s and Solana dropped to near zero (for example Base $141M → $3.3M), which may be a methodology change.

## Q3. Value accrual and valuation: revenue, buybacks/burns, fee switches, revenue share, valuation ratios; best/worst performers and why

### Takeaway
Revenue is highly concentrated. On DefiLlama trailing-12-month figures:
- Sky Lending earns $197.6M in revenue, of which $57.8M goes to holders.
- World Liberty earns $127.5M in revenue, apparently USD1 reserve income, with nothing reported to holders.
- Aave earns about $87.6M.
- Maple earns $14.4M, Usual $8.9M and USD.AI $7.5M.
- Most other scope protocols earn under $5M a year.

SKY (+33%) and AAVE (+7%), which combine real revenue with buybacks, beat small CDP tokens. Those small tokens trade at 2–10× revenue yet still fell 45–90%. The richest valuations relative to revenue are WLFI's FDV (44× revenue), CAP (FDV 95× fees) and RE (FDV 33× fees).

### Cited Findings

#### 3A. Protocol revenue (DefiLlama, trailing 1y to 21 Oct 2026; fees / revenue / holders revenue)
Sources: [fees](https://api.llama.fi/overview/fees?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true) · [revenue](https://api.llama.fi/overview/fees?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType=dailyRevenue) · [holders revenue](https://api.llama.fi/overview/fees?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType=dailyHoldersRevenue)

| Protocol | Fees (1y) | Revenue (1y) | Holders revenue (1y) | Notes |
|---|---|---|---|---|
| Sky Lending | $388.9M | $197.6M | $57.8M | 30d: revenue $13.45M, holders $5.80M |
| World Liberty Financial | $127.5M | $127.5M | $0 | 30d revenue $12.16M (≈$148M annualized) |
| Aave V3 | $673.5M | $85.8M | $17.35M | plus V2 revenue $1.5M and V4 $0.33M |
| Spark | SLL $129.9M; SparkLend $59.1M | SLL $5.5M; SparkLend $4.2M | SparkLend $3.96M | — |
| Grove | $57.0M | not tracked | — | — |
| Ondo Yield Assets | $63.3M | not tracked | — | — |
| Maple | $111.2M | $14.4M | $2.9M | — |
| USD AI | $26.6M | $7.46M | $0 | 30d revenue $0.45M |
| Usual USD0 | $11.7M | $8.9M | $0.84M | 30d revenue $0.29M |
| Curve | DEX $56.2M; crvUSD $2.46M | DEX $26.1M; crvUSD $1.52M | DEX $25.7M; crvUSD $1.37M | — |
| Yield Basis | $20.1M | $3.9M | $3.9M | — |
| Inverse FiRM | $4.14M | $4.02M | $0.11M | — |
| Lista | CDP $3.04M | CDP $3.00M; Lending $0.54M; LST $0.40M | LST $0.16M | — |
| Avalon USDa | $2.79M | $2.79M | — | — |
| Resupply | $1.48M | $1.11M | $1.03M | — |
| fx Protocol | $4.96M | $1.01M | — | — |
| infiniFi | $6.95M | $0.71M | — | — |
| OpenEden | USDO $2.49M; TBILL $0.43M | USDO $0.42M; TBILL $0.21M | — | — |
| Liquity | V2 $1.91M | V2 $0.41M; V1 $0.11M | — | — |
| cap | $7.18M | $0.21M | — | — |
| Re | $12.06M | $0.16M | — | — |
| M0 | $14.5M | $0.05M | — | — |
| Midas | $23.4M | $0.06M | — | — |
| Apyx | $11.4M | $0.01M | — | — |
| Reservoir | $4.49M | $0 | — | — |
| Frax USD | $3.37M | $0 | — | — |
| River Omni-CDP | — | $0.03M | — | — |
| Mezo Borrow | — | $0.15M | — | — |
| GAIB | $1.88M | $0.38M | — | — |

#### 3B. Buybacks, burns, fee switches and revenue share
- **Sky:**
  - **Buyback cut.** Buybacks ran at $300k of USDS per day from Feb 2025 until a 12–13 Mar 2026 vote cut them to **$37.6k/day (−87%) for three months**. Rune Christensen cited an expected "massive oil shock" from the war in Iran. $116.6M of USDS had been spent on buybacks since Feb 2025 (BlockAnalytica) ([DL News, 13 Mar 2026](https://www.dlnews.com/articles/defi/sky-slashes-buybacks-to-boost-reserves-of-usds-stablecoin/)).
  - **April treasury overhaul.** Revenue now goes to fixed-percentage buckets: security, backstop capital, the Smart Burn Engine and staking rewards. A **$150M solvency reserve** is prioritized ahead of buybacks ([FinanceFeeds, 12 May 2026](https://financefeeds.com/sky-price-forecast-what-reduced-buybacks-mean/)).
  - **Results and projections.** Q1 2026 revenue was **$124M gross / $61M net**, described as a record. The Sky Frontier Foundation had projected USDS could reach $20.6B and gross revenue $611.5M in 2026 ([FinanceFeeds](https://financefeeds.com/sky-price-forecast-what-reduced-buybacks-mean/)).
  - **Credit rating.** S&P rated Sky B- in 2025 ([DL News](https://www.dlnews.com/articles/defi/sky-slashes-buybacks-to-boost-reserves-of-usds-stablecoin/)).
- **Spark (SPK):**
  - The Feb 2026 Sky executive sent 571,957 USDS to the Spark Operations multisig for SPK buybacks ([Sky executive](https://vote.sky.money/executive/template-executive-vote-launch-agent-onboardings-january-monthly-settlement-cycle-and-treasury-management-function-sky-staking-rewards-normalization-prime-agent-proxy-spells-february-26-2026)).
  - In Q2 2026, Spark spent **$1.31M of USDS buying 58.26M SPK** (1,301 fills) ([Spark Q2 2026 report](https://paragraph.com/@spark-11/spark-q2-2026-financial-report)).
  - Q2 2026 results: gross protocol returns $40.6M (+29% QoQ), net protocol returns $4.31M (−38%), net surplus $0.71M (−79%). Captured spread on the Spark Liquidity Layer went from +0.64% to −0.13% ([Spark Q2 2026 report](https://paragraph.com/@spark-11/spark-q2-2026-financial-report)).
  - A March 2026 plan reportedly earmarked about $35M of operating reserves, with 10% a month used for buybacks over 12 months (search summary; primary page not opened). [Medium]
- **WLFI:**
  - 100% of fees from WLFI's protocol-owned liquidity on Ethereum, BNB Chain and Solana go to open-market buy-and-burn. The plan passed in Sep 2025 with about 99.5–99.8% support ([CoinDesk](https://www.coindesk.com/markets/2025/09/12/world-liberty-financial-token-holds-steady-as-community-backs-buyback-and-burn-plan); [CoinGecko Learn](https://www.coingecko.com/learn/world-liberty-financial-buyback-proposal-underway)).
  - The USD1 reserve income (the ~$127M/yr DefiLlama revenue) is not reported as flowing to WLFI holders (holders revenue $0).
  - A 21 Sep 2026 forum proposal for a USD1 payments wallet whose fees would fund WLFI buybacks has no recorded vote ([WLF forum](https://governance.worldlibertyfinancial.com/t/proposal-usd1-payments-wallet-with-wlfi-buyback-burn/54688)).
  - Search summaries mention a first burn on 26–27 Sep 2025 of 7,893,828 WLFI (~$1.43M). [Low; exact source page not opened]
- **OpenEden (EDEN):** buybacks and burns are described only as "conditional future mechanisms" ([CoinDesk EDEN page](https://www.coindesk.com/price/eden-token)). xEDEN staking gives governance rights and "future fee accrual". A portion of revenue "may be allocated" to buybacks, which is not a commitment ([OpenEden](https://openeden.com/news/openeden-eden-token-tokenized-rwa-ecosystem/)).
- **RE:** the token "does not represent equity, debt, profit-sharing, dividend rights". Staking rewards are for governance participation, not passive yield ([re.xyz](https://re.xyz/insights/re-tge-launch)).
- **GROVE:** no buyback or value accrual stated. Staking and voting are to be "introduced progressively" ([Sky blog](https://sky.money/blog/grove-sky-ecosystem-rewards)).
- **CHIP:** governance covers how "origination, servicing, and liquidity fees are collected and routed", but no buyback is specified. sCHIP staking backs the insurance framework ([USD.AI](https://usd.ai/insights/chip-is-live)).
- **Usual:** introduced a "revenue switch" after the January 2025 USD0++ depeg ([Cointelegraph](https://cointelegraph.com/news/usd0-stablecoin-depeg-revenue-switch)). DefiLlama holders revenue is now only $0.84M/yr ([holders revenue](https://api.llama.fi/overview/fees?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType=dailyHoldersRevenue)).
- **Others with meaningful DefiLlama holders revenue:** Curve/veCRV $27.0M, Aave $17.35M, Yield Basis $3.9M, Maple $2.9M, Resupply $1.03M ([holders revenue](https://api.llama.fi/overview/fees?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType=dailyHoldersRevenue)).

#### 3C. Valuation ratios (my calculations)
Inputs: CoinGecko MC/FDV as of 21 Oct 2026, DefiLlama trailing-1y revenue/fees, and DefiLlama supply/TVL as of 21 Oct 2026 (sources as in the tables above).

| Token | MC / revenue | FDV / revenue | MC / holders revenue | FDV / fees | MC / stablecoin supply (or TVL) | FDV / supply | Supply basis |
|---|---|---|---|---|---|---|---|
| SKY | 9.1× | 9.1× | 31× | 4.6× | 0.16 | 0.16 | USDS+DAI $11.46B |
| WLFI | 14.1× | 44.3× | n/a ($0) | 44× | 0.45 | 1.41 | USD1 $4.02B |
| AAVE | 27.5× | 28.5× | 139× | 3.7× | 3.45 | 3.57 | GHO only $0.70B (misleading; Aave is mainly a lender) |
| CRV | 22.4× | 34.4× | 22.9× | 16.2× | 2.54 | 3.90 | crvUSD $0.24B |
| SYRUP | 16.6× | 18.0× | 82× | 2.3× | 0.09 | 0.09 | Maple TVL $2.77B |
| CHIP | 12.3× | 61.3× | n/a | 17.2× | 0.35 | 1.74 | USDai $262M |
| CAP | 505× | 3,238× | n/a | 94.7× | 1.28 | 8.21 | cUSD $82.8M |
| RE | n/a | 2,465× | n/a | 32.7× | n/a | 1.15 | reUSD MC $344M |
| EDEN | 41.6× | 95.2× | n/a | 20.5× | 0.74 | 1.70 | USDO + TBILL ≈ $35M |
| ONDO | revenue not tracked | — | — | 73× | 0.96 | 1.96 | USDY MC $2.36B |
| SPK | 6.9× | 20.4× | 16.8× | 1.05× | 0.01 | 0.04 | SparkLend TVL $5.17B |
| LISTA | 8.7× | 16.0× | — | 3.9× | 0.45 | 0.83 | lisUSD $75.9M |
| YB | 4.5× | 12.5× | 4.5× | 2.4× | 0.14 | 0.39 | YB TVL $125M |
| FXN | 4.3× | 31.9× | — | 6.5× | 0.05 | 0.41 | fxUSD $79.5M |
| AVL | 3.1× | 6.8× | — | 6.3× | 0.06 | 0.13 | USDa $145.6M |
| RSUP | 2.7× | 7.3× | 2.9× | 5.5× | 0.06 | 0.15 | reUSD $52.8M |
| USUAL | 2.4× | 2.5× | 25.7× | 1.9× | 0.04 | 0.04 | USD0 $542M |
| INV | 2.0× | 2.1× | 74× | 2.0× | 0.07 | 0.07 | DOLA $113M |
| LQTY | 40× | 40× | 189× | 8.4× | 0.33 | 0.33 | BOLD+LUSD $64M |
| FRAX (gov) | 46× | 49× | — | ~3× | 0.10 | 0.10 | frxUSD + legacy FRAX $249M |
| GROVE | n/a | n/a | n/a | 0.9× | 0.003 | 0.036 | Grove TVL $1.41B |
| RIVER | 727× | 3,703× | 727× | 3,703× | 0.17 | 0.89 | satUSD $125M |
| Benchmark: FF | — | — | — | 162× | 0.21 | 0.63 | USDf $1.73B |

- A rough cross-check on WLF's DefiLlama revenue: about $4.0B of USD1 × the ~3.7% T-bill-like yield (USDY's current APY is 3.71% per [DefiLlama yields](https://yields.llama.fi/pools)) ≈ $148M a year. That matches the 30-day annualized revenue. [Inference]

#### 3D. Best and worst 2026 performers (YTD to 21 Oct 2026, DefiLlama 1-Jan vs CoinGecko current)
- **Best:**
  - SKY +33.0% (and a new ATH of $0.10087 on 5 Oct 2026)
  - ONDO +29.0%
  - PLUME +9.8%
  - FXN +9.7%
  - CRV +9.1%
  - AAVE +6.8%
  - Among 2026 TGEs: CAP +150% vs first print
- **Middle:** SPK −5.8%, EDEN −8.4%, GAIB −28.2%, SYRUP −36.5%.
- **Worst:**
  - RIVER −90.6%
  - DAM −85.4%
  - YB −83.9%
  - AVL −74.2%
  - WLFI −60.6%
  - INV −59.7%
  - FRAX −59.3%
  - USUAL −55.3%
  - RSUP −54.5%
  - LISTA −53.7%
  - LQTY −44.4%
  - Among 2026 TGEs: MEZO −95.7%, SLX −82.6% and GROVE −70.1% vs first print

  (Per-token links are in 1B/1C.)

### Inferences
- **What explains the winners** (inference, Medium confidence):
  1. Large, recurring revenue tied to a stablecoin that kept growing, plus buybacks. SKY: USDS+DAI +10.6% and holders revenue of about $58M a year.
  2. The institutional or RWA narrative and the largest tokenized-yield product. ONDO: USDY MC $2.36B.
  3. Lending exposure as rates and leverage recovered in Sep–Oct. AAVE and GHO.
- **What explains the losers:**
  1. Shrinking stablecoin supply after incentives ended (USDai, cUSD, iUSD, USDa, satUSD).
  2. Low or no revenue to token holders (RIVER, DAM, GROVE, MEZO).
  3. Heavy uncirculated supply (GROVE about 10×, CAP about 5×, CHIP about 4×).
  4. For WLFI, a falling USD1 float (−25% from peak) while none of the reserve income reaches token holders.
- **Valuation dispersion is extreme.** Legacy CDP tokens (INV, RSUP, USUAL, AVL, YB) trade at 2–5× trailing revenue, which prices them as distressed or ex-growth. Newer issuer tokens (CAP, CHIP on FDV, RE, EDEN, WLFI on FDV) trade at 30–3,000× revenue, which prices in growth that 2026 supply data does not yet show.
- **SKY** at about 0.16× MC to stablecoin supply and about 9× revenue is the cheapest large issuer token per dollar of float. WLFI on an FDV basis is about 9× more expensive per dollar of float (1.41 vs 0.16).

### Gaps
- DefiLlama does not report revenue for Ondo, Grove, Reservoir, Frax USD or Plume vaults, and reports Ethena and Falcon revenue in a way that is hard to compare. So revenue multiples for ONDO and GROVE cannot be calculated.
- Maple's buyback mechanics in 2026 and Aave's 2026 buyback amounts were not verified from primary sources. Only DefiLlama holders-revenue totals are available.
- Sky's 2026 cumulative burn total after the March cut, and whether the $37.6k/day level was extended after three months, were not verified.
- Token Terminal, Artemis and Messari valuation pages were not fetched because the search budget was exhausted.

## Q4. Regulation: the GENIUS Act yield ban and 2026 rules, and their effect on RWA and yield-bearing stablecoin business models

### Takeaway
The OCC's final GENIUS Act rule, issued today (21 Oct 2026), keeps the ban on issuers paying yield. It drops the proposed presumption against yield paid through affiliates or third parties and moves to case-by-case review. GENIUS and the rule take effect on 18 Jan 2027, and the CLARITY Act stalled in a September 2026 Senate vote.

The practical result is that payment-stablecoin issuers (USD1, USDG, PYUSD, RLUSD) compete on distribution and on rewards paid by third parties. Yield in this scope is delivered through other structures:
- savings wrappers (sUSDS, sGHO, bUSD0, sUSDai, siUSD, stcUSD);
- KYC-gated, offshore or tokenized-fund formats (USDY, TBILL, reUSD, USD3).

### Cited Findings
- **OCC final rule (21 Oct 2026):**
  - It is the first final rule from a federal banking regulator under GENIUS.
  - It bars payments made "solely in connection with the holding, use, or retention" of a payment stablecoin, applied case by case. The OCC gave no examples. Payments that "might be made, at least in part, for other reasons" fall outside the ban.
  - Rewards programs that predate GENIUS get no safe harbor.
  - The OCC said: "Unless and until such legislation passes, the OCC must implement the GENIUS Act's yield prohibition, as enacted."
  - Source: [CoinDesk, 21 Oct 2026](https://www.coindesk.com/policy/2026/10/21/occ-s-final-rule-to-start-fresh-in-weighing-stablecoin-rewards-against-genius-act-ban).
- **Scope and effective date.** Search summaries of the same coverage say the rule drops the proposed presumption that affiliate or third-party arrangements violate the yield ban. They say it takes effect on 18 Jan 2027, the same day as GENIUS itself. It applies to national banks, federal savings associations, federal branches and nonbank firms seeking federal qualified issuer status ([Bitcoin.com](https://news.bitcoin.com/regulation-and-legal/occ-finalizes-genius-act-rules-as-stablecoin-yield-faces-limits/); [CryptoTimes](https://www.cryptotimes.io/2026/10/21/occ-finalizes-first-genius-act-stablecoin-rule-drops-rewards-presumption/); [OCC release PDF](https://www.occ.gov/news-issuances/news-releases/2026/nr-occ-2026-9a.pdf)). [High]
- **OCC's March 2026 proposal:**
  - A PPSI was "presumed" to pay impermissible yield if it contracted to pay holders through affiliates or third parties. The issuer could rebut this in writing.
  - Not intended to be banned: merchant discounts, and white-label profit-sharing with non-affiliates.
  - Reserve safe-harbor proposal: at least 10% daily liquidity, at least 30% weekly liquidity, at most 40% with any one counterparty, and a weighted average maturity of 20 days or less. Issuers with $25B or more outstanding would hold 0.5% of reserves in insured deposits.
  - Source: [Morgan Lewis, Apr 2026](https://www.morganlewis.com/pubs/2026/04/occs-genius-act-proposal-what-prospective-issuers-need-to-know).
  - The final rule replaced reserve "rebuttable presumptions" with a "principles-based approach" plus minimum daily liquidity and single-counterparty limits ([CoinDesk](https://www.coindesk.com/policy/2026/10/21/occ-s-final-rule-to-start-fresh-in-weighing-stablecoin-rewards-against-genius-act-ban)).
- **Other agencies** (none met the statutory mid-year deadline) ([CoinDesk](https://www.coindesk.com/policy/2026/10/21/occ-s-final-rule-to-start-fresh-in-weighing-stablecoin-rewards-against-genius-act-ban)):

| Agency | Action and date |
|---|---|
| FDIC | Proposals on 16 Dec 2025 and 7 Apr 2026 |
| FinCEN/OFAC | Joint proposal on 8 Apr 2026 |
| Treasury | GENIUS proposal on 17 Aug 2026, including foreign issuers such as Tether |
| Federal Reserve | Proposals on 24 Sep 2026 |

- **CLARITY Act.** The market-structure bill "failed to advance in a key Senate vote last month", with bank lobbying pushing to tighten GENIUS's yield language ([CoinDesk](https://www.coindesk.com/policy/2026/10/21/occ-s-final-rule-to-start-fresh-in-weighing-stablecoin-rewards-against-genius-act-ban)). [High]
- **Distributor rewards continue** (named by CoinDesk): Coinbase One pays 3.75% on USDC, PayPal pays 4% on PYUSD, and Kraken+ pays up to 4.5% on USDG ([CoinDesk](https://www.coindesk.com/policy/2026/10/21/occ-s-final-rule-to-start-fresh-in-weighing-stablecoin-rewards-against-genius-act-ban)).
- **USD1 moving to a US trust charter.** World Liberty Trust Company received preliminary conditional OCC approval on 14 Aug 2026 to take over USD1 issuance, redemption, reserves and custody from BitGo. In October, the ICBA sued to challenge the OCC's broader chartering authority ([FinanceFeeds](https://financefeeds.com/world-libertys-usd1-supply-falls-9-1-after-heavy-ethereum-bnb-burns/)).
- **Examples of how in-scope projects are structured:**
  - **Re:** reUSD is a KYC-gated "deposit token" for non-US persons. The reinsurer is Cover Re SPC (Cayman, CIMA-regulated) and the issuer is Resilience Foundation Cayman LLC ([Yearn](https://github.com/yearn/risk-score/blob/master/reports/report/re-reusd.md)).
  - **OpenEden:** USDO is issued by a "Bermuda-regulated and licensed entity". EDEN is issued by a BVI company and is not registered under the Securities Act. TBILL is rated "A" by Moody's ([OpenEden](https://openeden.com/news/openeden-eden-token-tokenized-rwa-ecosystem/)).
  - **3Jane:** the docs call USD3 "a yield-bearing ERC-4626 token that represent[s] 3Jane deposits" ([3Jane FAQ](https://docs.3jane.xyz/resources/faq)).
  - **GROVE:** not available in the US ([Sky blog](https://sky.money/blog/grove-sky-ecosystem-rewards)).
  - **Usual:** separates the non-yield USD0 from the bond-like bUSD0 that carries the yield ([Usual blog](https://usual.money/blog)).
  - **Sky:** pairs USDS with the sUSDS savings wrapper at 3.80% ([DefiLlama yields](https://yields.llama.fi/pools)).
- **Market tagging.** CoinGecko's "GENIUS Act Compliant Stablecoin" category is $75.15B, versus $297.8B for all stablecoins (21 Oct 2026) ([CoinGecko categories](https://api.coingecko.com/api/v3/coins/categories)).

### Inferences
- Dropping the presumption against affiliate and third-party rewards is a modest positive for distribution-led models (exchange rewards on USDC, PYUSD and USDG). It also helps DeFi wrappers that sit on top of a non-yield payment token, such as sUSDS, sGHO and Spark Savings. These look likely to survive case-by-case review if payments are "at least in part" for other reasons, such as lending or staking risk. [Medium]
- Issuer tokens whose value depends on reserve interest (WLFI's USD1 income) cannot pass that yield to stablecoin holders. Their growth therefore depends on distribution partners and exchange incentives. USD1's Binance concentration is consistent with this. [Medium]
- Credit-backed and RWA yield products in scope already avoid "payment stablecoin" status:
  - by being KYC-gated deposit or vault tokens (reUSD, USD3);
  - by being tokenized funds or notes (TBILL, USDY);
  - by sitting offshore (Bermuda, BVI, Cayman).
  The 2026 rules did not visibly change their supply, and their outflows look incentive-driven rather than regulatory. [Medium-Low]
- With CLARITY stalled, the status quo through the 18 Jan 2027 effective date is that the issuer yield ban stands while third-party rewards are reviewed case by case. That leaves DeFi savings wrappers as the main on-chain channel for yield.

### Gaps
- I could not open the OCC release, Treasury's 17 Aug 2026 proposal or the Federal Register entries directly. One search summary claimed Treasury finalized a binding GENIUS rule on 30 Sep 2026, which conflicts with CoinDesk calling the OCC's rule the first final rule. This is unresolved.
- I found no 2026 source on whether Sky, Ethena, Ondo or Maple formally restructured specifically in response to GENIUS, for example by creating non-payment entities.
- No MiCA-specific 2026 impact data was gathered for EUR0 or USDO.

## Q5. Pre-TGE pipeline: points design, TVL committed, funding and valuation, token status, expected TGE window, airdrop expectations, mercenary-capital signals

### Takeaway
The live pipeline in scope is small: infiniFi (INFI, Q4 2026), 3Jane (JANE, final mint "in 2026"), Apyx (APYX, a 13 Oct TGE was announced but is not trading), and Avant (no token yet).

The 2026 evidence argues for modest airdrop expectations. Most 2026 TGEs trade 70–96% below their first print. Points-driven TVL repeatedly left after campaigns or TGEs: cUSD −81%, iUSD −64%, apxUSD −44% and USX −60% from their 2026 peaks.

### Cited Findings
- **infiniFi (INFI):** [Medium; aggregator source]
  - **Timing:** TGE planned for Q4 2026 (23 Sep 2026 announcement); "coming soon" as of 14 Oct 2026.
  - **Tokenomics:** Ecosystem 45% (including the community airdrop), Team 20%, Investors 20%, Foundation 15%. Total supply and vesting are undisclosed.
  - **Funding:** more than $6M in total ($3M pre-seed in Feb 2025 and more than $3M seed on 23 Sep 2026), led by Electric Capital.
  - **Scale:** TVL peaked at about $180M and is now above $50M, with more than $9M of yield generated.
  - Source: [CoinGabbar, 14 Oct 2026](https://www.coingabbar.com/en/infinifi-token-launch-date-tokenomics-infi-airdrop-updates).
  - **Supply data:** iUSD went from $178.5M (1 Jan) to a $190.5M peak (7 Jan) and $68.3M now ([DefiLlama](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=298)).
  - **Points:** search summaries say Season 1 and Season 2 points have fixed token allocations. Activity from 26 Aug until TGE earns from a new fixed allocation. infiniFi Prime went live on Blend on 17 Oct 2026 (search summary). [Low-Medium]
- **3Jane (JANE):** [High]
  - **Design:** liquidity mining went live on 9 Jun 2026. Rewards are claimable weekly but locked until the "final mint" in 2026, which enables transferability.
  - **Supply:** the final supply will fall between 1,111,111,111 and 6,666,666,666 JANE.
  - **Emissions:** the first-epoch minimum is 1.35M JANE a week (0.0203–0.1215% of supply), spread across USD3, sUSD3, Pendle PT/YT/LP (Dec-2026 maturity), Morpho and the USD3/frxUSD pool.
  - **Caps and pricing:** the initial USD3 cap was $50M. The program says "You are underwriting $JANE total token supply and $JANE FDV upon final mint."
  - Source: [3Jane](https://www.3jane.xyz/reports/3jane-liquidity-mining-program-is-live).
  - **Backers:** described as Paradigm-backed ([cryptonews headline](https://cryptonews.net/news/altcoins/32997895/)). [Medium]
  - **Size:** USD3 MC is $102.4M ([CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=3jane-usd3)).
- **Apyx (APYX; apxUSD "Dividend-Backed Dollar"):**
  - **Backing:** preferred shares paying STRC (Strategy) and SATA dividends.
  - **Points:** Season 2 ended on 11 Oct 2026, with rewards raised to 6% of total supply (from 4% in Season 1).
  - **TGE and funding:** TGE planned for 13 Oct 2026; the project describes itself as having "zero VC funding" ([Today in DeFi, 27 May 2026](https://news.todayindefi.com/p/airdrop-alpha-re-protocol-announced)).
  - **Current status:** CoinGecko shows a preview listing, 100M total supply and no price on 21 Oct 2026 ([CoinGecko](https://api.coingecko.com/api/v3/coins/apyx)).
  - **Supply data:** apxUSD peaked at $524.7M (28 May) and is now $291.7M ([DefiLlama](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=354)).
  - **Activity:** Apyx fees are $11.4M a year ([DefiLlama fees](https://api.llama.fi/overview/fees?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true)).
- **Avant (avUSD):**
  - The CoinGecko "avant" id has no market data ([CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=avant)).
  - avUSD grew from $101.0M to $120.2M YTD ([DefiLlama](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=271)).
  - savUSD yields 7.95% ([yields](https://yields.llama.fi/pools)).
- **Post-TGE points programs that still matter:**
  - **USD.AI Season 2 ("Flatiron")** runs to 14 Oct 2026 and pays all rewards as CHIP airdrops. Multipliers range from 1× to 40×, and sCHIP earns Allo points ([USD.AI](https://usd.ai/insights/chip-is-live)).
  - **Cap** halved points emissions on 1 Jun 2026, ahead of TGE ([Today in DeFi](https://news.todayindefi.com/p/airdrop-alpha-re-protocol-announced)).
  - **Re** ties later airdrop tranches to keeping the Season 1 TVL baseline, which is an anti-mercenary design ([re.xyz](https://re.xyz/insights/re-tge-launch)).
- **Sky Star and agent pipeline:**
  - Obex launched in 2025 with a "$2.5B mandate to incubate stablecoin projects" ([Sky on X](https://x.com/SkyEcosystem/status/2021634599374254411)). [Medium]
  - Launch Agents 6 (Prysm) and 7 (Interval) were onboarded in the Feb 2026 executive, each with a 10M USDS line. The same executive minted settlement debt for Grove ($6.2M) and Obex ($2.1M) ([Sky executive](https://vote.sky.money/executive/template-executive-vote-launch-agent-onboardings-january-monthly-settlement-cycle-and-treasury-management-function-sky-staking-rewards-normalization-prime-agent-proxy-spells-february-26-2026)). No token plans were stated.
  - Keel's 2026 post mentions no token. Its team is changing from Matariki Labs to Elodin ([Keel](https://keelfi.substack.com/p/keel-in-2026-expanding-the-mandate)).
- **Funding of 2026 launches, for context:**
  - **Cap:** $1.9M pre-seed (Oct 2024; Kraken, Robot Ventures, Kain Warwick) and an $8M seed (Apr 2025; Selini, Franklin Templeton, GSR, Laser Digital) ([ICO Drops](https://icodrops.com/cap-3/)).
  - **USD.AI:** $13.4M Series A (Aug 2025; Framework, Dragonfly, CMT), a YZi Labs strategic round and a $4M Bullish round ([ICO Drops](https://icodrops.com/usd-ai/)).
- **Mercenary-capital signals in 2026 supply and TVL data** (DefiLlama links in Q2):

| Product | Move | Trigger or context |
|---|---|---|
| Cap cUSD | −81% from 28 Jan peak | Frontier/Stabledrop phase ended 4 Feb |
| USDai on Plasma | $147M → $0.9M | — |
| USDai overall | −60% YTD | around the Feb ICO and Apr TGE |
| infiniFi iUSD | −64% from 7 Jan peak | ahead of TGE |
| Apyx apxUSD | −44% from 28 May peak | during Season 2 |
| Solstice USX | −60% from 31 Jul peak | after the 25 May SLX TGE |
| Mezo Borrow TVL | $29.2M → $1.4M | after the Apr MEZO TGE |
| Grove TVL | −58% from 17 Apr peak | — |
| Reservoir TVL | $237.5M → $20.1M (12 Apr → 1 Sep) | — |
| Native Markets USDH | −94% from 8 May peak | — |

- **Neutrl (NUSD), adjacent:** an OTC/synthetic product, probably covered by another researcher. Season 2 ran 4 Jun – mid-Sep 2026 into a TGE, after Season 1 peaked at $230M AUM ([Today in DeFi](https://news.todayindefi.com/p/airdrop-alpha-re-protocol-announced)). NUSD fell from $43.3M to $28.6M over the past month ([DefiLlama list](https://stablecoins.llama.fi/stablecoins?includePrices=true)).

### Inferences
- Comparing launch FDVs with retained TVL:
  - 2026 TGEs priced at first-print FDVs of $66–609M (MEZO $66M, GROVE $168M, CAP $272M, SLX $290M, RE $475M, CHIP $609M).
  - Their stablecoin floats are $30–350M and mostly shrinking.
  - This suggests the market will apply steep discounts to the next wave. A reasonable prior for INFI or JANE launching above about a $150–300M FDV is a post-TGE drawdown, unless TVL is locked in the way Re ties vesting to TVL baselines. [Speculation, Low-Medium]
- Airdrop value is likely to be thin relative to the capital deployed:
  - infiniFi's TVL is already down 60% or more from its peak.
  - 3Jane's JANE has an undetermined supply (a 6× range).
  - Apyx allots 6% of a 100M supply.
  - Cap's cUSD Stabledrop was cut from $12M to $4.2M.
- Durable anti-mercenary features observed in 2026: vesting tied to holdings (Re), ICOs with refund or settle-down protection (CHIP), and stablecoin-denominated airdrops (Cap). The last of these lost credibility when it was cut.

### Gaps
- No funding round or valuation found for Apyx, Avant or 3Jane. No confirmation of whether Apyx's 13 Oct TGE happened. No INFI total supply or vesting.
- Agora, M0 and Midas token plans could not be checked. I treat them as "no token announced" with Medium confidence.
- Points-program TVL (committed vs organic) could not be separated without dashboards such as Dune or the project apps.
- Hyperliquid-native CDP or credit stablecoins (Felix, Hyperbeat, USDH) were not researched for token plans.

## Q6. What the evidence implies for capital flows into these sub-sectors and their remaining upside

### Takeaway
2026 was a zero-sum year for stablecoin supply ($305.0B → $305.2B). Capital moved toward:
- regulated, token-less dollars and exchange-distributed ones;
- the largest CDP/savings franchise (Sky +10.6%);
- Aave's GHO (+41%);
- Maple's institutional credit (TVL +17.5%).

It moved away from points-farmed credit and yield coins and small CDPs. For tokens, upside looks concentrated where three things line up: revenue on a large, sticky float, an explicit holder share (buybacks), and low supply overhang. SKY is the clearest current example. WLFI could join it only if USD1 reserve income or wallet fees are routed to holders. Most small CDP and new issuer tokens remain incentive- and float-driven.

### Cited Findings
- **Market and segment flows** (YTD to 21 Oct 2026):
  - Total stablecoins +0.04%; USDT −2.3%; USDC −4.1% ([DefiLlama](https://stablecoins.llama.fi/stablecoincharts/all)).
  - Token-less issuers: USDG +149%, RLUSD +88%, plus new entrants U ($1.59B), USDGO ($1.30B) and Open USD ($0.83B) ([DefiLlama list](https://stablecoins.llama.fi/stablecoins?includePrices=true)).
- **In-scope winners:** USDS+DAI +10.6%; GHO +41.1%; fxUSD +142%; Maple TVL +17.5%; SparkLend TVL +55%; Plume Vaults TVL +415% ([DefiLlama](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=209); [DL 118](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=118); [Maple TVL](https://api.llama.fi/protocol/maple); [SparkLend](https://api.llama.fi/protocol/sparklend); [Plume Vaults](https://api.llama.fi/protocol/plume-vaults)).
- **In-scope losers:**
  - Credit-backed: cUSD −76%, USDai −60%, iUSD −62%.
  - RWA/T-bill: USDO −81%, M −76%, pUSD −76%.
  - CDP: crvUSD −30%, DOLA −36%, USDa −47%, feUSD −52%.
  - Sources: [DefiLlama](https://stablecoins.llama.fi/stablecoins?includePrices=true), with per-id links in Q2.
- **Token tape:**
  - The median YTD for 21 older in-scope tokens is −44%, with 6 of 21 positive.
  - The median late-2025/2026 TGE trades at −81% vs first print, and CAP is the only one above.
  - Sources: Q1 tables ([CoinGecko](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=sky,ondo-finance,world-liberty-financial,cap-4,chip-2); [DefiLlama coins](https://coins.llama.fi/prices/historical/1767225600/coingecko:sky)).
- **Sky's own 2026 projections vs reality:** it projected USDS at $20.6B and gross revenue at $611.5M ([FinanceFeeds](https://financefeeds.com/sky-price-forecast-what-reduced-buybacks-mean/)). Actual USDS is $6.71B on 21 Oct 2026 ([DefiLlama](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=209)), and Q1 gross revenue was $124M.
- **Sky's risk-first posture:** buybacks were cut 87% in March and a $150M solvency reserve was prioritized ([DL News](https://www.dlnews.com/articles/defi/sky-slashes-buybacks-to-boost-reserves-of-usds-stablecoin/); [FinanceFeeds](https://financefeeds.com/sky-price-forecast-what-reduced-buybacks-mean/)). Even so, SKY hit an ATH on 5 Oct 2026 ([CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=sky)).
- **Spark margin squeeze:** the Q2 captured spread turned negative (−0.13%) and net surplus fell 79% QoQ ([Spark Q2](https://paragraph.com/@spark-11/spark-q2-2026-financial-report)).
- **Policy:** the issuer yield ban stays; third-party rewards are judged case by case from 18 Jan 2027; CLARITY stalled ([CoinDesk](https://www.coindesk.com/policy/2026/10/21/occ-s-final-rule-to-start-fresh-in-weighing-stablecoin-rewards-against-genius-act-ban)).

### Inferences
- **RWA/T-bill issuer tokens (WLFI, USUAL, EDEN, DAM, PLUME, and ONDO as benchmark).**
  - Tokens without a contractual claim on reserve income underperformed, even where the stablecoin grew. WLFI fell 61% while USD1 grew 19.5%.
  - ONDO's outperformance looks like a re-rating of the RWA platform, not of a stablecoin.
  - Remaining upside depends on whether reserve carry is routed to tokens through buybacks or fee switches. Rate cuts would also shrink that carry: USDY yields 3.71% now. [Medium]
- **Credit-backed (SYRUP, CHIP, CAP, RE; JANE and INFI pre-TGE).**
  - Maple is the only franchise with 2026 TVL growth and meaningful fees ($111M a year). Its token still fell 36.5%, which leaves it at 0.09× MC to TVL and 2.3× FDV to fees, the cheapest in the group.
  - Newer credit tokens trade at high FDV-to-fee multiples (CHIP 17×, RE 33×, CAP 95×) while their floats shrink, so they need a turnaround in supply growth to justify current FDVs. [Medium]
- **CDP/decentralized (SKY, SPK, GROVE, CRV, AAVE/GHO, LQTY, FXN, INV, RSUP, LISTA, FRAX).**
  - Scale wins. Sky and GHO captured organic growth, while Liquity forks and small CDPs mostly lost supply.
  - Small CDP tokens at 2–5× revenue (INV, RSUP, USUAL, YB, AVL) are statistically cheap, but every one of them is in a supply downtrend. That looks like a value trap unless their stablecoin supply turns. [Medium-Low]
- **Overall direction of flows.** In a flat-supply market, the next leg of growth in these sub-sectors probably depends on three things:
  - distribution (exchanges and wallets, as with U on Binance or mUSD on MetaMask);
  - integrations with savings wrappers;
  - how the post-18 Jan 2027 case-by-case rewards regime plays out.
  New points campaigns look less likely to drive it, given how fast points-driven TVL left in 2026. [Speculation, Medium]

### Gaps
- No primary dashboard data was available from Steakhouse, info.sky.money, Artemis or Token Terminal. A multi-year view of revenue per dollar of float would strengthen the valuation comparisons.
- Without unlock calendars, the forward supply overhang (next 6 months) is only approximated by total-minus-circulating. That approximation understates or overstates near-term pressure depending on each vesting schedule.
- The search budget ran out before I could verify the causes behind several large moves: RIVER's spike and collapse, FRAX's collapse, the M0/USDai collateral change, Reservoir's TVL collapse, USDO's decline and USD1's January–February spike. A follow-up search pass is needed for these.
