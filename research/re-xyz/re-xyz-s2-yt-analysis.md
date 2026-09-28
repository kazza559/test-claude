# Re Protocol (re.xyz) — Định giá $RE, Point Season 2 & có nên mua YT Pendle không?

> Snapshot dữ liệu: **28/09/2026** (Re public API, Pendle API/SDK, CoinGecko, DefiLlama, docs.re.xyz, blog.re.xyz).
> Script tính toán: [`yt_model.py`](./yt_model.py) · Data thô: [`data/`](./data)
> Không phải lời khuyên đầu tư. Các giả định được cố ý đặt lệch **bearish**.

---

## 0. TL;DR

| Câu hỏi | Kết luận |
|---|---|
| Re đã TGE chưa? | **Đã TGE ngày 18/06/2026.** $RE đang giao dịch ~**$0.46 → FDV ~$460M**, MC ~$75–83M, ATH $1.08 (20/06), ATL $0.357 (20/07). Nên "FDV dự kiến" cần hiểu là **FDV tại thời điểm claim S2** (dự kiến cuối 12/2026 – Q1/2027). |
| FDV dự kiến lúc claim S2 | **Bear $150–250M · Base $280–380M (~$0.33) · Bull $500–650M.** Có xu hướng giảm vì áp lực unlock (monthly 7.09M, tranche S1 18/12, claim S2, cliff team+investor 37% vào 18/06/2027). |
| S2 | 01/06/2026 → ~01–10/12/2026, **tối thiểu 3.5% supply (35M RE)**. Hiện **686.85B point** (27/09), đang in **9.62B point/ngày**. Dự phóng tổng S2: **1.30T (bull) / 1.55T (base) / 2.0T (bear) / 2.5T (super-bear)**. |
| Giá trị point S2 | **~$7.9k / 1B point (base)**; bear $3.85k; super-bear $2.1k; bull $19k. (S1 = $44k/1B ở giá hiện tại → S2 loãng hơn ~5–6 lần.) |
| Cost YT hiện tại | YT-reUSD $0.0215 (gross) nhưng **yield trả về ~$0.0127/YT** → **net cost ≈ $0.0093/YT ≈ $3.9k/1B point**. Thị trường đang ngầm định RE FDV ~**$175M** (hòa vốn cho ví nhỏ). |
| Có nên mua YT? | **Ví nhỏ (≤ ~$1.3k YT-reUSD/ví, dưới ngưỡng 150M point): CÓ, size nhỏ** — EV base +43%, bear −15%, super-bear −30%. **Ví ≥$10k: KHÔNG hấp dẫn** — dính vesting 3 năm + slippage → base chỉ +9%, bear −32%; ≥$50k EV âm. Ưu tiên **YT-reUSD** hơn YT-reUSDe (junior tranche + thanh khoản mỏng). Nếu bearish mạnh → **PT-reUSD fixed 11.6%** là lựa chọn "an toàn". |

---

## 1. Dự án là gì

**Re** đưa thị trường tái bảo hiểm (reinsurance, ~$800B+) on-chain. Người dùng nạp stablecoin → vốn đi qua **Principal-at-Risk Notes** của **Cover Re SPC Ltd.** (reinsurer được cấp phép tại Cayman, CIMA) → làm collateral cho các hợp đồng tái bảo hiểm (quota-share) với 40+ công ty bảo hiểm Mỹ.

| Token | Vị trí | Yield | Thanh khoản | Hiện tại |
|---|---|---|---|---|
| **reUSD** | Senior | Bình quân gia quyền SOFR & sUSDe 7d **+250 bps** | Rút tức thì (buffer, cap 20%/ngày), từ 09/2026 chỉ rút ra USDC | APY 7d **6.75%**, NAV 1.1036, TVL **$295.8M** |
| **reUSDe** | Mezzanine (chịu lỗ sau equity $77M của reinsurer) | Risk-free **+850 bps** | Rút theo quý | APY 7d **11.94%**, NAV 1.4235, TVL **$20.5M** |
| **$RE** | Governance | **Không** có quyền với doanh thu/phí | CEX lớn | $0.46, FDV $460M |

