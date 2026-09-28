# Stablecoin / yield-dollar / RWA-credit token TGE comps: benchmarking USD.AI (CHIP), data as of 2026-09-28

Data notes (read first):
- **Primary quantitative source:** DefiLlama public APIs, pulled 2026-09-28. Prices come from `coins.llama.fi/chart` (daily 00:00 UTC snapshots, sourced from CoinGecko). TVL comes from `api.llama.fi/protocol/{slug}`. Stablecoin supply comes from `stablecoins.llama.fi`. Fees and revenue come from `api.llama.fi/summary/fees/{slug}`. CoinGecko (`/coins/{id}`) and CoinPaprika (`/v1/tickers`) were used to cross-check supply, ATH and venues. DefiLlama pages: [DefiLlama protocols](https://defillama.com/), [DefiLlama stablecoins](https://defillama.com/stablecoins), [USD AI on DefiLlama](https://defillama.com/protocol/usd-ai), [CoinPaprika API](https://api.coinpaprika.com/v1/tickers), [CoinGecko CHIP](https://www.coingecko.com/en/coins/usd-ai).
- **"FDV at TGE"** means the first daily snapshot after listing ("day-1 close") × fixed/max supply. Intraday listing wicks are not in daily data, so opening/intraday FDVs from news sources are quoted separately where available. **"ATH FDV"** uses the intraday ATH from CoinGecko/CoinPaprika where available, otherwise the daily max.
- **Supply used for FDV:** ENA 15B, USUAL 4B max, SYRUP ~1.1–1.2B (inflationary), SKY 23.46B, ONDO 10B, AVL 1B, ELX 1B, HUMA 10B, RESOLV 1B, SPK 10B, TREE 1B, DAM 1B, WLFI 100B, XPL 10B, FF 10B, EDEN 1B, YB 1B, GAIB 1B, STABLE 100B, UP 1B, CHIP 10B, SLX 1B, CAP 10B.
- **"Scale" (the denominator):** for stablecoin issuers this is stablecoin supply (DefiLlama stablecoins). For lending/credit or non-issuer protocols it is DefiLlama TVL. DefiLlama TVL for lending protocols is **net of borrowed**, so gross = TVL + "borrowed", which matters a lot for USD.AI (see Q5).

---

## Q1. Comparison table: FDV vs TVL at TGE and now, and the price path 1/3/6 months after TGE

### Takeaway
Across 22 stablecoin, yield-dollar and RWA-credit tokens, the 2025 cohort was the worst. Its median token is **-86% below its day-1 FDV**, 13 of 14 are down, and the median path was -45% at 1 month, -62% at 3 months and -77% at 6 months. At 2026-09-28, CHIP (FDV ≈$443M, 2.0x net TVL / 0.71x gross TVL incl. loans) is down 27% from its day-1 close but still 1.48x its $0.03 ICO price. That places it in the middle of the peer range, which spans roughly 0.05x (SYRUP) to 2.4x (ONDO) FDV/TVL for live, non-broken protocols.

### Cited Findings

**Table A: at TGE** (FDV in $M. "D1" = day-1 close from daily data. Scale = stablecoin supply or TVL at TGE, from DefiLlama unless noted.)

| Token (protocol) | TGE / listing date | Scale at TGE ($M) | FDV D1 ($M) | FDV 1st-week avg ($M) | Opening / intraday FDV from news | FDV/Scale at TGE |
|---|---|---|---|---|---|---|
| **CHIP (USD.AI, subject)** | TGE 2026-03-30 (claims); trading 2026-04-21/22 | 284 net TVL (344 gross incl. $61M loans); USDai 281 | 608 | 816 | ICO $0.03 = $300M; ATH $0.140 = $1.40B on 04-23 | 2.14x net / 1.77x gross |
| ENA (Ethena) | 2024-04-02 | USDe 1,560 | 11,721 | 16,358 | – | 7.5x |
| USUAL (Usual) | 2024-11-18/19 | USD0 364 | 4,288 (4B max) | 4,807 | – | 11.8x |
| SYRUP (Maple) | 2024-11-13 | TVL 316–340 (gross ~595 incl. borrowed) | 245 | 247 | – | 0.78x (0.41x gross) |
| ONDO (Ondo) | 2024-01-18 | ~190 (estimate, unverified) | 2,196 | 2,346 | – | ~11.6x (est.) |
| AVL (Avalon) | 2025-02-12 | USDa 255 (protocol TVL 1,794 incl. BTC CeDeFi) | 397 | 310 | – | 1.56x (0.22x on total TVL) |
| ELX (Elixir) | 2025-03-07 | deUSD 291 | 385 | 471 | – | 1.32x |
| HUMA (Huma) | 2025-05-26 | ~50 (Huma 2.0 deposits as of 29 May 2025) | 669 | 477 | ATH $0.1156 = $1.16B on TGE day | ~13x |
| RESOLV (Resolv) | 2025-06-10/11 | USR 220 (TVL 351) | 343 | 279 | – | 1.56x |
| SPK (Spark) | 2025-06-17 | TVL 6,273 | 571 | 478 | – | 0.09x |
| TREE (Treehouse; ETH-rate, not a stable) | 2025-07-29 | TVL 560 | 674 | 501 | ATH $1.36 = $1.36B | 1.2x |
| DAM (Reservoir) | 2025-08-18 | rUSD 61 | 96 | 65 | – | 1.57x |
| WLFI (USD1 issuer) | 2025-09-01 | USD1 2,462 | 23,362 | 21,278 | – | 9.5x |
| XPL (Plasma, stablecoin L1) | 2025-09-25 | on-chain stables 2,052 | 12,800 | 11,987 | $8.6–10.4B early trading; $500M public-sale FDV | 6.2x |
| FF (Falcon) | 2025-09-29 | USDf 1,899 | 2,842 | 2,005 | ATH $0.77 = $7.7B on listing day | 1.5x (≈4x on intraday) |
| EDEN (OpenEden) | 2025-09-30 | USDO 235 (excl. TBILL) | 402 | 367 | Paprika ATH $1.53 listing wick (unverified) | 1.7x |
| YB (Yield Basis; BTC LP, not a stable) | 2025-10-15 | TVL 153 | 677 | 487 | sale $0.20 = $200M FDV | 4.4x |
| GAIB (GAIB, AI/GPU synthetic dollar AID) | 2025-11-19 | AID 21 / TVL 18 | 165 | 86 | ATH $0.249 = $249M on TGE day; "reference FDV" $120M | 7.9x |
| STABLE (Stable, USDT L1) | 2025-12-08 | pre-deposits ~1,100 (phase 2) | 1,770 | 1,659 | opened ~$0.036 (≈$3.6B), high ~$0.046 | 1.6x |
| UP (Unitas, Solana JLP-hedged) | 2026-03-13/15 | USDu 83 | 72 | 110 | – | 0.87x |
| SLX (Solstice, Solana delta-neutral) | 2026-05-25 | USX 401 | 207 | 220 | ICO $130M FDV | 0.52x |
| CAP (Cap, covered credit cUSD) | 2026-06-26 | TVL 221 net / 265 gross; cUSD 68 | 275 | 254 | auction $106M FDV; day-1 close $325M | 1.24x (1.04x gross) |

**Table B: now (2026-09-28)** (current price from DefiLlama `/prices/current`. Mcap from DefiLlama protocol `mcap` field or CoinGecko where noted, otherwise CoinPaprika.)

| Token | Price | FDV ($M) | Mcap ($M) | Scale now ($M) | FDV/Scale now | Ann. fees ($M, 30d×12.17) | FDV/fees | FDV vs D1 | FDV vs ATH |
|---|---|---|---|---|---|---|---|---|---|
| **CHIP** | 0.0443 | 443 | 88.5 (20% circ, CoinGecko) | TVL net 219; borrowed 401; **gross 620**; USDai 215 | **2.0x net / 0.71x gross** | 20.6 (rev 2.1) | **21.5x** (FDV/rev ~214x on 30d; ~61x on 1y rev $7.2M) | -27% | -68% (vs $0.140) |
| ENA | 0.263 | 3,947 | 2,647 | USDe 4,944 / TVL 5,376 | 0.80x / 0.73x | 244.5 | 16.1x | -66% | -83% (vs $1.52) |
| USUAL | 0.0151 | 60 | ~29 | USD0 547 | 0.11x | 4.1 | 14.5x | -99% | -99% |
| SYRUP | 0.210 | ~252 | ~243 | TVL 3,006; gross 4,766 | 0.08x / 0.05x | 109.4 (rev 16.3) | 2.3x (15.5x rev) | ~-6% | -68% |
| SKY | 0.0806 | 1,890 | 1,889 | USDS+DAI ~11,400; TVL 5,938 | 0.17x | 329 (rev 164) | 5.7x (11.5x rev) | +18% (vs rebrand) | -19% |
| ONDO | 0.523 | 5,234 | 2,542 | USDY 2,194 (Ondo total RWA larger) | 2.4x (vs USDY only) | 81.4 | 64x | +138% | -76% |
| AVL | 0.0224 | 22 | ~3.6 | USDa 146 | 0.15x | – | – | -94% | -97% |
| ELX | 0.0012 | 1 | ~1 | deUSD wound down | n/m | – | – | -100% | -100% |
| HUMA | 0.0266 | 266 | 46 | TVL 372 (DefiLlama only from May 2026) | 0.71x | 29.5 | 9.0x | -60% | -77% |
| RESOLV | 0.0186 | 19 | ~9 | USR ~6 (post-exploit) | n/m | – | – | -95% | -95% |
| SPK | 0.0228 | 228 | 39–76 (sources conflict) | TVL 7,152; gross 10,025 | 0.03x | 173.7 | 1.3x | -60% | -88% |
| TREE | 0.046 | 46 | ~7 | TVL 75 | 0.61x | – | – | -93% | -97% |
| DAM | 0.0022 | 2 | ~1 | rUSD ~0 | n/m | – | – | -98% | -98% |
| WLFI | 0.0564 | 5,644 | 1,794 | USD1 4,415 | 1.28x | – | – | -76% | -77%+ |
| XPL | 0.1006 | 1,006 | 182–457 (sources conflict) | on-chain stables 1,460 | 0.69x | ~0.2 | n/m | -92% | -95% |
| FF | 0.130 | 1,299 | 407 (CoinGecko, 31.4% circ) | USDf 1,213 | 1.07x | 3.2 (DefiLlama likely undercounts) | n/m | -54% | -83% |
| EDEN | 0.0587 | 59 | ~11 | USDO 15 | 3.9x (USDO only) | 1.5 | 40x | -85% | -85% to -96% |
| YB | 0.0842 | 84 | ~7 | TVL 135 | 0.62x | – (1y fees 27.7) | ~3x (1y) | -88% | -90% |
| GAIB | 0.0300 | 30 | 6.1 (20.5% circ) | AID 19 | 1.58x | 2.2 | 13.7x | -82% | -88% |
| STABLE | 0.0271 | 2,713 | ~478 | on-chain stables **25** | ~108x | n/a | n/a | +53% | -37% |
| UP | 0.268 | 268 | 39–57 | USDu 44 | 6.1x | n/a | n/a | +272% | -48% |
| SLX | 0.0659 | 66 | 16 | USX 216 | 0.31x | 0.6 | 108x | -68% | -90% |
| CAP | 0.0554 | 554 | 87 | TVL 288 net / 348 gross | 1.9x / 1.59x | 6.0 | 93x | +101% | -24% to -37% |

**Table C: price path after TGE** (% vs day-1 close, daily data)

| Token | +30d | +90d | +180d | Now |
|---|---|---|---|---|
| **CHIP** | -18% | -51% | n/a (157 days) | -27% |
| ENA | +2% | -32% | -53% | -66% |
| USUAL | -7% | -77% | -88% | -99% |
| SYRUP | -14% | -50% | +23% | -6% |
| ONDO | +15% | +276% | +409% | +138% |
| AVL | +21% | -27% | -63% | -94% |
| ELX | -68% | -76% | -67% | -100% |
| HUMA | -48% | -57% | -63% | -60% |
| RESOLV | -56% | -52% | -78% | -95% |
| SPK | -40% | +24% | -63% | -60% |
| TREE | -42% | -71% | -83% | -93% |
| DAM | -26% | -68% | -81% | -98% |
| WLFI | -12% | -32% | -52% | -76% |
| XPL | -70% | -90% | -92% | -92% |
| FF | -49% | -67% | -75% | -54% |
| EDEN | -59% | -83% | -94% | -85% |
| YB | -33% | -39% | -82% | -88% |
| GAIB | -77% | -81% | -88% | -82% |
| STABLE | -21% | +57% | +92% | +53% |
| UP | +177% | +404% | +495% | +275% |
| SLX | +56% | -67% | n/a | -68% |
| CAP | -24% | +92% | n/a | +101% |

Cohort medians computed from Table C:
- **2024 (n=4):** -2.5% at 30d, -41% at 90d, -15% at 180d, -36% now.
- **2025 (n=14):** -45% at 30d, -62% at 90d, -76.5% at 180d, -86.5% now, with 13 of 14 below day-1 close.
- **2026 (n=4):** +19% at 30d, +20.5% at 90d, +37% now, with 2 of 4 below.

All three tables are computed from the DefiLlama APIs (see data notes). The cited facts behind them:
- USD.AI's TVL on DefiLlama is $218.6M supplied (Arbitrum) plus $401.4M "borrowed", for $620M gross. Borrowed rose from ~$18M (Apr 2026) to $106M (May), $236M (Aug) and $401M (2026-09-28). Net TVL peaked at $702M on 2025-11-22 and fell to $160M on Aug 1 2026 as idle deposits rotated into loans. — [DefiLlama USD AI](https://defillama.com/protocol/usd-ai)
- The CHIP CoinList sale was at $0.03 per token, 700M CHIP (7% of supply), raising $19.4M, dated Feb 27 2026. ICO Drops shows FDV $448.6M and price $0.04431 on 2026-09-28. — [ICO Drops USD.AI](https://icodrops.com/usd-ai/)
- The CHIP sale FDV was $300M on 10B total supply, and the airdrop was 300M CHIP (3%), fully unlocked at TGE. — [Coin Gabbar](https://www.coingabbar.com/en/crypto-currency-news/usd-ai-airdrop-chip-token-coinlist-sale-tge-march-2026-details)
- CoinGecko shows CHIP at $0.04428: mcap $88.56M, FDV $442.8M, circulating 2.0B of 10B, ATH $0.140189 (2026-04-23), ATL $0.02162 (2026-08-09). — [CoinGecko USD.AI](https://www.coingecko.com/en/coins/usd-ai)
- Circle's ARC presale sold 740M ARC at $0.30, raising $222M at a $3B FDV (May 2026). Investors included a16z crypto ($75M), BlackRock, Apollo and ICE. The token is not yet trading, which makes it a private-market mark for "stablecoin infrastructure". — [The Block](https://www.theblock.co/post/400709/circle-raises-222m-in-arc-token-presale-at-3b-fdv-from-a16z-crypto-blackrock-and-others-q1-revenue-up-20); [CNBC](https://www.cnbc.com/2026/05/11/circle-closes-222-million-from-blackrock-apollo-for-arc-blockchain.html)
- Plasma: the public sale was 10% of XPL at $500M FDV. Early trading was $0.90–1.10, or $8.6–10.4B FDV (Sep 25 2025). — [The Defiant](https://thedefiant.io/news/blockchains/plasma-mainnet-beta-xpl-token-launch); [Plasma on X](https://x.com/Plasma/status/1927370359696765241)
- Plasma deposits "proved temporary, with much of the capital having arrived to chase XPL incentives". By mid-August 2026 there were ~$710M of stablecoins on Plasma. DefiLlama shows $1.46B on 2026-09-28, down from a $6.35B peak on 2025-10-09. — [Datawallet](https://www.datawallet.com/crypto/what-is-plasma-chain)
- STABLE opened at ~$0.036, peaked near $0.046, then fell over 60% to $0.015. By 9 PM on Dec 9 2025 its FDV was $1.7B. Phase-2 pre-deposits were >$1.1B from 10,000+ wallets. — [Bitget/PANews via search](https://www.panewslab.com/en/articles/2050e827-52be-412e-9b7a-5cf172897c6b); [Bitget News](https://www.bitget.com/news/detail/12560605101899)
- Stable's FDV was $2.68B with $0 24h DEX volume (May 2026); the author calls it a "pricing puzzle". DefiLlama shows only ~$25M of stablecoins on Stable now, down from a $706M peak on 2025-12-16. — [BlockEden](https://blockeden.xyz/blog/2026/05/07/stable-l1-2-5b-fdv-zero-dex-volume-stablecoin-chain)
- The CAP auction cleared at ~$0.011, a $106M FDV, raising $16.4M from 1,002 bids at 5.5x oversubscription. The auction floor FDV was $75M. — [The Defiant](https://thedefiant.io/news/defi/cap-labs-cap-token-auction-106m-fdv-oversubscription)
- CAP closed its first 24 hours at a $325M FDV and traded ~$900M in its first 10 days. >$260M of deposits were on platform at launch. The seed was $11M (Apr 2025) from Franklin Templeton, Susquehanna and others. — [GlobeNewswire](https://www.globenewswire.com/news-release/2026/07/07/3323565/0/en/cap-token-debuts-with-nearly-900m-in-10-day-volume-closing-at-a-325m-fdv-in-first-24-hours.html)
- The Solstice ICO on Legion targeted $6.5M at a $130M FDV. SLX went live on Binance Alpha on May 25 2026. — [ICO Drops / search summary](https://icodrops.com/solstice/); [Coin Gabbar](https://www.coingabbar.com/en/price-prediction/solstice-listing-slx-tge-binance-alpha-airdrop-price-prediction)
- The Yield Basis public sale sold 2.5% of supply at $0.20 ($200M FDV) via Kraken Launch, Legion and Binance Wallet. It listed on Oct 15 2025 on Binance and Kraken. — [KuCoin News](https://www.kucoin.com/news/flash/kraken-and-legion-launch-yield-basis-yb-token-sale-with-200m-fdv)
- GAIB: TGE was Nov 19 2025 on Binance Alpha plus futures. The reference FDV was $120M with 21.3% initial circulation. Funding was a $5M pre-seed (Dec 2024; Hack VC, Faction, Hashed) plus a $10M strategic round (Jul 2025, led by Amber Group). — [Bitget Web3 Academy](https://web3.bitget.com/en/academy/gaib-listing-airdrop-guide-gaib-launch-date-what-is-gaibs-synthetic-ai-dollar-and-yield-system); [The Block](https://www.theblock.co/post/329306/crypto-ai-startup-gaib-funding)
- Huma 2.0 had $50M of USDC deposits from 53,400 depositors between its Apr 9 launch and May 29 2025. Deposits were $65.1M on Jun 30 and $151.6M on Sep 30 2025. Huma's Series A was $38M (Sep 2024), led by Distributed Global. — [Messari Q3 2025 via search](https://messari.io/report/state-of-huma-finance-q3-2025); [PR Newswire](https://www.prnewswire.com/news-releases/huma-raises-38m-to-hyper-scale-its-payfi-network-302247644.html)
- Resolv: USR depegged after an attacker minted 80M unbacked USR on 2026-03-22 and extracted ~$25M. — [The Block](https://www.theblock.co/post/394582/resolvs-usr-stablecoin-depegs-after-attacker-mints-80-million-unbacked-tokens-extracts-roughly-25-million); [CoinDesk](https://www.coindesk.com/markets/2026/03/23/resolv-stablecoin-drops-70-after-usd80-million-exploit-after-attacker-mints-usr)
- Elixir sunset deUSD after Stream Finance's $93M loss in Nov 2025. Stream owed Elixir >$68M, and deUSD fell ~98%. — [The Block](https://www.theblock.co/post/377961/elixir-sunsets-deusd-synthetic-stablecoin-following-stream-finance-unwinding-aims-full-redemptions); [Pharos](https://pharos.watch/learn/case-studies/stream-elixir-contagion-2025/)
- Level (lvlUSD) never held a TGE. In Sept 2025 the team joined Sky/Grove and sunset the protocol (last yield Oct 2 2025, front end retired Dec 15 2025). — [Bitget News](https://www.bitget.com/news/detail/12560604988048)
- infiniFi has no token yet; its TGE is guided to Q4 2026 (seed $3M+ led by Electric Capital). — [KuCoin blog](https://www.kucoin.com/blog/infinifi-3m-seed-funding-electric-capital)
- DefiLlama shows no traded token for Strata, Perena, M0, Agora, Noble, Midas, Avant, Neutrl, Re Protocol or Apyx as of 2026-09-28. — [DefiLlama](https://defillama.com/)
- Fees and revenue (30-day, DefiLlama): Ethena fees $20.09M; Maple fees $8.99M / revenue $1.34M; Sky fees $27.03M / revenue $13.47M; Spark fees $14.27M; Huma fees $2.42M; Ondo fees $6.69M; Cap fees $0.49M; GAIB fees $0.18M; USD.AI fees $1.69M / revenue $0.17M. USD.AI's 1-year totals are $24.5M fees and $7.2M revenue. — [DefiLlama fees](https://defillama.com/fees)

### Inferences
- **FDV/scale "now" medians** are ~0.45x for the 2024 cohort, ~1.07x for 2025 (excluding dead protocols) and ~1.96x for 2026 (Q1–Q3 1.5–3.0x). CHIP is at 2.0x net, right at the 2026 median, or 0.71x on gross deposits incl. loans. That is below FF (1.07x), GAIB (1.58x) and CAP (1.59x gross), in line with HUMA (0.71x) and ENA (0.73–0.80x), and far above SYRUP (0.05x gross).
- **FDV/annualized fees:** the peer median of 10 comparable tokens with fee data is ~14x. SYRUP 2.3x, SPK 1.3x, SKY 5.7x, HUMA 9.0x, GAIB 13.7x, USUAL 14.5x, ENA 16.1x, EDEN 40x, ONDO 64x, CAP 93x. CHIP at 21.5x trailing fees is above the median but well below CAP/ONDO. Its fee run-rate is likely understated because loans nearly doubled in Aug–Sep 2026.
- **GAIB is the closest business-model comp** (AI/GPU-financing synthetic dollar) and is a cautionary one. It launched at a $165M D1 FDV (intraday $249M) on only ~$21M of AID, fell 77% in 30 days and now sits at $30M FDV. CHIP launched with ~13x more TVL and major-venue listings, and has held up far better (-27% vs D1, +48% vs ICO).

### Gaps
- ONDO's TVL at TGE (Jan 2024) is not in the DefiLlama API response (`tvl` array empty). The ~$190M figure is an unverified estimate.
- OpenEden TBILL AUM at TGE is not in DefiLlama. The EDEN multiple uses USDO only, so it overstates the ratio.
- The Falcon fee data on DefiLlama ($0.26M/30d on $1.2B USDf) looks like an undercount. No reliable FF FDV/revenue figure was found.
- Circulating mcap for SPK and XPL conflicts between DefiLlama and CoinPaprika (e.g. XPL $457M vs $182M). This is likely stale unlock data at one source.
- NOON (Noon Capital) and GROVE (Grove Finance) traded in 2026, but their supply/FDV could not be verified, so they are excluded.
- CoinGecko rate-limited this session, so circulating supply at TGE could not be pulled from its market_chart. The circ % figures come from listing announcements (Q2).

---

## Q2. Listing venues (Binance spot/Alpha/HODLer/Launchpool, Coinbase, Bybit, OKX, Upbit) and their effect on FDV

### Takeaway
Tier-1 spot plus Binance Launchpool/HODLer listings produced the highest opening FDVs, and the steepest post-TGE declines followed from those high opens: ENA, USUAL, HUMA, FF, EDEN, TREE, XPL. Alpha-only or auction launches opened at much lower FDVs and were the only 2026 tokens to trade above launch (CAP, UP). CHIP had one of the strongest venue sets of any 2026 launch (Binance, Coinbase, Upbit, Bithumb, Kraken, Bybit; Hyperliquid perps). That set gave it a 4.7x day-2 spike versus ICO, followed by an ~85% drawdown into August. Launch valuation mattered more than venue for later performance.

### Cited Findings
- **ENA:** 50th Binance Launchpool project. Spot trading opened Apr 2 2024 with ENA/BTC, USDT, BNB, FDUSD and TRY pairs. The 750M airdrop was 5% of supply. — [Binance announcement](https://www.binance.com/en/support/announcement/introducing-ethena-ena-on-binance-launchpool-farm-ena-by-staking-bnb-and-fdusd-6c216f219f0e42adb1849759dee3fbd9); [CoinJournal](https://coinjournal.net/news/binance-adds-ethena-ena-as-50th-launchpool-project/)
- **USUAL:** Binance Launchpool farming ran Nov 15–18 2024, with Pre-Market trading from Nov 19 2024. Circulating at listing was 494.6M of 4B (12.37%). — [Binance Square](https://www.binance.com/en/square/post/11-14-2024-binance-launches-usual-usual-on-launchpool-with-pre-market-trading-to-follow-16224040648377)
- **HUMA:** Binance Launchpool (May 23–26 2025) plus Alpha. Initial circulating was 17.3% of 10B. Current venues include Binance, OKX, Bybit, Bithumb and others (CoinGecko). — [Bitget Academy](https://www.bitget.com/academy/human-finance-huma-airdrop-listing-date-investor-guide); [CoinGecko](https://www.coingecko.com/en/coins/huma-finance)
- **RESOLV:** Binance Alpha plus futures on Jun 10 2025, with a Binance HODLer Airdrop post. — [TradingView/CoinMarketCal](https://pl.tradingview.com/news/coinmarketcal:7d4e4f9ae094b:0-resolv-resolv-binance-alpha-listing-10-jun-2025); [Binance Square](https://www.binance.com/en/square/post/25532550057017)
- **TREE:** Binance HODLer Airdrop and spot listing on Jul 29 2025. Circulating at listing was 156.1M (15.61%). — [ChainCatcher](https://www.chaincatcher.com/en/article/2193825)
- **FF:** Binance HODLer Airdrop (49th project) with spot on Sep 29 2025. Circulating at listing was 2.34B (23.4%). CoinGecko now also lists Upbit, Bithumb, Kraken, Bybit and others. — [Binance Square](https://www.binance.com/en/square/post/09-26-2025-binance-to-list-falcon-finance-ff-on-sept-29-bnb-hodler-airdrop-live-for-eligible-users-30200061222225); [CoinGecko](https://www.coingecko.com/en/coins/falcon-finance-ff)
- **EDEN:** Binance HODLer Airdrop (47th project), spot on Sep 30 2025, circulating at listing 183.87M (18.39%). Upbit listed EDEN (BTC/USDT markets) on Aug 10 2026. — [PANews](https://www.panewslab.com/en/articles/22c47f7b-cdf5-4024-9e34-13f5903267ff); [CryptoRank](https://cryptorank.io/news/feed/80cae-upbit-lists-six-altcoins-including-depin-and-ai-tokens-in-btc-and-usdt-markets)
- **XPL:** Binance, OKX, Bitget and Bitfinex listed it on Sep 25 2025, with Binance spot from ~13:00 UTC. — [The Defiant](https://thedefiant.io/news/blockchains/plasma-mainnet-beta-xpl-token-launch)
- **STABLE:** Bitfinex listed it at TGE (Dec 8 2025), with Bitget, Backpack and Bybit also announcing. Binance, Coinbase and the Korean exchanges had not announced spot at TGE. Funding was a $28M seed led by Bitfinex and Hack VC. — [Bitfinex blog](https://blog.bitfinex.com/media-releases/bitfinex-to-list-stable-governance-token-of-the-stable-network/); [PR Newswire](https://www.prnewswire.com/news-releases/tether-focused-layer-1-stable-closes-28-million-funding-302518096.html)
- **GAIB:** Binance Alpha plus Binance Futures (Nov 19 2025). Current CoinGecko spot venues are Bitget, Bybit, Kraken, MEXC and others, with no Binance spot. — [Bitget Academy](https://www.bitget.com/academy/what-is-gaib-and-how-does-it-work); [CoinGecko](https://www.coingecko.com/en/coins/gaib)
- **UP:** the 44th Binance Wallet Exclusive TGE (Mar 13 2026). Hard cap 1B, 12.6% circulating at launch. — [MEXC blog](https://blog.mexc.com/news/what-is-unitas-labs-up-yield-bearing-stablecoin-earning-8-15-apy-binance-tge-march-13/); [PANews](https://www.panewslab.com/en/articles/019cdc4b-8469-7510-87e5-998d3d389778)
- **CAP:** launched via Binance Wallet on Jun 26 2026, with spot on Coinbase, Binance Alpha, Kraken, Bybit, Bithumb, Crypto.com and others, plus perps on Binance, OKX, Bybit, Bitget and Hyperliquid-style venues. Initial circulation is 15.6% per Bitget but ~5% per the Cap press release (the sources conflict). — [GlobeNewswire](https://www.globenewswire.com/news-release/2026/07/07/3323565/0/en/cap-token-debuts-with-nearly-900m-in-10-day-volume-closing-at-a-325m-fdv-in-first-24-hours.html); [Bitget News](https://www.bitget.com/asia/amp/news/detail/12560605474641)
- **CHIP:** listed on Binance and Coinbase around Apr 21 2026, together with Upbit and Bithumb, and Hyperliquid perps from Apr 22. The ATH was $0.1383 on Apr 23. — [search summary of CoinGecko/CMC/MEXC](https://www.coingecko.com/en/coins/usd-ai). CoinGecko's current ticker list includes Binance, Coinbase Exchange, Upbit, Bithumb, Kraken, Bybit, KuCoin, Gate and HTX. — [CoinGecko](https://www.coingecko.com/en/coins/usd-ai)
- **Memento Research (via The Defiant headline):** "Token launches with low FDVs vastly outperformed hyped debuts in 2025"; the article body was not retrievable. — [The Defiant](https://thedefiant.io/news/research-and-opinion/token-launches-with-low-fdvs-vastly-outperformed-hyped-debuts-in-2025-memento-research)

### Inferences
- The 8 tokens that got Binance spot via Launchpool or HODLer (ENA, USUAL, HUMA, RESOLV, TREE, FF, EDEN, XPL) have a median change of about -88% from day-1 close to now (range -54% to -99%, from Table C). Binance-spot distribution maximizes the opening FDV and supplies immediate sell-side liquidity for airdrop farmers.
- The two 2026 launches that are now above launch price (CAP +101%, UP +272%) both started at low FDVs ($72–275M D1) through auctions or the Binance Wallet. That supports the Memento thesis that a low launch FDV predicts outperformance.
- CHIP's venue set was top-tier, so the "new listing" catalyst is fully spent. An upside catalyst would have to come from fundamentals or a new mechanism such as a fee switch, not from venues.
- An Upbit listing gave only a modest boost in this cohort. EDEN rose +34% from Jun 30 to Aug 31 2026 around its Aug 10 Upbit listing, but is flat since.

### Gaps
- Exact first-hour or opening prices per venue were not collected for most tokens, because daily data misses listing wicks.
- There is no source confirming whether SPK or XPL were Binance HODLer airdrops (not verified here).

---

## Q3. FDV/TVL multiples at TGE by cohort: is the multiple compressing?

### Takeaway
**Yes. Launch multiples have compressed sharply.** Median FDV/scale at TGE fell from ~9.5x (2024) to ~1.6x (2025) to ~1.06x (2026). Post-TGE outcomes have worsened as well: the 2025 cohort median is -86% from day 1. CHIP's 2.1x at listing (on net TVL) was the highest of the 2026 cohort, i.e. it launched "rich" relative to 2026 peers, but it has since de-rated to ~2.0x net / 0.71x gross.

### Cited Findings
Cohort statistics are computed from Tables A and B (DefiLlama data, see Q1 sources):

| Cohort | n | FDV/scale at TGE: Q1 / median / Q3 | FDV/scale now: Q1 / median / Q3 | Median FDV change TGE → now |
|---|---|---|---|---|
| 2024 (ENA, USUAL, SYRUP, ONDO) | 4 | 5.8x / **9.5x** / 11.6x | 0.10x / 0.45x / 1.19x | -32% |
| 2025 (AVL, ELX, HUMA, RESOLV, SPK, TREE excluded, DAM, WLFI, XPL, FF, EDEN, YB, GAIB, STABLE) | 13 | 1.56x / **1.61x** / 6.24x | 0.65x / 1.07x / 2.37x (11 live) | -85% |
| 2025 core stablecoin issuers/credit (excl. chains, WLFI, SPK, YB) | 8 | 1.54x / **1.57x** / 3.25x | 0.80x / 1.32x / 2.77x | – |
| 2026 (UP, CHIP, SLX, CAP) | 4 | 0.78x / **1.06x** / 1.47x | 1.50x / 1.96x / 3.04x | +37% |
| All | 21 | 1.32x / 1.61x / 7.51x | 0.46x / 1.07x / 2.20x | – |

- 85% of 2025 token launches trade below TGE price, per Galaxy Research as reported by Bitget, with the context of BTC down ~46% from its Oct 6 2025 ATH. — [Bitget News](https://www.bitget.com/news/detail/12560605204237)
- 93% of 2024–2026 tokens that reached >$100M mcap trade below TGE price (8 of 113 above). The median return is -95.7%, with typical 50–70% declines within ~90 days. — [CryptoRank (via search summary; page 403 on fetch)](https://cryptorank.io/news/feed/91205-crypto-tokens-trade-below-launch-price)
- A Pine Analytics piece (Jan 28 2026), written before TGE, framed CHIP at a $300M FDV against $656M TVL (0.46x). It compared ENA at 0.38x ($6.5B USDe) and Maple at 0.16x ($2.55B TVL, ~$30M annualized revenue, 25% to buybacks). — [Pine Analytics](https://pineanalytics.substack.com/p/the-bear-case-for-chip)

### Inferences
- The compression reflects three things: (a) market-wide repricing of low-float/high-FDV launches, (b) a shift of airdrop venues from Launchpool to Alpha/Wallet, auctions (Echo/Sonar, Legion, CoinList, Kraken Launch) and lower list prices, and (c) the collapse of several 2025 yield-dollar protocols (Elixir, Resolv, Level, Stream contagion), which widened the risk discount.
- Even at compressed 2026 launch multiples, performance has been mixed (2 up, 2 down). The winners had low absolute FDV and growing TVL (CAP), or strong JLP-driven yields (UP, where USDu nonetheless fell 47% from TGE).
- The current dispersion is wide: ~0.03x (SPK) to ~6x (UP), excluding STABLE's ~108x on collapsed on-chain stablecoins. For a live credit/yield-dollar protocol, the "fair band" implied by peers is roughly 0.7x–1.6x FDV/gross TVL (HUMA, ENA, FF, GAIB, CAP), with SYRUP (0.05x) the cheap outlier.

### Gaps
- Sample sizes are small (2024 n=4, 2026 n=4), so treat quartiles as indicative.
- ONDO's TGE scale is estimated. HUMA's TGE scale uses Huma 2.0 deposits only (institutional/1.0 pools excluded), which likely overstates its launch multiple.

---

## Q4. Market backdrop Sept 2026 and the "stablecoin narrative is fading" thesis

### Takeaway
**Partly true.** Stablecoin supply growth stalled in 2026 (+1.6% YTD, first quarterly contraction in Q2 2026), and crypto-native yield dollars shrank 50–90% from their Oct 2025–Jan 2026 peaks. Most 2025 stablecoin TGEs are down 80–99%. **However**, since the July 2026 market bottom, stablecoin tokens with real traction have sharply outperformed BTC: ENA +235%, FF +98%, CAP +99%, GAIB +105%, ONDO +65%, SKY +53%, CHIP +36%, against BTC +38% (6/30 → 9/28). The current phase is better described as a shake-out and rotation (from crypto-native synthetic yield to RWA/credit/Treasury-backed yield) than as a uniform fade.

### Cited Findings
- **BTC** peaked at $126,173 intraday on 2025-10-06 (daily close ~$124.7k on 2025-10-07). It fell to ~$58.6k on 2026-07-01 (-53%) and was ~$83.0k on 2026-09-28. Month-end path: $88.4k (2025-12-31), $66.7k (2026-03-31), $60.1k (2026-06-30), $78.6k (2026-09-01). — [CoinPaprika](https://api.coinpaprika.com/v1/tickers/btc-bitcoin); [DefiLlama coins API](https://coins.llama.fi)
- **ETH** peaked at $4,946 intraday on 2025-08-24, bottomed at ~$1,565 on 2026-06-25, and was ~$2,665 on 2026-09-28. — [CoinPaprika](https://api.coinpaprika.com/v1/tickers); [DefiLlama coins API](https://coins.llama.fi)
- BTC is ~38% below its Oct 2025 peak after rebounding ~24% from August lows. The Altcoin Season Index is at 39 (down from ~67 in early August), total crypto market cap is ~$2.75T, and "a broad altcoin season has not started". — [Yahoo Finance / Bitrue / KuCoin via search](https://finance.yahoo.com/markets/crypto/articles/altcoin-season-starting-september-two-154722584.html); [Bitrue](https://www.bitrue.com/blog/crypto-september-outlook)
- **Total stablecoin supply** (DefiLlama): $204.8B (2025-01-01), $252.0B (2025-06-30), $296.1B (2025-09-30), $306.7B (2025-12-31), $313.2B (2026-03-31), peak $320.8B (2026-05-17), $309.6B (2026-06-30), $311.5B (2026-09-28). That is +50% in 2025 but only +1.6% YTD 2026. — [DefiLlama stablecoins](https://defillama.com/stablecoins)
- Q2 2026: yield-bearing stablecoin supply fell >$3.5B (-15%), ending nearly 3 years of quarterly growth. Total stablecoins posted their first quarterly contraction since Q3 2023 (to $312B from a $315B record). sUSDe -52% (~$2B), sUSDS -16%, while BUIDL +2%, USYC +16% and USDY +66%. Data from CEX.IO and Talos (Jul 2 2026). — [CoinMarketCap Academy](https://coinmarketcap.com/academy/article/yield-bearing-stablecoin-supply-falls-q2-2026-treasury-backed-growth); [CEX.IO](https://blog.cex.io/ecosystem/q2-2026-stablecoin-report-35673)
- **Yield-dollar supply collapses** (DefiLlama, peak → 2026-09-27):
  - USDe $14.82B (2025-10-04) → $4.94B (-67%)
  - USDf $2.15B → $1.21B (-44%)
  - USDai $663M (2026-01-20) → $215M (-68%); USD.AI gross deposits held up better at $620M
  - cUSD $443M → $87M
  - USX $523M (2026-07-31) → $216M
  - iUSD $191M → $50M
  - NUSD $231M → $41M
  - USDtb $1.84B → $536M
  - USR → ~$6M (exploit), lvlUSD → 0 (sunset), deUSD → wound down
  - Counter-trend: USD1 $4.4B, USDS $6.6B (peak $8.95B Apr 2026). — [DefiLlama stablecoins](https://defillama.com/stablecoins)
- **Ethena:** ENA hit an all-time low of ~$0.070 in June/July 2026 and remains ~89% below its $1.52 ATH. Ethena and FalconX announced a $1B warehouse facility on Aug 19 2026, and ENA rose 48% in a day (CoinDesk, Aug 21 2026). A fee switch (95% of net revenue to ENA buybacks) was approved Sep 2 2026, but it activates only when USDe supply reaches $7.5B (USDe ~$3.96B on Aug 18). — [CoinDesk](https://www.coindesk.com/markets/2026/08/21/ethena-surges-48-as-altcoins-pull-away-from-bitcoin); [CoinMarketCap ENA updates](https://coinmarketcap.com/cmc-ai/ethena/latest-updates/); [Bitcoin Foundation](https://bitcoinfoundation.org/news/analysis/ethena-ena-price-prediction-2026-is-the-project-slowly-dying-or-just-cooling-off/)
- **2026 returns** (DefiLlama daily; 2026-01-01 → 2026-09-28 / 2026-06-30 → 2026-09-28):

  | Token | YTD | Since Jun 30 |
  |---|---|---|
  | ENA | +32% | +235% |
  | FF | +46% | +98% |
  | ONDO | +35% | +65% |
  | SKY | +33% | +53% |
  | HUMA | +2% | +19% |
  | SPK | +4% | +30% |
  | SYRUP | -35% | +54% |
  | USUAL | -43% | +72% |
  | XPL | -41% | -4% |
  | WLFI | -61% | -2% |
  | YB | -79% | +25% |
  | TREE | -57% | +14% |
  | RESOLV | -74% | -2% |
  | GAIB | +9% | +105% |
  | STABLE | +94% | -29% |
  | CHIP | n/a | +36% (+104% from its Aug 9 low of $0.0217) |
  | CAP | n/a | +99% |
  | SLX | n/a | -88% |
  | UP | n/a | +5% |
  | **BTC** | **-5%** | **+38%** |
  | **ETH** | **-10%** | **+65%** |

  — [DefiLlama coins API](https://coins.llama.fi)
- **New-listing sentiment:** 85% of 2025 launches trade below TGE (Galaxy) and 93% of 2024–26 >$100M tokens are below TGE (CryptoRank). — [Bitget News](https://www.bitget.com/news/detail/12560605204237); [CryptoRank](https://cryptorank.io/news/feed/91205-crypto-tokens-trade-below-launch-price)
- Plasma's early deposits "proved temporary", with capital arriving "to chase XPL incentives". — [Datawallet](https://www.datawallet.com/crypto/what-is-plasma-chain)

### Inferences
- **Verify (fading):**
  - Supply growth for stablecoins overall has plateaued.
  - Crypto-native synthetic/basis yield dollars are down 45–70% from peak (USDe, USDf, USDai, USX, iUSD).
  - Stablecoin chain tokens are down more than 90% on XPL.
  - Launch FDVs have compressed ~9x in two years.
  - Several 2025 issuers failed outright (Elixir, Resolv, Level, Reservoir rUSD).
- **Refute (not dead):**
  - Institutional/RWA-backed products grew (USDY +66% in Q2).
  - Circle raised at a $3B FDV for ARC in May 2026.
  - Tokens with revenue and a recovery story (ENA, FF, SKY, ONDO) outperformed BTC and ETH in the Q3 2026 rebound.
  - The market is discriminating, not abandoning, the sector: it rewards credit/RWA yield and fee-switch/buyback mechanics and punishes incentive-driven TVL.
- For USD.AI this is double-edged. It sits in the favored "real-world credit yield" bucket: loans rose to $401M and a $40M K3 facility and a $100M Bullish facility were added. But its headline USDai supply fell 68% from peak, and CHIP has no revenue rights (Q5).

### Gaps
- There is no single authoritative source for 2026 altcoin/new-listing aggregate returns, only media-cited studies (Galaxy, CryptoRank) whose full methodology was not accessible.
- DefiLlama's Ethena revenue series shows near-zero 1-year "revenue" ($2.7M) against $267M fees. This is likely a methodology change, so ENA FDV/revenue was not computed.

---

## Q5. (Coordinator add-on) Where CHIP's FDV should trade over the next 1–6 months vs peers, and the April 2027 unlock cliff

### Takeaway
On peer multiples, CHIP's current ~$443M FDV sits inside the peer-implied band of roughly **$290M–$600M**. The low end (~$290M) comes from ~14x peer-median FDV/fees on trailing fees. The high end (~$580–600M) comes from ~0.95x peer-median FDV/gross TVL on $620M. Upside needs loan-book growth to show up in fees. Downside risk rises into Q1 2027 ahead of the ~April 2027 cliff, when ~1.75B CHIP (17.5% of supply, +~88% of today's float) unlocks at once.

### Cited Findings
- **CHIP state (2026-09-28):** price $0.0443, FDV $442.8M, mcap $88.6M, 2.0B circulating (20%). ATH $0.1402 (2026-04-23), ATL $0.0216 (2026-08-09). — [CoinGecko](https://www.coingecko.com/en/coins/usd-ai)
- **USD.AI scale:** DefiLlama shows supplied $218.6M plus borrowed $401.4M, for $620M gross. Loans ramped from ~$18M (Apr 1) to $401M (Sep 28). — [DefiLlama USD AI](https://defillama.com/protocol/usd-ai)
- **Company-reported figures:** $398M TVL and $202M deployed (June report), and TVL of $436.8M with 8.61% gross / 7.46% net APY around Aug 4 2026. — [search summary of CMC/USD.AI updates](https://coinmarketcap.com/cmc-ai/usd-ai/latest-updates/)
- **USD.AI financing:**
  - $40M revolving facility from K3 Capital (Sep 15 2026)
  - $100M facility from Bullish (Aug 2026)
  - named as expected issuer on PayPal's PYUSDx (Sep 11 2026)
  - migration from PYUSD to PYUSDx collateral planned for Q4 2026
  — [CoinMarketCap USD.AI updates](https://coinmarketcap.com/cmc-ai/usd-ai/latest-updates/)
- **USD.AI fees** (DefiLlama): $1.69M over 30 days (~$20.6M annualized) and $24.5M over 1 year. Revenue was $0.17M over 30 days and $7.2M over 1 year. — [DefiLlama fees](https://defillama.com/protocol/usd-ai)
- USD.AI: "At $1B in originations, this fee structure translates to $30M in annual revenue." Also: "CHIP does not entitle holders to protocol revenue." — [USD.AI Foundation/CHIP announcement](https://usd.ai/insights/usdai-foundation-chip)
- **CHIP vesting:** Core Contributors and Investors have a 12-month cliff, then 33% unlocks at month 12 and the remaining 67% unlocks monthly over 24 months (36 months total). Ecosystem is 27.5% and Reserve 19.8%. — [USD.AI docs: tokenomics](https://docs.usd.ai/governance/tokenomics)
- **Allocation:** Investors 29.6%, Contributors 23.5%, Ecosystem 27.5%, Reserve 19.5%. Circulating is ~2B (~20%). — [Datawallet](https://www.datawallet.com/crypto/usd-ai-chip-explained)
- **Funding:** Series A $13.4M (Aug 14 2025, led by Framework Ventures; investors include Dragonfly, CMT Digital, Arbitrum Foundation, Bullish). ICO Drops lists a "Strategic Round" (Aug 26 2025) with Binance Labs participation and a $4M round (Sep 23 2025). Its "$176.8M total raised" figure likely mixes in non-equity and should be treated with caution. — [ICO Drops](https://icodrops.com/usd-ai/)
- **Peer multiples now:** see Table B, Q1. FDV/gross-or-supply: SYRUP 0.05x, HUMA 0.71x, ENA 0.80x, FF 1.07x, GAIB 1.58x, CAP 1.59x. FDV/annualized fees: SYRUP 2.3x, SKY 5.7x, HUMA 9.0x, GAIB 13.7x, USUAL 14.5x, ENA 16.1x, CAP 93x. — [DefiLlama](https://defillama.com/)

### Inferences
- **Cliff arithmetic:** 33% × (29.6% + 23.5%) = **~17.5% of supply ≈ 1.75B CHIP** at month 12. The timing is ~late Mar–Apr 2027, depending on whether the clock starts at the Mar 30 TGE or the Apr 21–22 listing. That is +~88% of today's 2.0B float, worth ~$78M at $0.0443, about equal to the current mcap. After the cliff, ~1.48% of supply (~148M CHIP, ~$6.6M at the current price) unlocks monthly for 24 months.
- **Historical pre-cliff behavior** (inference; cliff dates assumed at TGE+12m and not individually verified), measured from 60 days before the cliff to the cliff date: ENA -52% (BTC -17%), USUAL -58% (BTC -20%), RESOLV -57% (BTC -16%), TREE -43% (BTC -13%), AVL -53% (BTC -26%), ELX -39% (BTC -27%). HUMA was the exception at +51% (BTC +8%). The median underperformance versus BTC in the 60 days before a cliff was ~25–35pp. For CHIP, that window is roughly **late Jan–Apr 2027**, i.e. months 4–6 of the requested horizon.
- **Scenario bands for CHIP FDV over 1–6 months** (analyst inference, not a forecast; based on peer multiples):
  - **Bear (~$200–300M FDV, $0.020–0.030):** fees stay at ~$20M/yr, the market applies the HUMA–GAIB fee multiples (9–14x), and pre-cliff selling starts in Q1 2027. The Aug 9 2026 low of $0.0216 (~$216M FDV) is the empirical floor reference.
  - **Base (~$350–550M, $0.035–0.055):** CHIP holds ~0.6–0.9x gross TVL ($620M → $700M) while loans keep scaling. This is consistent with where it has traded since mid-August.
  - **Bull (~$600M–1B, $0.06–0.10):** loans reach ~$0.7–1B, with fees ~$40–60M/yr at ~12–15% gross on the loan book and ENA/CAP-like multiples (16x+). It would also need a revenue-share or buyback mechanism for CHIP (none exists today) or an AI-infrastructure narrative bid. Reaching this before the April 2027 cliff looks less likely given the unlock overhang.
- **Relative-value framing:** on net TVL (2.0x), CHIP already trades at the 2026 cohort median, so it is not cheap. On gross deposits (0.71x) it is in line with HUMA and ENA. On trailing fees (21.5x) it is above the peer median (~14x). Its lack of revenue rights argues for a discount to SYRUP, SKY and ENA, which have buybacks or fee switches.

### Gaps
- The exact cliff date (anchored to the Mar 30 TGE or the Apr 21–22 listing) is not confirmed in official docs. Investor and contributor percentages come from Datawallet, not the official docs page.
- USD.AI's current gross loan yield and forward fee run-rate are not published in a verifiable dated source. The $40–60M bull-case fee figure is an inference from $401M in loans at an assumed ~12–15% gross rate.
- CHIP's circulating supply at listing (Apr 21) could not be confirmed from CoinGecko history because of the rate limit. The ~20% figure is current.
