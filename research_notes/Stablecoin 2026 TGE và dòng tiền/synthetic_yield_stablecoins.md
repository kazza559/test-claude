# Synthetic, delta-neutral and DeFi-native yield-bearing stablecoins: 2026 fact base (as of 21 Oct 2026)

Data conventions. "DL" = DefiLlama and "CG" = CoinGecko. All API pulls were made on 2026-10-21 at about 13:20 UTC unless another date is given. Stablecoin supply comes from DL's stablecoin API and protocol TVL from DL's protocol API. Prices, MC and FDV come from CG `/coins/markets` (last_updated 2026-10-21T13:20:50Z), and 2026 price paths from CG `/market_chart` (daily, 365 days). Unlock figures come from DL's public emissions datasets. "MC" always means circulating market cap and is reported separately from FDV.

Coverage limits:
- The shared web-search budget ran out early in this session. Most findings therefore come from primary data APIs, project docs and governance forums rather than news coverage.
- News-only facts (exact listing prices, airdrop sizes, causes of some outflows) are often missing. They are listed under Gaps rather than estimated.
- CG's own circulating-supply method can differ sharply from documented vesting. ENA is the clearest case: CG reports 13.41B circulating, while DL's documented unlocked supply is 10.33B.

---

## 1. Token scorecard: TGE'd tokens (TGE and venue, sale, listing, ATH, current price, MC vs FDV, airdrops, 6-month unlocks)

### Takeaway
Almost every synthetic or yield-dollar governance token is 70–99% below its ATH.
- ENA is roughly flat YTD (+4%) but went through a –64% drawdown to July and then a +282% rally to late September. The rally followed the fee-switch vote and the recovery in USDe supply.
- FF is the strongest of the large caps YTD (+26%). However, it starts roughly 6% of circulating supply per month in unlocks from 29 Oct 2026.
- 2026 TGEs split into three groups:
  - Above first trade: Unitas UP (+73%) and Cap CAP (+177%).
  - Moderately below: USD.AI CHIP (–28%).
  - Collapsed: Solstice SLX (–83%), MegaETH MEGA (–79%) and Mezo MEZO (–97%).
- RESOLV (–75% YTD) and ELX (~–99.9%) are effectively post-failure tokens.

### Cited Findings

**Large and seed-list tokens (CG markets, 2026-10-21; 2026 path from CG daily chart)**

