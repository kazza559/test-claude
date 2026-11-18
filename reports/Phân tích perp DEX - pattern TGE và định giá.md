# Perp DEX: pattern TGE từ dữ liệu lịch sử và định giá Extended, Variational, nhóm new-gen

*Số liệu chốt ngày 18/11/2026 (UTC). Nguồn chính: Polymarket (gamma API + lịch sử giá CLOB), CoinGecko, DefiLlama (phí, doanh thu, OI), Castle Labs (OI/volume ngày 17/11/2026) và tin tức của từng dự án (xem mục Nguồn). Các con số có ghi "ước tính" là suy luận của mình, không phải số công bố. Không phải lời khuyên đầu tư.*

---

## 0. TL;DR

1. **Polymarket định giá quá cao trước TGE perp DEX, và kỳ vọng tụt dần theo thời gian.** Với 5 perp đã TGE có kèo "FDV one day after launch" (Lighter, edgeX, Backpack, GRVT, Paradex):
   - Lúc mới mở kèo, FDV thực tế D1 thấp hơn median ngụ ý khoảng 80% (trung vị, 4/4 trường hợp).
   - Ở T-30 ngày, FDV thực tế vẫn thấp hơn median khoảng 42% (4/5 trường hợp).
   - Ở T-2 ngày, vẫn thấp hơn khoảng 30% (4/5 trường hợp).
   - Quy tắc thực dụng: lấy median T-30 nhân 0.6, median T-7/T-2 nhân 0.7, hoặc giá pre-market nhân 0.9.
2. **Thị trường chung quyết định mặt bằng FDV nhiều hơn fundamentals.**
   - TGE trong bull hoặc mania: HYPE (11/2024) khoảng $4B, ASTER (9/2025) khoảng $4–6B.
   - TGE trong bear 2026: EDGE $656M, GRVT khoảng $260M, BP khoảng $230M, DIME khoảng $45M.
   - Hiện BTC khoảng $63.9k, ETH khoảng $1.79k. Extended và Variational sẽ TGE trong môi trường này.
3. **Sau TGE, D30 giảm 27–39% ở 4/5 token.** Đáy rơi vào D34–D115 (trung vị khoảng D91). Ngoại lệ duy nhất là EDGE: float thấp nên bị đẩy lên +130%, rồi sập khoảng 70% trong một giờ ngày 2/6/2026.
4. **Sau đáy, chỉ token có catalyst thật mới hồi.**
   - BP gấp 4.4 lần D1, nhờ giấy phép CFTC, Backpack Securities và cổ phiếu token hóa.
   - LIT tăng 6.5 lần từ đáy, nhờ buyback từ doanh thu và kênh phân phối Robinhood.
   - DIME, GRVT, EDGE tiếp tục giảm.
5. **"OI cliff": dự án sống nhờ points mất 59–98% OI trong 90 ngày sau TGE.**
   - Mức mất: edgeX −59%, Lighter −61%, Paradex −98%.
   - Ngoại lệ: token có flywheel (HYPE), hoặc airdrop trả dần (GRVT giữ được OI).
   - Extended đã "cliff" ngay trước TGE: points kết thúc 6/10, OI giảm 48% trong 30 ngày.
6. **Chỉ số mới: "Breakeven FDV" = phí user đã trả trước TGE ÷ % airdrop.** Hệ số FDV D1 ÷ breakeven dự báo được tâm lý sau TGE.
   - Tích cực: ASTER khoảng 12x, LIT khoảng 17x (cận trên, vì DefiLlama thiếu dữ liệu phí trước 10/2025).
   - Tiêu cực: edgeX 0.55x, Paradex 0.42x. Farmer lỗ phí ròng nên xả mạnh.
7. **Định giá D1, kịch bản cơ sở:**
   - **Variational: $0.6–1.0B**, khoảng $17–29/point.
   - **Extended: $130–220M**, khoảng $0.55–0.95/point.
   - Đối chiếu Polymarket hiện tại: VAR median khoảng $930–950M, XTEN khoảng $170–185M. Pre-market XTEN $0.20–0.27.
8. **Điểm chất lượng (thang 5):** Variational 3.70 > Arcus 3.00 ≈ QFEX 2.95 > RISEx 2.85 > TxFlow 2.55 ≈ Bulk 2.55 > Extended 2.50.
   - Theo Polymarket, không dự án new-gen nào có khả năng cao TGE trước 2027: RISE 11% trước 31/12/2026, BULK 6%, RISEx 2.5%.
9. **Narrative tăng trưởng của 2026 là TradFi perps 24/7** (cổ phiếu, chỉ số, hàng hóa, FX).
   - trade[XYZ] (HIP-3 trên Hyperliquid) có OI $4.15B.
   - 57–70% volume của Variational là TradFi.
   - OI của QFEX tăng 49% trong 30 ngày.
   - Arcus bán cổ phiếu token hóa qua hạ tầng Robinhood.
   - Dự án đứng đúng narrative này được trả premium.

---

## 1. Bối cảnh thị trường (18/11/2026)

- **Giá chính:** BTC $63,890 (−1.5%/24h), ETH $1,791, SOL $74.
  - Ghi chú thị trường trước đó trong repo đặt BTC quanh $81.5k giữa tháng 10. Như vậy BTC đã giảm khoảng 20% trong một tháng.
  - Hàng loạt token perp lập đáy mới ngày 14/11/2026: DYDX, AVNT, ORDER, MYX, AEVO, F (SynFutures).
- **HYPE như "chỉ số ngành":**
  - Giá $68.4, FDV khoảng $65–68B.
  - Thấp hơn khoảng 30% so với ATH khoảng $97–98 (23/9/2026), và −13% trong 30 ngày.
  - Đỉnh của LIT (24/9) và BP (26/9–1/10) trùng gần như cùng ngày với đỉnh HYPE. Token perp đi theo beta HYPE.

**Bảng 1. Ảnh chụp thị trường perp DEX, 17/11/2026** (OI và volume từ Castle Labs, phí/doanh thu 30 ngày từ DefiLlama)

| Sàn | OI | Thị phần OI | Volume 7 ngày | Vol 24h / OI | Phí hoặc doanh thu 30 ngày | Token |
|---|---|---|---|---|---|---|
| Hyperliquid | $5.54B | 54% | $82.6B | 1.7x | doanh thu $70.0M | HYPE |
| Aster | $1.16B | 11% | $15.0B | 1.6x | phí $4.45M | ASTER |
| Variational | $693M | 6.7% | $13.5B | 3.0x | 0 phí (thu qua spread, DefiLlama không theo dõi) | chưa TGE |
| Lighter | $569M | 5.5% | $22.3B | 4.5x | doanh thu $3.54M (+$2.10M ở bản Robinhood Chain) | LIT |
| GRVT | $341M | 3.3% | $3.75B | 1.6x | không có dữ liệu | GRVT |
| QFEX | $211M | 2.0% (+49%/30 ngày) | $3.01B | 2.7x | không có dữ liệu | chưa có |
| edgeX | $139M | 1.3% | $5.10B | 3.3x | doanh thu $1.41M | EDGE |
| Arcus | $86M | 0.8% | không có dữ liệu | không có dữ liệu | doanh thu $1.63M | chưa có |
| Extended | $50M | 0.5% (−48%/30 ngày) | $2.28B | 5.5x | phí $1.45M | chưa TGE |
| Pacifica | $46M | 0.4% | $5.10B | **15.2x** | doanh thu $3.47M | chưa có |
| RISEx | $34M | 0.3% | $0.83B | 2.9x | phí chain RISE $1.38M | chưa có |
| Nado | $29M | 0.3% | $3.38B | **13.4x** | doanh thu $0.87M | chưa có |
| TxFlow | $27M | 0.3% | khoảng $1.4B (ước tính từ phí) | khoảng 7x (ước tính) | doanh thu $1.76M | chưa có |
| Bulk | khoảng $12M (DefiLlama) | — | $0.29B | — | phí $0.48M | chưa có |

