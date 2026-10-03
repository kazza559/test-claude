# KNTQ (Kinetiq) — Who Is Buying, Who Is Selling, and Market Structure (as of 2026-10-03)

Provenance tags used below:
- **[V-API]**: verified by me directly against the Hyperliquid public info API (`POST https://api.hyperliquid.xyz/info`), pulled 2026-10-03 ~12:00–12:15 UTC.
- **[V-HS]**: verified via the Hypurrscan public API.
- **[V-RPC]**: verified via the HyperEVM public RPC (`eth_call`).
- **[V-CG/DS/GT]**: pulled from the CoinGecko, DexScreener or GeckoTerminal public APIs on 2026-10-03 ~12:10 UTC.
- **[R]**: reported by a third party and not checked on-chain by me.

Key identifiers [V-API]:
- KNTQ is HyperCore spot token index 124, tokenId `0xbd31bd605c0a1b82c72aae3587f9061f`.
- Its HyperEVM ERC-20 is `0x000000000000780555bd0bca3791f89f9542c2d6`.
- Main market: KNTQ/USDC, spot pair `@334`. The legacy KNTQ/USDH pair is `@254` and is now dormant.
- Max supply is 1,000,000,000.

## 1. Price history, performance, support/resistance, and the $0.26 question

### Takeaway
KNTQ listed on 2025-11-27 at about $0.11. It fell 76% to an all-time low near $0.035 in mid-December 2025, spent about 93% of its life closing below $0.26, and only broke and held above $0.26 from 2026-09-18. It set its ATH of about $0.452–0.456 on 2026-10-01, then crashed about 35–39% within hours of the kPoints-claim announcement. The claim lets kPoints holders buy 50M KNTQ at $0.26. At about $0.302 (2026-10-03 12:07 UTC), price sits about 14% above $0.26. That level is both the claim price and a prior resistance that has acted as support since 2026-09-18. It has not traded below $0.26 since 2026-09-19.