- **ENA (Ethena)**
  - Price and size: $0.2083. MC $2,792.2M vs FDV $3,124.2M. Circulating 13,406M of 15,000M (CG).
  - Drawdown: ATH $1.52 on 2024-04-11, now –86.3%. CG ATL $0.0702 on 2026-06-30. One-year change –53.7%. — [CG markets](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=ethena)
  - 2026 path: $0.2000 on 1 Jan 2026 → $0.1387 (1 Feb) → $0.0908 (1 Apr) → 2026 low $0.0712 (2 Jul) → $0.1495 (1 Sep) → 2026 high $0.2722 (28 Sep) → $0.2081 (21 Oct). YTD +4.1%. — [CG chart](https://api.coingecko.com/api/v3/coins/ethena/market_chart?vs_currency=usd&days=365&interval=daily)
  - Implied circulating supply: CG's market-cap series implies MC of about $1,538M on 1 Jan 2026 (about 7.7B circulating at $0.200). MC has therefore risen far more than price because CG's circulating count rose. — [CG chart](https://api.coingecko.com/api/v3/coins/ethena/market_chart?vs_currency=usd&days=365&interval=daily)
  - Documented unlocked supply: DL's emissions dataset shows 10,327.6M ENA unlocked on 21 Oct 2026. At $0.2083 that implies roughly $2.15B MC on that basis. — [DL emissions ENA](https://defillama-datasets.llama.fi/emissions/ethena)
  - Vesting: core contributors (30%) and investors both have a 1-year 25% cliff followed by 3-year linear monthly vesting. The docs say vesting started at "ENA TGE at March 5th 2024", and 30% of supply goes to ecosystem development and airdrops. — [Ethena docs: Tokenomics](https://docs.ethena.fi/overview/ena/tokenomics)
  - Next 6 months (21 Oct 2026 → 21 Apr 2027): about 1,597.7M ENA unlocks (investors 467.2M, team 560.6M, ecosystem 327.0M, foundation 242.9M). That is about 266M a month, about 11.9% of CG circulating, or about $333M at today's price. — [DL emissions ENA](https://defillama-datasets.llama.fi/emissions/ethena)
  - sENA: market cap $204.9M (967.5M sENA). — [CG markets](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=ethena-staked-ena)
  - sENA holder distributions: "$BASED claiming live for sENA holders" (Mar–Apr 2026). — [Ethena Mar–Apr 2026 gov update](https://gov.ethenafoundation.com/t/ethena-s-march-and-april-2026-governance-update/791)
- **FF (Falcon Finance)**
  - Price and size: $0.1092. MC $365.2M vs FDV $1,092.3M. Circulating 3,343M of 10,000M.
  - Drawdown: ATH $0.7708 on 2025-09-29 (TGE day), now –85.8%. ATL $0.0571 on 2026-07-11. One-year change –25.5%. — [CG markets](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=falcon-finance-ff)
  - TGE date: Falcon Miles Season 2 "launched on September 29, 2025, coinciding with the FF Token Generation Event". Claimed FF could be auto-staked to sFF with multipliers. — [Falcon docs: Season 2 Miles](https://docs.falcon.finance/falcon-miles/season-2-miles)
  - Funding: DL raises list a $4M "public token sale" (2025-09-23), $10M from World Liberty Financial (2025-07-30) and $10M led by M2 Group (2025-10-09). — [DL protocol: falcon-finance](https://api.llama.fi/protocol/falcon-finance)
  - Venues: the top CG venues include Binance, WhiteBIT, Bybit, Upbit and Gate. — [CG coin FF](https://api.coingecko.com/api/v3/coins/falcon-finance-ff?tickers=true)
  - 2026 path: $0.0864 on 1 Jan → 2026 low $0.0583 (9 Jul) → 2026 high $0.1686 (11 Sep) → $0.1092. YTD +26.4%. — [CG chart](https://api.coingecko.com/api/v3/coins/falcon-finance-ff/market_chart?vs_currency=usd&days=365&interval=daily)
  - Unlocks: about 203.1M FF unlock monthly starting 2026-10-29 (core team, investors, ecosystem and foundation buckets). The next-6-month total is about 1,218.3M, or 36.4% of circulating (about $133M at spot). — [DL emissions Falcon](https://defillama-datasets.llama.fi/emissions/falcon-finance)
  - sFF staking vault: DL tracks $22.5M TVL. — [DL yields pools](https://yields.llama.fi/pools)
- **RESOLV (Resolv)**
  - Price and size: $0.01708. MC $8.8M vs FDV $17.1M. Circulating 514.7M of 1,000M.
  - Drawdown: ATH $0.4085 on 2025-06-11, now –95.8%. — [CG markets](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=resolv)
  - 2026 path: $0.0695 on 1 Jan → 2026 high $0.1302 (27 Jan) → $0.0445 (1 Apr, after the exploit) → $0.0171. YTD –75.4%. — [CG chart](https://api.coingecko.com/api/v3/coins/resolv/market_chart?vs_currency=usd&days=365&interval=daily)
  - Airdrops: Season 1 claims (TGE) ran 27 May–27 Jun, Season 2 claims 19 Sep–19 Oct, and Season 3 claims 16 Dec–16 Jan 2026. Season 3 was paid in stRESOLV. — [Resolv docs: airdrop](https://docs.resolv.xyz/litepaper/resolv-token/resolv-token-airdrop)
  - Unlocks: 159.9M over the next 6 months (team 53.4M, private sale 51.1M, ecosystem 34.3M, treasury 16.2M, advisors 5.0M). That is about 31% of circulating, but only about $2.7M of value. — [DL emissions Resolv](https://defillama-datasets.llama.fi/emissions/resolv)
  - Funding: $10M seed (Apr 2025; Cyber Fund, Maven 11). — [DL protocol: resolv](https://api.llama.fi/protocol/resolv)
- **ELX (Elixir)**
  - Price and size: $0.000635. MC $0.3M. ATH $0.735 on 2025-03-10, now –99.9%. — [CG markets](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=elixir-finance)
  - CG daily path: $0.095 (22 Oct 2025) → $0.0042 (1 Jan 2026), an odd rebound to $0.064 (1 Mar), then $0.0011 (1 Apr). Confidence is low because of thin liquidity. — [CG chart](https://api.coingecko.com/api/v3/coins/elixir-finance/market_chart?vs_currency=usd&days=365&interval=daily)
- **YALA (Yala)**
  - Price: $0.0000116, –99.997% from ATH $0.4505 (2025-08-08). CG data was last updated 2026-08-16. — [CG markets](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=yala)
  - Pivot: Yala's docs now describe YALA as the token of a "Yala AI ecosystem" with agent vaults and buybacks. — [Yala docs](https://docs.yala.org/prediction-market-intelligence/yala-tokenomics)
- **Level (lvlUSD issuer)**: no project token was found. CG's "LVL" (ATH 2023) is an unrelated Level Finance token. — [CG markets](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=level)

**Tokens that TGE'd in 2026 (or late 2025) in or near the sub-sector**

- **UP (Unitas; Solana/BSC JLP delta-neutral dollar)**
  - TGE: 13 Mar 2026. Core contributors have a 1-year cliff then 3-year monthly vesting; investors a 1-year cliff then 2-year monthly vesting. — [Unitas docs: tokenomics](https://docs.unitas.so/overview/up/tokenomics)
  - Price and size: $0.1381. MC $29.9M vs FDV $138.2M. Circulating 216M of 1,000M. ATH $0.5226 (2026-08-31), now –73.6%. 30-day change –58.9%. — [CG markets](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=unitas)
  - Versus first trade: first CG daily price $0.0797 (14 Mar 2026), so +73% to date. — [CG chart](https://api.coingecko.com/api/v3/coins/unitas/market_chart?vs_currency=usd&days=365&interval=daily)
  - Venues include Gate, MEXC, Bitget, Kraken and PancakeSwap. — [CG coin UP](https://api.coingecko.com/api/v3/coins/unitas?tickers=true)
  - Funding: $13.33M seed led by Amber Group (2026-03-12). — [DL protocol: unitas](https://api.llama.fi/protocol/unitas)
- **SLX (Solstice; Solana USX)**
  - Price and size: $0.0503. MC $12.2M vs FDV $50.3M. Circulating 242.8M of 1,000M. ATH $0.6582 (2026-06-27), now –92.4%. — [CG markets](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=solstice)
  - Versus first trade: first CG daily price $0.2982 on 25 May 2026 (MC about $96M), so –83%. — [CG chart](https://api.coingecko.com/api/v3/coins/solstice/market_chart?vs_currency=usd&days=365&interval=daily)
  - Venues include Upbit, OKX, Bybit, Bitget, Bithumb and MEXC; CG tags it "Binance Alpha Spotlight". — [CG coin SLX](https://api.coingecko.com/api/v3/coins/solstice?tickers=true)
  - Tokenomics (1B fixed; incubated by Deus X Capital):

    | Bucket | Share | Released at TGE | Vesting |
    |---|---|---|---|
    | Foundation | 24% | 50% | 20 months |
    | Community | 37.71% | 21.2% | 36 months |
    | Team & Advisors | 20% | 0% | 12-month cliff, then 24 months |
    | Airdrops (Flares) | 10% | varies | varies |
    | Strategic TVL Partners | 8% | 25% | 12 months |
    | Public sale (Legion) | 0.29% | 100% | none |

    — [Solstice docs: tokenomics](https://docs.solstice.finance/solstice-for-users/slx/tokenomics)
  - Unlocks: about 103.2M over the next 6 months (community 49.3M, strategic TVL partners 29.9M, foundation 23.9M). That is about 42.5% of CG circulating. — [DL emissions Solstice](https://defillama-datasets.llama.fi/emissions/solstice)
- **CAP (Cap; cUSD/stcUSD)**
  - Sale: a public token sale of $5.5M at a $110M valuation on 2026-06-17. Earlier rounds were an $8M seed (Apr 2025; Franklin Templeton, Triton) and a $1.9M pre-seed. — [DL protocol: cap](https://api.llama.fi/protocol/cap)
  - Price and size: $0.0680. MC $106.0M vs FDV $679.6M. Circulating 1,560M of 10,000M. ATH $0.1208 (2026-10-12). — [CG markets](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=cap-4)
  - Versus first trade: first CG daily price $0.0246 on 26 Jun 2026 (MC about $37M), so +177%. — [CG chart](https://api.coingecko.com/api/v3/coins/cap-4/market_chart?vs_currency=usd&days=365&interval=daily)
  - Venues include Upbit, Bybit, Bithumb, Coinbase Exchange, Kraken and Bitvavo. — [CG coin CAP](https://api.coingecko.com/api/v3/coins/cap-4?tickers=true)
  - Tokenomics: 10B supply. Ecosystem 47.37%, private investors ≤20%, team ≤20%, ICO 5%, private TVL deals 3.75%, Echo community sale 3.28%, market makers 0.6%. TGE float is about 15%.
  - Cliff-gated buckets unlock 25% at month 12 and then vest monthly over 3 years, so the first cliff is about late June 2027, outside the 6-month window.
  - "Revenue generated will be used to conduct discretionary buybacks." — [Cap docs: tokenomics](https://docs.cap.app/overview/tokenomics)
- **CHIP (USD.AI; GPU-loan-backed "synthetic dollar")**
  - Price and size: $0.0458. MC $91.6M vs FDV $457.8M. Circulating 2,000M of 10,000M. ATH $0.1402 (2026-04-23), now –67.3%. — [CG markets](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=chip-2)
  - Versus first trade: first CG daily price $0.0636 on 21 Apr 2026 (MC about $127M), so –28%. — [CG chart](https://api.coingecko.com/api/v3/coins/chip-2/market_chart?vs_currency=usd&days=365&interval=daily)
  - Venues: Binance, Upbit, Bybit, KuCoin and Coinbase. — [CG coin CHIP](https://api.coingecko.com/api/v3/coins/chip-2?tickers=true)
  - Allocation: ecosystem bootstrapping 27.5% (the first 10% went out in Season 1, "The Allo Game"); reserve 19.8%. Investors and core contributors receive 0% before month 12, 33% at month 12 and the rest monthly over 24 months. — [USD.AI docs: tokenomics](https://docs.usd.ai/governance/tokenomics)
  - Unlocks: a cliff of about 2,773M CHIP on 2027-04-16, about 139% of current circulating supply. The next-6-month total is 2,933M. — [DL emissions USD.AI](https://defillama-datasets.llama.fi/emissions/usd-ai)
- **MEZO (Mezo; BTC-backed MUSD)**
  - Price and size: $0.00286. MC $1.4M vs FDV $2.9M. ATH $0.1485 (2026-04-13), now –98.1%. — [CG markets](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=mezo)
  - Versus first trade: first CG daily price $0.1034 on 1 Apr 2026, so –97%. — [CG chart](https://api.coingecko.com/api/v3/coins/mezo/market_chart?vs_currency=usd&days=365&interval=daily)
  - Venues: Coinbase, Kraken, KuCoin and Gate. — [CG coin MEZO](https://api.coingecko.com/api/v3/coins/mezo?tickers=true)
- **MEGA (MegaETH; host chain of Ethena's USDm white-label)**
  - Price and size: $0.0462. MC $52.2M vs FDV $461.9M. — [CG markets](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=megaeth)
  - Versus first trade: first CG daily price $0.2164 on 30 Apr 2026 (MC about $244M), so –79%. — [CG chart](https://api.coingecko.com/api/v3/coins/megaeth/market_chart?vs_currency=usd&days=365&interval=daily)
  - Venues: Binance, Bybit, Upbit, OKX, Coinbase and Kraken. — [CG coin MEGA](https://api.coingecko.com/api/v3/coins/megaeth?tickers=true)
- **GAIB (AID "AI synthetic dollar")**
  - Price and size: $0.0199. MC $4.1M vs FDV $19.9M. ATH $0.2494 (2025-11-19, its first trading day), now –92%. — [CG markets](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=gaib)
  - Unlocks: 110.2M over the next 6 months, about 54% of CG circulating. — [DL emissions GAIB](https://defillama-datasets.llama.fi/emissions/gaib)
- **YB (YieldBasis)**
  - Price and size: $0.0648. MC $17.8M vs FDV $49.1M. ATH $0.8185 (2025-10-15), now –92.1%. — [CG markets](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=yield-basis)
  - 2026 path: $0.4003 on 1 Jan, so YTD –83.9%. — [CG chart](https://api.coingecko.com/api/v3/coins/yield-basis/market_chart?vs_currency=usd&days=365&interval=daily)
  - Funding: $5M at a $50M valuation (Feb 2025) and a $5M public token sale (Oct 2025). — [DL protocol: yield-basis](https://api.llama.fi/protocol/yield-basis)
  - Unlocks: 166.8M over the next 6 months, about 61% of CG circulating. — [DL emissions YB](https://defillama-datasets.llama.fi/emissions/yield-basis)
- **Yield-venue and ecosystem comparables (CG markets / chart, 21 Oct 2026)**:

  | Token | Price | MC | FDV | Performance | Source |
  |---|---|---|---|---|---|
  | PENDLE | $2.19 | $381.1M | $617.1M | –70.8% vs $7.50 ATH; 2026 low $1.018 (7 Apr); YTD +16.4% | [CG](https://api.coingecko.com/api/v3/coins/pendle/market_chart?vs_currency=usd&days=365&interval=daily) |
  | MORPHO | $2.39 | $1,678.4M | $2,388.3M | YTD +118%; 2026 high $2.90 (24 Aug) | [CG](https://api.coingecko.com/api/v3/coins/morpho/market_chart?vs_currency=usd&days=365&interval=daily) |
  | EUL | $1.20 | $28.9M | $32.7M | –92.4% vs ATH; YTD –60%; 2026 low $0.733 (30 Mar) | [CG](https://api.coingecko.com/api/v3/coins/euler/market_chart?vs_currency=usd&days=365&interval=daily) |
  | SKY | $0.0767 | $1,796.3M | — | YTD +32.6%; ATH $0.1009 on 5 Oct 2026 | [CG](https://api.coingecko.com/api/v3/coins/sky/market_chart?vs_currency=usd&days=365&interval=daily) |
  | HYPE | $81.59 | $18.15B | $77.9B | YTD +220%; ATH $97.96 (23 Sep 2026) | [CG](https://api.coingecko.com/api/v3/coins/hyperliquid/market_chart?vs_currency=usd&days=365&interval=daily) |
  | KNTQ | $0.3726 | $117.3M | — | YTD +542% | [CG](https://api.coingecko.com/api/v3/coins/kinetiq/market_chart?vs_currency=usd&days=365&interval=daily) |
  | USUAL | — | — | — | YTD –55.3%; –99.3% vs ATH | [CG](https://api.coingecko.com/api/v3/coins/usual/market_chart?vs_currency=usd&days=365&interval=daily) |
  | RIVER (satUSD) | $1.11 | — | — | $11.62 (1 Jan) → $85.11 (27 Jan) → $1.11; –98.7% from ATH | [CG](https://api.coingecko.com/api/v3/coins/river/market_chart?vs_currency=usd&days=365&interval=daily) |
  | STABLE | — | $485.8M | $2.699B | first trade $0.0268 (8 Dec 2025) | [CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=stable-2) |
  | XPL | — | — | — | –95.2% vs ATH; YTD –49.8% | [CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=plasma) |
  | ASTER | — | $1,957.6M | $5,614.1M | YTD +4.1% | [CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=aster-2) |

- **Other 6-month unlock loads (DL emissions, % of CG circulating)**:
  - [MORPHO](https://defillama-datasets.llama.fi/emissions/morpho): 53.1M (about 7.6%).
  - [ASTER](https://defillama-datasets.llama.fi/emissions/aster): 73.3M (about 2.7%).
  - [SPK](https://defillama-datasets.llama.fi/emissions/spark): 149.5M (about 4.4%).
  - [USUAL](https://defillama-datasets.llama.fi/emissions/usual): 268M (about 13.6%).
  - [KNTQ](https://defillama-datasets.llama.fi/emissions/kinetiq): 64.6M (about 20.5%).
  - [XPL](https://defillama-datasets.llama.fi/emissions/plasma): 1,366.7M (about 30%).
  - [STABLE](https://defillama-datasets.llama.fi/emissions/stable): 10,889M (about 60%).
  - [PENDLE](https://defillama-datasets.llama.fi/emissions/pendle): zero.

### Inferences
- The 2026 TGE cohort shows the "points → TGE → TVL exit" pattern more clearly than earlier cohorts (high confidence). SLX, MEGA, MEZO and GAIB lost 79–98% from their first prints. CAP and UP are the exceptions; they listed at low FDVs ($110M ICO for Cap) and rallied afterwards.
- The best-performing 2026 assets near this niche are not synthetic-dollar tokens. They are venue and infrastructure tokens: HYPE +220%, MORPHO +118%, KNTQ +542%, SKY +33% (high confidence). Capital rewarded where stablecoin yield is distributed (lending and exchanges) more than synthetic issuers themselves.
- ENA's +282% move from the July low to 28 Sep tracks the fee-switch proposal (27 Aug), the vote (27 Aug–2 Sep) and the September supply recovery (medium confidence on causality).
- The next 6 months carry heavy unlock overhang for the sub-sector:
  - FF: about 36% of circulating, about $133M.
  - ENA: about 12%, about $333M.
  - CHIP: a cliff of about 139% in April 2027.
  - SLX: about 42%.
  - YB: about 61%.
- Supply pressure is therefore a headwind independent of fundamentals (high confidence on the schedule; medium confidence on price impact).

### Gaps
- Exact listing (first-minute) prices and listing FDVs for ENA, FF, RESOLV and YB fall outside CG's 365-day free window and could not be checked without search. The FF community-sale price (reportedly a Buidlpad sale) was not verified.
- Airdrop sizes (as % of supply and $ value at TGE) for FF, RESOLV, UP and CAP, and claim rates for all tokens, were not found.
- UP's cliff size (team/investor %, first cliff about 13 Mar 2027) was not captured. MEGA and MEZO have no DL emissions datasets.
- Mezo's –97% collapse and SLX's –86% fall in July 2026 have no news context in this session.

---

## 2. Stablecoin supply/TVL in 2026, yields vs funding, and redemption/depeg episodes

### Takeaway
The crypto-native synthetic and yield-dollar basket shrank by about a third in 2026, while USDT and USDC were roughly flat and Sky's USDS grew.
- USDe fell –26% YTD to $4.66B, –69% from its October 2025 ATH.
- USDf –16% (but +42% in October 2026 alone); USR –99.9% after an exploit; NUSD –86%; cUSD –76%; USDai –60%; USDH –90%.
- sUSDe yield sat near 3.5–4% from February to July 2026 because Ethena had rotated backing out of basis trades into stables and lending. It recovered to about 5% only when funding normalised in Q3 and basis positions were rebuilt to 17% of backing.

### Cited Findings

**Supply table (DL stablecoin charts; USD millions)**

| Stablecoin | 1 Jan 2026 | 2026 peak (date) | Latest 21 Oct 2026 | Notes / ATH | Source |
|---|---|---|---|---|---|
| USDe (Ethena) | 6,294.4 | 6,591.2 (26 Jan) | 4,667.2 | ATH 14,826.5 on 4 Oct 2025; 2026 min 3,750.1 (28 Apr); 1 Oct 2026 4,864 | [DL 146](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=146) |
| USDtb (Ethena, BUIDL-backed) | 842.8 | 1,131.6 (26 May) | 517.5 | 2026 min 333.6 (22 Aug); ATH 1,841.3 (5 Nov 2025) | [DL 221](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=221) |
| USDf (Falcon) | 2,050.5 | 2,056.4 (26 Jan) | 1,717.9 | 2026 min 1,172.7 (12 Aug); 1 Oct 2026 1,209 → +42% in Oct; ATH 2,148.6 (15 Oct 2025); DL price $0.9946 | [DL 246](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=246) |
| USR (Resolv) | 300.7 | 406.7 (30 Jan) | 0.45 | 1 Feb 403 → 1 Mar 111 → 1 Apr 22; DL price $0.0733 | [DL 197](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=197) |
| NUSD (Neutrl) | 210.6 | 231.3 (16 Feb) | 30.3 | launched 4 Oct 2025 | [DL 346](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=346) |
| USDu (Unitas) | 27.2 | 106.0 (19 Apr) | 53.3 | | [DL 283](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=283) |
| USX (Solstice) | 305.8 | 523.0 (24 Jul) | 209.3 | 1 Aug 517 → 1 Sep 250 | [DL 310](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=310) |
| avUSD (Avant) | 100.9 | 134.3 (29 Aug) | 120.0 | | [DL 271](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=271) |
| hyUSD (Hylo) | 35.2 | 39.2 (22 Jan) | 24.9 | 2026 min 10.5 (26 Jun) | [DL 302](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=302) |
| YU (Yala) | 13.2 | 29.2 (3 Jun) | 22.7 | ATH 153.5 (23 Sep 2025); fell to 12.8 by 1 Dec 2025 | [DL 268](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=268) |
| MUSD (Mezo) | 20.8 | 31.5 (17 Jul) | 29.2 | DL price $0.990 | [DL 303](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=303) |
| lvlUSD (Level) | 1.3 | 1.3 | 0.4 | ATH 185.0 (23 May 2025); already 6.9 by 1 Oct 2025 | [DL 229](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=229) |
| deUSD (Elixir) | ~0 (DL series glitchy) | — | 0 | 114.3 on 10 Oct 2025 → ~0.1 by 1 Dec 2025; DL price 1e-8 | [DL 210](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=210) |
| USDX (Stables Labs, delta-neutral) | 36.3 | — | 10.9 (stale since 20 May 2026) | 683.4 on 5 Nov 2025 → 36.3 on 13 Nov 2025 | [DL 214](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=214) |
| USDF (Aster) | 172.2 | 177.0 (23 Jan) | 111.3 | ATH 370.8 (1 Oct 2025) | [DL 219](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=219) |
| DUSD (StandX) | 153.8 | 165.1 (22 Jan) | 24.6 | | [DL 252](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=252) |
| YUSD (Aegis) | 43.7 | 43.7 | 34.4 | | [DL 255](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=255) |
| USN (Noon) | 22.4 | 39.1 (28 Aug) | 36.6 | | [DL 230](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=230) |
| USDai (USD.AI) | 653.5 | 663.3 (18 Jan) | 261.8 | 2026 min 153.5 (21 Jul) | [DL 309](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=309) |
| cUSD (Cap) | 348.6 | 443.2 (28 Jan) | 82.8 | 2026 min 61.0 (16 Jul) | [DL 296](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=296) |
| iUSD (infiniFi) | 178.7 | 190.6 (7 Jan) | 68.3 | | [DL 298](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=298) |
| USDH (DL "USDH Stablecoin", likely Native Markets) | 62.9 | 106.4 (8 May) | 6.5 | first data 18 Nov 2025 | [DL 321](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=321) |
| feUSD (Felix) | 19.7 | 19.7 | 9.4 | ATH 82.3 (14 Jul 2025) | [DL 251](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=251) |
| USDm / MegaUSD (Ethena white-label) | — (launched 28 Jan) | 578.1 (6 May) | 16.1 | | [DL 342](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=342) |
| JupUSD (Ethena white-label) | — (launched 5 Jan) | 82.7 (29 Mar) | 42.9 | | [DL 335](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=335) |
| suiUSDe (Ethena white-label) | — (launched 29 Apr) | 13.9 (13 May) | 12.4 | | [DL 376](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=376) |
| USDS (Sky; benchmark) | 5,856.6 | 8,949.7 (1 Apr) | 6,718.3 | | [DL 209](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=209) |
| USDT / USDC (benchmarks) | 187,038.9 / 75,302.0 | 190,240.5 (20 May) / 79,620.2 (18 Mar) | 182,720.5 / 72,212.3 | | [DL 1](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=1), [DL 2](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=2) |

- Total USD-pegged stablecoin supply tracked by DL was about $304.9B on 21 Oct 2026. — [DL stablecoins](https://stablecoins.llama.fi/stablecoins?includePrices=true)

**New synthetic / yield-dollar launches in 2026 (DL first data point → latest, $M)**
- apxUSD (Apyx, "Dividend-Backed Dollar" backed by Strategy's STRC preferred)
  - Supply: launched 26 Feb 2026, peaked at 524.5 on 31 May, now 288.4. DL price $0.9886, i.e. below peg. — [DL 354](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=354)
  - Design: backed by "variable rate perpetual preferred stock such as STRC". — [CG coin APYX](https://api.coingecko.com/api/v3/coins/apyx?tickers=true)
- USDat (Saturn)
  - USDat is backed by tokenized treasuries; sUSDat by "digital credit" (BTC-treasury company securities). — [DL protocol: saturn](https://api.llama.fi/protocol/saturn)
  - Supply: from 25 Jun 2026, peaked at 114.9 on 28 Jul, now 105.8. — [DL 400](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=400)
- trUSD (Tori, delta-neutral): from 29 Jun 2026, now 71.9. — [DL 401](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=401)
- USDx (Axis, cross-venue arbitrage): from 16 Sep 2026, now 67.3. — [DL 442](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=442)
- yzUSD (Yuzu): from 4 Feb 2026, peaked at 70.9, now 58.9. — [DL 344](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=344)
- U (United Stables)
  - Supply: from 9 Jan 2026 (409), at a new high of 1,585.7 on 21 Oct 2026. DL labels it crypto-backed; its yield and synthetic nature are unverified. — [DL 336](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=336)
  - Venues include Binance and Aster. — [CG coin U](https://api.coingecko.com/api/v3/coins/united-stables?tickers=true)

**Ethena primary detail (governance reports)**
- **Jan–Feb 2026**
  - USDe was $6.07B at end-February. sUSDe was 3.528B, a staking ratio of 57.96% (55.25% at end-December). sUSDe APY was 3.59% vs Aave USDC 2.54%.
  - Liquid stables rose from 64.5% of backing (start of year) to 75.1%. Basis positions were $935M BTC and $454M ETH; venues were about 64% Binance and 19% OKX, then Deribit and Bybit.
  - The report blamed "general deterioration in market conditions, which compresses basis trade profitability". — [Ethena Jan–Feb 2026 update](https://gov.ethenafoundation.com/t/ethena-s-january-and-february-2026-governance-update/753)
- **Mar–Apr 2026**
  - Supply fell from $5.92B to $3.90B. The sUSDe cooldown became dynamic (1/3/5/7 days) and was set to 1 day.
  - Ethena signed its first direct institutional lending agreements (Anchorage Digital, Maple Institutional, Coinbase Asset Management).
  - White-label supply rose above $600M, about 4× from $150M+ in early March.
  - The protocol ran through the late-April rsETH incident "without disruption … no peg break and no draw on the Reserve Fund". It paused the LayerZero OFT bridge and joined the "DeFi United" recovery coalition.
  - Annualized run-rate was "$234M by month-end". — [Ethena Mar–Apr 2026 update](https://gov.ethenafoundation.com/t/ethena-s-march-and-april-2026-governance-update/791)
- **Dynamic cooldown rationale**: "perpetual futures make up just 11% of the backing of USDe, with 89% in liquid stablecoins", compared with 93% perps at the start of 2025. — [Dynamic cooldown proposal](https://gov.ethenafoundation.com/t/proposal-adopt-a-dynamic-cooldown-period-for-susde-unstaking/759)
- **May 2026**
  - Supply recovered from $3.90B to $4.51B. Liquid cash was 89% of backing and BTC/ETH basis $391M (9%).
  - "Protocol yield is primarily driven by DeFi lending rates and perpetual funding rates playing a secondary role."
  - Ethena markets on Kamino and Jupiter Lend passed $1B within days. White-label supply fell from about $560M to about $300M (USDm "moderation"). — [Ethena May 2026 update](https://gov.ethenafoundation.com/t/ethenas-may-2026-governance-update/796)
- **June 2026**
  - Supply was about $4.46B. Backing composition:

    | Bucket | Value | Share | APY |
    |---|---|---|---|
    | DeFi lending | ~$2B | 46% | 3.1% |
    | Liquid stables | ~$2B | 35% | 3.8% |
    | RWA (JAAA/STAC CLOs) | $501M | 11.2% | 5% |
    | Institutional lending | $310M | 6.9% | 4–7% |
    | Crypto basis | $39M | 1.0% | –0.1% |

  - sUSDe month-end APY was 3.84% (30-day average 3.6%).
  - Coinbase became Ethena's primary custodian, wallet and perps venue (more than $5B of assets).
  - Janus Henderson partnership: an ENA investment, CLO reserve integration and a USDe allocation.
  - USDtb supply was about $889M. — [Ethena June 2026 update](https://gov.ethenafoundation.com/t/ethena-s-june-2026-governance-update/808)
- **Q3 2026**
  - Supply went from $4.51B (1 Jul) to a low of $3.90B (end-July), then peaked at $5.00B (27 Sep) and ended the quarter at $4.94B. The July redemption wave included $164M on 9 Jul and $235M on 10 Jul and coincided with the USDm unwind (8–11 Jul).
  - Yield: sUSDe 7-day APY rose from 3.8% to 5.0% and the 30-day from 3.9% to 4.8%. Annualized fees went from 4.5% to 5.3% of supply.
  - Staking ratio fell from 38% to 26%, and was 25.45% (1.212B staked) on 12 Oct. sUSDe ended 1.5pp above Sky USDS. Basis positions grew from negligible to $0.84B (17% of backing).
  - Reserve Fund was $62.57M; backing ratio 101.43%.
  - White-label total (jupUSD, USDm, suiUSDe) fell from $284M to $66M. — [Ethena Q3 2026 update](https://gov.ethenafoundation.com/t/ethena-s-july-september-2026-governance-update/857)
- **Ethena API (14 Oct 2026)**: 30-day sUSDe yield 4.74%, 90-day 4.53%, average since inception 10.34%. — [Ethena yields API](https://ethena.fi/api/yields/protocol-and-staking-yield)

**Yield history (DL yields; monthly average APY)**

| Vault | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct |
|---|---|---|---|---|---|---|---|---|---|---|
| sUSDe | 4.76 | 3.75 | 3.49 | 4.19 | 3.80 | 3.86 | 3.98 | 4.33 | 4.83 | 4.95 |
| sUSDS | 4.00 | 4.00 | 3.81 | 3.72 | 3.64 | 3.60 | 3.58 | 3.52 | 3.59 | 3.74 |
| sUSDf | 7.09 | 6.44 | 6.01 | 6.25 | 4.92 | 5.17 | 5.34 | 4.74 | 4.70 | 4.03 |

- sUSDe in H2 2025 for comparison: Jul 6.38%, Aug 7.61%, Sep 7.08%, Oct 4.23%, Nov 5.17%, Dec 4.41%. sUSDe TVL went from $6.02B (end-Sep 2025) to $3.75B (end-Jan 2026) to $1.19B (Oct 2026). — [DL yields sUSDe](https://yields.llama.fi/chart/66985a81-9c51-46ca-9977-42b4fe7bc6df); [DL yields sUSDS](https://yields.llama.fi/chart/d8c4eff5-c8a9-46fc-a888-057c4c668e72)
- sUSDf: DL's tracked pool TVL is only $54M, which looks like partial coverage. — [DL yields sUSDf](https://yields.llama.fi/chart/0f67a08c-3f24-4a4b-963e-541f5a5c0364)
- Other current yields (spot / 30-day average, DL pools, 21 Oct 2026):

  | Vault | APY (spot / 30d) | TVL | Note |
  |---|---|---|---|
  | savUSD (Avant) | 7.9% / 7.7% | $100M | |
  | sUSDu (Unitas, BSC) | 11.6% | $37.5M | |
  | sUSDat (Saturn) | 12.8% | | monthly average 43.1% in June |
  | strUSD (Tori) | 9.0% / 10.5% | | |
  | sUSDx (Axis) | 15.5% / 19.5% | | |
  | stcUSD (Cap) | 4.9% / 5.9% | | |
  | sUSDai | 6.2% / 6.9% | $554M | TVL exceeds DL's USDai stablecoin count |
  | siUSD (infiniFi) | 6.4% | | |
  | sAID (GAIB) | 10.7% | | |
  | syzUSD (Yuzu) | 7.8% | | |
  | YUSD (Aegis) | 4.5% | | |
  | jrUSDe (Strata) | 6.9% | | |
  | srUSDe (Strata) | 3.8% | | |
  | sUSDS (Sky) | 3.8% | $4.83B on Ethereum | |

  — [DL yields pools](https://yields.llama.fi/pools)

**Perp funding (Hyperliquid API, monthly average annualized; share of negative hours in parentheses)**

| Month | BTC | ETH |
|---|---|---|
| Oct 2025 | 10.7% | 7.3% |
| Dec 2025 | 6.2% | 8.9% |
| Jan 2026 | 7.3% | 7.7% |
| Feb 2026 | 2.3% (32% neg) | 2.2% |
| Mar 2026 | 0.9% (40% neg) | 2.6% |
| Apr 2026 | –0.8% (47% neg) | –0.4% (42% neg) |
| May 2026 | 3.1% | 7.6% |
| Jun 2026 | 5.9% | 3.3% |
| Jul 2026 | 9.5% | 9.6% |
| Aug 2026 | 8.3% | 8.6% |
| Sep 2026 | 8.8% | 10.2% |
| Oct 2026 | 8.2% | 7.4% |

— [Hyperliquid info API (fundingHistory)](https://api.hyperliquid.xyz/info)

**Protocol TVL (DL protocol API, $M)**

| Protocol | 1 Jan 2026 | 2026 peak | Latest | Notes |
|---|---|---|---|---|
| [Falcon](https://api.llama.fi/protocol/falcon-finance) | 2,049 | | 1,718 | |
| [Resolv](https://api.llama.fi/protocol/resolv) | 446.8 | 590.4 (30 Jan) | 13.6 | 154 by 1 Mar |
| [Solstice](https://api.llama.fi/protocol/solstice) | 305.9 | 523.0 (17 Jul) | 209.3 | |
| [Cap](https://api.llama.fi/protocol/cap) | 381.7 | 483.8 (28 Jan) | 232.9 | |
| [USD AI](https://api.llama.fi/protocol/usd-ai) | 684.4 | | 263.2 | |
| [infiniFi](https://api.llama.fi/protocol/infinifi) | 178.5 | | 68.5 | |
| [Unitas](https://api.llama.fi/protocol/unitas) | 27.2 | | 57.3 | |
| [Avant avUSD](https://api.llama.fi/protocol/avant-avusd) | 100.8 | | 120.0 | |
| [Hylo](https://api.llama.fi/protocol/hylo) | 82.4 | 107.6 | 61.8 | |
| [Perena](https://api.llama.fi/protocol/perena) | 30.8 | | 13.4 | |
| [Saturn](https://api.llama.fi/protocol/saturn) | — | 214.1 (9 Jun) | 159.5 | launched 9 Apr 2026 |

### Inferences
- In H1 2026 sUSDe stopped being a funding-rate product and became a "T-bill + DeFi lending + institutional credit" product (high confidence).
  - That is why sUSDe yield only slightly beat sUSDS, and was sometimes below it in February and March.
  - It explains part of the 74% sUSDe staking-ratio and TVL compression, from about 58% to about 25% staked.
  - When funding rebounded to 8–10% annualized on Hyperliquid in July–September, Ethena re-levered the basis to 17% of backing and the spread to sUSDS widened to about 1.2–1.5pp.
- Caveat on the funding series: Hyperliquid funding includes a baseline interest component, so its levels read higher than CEX funding. The direction of travel, not the level, is the useful signal (medium confidence; the formula was not re-verified this session).
- Rough basket estimate (medium confidence; own arithmetic from the DL series above):
  - Crypto-native synthetic and yield dollars (USDe, USDf, USR, NUSD, USDu, USX, hyUSD, avUSD, YU, lvlUSD, deUSD, USDai, cUSD, iUSD, USDF, USN, YUSD, DUSD, USDX) went from about $10.95B on 1 Jan 2026 to about $7.48B on 21 Oct 2026, roughly –$3.5B or –32%.
  - New 2026 entrants (apxUSD, USDat, trUSD, Axis USDx, yzUSD and Ethena white-labels) add only about $0.66B today.
  - USDT moved –2.3% YTD, USDC –4.1% and USDS +14.7% over the same period.
- USDe moved in redemption waves tied to external shocks: rsETH in April and the USDm/MegaETH unwind in July. These were not depegs, and the peg held through roughly $2B of April outflows (high confidence, per Ethena's own reports).
- Several 2026 dollars trade below peg on DL pricing (21 Oct): apxUSD $0.9886, USDf $0.9946 and MUSD $0.990. pmUSD ($0.554), Main Street msUSD ($0.508), Metronome msUSD ($0.885) and cdxUSD ($0.198) are effectively broken. Small-cap synthetic dollars carry real depeg tail risk (medium confidence; DL prices for small caps can be stale).

### Gaps
- The cause of USR's $403M → $111M outflow in February 2026, before the exploit, was not found.
- The cause of USDf's 2026 decline, and of its +$510M October rebound, was not found.
- The cause of NUSD's –87% decline (beyond the 18 Mar 2026 DNS hijack) is unknown; Neutrl's docs site returned errors.
- The cause of USDH's collapse (about $106M → $6.5M) is unknown, and DL ID 321 is only "likely" Native Markets' USDH.
- Level's wind-down timing and reason were not documented this session (lvlUSD was already about $1M by January 2026).
- No CEX funding series (Binance/OKX/Bybit) were pulled; Hyperliquid was the only funding source.

---

## 3. Valuation ratios: MC/FDV vs supply and revenue; revenue-sharing and buybacks

### Takeaway
On supply-based multiples, ENA trades at about 0.6× MC/USDe and FF at about 0.21× MC/USDf (0.64× FDV). Sky trades at about 0.16× MC/(USDS+DAI) and about 9× revenue; ENA is at about 11–14× gross fees.
- ENA's premium rests on an approved but not yet active buyback. It switches on only at a 14-day average USDe supply of $7.5B, about 60% above today's level.
- Small 2026 tokens are cheap on supply (SLX about 0.06× MC/USX) but expensive on FDV and fees (CAP about 117× FDV/fees). Unlocks dominate their valuation.

### Cited Findings
- **ENA fee switch**
  - Proposal posted 27 Aug 2026; Snapshot "ENA Fee Switch" ran 27 Aug–2 Sep 2026 and closed with 17,786,102 For, 0 Against, 0 Abstain. — [Snapshot](https://snapshot.box/#/s:ethenagovernance.eth/proposal/0xcb6b9ed95bf0c64b6101ff7d3a770af86e07701d8419b541cf91a6894022f2a3)
  - The buyback share rises with each USDe-supply milestone, "set intentionally to support aggressive growth back to the heights of 2025 at ~$15b of USDe supply".
  - Once the first milestone is hit, "95% of the net revenue" paid to the Ethena Foundation from USDe savings, white-label stablecoins and "Ethena [X]" goes to ENA buybacks. The long-term goal is ">$100b in the next 5 years". — [Forum: ENA Fee Switch Activation](https://gov.ethenafoundation.com/t/ena-fee-switch-activation/830)
  - Buybacks start "at $7.5B of USDe supply". — [Ethena Q3 2026 update](https://gov.ethenafoundation.com/t/ethena-s-july-september-2026-governance-update/857)
- **History of the fee-switch criteria**
  - The November 2024 governance criteria were: USDe supply >$6B; cumulative revenue >$250M; listing on 4 of the 5 largest derivatives exchanges; and an sUSDe APY advantage of "5 to 7.5%" vs sUSDS.
  - The Foundation said the criteria were met on 15 Sep 2025, but the switch was not implemented.
  - OAK Research argued that buybacks "today would be a mistake" and that capture "would mechanically reduce yield". — [OAK Research forum post (16 Mar 2026)](https://gov.ethenafoundation.com/t/ethena-fee-switch-models-and-oak-researchs-recommendations/770)
- **ENA treasury vehicle**: StablecoinX ("a stablecoin infrastructure company and major ENA holder") "began trading on Nasdaq under the ticker 'USDE'" in June 2026. — [Ethena June 2026 update](https://gov.ethenafoundation.com/t/ethena-s-june-2026-governance-update/808)
- **Other ENA demand events**: Grayscale added ENA to its DeFi Fund at a 13.59% weight (7 May 2026), and ENA launched on Solana via Sunrise (14 May). — [Ethena May 2026 update](https://gov.ethenafoundation.com/t/ethenas-may-2026-governance-update/796)
- **Ethena fees**
  - DL "Ethena USDe" fees: 30 days $16.70M (about $203M annualized); trailing year $245.0M.
  - DL's "revenue" line is near zero ($0.05M over 30 days; $2.0M over the year), so DL books almost all of it as supply-side.
  - Comparators: Sky Lending revenue $197.6M over the year (fees $388.9M). Morpho Blue fees $204.3M (no protocol revenue). Pendle V2 revenue $14.06M. Euler V2 fees $41.1M (revenue $2.2M). USD AI fees $26.6M (revenue $7.46M). Avant avUSD fees $9.5M. Unitas fees $3.06M over the year, but $5.6M annualized from the last 30 days. Hylo fees about $5.7M annualized. Yield Basis revenue $3.90M over the year. — [DL fees](https://api.llama.fi/overview/fees?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType=dailyFees); [DL revenue](https://api.llama.fi/overview/fees?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType=dailyRevenue)
  - Ethena's own reporting: annualized run-rate of $234M at end-April 2026; fees of 5.3% of supply in September; staker share 27% (about $5.3–5.4M a month to sUSDe). — [Mar–Apr update](https://gov.ethenafoundation.com/t/ethena-s-march-and-april-2026-governance-update/791); [Q3 update](https://gov.ethenafoundation.com/t/ethena-s-july-september-2026-governance-update/857)
- **Falcon fees**: DL does not track Falcon fees or revenue (its revenue entry is zero and it has no fees entry). — [DL revenue](https://api.llama.fi/overview/fees?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType=dailyRevenue)
- **Ratios (own calculation from the CG MC/FDV and DL supply/fees cited above, 21 Oct 2026)**:
  - ENA:
    - MC/USDe = $2,792M / $4,667M = 0.60×.
    - FDV/USDe = 0.67×.
    - MC/(USDe+USDtb $5,185M) = 0.54×.
    - MC/trailing-year fees = 11.4×; MC/30-day annualized fees = 13.7×; FDV/30-day annualized fees = 15.4×.
    - With DL's documented unlocked supply (about $2.15B MC), MC/USDe is 0.46×.
  - FF: MC/USDf = $365M / $1,718M = 0.21×; FDV/USDf = 0.64×. No revenue multiple is possible.
  - SKY: MC/(USDS $6,718M + DAI $4,755M) = 0.16×; MC/revenue = $1,796M / $197.6M = 9.1×.
  - UP: MC/USDu = 0.56×; FDV/USDu = 2.6×; MC/annualized fees = 5.3×; FDV/annualized fees = 25×.
  - SLX: MC/USX = 0.06×; FDV/USX = 0.24×.
  - CAP: MC/cUSD = 1.28× (0.46× vs Cap TVL $233M); FDV/cUSD = 8.2×; FDV/annualized fees ($5.8M) ≈ 117×.
  - CHIP: MC/USDai = 0.35×; FDV/USDai = 1.75×; MC/trailing-year revenue = 12.3×; FDV/trailing-year revenue = 61×.
  - PENDLE: MC/TVL = 0.34×; MC/revenue ≈ 27×.
  - MORPHO: MC/TVL = 0.15×; MC/fees ≈ 8.2×.
  - YB: MC/TVL = 0.14×.
  - RESOLV: not meaningful (USR $0.45M).
- **Buyback and value-accrual designs elsewhere**:
  - Cap: "discretionary buybacks" funded from revenue. — [Cap docs](https://docs.cap.app/overview/tokenomics)
  - Falcon: FF/sFF gives boosted USDf APY, lower overcollateralization and fee discounts; the docs mention no buyback. — [Falcon docs: FF Token](https://docs.falcon.finance/ff-token)
  - Unitas: UP "does not represent … any claim on protocol revenue". — [Unitas docs](https://docs.unitas.so/overview/up/tokenomics)
  - Yala: lists "future buybacks funded by platform revenue". — [Yala docs](https://docs.yala.org/prediction-market-intelligence/yala-tokenomics)

### Inferences
- ENA's multiple prices a meaningful probability of a return to $7.5B or more in USDe supply (medium confidence). Today ENA receives no buyback cash flow.
- Gross fees of 5.3% on about $4.9B give roughly $250–260M a year. With only about 27% going to stakers, the Foundation-side "net revenue" (fees minus staker share, white-label economics and costs) is plausibly large. If and when buybacks start, 95% of it would be directed to ENA. The magnitude of net revenue is not disclosed, so treat this as a low-to-medium-confidence estimate.
- FF's 0.21× MC/supply looks cheap against ENA's 0.60×, but there are no audited revenue disclosures and about 36% of circulating supply unlocks within 6 months (medium confidence).
- Comparing yield venues and issuers: Sky (cash-flowing, about 9× revenue) and Morpho (distribution layer, growing TVL) were rewarded in 2026. Issuers with yield-dependent demand were not (medium-high confidence).

### Gaps
- Ethena's Foundation-level net revenue (the base for the 95% buyback) is not disclosed in the pages reviewed.
- The table of fee-switch milestones (buyback % by supply tier beyond $7.5B) is an image in the forum post and could not be read.
- No Token Terminal or Artemis revenue cross-check was possible.
- Falcon's revenue, insurance-fund size and any FF buyback were not found.

---

## 4. Pre-TGE pipeline: points design, committed TVL, funding, token status, TGE window, mercenary capital

### Takeaway
The Ethena-ecosystem pre-TGE projects have seen their deposits all but disappear:
- Ethereal Season Zero: from a $1.32B peak to $1.2M.
- Terminal pre-deposits: from $310M to $0.5M.
- Strata: from $326M to $33M.

None of the three has a priced token yet. The active 2026 points pipeline sits mostly in newer, higher-yield, smaller issuers, each with roughly $50–160M of supply: Avant (Season 1 airdrop preview live, TGE TBA), Apyx (Season 2 to 20 Dec 2026), Saturn (Season 2), Tori (Cores S1), Hylo (XP), Axis and Yuzu. Solstice shows the pattern: USX halved within about 6 weeks of its Season 2 ending.

### Cited Findings
- **Ethereal (Ethena perp DEX)**
  - Snapshot temp check (1–3 Oct 2024; 13.5M For): Ethereal proposed that "a 15% allocation of any potential Ethereal governance token" go to circulating ENA holders. — [Snapshot](https://snapshot.box/#/s:ethenagovernance.eth/proposal/0x10fbcb74e6419c32151470af542212a25762fe1f8cfc96481da6cd6afe7dd6e4)
  - Docs:
    - Ethereal is in "Mainnet Alpha phase as of October 20th" (the year is not stated; DL's first DEX TVL is from 24 Oct 2025). — [Ethereal docs](https://docs.ethereal.trade/introduction/ethereal-mainnet-rollout)
    - Weekly Ethereal Points; "Ethena Exchange Points … will convert into ENA at the end of the program"; USDe rewards capped at a 27.18% APR. — [Ethereal docs: rewards](https://docs.ethereal.trade/points/rewards-and-points)
  - TVL:
    - Season Zero pre-deposit: ATH $1,318.8M (8 Aug 2025) → $406.6M (1 Oct 2025) → $11.3M (1 Jan 2026) → $1.2M (21 Oct 2026). — [DL protocol: ethereal-season-zero](https://api.llama.fi/protocol/ethereal-season-zero)
    - DEX: $49.8M (1 Jan) → peak $74.9M (23 Jan) → $1.7M. — [DL protocol: ethereal-dex](https://api.llama.fi/protocol/ethereal-dex)
  - Token: no CG listing found, so it is pre-TGE.
- **Terminal Finance (Ethena-ecosystem spot DEX)**
  - Pre-deposits earned "Roots" points. TVL: ATH $310.3M (14 Sep 2025) → $175.4M (1 Oct 2025) → $14.1M (1 Jan 2026) → $0.5M. — [DL protocol: terminal-finance-pre-deposits](https://api.llama.fi/protocol/terminal-finance-pre-deposits)
- **Strata (USDe tranching)**
  - TVL: ATH $326.4M (8 Oct 2025) → $226.2M (1 Jan) → $276.9M (21 Mar) → $32.6M. Funding: $3M seed led by Maven 11 (16 Dec 2025). — [DL protocol: strata](https://api.llama.fi/protocol/strata)
  - Expanded beyond USDe to tranches on NUSD, Midas mHYPER/mM1-USD, Saturn USDat, Hastra PRIME and Plume nOPAL. — [Strata docs index](https://docs.strata.money/llms.txt)
  - Multi-season points program. — [Strata docs: points](https://docs.strata.markets/rewards/strata-points-program)
  - CG lists "STRATA" with no price (not trading or pre-TGE). — [CG markets](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=strata)
  - Yields: srUSDe 2.4–4.2% and jrUSDe 6–15% monthly averages since November 2025. — [DL yields jrUSDe](https://yields.llama.fi/chart/8352355c-5ad7-45c5-aca2-628de224f8d8)
- **Avant (avUSD; Avalanche)**
  - Season 1 points converted linearly into an AVANT allocation preview. "TGE timing: To be announced." — [Avant docs](https://docs.avantprotocol.com/avant-season-1-airdrop)
  - avUSD grew +19% YTD to $120M; trailing-year fees $9.5M. — [DL 271](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=271); [DL fees](https://api.llama.fi/overview/fees?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType=dailyFees)
  - CG lists AVANT with no price. — [CG markets](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=avant)
- **Apyx (apxUSD)**
  - "Pips" Season 1 ended 22 May 2026; Season 2 runs 23 May–20 Dec 2026. The US, EU and EEA are restricted. — [Apyx docs](https://docs.apyx.fi/apyx-overview/apyx-pips-points-program)
  - CG lists APYX (100M total supply) with no price. — [CG markets](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=apyx)
  - Funding: a round led by DeFi Dev Corp (26 Feb 2026). — [DL protocol: apyx-protocol](https://api.llama.fi/protocol/apyx-protocol)
- **Saturn (USDat/sUSDat)**
  - Points: Gravity (S1) and Orbital (S2). The highest multipliers go to Pendle YT and LP positions (for example 30–38× for yt-USDat) and to Curve and PancakeSwap LPs. — [Saturn docs](https://saturncredit.gitbook.io/saturn-docs/overview/allocations)
  - Funding: $0.8M (Jan 2026; YZi Labs, Sora), $2M seed (May 2026; Spartan, Anchorage, Susquehanna) and a strategic round with Ondo (Aug 2026). — [DL protocol: saturn](https://api.llama.fi/protocol/saturn)
- **Tori (trUSD)**: Cores Season 1 began 23 Jun 2026 with a pre-deposit phase (now complete). "Cores are not a promise of any token or payment." — [Tori docs](https://docs.tori.finance/resources/cores); a seed round led by Delphi Digital (24 Mar 2026) — [DL protocol: tori-finance](https://api.llama.fi/protocol/tori-finance)
- **Axis (USDx)**: $5M led by Galaxy Digital (3 Dec 2025; FalconX, OKX Ventures, Maven 11, GSR and others), plus a June 2026 round with Steakhouse Financial and Serotonin. — [DL protocol: axis](https://api.llama.fi/protocol/axis)
- **Hylo (hyUSD/xSOL)**
  - XP points: xSOL/xBTC earn 20 XP per $ per day vs 5 for hyUSD; referrals earn 10%. — [Hylo docs](https://docs.hylo.so/product-guide/xp-system)
  - Funding: $1.5M seed (Aug 2025, Robot Ventures) and a $1M strategic round (20 Oct 2026, Solana Ventures). No token yet. — [DL protocol: hylo](https://api.llama.fi/protocol/hylo)
- **Perena (USD*)**: TVL $30.8M → $13.4M. Pre-seed led by Borderless (with Binance Labs, Anagram, Maelstrom and others). No token found. — [DL protocol: perena](https://api.llama.fi/protocol/perena)
- **infiniFi (iUSD)**: a second $3M round led by Electric Capital (23 Sep 2026) while iUSD supply fell 62% YTD. — [DL protocol: infinifi](https://api.llama.fi/protocol/infinifi)
- **Makina**: exploited for $4.2M on 20 Jan 2026 ($3.41M returned). CG lists MAK with no price. — [DL hacks](https://api.llama.fi/hacks); [CG markets](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=makina)
- **Mercenary capital after seasons and TGEs**:
  - Solstice: Season 2 Flares closed 1 Aug 2026. SLX claims opened 10 Aug with 6-month vesting (which requires keeping TVL) or 9-month vesting. Season 3 runs 1 Aug–1 Dec 2026. — [Solstice S2 claims](https://docs.solstice.finance/solstice-for-users/flares/claims-and-vesting/season-2-claims-and-vesting); [Solstice S3](https://docs.solstice.finance/solstice-for-users/flares/season-3)
    - USX went from $517M on 1 Aug to $250M on 1 Sep 2026. — [DL 310](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=310)
  - Cap (TGE 26 Jun 2026): cUSD went from $443M (28 Jan) to $61M (16 Jul). — [DL 296](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=296)
  - USD.AI (TGE 21 Apr 2026): USDai went from $663M (18 Jan) to $153.5M (21 Jul). — [DL 309](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=309)
  - MegaETH (TGE 30 Apr 2026): USDm went from $578M (6 May) to $16M. — [DL 342](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=342)
    - MegaETH Bridge TVL is now $4.8M. — [DL protocols](https://api.llama.fi/protocols)
  - Counter-example, Unitas (TGE 13 Mar 2026): USDu went from $27M to $106M (19 Apr) and is $53M now. — [DL 283](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=283)

### Inferences
- The Ethereal 15%-to-ENA-holders promise and the conversion of "Ethena Exchange Points" into ENA are the main remaining Ethena-ecosystem airdrop catalysts. But Ethereal's TVL ($1.7M) suggests little organic usage (high confidence on TVL; low confidence on token timing, which has not been announced).
- Points programs in 2026 lean heavily on Pendle YT and LP multipliers (Saturn, Unitas tasks) and on "end-of-season multiplier settlement" with vesting tied to TVL (Solstice). These designs exist to slow post-season exits; the evidence suggests they only partly work (medium confidence).
- The likely next TGEs (speculative, low confidence; inferred from "token listed without price" or "allocation preview live"): Avant (AVANT), Apyx (APYX), Strata (STRATA) and possibly Makina (MAK). Saturn and Tori explicitly avoid promising tokens.

### Gaps
- TGE windows, airdrop pool sizes and fundraising valuations for Ethereal, Terminal, Strata, Avant, Apyx, Saturn, Tori, Axis, Hylo, Perena, Neutrl and Yuzu were not found. Most DL raise entries carry no valuation.
- Terminal Finance's status (launched, merged or abandoned) could not be checked; its docs host returned 502.
- Neutrl's token plans and current status are unknown; its docs returned 522.

---

## 5. Risk and contagion: 10 Oct 2025, Nov 2025 xUSD/deUSD, and 2026 incidents

### Takeaway
Three waves hit the sub-sector:
- **October–November 2025.** The USDe drawdown after 10 Oct (supply halved to about $7.2B by December), then the Stream xUSD loss ($93M) that sank Elixir deUSD and hit Euler and Reservoir. Stables Labs' USDX also collapsed.
- **March–April 2026.** The Resolv USR key-compromise exploit (80M unbacked USR minted, about $23–25M extracted), then the Kelp rsETH bridge exploit ($293M), which triggered roughly $2B of USDe redemptions without a depeg.
- **Summer 2026.** Smaller unwinds (the USDm/MegaETH unwind in July) and post-TGE TVL exits.

Lending venues that warehoused synthetic-dollar risk (Euler, –71% TVL YTD; EUL –60%) lost share to Morpho, whose TVL doubled.

### Cited Findings
- **The 10 Oct 2025 aftermath, as seen in supply data**: USDe hit its ATH of $14.83B on 4 Oct 2025, was $14.63B on 10 Oct and $7.17B on 1 Dec 2025. — [DL 146](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=146)
  - sUSDe monthly average APY fell from 7.08% (Sep 2025) to 4.23% (Oct 2025). — [DL yields sUSDe](https://yields.llama.fi/chart/66985a81-9c51-46ca-9977-42b4fe7bc6df)
- **November 2025**
  - Stream Finance "reported loss $93 million users fund" (4 Nov 2025). — [DL protocol: stream-finance](https://api.llama.fi/protocol/stream-finance)
  - Euler annotated "Stream finance rug" (4 Nov 2025). — [DL protocol: euler](https://api.llama.fi/protocol/euler)
  - Reservoir annotated "Stream finance XUSD depeg". — [DL protocol: reservoir-protocol](https://api.llama.fi/protocol/reservoir-protocol)
  - Balancer V2 was exploited for $128M the day before (3 Nov 2025). — [DL hacks](https://api.llama.fi/hacks)
  - deUSD went from $114.3M (10 Oct 2025) to about $0 (DL price 1e-8). — [DL 210](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=210)
  - Stables Labs USDX went from $683.4M (5 Nov 2025) to $36.3M (13 Nov 2025). — [DL 214](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=214)
  - Euler TVL went from an ATH of $2.20B (6 Oct 2025) to $1.006B (1 Jan 2026), a 2026 low of $252.8M (22 Apr) and $292.5M now. — [DL protocol: euler](https://api.llama.fi/protocol/euler)
- **Yala, September 2025**: a $7.64M deployer-key compromise (14 Sep 2025). — [DL hacks](https://api.llama.fi/hacks)
  - YU went from $125.4M (10 Oct 2025) to $12.8M (1 Dec 2025). — [DL 268](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=268)
- **Resolv USR exploit, 22 Mar 2026**
  - An attacker minted 80M unbacked USR and the price fell to as low as about $0.14. — [Cointelegraph](https://cointelegraph.com/news/resolv-labs-stablecoin-depegs-attacker-mints-millions-of-tokens)
  - About $23M was extracted using a compromised signing key. — [Chainalysis](https://www.chainalysis.com/blog/lessons-from-the-resolv-hack/)
  - DL records $24.5M, "Key Leaked via Infrastructure". — [DL hacks](https://api.llama.fi/hacks)
  - Euler, Venus, Lista and Fluid paused markets. — [Cointelegraph](https://cointelegraph.com/news/resolv-says-no-assets-lost-as-defi-partners-respond-to-usr-depeg)
  - Recovery terms:
    - Pre-incident USR/wstUSR: 1 USR : 1 USDC.
    - Post-incident USR: 1 USR : 0.5 USDC.
    - RLP is the junior tranche absorbing the impairment.
    - Claims ran 26 May → 26 Sep 2026 (extended) and require a release of claims. — [Resolv recovery overview](https://docs.resolv.xyz/litepaper/using-resolv/resolv-recovery-portal-overview); [Recovery guide](https://docs.resolv.xyz/litepaper/using-resolv/resolv-recovery-portal-overview/recovery-guide)
- **Other 2026 incidents relevant to stable-yield venues**:
  - Neutrl DNS hijack (18 Mar 2026).
  - Drift Trade $295M (1 Apr 2026).
  - Kelp rsETH $293M via cross-chain message spoofing (18 Apr 2026).
  - Term Finance vaults $8.5M via a malicious proposal (23 Aug 2026).
  - Bitget hot wallet $387M (24 Sep 2026).
  - Ledger supply-chain attack $93M (9 Oct 2026).
  — [DL hacks](https://api.llama.fi/hacks)
- **Ethena under the rsETH shock**:
  - Supply went from $5.9B to $3.90B by end-April, then "first meaningful supply recovery" in May. — [Ethena May 2026 update](https://gov.ethenafoundation.com/t/ethenas-may-2026-governance-update/796)
  - "No peg break … no draw on the Reserve Fund"; the LayerZero OFT bridge was paused. — [Mar–Apr update](https://gov.ethenafoundation.com/t/ethena-s-march-and-april-2026-governance-update/791)
- **Ethena's July 2026 redemption wave**: $164M on 9 Jul and $235M on 10 Jul. The mint/redeem contract never dropped below $80M of liquidity. USDe DEX liquidity fell from $68–74M to $49–52M. — [Ethena Q3 2026 update](https://gov.ethenafoundation.com/t/ethena-s-july-september-2026-governance-update/857)
- **Ethena Reserve Fund sizing**:
  - $62M against a recommended $5–7M in March 2026 (LlamaRisk/Blockworks Advisory). — [Reserve Fund March 2026](https://gov.ethenafoundation.com/t/reserve-fund-march-2026-update/775)
  - $62.57M against a recommended $45.7M in October 2026. — [Q3 update](https://gov.ethenafoundation.com/t/ethena-s-july-september-2026-governance-update/857)
- **Felix**: sunset its FLX HIP-3 DEX, which listed a USDE market, with settlement on Friday 19 June. The year is not stated; it is inferred as 2026 because 19 June 2026 falls on a Friday. — [Felix docs](https://usefelix.gitbook.io/docs/felix-perpetual-futures/getting-started/flx-hip-3-sunset-guide)

### Inferences
- The main contagion channel in 2025–26 was not delta-neutral hedge failure. It was operational and credit risk sitting inside "delta-neutral" wrappers: Stream's external manager, Resolv's signing key and Yala's deployer key, amplified through curated lending markets (high confidence).
- Ethena survived every shock as a redemption event rather than a solvency event. The trade-off is that its backing became mostly stables and credit, which erased the yield premium (high confidence).
- Risk repricing showed up as TVL migration from Euler to Morpho. Morpho went from $5.88B to $11.32B (+93% YTD), and USDe became "the largest dollar collateral asset on Morpho". — [DL protocol: morpho](https://api.llama.fi/protocol/morpho); [Ethena Q3 update](https://gov.ethenafoundation.com/t/ethena-s-july-september-2026-governance-update/857) (medium-high confidence).

### Gaps
- Primary detail on the 10 Oct 2025 Binance USDe price dislocation (the low print and Binance's compensation) was not re-verified this session.
- The Stream/xUSD final recovery, any lawsuits and Elixir's deUSD redemption terms were not found.
- The causes of the pmUSD, Main Street msUSD and cdxUSD depegs were not investigated.
- No source covers whether the Bitget hack touched any delta-neutral issuer's hedges.

---

## 6. Sentiment, and how much demand depends on Pendle loops and points

### Takeaway
The available primary commentary is cautious:
- Research firms on Ethena's risk committee describe "compressed crypto carry regimes" and diversify into gold, tokenized-equity basis trades and CLOs.
- OAK Research argued against buybacks that would cut yield.

The Pendle-loop and points demand that drove the 2025 USDe peak has largely gone. Pendle's sUSDe-related TVL went to "near zero" after the 13 Aug 2026 maturity, Pendle's total TVL is down 92% from its ATH, and Ethereal and Terminal pre-deposits are about 99% gone. Remaining USDe demand comes from CeFi distribution (Binance, Coinbase, Robinhood, Kraken) and lending-market collateral.

### Cited Findings
- **Pendle-related demand for USDe**
  - Pendle's Ethena-related TVL stabilized at about $230–240M after the 6 May 2026 sUSDe maturity. — [Ethena May 2026 update](https://gov.ethenafoundation.com/t/ethenas-may-2026-governance-update/796)
  - It "fell from $38M to near zero after the sUSDe 13 Aug 2026 maturity". USDe-related deposits on Aave, Morpho, Jupiter Lend and Kamino rose from $2.76B to $2.98B, with Morpho tripling from $0.29B to $0.87B. — [Ethena Q3 2026 update](https://gov.ethenafoundation.com/t/ethena-s-july-september-2026-governance-update/857)
- **Pendle and Boros TVL**
  - Pendle TVL: ATH $13.39B (19 Sep 2025) → $3.69B (1 Jan 2026) → 2026 low $928M (19 Jun) → $1.12B (21 Oct). — [DL protocol: pendle](https://api.llama.fi/protocol/pendle)
  - Boros (funding-rate trading): $6.9M → $12.3M (18 Apr) → $7.5M. — [DL protocol: boros](https://api.llama.fi/protocol/boros)
- **CeFi and retail distribution**:
  - Q3 2026: USDe on Robinhood Chain above $300M; the Coinbase DeFi earn product above $300M; Ethena Pay beta on Avalanche (48 countries). — [Ethena Q3 update](https://gov.ethenafoundation.com/t/ethena-s-july-september-2026-governance-update/857)
  - Kraken became "the first US exchange to support USDe rewards". — [Mar–Apr update](https://gov.ethenafoundation.com/t/ethena-s-march-and-april-2026-governance-update/791)
- **Risk-committee language**:
  - The tokenized gold proposal cites "near-zero funding correlation with crypto" and "compressed crypto carry regimes" (PAXG about 3.6%, XAUT about 5.1% funding). — [Mar–Apr update](https://gov.ethenafoundation.com/t/ethena-s-march-and-april-2026-governance-update/791)
  - Tokenized-equity basis framework: about $2.9B of one-sided OI across four venues. — [Kairos framework](https://gov.ethenafoundation.com/t/a-framework-for-the-tokenized-equity-basis-trade/832)
  - Ethena's January–February report: "broader market conditions having pushed all stablecoin yields down". — [Jan–Feb update](https://gov.ethenafoundation.com/t/ethena-s-january-and-february-2026-governance-update/753)
  - Proposals to add JAAA/STAC CLOs, RLUSD, USDG, GHO/sGHO and mUSD as USDe backing show a shift toward RWA and stablecoin carry. — [JAAA proposal](https://gov.ethenafoundation.com/t/proposal-jaaa-as-usde-backing-asset/797); [Gov forum index](https://gov.ethenafoundation.com/latest)
- **Analyst views**:
  - OAK Research: buybacks are risky because "when protocol revenues decline or sUSDS yield increases, buybacks can stop abruptly. An intermittent buyback may be more harmful to ENA than no buyback at all." — [OAK forum post](https://gov.ethenafoundation.com/t/ethena-fee-switch-models-and-oak-researchs-recommendations/770)
  - Ethena's own outlook is the bull case: grow USDe to more than $100B in 5 years. — [Fee switch post](https://gov.ethenafoundation.com/t/ena-fee-switch-activation/830)
- **Yield dispersion among new entrants**: sUSDx (Axis) 17.8% in October, sUSDat (Saturn) 43.1% in its June average, strUSD about 10%, sUSDu about 11.6%. Incumbents pay about 4–5% (sUSDe and sUSDf). — [DL yields pools](https://yields.llama.fi/pools); [DL yields sUSDat](https://yields.llama.fi/chart/47e72726-3b2b-4fe6-b4a9-a26e1fcd9a50)

### Inferences
- USDe demand in 2026 has largely decoupled from Pendle and points (high confidence for H2 2026). This makes it stickier but also more like sUSDS, so ENA's upside now depends on CeFi and fintech distribution and on funding regimes rather than on DeFi loop capacity.
- The "too many synthetic dollars" thesis is consistent with the data (medium-high confidence):
  - The basket shrank by about $3.5B YTD.
  - More than 10 new issuers launched with small supply ($50–300M) and sharply higher, riskier yields.
  - Token performance from the 2026 TGE cohort was poor.

  No research-house quote using that phrase was captured, however.
- Yield compression is structural for incumbents. With backing spread across stables, lending, credit and basis, the APY stays in a 3.5–5% band unless funding rises well above about 8–10% (medium confidence).

### Gaps
- No Messari, Delphi, Blockworks Research, Steakhouse, Chaos Labs or news-desk (The Block, CoinDesk, DL News) commentary on 2026 saturation or yield compression was retrieved, because web search was exhausted.
- Pendle's 2026 product and token changes (vePENDLE reform, Boros adoption) and Pendle's USDe share at the 2025 peak were not verified.

---

## 7. Implications for capital flows into the sub-sector and its remaining upside

### Takeaway
On balance, the evidence points to net capital outflow from synthetic and yield dollars in 2026, about –32% YTD for the basket, against roughly flat fiat stablecoins. Value has moved to distribution and credit layers (Morpho, Sky, Hyperliquid) rather than to issuers.

Remaining upside looks concentrated and conditional:
- (a) ENA, if USDe gets back above $7.5B and the 95% buyback switches on.
- (b) Selected low-FDV tokens with real revenue (CAP, UP), against heavy unlock calendars.
- (c) Funding-regime recoveries. The Q3 2026 rebound showed supply responds within weeks when funding is 8–10%.

### Cited Findings
- **Basket vs benchmarks (DL series from Section 2)**:
  - USDe –25.9% YTD and –68.5% from ATH; USDf –16.2%; USDtb –38.6%.
  - USDS +14.7%; USDT –2.3%; USDC –4.1%.
  — [DL 146](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=146); [DL 246](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=246); [DL 209](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=209); [DL 1](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=1)
- **Supply responds to funding**:
  - September 2026 "added over $700M of supply" as basis positions were rebuilt to $0.84B, with "sustained USDT and USDC mint flows". — [Ethena Q3 update](https://gov.ethenafoundation.com/t/ethena-s-july-september-2026-governance-update/857)
  - BTC funding on Hyperliquid averaged 8.3–9.5% annualized in July–September 2026, versus –0.8% to 2.3% in February–April. — [Hyperliquid API](https://api.hyperliquid.xyz/info)
- **The buyback trigger is distant**: $7.5B against 4.67B USDe on 21 Oct 2026, roughly +61% needed. — [Ethena Q3 update](https://gov.ethenafoundation.com/t/ethena-s-july-september-2026-governance-update/857); [DL 146](https://stablecoins.llama.fi/stablecoincharts/all?stablecoin=146)
- **Morpho**
  - TVL went from $5.88B to $11.32B, an ATH on 6 Oct 2026. — [DL protocol: morpho](https://api.llama.fi/protocol/morpho)
  - It raised $175M (9 Jun 2026; Paradigm, a16z crypto, Ribbit, with VanEck, Apollo and Circle Ventures). — [DL protocol: morpho](https://api.llama.fi/protocol/morpho)
  - MORPHO is up 118% YTD. — [CG](https://api.coingecko.com/api/v3/coins/morpho/market_chart?vs_currency=usd&days=365&interval=daily)
- **Institutional entry into Ethena**:
  - Janus Henderson strategic investment (9 Jun 2026). — [DL protocol: ethena](https://api.llama.fi/protocol/ethena)
  - Coinbase custody and perps partnership; StablecoinX listed on Nasdaq. — [Ethena June update](https://gov.ethenafoundation.com/t/ethena-s-june-2026-governance-update/808)
- **Supply overhang over the next 6 months**: ENA about 1.6B tokens; FF about 1.22B (36% of circulating); CHIP's April 2027 cliff (about 139%); SLX about 42%. — [DL emissions ENA](https://defillama-datasets.llama.fi/emissions/ethena); [DL emissions FF](https://defillama-datasets.llama.fi/emissions/falcon-finance); [DL emissions USD.AI](https://defillama-datasets.llama.fi/emissions/usd-ai); [DL emissions Solstice](https://defillama-datasets.llama.fi/emissions/solstice)

### Inferences
- **Capital flows.** Marginal stablecoin capital in 2026 prefers:
  - regulated or fiat stables and Sky (USDS +15%);
  - RWA-backed dollars, including Ethena's own pivot to CLOs and institutional credit;
  - CeFi-distributed yield.

  It does not favour new synthetic issuers (high confidence). Inflows into new synthetic dollars ($0.66B) are about a fifth of incumbents' outflows ($3.5B).
- **ENA asymmetry** (medium confidence):
  - Upside: a funding upcycle plus CeFi and fintech distribution could take USDe back toward $7.5B+, which would switch on 95% net-revenue buybacks. That is a reflexive catalyst the market partly priced in during the Sep 2026 run-up.
  - Downside: low-funding regimes push sUSDe toward parity with sUSDS. Combined with about 266M ENA a month of unlocks, that caps the rerating.
- **FF** (low-medium confidence): FF's relative YTD strength (+26%) meets its largest unlock phase from 29 Oct 2026 (about 6% of circulating per month). Without disclosed revenue or a buyback, supply risk is skewed to the downside.
- **2026 TGE cohort and pre-TGE pipeline** (medium-high confidence):
  - Expect continued "points → TVL → TGE → exit".
  - The best risk-adjusted entries were low-FDV listings with sticky distribution (CAP from a $110M ICO valuation; UP).
  - High-yield newcomers (Axis, Saturn, Tori, Apyx) carry credit, operational or equity-preferred risk that the 2025–26 failures (Stream, Resolv, Yala) show can wipe out tokens.
- **Sub-narrative status** (medium confidence): the "synthetic dollar" story is mature and saturated. Remaining upside lies with issuers that:
  - can show audited net revenue and genuine buybacks (Ethena once the trigger is met);
  - win distribution via exchanges, fintechs and chains through white-labels — though white-labels shrank from $600M+ to $66M in 2026;
  - offer diversified carry (equity and commodity basis, CLOs) without hidden credit risk.

### Gaps
- No consensus or sell-side forecasts for 2027 USDe supply or funding regimes were found.
- No data was gathered on who holds ENA or FF (funds vs treasury vehicles), and StablecoinX's ENA holdings in 2026 were not quantified.
- Total sub-sector token MC was not aggregated, and a consistent "synthetic dollar" basket definition across DL categories is lacking.