Ngoài bảng trên: trade[XYZ] (giao diện HIP-3 trên Hyperliquid, chủ yếu cổ phiếu và chỉ số) có OI $4.15B theo DefiLlama, lớn hơn mọi perp DEX khác trừ chính Hyperliquid.

---

## 2. Dữ liệu lịch sử các perp DEX đã TGE

**Bảng 2. Hồ sơ TGE và kết quả**

| Token | Ngày TGE | Airdrop tại TGE | Insider | Vốn private | FDV D1 | Đáy sau TGE | Đỉnh sau TGE | FDV hiện tại | Hiện tại / D1 |
|---|---|---|---|---|---|---|---|---|---|
| **HYPE** | 29/11/2024 | 31%, mở khóa 100% | 0% VC (contributors khoảng 23.8%) | không gọi vốn | khoảng $4B | — | khoảng $97B (23/9/2026) | khoảng $65–68B | khoảng **16x** |
| **ASTER** | 17/9/2025 | 8.8% (704M). Tổng phần cộng đồng 53.5% (nhiều stage) | n/a | YZi Labs (CZ) hậu thuẫn | khoảng $4–6B (giá $0.5–0.77 trong 24–48h đầu) | khoảng $3.7B (6/2/2026) | $19.3B (24/9/2025) | khoảng $4.3B | khoảng 0.8–1x |
| **LIT** (Lighter) | 30/12/2025 | 25% (12.5M points thành 250M LIT, khoảng 20 LIT/point, khoảng $54/point ở D1) | 50% (26% team, 24% nhà đầu tư; cliff 12 tháng, sau đó 36 tháng) | $68M ở định giá $1.5B (Founders Fund, Ribbit, Haun, Robinhood) | khoảng $2.7B | $0.81B (D91) | $5.3B (D268) | khoảng $2.8B | khoảng 1.0x |
| **DIME** (Paradex) | 5/3/2026 | 25% | n/a | Paradigm ấp ủ | khoảng $40–50M | $7.7M (D115) | khoảng $70M (D220) | khoảng $28M | khoảng 0.6x |
| **BP** (Backpack) | 23/3/2026 | 25% | báo chí đưa tin "0% insider", cần kiểm chứng | n/a | khoảng $230M | $120M (D65) | $1.35–1.65B (26/9–1/10) | khoảng $1.0B | khoảng **4.4x** |
| **EDGE** (edgeX) | 31/3/2026 | 25% (30% nếu gồm pre-TGE season) | float thấp; ZachXBT cáo buộc insider kiểm soát cung | Amber Group ấp ủ | khoảng $656M | $242M (D97) | $1.51B (D52) | khoảng $277M | khoảng 0.42x |
| **GRVT** | 30/7/2026 | 28% (S1+S2), trả dần trong 12 tháng | n/a | nguồn mâu thuẫn ($14–33M) | khoảng $250–260M | $150M (D34) | $328M (D12) | khoảng $168M | khoảng 0.65x |

Ghi chú về cách đo:
- D1 là "1 ngày sau launch". Polymarket chốt lúc 16:00 ET ngày hôm sau.
- LIT, EDGE, BP, DIME, GRVT dùng giá đóng cửa ngày trên CoinGecko. HYPE và ASTER lấy từ tin tức, vì API công khai của CoinGecko chỉ trả 365 ngày gần nhất.

**Bảng 3. Đường giá sau TGE** (giá đóng cửa ngày, % so với D1)

| Token | D1 | D7 | D30 | D90 | D180 | Đáy (ngày) | Đỉnh (ngày) | Hiện tại |
|---|---|---|---|---|---|---|---|---|
| LIT | $2.70 | $3.00 (+11%) | $1.97 (−27%) | $0.83 (−69%) | $1.72 (−36%) | $0.81 (D91) | $5.32 (D268) | $2.82 (+4%) |
| EDGE | $0.656 | $0.923 (+41%) | $1.18 (+80%) | $0.278 (−58%) | $0.602 (−8%) | $0.242 (D97) | $1.51 (D52) | $0.277 (−58%) |
| BP | $0.229 | $0.156 (−32%) | $0.141 (−39%) | $0.655 (+186%) | $0.571 (+149%) | $0.120 (D65) | $1.35 (D187) | $1.007 (+340%) |
| DIME | $0.040 | $0.042 (+5%) | $0.027 (−32%) | $0.020 (−50%) | $0.015 (−63%) | $0.0077 (D115) | $0.070 (D220) | $0.0275 (−31%) |
| GRVT | $0.244 | $0.300 (+23%) | $0.165 (−32%) | $0.235 (−4%) | — | $0.150 (D34) | $0.328 (D12) | $0.168 (−31%) |

**Bảng 4. Open interest quanh TGE** (DefiLlama)

| Sàn | T-30 | T0 | T+30 | T+90 | Hiện tại | Diễn giải |
|---|---|---|---|---|---|---|
| Lighter | $820M | $699M | $648M | $318M (−61% so với T-30) | $578M | Hồi lại nhờ bản Robinhood Chain và points thưởng bằng LIT |
| edgeX | $1.01B | $1.03B | $896M | $418M (−59%) | $141M (−86%) | Points hết là OI rút |
| Paradex | $286M | $207M | $24M | $7M (−98%) | $11M | Sụp hoàn toàn |
| GRVT | $340M | $355M | $433M | $435M (+28%) | $339M | Airdrop trả dần 12 tháng giữ chân user |
| Hyperliquid | — | — | $1.6B | $1.6B | $5.7B (+$4.15B ở trade[XYZ]) | Token có flywheel: khoảng 97–99% phí dùng để buyback |
| Aster | — | — | $1.62B | $1.27B | $1.16B | Airdrop chia nhiều stage |

---

## 3. Polymarket: pattern định giá trước TGE

Mình kéo toàn bộ ladder "FDV above $X one day after launch" của các perp DEX qua Polymarket API. Cách tính:
- Ghép xác suất các ngưỡng $X thành đường P(FDV > X) theo từng ngày.
- Median ngụ ý là điểm đường này cắt 50%, nội suy theo log giữa hai ngưỡng.

**Bảng 5. Median FDV ngụ ý trên Polymarket so với kết quả thực tế**

| Dự án | Median lúc mở kèo | T-90 | T-30 | T-7 | T-2 | FDV D1 thực tế | Sai số ở T-30 | Sai số ở T-2 |
|---|---|---|---|---|---|---|---|---|
| Lighter | dưới $2.0B (6/2025)\* | $3.92B | $2.60B | $3.35B | $2.89B | khoảng $2.7B (kèo chốt khoảng $2–3B) | +4% | −7% |
| edgeX | $2.72B (11/2025) | $1.39B | $1.13B | $515M | $465M | khoảng $656M (khoảng $600–700M) | −42% | +41% |
| Backpack | $1.42B (11/2025) | $1.10B | $510M | $352M | $327M | khoảng $230M (khoảng $200–300M) | −55% | −30% |
| GRVT | $278M (2/2026) | $191M | $356M | $362M | $377M | khoảng $260M (khoảng $250–300M) | −27% | −31% |
| Paradex | dưới $750M (11/2025) | dưới $750M | dưới $300M | dưới $300M | dưới $300M | khoảng $45M (khoảng $40–80M) | −85% hoặc tệ hơn | −85% hoặc tệ hơn |

\*Kèo Lighter đầu tiên có hạn 31/12/2025, nên giá kèo gồm cả rủi ro TGE trễ.

**Thống kê sai số** (FDV thực tế so với median Polymarket, trung vị):

| Mốc | Sai số trung vị | Số lần Polymarket định giá quá cao |
|---|---|---|
| Lúc mở kèo | −80% | 4/4 |
| T-30 | −42% | 4/5 |
| T-7 | −28% | 4/5 |
| T-2 | −30% | 4/5 |