### Cited Findings
**Listing, ATH and ATL**
- **Genesis/TGE.** KNTQ genesis balances were created on 2025-11-27 at 11:36 UTC (`spotGenesis` ledger entries). The token itself was registered on HyperCore on 2024-10-26 by deployer `0x51172933b60847085e2a959e860e2ec9e240ac09`. [V-API] — [Hyperliquid info API: tokenDetails / userNonFundingLedgerUpdates](https://api.hyperliquid.xyz/info)
- **First trading day (2025-11-27, KNTQ/USDH `@254`).** Open 0.11, high 0.22485, low 0.025 (a thin-book wick), close 0.14878. Volume was about 141.5M KNTQ (≈$17.7M). [V-API] — [Hyperliquid info API: candleSnapshot @254](https://api.hyperliquid.xyz/info)
- **Venue migration.** The KNTQ/USDC pair `@334` started trading on 2026-05-20. The USDH pair's last active candle was 2026-05-26; it now shows 0 volume and no mid price. [V-API] — [Hyperliquid info API: candleSnapshot / spotMetaAndAssetCtxs](https://api.hyperliquid.xyz/info)
- **ATH.** CoinGecko lists $0.452145 at 2026-10-01 06:18:50 UTC. Hyperliquid spot printed $0.45572 in the 07:00 UTC hour on 2026-10-01. The highest daily close was $0.404 on 2026-09-30. [V-CG] [V-API] — [CoinGecko API](https://api.coingecko.com/api/v3/coins/kinetiq); [Hyperliquid info API](https://api.hyperliquid.xyz/info)
- **ATL.** CoinGecko lists $0.03578 at 2025-12-17 19:22 UTC. On Hyperliquid the lowest daily close was 0.037561 (2025-12-17) and the lowest intraday low excluding the TGE wick was 0.0348 (2025-12-18), both on the USDH pair. [V-CG] [V-API] — [CoinGecko API](https://api.coingecko.com/api/v3/coins/kinetiq); [Hyperliquid info API](https://api.hyperliquid.xyz/info)

**Current price and performance**
- **Current price (2026-10-03 ~12:07 UTC).** Hyperliquid mid was 0.30225 (bid 0.30195 / ask 0.30255) and the mark was 0.3015. CoinGecko showed $0.3025, with market cap $84.85M on 280.48M circulating and FDV $302.5M. [V-API] [V-CG] — [Hyperliquid info API: l2Book](https://api.hyperliquid.xyz/info); [CoinGecko](https://www.coingecko.com/en/coins/kinetiq)
- **Performance from Hyperliquid daily closes to $0.3022:**
  - 7d −5.7% (vs 0.32052 on 09-26)
  - 14d +2.9%
  - 30d +50.7% (vs 0.20051 on 09-03)
  - 60d +205.7% (vs 0.09887 on 08-04)
  - 90d +87.2% (vs 0.16144 on 07-05)
  - Since the TGE open: +174.7%
  - CoinGecko's figures: 7d −6.65%, 14d −0.59%, 30d +59.2%, 60d +205.9%, 200d +90.0%.
  - [V-API] [V-CG] — [Hyperliquid info API](https://api.hyperliquid.xyz/info); [CoinGecko API](https://api.coingecko.com/api/v3/coins/kinetiq)

**Price path by phase** [V-API, daily candles] — [Hyperliquid info API](https://api.hyperliquid.xyz/info)
- **Post-TGE dump.** From 0.149 (11-27 close) to 0.0376 (12-17 close), −76%. This came while the S1 airdrop supply hit the market; TGE gave about 24% of supply to kPoints holders [R — [WEEX](https://www.weex.com/news/detail/liquidity-staking-protocol-kinetiq-has-launched-the-kntq-token-and-will-airdrop-24-to-kpoints-holders-200262)].
- **January 2026 rally.** Up to 0.30526 (2026-01-28 high). It closed above $0.26 for only one day (01-28, 0.275), then fell −29% the next day and reached about 0.104 by 02-11.
- **Feb–Apr 2026 grind lower.** Down to 0.08816 (2026-04-07 low).
- **2026-05-06 spike.** +45% intraday (0.1256 → 0.2263). It faded to about 0.13–0.15 by mid-May.
- **May 31–June 2 spike.** Up to 0.37727 (2026-06-02 high), closing above $0.26 on 05-31, 06-01, 06-02 and 06-03. On 06-04 the low was 0.20.
- **June: $0.26 rejected repeatedly.** Highs were 0.26293 (06-05), 0.26 (06-09) and 0.25986 (06-16). Price then bled to 0.08849 (2026-07-31 low), about −77% from the June high.
- **August rally.** From 0.096 (08-11) to a 0.29545 wick on 08-24, closing 0.219.
- **September breakout.** From the 0.193 base (09-15/16 lows) to 0.35253 (09-23 high).
- **Sep 30 / Oct 1.** Sep 30 rose +41.8% (0.285 → 0.404). Oct 1 made the ATH 0.45572, then crashed to 0.27778.

**The Oct 1 crash, hour by hour (UTC)** [V-API, hourly candles] — [Hyperliquid info API](https://api.hyperliquid.xyz/info)
- 12:00 candle: open 0.4275, low 0.32529, close 0.33344, volume 11.65M KNTQ.
- 13:00 candle: low 0.27778, close 0.28403, volume 11.0M KNTQ. That is −35% from the 12:00 open and −39% from the ATH.
- Rebound: 0.36871 by 18:00 (+33% off the low).
- Oct 1 daily volume was about 57.9M KNTQ (≈$21.3M), a record for the USDC pair.
- Oct 2 low 0.287, close 0.29877. Oct 3 to 12:00 UTC: low 0.287 again, last about 0.302.

**The trigger for the crash**
- **Kinetiq's post.** At 2026-10-01 12:01:39 UTC (time derived from the X status ID) Kinetiq posted: "The final kPoints have now been distributed. Your kPoints now allow you to claim KNTQ." This matches the minute the crash started. — [Kinetiq on X](https://x.com/Kinetiq_xyz/status/2105629210048078216)
- **Claim terms.** 50M KNTQ (5% of supply) can be bought at $0.26 over a 10-day window opening 2026-10-01. There is "no lockup and no vesting", so tokens are usable immediately. Unclaimed tokens revert to the Kinetiq Foundation. The kPoints program ran 46 weeks and distributed 36.8M points. Crypto Briefing reported price at about $0.40 at the announcement and about $0.33 later. [R] — [Crypto Briefing](https://cryptobriefing.com/kinetiq-ends-kpoints-kntq-price-drop/)
- **Conflicting date.** ChainCatcher dates the announcement 2026-10-02 12:22 UTC and says KNTQ fell 23%. The on-chain price action and the X post timestamp both point to 2026-10-01 ~12:00 UTC. [R] — [ChainCatcher](https://www.chaincatcher.com/en/article/2293658)
- **KuCoin's account.** KNTQ traded at about $0.422 before the news, fell to as low as about $0.281 (−33%) and recovered to about $0.325. KuCoin framed the claim as an arbitrage incentive for claimants to sell above $0.26. [R] — [KuCoin News](https://www.kucoin.com/news/flash/kinetiq-ends-kpoints-program-kntq-price-drops-23-after-token-sale-launch)

**Catalysts for the September run-up**
- **KIP-5 (≈2026-09-15 17:08 UTC, time derived from the post ID).** Kinetiq redirected 100% of KNTQ buybacks to the Hyperliquid Assistance Fund. It said 5.39M KNTQ had already been bought with protocol revenue at an average of $0.15 (≈0.53% of supply). [R] — [Vikingo.hl on X](https://x.com/VikingoDigital_/status/2099908097401602439)
  - The same day, 2.51M KNTQ was delivered on-chain to the Assistance Fund (see section 5) [V-API].
  - Price went from a 0.1956 close (09-16) to a 0.3525 high (09-23), +80%.
- **Ascend buyback allocation change, effective 2026-09-30.** The split moved from 90% HYPE / 10% KNTQ to 50/50. Of KNTQ bought, 60% is burned, 20% goes to kHYPE/KNTQ liquidity and 20% to Ascend points. This comes from a search summary; I did not open the page. [R] — [TradingView/CoinMarketCal](https://www.tradingview.com/news/coinmarketcal:0115aaccb094b:0-kinetiq-ascend-buyback-allocation-shifts-to-50-hype-50-kntq-30-sep-2026/)
  - Sep 30 coincided with the +41.8% day [V-API].
  - KuCoin described the move as "ripped ~28% in 24h and printed a new ATH at $0.45" [R]. — [KuCoin insight](https://www.kucoin.com/news/insight/HYPE/6abf1f5d38a2640007922a32)
- **Kraken listing.** KNTQ reportedly went live on Kraken on 2026-05-27. This is from a search snippet; I did not open the page. That was a few days before the May 31–June 2 spike. [R] — [Kraken Blog](https://blog.kraken.com/product/asset-listings/kntq-is-available-for-trading)

**Distance to $0.26 and history around the level** [V-API] — [Hyperliquid info API](https://api.hyperliquid.xyz/info)
- $0.26 is 14.0% below the 0.3022 mid.
- Only 21 of 311 daily closes since TGE were above $0.26:
  - 2026-01-28
  - 2026-05-31 to 06-03
  - 2026-09-18 to 10-03 (16 consecutive closes, ongoing)
- Breakout above $0.26: 2026-09-18 (close 0.26477). The last trade below $0.26 was the 2026-09-19 low of 0.25553.
- The lowest low since then is 0.27778 (Oct 1 crash).
- Earlier bounces near $0.26:
  - 2026-06-02/03: wicks to 0.2639 and 0.2571, bounce to 0.332, then failure on 06-04 (low 0.20).
  - 2026-09-19: low 0.2555, rally to 0.3525.
  - 2026-10-01: low 0.2778, rebound to 0.3687.

**Volume trend (approximate USD on HL spot, from candles)** [V-API] — [Hyperliquid info API](https://api.hyperliquid.xyz/info)
- Jul 5–Aug 3: $0.28M/day.
- Aug 4–Sep 2: $1.80M/day.
- Sep 3–Oct 2: $2.29M/day.
- Sep 19–Oct 2: $3.32M/day.
- Sep 26–Oct 2: $5.09M/day, inflated by Oct 1's $21.3M.
- Exact trailing 24h at 12:07 UTC Oct 3: $3,164,242 (10.65M KNTQ).

### Inferences
**Support levels (observed):**
- $0.287: repeated floor on Oct 2–3.
- $0.278: Oct 1 crash low.
- $0.26: claim price, June resistance turned support, and a dense bid cluster (section 2).
- $0.25: the largest visible bid bucket.
- $0.19–0.20: the mid-September base.

**Resistance levels (observed):**
- $0.31–0.32
- $0.34–0.35: Sep 22–23 highs and the Oct 2 high of 0.3415.
- $0.368–0.377: Oct 1 rebound high and the Jun 1–2 highs.
- $0.40–0.407: Sep 30 high.
- $0.452–0.456: ATH.

**Recurring pattern:** KNTQ's big rallies (Jan, May–Jun, Aug, Sep) have all retraced sharply. The two previous excursions above $0.26 failed within 1–4 daily closes. The current one has held 16 closes, which is structurally stronger. But it now faces an explicit supply source anchored at $0.26 (the claim).

**Claim arbitrage:** As long as the market trades above $0.26 during the claim window, any claimant can buy at $0.26 and sell for a risk-free spread (about 16% at $0.302). That should pull price toward $0.26, plus some premium for friction, until the window closes around 2026-10-10/11.

### Gaps
- I could not confirm the exact claim window end (10 vs 11 Oct) or any per-wallet claim caps. Other researchers cover S2/kPoints terms.
- I did not identify the causes of the 2026-01-13–28, 2026-05-06 and 2026-08-12–24 rallies.
- The Kraken listing date (2026-05-27) and the Ascend 50/50 details come from search snippets, not opened pages.

## 2. Venues and liquidity

### Takeaway
Hyperliquid spot (KNTQ/USDC) carries about 77% of reported volume. HyperEVM DEXs (Nest, Project X) carry about 14% and Kraken about 9%. CoinGecko lists no Binance, Bybit, OKX, Bitget, Gate or MEXC market. The Hyperliquid book is thin near the touch (about $23–29k per side within ±2%) but bid-heavy further out: about $1.3M of bids versus about $0.5M of asks within ±20%. A large stack of resting bids sits between $0.25 and $0.29. HyperEVM DEX liquidity totals about $2.2M.

### Cited Findings
**24h volume by venue (CoinGecko, 2026-10-03 12:09 UTC; total $4.19M)** [V-CG] — [CoinGecko API: coins/kinetiq tickers](https://api.coingecko.com/api/v3/coins/kinetiq)

| Venue | Pair | 24h volume | Share | Spread |
|---|---|---|---|---|
| Hyperliquid | KNTQ/USDC | $3,221,387 | 76.9% | 0.20% |
| Nest (HyperEVM) | KNTQ/WHYPE | $318,706 | 7.6% | flagged "anomaly" by CoinGecko |
| Kraken | KNTQ/USD | $259,223 | 6.2% | 0.12% |
| Kraken | KNTQ/EUR | $129,278 | 3.1% | — |
| Project X | KNTQ/USDC | $124,177 | 3.0% | — |
| Nest | KNTQ/kHYPE | $56,119 | 1.3% | — |
| Project X | KNTQ/WHYPE | $47,243 | 1.1% | — |
| Nest | KNTQ/USDC | $29,156 | 0.7% | — |

- No other CEX tickers appear.

**Hyperliquid order book, `@334` (2026-10-03 12:07 UTC)** [V-API, l2Book] — [Hyperliquid info API](https://api.hyperliquid.xyz/info)

At full precision (spread 19.9 bps):

| Distance from mid | Bids | Asks |
|---|---|---|
| ±1% | $12.2k | $8.5k |
| ±2% | $29.2k | $22.9k |

- A 188k-KNTQ (≈$56k) bid sits at $0.296, just outside −2%.

At aggregated precision:

| Distance from mid | Bids | Asks |
|---|---|---|
| ±5% | ≈$98–163k | ≈$76–93k |
| ±10% | ≈$428–434k | ≈$159–161k |
| ±20% | ≈$1.30M | ≈$0.50M |
| ±30% | ≈$1.47M | ≈$0.63M |

**Bid buckets (2-significant-figure aggregation)** [V-API] — [Hyperliquid info API](https://api.hyperliquid.xyz/info)

| Bucket | KNTQ | Orders |
|---|---|---|
| 0.29x | 305k | 22 |
| 0.28x | 1.18M | 166 |
| 0.27x | 939k | 180 |
| 0.26x | 673k | 147 |
| 0.25x | 1.76M | 218 |
| 0.14x | 762k | — |
| 0.13x | 589k | — |

- That is about 4.9M KNTQ (≈$1.33M) of bids between $0.25 and $0.30.

**Ask buckets** [V-API] — [Hyperliquid info API](https://api.hyperliquid.xyz/info)
- 0.31: 106k; 0.32: 188k; 0.33: 205k; 0.34: 249k; 0.35: 118k; 0.36: 595k; 0.40: 181k; 0.44: 435k; 0.50: 547k.
- That is about 2.0M KNTQ (≈$0.69M) of asks between $0.30 and $0.40.

**HyperEVM DEX pools (2026-10-03)** [V-GT] [V-DS] — [GeckoTerminal API](https://api.geckoterminal.com/api/v2/networks/hyperevm/tokens/0x000000000000780555bd0bca3791f89f9542c2d6/pools); [DexScreener API](https://api.dexscreener.com/latest/dex/tokens/0x000000000000780555bd0bca3791f89f9542c2d6)

| DEX | Pool | Address | Reserves | 24h volume |
|---|---|---|---|---|
| Nest | KNTQ/WHYPE 0.45% | `0xc8e5…12e7` | $692k | $317k |
| Project X | KNTQ/USDC 1% | `0x99cb…bd08` | $527k | $123k |
| Project X | KNTQ/WHYPE 1% | `0xd19a…12c5` | $446k | $47k |
| Nest | KNTQ/kHYPE | `0x5132…5510` | $239k | $56k |
| Project X | sKNTQ/KNTQ 0.1% | `0xcdc3…7992` | $129k | $144k |
| Nest | KNTQ/USDC | `0xf410…0556` | $90k | $29k |
| Nest | KNTQ/NEST | — | $29k | — |
| Nest | sKNTQ/KNTQ | — | $20k | $92k |

- Total is about $2.2M. Most pools were created on 2025-11-27, the TGE day.

**KNTQ held directly by the main DEX pools** [V-RPC] — [HyperEVM RPC](https://rpc.hyperliquid.xyz/evm)
- Project X KNTQ/USDC: 1.36M.
- Project X KNTQ/WHYPE: 1.01M.
- Nest KNTQ/WHYPE: 0.85M.
- Total about 4.16M across the major Nest/Project X pools.

### Inferences
- Price discovery is almost entirely on Hyperliquid's CLOB. DEX and Kraken prices arbitrage to it, so HL order-book flows are the right lens for "who is the marginal buyer/seller".
- The ±2% depth of about $25k means a $100k market order moves price several percent. Sudden large sellers, such as claimants dumping, can gap price down quickly until they hit the $0.25–0.29 bid stack.
- Resting bids can be pulled; they are not committed demand. Part of the stack belongs to identifiable wallets (section 5): 0xaf0f… has 400k KNTQ of bids at $0.2666–0.2866 and the market-maker-like 0xbf66… has 561k at $0.2718–0.3031.

### Gaps
- Binance Alpha status was not verified. CoinGecko does not track Alpha, and I found no evidence of a Binance, Bybit, OKX, Bitget, Gate or MEXC spot listing.
- Kraken order-book depth was not retrieved.

## 3. Derivatives (perps, OI, funding, liquidations)

### Takeaway
There is no KNTQ perpetual on Hyperliquid, neither on the main perp dex nor on any of the 10 HIP-3 dexes, including Kinetiq's own "Markets by Kinetiq" (`km`). CoinGecko's derivatives feed lists no KNTQ contract on any CEX. KNTQ positioning is therefore spot-only: there is no OI, funding, long/short skew or liquidation map to analyze.

### Cited Findings
- The main perp universe (`meta`) contains no KNTQ. HIP-3 dexes (`perpDexs`: xyz, flx, vntl, hyna, km, abcd, cash, para, mkts, io) were each checked and none lists KNTQ (2026-10-03). [V-API] — [Hyperliquid info API](https://api.hyperliquid.xyz/info)
- `km` is "Markets by Kinetiq". Deployer `0x71f0019cc7fa79e4f42587fb7b9a817d8d2429ec`, fee recipient `0xbcd4071d023bf2aae484d724c130b5af6f0ca0d2`. It lists equities, FX and commodities (km:AAPL, km:EUR, km:GOLD…), not KNTQ. [V-API] — [Hyperliquid info API](https://api.hyperliquid.xyz/info)
- The CoinGecko derivatives API (26,651 tickers) returned 0 KNTQ contracts on 2026-10-03. [V-CG] — [CoinGecko derivatives API](https://api.coingecko.com/api/v3/derivatives)

### Inferences
- With no perp, there is no cheap way to short KNTQ or to hedge claim allocations. Claimants who want to lock in the $0.26 → market spread must sell spot. That makes the claim window a direct spot-supply event rather than something absorbed by perp basis trades.
- There are also no liquidation cascades to drive moves. Sharp moves (Oct 1) reflect spot order-flow imbalance against a thin book.

### Gaps
- I did not check HyperEVM lending markets for KNTQ borrow (a possible shorting route).
- The web search for KNTQ perps returned only QNT (Quant) results, which were irrelevant.

## 4. Holder distribution and labeled wallets

### Takeaway
85.8% of KNTQ (857.8M) sits on HyperEVM. The HyperCore spot float is only 142.2M (14.2% of supply), held by 11,762 nonzero addresses, about 6,200 of them with at least 1 KNTQ. That float is concentrated: the top 10 hold 34.5% and the top 100 hold 70.9%.
- **Deployer:** received 730M at genesis and bridged it all to HyperEVM within 31 minutes of TGE.
- **Staking:** 75.8M KNTQ is staked in sKNTQ.
- **Assistance Fund:** holds 3.98M KNTQ from buybacks.
- **CEXs:** no CEX-labeled HyperCore wallet holds KNTQ.
- **Unknown:** I could not enumerate HyperEVM holders, and about 778M KNTQ there is unattributed.

### Cited Findings
**HyperCore holders (Hypurrscan snapshot, 2026-10-03 12:01 UTC)** [V-HS] — [Hypurrscan holders API](https://api.hypurrscan.io/holders/KNTQ)
- 11,762 addresses with a nonzero balance:
  - 5,565 hold less than 1 KNTQ (dust).
  - 1,723 hold 1–100.
  - 2,296 hold 100–1k.
  - 1,420 hold 1k–10k.
  - 550 hold 10k–100k.
  - 184 hold 100k–1M.
  - 21 hold 1M–10M.
  - 2 hold more than 10M.
- The HyperEVM system/bridge address `0x200000000000000000000000000000000000007c` holds 857,813,734 KNTQ. That is the amount bridged to HyperEVM.
- **Concentration, excluding the bridge address (float 142.19M):**

| Group | KNTQ | Share of HyperCore float | Share of supply |
|---|---|---|---|
| Top 10 | 49.07M | 34.5% | 4.9% |
| Top 50 | 82.30M | 57.9% | 8.2% |
| Top 100 | 100.81M | 70.9% | 10.1% |

**Largest HyperCore holders** [V-HS], with labels from Hypurrscan aliases where they exist [V-HS] — [Hypurrscan aliases API](https://api.hypurrscan.io/globalAliases)
- `0xaf0fdd39e5d92499b0ed9f68693da99c0ec1e92e`: 18.48M. Unlabeled. Received a 774,890 genesis (S1 airdrop-sized) allocation. Active whale; see section 5.
- `0xa9b95f2a2e7ef219021efc5c04c32761b8553bbd`: 11.00M. Unlabeled. Also holds $10.28M USDC and 220,001 HYPE on HyperCore [V-API].
- `0xfefefefefefefefefefefefefefefefefefefefe`: 3.98M. "Assistance Fund", the KIP-5 buyback sink.
- `0x77375a8c9d13bf79afb2a87f1b0ac1dfd5f5bf66`: 3.23M. Genesis 879k.
- `0xbf66cb8b987fee1f6526bb6ee04345d36405f913`: 2.88M. Behaves like a market maker.
- `0xfeb63b9e4a871b644816d94a1d19517a87ce5fa0`: 2.80M.
- `0xab11bfc2e491378b79675dc3e996ed01ea034d5f`: 1.86M. Received a round 10M at genesis.
- `0x58f0bf4307c61bc7a5fe11e24fe36e64300b0d20`: 1.50M.

**Genesis allocation** [V-API] — [Hyperliquid info API: tokenDetails](https://api.hyperliquid.xyz/info)
- 10,000 addresses received 1B in total. The deployer `0x51172933…ac09` (Hypurrscan alias "KNTQ Deployer") received 730,000,000 (73%).
- The other 9,999 addresses received 270M (27%), all in amounts of 100 KNTQ or more:
  - 2,032 got 100–1k.
  - 5,825 got 1k–10k.
  - 1,783 got 10k–100k.
  - 334 got 100k–1M.
  - 21 got 1M–10M.
  - 4 got 10M or more.
- The four largest non-deployer allocations were 15.8M (`0x63af…4b36`), 12.77M (`0x9794…333b`), 10M (`0x44ca…adf5`) and 10M (`0xab11…4d5f`).
- No blacklist; no future emissions are configured on HyperCore.

**Where the deployer's 730M went** [V-API] [V-RPC] — [Hyperliquid info API: userNonFundingLedgerUpdates](https://api.hyperliquid.xyz/info); [HyperEVM RPC](https://rpc.hyperliquid.xyz/evm)
- 2025-11-27 12:07 UTC: the deployer bridged 729,999,990 KNTQ to HyperEVM (ledger value at the time: $117.3M).
- The deployer's HyperEVM balance is now 0 and its HyperCore balance is 23,806. So the allocation was moved on to other EVM addresses, presumably treasury or vesting contracts, which I could not identify.

**Staking and supply** [V-RPC] [V-CG] — [HyperEVM RPC](https://rpc.hyperliquid.xyz/evm); [CoinGecko API](https://api.coingecko.com/api/v3/coins/kinetiq)
- The sKNTQ contract `0x696238e0Ca31c94e24ca4CBe7921754E172E4d0F` holds 75,818,414 KNTQ (7.6% of supply). sKNTQ total supply is 73,367,575, implying about 1.033 KNTQ per sKNTQ.
- CoinGecko circulating supply is 280.48M, which implies about 720M non-circulating.

**What genesis recipients did** [V-HS] [V-API] [V-RPC] — [Hypurrscan holders API](https://api.hypurrscan.io/holders/KNTQ); [Hyperliquid info API](https://api.hyperliquid.xyz/info); [HyperEVM RPC](https://rpc.hyperliquid.xyz/evm)
- Of the 9,999 non-deployer recipients, only 2,843 still hold any KNTQ on HyperCore, and 885 hold at least their genesis amount.
- Their combined HyperCore balance is 60.5M, down from 270M.
- Several of the largest moved their whole allocation to HyperEVM early:
  - `0x9794bbbc222b6b93c1417d01aa1ff06d42e5333b` bridged 12,765,794 on 2025-12-03 08:16 UTC. Its EVM balance is now 1.42M.
  - `0x29f95aecc3d5ad0c8698dd6dccad71cacb087d2c` sent 4,519,243 to `0x63af859d7b4717bd4d3705f15b6d4caad6cf4b36`, which bridged 20,324,572 to EVM on 2025-12-05 20:12 UTC. Its EVM balance is now 1.06M.
  - `0x44ca55a6fd39c68a7510d7b03c25810b1299adf5` (10M) bridged in tranches between Jan and Jun 2026 and now holds 0 on both layers.
  - The 7.57M, 7.54M and 6.75M recipients (`0x0edc…`, `0xb57f…`, `0x2326…`) hold 0 on both layers.

**Exchange and market-maker wallets** [V-HS] — [Hypurrscan aliases API](https://api.hypurrscan.io/globalAliases)
- HyperCore wallets labeled Bybit, OKX 1–3, KuCoin 1–4, Gate.io 1–2, Bitget 1–3, MEXC and Binance US all hold 0 KNTQ.
- No Wintermute, GSR, Flowdesk or Amber label appears among KNTQ holders.

### Inferences
- **Float.** The tradable HyperCore float (142M) is small versus HyperEVM holdings. Large EVM→Core bridge transfers are the main early-warning signal for new supply. Example: whale 0xaf0f… bridged 10.66M in on 2026-09-28 (section 5).
- **Locked supply.** The ~720M gap between total and circulating supply is consistent with the deployer's 730M sitting in locked or treasury contracts on HyperEVM. Who controls it, and any unlock schedule, could not be verified here.
- **Airdrop selling.** The roughly 78% drop in genesis recipients' HyperCore balances is an upper bound on selling, because some of it went to HyperEVM for staking or LP. The −76% price slide in the three weeks after TGE indicates heavy S1 airdrop selling.
- **Round allocations.** The round 10M genesis allocations (0xab11…, 0x44ca…) look like partner, market-maker or investor allocations rather than points-based airdrops. Identity is not verified.

### Gaps
- I could not get a HyperEVM holder count or top-holder list. hyperevmscan.io returned a Cloudflare 403. The Blockscout, Routescan and hl.eco APIs returned 404 or 400. The public RPC caps `eth_getLogs` at a 1,000-block range and rate-limits.
- As a result, team, treasury, investor and vesting contract addresses and their recent balance changes are unknown. About 778M KNTQ on EVM, outside sKNTQ and the DEX pools, is unattributed.
- Whale #2 (`0xa9b9…`) has no KNTQ transfers in its ledger and no KNTQ fills in the windows I retrieved, so how it acquired 11M is unresolved.

## 5. Recent flows (last 30 days, emphasis on the last 14)

### Takeaway
Verified HyperCore flows split cleanly:
- **Buyers:** one unlabeled whale, `0xaf0f…`, net-bought about 5.1M KNTQ (≈$1.37M net) over 30 days and kept buying through the Oct 1 crash, including an active TWAP on Oct 3. A second wallet, `0x58f0…`, TWAP-bought at least 1.09M on Oct 1.
- **Sellers:** a cluster fed by the 10M-genesis wallet `0xab11…` (execution wallets `0x259a…` and `0x366f…`) sold into the September rally at about $0.35–0.39, and `0xfeb6…` net-sold about 0.35M.
- **Buybacks:** protocol buybacks are visible but small, about $3–8k per day into the Assistance Fund, plus one-off lump transfers of 2.51M on Sep 15.
- **Unattributed:** I found no CEX-deposit flows on HyperCore and no KNTQ alerts from the usual on-chain sleuths. The Oct 1 crash volume (≈58M KNTQ) is far larger than what these named wallets account for, so most of that selling remains unattributed.

### Cited Findings
**Whale accumulator: `0xaf0fdd39e5d92499b0ed9f68693da99c0ec1e92e`** [V-API] — [Hypurrscan address](https://hypurrscan.io/address/0xaf0fdd39e5d92499b0ed9f68693da99c0ec1e92e); [Hyperliquid info API: userFillsByTime / userTwapSliceFills / frontendOpenOrders / ledger](https://api.hyperliquid.xyz/info)
- 30-day regular fills on KNTQ: bought 5,612,051 KNTQ for $1,577,638 (avg about $0.281). Sold 485,583 for $208,935 (avg about $0.430).
- Weekly net:
  - Sep 3–10: +853,730.
  - Sep 10–17: +1,407,033.
  - Sep 17–24: +40,887.
  - Sep 24–Oct 1: +632,121 bought / −383,632 sold.
  - Oct 1–3: +2,678,281 bought / −101,950 sold.
- On 2026-09-28 22:02 UTC it bridged 10,662,466 KNTQ in from HyperEVM (≈$3.25M). It sent 500,000 back to EVM on Oct 1 at 14:55 UTC.
- TWAP buy running on Oct 3: 355 slices, 16,121 KNTQ, 09:29–12:09 UTC.
- Open orders: 74 orders, with bids of 399,961 KNTQ at $0.2666–0.2866 and asks of 898,049 KNTQ at $0.368–0.442.
- It also trades BTC, ETH, HYPE and other perps, so it looks like a discretionary whale rather than a pure market maker.

**TWAP buyer: `0x58f0bf4307c61bc7a5fe11e24fe36e64300b0d20`** (now 1.50M KNTQ) [V-API] — [Hypurrscan address](https://hypurrscan.io/address/0x58f0bf4307c61bc7a5fe11e24fe36e64300b0d20); [Hyperliquid info API: userTwapSliceFills](https://api.hyperliquid.xyz/info)
- TWAP-bought 1,093,492 KNTQ in 2,000 slices on 2026-10-01 between 05:03 and 18:52 UTC. 2,000 is the API cap, so the total may be higher.
- Also bought 69,090 KNTQ with market fills at 12:38–12:39 UTC, inside the crash.

**Market-maker-like wallet: `0xbf66cb8b987fee1f6526bb6ee04345d36405f913`** (2.88M KNTQ) [V-API] — [Hypurrscan address](https://hypurrscan.io/address/0xbf66cb8b987fee1f6526bb6ee04345d36405f913); [Hyperliquid info API](https://api.hyperliquid.xyz/info)
- 7,304 KNTQ fills between Oct 2 15:34 and Oct 3 12:09 UTC (the API's fill window may truncate earlier history).
- Bought 3,083,639 ($911k) and sold 2,739,645 ($809k).
- 16 resting quotes on both sides: bids of 561k at $0.2718–0.3031 and asks of 528k at $0.3036–0.3327.
- Identity unknown.

**Distributor cluster** [V-API] — [Hypurrscan address 0xab11…](https://hypurrscan.io/address/0xab11bfc2e491378b79675dc3e996ed01ea034d5f); [Hyperliquid info API](https://api.hyperliquid.xyz/info)
- **Root wallet `0xab11bfc2e491378b79675dc3e996ed01ea034d5f`** received 10,000,000 at genesis. It sent to `0x259a6f10ec4c3d4819b44e901b3417227c8b4df0`:
  - 2M at TGE
  - 900k on 2026-03-17
  - 1.1M on 05-07
  - 4M on 05-31 at 21:44 UTC, during the May 31 spike
  
  It sent to `0x366fed19e5b826f4f9ad2bce41114631270ea181`:
  - 80k on 05-20
  - 1M on 06-02, during the June spike
  - 500k on 09-22

  It also sent 200k to `0xafc34e5917685204bd6dfb1f71fe039b65b50823` on 09-22.
- **`0x259a…`:** its last 2,000 fills (Sep 21–30) were all KNTQ sells, 161,269 KNTQ at an average of $0.3467. It holds $1.58M USDC and 150k KNTQ. It returned 2M KNTQ to `0xab11…` on 09-22.
- **`0x366f…`:** since Jun 2 it bought 155,344 (avg $0.351) and sold 1,210,810 (avg $0.3935). Its last sale was Oct 1 at 05:51 UTC, near the ATH. It holds $1.09M USDC and 400k KNTQ.

**Net seller: `0xfeb63b9e4a871b644816d94a1d19517a87ce5fa0`** (2.80M KNTQ) [V-API] — [Hypurrscan address](https://hypurrscan.io/address/0xfeb63b9e4a871b644816d94a1d19517a87ce5fa0); [Hyperliquid info API](https://api.hyperliquid.xyz/info)
- Sold 538,769 KNTQ ($143,676, avg about $0.267) in regular fills between Sep 10 and Oct 1: 342,485 in Sep 10–17 and 196,284 in Sep 24–Oct 1.
- TWAP-bought 184,881 between Sep 17 and Oct 1. Net about −354k.

**Passive large holders** [V-API] — [Hyperliquid info API](https://api.hyperliquid.xyz/info)
- `0xa9b9…` (11.0M) and `0x7737…` (3.23M) made no KNTQ trades in the last 30 days.

**Buybacks into the Assistance Fund (`0xfefe…`) since 2026-08-04** [V-API] — [Hyperliquid info API: Assistance Fund ledger](https://api.hyperliquid.xyz/info)
- About 3.19M KNTQ arrived in total, roughly $671k at transfer-time values.
- Lump transfers on 2026-09-15, the KIP-5 day:
  - 1,663,332 KNTQ (≈$335k) at 14:25 UTC from `0xbcd4071d023bf2aae484d724c130b5af6f0ca0d2`, the "Markets by Kinetiq" HIP-3 fee recipient.
  - 850,991 KNTQ (≈$169k) at 16:22–16:53 UTC from the sKNTQ contract address `0x696238e0…4d0F`.
- An hourly feed from `0xaa3b7392052d62928cc87701e3ca6fb6630bb6e2` (unlabeled; behaves like a buyback bot): 389 transfers totalling 436,730 KNTQ (≈$118.7k) between Sep 17 07:05 and Oct 3 12:01 UTC.
  - That is about $2.9–8.2k per day, or 9–25k KNTQ per day.
  - The per-hour size rose from about $74 to about $182 from 2026-10-03 09:06 UTC.
- 26 small transfers from the deployer totalling 240,260 KNTQ (≈$48k) between Aug 4 and Oct 1.

**Third-party reporting**
- KIP-5 cites 5.39M KNTQ bought at an average of $0.15 (≈2.15% of circulating). [R] — [Vikingo.hl on X](https://x.com/VikingoDigital_/status/2099908097401602439)
- CoinMarketCap's AI summary says the "Elysium" mainnet launches on 2026-10-20 and will send 50% of sequencer revenue to buy and burn KNTQ. This is an AI-generated aggregator and unverified. [R] — [CoinMarketCap AI updates](https://coinmarketcap.com/cmc-ai/kinetiq/latest-updates/)

### Inferences
- **Who buys:** the only large, verifiable net buyer is the discretionary whale `0xaf0f…`, together with TWAP buyer `0x58f0…`. Both buy weakness, with resting bids at $0.267–0.287, and sell strength, with `0xaf0f…`'s 898k-KNTQ ask ladder at $0.368–0.442. That reinforces a $0.27–0.29 floor and a $0.37–0.44 ceiling.
- **Who sells:** the `0xab11…` cluster has repeatedly moved KNTQ to execution wallets just before or during spikes (May 7, May 31, Jun 2, Sep 22) and sold into them. It still controls about 2.65M KNTQ on HyperCore (1.86M + 0.15M + 0.40M + 0.24M), so more supply can appear on rallies.
- **Buybacks:** at about $3–8k per day, buybacks are about 0.1–0.2% of daily HL volume. They signal intent but are not the marginal buyer. The Sep 15 lump transfers were accumulated tokens moved to the Assistance Fund, not new market buying.

### Gaps
- I could not retrieve a global list of active KNTQ TWAPs; the Hypurrscan endpoint `/twap/KNTQ` returned an empty list. TWAP data above comes from per-wallet queries only.
- I found no KNTQ-specific alerts from Lookonchain, OnchainLens, EmberCN, Spot On Chain or Arkham in my searches.
- I could not attribute the Oct 1 12:00–14:00 UTC sell volume (≈22.6M KNTQ in two hours) without a full trade tape. The named wallets explain only a small fraction of it.
- HyperEVM DEX flows by wallet and Kraken deposit flows are not covered.
- A KuCoin/TechFlow snippet about a whale liquidating DeFi tokens at a $9.61M loss had no confirmed link to KNTQ, so I did not use it.

## 6. Net assessment: the marginal buyer and seller, and the sell-pressure outlook

### Takeaway
Right now the marginal seller is the kPoints claimant. Up to 50M KNTQ is purchasable at $0.26 with no lockup during roughly Oct 1–10/11. Behind the claimants come opportunistic distributors such as the `0xab11…` cluster. The marginal buyers are a handful of whales and TWAPs (`0xaf0f…`, `0x58f0…`), a large resting-bid stack at $0.25–0.29, and small programmatic buybacks. Sell pressure should stay elevated, and price should gravitate toward $0.26–0.29, until the claim window closes. After that it should ease, with two caveats: unclaimed tokens revert to the Foundation, and the roughly 720M non-circulating supply on HyperEVM has an unverified unlock schedule.

### Cited Findings
- **Claim size and terms:** 50M KNTQ at $0.26, 10-day window from Oct 1, tokens usable immediately, unclaimed tokens to the Foundation. [R] — [Crypto Briefing](https://cryptobriefing.com/kinetiq-ends-kpoints-kntq-price-drop/)
- **How 50M compares with the market** [V-HS] [V-CG] [V-API] — [Hypurrscan holders API](https://api.hypurrscan.io/holders/KNTQ); [CoinGecko API](https://api.coingecko.com/api/v3/coins/kinetiq); [Hyperliquid info API](https://api.hyperliquid.xyz/info)
  - HyperCore float: 142.2M.
  - CoinGecko circulating: 280.5M.
  - Trailing-week average HL volume: about 14.6M KNTQ per day.
- **Buy side visible on the book** [V-API] — [Hyperliquid info API](https://api.hyperliquid.xyz/info)
  - About 4.9M KNTQ (≈$1.33M) of resting bids at $0.25–0.30, versus about 2.0M KNTQ of asks at $0.30–0.40.
  - Whale `0xaf0f…` net +5.1M KNTQ over 30 days.
  - Buyback feed about $3–8k per day.

### Inferences
- **Ratios:** 50M KNTQ is about 35% of the HyperCore float, about 18% of CoinGecko circulating, and about 3–4 days of last week's average HL volume. If even a third is claimed and sold, that is roughly 16–17M KNTQ of supply. Each sale arbitrages the $0.26 cost against a book with only about $25k of depth within ±2%.
- **Expected path during the window:** price is likely pinned between about $0.26 and $0.30, with the $0.25–0.29 bid stack absorbing claimant flow. A daily close below $0.287, then $0.278, would show claimant supply overwhelming the bids. A break below $0.26 would mean non-arbitrage selling, since claimants have no incentive to sell below cost. That would likely draw a test of the $0.25 bucket and, further down, the $0.19–0.20 September base.
- **After the window:** claim-arbitrage supply ends. Support could come from three sources:
  - The Ascend 50/50 buyback split, if confirmed.
  - The possible Elysium buyback, which is unverified.
  - Continued accumulation by the whales.
- **Risks after the window:**
  - The size and timing of Foundation-held unclaimed tokens.
  - Supply bridged in from HyperEVM by large holders.
  - The `0xab11…` cluster selling into any rebound toward $0.35–0.40.
  - Unknown team, investor or treasury unlocks among the roughly 720M non-circulating tokens.
- **History:** KNTQ's history argues for caution. Every prior rally above $0.26 retraced 40–77%, and the September breakout is the first to hold above $0.26 for more than four closes.
- **Bottom line:** in the near term (to about Oct 11), expect net distribution, with claimants as the marginal sellers. Whale and TWAP absorption at $0.27–0.29 is the key offset, and there is no perp market to amplify or hedge either side. Beyond mid-October the balance is uncertain and depends mainly on unverified buyback upgrades and unverified unlocks.

### Gaps
- Live claim uptake: how many kPoints holders have claimed and how many claimed tokens were sold. This needs the claim contract address, which other researchers covering S2 may have.
- The team, investor and treasury vesting schedule and the related HyperEVM contract addresses. These are needed to judge post-October supply.
- Confirmation of the Elysium launch date and its buyback mechanics from a primary Kinetiq source.