Số liệu vận hành (Re API 28/09/2026):
- "TVL" marketing **$709.8M** = on-chain $208.3M + off-chain $182.6M + **premium receivables $318.9M** (khoản phí bảo hiểm phải thu — *không phải tiền user*). **Tiền user thực = reUSD + reUSDe ≈ $316M.**
- Danh mục bảo hiểm $510–512M: Small Business Commercial 44%, Commercial Auto 26%, Homeowners 17% (có rủi ro catastrophe), Workers' Comp 12%, Personal Auto 1%.
- Premium đã viết ~$500M; mục tiêu run-rate ~$1B/năm đầu 2027; tổng yield đã trả cho holder ~$10M.
- reUSD tăng **+24% MoM** (DefiLlama: $224.6M → $279.5M) trong khi mảng yield-bearing stablecoin co lại.
- Backers: Electric Capital, Framework, Tribe, Morgan Creek, Stratos, Exor Seeds (seed $14M + $7M), **Coinbase Ventures** (strategic). Binance Prime Sale 1% supply @ **FDV $50M**.
- Listing: Binance (Seed Tag), Coinbase, OKX, Bybit, KuCoin, Kraken, Robinhood, Upbit, Bithumb… (16 spot + 11 perp venue tuần đầu).

---

## 2. Tokenomics & lịch unlock $RE (quan trọng cho định giá)

| Nhóm | % | Vesting |
|---|---|---|
| Ecosystem | 50% | 159.6M liquid tại TGE, phần còn lại linear 48 tháng (**~7.09M RE/tháng**, đã xác nhận đợt 17/08) |
| Core Contributors | 20% | Cliff 12 tháng, linear 36 tháng |
| Investors | 17% | Cliff 12 tháng, linear 36 tháng |
| Ecosystem Dev Reserve | 13% | Dài hạn |

Airdrop S1 = 7% (70M RE). Ví ≤150M point nhận 100% ngay; ví >150M nhận `(135M + 10%·tổng point) × rate` ngay, phần còn lại chia 6 tranche/6 tháng trong 3 năm, **4 tranche đầu yêu cầu giữ TVL** (bằng số dư USD bình quân của ví trong season; YT/PT tính theo giá thị trường TWAP). Tính trên full leaderboard S1: **~82.5% token S1 bị vest (~57.7M RE)** → tranche 1 ngày **18/12/2026 ≈ 9.6M RE**.

Lịch áp lực cung (ước tính):

| Thời điểm | Sự kiện | RE |
|---|---|---|
| Hàng tháng | Ecosystem unlock | ~7.09M |
| 18/12/2026 | Tranche 1 S1 (có điều kiện TVL) | ≤9.6M |
| ~Cuối 12/2026 – Q1/2027 | Claim S2 (phần liquid ~20–25% của 35M nếu giữ luật S1) | ~7–10M |
| **18/06/2027** | **Cliff team + investor (370M = 37% supply)** bắt đầu vest ~10.3M/tháng | lớn |

Circulating ước tính ~175–181M hiện tại → ~225–230M vào cuối 01/2027 (**+25%**). Giữ nguyên market cap thì giá tự giảm ~20%.

---

## 3. Bối cảnh ngành & so sánh các dự án stablecoin đã TGE

**Trend đúng là đang thoái trào:**
- 11/2025: Stream Finance mất $93M → xUSD, Elixir deUSD depeg; TVL yield-stablecoin tháo chạy.
- 03/2026: **Resolv USR bị exploit** (mint 80M USR không backing), USR còn ~$0.09, protocol mất khả năng thanh toán.
- Q2/2026: supply yield-bearing stablecoin **−15% (−$3.5B)**, sUSDe **−52%**; dòng tiền chuyển sang T-bill token (USDY +66%, USYC +16%). USDe từ đỉnh $14.8B (10/2025) còn $4.94B.
- 09/2026: **Apyx hoãn TGE** (vốn dự kiến 13/10) và tăng airdrop S2 từ 6% → 9% — ví dụ điển hình của "season bị kéo dài + tăng allocation".
- Tín hiệu hồi nhẹ tháng 9: ENA +66%/30d, FF +40%/30d.

**Bảng so sánh** (FDV theo total supply; TVL = supply stablecoin theo DefiLlama):