**Diễn biến kỳ vọng của từng dự án theo thời gian:**
- **Backpack:** $1.42B, rồi $1.10B, $510M, $352M, $327M; thực tế khoảng $230M.
- **edgeX:** $2.72B, rồi $1.39B, $1.13B, $515M; thực tế $656M.
  - Đây là trường hợp duy nhất kết quả cao hơn median cuối, vì FUD về minh bạch kéo kèo xuống quá đà.
  - Pre-market khi đó khoảng $700–729M, sát kết quả hơn Polymarket.
- **Lighter:** dự án mạnh nhất về traction có sai số nhỏ nhất (+4% ở T-30, −7% ở T-2).

**Đối chiếu với TGE không phải perp:**
- Monad: T-30 $6.24B, thực tế $3–4B, tức định giá quá cao.
- MegaETH: T-30 dưới $600M, thực tế $1.5–2B, tức định giá quá thấp.
- Như vậy thiên lệch một chiều (quá cao) đặc biệt rõ ở nhóm perp DEX.

**Vì sao nhóm perp bị định giá quá cao** (diễn giải của mình):
1. Người mua YES phần lớn là cộng đồng hoặc farmer lạc quan. Người có lý do bán là farmer muốn hedge, nhưng họ ít dùng Polymarket.
2. Thời điểm chốt kèo (16:00 ET ngày D1) rơi đúng lúc áp lực xả airdrop cao nhất. Ở 3/5 token, giá D1 thấp hơn giá ngày TGE: BP −40%, DIME −20%, GRVT −12%.
3. Thông tin xấu thường được tiết lộ dần: % insider, lạm phát points, timeline trễ, rồi thị trường chung yếu đi.
4. Năm 2026 có quá nhiều perp TGE, nên dòng tiền và sự chú ý bị chia nhỏ.

**Quy tắc áp dụng:**
- FDV D1 cơ sở bằng khoảng 0.6 lần median T-30, hoặc 0.7 lần median T-7/T-2. Với dự án top đầu về traction (kiểu Lighter, Variational), nên dùng hệ số 0.85–0.95.
- Pre-market perp (Hyperliquid, MEXC, Whales) chính xác hơn Polymarket. Lịch sử vẫn hơi cao khoảng 5–10%: edgeX khoảng $700–729M thành $656M; Lighter trên $3B thành $2.7B.
- Độ dốc của kỳ vọng là một tín hiệu riêng. Ladder giảm đều qua nhiều tháng (Backpack, edgeX, Paradex) là cảnh báo. Ladder tăng nhờ catalyst cụ thể (Variational từ 5/2026, sau Series A $50M do Dragonfly dẫn) là tín hiệu tốt.

---

## 4. Các pattern rút ra từ dữ liệu

| # | Pattern | Bằng chứng |
|---|---|---|
| P1 | Polymarket quá cao và giảm dần theo thời gian | Mục 3 |
| P2 | Pre-market chính xác hơn Polymarket nhưng vẫn cao khoảng 5–10% | edgeX, Lighter |
| P3 | Chế độ thị trường quyết định mặt bằng FDV | Bull: HYPE, ASTER $4B+. Bear 2026: $45–656M |
| P4 | D30 giảm 27–39%; đáy ở D34–D115, trung vị khoảng D91 | Bảng 3: LIT, BP, DIME, GRVT |
| P5 | Float thấp cộng insider kiểm soát dễ bị thao túng: tăng mạnh rồi sập | EDGE +130% đến D52, sau đó −70% trong 1 giờ (2/6/2026) |
| P6 | OI cliff sau TGE (−59% đến −98% trong 90 ngày) nếu token không có flywheel hoặc vesting | Bảng 4 |
| P7 | Hệ số FDV D1 ÷ breakeven dự báo tâm lý sau TGE | Bảng 6 |
| P8 | Re-rating chỉ đến từ catalyst thật: buyback bằng doanh thu, giấy phép pháp lý, đối tác phân phối | LIT (buyback, Robinhood), BP (CFTC, chứng khoán token hóa), HYPE (buyback, ETF) |
| P9 | Đối tác phân phối có thể thành đối thủ | Robinhood chọn Bitstamp cho perps tại Mỹ (30/9/2026), LIT −20% trong ngày |
| P10 | Beta ngành: token perp đi theo HYPE | Đỉnh HYPE 23/9, LIT 24/9, BP 26/9 |
| P11 | Timeline luôn trễ hơn công bố, nên chi phí farm và độ pha loãng tăng | Extended "H1/2026" thành 11–12/2026; Variational Q3 thành Q4; kèo "launch by" của Pacifica thua 4 quý liền, Hibachi 3 quý, Bulk 2 quý |
| P12 | Cliff 12 tháng của insider là "đợt xả" thứ hai | LIT: mở khóa đầu tiên khoảng 27/12/2026–28/1/2027 (500M LIT trong 3 năm, khoảng 3.2M/tuần, khoảng 20 lần mức buyback 10/2026). BP/EDGE khoảng 3/2027, GRVT khoảng 7/2027, VAR/XTEN khoảng Q4/2027 |
| P13 | Vol/OI là máy phát hiện wash/farm | Pacifica 15x, Nado 13x, Extended 5.5x, Lighter 4.5x, so với HL 1.7x, GRVT 1.6x |
| P14 | Narrative TradFi perps 24/7 được trả premium | trade[XYZ] OI $4.15B; Variational 57–70% TradFi; QFEX OI +49%/30 ngày |

**Bảng 6. Breakeven FDV: farmer có lời trên phí hay không** (chỉ tính phí giao dịch, chưa tính spread, slippage, funding, PnL)

| Dự án | Phí user đã trả trước TGE (DefiLlama) | % airdrop | Breakeven FDV | FDV D1 | Hệ số D1 / breakeven |
|---|---|---|---|---|---|
| Aster | $35.8M | 8.8% | khoảng $0.41B | khoảng $4.8B | khoảng **12x** |
| Lighter | từ $38.5M trở lên\* | 25% | khoảng $0.15B | khoảng $2.7B | khoảng **17x** (cận trên) |
| edgeX | **$299M** | 25% | khoảng $1.2B | khoảng $0.66B | **0.55x** |
| Paradex | $26.6M | 25% | khoảng $0.11B | khoảng $0.045B | **0.42x** |
| *Extended (chưa TGE)* | $36.3M | 28.3% (30% trừ 5.8% của desk market-making nội bộ) | khoảng $0.13B | pre-market $0.20–0.27B | khoảng 1.3–1.9x (dự phóng) |
| *Variational (chưa TGE)* | 0 phí; spread gộp khoảng $119M/năm (9/2026) | 32% | khoảng $0.2–0.3B (ước tính, nếu tổng spread đã trả khoảng $60–100M) | Polymarket khoảng $0.93B | khoảng 3–5x (dự phóng) |

\*DefiLlama chỉ theo dõi phí Lighter từ 12/10/2025, và Lighter miễn phí cho retail, nên hệ số 17x là cận trên. Phí trước TGE của Hyperliquid không có trên DefiLlama; ước tính thô của mình là trên 10x.

---

## 5. Framework chấm điểm perp DEX: 7 trụ

