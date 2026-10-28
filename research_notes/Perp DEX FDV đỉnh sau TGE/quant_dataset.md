# Perp DEX tokens: FDV at TGE vs highest FDV reached after TGE (quantitative dataset, TGEs 2023-10-01 to 2026-10-27)

Dataset: `quant_dataset.csv` in this folder (142 in-window candidate tokens, 70 columns, one row per token, including excluded and micro-cap rows with their class labels). Everything below is computed by one pipeline from cached API downloads: DefiLlama coins API for prices (CoinGecko-sourced, hourly for the first 31 days, daily 00:00 UTC snapshots for the full history, plus an hourly window around the CoinGecko ATH) and one CoinGecko `/coins/markets` call for intraday ATH/ATL, current price and supply. Data snapshot: 2026-10-27. Prices in USD.

## Q1. Universe: which perp DEX tokens had their TGE in the window, and what was excluded?

### Takeaway
Discovery across CoinGecko's "Perpetuals" and "Derivatives" categories, DefiLlama's derivatives-type protocols with a CoinGecko id, and the seed list gave 290 candidate ids. 142 had a first recorded price on or after 2023-10-01. They split into 45 core perp DEX tokens, 22 borderline, 30 unverified micro-caps and 45 non-perp exclusions. The main statistics use the 63 core plus borderline tokens with usable data.