| Dự án | Stable | TGE | FDV mở cửa / TB tuần 1 | Supply lúc TGE | FDV/TVL tuần 1 | FDV hiện tại | Supply hiện tại | FDV/TVL nay | Nay vs tuần 1 |
|---|---|---|---|---|---|---|---|---|---|
| Ethena (ENA) | USDe | 04/2024 | $11.7B / $16.0B | $1.98B | 8.1x | $3.95B | $4.94B | 0.80x | −75% |
| Usual (USUAL) | USD0 | 12/2024 | $4.0B / $4.9B | $1.03B | 4.8x | ~$0.03–0.06B | $0.55B | ~0.1x | −99% |
| Resolv (RESOLV) | USR | 06/2025 | $350M / $286M | $216M | 1.3x | $19M | ~0 (hack) | n/a | −93% |
| OpenEden (EDEN) | USDO | 09/2025 | $402M / $372M | $244M | 1.5x | $59M | $14.5M (chưa tính vault TBILL) | 4.1x | −84% |
| Falcon (FF) | USDf | 09/2025 | $2.84B / $2.03B | $1.90B | 1.07x | $1.30B | $1.21B | 1.07x | −36% |
| Unitas (UP) | USDu | 03/2026 | $71M / $100M | $83M | 1.2x | $267M | $46M | 5.8x | +167% |
| Mezo (MEZO) | MUSD | 04/2026 | $68M / $50M | $19M | 2.6x | $4M | $30M | 0.14x | −92% |
| USD.AI (CHIP) | USDai | 04/2026 (ICO $300M) | $608M / $834M | $281M | 3.0x | $443M | $218M | 2.0x | −47% |
| Cap (CAP) | cUSD | 06/2026 (auction $106M) | $294M / $262M | $65M | 4.0x | $554M | $87M | 6.4x | +111% |
| **Re (RE)** | reUSD+reUSDe | **18/06/2026** (Prime $50M) | **$431M / $795M** | **~$176M** | **4.5x** | **$460M** | **~$316M** | **1.45x** | **−42%** |
| *Tham chiếu:* Maple (SYRUP) | syrupUSDC | 11/2024 | $268M / $261M | – | – | $262M | ~$1.0B | ~0.26x | ~0% (có buyback) |
| *Tham chiếu:* Plasma (XPL) | chain | 09/2025 | $12.8B / $12.5B | – | – | $1.0B | – | – | −92% |

**Rút ra:**
1. Cohort 2024–2025 mất 36–99% FDV trong 12 tháng; chỉ những token có TVL giữ được (Falcon) hoặc có doanh thu/buyback (Syrup) là giữ giá.
2. Cohort 2026: token nào ra mắt FDV thấp (CAP auction $106M, UP $71M) thì tăng; token ra mắt FDV cao (CHIP, **RE**) giảm ~45% sau 3–5 tháng — RE đang đi đúng pattern này.
3. **Pattern "TVL sập sau TGE"**: USDai $663M → $218M, cUSD $443M → $87M. Re là ngoại lệ (TVL tăng sau TGE) — nhưng **do S2 + Pendle**: ~**72% reUSD nằm trong Pendle** (YT/PT 213M), **$127M PT được loop trên Morpho** → TVL mang tính "mercenary", rủi ro rút mạnh khi S2 kết thúc nếu không có S3.
4. RE FDV/TVL 1.45x — **cao hơn ENA (0.8x), FF (1.07x)**, trong khi token **không có value accrual** (DefiLlama: Re fee ~$19M/năm trả cho holder, protocol revenue ≈ $0.1M/năm). ENA ~16x fees, Sky ~5.7x, Syrup ~2.4x; **RE ~24x fees**.

---

## 4. Đánh giá tiềm năng dự án

**Điểm mạnh**
- Nguồn yield thật, không tương quan crypto (premium bảo hiểm), cấu trúc pháp lý rõ ràng (CIMA-approved note program $100M, Reg 114 trust, audited financials, Chainlink PoR, Sherlock audit oracle).
- Tăng trưởng deposit ngược trend ngành; mở rộng 13 chain (Solana: Kamino cap $1M lấp đầy trong 76 phút → $20M sau 8 ngày).
- Backers/listing hạng A; narrative RWA/insurance còn "xanh" so với delta-neutral đã bão hòa.

