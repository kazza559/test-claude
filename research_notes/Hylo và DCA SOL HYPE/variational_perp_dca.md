# Variational Omni: how it works, what it costs, and "DCA with perps" into SOL/HYPE at 2x–3x (as of 30 Sep 2026)

Data-collection notes: the live Omni public stats API was read on 2026-09-30 around 10:16 UTC. Hyperliquid (HL) funding history (hourly, 2025-01-01 to 2026-09-30 09:00 UTC, 15,298 prints per coin) and HL market metadata were pulled from the public HL API the same day. All worked examples were computed by the researcher from parameters in the Variational and HL docs. The formulas are shown so the report writer can check them. Sources that could not be reached are listed under Gaps: web.archive.org (connection closed by the remote), the Arbitrum public RPC (proxy 403), BusinessWire (403), and two community points calculators (HTTP 402).

---

## 1. How does Variational Omni work? (chain, collateral, counterparty/RFQ/OLP, fees and spreads, loss refunds, leverage, margin, liquidation, deposits, scale, audits, incidents)

### Takeaway
Omni runs on Arbitrum and is collateralized in USDC. It has no order book. Every trade is an RFQ against a single in-house market maker, OLP, which is the counterparty to all user trades and hedges on outside venues. Each user's funds sit in their own on-chain settlement pool (User <> OLP). Omni charges no trading fees; it earns from the bid/ask spread, and 20% of spread goes to the protocol treasury. Leverage runs from 1x to 50x. Initial margin (IM) is 1/leverage and maintenance margin (MM) is half of IM, so MM depends on the leverage you pick, not on the asset. Liquidations are partial and carry a 0.5% penalty. As of 30 Sep 2026 Omni was still in private beta and needed an access code. On-chain TVL was about $261M and 24h volume about $3.55B. Audits: Zellic (Dec 2024) and Spearbit (Mar 2025). The status of the "loss refund" program is contradictory: see the findings below.