| Trụ (trọng số) | Đo bằng gì | Dấu hiệu tốt | Dấu hiệu xấu | Nguồn dữ liệu |
|---|---|---|---|---|
| **1. Đội ngũ và vốn (15%)** | Lý lịch (HFT/quant, vận hành sàn), từng exit chưa; tier VC; định giá vòng cuối; angel hoặc advisor có sức kéo hệ sinh thái; % insider và lịch vesting | Cựu HRT, Citadel, Tower, Jane Street; VC tier-1; insider tối đa 50% với cliff từ 12 tháng | Ẩn danh và không có backer; insider nắm phần lớn float | The Block, Crunchbase, docs dự án |
| **2. Sản phẩm và moat (15%)** | Kiến trúc (L1 riêng, ZK, tích hợp vào validator, RFQ/OLP, CEX); độ trễ; tự lưu ký; độ phủ thị trường (TradFi 24/7, pre-IPO); chi phí giao dịch thực (phí cộng spread); engine rủi ro và lịch sử sự cố | Có lợi thế khó sao chép; ít sự cố; đúng narrative | Fork hoặc copy; oracle yếu; từng bị thao túng | Docs, báo cáo audit, X |
| **3. Chất lượng traction (20%)** | OI và thị phần OI; Vol/OI; phí và doanh thu thật; doanh thu trên OI; xu hướng OI 30/90 ngày; % volume không đến từ points | Vol/OI dưới 3x; OI tăng; có dòng lệnh từ đối tác phân phối | Vol/OI trên 5x; OI giảm khi points giảm | Castle Labs, DefiLlama |
| **4. Kinh tế airdrop (20%)** | % airdrop và lịch mở khóa; tổng points và tốc độ phát; pha loãng mỗi tuần; breakeven FDV; phần dự án tự phân bổ cho mình; chính sách sybil/wash; độ trễ timeline | Từ 25% cho user; hệ số D1/breakeven trên 3x | Hệ số dưới 1x; desk nội bộ cũng farm points | Docs, DefiLlama, kèo "launch by" trên Polymarket |
| **5. Giá trị token (10%)** | Buyback/burn (% doanh thu thật); staking (giảm phí, boost vault); trả phí bằng token; quyền quản trị | Buyback từ doanh thu thật | Token chỉ để quản trị | Docs, on-chain |
| **6. Tín hiệu và timing (10%)** | Mức và độ dốc của ladder Polymarket; pre-market; giá OTC của points; chế độ BTC/HYPE; lịch TGE trùng nhau; sàn niêm yết ngày TGE | Kỳ vọng ổn định hoặc tăng; niêm yết Binance hoặc Coinbase | Kỳ vọng giảm đều; không lên CEX lớn (như DIME) | Polymarket, pre-market trên Hyperliquid/MEXC |
| **7. Rủi ro (10%; điểm cao là rủi ro thấp)** | Rủi ro đối ứng (OLP, vault); mức tập trung hóa; pháp lý (KYC, chặn vùng); minh bạch đội ngũ; phụ thuộc đối tác | Kiểm toán, minh bạch, có giấy phép | Đối ứng không minh bạch; khóa bình luận khi bị hỏi (edgeX) | Audit, tin tức |

**Những khía cạnh ít người để ý** (đã kiểm chứng ở trên, dùng được ngay):
1. **Độ dốc ladder Polymarket.** Kỳ vọng giảm qua 3 tháng liên tiếp là tín hiệu xấu hơn bản thân mức giá.
2. **Chênh lệch pre-market và Polymarket.** Với XTEN, pre-market $0.20–0.27 nhưng Polymarket khoảng $0.17–0.18, tức thị trường dự đoán D1 thấp hơn pre-market.
3. **Breakeven FDV và hệ số D1/breakeven** (Bảng 6).
4. **Độ nhạy của OI với points.** Khi tốc độ phát points giảm hoặc dừng, OI giảm bao nhiêu? Extended giảm 73% từ đỉnh và 48% trong 30 ngày sau khi points kết thúc.
5. **Vol/OI và doanh thu trên OI.** Dùng để phân biệt volume thật với volume farm.
6. **Phần dự án tự phân bổ cho mình.** Desk market-making nội bộ của Extended nhận 5.8% pool airdrop. EDGE có float tập trung.
7. **Thiết kế vesting của airdrop.** Mở khóa 100% (LIT, EDGE, BP, XTEN, VAR) thì xả nhanh hơn. Trả dần (GRVT) giữ được OI nhưng ít hype.
8. **Phụ thuộc đối tác phân phối, và rủi ro đối tác thành đối thủ.**
   - Các cặp phụ thuộc: Robinhood với Lighter, Arcus, Meridian; Circle (Arc) với Extended; CZ/Binance với Aster.
   - Bài học Robinhood chọn Bitstamp ở P9.
9. **Sự kiện pháp lý như catalyst.** CFTC chấp thuận Backpack làm sàn phái sinh và clearinghouse, BP tăng 42% trong ngày. Extended nộp whitepaper MiCA lên CySEC.
10. **Lịch cliff 12 tháng** của các TGE 2025–2026 (P12).
11. **Thời điểm đáy sau TGE (D34–D115)** để canh mua lại token tốt.
12. **Chỉ số trễ timeline:** số kèo "launch by" đã thua liên tiếp.
13. **Trọng số chấm điểm của points.** Chỉ volume thì dễ wash. Có thêm OI, thời gian, phí, TVL (như TxFlow) thì khó wash hơn. KYC (Arcus, QFEX) nghĩa là ít sybil, phần chia cho user thật lớn hơn.

**Kiểm tra hợp lý (retro) của scorecard:**

| Dự án (chấm tại TGE) | Đội ngũ | Sản phẩm | Traction | Airdrop | Token | Tín hiệu | Rủi ro | **Điểm** | Hiện tại / D1 |
|---|---|---|---|---|---|---|---|---|---|
| HYPE | 5 | 5 | 5 | 5 | 5 | 4 | 4 | **4.80** | khoảng 16x |
| LIT | 5 | 4 | 4 | 4 | 3 | 3 | 4 | **3.95** | khoảng 1.0x (đáy −70%, đỉnh gấp đôi) |
| BP | 4 | 4 | 3 | 3 | 3 | 2 | 3 | **3.20** | khoảng 4.4x |
| ASTER | 3 | 3 | 2 | 3 | 3 | 5 | 2 | **2.90** | khoảng 0.8–1x (từng đạt đỉnh gấp 4) |
| GRVT | 3 | 3 | 3 | 2 | 2 | 2 | 3 | **2.60** | khoảng 0.65x |
| EDGE | 2 | 3 | 2 | 1 | 2 | 2 | 1 | **1.85** | khoảng 0.42x |
| DIME | 3 | 2 | 1 | 1 | 1 | 1 | 3 | **1.65** | khoảng 0.6x |

- Tương quan hạng Spearman giữa điểm và kết quả là 0.93.
- Đây là kiểm tra trong mẫu: mình chấm khi đã biết kết quả, nên có thiên lệch hindsight. Coi đây là kiểm tra logic, không phải kiểm định.
- Lưu ý ASTER: điểm "Tín hiệu" (CZ, mania) chi phối biến động ngắn hạn. Các trụ còn lại dự báo xu hướng 6–12 tháng tốt hơn.

---

## 6. Extended (XTEN)

**Hồ sơ**
- **Đội ngũ:** founder Ruslan Fakhrutdinov, cựu trưởng mảng vận hành crypto ở Revolut. Thành lập 2023.
- **Vốn:** $6.5M từ Tioga, Semantic, StarkWare, Konstantin Lomashuk (Lido), Prelude, Cyber Fund.
  - Có tin đồn dự án từ chối vòng mới ở FDV trên $300M. Mình chưa kiểm chứng được.
- **Sản phẩm:** CLOB lai với settlement on-chain.
  - Lộ trình hạ tầng: StarkEx, sang Starknet (8/2025), rồi chuyển settlement sang **Arc**, L1 của Circle, ngày 22/10/2026.
  - Hơn 400 thị trường, gồm vàng, dầu, FX, S&P và Nasdaq. Đòn bẩy tới 100x.
- **Tokenomics:** tổng cung 1B XTEN.
  - **30% cộng đồng (300M), mở khóa 100% tại TGE.** Trong đó 17.38M (khoảng 5.8% pool) là points do **desk market-making nội bộ** (X10 Ltd) kiếm được từ 11/2024 đến 4/2026.
  - 20% hệ sinh thái: 150M cho staking, 50M quỹ phát triển (28.6M mở khóa tại TGE).
  - 50% founders, team và nhà đầu tư, khóa 12 tháng. Nhà đầu tư nhận 25% ở tháng 12, phần còn lại trả dần đến tháng 48. Team trả dần từ tháng 13 đến tháng 48.
  - Staking 6 bậc: giảm phí 5–30%, boost vault 0.5–5x, mức gửi vault tối đa tới $2M, unstake mất 7 ngày.
  - Whitepaper đã nộp CySEC theo MiCA.