**Điểm yếu / rủi ro**
- $RE **chỉ governance**, docs ghi rõ không có quyền với revenue → định giá thuần narrative + tăng trưởng.
- TVL phụ thuộc incentive (72% qua Pendle), whale cực tập trung: **top 10 ví = 65–68% point** (S1 & S2), ví #1 `0x614d…2ade` chiếm 23% S1 và 28% S2.
- Thanh khoản $RE sụt: volume ~$300–460M/ngày tuần đầu → **$5–7M/ngày** hiện tại.
- Rủi ro bảo hiểm off-chain (tin vào Cover Re; Homeowners 17% có rủi ro bão), rủi ro lãi suất (SOFR giảm → yield reUSD giảm → hút TVL kém).
- Overhang unlock nặng từ 12/2026 và đặc biệt 06/2027.

**Chấm điểm tương đối** (so peer stablecoin đã TGE): Fundamental **7/10**, Tokenomics/value-accrual **3.5/10**, Momentum giá **4/10** → dự án tốt hơn trung bình ngành, nhưng **token không rẻ** ở $460M.

---

## 5. Dự phóng FDV $RE tại thời điểm claim S2 (~cuối 12/2026 – Q1/2027)

Ba cách tiếp cận:

| Phương pháp | Lập luận | FDV |
|---|---|---|
| A. FDV/TVL comps | Peer "trưởng thành" 0.1–1.1x, launch 2026 2–6x; cho Re premium 1.0–1.5x. Deposit lúc claim: bull $400M / base $300M / bear $180M (Pendle unwind sau maturity 10/12) | $160M – $600M, base ~$330M |
| B. Đường decay hậu TGE | Cohort 2026 −45% sau 3–5 tháng, cohort cũ −75…−99% sau 12 tháng; RE TB tuần 1 $795M → tháng thứ 6: −50…−65% | $280M – $400M |
| C. Supply overhang | Circulating +25% đến cuối 01/2027, market cap giữ ~$83M → giá ~$0.37; trừ thêm yếu tố ngành | $300M – $370M |

**Kịch bản dùng cho mô hình:**

| Kịch bản | Xác suất (lệch bear) | Giá RE | FDV | Điều kiện |
|---|---|---|---|---|
| Super-bear | 15% | $0.15 | $150M | Ngành xấu tiếp, TVL rút mạnh sau S2, break ATL |
| Bear | 30% | $0.22 | $220M | Unlock tháng 12 + claim S2 xả, không có S3 |
| Base | 40% | $0.35 | $350M | Trượt nhẹ theo overhang, TVL giữ ~$300M |
| Bull | 15% | $0.55 | $550M | S3 giữ TVL, deposit >$400M, altcoin hồi |

---

## 6. Chương trình point Season 2 — chi tiết

**Thông số chính thức:**
- S1: 03/08/2025 → 31/05/2026, **7%** supply, **724.99B point** tổng, 5,301 ví.
- S2: bắt đầu **01/06/2026**, "khoảng 6 tháng" (→ ~01/12; Pendle maturity & Beefy end date **10/12/2026**), **tối thiểu 3.5%** supply. (Một số site airdrop ghi "6%" — **không có trong docs chính thức**, coi là chưa xác thực.)
- Công thức: `point/ngày = số dư USD × multiplier` (tính daily snapshot). PT = **x0**.
- Referral 2 chiều: người được mời **x1.06**; người mời nhận **+6%** point chưa boost của F1 (không cộng dồn tầng).
- Luật vesting cho S2: **chưa công bố** — mô hình giả định giống S1 (ngưỡng 150M point).

**Multiplier & phân bổ point/ngày hiện tại (27/09/2026, Re API):**