### Cited Findings
**Architecture and counterparty model**
- Variational is "a protocol for on-chain derivatives trading across crypto, equities, commodities, and forex". It powers two apps: Omni ("a zero-fee perps trading venue") and Pro (institutional OTC). Backers include Dragonfly Capital, Bain Capital Crypto and Coinbase Ventures. — [Variational docs: What Is Variational](https://docs.variational.io/getting-started/readme)
- "Omni is deployed on Arbitrum. You will need an EVM-compatible wallet with USDC on Arbitrum… You do not need ETH: deposits, withdrawals, and authentication are gasless." — [Getting Started with Omni](https://docs.variational.io/omni/getting-started-with-omni)
- "Omni is currently in private beta. You will need an access code to create an account." Access codes are posted in the Variational Discord or on X. The roadmap still lists "Omni public mainnet launch" as not done (docs read 2026-09-30). — [Getting Started with Omni](https://docs.variational.io/omni/getting-started-with-omni); [Roadmap](https://docs.variational.io/getting-started/roadmap)
- Variational is "a request-for-quote (RFQ) protocol, and does not utilize an orderbook." On Omni, OLP "as the only eligible maker on Omni, responds with a quote". OLP gets a "last look" to check the trade against its risk limits. The user then has a final last look against their slippage limit. — [Trading via RFQ](https://docs.variational.io/variational-protocol/key-concepts/trading-via-rfq)
- OLP is "a vertically integrated market maker that acts as the counterparty to all trades on Omni". It has three parts: a USDC vault (smart contract), a market-making engine, and a risk system that hedges on outside venues. "Both OLP and the user are subject to margin requirements." — [The Omni Liquidity Provider (OLP)](https://docs.variational.io/omni/the-omni-liquidity-provider-olp)
- OLP funding: "Initially, the Variational team has provided seed capital for OLP." A community vault is planned once there is a track record. "There is a risk that OLP loses money." — [OLP docs](https://docs.variational.io/omni/the-omni-liquidity-provider-olp). The roadmap lists the "Open community vault for OLP" as not done (2026-09-30). — [Roadmap](https://docs.variational.io/getting-started/roadmap)
- Fund segregation: "All users trading on Omni have their own settlement pools defined as User <> OLP". Each pool is an on-chain contract whose funds are isolated from other pools. "OLP never transfers traders' funds to external venues"; it hedges only with its own capital. "If OLP were insolvent, any unrealized or realized PnL accrued going forward would be considered 'bad debt,' and would not be able to be paid out to the user." — [P2P Trading Protocol vs DEX](https://docs.variational.io/variational-protocol/key-concepts/p2p-trading-protocol-vs-dex); [OLP docs](https://docs.variational.io/omni/the-omni-liquidity-provider-olp)
- The P2P model has no platform backstop: "In an exchange model, if your counterparty has a negative balance, you are still guaranteed payout as long as the exchange is solvent. There is no such backstop in a peer to peer model." — [P2P Trading Protocol vs DEX](https://docs.variational.io/variational-protocol/key-concepts/p2p-trading-protocol-vs-dex)
- Terms of Use: the Company "does not verify and cannot guarantee whether any given settlement pool has sufficient assets or collateral to execute or maintain a transaction." — [Terms of Use](https://docs.variational.io/legal/terms-of-use) (via the docs corpus [llms-full.txt](https://docs.variational.io/llms-full.txt))
- Contracts on Arbitrum: Protocol Treasury 0x5e91…d645, Core OLP Vault 0x74bb…f2cd, Settlement Pool Factory 0x0F82…074C, Oracle 0x84BE…6172. — [Mainnet Contracts](https://docs.variational.io/technical-documentation/mainnet-contracts)

**Prices (index, mark, quote)**
- The index price comes from the in-house Variational Oracle, a "weighted combination of prices on different exchanges". The mark price "is derived from a combination of the underlying asset's spot price (Index Price) and additional data (e.g. funding rates, OLP's current risk profile)". The mark price "is used as the reference price for UPnL, margin calculations and liquidations." Displayed quotes are "indicative"; the firm quote is produced when you click buy or sell. — [Quoted, Index, and Mark Prices](https://docs.variational.io/omni/trading/quoted-index-and-mark-prices); [Variational Oracle](https://docs.variational.io/variational-protocol/key-concepts/variational-oracle)

**Fees and spreads**
- "There are no trading fees on Omni." Deposits and withdrawals cost a flat $0.1 each. The liquidation penalty is covered below. — [Fees](https://docs.variational.io/omni/trading/fees)
- Revenue model: OLP captures spread and hedges externally. "Currently, 20% of spreads paid is transferred to Variational's protocol treasury wallet" (the percentage is "still being tested and is subject to change"). — [OLP docs](https://docs.variational.io/omni/the-omni-liquidity-provider-olp)
- Live quotes on 2026-09-30 ~10:16 UTC from the public API (full bid/ask width, researcher-computed; the API notes quotes may be cached up to 600 s):
  - **SOL** (mark $119.21): 2.43 bps at base/$1k size, 4.45 bps at $100k, 15.94 bps at $1M. API `base_spread_bps` = 2.43.
  - **HYPE** (mark $86.28): 0.86 bps at $1k, 7.91 bps at $100k, 38.31 bps at $1M.
  - — [Omni stats API](https://omni-client-api.prod.ap-northeast-1.variational.io/metadata/stats); field definitions in [API docs](https://docs.variational.io/technical-documentation/api)
- In the order form, "Spread" is "Half of the difference between the bid and ask quotes for your inputted size". Market-order slippage is the gap between mark and quoted price and can be capped with a slippage limit. — [Getting Started with Omni](https://docs.variational.io/omni/getting-started-with-omni); [Slippage](https://docs.variational.io/omni/trading/slippage)
- For comparison, HL perps base-tier fees (14-day volume under $5M) are 0.045% taker and 0.015% maker. — [Hyperliquid docs: Fees](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/fees)

**Loss refunds (status is contradictory)**
- Secondary sources describe the historical mechanism as follows:
  - Datawallet (updated 28 Sep 2026): a lottery-style "1% to 5% probability of a refund, determined by the account's reward tier", a "luckiness multiplier", and a single refund capped at 20% of the refund pool. Datawallet describes the program as "Active". — [Datawallet](https://www.datawallet.com/crypto/variational-explained)
  - AltcoinBuzz (17 Aug 2026): "10% of spreads paid on Omni" funds a loss-refund pool, with odds by tier. — [AltcoinBuzz](https://www.altcoinbuzz.io/how-to-maximize-variational-points)
  - A search-engine summary said 1/6 of spread funded the pool; I could not verify this.
- Official evidence points the other way on 30 Sep 2026:
  - The live API shows `loss_refund.pool_size = "0"` and `refunded_24h = "0"` (2026-09-30 10:16 UTC). The API docs' sample response dated 2026-01-06 showed pool_size $106,919.70 and refunded_24h $25,475.04. — [Omni stats API](https://omni-client-api.prod.ap-northeast-1.variational.io/metadata/stats); [API docs](https://docs.variational.io/technical-documentation/api)
  - The current Rewards doc lists only tiers, a 0% fee rate and points boosts. There is no loss-refund column, and the URL `docs.variational.io/omni/rewards/loss-refunds` returns "Page Not Found". — [Rewards](https://docs.variational.io/omni/rewards)
  - The Terms of Use list "loss refunds" as a discretionary "Trading Incentive" that "may [be] discontinue[d]… at any time without any notice". — [Terms of Use](https://docs.variational.io/legal/terms-of-use)

**Leverage, margin and liquidation (official parameters)**
- Leverage is selectable "from a minimum of 1x to a maximum of 50x"; Omni markets itself as "up to 50x". — [Getting Started with Omni](https://docs.variational.io/omni/getting-started-with-omni). Datawallet says 50x is available on "major pairs (BTC, ETH, SOL)". — [Datawallet](https://www.datawallet.com/crypto/variational-explained). I found no official per-market cap for HYPE.
- "Leverage is defined as `1 / initial_margin_percentage`." "Generally speaking, the maintenance margin requirement will be half that of the initial margin requirement. Example: 5x leverage = 20% initial margin requirement and 10% maintenance margin requirement." The docs also say: "Decreasing your leverage will increase both your initial margin and maintenance margin requirements… Decreasing your leverage may move your estimated liquidation price closer." — [Leverage](https://docs.variational.io/omni/trading/leverage); [Margin](https://docs.variational.io/omni/trading/margin)
- Margin modes: "On certain markets users have the ability to toggle between isolated margin and cross margin mode." In cross mode, "your USDC balance is used to collateralize every position in cross margin mode". In isolated mode, "you have to deliberately add or remove USDC collateral for one position… Liquidations will only affect this one position." A closed isolated position's balance "is automatically swept to the cross margin account." Isolated margin was a completed roadmap item. — [Margin](https://docs.variational.io/omni/trading/margin); [Roadmap](https://docs.variational.io/getting-started/roadmap)
- Liquidation trigger: "maintenance margin >=100%", computed "using a very fast EMA of the mark price", which "dampens the effect of sudden wicks". "Omni performs partial liquidations, meaning only the necessary quantity… to bring maintenance margin back under 100% is liquidated at a time." Execution is at "bid - 0.5%" for a long: "the platform-wide liquidation penalty on Omni is currently set to 0.5%". — [Liquidation](https://docs.variational.io/omni/trading/liquidation)
- ADL / counterparty liquidation: if OLP itself falls below margin, "the user's position is closed at the settlement price plus a liquidation reward (the user gains the liquidation penalty)". This can happen in "extreme volatility" or when OLP faces "severe liquidity constraints". — [ADL / Counterparty Liquidation](https://docs.variational.io/omni/trading/automatic-deleveraging-counterparty-liquidation)
- Risk limits can reject orders in several ways:
  - Per-user gross/net/per-instrument notional caps.
  - OLP value-at-risk and notional caps ("OLP is currently at its maximum risk capacity").
  - Skew and OI caps set as a percent of the token's FDV (`SkewAsPercentOfFdvLimit`, `OiAsPercentOfFdvLimit`).
  - `GlobalConfigsCheck`: "Trading is currently disabled by admins."
  - — [Risk Limits / Rate Limits](https://docs.variational.io/omni/trading/risk-limits-rate-limits)
- Withdrawals from a settlement pool: "A user may withdraw the unused balance from the pool, up to the maintenance margin requirement." — [Settlement Pools](https://docs.variational.io/variational-protocol/key-concepts/settlement-pools). Funds can only be withdrawn to the connected wallet. — [Getting Started with Omni](https://docs.variational.io/omni/getting-started-with-omni)

**Order types (for laddered entries)**
- Market, Limit and "Pro" order types (Pro covers Trigger and TP/SL). Limit orders fill when "OLP's quoted price crosses the set limit price". They are "currently all-or-nothing" (partial fills are on the roadmap) and are checked every 0.1 s. "Both limit and trigger orders expire 120 days after being placed." Trigger orders fire a market order when the mark price crosses the trigger. — [Market, Limit, and Trigger Orders](https://docs.variational.io/omni/trading/market-limit-and-trigger-orders)
- TP/SL orders are market orders triggered by the mark price (default) or the quoted price. They expire after 120 days and are checked every 0.1 s. "If the mark price also crosses a liquidation price within 0.1 seconds of crossing the trigger price, it is possible for a liquidation to trigger before a TP/SL." They "will only process when both the trigger condition is met and the estimated slippage is within the defined slippage limit. Otherwise, the order will remain pending." An auto-resize option keeps TP/SL alive through partial closes and liquidations. — [Take Profit and Stop Loss](https://docs.variational.io/omni/trading/take-profit-and-stop-loss)
- The order form includes "Reduce Only" (rejects any order that would increase or flip a position). "Size" is "the after leverage sizing", meaning you enter notional, not margin. The positions table shows the estimated liquidation price, position margin and cumulative funding, and supports partial or full Close, Reverse, and Add TP/SL. The portfolio panel shows "MM Usage" (Maintenance Margin / Account Balance), "Margin Ratio" (Initial Margin / Account Balance) and "Portfolio Leverage". — [Getting Started with Omni](https://docs.variational.io/omni/getting-started-with-omni)

**Access restrictions**
- Restricted persons include US and Canadian persons, Taiwan, Cuba, Iran, North Korea, Sudan, Syria, occupied regions of Ukraine and US territories. Vietnam is not on the list (last updated 20 Apr 2026). — [Restricted Persons](https://docs.variational.io/legal/restricted-persons)

**Scale (TVL, OI, volume)**
- Live API, 2026-09-30 ~10:16 UTC:
  - TVL $260.84M ("in settlement pools and the OLP vault")
  - `open_interest` field $2,082.7M
  - 24h volume $3,554.7M
  - cumulative volume $370.79B
  - 555 markets
  - — [Omni stats API](https://omni-client-api.prod.ap-northeast-1.variational.io/metadata/stats)
- The same API's sample dated 2026-01-06 showed TVL $100.7M, OI $901.7M, 24h volume $1,852.9M, cumulative $108.67B and 486 markets. — [API docs](https://docs.variational.io/technical-documentation/api)
- OI definition check (researcher-computed): summing per-market long plus short OI across all 555 listings gives $1,041.35M (long $695.4M, short $346.0M). The platform-level `open_interest` field ($2,082.7M) is exactly twice that. DefiLlama reports $1,020M (24h, 2026-09-30); its series shows $429.7M (2026-01-04), $319.4M (2026-04-04), $570.2M (2026-07-03) and $744.1M (2026-09-01). DefiLlama tags the protocol's chain as "Off Chain" and lists 0 audits in its metadata. — [Omni stats API](https://omni-client-api.prod.ap-northeast-1.variational.io/metadata/stats); [DefiLlama OI API](https://api.llama.fi/summary/open-interest/variational); [DefiLlama protocol API](https://api.llama.fi/protocol/variational)
- SOL and HYPE on Omni (2026-09-30 ~10:16 UTC):

| Market | OI long | OI short | Total OI | Long share | 24h volume | Funding interval |
|---|---|---|---|---|---|---|
| SOL | $23.63M | $13.31M | $36.94M | 64% | $53.0M | 8h |
| HYPE | $22.72M | $6.10M | $28.82M | 79% | $52.4M | 8h |

  — [Omni stats API](https://omni-client-api.prod.ap-northeast-1.variational.io/metadata/stats)
- HL on the same date: SOL OI 5.69M SOL (~$680M) with 24h notional volume $216.3M; HYPE OI 20.46M HYPE (~$1.77B) with $417.1M. — [HL API metaAndAssetCtxs](https://api.hyperliquid.xyz/info)
- Alea Research (6 Jan 2026): Omni OI ~ $900M ("5th on DefiLlama"), ~$1.7B average daily volume, ~15K active addresses (27K received retroactive points). It flags incentive-driven "capital rotation" and OLP counterparty concentration as risks. — [Alea Research](https://alearesearch.substack.com/p/variational)

**Audits, bug bounty, incidents, funding**
- Audits: Zellic (completed December 2024) and Spearbit (completed March 2025); the report files are attached on the docs page. The bug bounty runs on Immunefi. — [Audits](https://docs.variational.io/technical-documentation/audits); [Bug Bounties](https://docs.variational.io/technical-documentation/bug-bounties). Datawallet claims "full public reports not released" (28 Sep 2026), which conflicts with the attachments on the docs page. — [Datawallet](https://www.datawallet.com/crypto/variational-explained)
- Incidents: searches on 2026-09-30 found no reported exploit, hack, bad-debt event or major outage for Variational Omni. The "Omni" hacks in results (NFT lender, July 2022, ~$1.4M) belong to an unrelated protocol. — [Immunefi hack analysis (different "Omni")](https://medium.com/immunefi/hack-analysis-omni-protocol-july-2022-2d35091a0109)
- Raise: a BusinessWire release dated 2026-05-20 is titled "Variational Secures ~$50M to Bring Liquidity from Traditional Markets To Crypto". Only the title was seen; the page returned 403. — [BusinessWire](https://www.businesswire.com/news/home/20260520402312/en/Variational-Secures-$50M-to-Bring-Liquidity-from-Traditional-Markets-To-Crypto)

### Inferences
- Omni is an RFQ broker with its own market maker. The user's counterparty is always OLP, so the user's winnings depend on OLP's solvency within the user's settlement pool, not on a shared insurance fund. This removes contagion from other users but concentrates risk in one team-seeded, opaque market maker.
- Trading costs for a small DCA are negligible on Omni. From the quoted spreads, entering and later exiting $10,800 of SOL costs about $2.6 and HYPE about $0.9. On HL at base-tier taker fees the same round trip costs about $9.7 (0.045% × 2). For a slow DCA, **funding is the dominant cost**, not fees or spreads (see Q2).
- The mark price includes "OLP's current risk profile" and liquidations key off an EMA of that mark. The counterparty therefore has some influence over the price used to liquidate you. This is less transparent than HL's documented mark-price formula (median of oracle+EMA, book, and CEX perp mids per [HL docs](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/robust-price-indices)).
- Loss refunds: given an empty pool in the live API, a removed docs page, and discretionary Terms, a user should **not count on loss refunds** as of 30 Sep 2026, whatever secondary sites say.
- HYPE on Omni was 79% long (by OI) on 30 Sep 2026. OLP is therefore net short HYPE, and skew/OLP-capacity limits could in principle reject new longs in a crowded market.

### Gaps
- No official per-market max leverage for SOL or HYPE on Omni (only the platform-wide 1x–50x). Irrelevant at 2–3x, but unverified.
- Whether isolated margin is enabled for SOL/HYPE specifically ("on certain markets") is not verified.
- Loss-refund status: no official announcement of discontinuation found. Wayback Machine snapshots of older docs were unreachable (connection closed by the remote).
- OLP vault balance, OLP PnL and hedge venues are not published. An on-chain read via the public Arbitrum RPC was blocked by the proxy (403).
- Contents of the Zellic and Spearbit PDFs were not reviewed.

---

## 2. Funding on Omni for SOL and HYPE vs Hyperliquid, and the yearly cost of holding a 2x–3x long

### Takeaway
Omni uses the same funding formula as HL and the major CEXs: premium plus an interest-rate term clamped to ±0.05%. The fixed interest term is 0.00125% per hour, or **10.95% per year paid by longs to shorts when the perp trades at no premium**. On 30 Sep 2026 Omni showed SOL at +10.81% APR and HYPE at +5.96% APR, both paid every 8h. Omni does not publish funding history. On HL, SOL averaged +3.0% APR and HYPE +16.6% APR from Jan 2025 to Sep 2026. HYPE longs paid +22.1% in 2025 and about +9.2% in 2026 year to date; SOL was about 0% in 2026 year to date. At "neutral" funding, holding $10,800 notional (interpretation A at 3x) costs about $1,183 a year, 29.6% of $4,000 capital. Holding $3,600 notional (interpretation B) costs about $394 a year, 9.9% of capital.

### Cited Findings
- **Omni formula**: `Funding Rate (F) = Average Premium Index (P) + clamp(interest rate − P, −0.0005, 0.0005)`, where premium = impact price difference / index price.
  - The premium is sampled every 60 s and averaged with linearly increasing weights (2i/(N(N+1))).
  - The interest rate is "fixed at 0.00125% / hour". The funding rate "is capped at 2% per hour, except in certain special circumstances where a manual override is necessary."
  - Impact prices use RFQ quotes at a $7,500 "impact margin notional", counting base spread only.
  - The calculation window matches Bybit's, else Binance's, else 1h. For an 8h market, "in hours 1-7, the hourly funding rate will be 0. In hour 8, the funding rate will be computed off the previous 8 hours of data."
  - "A positive funding rate means longs pay shorts."
  - — [Omni Funding Rates](https://docs.variational.io/omni/trading/funding-rates)
- **Omni snapshot (API, 2026-09-30 ~10:16 UTC)**:

| Market | `funding_rate` | Implied APR | Interval |
|---|---|---|---|
| SOL | 0.108092 | 10.81% | 28,800 s (8h) |
| HYPE | 0.059554 | 5.96% | 28,800 s (8h) |
| BTC | 0.059003 | 5.90% | — |
| ETH | 0.1095 | 10.95% | — |

  - 279 + 51 = 330 of the 462 markets with non-zero funding (71%) showed exactly 0.1095.
  - The API docs say funding rates "are decimals (multiply by 100 for percentage)".
  - — [Omni stats API](https://omni-client-api.prod.ap-northeast-1.variational.io/metadata/stats); [API docs](https://docs.variational.io/technical-documentation/api)
- **HL formula**: the same structure (premium + clamp(interest − premium, ±0.05%)), with the interest component "0.01% every 8 hours, which is 0.00125% every hour". HL's docs call this "11.6% APR paid to short" (compounded; simple annualization is 10.95%). HL pays funding hourly, caps it at 4%/hour, and computes the payment on oracle-price notional. — [Hyperliquid docs: Funding](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/funding)
- **HL current (2026-09-30 ~10:00 UTC)**: SOL funding 0.00125%/h (10.95% APR). HYPE funding −0.00053%/h (−4.61% APR, shorts paying longs). HL max leverage: SOL 20x, HYPE 10x. — [HL API metaAndAssetCtxs](https://api.hyperliquid.xyz/info)
- **HL realized funding, researcher-computed from HL API `fundingHistory`** (hourly prints 2025-01-01 → 2026-09-30 09:00 UTC; APR = mean hourly rate × 8,760) — [HL API fundingHistory](https://api.hyperliquid.xyz/info):

| Period | SOL avg APR | HYPE avg APR |
|---|---|---|
| 2025 (full year) | +5.31% | +22.07% |
| 2026 YTD (to 30 Sep) | −0.06% | +9.17% |
| Jan 2025–Sep 2026 | +3.01% | +16.56% |
| Last 365 days | −0.17% | +9.79% |
| Last 180 days | +3.84% | +9.46% |
| Last 90 days | +7.20% | +10.15% |
| Last 30 days | +7.30% | +9.18% |
| Last 7 days | +9.61% | +8.55% |
| Share of hours exactly at baseline (0.00125%/h) | 44.3% | 68.3% |
| Highest single hour | +0.0138%/h (2025-01-19 05:00 UTC; ≈121% annualized) | +0.0886%/h (2025-01-19 10:00 UTC; ≈776% annualized) |
| Lowest single hour | −0.2051%/h (2025-10-10 22:00 UTC crash) | −0.1866%/h (same hour) |

- **HL monthly average APR** (same dataset):

| Month | SOL | HYPE |
|---|---|---|
| 2025-01 | 11.1% | 55.3% |
| 2025-02 | 1.3% | 30.0% |
| 2025-03 | −1.8% | 22.3% |
| 2025-04 | −5.9% | 11.6% |
| 2025-05 | 10.6% | 32.9% |
| 2025-06 | 6.9% | 19.8% |
| 2025-07 | 19.9% | 26.8% |
| 2025-08 | 11.8% | 14.1% |
| 2025-09 | 10.9% | 17.3% |
| 2025-10 | −4.8% | 10.2% |
| 2025-11 | −2.4% | 12.3% |
| 2025-12 | 5.5% | 12.1% |
| 2026-01 | 3.1% | 11.7% |
| 2026-02 | −17.6% | 7.0% |
| 2026-03 | −9.7% | 6.9% |
| 2026-04 | −0.5% | 5.1% |
| 2026-05 | 3.2% | 7.4% |
| 2026-06 | −2.2% | 14.0% |
| 2026-07 | 5.9% | 9.4% |
| 2026-08 | 8.7% | 11.8% |
| 2026-09 (to 30th) | 7.2% | 9.2% |

### Inferences
- **The API's `funding_rate` is annualized.** The modal value 0.1095 equals 0.0000125/h × 8,760 h exactly, the documented interest-only rate. SOL at 0.108092 therefore means about 10.81% APR, charged as about 0.0099% per 8h interval.
- Because Omni's premium is measured from OLP's own quotes (base spread) against the index, OLP's quoting indirectly shapes funding. In a crowded-long market (HYPE 79% long on Omni), long funding may stay positive even when HL is negative, as on 30 Sep 2026: Omni HYPE +5.96% vs HL HYPE −4.61%. Omni funding can differ materially from HL.
- **Yearly carry cost of the long** (simple; notional at entry; researcher-computed):

| Funding assumption | A-3x ($10,800) | A-2x ($7,200) | B ($3,600) |
|---|---|---|---|
| Neutral baseline 10.95% | $1,183/yr (29.6%) | $788/yr (19.7%) | $394/yr (9.9%) |
| Omni SOL now 10.81% | $1,167/yr (29.2%) | $778/yr (19.5%) | $389/yr (9.7%) |
| Omni HYPE now 5.96% | $643/yr (16.1%) | $429/yr (10.7%) | $214/yr (5.4%) |
| HL HYPE 2025 avg 22.07% | $2,384/yr (59.6%) | $1,589/yr (39.7%) | $795/yr (19.9%) |
| HL HYPE 2026 YTD 9.17% | $990/yr (24.8%) | $660/yr (16.5%) | $330/yr (8.3%) |
| HL SOL Jan25–Sep26 3.01% | $325/yr (8.1%) | $217/yr (5.4%) | $108/yr (2.7%) |
| HL SOL 2026 YTD −0.06% | ≈ $0 (slight income) | ≈ $0 | ≈ $0 |

  - Percentages are of the $4,000 capital.
  - Rule of thumb: yearly cost as % of capital = funding APR × (total notional ÷ capital), where notional ÷ capital is 2.7 for A-3x, 1.8 for A-2x and 0.9 for B.
  - Spot has no funding cost. Positive funding is a structural drag on a long perp "DCA" held for months.
- In cross margin, funding payments come out of collateral and push the liquidation price up over time. Worked out in Q4: for A-3x, one year at 10.95% moves the HYPE liquidation price from $52.16 to $61.24.

### Gaps
- No historical funding series for Omni was found. The public API gives only a live snapshot; the in-app history and the Dune dashboard (entropy_advisors/variational-protocol) were not accessible as data. Omni's 2025–2026 average funding for SOL and HYPE is therefore unknown; the HL series is the best available proxy.
- Coinglass/Laevitas cross-venue funding was not pulled. HL's own API was used as the primary source instead.

---

## 3. Variational points and $VAR: TGE status, how points are earned, and whether a slow DCA-perp strategy earns meaningful points

### Takeaway
As of 30 Sep 2026, $VAR had **not** launched. The official docs say it "will be launched in Q4 2026". Polymarket priced launch by 31 Oct at 18.5%, by 30 Nov at 69.5% and by 31 Dec at 89.1%. At TGE, 32% of supply goes to points holders, fully unlocked. About 150,000 points are issued weekly, and weekly distributions "conclude no later than the end of Q4 2026". The official points formula is not published: it is described only as "platform activity". A third-party estimate, unverified and seen only in a search snippet, says holding open interest earns far more points than volume. Under that estimate, a $10,800 position (A-3x) might earn about 0.9 points a week and a $3,600 position (B) about 0.3. At Polymarket-implied values of roughly $37–$59 per point, that is about $170–$715 (A-3x) or $58–$239 (B) over the 5–13 remaining weekly distributions. The funding cost over the same period at the neutral rate would be $114–$296 (A-3x) or $38–$99 (B). **All of this is highly speculative.**

### Cited Findings
- "**The Variational token ($VAR) will be launched in Q4 2026.**" Allocation:
  - Genesis Distribution 32%: "airdropped proportionally to points holdings", 100% unlocked at TGE.
  - Ecosystem Reserve 18%.
  - Team and Investors 50%: locked 12 months, then unlocking over at least 3 years.
  - "We intend to use 100% of revenue directed to the treasury to buy and burn the $VAR token."
  - — [$VAR docs](https://docs.variational.io/token/usdvar)
- Points program:
  - Launched 17 Dec 2025. 3,000,000 points were distributed retroactively "based on a variety of activity metrics through December 11".
  - Weekly distributions come every Friday for "the previous week's platform activity".
  - "Weekly point distributions will conclude no later than the end of Q4 2026."
  - Referrers get 1 point per 10 points their referrals earn. Pre-launch traders get a +10% boost. Tier boosts range from +0% (Iron) to +5% (Infinity, $2.5B in 30-day volume).
  - "Variational reserves all rights to modify the points program or point totals at its sole discretion."
  - — [Points](https://docs.variational.io/omni/rewards/points); [Rewards](https://docs.variational.io/omni/rewards)
- Tier thresholds: Bronze needs ≥$1M in 30-day volume (+0.5% points). Referral codes unlock at $1M volume; referrers earn 5% of referees' spread in USDC. — [Rewards](https://docs.variational.io/omni/rewards); [Referrals](https://docs.variational.io/omni/rewards/referrals)
- The weekly issuance was 150k points from Dec 2025 (Alea Research, 6 Jan 2026). — [Alea Research](https://alearesearch.substack.com/p/variational)
- ChainCatcher (25 Sep 2026):
  - TGE "pushed back"; points continue "until VAR completes TGE in the fourth quarter", with "an additional 150,000 points… added weekly".
  - About 9.15M points by the end of Q3; 10–11M points expected in total.
  - At the time: Polymarket median FDV about $1.53B, expected FDV about $1.85B, and value per point "approximately between 44.5 and 59.2 dollars".
  - Users "must hold at least 1 point to be eligible".
  - — [ChainCatcher](https://www.chaincatcher.com/en/article/2292254)
- Polymarket (read via the gamma API on 2026-09-30):
  - "Will Variational launch a token by…": 30 Sep 2026 Yes = 0.05%; 31 Oct 2026 = 18.5%; 30 Nov 2026 = 69.5%; 31 Dec 2026 = 89.1%.
  - "Variational FDV above ___ one day after launch?" (event volume about $3.11M): >$100M 97.95%; >$300M 91.85%; >$500M 83%; >$800M 73.5%; >$1B 61%; >$2B 30%; >$3B 14.25%; >$4B 5.15%; >$5B 4.35%.
  - — [Polymarket FDV market](https://polymarket.com/event/variational-fdv-above-one-day-after-launch); [Polymarket launch-date market](https://polymarket.com/event/will-variational-launch-a-token-in-2025) (data via [gamma API](https://gamma-api.polymarket.com/public-search?q=variational))
- **Unverified third-party estimate** (search-result snippet; the source pages returned HTTP 402 when fetched): "Holding money open earns approximately 86.3 points per $1M held open interest per week, compared to approximately 9.6 points per $1M traded in volume per week". The snippet also says 150,000 points are split weekly, "so the more total volume and open interest there is, the fewer points each dollar earns". — [funding-farm.vercel.app](https://funding-farm.vercel.app/); [variational-ev.vercel.app](https://variational-ev.vercel.app/); [X article "Variational Points Valuation"](https://x.com/shaundadevens/article/2103526724562477539)
- AltcoinBuzz (17 Aug 2026) says the official formula is not disclosed, and that "Variational has not guaranteed that its points will convert into a token or provide a specific future payout." — [AltcoinBuzz](https://www.altcoinbuzz.io/how-to-maximize-variational-points)
- The On-Chain Trader Rewards Campaign (from 12 Aug 2026) pays points and USDC only to about 10,000 pre-listed on-chain addresses reaching $1M–$50M volume milestones. It is not relevant to a small DCA user. — [Trader Rewards Campaign](https://docs.variational.io/omni/trader-rewards)
- Points under campaign terms "have no cash value, and confer no right, title, interest, or expectation in or to any token". — [Trader Rewards Campaign terms](https://docs.variational.io/omni/trader-rewards)

### Inferences
- **Polymarket-implied FDV** (researcher interpolation of the 30 Sep ladder): median about $1.28B (log interpolation) to $1.35B (linear); mean about $1.7–1.8B depending on the tail assumption. **Implied value per point** = 0.32 × FDV ÷ total points:
  - 10M points: $41.0 at a $1.28B FDV, $43.5 at $1.36B, $49.0 at $1.53B, $59.2 at $1.85B.
  - 11M points: $37.2, $39.6, $44.5 and $53.8 respectively.
  - Overall range: **roughly $37–$59 per point**, speculative and ignoring the timing of the 1-day-after-launch FDV and sell pressure.
- Weekly distributions left after 30 Sep 2026 (a Wednesday), assuming distributions stop at TGE: 5 Fridays to 31 Oct, 9 to 30 Nov, 13 to 31 Dec.
- **Illustrative points for the DCA plans** (only if the unverified 86.3 pts per $1M OI per week estimate holds and stays constant):

| Plan | Points per week | 5 / 9 / 13 weeks | Value at $37–$59/pt (5 → 13 weeks) | Funding cost at 10.95% (5 / 9 / 13 weeks) |
|---|---|---|---|---|
| A-3x ($10,800 OI) | ≈0.93 | 4.7 / 8.4 / 12.1 pts | ≈ $172–$715 | $114 / $205 / $296 |
| A-2x ($7,200 OI) | ≈0.62 | 3.1 / 5.6 / 8.1 pts | ≈ $115–$476 | $76 / $136 / $197 |
| B ($3,600 OI) | ≈0.31 | 1.6 / 2.8 / 4.0 pts | ≈ $58–$239 | $38 / $68 / $99 |

  - Volume points from one entry plus one exit are small: about 0.2 points for A-3x and 0.07 for B.
  - Cross-check (upper bound if all 150k weekly points were allocated pro rata to one-sided OI of $1,041M): A-3x ≈1.56 pts/week, B ≈0.52 pts/week.
- The formula is unpublished and the team can change totals at its discretion. FDV and dilution are unknown, and the program may end within 5–13 weeks. The points upside should therefore be treated as a lottery-like, speculative extra, not as income that offsets funding or liquidation risk. It also rewards size (notional), which is precisely what increases liquidation risk in interpretation A.
- A $4,000 account will stay at Iron tier (0% boost) and cannot earn referral codes ($1M volume threshold).

### Gaps
- No official statement of how weekly points are weighted (volume vs OI vs PnL vs spread paid). The OI-weighted figures come from an unverified third-party snippet.
- The exact TGE date, total points at TGE, and eligibility filters (sybil or minimum points beyond "at least 1 point") are not official.

---

## 4. Perp DCA mechanics with worked numbers ($4,000 USDC; ~30% = $1,200 per tranche; HYPE $80/$70/$60 and SOL $120/$105/$90; 2x and 3x; cross vs isolated; A vs B)

### Takeaway
The key beginner distinction is **margin versus notional**. If "$1,200 per tranche" means margin at 3x (A), the plan holds $10,800 of exposure (2.7x the $4,000 capital). It then gets liquidated after roughly a further 13% drop below the last entry (cross), or 8% (isolated). Its third tranche may not even be fillable, because unrealized losses eat the margin available for new orders. If "$1,200" means notional (B), exposure equals spot ($3,600). **In cross margin with all $4,000 deposited, B has no liquidation price at all**, because collateral exceeds notional. B then behaves like spot plus a funding cost and platform risk. B in isolated mode with only $400–$600 margin per tranche is liquidated 20% (3x) or 33% (2x) below the average entry. Omni's MM is half of the chosen IM (MM = 1/(2 × leverage)), so liquidation distances are noticeably shorter than on HL at the same leverage. Also on Omni, picking a lower leverage setting in cross mode can move the liquidation price closer.

### Cited Findings (parameters used)
- IM = 1/leverage and MM ≈ IM/2. At 3x: IM 33.3%, MM 16.67%. At 2x: IM 50%, MM 25%. — [Leverage](https://docs.variational.io/omni/trading/leverage); [Margin](https://docs.variational.io/omni/trading/margin)
- Liquidation happens at MM usage ≥ 100% on an EMA of the mark price. It is partial, executed at bid − 0.5% for longs. — [Liquidation](https://docs.variational.io/omni/trading/liquidation)
- Cross mode uses the whole USDC balance; isolated mode uses only the margin assigned to that position. — [Margin](https://docs.variational.io/omni/trading/margin)
- "Available to Trade: The current funds available for a trade given your Initial Margin usage"; the "Size" field is after-leverage notional. — [Getting Started with Omni](https://docs.variational.io/omni/getting-started-with-omni)
- HL comparison parameters:
  - MM is "half of the initial margin at max leverage". HYPE max 10x gives MM 5%; SOL max 20x gives MM 2.5% (max leverage from the HL API, 2026-09-30).
  - "The actual liquidation price is independent on the leverage set for cross margin positions."
  - Formula: `liq_price = price − side × margin_available / position_size / (1 − l × side)`.
  - — [HL Liquidations](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/liquidations); [HL Margining](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/margining); [HL API](https://api.hyperliquid.xyz/info)
- Price context (Omni marks, 2026-09-30 ~10:16 UTC): HYPE $86.28, SOL $119.21. The HYPE ladder ($80/$70/$60) sits −7%/−19%/−30% below spot. The SOL ladder ($120/$105/$90) sits about 0%/−12%/−25% below spot. Both ladders use the same proportions (first entry, −12.5%, −25%). — [Omni stats API](https://omni-client-api.prod.ap-northeast-1.variational.io/metadata/stats)

### Inferences (all computations by the researcher from the parameters above; funding, spread and EMA lag ignored unless stated)

#### 4a. Margin vs notional in plain terms
- **Notional** (position size) = quantity × price. PnL is computed on this. A $3,600 HYPE long gains or loses $36 for every 1% move.
- **Margin** (collateral) = USDC locked to back the position. Initial margin = notional ÷ leverage.
- **Leverage** = notional ÷ margin. **Effective account leverage** = total notional ÷ total account equity; this is what drives risk in cross mode.
- On Omni you type the **notional** into "Size". Typing $1,200 at 3x opens $1,200 of exposure using $400 margin (interpretation B). Typing $3,600 at 3x opens $3,600 using $1,200 margin (interpretation A).

#### 4b. Formulas
- Average entry after equal-dollar tranches = total notional ÷ total quantity. This is the harmonic mean of the entry prices. For HYPE: 3 ÷ (1/80 + 1/70 + 1/60) = **$69.04**; after two tranches, **$74.67**. For SOL: **$103.56** and **$112.00**.
- Equity(P) = C + Q·(P − E), where C = collateral (the whole deposit in cross, or the isolated margin), Q = total quantity, E = average entry.
- Liquidation when Equity(P) ≤ m·Q·P, with m = MM rate = 1/(2L). This gives **P_liq = (Q·E − C) / (Q·(1 − m))**. If the result is ≤ 0, there is no liquidation price. This is algebraically the same as HL's documented formula.
- Single-entry isolated long: the liquidation drop is d = (IM − MM)/(1 − MM) = **1/(2L − 1)** on Omni: 2x → 33.3%, 3x → 20.0%, 5x → 11.1%, 10x → 5.3%. On HL at 3x: HYPE 29.8%, SOL 31.6%. At 2x: HYPE 47.4%, SOL 48.7%.
- Cross order check (standard definition, assumed): Available = Equity − Σ(notional at mark ÷ L). A new tranche needs notional_new ÷ L.
- Partial-liquidation path (continuous approximation, no penalty): once liquidation starts, equity is held at m·Q·P, so **Equity ∝ P^(1/m)**, i.e. ∝ P⁶ at 3x and ∝ P⁴ at 2x. The simulation below also deducts the 0.5% penalty on every liquidated slice (0.05% price steps, fills at mark).

#### 4c. Position build-up

| Plan | Notional per tranche | Margin per tranche | Total notional | HYPE qty (T1 / T2 / T3 = total) | SOL qty total | Notional ÷ $4,000 |
|---|---|---|---|---|---|---|
| A-3x | $3,600 | $1,200 | $10,800 | 45 / 51.43 / 60 = 156.43 | 104.29 | 2.7x |
| A-2x | $2,400 | $1,200 | $7,200 | 30 / 34.29 / 40 = 104.29 | 69.52 | 1.8x |
| B-3x | $1,200 | $400 | $3,600 | 15 / 17.14 / 20 = 52.14 | 34.76 | 0.9x |
| B-2x | $1,200 | $600 | $3,600 | 15 / 17.14 / 20 = 52.14 | 34.76 | 0.9x |
| Spot | $1,200 cash each | — | $3,600 | 52.14 | 34.76 | 0.9x |

Average entry is the same for every plan: HYPE $80.00 → $74.67 → $69.04; SOL $120.00 → $112.00 → $103.56. The remaining $400 is a cash buffer.

#### 4d. Liquidation price after each tranche (HYPE; SOL = HYPE × 1.5, identical in % terms)

| Plan / margin mode | After T1 (@$80) | After T2 (@$70) | After T3 (@$60) | T3 liq vs $60 entry / vs avg |
|---|---|---|---|---|
| A-3x **cross** (C=$4,000, m=16.67%) | none (C > notional) | **$39.82** | **$52.16** | −13.1% / −24.4% |
| A-3x **isolated** (C=$1,200 → $2,400 → $3,600) | **$64.00** | **$59.73** | **$55.23** | −7.9% / −20.0% |
| A-2x **cross** (m=25%) | none | **$16.59** | **$40.91** | −31.8% / −40.7% |
| A-2x **isolated** (C=$1,200 → $2,400 → $3,600) | **$53.33** | **$49.78** | **$46.03** | −23.3% / −33.3% |
| B-3x / B-2x **cross** | none | none | **none** | — |
| B-3x **isolated** (C=$400 → $800 → $1,200) | **$64.00** | **$59.73** | **$55.23** | −7.9% / −20.0% |
| B-2x **isolated** (C=$600 → $1,200 → $1,800) | **$53.33** | **$49.78** | **$46.03** | −23.3% / −33.3% |

SOL liquidation prices for the same cells:
- A-3x cross: none / $59.73 / $78.25
- A-3x or B-3x isolated: $96.00 / $89.60 / $82.85
- A-2x cross: none / $24.89 / $61.37
- A-2x or B-2x isolated: $80.00 / $74.67 / $69.04
- B cross: none

Worked example (A-3x cross after T3): P_liq = (156.43 × 69.04 − 4,000) / (156.43 × (1 − 1/6)) = (10,800 − 4,000) / 130.36 = **$52.16**.

Execution caveats:
- **Interpretation A cannot fully fill T3 in cross mode.** Under the standard Available = Equity − IM rule:
  - A-3x at $60: equity is $2,585.71 and IM on the existing position is $1,928.57, so only **$657.14** is free against $1,200 needed. T3 is capped at about $1,971 notional, giving a total of $9,171, an average of $70.94 and a liquidation price of **$48.00**.
  - A-2x at $60: $1,128.57 free against $1,200 needed. T3 is capped at $2,257, giving a total of $7,057 and a liquidation price of **$40.00**.
- **Isolated 3x is a near-miss.** The T1+T2 liquidation price ($59.73) is only 0.45% below the $60 T3 limit. A fast wick could liquidate before T3 fills (checks run every 0.1 s). A T1-only isolated 3x position ($64.00) would be liquidated before a $60 add if T2 had not filled.

#### 4e. If price then falls a further 30% / 40% / 50% below the last entry (HYPE $42 / $36 / $30; SOL $63 / $54 / $45)
Total account value out of $4,000; SOL results in $ are identical.

| Plan | −30% | −40% | −50% | Note |
|---|---|---|---|---|
| Spot (reference) | $2,590 (−35.2%) | $2,277 (−43.1%) | $1,964 (−50.9%) | keeps the full 52.14 HYPE |
| **B-3x / B-2x cross** | $2,590 (−35.2%) | $2,277 (−43.1%) | $1,964 (−50.9%) | never liquidated (MM usage 13–21%); same as spot before funding |
| B-3x isolated | $2,889 (−27.8%) | $2,834 (−29.1%) | $2,811 (−29.7%) | loss capped near the isolated margin, but 76–96% of the position is force-sold |
| B-2x isolated | $2,614 (−34.7%) | $2,421 (−39.5%) | $2,305 (−42.4%) | 25–73% of the position force-sold |
| A-2x cross | $1,180 (−70.5%) | $634 (−84.1%) | $302 (−92.4%) | at $42 not yet liquidated (MM usage 93%) |
| A-2x isolated | $1,227 (−69.3%) | $842 (−78.9%) | $611 (−84.7%) | |
| A-3x isolated | $666 (−83.3%) | $503 (−87.4%) | $433 (−89.2%) | |
| **A-3x cross** (if T3 fully filled) | **$358 (−91.1%)** | $138 (−96.5%) | $45 (−98.9%) | liquidations start at $52.16; 33% / 15% / 6% of the position left |

#### 4f. V-shaped recovery
Price bottoms at −30% ($42 HYPE / $63 SOL) and then returns to the first entry ($80 / $120). No funding.

| Plan | Account value | Result |
|---|---|---|
| Spot / B cross | $4,571 | +14.3% |
| A-2x cross (survived; liq $40.91 < $42) | $5,143 | +28.6% |
| A-2x isolated | $4,220 | +5.5% |
| B-2x isolated | $4,110 | +2.8% |
| B-3x isolated | $3,371 | −15.7% |
| A-3x cross | $2,299 | −42.5% |
| A-3x isolated | $2,112 | −47.2% |

If the bottom is −50% ($30) before the rebound to $80:

| Plan | Result |
|---|---|
| Spot / B cross | +14.3% |
| B-2x isolated | −24.8% |
| B-3x isolated | −26.9% |
| A-2x cross | −42.1% |
| A-3x cross | −87.6% |

Liquidation sells at the lows, so the "lower average entry" thesis of DCA breaks when leverage is too high.

#### 4g. Upside with no deep drawdown
After all three fills, price returns to $80, or rises to $100 (HYPE; SOL $120 / $150). No funding.

| Plan | Price back to $80 | Price at $100 |
|---|---|---|
| A-3x | +$1,714 (+42.9%) | +$4,843 (+121.1%) |
| A-2x | +$1,143 (+28.6%) | +$3,229 (+80.7%) |
| B / spot | +$571 (+14.3%) | +$1,614 (+40.4%) |

Interpretation A roughly triples (3x) or doubles (2x) both gains and losses relative to spot.

#### 4h. Omni vs HL liquidation after T3 (same plans)

| Plan | HYPE: Omni | HYPE: HL | SOL: Omni | SOL: HL |
|---|---|---|---|---|
| A-3x cross | $52.16 | $45.76 | $78.25 | $66.88 |
| A-3x isolated | $55.23 | $48.45 | $82.85 | $70.81 |
| A-2x cross | $40.91 | $32.30 | $61.37 | $47.21 |
| A-2x isolated | $46.03 | $36.34 | $69.04 | $53.11 |
| B cross | none | none | none | none |

HL uses the base margin tier (HL has larger-position tiers, marginTableId 52/54, not modeled).

#### 4i. Omni-specific quirk: the leverage setting changes MM in cross mode
Same $10,800 HYPE position, $4,000 collateral, cross mode:

| Leverage setting | MM rate | Liquidation price | IM needed to open |
|---|---|---|---|
| 1x | 50% | $86.94 (impossible to hold) | $10,800 |
| 2x | 25% | $57.96 | $5,400 |
| 3x | 16.67% | $52.16 | $3,600 |
| 5x | 10% | $48.30 | $2,160 |
| 10x | 5% | $45.76 | $1,080 |

On HL, the cross liquidation price does not depend on the leverage setting (per HL docs). On Omni, for a fixed notional, a *higher* setting lowers MM and pushes liquidation further away, but frees margin to add more size. The docs' "generally" wording means the in-app estimated liquidation price should be the final check.

#### 4j. Funding erodes cross collateral
- A-3x cross (HYPE, 10.95%/yr on $10,800): collateral goes from $4,000 to $3,409 after 6 months, moving liquidation from $52.16 to **$56.70**. After 1 year, collateral is $2,817 and liquidation is **$61.24**, above the $60 last entry.
- B-3x cross: after 2 years at 10.95%, collateral is $3,212 and a liquidation price appears at $8.94.

### Gaps
- Omni's exact "available margin" formula (mark vs entry notional; whether unrealized losses count) and whether resting limit orders reserve margin are not documented. The T3-cap numbers assume the standard definition.
- The docs say MM is "generally" half of IM. Per-asset exceptions, and whether isolated and cross use identical MM, are not confirmed; verify with the app's estimated liquidation price.
- The partial-liquidation simulation assumes fills at mark minus 0.5% with no extra spread or EMA lag. Real outcomes in fast markets may be worse.

---

## 5. Practical how-to on Omni for a laddered long (order types, reduce-only, TP/SL, monitoring, adding margin, partial close) and common beginner mistakes

### Takeaway
A laddered perp DCA on Omni takes three steps:
1. Deposit USDC on Arbitrum (gasless; $0.1 fee) and pick cross or isolated.
2. Place a market or limit order for tranche 1, then resting **limit buys** at the lower levels. Limit orders fill only when OLP's quote crosses, are all-or-nothing, and expire after 120 days.
3. Watch **MM Usage** (liquidation at 100%) and the estimated liquidation price. Add USDC (cross) or add isolated margin to push liquidation away, and use **Reduce Only**, partial **Close**, and TP/SL to exit.

The most common mistakes are mixing up margin and notional, assuming isolated or lower leverage is automatically "safer", setting stop-loss slippage too tight, and ignoring the 120-day order expiry and funding drag.

### Cited Findings
- Onboarding steps: connect wallet → enter access code → accept Terms → create portfolio → sign login (no gas). Deposit USDC on Arbitrum ($0.1 fee deducted); bridge first if the funds are on another chain. Withdrawals go only to the connected wallet. — [Getting Started with Omni](https://docs.variational.io/omni/getting-started-with-omni)
- Order form: Leverage (1–50x), Margin Mode (cross/isolated), Order Type (Market / Limit / Pro), Size (after leverage), Reduce Only, TP/SL. The trade-information panel shows the estimated liquidation price, order value, margin reduction, quoted price and estimated slippage. — [Getting Started with Omni](https://docs.variational.io/omni/getting-started-with-omni)
- Limit orders: executed "once OLP's quoted price crosses the set limit price"; "all-or-nothing"; checked every 0.1 s ("If the quoted price crosses the limit price for less than 0.1 seconds, it is possible for the order to not trigger"); expire after 120 days. — [Market, Limit, and Trigger Orders](https://docs.variational.io/omni/trading/market-limit-and-trigger-orders)
- TP/SL: trigger on mark (default) or quote. The slippage limit must also be satisfied or the order "will remain pending". A liquidation can fire before a TP/SL if both prices are crossed within 0.1 s. Auto-resize is recommended. Orders expire after 120 days. — [Take Profit and Stop Loss](https://docs.variational.io/omni/trading/take-profit-and-stop-loss)
- Monitoring and management:
  - The positions table shows the estimated liquidation price, position margin and cumulative funding, and allows partial or full Close, Reverse, and Add TP/SL.
  - The portfolio panel shows MM Usage (Maintenance Margin / Account Balance), Margin Ratio and Portfolio Leverage.
  - In isolated mode you "deliberately add or remove USDC collateral".
  - — [Getting Started with Omni](https://docs.variational.io/omni/getting-started-with-omni); [Margin](https://docs.variational.io/omni/trading/margin)
- The roadmap marks "Display estimated liquidation prices" (Q3 2025) and "Configurable leverage" as done. "Partial fills of limit orders" and "API trading" are not yet available. — [Roadmap](https://docs.variational.io/getting-started/roadmap)
- The trading API "is still in development, and is not yet available to any users". Only the read-only stats endpoint exists, so a DCA cannot be automated via API. — [API docs](https://docs.variational.io/technical-documentation/api)

### Inferences
- **Suggested mechanics for each interpretation** (descriptive, not a recommendation):
  - *B (spot-like):* choose cross, deposit the full $4,000, and set Size = $1,200 per tranche. Use a limit buy at each level, with Reduce Only on any sell. As computed in Q4, no liquidation price exists while notional ($3,600) is below collateral.
  - *A (leveraged):* it is essential to pre-check "Available to Trade" at the lower levels, because T3 may be rejected or need a smaller size.
- **Monitoring routine:** read MM Usage (100% triggers liquidation). Re-read the estimated liquidation price after every fill, after every funding interval (8h for SOL/HYPE), and after any other position change in cross mode. **Adding margin** means depositing more USDC (cross) or moving USDC into the isolated position. As Q4 shows, adding all remaining cash to an isolated position makes it equivalent to cross.
- **Partial close:** use Close with a partial size, or a sell with Reduce Only, so a size mismatch cannot flip the position short.
- **Common beginner mistakes** (drawn from the documented mechanics and the Q4 numbers):
  1. Entering margin as "Size": Size is notional.
  2. Believing isolated mode is always safer. It caps the loss but moves liquidation much closer: B-3x isolated liquidates at $55.23, while B cross never liquidates.
  3. Assuming a lower leverage setting is safer in Omni cross. It raises MM (see the Q4 quirk table).
  4. Setting a tight stop-loss slippage limit: in a crash the SL may stay "pending" while liquidation fires.
  5. Forgetting 120-day expiry on ladder, TP and SL orders.
  6. Ignoring funding: about 10.95%/yr of notional at neutral rates, which slowly raises the liquidation price.
  7. Relying on a wick hitting the level: a limit fills only if OLP's quote crosses, for more than 0.1 s.
  8. Adding leverage to farm points: points scale with size, and so does liquidation risk.
  9. Treating a "loss refund" as insurance: the pool read $0 on 30 Sep 2026.
  10. Not keeping a USDC buffer or a plan for adding margin.

### Gaps
- Screens for adding or removing isolated margin and for the in-app liquidation-price display were not verified hands-on; access requires a private-beta code.
- Whether resting limit orders count against available margin (which affects ladders) is undocumented.

---

## 6. Risks: wicks, mark/oracle mechanics, OLP/counterparty solvency, contract and bridge risk, funding spikes, venue-specific (new, pre-TGE) risk, behavioral risk

### Takeaway
The main risks are:
- **Liquidation risk**: higher on Omni than HL at the same leverage, because MM = IM/2.
- **Single-counterparty risk**: OLP is team-seeded and opaque; there is no insurance backstop, and OLP insolvency turns user PnL into bad debt.
- **Discretionary and centralized controls**: admins can disable trading, override funding, halt or change incentives, and apply risk limits that can reject orders.
- **Funding drag and spikes**: cap of 2% per hour.
- **Venue maturity**: private beta, pre-TGE, incentive-driven activity that may fade after TGE.
- **Behavioral risk**: leverage turns a "buy-the-dip" plan into forced selling at the bottom.
- **Smart-contract, Arbitrum and bridge risk**: audited (two audits, bug bounty), but not zero.

### Cited Findings
- Wicks and mark price: liquidation uses "a very fast EMA of the mark price" to dampen "sudden wicks". The mark includes "OLP's current risk profile". Liquidation executes at bid − 0.5%. — [Liquidation](https://docs.variational.io/omni/trading/liquidation); [Quoted, Index, and Mark Prices](https://docs.variational.io/omni/trading/quoted-index-and-mark-prices)
- Stops can lag liquidation: "If the mark price also crosses a liquidation price within 0.1 seconds of crossing the trigger price, it is possible for a liquidation to trigger before a TP/SL." — [Take Profit and Stop Loss](https://docs.variational.io/omni/trading/take-profit-and-stop-loss)
- Counterparty and solvency:
  - "If OLP were insolvent, any unrealized or realized PnL accrued going forward would be considered 'bad debt'." OLP moves its own capital to outside venues for hedging, so "If an exchange were to suffer a hack or incident that loses funds, OLP depositors may face a loss of capital". — [OLP docs](https://docs.variational.io/omni/the-omni-liquidity-provider-olp)
  - The P2P model has "no such backstop". — [P2P Trading Protocol vs DEX](https://docs.variational.io/variational-protocol/key-concepts/p2p-trading-protocol-vs-dex)
  - ADL: OLP can be "liquidated", closing user positions in extreme volatility. — [ADL](https://docs.variational.io/omni/trading/automatic-deleveraging-counterparty-liquidation)
- Discretionary controls:
  - "Trading is currently disabled by admins" (GlobalConfigsCheck) is a documented state.
  - OLP-capacity and skew/OI-vs-FDV limits can reject trades.
  - — [Risk Limits](https://docs.variational.io/omni/trading/risk-limits-rate-limits)
  - Funding can be manually overridden in "special circumstances" and is capped at 2%/hour. — [Funding Rates](https://docs.variational.io/omni/trading/funding-rates)
  - Incentives (points, loss refunds) can be changed or discontinued "at any time without any notice". — [Terms of Use](https://docs.variational.io/legal/terms-of-use); [Points](https://docs.variational.io/omni/rewards/points)
- Funding spikes (HL proxy): the highest hourly HYPE funding in 2025–26 was +0.0886%/h (19 Jan 2025, ≈776% annualized for that hour). The 10 Oct 2025 crash produced −0.2051%/h on SOL and −0.1866%/h on HYPE (shorts paying longs). — [HL API fundingHistory](https://api.hyperliquid.xyz/info)
- Venue maturity: Omni is in "private beta" with public mainnet not yet launched, and the OLP community vault is not open (2026-09-30). — [Getting Started](https://docs.variational.io/omni/getting-started-with-omni); [Roadmap](https://docs.variational.io/getting-started/roadmap)
- Research views on venue risk:
  - Alea Research (6 Jan 2026) highlights "incentive-driven capital rotation", uncertain retention after incentives, and OLP counterparty concentration. — [Alea Research](https://alearesearch.substack.com/p/variational)
  - Datawallet (28 Sep 2026) lists vault opacity, last-look rejection in volatility, smart-contract risk, beta-stage discretionary rule changes, and unknown post-TGE float behavior. — [Datawallet](https://www.datawallet.com/crypto/variational-explained)
- Smart-contract and chain: Omni is deployed on Arbitrum and USDC must be on Arbitrum ("bridge them to Arbitrum" if elsewhere). Audits by Zellic (Dec 2024) and Spearbit (Mar 2025); Immunefi bug bounty. — [Getting Started](https://docs.variational.io/omni/getting-started-with-omni); [Audits](https://docs.variational.io/technical-documentation/audits); [Bug Bounties](https://docs.variational.io/technical-documentation/bug-bounties)
- Comparative context: HL's mark price is a documented median of oracle+EMA, HL book, and weighted CEX perp mids. HL backstop liquidation keeps the maintenance margin ("the maintenance margin is not returned to the user"). — [HL Robust price indices](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/robust-price-indices); [HL Liquidations](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/liquidations)

### Inferences
- **Liquidation-on-wick risk depends mainly on effective leverage and margin mode, not on the "3x" label.** Interpretation B in cross mode with the full $4,000 deposited has no liquidation price. Interpretation A at 3x is liquidated about 13% below the last rung (cross) or 8% below it (isolated). SOL and HYPE have historically moved 25–50% within weeks: the HL funding data show both the 10 Oct 2025 crash and multi-month regime shifts. Leveraged ladders are therefore exposed to exactly the moves a DCA plan is built to buy.
- **Counterparty concentration.** User funds sit in the user's own pool and are never sent to CEXs, but profits and exits depend on OLP's margin, its hedging on third-party venues, and admin controls. In a stress event, OLP last-look rejections, risk-limit rejections or ADL could stop a user adding, closing or keeping a position exactly when needed.
- **Venue-specific, pre-TGE risk.** Activity is likely boosted by the points program (a 150k points per week race, weeks from TGE). After TGE, liquidity, spreads and OLP capacity could change. The rules (points, refunds, fees) are discretionary.
- **Funding risk.** The neutral-market cost of about 10.95%/yr on notional is structural. HYPE longs paid about 22% in 2025 on HL. Spikes are allowed up to 2%/hour on Omni, which would be catastrophic for leveraged longs if sustained, though such levels were not observed on HL in 2025–26.
- **Behavioral risk.** Leverage reverses the DCA logic. Instead of accumulating more coins as price falls, partial liquidations sell coins as price falls; the recovery example ends at −42.5% for A-3x cross vs +14.3% for spot. Points incentives push toward more notional. Beginners also tend to add margin or leverage to "defend" a position.
- **Bridge and chain risk** applies whenever USDC is moved to Arbitrum from another chain. The size of that risk depends on the bridge used; it was not assessed here.

### Gaps
- No incident history, uptime record or OLP drawdown data was found for Omni. Behavior during the 10–11 Oct 2025 crash on Variational specifically was not found.
- No independent assessment of the Variational Oracle's sources, weights or manipulation resistance.
- No data on how often ADL (counterparty liquidation) has occurred on Omni.