- **Points:** khoảng 70M points (ước tính cộng đồng; 69.2M đã phát đến 6/10/2026). Chương trình **đã kết thúc**. Tỷ lệ quy đổi khoảng 4.3 XTEN/point.
- **Traction:** OI đỉnh $189M (28/1/2026), nay $50–51M.
  - Volume 7 ngày $2.28B, Vol/OI 5.5x.
  - Phí 30 ngày $1.45M (khoảng $17M/năm). Tổng phí đã thu $36.3M.
- **Trạng thái:**
  - Công cụ kiểm tra allocation và điều khoản phân phối mở từ 11/11/2026.
  - **Hạn ký: 31/12/2026, 23:59 UTC.**
  - Ví Starknet phải chỉ định một ví EVM để nhận token.
  - Chưa công bố ngày TGE; hướng dẫn trước đó là "tháng 11/2026".
- **Thị trường:**
  - Pre-market XTEN khoảng $0.20–0.27 trên Hyperliquid, Lighter, edgeX, MEXC (Coinglass ghi $0.1995 ngày 13/11), tương đương FDV $200–270M.
  - Polymarket (hạn 31/12/2026): P(>$150M) 57%, P(>$300M) 16.5%, P(>$500M) 5.5%.
  - Median khoảng **$169M**, hoặc khoảng $184M nếu giả định chắc chắn có launch (P(launch) khoảng 0.9).
  - Diễn biến median: $479M (1/2026), $294M (2), $181M (4), $315M (7), $150M (8), $251M (10), $169M (18/11).

**Định giá D1** (4 phương pháp)

| Phương pháp | Kết quả |
|---|---|
| Polymarket nhân hệ số hiệu chỉnh 0.7 | khoảng $120–130M |
| Pre-market nhân hệ số hiệu chỉnh 0.9 | khoảng $180–240M |
| So sánh với FDV D1 / chỉ số 30 ngày trước TGE của LIT, EDGE, GRVT, BP | OI khoảng $70M cho $43–227M (trung vị khoảng $52M); volume 30 ngày khoảng $10B cho $74–142M; phí năm hóa $17.4M cho $44–341M. Trung tâm khoảng $100–150M |
| Breakeven farmer | khoảng $128M |

**Kịch bản FDV D1**

| Kịch bản | FDV D1 | Giá trị mỗi point |
|---|---|---|
| Bear (BTC thủng $60k, niêm yết yếu) | $70–120M | khoảng $0.30–0.51 |
| **Base** | **$130–220M** | **khoảng $0.55–0.95** |
| Bull (Binance hoặc Coinbase spot, narrative Arc/Circle) | $250–350M | khoảng $1.07–1.50 |

Giá trị mỗi point theo FDV, với 300M XTEN chia cho khoảng 70M points: $100M cho $0.43; $150M cho $0.64; $200M cho $0.86; $250M cho $1.07; $300M cho $1.29.

**Sau TGE**
- Theo pattern P4, kỳ vọng D30 giảm 25–40%. Đáy có thể rơi vào D35–D115.
- OI đã "cliff" trước TGE nên lực đỡ từ volume yếu. Staking (giảm phí, boost vault) có thể hút bớt một phần cung.
- D90 kịch bản cơ sở: $70–150M. Đợt cung tiếp theo là cliff 12 tháng, khoảng cuối 2027.

**Hành động gợi ý**
1. Ký điều khoản trước 31/12. Nếu dùng Starknet, chỉ định ví EVM nhận token.
2. Biết allocation rồi thì cân nhắc hedge, theo một trong hai cách:
   - Short pre-market. Rủi ro: squeeze và funding của pre-market perp.
   - Mua NO ở ngưỡng gần median trên Polymarket, ví dụ NO cho ">$150M" khoảng 43¢, để bảo hiểm kịch bản FDV thấp.
3. Mặc định theo dữ liệu: bán phần lớn trong 24–48h đầu.
4. Chỉ mua lại sau D60–D110, và chỉ khi OI ổn định và cơ chế staking/buyback rõ ràng.

**Điểm: 2.50/5.** Đội ngũ ổn. Nhưng traction đang giảm, hệ số D1/breakeven chỉ khoảng 1.3–1.9x, và dự án tự phân bổ 5.8% pool.

---

## 7. Variational (VAR)

**Hồ sơ**
- **Đội ngũ:** Lucas Schuermann (CEO) và Edward Yu, nhiều năm làm quant và market making ở quỹ. Engine định giá OLP đã phát triển hơn 7 năm. Công ty đặt ở Cayman.
- **Vốn:** tổng hơn $60M, định giá không công bố.
  - Seed $10.3M (10/2024), Bain Capital Crypto và Peak XV đồng dẫn.
  - Series A $50M (20/5/2026), Dragonfly dẫn, có Bain và Coinbase Ventures.
- **Sản phẩm:**
  - **Omni (retail):** RFQ, 0 phí maker/taker. OLP là đối ứng duy nhất và hedge ra bên ngoài. Đòn bẩy tới 50x.
  - **Pro (tổ chức):** RFQ nhiều market maker, đang ở giai đoạn waitlist.
  - Khoảng 450–500 thị trường. Hàng hóa (vàng, bạc, đồng, WTI) có từ 5/2026, cùng chỉ số, cổ phiếu và pre-IPO perps. Khoảng **57–70% volume là TradFi**.
  - Có chương trình hoàn lỗ (loss refund) với xác suất 1–5%.
- **Tokenomics:**
  - **32% Genesis airdrop, mở khóa 100%.** Để claim cần ít nhất 1 point và phải ký điều khoản. Token không ai claim sẽ bị burn.
  - 18% foundation.
  - 50% team và nhà đầu tư: khóa 12 tháng, sau đó trả dần ít nhất 3 năm.
  - **100% doanh thu treasury dùng để buyback và burn.**
- **Points:** 3M retro (17/12/2025) cộng 150k mỗi tuần.
  - Tổng 9.15M đến 25/9, khoảng 10.5M giữa tháng 11, khoảng 11.1M nếu TGE vào 31/12.
  - Mỗi tuần pha loãng khoảng 1.4%.
- **Traction:**
  - Đỉnh: 5 ngày 21–25/9 đạt $17.4B volume (ngày cao nhất $4.02B), thị phần 14.95%, đứng **thứ 2 sau Hyperliquid**.
  - OI đỉnh $1.15B (6/10), nay $693M (−29%/30 ngày). Volume 7 ngày $13.5B, Vol/OI khoảng 3x.
  - Spread gộp khoảng $119M/năm (9/2026). Treasury nhận 20%, khoảng $24M/năm, và tỷ lệ này "có thể thay đổi".
- **Polymarket** (hạn 2027):
  - Median khoảng **$930–950M**: P(>$500M) 88.5%, P(>$800M) 61.5%, P(>$1B) 44.5%, P(>$2B) 12.5%.
  - Diễn biến median: $235M (4/2026), $504M (5, sau Series A), $906M (8), đỉnh $1.27B (3/10), $1.12B (14/11), khoảng $0.95B (18/11).

**Định giá D1**

| Phương pháp | Kết quả |
|---|---|
| Polymarket nhân 0.6–0.7 (thiên lệch trung bình của nhóm) | khoảng $560–670M |
| Polymarket nhân 0.9 (sai số kiểu Lighter, cho dự án top đầu) | khoảng $840M |
| So sánh theo OI (khoảng $850M nhân bội số 0.61–3.24, trung vị 0.74) | $520M–2.75B (trung vị khoảng $630M) |
| So sánh theo volume 30 ngày (khoảng $58B nhân 0.0074–0.0142) | $430–820M |
| Doanh thu treasury $24M nhân 20–40 lần (LIT hiện khoảng 41x, EDGE khoảng 16x) | $480–950M |
| Mô hình VAR·EXT tracker trong repo (10/2026) | khoảng $705M |

**Kịch bản FDV D1**