| Chiến lược | Mult | Point/ngày | TVL tính point | % point/ngày |
|---|---|---|---|---|
| **Pendle YT reUSD 10DEC2026** (ETH) | **x30** | 6.94B | $231.3M notional | **72.1%** |
| **Pendle YT reUSDe 10DEC2026** | **x40** | 0.69B | $17.2M | 7.1% |
| Fluid reUSD/USDT LP collateral | x20 | 0.50B | $24.8M | 5.1% |
| Pendle LP reUSD | x30 | 0.35B | $11.5M | 3.6% |
| Fluid reUSD collateral | x10 | 0.32B | $32.2M | 3.4% |
| Pendle LP reUSDe | x40 | 0.16B | $4.0M | 1.7% |
| JupLend/Kamino/Morpho reUSD (Solana/ETH) | x10–x20 | 0.35B | ~$29M | 3.6% |
| Pendle YT/LP reUSD Monad, Exponent YT/LP (Solana) | x30 | ~0.08B | ~$2.7M | 0.8% |
| Hold reUSD (mọi chain) | x10 | ~0.04B | ~$4.4M | 0.5% |
| Khác (Curve, Beefy, StakeDAO, Feather, Euler…) | x10–x40 | ~0.20B | ~$5M | 2.1% |
| **Tổng** | | **9.62B** | | 4,549 ví active |

→ **~79% point S2 chảy vào YT.** Giá trị point S2 về bản chất được định bởi thị trường YT.

**Tập trung whale S2:** 6,312 ví; top 1 = 28.3%, top 10 = 64.9%, top 100 = 89%; **251 ví >150M point nắm 95% point**; median chỉ ~0.39M point.

**Lạm phát point:**
- S2 đến 27/09: 686.85B trong 119 ngày → TB 5.77B/ngày; hiện 9.62B/ngày (tăng gần gấp đôi TB) do deposit reUSD tăng ~$60M/tháng (Jul→Sep: $153M → $296M) và YT notional phình.

| Kịch bản | Giả định | Tổng point S2 |
|---|---|---|
| Bull | Point/ngày đi ngang 9.6B, kết thúc 01/12 | **1.30T** |
| Base | Tăng dần lên ~14B/ngày, TB ~11.8B × 73 ngày tới 10/12 | **1.55T** |
| Bear | TB ~13B/ngày, S2 kéo dài tới ~cuối 12 | **2.0T** |
| Super-bear | Kéo dài tới 01/2027 hoặc tăng multiplier | **2.5T** |

**Giá trị 1B point S2** = `allocation × giá RE / tổng point`:

| | Bull | Base | Bear | Super-bear |
|---|---|---|---|---|
| $/1B point (danh nghĩa) | $19,038 | $7,903 | $3,850 | $2,100 |

So sánh: 1B point **S1** = 96,552 RE ≈ **$44.4k** ở giá hiện tại (≈$76.8k ở giá TB tuần 1).

**Ngày claim S2 dự kiến:** S1 kết thúc 31/05 → claim 18/06 (18 ngày). S2 kết thúc 01–10/12 → **claim dự kiến ~18/12/2026 – 01/2027** (base, có thể trùng tranche 1 S1); **bear: Q1/2027** nếu kéo dài/hoãn như Apyx.

---

## 7. Phân tích YT trên Pendle (tính cả yield trả về)

### 7.1 Thông số thị trường (28/09/2026)

| | YT-reUSD 10DEC2026 | YT-reUSDe 10DEC2026 |
|---|---|---|
| Giá YT (mid) | **$0.021506** | **$0.033441** |
| Implied APY | 11.57% (tăng từ 10.4% tháng 6) | 18.72% |
| Underlying APY | 6.75–6.98% | 11.94–12.67% |
| Thanh khoản pool | $12.1M | $4.7M |
| Ngày tới maturity | 72.5 | 72.5 |
| Point/YT/ngày (thực nghiệm = daily_points ÷ YT supply) | **32.53** (nominal x30) | **43.45** (nominal x40) |
| Giá thực khi mua (Pendle SDK) | $1k: 0.02199 (+2.2%) · $10k: 0.02226 (+3.5%) · $50k: 0.02411 (+12%) · $100k: 0.02577 (+20%) | $1k: 0.03436 (+2.7%) · $10k: 0.03483 (+4.0%) · $50k: không route được |

> Re đếm YT theo notional × ~1.085 (TVL tính point 231.3M so với YT supply on-chain 213.35M) nên 1 YT-reUSD nhận ~32.5 point/ngày chứ không phải 30. Kịch bản bear dùng lại 30/40 cho an toàn.

