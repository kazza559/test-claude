# Tori Finance: community and social-media signals (as of 2026-09-28)

Scope: official X, Telegram and Discord; KOL and analyst commentary; prediction and pre-market markets; sentiment; red flags.
Labels used: **[OFFICIAL]** means the Tori team said it (X account, docs, website). **[3RD-PARTY]** means media, aggregator or KOL reporting. **[RUMOR/SPECULATION]** means unconfirmed. **[MARKET DATA]** means live API pulls taken on 2026-09-28.

Platform access log (what was tried):
- X (@tori_finance): x.com returned HTTP 402, and the xcancel.com mirror returned 451 ("service suspended"). I got the profile stats from the fxtwitter public API. The ~20 most recent posts came from Twitter's syndication endpoint (`syndication.twitter.com/srv/timeline-profile/user-id/1929232230884200449`). A first attempt by screen-name returned 429, and a retry by user-id returned 200. I could not get posts older than about Sep 4, 2026 directly, so I rebuilt the earlier history from news coverage.
- Telegram: the website lists only two official groups, `t.me/Tori_CN` and `t.me/ToriFinance_KR`. Both are groups rather than channels, so the `t.me/s/` preview does not work. I took member counts from their `t.me/<name>` landing pages. I found no official English Telegram. `t.me/tori_finance` is a squatter (see red flags).
- Discord: I pulled counts from the public invite API (`discord.com/api/v9/invites/torifinance?with_counts=true`). I could not read messages.
- Polymarket: gamma API `public-search?q=tori` and `events?slug=...`. This worked.
- Whales Market: API `api.whales.market/v2/tokens?search=tori`. I checked that the search works (a query for "monad" returns Monad) and that it returns 0 for Tori. The first 483 point-market listings also have no Tori entry.
- Hyperliquid: `/info` meta for the main perp universe (234 assets) and HIP-3 dexes xyz, flx, vntl, hyna, km, abcd, para, mkts and io. None list TORI. The `cash` dex query errored.
- Aevo: `/markets?instrument_type=PERPETUAL` returned 102 perps and none is TORI.
- Not checked directly: Binance pre-market. No search result mentioned a Tori listing there.

---

## Q1. What has Tori announced on X/Telegram in the last 6 months? Any AMA or founder hints about the TGE or token?

### Takeaway
Tori has made no official statement about a token, a TGE, an airdrop, an exchange listing or a Season 1 end date. The official docs go further and say that Cores (points) "are not a promise of any token or payment" and that "the form that takes has not been decided". Over the last 6 months the announcements have been about product and integrations: the pre-deposit vault, the strUSD launch, Pendle, Morpho, Tenor, Monad, BitGo, CN/KR communities, an AMA with RockawayX and Accountable, and "$1M rewards distributed".