### Cited Findings
- Discovery sources: CoinGecko category `decentralized-perpetuals` returned 111 coins and `decentralized-derivatives` returned 121 — [CoinGecko markets by category](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&category=decentralized-perpetuals&per_page=250&page=1); DefiLlama protocols in Derivatives/Options/Synthetics/Basis Trading with a `gecko_id` = 147 — [DefiLlama protocols](https://api.llama.fi/protocols). Seed names were resolved against CoinGecko's coin list — [CoinGecko coins/list](https://api.coingecko.com/api/v3/coins/list).
- TGE filter: the first recorded price per coin comes from DefiLlama. Of 290 ids, 142 first priced on or after 2023-10-01, 117 earlier (excluded as old) and 31 have no DefiLlama price — [DefiLlama prices/first](https://coins.llama.fi/prices/first/coingecko:hyperliquid,coingecko:vertex-protocol,coingecko:aevo-exchange).
- Seed tokens resolved and in-window (CoinGecko id): VRTX `vertex-protocol` (CG-delisted), JUP `jupiter-exchange-solana`, AEVO `aevo-exchange`, PRCL `parcl`, DRIFT `drift-protocol`, ZEX `zeta`, ORDER `orderly-network`, ADX `adrena`, HYPE `hyperliquid`, BLUE `bluefin`, MKL `merkle-trade` (CG-delisted), F `synfutures`, DRV `derive`, KILO `kiloex`, MYX `myx-finance`, AVNT `avantis`, ASTER `aster-2`, LIT `lighter`, EDGE `edgex`, DIME `paradex`, GRVT `grvt`, VOOI `vooi`, STRIKE `strike-2`, LOGX `logx-2`, HOLD `holdstation` — [CoinGecko coins/list](https://api.coingecko.com/api/v3/coins/list); [DefiLlama protocols](https://api.llama.fi/protocols).
- Seed names with no tradable token found as of 2026-10-27: StandX (CoinGecko has only the `standx-dusd` stablecoin), Pacifica, Ostium, Extended, Hibachi, Ethereal (DefiLlama symbol is USDe), Vest, Nado, Bullet, Perpl, Satori (CoinGecko `satori` is an unrelated Bittensor subnet) and IntentX. DefiLlama shows no token symbol for these protocols. Variational (`variational`), Reya (`reya`) and Zeta's new `zeta-markets` "Z" are listed on CoinGecko with no price. ZKX has no CoinGecko or DefiLlama price. RabbitX first priced before Oct 2023, so it counts as old — [DefiLlama protocols](https://api.llama.fi/protocols); [CoinGecko markets by ids](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=variational,reya,zeta-markets).
- Rebrands and migrations (the new token's first trading date is used): ASTER (from APX/ApolloX, first print 2025-09-17), DRV (from LYRA, 2025-01-15), AEVO (RBN migration, 2024-03-13), Holdstation HOLD (contract migrated Oct 2025; the original id is used), Avantis (DefiLlama now names the protocol "Veranta"), Nomina (rebrand of Omni Network, excluded because the predecessor was not a perp DEX) — [DefiLlama protocols](https://api.llama.fi/protocols); [CoinGecko Nomina](https://www.coingecko.com/en/coins/nomina).
- Merkle Trade (MKL) shut down; the token was redeemable — [The Defiant](https://thedefiant.io/news/defi/aptos-based-perp-dex-merkle-trade-shutters-business).
- Excluded in-window tokens (non-perp core product, or not a governance token), each with a reason:
  - DYDX (dydx-chain, first print 2023-10-31): Migration of 2021 DYDX token to dYdX Chain (old token per brief)
  - DRAGONX (dragonx-win, first print 2024-01-22): Deflationary token, not a perp protocol
  - JARVIS (jarvis-2, first print 2024-03-08): Not a perp protocol (pending CG description check)
  - SYK (stryke, first print 2024-04-04): Options protocol (ex-Dopex, SYK migration)
  - TLX (tlx, first print 2024-04-15): Leveraged-token platform (on Synthetix perps), not a perp exchange
  - OMNI (omni-network, first print 2024-04-17): Interoperability network (later Nomina)
  - NUTS (thetanuts-finance, first print 2024-05-20): Options
  - RWAX (rwax, first print 2024-05-29): RWA token (pending CG description check)
  - RCH (rch-token, first print 2024-06-10): Options
  - XCVX (leveraged-cvx, first print 2024-08-09): Leveraged yield token
  - XEZETH (leveraged-ezeth, first print 2024-08-09): Leveraged yield token
  - XFRXETH (leveraged-frxeth, first print 2024-08-09): Leveraged yield token
  - XEETH (leveraged-eeth, first print 2024-08-09): Leveraged yield token
  - XSTETH (leveraged-steth, first print 2024-08-09): Leveraged yield token
  - XWBTC (leverage-wbtc, first print 2024-08-09): Leveraged yield token
  - GS (gammaswap, first print 2024-09-04): Perpetual options / volatility AMM
  - USDX (usdx-money-usdx, first print 2024-09-26): Stablecoin
  - DEEP (deep, first print 2024-10-14): DeepBook: Sui spot order book
  - ITHACA (ithaca-protocol, first print 2024-12-18): Options
  - PMX (primex-finance, first print 2025-02-01): Spot margin trading on DEX pools
  - GRIX (grix, first print 2025-04-01): Options
  - ZLP (zo-perpetuals-lp-token, first print 2025-04-28): LP token, not a governance token
  - BIOS (basisos-by-virtuals, first print 2025-05-06): Basis-trading agent
  - UTY (unity-2, first print 2025-06-05): Stablecoin
  - RESOLV (resolv, first print 2025-06-10): Stablecoin protocol
  - ANA (nirvana-ana-2, first print 2025-07-13): Solana stable/yield
  - BOO (spookyswap-2, first print 2025-07-23): Spot DEX token
  - HOHM (origami-hohm, first print 2025-07-24): Leveraged vault token
  - LN (lnfi-network, first print 2025-07-25): Bitcoin/Lightning asset layer
  - APO (apo, first print 2025-07-30): Synthetics
  - OMFG (omnipair, first print 2025-08-20): Oracle-less lending + margin trading GAMM on Solana, not perps (CG description)
  - FF (falcon-finance-ff, first print 2025-09-29): Synthetic dollar
  - NOM (nomina, first print 2025-10-01): Rebrand of Omni Network interop token; now a cross-DEX trading platform (CG description) - predecessor not a perp DEX
  - ARBLUNA (eris-arbitrage-luna, first print 2025-10-06): LST arbitrage vault token
  - HOLD (holdstation-2, first print 2025-10-16): Duplicate: migrated contract of Holdstation HOLD (original listed as holdstation)
  - ZBT (zerobase, first print 2025-10-17): CeDeFi/basis
  - SIGMA (sigmadotmoney, first print 2025-10-21): Volatility tranching / leveraged-token model (f(x)-style), not perps (CG description)
  - ATM (a-t-m-by-basevol, first print 2025-10-23): Options
  - SOLO (solomon, first print 2025-11-19): Stablecoin
  - TREX (tea-rex, first print 2025-11-29): Margin trading inside DEX pools
  - KDK (kodiak-finance, first print 2025-12-23): Berachain spot DEX
  - GWEI (ethgas-2, first print 2026-01-21): Blockspace/gas futures market
  - BTW (bitway, first print 2026-03-03): CeDeFi basis trading
  - SLX (solstice, first print 2026-05-25): Stablecoin/basis
  - PIKU (piku-utility-token, first print 2026-08-28): Basis trading
- Old tokens (first price before 2023-10-01, excluded): antimatter, apex-token-2, apollox-2, arable-protocol, arkham, athos-finance, auctus, aurora-dao, barnbridge, bifrost-native-coin, bmx, btc-2x-flexible-leverage-index, bumper, chaotic-finance, chemix-ecology-governance-token, coin98, complifi, crafting-finance, cryptex-finance, dafi-protocol, delta-financial, delta-theta, deri-protocol, derivadao, dexcheck, divergence-protocol, dpex, dual-finance, duet-protocol, dydx, eth-2x-flexible-leverage-index, falcon, foom, fulcrom, futureswap, gains-network, gmx, govi, gplx, hakka-finance, handle-fi, hashdao-token, havven, hedget, hegic, hxro, ibuffer-token, ideamarket, indigo-dao-governance-token, ion, jarvis-reward-token, jojo, kalata, keep3rv1, klondike-finance-v2, krav, kromatika, kwenta, level, lien, linear, lyra-finance, mango-markets, mcdex, metalswap, metavault-trade, mettalex, mirror-protocol, mobius-finance, mummy-finance, mycelium, netherfi, oddz, offshift, opium, opx-finance, organix, palmswap, pancakeswap-token, pegasus-finance, pendle, perpetual-protocol, phame, pika-protocol, poison-finance, premia, psyoptions, quickswap, rabbitx, raydium, ribbon-finance, roseon, sakai-vault, sake-token, seth, shield-dao, siren, spot, srune, stp-network, synthetify-token, thales, thena, twindex, uma, uniwhale, unlimited-network-token, vanilla, vega-protocol, vela-token, whiteheart, woo-network, wrap-governance-token, yam-2, yfx, zeroliquid, zest-synthetic-protocol
- No DefiLlama price (cannot be measured): aboard, arrow-token, based-markets, cadence-protocol, core-markets, dip-exchange, dmx, fxdx, lexer-markets, liondex, minerva-money, my-metatrader, navi-2, onchain-trade-protocol, phoenix-token, reya, scientix, sobax, strips-finance, swych, synlev, syrup-finance, taiga, tigris, unbound-finance, urdex-finance, variational, youves-you-governance, zeta-markets, zkera-finance, zkx

### Inferences
- Many well-known 2025-26 perp DEXs (Ostium, Extended, Pacifica, StandX, Variational, Reya, Hibachi, Nado, Bullet, Perpl, Ethereal, Vest) had no tradable token on the snapshot date. The sample is therefore tilted toward tokens that did launch. It cannot say anything about how these upcoming TGEs will price.
- CoinGecko's "Perpetuals" category is noisy. 30 in-window entries are low-liquidity launchpad-style tokens (12 of 22 with a computable day-1 FDV are under $1M, all under $23M; median $0.54M) with names such as "pumpperps", "hoodperp" and "perpex", which I could not verify as real perp DEXs. I kept them out of the main statistics and ran them as a sensitivity case.

### Gaps
- The classification is manual. It rests on DefiLlama categories and descriptions, CoinGecko categories and descriptions for 8 ambiguous coins (genius-3, bullbit, nereus-token, full-moon, nomina, omnipair, rails, sigmadotmoney), and protocol names. CoinGecko descriptions for 14 other low-FDV coins could not be fetched because of rate limits. Those were classified as micro or by name: hyperbot, desk, quanto, ascend-3, cyberdex, treble, nemesis-2, jarvis-2, throne-3, gtr-trade, alt, k9-2, rwax, nexus-trading-labs.
- Strike Finance (STRIKE) first priced on CoinGecko in Oct 2024 at a $2M FDV and peaked in Aug 2025 (27x). Whether the Oct 2024 print is the "real" TGE should be checked against news-reported launch details.

## Q2. Per-token dataset: FDV at TGE vs highest FDV reached after TGE

### Takeaway
The table below gives TGE FDV (first print, day-1, day-3 average) against peak FDV for all 67 core and borderline tokens. The 4 with insufficient data are kept in the table but left out of the statistics. "Peak" is the highest price at any time after TGE, not today's price. It is the validated CoinGecko intraday ATH, or the highest DefiLlama sample when the ATH failed validation. "Peak after d7" ignores the first 7 days, so listing-week wicks drop out.

### Cited Findings
- Per-token FDV table, computed from [DefiLlama coins chart API](https://coins.llama.fi/chart/coingecko:hyperliquid?start=1732866636&span=500&period=1h) prices and [CoinGecko markets API](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=hyperliquid,aster-2,lighter) ATH and supply. Each token links to its CoinGecko page. Multiples are relative to the day-1 price, which is the price 24h after the (cleaned) first print. "Low before peak" is the lowest sampled price between TGE and the peak, relative to the day-1 price. Supply is CoinGecko max_supply, falling back to total_supply; manual values are used for the CG-delisted VRTX (1B fixed supply per the [MEXC listing notice](https://www.mexc.com/support/articles/17827791511662)) and MKL (100M per [CryptoRank](https://cryptorank.io/ico/merkle-trade)).

| # | Token (CoinGecko id) | Class | TGE date | Supply used | FDV @first print | FDV @day-1 | FDV @day-3 avg | Peak FDV (date, source) | Peak / day-1 | Peak after d7 / day-1 | Days to peak | Low before peak vs day-1 | Current FDV | Current / day-1 | Data quality / flags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | FOX ([foxify](https://www.coingecko.com/en/coins/foxify)) | borderline | 2023-10-16 | 10.4M | $8.46M | $8.37M | $8.39M | $8.68M (2023-10-19, sampled) | 1.04x | 1.02x | 3 | -3% | $2.3M | 0.27x | sparse; frontend; CG ATH suspect_bad_tick |
| 2 | XEN ([xena-finance](https://www.coingecko.com/en/coins/xena-finance)) | core | 2023-10-24 | n/a | n/a | n/a | n/a | n/a (2023-11-09, sampled) | 2.75x | 2.75x | 16.6 | -23% | n/a | 0.00x | sparse; delisted_from_cg;current=last_available_sample; CG ATH no_cg_data |
| 3 | VRTX ([vertex-protocol](https://www.coingecko.com/en/coins/vertex-protocol)) | core | 2023-11-21 | 1B | $231M | $288M | $286M | $520M (2023-11-28, sampled) | 1.81x | 1.74x | 6.4 | -20% | $122K | 0.00x | ok; delisted_from_cg;current=last_available_sample; CG ATH no_cg_data |
| 4 | HOLD ([holdstation](https://www.coingecko.com/en/coins/holdstation)) | borderline | 2023-11-27 | 30M | $39M | $38.4M | $36.8M | $225M (2024-03-25, CG ATH) | 5.85x | 5.85x | 119.3 | -17% | $4.85M | 0.13x | ok; migration_to_holdstation-2; CG ATH ok |
| 5 | PIKO ([pinnako](https://www.coingecko.com/en/coins/pinnako)) | core | 2023-12-12 | n/a | n/a | n/a | n/a | n/a (2023-12-19, sampled) | 2.20x | 2.20x | 7.3 | -28% | n/a | 0.62x | ok; delisted_from_cg;current=last_available_sample; CG ATH no_cg_data |
| 6 | LVN ([levana-protocol](https://www.coingecko.com/en/coins/levana-protocol)) | core | 2023-12-19 | 1B | $894M | $531M | $423M | $895M (2023-12-19, CG ATH) | 1.69x | 0.50x | 0 | 68% | $485K | 0.00x | ok; CG ATH pre_first_print_ok |
| 7 | JUP ([jupiter-exchange-solana](https://www.coingecko.com/en/coins/jupiter-exchange-solana)) | borderline | 2024-01-31 | 10B | $7.4B | $5.93B | $6.1B | $17.5B (2024-03-31, sampled) | 2.95x | 2.95x | 60.3 | -23% | $2.76B | 0.47x | ok; supply_burn_2025;dropped_1_launch_placeholder_prints; CG ATH pre_listing_print_rejected |
| 8 | OX ([ox-fun](https://www.coingecko.com/en/coins/ox-fun)) | borderline | 2024-02-20 | 2.62B | $25.9M | $25.6M | $26.3M | $92.3M (2024-12-05, CG ATH) | 3.61x | 3.61x | 289.3 | -74% | $40.5K | 0.00x | ok; CG ATH ok |
| 9 | AEVO ([aevo-exchange](https://www.coingecko.com/en/coins/aevo-exchange)) | core | 2024-03-13 | 1B | $2.99B | $2.98B | $2.95B | $3.76B (2024-03-27, CG ATH) | 1.26x | 1.26x | 14.2 | -32% | $21.6M | 0.01x | ok; migration_from_RBN;dropped_1_samples_above_CG_ATH; CG ATH ok |
| 10 | VELAR ([velar](https://www.coingecko.com/en/coins/velar)) | borderline | 2024-04-03 | 1B | $263M | $247M | $251M | $380M (2024-04-08, CG ATH) | 1.54x | 1.19x | 4.8 | -31% | $181K | 0.00x | sparse; CG ATH ok |
| 11 | PRCL ([parcl](https://www.coingecko.com/en/coins/parcl)) | borderline | 2024-04-16 | 1B | $645M | $491M | $484M | $737M (2024-04-22, CG ATH) | 1.50x | 1.19x | 5.5 | -17% | $5.95M | 0.01x | ok; CG ATH ok |
| 12 | PINGU ([pingu-exchange](https://www.coingecko.com/en/coins/pingu-exchange)) | core | 2024-04-17 | n/a | n/a | n/a | n/a | n/a (2024-04-19, sampled) | 1.79x | 1.69x | 2 | -8% | n/a | 0.09x | sparse; delisted_from_cg;current=last_available_sample; CG ATH no_cg_data |
| 13 | EMDX ([emdx](https://www.coingecko.com/en/coins/emdx)) | core | 2024-04-25 | n/a | n/a | n/a | n/a | n/a (2024-07-13, sampled) | 1.19x | 1.19x | 78.9 | -42% | n/a | 0.51x | sparse; delisted_from_cg;current=last_available_sample; CG ATH no_cg_data |
| 14 | SLP ([slp](https://www.coingecko.com/en/coins/slp)) | core | 2024-04-25 | n/a | n/a | n/a | n/a | n/a (2025-08-25, sampled) | 2.48x | 2.48x | 486.9 | -44% | n/a | 2.48x | insufficient; delisted_from_cg;current=last_available_sample; CG ATH no_cg_data |
| 15 | DRIFT ([drift-protocol](https://www.coingecko.com/en/coins/drift-protocol)) | core | 2024-05-16 | 1B | $728M | $307M | $351M | $2.6B (2024-11-09, sampled) | 8.49x | 8.49x | 176.6 | -27% | $13.3M | 0.04x | ok; dropped_1_launch_placeholder_prints; CG ATH ok |
| 16 | JAV ([javsphere](https://www.coingecko.com/en/coins/javsphere)) | borderline | 2024-05-23 | 2B | $687M | $694M | $694M | $810M (2024-06-10, CG ATH) | 1.17x | 1.17x | 18.1 | -42% | $425K | 0.00x | sparse; CG ATH ok |
| 17 | AARK ([aark-digital](https://www.coingecko.com/en/coins/aark-digital)) | core | 2024-06-10 | 1B | $93.7M | $65.2M | $54.5M | $98.9M (2024-06-10, CG ATH) | 1.52x | 0.62x | 0 | 44% | $683K | 0.01x | sparse; CG ATH pre_first_print_ok |
| 18 | ZEX ([zeta](https://www.coingecko.com/en/coins/zeta)) | core | 2024-06-27 | 1e+03M | $133M | $157M | $157M | $308M (2024-06-27, CG ATH) | 1.96x | 1.31x | 0 | -16% | $888K | 0.01x | ok; new_Z_token_listed_no_price; CG ATH pre_first_print_ok |
| 19 | RAGE ([rage](https://www.coingecko.com/en/coins/rage)) | borderline | 2024-08-10 | n/a | n/a | n/a | n/a | n/a (2024-12-17, sampled) | n/a | n/a | 129.6 | n/a | n/a | n/a | insufficient; delisted_from_cg;no_hourly_launch_data;current=last_available_sample; CG ATH no_cg_data |
| 20 | ORDER ([orderly-network](https://www.coingecko.com/en/coins/orderly-network)) | core | 2024-08-26 | 1B | $182M | $194M | $176M | $492M (2025-10-06, CG ATH) | 2.54x | 2.54x | 405.6 | -65% | $37.3M | 0.19x | ok; infra;dropped_7_samples_above_CG_ATH; CG ATH ok |
| 21 | LOGX ([logx-2](https://www.coingecko.com/en/coins/logx-2)) | core | 2024-09-24 | 1B | $74.3M | $36.9M | $42.7M | $74.3M (2024-09-24, sampled) | 2.01x | 1.87x | 0 | 101% | $30.4K | 0.00x | ok; CG ATH suspect_bad_tick |
| 22 | ADX ([adrena](https://www.coingecko.com/en/coins/adrena)) | core | 2024-09-26 | 1B | $179M | $131M | $141M | $179M (2024-09-26, sampled) | 1.36x | 1.16x | 0 | 36% | $44K | 0.00x | ok; no_hourly_launch_data; CG ATH suspect_bad_tick |
| 23 | PEAR ([pear-protocol](https://www.coingecko.com/en/coins/pear-protocol)) | borderline | 2024-10-02 | 852M | $21.1M | $26.8M | $25.5M | $79M (2024-12-04, CG ATH) | 2.95x | 2.95x | 62.4 | -33% | $25.5M | 0.95x | ok; frontend;no_hourly_launch_data; CG ATH ok |
| 24 | STRIKE ([strike-2](https://www.coingecko.com/en/coins/strike-2)) | core | 2024-10-08 | 25M | $1.95M | $1.99M | $1.83M | $54.2M (2025-08-27, CG ATH) | 27.32x | 27.32x | 322.7 | -20% | $11.8M | 5.95x | ok; CG ATH ok |
| 25 | CYB ([cyberperp](https://www.coingecko.com/en/coins/cyberperp)) | core | 2024-10-08 | 10M | $7.93M | $7.97M | $7.84M | $35.6M (2024-12-03, CG ATH) | 4.47x | 4.47x | 56.3 | -11% | $64.2K | 0.01x | ok; CG ATH ok |
| 26 | STORM ([storm-trade](https://www.coingecko.com/en/coins/storm-trade)) | core | 2024-10-18 | 1B | $21.1M | $25.2M | $24.8M | $44.7M (2024-12-05, CG ATH) | 1.77x | 1.77x | 47.7 | -16% | $2.59M | 0.10x | ok; CG ATH ok |
| 27 | MKL ([merkle-trade](https://www.coingecko.com/en/coins/merkle-trade)) | core | 2024-10-22 | 100M | $9.83M | $9.43M | $9.51M | $39.4M (2024-11-12, sampled) | 4.18x | 4.18x | 21.4 | -20% | $6.32M | 0.67x | ok; delisted_from_cg;shut_down;current=last_available_sample; CG ATH no_cg_data |
| 28 | TANGO ([contango](https://www.coingecko.com/en/coins/contango)) | borderline | 2024-10-29 | 1B | $48.4M | $77.4M | $71.6M | $118M (2024-12-06, CG ATH) | 1.53x | 1.53x | 38.1 | -57% | $1.83M | 0.02x | ok; CG ATH ok |
| 29 | NRS ([nereus-token](https://www.coingecko.com/en/coins/nereus-token)) | core | 2024-11-14 | 1B | $208M | $144M | n/a | $687M (2024-11-19, CG ATH) | 4.77x | 2.29x | 4.8 | -9% | $72.6M | 0.50x | ok; zero_volume;no_hourly_launch_data; CG ATH ok |
| 30 | TYPUS ([typus](https://www.coingecko.com/en/coins/typus)) | borderline | 2024-11-22 | 1B | $59.9M | n/a | n/a | $100M (2024-11-29, CG ATH) | n/a | n/a | 7.4 | n/a | $342K | n/a | ok; no_hourly_launch_data; CG ATH ok |
| 31 | HYPE ([hyperliquid](https://www.coingecko.com/en/coins/hyperliquid)) | core | 2024-11-29 | 1B | $3.9B | $6.83B | $7.65B | $98B (2026-09-23, sampled) | 14.35x | 14.35x | 662.9 | -43% | $78.9B | 11.56x | ok; CG ATH ok |
| 32 | F ([synfutures](https://www.coingecko.com/en/coins/synfutures)) | core | 2024-12-06 | 10B | $775M | $885M | $863M | $1.07B (2024-12-06, sampled) | 1.21x | 0.92x | 0.5 | -13% | $29.8M | 0.03x | ok; CG ATH pre_listing_print_rejected |
| 33 | BLUE ([bluefin](https://www.coingecko.com/en/coins/bluefin)) | core | 2024-12-11 | 1B | $227M | $320M | $430M | $857M (2024-12-14, CG ATH) | 2.68x | 1.80x | 3.2 | -32% | $8.39M | 0.03x | ok; CG ATH ok |
| 34 | SYMM ([symmio](https://www.coingecko.com/en/coins/symmio)) | core | 2024-12-17 | 880M | $131M | $87.9M | $85.6M | $133M (2024-12-17, CG ATH) | 1.51x | 1.04x | 0 | 49% | $4.91M | 0.06x | ok; infra; CG ATH pre_first_print_ok |
| 35 | SRG ([surge-2](https://www.coingecko.com/en/coins/surge-2)) | core | 2025-01-10 | n/a | n/a | n/a | n/a | n/a (2025-01-12, sampled) | n/a | n/a | 1.8 | n/a | n/a | n/a | insufficient; delisted_from_cg;no_hourly_launch_data;current=last_available_sample; CG ATH no_cg_data |
| 36 | DRV ([derive](https://www.coingecko.com/en/coins/derive)) | borderline | 2025-01-15 | 1.5B | $317M | $263M | $273M | $854M (2026-10-09, CG ATH) | 3.24x | 3.24x | 632.4 | -91% | $531M | 2.02x | ok; rebrand_from_LYRA; CG ATH ok |
| 37 | FDX ([flex-2](https://www.coingecko.com/en/coins/flex-2)) | core | 2025-02-20 | 5M | $24.3M | $25.7M | $26M | $31.4M (2025-02-20, CG ATH) | 1.22x | 0.92x | 0.2 | -5% | $18.7K | 0.00x | ok; CG ATH ok |
| 38 | KILO ([kiloex](https://www.coingecko.com/en/coins/kiloex)) | core | 2025-03-27 | 1B | $149M | $85.9M | $94.9M | $165M (2025-03-27, CG ATH) | 1.92x | 0.71x | 0 | 73% | $2.97M | 0.03x | ok; CG ATH pre_first_print_ok |
| 39 | FAF ([flash-trade](https://www.coingecko.com/en/coins/flash-trade)) | core | 2025-04-16 | 1.2B | $3.62M | $3.14M | $3.45M | $22M (2025-09-23, CG ATH) | 6.99x | 6.99x | 159.9 | -56% | $92.1K | 0.03x | ok; no_hourly_launch_data; CG ATH ok |
| 40 | MYX ([myx-finance](https://www.coingecko.com/en/coins/myx-finance)) | core | 2025-05-06 | 1B | $103M | $97.8M | $95.5M | $19B (2025-09-11, sampled) | 195x | 195x | 127.6 | -50% | $59M | 0.60x | ok; CG ATH ok |
| 41 | QTO ([quanto](https://www.coingecko.com/en/coins/quanto)) | core | 2025-07-10 | 1B | $7.1M | n/a | $6.49M | $67M (2025-09-23, CG ATH) | n/a | n/a | 74.8 | n/a | $57.6K | n/a | sparse; CG ATH ok |
| 42 | DESK ([desk](https://www.coingecko.com/en/coins/desk)) | core | 2025-07-25 | 1B | $1.17M | $1.56M | $1.69M | $4.75M (2025-09-26, CG ATH) | 3.05x | 3.05x | 63.7 | -28% | $47.2K | 0.03x | sparse; CG ATH ok |
| 43 | AMPED ([amped-finance](https://www.coingecko.com/en/coins/amped-finance)) | core | 2025-07-25 | 100M | $4.06M | $3.07M | $3.04M | $4.23M (2025-07-25, CG ATH) | 1.38x | 0.68x | 0 | 32% | $64.4K | 0.02x | insufficient; CG ATH pre_first_print_ok |
| 44 | SPRK ([sparkdex](https://www.coingecko.com/en/coins/sparkdex)) | borderline | 2025-07-30 | 1B | $20.4M | $21.2M | $21.3M | $47.3M (2025-08-07, CG ATH) | 2.23x | 2.23x | 8.3 | -4% | $5.62M | 0.27x | ok; CG ATH ok |
| 45 | SUP ([superp](https://www.coingecko.com/en/coins/superp)) | core | 2025-08-05 | 1B | $47.2M | $42.7M | $38.1M | $161M (2025-10-04, CG ATH) | 3.77x | 3.77x | 59.6 | -27% | $253K | 0.01x | ok; CG ATH ok |
| 46 | FM ([full-moon](https://www.coingecko.com/en/coins/full-moon)) | core | 2025-08-07 | 20B | $490M | $609M | $659M | $846M (2025-08-09, CG ATH) | 1.39x | 0.83x | 1.8 | -20% | $35.7M | 0.06x | ok; no_hourly_launch_data; CG ATH ok |
| 47 | OVL ([overlay-protocol](https://www.coingecko.com/en/coins/overlay-protocol)) | core | 2025-08-14 | 100M | $29.7M | $22.6M | $20.5M | $31.3M (2025-09-24, sampled) | 1.39x | 1.39x | 41.6 | -54% | $537K | 0.02x | ok; dropped_1_launch_placeholder_prints; CG ATH pre_listing_print_rejected |
| 48 | BOT ([hyperbot](https://www.coingecko.com/en/coins/hyperbot)) | borderline | 2025-09-03 | 1B | $38.9M | $56.7M | $49.9M | $201M (2025-09-20, CG ATH) | 3.54x | 3.54x | 17.4 | -31% | $155K | 0.00x | sparse; frontend;dropped_3_samples_above_CG_ATH; CG ATH ok |
| 49 | TRADOOR ([tradoor](https://www.coingecko.com/en/coins/tradoor)) | core | 2025-09-04 | 60M | $43.1M | $101M | $93.1M | $608M (2026-04-22, CG ATH) | 5.99x | 5.99x | 229.9 | -59% | $36.9M | 0.36x | ok; CG ATH ok |
| 50 | AVNT ([avantis](https://www.coingecko.com/en/coins/avantis)) | core | 2025-09-09 | 1B | $231M | $369M | $302M | $2.64B (2025-09-21, CG ATH) | 7.16x | 7.16x | 12 | -44% | $108M | 0.29x | ok; rebranded_Veranta; CG ATH ok |
| 51 | ASTER ([aster-2](https://www.coingecko.com/en/coins/aster-2)) | core | 2025-09-17 | 8B | $1.71B | $4.4B | $5.92B | $19.3B (2025-09-24, CG ATH) | 4.38x | 4.34x | 6.6 | -77% | $5.66B | 1.29x | ok; rebrand_from_APX; CG ATH ok |
| 52 | ARA ([ara](https://www.coingecko.com/en/coins/ara)) | core | 2025-09-26 | 1B | $7.3M | $14.6M | $12.2M | $15.3M (2025-09-27, CG ATH) | 1.05x | 0.47x | 1 | -50% | $26.1K | 0.00x | sparse; CG ATH ok |
| 53 | VOOI ([vooi](https://www.coingecko.com/en/coins/vooi)) | borderline | 2025-12-18 | 1B | $160M | $47.1M | $52.3M | $176M (2025-12-18, CG ATH) | 3.73x | 0.68x | 0 | 240% | $7.62M | 0.16x | ok; aggregator; CG ATH pre_first_print_ok |
| 54 | LIT ([lighter](https://www.coingecko.com/en/coins/lighter)) | core | 2025-12-30 | 1B | $3.2B | $2.71B | $2.67B | $5.32B (2026-09-24, sampled) | 1.96x | 1.96x | 267.6 | -70% | $3.02B | 1.11x | ok; CG ATH pre_listing_print_rejected |
| 55 | RNGR ([ranger](https://www.coingecko.com/en/coins/ranger)) | borderline | 2026-01-10 | 4.69M | $3.44M | $3.2M | $3.09M | $3.77M (2026-01-10, CG ATH) | 1.18x | 1.12x | 0 | 7% | $0.0562 | 0.00x | sparse; aggregator; CG ATH pre_first_print_ok |
| 56 | ROLL ([roll-2](https://www.coingecko.com/en/coins/roll-2)) | core | 2026-01-16 | 1B | $78.5M | $87.5M | $101M | $184M (2026-01-19, CG ATH) | 2.10x | 1.76x | 2.6 | -10% | $62.4M | 0.71x | ok; CG ATH ok |
| 57 | INX ([infinex-2](https://www.coingecko.com/en/coins/infinex-2)) | borderline | 2026-01-30 | 10B | $215M | $215M | $164M | $334M (2026-01-30, CG ATH) | 1.56x | 0.92x | 0.5 | 0% | $48.5M | 0.23x | ok; CG ATH ok |
| 58 | RAILS ([rails](https://www.coingecko.com/en/coins/rails)) | borderline | 2026-02-04 | 65M | $25.8M | $20.4M | $21.2M | $32M (2026-02-09, sampled) | 1.57x | 1.26x | 4.7 | -21% | $1.64M | 0.08x | ok; infra;dropped_1_launch_placeholder_prints; CG ATH pre_listing_print_rejected |
| 59 | FT ([flying-tulip](https://www.coingecko.com/en/coins/flying-tulip)) | borderline | 2026-02-23 | 517M | $50.8M | $51.3M | $51.1M | $87.2M (2026-10-12, CG ATH) | 1.70x | 1.70x | 230.4 | -29% | $65.2M | 1.27x | ok; dropped_3_samples_above_CG_ATH; CG ATH ok |
| 60 | DIME ([paradex](https://www.coingecko.com/en/coins/paradex)) | core | 2026-03-05 | 1B | $72.2M | $44.6M | n/a | $102M (2026-10-11, CG ATH) | 2.29x | 2.29x | 219.7 | -83% | $45.8M | 1.03x | ok; no_hourly_launch_data; CG ATH ok |
| 61 | LV ([leverup](https://www.coingecko.com/en/coins/leverup)) | core | 2026-03-26 | 1B | $43.6M | $40.9M | $42.3M | $88.7M (2026-10-02, CG ATH) | 2.17x | 2.17x | 190 | -1% | $54M | 1.32x | ok; no_hourly_launch_data; CG ATH ok |
| 62 | BASED ([based-one](https://www.coingecko.com/en/coins/based-one)) | borderline | 2026-03-30 | 1B | $146M | $114M | $102M | $322M (2026-04-16, CG ATH) | 2.82x | 2.82x | 17.3 | -56% | $52.5M | 0.46x | ok; frontend; CG ATH ok |
| 63 | EDGE ([edgex](https://www.coingecko.com/en/coins/edgex)) | core | 2026-03-31 | 1B | $526M | $667M | $682M | $1.54B (2026-05-22, CG ATH) | 2.31x | 2.31x | 51.7 | -24% | $333M | 0.50x | ok; CG ATH ok |
| 64 | GENIUS ([genius-3](https://www.coingecko.com/en/coins/genius-3)) | borderline | 2026-04-13 | 1B | $473M | $521M | $552M | $953M (2026-04-18, CG ATH) | 1.83x | 1.39x | 4.8 | -13% | $309M | 0.59x | ok; frontend;dropped_1_launch_placeholder_prints; CG ATH ok |
| 65 | GRVT ([grvt](https://www.coingecko.com/en/coins/grvt)) | core | 2026-07-30 | 1B | $383M | $258M | $267M | $454M (2026-07-30, CG ATH) | 1.76x | 1.49x | 0 | 49% | $213M | 0.83x | ok; CG ATH ok |
| 66 | BUBI ([bullbit](https://www.coingecko.com/en/coins/bullbit)) | core | 2026-09-12 | 4B | $194M | $194M | $195M | $206M (2026-09-14, CG ATH) | 1.06x | 0.99x | 2.1 | -1% | $89.6M | 0.46x | ok; CG ATH ok |
| 67 | TREAD ([tread-fi](https://www.coingecko.com/en/coins/tread-fi)) | borderline | 2026-09-16 | 100M | $47.4M | $49.4M | $51.3M | $136M (2026-09-27, CG ATH) | 2.75x | 2.75x | 11.1 | -28% | $76.9M | 1.56x | ok; frontend; CG ATH ok |

- Price-level detail (USD) behind the table: first print (raw DefiLlama first record and the value used after cleaning), day-1, day-3 average, day 7, day 30, max sampled price in the first 7 days, max daily close in the first 7 days and after day 7, CoinGecko intraday ATH with validation status, the peak used, low before the peak, CoinGecko ATL and the current price — [DefiLlama coins chart API](https://coins.llama.fi/chart/coingecko:drift-protocol?start=1715853661&span=500&period=1h); [CoinGecko markets API](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=drift-protocol).

| Token | First print (raw -> used) | Day-1 | Day-3 avg | Day 7 | Day 30 | Max sampled <=d7 | Max daily close <=d7 | Max daily close >d7 (date) | CG intraday ATH (date, status) | Peak used | Low before peak | CG ATL (date) | Current (source) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FOX | 0.8167 -> 0.8167 | 0.8081 | 0.8099 | 0.7918 | 0.5321 | 0.8378 | 0.8192 | 0.8148 (2023-10-27) | 0.9208 (2026-09-20, suspect_bad_tick) | 0.8378 | 0.7863 | 3.693e-05 (2026-04-10) | 0.2215 (CG) |
| XEN | 0.03271 -> 0.03271 | 0.02787 | 0.02675 | 0.02755 | 0.05375 | 0.03279 | 0.03103 | 0.07484 (2023-11-10) | n/a (nan, no_cg_data) | 0.07667 | 0.02133 | n/a (nan) | 1.569e-05 (last DefiLlama sample 2026-01-22) |
| VRTX | 0.2311 -> 0.2311 | 0.2879 | 0.2862 | 0.4885 | 0.3349 | 0.5198 | 0.4681 | 0.4893 (2023-11-29) | n/a (nan, no_cg_data) | 0.5198 | 0.2299 | n/a (nan) | 0.0001219 (last DefiLlama sample 2026-02-27) |
| HOLD | 1.3 -> 1.3 | 1.28 | 1.228 | 1.35 | 2.57 | 1.46 | 1.28 | 7.28 (2024-04-01) | 7.49 (2024-03-25, ok) | 7.49 | 1.067 | 0.1573 (2026-10-27) | 0.1616 (CG) |
| PIKO | 0.06422 -> 0.06422 | 0.05211 | 0.05995 | 0.07921 | 0.03076 | 0.1079 | 0.09424 | 0.0827 (2023-12-19) | n/a (nan, no_cg_data) | 0.1144 | 0.03759 | n/a (nan) | 0.03232 (last DefiLlama sample 2024-02-19) |
| LVN | 0.8942 -> 0.8942 | 0.5308 | 0.4233 | 0.2393 | 0.25 | 0.8942 | 0.5177 | 0.2594 (2024-01-18) | 0.8947 (2023-12-19, pre_first_print_ok) | 0.8947 | 0.8942 | 5e-06 (2025-07-20) | 0.0004854 (CG) |
| JUP | 2 -> 0.7401 | 0.5929 | 0.6095 | 0.5833 | 0.6105 | 0.7401 | 0.6627 | 1.752 (2024-03-31) | 2 (2024-01-31, pre_listing_print_rejected) | 1.752 | 0.4582 | 0.1358 (2026-02-12) | 0.2763 (CG) |
| OX | 0.009895 -> 0.009895 | 0.009774 | 0.01007 | 0.01033 | 0.014 | 0.01229 | 0.01216 | 0.03306 (2024-12-04) | 0.03527 (2024-12-05, ok) | 0.03527 | 0.002576 | 1.267e-05 (2026-08-04) | 1.548e-05 (CG) |
| AEVO | 6.85 -> 2.99 | 2.98 | 2.951 | 2.18 | 2.289 | 3.28 | 3.23 | 3.7 (2024-03-27) | 3.76 (2024-03-27, ok) | 3.76 | 2.04 | 0.0165 (2026-06-25) | 0.02156 (CG) |
| VELAR | 0.2629 -> 0.2629 | 0.2472 | 0.2506 | 0.2943 | 0.1579 | 0.3803 | 0.3478 | 0.2732 (2024-04-11) | 0.3803 (2024-04-08, ok) | 0.3803 | 0.1716 | 6.254e-05 (2026-04-01) | 0.0001814 (CG) |
| PRCL | 0.6454 -> 0.6454 | 0.4908 | 0.4843 | 0.5771 | 0.3475 | 0.737 | 0.6764 | 0.5865 (2024-12-16) | 0.737 (2024-04-22, ok) | 0.737 | 0.4056 | 0.004339 (2026-08-18) | 0.005948 (CG) |
| PINGU | 0.1292 -> 0.1292 | 0.1052 | 0.1251 | 0.1114 | 0.08739 | 0.1885 | 0.1607 | 0.1775 (2024-04-29) | n/a (nan, no_cg_data) | 0.1885 | 0.09662 | n/a (nan) | 0.009886 (last DefiLlama sample 2025-12-06) |
| EMDX | 0.02597 -> 0.02597 | 0.02247 | 0.02244 | 0.01846 | n/a | 0.02615 | 0.02258 | 0.02682 (2024-07-13) | n/a (nan, no_cg_data) | 0.02682 | 0.0131 | n/a (nan) | 0.01142 (last DefiLlama sample 2025-08-24) |
| SLP | 1.49 -> 1.49 | 1.54 | 1.469 | 1.47 | n/a | 1.57 | 1.57 | 3.819 (2025-08-25) | n/a (nan, no_cg_data) | 3.819 | 0.855 | n/a (nan) | 3.819 (last DefiLlama sample 2025-08-25) |
| DRIFT | 0.1 -> 0.7282 | 0.3067 | 0.3512 | 0.5762 | 0.4439 | 0.7282 | 0.6129 | 1.78 (2024-11-09) | 2.6 (2024-11-08, ok) | 2.604 | 0.2229 | 0.01067 (2026-07-29) | 0.01331 (CG) |
| JAV | 0.3434 -> 0.3434 | 0.3468 | 0.3468 | 0.3082 | 0.07572 | 0.3562 | 0.3468 | 0.308 (2024-05-30) | 0.4051 (2024-06-10, ok) | 0.4051 | 0.2028 | 8.955e-05 (2026-06-26) | 0.0002127 (CG) |
| AARK | 0.0937 -> 0.0937 | 0.06522 | 0.0545 | 0.041 | 0.01771 | 0.0937 | 0.06943 | 0.03711 (2024-06-18) | 0.09894 (2024-06-10, pre_first_print_ok) | 0.09894 | 0.0937 | 0.0001419 (2026-08-21) | 0.0006829 (CG) |
| ZEX | 0.1327 -> 0.1327 | 0.1573 | 0.1569 | 0.06268 | 0.04894 | 0.3015 | 0.1878 | 0.2065 (2025-06-19) | 0.3078 (2024-06-27, pre_first_print_ok) | 0.3078 | 0.1327 | 0.0006554 (2026-09-28) | 0.0008877 (CG) |
| RAGE | 0.1742 -> 0.1742 | n/a | n/a | n/a | 0.0842 | 0.1756 | 0.1741 | 0.2255 (2024-12-17) | n/a (nan, no_cg_data) | 0.2255 | 0.04936 | n/a (nan) | 0.000211 (last DefiLlama sample 2025-10-22) |
| ORDER | 0.5375 -> 0.1819 | 0.1935 | 0.1758 | 0.1679 | 0.151 | 0.2367 | 0.2072 | 0.435 (2025-10-06) | 0.4915 (2025-10-06, ok) | 0.4915 | 0.06821 | 0.02689 (2026-08-05) | 0.03731 (CG) |
| LOGX | 0.07433 -> 0.07433 | 0.03694 | 0.04268 | 0.03622 | 0.02837 | 0.07433 | 0.05297 | 0.06902 (2025-01-06) | 2.97 (2026-04-18, suspect_bad_tick) | 0.07433 | 0.07433 | 1.978e-05 (2026-07-29) | 3.036e-05 (CG) |
| ADX | 0.1786 -> 0.1786 | 0.1309 | 0.1405 | n/a | 0.05599 | 0.1786 | 0.1309 | 0.1513 (2024-11-17) | 0.2349 (2024-11-08, suspect_bad_tick) | 0.1786 | 0.1786 | 4.323e-05 (2026-08-24) | 4.396e-05 (CG) |
| PEAR | 0.02472 -> 0.02472 | 0.03145 | 0.02992 | 0.02364 | 0.05927 | 0.0336 | 0.0336 | 0.08936 (2024-11-14) | 0.09269 (2024-12-04, ok) | 0.09269 | 0.02122 | 0.004972 (2025-05-01) | 0.02995 (CG) |
| STRIKE | 0.07798 -> 0.07798 | 0.07942 | 0.0733 | 0.07922 | 0.08064 | 0.08042 | 0.07612 | 2.01 (2025-08-28) | 2.17 (2025-08-27, ok) | 2.17 | 0.0638 | 0.06369 (2024-10-25) | 0.4728 (CG) |
| CYB | 0.7933 -> 0.7933 | 0.7967 | 0.7839 | 0.8614 | 0.7849 | 0.8633 | n/a | 2.96 (2024-12-06) | 3.56 (2024-12-03, ok) | 3.56 | 0.7071 | 0.002599 (2026-09-30) | 0.006415 (CG) |
| STORM | 0.0211 -> 0.0211 | 0.02522 | 0.02479 | 0.02416 | 0.03974 | 0.02816 | 0.02636 | 0.0407 (2024-12-05) | 0.04469 (2024-12-05, ok) | 0.04469 | 0.0211 | 0.002446 (2026-10-23) | 0.002588 (CG) |
| MKL | 0.09827 -> 0.09827 | 0.09433 | 0.09508 | 0.08024 | 0.2104 | 0.1008 | n/a | 0.3776 (2024-12-25) | n/a (nan, no_cg_data) | 0.3944 | 0.0752 | n/a (nan) | 0.06317 (last DefiLlama sample 2026-04-17) |
| TANGO | 0.04844 -> 0.04844 | 0.0774 | 0.07157 | 0.04271 | 0.05459 | 0.08409 | 0.04477 | 0.1157 (2024-12-07) | 0.1182 (2024-12-06, ok) | 0.1182 | 0.03356 | 0.0001506 (2026-04-22) | 0.001831 (CG) |
| NRS | 0.2077 -> 0.2077 | 0.1442 | n/a | n/a | n/a | 0.6546 | 0.3337 | 0.1456 (2025-09-15) | 0.6873 (2024-11-19, ok) | 0.6873 | 0.131 | 0.07183 (2026-07-20) | 0.07258 (CG) |
| TYPUS | 0.0599 -> 0.0599 | n/a | n/a | 0.08137 | 0.0449 | 0.08137 | 0.08137 | 0.08997 (2024-11-29) | 0.1003 (2024-11-29, ok) | 0.1003 | 0.0599 | 0.0001722 (2026-06-06) | 0.0003418 (CG) |
| HYPE | 3.903 -> 3.903 | 6.827 | 7.652 | 13.07 | 27.89 | 13.9 | 12.59 | 97.19 (2026-09-23) | 97.96 (2026-09-23, ok) | 97.96 | 3.903 | 3.81 (2024-11-29) | 78.93 (CG) |
| F | 0.07752 -> 0.07752 | 0.08853 | 0.08629 | 0.0818 | 0.05289 | 0.1069 | 0.1058 | 0.07539 (2024-12-13) | 0.1923 (2024-12-06, pre_listing_print_rejected) | 0.1069 | 0.07743 | 0.002601 (2026-08-19) | 0.002983 (CG) |
| BLUE | 0.2271 -> 0.2271 | 0.3199 | 0.43 | 0.5279 | 0.3896 | 0.8431 | 0.7947 | 0.5075 (2025-01-05) | 0.8567 (2024-12-14, ok) | 0.8567 | 0.216 | 0.007216 (2026-08-19) | 0.008389 (CG) |
| SYMM | 0.1484 -> 0.1484 | 0.09989 | 0.09724 | 0.08291 | 0.06581 | 0.1484 | 0.1054 | 0.09334 (2025-01-07) | 0.1508 (2024-12-17, pre_first_print_ok) | 0.1508 | 0.1484 | 0.005465 (2026-10-27) | 0.005582 (CG) |
| SRG | 0.04276 -> 0.04276 | n/a | n/a | 0.04334 | 0.01773 | 0.04624 | n/a | 0.0112 (2025-07-11) | n/a (nan, no_cg_data) | 0.04624 | 0.04108 | n/a (nan) | 0.00223 (last DefiLlama sample 2026-02-09) |
| DRV | 0.2113 -> 0.2113 | 0.1756 | 0.1822 | 0.1572 | 0.05959 | 0.2113 | 0.1844 | 0.5382 (2026-10-11) | 0.5693 (2026-10-09, ok) | 0.5693 | 0.01634 | 0.01244 (2025-04-07) | 0.3543 (CG) |
| FDX | 4.86 -> 4.86 | 5.14 | 5.208 | 4.3 | 2.94 | 5.74 | 5.69 | 4.71 (2025-03-02) | 6.29 (2025-02-20, ok) | 6.29 | 4.86 | 0.003353 (2026-06-26) | 0.003746 (CG) |
| KILO | 0.1486 -> 0.1486 | 0.08586 | 0.09486 | 0.05364 | 0.04061 | 0.1486 | 0.1227 | 0.05886 (2025-04-04) | 0.1648 (2025-03-27, pre_first_print_ok) | 0.1648 | 0.1486 | 0.002569 (2026-07-30) | 0.002968 (CG) |
| FAF | 0.003014 -> 0.003014 | 0.002619 | 0.002875 | 0.002356 | 0.001159 | 0.003014 | 0.002992 | 0.01198 (2025-09-21) | 0.01831 (2025-09-23, ok) | 0.01831 | 0.001151 | 7.677e-05 (2026-10-27) | 7.679e-05 (CG) |
| MYX | 0.1031 -> 0.1031 | 0.09785 | 0.09547 | 0.1005 | 0.07453 | 0.1075 | 0.1024 | 17.47 (2025-09-18) | 19.03 (2025-09-10, ok) | 19.03 | 0.0485 | 0.04701 (2025-06-19) | 0.05905 (CG) |
| QTO | 0.007099 -> 0.007099 | n/a | 0.006489 | 0.005465 | 0.01647 | 0.007992 | 0.005028 | 0.04026 (2025-09-25) | 0.06696 (2025-09-23, ok) | 0.06696 | 0.004477 | 4.311e-05 (2026-06-25) | 5.76e-05 (CG) |
| DESK | 0.001173 -> 0.001173 | 0.001558 | 0.001693 | 0.001724 | 0.001513 | 0.002687 | 0.002599 | 0.003489 (2025-10-06) | 0.004749 (2025-09-26, ok) | 0.004749 | 0.001116 | 4.72e-05 (2026-10-21) | 4.721e-05 (CG) |
| AMPED | 0.0406 -> 0.0406 | 0.03071 | 0.03043 | 0.02052 | 0.009392 | 0.04171 | n/a | 0.009279 (2025-08-23) | 0.04234 (2025-07-25, pre_first_print_ok) | 0.04234 | 0.0406 | 0.0002745 (2026-03-01) | 0.0006437 (CG) |
| SPRK | 0.02035 -> 0.02035 | 0.02118 | 0.02131 | 0.04182 | 0.03043 | 0.04001 | n/a | 0.04288 (2025-09-24) | 0.04726 (2025-08-07, ok) | 0.04726 | 0.02035 | 0.004474 (2026-08-19) | 0.005616 (CG) |
| SUP | 0.04723 -> 0.04723 | 0.04271 | 0.0381 | 0.0397 | 0.05246 | 0.04992 | 0.04987 | 0.1406 (2025-10-08) | 0.161 (2025-10-04, ok) | 0.161 | 0.0313 | 0.00019 (2026-10-24) | 0.0002532 (CG) |
| FM | 0.02448 -> 0.02448 | 0.03047 | 0.03297 | 0.02975 | 0.01995 | 0.0423 | 0.03849 | 0.0254 (2025-08-14) | 0.0423 (2025-08-09, ok) | 0.0423 | 0.02448 | 0.001609 (2026-08-30) | 0.001785 (CG) |
| OVL | 0.4898 -> 0.2966 | 0.2257 | 0.2046 | 0.1398 | 0.1459 | 0.2966 | 0.2305 | 0.313 (2025-09-24) | 0.7661 (2025-08-14, pre_listing_print_rejected) | 0.313 | 0.1033 | 0.005333 (2026-10-19) | 0.005374 (CG) |
| BOT | 9.32 -> 0.03886 | 0.05667 | 0.04991 | 0.0554 | 0.08932 | 0.05854 | 0.05854 | 0.1538 (2025-09-21) | 0.2005 (2025-09-20, ok) | 0.2005 | 0.03886 | 2.224e-05 (2026-07-17) | 0.0001552 (CG) |
| TRADOOR | 0.7185 -> 0.7185 | 1.69 | 1.552 | 2.06 | 3.154 | 2.51 | 2.15 | 8.424 (2026-04-21) | 10.13 (2026-04-22, ok) | 10.13 | 0.6965 | 0.3369 (2026-06-06) | 0.6143 (CG) |
| AVNT | 0.2306 -> 0.2306 | 0.3687 | 0.3024 | 0.9278 | 0.8229 | 1.4 | 1.25 | 2.36 (2025-09-21) | 2.64 (2025-09-21, ok) | 2.64 | 0.2082 | 0.07776 (2026-08-03) | 0.1082 (CG) |
| ASTER | 0.2134 -> 0.2134 | 0.5501 | 0.7401 | 2.292 | 1.074 | 2.409 | 1.96 | 2.31 (2025-09-25) | 2.41 (2025-09-24, ok) | 2.41 | 0.129 | 0.09971 (2025-09-17) | 0.7079 (CG) |
| ARA | 0.007296 -> 0.007296 | 0.01456 | 0.01216 | 0.006779 | 0.005405 | 0.01518 | 0.01301 | 0.006557 (2025-10-03) | 0.01526 (2025-09-27, ok) | 0.01526 | 0.007296 | 2.548e-05 (2026-10-18) | 2.614e-05 (CG) |
| VOOI | 0.1604 -> 0.1604 | 0.04714 | 0.05229 | 0.02856 | 0.01373 | 0.1604 | 0.06732 | 0.03049 (2025-12-28) | 0.1759 (2025-12-18, pre_first_print_ok) | 0.1759 | 0.1604 | 0.004288 (2026-03-09) | 0.007625 (CG) |
| LIT | 3.196 -> 3.196 | 2.714 | 2.665 | 3.027 | 1.859 | 3.196 | 3.003 | 5.315 (2026-09-24) | 7.86 (2025-12-30, pre_listing_print_rejected) | 5.315 | 0.8069 | 0.7794 (2026-03-31) | 3.02 (CG) |
| RNGR | 0.7336 -> 0.7336 | 0.6829 | 0.6588 | 0.6783 | 0.5305 | 0.7588 | 0.7588 | 0.7668 (2026-03-06) | 0.805 (2026-01-10, pre_first_print_ok) | 0.805 | 0.7336 | 9.991e-09 (2026-08-05) | 1.2e-08 (CG) |
| ROLL | 0.07846 -> 0.07846 | 0.08749 | 0.1011 | 0.1327 | 0.09423 | 0.1832 | 0.1698 | 0.1539 (2026-07-20) | 0.1837 (2026-01-19, ok) | 0.1837 | 0.07846 | 0.02111 (2026-05-16) | 0.06242 (CG) |
| INX | 0.02153 -> 0.02153 | 0.02145 | 0.01638 | 0.01152 | 0.01245 | 0.02283 | 0.02145 | 0.01972 (2026-04-13) | 0.03339 (2026-01-30, ok) | 0.03339 | 0.02153 | 0.003869 (2026-10-18) | 0.004847 (CG) |
| RAILS | 0.2326 -> 0.397 | 0.3141 | 0.3266 | 0.2832 | 0.2146 | 0.4927 | 0.42 | 0.3506 (2026-02-28) | 1.091 (2026-02-04, pre_listing_print_rejected) | 0.4927 | 0.2479 | 0.02022 (2026-09-03) | 0.02526 (CG) |
| FT | 0.2998 -> 0.09829 | 0.09923 | 0.09877 | 0.09821 | 0.09804 | 0.1011 | 0.1004 | 0.1627 (2026-10-12) | 0.1687 (2026-10-12, ok) | 0.1687 | 0.07018 | 0.067 (2026-04-22) | 0.1261 (CG) |
| DIME | 0.07219 -> 0.07219 | 0.04461 | n/a | n/a | 0.02666 | 0.07219 | n/a | 0.06868 (2026-10-10) | 0.1023 (2026-10-11, ok) | 0.1023 | 0.007638 | 0.007599 (2026-06-28) | 0.04583 (CG) |
| LV | 0.04357 -> 0.04357 | 0.04089 | 0.04233 | 0.04572 | 0.05423 | 0.04581 | 0.04581 | 0.0839 (2026-10-03) | 0.08874 (2026-10-02, ok) | 0.08874 | 0.04046 | 0.002463 (2026-04-28) | 0.05401 (CG) |
| BASED | 0.1456 -> 0.1456 | 0.1139 | 0.1022 | 0.06418 | 0.1288 | 0.1467 | 0.1187 | 0.1647 (2026-04-16) | 0.3216 (2026-04-16, ok) | 0.3216 | 0.05028 | 0.04144 (2026-10-14) | 0.05252 (CG) |
| EDGE | 0.5255 -> 0.5255 | 0.6672 | 0.6819 | 0.9529 | 1.215 | 1.161 | 1.134 | 1.513 (2026-05-21) | 1.54 (2026-05-22, ok) | 1.54 | 0.5103 | 0.2375 (2026-07-05) | 0.3332 (CG) |
| GENIUS | 0.1965 -> 0.4734 | 0.521 | 0.5516 | 0.5874 | 0.5406 | 0.9378 | 0.7478 | 0.7241 (2026-05-24) | 0.9533 (2026-04-18, ok) | 0.9533 | 0.4531 | 0.2715 (2026-10-15) | 0.3088 (CG) |
| GRVT | 0.3833 -> 0.3833 | 0.2579 | 0.267 | 0.2891 | 0.1796 | 0.3833 | 0.3004 | 0.329 (2026-08-11) | 0.4545 (2026-07-30, ok) | 0.4545 | 0.3833 | 0.1457 (2026-09-02) | 0.213 (CG) |
| BUBI | 0.04848 -> 0.04848 | 0.04842 | 0.04868 | 0.04772 | 0.03088 | 0.05129 | 0.04956 | 0.04746 (2026-09-22) | 0.05147 (2026-09-14, ok) | 0.05147 | 0.04784 | 0.02207 (2026-10-27) | 0.0224 (CG) |
| TREAD | 0.4739 -> 0.4739 | 0.4942 | 0.5127 | 0.5675 | 1.027 | 0.65 | 0.5904 | 1.203 (2026-10-03) | 1.36 (2026-09-27, ok) | 1.36 | 0.3571 | 0.3265 (2026-09-16) | 0.7686 (CG) |

- Unverified micro-cap "perp" tokens (sensitivity group only; median day-1 FDV $0.54M, max $23.3M) — [CoinGecko Perpetuals category](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&category=decentralized-perpetuals&per_page=250&page=1):

| Token | TGE | FDV @day-1 | Peak / day-1 | Peak after d7 / day-1 | Current / day-1 | DQ |
|---|---|---|---|---|---|---|
| CYDX ([cyberdex](https://www.coingecko.com/en/coins/cyberdex)) | 2024-07-24 | $23.3M | 26.78x | 26.78x | 0.08x | sparse |
| AI69X ([ai69x](https://www.coingecko.com/en/coins/ai69x)) | 2025-01-04 | $3.33M | 1.00x | 0.09x | 0.00x | sparse |
| TREB ([treble](https://www.coingecko.com/en/coins/treble)) | 2025-03-01 | n/a | n/a | n/a | n/a | ok |
| ZEUZ ([zeuz](https://www.coingecko.com/en/coins/zeuz)) | 2025-05-18 | $2.66M | 1.93x | 1.16x | 0.00x | sparse |
| HELIX ([helix-2](https://www.coingecko.com/en/coins/helix-2)) | 2025-08-12 | $529K | 1.28x | 0.74x | 0.03x | insufficient |
| JOJO ([jojo-3](https://www.coingecko.com/en/coins/jojo-3)) | 2025-08-12 | n/a | n/a | n/a | n/a | insufficient |
| PDGN ([degen-perp-dex](https://www.coingecko.com/en/coins/degen-perp-dex)) | 2025-10-14 | n/a | n/a | n/a | n/a | insufficient |
| PLUTO ([pluto-3](https://www.coingecko.com/en/coins/pluto-3)) | 2025-10-25 | $548K | 2.26x | 0.16x | 0.01x | insufficient |
| NEMESIS ([nemesis-2](https://www.coingecko.com/en/coins/nemesis-2)) | 2025-10-31 | $5.85M | 1.30x | 0.79x | 0.11x | ok |
| TROVE ([trove](https://www.coingecko.com/en/coins/trove)) | 2026-01-20 | $321K | 2.75x | 0.82x | 0.01x | insufficient |
| LIQUID ([meme-liquid](https://www.coingecko.com/en/coins/meme-liquid)) | 2026-02-08 | $1.28M | 1.16x | 0.12x | 0.01x | sparse |
| AMARA ([amara](https://www.coingecko.com/en/coins/amara)) | 2026-02-12 | $1M | 2.39x | 0.59x | 0.00x | insufficient |
| K9 ([k9-2](https://www.coingecko.com/en/coins/k9-2)) | 2026-03-30 | n/a | n/a | n/a | n/a | sparse |
| PERK ([perk](https://www.coingecko.com/en/coins/perk)) | 2026-03-30 | $492K | 1.58x | 0.16x | 0.01x | sparse |
| PUMPPERPS ([pumpperps](https://www.coingecko.com/en/coins/pumpperps)) | 2026-03-30 | $77.7K | 1.97x | 1.68x | 0.05x | insufficient |
| FFX ([flap-futures](https://www.coingecko.com/en/coins/flap-futures)) | 2026-04-01 | n/a | n/a | n/a | n/a | sparse |
| ASCEND ([ascend-3](https://www.coingecko.com/en/coins/ascend-3)) | 2026-04-29 | $1.57M | 4.49x | 4.49x | 3.55x | ok |
| CRACKROCK ([crackrock](https://www.coingecko.com/en/coins/crackrock)) | 2026-04-29 | $206K | 1.19x | 0.02x | 0.02x | insufficient |
| ALT ([alt](https://www.coingecko.com/en/coins/alt)) | 2026-05-17 | $6.49M | 1.47x | 0.47x | 0.03x | sparse |
| PARQ ([parquet](https://www.coingecko.com/en/coins/parquet)) | 2026-06-07 | $483K | 4.57x | 2.03x | 0.01x | ok |
| NEXUS ([nexus-trading-labs](https://www.coingecko.com/en/coins/nexus-trading-labs)) | 2026-06-10 | n/a | n/a | n/a | n/a | sparse |
| PERPAD ([perpad](https://www.coingecko.com/en/coins/perpad)) | 2026-06-10 | $500K | 1.17x | 0.45x | 0.01x | sparse |
| SKEW ([skew](https://www.coingecko.com/en/coins/skew)) | 2026-07-02 | n/a | n/a | n/a | n/a | insufficient |
| YARROW ([yarrow](https://www.coingecko.com/en/coins/yarrow)) | 2026-07-16 | $175K | 1.76x | 0.06x | 0.03x | ok |
| HPERP ([hoodperp](https://www.coingecko.com/en/coins/hoodperp)) | 2026-07-21 | $12K | 2.89x | 0.59x | 0.40x | ok |
| GTR ([gtr-trade](https://www.coingecko.com/en/coins/gtr-trade)) | 2026-07-25 | $1.85M | 1.94x | 1.06x | 0.10x | ok |
| THRONE ([throne-3](https://www.coingecko.com/en/coins/throne-3)) | 2026-09-17 | $2.75M | 1.24x | 0.65x | 0.17x | insufficient |
| PERPEX ([perpex-2](https://www.coingecko.com/en/coins/perpex-2)) | 2026-09-17 | n/a | n/a | n/a | n/a | insufficient |
| TALIS ([talis](https://www.coingecko.com/en/coins/talis)) | 2026-09-25 | $422K | 5.66x | 0.03x | 0.02x | insufficient |
| EMPIREX ([empirex](https://www.coingecko.com/en/coins/empirex)) | 2026-10-18 | $389K | 2.96x | 0.09x | 0.03x | insufficient |

### Inferences
- The largest post-TGE runs after day 7, relative to day-1 FDV, were MYX 195x; STRIKE 27.32x; HYPE 14.35x; DRIFT 8.49x; AVNT 7.16x; FAF 6.99x; TRADOOR 5.99x; HOLD 5.85x. MYX's 195x peak (Sept 2025) is one token, which is why every mean in this dataset sits far above its median.
- Tokens whose price never rose above their day-1 level after day 7: LVN, AARK, F, FDX, KILO, FM, ARA, VOOI, INX, BUBI. Tokens whose all-time peak stayed under 1.5x day-1 FDV: FOX, AEVO, EMDX, JAV, ADX, F, FDX, FM, OVL, ARA, RNGR, BUBI.

### Gaps
- FDV cannot be computed for CG-delisted XEN, PIKO, PINGU and EMDX, whose supply is not in the API; their price multiples are still computed. Typus (no hourly launch data) and Quanto (an hourly gap around day 1 and sparse daily data) have no price within 48h of TGE + 24h, so they have no day-1 price.
- Current prices for CG-delisted tokens (VRTX, MKL, XEN, PIKO, PINGU, EMDX) are the last DefiLlama sample, not a live price. Dates are in the CSV.

## Q3. Hypothesis test: how often did post-TGE peak FDV exceed TGE FDV, overall and by TGE-FDV bucket?

### Takeaway
Low-FDV launches (day-1 FDV under $250M, n=39) usually traded higher than their day-1 FDV at some later point. After day 7, 82% went higher, 62% reached 1.5x or more, and only 49% reached 2x or more (median 1.87x). Larger launches did no worse: the >$3B group (HYPE, JUP, ASTER) all reached at least 2x. The claim "low FDV mostly gets pushed higher" holds only if "higher" means any amount. For 2x or more it is a coin flip, and low FDV gives no edge over high FDV.

### Cited Findings
- Primary specification: core plus borderline tokens, TGE price = day-1 price, data quality not "insufficient", computed from [DefiLlama coins chart API](https://coins.llama.fi/chart/coingecko:myx-finance?start=1746500000&span=500&period=1h) and [CoinGecko markets API](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=myx-finance,avantis,aster-2,hyperliquid).
  - Peak at any time vs day-1 FDV: n=61: >1x 100% (61), >=1.5x 80% (49), >=2x 52% (32), >=3x 30% (18), >=5x 13% (8), >=10x 5% (3); median 2.10x, mean 6.35x. ">1x" is 100% by construction: the series includes the day-1 price itself, and later hourly prices almost always exceed it at some point.
  - Peak after day 7 vs day-1 FDV: n=61: >1x 84% (51), >=1.5x 61% (37), >=2x 46% (28), >=3x 26% (16), >=5x 13% (8), >=10x 5% (3); median 1.80x, mean 6.09x.
  - Peak of 00:00 UTC daily closes (all days) vs day-1 FDV: n=61: >1x 93% (57), >=1.5x 57% (35), >=2x 43% (26), >=3x 23% (14), >=5x 10% (6), >=10x 5% (3); median 1.70x, mean 5.64x.
  - Day-1 FDV under $250M, peak at any time: n=39: >1x 100% (39), >=1.5x 82% (32), >=2x 56% (22), >=3x 33% (13), >=5x 13% (5), >=10x 5% (2); median 2.17x, mean 8.17x.
  - Day-1 FDV under $250M, peak after day 7: n=39: >1x 82% (32), >=1.5x 62% (24), >=2x 49% (19), >=3x 28% (11), >=5x 13% (5), >=10x 5% (2); median 1.87x, mean 7.87x.
  - Day-1 FDV under $250M, daily-close peak: n=39: >1x 95% (37), >=1.5x 56% (22), >=2x 44% (17), >=3x 23% (9), >=5x 8% (3), >=10x 5% (2); median 1.64x, mean 7.22x.
  - Day-1 FDV under $1B, peak after day 7: n=52: >1x 81% (42), >=1.5x 58% (30), >=2x 44% (23), >=3x 27% (14), >=5x 13% (7), >=10x 4% (2); median 1.77x, mean 6.52x. Day-1 FDV of $1B or more, peak after day 7: n=5: >1x 100% (5), >=1.5x 80% (4), >=2x 60% (3), >=3x 40% (2), >=5x 20% (1), >=10x 20% (1); median 2.95x, mean 4.97x.
  - Day-1 FDV of $1B or more (TGE FDV -> peak FDV, multiple): LIT ($2.71B -> $5.32B, 1.96x), AEVO ($2.98B -> $3.76B, 1.26x), ASTER ($4.4B -> $19.3B, 4.38x), JUP ($5.93B -> $17.5B, 2.95x), HYPE ($6.83B -> $98B, 14.35x).
  - $250M-$1B bucket, peak-after-d7 multiples: GRVT (1.49x), DRV (3.24x), VRTX (1.74x), DRIFT (8.49x), BLUE (1.80x), AVNT (7.16x), PRCL (1.19x), GENIUS (1.39x), LVN (0.50x), FM (0.83x), EDGE (2.31x), JAV (1.17x), F (0.92x).
- Full bucket tables (TGE bucket by day-1 FDV), followed by days to peak, share peaking in the first 7 days, share below TGE FDV now and the Spearman results:

**Primary specification:** core+borderline, TGE price = day-1 close (24h after first print)

**peak_any_time: overall**
| group | n | gt1x | ge1.5x | ge2x | ge3x | ge5x | ge10x | median_mult | mean_mult |
|---|---|---|---|---|---|---|---|---|---|
| All | 61 | 100% (61) | 80% (49) | 52% (32) | 30% (18) | 13% (8) | 5% (3) | 2.1 | 6.35 |

**peak_any_time: by TGE-FDV bucket**
| group | n | gt1x | ge1.5x | ge2x | ge3x | ge5x | ge10x | median_mult | mean_mult |
|---|---|---|---|---|---|---|---|---|---|
| <$250M | 39 | 100% (39) | 82% (32) | 56% (22) | 33% (13) | 13% (5) | 5% (2) | 2.17 | 8.17 |
| $250M-$1B | 13 | 100% (13) | 77% (10) | 38% (5) | 23% (3) | 15% (2) | 0% (0) | 1.81 | 2.79 |
| $1B-$3B | 2 | 100% (2) | 50% (1) | 0% (0) | 0% (0) | 0% (0) | 0% (0) | 1.61 | 1.61 |
| >$3B | 3 | 100% (3) | 100% (3) | 100% (3) | 67% (2) | 33% (1) | 33% (1) | 4.38 | 7.23 |
| FDV unknown | 4 | 100% (4) | 75% (3) | 50% (2) | 0% (0) | 0% (0) | 0% (0) | 1.99 | 1.98 |

**peak_after_day7: overall**
| group | n | gt1x | ge1.5x | ge2x | ge3x | ge5x | ge10x | median_mult | mean_mult |
|---|---|---|---|---|---|---|---|---|---|
| All | 61 | 84% (51) | 61% (37) | 46% (28) | 26% (16) | 13% (8) | 5% (3) | 1.8 | 6.09 |

**peak_after_day7: by TGE-FDV bucket**
| group | n | gt1x | ge1.5x | ge2x | ge3x | ge5x | ge10x | median_mult | mean_mult |
|---|---|---|---|---|---|---|---|---|---|
| <$250M | 39 | 82% (32) | 62% (24) | 49% (19) | 28% (11) | 13% (5) | 5% (2) | 1.87 | 7.87 |
| $250M-$1B | 13 | 77% (10) | 46% (6) | 31% (4) | 23% (3) | 15% (2) | 0% (0) | 1.49 | 2.48 |
| $1B-$3B | 2 | 100% (2) | 50% (1) | 0% (0) | 0% (0) | 0% (0) | 0% (0) | 1.61 | 1.61 |
| >$3B | 3 | 100% (3) | 100% (3) | 100% (3) | 67% (2) | 33% (1) | 33% (1) | 4.34 | 7.22 |
| FDV unknown | 4 | 100% (4) | 75% (3) | 50% (2) | 0% (0) | 0% (0) | 0% (0) | 1.94 | 1.96 |

**peak_daily_close: overall**
| group | n | gt1x | ge1.5x | ge2x | ge3x | ge5x | ge10x | median_mult | mean_mult |
|---|---|---|---|---|---|---|---|---|---|
| All | 61 | 93% (57) | 57% (35) | 43% (26) | 23% (14) | 10% (6) | 5% (3) | 1.7 | 5.64 |

**peak_daily_close: by TGE-FDV bucket**
| group | n | gt1x | ge1.5x | ge2x | ge3x | ge5x | ge10x | median_mult | mean_mult |
|---|---|---|---|---|---|---|---|---|---|
| <$250M | 39 | 95% (37) | 56% (22) | 44% (17) | 23% (9) | 8% (3) | 5% (2) | 1.64 | 7.22 |
| $250M-$1B | 13 | 85% (11) | 46% (6) | 38% (5) | 23% (3) | 15% (2) | 0% (0) | 1.44 | 2.33 |
| $1B-$3B | 2 | 100% (2) | 50% (1) | 0% (0) | 0% (0) | 0% (0) | 0% (0) | 1.6 | 1.6 |
| >$3B | 3 | 100% (3) | 100% (3) | 100% (3) | 67% (2) | 33% (1) | 33% (1) | 4.2 | 7.13 |
| FDV unknown | 4 | 100% (4) | 75% (3) | 25% (1) | 0% (0) | 0% (0) | 0% (0) | 1.75 | 1.84 |

**Extra by bucket (days to peak, share with peak in first 7d, share below TGE FDV now)**
| bucket | n | median_days_to_peak | share_peak_first7d | share_below_tge_now | median_current_mult |
|---|---|---|---|---|---|
| $1B-$3B | 2 | 141 | 0 | 0.5 | 0.56 |
| $250M-$1B | 13 | 5.5 | 0.615 | 0.923 | 0.043 |
| <$250M | 39 | 17.3 | 0.436 | 0.872 | 0.103 |
| >$3B | 3 | 60.3 | 0.333 | 0.333 | 1.29 |
| FDV unknown | 6 | 12 | 0.167 | 1 | 0.301 |

Overall median days TGE->peak: 12.0; share peak in first 7d: 0.43; share below TGE FDV now: 0.85

**Spearman (log TGE FDV vs multiple)**

- vs peak multiple (any time): rho=-0.07 (p=0.5989, n=57)
- vs peak multiple after day 7: rho=-0.093 (p=0.4872, n=57)
- vs current multiple: rho=0.121 (p=0.3666, n=57)

- 2023-24 (n=32): peak rho=-0.229 (p=0.2531, n=27); peak>d7 rho=-0.247 (p=0.2135, n=27); current rho=-0.189 (p=0.3416, n=27); median peak 1.96x; median peak>d7 1.77x; share >=2x after d7 0.42; share below TGE now 0.94

- 2025 (n=18): peak rho=0.255 (p=0.3217, n=17); peak>d7 rho=0.216 (p=0.4079, n=17); current rho=0.696 (p=0.0029, n=17); median peak 3.24x; median peak>d7 3.05x; share >=2x after d7 0.59; share below TGE now 0.82

- 2026 (n=13): peak rho=0.121 (p=0.6977, n=13); peak>d7 rho=0.0 (p=1.0, n=13); current rho=-0.005 (p=0.9932, n=13); median peak 1.83x; median peak>d7 1.70x; share >=2x after d7 0.38; share below TGE now 0.69




### Inferences
- For the user's hypothesis on its own terms (max FDV at any point after TGE, excluding listing-week wicks): about 8 in 10 low-FDV launches traded above their day-1 FDV again, and about 6 in 10 reached 1.5x. Only about half doubled, and the median low-FDV token peaked at roughly 1.9x day-1 FDV.
- Launching at low FDV does not raise the odds of a big later peak compared with mid or high FDV launches. The $250M-$1B bucket was weaker (31% at 2x or more after d7), while the >$3B bucket (n=3) was strongest. So the evidence does not support "low FDV is the reason it goes higher". Peaks of 2x or more look idiosyncratic and regime-driven (MYX, STRIKE, HYPE, DRIFT, AVNT, ASTER).
- The higher-FDV buckets are tiny (n=2 for $1B-$3B, n=3 for >$3B), so their shares are anecdotes, not rates.

### Gaps
- Bucket assignment uses a constant supply. If tokens were burned (JUP: CoinGecko total_supply is 6.86B vs the 10B max_supply used here) or the supply cap is uncapped or stale, a token's FDV bucket could shift. The price multiples are unaffected.

## Q4. Timing, drawdowns and current status

### Takeaway
The median token peaked 12 days after TGE, and 43% (27/63) peaked within the first 7 days. The median token fell -23% below its day-1 price before reaching its peak. Today 85% (52/61) trade below their day-1 FDV (87% (34/39) of the under-$250M group).

### Cited Findings
- Median days from TGE to peak: 12 (under-$250M bucket: 17). Share with the peak in the first 7 days: 43% (27/63) (under-$250M: 44%) — [DefiLlama coins chart API](https://coins.llama.fi/chart/coingecko:lighter?start=1767085080&span=500&period=1h); [CoinGecko markets API](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=lighter).
- Median low before the peak relative to the day-1 price: -23%. Per-token values are in the table above and in the CSV columns `low_before_peak` and `drawdown_before_peak_vs_day1` — [DefiLlama coins chart API](https://coins.llama.fi/chart/coingecko:hyperliquid?start=1732866636&span=500&period=1h).
- Share currently below day-1 FDV: all tokens 85% (52/61); under-$250M 87% (34/39); $250M-$1B 92%; >$3B 33% (only JUP, at 0.47x) — [CoinGecko markets API](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=jupiter-exchange-solana,hyperliquid,aster-2).
- Tokens with under 180 days of history (less time to peak): GRVT (88d), BUBI (44d), TREAD (40d).

### Inferences
- The typical path is a peak within weeks, then a slow bleed. Holding from day 1 to today lost money in about 85% of cases even though roughly half doubled at some point. Whether anyone captured a peak depends on timing, not on the launch FDV.
- Peaks are front-loaded: about 4 in 10 occur in the listing week. This is why the "after day 7" measure matters for the hypothesis.

### Gaps
- Unlock schedules and emissions were not modelled. Current FDV with constant supply ignores supply growth from emissions, and only matters for the bucket labels.

## Q5. Rank correlation between TGE FDV and multiples, and the market-regime split

### Takeaway
There is no significant rank correlation between TGE FDV and peak multiple in the primary specification (Spearman rho = -0.07, p = 0.60, n = 57). The sign is mildly negative in 2023-24 and mildly positive in 2025, and neither is significant. Current multiple vs TGE FDV is positive and significant only for 2025 launches (rho = +0.70, p = 0.003): larger 2025 launches held up better.

### Cited Findings
- Spearman on log(day-1 FDV), permutation p-values (20,000 shuffles), core plus borderline: vs peak multiple rho = -0.07 (p = 0.60, n = 57); vs peak-after-d7 multiple rho = -0.093 (p = 0.49); vs current multiple rho = +0.121 (p = 0.37) — computed from [DefiLlama coins chart API](https://coins.llama.fi/chart/coingecko:aster-2?start=1758096000&span=500&period=1h) and [CoinGecko markets API](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=aster-2).
- By launch year (core plus borderline, day-1 basis):
  - 2023-24 (n=27 with FDV): peak rho = -0.229 (p = 0.25); current rho = -0.189 (p = 0.34); median peak 1.96x; 2x or more after d7: 42%; below TGE FDV now: 94%.
  - 2025 (n=17): peak rho = +0.255 (p = 0.32); current rho = +0.696 (p = 0.003); median peak 3.24x; 2x or more after d7: 59%; below TGE FDV now: 82%.
  - 2026 (n=13): peak rho = +0.121 (p = 0.70); current rho ≈ 0 (p = 0.99); median peak 1.83x; 2x or more after d7: 38%; below TGE FDV now: 69%.

  Source: [DefiLlama coins API](https://coins.llama.fi/prices/first/coingecko:myx-finance,coingecko:avantis,coingecko:aster-2).
- Including the micro-caps (n=80), the correlation of FDV with the after-d7 peak multiple turns positive (rho = +0.19, p = 0.11). Tiny launches did worse, not better — [CoinGecko Perpetuals category](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&category=decentralized-perpetuals&per_page=250&page=1).

### Inferences
- Market regime matters more than launch FDV. The 2025 cohort had the highest median peak (3.24x) and the most doublings (59%), with peaks clustered in Sept-Oct 2025 (MYX 2025-09-11, AVNT 2025-09-21, FAF and QTO 2025-09-23, ASTER 2025-09-24, SUP 2025-10-04, ORDER 2025-10-06). The 2023-24 cohort is almost entirely below TGE FDV today (94%).
- None of the specifications shows low TGE FDV predicting higher peak multiples at conventional significance.

### Gaps
- Sample sizes per year are small (13-27 with FDV), so these correlations have wide uncertainty. A rho of ±0.3 is not distinguishable from zero.

## Q6. Sensitivity: TGE price basis, borderline tokens, micro-caps, recency

### Takeaway
The conclusions hold across specifications. With TGE priced at the first print, the day-1 price or the day-3 average, and with or without borderline tokens, 42-48% of tokens reached 2x or more after day 7. The median peak-after-d7 multiple was 1.7-1.9x and 85-90% are below TGE FDV now. Adding micro-caps lowers the success rates (42% at 2x or more after d7; 42% for the under-$250M bucket).

### Cited Findings
- Sensitivity grid (shares with counts; rho and p-values as in Q5; "mature180" keeps tokens with at least 180 days since TGE) — computed from [DefiLlama coins chart API](https://coins.llama.fi/chart/coingecko:jupiter-exchange-solana?start=1706713320&span=500&period=1h) and [CoinGecko markets API](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=jupiter-exchange-solana):



| universe | tge_basis | n | any>=1.5x | any>=2x | after_d7>=1.5x | after_d7>=2x | dailyclose>=2x | median_any | median_after_d7 | <$250M after_d7>=2x | below_TGE_now | rho(FDV,peak) | p | rho(FDV,peak>d7) | p7 | mature180 n | mature180 after_d7>=2x |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| core+borderline | day1 | 63 | 80% (49) | 52% (32) | 61% (37) | 46% (28) | 43% (26) | 2.1 | 1.8 | 49% (19) | 85% | -0.07 | 0.599 | -0.093 | 0.487 | 60 | 47% |
| core+borderline | first | 63 | 65% (41) | 56% (35) | 60% (38) | 48% (30) | 44% (28) | 2.12 | 1.78 | 53% (23) | 87% | -0.191 | 0.152 | -0.213 | 0.104 | 60 | 48% |
| core+borderline | day3avg | 63 | 82% (49) | 48% (29) | 58% (35) | 43% (26) | 40% (24) | 1.99 | 1.73 | 49% (18) | 87% | -0.118 | 0.387 | -0.148 | 0.276 | 60 | 44% |
| core | day1 | 42 | 78% (32) | 54% (22) | 63% (26) | 46% (19) | 44% (18) | 2.1 | 1.87 | 50% (12) | 85% | -0.078 | 0.649 | -0.089 | 0.604 | 40 | 49% |
| core | first | 42 | 64% (27) | 57% (24) | 60% (25) | 48% (20) | 45% (19) | 2.18 | 1.87 | 54% (15) | 90% | -0.194 | 0.241 | -0.172 | 0.295 | 40 | 50% |
| core | day3avg | 42 | 80% (32) | 45% (18) | 60% (24) | 42% (17) | 40% (16) | 1.98 | 1.78 | 48% (11) | 90% | -0.14 | 0.415 | -0.181 | 0.293 | 40 | 45% |
| all_incl_micro | day1 | 80 | 77% (57) | 49% (36) | 54% (40) | 42% (31) | 39% (29) | 1.96 | 1.72 | 42% (22) | 86% | 0.034 | 0.784 | 0.194 | 0.108 | 70 | 45% |
| all_incl_micro | first | 80 | 61% (49) | 50% (40) | 52% (42) | 42% (34) | 41% (33) | 2 | 1.57 | 45% (27) | 89% | -0.04 | 0.732 | 0.124 | 0.281 | 70 | 46% |
| all_incl_micro | day3avg | 80 | 76% (57) | 47% (35) | 51% (38) | 39% (29) | 36% (27) | 1.97 | 1.52 | 40% (21) | 88% | -0.006 | 0.96 | 0.181 | 0.13 | 70 | 42% |


**core|day1: peak after day 7 by bucket
| group | n | gt1x | ge1.5x | ge2x | ge3x | ge5x | ge10x | median_mult | mean_mult |
|---|---|---|---|---|---|---|---|---|---|
| <$250M | 24 | 79% (19) | 62% (15) | 50% (12) | 33% (8) | 17% (4) | 8% (2) | 2.02 | 11.4 |
| $250M-$1B | 9 | 67% (6) | 56% (5) | 33% (3) | 22% (2) | 22% (2) | 0% (0) | 1.74 | 2.81 |
| $1B-$3B | 2 | 100% (2) | 50% (1) | 0% (0) | 0% (0) | 0% (0) | 0% (0) | 1.61 | 1.61 |
| >$3B | 2 | 100% (2) | 100% (2) | 100% (2) | 100% (2) | 50% (1) | 50% (1) | 9.35 | 9.35 |
| FDV unknown | 4 | 100% (4) | 75% (3) | 50% (2) | 0% (0) | 0% (0) | 0% (0) | 1.94 | 1.96 |


**core|day1: peak any time by bucket
| group | n | gt1x | ge1.5x | ge2x | ge3x | ge5x | ge10x | median_mult | mean_mult |
|---|---|---|---|---|---|---|---|---|---|
| <$250M | 24 | 100% (24) | 79% (19) | 58% (14) | 38% (9) | 17% (4) | 8% (2) | 2.13 | 11.7 |
| $250M-$1B | 9 | 100% (9) | 78% (7) | 44% (4) | 22% (2) | 22% (2) | 0% (0) | 1.81 | 3.17 |
| $1B-$3B | 2 | 100% (2) | 50% (1) | 0% (0) | 0% (0) | 0% (0) | 0% (0) | 1.61 | 1.61 |
| >$3B | 2 | 100% (2) | 100% (2) | 100% (2) | 100% (2) | 50% (1) | 50% (1) | 9.37 | 9.37 |
| FDV unknown | 4 | 100% (4) | 75% (3) | 50% (2) | 0% (0) | 0% (0) | 0% (0) | 1.99 | 1.98 |

Spearman by year: 2023-24: peak rho=-0.238 (p=0.3453, n=18), current rho=-0.125 (p=0.6167, n=18); 2025: peak rho=0.258 (p=0.3914, n=13), current rho=0.78 (p=0.0024, n=13); 2026: peak rho=-0.029 (p=1.0, n=6), current rho=-0.714 (p=0.1337, n=6)


**all_incl_micro|day1: peak after day 7 by bucket
| group | n | gt1x | ge1.5x | ge2x | ge3x | ge5x | ge10x | median_mult | mean_mult |
|---|---|---|---|---|---|---|---|---|---|
| <$250M | 52 | 71% (37) | 52% (27) | 42% (22) | 25% (13) | 12% (6) | 6% (3) | 1.61 | 6.64 |
| $250M-$1B | 13 | 77% (10) | 46% (6) | 31% (4) | 23% (3) | 15% (2) | 0% (0) | 1.49 | 2.48 |
| $1B-$3B | 2 | 100% (2) | 50% (1) | 0% (0) | 0% (0) | 0% (0) | 0% (0) | 1.61 | 1.61 |
| >$3B | 3 | 100% (3) | 100% (3) | 100% (3) | 67% (2) | 33% (1) | 33% (1) | 4.34 | 7.22 |
| FDV unknown | 4 | 100% (4) | 75% (3) | 50% (2) | 0% (0) | 0% (0) | 0% (0) | 1.94 | 1.96 |


**all_incl_micro|day1: peak any time by bucket
| group | n | gt1x | ge1.5x | ge2x | ge3x | ge5x | ge10x | median_mult | mean_mult |
|---|---|---|---|---|---|---|---|---|---|
| <$250M | 52 | 98% (51) | 77% (40) | 50% (26) | 31% (16) | 12% (6) | 6% (3) | 1.98 | 7.13 |
| $250M-$1B | 13 | 100% (13) | 77% (10) | 38% (5) | 23% (3) | 15% (2) | 0% (0) | 1.81 | 2.79 |
| $1B-$3B | 2 | 100% (2) | 50% (1) | 0% (0) | 0% (0) | 0% (0) | 0% (0) | 1.61 | 1.61 |
| >$3B | 3 | 100% (3) | 100% (3) | 100% (3) | 67% (2) | 33% (1) | 33% (1) | 4.38 | 7.23 |
| FDV unknown | 4 | 100% (4) | 75% (3) | 50% (2) | 0% (0) | 0% (0) | 0% (0) | 1.99 | 1.98 |

Spearman by year: 2023-24: peak rho=-0.288 (p=0.1368, n=28), current rho=-0.218 (p=0.2645, n=28); 2025: peak rho=0.374 (p=0.1075, n=20), current rho=0.66 (p=0.0019, n=20); 2026: peak rho=-0.034 (p=0.8787, n=22), current rho=0.517 (p=0.0163, n=22)


**core+borderline|first: peak after day 7 by bucket
| group | n | gt1x | ge1.5x | ge2x | ge3x | ge5x | ge10x | median_mult | mean_mult |
|---|---|---|---|---|---|---|---|---|---|
| <$250M | 43 | 77% (33) | 65% (28) | 53% (23) | 33% (14) | 19% (8) | 9% (4) | 2.12 | 7.69 |
| $250M-$1B | 11 | 82% (9) | 36% (4) | 27% (3) | 9% (1) | 0% (0) | 0% (0) | 1.12 | 1.58 |
| $1B-$3B | 2 | 100% (2) | 50% (1) | 50% (1) | 50% (1) | 50% (1) | 50% (1) | 6.23 | 6.23 |
| >$3B | 3 | 100% (3) | 100% (3) | 67% (2) | 33% (1) | 33% (1) | 33% (1) | 2.37 | 9.71 |
| FDV unknown | 4 | 100% (4) | 50% (2) | 25% (1) | 0% (0) | 0% (0) | 0% (0) | 1.58 | 1.63 |


**core+borderline|first: peak any time by bucket
| group | n | gt1x | ge1.5x | ge2x | ge3x | ge5x | ge10x | median_mult | mean_mult |
|---|---|---|---|---|---|---|---|---|---|
| <$250M | 43 | 95% (41) | 70% (30) | 63% (27) | 37% (16) | 19% (8) | 9% (4) | 2.32 | 7.91 |
| $250M-$1B | 11 | 100% (11) | 45% (5) | 36% (4) | 9% (1) | 0% (0) | 0% (0) | 1.45 | 1.84 |
| $1B-$3B | 2 | 100% (2) | 50% (1) | 50% (1) | 50% (1) | 50% (1) | 50% (1) | 6.27 | 6.27 |
| >$3B | 3 | 100% (3) | 100% (3) | 67% (2) | 33% (1) | 33% (1) | 33% (1) | 2.37 | 9.71 |
| FDV unknown | 4 | 100% (4) | 50% (2) | 25% (1) | 0% (0) | 0% (0) | 0% (0) | 1.62 | 1.65 |

Spearman by year: 2023-24: peak rho=-0.259 (p=0.1864, n=28), current rho=-0.209 (p=0.2879, n=28); 2025: peak rho=-0.077 (p=0.7634, n=18), current rho=0.631 (p=0.0072, n=18); 2026: peak rho=0.203 (p=0.5004, n=13), current rho=0.016 (p=0.9645, n=13)


**core+borderline|day3avg: peak after day 7 by bucket
| group | n | gt1x | ge1.5x | ge2x | ge3x | ge5x | ge10x | median_mult | mean_mult |
|---|---|---|---|---|---|---|---|---|---|
| <$250M | 37 | 84% (31) | 65% (24) | 49% (18) | 35% (13) | 16% (6) | 8% (3) | 1.8 | 8.65 |
| $250M-$1B | 14 | 79% (11) | 36% (5) | 29% (4) | 21% (3) | 14% (2) | 0% (0) | 1.33 | 2.38 |
| $1B-$3B | 2 | 100% (2) | 50% (1) | 0% (0) | 0% (0) | 0% (0) | 0% (0) | 1.63 | 1.63 |
| >$3B | 3 | 100% (3) | 100% (3) | 100% (3) | 67% (2) | 33% (1) | 33% (1) | 3.23 | 6.3 |
| FDV unknown | 4 | 100% (4) | 50% (2) | 25% (1) | 0% (0) | 0% (0) | 0% (0) | 1.66 | 1.85 |


**core+borderline|day3avg: peak any time by bucket
| group | n | gt1x | ge1.5x | ge2x | ge3x | ge5x | ge10x | median_mult | mean_mult |
|---|---|---|---|---|---|---|---|---|---|
| <$250M | 37 | 100% (37) | 84% (31) | 54% (20) | 38% (14) | 16% (6) | 8% (3) | 2.1 | 8.89 |
| $250M-$1B | 14 | 100% (14) | 79% (11) | 36% (5) | 21% (3) | 14% (2) | 0% (0) | 1.77 | 2.69 |
| $1B-$3B | 2 | 100% (2) | 50% (1) | 0% (0) | 0% (0) | 0% (0) | 0% (0) | 1.63 | 1.63 |
| >$3B | 3 | 100% (3) | 100% (3) | 100% (3) | 67% (2) | 33% (1) | 33% (1) | 3.26 | 6.31 |
| FDV unknown | 4 | 100% (4) | 75% (3) | 25% (1) | 0% (0) | 0% (0) | 0% (0) | 1.71 | 1.87 |

Spearman by year: 2023-24: peak rho=-0.238 (p=0.2331, n=26), current rho=-0.208 (p=0.3045, n=26); 2025: peak rho=0.034 (p=0.894, n=18), current rho=0.701 (p=0.0014, n=18); 2026: peak rho=0.196 (p=0.5416, n=12), current rho=0.063 (p=0.8518, n=12)


### Inferences
- The "any time" measure depends most on the TGE basis. On a first-print basis, only 65% of tokens reached 1.5x or more at any time, versus 80% on a day-1 basis. Listing prints are often above the day-1 price, so measuring from the first print makes later peaks look smaller. The after-day-7 shares barely move (58-61% at 1.5x or more).
- Recency is not driving the result. Only 3 main-universe tokens have under 180 days of history, and the mature subset gives the same 2x-or-more share after d7 (44-50%).

### Gaps
- Exchange klines (Binance, Bybit, OKX, Gate) for launch-day intraday highs were not pulled, to save API budget. Listing-day wicks rely on CoinGecko's intraday ATH and DefiLlama hourly samples.

## Q7. Methodology, reproducibility, data quality and caveats

### Takeaway
A single rule set was applied to every token: CoinGecko-sourced DefiLlama prices, an explicit cleaning pass for placeholder and bad-tick prints, and constant-supply FDV. The main risks are placeholder prints before listing, rejected CoinGecko ATHs (LIT is the most consequential), constant-supply FDV, and sparse histories for delisted small caps. All are flagged per token in the CSV.

### Cited Findings
- Price data: `coins.llama.fi/prices/first` gives the first record. `coins.llama.fi/chart` gives hourly data (span ≤ 500 per call) for 31 days after the first print, daily 00:00 UTC snapshots from the first midnight to 2026-10-27, and hourly data ±36h around the CoinGecko ATH date. 632 cached files, no request errors — [DefiLlama first price](https://coins.llama.fi/prices/first/coingecko:hyperliquid); [DefiLlama chart](https://coins.llama.fi/chart/coingecko:hyperliquid?start=1732866636&span=72&period=1h).
- Market data: one `/coins/markets?ids=...` call (150 ids) for current price, intraday ATH/ATL with dates, max/total supply and FDV. CoinGecko's own FDV uses total supply (e.g. HYPE FDV $75.4B = $78.93 × 955.3M total supply), whereas this dataset uses max supply when available — [CoinGecko markets API](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=hyperliquid).
- Definitions:
  - TGE date = timestamp of the first price that survives cleaning.
  - Day-1 price = hourly sample nearest TGE + 24h (±3h), falling back to the nearest daily close.
  - Day-3 average = mean of hourly samples over the first 72h.
  - Day 7 and day 30 = nearest samples.
  - Peak = max(validated CoinGecko intraday ATH, all cleaned samples).
  - Peak after d7 = the same, restricted to after TGE + 7 days.
  - Daily-close peak = max of 00:00 UTC snapshots.
  - Supply = max_supply, else total_supply. total_supply is used when max_supply is more than 3x total_supply (Tradoor: 8B max vs 60M total).
  - Multiples = price ratios at constant supply.

  Source: [DefiLlama chart](https://coins.llama.fi/chart/coingecko:tradoor?start=1756944000&span=500&period=1h); [CoinGecko markets API](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=tradoor).
- Cleaning rules:
  - (R1) A CoinGecko ATH more than 1.5x the highest DefiLlama sample within ±36h is rejected as a bad tick or pre-listing print.
  - (R2) If the ATH is accepted, samples above 1.05x the CoinGecko ATH are dropped as prices CoinGecko itself has since cleaned.
  - (R3) The first print is dropped if it is more than 1.5x the max, or less than 1/1.5 of the min, of the next 6 samples (iterated).

  Effects: JUP's $2.00 first print (next hour $0.74) was dropped. CoinGecko still reports $2.00 as JUP's ATH; it was rejected, so JUP's peak becomes $1.75 (2024-03-31). Also dropped: AEVO's $6.85 first print (next hour $2.99; CoinGecko ATH $3.76), DRIFT's $0.10 placeholder (next hour $0.73), ORDER's 7 prints at about $0.54 the day before trading began at about $0.18 (TGE date moves to 2024-08-26), Hyperbot's $9.32 prints (CoinGecko ATH $0.20), and FT's $0.30 print (CoinGecko ATH $0.169) — [DefiLlama chart JUP](https://coins.llama.fi/chart/coingecko:jupiter-exchange-solana?start=1706713320&span=8&period=1h); [DefiLlama chart AEVO](https://coins.llama.fi/chart/coingecko:aevo-exchange?start=1710321270&span=8&period=1h).
- Rejected CoinGecko ATHs:
  - LIT: $7.86 on its TGE day vs ≤ about $3.2 in samples. If accepted, LIT's peak would be 2.9x day-1 instead of 1.96x.
  - SynFutures F: $0.192 vs $0.107.
  - Overlay: $0.766.
  - Rails.
  - LogX: $2.97, 62,000x the nearby samples.
  - Adrena: $0.235, 1.55x the samples (a borderline call).
  - Foxify: $0.92 (Sep 2026).

  Source: [CoinGecko markets API](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=lighter,synfutures,overlay-protocol,logx-2,adrena,foxify).
- Data-quality flags. "Insufficient" (fewer than 30 daily points; excluded from statistics): slp, rage, surge-2, amped-finance. "Sparse" means daily coverage under 50% of days, common for small caps whose peaks still rely on the CoinGecko ATH. "No hourly launch data" applies to ADX, PEAR, FAF, LV, TYPUS, DIME, NRS and FM, where the day-1 price falls back to the daily close. FDV is unknown for xena-finance, pinnako, pingu-exchange, emdx, typus, quanto — [DefiLlama chart](https://coins.llama.fi/chart/coingecko:slp?start=1714000000&span=500&period=1d).
- Reproducibility: scripts are in `/tmp/claude-0/-home-user-test-claude/2ad751b0-58d6-5348-a96a-1b74151bb386/scratchpad/quant_scripts/` (discover, first_prices, cg_markets_ids, fetch_history, classify, compute, stats, make_outputs). Raw downloads are in `/tmp/claude-0/-home-user-test-claude/2ad751b0-58d6-5348-a96a-1b74151bb386/scratchpad/quant_raw/`. All Python was run with `-I` — [DefiLlama coins API](https://coins.llama.fi/prices/first/coingecko:hyperliquid).

### Inferences
- The cleaning rules mostly shrink "any time" peaks for tokens whose CoinGecko or DefiLlama history begins with placeholder prices. Without them, JUP, AEVO, ORDER, Hyperbot and FT would show artificial launch peaks and inflated first-print FDVs. These are exactly the tokens where news-reported "opening FDV" figures will disagree with this dataset.
- Hourly sampling understates true intraday highs. The validated CoinGecko ATH partly corrects this, but tokens whose ATH was rejected (LIT, F, ADX) may have higher true intraday peaks than shown.

### Gaps
- No historical circulating or total supply series was used. FDV is price × current max supply, so bucket labels for tokens with burns or migrations are approximate (JUP, HYPE, HOLD, ASTER, DRV, AEVO).
- DefiLlama's first record is a proxy for TGE. A CoinGecko listing that lagged on-chain trading (e.g. DEX-only launches) shifts the TGE date and price. Other researchers' news-reported launch details should be used to reconcile individual tokens.
- 14 small-cap classifications rest on names or CoinGecko categories rather than verified descriptions, because CoinGecko rate limits blocked those calls.