| Kịch bản | FDV D1 | Giá trị mỗi point (khoảng 11.1M points) |
|---|---|---|
| Bear (risk-off kéo dài, lo ngại OLP thiếu minh bạch) | $350–550M | khoảng $10–16 |
| **Base** | **$600M–1.0B** (trung tâm khoảng $800M) | **khoảng $17–29** (khoảng $23 ở $800M) |
| Bull (thị trường hồi, niêm yết tier-1, buyback chạy rõ) | $1.2–1.8B | khoảng $35–52 |

**Sau TGE**
- 32% mở khóa là float lớn nhất nhóm, nên áp lực bán tuần đầu sẽ mạnh.
- Buyback khoảng $24M/năm chỉ bằng khoảng 3%/năm của FDV $800M.
- Nếu points dừng, OI có thể giảm 40–60% trong 90 ngày (P6). Tuy vậy, mô hình 0 phí cộng TradFi có thể giữ volume tốt hơn Extended hay edgeX.
- D90 kịch bản cơ sở: $350–700M.
- Catalyst có thể giúp re-rating: ra mắt Pro, mở OLP cho cộng đồng gửi vốn, niêm yết tier-1, buyback minh bạch on-chain.

**Rủi ro**
- OLP là đối ứng duy nhất và không công bố vị thế.
- Có last-look khi thị trường biến động mạnh.
- Chặn user ở Mỹ và Canada.
- 50% thuộc insider.

**Hành động gợi ý**
- Chỉ farm tiếp khi chi phí mỗi point (spread cộng funding) thấp hơn khoảng $17–20, tức đã chiết khấu so với kịch bản cơ sở. Nhớ mỗi tuần points bị pha loãng khoảng 1.4%.
- Ưu tiên cặp có spread thấp. Ví dụ, NDX từng được báo giá 0.68 bps ở quy mô $1M.
- Muốn khóa một phần giá trị: mua NO cho ">$1B" (khoảng 55.5¢).
- Ký điều khoản claim ngay khi mở.

**Điểm: 3.70/5.** Cao nhất nhóm chưa TGE.

---

## 8. Nhóm new-gen: RISEx, TxFlow, Bulk, Arcus, QFEX

**Bảng 7. So sánh nhanh**

| | RISEx | TxFlow | Bulk | Arcus | QFEX |
|---|---|---|---|---|---|
| **Kiến trúc** | Perp DEX chủ lực trên RISE (Ethereum L2 tốc độ cao) | L1 riêng, gồm perps, spot, prediction | CLOB tích hợp vào validator Solana (fork Jito-Agave) | Ứng dụng trên Robinhood Chain (L2 dựa trên Arbitrum) | Sàn tập trung (CLOB + clearing), lưu ký tại BitGo, bắt buộc KYC |
| **Đội ngũ** | RISE Labs (CEO Sam Battenally) cùng team BSX (mua lại 11/2025) | Gần như ẩn danh (một nguồn nêu Matt Hu, Harrison Rea, Jack Wang) | North Star Labs | Eddie Zhang (CEO); Antonio Juliano trong hội đồng quản trị; ấp ủ tại dYdX Labs | Cựu Tower, Citadel, Jump, HRT, Optiver, Jane Street |
| **Vốn** | khoảng $8M (Galaxy dẫn; angel Vitalik, Stani Kulechov) | Không VC, không phân bổ cho nhà đầu tư | Seed $8M (6MV và Robot dẫn; Wintermute, Big Brain, Anatoly) | Robinhood Crypto đầu tư | Seed $9.5M ở định giá $95M (General Catalyst, YC; Paul Graham) |
| **Points** | Ignite S1: 200k/tuần từ cuối 7/2026, kết thúc muộn nhất Q2/2027. 100% RISE points dành cho user RISEx. 1.5% cung RISE dành cho holder BSX | S1 từ 12/10/2026: 1.25M/tuần cho trader (82% ngân sách) cộng 488k/tháng quỹ growth. Kết thúc muộn nhất Q1/2027. Chỉ tính perps | AURA = USDC gửi trước nhân thời gian (cộng stake SOL, referral). Team nói 30% cung dành cho user | S1 từ 1/10/2026, khoảng 250k/tuần | Không có points chính thức; tin đồn "Season 0" |
| **Token** | Chưa công bố | Chưa xác nhận | Chưa có (30% "để dành" cho user) | "Đã xác nhận", có phần cho cộng đồng dYdX | Chưa có |
| **OI (17/11)** | $34M (đỉnh $45M) | $27–28M (đỉnh $48M) | khoảng $12M | $84–86M (đỉnh $124M) | **$197–211M (+49%/30 ngày)** |
| **Phí hoặc doanh thu 30 ngày** | $1.38M (phí chain RISE) | $1.76M (khoảng $21M/năm) | $0.48M | $1.63M (khoảng $20M/năm) | không có dữ liệu |
| **Polymarket** | RISE có token trước 31/12/2026: 11%; RISEx: 2.5%; trước 30/6/2027: khoảng 34–40% | — | Trước 31/12/2026: 6%; trước 30/6/2027: 29.5% | — | Launch và FDV > $50M trước hết 2027: 63.5%; > $200M: 48%; > $500M: 26.5% (kèo mỏng) |
| **FDV D1 ước tính (bear / base / bull)** | $80–150M / $200–400M / $600M–1B | $30–80M / $100–250M / trên $400M | $50–100M / $150–300M / trên $500M | $100–200M / $300–600M / trên $1B | không có token / $200–500M / khoảng $1B |
| **Điểm** | 2.85 | 2.55 | 2.55 | **3.00** | 2.95 |

### 8.1 RISEx
- **Luận điểm:** tích hợp dọc giữa hạ tầng và ứng dụng: L2 tốc độ cao cộng orderbook. Đây là cách Hyperliquid làm, nhưng RISE làm trên Ethereum.
  - Có Galaxy, Vitalik, Stani đứng sau.
  - Mua lại BSX, một perp DEX trên Base với hơn $15B volume.
  - S1 vừa bắt đầu, phát cố định 200k points/tuần, mainnet có giới hạn truy cập. Ít đối thủ hơn so với farm công khai.
- **Rủi ro:**
  - Token nhiều khả năng là token của chain. Giá trị phụ thuộc vào việc chain có người dùng ngoài RISEx hay không.
  - Vốn gọi nhỏ, ảnh hưởng tới hỗ trợ market making và niêm yết.
  - TGE nhiều khả năng sau giữa năm 2027.
- **Ví dụ tính giá trị point** (giả định, minh họa):
  - S1 có khoảng 8–10M points.
  - Nếu S1 nhận 10% cung và FDV là $300M, mỗi point đáng khoảng $3–4.
  - Hãy thay tỷ lệ % và FDV thật khi dự án công bố.

### 8.2 TxFlow
- **Luận điểm:**
  - Câu chuyện "L1 riêng, không VC, không phân bổ cho nhà đầu tư" giống Hyperliquid, nên phần cộng đồng có thể lớn.
  - Doanh thu khoảng $21M/năm khi vẫn chỉ cho vào bằng mã mời, khá ấn tượng.
  - Hơn 150 cặp, gồm crypto, cổ phiếu, FX, pre-IPO.
  - Points chấm theo cả volume, OI, thời gian hoạt động, phí và TVL, nên khó wash hơn.
- **Rủi ro:**
  - Đội ngũ gần như ẩn danh, không có backer hỗ trợ niêm yết hay market making.
  - Token chưa được xác nhận.
  - Vol/OI ước tính khoảng 7x, tức volume farm nhiều.
  - Bảo mật và mức tập trung hóa của L1 chưa rõ.
- **Cách farm:** phân bổ nhỏ. Ưu tiên giữ OI có lý do kinh tế, đừng chạy volume vòng tròn, vì có thể bị trừ points hồi tố.

### 8.3 Bulk
- **Luận điểm:**
  - Kiến trúc mới: matching chạy ngay trong validator Solana (Bulk-Agave, plugin "Bulk Tile", BULKBFT), tick khoảng 20ms, độ trễ cố ý 25ms cho lệnh taker.
  - Có Anatoly và Wintermute đứng sau.
  - Farm ít công: chỉ cần gửi USDC (khoảng $27.5M pre-deposit tính đến 8/2026).
