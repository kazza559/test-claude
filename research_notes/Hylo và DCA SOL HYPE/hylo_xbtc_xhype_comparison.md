# Hylo xBTC and xHYPE vs xSOL: what they are, parameters, performance, risks and practicalities (as of 30 Sep 2026)

*Snapshot conventions. "On-chain snapshot" means the researcher decoded Hylo's live Solana program accounts on 2026-09-30 at 10:29 UTC (slot 451,937,889, Solana epoch 1046). The account layouts come from Hylo's open-source SDK/IDL ([hylo-so/sdk, commit 1b1f90d, 14 Sep 2026](https://github.com/hylo-so/sdk), [exchange IDL v2.0.5](https://github.com/hylo-so/sdk/blob/main/hylo-idl/idls/hylo_exchange.json)). Accounts read: [Hylo SOL-pool state 9cd2sA…](https://solscan.io/account/9cd2sAfbBvKs4SX9YKo4dcjwP3TgTVQ8dT5koshGcDND), [BTC exo pair 8mgw2T…](https://solscan.io/account/8mgw2TsNxTMndWPyswLELw3V2tPrPvtqS7Ex9RyiGhML), [HYPE exo pair 42GzNW…](https://solscan.io/account/42GzNWvZ1H1hwXaBZ8mbeVZaSEgh6zMm8BABdS3v1BEB), [USDC pair CMNPAC…](https://solscan.io/account/CMNPACEDebyvNJDgBxRc5fbScF8kmx52ZPBY4Cu4wuwS), plus the vaults, mints and Pyth price accounts. Market data (Jupiter, GeckoTerminal, CoinGecko, DefiLlama) was pulled between 10:19 and 10:31 UTC on 30 Sep 2026. X/Twitter post times were decoded from the status IDs, because x.com pages returned HTTP 402 and could not be read directly. Anything I could not verify is marked as such.*

## 1. What are xBTC and xHYPE, when and where did they launch, how are they structured, and what backs them?

### Takeaway
Both products exist and are live on **Solana only**. They are "xAssets" of Hylo V2. **xBTC** is backed by **Coinbase cbBTC**; its mint was deployed on 13 Jul 2026 and it opened publicly on 20 Jul 2026. **xHYPE** is backed by **plain Wormhole-NTT-bridged HYPE on Solana**, not an LST such as kHYPE or stHYPE; it launched on 17 Aug 2026. Each product has its own isolated collateral pool. Inside each pool sits a virtual stablecoin tranche (vUSD, which is not a token) with its own CR, zones, fees, borrow-rate curve and $3M market-cap cap. All pools share one hyUSD stablecoin, one USDC rebalancing pool and **one Earn Pool (eHYUSD, formerly sHYUSD)**, which is the first-loss backstop for every pool.

### Cited Findings
**Launch timing and chain**
- Hylo's docs list three live leveraged tokens: "xSOL, xBTC, xHYPE, and soon more. Hold a token, get 3x upside without margin calls". The docs also say all products are Solana-native. — [Hylo docs: Introduction](https://docs.hylo.so/introduction); [Leveraged Tokens (xAssets)](https://docs.hylo.so/product-guide/xassets)
- The V2 timeline has four steps:
  - Pine Analytics reports a V2 beta in "late March" 2026 at v2.hylo.so/early-access, with "xBTC launch planned for Q2 2026". — [Pine Analytics, Hylo Q1 2026 overview (15 Apr 2026)](https://pineanalytics.substack.com/p/hylo-quarterly-operations-overview)
  - KuCoin reported the V2 "xAsset Engine" launch on 17 Jun 2026. — [KuCoin News, 17 Jun 2026](https://www.kucoin.com/news/flash/hylo-launches-v2-expands-on-chain-leverage-to-stocks-and-multi-asset-collateral); [CryptoBriefing, 17 Jun 2026](https://cryptobriefing.com/hylo-v2-leveraged-equities-solana/)
  - Solana's June roundup says Hylo "shipped V2 with its xAsset Engine, expanding from a single live xAsset to a suite of leveraged instruments". — [Solana Ecosystem Roundup: June 2026](https://solana.com/news/solana-ecosystem-roundup-june-2026)
  - Accretion audited "Hylo v2, Exchange, Earn Pool & Router" in July 2026. — [Hylo docs: Audits](https://docs.hylo.so/security/audits)
- **xBTC launch.** Jupiter records the xBTC mint (2zCo6bUowJMvr89ajxuWsPadAqJ2F9akCkxumNsSdgsL, 6 decimals, name "Hylo Leveraged BTC") as created on 2026-07-13 19:20 UTC. Its first DEX pool was created on 2026-07-20 20:53 UTC. — [Jupiter token API (xBTC)](https://lite-api.jup.ag/tokens/v2/search?query=2zCo6bUowJMvr89ajxuWsPadAqJ2F9akCkxumNsSdgsL)
- **Pine Analytics on the xBTC launch** (post dated 20 Jul 2026 22:52 UTC; text read only from a search excerpt):
  - "the mint was deployed on July 13, the market opened to the public on July 20 — supply went from zero to roughly 24.8K xBTC (~$29K at a $1.17 NAV) in about seven hours"
  - The post describes xBTC as "2x–4x long BTC (currently ~2.7x) with no perps, no funding rates, and no liquidation price".
  - [Pine Analytics on X](https://x.com/PineAnalytics/status/2079338696726229180)
- Foresight/Bitget reported the xBTC listing on 21 Jul 2026 ("3x exposure to Bitcoin"). — [Bitget News](https://www.bitget.com/news/detail/12560605522633)
- On 29 Jul 2026 Hylo polled "$xBTC $xSOL Which xAsset should come next?". — [Hylo on X](https://x.com/hylo_so/status/2082507008503071171)
- **xHYPE launch.** Jupiter records the xHYPE mint (7ga6rtE9qSb3wdEiDCpTu2kHqoGVfT52jD8ign1rYTvx, 6 decimals, name "Hylo Leveraged HYPE") as created on 2026-08-17 16:38 UTC. Its first DEX pool was created on 2026-08-17 20:08 UTC. — [Jupiter token API (xHYPE)](https://lite-api.jup.ag/tokens/v2/search?query=7ga6rtE9qSb3wdEiDCpTu2kHqoGVfT52jD8ign1rYTvx)
- Coverage of the xHYPE launch:
  - An analyst post on 17 Aug 2026 (22:15 UTC) said "Hylo launched 3x xHYPE leverage". KuCoin republished it on 18 Aug 2026 with a note on "zero mint fees". — [Joshuwa Roomsburg on X](https://x.com/Joshuwa/status/2089476194789941491); [KuCoin](https://www.kucoin.com/news/insight/HYPE/6a83b37fec098c000710d543)
  - Hylo's own posts on 18 Aug ("The Home of 3x Leveraged Tokens across global markets") and 19 Aug ("When $HYPE moves, $xHYPE moves 3x harder."). — [Hylo X, 18 Aug](https://x.com/hylo_so/status/2089674156275085381); [Hylo X, 19 Aug](https://x.com/hylo_so/status/2090054568054792508)
- **The mints are Hylo-program-controlled.** The researcher derived the "exo_levercoin" PDA of the Hylo exchange program (HYEXCHtHkBagdStcJCp3xbbb9B7sdMdWXFNj6mdsG4hn) for each collateral mint. For cbBTC it equals the xBTC mint. For Wormhole-HYPE it equals the xHYPE mint. — [SDK tokens.rs](https://github.com/hylo-so/sdk/blob/main/hylo-idl/src/tokens.rs); [SDK pda.rs](https://github.com/hylo-so/sdk/blob/main/hylo-idl/src/pda.rs)
- **Stale docs page.** The docs "Onchain Addresses" page still lists the xBTC mint as "[TBD]" and does not list xHYPE at all. — [Hylo docs: Onchain Addresses](https://docs.hylo.so/security/onchain-addresses)

**Architecture: isolated pools, shared hyUSD and Earn Pool**
- "Hylo V2 introduces a more scalable, multi-asset approach. The protocol now supports independent collateral pools for each supported asset. Each collateral pool is split into an xASSET and its respective vUSD… The flagship stablecoin hyUSD is backed by the combined value of all virtual stablecoins." — [Hylo docs: Multi-Asset Architecture](https://docs.hylo.so/protocol-overview/multi-asset-architecture)
- vUSD are "internal accounting units within Hylo's exchange program. They are not tradeable tokens." — [Hylo docs: Core Mechanism](https://docs.hylo.so/protocol-overview/core-mechanism)
- The docs describe each pool as having a "Separate CR", "Risk Isolation", "Independent Rebalancing" and its own "Yield Mechanism". They also say "Each pool has its own CR, rebalance zone, fee schedule, and drawdown ledger." — [Multi-Asset Architecture](https://docs.hylo.so/protocol-overview/multi-asset-architecture); [Additional Risk Management](https://docs.hylo.so/technical-addendum/additional-risk-management)
- **The Earn Pool is shared.** "The pool aggregates yield from all collateral pools". eHYUSD "is the same token as sHYUSD: same mint address, only the ticker has changed for Hylo V2". It acts as first-loss capital: in the Destabilized zone (CR < 100%) the protocol "burns Earn Pool hyUSD to retire the unbacked virtual-stablecoin overhang". — [Earn Pool](https://docs.hylo.so/protocol-overview/earn-pool); [Additional Risk Management](https://docs.hylo.so/technical-addendum/additional-risk-management)
- **On-chain check of the shared-hyUSD equation.** The on-chain snapshot confirms hyUSD supply equals the sum of the pools' vUSD:
  - hyUSD supply: 24,692,086
  - vUSD by pool: SOL 20,977,295 + BTC 2,129,110 + HYPE 1,585,701 + USDC 0.002, for a total of 24,692,105
  - Share of hyUSD backing: SOL 85.0%, BTC 8.6%, HYPE 6.4%
  - [SOL-pool state](https://solscan.io/account/9cd2sAfbBvKs4SX9YKo4dcjwP3TgTVQ8dT5koshGcDND); [BTC pair](https://solscan.io/account/8mgw2TsNxTMndWPyswLELw3V2tPrPvtqS7Ex9RyiGhML); [HYPE pair](https://solscan.io/account/42GzNWvZ1H1hwXaBZ8mbeVZaSEgh6zMm8BABdS3v1BEB); [USDC pair](https://solscan.io/account/CMNPACEDebyvNJDgBxRc5fbScF8kmx52ZPBY4Cu4wuwS)
- **The USDC pool is the shared rebalancing counterparty.** It is "the other side of all collateral rebalancing routes". At the snapshot it held about $0.002 of USDC, so it was effectively empty. — [Multi-Asset Architecture](https://docs.hylo.so/protocol-overview/multi-asset-architecture); on-chain snapshot ([USDC pair](https://solscan.io/account/CMNPACEDebyvNJDgBxRc5fbScF8kmx52ZPBY4Cu4wuwS))

**Collateral**
- **xBTC collateral.** "The BTC collateral pool consists of cbBTC, backed 1:1 by real Bitcoin in Coinbase's institutional grade custody." The SDK hard-codes CBBTC as the xBTC pair's collateral mint (cbbtcf3aa214zXHbiAZQwf4122FBYbraNdFqgw4iMij). No zBTC or wBTC pair exists in the SDK. — [Multi-Asset Architecture](https://docs.hylo.so/protocol-overview/multi-asset-architecture); [SDK tokens.rs](https://github.com/hylo-so/sdk/blob/main/hylo-idl/src/tokens.rs)
- **xHYPE collateral.** "The HYPE collateral pool consists of HYPE on Solana". The docs link mint 98sMhvDwXj1RQi5c5Mndm3vPe9cBqPrbLaufMXFNMh5g. "Like BTC, HYPE doesn't generate native yield in the pool." — [Multi-Asset Architecture](https://docs.hylo.so/protocol-overview/multi-asset-architecture)
- That mint is the **Wormhole-bridged HYPE**. The Solana Foundation token page labels it "HYPE (Wormhole)" and gives the same mint address. — [tokens.solana.com/hyperliquid](https://tokens.solana.com/hyperliquid)
- **Wormhole announcements for HYPE:**
  - On 3 Sep 2025 Wormhole announced HYPE "is now multichain on Base, Solana and Unichain powered by Wormhole NTT" (Native Token Transfers). — [Wormhole blog](https://wormhole.com/blog/hype-goes-natively-multichain-with-wormhole-ntt)
  - On 29 Jan 2026 Wormhole posted "$HYPE, natively on @solana. Powered by Wormhole." — [Wormhole on X](https://x.com/wormhole/status/2016893209566466250)
- **Wormhole-HYPE on Solana, 30 Sep 2026** — [Jupiter token API (HYPE)](https://lite-api.jup.ag/tokens/v2/search?query=98sMhvDwXj1RQi5c5Mndm3vPe9cBqPrbLaufMXFNMh5g):
  - Mint first seen 2025-10-08; first pool 2025-10-10.
  - Supply 725,418 HYPE (about $62.7M).
  - DEX liquidity about $2.88M; 53,748 holders.
- **Collateral balances at the snapshot:**
  - HYPE vault: 29,072.23 HYPE, about 4.0% of all Wormhole-HYPE on Solana.
  - cbBTC vault: 42.796 cbBTC, about 1.4% of Solana cbBTC supply of 2,961.
  - Sources: on-chain snapshot ([HYPE pair](https://solscan.io/account/42GzNWvZ1H1hwXaBZ8mbeVZaSEgh6zMm8BABdS3v1BEB), [BTC pair](https://solscan.io/account/8mgw2TsNxTMndWPyswLELw3V2tPrPvtqS7Ex9RyiGhML)); [Jupiter token API (cbBTC)](https://lite-api.jup.ag/tokens/v2/search?query=cbbtcf3aa214zXHbiAZQwf4122FBYbraNdFqgw4iMij)
- **xSOL collateral (for comparison).** The SOL pool holds jitoSOL and hyloSOL, priced via Sanctum's SOL-value calculator and Pyth SOL/USD. At the snapshot it held 211,469.6 jitoSOL (at 1.30264 SOL each) and 22,339.0 hyloSOL (at 1.07736 SOL each), for 299,536 SOL in total. — [Multi-Asset Architecture](https://docs.hylo.so/protocol-overview/multi-asset-architecture); on-chain snapshot ([SOL-pool state](https://solscan.io/account/9cd2sAfbBvKs4SX9YKo4dcjwP3TgTVQ8dT5koshGcDND))

**Pipeline beyond xSOL/xBTC/xHYPE**
- The SDK (14 Sep 2026) already defines further exo pairs: xZEC (ZEC), xONYC (ONyc), xPST (PST) and xETH (Wormhole WETH). The researcher's RPC check found **no on-chain pair accounts or mints** for them at the snapshot, so they are not live. — [SDK tokens.rs](https://github.com/hylo-so/sdk/blob/main/hylo-idl/src/tokens.rs)
- The docs list "Yield", "Equities" and "Commodities" xAssets as "Coming soon". — [xAssets product guide](https://docs.hylo.so/product-guide/xassets)

### Inferences
- The products are **separate markets with separate risk accounting**. A holder of xHYPE is exposed to the HYPE pool's CR only, not to SOL or BTC. Holders of hyUSD and eHYUSD, however, are exposed to all pools at once, and the Earn Pool absorbs a failure of any single pool.
- "3x HYPE" on Hylo therefore means leverage on **bridged** HYPE held on Solana, priced at the native HYPE/USD oracle. It does not use Hyperliquid-native or staked HYPE, and it earns no staking yield.

### Gaps
- No official Hylo blog or announcement text for xBTC or xHYPE could be read: x.com returned 402 and xcancel returned 451. Launch details rely on Jupiter timestamps, press republications and search excerpts.
- The genesis parameters (initial CR, leverage and seed size) of the xBTC and xHYPE pools were not retrieved. Public-RPC rate limits prevented scanning the genesis transactions.
- The Wormhole NTT specifics were not documented in the sources read: hub/spoke versus burn/mint mode, rate limits, and the exact redemption path back to native HYPE on HyperCore.

## 2. What are the latest metrics for xBTC, xSOL and xHYPE?

### Takeaway
At 30 Sep 2026 10:29 UTC:

| Token | Effective leverage | CR | Pool TVL | Market cap |
|---|---|---|---|---|
| xHYPE | 2.71x (highest) | 158.5% | $2.51M | $0.93M |
| xBTC | 2.46x | 168.4% | $3.58M | $1.46M |
| xSOL | 2.41x | 170.7% | $35.8M | $14.8M |

All three charge 1% to mint and 1% to redeem in normal conditions. xBTC and xHYPE are each capped at a **$3.0M market cap**. The shared Earn Pool holds 21.6M hyUSD (87.5% of hyUSD supply). Its last-epoch yield harvest implies about 10.4% APY.

### Cited Findings
**On-chain snapshot table (2026-09-30 10:29 UTC)** — decoded by the researcher from [SOL-pool state](https://solscan.io/account/9cd2sAfbBvKs4SX9YKo4dcjwP3TgTVQ8dT5koshGcDND), [BTC pair](https://solscan.io/account/8mgw2TsNxTMndWPyswLELw3V2tPrPvtqS7Ex9RyiGhML), [HYPE pair](https://solscan.io/account/42GzNWvZ1H1hwXaBZ8mbeVZaSEgh6zMm8BABdS3v1BEB), the vault and mint accounts, and Pyth price accounts (layouts per [IDL](https://github.com/hylo-so/sdk/blob/main/hylo-idl/idls/hylo_exchange.json)). NAV, leverage and CR use the docs' formulas: NAV = (TVL − vUSD)/supply; leverage = TVL/xAsset market cap; CR = TVL/vUSD ([Hylo Equations](https://docs.hylo.so/technical-addendum/hylo-equations)).

| Metric | xSOL | xBTC | xHYPE |
|---|---|---|---|
| Collateral held | 211,469.6 jitoSOL + 22,339.0 hyloSOL (= 299,536 SOL) | 42.796 cbBTC | 29,072.2 HYPE (Wormhole) |
| Oracle price used (Pyth) | SOL $119.54 | BTC $83,766.8 | HYPE $86.45 |
| Pool TVL | $35.81M | $3.585M | $2.513M |
| vUSD (hyUSD backed by pool) | $20.98M | $2.129M | $1.586M |
| Collateral ratio | 170.7% (Buy Zone 1) | 168.4% (Buy Zone 1) | 158.5% (Neutral) |
| xAsset supply | 160,699,170 | 673,437 | 422,362 |
| NAV | $0.092279 | $2.1618 | $2.1962 |
| Market cap at NAV | $14.83M | $1.456M | $0.928M |
| Effective leverage | 2.41x | 2.46x | 2.71x |
| Mint / redeem fee, Neutral and buy zones | 1% / 1% | 1% / 1% | 1% / 1% |
| Mint / redeem fee, Sell Zone 1 (120–135%) | 0.5% / 4% | 0.5% / 1% | 0.5% / 1% |
| Mint / redeem fee, Sell Zone 2 (100–120%) | 0% / 8% | 0% / 8% | 0% / 8% |
| Leverage cost | none in Neutral; above 165% CR the LST-yield multiplier is m≤2 (ceiling 2.0) | floor 0.0824%/epoch (15.04% APR simple), ceiling 0.1648%/epoch (30.08%) on the xBTC market cap | same as xBTC |
| Treasury cut of yield or borrow harvest | 5% | 5% | 5% |
| xAsset market-cap limit | none in account layout | $3,000,000 (headroom about $1.54M) | $3,000,000 (headroom about $2.07M) |
| hyUSD mint threshold (CR) | 150% | 150% | 150% |
| Oracle confidence tolerance / max age | 1% / – | 1% / 10 s | 1% / 10 s |
| Outstanding Earn Pool drawdown debt | 0 | 0 | 0 |
| Paused? | no | no | no |

**System-wide figures from the same snapshot**
- hyUSD supply is 24,692,086.
- System CR is 169.7%, computed as (sum of pool TVLs + USDC vault) / sum of vUSD. The pool TVLs total $41.90M, split SOL 85.4%, BTC 8.6%, HYPE 6.0%. — on-chain snapshot (accounts above)
- **Earn Pool (shared "stability pool"):**
  - It holds 21,599,129 hyUSD, which is 87.5% of hyUSD supply.
  - eHYUSD supply is 14,449,639, so NAV is 1.49479 hyUSD per eHYUSD.
  - It holds 0 xSOL (V1-era xSOL conversions are fully unwound), and no xBTC or xHYPE account exists.
  - Last harvest (epoch 1046) sent 9,634 hyUSD from the SOL pool, 1,389 from BTC and 720 from HYPE, for 11,743 hyUSD in total.
  - Sources: on-chain snapshot; eHYUSD mint [HnnGv3…](https://solscan.io/account/HnnGv3HrSqjRpgdFmx7vQGjntNEoex1SU4e9Lxcxuihz); the APY formula (1+epoch rate)^182.5−1 comes from the [Earn Pool docs](https://docs.hylo.so/protocol-overview/earn-pool)
- **eHYUSD market price.** Jupiter shows eHYUSD at $1.4929 and a $21.57M market cap, but almost no DEX liquidity ($902). — [Jupiter token API (eHYUSD)](https://lite-api.jup.ag/tokens/v2/search?query=HnnGv3HrSqjRpgdFmx7vQGjntNEoex1SU4e9Lxcxuihz)
- **USDC pool.** vUSD is about 0 and the vault holds $0.0018. Mint fee 0%, redeem fee 0.2%, par tolerance $0.001. — on-chain snapshot; docs: "currently 0% to mint and 0.2% to redeem" ([Multi-Asset Architecture](https://docs.hylo.so/protocol-overview/multi-asset-architecture))

**Market data, 30 Sep 2026 about 10:19 UTC (Jupiter token API)**

| Token | Price | Market cap | DEX liquidity | Holders | Top-holder share | 24h change | 24h DEX volume (organic) |
|---|---|---|---|---|---|---|---|
| xHYPE | $2.2170 | $936k | $248k | 8,437 | 29.2% | −5.23% | $936k ($157k) |
| xBTC | $2.1363 | $1.44M | $212.5k | 7,228 | 38.3% | −1.83% | $373k ($33k) |
| xSOL | $0.09117 | $14.65M | $838k | 31,494 | 46.5% | −1.18% | $4.50M ($300k) |
| hyUSD | $0.99889 | – | $2.89M | 4,332 | 90.5% | – | – |

- The 24h volume column is Jupiter's buy plus sell volume, with "organic" volume in brackets.
- Sources: [Jupiter (xHYPE)](https://lite-api.jup.ag/tokens/v2/search?query=7ga6rtE9qSb3wdEiDCpTu2kHqoGVfT52jD8ign1rYTvx); [Jupiter (xBTC)](https://lite-api.jup.ag/tokens/v2/search?query=2zCo6bUowJMvr89ajxuWsPadAqJ2F9akCkxumNsSdgsL); [Jupiter (xSOL)](https://lite-api.jup.ag/tokens/v2/search?query=4sWNB8zGWHkh6UnmwiEtzNxL4XrN7uK9tosbESbJFfVs); [Jupiter (hyUSD)](https://lite-api.jup.ag/tokens/v2/search?query=5YMkXAYccHSGnHn9nob9xEvv6Pvka9DZWH7nTbotTu9E)

**CoinGecko, last updated 30 Sep 10:20 UTC**
- **xHYPE** (id xhype-3; rank about 3109):
  - Price $2.21, market cap $938,393, 24h volume $441,882.
  - Its ATH of $2.81 (24 Sep) and ATL of $2.11 (29 Sep) only cover CoinGecko's history, which starts around 24 Sep 2026.
  - Main tickers: Meteora xHYPE/USDC ($190k 24h), Meteora xHYPE/WSOL ($154k) and Orca xHYPE/USDC ($40k). Quoted bid-ask spreads are about 0.6–0.8%.
  - [CoinGecko xHYPE](https://www.coingecko.com/en/coins/xhype-3)
- **xSOL:**
  - Price $0.091344, 24h volume $299,362; +38.1% over 30 days.
  - ATH $2.08 (26 Oct 2025); ATL $0.01486 (6 Jun 2026).
  - [CoinGecko xSOL](https://www.coingecko.com/en/coins/hylo-leveraged-sol)
- **xBTC:** Hylo's xBTC did not appear in CoinGecko search results. — [CoinGecko search API](https://api.coingecko.com/api/v3/search?query=hylo)

**Largest DEX pools (GeckoTerminal, 30 Sep 2026)**
- xHYPE:
  - Meteora xHYPE/USDC: $99.8k reserve, $188k 24h volume. — [GeckoTerminal](https://www.geckoterminal.com/solana/pools/8tp8GJADuYu2czhnaWzXYxpXTq2dwjribGwSav4J4m7e)
  - Meteora xHYPE/SOL: $26.6k reserve, $153k 24h volume. — [GeckoTerminal](https://www.geckoterminal.com/solana/pools/AvPqWvQoEnC5aiFm3y3y1AkDyR8Dns8u4RL1VbKLXvtd)
- xBTC:
  - Meteora xBTC/USDC: $97.1k reserve, $58k 24h volume. — [GeckoTerminal](https://www.geckoterminal.com/solana/pools/4m1WVt7dWwkZG3cZcEHcKKXbb5EL4rLAFD1ne1aFdngb)
- xSOL:
  - Orca xSOL/SOL: $505k reserve, $1.55M 24h volume. — [GeckoTerminal](https://www.geckoterminal.com/solana/pools/coj59LYbLc6DhMwnxxfPc9mUiknjFSsW4XcuYw4DMPk)

**DefiLlama, 30 Sep 2026**
- Hylo TVL is $65.2M, all on Solana. The breakdown is jitoSOL $32.3M, SOL $24.0M, cbBTC $3.56M, hyloSOL $2.85M and HYPE $2.50M. — [DefiLlama Hylo](https://defillama.com/protocol/hylo) ([API](https://api.llama.fi/protocol/hylo))
- The "SOL $24.0M" line matches the separate hyloSOL LST product: DefiLlama yields lists "hylo-lsts" HYLOSOL with a TVL of $22.9M and 5.85% APY. — [DefiLlama yields](https://yields.llama.fi/pools)

**Historical leverage ranges**
- Pine Analytics described xBTC as about 2.7x at launch, within a 2x–4x range. — [Pine Analytics on X](https://x.com/PineAnalytics/status/2079338696726229180)
- CryptoBriefing describes xSOL leverage as "2-4x variable". — [CryptoBriefing](https://cryptobriefing.com/hylo-v2-leveraged-equities-solana/)
- By formula, leverage = CR/(CR−1):

| CR | Leverage | Zone |
|---|---|---|
| 175% | 2.33x | Buy Zone 2 boundary |
| 165% | 2.54x | Buy Zone 1 boundary |
| 150% | 3x | target |
| 135% | 3.86x | Neutral lower boundary |
| 120% | 6x | Sell Zone 2 boundary |
| 100% | → infinity | NAV goes to 0 |

  — [Hylo Equations](https://docs.hylo.so/technical-addendum/hylo-equations)

### Inferences
- **Borrow cost now:**
  - xHYPE is in the Neutral zone and pays the floor borrow rate: about 15.0% APR simple (16.2% compounded) on its NAV. At 2.71x leverage that is about 5.5% per year of notional exposure.
  - xBTC sits at 168.4% CR, in Buy Zone 1. By the curve its rate is about 1.34× the floor, which is about 20.1% APR on NAV, or about 8.2% of notional.
  - The last harvest is consistent with these rates. BTC paid 1,389 hyUSD net of the 5% fee on a $1.456M market cap, which is 0.100%/epoch, or about 1.22× floor. HYPE paid 720 hyUSD on $0.928M, about the floor rate.
- **xSOL is currently paying a borrow cost too.** Last epoch the pool's LSTs appreciated about 52.5 SOL (jitoSOL +0.0173%, hyloSOL +0.0199%), which is about $6.3k. The harvest of 9,634 hyUSD net of the 5% fee implies a multiplier of about 1.6×. So roughly 0.6× the LST yield came out of xSOL equity: about 3.3% of notional, or about 8% of NAV per year, at a 5.85% LST yield. In the Neutral zone xSOL would pay nothing extra.
- **Estimated Earn Pool APY.** 11,743 hyUSD per epoch on 21.6M hyUSD is 0.0544% per epoch. Compounded over 182.5 epochs that is about **10.4% APY**, before any rebalancing P&L. This is the researcher's derived estimate, not a Hylo-published figure.
- **DEX prices sit inside the protocol's mint/redeem band.**
  - xBTC and xSOL DEX prices are about 1% below NAV, which is roughly the redemption value after the 1% fee.
  - xHYPE trades about 1% above NAV, closer to the mint price.
  - This is consistent with arbitrage against a 1%/1% fee band.

### Gaps
- Hylo's own stats page could not be read: hylo.so returned a Vercel bot checkpoint. Official APY, CR history and leverage charts were therefore not accessible.
- There is no time series of CR or leverage for any pool. Historical minimum and maximum leverage for xBTC and xHYPE is unverified; only the launch-time figure (about 2.7x, per Pine) and the current snapshot are known.
- Top-holder shares are Jupiter's aggregate metric. The individual holders (for example, DEX pools versus wallets) could not be identified because the public RPC rate-limited getTokenLargestAccounts.

## 3. How do the mechanisms of the three products differ?

### Takeaway
All three share the same equations. Each pool targets a 150% CR (3x) and uses the same six-zone rebalancing, the same hyUSD fee curves and the same shared Earn Pool backstop. The differences are:
- **Cost of leverage.** xSOL is free while its CR is in the Neutral zone. xBTC and xHYPE always pay a 15–30% APR borrow rate on NAV.
- **Collateral and oracle.** xSOL uses LSTs valued via Sanctum plus Pyth SOL/USD. xBTC uses cbBTC priced at Pyth BTC/USD. xHYPE uses Wormhole HYPE priced at Pyth HYPE/USD.
- **Sell-zone redeem penalty.** In Sell Zone 1 the redeem fee is 1% for xBTC/xHYPE versus 4% for xSOL.
- **Capacity.** xBTC and xHYPE each have a $3M market-cap cap.

At the snapshot, xHYPE runs at slightly higher leverage than xSOL and xBTC because its pool sits nearer the 150% target.

### Cited Findings
**Zones and targets**
- The six zones are:
  - Buy Zone 2: ≥175%
  - Buy Zone 1: 165–175%
  - Neutral: 135–165% (target about 150%)
  - Sell Zone 1: 120–135%
  - Sell Zone 2: 100–120%
  - Destabilized: <100%, where "xASSET NAV → 0; rebalancing, P&L settlement, and minting halt"
  - "Each xASSET-vUSD pair targets a collateral ratio of 150%, implying structural leverage at 3x".
  - Sources: [Hylo Equations](https://docs.hylo.so/technical-addendum/hylo-equations); [Protocol xASSETs](https://docs.hylo.so/protocol-overview/xassets)
- **VaR basis for the target.**
  - The VaR table covers SOL (1-day 99.9% VaR −32.95%) and BTC (about −25%), both with a 150% target. It has **no HYPE row**.
  - For new pools the framework "prefers" at least 2 years of data and a 1-day 99.9% VaR better than −40%.
  - The BTC target keeps 150% partly as a "buffer for wrapped BTC risks (custody, bridging)".
  - [Value-at-Risk Analysis](https://docs.hylo.so/technical-addendum/value-at-risk-analysis)

**Fees**
- **hyUSD (stablecoin) fee curves** are hard-coded in the SDK:
  - Mint fee: 0.20% at 150% CR, falling to 0.005% at 170% and above. Mints below the curve (150%) are blocked.
  - Redeem fee: 0% at 130% CR or below, rising to 0.20% at 150%. Above 150% there is no quote.
  - [SDK fees/curves.rs](https://github.com/hylo-so/sdk/blob/main/hylo-core/src/fees/curves.rs); [Dynamic Collateral Routing](https://docs.hylo.so/protocol-overview/dynamic-collateral-routing)
- **xAsset fees are zone-tiered.** The docs give an "example" of 100/100 bps in normal zones, 50/400 in Sell Zone 1 and 0/800 in Sell Zone 2, with mints and redemptions blocked when Destabilized. On-chain, xSOL matches this. xBTC and xHYPE use **50/100 bps in Sell Zone 1**. — [Additional Risk Management](https://docs.hylo.so/technical-addendum/additional-risk-management); on-chain snapshot

**Earn Pool behaviour (V2)**
- The Earn Pool settles rebalancing P&L: "profitable rebalances mint hyUSD into the pool, subsidized ones burn hyUSD from it".
- In the Destabilized zone it burns hyUSD to retire the vUSD overhang, capped at its balance. The amount is recorded as pool drawdown debt.
- While that debt is outstanding, stablecoin minting is frozen for that pool and yield harvesting pauses. Future yield then repays the drawdown first.
- [Additional Risk Management](https://docs.hylo.so/technical-addendum/additional-risk-management); [Collateral Rebalancing](https://docs.hylo.so/protocol-overview/collateral-rebalancing)
- This replaces V1's model, in which the stability pool converted hyUSD into xSOL. During that V1 era, Pine reported that "multiple stability pool activations… deployed $7.9M in hyUSD to defend the peg" in Q1 2026. — [Pine Analytics Q1 2026](https://pineanalytics.substack.com/p/hylo-quarterly-operations-overview); [KuCoin V2](https://www.kucoin.com/news/flash/hylo-launches-v2-expands-on-chain-leverage-to-stocks-and-multi-asset-collateral)

**Rebalancing**
- In the sell zones the protocol opens an ASSET→USDC route that sells collateral at a CR-dependent discount. In the buy zones it opens a USDC→ASSET route. Both routes are capped so they cannot overshoot 135% or 165%. — [Collateral Rebalancing](https://docs.hylo.so/protocol-overview/collateral-rebalancing)
- On-chain rebalance spread settings:
  - Sell curve: floor 0.2%, ceiling 0.1% for all three pools.
  - Buy curve: 0.1% / 0.1% for all three pools.
  - on-chain snapshot

**Oracles**
- Oracles are Pyth SOL/USD (with Sanctum LST value), Pyth BTC/USD and Pyth HYPE/USD. Pyth USDC/USD is used only as a par check. — [Hylo Equations](https://docs.hylo.so/technical-addendum/hylo-equations)
- The pairs store Pyth feed IDs: 0xe62df6c8… (BTC/USD) for the cbBTC pair and 0x4279e31c… (HYPE/USD) for the HYPE pair. The SDK names these feeds BTC_USD and HYPE_USD, so the pairs are priced at the **underlying asset's USD price, not the wrapper's market price**. — on-chain snapshot; [SDK pyth/feeds.rs](https://github.com/hylo-so/sdk/blob/main/hylo-core/src/pyth/feeds.rs)
- The oracle code:
  - rejects prices older than the configured interval (10 s for the exo pairs);
  - rejects prices whose confidence/price ratio exceeds the tolerance (1%);
  - uses the confidence band "lower in minting, higher in redeeming".
  - [SDK pyth/oracle.rs](https://github.com/hylo-so/sdk/blob/main/hylo-core/src/pyth/oracle.rs); on-chain snapshot

**Yield sources and cost of leverage**
- **xSOL:** the SOL pool's LST yield goes to the Earn Pool. "Leverage is effectively free… The one exception is a high collateral ratio. Above 165% CR the protocol harvests a multiple of the LST yield, and xSOL holders pay the amount above 1×." The multiplier ceiling is m_c=2 (on-chain yield_ceil_mult 2.0). — [Protocol xASSETs](https://docs.hylo.so/protocol-overview/xassets); [Hylo Equations](https://docs.hylo.so/technical-addendum/hylo-equations)
- **xBTC and xHYPE:** they pay a "configurable borrow rate… through gradual NAV reduction… based on the xBTC market cap, so the effective rate on a holder's leveraged exposure rises as effective leverage falls". The rate is the base rate in Neutral, rises linearly to 2× base at 175%, and is paused below 135%. — [Multi-Asset Architecture](https://docs.hylo.so/protocol-overview/multi-asset-architecture)
  - The SDK caps the per-epoch rate at 0.001648352, which it describes as "~30% annualized". On-chain, both pairs sit at floor 0.000824176 and ceiling 0.001648352 per epoch. — [SDK borrow_rate.rs](https://github.com/hylo-so/sdk/blob/main/hylo-core/src/borrow_rate.rs); on-chain snapshot
- **Market-cap cap:** the levercoin limiter rejects any mint that would take the xAsset market cap above the limit. That limit is $3M for both xBTC and xHYPE. — [SDK limiter/levercoin.rs](https://github.com/hylo-so/sdk/blob/main/hylo-core/src/limiter/levercoin.rs); on-chain snapshot

**Why xHYPE runs at higher leverage than xSOL and xBTC right now**
- Leverage rises when vUSD is minted or xASSET is redeemed, and falls when vUSD is burned or xASSET is minted. — [Protocol xASSETs](https://docs.hylo.so/protocol-overview/xassets)
- hyUSD mints are routed to pools above 150% at fees that shrink toward 0.005% as CR rises. The USDC pool "takes the flow when no volatile pool can". — [Dynamic Collateral Routing](https://docs.hylo.so/protocol-overview/dynamic-collateral-routing)
- A higher borrow rate is meant to attract eHYUSD deposits when CR is high. The docs expect these increases to be "occasional and short-lived". — [Multi-Asset Architecture](https://docs.hylo.so/protocol-overview/multi-asset-architecture)

### Inferences
- **The pools sit above target because there is too little hyUSD minting and no USDC to rebalance with.**
  - SOL (170.7%) and BTC (168.4%) are in Buy Zone 1. Buy-zone rebalancing needs USDC in the USDC pool, which was empty at the snapshot. So the only ways back to 150% are new hyUSD minting from those pools, or xAsset redemptions and price declines.
  - The HYPE pool (158.5%) sits nearest the target, so xHYPE carries the most leverage (2.71x). The difference is modest.
  - The "3x" marketing overstates the current leverage of all three (2.4–2.7x).
- **The borrow-rate design makes xBTC and xHYPE structurally more expensive to hold than xSOL.**
  - The floor rate of about 15% APR on NAV applies whenever CR is between 135% and 165%. It is not a rare event.
  - By contrast, xSOL pays nothing in that band and at most (m−1)× LST yield above it.
  - For a multi-month hold, this cost difference plausibly outweighs the small leverage difference.
- **The Sell Zone 1 redeem fee cuts both ways.** xBTC and xHYPE holders face only 1% (versus 4% for xSOL) to exit in Sell Zone 1. That is friendlier to holders, but gives the pool less protection against destabilizing redemptions.
- **Oracle design:** pricing at BTC/USD and HYPE/USD means a depeg of the cbBTC or Wormhole-HYPE wrapper would not be reflected in NAV. xAsset holders, then the Earn Pool, would bear it.

### Gaps
- Hylo publishes no VaR analysis for HYPE and no stated rationale for using the same 150% target for HYPE.
- It is unclear whether the "vUSD floor" parameters (0.827 for BTC, 0.0987 for HYPE) affect users.
- The Earn Pool withdrawal fee value was not decoded.

## 4. How have they performed since launch, and how did they behave under stress?

### Takeaway
- **xHYPE (since 17 Aug 2026):** about +120% versus HYPE about +46% (roughly 2.6x). The worst close-to-close drawdown was −34.8% (6–15 Sep), when HYPE fell 12.1%.
- **xBTC (since 20–21 Jul 2026):** about +71% to +85% versus BTC about +26% to +28% (roughly 2.7–3.0x). The worst drawdown was −18.1% when BTC fell 6.8%.
- **xSOL over the same windows:** about +178% to +192% versus SOL about +53% to +55%.
- Daily-return betas were 2.5–2.6 for all three.
- No low-CR episode, Earn Pool loss absorption, depeg or incident was found for the xBTC or xHYPE pools.
- xSOL's longer history shows the tail risk of a sustained bear market: from 15 Oct 2025 to 7 Jun 2026 it went from $1.95 to $0.0165 (−99.2%) while SOL fell 69%.

### Cited Findings
**Method.** Performance uses:
- xHYPE daily closes from the Meteora xHYPE/USDC pool — [GeckoTerminal OHLCV](https://www.geckoterminal.com/solana/pools/8tp8GJADuYu2czhnaWzXYxpXTq2dwjribGwSav4J4m7e)
- xBTC daily closes from the Meteora xBTC/USDC pool (jecknZ…) — [GeckoTerminal OHLCV](https://www.geckoterminal.com/solana/pools/jecknZ7TgMYYBnbQ1ZHF9Z145aDSzAFbHHiGQw8ZkAb)
- xSOL, HYPE, BTC and SOL hourly prices from CoinGecko — [xSOL](https://www.coingecko.com/en/coins/hylo-leveraged-sol), [HYPE](https://www.coingecko.com/en/coins/hyperliquid), [BTC](https://www.coingecko.com/en/coins/bitcoin), [SOL](https://www.coingecko.com/en/coins/solana)
- the 30 Sep on-chain NAV snapshot for the NAV-based variants

| Window | xAsset return | Underlying return | Ratio | Daily log-return beta (corr) | Worst close-to-close drawdown: xAsset vs underlying |
|---|---|---|---|---|---|
| **xHYPE**, DEX: 17 Aug close $0.9987 → 30 Sep $2.221 | **+122.4%** | HYPE $59.06 → $86.48: **+46.4%** | 2.64x | 2.62 (0.95), 18 Aug–30 Sep | **−34.8%** (6→15 Sep) vs HYPE −12.1% |
| **xHYPE**, NAV: $1.00 at genesis (NAV defaults to $1) → $2.1962 | +119.6% | HYPE $59.16 (17 Aug 17:00 UTC) → $86.45: +46.1% | 2.59x | – | – |
| **xBTC**, DEX: 21 Jul close $1.2586 → 30 Sep $2.1568 | **+71.4%** | BTC $66,264 → $83,603: **+26.2%** | 2.73x | 2.48 (0.95), 21 Jul–30 Sep | **−18.1%** (3→15 Sep) vs BTC −6.8% |
| **xBTC**, NAV: $1.17 at public open (per Pine) → $2.1618 | +84.8% | BTC $65,316 (20 Jul 21:00 UTC) → $83,767: +28.2% | 3.0x | – | – |
| **xSOL**, same window as xBTC (21 Jul → 30 Sep) | **+177.7%** | SOL $77.94 → $119.32: **+53.1%** | 3.35x | 2.61 (0.97) | −26.5% vs SOL −11.1% |
| **xSOL**, same window as xHYPE (18 Aug → 30 Sep) | **+192.3%** | SOL $76.91 → $119.32: **+55.1%** | 3.49x | 2.53 (0.98) | −26.5% vs SOL −11.1% |

- The Pine source for the $1.17 xBTC opening NAV is [Pine Analytics on X](https://x.com/PineAnalytics/status/2079338696726229180).
- The xSOL drawdown figure is from the CoinGecko hourly series.

**xHYPE price range since launch (DEX)**
- Intraday low: about $0.954 on 19 Aug 2026.
- Intraday high: about $3.25 on 22 Sep 2026.
- Highest close: $2.912 on 22 Sep.
- On 30 Sep: close $2.221; on-chain NAV $2.196.
- [GeckoTerminal](https://www.geckoterminal.com/solana/pools/8tp8GJADuYu2czhnaWzXYxpXTq2dwjribGwSav4J4m7e)

**Stress and large moves inside the windows (daily closes)** — [GeckoTerminal](https://www.geckoterminal.com/solana/pools/8tp8GJADuYu2czhnaWzXYxpXTq2dwjribGwSav4J4m7e); [CoinGecko HYPE](https://www.coingecko.com/en/coins/hyperliquid); [GeckoTerminal xBTC](https://www.geckoterminal.com/solana/pools/jecknZ7TgMYYBnbQ1ZHF9Z145aDSzAFbHHiGQw8ZkAb); [CoinGecko BTC](https://www.coingecko.com/en/coins/bitcoin); [CoinGecko xSOL](https://www.coingecko.com/en/coins/hylo-leveraged-sol)

| Dates | Underlying move | xAsset move |
|---|---|---|
| 18–19 Aug | HYPE $58.40 → $70.77 (+21.2%) | xHYPE $0.971 → $1.491 (+53.6%) |
| 6–15 Sep | HYPE $87.39 → $76.78 (−12.1%) | xHYPE $2.425 → $1.581 (−34.8%) |
| 22–29 Sep | HYPE $97.18 → $86.31 (−11.2%) | xHYPE $2.912 → $2.131 (−26.8%) |
| 26 Jul–1 Aug | BTC $65,362 → $62,780 (−4.0%) | xBTC $1.139 → $1.031 (−9.5%) |
| 3–15 Sep | BTC $81,142 → $75,646 (−6.8%) | xBTC $2.088 → $1.711 (−18.1%) |

**Thin-pool artefacts on launch days.** The xBTC/USDC pool printed a $0.885–$1.305 range on 21 Jul (launch day) and a $0.91–$1.75 wick on 11 Aug. These look like thin-pool artefacts rather than NAV moves. — [GeckoTerminal](https://www.geckoterminal.com/solana/pools/jecknZ7TgMYYBnbQ1ZHF9Z145aDSzAFbHHiGQw8ZkAb)

**No outstanding pool stress at the snapshot.** Pool drawdown debt was 0 for the SOL, BTC and HYPE pools, and none of the pools was paused. — on-chain snapshot

**No incident reports found.** Searches found no reports of exploits, depegs or Earn Pool loss absorption involving xBTC, xHYPE or hyUSD in 2026. A 2025 article notes that hyUSD survived "one depeg-free $19B liquidation event". hyUSD traded at $0.9989 on 30 Sep. — [SolanaFloor](https://solanafloor.com/news/top-breakout-solana-apps-in-2025); [Jupiter (hyUSD)](https://lite-api.jup.ag/tokens/v2/search?query=5YMkXAYccHSGnHn9nob9xEvv6Pvka9DZWH7nTbotTu9E)

**xSOL's stress history (V1 era)**
- Q1 2026: TVL fell from $52M to $22.8M as SOL dropped 33%. "Multiple stability pool activations… deployed $7.9M in hyUSD to defend the peg". sHYUSD earned 52.4% APY in Q1. — [Pine Analytics Q1 2026](https://pineanalytics.substack.com/p/hylo-quarterly-operations-overview)
- xSOL supply grew from 8.4M (Oct 2025) to 235M (Jun 2026). The growth came from new deposits and from stability-pool conversions of hyUSD into xSOL. — [DefiLlama Research, 30 Jul 2026](https://research-newsletters.defillama.com/p/leverage-without-liquidation)
- CoinGecko daily closes, 15 Oct 2025 → 7 Jun 2026: xSOL fell from $1.95 to $0.01653 (−99.2%) while SOL fell from $202.58 to $62.18 (−69.3%). From 7 Jun to 30 Sep 2026, xSOL rose about +453% ($0.0165 → $0.0915) while SOL rose about +92%. — [CoinGecko xSOL](https://www.coingecko.com/en/coins/hylo-leveraged-sol); [CoinGecko SOL](https://www.coingecko.com/en/coins/solana)
- DefiLlama Research estimated SOL would need to reach roughly $630–$719 for xSOL to recover. Its methodology and reference point were not reproduced here. — [DefiLlama Research](https://research-newsletters.defillama.com/p/leverage-without-liquidation)

### Inferences
- **Leverage in practice.** Realized sensitivity has been about 2.5–2.7x for all three products, consistent with the on-chain leverage of 2.4–2.7x.
- **Why xSOL's return multiple exceeded 3x.** SOL rose strongly with a mostly one-way path. xSOL also started the windows at higher leverage (CR was lower after the H1-2026 crash), so compounding in a trending market pushed its return multiple above 3x.
- **The launch windows are benign.** xBTC and xHYPE launched into rising markets (BTC +26–28%, HYPE +46%). Neither has yet been tested by a SOL-2026-style drawdown.
- **Static distance to trouble.** Assuming no rebalancing or flows, the price drop needed to reach each zone from the snapshot CR is:

| Pool | To Sell Zone 1 (135%) | To Sell Zone 2 (120%) | To Destabilized (<100%, NAV → 0) |
|---|---|---|---|
| HYPE | −14.8% | −24.3% | −36.9% |
| BTC | −19.8% | −28.7% | −40.6% |
| SOL | −20.9% | −29.7% | −41.4% |

  Rebalancing sales in the sell zones would widen these buffers, but only if arbitrageurs absorb the collateral. As a point of reference, HYPE moved −12% in just nine days in September.

### Gaps
- No NAV time series is available for xBTC or xHYPE. Performance uses DEX prices, which can deviate from NAV by about ±1%, and Pine's opening NAV of $1.17 for xBTC.
- Intraday CR during the 6–15 Sep HYPE drop is unknown, so it is unverified whether the HYPE pool touched Sell Zone 1.
- No 2026 sharp-drop stress event (larger than −15% in the underlying) has occurred since the xBTC and xHYPE launches, so their stress behaviour is untested.

## 5. What product-specific risks do xHYPE and xBTC carry?

### Takeaway
xHYPE combines the most fragile inputs:
- a bridged asset (Wormhole NTT HYPE) priced at the native HYPE oracle;
- the smallest pool ($2.5M TVL) and a $3M market-cap cap;
- thin Solana HYPE liquidity for arbitrage and rebalancing;
- the highest current leverage;
- a permanent borrow rate of 15% or more on NAV;
- a DEX exit cost of about 1.6–1.7% per sale.

xBTC's wrapper risk is Coinbase custody rather than a bridge. It shares the same borrow-rate and market-cap-cap structure.

### Cited Findings
**Wrapper and bridge risk**
- xHYPE's collateral is "HYPE (Wormhole)". — [tokens.solana.com](https://tokens.solana.com/hyperliquid); [Wormhole blog](https://wormhole.com/blog/hype-goes-natively-multichain-with-wormhole-ntt)
- xBTC's collateral is cbBTC, "backed 1:1 by real Bitcoin in Coinbase's institutional grade custody". — [Multi-Asset Architecture](https://docs.hylo.so/protocol-overview/multi-asset-architecture)
- Hylo lists "Wrapped asset custody, bridge security, oracle reliability" as BTC-specific risks. — [VaR Analysis](https://docs.hylo.so/technical-addendum/value-at-risk-analysis)

**Oracle risk**
- The pairs are priced at Pyth BTC/USD and HYPE/USD, not at the wrapper's price. — on-chain feed IDs; [SDK feeds.rs](https://github.com/hylo-so/sdk/blob/main/hylo-core/src/pyth/feeds.rs)
- Operations revert if Pyth confidence exceeds 1% of price, or if the price is older than 10 s. — [SDK oracle.rs](https://github.com/hylo-so/sdk/blob/main/hylo-core/src/pyth/oracle.rs); on-chain snapshot
- An OtterSec audit of V1 noted that EMA-price lag could be exploited during sharp swings when the spot–EMA spread exceeds 1%. The V2 code reads the spot price plus confidence. — [OtterSec audit (V1)](https://hylo-audits.s3.us-east-2.amazonaws.com/OtterSec-Exchange-Stability-Pool-20250513.pdf); [SDK oracle.rs](https://github.com/hylo-so/sdk/blob/main/hylo-core/src/pyth/oracle.rs)

**Thin liquidity**
- Liquidity figures on Jupiter:
  - Wormhole-HYPE on Solana: about $2.88M total DEX liquidity, versus cbBTC's $31.5M.
  - xHYPE: $248k.
  - xBTC: $212.5k.
  - xSOL: $838k.
  - [Jupiter HYPE](https://lite-api.jup.ag/tokens/v2/search?query=98sMhvDwXj1RQi5c5Mndm3vPe9cBqPrbLaufMXFNMh5g); [Jupiter cbBTC](https://lite-api.jup.ag/tokens/v2/search?query=cbbtcf3aa214zXHbiAZQwf4122FBYbraNdFqgw4iMij); [Jupiter xHYPE](https://lite-api.jup.ag/tokens/v2/search?query=7ga6rtE9qSb3wdEiDCpTu2kHqoGVfT52jD8ign1rYTvx)
- Selling $1k–$4k of xHYPE to USDC via Jupiter cost about 1.6–1.7% below mid, versus about 0.3% for xSOL (see Q6). — [Jupiter Quote API](https://lite-api.jup.ag/swap/v1/quote)

**Size, concentration and capacity**
- HYPE pool TVL is $2.51M and xHYPE market cap is $0.93M. The xHYPE market-cap limit is $3.0M; the xBTC limit is also $3.0M. — on-chain snapshot
- Top-holder share (Jupiter metric): xHYPE 29.2%, xBTC 38.3%, xSOL 46.5%. Holders: 8,437, 7,228 and 31,494. — [Jupiter token API](https://lite-api.jup.ag/tokens/v2/search?query=7ga6rtE9qSb3wdEiDCpTu2kHqoGVfT52jD8ign1rYTvx)

**Earn Pool backstop**
- The Earn Pool is shared and holds 21.6M hyUSD. That compares with HYPE-pool vUSD of $1.59M and BTC-pool vUSD of $2.13M. — on-chain snapshot
- Its loss absorption protects the **hyUSD peg only**. In the Destabilized zone, "xASSET NAV → 0". — [Hylo Equations](https://docs.hylo.so/technical-addendum/hylo-equations)

**Structural costs**
- Borrow rate is 15.04–30.08% APR on the xAsset market cap. — on-chain snapshot; [Multi-Asset Architecture](https://docs.hylo.so/protocol-overview/multi-asset-architecture)
- "Volatility decay causes leveraged tokens to lose value over time in sideways markets." — [Protocol xASSETs](https://docs.hylo.so/protocol-overview/xassets)

**Short HYPE history and missing VaR**
- HYPE's genesis was 29 Nov 2024. — [eco.com](https://eco.com/support/en/articles/15039713-what-is-hype-token-hyperliquid-s-native-asset)
- Hylo's framework prefers at least 2 years of data for new pools. — [VaR Analysis](https://docs.hylo.so/technical-addendum/value-at-risk-analysis)
- No HYPE VaR is published. — [VaR Analysis](https://docs.hylo.so/technical-addendum/value-at-risk-analysis)

**Name collisions and copycats**
- Solana also has **OKX Wrapped BTC with the ticker "xBTC"**: mint CtzPWv…, price about $83.6k, market cap $22.9M. — [Jupiter search "xBTC"](https://lite-api.jup.ag/tokens/v2/search?query=xBTC)
- Jupiter search for "xHYPE" returns multiple pump.fun, stonkfun and Raydium LaunchLab tokens named "Hylo 3x Leveraged HYPE" or "XHYPE", mostly created 23–29 Sep 2026. — [Jupiter search "xHYPE"](https://lite-api.jup.ag/tokens/v2/search?query=xHYPE)

**xHYPE as a memecoin quote asset**
- A 23 Sep 2026 Hylo post (per search excerpt) says xHYPE "is now available as" a quote asset on StonkFun. The HYPERPS launchpad uses xHYPE as its quote token. — [Hylo on X](https://x.com/hylo_so/status/2102820846280872403); [hyperps.lol](https://hyperps.lol/)
- GeckoTerminal lists memecoin/xHYPE pools created 23–24 Sep, e.g. PURRP/xHYPE ($53.9k reserve) and HYPERCAT/xHYPE ($87.0k). — [GeckoTerminal xHYPE pools](https://www.geckoterminal.com/solana/tokens/7ga6rtE9qSb3wdEiDCpTu2kHqoGVfT52jD8ign1rYTvx)

### Inferences
- **Bridge or wrapper depeg.** If Wormhole-HYPE or cbBTC depegged (for example through a bridge exploit or a custody failure), the oracle would keep valuing the collateral at the native price. The pool would be silently undercollateralized, and the loss would land first on xAsset NAV and then on Earn Pool hyUSD.
- **Rebalancing may not work when it is most needed.** The HYPE pool's sell-zone rebalancing relies on arbitrageurs buying HYPE from the pool and exiting through about $2.9M of Solana HYPE liquidity or the Wormhole bridge. In a fast HYPE crash this may not deleverage the pool quickly enough. That raises the chance that xHYPE is pushed deep into the sell zones, where the redeem fee is 8% in Sell Zone 2, or into the Destabilized zone.
- **The market-cap cap can distort prices.** If demand pushed xHYPE toward the $3M cap, protocol mints would be blocked, and the DEX price could trade at a premium to NAV. Buying such a premium is a hidden cost.
- **Memecoin pools are low-quality liquidity.** Liquidity in memecoin/xHYPE pools can vanish, so it adds depth that is not reliable. Some xHYPE demand may also be speculative and transient.
- **Copycat tokens.** Users must verify mint addresses (7ga6rt… for xHYPE and 2zCo6b… for xBTC) because of the copycat and ticker-collision tokens.

### Gaps
- No holder-by-holder breakdown was obtained, so it is unknown whether the top holders are DEX pools, the team or whales.
- Wormhole NTT security settings (rate limits, the transceiver/guardian set) for HYPE were not found.
- No independent audit of the xHYPE pair configuration beyond the Accretion V2 audit (July 2026) was identified. The audit report contents were not reviewed.

## 6. Practicalities: how to buy and sell, expected slippage, wallets and points

### Takeaway
Buy or sell xHYPE and xSOL with any Solana wallet (Phantom, Solflare, Backpack and similar), either in the Hylo app (hylo.so/leverage) or through Jupiter or Titan. Hylo Exchange is integrated as a Jupiter route, and USDC or SOL work as inputs through aggregators.

For $1k–$4k trades on 30 Sep:
- Buying xHYPE cost about 0–0.15% above mid, but selling cost about 1.6–1.7% below mid, so a round trip costs about 1.7–1.8%.
- A round trip in xSOL cost about 0.2–0.3%.
- A round trip in xBTC cost about 0.1–0.4%.

Minting directly in the protocol costs 1% in and 1% out. XP is documented at 20 XP/$/day for xSOL and xBTC; the XP rate for xHYPE is unverified.

### Cited Findings
**Direct protocol routes (SDK)**
- xHYPE: HYPE (Wormhole) or hyUSD in, redeem to HYPE or hyUSD.
- xBTC: cbBTC or hyUSD.
- xSOL: jitoSOL, hyloSOL or hyUSD.
- hyUSD can be minted and redeemed with USDC, cbBTC, HYPE, jitoSOL or hyloSOL.
- [SDK runtime_quote_strategy.rs](https://github.com/hylo-so/sdk/blob/main/hylo-quotes/src/runtime_quote_strategy.rs)
- Where to transact:
  - The Hylo app mint page is hylo.so/leverage. — [xAssets product guide](https://docs.hylo.so/product-guide/xassets)
  - DEX routers such as Titan and Jupiter pick the cheapest pool. The SDK includes a Jupiter AMM implementation (hylo-jupiter), and Jupiter's program-label list maps HYEXCH… to "Hylo Exchange". — [Dynamic Collateral Routing](https://docs.hylo.so/protocol-overview/dynamic-collateral-routing); [Developer Resources](https://docs.hylo.so/developer-resources); [Jupiter labels](https://lite-api.jup.ag/swap/v1/program-id-to-label)
  - Phantom has an xHYPE trading page. — [Phantom xHYPE](https://phantom.com/tokens/solana/7ga6rtE9qSb3wdEiDCpTu2kHqoGVfT52jD8ign1rYTvx)

**Jupiter quotes, 30 Sep 2026 10:20–10:21 UTC, 1% slippage setting.** Effective prices are compared with the Jupiter mid prices: xHYPE $2.2170, xSOL $0.09117 and xBTC $2.1363. — [Jupiter Quote API](https://lite-api.jup.ag/swap/v1/quote)

| Trade | $1,000 | $2,000 | $4,000 | Main route |
|---|---|---|---|---|
| USDC → xHYPE | $2.2174 (+0.02%) | $2.2173 (+0.02%) | $2.2203 (+0.15%) | Meteora DLMM (+Orca, +Hylo mint at $4k) |
| xHYPE → USDC | $2.1793 (−1.70%) | $2.1822 (−1.57%) | $2.1799 (−1.67%) | Meteora + Hylo Exchange redeem (73–87%) |
| USDC → xSOL | $0.091578 (+0.45%) | $0.091603 (+0.48%) | $0.091689 (+0.57%) | Orca Whirlpool, prop AMMs |
| xSOL → USDC | $0.091425 (+0.28%) | $0.091423 (+0.28%) | $0.091423 (+0.28%) | Hylo Exchange redeem → USDC |
| USDC → xBTC | $2.1401 (+0.18%) | $2.1431 (+0.32%) | $2.1472 (+0.51%) | Meteora DLMM |
| xBTC → USDC | $2.1389 (+0.12%) | $2.1395 (+0.15%) | $2.1394 (+0.15%) | Hylo Exchange redeem → USDC |

**Hylo-only quotes (Jupiter restricted to the "Hylo Exchange" route), same time** — [Jupiter Quote API](https://lite-api.jup.ag/swap/v1/quote)

| Direction | xHYPE | xBTC | xSOL |
|---|---|---|---|
| hyUSD → xAsset (mint via hyUSD) | $2.2310/xHYPE | $2.1858 | $0.093325 |
| xAsset → hyUSD (redeem to hyUSD) | $2.1803 | $2.1397 | $0.091415 |
| Collateral → xAsset | 10 HYPE → 387.98 xHYPE | 0.02 cbBTC → 765.94 xBTC | 10 jitoSOL → 16,691 xSOL |

- These quotes are consistent with the on-chain 1%/1% fees around the snapshot NAVs of $2.196, $2.162 and $0.0923.

**Wallets and access**
- All three tokens are Solana SPL tokens (6 decimals), so any Solana wallet works. — [Jupiter token API](https://lite-api.jup.ag/tokens/v2/search?query=7ga6rtE9qSb3wdEiDCpTu2kHqoGVfT52jD8ign1rYTvx)
- Minting xHYPE directly with collateral needs Wormhole-HYPE on Solana. The Solana DEXs for that token have about $2.88M of liquidity. — [Jupiter HYPE](https://lite-api.jup.ag/tokens/v2/search?query=98sMhvDwXj1RQi5c5Mndm3vPe9cBqPrbLaufMXFNMh5g)
- The xHYPE and xBTC mints carry Jupiter's "verified" tag. Wormhole-HYPE and Hylo's tokens were also reported as "moonshot-verified" / verified on Moonshot. — [Jupiter token API](https://lite-api.jup.ag/tokens/v2/search?query=7ga6rtE9qSb3wdEiDCpTu2kHqoGVfT52jD8ign1rYTvx); [KuCoin trends (Moonshot)](https://www.kucoin.com/news/trends/SOL/6ab78f3074fd460007c57f44)

**Points (XP)**
- XP per $ per day: "xSOL / xBTC: 20", hyUSD 5, hyloSOL+ 5, eHYUSD 1, hyloSOL 1.
- Referrers earn 10% of their referrals' XP. New users with a code get a 5% boost.
- XP runs in seasons.
- [Hylo docs: XP System](https://docs.hylo.so/product-guide/xp-system)
- xHYPE is not listed in the docs' XP table.

**Launch promotion for xHYPE**
- The launch carried a "0% minting fees" promotion. — [Hylo on X (profile/search excerpt)](https://x.com/hylo_so?lang=en); [KuCoin, 18 Aug 2026](https://www.kucoin.com/news/insight/HYPE/6a83b37fec098c000710d543)
- On 30 Sep the on-chain normal-zone mint fee was 1%. — on-chain snapshot

### Inferences
- **Buying xHYPE for a $1k–$4k DCA.**
  - At these sizes, buying through Jupiter or DEX pools is cheaper than minting (about +0.0–0.15% versus about +1.6% for mint via hyUSD).
  - Selling xHYPE is the costly leg: the market for exits is effectively the Hylo redeem path (1% fee) plus thin pools.
  - Budget about 1.7–2% for a full buy-then-sell cycle in xHYPE.
  - For xSOL, the cost is about 0.3% on the market route, or 2% via mint and redeem.
- **Point-in-time quotes.** These prices will vary. In volatile periods, pool spreads widen and Pyth confidence can exceed 1%, which would block protocol mints and redeems. In that case, exits must go through DEX pools alone.
- **What a holder actually owns.** Holding xHYPE gives HYPE-denominated upside only through USD NAV. A holder does not "accumulate HYPE". Redemption returns Wormhole-HYPE on Solana, not native HYPE on Hyperliquid.

### Gaps
- The xHYPE XP rate and current season boosts were not found in the docs or readable announcements.
- The exact duration of the 0% mint-fee promotion is unverified.
- The input tokens the hylo.so UI itself accepts (beyond the SDK's protocol routes) could not be checked because of the Vercel checkpoint.

## 7. Side-by-side comparison: xSOL vs xHYPE (and xBTC) for an investor accumulating SOL or HYPE exposure

### Takeaway
For multi-month accumulation, **xSOL is structurally cheaper and more liquid** than xHYPE. xSOL has no borrow rate while its CR is 135–165% (it paid about 3% of notional at the snapshot's 171% CR), a roughly 0.3% round trip, a $35.8M pool, and a published VaR basis for its 150% target (SOL data 2020–2026). Hylo publishes no VaR analysis for HYPE. xHYPE has a borrow rate of 15% or more on NAV, a roughly 1.7% exit cost, a $2.5M pool, a $3M cap and bridged collateral.

xHYPE offers slightly more leverage today (2.71x versus 2.41x) and exposure to HYPE. Both products share the same catastrophic tail: NAV goes to zero below 100% CR. xSOL's −99% drawdown between Oct 2025 and Jun 2026 shows what a sustained bear market does to these tokens.

### Cited Findings
**Comparison table** (all figures as of 30 Sep 2026 about 10:20–10:30 UTC unless dated). Sources are the on-chain snapshot plus the docs, SDK, Jupiter, GeckoTerminal and CoinGecko links cited in sections 1–6.

| Dimension | xSOL | xHYPE | xBTC |
|---|---|---|---|
| Launch | V1: 2025 (CryptoBriefing and KuCoin say July 2025; Jupiter shows mint created 11 Apr 2025) | 17 Aug 2026 | Mint 13 Jul 2026; public 20 Jul 2026 |
| Chain | Solana | Solana | Solana |
| Collateral | jitoSOL + hyloSOL (LSTs) | Wormhole-NTT HYPE on Solana (no staking) | Coinbase cbBTC |
| Oracle | Pyth SOL/USD + Sanctum LST value | Pyth HYPE/USD (max age 10 s, confidence ≤1%) | Pyth BTC/USD (10 s, ≤1%) |
| Pool TVL | $35.81M | $2.51M | $3.58M |
| CR / zone | 170.7% / Buy Zone 1 | 158.5% / Neutral | 168.4% / Buy Zone 1 |
| Effective leverage | 2.41x | 2.71x | 2.46x |
| NAV / DEX price | $0.09228 / $0.0912–0.0914 | $2.196 / $2.217 | $2.162 / $2.136–2.157 |
| Market cap | $14.83M | $0.93M | $1.46M |
| Market-cap cap | none found | $3.0M | $3.0M |
| Holders / top-holder share | 31,494 / 46.5% | 8,437 / 29.2% | 7,228 / 38.3% |
| Cost of leverage | 0 at CR 135–165%; above that, (m−1)× LST yield (now about 3.3% of notional, about 8% of NAV per year) | 15.04% APR on NAV at CR 135–165% (about 5.5% of notional at 2.71x); up to 30.08% at CR ≥175% | Same curve; now about 20.1% APR on NAV (about 8.2% of notional) |
| Mint / redeem fee (normal) | 1% / 1% | 1% / 1% | 1% / 1% |
| Sell Zone 1 redeem fee | 4% | 1% | 1% |
| Sell Zone 2 redeem fee | 8% | 8% | 8% |
| DEX liquidity (Jupiter) | $838k | $248k | $212.5k |
| 24h DEX volume (Jupiter; organic) | $4.50M ($300k) | $936k ($157k) | $373k ($33k) |
| Round-trip cost, $1k–4k via Jupiter | about 0.2–0.3% | about 1.7–1.8% | about 0.1–0.4% |
| Return since the xHYPE launch window (18 Aug → 30 Sep) | +192% (SOL +55%) | +122–129% (HYPE +46–48%) | – |
| Return since the xBTC launch window (21 Jul → 30 Sep) | +178% (SOL +53%) | – | +71% DEX / +85% NAV (BTC +26–28%) |
| Realized daily beta | 2.53–2.61 | 2.62 | 2.48 |
| Worst close-to-close drawdown in window | −26.5% (SOL −11.1%) | −34.8% (HYPE −12.1%) | −18.1% (BTC −6.8%) |
| Long-run tail evidence | −99.2% from 15 Oct 2025 to 7 Jun 2026 (SOL −69%) | none yet (6 weeks old) | none yet (10 weeks old) |
| Price drop to NAV = 0, static | −41.4% | −36.9% | −40.6% |
| XP | 20 XP/$/day | unverified | 20 XP/$/day |
| Backstop | Shared Earn Pool, 21.6M hyUSD (about 10.4% APY run-rate, derived) | same | same |

- The xSOL launch-date sources are [CryptoBriefing](https://cryptobriefing.com/hylo-v2-leveraged-equities-solana/), [KuCoin](https://www.kucoin.com/news/flash/hylo-launches-v2-expands-on-chain-leverage-to-stocks-and-multi-asset-collateral) and [Jupiter](https://lite-api.jup.ag/tokens/v2/search?query=4sWNB8zGWHkh6UnmwiEtzNxL4XrN7uK9tosbESbJFfVs).

### Inferences
**The effective annual carry gap favours xSOL.**
- At 2.7x, xHYPE's floor borrow rate (about 15% of NAV per year) is roughly equivalent to paying 5.5% per year on notional HYPE exposure.
- xSOL's carry is zero in Neutral. At the snapshot's Buy Zone 1 CR, it is about 3.3% of notional (about 8% of NAV) until the CR normalizes.
- Over a 12-month DCA, this gap alone could plausibly be 5–15 percentage points of NAV, depending on how long each pool spends in which zone.

**Tail behaviour.** Both tokens can go to zero. xHYPE's pool is closer to the sell zones (−15% static) than xSOL's (−21%). HYPE's volatility and the thin Solana HYPE liquidity also make its deleveraging path less reliable.

**Where xHYPE is better.**
- It is the only on-chain, liquidation-free, roughly 3x HYPE token on Solana.
- Its Sell Zone 1 exit fee is lower.
- It currently has more effective leverage.
- Its holder base is less concentrated by Jupiter's metric.

**Practical guidance for $1k–$4k DCA buys.**
- Buy through Jupiter or DEX pools, not the mint, when the DEX price is at or below NAV + 1%.
- Plan exits with the roughly 1.6% xHYPE sell-side cost in mind.
- Avoid chasing DEX premiums if xHYPE approaches its $3M cap.
- Monitor pool CR, which changes the borrow rate and the sell-zone fees.

**The alternative for "accumulating HYPE units".** An investor who mainly wants to accumulate HYPE units, not leveraged USD exposure, would get that from spot HYPE (or spot SOL). A leveraged token's number of underlying units is not fixed and falls in drawdowns. This is covered by other researchers.

### Gaps
- There is no historical CR or borrow-rate time series, so the realized cumulative borrow cost paid by xBTC and xHYPE holders since launch was not computed.
- There is no official Hylo statistics page (Vercel checkpoint) to cross-check the derived Earn Pool APY or leverage.
- There is no data on xHYPE behaviour in a severe HYPE crash (larger than −25%), because none has occurred since launch.