### 7.2 Net cost: phải trừ yield trả về

YT nhận toàn bộ yield của underlying tới maturity (Pendle thu 5% phí trên yield):

- YT-reUSD: yield ≈ 6.75% × 72.5/365 × 0.95 = **$0.0127/YT** → net cost ≈ 0.02199 − 0.0127 = **$0.0093/YT** (≈ 42% giá mua). Bear (APY 6%): yield $0.0113.
- YT-reUSDe: yield ≈ 12% × 72.5/365 × 0.95 = **$0.0226/YT** → net ≈ **$0.0117/YT**. Nhưng reUSDe là tranche chịu lỗ: nếu NAV giảm, YT mất yield cho tới khi NAV vượt đỉnh cũ.

**Chi phí thực trên point:** $1k YT-reUSD → 107.3M point, net cost $421 → **~$3.9k/1B point**.
**Thị trường đang ngầm định:** với T = 1.55T, 35M RE, không vesting → hòa vốn ở **RE ≈ $0.174 (FDV ~$174M)** — đã chiết khấu ~62% so với giá RE hiện tại. Đây là "biên an toàn" chính của lệnh YT.

### 7.3 Kết quả theo size vị thế (ROI trên vốn bỏ ra; đã tính slippage, yield trả về, vesting)

**YT-reUSD**

| Vốn | Point/ngày | Tổng point (→10/12) | Yield trả về | % liquid | Bull | Base | Bear | Super-bear | EV có trọng số* |
|---|---|---|---|---|---|---|---|---|---|
| $1,000 | 1.48M (1.57M có ref) | 107M | $579 | 100% | **+162%** | **+43%** | **−15%** | **−30%** | **≈ +32%** |
| $10,000 | 14.6M | 1.06B | $5,723 | 23% | +112% | +9% | −32% | −41% | ≈ +4% |
| $50,000 | 67.5M | 4.89B | $26,415 | 13% | +90% | −4% | −40% | −47% | ≈ −7% |
| $100,000 | 126M | 9.15B | $49,432 | 12% | +77% | −10% | −44% | −51% | ≈ −13% |

**YT-reUSDe**

| Vốn | Tổng point | Yield trả về | Bull | Base | Bear | Super-bear | EV* |
|---|---|---|---|---|---|---|---|
| $1,000 | 92M | $659 | +140% | +38% | −17% | −30% | ≈ +27% |
| $10,000 | 905M | $6,502 | +98% | +10% | −31% | −39% | ≈ +4% |

\*Trọng số: super-bear 15% / bear 30% / base 40% / bull 15%. Chưa tính tail risk (hack/depeg/pause reUSD → YT ≈ −100%); trừ thêm ~2–3 điểm % nếu gán xác suất 2–3%.
Phần vest được chiết khấu 50% (base), 35% (bear), 25% (super-bear), 70% (bull) cho 3 năm khóa + điều kiện giữ TVL + unlock team 06/2027.

### 7.4 Độ nhạy — YT-reUSD $1k (liquid), ROI theo giá RE × tổng point S2

| Tổng point \ Giá RE | $0.15 | $0.22 | $0.30 | $0.35 | $0.46 | $0.60 |
|---|---|---|---|---|---|---|
| 1.30T | +1% | +21% | +45% | +59% | +91% | +131% |
| 1.55T | −6% | +11% | +31% | +43% | +69% | +103% |
| 1.80T | −11% | +4% | +20% | +31% | +54% | +83% |
| 2.00T | −14% | −1% | +14% | +24% | +44% | +71% |
| 2.50T | −20% | −9% | +3% | +10% | +27% | +48% |

**YT-reUSD $10k (dính vesting):**

| Tổng point \ Giá RE | $0.15 | $0.22 | $0.30 | $0.35 | $0.46 | $0.60 |
|---|---|---|---|---|---|---|
| 1.30T | −17% | −4% | +10% | +19% | +38% | +62% |
| 1.55T | −21% | −10% | +1% | +9% | +25% | +45% |
| 2.00T | −26% | −18% | −9% | −3% | +10% | +26% |
| 2.50T | −29% | −23% | −15% | −11% | −1% | +12% |