- **Rủi ro:**
  - Token perp trên Solana lịch sử yếu: FDV DRIFT hiện khoảng $10M, ZEX khoảng $1M.
  - Points nghiêng về cá voi.
  - Hệ thống chưa chạy thực tế ở quy mô lớn.
  - Vốn bị khóa, chi phí cơ hội khoảng 4–5% lãi USDC.
  - TGE nhiều khả năng giữa hoặc cuối 2027.
- **Cách farm:** chỉ dùng USDC nhàn rỗi. Tính lợi nhuận kỳ vọng so với lãi suất phi rủi ro.

### 8.4 Arcus
- **Luận điểm:**
  - Nguồn gốc dYdX, Robinhood đầu tư, có kênh phân phối hơn 27 triệu tài khoản Robinhood đã nạp tiền.
  - Cổ phiếu token hóa phát hành qua hạ tầng Robinhood.
  - Doanh thu khoảng $20M/năm chỉ sau khoảng 4 tháng.
  - Bắt buộc KYC nên ít sybil, phần chia cho user thật lớn hơn.
- **Rủi ro:**
  - Token phải chia cho cộng đồng dYdX (trader, staker, validator). Khi Arcus công bố, DYDX giảm 23%, cho thấy thị trường kỳ vọng giá trị dịch chuyển sang Arcus.
  - Không mở cho Mỹ, Anh, Canada.
  - Robinhood có thể ưu tiên sản phẩm của chính mình (xem P9).
- **Cách farm:** đây là new-gen mình đánh giá cao nhất về chất lượng. Phù hợp nếu bạn KYC được và ở vùng được phép.

### 8.5 QFEX
- **Luận điểm:**
  - Đội ngũ có lý lịch mạnh nhất nhóm new-gen (HFT).
  - OI tăng tự nhiên khi chưa có points: từ $90M lên $211M trong khoảng 3 tháng.
  - Không dùng oracle: lấy giá trực tiếp từ NYSE và Nasdaq, từ hợp đồng E-mini của CME cho chỉ số.
  - Tháng 9/2026, CEO viết bài ủng hộ việc airdrop token chưa vesting cho user sớm nhất.
- **Rủi ro:**
  - Đây là **sàn tập trung**, không phải DEX.
  - Token có thể không bao giờ ra, hoặc ưu tiên cổ phần.
  - Bắt buộc KYC.
  - Cạnh tranh trực tiếp với HIP-3 (trade[XYZ]), Variational, Arcus, Ondo perps.
- **Cách farm:** chỉ giao dịch "hữu cơ" khi bạn thật sự cần hedge TradFi hoặc trade cuối tuần. Đừng tạo volume giả cho một chương trình chưa tồn tại.

---

## 9. Xếp hạng và phân bổ

**Xếp hạng chất lượng (scorecard):**
1. Variational 3.70
2. Arcus 3.00
3. QFEX 2.95
4. RISEx 2.85
5. TxFlow 2.55 và Bulk 2.55 (ngang nhau)
6. Extended 2.50

**Độ hấp dẫn để farm ngay lúc này** (cân nhắc giá trị kỳ vọng so với chi phí, mức sớm, cạnh tranh):
1. **Variational:** farm đến TGE, nhưng chỉ khi chi phí mỗi point dưới khoảng $17–20.
2. **Arcus:** S1 còn sớm, có KYC, có Robinhood và dYdX đứng sau. Điểm trừ là phải chia token với cộng đồng dYdX.
3. **RISEx:** S1 còn sớm, phát cố định 200k/tuần, truy cập có giới hạn. Chấp nhận chờ đến năm 2027.
4. **TxFlow:** rủi ro cao, nhưng points chấm nhiều chiều và không có phần cho VC.
5. **Bulk:** gửi USDC tiện, nhưng nghiêng về cá voi và khóa vốn.
6. **QFEX:** chưa có points, chỉ nên giao dịch hữu cơ.

Extended: đã hết farm. Việc còn lại là ký điều khoản, hedge, và bán theo pattern.

**Gợi ý theo quy mô vốn:**
- **Vốn nhỏ (khoảng $5–10K, như kế hoạch 7K trước đó):**
  - Tối đa 2 sàn: Variational đến TGE, cộng một new-gen (Arcus hoặc RISEx).
  - Không khóa vốn vào farm kiểu gửi tiền.
  - Dùng đòn bẩy thấp. Volume chỉ nên đến từ lệnh có lý do.
- **Vốn vừa hoặc lớn:** thêm Bulk (bằng USDC nhàn rỗi) và TxFlow (phân bổ nhỏ). Giao dịch hữu cơ ở QFEX.

---

## 10. Checklist và công cụ

- [ ] **Extended:** ký Community Distribution Terms trước **31/12/2026, 23:59 UTC**. Nếu dùng Starknet, chỉ định ví EVM (Arc).
- [ ] **Variational:** ký điều khoản claim khi mở. Token không claim sẽ bị burn.
- [ ] Theo dõi ladder Polymarket hằng tuần bằng lệnh `python3 research/perp-dex-tge/tools/polymarket_fdv_ladder.py <slug> 14 <P_launch>`. Các slug:
  - `variational-fdv-above-one-day-after-launch`
  - `extended-fdv-above-one-day-after-launch`
  - `qfex-fdv-above-one-day-after-launch`
- [ ] Theo dõi Vol/OI và xu hướng OI 30 ngày trên Castle Labs. Cảnh báo khi OI giảm hơn 30% lúc points giảm.
- [ ] Lịch cliff:
  - LIT khoảng 27/12/2026 đến 28/1/2027
  - BP và EDGE khoảng 3/2027
  - GRVT khoảng 7/2027
- [ ] Hẹn xem lại token mới TGE ở mốc D60–D110, tức cửa sổ đáy lịch sử.
- Đã có sẵn trong repo: dashboard "VAR · EXT TGE Watch" (`var-ext-tracker/`), cập nhật FDV kỳ vọng D+1 hằng ngày.

---

## 11. Giới hạn của phân tích

- **Mẫu nhỏ:** chỉ 5 perp có kèo Polymarket để hiệu chỉnh, và 4–7 token để rút pattern sau TGE.
- **Nguồn thứ cấp:** nhiều số liệu lấy từ báo hoặc aggregator, có chỗ mâu thuẫn. Ví dụ: vốn của GRVT, tổng points của Extended (ước tính cộng đồng), "0% insider" của BP.
- **Thiếu dữ liệu phí/doanh thu:** DefiLlama không theo dõi doanh thu của Variational, GRVT, Backpack, QFEX. Phí trước TGE của Lighter và HYPE bị thiếu.
- **Scorecard và FDV:** điểm do mình chấm. Bảng retro có thiên lệch hindsight. Các khoảng FDV là kịch bản, không phải dự báo điểm.
- **Thời điểm số liệu:** giá và Polymarket là ảnh chụp ngày 18/11/2026 và thay đổi liên tục.

---

## Nguồn

