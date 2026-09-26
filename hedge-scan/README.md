# hedge-scan · chọn cặp TradFi hedge VAR ↔ EXT rẻ nhất

Tool CLI nhỏ (Python 3.8+, chỉ dùng thư viện chuẩn) để chọn cặp TradFi nào nên mở hedge delta-neutral giữa
**Variational Omni** và **Extended** ngay lúc này, tối ưu **chi phí trên mỗi point**. Tool chỉ gọi API public, không cần key.

```bash
python3 hedge-scan/scan.py                          # top 10, $15k/chân, giữ 8h
python3 hedge-scan/scan.py --size 20000 --hold 24   # đổi size mỗi chân / thời gian giữ
python3 hedge-scan/scan.py --only AAPL,TSLA,XAG     # chỉ xét vài mã (ticker Variational)
python3 hedge-scan/scan.py --all                    # hiện cả cặp đang không giao dịch được
python3 hedge-scan/scan.py --exit AAPL:short-var    # đang SHORT VAR/LONG EXT: đóng bây giờ tốn bao nhiêu?
python3 hedge-scan/scan.py --json                   # xuất JSON
python3 hedge-scan/scan.py --log spreads.csv        # ghi snapshot để tự thống kê giờ nào rẻ nhất
```

## Tool tính gì

Với mỗi cặp cùng tài sản trên 2 sàn (vd `AAPL` ↔ `AAPL_24_5-USD`, `BZ` ↔ `XBR-USD`, `CL` ↔ `WTI-USD`), ở size `N` mỗi chân:

| Thành phần | Nguồn | Cách tính |
|---|---|---|
| Spread VAR (mở+đóng) | `metadata/stats`: quote base / $1k / $100k / $1M | Nội suy giá ask/bid tại `N` (xem "Giả định") |
| Spread EXT (mở+đóng) | orderbook `/info/markets/{m}/orderbook` | Đi sổ lệnh đủ `N` cho cả 2 phía |
| Phí EXT | Docs Extended | Taker RWA 0.010% × 2 (RFQ luôn tính taker; sổ lệnh có thể maker 0%) |
| Phí VAR | Docs Variational | 0 — VAR ăn phần spread |
| Funding | VAR: `funding_rate` (APR); EXT: TB 8 lần trả gần nhất (theo giờ) | Chọn chiều nhận funding, nhân thời gian giữ |
| Points | `config.json` | `2 × N` volume VAR (mở+đóng) × pts/$1M × (1+boost) |

`$/pt = (spread VAR + spread EXT + phí − funding nhận) × N / points`. Xếp hạng theo `$/pt`, cặp có cảnh báo biến động bị đẩy xuống,
cặp không giao dịch được (EXT đóng cửa, vượt max lệnh, sát trần OI RFQ, quote VAR cũ, sổ mỏng) bị bỏ ra.

**Chiều lệnh**: nếu chênh funding giữa 2 chiều ≥ 0.25 bps trong thời gian giữ → chọn chiều nhận funding (long ở sàn funding âm,
short ở sàn funding dương). Nếu không → chọn chiều vào lệnh rẻ hơn ngay lúc này (basis giữa 2 sàn + skew quote của VAR).

**Basis** = giá mid VAR − mid EXT. Chi phí trọn vòng không phụ thuộc basis nếu basis giữ nguyên, nhưng basis thường co giãn:
vào lệnh theo chiều có lợi, rồi dùng `--exit` để đóng khi basis đảo chiều → đó là phần "spread arbitrage".

## Phân tích (research 26/09/2026)

**Cấu trúc chi phí 2 sàn**
- Variational: 0 phí, toàn bộ chi phí nằm ở spread OLP. Spread tăng theo size: AAPL cuối tuần ≈ 4 bps round-trip ở $1k,
  ≈ 8–9 bps ở $15k, ≈ 15 bps ở $100k. Quote có thể cache tới 600s (tool báo tuổi quote).
- Extended: phí RWA taker 0.010%, maker 0%. Cổ phiếu phần lớn là **RFQ** (sổ lệnh chỉ mang tính tham khảo, lệnh bạn đặt
  luôn tính taker). Vàng, bạc, dầu, SPX, NDX, NVDA, MSTR, MU, SNDK, EUR, JPY là **sổ lệnh thật** → có thể đặt limit maker 0 phí.
- Funding: TradFi trên VAR có lãi suất 0%, chu kỳ 8h (cổ phiếu) / 4h (hàng hoá); EXT trả mỗi giờ.
  Funding thường chỉ vài bps / 8h → là yếu tố phụ, trừ khi lệch mạnh (vd CRCL trên VAR có lúc ~38% APR).