### Cited Findings
**Official token and points stance**
- [OFFICIAL] The docs Cores page says: "Cores represent your contribution to Tori. As the protocol evolves, they will factor into how early supporters are recognized. The form that takes has not been decided, and Cores are not a promise of any token or payment." — [Tori Docs: Cores](https://docs.tori.finance/resources/cores)
- [OFFICIAL] Season 1 began June 23, 2026 with the pre-deposit phase, "which carried the largest boost the program plans to offer. That phase is complete: the vault has converted to the Ecosystem Vault." The emission rate is "set per season". During the pre-deposit phase it was 30 Cores per dollar per day, and that figure already includes the 2x boost. Referrals earn 10% of referees' Cores with no cap. No Season 1 end date is published. — [Tori Docs: Cores](https://docs.tori.finance/resources/cores); [Tori Docs: Pre-Deposit Vault](https://docs.tori.finance/resources/pre-deposit)
- [OFFICIAL] Pre-deposit vault terms: curated by RockawayX via Upshift, $50M cap, USDC/USDT, LP token etrUSD, fees waived, "2x boost, 30 Cores per dollar per day", 30-day hard lock-up. It then converted to the Ecosystem Vault with a "soft lock-up and 7-day withdrawal period". — [Tori Docs: Pre-Deposit Vault](https://docs.tori.finance/resources/pre-deposit)
- [OFFICIAL] The tori.finance homepage makes no mention of points, seasons, a token, a TGE or an airdrop. It shows TVL of $73.0M, APY of 10.6% and a collateral ratio of 100.52% (fetched 2026-09-28). — [tori.finance](https://tori.finance/)
- [3RD-PARTY] Airdrop trackers all agree: "Tori has not announced a token, a TGE date, or a conversion rate from Cores to any future asset." — [UseTheBitcoin (Jul 2, 2026)](https://usethebitcoin.com/airdrop/tori-finance/); [Airdrops.io (updated Jul 24, 2026)](https://airdrops.io/tori-finance/)
- Rate discrepancy: Airdrops.io says Cores accrue at "30 per dollar per day, doubled during the pre-deposit phase", which reads as 60 during pre-deposit. The official docs say 30 during pre-deposit, with the 2x boost already included. UseTheBitcoin gives a 15 Cores/$/day "standard rate" after the boost. The docs do not publish a post-pre-deposit rate. — [Airdrops.io](https://airdrops.io/tori-finance/) vs [Tori Docs: Cores](https://docs.tori.finance/resources/cores); [UseTheBitcoin](https://usethebitcoin.com/airdrop/tori-finance/)

**Announcement timeline (dated)**
- 2026-02-25: the Canton Foundation announced a Chainlink integration on Canton. This is context only: Tori runs a Canton front-end at canton.tori.finance, but I found no dated Tori announcement for it. — [Canton Foundation on X](https://x.com/CantonFdn/status/2026703390093566323); [canton.tori.finance](https://canton.tori.finance/)
- 2026-03-25 [OFFICIAL/3RD-PARTY]: seed round led by Delphi Ventures, with QInvest, CMCC Global and Bering Waters named in some reports. Other reports name ScaleX Ventures and QInvest. The amount was not disclosed. — [Binance Square](https://www.binance.com/en/square/post/03-25-2026-tori-finance-secures-seed-funding-led-by-delphi-ventures-305338094832850); [PANews](https://www.panewslab.com/en/articles/019d24a9-7508-7621-9040-5569a9715caf); [UseTheBitcoin](https://usethebitcoin.com/airdrop/tori-finance/) (investor lists differ between sources)
- 2026-06-23 [OFFICIAL]: Cores Season 1 and the pre-deposit vault open. — [Tori Docs: Cores](https://docs.tori.finance/resources/cores)
- 2026-06-24 [3RD-PARTY]: about $38.07M was deposited against the $50M cap at the time of publication. — [Bitget News (Jun 24, 2026)](https://www.bitget.com/news/detail/12560605474778). CoinGecko says the vault "received $44M in first 24 hours". — [CoinGecko (Aug 20, 2026)](https://www.coingecko.com/learn/pendle-tori-trusd-strusd-institutional-yield)
- About 2026-06-30: the $50M cap filled within 7 days. — [The Defiant press release (Jul 27, 2026)](https://thedefiant.io/news/press-releases/tori-brings-institutional-trades-on-chain-fills-50m-before-launch)
- 2026-07-27 [OFFICIAL, X]: "We are excited to launch strUSD... 12%* APY, uncorrelated with crypto." It came with day-one DeFi integrations (Morpho, Pendle, Curve, Royco) and drew 313 likes, 43 RTs and 81 replies. — [X post 2081758481057784130](https://x.com/tori_finance/status/2081758481057784130); [CoinGecko](https://www.coingecko.com/learn/pendle-tori-trusd-strusd-institutional-yield)
- 2026-08-03 [3RD-PARTY]: the Pendle newsletter lists the new Tori strUSD and trUSD markets, both maturing in November 2026. It also carries Pendle's "intern insight": "just Pendle LP instead for: 1) MORE points 2) MORE yield". — [Pendle Print #122](https://pendlefi.substack.com/p/pendle-print-122)
- 2026-08-20 [3RD-PARTY]: PT-strUSD fixed rate 11.56%, PT-trUSD 9.51%, maturity Nov 26, 2026, about $19M of Pendle liquidity and about $270K of daily volume. Tori TVL was $63M+. — [CoinGecko](https://www.coingecko.com/learn/pendle-tori-trusd-strusd-institutional-yield)
- About 2026-08-23 [OFFICIAL, X; undated in the snippet]: after the Term Finance governance exploit ($8.5M, Aug 23, 2026), Tori said "trUSD and strUSD had zero exposure, Ecosystem Vault participants are fully covered, and all operations continue as normal." — [X @tori_finance (search snippet)](https://x.com/tori_finance); exploit date from [CryptoTimes (Aug 23, 2026)](https://www.cryptotimes.io/2026/08/23/term-finance-loses-8-5m-after-attacker-hijacks-dao-governance-vote/)
- Undated [OFFICIAL, X via search snippet]: RockawayX and HT Digital were added as external verifiers of reserves. Tori also started publishing reserve liquidity and time-to-exit data. — [X @tori_finance](https://x.com/tori_finance); [Tori transparency page](https://app.tori.finance/transparency)
- 2026-09-10 [OFFICIAL, X]: the app and website are now in nine languages, and Mandarin and Korean Telegram communities opened (73 likes, 17 replies). — [X post 2097961000964350270](https://x.com/tori_finance/status/2097961000964350270)
- 2026-09-10 [OFFICIAL, X]: a fixed-rate strUSD market went live on Tenor Finance, which runs on Morpho. — [X post 2098048909088334201](https://x.com/tori_finance/status/2098048909088334201)
- 2026-09-11 [OFFICIAL, X]: trUSD and strUSD are supported at BitGo Bank & Trust, N.A. (443 likes, 5 RTs). — [X post 2098432217953542654](https://x.com/tori_finance/status/2098432217953542654)
- 2026-09-14 [OFFICIAL, X]: etrUSD (the Ecosystem Vault receipt) is live as collateral on Morpho, so holders can borrow USDC "without withdrawing... no exit queue". — [X post 2099520124147658911](https://x.com/tori_finance/status/2099520124147658911)
- 2026-09-17 [OFFICIAL, X]: "Tori is not affected in any way by the fund wind-downs, forced selling and volatility in local markets. All operations are running as normal. Reserves and custody balances are independently verified in real time." — [X post 2100523360946176201](https://x.com/tori_finance/status/2100523360946176201)
- 2026-09-22 [OFFICIAL, X]: strUSD is live on Monad. Users can borrow AUSD against it on Morpho at 86% LLTV, through a SharpByte-curated AUSD Tori Ecosystem vault with wMON/AUSD rewards. — [X post 2102356471111459183 thread](https://x.com/tori_finance/status/2102433356457910542)
- 2026-09-24 [OFFICIAL, X]: live session ("Going live Today at 12:00 UTC") with RockawayX and Accountable "to discuss Tori, DeFi and more". I could not access a transcript. — [X post 2103058546845778132](https://x.com/tori_finance/status/2103058546845778132)
- 2026-09-27 [OFFICIAL, X]: "Tori has distributed a total of $1,000,000 in rewards to users." (90 likes, 20 replies) — [X post 2104192554401239092](https://x.com/tori_finance/status/2104192554401239092)
- Founder interview [3RD-PARTY]: the Delphi Podcast with Samed Düzçay, "Accessing Institutional Yield Strategies at Tori Finance". The listing summary covers his background (mining Bitcoin as a child, building and exiting a SaaS company). I could not get a transcript or confirm a date. — [YouTube](https://www.youtube.com/watch?v=hJ88hDHf-xA); [Delphi Podcast listing](https://www.listennotes.com/podcasts/the-delphi-podcast-the-delphi-podcast-b8TnOVkhWJc/)

### Inferences
- The team sounds legally careful: long "Not financial advice... Not available to US persons" disclaimers on threads, and docs that explicitly disclaim any token promise. That lowers the odds of an explicit TGE hint in public channels. Any TGE signal will probably arrive late, possibly together with a "Season 2" announcement.
- The recent run of distribution news (Monad, Tenor, BitGo, CN/KR communities, nine languages, the "$1M rewards distributed" milestone) looks like a growth-before-TGE playbook. That is only an inference; nothing official says so.
- "Season 1" has no published end date. The docs say rates are "set per season", which suggests later seasons. Farmers should treat this as an open-ended points program.

### Gaps
- I could not retrieve X posts from roughly Mar 28 to Sep 3, 2026 directly (only via news). The earlier history may include posts I did not see.
- No transcript of the Sep 24, 2026 AMA or the Delphi Podcast, so I could not check them for TGE hints.
- No Discord announcement channel content (not public).
- The date of the Term Finance "not affected" post and of the RockawayX/HT Digital verification post are unknown (they surfaced only as search snippets).

---

## Q2. Are there prediction markets, pre-market perps or OTC points markets for Tori? Prices and implied FDVs?

### Takeaway
Two Polymarket events exist, and both are thin (under $30K volume each). The market puts about 39% on a token by Dec 31, 2026 and about 66.5% by Dec 31, 2027. Conditional on launch, the FDV ladder implies roughly a 34% chance of FDV above $100M one day after launch. There is no Tori market on Whales Market, Hyperliquid (main or HIP-3) or Aevo, and I found no OTC $/Core price anywhere.

### Cited Findings
- [MARKET DATA, 2026-09-28] Polymarket, "Will Tori launch a token by ___?" (created 2026-05-20; total volume about $28.4K; open interest about $874; resolves on an official tradable token, with announcements alone not counting):
  - Jun 30, 2026: resolved/closed **No** (price 0).
  - Sep 30, 2026: no trades (bid 0.01 / ask 0.99).
  - **Dec 31, 2026: 0.39** (bid 0.38 / ask 0.40, last 0.34; volume about $7.5K). 1-week change +0.045, 1-month change +0.07.
  - Mar 31, 2027: no trades (bid 0.06 / ask 0.94).
  - **Jun 30, 2027: 0.575** (bid 0.57 / ask 0.58). 1-month change +0.145.
  - **Sep 30, 2027: 0.575** (bid 0.56 / ask 0.59). 1-month change +0.175.
  - **Dec 31, 2027: 0.665** (bid 0.66 / ask 0.67).
  — [Polymarket event](https://polymarket.com/event/will-tori-launch-a-token-by); [gamma API](https://gamma-api.polymarket.com/events?slug=will-tori-launch-a-token-by)
- [MARKET DATA, 2026-09-28] Polymarket, "Tori Finance FDV above ___ one day after launch?" (created 2026-03-26; total volume about $16.7K; listed liquidity about $25.5K; resolves No if there is no token by Dec 31, 2027). Mid prices:
  - >$50M: 0.275 (bid 0.21 / ask 0.34)
  - >$100M: 0.225 (bid 0.21 / ask 0.24; the most-traded strike at about $12.4K volume)
  - >$200M: 0.19
  - >$300M: 0.165
  - >$500M: 0.105
  - >$700M: 0.105
  - >$1B: 0.105 (last trade 0.07)
  — [Polymarket event](https://polymarket.com/event/tori-finance-fdv-above-one-day-after-launch); [gamma API search](https://gamma-api.polymarket.com/public-search?q=tori)
- [MARKET DATA] Whales Market has no Tori token or points market. The API search returns count 0 even though the same search finds other projects. — [Whales Market API](https://api.whales.market/v2/tokens?search=tori); [Whales points markets](https://app.whales.market/points-markets)
- [MARKET DATA] Hyperliquid has no TORI perp on the main universe (234 assets) or on HIP-3 dexes xyz, flx, vntl, hyna, km, abcd, para, mkts and io. — [Hyperliquid info API](https://api.hyperliquid.xyz/info)
- [MARKET DATA] Aevo has no TORI perp among its 102 perpetual markets. — [Aevo API](https://api.aevo.xyz/markets?instrument_type=PERPETUAL)
- Searches of trackers found no quoted OTC or points price for Cores. — [UseTheBitcoin](https://usethebitcoin.com/airdrop/tori-finance/); [Airdrops.io](https://airdrops.io/tori-finance/); [AlphaDrops](https://alphadrops.net/airdrops/tori)

### Inferences
- **Conditional FDV curve.** The FDV market resolves No if there is no launch, so each rung is P(launch by end-2027) × P(FDV > X | launch). Dividing by 0.665 gives these rough conditional odds of FDV above each level: $50M about 41%, $100M about 34%, $200M about 29%, $300M about 25%, $500M/$700M/$1B about 16%. The flat 0.105 at $500M, $700M and $1B looks like stale or passive quotes rather than a real distribution. The implied median FDV at launch is below $50M, but with a fat right tail. The books are very thin (the $100M strike carries most of about $16.7K lifetime volume), so this is a weak signal.
- The two events are inconsistent at the margin. Launch by end-2027 is 0.665 while the $50M strike is only 0.275, so traders implicitly expect a sub-$50M FDV in roughly 59% of launch scenarios. That seems pessimistic next to a Delphi-led seed and $73M TVL, and reflects illiquidity more than considered pricing.
- **Rising TGE odds.** Every dated launch rung rose over the last month (+7 to +17.5 points). This fits the September burst of growth announcements, but no official hint drove it.
- **No live 2026 TGE window priced.** Only 39% by Dec 31, 2026, and the Sep 30, 2026 rung is untraded. This fits the Pendle markets maturing on Nov 26, 2026 (per CoinGecko) sitting before any priced-in TGE.
- **Rough Core supply (my estimate, not sourced).** About $50M × 30 Cores/$/day × about 30 days of pre-deposit ≈ 45B Cores. Add about $55–73M TVL × about 15 Cores/$/day (the unofficial post-boost rate) × about 60 days ≈ 50–65B more. That puts the total near 95–110B Cores by end-September, before counting Pendle/DeFi multipliers and the 10% referral bonus. At a $100M FDV with a 5–10% community allocation, that is about $0.00005–0.0001 per Core. This is an illustration only. Tori has not published total Cores or any allocation.

### Gaps
- I did not check Binance pre-market or Bybit/OKX pre-market. No search result suggested a Tori listing there.
- No points OTC price anywhere, so I cannot record a $/Core quote.
- Polymarket price history before the current snapshot came only from the 1-week and 1-month change fields; I did not pull a full time series.

---

## Q3. What do KOLs and analysts estimate for Tori's FDV or airdrop value per point?

### Takeaway
I found no published KOL or analyst estimate of Tori's FDV or $/Core in English, Chinese, Korean or Vietnamese sources. Commentary covers the product (an "on-chain bank carry trade", about 12% APY) and its risks. Sentiment runs cautiously positive, and every airdrop guide stresses that the token is unconfirmed.

### Cited Findings
- [3RD-PARTY, 2026-04-07] DeFi Dad on X: "Tori is promising to bring a real-world tokenized yield onchain that you can access permissionlessly, earn passively (15% APY), and borrow against... their @AccountableData dashboard tracking reserves backing trUSD/strUSD. We just…" (truncated in the snippet). The date comes from decoding the tweet ID. — [DeFi Dad on X](https://x.com/DeFi_Dad/status/2041570403395486143)
- [3RD-PARTY, 2026-08-08] Serenity Research (Kane), "[Serenity Premium] Tori Finance and trUSD, the bank carry trade on-chain". It frames the core trade as "borrow in a low-rate currency, deposit in a high-rate global market, hedge the currency risk back". It compares Tori with sUSDe at 4.01% and Falcon sUSD at 4.10%, and with Ethena ($3.88bn TVL) and Falcon ($1.26bn). It notes a 10% performance fee and a 7-day unstaking cooldown. The FDV and risk sections are paywalled. — [Serenity Research](https://serenityresearch.substack.com/p/serenity-premium-tori-finance-and)
- [3RD-PARTY, 2026-07-30] KuCoin blog, "What is strUSD and is its 12% yield safe?", lists these risks: counterparty exposure to prime brokers and banks, reliance on "human operators and external entities", possible de-pegging in a liquidity crunch, and the protocol being "yet to be stress-tested through a prolonged macro crisis". It advises against treating strUSD as a substitute for USDC. There is no FDV estimate. — [KuCoin](https://www.kucoin.com/blog/what-is-strusd-and-is-its-12-yield-safe)
- [3RD-PARTY, 2026-08-20] CoinGecko Learn explains Pendle PT/YT for trUSD and strUSD (YT carries about 33x floating-yield leverage) and says "None of this is risk-free". There is no token discussion. — [CoinGecko](https://www.coingecko.com/learn/pendle-tori-trusd-strusd-institutional-yield)
- [3RD-PARTY, Chinese KOL] On Sep 22, 2026 Tori retweeted @KazumaxCrypto: "你知道Tori的策略没有任何crypto风险曝露吗? 你知道Tori其实是专门耕耘非美元, 新型市场的汇率的吗?" ("Did you know Tori's strategy has no crypto risk exposure? Did you know Tori actually specialises in non-USD, emerging-market FX?"). — [X @tori_finance retweet (syndication pull)](https://x.com/tori_finance)
- [3RD-PARTY] Airdrop guides say: "Treat any future distribution as a possibility rather than a promise." — [UseTheBitcoin](https://usethebitcoin.com/airdrop/tori-finance/); "Airdrop unconfirmed" — [Airdrops.io](https://airdrops.io/tori-finance/)
- A search for FDV or "worth it" analyses returned nothing: "The search results do not contain any specific FDV... estimate." (WebSearch, 2026-09-28; results included [AirdropAlert](https://airdropalert.com/airdrops/tori-finance/), [CryptoRank drophunting](https://cryptorank.io/drophunting/tori-finance-activity1224))

### Inferences
- The only market-based FDV signal is the thin Polymarket ladder (Q2). A writer who needs a number has to build it from comparables such as Ethena/ENA, Falcon/FF or Resolv, which are outside this scope.
- KOL coverage is thin and mostly sponsored, educational or exchange-blog content (KuCoin, CoinGecko, Bitget, MEXC). I found no strong independent "alpha" threads, which fits the small follower base.

### Gaps
- Serenity's full report is paywalled, so its FDV view and risk section are unknown.
- I searched Vietnamese (kèo airdrop), Chinese (积分, 撸毛) and Korean (에어드랍) terms and found no specific community estimates.
- I did not review YouTube beyond the Delphi Podcast listing.

---

## Q4. What is the follower count and community size trend on X, Telegram and Discord?

### Takeaway
The community is small but growing slowly. The X account has 6,163 followers. Discord has 819 members, with 141 online. The CN and KR Telegram groups have 42 and 12 members. Engagement on posts is modest (usually 5 to 120 likes), with occasional spikes on major launches. Growth in TVL (about $0 to $73M in three months) is much stronger than growth in social audience. That points to a capital-heavy base of whales, Pendle and Morpho users, not retail farmers.

### Cited Findings
- [MARKET DATA, 2026-09-28] X @tori_finance: **6,163 followers**, 9 following, 182 tweets, 93 media, joined Jun 1, 2025, verified "organization", bio "Institutional yield, on-chain. Backed by @Delphi_Ventures". — [fxtwitter API](https://api.fxtwitter.com/tori_finance); [X profile](https://x.com/tori_finance)
- [3RD-PARTY, undated] An earlier search snapshot put the account at 5,775 followers, which suggests growth of about 400 recently. The snapshot date is unknown, so treat this as indicative. — WebSearch summary citing [X @tori_finance](https://x.com/tori_finance)
- [MARKET DATA] Engagement on recent posts (Sep 2026): the "$1M rewards distributed" post got 90 likes and 20 replies. The Monad launch got 120 likes. The BitGo post got 443 likes but only 5 RTs, a like/RT ratio that may suggest boosted or promoted engagement (unverified). The Sep 10 CN/KR/nine-languages post got 73 likes. The Tenor post got 37 likes. The Morpho etrUSD post got 45. The "not affected by fund wind-downs" post got 80. The strUSD launch (Jul 27) is the high-water mark at 313 likes, 43 RTs and 81 replies. — [X syndication timeline](https://syndication.twitter.com/srv/timeline-profile/user-id/1929232230884200449)
- [MARKET DATA, 2026-09-28] Discord "Tori Finance" (guild ID 1427720889839128758): **819 members, 141 online**. Description: "The official community hub for Tori Finance". — [Discord invite](https://discord.gg/torifinance)
- [MARKET DATA, 2026-09-28] Telegram "Tori 中文" (@Tori_CN): **42 members, 12 online**. Telegram "Tori KOREA" (@ToriFinance_KR): **12 members, 7 online**. Both opened around Sep 10, 2026. — [t.me/Tori_CN](https://t.me/Tori_CN); [t.me/ToriFinance_KR](https://t.me/ToriFinance_KR); [X post Sep 10](https://x.com/tori_finance/status/2097961000964350270)
- [MARKET DATA] Growth in TVL and trUSD supply (DefiLlama, listed Jun 24, 2026): $0 on Jun 24 → $46.0M on Jun 27 → about $50.0M flat through Jul 27 (the pre-deposit cap) → $55.0M on Aug 2 → $63.8M on Aug 14 → $66.2M on Sep 1 → $67.9M on Sep 22 → **$73.07M on Sep 28**. trUSD circulating supply is $73.06M, against $67.96M a week earlier and $66.17M a month earlier. The price is $1.0002. — [DefiLlama protocol](https://defillama.com/protocol/tori-finance); [DefiLlama stablecoin](https://defillama.com/stablecoin/tori-trusd)
- [OFFICIAL] The app and website were translated into nine languages on Sep 10, 2026, "as we expand globally". — [X post](https://x.com/tori_finance/status/2097961000964350270)

### Inferences
- The social footprint is very small next to TVL. The ratio of TVL to X followers is about $12K per follower, which fits a whale- and integration-driven depositor base. It also points to lower airdrop dilution from sybil farmers than broad retail campaigns see, though the capital-weighted Cores system means whales dominate the allocations anyway.
- TVL growth slowed after August (about +10% from Sep 1 to Sep 28). There was a jump of about $4.6M around Sep 23–25, coinciding with the Monad and Morpho AUSD launch and the AMA.
- The new CN and KR groups are tiny after about 2.5 weeks, so the Asia push has not yet produced community traction.

### Gaps
- I have no historical follower series for X (Social Blade and similar were not accessed), so the X trend rests on two data points.
- No historical Discord member counts.
- No English Telegram exists to measure.

---

## Q5. What do users say (sentiment and concerns), and are there red flags such as anonymity, incidents, controversies or TGE delays?

### Takeaway
I found no public evidence of depeg events, withdrawal failures, exploits or broken TGE promises. trUSD has held its peg, the founder is public, and there are named custodians, auditors and a risk curator. The main concerns are structural. The yield depends on off-chain, emerging-market FX carry run through counterparties, with KYC-gated primary mint/redeem, a single-entity operator and a short track record. On points, there is no token commitment and no season end date. There is also impersonation risk from a squatted Telegram handle.

### Cited Findings
**Positives and mitigants**
- [3RD-PARTY] trUSD has held par since launch with no depeg events reported (page modified Sep 7, 2026). DefiLlama price is $1.0002 on Sep 28. — [Pharos](https://pharos.watch/stablecoin/trusd-tori/); [DefiLlama](https://defillama.com/stablecoin/tori-trusd)
- [OFFICIAL] The team is not anonymous. Founder Samed Düzçay is named in press, and the company LinkedIn is "tori-labs". — [The Defiant PR (Jul 27, 2026)](https://thedefiant.io/news/press-releases/tori-brings-institutional-trades-on-chain-fills-50m-before-launch); [tori.finance links](https://tori.finance/)
- [OFFICIAL] Security stack: Sherlock and Nethermind audits, Hypernative monitoring, custodians BitGo, Anchorage Digital and Cactus Custody, RockawayX as risk curator and anchor LP, Accountable proof-of-solvency, and Nexus Mutual cover. — [tori.finance](https://tori.finance/); [Tori Docs: Pre-Deposit](https://docs.tori.finance/resources/pre-deposit); [The Defiant](https://thedefiant.io/news/press-releases/tori-brings-institutional-trades-on-chain-fills-50m-before-launch)
- [OFFICIAL] "$1,000,000 in rewards" distributed to users (Sep 27, 2026). — [X post](https://x.com/tori_finance/status/2104192554401239092)

**Concerns and red flags**
- [3RD-PARTY] Pharos risk notes: "Primary minting/redemption require KYC whitelisting; unnamed custodian banks; collateral traced to exchange deposit addresses; no on-chain price feeds for quotes; single-entity operation; brief track record." Mint/redeem is 1:1 against USDC/USDT with a 0.1% fee. — [Pharos](https://pharos.watch/stablecoin/trusd-tori/)
- [3RD-PARTY] KuCoin warns of off-chain counterparty risk, possible depeg in a liquidity crunch, and "yet to be stress-tested through a prolonged macro crisis". — [KuCoin (Jul 30, 2026)](https://www.kucoin.com/blog/what-is-strusd-and-is-its-12-yield-safe)
- [OFFICIAL] Withdrawal friction: strUSD has a 7-day unstaking cooldown (per Serenity). The Ecosystem Vault has a soft lock-up and a 7-day withdrawal period. The pre-deposit had a 30-day hard lock. Tori promoted etrUSD as Morpho collateral on Sep 14 with "Nothing to unwind, no exit queue", which is an implicit answer to exit-liquidity concerns. — [Serenity](https://serenityresearch.substack.com/p/serenity-premium-tori-finance-and); [Tori Docs](https://docs.tori.finance/resources/pre-deposit); [X post](https://x.com/tori_finance/status/2099520124147658911)
- [OFFICIAL] Incident-adjacent reassurance posts:
  - After the Term Finance exploit (Aug 23, 2026), Tori said "Ecosystem Vault participants are fully covered". The words "fully covered" may imply the vault had some exposure that was made whole, as opposed to "zero exposure" for trUSD/strUSD. This is an interpretation and is not confirmed.
  - On Sep 17, 2026 Tori said it was "not affected in any way by the fund wind-downs, forced selling and volatility in local markets", which points to some mid-September market stress. The specific event was not identified in this research.
  — [X @tori_finance](https://x.com/tori_finance); [X post Sep 17](https://x.com/tori_finance/status/2100523360946176201)
- [OFFICIAL] Points risk: Cores "are not a promise of any token or payment". The pre-deposit 2x boost, "the highest planned for the program", has ended, so later depositors earn at lower rates. — [Tori Docs: Cores](https://docs.tori.finance/resources/cores)
- [MARKET DATA] Impersonation risk: `t.me/tori_finance` is not official. It was created Jan 22, 2026, has 4 subscribers, and posts "This username for sale, you can check it at @userpump or contact @geranate". The official site links only @Tori_CN and @ToriFinance_KR. — [t.me/s/tori_finance](https://t.me/s/tori_finance); [tori.finance](https://tori.finance/)
- No TGE delay found. Polymarket's "token by Jun 30, 2026" resolved No, but I found no official TGE promise that this would have broken. — [Polymarket](https://polymarket.com/event/will-tori-launch-a-token-by)
- Name-collision noise: "TORI" is also the ticker of Teritori (an unrelated Cosmos chain) and of "TORI Global" (unrelated). Airdrop and search results mix them up, which is a phishing and confusion risk. — [Airdrops.io Teritori](https://airdrops.io/teritori/); [toriglobal.com](https://www.toriglobal.com/)
- Launch-date inconsistency: one search summary said trUSD "soft-launched on Ethereum on March 24". DefiLlama TVL starts Jun 24, 2026 and the pre-deposit opened Jun 23. The March date may be confused with the seed announcement (Mar 25) or refer to a testnet. — [DefiLlama](https://defillama.com/protocol/tori-finance); [Tori Docs: Cores](https://docs.tori.finance/resources/cores)
- Investor lists also differ: Delphi, QInvest, CMCC Global and Bering Waters ([PANews/Binance Square summary](https://www.panewslab.com/en/articles/019d24a9-7508-7621-9040-5569a9715caf)) versus Delphi, ScaleX Ventures and QInvest ([UseTheBitcoin](https://usethebitcoin.com/airdrop/tori-finance/)).

### Inferences
- I found no evidence of "farming fatigue" or complaints about points dilution in public sources. With a small, whale-weighted user base and only one season so far, the discourse has not matured to that stage. The absence of a TGE timeline is the main latent frustration risk for farmers.
- Depeg risk here comes from EM-FX and counterparty events off-chain, not crypto funding rates. The Sep 17 reassurance post suggests the team watches that tail risk. Any EM-FX turmoil is the scenario to monitor.
- For Pendle YT buyers this means: Tori has made no TGE commitment, the Polymarket odds of a token by Dec 31, 2026 are about 39%, and the Pendle markets mature Nov 26, 2026. Points accrued through YT may therefore not be priced or claimable until well after maturity, if ever. I could not source the Pendle Cores multiplier for YT or LP; Pendle's own newsletter says LP earns "MORE points".

### Gaps
- Discord message content, X reply threads and Telegram chat history were not accessible, so user-level sentiment (complaints about withdrawal delays and the like) could not be sampled directly.
- The Pendle YT/LP Cores multipliers for strUSD and trUSD were not found in public sources.
- The Sep 17 "fund wind-downs" market event was not identified.
- The seed round amount and valuation are undisclosed ([CryptoRank](https://cryptorank.io/ico/tori-finance)).