**Dữ liệu thị trường**
- Polymarket (gamma API và lịch sử giá CLOB), các event:
  - [Lighter FDV 2025](https://polymarket.com/event/lighter-market-cap-fdv-one-day-after-launch), [Lighter FDV 2026](https://polymarket.com/event/lighter-fdv-above-one-day-after-launch)
  - [edgeX FDV](https://polymarket.com/event/edgex-fdv-above-one-day-after-launch), [Paradex FDV](https://polymarket.com/event/paradex-fdv-above-one-day-after-launch), [Backpack FDV](https://polymarket.com/event/backpack-fdv-above-one-day-after-launch), [GRVT FDV](https://polymarket.com/event/grvt-fdv-above-one-day-after-launch)
  - [Extended FDV](https://polymarket.com/event/extended-fdv-above-one-day-after-launch), [Variational FDV](https://polymarket.com/event/variational-fdv-above-one-day-after-launch), [QFEX FDV](https://polymarket.com/event/qfex-fdv-above-one-day-after-launch)
  - [RISE launch](https://polymarket.com/event/will-rise-launch-a-token-by), [RISEx launch](https://polymarket.com/event/will-risex-launch-a-token-by-20260708174012702), [BULK launch](https://polymarket.com/event/will-bulk-launch-a-token-by)
  - [Monad FDV](https://polymarket.com/event/monad-market-cap-fdv-one-day-after-launch), [MegaETH FDV](https://polymarket.com/event/megaeth-market-cap-fdv-one-day-after-launch)
- CoinGecko API: giá, FDV, ATH/ATL, lịch sử 365 ngày.
- DefiLlama API: [phí](https://api.llama.fi/overview/fees), [OI](https://api.llama.fi/overview/open-interest).
- [Castle Labs: Perp DEX rankings (17/11/2026)](https://castlelabs.io/research/perp-dex-rankings).

**Hyperliquid và Aster**
- [The Block: HYPE crosses $4B FDV](https://www.theblock.co/post/328769/hyperliquid-airdrops-over-1-2-billion-worth-of-tokens-to-users-as-hype-crosses-4-billion-fdv)
- [The Block: HL OI $14.3B, HYPE ATH (9/2026)](https://www.theblock.co/news/ecosystems/2026-09-08-hyperliquid-open-interest-climbs-14-3-billion-hype-hits-all-time-high-413855)
- [The Block: Aster TGE countdown](https://www.theblock.co/post/369813/asters-next-era-begins-airdrop-points-stage-2-live-tge-countdown-begins)
- [finanzen.net: ASTER first-day rally](https://www.finanzen.net/nachricht/aktien/backed-by-cz-aster-token-ignites-with-1-650-first-day-rally-14858686)

**Lighter**
- [KuCoin: LIT 25% airdrop](https://www.kucoin.com/news/flash/lighter-debuts-lit-token-with-a-25-community-airdrop)
- [Yahoo/CoinDesk: LIT and $3B FDV](https://finance.yahoo.com/news/traders-split-over-whether-lighter-095119926.html)
- [The Block: Lighter raises $68M at $1.5B](https://www.theblock.co/post/378358/lighter-raises-68-million-1-5-billion-valuation-vc-bets-flood-perp-dex-infrastructure-report)
- [CryptoTimes: LIT buybacks (6/2026)](https://www.cryptotimes.io/2026/06/30/why-lighter-lit-surged-25-this-week-buybacks-50m-trading-volume-more/)
- [KuCoin: Robinhood chọn Bitstamp, LIT −20%](https://www.kucoin.com/news/flash/lighter-s-token-dips-20-as-robinhood-announces-bitstamp-futures-expansion)

**edgeX**
- [The Defiant: edgeX TGE 31/3](https://thedefiant.io/news/defi/amber-group-backed-perp-dex-edgex-to-launch-token-on-march-31)
- [crypto.news: transparency concerns](https://crypto.news/edgex-set-to-launch-edge-token-amid-transparency-concerns/)
- [Cointelegraph: EDGE crash, ZachXBT](https://cointelegraph.com/news/edgex-blames-external-party-for-token-crash-as-zachxbt-points-to-insider-manipulation)

**Paradex**
- [Phemex: DIME $43M FDV](https://phemex.com/news/article/paradex-launches-dime-token-with-43-million-fdv-65097)
- [Decrypt: Paradex DIME TGE](https://decrypt.co/359780)

**Backpack**
- [KuCoin: BP TGE 23/3/2026](https://www.kucoin.com/news/flash/backpack-to-launch-bp-token-tge-on-march-23-2026)
- [KuCoin: BP TGE amid bear market](https://www.kucoin.com/news/flash/backpack-launches-bp-token-tge-amid-bear-market)
- [CryptoBriefing: BP and SpaceX stock](https://cryptobriefing.com/backpack-bp-token-surges-spacex-stock/)
- [Bloomingbit: CFTC approval, BP +42%](https://en.bloomingbit.io/feed/news/124591)

**GRVT**
- [The Block: GRVT 28% community](https://www.theblock.co/post/393389/)
- [KuCoin: GRVT TGE 30/7](https://www.kucoin.com/news/flash/grvt-announces-tge-details-grvt-airdrop-claims-open-on-july-30)

**Extended**
- [AirdropAlert: XTEN tokenomics](https://airdropalert.com/blogs/xten-tokenomics/)
- [KuCoin: XTEN tokenomics](https://www.kucoin.com/news/flash/extended-reveals-xten-tokenomics-30-airdropped-at-tge)
- [FinanceFeeds: Extended](https://financefeeds.com/extended-token-stirs-fierce-speculation/)
- [CryptoRank: XTEN pre-market](https://cryptorank.io/price/x-10)
- [Coinglass: XTEN](https://www.coinglass.com/currencies/XTEN)
- [Orbit airdrop calendar](https://orbitperpscreener.com/airdrop-calendar)

**Variational**
- [Datawallet: Variational explained](https://www.datawallet.com/crypto/variational-explained)
- [Alea Research: Only Hyperliquid traded more](https://alearesearch.substack.com/p/only-hyperliquid-traded-more-then)
- [Pulse 2.0: $50M Series A](https://pulse2.com/variational-about-50-million-raised-for-on-chain-derivatives-trading-protocol)
- [KuCoin: VAR valuation estimates](https://www.kucoin.com/news/flash/variational-reveals-airdrop-details-var-token-valuation-estimated-at-1-53b-1-85b)

**RISEx**
- [CryptoBriefing: Ignite S1](https://cryptobriefing.com/risex-launches-ignite-season-1-points-program-following-3b-in-volume-during-the-early-access-phase/)
- [Decrypt: RISE $8M, Galaxy](https://decrypt.co/324190/galaxy-ventures-backs-rise-chain-8m-raised-to-launch-fastest-zone-for-real-time-apps-on-ethereum)
- [Decrypt: RISE acquires BSX](https://decrypt.co/348127/rise-acquires-bsx-a-perp-dex-on-base-to-accelerate-development-of-the-first-integrated-orderbooks)

**TxFlow**
- [airdrop.promo: TxFlow](https://airdrop.promo/airdrops/txflow/)
- [BitDegree: TxFlow review](https://www.bitdegree.org/crypto/txflow-review)
- [Cointelegraph PR: TxFlow L1 mainnet](https://cointelegraph.com/press-releases/txflow-l1-mainnet-launch-marks-a-new-phase-for-multi-application-on-chain-finance)
- [CoinLaunch: TxFlow](https://coinlaunch.space/projects/txflow/)

**Bulk**
- [DeFi Secret: Bulk review](https://defisecret.com/bulk-trade-review-solana-perps-aura-points/)

**Arcus**
- [CoinCodeCap: Arcus review](https://coincodecap.com/arcus-review-24-7-stock-token-perps-dex-from-the-dydx-team)
- [AirdropMeta: Arcus](https://www.airdropmeta.com/projects/arcus)
- [Cointelegraph: Arcus debut](https://cointelegraph.com/news/robinhood-backed-dex-arcus-debut-multi-asset-trading)

**QFEX**
- [Four Pillars: QFEX, FTX without the fraud](https://research.4pillars.io/en/research/qfex-ftx-without-the-fraud) (bài được QFEX tài trợ)
- [Phemex: QFEX $9.5M seed](https://phemex.com/news/article/qfex-secures-95m-seed-funding-led-by-general-catalyst-64490)
- [CoinLaunch: QFEX airdrop](https://coinlaunch.space/events-contests/qfex-airdrop-retrodrop/)

**Trong repo này:** ghi chú `research_notes/Chiến lược 7K cho nhịp pump/hype_lit_kntq_variational.md` (17/10/2026), dùng cho cliff LIT, buyback LIT và Polymarket VAR tháng 10; mô hình hiệu chỉnh trong `var-ext-tracker/collect.py`.
