# Comps: TGEs of major yield-bearing/synthetic stablecoin projects (Ethena, Usual, OpenEden, Falcon, Resolv, + Elixir, Level) — valuation dataset as of 2026-09-28

Method note (applies to all sections): Prices are daily closes (UTC) from the Gate.io public candlestick API ([Gate API](https://api.gateio.ws/api/v4/spot/candlesticks?currency_pair=ENA_USDT&interval=1d)), cross-checked against DefiLlama's coin price API ([DefiLlama coins](https://coins.llama.fi/prices/current/coingecko:ethena,coingecko:usual,coingecko:openeden,coingecko:falcon-finance-ff,coingecko:resolv)), CoinGecko ([CG usual](https://api.coingecko.com/api/v3/coins/usual), [CG resolv](https://api.coingecko.com/api/v3/coins/resolv)) and CoinPaprika ([Paprika FF](https://api.coinpaprika.com/v1/tickers/ff-falcon-finance)). CoinGecko's free API only serves the last 365 days, so older launch-window prices come from Gate + DefiLlama. Stablecoin supply comes from DefiLlama's stablecoins API (USDe id 146, USD0 195, USDO 241, USDf 246, USR 197, lvlUSD 229, deUSD 210: e.g. [DefiLlama USDe](https://stablecoins.llama.fi/stablecoin/146)). Protocol TVL comes from the DefiLlama protocol API ([resolv-usr](https://api.llama.fi/protocol/resolv-usr), [usual-usd0](https://api.llama.fi/protocol/usual-usd0), [ethena-usde](https://api.llama.fi/protocol/ethena-usde)). Pendle implied/underlying APY is from Pendle's API ([Pendle market history example](https://api-v2.pendle.finance/core/v2/1/markets/0xb4460e76d99ecad95030204d3c25fb33c4833997/historical-data?time_frame=week)). "FDV" = price × max/total supply as stated per token. Any figure labeled "calc" is my own arithmetic on these sourced inputs.

## Q1. FDV at TGE and FDV/TVL multiples, and how they have evolved

### Takeaway
Ethena was the outlier: it launched at a ~7x FDV/USDe-supply multiple (FDV about $11.6B on day-1 close against $1.56B USDe). Usual launched at about 4.8x. Every 2025 launch (Resolv, Falcon, OpenEden, Elixir) launched at only about 1–1.7x FDV/TVL. Since then every token has de-rated hard. Today ENA trades at about 0.8x FDV/USDe supply and FF at about 1.1x. USUAL, RESOLV, EDEN and ELX are down 85–99.7% from their TGE-day close, and three of the stablecoins (USR, deUSD, lvlUSD) have effectively collapsed or wound down.

### Cited Findings

**Master valuation table (calc from sourced prices/supplies; dates stated)**

| Project / token | TGE (spot) date | Max/total supply | TGE-day close (FDV) | Week-1 avg close (FDV) | Stablecoin supply / TVL at TGE | FDV/TVL at TGE (day-1 close) | Price 2026-09-28 (FDV) | Stablecoin supply 2026-09-27 | FDV/TVL now |
|---|---|---|---|---|---|---|---|---|---|
| Ethena ENA | 2024-04-02 | 15B | $0.773 ($11.6B) | $1.067 ($16.0B) | USDe $1.56B | ~7.4x (6.2x at $0.64 launch price) | $0.263 ($3.95B) | USDe $4.94B (+USDtb $0.54B) | ~0.80x (0.72x incl. USDtb) |
| Usual USUAL | 2024-12-18 (Binance pre-market from 2024-11-19) | 4B max at TGE (CG now shows 3B max, 1.958B total) | $1.04 ($4.16B on 4B) | $1.228 ($4.91B) | USD0 $875M (protocol TVL $881M) | ~4.8x | $0.0151 ($29M on total supply per CG, $45M on 3B max) | USD0 $547M (stablecoins API) vs protocol TVL $88M (conflict) | ~0.05–0.5x depending on denominator |
| Resolv RESOLV | 2025-06-10 | 1B | $0.351 ($351M) | $0.286 ($286M) | protocol TVL $351M; USR $220M | ~1.0x (TVL) / 1.6x (USR) | $0.0186 ($18.6M) | USR ~$6M (post-exploit) | not meaningful |
| Falcon FF | 2025-09-29 | 10B | $0.281 ($2.81B) | $0.2015 ($2.0B) | USDf $1.90B | ~1.5x | $0.130 ($1.30B) | USDf $1.21B | ~1.1x |
| OpenEden EDEN | 2025-09-30 | 1B | $0.3985 ($398M) | $0.372 ($372M) | USDO $235M (excludes TBILL, not captured) | ~1.7x (USDO only) | $0.0589 ($59M) | USDO $15M | ~3.9x (USDO only; misleading) |
| Elixir ELX | 2025-03-07 | 1B | $0.389 ($389M) | $0.478 ($478M) | deUSD ~$300M | ~1.3x | $0.0012 ($1.2M) | deUSD dead (shut down Nov 2025) | n/a |
| Level (lvlUSD) | No token launched (see Gaps) | – | – | – | lvlUSD peak $185M (2025-05-23) | – | – | ~$0.4M | – |

Sources for the table:
- Launch-day and subsequent daily OHLC are from the Gate API ([Gate ENA](https://api.gateio.ws/api/v4/spot/candlesticks?currency_pair=ENA_USDT&interval=1d), [Gate USUAL](https://api.gateio.ws/api/v4/spot/candlesticks?currency_pair=USUAL_USDT&interval=1d), [Gate RESOLV](https://api.gateio.ws/api/v4/spot/candlesticks?currency_pair=RESOLV_USDT&interval=1d), [Gate FF](https://api.gateio.ws/api/v4/spot/candlesticks?currency_pair=FF_USDT&interval=1d), [Gate EDEN](https://api.gateio.ws/api/v4/spot/candlesticks?currency_pair=EDEN_USDT&interval=1d), [Gate ELX](https://api.gateio.ws/api/v4/spot/candlesticks?currency_pair=ELX_USDT&interval=1d)). DefiLlama's first daily prints match closely: ENA $0.781 (2024-04-03 00:01), RESOLV $0.3505, FF $0.284, EDEN $0.402, ELX $0.385 ([DefiLlama chart API](https://coins.llama.fi/chart/coingecko:ethena?start=1711584000&span=500&period=1d)). OKX RESOLV candles also agree: 2025-06-10 close $0.3514 ([OKX RESOLV](https://www.okx.com/api/v5/market/history-candles?instId=RESOLV-USDT&bar=1Dutc)).
- Stablecoin supplies at TGE: USDe $1,560M on 2024-04-02; USD0 $875M on 2024-12-18 ($364M on 2024-11-18); USR $220M on 2025-06-10; USDf $1,899M on 2025-09-29; USDO $235M on 2025-09-30; deUSD $302M on 2025-03-08 ([DefiLlama stablecoins](https://stablecoins.llama.fi/stablecoins?includePrices=false), [USDe](https://stablecoins.llama.fi/stablecoin/146), [USD0](https://stablecoins.llama.fi/stablecoin/195), [USR](https://stablecoins.llama.fi/stablecoin/197), [USDf](https://stablecoins.llama.fi/stablecoin/246), [USDO](https://stablecoins.llama.fi/stablecoin/241), [deUSD](https://stablecoins.llama.fi/stablecoin/210)).
- Protocol TVL at TGE was $1,559M for Ethena USDe (2024-04-02), $368M for Usual USD0 (2024-11-18) and $351M for Resolv USR (2025-06-10) ([DefiLlama ethena-usde](https://api.llama.fi/protocol/ethena-usde), [usual-usd0](https://api.llama.fi/protocol/usual-usd0), [resolv-usr](https://api.llama.fi/protocol/resolv-usr)). Current protocol TVLs are Ethena USDe $4,939M, Falcon $1,208M, Usual USD0 $88M and Resolv USR $6.3M ([DefiLlama protocols](https://api.llama.fi/protocols)).
- ENA listing facts: The Defiant reported that ENA "launched at $1 billion market cap" at a $0.64 price with FDV "over $10 billion" ([The Defiant](https://thedefiant.io/news/defi/ethena-labs-ena-launches-at-usd1-billion-post-airdrop-as-sats-campaign-kicks-off)). Initial circulating supply was 1.425B ENA (9.5%), and Binance listed it at 08:00 GMT on 2024-04-02 ([CoinJournal](https://coinjournal.net/news/binance-adds-ethena-ena-as-50th-launchpool-project/), [Coinspeaker](https://www.coinspeaker.com/binance-ethena-ena-50th-launchpool/)).
- USUAL timing: Launchpool farming ran Nov 15–18, 2024 and Binance Pre-Market opened USUAL/USDT on Nov 19, 2024 at 10:00 UTC ([Coinspeaker](https://www.coinspeaker.com/binance-introduces-usual-launchpool-pre-market-trading-soon/), [CoinChapter/Binance Square](https://www.binance.com/en/square/post/16286917390690)). Usual's blog gives spot trading as December 18, 2024 11:00 UTC, with ~494.6M USUAL circulating at listing and a max supply of "4B USUAL in 4 years" ([Usual blog](https://usual.money/blog/airdrop-the-genesis-of-ownership)). In the pre-market window Gate showed USUAL closing at $0.528 on 2024-11-18 (FDV about $2.1B on 4B) and falling as low as $0.221 before spot TGE ([Gate USUAL](https://api.gateio.ws/api/v4/spot/candlesticks?currency_pair=USUAL_USDT&interval=1d)).
- USUAL current supply: CoinGecko shows total supply 1.958B, max supply 3.0B, circulating 1.937B and FDV $29.4M on 2026-09-28 ([CoinGecko API usual](https://api.coingecko.com/api/v3/coins/usual)). The drop of max supply from 4B to 3B is presumably a governance change; I have not verified this.
- FF: circulating supply at listing was 2.34B (23.4%) and total supply is 10B ([Falcon launch post](https://falcon.finance/news/falcon-finance-enters-its-next-chapter-with-the-launch-of-ff-token), [CryptoNewsZ](https://www.cryptonewsz.com/binance-falcon-finance-as-49th-hodler-airdrop/)). The Buidlpad community sale was priced at a $350M FDV and drew over $112M of commitments against a $4M target ([Gate Learn/TipRanks via search](https://www.tipranks.com/news/newswire/falcon-finance-announced-ff-and-community-sale-on-buidlpad), [MEXC news](https://www.mexc.com/news/107631)). FF "debut[ed] at $0.67" and crashed 75% to $0.19 within a day ([CCN](https://www.ccn.com/analysis/crypto/falcon-finance-ff-price-crashes-token-debut-what-lies-ahead/)). CoinPaprika's ATH is $0.797 at 2025-09-29 13:18 UTC ([CoinPaprika](https://api.coinpaprika.com/v1/tickers/ff-falcon-finance)). Tokenomist on 2026-09-28 shows circulating supply of 3.14B (31.4%) and an FDV of $1.31B ([Tokenomist FF](https://tokenomist.ai/falcon-finance-ff)).
- EDEN: 1B supply, TGE on 2025-09-30 with trading from 11:00 UTC ([CryptoNinjas](https://www.cryptoninjas.net/news/binance-airdrops-15m-eden-tokens-as-openeden-debuts-with-1b-supply/), [Bitget Academy](https://web3.bitget.com/en/academy/openeden-airdrop-guide-how-to-participate-and-claim-eden-rewards)). The intraday ATH was $1.526 at 2025-09-30 09:15 UTC per CoinPaprika and $1.112 on Gate, against a day-1 close of $0.3985 ([CoinPaprika EDEN](https://api.coinpaprika.com/v1/tickers/eden-openeden)). Tokenomist now shows circulating supply of 425.2M, market cap $26.6M and FDV $59.5M ([Tokenomist EDEN](https://tokenomist.ai/openeden)).
- RESOLV: CoinGecko now shows circulating supply 483.1M, market cap $8.98M, FDV $18.6M, ATH $0.4085 (2025-06-11) and ATL $0.0142 (2026-06-20) ([CoinGecko API resolv](https://api.coingecko.com/api/v3/coins/resolv)).
- ELX trading began 2025-03-07 at 10:00 UTC on MEXC, alongside a Bitget Launchpool that ran Mar 7–10, 2025 ([CoinMarketCap Academy](https://coinmarketcap.com/academy/article/how-to-claim-elixir-elx-token-airdrop-step-by-step-guide)).
- Peak supplies and dates: USDe $14.82B (2025-10-04); USD0 $1.86B (2025-01-07); USR $586M (2025-01-27; Resolv protocol TVL peak $685M on 2025-02-20); USDf $2.15B (2025-10-15); USDO $299M (2025-07-21); lvlUSD $185M (2025-05-23); deUSD $302M (2025-03-08) ([DefiLlama stablecoins](https://stablecoins.llama.fi/stablecoins?includePrices=false), [resolv-usr](https://api.llama.fi/protocol/resolv-usr)).

### Inferences
- Evolution of FDV/TVL (calc):
  - ENA went from 7.4x (TGE) to a peak near 10x in week 1, then to 0.8x now. Its FDV fell 66% while USDe supply grew 3.2x.
  - USUAL went from 4.8x to below 0.1x on stablecoin supply.
  - FF went from 1.5x to 1.1x. Its FDV is down 54% while USDf is down 36%, which makes FF the most "TVL-anchored" of the group.
  - RESOLV, EDEN and ELX are all down more than 85% from TGE close.
- Launch multiples compressed from roughly 5–7x (2024 cohort: ENA, USUAL) to about 1–1.7x (2025 cohort: ELX, RESOLV, FF, EDEN). A 2026 launch should probably assume the 1–2x FDV/TVL range at TGE, not the 2024 multiples.
- Launch-day intraday wicks are not reliable anchors for FDV: FF touched $0.80–0.85 and EDEN $1.11–1.53, versus day-1 closes of $0.28 and $0.40. The day-1 close or week-1 average is the more honest "TGE FDV".

### Gaps
- There is no CoinGecko historical FDV series before 2025-09-28, because the free API is limited to 365 days. Historic FDVs here are price × stated supply (calc), not CoinGecko-reported FDVs.
- OpenEden's TVL at TGE should include TBILL/other RWA AUM. DefiLlama's protocol list returned no positive-TVL OpenEden entry, so only USDO supply is used, which understates TVL and overstates FDV/TVL.
- I could not reconcile the two USUAL denominators: DefiLlama's stablecoin dataset shows USD0 at $547M while its protocol TVL shows $88M. I also did not confirm when or how USUAL's max supply changed from 4B to 3B.
- Elixir and Level have no clean "TVL at TGE" from protocol TVL. For Elixir only deUSD supply is available, and Level has no TGE.
- f(x) Protocol (FXN) was skipped: it has no comparable points-to-TGE event. FXN is ~$29.9 on 2026-09-28 per [DefiLlama coins](https://coins.llama.fi/prices/current/coingecko:fxn-token) and fxUSD supply is $88M ([DefiLlama fxUSD](https://stablecoins.llama.fi/stablecoin/168)).

## Q2. % of supply to airdrop/points and realized $ value per point / per $ deposited per day

### Takeaway
Season-1 airdrops clustered at 5–10% of supply: ENA 5%, USUAL 7.5%, EDEN 7.5%, RESOLV 10%, ELX 8%, and FF about 5% public Miles inside an 8.3% community bucket. Binance HODLer/Launchpool took another 1.5–7.5%. Normalized by average stablecoin supply over the campaign, only Ethena S1 (about 450–550% annualized airdrop yield on average capital) and Usual Pills (about 120–365%) paid "hyper" yields. Later campaigns paid roughly 7–38% annualized on average capital, before vesting and forfeiture haircuts: Ethena S2/S3, Resolv, Falcon and OpenEden.

### Cited Findings

**Allocation and structure**
- **ENA:**
  - S1 (Shards): 750M ENA, 5% of supply ([DL News](https://www.dlnews.com/articles/defi/ethena-500m-airdrop-leads-defi-project-to-plan-the-next-one/), [CoinGecko Learn](https://www.coingecko.com/learn/ethena-labs-airdrop-shard-campaign)). The campaign began Feb 19 and ran about 6 weeks, ending April 1, 2024, with claims from April 2 ([Bitcoin.com](https://news.bitcoin.com/ethena-details-ena-airdrop-for-shard-holders-announces-bitcoin-sats-campaign/), [Airdroplet](https://www.airdroplet.com/airdrop/ethena)).
  - S2 (Sats): 5% (750M ENA). Snapshot Sep 1, season end Sep 2, claim from the week of Sep 30, 2024 ([cruzcontrol X post](https://twitter.com/cruzcontrol660/status/1830794262562382323), [Bitget News](https://www.bitget.com/news/detail/12560604187162)).
  - S3: 3.5%, claimable May 1, 2025, reported as about $178.5M at then-current price ([X post](https://x.com/Airdrop_Adv/status/1917709309632471225), [Ethena mirror S3](https://mirror.xyz/0xF99d0E4E3435cc9C9868D1C6274DfaB3e2721341/doylqNcqvkZ04XPlaMwIM1We5ZlQfnTYQNXfPKiRRh8)). S3 gave 40x rewards for sENA versus 2x for sUSDe and ended March 23, 2025 ([CoinGecko Learn](https://www.coingecko.com/learn/ethena-labs-airdrop-shard-campaign)).
  - S4: "at least match the 3.5%" ([search summary of Airdrop Alert/Ethena](https://airdropalert.com/airdrops/ethena-season-3/)).
  - Binance Launchpool: 300M ENA (2%) ([CoinJournal](https://coinjournal.net/news/binance-adds-ethena-ena-as-50th-launchpool-project/)).
- **USUAL:**
  - Airdrop: 7.5% of supply to Pills holders ([CoinGecko Learn](https://www.coingecko.com/learn/what-is-usual-crypto-rwa-usual-airdrop), [Usual blog/pendle](https://usual.money/blog/pendle)).
  - Structure: 98.5% of wallets could claim 100% instantly ("Fair Launch"). The top 1.5% got 10% immediately and the remaining 90% either vested over 6 months (Jan 18 to Jun 18, 2025) or exited early with a "DAO contribution" that decreased linearly over 6 months. The blog breakdown also lists Binance Launchpool 7.5%, market makers 0.6%, "normal distribution" 1% and "instantly vested" 2.5% ([Usual blog](https://usual.money/blog/airdrop-the-genesis-of-ownership)).
  - Usual docs: unwrapping USD0++ early via `temporaryOneToOneExitUnwrap` "voids any USUAL airdrop" ([Usual tech docs llms-full](https://tech.usual.money/llms-full.txt)).
  - Pendle took a 3% fee on all YT Pills ([Usual blog/pendle](https://usual.money/blog/pendle)).
- **RESOLV:**
  - Allocation: 1B supply; Season-1 airdrop 10%, ecosystem/community 40.9%, team 26.7%, investors 22.4% ([ChainCatcher](https://www.chaincatcher.com/en/article/2180331)). S1 was fully unlocked at TGE ([search summary citing BingX](https://bingx.com/en/learn/article/what-is-resolv-protocol-and-how-to-claim-your-resolv-token-airdrop)).
  - Campaign and claim: 9-month campaign ending May 2025, snapshot June 4, 2025. Registration ran May 9–25 and claims May 27–Jun 27. Rewards were paid as stRESOLV with a 2-week unstake cooldown ([Resolv docs](https://docs.resolv.xyz/litepaper/resolv-token/resolv-token-airdrop)).
  - Binance HODLer: 20M RESOLV (2%), 21st project ([CryptoNinjas](https://www.cryptoninjas.net/news/binance-launches-20m-resolv-airdrop-for-bnb-holders-ahead-of-major-token-listing/)).
  - Later seasons: S2 5%, S3 3% ([search summary of Resolv docs](https://docs.resolv.xyz/litepaper/using-resolv/resolv-points/seasons/season-2)).
- **FF:**
  - Official allocation: community airdrops and launchpad sale 8.3% (Miles, Buidlpad sale, Kaito Yap2Fly), ecosystem 35%, foundation 24%, team 20%, marketing 8.2%, investors 4.5% ([Falcon tokenomics](https://falcon.finance/news/introducing-ff-tokenomics)).
  - Tokenomist line items: "Airdrop PUBLIC (TGE) 2.50%", "Airdrop PUBLIC (Remaining) 2.50%", "Airdrop BETA categories 1.00% each" and "Pre-TGE Sale & Marketing 1.30%" ([Tokenomist FF](https://tokenomist.ai/falcon-finance-ff)).
  - Claim options: 30% unlocked with 70% on a 1-month cliff plus 6-month vesting, or 50% forfeited for immediate access. The claim window ran Sep 29 to Dec 28, 2025 ([blockchain.news](https://blockchain.news/flashnews/falcon-finance-ff-airdrop-window-staking-bonus-and-pendle-claim-2-32m-ff-after-10-11-flash-crash-trading-takeaways), [Falcon launch post](https://falcon.finance/news/falcon-finance-enters-its-next-chapter-with-the-launch-of-ff-token)).
  - Binance HODLer: 150M FF (1.5%) ([CryptoNewsZ](https://www.cryptonewsz.com/binance-falcon-finance-as-49th-hodler-airdrop/)).
- **EDEN:**
  - Bills airdrop: 7.5% (75M EDEN) plus a 0.25% shared pool. The Bills campaign ran March 2025 to Sep 15, 2025 ([OpenEden](https://openeden.com/news/openseason-next-phase-bills-points-eden-rewards/), [Bitget Academy](https://web3.bitget.com/en/academy/openeden-airdrop-guide-how-to-participate-and-claim-eden-rewards)).
  - Distribution rules: tokens were distributed through the "EDEN HODLers Bonus Mechanism". Wallets under 100K points were ineligible, and the "Starting Portion" was raised from 20% to 80% for wallets under 10M points ([OpenEden](https://openeden.com/news/openseason-next-phase-bills-points-eden-rewards/)).
  - Other allocations: early adopters 6%, ecosystem 41.22%, team 20%, investors 15.28%, foundation 10% ([Tokenomist EDEN](https://tokenomist.ai/openeden)).
  - Binance HODLer: 15M EDEN (1.5%), 47th project ([Coinfomania](https://coinfomania.com/binance-eden-47th-hodler-airdrop-15m-tokens/)).
- **ELX:** 8% airdrop, mostly to Apothecary potion holders (S1 1.25%, S2 3.00%, S3 2.75%); 41% of supply to community ([CoinMarketCap Academy / Elixir via search](https://coinmarketcap.com/academy/article/how-to-claim-elixir-elx-token-airdrop-step-by-step-guide), [Elixir mirror](https://mirror.xyz/0x25832C2fC7B7380E5B74Ea280ea2D2C98a0d5644/XXZuIQ1Awjzn2KkNGENrJcl1zvsj2RVUWKunVHFq2rA)).
- **Pendle's own FF claim:** 2.32M FF (~$294K) from Falcon Miles S1 ([Phemex](https://phemex.com/news/article/pendle-claims-294k-in-falcon-finance-airdrop-25424)).

**Realized airdrop value normalized per $ of average stablecoin supply per day (calc)**

Inputs are the airdrop tokens × price, divided by (average daily stablecoin supply over the campaign × days). The supply inputs come from [DefiLlama stablecoins](https://stablecoins.llama.fi/stablecoin/146) and [DefiLlama resolv-usr](https://api.llama.fi/protocol/resolv-usr), and the prices from the [Gate API](https://api.gateio.ws/api/v4/spot/candlesticks?currency_pair=ENA_USDT&interval=1d). This is an average across all capital. Boosted venues such as Pendle YT/LP earned more per $ than average, and non-earning or low-multiplier capital earned less.

| Campaign | Window used | Avg supply | TVL-days | Airdrop tokens | $ value (price, date) | $ per $1 per day | Annualized on avg capital |
|---|---|---|---|---|---|---|---|
| Ethena S1 | 2024-02-19→04-01 (43d) | USDe $899M | $38.7B | 750M ENA | $580M (@$0.773, 04-02); $480M (@$0.64 launch) | $0.0124–0.0150 | ~453–547% |
| Ethena S2 | 2024-04-02→09-02 (154d) | USDe $2.93B | $450.9B | 750M ENA | $179M (@$0.2385, 09-02) – $275M (@$0.367, 09-30 claim) | $0.00040–0.00061 | ~14.5–22.3% |
| Ethena S3 | 2024-09-02→2025-03-23 (203d) | USDe $4.44B | $900.4B | 525M ENA | $169M (@$0.322, 2025-05-01 claim) | $0.00019 | ~6.9% |
| Usual Pills | 2024-07-10→11-18 (132d) or →12-18 (162d) | USD0 $236M / $300M | $31.2B / $48.5B | 300M USUAL (7.5% of 4B) | $312M (@$1.04, 12-18 TGE close); $158M (@$0.528 pre-market 11-18) | $0.0033–0.0100 | ~119–365% |
| Resolv S1 | 2024-09-02→2025-06-04 | protocol TVL $338M (USR-only $262M) | $87.8B ($72.3B) | 100M RESOLV | $35.1M (@$0.351, 06-10); $22.7M (@$0.2265, d7) | $0.00026–0.00049 | ~9.4–17.7% |
| Falcon Miles S1 | 2025-03-24→09-28 (189d) | USDf $709M | $134.1B | ~250M–500M FF (2.5–5% public, Tokenomist) | $70M–$140M (@$0.281, 09-29); $50M–$101M (@$0.2015 wk-1 avg) | $0.00037–0.00105 | ~14–38% (before vest/forfeit) |
| OpenEden Bills | 2025-03-01→09-15 (199d) | USDO $205M | $40.8B | 75M EDEN | $29.9M (@$0.3985, 09-30); $9.7M (@$0.1298, d30) | $0.00024–0.00073 | ~8.7–26.7% (USDO only; before EHBM haircuts) |

### Inferences
- The "hyper-yield" airdrops (ENA S1, USUAL Pills) share three features: short campaigns (6 weeks to 4–5 months), a small average TVL relative to the FDV the market later assigned, and a hot sector narrative. Once a campaign's TVL-days grew large (ENA S2/S3 at $450–900B TVL-days; Falcon at $134B), value per $-day fell by one to two orders of magnitude, even with similar % allocations.
- For a new entrant the relevant anchor is the 2025 cohort: RESOLV/FF/EDEN paid about 9–38% annualized on average capital at TGE prices, and less after vesting, forfeiture or price decay. A 5–10% airdrop at a 1–1.5x FDV/TVL implies roughly 5–15% of TVL paid out as tokens. Spread over a 6–9 month campaign, that is 7–30% annualized on average capital.
- Vesting and forfeiture structures (USUAL top 1.5%; FF 50% forfeiture or 70% vest; EDEN EHBM starting portion 20–80%; RESOLV paid as stRESOLV with a cooldown) materially cut realized value versus headline value. Tokens fell 17–67% within 30 days for RESOLV, FF and EDEN.

### Gaps
- No official "value per point" (total points outstanding) was found for any of the projects: total Shards/Sats, Pills, Resolv points, Miles or Bills. So per-point values cannot be computed. The per-$-day metric above is a substitute.
- The exact Falcon Miles S1 share of the 8.3% bucket is not officially broken out. The 2.5% + 2.5% public figure is from Tokenomist, and its "Airdrop BETA 1% each" line count is unclear.
- USUAL: the blog's breakdown (Launchpool 7.5% vs Pills 7.5%) is ambiguous about whether Pills received 7.5% of the 4B max or 7.5% of TGE-minted supply. The $ values above assume 300M USUAL and should be treated as an upper bound.
- The Ethena S1 vesting details for larger wallets and the S2 vesting terms were not re-sourced.
- A search snippet claimed "1K USDe on day one → 640 ENA; 1K YT-USDe → 8K ENA", but I could not trace it to a verifiable primary source, so it is excluded.

## Q3. Did Pendle YT buyers make or lose money in each points season?

### Takeaway
Few published post-mortems with hard numbers exist. Comparing Pendle's historical implied APY (the cost of holding YT) with realized airdrop value per $-day gives this pattern:
- **Clearly profitable:** Ethena S1 and Usual Pills (airdrop yield about 2–5x and 5–15x the implied cost respectively).
- **Probably roughly break-even to negative:** Ethena S2 (depended on entry timing) and Ethena S3 for USDe YT.
- **Marginal:** Resolv S1, where late cheap YT-USR won and early expensive wstUSR YT likely lost.
- **Likely profitable at TGE, with realized value eroded by vesting and price decay:** Falcon S1 and OpenEden Bills.
- **Total loss:** Level XP YT buyers, since no token launched and lvlUSD wound down.

### Cited Findings
- **Pendle weekly implied APY versus underlying APY during each campaign** ([Pendle API](https://api-v2.pendle.finance/core/v2/1/markets/0xb4460e76d99ecad95030204d3c25fb33c4833997/historical-data?time_frame=week); market addresses from [Pendle markets API](https://api-v2.pendle.finance/core/v1/1/markets?limit=100)). Final-week values near maturity are excluded as artifacts.
  - ENA S1:
    - PT/YT-USDe-4APR2024 implied 102–196% (Feb 26 to Mar 25, 2024) and 231% in the Apr 1 week. Underlying yield was 0; max TVL $59M.
    - sUSDe-25APR2024 implied 38–113% against 12–55% underlying.
  - ENA S2: USDe-25JUL2024 implied 70% (Apr 1, 2024) falling to 19% by late June/July 2024.
  - ENA S2 tail/S3: USDe-24OCT2024 implied 10–16%; USDe-27MAR2025 implied 9–25%.
  - Usual Pills:
    - USD0++-31OCT2024 implied 15–29% (Aug 5 to Oct 21, 2024), max TVL $42M.
    - USD0++-30JAN2025 implied 21–39%, with underlying 17–65% once USUAL emissions started.
  - Resolv S1: wstUSR-27MAR2025 implied 10–36% against 2–14% underlying; USR-29MAY2025 implied 6–14% (Feb 17 to May 19, 2025).
  - Falcon S1: sUSDf-25SEP2025 implied 9–21% against 8–15% underlying (Apr 14 to Sep 1, 2025), rising to 33–45% in September 2025.
  - OpenEden Bills: cUSDO-19JUN2025 implied 2–16% against ~4% underlying; cUSDO-20NOV2025 implied 9–15% against 3–4%.
  - Level XP: lvlUSD-29MAY2025 implied 9–19%; slvlUSD implied 11–18% against 6–13% underlying.
- **Qualitative and ex-ante YT estimates from sources:**
  - Usual/Pendle material: "YT farmers are looking to gain a 5x return once $USUAL tokens are airdropped", and "ROI of 3x to 4x at certain valuations" ([Usual blog/pendle](https://usual.money/blog/pendle), [DOKDO DAO AMA recap](https://medium.com/cryptodokdo/ama-recap-dokdo-dao-x-pendle-1612fe6b3381)). These are pre-TGE projections, not realized figures.
  - A ChainCatcher article (the page now returns HTTP 410) reportedly stated the Usual airdrop yielded "over 10 times returns" for YT, and that EigenLayer eETH YT buyers recouped costs from the ETHFI airdrop ([ChainCatcher via search snippet](https://www.chaincatcher.com/en/article/2196073)). I could not verify this directly.
  - For Resolv, a French guide notes that the displayed YT-USR multiplier (1432x) overstates leverage: the "real multiplier" was ~47.7x versus holding USR at 30 points/day ([Cryptoast via search](https://cryptoast.fr/airdrop-resolv-quelques-jours-pour-enregistrer-afin-recevoir-cryptos/)).
  - During S2, Pendle YT/LP USDe on Mantle earned 20x Sats per USDe ([Mantle blog](https://www.mantle.xyz/blog/guide/ethena-season-2-sats-campaign-comes-to-mantle-network)).
  - Pendle sUSDf pools (Jan 29, 2026 maturity, Falcon S2) offered 72x Miles for two weeks ([search summary, Boxmining/Messari](https://www.boxmining.com/airdrops/falcon-finance/)).
  - Pendle itself claimed 2.32M FF (~$294K) from Falcon S1 ([Phemex](https://phemex.com/news/article/pendle-claims-294k-in-falcon-finance-airdrop-25424)).

### Inferences
Comparison basis (calc, combining Q2's airdrop yield on average capital with the Pendle implied APY above): a YT buyer paying implied APY X (net of any underlying yield the YT still receives) profits if their points' value per $-day, annualized, exceeds X. Pendle positions usually carried equal or higher point multipliers than average capital, so average-capital airdrop yield is a conservative, lower-bound proxy for the YT side.
- **Ethena S1: profitable.** Airdrop yield was ~453–547% at launch-day prices (~750% at the week-1 average of $1.07) against 102–196% implied. That is roughly 2.3–5x gross, or about +130% to +400% ROI (calc).
- **Ethena S2: mixed, likely negative for early buyers.**
  - April–May buyers paid 27–70% implied against a 14.5–22.3% average airdrop yield.
  - Late June–July buyers paid about 19%, which was near break-even at the Sep 30 claim price.
  - The 20x Pendle Sats boost on Mantle, and similar boosts, may have flipped some positions positive; this is uncertain.
- **Ethena S3: likely negative for USDe YT.** Average airdrop yield was about 6.9% against 9–25% implied, and S3 rewards tilted to sENA (40x) over sUSDe (2x), so USDe-based YT got less.
- **Usual Pills: strongly profitable** for buyers of the Oct 2024 or Jan 2025 YT at 15–39% implied, against a 119–365% airdrop yield. That is roughly 5–15x gross, consistent with the qualitative "5x" and "10x" reports. Large YT holders in the top 1.5% faced 90% vesting while USUAL fell 91% in 180 days, so their realized ROI depended on taking the early-exit penalty.
- **Resolv S1: marginal.**
  - Airdrop yield was about 9–18%. YT-USR cost 6–14%, while wstUSR YT cost 10–36% implied minus 2–14% underlying.
  - Late buyers of cheap YT-USR (6–10% implied, Mar–May 2025) likely made modest profits if they sold stRESOLV quickly.
  - Buyers of wstUSR YT in Dec 2024–Jan 2025 (24–36% implied) likely lost money, especially since RESOLV fell 35% in week 1.
- **Falcon S1: likely profitable at TGE, but fragile.**
  - Net YT cost was about 0–13% (implied minus underlying), against 14–38% average airdrop yield before haircuts.
  - The 50% forfeiture or 70% vesting options, plus FF's slide to about $0.11 by Oct 11, 2025, cut realized value significantly.
- **OpenEden Bills: probably modestly positive** if claimed and sold near TGE: net YT cost about 5–12% against 9–27% gross.
  - EHBM starting portions of 20–80%, plus EDEN falling 67% in 30 days, make the realized outcome highly dependent on claim timing.
- **Level: YT buyers lost 100% of YT cost.** They paid 9–19% implied and no token has launched; lvlUSD supply fell from $185M to about $0.

### Gaps
- I found no published, data-backed post-mortem with a realized YT ROI figure (e.g., an "Ethena Season 1 YT ROI" or "Resolv YT ROI" thread or Dune dashboard) that I could fetch. The ROI inferences are my calc from Pendle implied APY and airdrop value on average capital, not realized per-wallet outcomes.
- The per-venue point multipliers for Pendle YT versus base holders in each season were not systematically collected. They could raise or lower YT ROI versus the average-capital proxy.
- Pendle's historical YT price series was not pulled; only implied APY was. Daily-level data may shift the break-even estimates.

## Q4. How long did points programs run before TGE, and how did TGE timing relate to TVL milestones or funding?

### Takeaway
Campaign lengths ranged from about 6 weeks (Ethena S1) to about 9 months (Resolv S1). Usual, Falcon and OpenEden ran about 4–6.5 months to TGE. The successful TGEs landed at or near stablecoin-supply highs: Ethena at +540% supply growth during S1, Usual 3 weeks before its supply peak, Falcon near its peak, and Elixir exactly at its peak. Resolv's TGE came after supply had already halved from its peak, and OpenEden's after a roughly 21% decline.

### Cited Findings
- **Ethena:**
  - Shards ran Feb 19 to Apr 1, 2024 (about 6 weeks) with TGE on Apr 2, 2024 ([Bitcoin.com](https://news.bitcoin.com/ethena-details-ena-airdrop-for-shard-holders-announces-bitcoin-sats-campaign/), [Airdroplet](https://www.airdroplet.com/airdrop/ethena)).
  - USDe supply grew from $242M (2024-02-19) to $1.56B at TGE, then $2.22B a week later and $3.46B by 2024-07-10 ([DefiLlama USDe](https://stablecoins.llama.fi/stablecoin/146)).
  - S2 was planned to end Sep 2 or when USDe supply hit $5B. TVL had declined to $2.92B from a $3.612B peak in early July ([Gate Learn/PANews via search](https://www.gate.com/learn/articles/detailed-explanation-of-ethena-s-three-strategies-in-season-2-and-their-potential-rewards/2709)).
- **Usual:**
  - Mainnet launched July 10, 2024 with a 4-month Pills campaign, and reached $355M TVL and 50k users in 3 months ([CoinGecko Learn](https://www.coingecko.com/learn/what-is-usual-crypto-rwa-usual-airdrop)).
  - Launchpool ran Nov 15–18, 2024; pre-market opened Nov 19, 2024; spot TGE was Dec 18, 2024 ([Coinspeaker](https://www.coinspeaker.com/binance-introduces-usual-launchpool-pre-market-trading-soon/), [Usual blog](https://usual.money/blog/airdrop-the-genesis-of-ownership)). That is about 132 days to pre-market and 161 days to spot (calc).
  - USD0 supply was $364M on 2024-11-18, $875M on 2024-12-18, peaked at $1.86B on 2025-01-07, and fell to $1.17B by 2025-02-10 ([DefiLlama USD0](https://stablecoins.llama.fi/stablecoin/195)).
- **Resolv:**
  - The S1 campaign ran 9 months, ended May 2025, with snapshot June 4, 2025 ([search summary of BingX](https://bingx.com/en/learn/article/what-is-resolv-protocol-and-how-to-claim-your-resolv-token-airdrop)). Trading began 2025-06-10 ([Gate RESOLV](https://api.gateio.ws/api/v4/spot/candlesticks?currency_pair=RESOLV_USDT&interval=1d)).
  - Protocol TVL peaked at $685M on 2025-02-20 and was $351M at TGE. USR supply was $572M on 2025-02-15 and $220M at TGE ([DefiLlama resolv-usr](https://api.llama.fi/protocol/resolv-usr), [DefiLlama USR](https://stablecoins.llama.fi/stablecoin/197)).
- **Falcon:**
  - USDf supply first appears on DefiLlama on 2025-03-24 at $95M (2025-03-26) and reached $1.90B at TGE on 2025-09-29, which is about 189 days of supply history before TGE (calc) ([DefiLlama USDf](https://stablecoins.llama.fi/stablecoin/246)).
  - At launch Falcon cited 1.9B USDf and "nearly $2 billion" TVL ([Falcon launch post](https://falcon.finance/news/falcon-finance-enters-its-next-chapter-with-the-launch-of-ff-token)). USDf peaked at $2.15B on 2025-10-15.
  - Buidlpad sale commitments exceeded $112M against a $4M target ([MEXC news via search](https://www.mexc.com/news/107631)).
- **OpenEden:**
  - Bills ran March 2025 to Sep 15, 2025 and TGE was Sep 30, 2025, about 6.5 months ([OpenEden](https://openeden.com/news/openseason-next-phase-bills-points-eden-rewards/)).
  - USDO peaked at $299M on 2025-07-21 and was $235M at TGE ([DefiLlama USDO](https://stablecoins.llama.fi/stablecoin/241)). Tokenomist lists a $5M raise ([Tokenomist EDEN](https://tokenomist.ai/openeden)).
- **Elixir:** deUSD first appears 2024-07-18 on DefiLlama and peaked at $302M on 2025-03-08, one day after the ELX TGE on 2025-03-07 ([DefiLlama deUSD](https://stablecoins.llama.fi/stablecoin/210), [CoinMarketCap Academy](https://coinmarketcap.com/academy/article/how-to-claim-elixir-elx-token-airdrop-step-by-step-guide)).
- **Level:**
  - Raised over $6M in total, including a $2.6M strategic round led by Dragonfly announced March 18, 2025 ([search summary, CoinDesk](https://www.coindesk.com/business/2025/03/17/stablecoin-protocol-level-aims-to-expand-usd80m-defi-yield-token-with-fresh-capital-raise), [The Block](https://www.theblock.co/post/313461/peregrine-exploration-polychain-dragonfly-stablecoin-level)).
  - lvlUSD peaked at $185M on 2025-05-23 and is about $0.4M now ([DefiLlama lvlUSD](https://stablecoins.llama.fi/stablecoin/229)).
  - A secondary source says Level announced it would cease operations and be purchased by a larger DeFi protocol, with a withdrawal deadline of Dec 15 ([Bitget Academy via search](https://web3.bitget.com/en/academy/top-10-airdrops-in-october-2025-complete-guide-to-free-crypto-rewards)). This is unverified.

### Inferences
- Pattern: TGEs timed into rising or peak supply (ENA, USUAL, FF, ELX) got the highest launch FDVs. After TGE, supply typically peaked within weeks and then bled as mercenary points capital left. Examples:
  - USD0 fell about 37% from its peak ($1.86B on 2025-01-07 to $1.17B on 2025-02-10) in about 5 weeks.
  - USDf dipped from $1.90B at TGE to $1.43B on 2025-10-10 (the market-wide crash), recovered to a $2.15B peak on 2025-10-15, and has since drifted to $1.21B.
  - USR fell from $586M to $220M before TGE.
- Long campaigns of 9 months or more (Resolv) diluted per-$-day value and let TVL decay before TGE. A 4–6 month campaign timed at a TVL high is the pattern the successful comps followed.

### Gaps
- Exact start dates are missing for: Falcon Miles (the Pilot Season start is not sourced; the USDf launch date is used as a proxy); Resolv points (September 2024 is inferred from "9 months ending May 2025"); and Elixir Potions seasons.
- Funding-round timing relative to TGE was not systematically collected (Ethena, Usual and Resolv rounds not re-sourced here).

## Q5. Post-TGE price performance

### Takeaway
Every token in the set is below its TGE-day close as of 2026-09-28. The group's median is about −85%, and every token suffered a peak-to-trough drawdown of −79% to −99.8%.
- **Only ENA and USUAL sustained trading well above their TGE-day close:** ENA reached +97% at its ATH in week 2 and USUAL +55% in week 1. Both are 2024-cohort launches.
- **2025 cohort:** ELX briefly traded up to about +41% on a closing basis in its first week, then collapsed. RESOLV, FF and EDEN dumped from day 1. FF is the relative winner, at −54% versus its TGE close.

### Cited Findings

Performance table (calc from [Gate API](https://api.gateio.ws/api/v4/spot/candlesticks?currency_pair=ENA_USDT&interval=1d) daily closes; % versus TGE-day close):

| Token | TGE-day close | +7d | +30d | +90d | +180d | +365d | 2026-09-28 | ATH (date) | Max drawdown (close, from running peak) / low |
|---|---|---|---|---|---|---|---|---|---|
| ENA | $0.773 (2024-04-02) | $1.241 (+60%) | $0.797 (+3%) | $0.505 (−35%) | $0.389 (−50%) | $0.331 (−57%) | $0.263 (−66%) | $1.52 (2024-04-11) | −95.1%; low ~$0.070 (Jun–Jul 2026) |
| USUAL | $1.04 (2024-12-18) | $1.401 (+35%) | $0.547 (−47%) | $0.159 (−85%) | $0.089 (−91%) | $0.0229 (−98%) | $0.0151 (−98.5%) | $1.61–1.66 (2024-12-19/20) | −99.5%; low $0.0076 (2026-07-29) |
| RESOLV | $0.351 (2025-06-10) | $0.2265 (−35%) | $0.151 (−57%) | $0.165 (−53%) | $0.0746 (−79%) | $0.0165 (−95%) | $0.0186 (−95%) | $0.41 (2025-06-11) | −95.8%; low $0.0143 (2026-06-20) |
| FF | $0.281 (2025-09-29) | $0.187 (−33%) | $0.152 (−46%) | $0.093 (−67%) | $0.071 (−75%) | n/a | $0.130 (−54%) | $0.80–0.85 intraday (2025-09-29) | −79.2%; intraday low $0.048 (2025-10-10 flash crash) |
| EDEN | $0.3985 (2025-09-30) | $0.3295 (−17%) | $0.1298 (−67%) | $0.0667 (−83%) | $0.026 (−93%) | n/a | $0.0589 (−85%) | $1.11–1.53 intraday (2025-09-30) | −93.5%; low $0.0257 (2026-03-30) |
| ELX | $0.389 (2025-03-07) | $0.428 (+10%) | $0.124 (−68%) | $0.085 (−78%) | $0.126 (−68%) | $0.0018 (−99.5%) | $0.0012 (−99.7%) | $0.77 intraday (2025-03-07/11) | −99.8% |

- Cross-checks:
  - DefiLlama shows the same shape: ENA ATL $0.0712 on 2026-07-01, USUAL ATL $0.00758 on 2026-07-30, and FF closing low $0.0583 on 2026-07-08 ([DefiLlama chart API](https://coins.llama.fi/chart/coingecko:ethena?start=1711584000&span=500&period=1d)).
  - CoinGecko has the USUAL ATH at $1.61 on 2024-12-19 and the RESOLV ATH at $0.4085 on 2025-06-11 ([CG usual](https://api.coingecko.com/api/v3/coins/usual), [CG resolv](https://api.coingecko.com/api/v3/coins/resolv)).
  - CoinPaprika has the ENA ATH at $1.52 on 2024-04-11 ([CoinPaprika ENA](https://api.coinpaprika.com/v1/tickers/ena-ethena)).
- **Controversies and events:**
  - FF "loses over 70% on suspected team selling". Claims were delayed, and influencers (and possibly the team) sold while airdrop claims were still processing ([Cryptopolitan](https://www.cryptopolitan.com/falcon-finance-loses-suspected-team-selling/), [CCN](https://www.ccn.com/analysis/crypto/falcon-finance-ff-price-crashes-token-debut-what-lies-ahead/)).
  - Resolv exploit, March 22, 2026:
    - A compromised privileged signing key minted about $80M of unbacked USR, and roughly $23–25M was extracted ([CoinDesk](https://www.coindesk.com/markets/2026/03/23/resolv-stablecoin-drops-70-after-usd80-million-exploit-after-attacker-mints-usr), [Chainalysis](https://www.chainalysis.com/blog/lessons-from-the-resolv-hack/), [Blockaid](https://www.blockaid.io/blog/how-a-compromised-key-minted-80m-in-resolvs-usr-stablecoin-and-triggered-a-depeg)).
    - USR fell as low as $0.025 on Curve ([Web3Firewall via search](https://www.web3firewall.xyz/resolv-exploit)).
    - USR supply went from $173M (2026-03-31) to $9M (2026-06-30) to $6M now ([DefiLlama USR](https://stablecoins.llama.fi/stablecoin/197)).
    - RESOLV was $0.0598 on 2026-03-21 and $0.0512 on 2026-03-23 ([Gate RESOLV](https://api.gateio.ws/api/v4/spot/candlesticks?currency_pair=RESOLV_USDT&interval=1d)).
  - Elixir shut down deUSD in November 2025 after Stream Finance disclosed a $93M loss. Stream owed Elixir $68M and held about $75M of deUSD, and deUSD fell more than 97% in 24 hours ([Yahoo Finance](https://finance.yahoo.com/news/elixir-shuts-down-deusd-stablecoin-104937488.html), [FXStreet](https://www.fxstreet.com/cryptocurrencies/news/elixir-deusd-stablecoin-collapse-stream-finance-loss-2025-202511071458), [crypto.news](https://crypto.news/elixir-retires-deusd-after-streams-93m-loss/)).
  - Ethena postponed the launch of the Season 2 eligibility-check page ([Bittime](https://www.bittime.com/en/blog/halaman-inspeksi-airdrop-ethena-season-2)).
  - USDe supply fell from $14.66B (2025-10-10) to $9.07B (2025-11-05) and $4.46B (2026-06-30); it is $4.94B now ([DefiLlama USDe](https://stablecoins.llama.fi/stablecoin/146)).
- **Listing venues:**
  - ENA: Binance Launchpool #50 ([CoinJournal](https://coinjournal.net/news/binance-adds-ethena-ena-as-50th-launchpool-project/)).
  - USUAL: Binance Launchpool #61 plus Binance Pre-Market ([Coinspeaker](https://www.coinspeaker.com/binance-introduces-usual-launchpool-pre-market-trading-soon/)).
  - RESOLV: Binance HODLer Airdrop #21 ([CryptoNinjas](https://www.cryptoninjas.net/news/binance-launches-20m-resolv-airdrop-for-bnb-holders-ahead-of-major-token-listing/)).
  - FF: Binance HODLer Airdrop, reported as the 46th by [CoinEdition](https://coinedition.com/falcon-finance-ff-debuts-with-binance-airdrop/) but the 49th in the [CryptoNewsZ URL](https://www.cryptonewsz.com/binance-falcon-finance-as-49th-hodler-airdrop/). The sources conflict.
  - EDEN: Binance HODLer Airdrop #47 plus a Binance Alpha airdrop ([Coinfomania](https://coinfomania.com/binance-eden-47th-hodler-airdrop-15m-tokens/), [PANews](https://www.panewslab.com/en/articles/aee5346c-1b94-4a3d-b230-41c529e17e38)).
  - ELX: MEXC plus Bitget Launchpool ([CoinMarketCap Academy](https://coinmarketcap.com/academy/article/how-to-claim-elixir-elx-token-airdrop-step-by-step-guide)).

### Inferences
- **Base rate:** stablecoin-protocol governance tokens have not held TGE valuations. Even Ethena, the category winner with USDe up 3x since TGE, is −66% versus TGE close. For airdrop farmers and YT buyers, the realized value is best proxied by prices within the first 0–7 days. Using 30-day or later prices cuts value by 45–70% for the 2025 cohort.
- **Tail risks are real and recurring:** 3 of the 7 stablecoins in this set suffered existential events:
  - deUSD collapsed in Nov 2025, about 8 months after the ELX TGE.
  - USR was exploited in Mar 2026, about 9 months after the RESOLV TGE.
  - Level wound down without ever launching a token.
  - Separately, USD0 lost about 70% of its peak supply. Airdrop valuations should carry a meaningful haircut for protocol-failure risk.
- **Launch microstructure:** HODLer/Launchpool listings with 23–31% float at TGE (FF) and thin early books produce extreme first-hour wicks (FF $0.85, EDEN $1.53), then a rapid slide. The day-1 close sits 50–75% below those wicks.

### Gaps
- Hourly launch data for TGE-day VWAP/first-hour prices was not pulled (only daily OHLC). Different exchanges show different intraday highs.
- The USUAL price path in Jan 2025 is associated with the USD0++ redemption-floor change. I did not re-source that event here; only the supply and price data are cited.
- ENA's 2026 drawdown to about $0.07 (Jun–Jul 2026) and its causes were not researched beyond the price data.
- I found no reliable source confirming whether Level Money ever launched a token. The CoinGecko id "level" (LVL, $0.0048) appears to be the unrelated Level Finance perp DEX (DefiLlama lists "level-perps" under parent "level-finance"), so it is not used.