Hòa vốn (ví nhỏ): RE ≥ $0.146 @1.3T · $0.174 @1.55T · $0.224 @2.0T · $0.280 @2.5T.
Hòa vốn ($10k, có vesting): RE ≈ $0.30 @1.55T · ≈ $0.37 @2.0T.

---

## 8. Kết luận & chiến lược

1. **Dự án**: fundamental thuộc nhóm tốt của mảng stablecoin/RWA (yield thật, tăng trưởng ngược trend), nhưng **$RE là governance token không value accrual, FDV/TVL đắt hơn peer, và sắp gánh nhiều đợt unlock** → kỳ vọng giá RE trung hạn nên **thấp hơn hiện tại** (base ~$0.33–0.35).
2. **YT là trade trên point, không phải trade trên dự án.** Nhờ yield trả về lớn (~58% giá YT-reUSD) và thị trường đã chiết khấu sẵn (ngầm định FDV ~$174M), YT **size nhỏ** có tỷ lệ lời/lỗ tốt: xấu nhất hợp lý −15…−30%, base +40%, bull +100–160%.
3. **Khuyến nghị cụ thể:**
   - ✅ **Mua YT-reUSD size nhỏ**, giữ tổng point S2 mỗi ví **< 150M** (≈ ≤ $1.3k YT mua hôm nay nếu ví chưa có point S2). Dùng **referral** (+6% miễn phí). Không dùng đòn bẩy, không loop.
   - ⚠️ Size $10k: chỉ khi tự tin RE ≥ $0.35 và S2 không bị kéo dài. EV ~0.
   - ❌ Size ≥ $50k: EV âm (slippage 12–20% + vesting).
   - ⚠️ YT-reUSDe: kinh tế tương tự nhưng rủi ro tranche chịu lỗ + thanh khoản mỏng → chỉ dùng phụ.
   - 🛡️ Bearish hẳn: **PT-reUSD** khóa 11.57% APY (~2.2% trong 72 ngày), là phía "bán point" cho người mua YT.
   - Vào lệnh chia 2–3 lần; YT mua càng muộn càng ít point nhưng rẻ hơn — không có lợi thế lớn khi chờ vì implied APY đang tăng dần.
4. **Checklist theo dõi (có thể làm EV đổi dấu):**
   - Re công bố **ngày kết thúc S2 / kéo dài S2** (kéo dài = xấu cho YT Dec-2026).
   - Re công bố **luật vesting S2** (nếu bỏ vesting → ví lớn hấp dẫn hơn; nếu siết → xấu).
   - **S3** có hay không (quyết định TVL sau 10/12 và giá RE).
   - Point/ngày (API `/public/opportunities`) vượt 13–14B trước tháng 11 → đang đi về kịch bản bear.
   - RE thủng $0.357 (ATL) → chuyển sang giả định bear.
   - Sự kiện bảo hiểm lớn (bão Mỹ tới 30/11), thay đổi redemption buffer reUSD.

---

## 9. Rủi ro chính cho người mua YT

- **Giá RE lúc claim** (lớn nhất) và **lạm phát point / kéo dài season**.
- **Luật S2 chưa công bố** (vesting, điều kiện TVL, có thể loại trừ một số địa chỉ/khu vực — token không dành cho US persons, cần đồng ý ToS khi claim).
- **Smart contract / oracle / depeg**: nếu reUSD dừng tích lũy yield hoặc NAV giảm → YT mất cả phần yield trả về. Tiền lệ: Resolv 03/2026, Stream/Elixir 11/2025.
- **Rủi ro whale/insider**: ví #1 chiếm 28% point S2 — không làm thay đổi giá trị/point nhưng tăng rủi ro xả khi claim.
- **YT về 0 tại maturity** — lợi nhuận chỉ đến từ yield đã nhận + airdrop.

---

## 10. Phương pháp, giới hạn & nguồn

