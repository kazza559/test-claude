# Saturn (saturn.credit) Pendle markets: YT pricing, cost of carry and points math (snapshot 2026-09-28)

Data timestamp: all live Pendle data was pulled on **2026-09-28 between 11:47:17 and 11:55:05 UTC**. The Pendle v1 market endpoint reports `dataUpdatedAt = 2026-09-28T11:47:00Z`, price stamps are `2026-09-28T11:47:30Z`, and the v2 `/data` endpoint reports `timestamp = 2026-09-28T11:00:00Z`. The Pendle API was reachable and every number below comes from live API responses, not from snapshots.

API endpoints used (Pendle V2 API docs: [api-v2.pendle.finance/core/docs](https://api-v2.pendle.finance/core/docs)):
- Market list (803 markets on chains 1, 10, 56, 143, 146, 196, 4663, 5000, 8453, 9745, 999, 42161, 80094): `GET https://api-v2.pendle.finance/core/v1/markets/all?limit=100`
- Market detail (YT and PT prices, APYs, reward breakdown): `GET https://api-v2.pendle.finance/core/v1/{chainId}/markets/{address}`
- Market data: `GET https://api-v2.pendle.finance/core/v2/{chainId}/markets/{address}/data`
- Daily history: `GET https://api-v2.pendle.finance/core/v3/{chainId}/markets/{address}/historical-data?time_frame=day&fields=timestamp,impliedApy,underlyingApy,ytPrice,ptPrice,syPrice,tvl,totalTvl,tradingVolume,...`
- Spot swap rates: `GET https://api-v2.pendle.finance/core/v1/sdk/{chainId}/markets/{address}/swapping-prices`
- Executable quotes for buying YT: `POST https://api-v2.pendle.finance/core/v3/sdk/{chainId}/convert` with inputs = USDat (or sUSDat/srUSDat where USDat is not an input token), outputs = YT, slippage 1%, aggregator off, limit orders on.
- DefiLlama yields: `GET https://yields.llama.fi/pools`

Pendle app pages have the form `https://app.pendle.finance/trade/markets/{market}/swap?view=yt&chain={ethereum|bnbchain|monad}`. I did not scrape these pages because they are JS-rendered.

---

## Q1. Which Pendle markets are on Saturn assets (chain, address, SY, expiry, days, TVL, volume)?

### Takeaway
Pendle lists **7 live markets** on Saturn-linked assets, all expiring **2027-01-14**, which is **108 calendar days** after 2026-09-28 (107.5 days from the snapshot time):
- **USDat** on Ethereum, BNB and Monad.
- **sUSDat** on Ethereum and Monad.
- **srUSDat** on Ethereum and Monad. srUSDat is Strata's senior tranche built on USDat and staked USDat. Pendle labels its protocol "Strata" but tags it `saturn`.

A previous series expired on 2026-08-27. I found no Saturn markets on Arbitrum, Base, Plasma, HyperEVM, Sonic, Berachain, Mantle or the other chains. Measured by pool liquidity, the deepest pools are Ethereum USDat ($1.96M), Monad sUSDat ($1.61M), Monad USDat ($1.47M) and Ethereum sUSDat ($1.35M). The BNB USDat pool is tiny ($42.5k).

### Cited Findings
- **The tokens are the genuine saturn.credit assets.** Saturn's Key Addresses page lists:
  - USDat on Ethereum: `0x23238f20b894f29041f48D88eE91131C395Aaa71`
  - sUSDat on Ethereum: `0xD166337499E176bbC38a1FBd113Ab144e5bd2Df7`
  - USDat on BNB and Monad: `0x0Bb150DFa86EA5d7742F07FEfCD8E8edA81D64eF`
  - sUSDat on BNB and Monad: `0x9cd57d3685e6868cacaa8bdcaaf52cbdebf4fa25`

  These are exactly the `underlyingAsset` / `accountingAsset` addresses in the Pendle markets below — [Saturn Key Addresses](https://saturncredit.gitbook.io/saturn-docs/operations-and-governance/key-addresses); [Pendle markets/all API](https://api-v2.pendle.finance/core/v1/markets/all?limit=100)
- **Excluded as unrelated:** the "satUSD+" markets (protocol "River", BNB) matched a "sat" search but are not Saturn assets — [Pendle markets/all API](https://api-v2.pendle.finance/core/v1/markets/all?limit=100)
- **Live markets.** Liquidity is AMM pool TVL. Total TVL includes floating PT outside the AMM. Volume is 24h. Source: [Pendle v1 market detail API](https://api-v2.pendle.finance/core/v1/1/markets/0x4ccf6deb3d1895373f604b418ff55d8adae8b846) (the same endpoint per chain/address) and [markets/all](https://api-v2.pendle.finance/core/v1/markets/all?limit=100). All markets expire 2027-01-14, 108 days out.

| # | Chain (id) | Market (LP) address | SY → underlying | Liquidity | Total TVL | 24h vol |
|---|---|---|---|---|---|---|
| 1 | Ethereum (1) | `0x4ccf6deb3d1895373f604b418ff55d8adae8b846` | SY-USDat `0x7a7de491…a0a9` → USDat | $1,957,451 | $20,445,982 | $425,611 |
| 2 | Ethereum (1) | `0xb6fe0f0811931a38aa97534bac3c147437223e38` | SY-sUSDat `0x8917f8c7…89f9` → sUSDat (pyUnit "USDat staked in Saturn") | $1,347,975 | $6,121,623 | $4,077 |
| 3 | Ethereum (1) | `0xdf2e3e0250f679d6284a39a0c1a16a850a9d7aa6` | SY-srUSDat `0x9d0fc59f…3185` → srUSDat (Strata; pyUnit "USDat staked in Strata") | $229,282 | $910,458 | $16,859 |
| 4 | BNB (56) | `0x48fd92fd80e0256d455e82b7709b265fe44da9d2` | SY-USDat `0x81a77db8…8277` → USDat | $42,549 | $90,354 | $1,298 |
| 5 | Monad (143) | `0x22c2967cc989c313c8c3f205468a11f40f0a95f7` | SY-sUSDat `0x8d3127aa…c286` → sUSDat | $1,612,143 | $4,721,890 | $0 |
| 6 | Monad (143) | `0x88c5d8a908834e44b421cb67aec9a931782f9538` | SY-USDat `0x0898c334…f274` → USDat | $1,468,038 | $42,810,617 | $274,122 |
| 7 | Monad (143) | `0xc945210f85b55946eb970f427e4b9150fff600de` | SY-srUSDat `0xa544d9b7…8c51` → srUSDat (Strata) | $363,090 | $1,090,332 | $4,204 |

- **PT and YT token addresses** — [Pendle v1 market detail API](https://api-v2.pendle.finance/core/v1/1/markets/0x4ccf6deb3d1895373f604b418ff55d8adae8b846):

| Market | PT | YT |
|---|---|---|
| ETH USDat | `0xba96292ee7673e3b546cc90db6d97111cd9a314f` | `0x480c3c9470fa4bbda030f6396fa4b17adefc1ce0` |
| ETH sUSDat | `0x0b985c624bb2949432cce77cfd246f01390a0517` | `0xc38901aa77112efc519a1f8bd501eb2f68055689` |
| ETH srUSDat | `0x2c3e7c0fab3d546ea0715d2a96fbdf598711a062` | `0xf26e7953bab8b301945bb551b4607dffa8500de0` |
| BNB USDat | `0x476aa4205b4eac187011fd8fa07e53d445f213fc` | `0x99010c74fb8733d399b21a5880cee15b35dc5773` |
| Monad sUSDat | `0x2e570a44909df47c4cad13c626626f59d056e9da` | `0x3ebb97649af955e86699444aabc5aee3787bb7ce` |
| Monad USDat | `0xa08a69ab9dd3b04d0992bc7afb2c0b907bbdc147` | `0x5aff25c86c7cb739e554be8904b32047738b7440` |
| Monad srUSDat | `0x355e82c60d51d6942bdfd0f2b95a204acd068963` | `0x0435a599e3fcf2e53028760060499350e25c3dd2` |

- **Expired markets (27-Aug-2026 series), included for history:**
  - Ethereum: USDat `0x9afe7a05…4329`, sUSDat `0x91bc8689…a189`, srUSDat `0x4237a8ac…02b8`, jrUSDat `0x8cef2919…270a`
  - BNB: USDat `0x9757834d…52d9`, sUSDat `0x1017e73c…5387`
  - Monad: USDat `0x1519fb0d…afa`

  There is no live jrUSDat market and no BNB sUSDat market for Jan-2027 — [Pendle markets/all API](https://api-v2.pendle.finance/core/v1/markets/all?limit=100)
- Pendle tags the markets `stables`, `points`, `rwa`, `strc` and `saturn`. Ethereum USDat also has `points-market`. The Ethereum USDat market was created 2026-08-08 and whitelisted in the Pendle "Pro" UI on 2026-08-10. It is `isWhitelistedSimple=false` and `votable=false` — [Pendle v1 market detail](https://api-v2.pendle.finance/core/v1/1/markets/0x4ccf6deb3d1895373f604b418ff55d8adae8b846)
- DefiLlama agrees on pool TVLs:
  - Pendle ETH USDat $1.957M, Monad sUSDat $1.612M, Monad USDat $1.468M, ETH sUSDat $1.348M, BNB USDat $42.5k.
  - Saturn's sUSDat vault itself has $66.05M TVL.

  — [DefiLlama yields API](https://yields.llama.fi/pools)

### Inferences
- Total TVL ($20.4M on ETH USDat, $42.8M on Monad USDat) is 10–30× pool liquidity. Most PT sits outside the AMM, largely as collateral: DefiLlama shows $23.9M of PT-USDat on Morpho Monad and $7.6M on Morpho Ethereum. YT size you can trade without large impact is therefore limited by pool liquidity, not by headline TVL.
- The srUSDat markets are built by Strata on Saturn's USDat and sUSDat. They qualify as Saturn-related (Saturn's own points table lists them), but the SY is a Strata tranche token, which adds Strata tranche risk.

### Gaps
- I did not check Spectra or Napier, because Pendle markets exist.

---

## Q2. YT and PT prices, implied and underlying APY, long-yield APY, fixed APY and points multipliers

### Takeaway
YT prices are $0.023–0.046 per unit, and each YT gives exposure to 1 USDat (≈$1).
- **USDat YTs:** implied APY is **8.3–9.1%**. Intrinsic underlying yield is **0%**, because USDat is non-yielding. Pendle shows a 3% USDC "external reward" whose continuation is uncertain.
- **sUSDat YTs:** implied APY is **12.9% (ETH) and 17.4% (Monad)**, against a Pendle-reported underlying APY of about 15.9–16.4%. Realized sUSDat NAV growth has been much lower and more volatile.
- **Season 2 points multipliers:** YT-USDat 30×, YT-sUSDat 10×, YT-srUSDat 15× (Ethereum only). LP gets half the YT multiplier.

### Cited Findings
- **Price and APY table** as of 2026-09-28 ~11:47 UTC. The USDat price was $0.99992.
  - "Long-yield APY" is Pendle's `ytFloatingApy`. "Fixed APY" is the PT implied APY.
  - "LP APY" is Pendle's `aggregatedApy` (swap fee + PENDLE + underlying + PT fixed), shown next to the max-boosted figure.
  - Source: [Pendle v1 market detail API](https://api-v2.pendle.finance/core/v1/143/markets/0x88c5d8a908834e44b421cb67aec9a931782f9538); the same fields are in [markets/all](https://api-v2.pendle.finance/core/v1/markets/all?limit=100).

| Market | YT price $ | PT price $ | Implied APY (= PT fixed) | Underlying APY Pendle shows for YT | Long-yield APY | LP APY / max boosted | Pool fee rate |
|---|---|---|---|---|---|---|---|
| ETH USDat | 0.02502 | 0.97491 | 8.98% | 3.00% (0% interest + 3.00% USDC "EXTERNAL_REWARD") | −97.5% | 9.31% / 13.84% | 0.169% |
| ETH sUSDat | 0.03506 | 0.96208 | 12.92% | 15.91% (interest) | +86.1% | 15.93% / 16.62% | 0.230% |
| ETH srUSDat | 0.02821 | 0.97172 | 10.20% | 8.11% (interest) | −56.5% | 9.21% / 9.21% | 0.181% |
| BNB USDat | 0.02317 | 0.97675 | 8.29% | 0.00% | −100% | 13.85% / 13.85% | 0.165% |
| Monad sUSDat | 0.04605 | 0.95131 | 17.41% | 16.35% (interest) | −19.5% | 17.64% / 18.19% | 0.313% |
| Monad USDat | 0.02532 | 0.97461 | 9.10% | 3.00% USDC; also 1.74% MON YT-only incentive | −88.1% | 7.44% / 12.68% | 0.171% |
| Monad srUSDat | 0.02875 | 0.97133 | 10.41% | 8.25% (interest) | −56.9% | 10.28% / 10.91% | 0.198% |

- **YT prices in underlying units** (USDat per YT): ETH USDat 0.02502, ETH sUSDat 0.03506, ETH srUSDat 0.02821, BNB USDat 0.02318, Monad sUSDat 0.04606, Monad USDat 0.02532, Monad srUSDat 0.02875 — [Pendle v1 market detail API](https://api-v2.pendle.finance/core/v1/1/markets/0x4ccf6deb3d1895373f604b418ff55d8adae8b846)
- **Spot swap rates** (1 USDat → YT):
  - ETH USDat: 1 USDat → 39.207 YT; YT → 0.024536 USDat.
  - BNB USDat: 1 USDat → 40.503 YT.
  - ETH srUSDat: 1 srUSDat → 35.918 YT.

  — [swapping-prices ETH USDat](https://api-v2.pendle.finance/core/v1/sdk/1/markets/0x4ccf6deb3d1895373f604b418ff55d8adae8b846/swapping-prices); [swapping-prices BNB](https://api-v2.pendle.finance/core/v1/sdk/56/markets/0x48fd92fd80e0256d455e82b7709b265fe44da9d2/swapping-prices)
- **What 1 YT represents.** For sUSDat and srUSDat the Pendle `pyUnit` is "USDat staked in Saturn" / "USDat staked in Strata", and the accounting asset is USDat. 1 YT therefore represents the yield (and points) on 1 USDat of principal, not on 1 sUSDat. This is consistent with PT + YT ≈ 1 USDat in every market: ETH USDat 0.97491 + 0.02502 = 0.99993; Monad sUSDat 0.95131 + 0.04605 = 0.99737 — [Pendle v1 market detail](https://api-v2.pendle.finance/core/v1/1/markets/0xb6fe0f0811931a38aa97534bac3c147437223e38)
- **USDat YTs have 0% intrinsic yield.** Pendle reports `underlyingInterestApy = 0` for USDat. USDat is "a non-yielding stablecoin backed 100% by tokenized U.S. Treasuries" — [Pendle v1 market detail](https://api-v2.pendle.finance/core/v1/1/markets/0x4ccf6deb3d1895373f604b418ff55d8adae8b846); [CoinGecko Learn](https://www.coingecko.com/learn/strategy-strc-defi-strc-yield-saturn-pendle)
- **The 3% USDC reward on USDat YT is an external incentive, not intrinsic yield.** It appears in Pendle history from **2026-09-09** on both the Ethereum and Monad USDat markets, and is exactly 0.0300 every day since — [Pendle historical-data API](https://api-v2.pendle.finance/core/v3/1/markets/0x4ccf6deb3d1895373f604b418ff55d8adae8b846/historical-data?time_frame=day)
  - CoinMarketCal/TradingView reported that Saturn would fund $32k of YT incentives ($8k per week) on the Jan-14 Ethereum USDat market, co-distributed with PENDLE, from **27 Aug to 27 Sep 2026**. On that dating the program ended the day before this snapshot — [TradingView/CoinMarketCal](https://www.tradingview.com/news/coinmarketcal:9fe81b1c1094b:0-pendle-usdat-yt-incentives-support-the-rollover-27-aug-2026-to-27-sep-2026/)
- **The Monad USDat MON reward is short-lived.** It is a Pendle "PORTAL_INCENTIVE", YT-exclusive, 1,019,359 MON (MON = $0.02817, ≈ $28.7k), running 2026-09-17 to **2026-10-01** — [markets/all ytApyBreakdown](https://api-v2.pendle.finance/core/v1/markets/all?limit=100)
- **sUSDat yield mechanism.**
  - Yield comes from STRC holdings and vests linearly over 30 days.
  - sUSDat value is `totalAssets = usdatBalance + (vestedStrcBalance × strcPrice)`, so NAV is marked to the STRC market price.
  - Staking fee is 10 bp. Unstaking goes through a queue (3–7 days).

  — [Saturn Staking & Unstaking](https://saturncredit.gitbook.io/saturn-docs/solution/susdat-overview/staking-and-unstaking-process); [Saturn Allocations](https://saturncredit.gitbook.io/saturn-docs/overview/allocations)
- Saturn charges a 10% protocol fee on sUSDat yield, but returns 100% of it to sUSDat holders during an unspecified bootstrap period — [Saturn Fees & Risk Reserve](https://saturncredit.gitbook.io/saturn-docs/operations-and-governance/fees-and-risk-reserve)
- **Cross-checks on the underlying APY:**
  - DefiLlama shows Saturn sUSDat (Ethereum) at **14.49%** APY with a 30-day mean of 14.83%, and Strata srUSDat at 8.11% — [DefiLlama yields](https://yields.llama.fi/pools)
  - The STRC dividend rate was cited as 11.50% annualized, paid monthly, in May 2026 — [CoinGecko Learn](https://www.coingecko.com/learn/strategy-strc-defi-strc-yield-saturn-pendle)
- **Season 2 "Orbital Points" multipliers** (identical on Ethereum, BNB and Monad):

| Position | Multiplier |
|---|---|
| Hold USDat | 5× |
| Hold sUSDat | 1× |
| Curve USDC/USDat and USDC/sUSDat LP | 25× |
| PancakeSwap USDT/USDat and USDT/sUSDat LP (active range) | 25× |
| Pendle USDat LP | 15× |
| **Pendle YT-USDat** | **30×** |
| Pendle sUSDat LP | 5× |
| **Pendle YT-sUSDat** | **10×** |
| Pendle srUSDat LP (Ethereum only) | 7.5× |
| YT-srUSDat (Ethereum only) | 15× |
| Pendle jrUSDat LP | 5× |
| YT-jrUSDat | 10× |
| Strata srUSDat | 1× |
| Strata jrUSDat | 5× |

  Source: [Saturn Orbital Points – Season 2](https://saturncredit.gitbook.io/saturn-docs/overview/orbital-points-season-2); [Saturn Allocations](https://saturncredit.gitbook.io/saturn-docs/overview/allocations)
- **Season 2 dates:** 12:00 AM ET on **Aug 9, 2026** to 11:59 PM ET on **Dec 8, 2026**, or when Saturn TVL reaches $1B, whichever comes first. Up to 5% of initial token supply may go to Season 2, conditioned on a governance token launch. Users with more than 1,000,000 Season 1 Gravity Points get a **20% Orbital Points boost**. Saturn may add temporary campaigns or boosts — [Saturn Orbital Points – Season 2](https://saturncredit.gitbook.io/saturn-docs/overview/orbital-points-season-2)
- **Season 1 (Gravity, Apr 8 – Aug 8, 2026)** had chain-specific multipliers:
  - YT-USDat: 30× on Ethereum, 36× on BNB, 38× on Monad.
  - The Season 1 table header was "Points/Day" and read "Hold USDat 7×".

  — [Saturn Gravity Points – Season 1](https://saturncredit.gitbook.io/saturn-docs/overview/gravity-points-season-1)
- **Past boosts:**
  - A "Gravity Accelerate" campaign (ended June 6, 2026) doubled Pendle rates for the Aug-2026 markets: Ethereum 60× YT / 30× LP, BNB 72× YT / 36× LP — [Today in DeFi, June 3 2026](https://news.todayindefi.com/p/airdrop-alpha-saturn-and-apyx-boosted)
  - Double points ran on the Monad USDat and sUSDat Pendle markets from **Aug 4–13, 2026**, with MON rewards for YT — [Bitget News](https://www.bitget.com/news/detail/12560605648916)
- The Saturn app strategies page, rendered server-side, shows Hold USDat 5×, Hold sUSDat 1×, Curve 25×, Morpho 1–2×, Strata srUSDat 1× and jrUSDat 5×. The Pendle rows are not in the server HTML — [app.saturn.credit/strategies](https://app.saturn.credit/strategies)

### Inferences
- **Base points rate.** "1×" most plausibly means 1 point per $1 of exposure per day, because the Season 1 table's column is labelled "Points/Day". No page states the base rate explicitly, so all point counts below assume B = 1 pt / $ / day. If B differs, point counts scale linearly and $/point scales as 1/B.
- **ETH sUSDat is the only market where the Pendle-reported underlying APY (15.9%) is above implied (12.9%)**, hence the +86% long-yield APY. That reported APY is noisy: its daily values ranged roughly 7% to more than 200% in September, and realized NAV growth is much lower (see Q5). Treat the 86% long-yield figure as unreliable.
- **USDat YT buyers now pay about 9% implied for 0% intrinsic yield.** Any 3% USDC top-up, if it continues, only partly offsets the cost.

### Gaps
- I could not retrieve the multiplier badge shown in the Pendle UI. The Pendle API has no points field, and the app is JS-rendered. Multipliers above come from Saturn docs only.
- Monad srUSDat YT and LP are **not listed** in Saturn's Season 2 table, which lists srUSDat only for Ethereum. Whether they earn Orbital Points is unconfirmed.
- One search-engine summary said double points are "live now" on the Jan-14-2027 Monad USDat and sUSDat markets. I found no primary source confirming a double-points campaign after Aug 13, 2026, so I did not apply it.
- I found no primary source on whether the 3% USDC YT reward continues after Sep 27, 2026.

---

## Q3. Cost of holding YT for $1,000 of capital: units, exposure, yield returned, net cost, points and breakeven $/point

### Takeaway
Using executable Pendle quotes for $1k, including fees and price impact:
- **YT-USDat (Ethereum and Monad)** buys about 38–39k YT, i.e. **about $38–39k of points exposure**. That earns about **1.09–1.12M points/day**, or **78–80M points** over the ~71.7 days left in Season 2 (30×, after Pendle's 5% points fee).
- **Net cost** is **$675–683** if the 3% USDC reward runs to expiry, or **$1,000** if it has ended. Breakeven is **$8.4–8.8 per 1M points** (with USDC) or **$12.5–12.8 per 1M points** (without).
- **YT-sUSDat** is only 10× and its economics depend on sUSDat NAV growth. It runs from roughly free (at the Pendle-reported 16% APY) to **$53–69 per 1M points** if STRC weakness pushes YT yield to zero.
- **YT-USDat is the cheapest points source per dollar.**

### Cited Findings
- **Inputs** — [Pendle convert API](https://api-v2.pendle.finance/core/v3/sdk/1/convert) (quotes 11:52:46–11:55:05 UTC); [Pendle v1 market detail](https://api-v2.pendle.finance/core/v1/1/markets/0x4ccf6deb3d1895373f604b418ff55d8adae8b846); [Saturn Season 2](https://saturncredit.gitbook.io/saturn-docs/overview/orbital-points-season-2); [Pendle Fees doc](https://docs.pendle.finance/pendle-v2/ProtocolMechanics/Mechanisms/Fees)
  - $1k YT quotes:

    | Market | Input | YT out |
    |---|---|---|
    | ETH USDat | 1,000 USDat | 39,150.58 |
    | ETH sUSDat | USDat | 27,469.89 |
    | ETH srUSDat | USDat | 31,647.95 |
    | Monad sUSDat | sUSDat | 21,223.08 |
    | Monad USDat | USDat | 38,125.41 |
    | Monad srUSDat | srUSDat | 32,325.25 |
    | BNB USDat | USDat | **no route at $1k**; $100 → 3,881.00 YT; $500 → 14,881.63 YT |

  - Time to expiry T = 107.51 days (2026-09-28 11:48 UTC → 2027-01-14 00:00 UTC).
  - Remaining Season 2 = 71.72 days (to Dec 8, 2026 11:59 PM ET, i.e. Dec 9 04:59 UTC).
  - Pendle takes 5% of all YT yield, including points.

**Formulas used:**
- N = YT units received for $1,000, from the executable convert quote.
- Exposure E = N × P_USDat, where P_USDat = $0.99992, because 1 YT corresponds to 1 USDat of principal.
- Expected yield to expiry: Y = E × [(1 + APY)^(T/365) − 1] × (1 − 0.05).
- Net cost C = $1,000 − Y. YT value goes to 0 at expiry.
- Points per day = E × M × B × 0.95, with B = 1 pt / $ / day (assumed) and M the Season 2 multiplier.
- Points over Season 2 = points per day × 71.72.
- Breakeven $/point = C / points. It is shown per 1M points.
- APY scenarios:
  - USDat base: 3% USDC reward continues. USDat bear: 0%.
  - sUSDat base: Pendle-reported APY. Bear: 10%. Realized: 6.4%, the Apr–Sep annualized NAV growth. Stress: 0%, NAV below its prior high.
  - srUSDat base: Pendle 8.11–8.25%. Bear: 6%.

**Results for $1,000 at executable prices:**

| Market (mult.) | YT units N | Exposure E | Scenario APY | Yield Y to expiry | Net cost C | Points/day | Points to S2 end (71.7 d) | Breakeven $ per 1M pts | If points ran to expiry (107.5 d) |
|---|---|---|---|---|---|---|---|---|---|
| ETH USDat (30×) | 39,150.6 | $39,147 | 3% USDC | $325.20 | $674.80 | 1,115,702 | 80.0M | **$8.43** | $5.63 |
| ETH USDat (30×) | 39,150.6 | $39,147 | 0% | $0 | $1,000.00 | 1,115,702 | 80.0M | **$12.50** | $8.34 |
| Monad USDat (30×) | 38,125.4 | $38,122 | 3% USDC | $316.69 | $683.31 | 1,086,487 | 77.9M | **$8.77** | $5.85 |
| Monad USDat (30×) | 38,125.4 | $38,122 | 0% | $0 | $1,000.00 | 1,086,487 | 77.9M | **$12.83** | $8.56 |
| BNB USDat (30×), $100 ticket | 3,881.0 | $3,881 | 0% | $0 | $100 | 110,600 | 7.93M | **$12.61** | — |
| BNB USDat (30×), $500 ticket | 14,881.6 | $14,880 | 0% | $0 | $500 | 424,093 | 30.4M | **$16.44** | — |
| ETH sUSDat (10×) | 27,469.9 | $27,468 | 15.91% (Pendle) | $1,159.67 | −$159.67 (gain) | 260,943 | 18.7M | < $0 | < $0 |
| ETH sUSDat (10×) | 27,469.9 | $27,468 | 10% | $742.92 | $257.08 | 260,943 | 18.7M | **$13.74** | $9.16 |
| ETH sUSDat (10×) | 27,469.9 | $27,468 | 6.4% realized | $481.19 | $518.81 | 260,943 | 18.7M | **$27.72** | — |
| ETH sUSDat (10×) | 27,469.9 | $27,468 | 0% stress | $0 | $1,000 | 260,943 | 18.7M | **$53.43** | — |
| Monad sUSDat (10×) | 21,223.1 | $21,221 | 16.35% (Pendle) | $919.58 | $80.42 | 201,603 | 14.5M | **$5.56** | $3.71 |
| Monad sUSDat (10×) | 21,223.1 | $21,221 | 10% | $573.98 | $426.02 | 201,603 | 14.5M | **$29.46** | $19.66 |
| Monad sUSDat (10×) | 21,223.1 | $21,221 | 6.4% realized | $371.76 | $628.24 | 201,603 | 14.5M | **$43.45** | — |
| Monad sUSDat (10×) | 21,223.1 | $21,221 | 0% stress | $0 | $1,000 | 201,603 | 14.5M | **$69.16** | — |
| ETH srUSDat (15×) | 31,648.0 | $31,645 | 8.11% | $698.49 | $301.51 | 450,947 | 32.3M | **$9.32** | $6.22 |
| ETH srUSDat (15×) | 31,648.0 | $31,645 | 6% | $520.42 | $479.58 | 450,947 | 32.3M | **$14.83** | $9.89 |
| Monad srUSDat (? not listed) | 32,325.3 | $32,323 | 8.25% / 6% | $725.41 / $531.56 | $274.59 / $468.44 | unconfirmed | — | — | — |

- **Mid-price (no-impact) reference values** — [Pendle v1 market detail](https://api-v2.pendle.finance/core/v1/1/markets/0x4ccf6deb3d1895373f604b418ff55d8adae8b846):

  | Market | YT per $1k at mid | Breakeven $ per 1M pts |
  |---|---|---|
  | ETH USDat | 39,972 | $8.18 with USDC / $12.24 without |
  | Monad USDat | 39,500 | $8.32 / $12.39 |
  | BNB USDat | 43,151 | $11.34 (theoretical; not executable at $1k) |

- **Sanity check on USDat YT carry:** YT price ÷ days = 0.02502 / 107.5 = $0.000233 per $1 of exposure per day. At 30× × 0.95 = 28.5 pts / $ / day, that is $8.2 per 1M points if points ran to expiry. It rises to $12.2 per 1M because the season ends about 36 days before expiry — [Pendle v1 market detail](https://api-v2.pendle.finance/core/v1/1/markets/0x4ccf6deb3d1895373f604b418ff55d8adae8b846)

### Inferences
- **Season end vs expiry is the key mismatch.** Season 2 ends Dec 8, 2026, and it ends earlier if TVL hits $1B or, per a community report, if TGE comes first. The YTs expire Jan 14, 2027. Holding to expiry pays for about 36 days of decay with no committed points. For USDat YT, which has no intrinsic yield, YT demand after the season likely collapses. Selling around Dec 8 might recover a small residual; I did not model it because it depends on unknown post-season demand.
- **$/point only becomes a buy/no-buy signal against a valuation.** Break-even requires the airdrop to be worth at least about $12.5 per 1M Orbital Points (USDat YT, no USDC reward). The Season 2 pool is "up to 5% of initial token supply", so breakeven FDV = (total Season 2 points × $/pt) / 0.05. Total points outstanding is not public (see Gaps).
- **S1 boost.** Users with more than 1M Season 1 points get +20% Orbital Points, which cuts breakeven $/pt by 1/1.2, e.g. USDat YT from $12.50 to $10.42 per 1M.
- **sUSDat YT is a leveraged bet on sUSDat NAV growth**, not a pure points play. At 10× it earns only a third of the points per YT that USDat YT earns (30×) and costs 1.4–1.8× more per YT.

### Gaps
- The base points rate B is not stated explicitly anywhere I found.
- Total Orbital Points issued, and therefore market $/point or implied FDV, are not public.
- The exact Pendle YT-to-points attribution formula Saturn uses (e.g. SY-held-by-YT vs YT balance) is not documented. I assumed 1 YT = $1 of exposure.

---

## Q4. Pendle fees, points fee, slippage and price impact for $1k/$10k/$50k, and whether points accrue automatically

### Takeaway
- **Fees:** Pendle takes **5% of all YT yield including points**. Saturn deducts it off-chain when crediting points to wallets.
- **Accrual:** points accrue automatically to the YT holder's wallet, with no claim needed.
- **Swap fees** add about 1.6–1.9% of capital on a YT buy.
- **Price impact:**
  - Monad sUSDat is the deepest pool for YT.
  - ETH USDat and Monad USDat are fine at $1–10k (PI 2–7%) but bad at $50k (−16% and −44%).
  - srUSDat breaks above about $5k.
  - BNB cannot fill $1k.

### Cited Findings
- **Pendle YT fee:**
  - "Pendle collects a 5% fee from all yield accrued (including points) by all YT in existence."
  - "Since points are tracked off-chain, partner protocols deduct the 5% fee when allocating points to user wallets."
  - Swap fees are "percentage-based… scaled with maturity" on PT swaps.

  — [Pendle Docs – Fees](https://docs.pendle.finance/pendle-v2/ProtocolMechanics/Mechanisms/Fees)
- **Quote table.** Effective $/YT is compared with the mid price. PI is the API `priceImpact`, which includes the swap fee. "Implied after" is the pool implied APY after the trade. All quotes were taken on 2026-09-28 at 11:52–11:55 UTC with slippage 1%, aggregator off and limit orders on — [Pendle convert API](https://api-v2.pendle.finance/core/v3/sdk/1/convert)

| Market | Size | YT out | YT per $ | Eff. $/YT vs mid | Price impact | Implied APY after | Fee (USD) |
|---|---|---|---|---|---|---|---|
| ETH USDat | $1k | 39,150.6 | 39.15 | +2.10% | −2.06% | 8.98% → 8.99% | $18.97 |
| ETH USDat | $10k | 370,318 | 37.03 | +7.94% | −7.36% | 8.98% → 9.49% | $179.20 |
| ETH USDat | $50k | 1,678,100 | 33.56 | +19.10% | −16.04% | 8.98% → 10.01% | $809.71 |
| Monad USDat | $1k | 38,125.4 | 38.13 | +3.61% | −3.48% | 9.10% → 9.20% | $18.70 |
| Monad USDat | $10k | 370,832 | 37.08 | +6.52% | −6.12% | 9.10% → 9.78% | $181.71 |
| Monad USDat | $50k | 1,108,794 | 22.18 | +78.1% | −43.86% | 9.10% → 16.30% | $533.19 |
| ETH sUSDat | $1k | 27,469.9 | 27.47 | +3.83% | −3.69% | 12.92% → 13.12% | $17.89 |
| ETH sUSDat | $10k | 264,463 | 26.45 | +7.85% | −7.28% | 12.92% → 14.25% | $171.99 |
| ETH sUSDat | $50k | 938,903 | 18.78 | +51.9% | −34.16% | 12.92% → 21.50% | $600.77 |
| Monad sUSDat | $1k | 21,223.1 | 21.22 | +2.31% | −2.26% | 17.41% → 17.46% | $18.57 |
| Monad sUSDat | $10k | 210,401 | 21.04 | +3.20% | −3.11% | 17.41% → 17.84% | $184.06 |
| Monad sUSDat | $50k | 967,775 | 19.36 | +12.18% | −10.86% | 17.41% → 18.66% | $842.92 |
| ETH srUSDat | $1k | 31,648 | 31.65 | +12.0% | −10.74% | 10.20% → 11.31% | $16.30 |
| ETH srUSDat | $2.5k / $5k | 71,759 / 135,857 | 28.70 / 27.17 | — | −19.04% / −23.37% | → 11.94% / 12.78% | $36.84 / $69.61 |
| ETH srUSDat | $10k, $50k | no route | — | — | — | — | — |
| Monad srUSDat | $1k / $2.5k / $5k | 32,325 / 74,585 / 139,537 | 32.33 / 29.83 / 27.91 | +7.6% / — / — | −7.08% / −14.24% / −19.78% | 10.41% → 11.03% / 11.73% / 12.61% | $18.27 / $42.04 / $78.46 |
| BNB USDat | $100 / $500 | 3,881 / 14,882 | 38.81 / 29.76 | — | −10.06% / −31.03% | 8.29% → 9.08% / 11.95% | $1.83 / $6.98 |
| BNB USDat | $1k+ | no route | — | — | — | — | — |

- **$/point by trade size** (0% yield scenario, 30× or 10×, 5% points fee, 71.72 days) — [Pendle convert API](https://api-v2.pendle.finance/core/v3/sdk/143/convert):

  | Market | $1k | $10k | $50k |
  |---|---|---|---|
  | ETH USDat, $ per 1M pts | $12.50 | $13.21 | $14.58 |
  | Monad USDat, $ per 1M pts | $12.83 | $13.19 | $22.06 |
  | ETH sUSDat, $ per 1M pts | $53.43 | $55.50 | $78.17 |
  | Monad sUSDat, $ per 1M pts | $69.16 | $69.76 | $75.83 |
  | ETH srUSDat, $ per 1M pts | $30.92 | $36.01 at $5k | — |
- The ETH USDat $1k route partly filled against a Pendle limit order (`flashFills`, maker `0x8c743f9c…2026`). Limit-order depth therefore affects the quotes — [Pendle convert API response](https://api-v2.pendle.finance/core/v3/sdk/1/convert)
- **Points accrue automatically.** Points are tracked off-chain and allocated by the partner protocol to user wallets, after the 5% fee — [Pendle Docs – Fees](https://docs.pendle.finance/pendle-v2/ProtocolMechanics/Mechanisms/Fees)
- **YT yield is claimed manually.** YT interest and rewards (e.g. the USDC external reward, the MON portal incentive) are claimed through Pendle. The API offers a `redeem-interests-and-rewards` SDK endpoint — [Pendle API docs](https://api-v2.pendle.finance/core/docs)

### Inferences
- **The swap fee is a large fixed tax on YT.** A YT buy flash-sells about 39× notional of PT, so the ~0.17% rate-based fee costs about 1.9% of capital on USDat YT. Round-tripping (buy, then sell before expiry) roughly doubles that.
- **Practical sizing:**
  - ETH USDat and Monad USDat YT: up to about $10k per market with at most ~8% impact.
  - Monad sUSDat: absorbs $50k at about 11%.
  - Split larger tickets across ETH and Monad USDat, or use limit orders.

### Gaps
- I did not verify whether Saturn's displayed 30× already nets out Pendle's 5% points fee. I applied the 0.95 factor on top.
- The claim mechanics for the 3% USDC external reward (merkle claim vs streamed) are not documented in the sources I found.

---

## Q5. History: how implied APY and YT price have moved, and whether YT is cheap or expensive now

### Takeaway
- **USDat YTs are at the most expensive level of their lives** in implied-APY terms:
  - ETH 8.98%, the maximum of 52 daily points.
  - Monad 9.10%, the 98th percentile.
  - BNB 8.29%, the 96th percentile.
- The jump came after ETH USDat pool liquidity fell from about $5.9M to $1.96M during Sep 17–27. YT-USDat price rose about 25% in 6 days.
- **sUSDat YTs are mid-range** (52nd–54th percentile) and far below their August highs.
- **sUSDat NAV history shows real STRC risk.** NAV fell about 23% in June 2026, and YT-sUSDat on the Aug-2026 market earned **zero** yield from about late May until expiry.

### Cited Findings
- **Daily history** — [Pendle v3 historical-data API](https://api-v2.pendle.finance/core/v3/1/markets/0x4ccf6deb3d1895373f604b418ff55d8adae8b846/historical-data?time_frame=day):
  - **ETH USDat Jan-27** (since 2026-08-08):
    - Implied APY rose from 5.00% at launch (YT $0.0209) to 6.9% (Aug 18–23), 6.1% (early Sep) and 6.74% (Sep 22), then 8.86% (Sep 27) and **8.98% (Sep 28)**. Range 5.00–8.98%.
    - YT price range $0.0194–$0.0287: $0.01998 on Sep 22, $0.02502 now.
    - Pool TVL was $5.94M on Sep 17, $3.45M on Sep 22 and $1.96M on Sep 27. Total TVL rose to $20.4M.
  - **Monad USDat Jan-27** (since 2026-07-27): launched at 8.00%, fell to 5.57% (Aug 1), then 6.3% (early Sep), 7.04% (Sep 20) and **9.10%** now. Range 5.57–9.22%. YT range $0.0206–$0.0398.
  - **BNB USDat Jan-27:** range 3.87–8.58%; 4.47% on Sep 24, then 8.29% on Sep 28. The pool is thin ($42.5k).
  - **ETH sUSDat Jan-27:** launched at 13.0%, peaked at 19.4% (mid-Aug), fell to 10.1% (Sep 7–12), now **12.92%**. YT fell from $0.0715 (Aug) to $0.0351.
  - **Monad sUSDat Jan-27:** range 12.98–32.93%; 20.5–22.7% in early August, **17.41%** now. YT range $0.0457–$0.1203.
  - **ETH srUSDat:** range 8.78–10.50%, now 10.20% (87th percentile). **Monad srUSDat:** range 9.90–15.63%, now 10.41% (39th percentile).
- **Prior generation (Aug-27-2026 expiry)** — [Pendle historical-data API, ETH USDat Aug-26](https://api-v2.pendle.finance/core/v3/1/markets/0x9afe7a057a09cf5da748d952078c9c99938b4329/historical-data?time_frame=day):
  - ETH USDat launched 2026-04-11 at 8.00% implied and ranged **5.04–9.85%** over its life. Total TVL peaked around $72.8M (May 31). YT decayed from $0.0285 to 0 at expiry.
  - Monad USDat Aug-26 ranged 4.84–9.67%.
- **sUSDat NAV**, from the SY-sUSDat USD price on Ethereum — [Pendle historical-data API, ETH sUSDat Aug-26 and Jan-27](https://api-v2.pendle.finance/core/v3/1/markets/0x91bc86899c8391b6caaf26535b9cd82efe49a189/historical-data?time_frame=day):
  - Path: 1.0012 (Apr 11), about 1.008 (mid-May), **0.7780 low (Jun 26)**, 1.0332 high (Sep 22), **1.0306 (Sep 28)**.
  - Realized growth Apr 11 → Sep 28 was +2.93%, or **6.4% annualized**.
  - The last 14 days returned only +0.07% (1.9% annualized), and the current rate is about 0.25% below the Sep 22 high.
- On the expired Aug-26 sUSDat market, Pendle's reported underlying APY for YT was **0** on every weekly sample from May 23 to Aug 22, 2026, after positive values in April and May — [Pendle historical-data API](https://api-v2.pendle.finance/core/v3/1/markets/0x91bc86899c8391b6caaf26535b9cd82efe49a189/historical-data?time_frame=day)
- **Saturn's own account:** TVL "peaked at approximately $248 million before heightened STRC volatility… subsequently stabilized at approximately $180 million", and Saturn holds more than 816,876 STRC shares. Its risk pages cover a Bitcoin price shock and STRC dividend deferral — [Saturn Orbital Points – Season 2](https://saturncredit.gitbook.io/saturn-docs/overview/orbital-points-season-2); [Saturn docs index](https://saturncredit.gitbook.io/saturn-docs/llms.txt)

### Inferences
- **The zero-yield stretch reflects Pendle's YT index mechanics.** As I understand the design, YT interest accrues only when the SY exchange rate exceeds its previously recorded high. After the June STRC drawdown, sUSDat's rate stayed below its May peak, so Aug-26 YT holders received essentially nothing for about 3 months. The zero-APY history is consistent with this.
- **The current Jan-27 sUSDat YT is below its recorded high right now** (1.0306 vs 1.0332). New yield accrues only after NAV recovers about 0.25%.
- **USDat YT is "expensive" now** relative to its own history and the prior series' average of roughly 7–9%. Waiting for liquidity to return, or using limit orders at lower implied APY (6.5–7.5%, where it traded Sep 12–22), would cut cost per point by about 15–25%.

### Gaps
- I did not pull hourly data, so intraday spikes are not captured.
- `ytRoi` (ETH USDat −66.4%, ETH sUSDat +20.1%) is an API field whose exact definition is not documented. I did not use it.

---

## Q6. Alternatives: PT fixed APY and LP (with points)

### Takeaway
- **PT earns the implied APY and no Saturn points:** 8.3–9.1% on USDat, 12.9–17.4% on sUSDat, about 10.2–10.4% on srUSDat.
- **LP earns a similar or higher APY plus Saturn points** at half the YT multiplier (USDat LP 15×). Per dollar, though, LP earns about 1/74th (if credited on full LP value) to 1/178th (if credited on the SY portion only) of the points YT-USDat does: at most 15 pts/$/day, versus about 1,116 pts/day per $ for YT-USDat.
- LP is effectively "free" points at positive carry. YT-USDat is concentrated points at about $12.5 per 1M points.

### Cited Findings
- **LP metrics for $1k LP, held to expiry**, using Pendle aggregatedApy compounded over 107.5 days. Points are unboosted at 1 pt/$/day, with no 5% fee (the Pendle fee applies to YT). SY share = totalSy ÷ pool liquidity — [Pendle v1 market detail](https://api-v2.pendle.finance/core/v1/1/markets/0x4ccf6deb3d1895373f604b418ff55d8adae8b846); [Saturn Season 2](https://saturncredit.gitbook.io/saturn-docs/overview/orbital-points-season-2)

| Market | LP APY | $ yield to expiry | SY share of pool | S2 pts if LP credited on full value | …if credited on SY portion only |
|---|---|---|---|---|---|
| ETH USDat | 9.31% (max 13.84%) | $26.56 | 41.8% | 1.076M | 0.450M |
| Monad USDat | 7.44% (max 12.68%) | $21.36 | 60.1% | 1.076M | 0.646M |
| BNB USDat | 13.85% | $38.95 | 49.8% | 1.076M | 0.535M |
| ETH sUSDat | 15.93% (max 16.62%) | $44.50 | 72.6% | 0.359M | 0.260M |
| Monad sUSDat | 17.64% (max 18.19%) | $49.02 | 25.0% | 0.359M | 0.090M |
| ETH srUSDat | 9.21% | $26.29 | 54.1% | 0.538M | 0.291M |

- **PT fixed APY** equals the implied APY: ETH USDat 8.98%, Monad USDat 9.10%, BNB USDat 8.29%, ETH sUSDat 12.92%, Monad sUSDat 17.41%, ETH srUSDat 10.20%, Monad srUSDat 10.41%. PT holding is not in Saturn's Season 2 points table — [Pendle v1 market detail](https://api-v2.pendle.finance/core/v1/143/markets/0x22c2967cc989c313c8c3f205468a11f40f0a95f7); [Saturn Season 2](https://saturncredit.gitbook.io/saturn-docs/overview/orbital-points-season-2)
- **Composition of Pendle's ETH USDat LP APY:**
  - PT fixed 5.22%.
  - External USDC reward 1.26%.
  - Swap fees 1.06%.
  - PENDLE 1.77% (about 39.5 PENDLE/day to the pool at $2.39).
  - Underlying 0%.

  — [Pendle v1 market detail](https://api-v2.pendle.finance/core/v1/1/markets/0x4ccf6deb3d1895373f604b418ff55d8adae8b846)
- **DefiLlama figures:**
  - Pendle ETH USDat LP 9.33% (30-day mean 4.67%); PT-buy 8.98% (30-day mean 6.79%).
  - Monad sUSDat PT 17.41%.
  - Curve USDC/USDat (Ethereum, $9.47M TVL) earns only 0.15% base but carries 25× Saturn points.

  — [DefiLlama yields](https://yields.llama.fi/pools)
- **Other 25× venues:** Curve USDC/USDat and USDC/sUSDat (Ethereum, Monad) and PancakeSwap active-range pools (BNB) earn 25×, above Pendle LP's 15× — [Saturn Season 2](https://saturncredit.gitbook.io/saturn-docs/overview/orbital-points-season-2)
- **TGE timing (community source):** a KuCoin community post dated Sep 25, 2026 says:
  - 5% of $STRN goes to Season 2.
  - If TGE is before Dec 8, 2026, Season 2 ends early and the allocation is reduced by running days ÷ total days.

  This is secondary and unverified against a primary Saturn post — [KuCoin Insight](https://www.kucoin.com/news/insight/PENDLE/6ab625c874fd460007c54ed9)

### Inferences
- **Opportunity cost for YT:** comparing against PT-USDat (about 9% for 107.5 days ≈ $26 per $1k) adds about $26 to YT's net cost. ETH USDat YT becomes about $1,026, or $12.8 per 1M points with no USDC reward.
- **Curve USDC/USDat looks like the best "points without principal decay" option:** 25× on principal, about 0% yield, no expiry. $1k gives 25k pts/day (1.79M over the season) and costs only the forgone roughly 9% PT yield (≈ $18 over 71.7 days), i.e. about $10 per 1M points of opportunity cost. That is close to YT-USDat's cost, without YT's leverage or the season/expiry mismatch.
  - This is an inference from multipliers and APYs. It does not account for Curve depeg or impermanent-loss risk.
- **LP is best for yield-focused users** who want some points (ETH USDat LP: about 9.3% plus 15×). **YT is only rational** if you value Orbital Points above about $12.5 per 1M (USDat YT, no USDC reward, $1–10k size) and accept that points could end before Dec 8.

### Gaps
- Saturn does not document whether Pendle LP points are credited on the full LP value or only on the SY portion. The difference is up to 4× for Monad sUSDat LP.
- No primary source gives Orbital Points totals or a STRN valuation, so the absolute value of points (and whether $12.5 per 1M is cheap) cannot be determined from these sources.