**Kết luận thực tế**
1. **Giờ giao dịch là yếu tố lớn nhất.** Cuối tuần/ngoài phiên, spread cổ phiếu trên VAR rộng ~4–6 bps ở size nhỏ
   (so với ~0.8 bps của AAPL trong phiên chính, theo bài bạn chia sẻ). Farm cổ phiếu trong **phiên chính Mỹ 20:30–03:00 giờ VN**
   (mùa đông 21:30–04:00), tránh 15 phút đầu/cuối phiên và giờ ra tin (CPI, FOMC, earnings).
2. **Size nhỏ rẻ hơn trên mỗi point.** Points tỉ lệ thuận với volume nhưng spread VAR tăng theo size: AAPL 10k ≈ 12.5 bps,
   20k ≈ 17.6 bps (cuối tuần). Với cổ phiếu, 10k là điểm ngọt; chia nhỏ lệnh nếu quote UI xấu.
   Vàng/bạc/dầu thì spread gần như không đổi theo size → dùng size lớn được.
3. **Hàng hoá sổ lệnh (XAU, XAG, WTI/CL, XBR/BZ) thường rẻ nhất**: sổ EXT dày (0.2–4 bps round-trip), mở 24/5 (WTI cả cuối tuần), có thể
   maker 0 phí bên EXT. XAG và BZ nằm trong list 50 pts/$1M đã xác minh.
4. **Cổ phiếu trong list (AAPL, TSLA, MSFT, AMZN, MSTR)**: snapshot cuối tuần ở $15k: AAPL/TSLA ≈ 15 bps, MSFT ≈ 24,
   AMZN/MSTR ≈ 29 → AAPL/TSLA rẻ nhất, các mã còn lại đắt gấp ~1.6–2 lần do spread VAR theo size và sổ EXT mỏng hơn.
5. **Tránh**: cặp VAR volume < $50k/ngày, cặp RFQ sát trần OI (EXT chuyển reduce-only, kẹt không mở/đóng được),
   lúc biến động mạnh (tool gắn cờ khi σ 30 phút gần nhất ≥ 2× trung bình 24h).

## Giả định & giới hạn

- **Spread VAR ở 10–20k là ước tính.** API public chỉ có quote $1k và $100k; API quote đúng size của Omni nằm sau
  Cloudflare. Tool nội suy phần tăng thêm theo `((N−1k)/(99k))^0.6` (`var_size_curve_exp`). Luôn so với quote thật trên UI
  Omni trước khi bấm; nếu UI luôn xấu/tốt hơn, chỉnh `var_size_curve_exp` (lớn hơn = lạc quan hơn, 1.0 = tuyến tính).
- **Points/$1M**: chỉ 7 mã có số liệu từ bạn bè (★, 50 pts/$1M). Các mã khác mặc định 50 và bị đánh dấu "chưa xác minh".
  Cập nhật `var_points_per_m` trong `config.json` từ lịch sử points của bạn. Nếu có boost (tier/referral) thì sửa `points_boost`
  (vd 0.15). Points Extended chưa công bố tỉ lệ → `ext_points_per_m` = 0.
- Funding là ước tính từ tỉ lệ hiện tại / TB 8h; thực tế thay đổi mỗi giờ.
- Giờ nghỉ lễ Mỹ không được tính; tool dựa vào cờ `isOffHours` của Extended để biết sàn có mở không.
- Không tính rủi ro lệch chân khi vào 2 lệnh không cùng lúc (tool chỉ báo ước lượng `rủi ro lệch chân` theo σ 5 phút).

## config.json

| Khoá | Ý nghĩa |
|---|---|
| `size_usd`, `hold_hours`, `top` | Mặc định cho `--size`, `--hold`, `--top` |
| `var_points_per_m`, `var_points_default`, `points_boost`, `ext_points_per_m` | Mô hình points |
| `ext_taker_fee`, `ext_maker_fee` | Phí RWA Extended (0.0001 = 0.01%) |
| `var_size_curve_exp` | Độ cong nội suy spread VAR theo size |
| `leg_delay_s` | Thời gian dự kiến giữa 2 lệnh, để ước lượng rủi ro lệch chân |
| `aliases`, `proxies` | Map ticker EXT → VAR (proxy = tài sản khác nhưng tương quan, vd SPX500m ↔ US500) |
| `max_price_diff` | Lệch giá tối đa để coi là cùng tài sản (loại các mã trùng tên khác công ty) |
| `max_quote_age_s`, `min_var_volume_24h`, `vol_spike_ratio` | Ngưỡng cảnh báo |
| `exclude` | Mã không muốn xét |

Không phải lời khuyên đầu tư.