**Giới hạn:** Discord, Telegram và X.com yêu cầu đăng nhập/chặn crawler nên **không đọc trực tiếp được**; phần cộng đồng/sentiment dựa trên nội dung đã được index (tin tức, blog, bài phân tích). Toàn bộ số liệu định lượng lấy trực tiếp từ API (Re, Pendle, DefiLlama, CoinGecko) và on-chain (totalSupply YT qua RPC) tại 28/09/2026 — cần cập nhật lại trước khi vào lệnh vì giá YT/point thay đổi hằng ngày. Chạy lại `python3 yt_model.py` sau khi sửa các input ở đầu file.

**Nguồn chính**
- Docs Re: [About Re Points](https://docs.re.xyz/re-points/about-re-points) · [Referrals](https://docs.re.xyz/re-points/referrals) · [Vesting + TVL requirements](https://docs.re.xyz/re-points/vesting-+-tvl-requirements) · [$RE Tokenomics](https://docs.re.xyz/governance-and-tokenomics/re-tokenomics) · [Governance](https://docs.re.xyz/governance-and-tokenomics/re-governance) · [API reference](https://docs.re.xyz/products/api-reference) · [About reUSD](https://docs.re.xyz/products/about-reusd) · [About reUSDe](https://docs.re.xyz/products/about-reusde)
- Re API: `api.re.xyz/points/public/opportunities`, `/points/public/leaderboard`, `/tvl`, `/tvl/history`, `/apy`, `/supply/*`
- Blog Re: [TGE launch](https://re.xyz/insights/re-tge-launch) · [Inside the Re launch](https://re.xyz/insights/inside-the-re-launch) · [August 2026 update](https://blog.re.xyz/august-2026-performance-update/) · [Coinbase invests](https://re.xyz/insights/coinbase-invests)
- Pendle: API `api-v2.pendle.finance` (markets 0x13285b…77c0, 0x90b70c…737a), SDK quotes · [Pendle fees](https://docs.pendle.finance/pendle-v2/ProtocolMechanics/Mechanisms/Fees)
- Giá/Supply: [CoinGecko RE](https://www.coingecko.com/en/coins/re) · [CoinMarketCap RE](https://coinmarketcap.com/currencies/re-protocol/) · [Tokenomist RE](https://tokenomist.ai/re) · [DefiLlama Re](https://defillama.com/protocol/re) · DefiLlama stablecoins & coins API
- Funding: [The Block – $14M seed](https://www.theblock.co/post/173386/karn-saroya-raises-14-million-for-insurance-protocol-re-as-insurtech-platform-cover-is-wound-down) · [Blockworks](https://blockworks.com/news/first-blockchain-powered-reinsurer-gets-a-funding-boost)
- Listing/giá: [Binance lists RE (Seed Tag)](https://nftevening.com/binance-lists-re-with-seed-tag-for-spot-trading/) · [InteractiveCrypto](https://www.interactivecrypto.com/why-re-token-s-volatility-masks-the-real-value-in-re-protocol-s-yield-products-jul-2026)
- Ngành: [CMC – Yield-bearing stablecoin supply −15% Q2 2026](https://coinmarketcap.com/academy/article/yield-bearing-stablecoin-supply-falls-q2-2026-treasury-backed-growth) · [Bitcoin.com – stampede after 3 collapses](https://news.bitcoin.com/yield-bearing-stablecoins-witness-a-stampede-for-the-exits-after-3-tokens-collapse/) · [FXStreet – slowdown ends three-year run](https://www.fxstreet.com/cryptocurrencies/news/yield-bearing-stablecoin-slowdown-ends-three-year-run-for-crypto-native-products-202607021127) · [CoinDesk – Resolv exploit](https://www.coindesk.com/markets/2026/03/23/resolv-stablecoin-drops-70-after-usd80-million-exploit-after-attacker-mints-usr) · [Chainalysis – Resolv hack](https://www.chainalysis.com/blog/lessons-from-the-resolv-hack/)
- Peer TGE: [Cap auction $106M FDV](https://thedefiant.io/news/defi/cap-labs-cap-token-auction-106m-fdv-oversubscription) · [USD.AI tokenomics](https://docs.usd.ai/governance/tokenomics) · [Apyx hoãn TGE, S2 6%→9%](https://panews.io/articles/01a0cef7-c910-768e-9d43-2194fd1a5897) · [Unitas](https://coinmarketcap.com/currencies/unitas/)
