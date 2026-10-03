# Gom KNTQ vùng 0.267–0.288, thoát trước 27/11

**Chốt trước: có vào, nhưng không vào ở giá hiện tại.** KNTQ đang ở **$0.3030** (HyperCore `@334` mid, 2026-10-03 23:45 UTC), cao hơn **+15.94%** so với giá claim thực tế **0.261331 USDC** mà contract đang chào bán cho 3.000+ ví có kPoints tới 11/10 ([api.hyperliquid.xyz/info](https://api.hyperliquid.xyz/info); [rpc.purroofgroup.com](https://rpc.purroofgroup.com)). **0.26 không phải đáy — nó là nam châm và là vùng cost basis, không phải sàn có bid đỡ.** Đáy cục bộ thật mà dữ liệu chống lưng là **band bid có tiền thật của whale `0xaf0fdd39…1e92e`: 0.2666–0.28656 (399.961 KNTQ, ~$110k)**, cộng stack bid tổng ~4,9M KNTQ (~$1,33M) giữa 0.25–0.30. Mặt tốt: áp lực bán cơ học phần lớn đã xong — **44,09% pool đã claim (22.046.576 KNTQ / 3.059 ví / $5.761.454)** nhưng 38,6% rơi vào 12 giờ đầu, tốc độ claim đã giảm ~93%, bridge EVM→HyperCore rớt về **44k KNTQ/giờ** so với baseline trước claim 132k/giờ, và **~10–11M KNTQ token đã claim đã bị bán xong (≈$3,0–3,3M)** mà giá vẫn đóng ngày 3/10 gần đỉnh ngày. Mặt xấu: nội tại đang **giảm trên trục quan trọng nhất** — HYPE staked rớt từ 50,07M đỉnh xuống **12,47M (−75%)** và vẫn giảm đơn điệu, trong khi doanh thu tăng gấp đôi chỉ nhờ take rate một lần (fee switch 9/4/2026), không nhờ volume; **FDV/Revenue = 61,8x**; và — phát hiện mới nhất, đo lúc 2026-10-03 23:42 UTC — **660.000.000 KNTQ = 66% total supply đang nằm trong 5 ví EOA thuần, không một vesting contract hay timelock nào**, nên "cliff 27/11" là **lời hứa trong docs, không phải cơ chế**: rủi ro cung là **liên tục**, không phải một sự kiện có ngày. Kế hoạch: rải lệnh 0.262–0.295 trước deadline (70% vị thế), thêm 20% sau 11/10 nếu giữ được 0.29, **cắt nếu đóng ngày dưới 0.2550**, chốt dần 0.335–0.377, và **giảm về ≤25% vị thế trước 20/11** — hoặc ngay lập tức nếu ví team/investor có bất kỳ lệnh chuyển ra nào.

*(Báo cáo viết 2026-10-03 ~23:55 UTC = 2026-10-04 ~06:55 giờ VN. Deadline claim: **2026-10-11 12:00 UTC = 19:00 giờ VN ngày 11/10**.)*

---

## 1. Kết luận & khuyến nghị: mua dưới 0.288, không mua trên 0.30 trước 11/10

**Verdict: CÓ vào hàng, với size vừa, theo thang lệnh, và có ngày thoát định trước.** Đây không phải kèo "mua và giữ" — đây là kèo giao dịch một sự kiện cung cầu có lịch rõ ràng (overhang claim hết hạn 11/10 → Elysium mainnet 20/10) trên một token có nội tại đang xấu dần ở trục cốt lõi, và trong đó **66% supply nằm ở 5 ví EOA không bị code nào ràng buộc** — tức rủi ro cung không có ngày hẹn, nó mở suốt. Chính điều đó là lý do mạnh nhất để coi đây là trade có horizon xác định chứ không phải vị thế giữ qua tháng 11.

**Vùng giá và chia lệnh** (% của vị thế dự kiến, không phải % tài khoản):

| Lệnh | Vùng giá | % vị thế | Thời điểm | Lý do |
|---|---|---|---|---|
| L1 | **0.2880–0.2950** | 20% | bất kỳ lúc nào trước 11/10 | đáy sàn ngày 2–3/10 (0.287) và đáy ngày 3/10 (0.2949); premium còn 10–13% |
| L2 | **0.2700–0.2880** | 30% | dip trong 48h cuối trước deadline | trùng band bid có fund của whale (0.2666–0.28656) + đáy crash 1/10 (0.27778) |
| L3 | **0.2620–0.2700** | 20% | chỉ nếu có flush do claim-rush | ngay trên giá claim; dưới 0.2613 nguồn cung claim tự tắt |
| L4 | **0.2900–0.3150** | 20% | **sau 19:00 VN 11/10**, nếu giữ ≥0.29 và bridge-in <130k/h | trả giá cho việc overhang biến mất, trước Elysium 20/10 |
| Dự phòng | — | 10% | dip "sell-the-news" sau 20/10 hoặc sau FOMC 28/10 | |

Nếu L1–L3 lấp hết, giá vốn ~**0.284**. Nếu chỉ L1+L4 lấp, ~**0.297** — vẫn tốt hơn mua spot bây giờ.

**Điều kiện huỷ kèo (invalidation), theo thứ tự nghiêm ngặt:**
- **Cắt toàn bộ: đóng nến ngày dưới 0.2550.** Đây là dưới đáy 2026-09-19 (0.25553) — lần cuối KNTQ giao dịch dưới giá claim. Mất mốc này là mất cả nền 16 nến ngày đóng trên 0.26 kể từ 18/9, mở lại vùng 0.19–0.20 ([api.hyperliquid.xyz/info](https://api.hyperliquid.xyz/info)). Từ giá vốn 0.284 đó là −10,2%.
- **Ngừng gom (không bình quân tiếp quá L3): mất 0.2778 trên nến ngày** trước 11/10 → nghĩa là cung claimant đang đè hết bid, không phải chỉ arbitrage.
- **Cắt ngay lập tức, không chờ giá: bất kỳ lệnh chuyển KNTQ ra khỏi ví team `0x373e0b6b…d90e` (235M) hoặc ví investor `0x9ef3b3a4…a1a2` (75M).** Hai ví này là EOA, số dư nguyên si 10 tháng; một lệnh chuyển ra là sự kiện on-chain bearish nhất KNTQ có thể tạo ra, và nó đi trước lệnh nạp sàn vài phút tới vài giờ. Tracker đã canh sẵn (mục 8).
- **Huỷ luận điểm cơ bản:** Elysium mainnet trượt qua 31/10; hoặc Elysium ra mà HYPE staked tiếp tục xuống dưới ~11M; hoặc kHYPE TVL mất mốc $900M.
- **Ngày thoái bắt buộc: giảm về ≤25% vị thế trước 2026-11-20**, trừ khi lúc đó đã có tín hiệu mới cụ thể (Elysium có doanh thu đo được, HYPE staked tạo đáy hai tháng liên tiếp, hoặc listing tier-1). Lưu ý mốc này là **quy ước quản trị rủi ro của riêng ta, không phải mốc do cơ chế on-chain áp đặt** — vì không có vesting contract nào, 27/11 không có gì đặc biệt về mặt kỹ thuật.

**Mục tiêu chốt:** T1 **0.335–0.3525** (đỉnh 22–23/9 và đỉnh 2/10 là 0.3415) chốt 1/3; T2 **0.368–0.377** (đỉnh hồi 1/10 + đỉnh tháng 6; **đúng nơi whale `0xaf0f…` bắt đầu ladder bán 898.049 KNTQ từ 0.36805 tới 0.442**) chốt 1/3 nữa; T3 **0.40–0.452** chỉ trail phần còn lại.

**Những gì KHÔNG nên làm:** không FOMO vùng 0.30+ trước 11/10 (contract đang chào 27,95M token ở 0.2613 cho một nhóm ví có thể undercut bạn bất cứ lúc nào); không dùng market order trên ~$30–50k (depth ±2% chỉ $12,1k bid / $22,6k ask); không cố hedge bằng perp (không tồn tại, xem mục 9); không mua "suất claim" từ người khác (allocation là Merkle gắn ví, không chuyển nhượng); không vào `kntq-claim.vercel.app` (tên giả — official là **kinetiq.xyz/kntq**); không giữ qua 27/11 theo quán tính.

---

## 2. Doanh thu tăng gấp đôi nhưng HYPE staked mất 75%: trục nào quan trọng hơn

Kinetiq là protocol liquid staking thống trị hệ Hyperliquid: kHYPE $1.020,6M trên tổng ~$1.295,8M TVL của cả category LST, tức **78,8%**, và cả nhà Kinetiq (kHYPE + kmHYPE + Launch) là **82,9%** — gấp ~5x đối thủ số 2 stHYPE ($204,7M) ([api.llama.fi/protocols](https://api.llama.fi/protocols)). Nhưng thị phần đứng yên ở 83–84% suốt sáu tháng **không phải vì Kinetiq thắng, mà vì cả category co lại cùng nhau**: tổng HYPE trong các LST đi từ 30,4M xuống 14,45M (−52%) trong cùng kỳ.

Đây là con số quyết định: **HYPE staked qua Kinetiq rớt từ đỉnh 50.068.715 (4/10/2025) xuống 29.687.124 lúc TGE (27/11/2025) xuống 12.470.331 ngày 3/10/2026** — **−16,8% trong 30 ngày, −22,8% trong 90 ngày, −42,8% trong 180 ngày, −58,0% kể từ TGE, −75,1% so với đỉnh**, và giảm đơn điệu từng tháng không có một quý nào đảo chiều ([api.llama.fi/protocol/kinetiq](https://api.llama.fi/protocol/kinetiq)). TVL tính bằng USD nhìn phẳng (~$1,11B) chỉ vì giá HYPE tăng. Riêng tuần gần nhất kHYPE mất **−11,1% TVL trong 7 ngày** trong khi HYPE chỉ −4,5% — tức là dòng vốn thật sự rút ra, không phải hiệu ứng giá.

Phía đối diện là chuỗi dữ liệu duy nhất thật sự tích cực: **doanh thu Kinetiq đi từ $199.782 (tháng 4/2026) lên $410.597 (tháng 9/2026), +105,5%**, annualize ~**$4,91M** ([api.llama.fi/summary/fees/kinetiq](https://api.llama.fi/summary/fees/kinetiq)). Nhưng bóc ra thì **gross fees phẳng ở $1,9–2,1M/tháng suốt 2026 — toàn bộ tăng trưởng doanh thu đến từ take rate và mix, không một đồng nào từ volume.** Fee switch ngày 9/4/2026 là một bước nhảy một lần từ ~0% lên 10% performance fee trên staking rewards; nó không lặp lại được. Và cái 10% đó đánh trên một base đang teo: pool staking yield là ~2,18% APR × 12,47M HYPE ≈ 272k HYPE/năm ≈ **$24,3M/năm**, khớp gần như chính xác với gross fees annualized $25,81M của DefiLlama — một cross-check tốt rằng số liệu là thật, và cũng là lời nhắc rằng doanh thu LST giảm 1:1 theo số HYPE staked nếu giá HYPE không bù lại.

**Trả lời thẳng: HYPE staked quan trọng hơn.** Doanh thu là đạo hàm của nó cộng một hệ số take rate đã dùng hết room; HYPE staked là base. Chân đỡ thứ hai thật sự duy nhất là **builder-code fees của Markets by Kinetiq: $157.774/30 ngày, biên 100%, chiếm 39% doanh thu**, chạy trên ~$5,11M/ngày volume HIP-3 — và chân này mong manh: **19 trong 24 market của `mkts` đã delisted, toàn bộ 23 market của `km` delisted**, HIP-3 nói chung rớt từ ~48% volume Hyperliquid lúc đỉnh xuống ~30% đầu tháng 9, và **>90% open interest HIP-3 nằm ở một deployer duy nhất (TradeXYZ)** ([api.hyperliquid.xyz/info](https://api.hyperliquid.xyz/info); [FinanceFeeds](https://financefeeds.com/hyperliquid-hip-3-explained/)). Kinetiq Earn còn tệ hơn: vault vkHYPE **lỗ −$68.963 yield trong 30 ngày**, và Kinetiq Launch tạo ra $865 doanh thu trong 30 ngày.

Valuation vì vậy chỉ đẹp nếu chọn mẫu số dễ: **mcap/Revenue 17,3x** (rẻ hơn Jito 39,8x, Hyperliquid 29,0x) nhưng **FDV/Revenue 61,8x** và **mcap/Holders-Revenue 47,9x** so với Lido 14,2x; mcap/TVL 0,0792 là **5,4x của Lido (0,0146)** — và Lido rẻ hơn trên *mọi* multiple doanh thu ([api.coingecko.com/api/v3/coins/kinetiq](https://api.coingecko.com/api/v3/coins/kinetiq); [api.llama.fi/protocols](https://api.llama.fi/protocols)). Với 72% supply chưa lưu hành và cliff 31% sau 55 ngày, **FDV là mẫu số trung thực**, và ở FDV doanh thu phải ×3,6 lên ~$17,5M/năm mới về mức 10x của Lido tại giá hiện tại. KIP-5 (~15/9/2026) còn lấy đi quyền dòng tiền duy nhất của holder: buyback giờ chảy 100% vào Hyperliquid Assistance Fund thay vì trả cho sKNTQ, nên **KNTQ thành token governance + supply sink thuần** — trong khi trang KNTQ chính chủ vẫn còn quảng cáo mô hình cũ ("distributed to stakers"), một vấn đề công bố thông tin nên tự nó là lý do để không tin các claim "real yield" từ marketing ([kinetiq.xyz/docs/kntq](https://kinetiq.xyz/docs/kntq); [kinetiq.xyz/kntq](https://kinetiq.xyz/kntq)).

Điểm cộng thật, ít được nhắc: **15 tháng, TVL $1–2,6B, 8 audit từ 5 hãng, không một vụ exploit nào** (mảng `hacks` của DefiLlama trống), và cơ chế redemption còn nguyên — NAV kHYPE hiện ~1,064 HYPE/kHYPE. Vụ depeg kHYPE về 0,8802 (24–27/9/2025) là sự kiện thanh khoản tiền-TGE, không phải mất khả năng chi trả. Nhưng **audit mới nhất là 15/1/2026 — Elysium (mainnet 20/10) và cả contract claim S2 đều chưa có audit công bố.**

---

## 3. Ai đang mua, ai đang bán: whale đã ngừng mua, claimant đã bán gần xong

Điểm quan trọng nhất của mục này: **tính tới 23:50 UTC 3/10, cả hai người mua lớn đã biết mặt đều đứng im.**

### Bên mua

| Ví | Vai trò | Số liệu đã verify | Trạng thái hiện tại |
|---|---|---|---|
| `0xaf0fdd39…1e92e` | whale gom chính | 30 ngày: mua **5.612.051 KNTQ / $1.577.638 (avg ~$0.281)**, bán 485.583 @ ~$0.430 → **net +5,1M**. Bridge vào 10.662.466 KNTQ ngày 28/9 22:02 UTC (~$3,25M). Riêng 1–3/10 mua thêm 2.678.281. Claim S2 167.982 KNTQ. Giữ 18,48–18,67M trên HyperCore | **Không một fill, không một TWAP slice nào từ 12:00 UTC 3/10.** Ladder treo nguyên: **19 bid / 399.961 KNTQ ở 0.2666–0.28656 (~$110k)** và **55 ask / 898.049 KNTQ ở 0.36805–0.442 (~$369k)** |
| `0x58f0bf43…0d20` | TWAP buyer | TWAP **1.093.492 KNTQ trong 2.000 slice ngày 1/10, 05:03–18:52 UTC** (2.000 là trần API nên có thể nhiều hơn) + 69.090 market fill ngay trong cú crash 12:38–12:39. Giữ 1,50M | **Zero hoạt động từ 12:00 UTC 3/10** |
| `0xbf66cb8b…f913` | giống market maker | 2/10 15:34 → 3/10 12:09: 7.304 fill, mua 3.083.639 ($911k) / bán 2.739.645 ($809k), net +344k. Giữ 2,88M | Quote hai chiều: 561k bid ở 0.2718–0.3031, 528k ask ở 0.3036–0.3327 |
| `0xaa3b7392…b6e2` | bot buyback protocol | 389 transfer, 436.730 KNTQ (~$118,7k) từ 17/9 07:05 → 3/10 12:01 = **~$2,9–8,2k/ngày, 9–25k KNTQ/ngày**. Size/giờ tăng từ ~$74 lên ~$182 từ 09:06 UTC 3/10 | Assistance Fund giữ **3.988.286 KNTQ = 0,399% supply** |
| 4 claimant lớn nhất | giữ hàng, không arb | `0x9794bbbc…333b` 1,42M, `0x63af859d…4b36` 1,06M, `0xbd8c75a0…971d` 1,00M, `0x9f58a3c3…1dfb` 0,92M (ví này giữ tổng 9,98M) | **Vẫn nguyên si trên HyperEVM** — 5,95M KNTQ không bán |

Nguồn: [api.hyperliquid.xyz/info](https://api.hyperliquid.xyz/info) (`userFillsByTime`, `userTwapSliceFills`, `frontendOpenOrders`, ledger); [api.hypurrscan.io/holders/KNTQ](https://api.hypurrscan.io/holders/KNTQ); [rpc.purroofgroup.com](https://rpc.purroofgroup.com).

Đọc được gì: whale đã **công bố bằng tiền** vùng gom của nó là **0.267–0.287** và vùng phân phối là **0.368–0.442**. Nhịp đi lên của ngày 3/10 từ 0.2949 lên 0.3030 trên volume giảm (từ ~0,8M KNTQ/giờ xuống 0,08–0,46M) **không phải do whale gom** — nó do dòng nhỏ. Đừng đọc cú grind này là nhu cầu mạnh, và cũng đừng đọc việc whale không bid trên 0.287 là tín hiệu nó bỏ hàng. Buyback thì vô nghĩa về kinh tế: $3–8k/ngày là **0,1–0,2% volume ngày**, và tổng cộng dồn 3,99M KNTQ = 0,399% supply bằng **1/32 một năm vest nội bộ**.

### Bên bán

**Người bán lớn nhất về danh nghĩa chính là nhà phát hành.** Kinetiq Foundation đã bán **22.046.576 KNTQ ở 0.261331 lấy $5.761.454** và **chưa rút một đồng nào** — số dư USDC của contract bằng đúng tổng đã thu, không có event `Withdrawn` ([rpc.purroofgroup.com](https://rpc.purroofgroup.com)). Đổi 46 tuần kPoints thành một đợt huy động tiền từ chính cộng đồng ở $0.26 là một tín hiệu về runway và về cách team tự định giá token của mình.

**Claimant: đã bán gần xong, không phải sắp bán.** Đo trực tiếp 200 claimer lớn nhất (17,27M KNTQ = 78% toàn bộ đã claim), phân loại theo (balance HyperEVM + balance HyperCore) ÷ số đã claim:

| Nhóm | Số ví | KNTQ đã claim | % của top-200 |
|---|---|---|---|
| giữ <10% ("đã xả") | **151** | **9.815.000** | **56,8%** |
| giữ 10–90% (bán một phần) | 16 | 1.511.437 | 8,8% |
| giữ ≥90% ("còn giữ") | 33 | 5.947.005 | 34,4% |

Ví xả sạch lớn nhất: `0x0b83821b…3140` 612k, `0xd507eeef…c948` 586k, `0xcc6bf6bf…7c75` 521k, `0x64b3bf0c…d0d4` 460k, `0x418769f7…c925` 362k, `0xd782059d…6ca7` 360k, `0xb2e27551…377c` 326k.

Dòng bridge EVM→HyperCore (đường duy nhất để bán trên orderbook `@334`) xác nhận cùng kết luận và đóng đinh nguyên nhân cú crash 1/10:

| Khung giờ (UTC) | KNTQ bridge vào HyperCore | mỗi giờ |
|---|---|---|
| 30/9 00:00 → 1/10 12:00 (baseline) | 4.744.630 | ~132k/h |
| **1/10 12:00 → 24:00 (claim mở)** | **24.546.650** | **2.045k/h** |
| 2/10 cả ngày | 2.947.696 | 123k/h |
| 3/10 00:00 → 23:00 | 977.468 | **44k/h** |

24,5M bridge vào trong 12 giờ đầu so với 19,3M được claim cùng khung đó nghĩa là **gần như toàn bộ cung claim ngày một đã được đưa lên sổ lệnh ngay**, kèm cả tồn EVM có từ trước — đó là lời giải cơ học cho nến −35% ngày 1/10, và nó **đã xong**: bridge-in giờ chỉ bằng **một phần ba baseline trước claim**. Gộp hai thước đo lại, **khoảng 10–11M KNTQ cung claim đã bị bán (≈$3,0–3,3M ở giá $0,29–0,30)**, còn ~6M nằm trong tay bốn ví lớn chọn không arbitrage.

**Cluster phân phối `0xab11bfc2…4d5f`** (nhận tròn 10.000.000 KNTQ tại genesis — dạng phân bổ partner/MM/investor, không phải points) vẫn là rủi ro treo trên mọi nhịp hồi. Nó bơm hàng cho ví thực thi đúng lúc có sóng: sang `0x259a6f10…4df0` 2M lúc TGE, 900k ngày 17/3, 1,1M ngày 7/5, **4M ngày 31/5 21:44 UTC ngay trong cú spike**; sang `0x366fed19…a181` 80k ngày 20/5, **1M ngày 2/6 trong spike tháng 6**, 500k ngày 22/9. 2.000 fill gần nhất của `0x259a…` (21–30/9) **toàn bộ là bán KNTQ: 161.269 token ở avg $0.3467**, và ví này đang giữ $1,58M USDC. `0x366f…` từ 2/6 mua 155.344 (avg $0.351) / **bán 1.210.810 (avg $0.3935)**, lần bán cuối **1/10 05:51 UTC sát ATH**, đang giữ $1,09M USDC. Cluster còn kiểm soát **~2,65M KNTQ trên HyperCore** — tức khi giá về 0.35–0.39 sẽ có người bán biết mình đang làm gì.

Thêm: `0xfeb63b9e…5fa0` (2,80M) bán 538.769 KNTQ ở avg ~$0.267 từ 10/9 đến 1/10, TWAP mua lại 184.881, net ~−354k. Và nhóm genesis nói chung: trong 9.999 ví nhận airdrop S1, **chỉ 2.843 còn giữ bất kỳ KNTQ nào trên HyperCore; tổng balance của họ còn 60,5M so với 270M ban đầu (−78%)**.

Phần chưa quy được: **22,6M KNTQ bán ra trong hai giờ 12:00–14:00 UTC ngày 1/10** (volume ngày 57,9M ≈ $21,3M, kỷ lục của cặp USDC) lớn hơn rất nhiều so với những gì các ví nêu trên giải thích được. Không tìm thấy dòng nạp CEX nào trên HyperCore, và không có ví CEX nào được gán nhãn đang giữ KNTQ.

---

## 4. Cơ chế claim $0.26 thật sự: 0.261331, không lock, hết hạn 19:00 VN 11/10

**Giá thật là 0.261331 USDC/KNTQ, không phải $0.26.** `quote()` của contract tuyến tính và đồng nhất ở mọi size: quote(1e18)=261.331, quote(1000e18)=261.331.000 → **1.000 KNTQ tốn 261,331 USDC, không phải 260**, tức +0,51% so với đúng câu ví dụ trong bài công bố chính thức, và **đồng nhất trên cả 3.666 lần claim** ([kinetiq.xyz/blog/kntq-kpoints-claim](https://kinetiq.xyz/blog/kntq-kpoints-claim); [rpc.hypurrscan.io](https://rpc.hypurrscan.io)). Không nguồn nào giải thích tại sao là 0.261331 chứ không phải 0.260000 — không TWAP, không fee, không quy ước làm tròn nào được nêu. **Dùng 0.261331 cho mọi tính toán arbitrage; nó là số máy thu tiền.**

Điều khoản chính thức, nguyên văn: allocation bằng số kPoints cuối kỳ, cho **"the right to acquire up to that amount of KNTQ at the fixed $0.26 price during the 10-day window"**; được claim một phần ("You do not have to claim the full allocation"); giá **không** liên động giá thị trường ("The claim price does not change with the KNTQ market price"); **"the KNTQ received has no lockup or vesting period"**; thanh toán bằng **USDC trên HyperEVM** (native USDC `0xb88339cb…ba630f`); claim tại **kinetiq.xyz/kntq**, đăng nhập bằng ví / email (khuyến nghị) / Google / passkey, **"Apple login is not recommended"**; **không gia hạn** ("There is no additional claim period announced after the 10-day window"); phần chưa claim **quay về Kinetiq Foundation** cho "ecosystem and growth initiatives" ([kinetiq.xyz/blog/kntq-kpoints-claim](https://kinetiq.xyz/blog/kntq-kpoints-claim)).

Cửa sổ đọc thẳng từ contract `0x435bb7ea4eb481cb686606d089ea4dee4c6cc03b`: `start()` = 1790856000 = **2026-10-01 12:00:00 UTC**, `end()` = 1791720000 = **2026-10-11 12:00:00 UTC = 19:00 giờ VN ngày 11/10** (đúng 864.000 giây). Pool được nạp **đúng 50.000.000 KNTQ = 5,0% total supply** trong hai giao dịch (100 KNTQ test + 49.999.900) từ `0x5bd9e766…aae4` — **ví "growth/ecosystem 30%"**, nên đợt bán này được tài trợ từ túi growth chứ không từ một quỹ airdrop riêng (xem mục 6 cho hệ quả). Allocation là **Merkle snapshot cố định trước 1/10 12:00 UTC** (UI trả lỗi `invalid_proof`: "This wallet's allocation could not be verified"), có theo dõi phần còn lại (`exceeded`), có mức mua tối thiểu (`below_min`, nhưng claim nhỏ nhất quan sát được là **0,130 KNTQ ≈ $0,034** nên không đáng kể), và **claim có thể bị pause** ([rpc.hypurrscan.io](https://rpc.hypurrscan.io); [kinetiq.xyz/kntq](https://kinetiq.xyz/kntq)).

**Tiến độ thực, đo trực tiếp (2026-10-03 23:22 UTC, block 47.593.005):**

| Mốc | Số liệu |
|---|---|
| Đã claim | **22.046.576 KNTQ = 44,093% của pool 50M** |
| Số ví | **3.059** (3.666 lần claim) |
| USDC đã thu | **$5.761.454** (contract vẫn giữ đủ — team chưa rút) |
| Còn trong contract | **27.953.424 KNTQ = 55,91%** |
| Premium so với 0.261331 | **+15,88%** (giá 0.302835) |
| Còn lại tới deadline | ~180,6 giờ |

Đường cong claim: **giờ đầu tiên 7.096.543 KNTQ = 14,19% cả pool; 12 giờ đầu 19.289.818 = 38,58%**; rồi 2/10 chỉ +1.501.029; 3/10 (tới 23:00) +1.255.729 — mà con số ngày 3/10 bị chi phối bởi **một giờ duy nhất claim 1,02M KNTQ (09:00 UTC, 10 lần claim)**; bỏ giờ đó ra, cả ngày 3/10 chỉ ~0,24M. Tốc độ ngày: **19,29M → 1,50M → 1,26M, giảm ~93%**. Hai snapshot cách nhau 11 giờ (43,788% → 44,093%) cho thấy claim giờ là **nhỏ giọt, không phải sóng**.

Claim cũng tập trung y như token: **median claim 305,2 KNTQ (~$80)**, mean 7.207, max 1.422.137; **top 10 ví = 33,2%, top 25 = 47,2%, top 100 = 68,5%, top 500 = 91,4%** của tất cả KNTQ đã claim; 1.147 trong 3.059 ví mua dưới $26. Và đúng những ví đã farm S1 nặng nhất lại farm kPoints S2 nặng nhất: `0x9794bbbc…333b` từng nhận **12,77M genesis S1**, `0x63af859d…4b36` từng bridge **20,32M** sang HyperEVM tháng 12/2025 — cả hai lấy tối đa suất S2. Giờ 06:00–07:00 UTC ngày 3/10 có **515 lần claim cho tổng 48k KNTQ (avg ~93 KNTQ)** — một đợt ví bụi, không phải cung có ý nghĩa kinh tế.

**27,95M còn lại là áp lực cung CÓ ĐIỀU KIỆN, không phải cung đã lên lịch.** Ba lý do nó không nên được mô hình hoá như 27,95M token sắp đổ ra: (1) nó chỉ chuyển thành cung khi giá còn thoải mái trên 0.2613; (2) **nó cần $7,31M USDC tiền mới** để convert — ngày một đã tiêu $5,04M, và hỏi 3.000-ví-phần-lớn-nhỏ bỏ thêm $7,3M trong 8 ngày là một câu hỏi khó; (3) ngoại suy tuyến tính theo tốc độ hiện tại (~0,26M/ngày nếu bỏ các cục lớn) chỉ cho ra **~48–52% claim cuối kỳ**, còn nếu tính theo tốc độ gộp 1,26M/ngày thì ~62–64%. Dải hợp lý: **55–70% claim cuối kỳ, 100% gần như chắc chắn không xảy ra**, nhưng **hãy chờ một đợt dồn trong 24–48 giờ cuối** — đó là hình mẫu chuẩn của mọi deadline-driven claim, và với depth ±2% chỉ $12–25k thì đợt dồn đó là rủi ro cơ học chính còn lại.

Tổng P&L của toàn bộ claimant hiện mỏng: trả $5.761.454, giá trị ~$6,68M ở $0.3030 → **+~$0,92M (+15,9%) gross, không hedge**. Nhỏ so với slippage khi phải bán 22M token vào một thị trường $3,9M/ngày — đó vừa là lý do tin claimant rải hàng chứ không dump, vừa là lý do claimant biên ngừng claim ngay khi spot tiến về 0.26.

Hai cảnh báo phải mang theo: **`kntq-claim.vercel.app` ("KNTQ Season 2 Claim") KHÔNG phải domain Kinetiq** — official duy nhất là **kinetiq.xyz/kntq**; coi nó là bản clone phishing. Và **[airdrops.io/kinetiq](https://airdrops.io/kinetiq/) vẫn treo tiêu đề "Claim free KNTQ tokens"** — sai hoàn toàn, đợt này là **quyền mua có trả tiền, không có phần airdrop miễn phí nào**. Thêm chi tiết nhỏ nhưng nên biết: **"Season 2" không phải cách Kinetiq gọi** — framing chính thức là "the final kPoints have now been distributed", tức một sự kiện kết thúc, không phải mùa mới.

---

## 5. $0.26 có phải đáy cục bộ ngắn hạn? Không — nó là nam châm trước 11/10 và chỉ là mốc tham chiếu sau đó

**Trả lời thẳng: không.** $0.26 không phải đáy; nó là **giá thực thi của một quyền chọn có hạn** và là **cụm cost basis**, hai thứ hoàn toàn khác với một mức có bid đỡ.

### Vì sao nó hoạt động như nam châm — và thực chất là *trần* — trước deadline

Contract là một **chào bán thường trực 27,95M token ở 0.261331** cho bất kỳ ai có allocation, cho tới 19:00 VN 11/10. Với một người có suất, mua trên thị trường ở 0.28 là **vô nghĩa về kinh tế** khi contract bán 0.2613. Nghĩa là **mọi bid thị trường trên 0.26 đều bị contract ăn mất khách**: nó triệt tiêu một tầng cầu tự nhiên và **đè trần lên lực mua của nhóm claimant**, đúng cái cơ chế nhìn như hỗ trợ nhưng hành xử như kháng cự. Đồng thời arbitrage kéo giá về phía 0.26 cộng một chút ma sát, và đúng là nó đã kéo: ATH $0.4521 ngày 1/10 06:18 UTC → sàn $0.27778 trong vòng vài giờ sau khi công bố 12:01:39 UTC ([api.coingecko.com/api/v3/coins/kinetiq](https://api.coingecko.com/api/v3/coins/kinetiq); [Kinetiq trên X](https://x.com/Kinetiq_xyz/status/2105629210048078216)).

Nhưng ba ngày dữ liệu đã **bác bỏ một phần** luận điểm "giá phải hội tụ về 0.26": premium vẫn **+15,9%** sau khi 44% pool đã claim và 10–11M token claim đã bán xong. Nến giờ ngày 3/10 đi 0.2999 (10:00) → đóng 0.3030 (23:00), cả ngày chỉ dao động 0.2949–0.3084, và **đáy ngày (0.2949) đến LÚC 10:00, tức TRƯỚC khi giờ claim 1,02M KNTQ ở 09:00 được tiêu hoá** — rồi giá đóng gần đỉnh ngày. Cung claim ngày 3/10 được hấp thụ mà không tạo đáy mới. Arbitrage không đóng được gap nghĩa là **có bid thật đang hấp thụ**, không phải mức giá được giữ bởi chính claimant.

### Vì sao nó KHÔNG phải sàn sau deadline

Sau 19:00 VN 11/10, **không gì enforce mức 0.26**. Không lockup. Không perp để ai đó bị ép đóng short. Không cam kết nào từ Foundation hay treasury về việc bid ở 0.26 — buyback là cơ chế theo doanh thu, chạy $4–6k/ngày, và lịch sử mua vào ở **giá trung bình ~$0.15**, thấp hơn giá claim rất xa. Nặng hơn: **chính nhà phát hành là người bán tự nguyện ở 0.261331** — điều đó làm 0.2613 trở thành **mốc neo trần đáng tin hơn là mốc neo sàn**. Và lịch sử giá nói phần còn lại: KNTQ **dành ~93% thời gian tồn tại đóng dưới $0.26**; chỉ **21 trong 311 nến ngày kể từ TGE đóng trên $0.26** (1 nến 28/1, 4 nến 31/5–3/6, và 16 nến liên tiếp từ 18/9 tới nay); hai lần vượt $0.26 trước đây đều thất bại trong 1–4 nến; **ATL $0.03578 (17/12/2025)** nghĩa là **$0.26 hôm nay là 7,3x đáy tháng 12/2025** ([api.hyperliquid.xyz/info](https://api.hyperliquid.xyz/info); [api.coingecko.com/api/v3/coins/kinetiq](https://api.coingecko.com/api/v3/coins/kinetiq)). Gọi một mức mà token từng giao dịch sâu dưới đó cách đây chưa đầy một năm là "sàn cấu trúc" là nhầm lẫn thể loại.

Base rate cũng nghiêng về phía bi quan: nghiên cứu Bitquery trên 51 đợt airdrop lớn 2026 (ETH/BNB/Base/Arbitrum, $809,4M phân phối) cho **35/46 token (76%) giao dịch dưới giá tuần đầu, median −48%; 73% claimer chuyển token trong vòng một ngày; chỉ 23% còn giữ ≥nửa suất sau 30 ngày, 8% sau 90 ngày; top 10% claimer nhận 73% token** ([Bitquery](https://bitquery.io/investigations/crypto-airdrops-2026)). Hai điều chỉnh cần làm khi áp vào đây: cơ chế tạo ra kết quả −48% là **cung giá-0** (claimer free bán ở mọi giá), và cơ chế đó **bị tắt một phần** ở S2 vì mọi claimant đã trả 0.261331 — nên kỳ vọng bán **chậm hơn và nông hơn base rate**. Nhưng phần **tập trung** thì chuyển thẳng và đã được xác nhận: top 10 ví lấy 33,2%, và đó đúng là nhóm thoát nhanh nhất — **với không một perp nào để hedge, đường thoát duy nhất của họ là bán spot**.

### Sự bất đối xứng thật sự nằm ở dưới 0.2613

Nếu spot xuống dưới 0.261331 thì **mọi claim còn lại trở thành phi lý: tới 27,95M token cung tiềm ẩn bị TẮT và quay về Foundation.** Đó là tính chất giống-sàn duy nhất và nó có thật: **dưới 0.26 thì nguồn cung tự diệt, overhang là tự giới hạn chứ không tự khuếch đại.** Nhưng nó đi kèm mặt sau: **một lần in giá dưới 0.2613 cũng có nghĩa là có người bán KHÔNG phải arbitrageur** — tức là genesis holder, cluster phân phối, hay dòng bán do macro. Đó là người bán không có giá sàn tâm lý nào ở 0.26, và vì vậy một cây nến xuyên 0.2613 phải được đọc là **tín hiệu xấu về chất lượng cầu**, chứ không phải "tin tốt vì cung claim tắt".

**Kết luận thực dụng cho người giao dịch:** vùng đáy cục bộ mà dữ liệu chống lưng không phải 0.26 mà là **0.267–0.288** — band bid có tiền thật của whale (0.2666–0.28656), cộng đáy crash 1/10 (0.27778), cộng sàn 2–3/10 (0.287), cộng stack bid tổng ~4,9M KNTQ ($1,33M) ở 0.25–0.30. 0.2613 là mức mà **dòng bán cơ học dừng**, không phải mức mà **lực mua bắt đầu**. Hết hạn claim là **điểm kết thúc một vách cung, không phải một vách cung** — về cơ học đó là tích cực ở biên; rủi ro bù lại là những ai đã claim chỉ để arb mà còn hàng chưa bán sẽ phải bán sau khi cái lý do để arb đã mất.

---

## 6. Kịch bản tới 11/10 rồi tới 27/11: xác suất, giá, và hai mốc không được bỏ qua

### A. Từ nay tới 19:00 VN 11/10 (còn ~180 giờ)

| Kịch bản | P | Vùng giá | Lý do |
|---|---|---|---|
| **Base** | **55%** | giữ dải **0.275–0.315**, có một dip về **0.27–0.29** trong 48h cuối | tốc độ claim đã chết nhưng deadline luôn tạo đợt dồn; 27,95M cần $7,3M tiền mới nên đợt dồn sẽ chỉ là một phần; depth ±2% $12–25k khuếch đại mọi cú market sell |
| Bull | 20% | giữ 0.30+, grind lên **0.32–0.34** | claim thực tắt (<0.3M/ngày), premium giữ hai chữ số, altseason index 61 còn lên, HYPE hồi về ATH $97,96 |
| Bear | 25% | **0.255–0.275**, có thể wick xuyên 0.2613 | đợt dồn claim + CPI 14/10 nóng + cluster `0xab11…` bán vào mọi nhịp hồi; Hyperliquid L1 TVL −23,6%/30 ngày là cơn gió ngược cơ bản |

### B. Từ 11/10 tới 27/11 (6,5 tuần)

| Kịch bản | P | Vùng giá | Lý do |
|---|---|---|---|
| **Base** | **45%** | hồi sau hết hạn + narrative Elysium → đỉnh **0.33–0.37** quanh 20/10, rồi fade về **0.27–0.31** vào cliff | overhang biến mất, nhưng Elysium là catalyst "show me": 50% sequencer revenue mua-và-burn KNTQ đã confirm là *thiết kế*, mà doanh thu hôm nay = $0 trên một Orbit chain mới nhắm HFT. "Burn rate phụ thuộc hoạt động giao dịch thật, không phụ thuộc sự kiện ra mắt" ([CoinMarketCal qua TradingView](https://www.tradingview.com/news/coinmarketcal:ab9da4724094b:0-kinetiq-elysium-mainnet-launch-brings-its-hyperliquid-l2-live-by-20-oct-2026/)) |
| Bull | 25% | **0.42–0.50** (ATH mới) | Elysium ship đúng hẹn với volume nhìn thấy được, altseason index vượt 75, dòng ETF tiếp tục vào (tháng 9: BTC +$2,65B, ETH +$832M), và KNTQ là token HyperEVM-native lớn nhất ($85,1M mcap) nên hưởng beta cao nhất |
| Bear | 30% | **0.19–0.24** | FOMC 28/10 xác nhận lộ trình tăng tháng 12; HYPE multiple nén (FDV $85,4B / ~$885M fees ≈ 97x) kéo KNTQ nén mạnh hơn; HYPE staked tiếp tục −17%/tháng; cliff 27/11 được front-run từ giữa tháng 11 |

**Lịch catalyst dày rồi trống hẳn:** 11/10 hết hạn claim → 14/10 CPI tháng 9 (08:30 ET = 19:30 VN) → **20/10 Elysium mainnet** → 28/10 FOMC (14:00 ET = 01:00 VN ngày 29/10) → 29/10 CPI tháng 10 → rồi **không có gì KNTQ-specific được định ngày cho tới FOMC tháng 12** ([TradersQuant](https://tradersquant.com/calendar); [FinanceCalendar](https://www.financecalendar.com/fomc-meetings/)). Vì vậy risk/reward dồn vào **khung 11/10 – 20/10**: overhang sạch, rồi catalyst cơ bản lớn nhất của quý bắn.

**Hai mốc phải đưa vào mọi mô hình:**

**20/10 — Elysium mainnet.** Xác nhận qua 3+ nguồn độc lập; testnet mở 22/9/2026, chain ID 99801; thiết kế Arbitrum Orbit settle về HyperEVM, HYPE làm gas, mục tiêu block 100–200ms; **50% sequencer revenue lập trình mua KNTQ trên thị trường mở** — con số 50% được **xác nhận bởi chính docs Kinetiq**, không chỉ báo chí ([kinetiq.xyz/docs/kntq](https://kinetiq.xyz/docs/kntq); [Chainstack](https://chainstack.com/what-is-elysium/)). Nhưng ngày 3/10 23:18 UTC `elysium.kinetiq.xyz` vẫn render badge **"Testnet"**, **không có audit công bố**, và hai nguồn thứ cấp còn **mâu thuẫn về chính stack của nó** (OP Stack settle về HyperEVM vs Arbitrum Orbit). Đọc Elysium là **cú đẩy narrative, không phải sự kiện dòng tiền** — kinh điển "buy the rumor, sell the news". Điểm đáng giá hơn vẻ ngoài: nếu KIP-5 đã lấy buyback khỏi sKNTQ, thì Elysium là **kênh value-accrual THAY THẾ** và không phụ thuộc dòng fee LST đang teo.

**27/11 — cliff 310M token = 31% supply.** TGE 27/11/2025, docs ghi nguyên văn **"Total duration: 3 years. Cliff: 1 year. Vesting: 2-year monthly linear vesting following the cliff"** cho toàn bộ core contributors (235M) + investors (75M) ([kinetiq.xyz/docs/kntq](https://kinetiq.xyz/docs/kntq)). Đọc theo đúng chữ: **12,92M KNTQ/tháng ≈ $3,92M/tháng ở $0.30 = 4,61% circulating mỗi tháng, 155M trong năm đầu**. Buyback $1,78M/năm **bù được 3,8%** giá trị đó. Và cost basis của nhóm vest là **$0.0175–0.0233** (seed $1,75M đóng 22/10/2025, ~$17,5M pre-money, Maven 11 dẫn) — **lãi 13–17x ở $0.30, 11–15x ở giá claim**, không lockup sau khi vest ([api.llama.fi/protocol/kinetiq](https://api.llama.fi/protocol/kinetiq)). Lưu ý: ngày 27/11 là **suy ra** từ TGE + "1 năm" trong docs, không phải ngày do tracker unlock nào công bố; và **không có nguồn nào xác nhận mốc unlock HYPE 29/11** (bài gốc không ghi năm, có thể đang nói 11/2025) nên đừng dùng nó như catalyst Q4/2026. Rủi ro lớn hơn cả 310M theo hợp đồng là **350M token growth + foundation KHÔNG có lịch vest công bố nào** — tuỳ ý phát hành, và S2 chính là bản mẫu: 5% supply bán ở $0.26, không lockup, công bố trước khi mở cửa sổ **23 phút**.

**Và đây là điều làm mốc 27/11 nguy hiểm hơn vẻ ngoài của nó: không có vesting contract nào cả.** Truy trực tiếp log `Transfer` của KNTQ từ deployer trong 3,5 ngày sau TGE (block 20.320.000–20.620.000; block 20.324.553 = 27/11/2025 12:00:00 UTC) cho thấy 730M được chia vào **đúng năm địa chỉ trong cùng một phút, 27/11/2025 12:07 UTC** — và `eth_getCode` của cả năm đều **rỗng: tất cả là EOA, không một dòng code nào** ([rpc.purroofgroup.com](https://rpc.purroofgroup.com)):

| Ví | Phân bổ | Số dư 3/10/2026 23:42 UTC | Đã chuyển đi |
|---|---|---|---|
| `0x373e0b6b…d90e` | core contributors 23,5% | **235.000.000** | 0 |
| `0x9ef3b3a4…a1a2` | investors 7,5% | **75.000.000** | 0 |
| `0xf50ad637…2b36` | foundation 10% | **100.000.000** | 0 |
| `0x5bd9e766…aae4` | growth 30% | 250.000.000 | −50.000.000 (→ contract claim S2) |
| `0x4664b045…e734` | liquidity 2% | 4.523.810 | −15.476.190 (đã deploy vào pool) |

Ba hệ quả. **Một:** lịch "cliff 1 năm + vest 24 tháng" là **một dòng công bố trong docs, không phải một cơ chế được code cường chế** — không có contract để đọc schedule, không có gì ngăn phát hành sớm hơn hoặc nhiều hơn, và vì vậy **không thể phân xử on-chain** giữa hai cách đọc (12,92M/tháng so với 103,3M ngay tại cliff). Rủi ro cung vì thế là **liên tục từ bây giờ**, không phải một sự kiện có ngày — đó chính là lý do kèo này phải có ngày thoát định trước thay vì "giữ qua tháng 11 xem sao". **Hai:** pool claim $0.26 được rút ra từ **túi growth 30%**, không phải từ một quỹ airdrop riêng — `0x5bd9e766…aae4` chính là ví đã nạp 50M vào contract claim, nên S2 là một lần **chuyển túi growth thành tiền**, và túi đó còn 250M. **Ba, phía tích cực và cần nói cho công bằng:** sau 10 tháng, ba ví team/investor/foundation vẫn đứng ở **số dư tròn, nguyên si**; thứ duy nhất đã động là liquidity (vào pool) và growth (vào contract claim). Không có dòng rỉ âm thầm nào ra sàn. "EOA" nghĩa là **không có cường chế on-chain**, chứ không nhất thiết là không có cam kết — khoá có thể đang được custody hoặc ràng buộc pháp lý ngoài chuỗi.

---

## 7. Kế hoạch vào hàng: hai lộ trình khác nhau tuỳ bạn CÓ hay KHÔNG CÓ allocation

**Quyền mua 0.261331 chỉ thực thi được bởi ví nằm trong Merkle snapshot kPoints.** Ví không có suất gọi contract sẽ bị trả lỗi `invalid_proof` — "This wallet's allocation could not be verified". Allocation **gắn ví, không chuyển nhượng được**, và snapshot đã đóng trước 1/10 12:00 UTC nên **không còn gì để farm**. Hai nhóm người đọc báo cáo này phải làm hai việc khác nhau.

### Nếu bạn CÓ allocation (có kPoints)

**Claim 100% suất, và claim trước 8–9/10, không chờ giờ cuối.** Đây là một quyền chọn đang in-the-money +15,9%; chi phí duy nhất là USDC và gas. Về lý thuyết thì để quyền chọn sống lâu hơn là có giá hơn (nếu giá rớt dưới 0.2613 bạn khỏi phải trả), nhưng thực tế **thanh khoản ngày cuối là tệ nhất** đúng lúc tất cả mọi người cùng đổ ra, và còn rủi ro UI/nghẽn/`paused`. Nên: **front-run đám đông 48 giờ cuối.**

Cấu trúc tối ưu sau khi claim, với điều kiện không có perp để hedge: **bán ~86% số token đã claim ở 0.3030 là hoàn đủ vốn USDC** (0.261331 ÷ 0.3030 = 0,8625), giữ lại **~14% với cost basis bằng 0**. Đó là cách duy nhất khoá được chênh lệch mà vẫn giữ exposure, trong một tài sản không thể hedge. Nếu muốn giữ full exposure thì cứ claim và giữ — bạn đang sở hữu ở 0.2613, tức basis tốt hơn giá thị trường 14%, nhưng đường drawdown của bạn là **0.267–0.287** rồi 0.2550.

Kỹ thuật thực thi: cần **native USDC `0xb88339cb…ba630f` trên HyperEVM** (không phải USDC bridge loại khác); claim một phần được phép nên có thể chia nhiều lần; muốn bán trên orderbook `@334` thì phải **bridge KNTQ từ EVM sang HyperCore** qua system address `0x2000…007c`; **mọi lệnh bán trên ~$30–50k phải TWAP qua nhiều giờ** vì depth ±2% chỉ $12,1k bid; đừng dùng pool DEX cho size lớn (Nest KNTQ/WHYPE $692k, Project X KNTQ/USDC $527k, Nest KNTQ/USDC chỉ $90k). Và **chỉ vào kinetiq.xyz/kntq**.

### Nếu bạn KHÔNG CÓ allocation

Bạn không mua được ở $0.26 và **không nên trả 0.30+ trước 11/10**, vì bạn đang mua một tài sản mà contract đồng thời chào 27,95M đơn vị ở 0.2613 cho một nhóm 3.000+ ví có thể cắt giá bạn bất cứ lúc nào. Kèo bất đối xứng của bạn là **đặt bid thụ động song song với whale ở 0.267–0.288**, và chỉ tăng size **sau** deadline. Dùng đúng thang lệnh L1–L4 ở mục 1. Hai điều kiện để lấp L4 (20% ở 0.29–0.315 sau 11/10): giá **giữ ≥0.29** và **bridge-in EVM→HyperCore ở dưới baseline 130k KNTQ/giờ** — cái thứ hai là bằng chứng cung claim thật đã hết chứ không chỉ tạm nghỉ.

### Quản trị vị thế chung cho cả hai nhóm

Size: coi đây là **kèo event-driven có hạn, không phải core holding**. Nội tại (mục 2) không chống được một vị thế dài hạn lớn. Stop: **đóng ngày dưới 0.2550 là cắt, không bàn lại** — từ giá vốn ~0.284 đó là −10,2%, đúng kích cỡ một stop nên chấp nhận cho kèo này. Chốt: 1/3 ở 0.335–0.3525, 1/3 ở 0.368–0.377 (nhớ 898k KNTQ ask của whale nằm từ 0.36805 đến 0.442 — đó là tường cung thật, không phải giả), trail phần cuối. **Deadline tự giải phóng: ≤25% vị thế trước 20/11.**

Những gì tránh, nhắc lại vì đây là nơi người ta mất tiền: không FOMO 0.30+ trước 11/10; không market order lớn; không cố short/hedge (không có perp, 234 market perp chính + 299 market trên 10 HIP-3 dex, **không một cái nào là KNTQ**); không mua lại "suất claim" của ai; không giữ qua 27/11 theo quán tính; không tin trang chính chủ về "yield cho staker" (đã lỗi thời hậu KIP-5); không tin `airdrops.io` về "free KNTQ".

---

## 8. Tracker 2 giờ/lần đang chạy: những cột cần đọc và 5 ngưỡng đổi quyết định

Một tracker read-only **đang chạy**, Routine `trig_01LeFrUzwx26aLiWAPvdunLG`, cron `7 */2 * * *` (phút :07 UTC mỗi 2 giờ), lần chạy kế tiếp **2026-10-04 00:07 UTC**, và **tự tắt sau 2026-10-11 12:00 UTC** sau khi chốt số claim cuối cùng. Code tại `/home/user/test-claude/kntq-s2-tracker/` (`tracker.py` chạy incremental từ `state.json`, ~2 phút và ~400 RPC call mỗi lượt, cộng dồn event `Claimed(address,uint256,uint256)` topic0 `0x987d620f…5a2f9a`, rồi đọc `balanceOf` của claim contract cho cả KNTQ và USDC, mid HyperCore `@334`, giá pool HyperEVM qua `slot0()`, và — từ bản cập nhật sau phát hiện ở mục 6 — **số dư của cả năm ví allocation**). Không ký giao dịch, không kết nối ví, không cần API key.

Mỗi lượt ghi một dòng vào `snapshots.csv`. Các cột quan trọng nhất và cách đọc:

| Cột | Đọc gì |
|---|---|
| `pct_of_pool_claimed` | % của 50M đã được **kích hoạt** thành cung tự do bán (không lock) |
| `kntq_left_in_contract` | cung còn treo; chỉ chuyển thành bán khi giá > 0.2613, và sẽ dồn về sát deadline |
| `premium_vs_claim_pct` | biên arbitrage còn lại. Về 0 nghĩa là quyền mua hết giá trị **và** lực bán cơ học biến mất |
| `new_wallets`, `new_kntq_claimed`, `claim_pace_kntq_per_h` | nhịp claim trong 2 giờ vừa rồi — thước đo trực tiếp của cung sắp tới |
| `projected_pct_at_deadline` | ngoại suy tuyến tính tới 11/10 12:00 UTC |
| `kntq_px_core_mid`, `kntq_px_evm_pool`, `px_chg_pct_since_prev` | giá HyperCore vs pool HyperEVM (lệch nhau là cơ hội arb nhỏ) và biến động 2h |
| `usdc_held_by_contract` vs `usdc_paid` | **bằng nhau = team chưa rút tiền**; lệch ra là tín hiệu Foundation bắt đầu rút $5,76M+ |
| `alloc_team`, `alloc_investors`, `alloc_foundation`, `alloc_growth`, `alloc_liquidity` | số dư 5 ví EOA giữ 66% supply. Mốc nguyên trạng: **235.000.000 / 75.000.000 / 100.000.000 / 250.000.000 / 4.523.810** |
| **`alloc_moved`** | **cột quan trọng nhất của toàn bộ file.** Trống = bình thường. Có chữ = insider đã chuyển token, kèm tên túi, số lượng và địa chỉ |
| `check_funded_minus_claimed_minus_left` | kiểm tra toàn vẹn, phải bằng 0 |
| `hours_left` | đếm ngược tới deadline |

Ba dòng đã có: `2026-10-03T12:16Z` (block 47.395.562 — 2.955 ví, 43,788%, $0.30225, premium 15,66%); `2026-10-03T23:22Z` (block 47.593.005 — 3.059 ví, 44,093%, $0.302835, premium 15,88%, check = 0); và `2026-10-03T23:38Z` (block 47.594.315 — **3.061 ví, 44,101%, $0.30355, premium 16,16%**, tốc độ 15.766 KNTQ/giờ, `projected_pct_at_deadline` **49,79%**, cả năm cột `alloc_*` đúng mốc nguyên trạng, `alloc_moved` trống). Chú ý con số projection đó: theo nhịp 2 giờ gần nhất, **claim cuối kỳ chỉ ~50%** — khớp với ngoại suy ở mục 4 và là bằng chứng mới nhất rằng 27,95M còn lại phần lớn **sẽ không** biến thành cung.

**Năm ngưỡng cảnh báo đã nối vào Routine — và quyết định tương ứng:**

1. **Premium <5% (giá về 0.262–0.275).** → Quyền mua gần như hết giá trị, lực bán cơ học tắt. **Đây là tín hiệu lấp L2/L3**, không phải tín hiệu chạy.
2. **Bất kỳ khung 2 giờ nào claim >2M KNTQ.** → Đợt dồn deadline đã bắt đầu. **Ngừng mua chủ động, chuyển sang bid thụ động thấp hơn** và chờ 24–48h cho cung tiêu hoá.
3. **Mất 0.287 rồi 0.278 (đóng nến ngày).** → Cung claimant đang đè hết bid. **Không bình quân tiếp quá L3**; nếu mất 0.278 thì chỉ còn L3 được phép.
4. **Bất kỳ lần in giá dưới 0.2613.** → Hai nghĩa trái chiều, phải đọc cả hai: 27,95M cung claim bị **tắt** (tốt về cơ học) nhưng có **người bán thật không phải arbitrageur** (xấu về chất lượng cầu). **Hành động: dừng mọi lệnh mua, chờ đóng ngày. Dưới 0.2550 là cắt.**
5. **`alloc_moved` có bất kỳ nội dung nào** — tức một trong năm ví EOA đã chuyển token ra. → Tín hiệu bearish mạnh nhất có thể đo được, và nó đi **trước** lệnh nạp sàn vài phút tới vài giờ. **Hành động: nếu là ví team `0x373e0b6b…d90e` hoặc investor `0x9ef3b3a4…a1a2` thì thoát toàn bộ, không chờ giá; nếu là ví growth `0x5bd9e766…aae4` rút thêm (ngoài 50M đã biết) thì giảm nửa vị thế và chờ xem đích đến (pool/MM là trung tính, ví mới hoặc sàn là bán).** Mốc so sánh nguyên trạng ghi sẵn trong `tracker.py`, nên không cần nhớ số.

Ngoài snapshots.csv, hai chuỗi nên theo tay: **bridge-in EVM→HyperCore** (`sold.py`, `bridge_in_hourly.json`) — dưới baseline 130k KNTQ/giờ là cung đã cạn thật, vượt trở lại 500k/giờ là hàng mới đang lên sổ; và **ladder của `0xaf0fdd39…1e92e`** — nếu 399.961 KNTQ bid ở 0.2666–0.28656 bị **rút** thì vùng đáy 0.267–0.287 trong báo cáo này mất chân đỡ chính và toàn bộ thang lệnh phải dịch xuống. Sau 11/10, khi Routine này tự tắt, **cột `alloc_*` là thứ duy nhất đáng giữ lại chạy tiếp** — nó không liên quan gì tới cửa sổ claim và là early-warning duy nhất cho 66% supply.

---

## 9. Rủi ro và những điều chưa biết: 720M token không truy được, không perp để hedge, sổ lệnh $12–25k

**Khoảng trống lớn nhất: không ai trong nhóm nghiên cứu enumerate được holder KNTQ trên HyperEVM**, nơi **85,74% supply (857.384.168 KNTQ) đang nằm**. Mọi API explorer đều chặn: `hyperevmscan.io` trả Cloudflare 403, `api.hl.eco/.../holders` 404, `api.hypurrscan.io/evmHolders` 404, routescan "chain not supported" / 403; quét bằng `eth_getLogs` qua ~26M block ở 10k/lần là bất khả thi trong budget. **Phần lớn khoảng trống này đã được lấp ở phút cuối** bằng cách bỏ explorer và truy thẳng log `Transfer` từ deployer: 730M nằm ở **đúng 5 ví EOA** (mục 6), nên **660M = 66% supply giờ đã được định vị và dán nhãn**. Cộng sKNTQ (75,83M) và contract claim (27,95M), **763,8M = 76,4% supply đã truy được**, để lại ~236M thật sự phân tán trong tay thị trường — khớp với circulating 280,5M của CoinGecko và thấp hơn hẳn 335,48M của DropsTab.

**Nhưng câu hỏi quan trọng chỉ đổi dạng, không mất đi.** Biết 310M token nội bộ nằm ở hai EOA cụ thể tốt hơn là không biết, song **"EOA" nghĩa là không có cơ chế nào cường chế lịch vest**: không có contract để đọc schedule, không phân xử được 12,92M/tháng so với 103,3M tại cliff, và không loại trừ được một lần phát hành sớm. Khoá có thể đang nằm trong custody hoặc bị ràng buộc bằng hợp đồng pháp lý ngoài chuỗi — **không kiểm chứng được từ on-chain, và đó là ẩn số số một còn lại**. Mặt bù: 10 tháng qua **không một token nào rời hai ví đó**, và mọi lệnh chuyển ra sẽ hiện trong tracker 2 giờ/lần ở cột `alloc_moved` trước khi hàng kịp lên sàn. Hai điều vẫn chưa truy được: **~94M KNTQ trên HyperEVM ngoài 5 ví + sKNTQ + contract claim** (DEX pool ~4,2M, phần còn lại là claimant và holder phân tán), và **số dư phía HyperCore của chính 5 ví đó**.

**Không có perp KNTQ ở bất cứ đâu.** Đã kiểm tra `meta` (234 market perp chính) và `perpDexs` (10 builder dex: `xyz`, `flx`, `vntl`, `hyna`, `km`, `abcd`, `cash`, `para`, `mkts`, `io`, thêm 299 market) — **không một market nào chứa "KNTQ"**, kể cả trên HIP-3 dex của chính Kinetiq; và CoinGecko derivatives API (26.651 ticker) trả về 0 contract KNTQ ([api.hyperliquid.xyz/info](https://api.hyperliquid.xyz/info); [api.coingecko.com/api/v3/derivatives](https://api.coingecko.com/api/v3/derivatives)). Nghĩa là: không hedge được, không short được, không có funding/OI/long-short skew để đọc vị thế, không có cascade thanh lý để giải thích biến động. Mọi cú move là mất cân bằng order flow spot trên sổ mỏng. Điều này vừa làm claimant chỉ có một đường thoát (bán spot), vừa làm **bạn không có cách nào bảo hiểm vị thế qua cliff 27/11 ngoài việc bán**.

**Thanh khoản là ràng buộc cứng.** Tại 23:45 UTC 3/10, depth full-precision chỉ **~$12,1k bid trong −2% và ~$22,6k ask trong +2%** — và lưu ý bid đã **mỏng đi ~60%** so với $29,2k lúc 12:07 UTC cùng ngày, tự nó là một tín hiệu. Dày hơn thì có: ~$98–163k bid / $76–93k ask trong ±5%, ~$1,30M bid / $0,50M ask trong ±20%, và stack 4,9M KNTQ ($1,33M) ở 0.25–0.30. Nhưng **bid treo có thể bị rút — nó không phải cầu đã cam kết**. Volume 24h $3,88–4,19M với **77–85% nằm trên một venue duy nhất (Hyperliquid spot)**, phần còn lại là Kraken ~6–9% và DEX HyperEVM ~14% (tổng pool ~$2,2M); **không có Binance/OKX/Bybit/Bitget/Gate/MEXC**. Một market sell $100–200k gap giá vài phần trăm. Mặt khác, việc chưa có listing tier-1 nào là **call option chưa được định giá** lớn nhất của token này — nhưng không có bằng chứng nào về một listing đang tới, nên **đừng mô hình hoá nó**.

**Foundation sẽ làm gì với phần chưa claim — không ai biết.** ~28M KNTQ (2,8–3,1% supply) sẽ quay về Foundation nếu take-up dừng ở 44–60%, với mô tả duy nhất là "ecosystem and growth initiatives", **không timeline, không lockup, không cam kết không bán**. Đó là **tái tập trung supply vào một túi tuỳ ý — ngược hẳn với một vụ burn**. Tương tự, **$5,76M USDC (và đang tăng) nằm trong claim contract không có tuyên bố nào về mục đích sử dụng**.

**Các con số nguồn xung đột, và số tôi tin:**

| Chỉ tiêu | Các giá trị | Số tin dùng, vì sao |
|---|---|---|
| Giá claim | $0.26 (marketing) vs **0.261331** (contract) | **0.261331** — `quote()` đồng nhất trên 3.666 claim; marketing thấp hơn 0,51% |
| Giá hiện tại | 0.30225 (12:07) / **0.302835–0.30300** (23:22–23:45) / 0.303319 (CoinGecko) | **$0.3030 mid HyperCore `@334` 23:45 UTC** — mới nhất và là venue 77–85% volume; CoinGecko khớp trong 0,1% |
| ATH | **$0.452145** (CoinGecko, 1/10 06:18:50) vs $0.45572 (HL hourly) | **$0.4521** cho tính % từ ATH (−33%); HL in 0.4557 intraday — cả hai đúng theo venue |
| Circulating | **280.476.290** (CoinGecko) vs 335,48M (DropsTab) | **280,5M** cho mcap ($85,1M) — bảo thủ; chênh 55M ≈ đúng pool S2 50M + liquidity. Mcap thật là **$85–102M** tuỳ cách tính, và **FDV $303M là mẫu số trung thực** |
| Ngày công bố | **1/10 ~12:00 UTC** vs 2/10 12:22 UTC (ChainCatcher) | **1/10** — ba xác nhận độc lập: timestamp X post 12:01:39, giờ crash, và `start()` = 1790856000 |
| Buyback lũy kế | 5,39M @ ~$0.15 (KIP-5) vs **3.988.286 KNTQ** (on-chain) vs $1.291.524 all-time (DefiLlama) vs "$322K to date" (30/6) | **Chỉ dùng 3.988.286 KNTQ = 0,399% supply** trong Assistance Fund (đo on-chain). Bốn số không khớp được; **không trình bày một con số lũy kế nào như sự thật** |
| Stack Elysium | OP Stack settle HyperEVM vs **Arbitrum Orbit** | Chưa giải quyết — cả hai đều là nguồn thứ cấp. Việc mô tả công khai về sản phẩm chủ lực còn mâu thuẫn là một cờ đỏ về minh bạch |

**Giới hạn của chính phép đo "claimer đã bán bao nhiêu":** nhãn "đã xả" gộp cả bán thật với chuyển sang ví khác cùng chủ, nạp CEX, hay vào staking/LP (sKNTQ, pool Nest/Project X) — **không match từng fill**. Ví số dư 0 là **giới hạn dưới chắc chắn** của lượng bán (ví không còn gì thì không thể đã giữ), còn nhóm "còn giữ ≥90%" là **giới hạn trên**, vì balance HyperCore có thể gồm token có từ trước claim. Và **chỉ 200 ví lớn nhất được kiểm balance (78% KNTQ đã claim)**; 2.859 ví còn lại giữ 22% chưa phân loại.

**Những thứ không kiểm chứng được trong vòng nghiên cứu này, nên coi là chưa biết:** **công thức kPoints được giữ kín theo chính sách** của Kinetiq ("Details around the kPoints program are kept entirely private"; hỏi lại trong Discord bị mute/ban) nên **mẫu số ví eligible không công khai** — không tính được "% ví đã claim", chỉ tính được % pool; tỉ lệ gộp suy ra là **1,3587 KNTQ/kPoint** (50M ÷ 36,8M) nhưng **giả định pro-rata tuyến tính là chưa xác nhận**. **X/Twitter không truy cập được (HTTP 402)** suốt quá trình nghiên cứu, nên không có sentiment cộng đồng, không có KOL call có ngày nào ngoài **DeFi Dad** (ủng hộ cấu trúc "call option" nhưng phê phán cách truyền thông); bài bull thesis của **4Pillars** ("17x", đường tới $2B FDV, KNTQ là "HIP-3 infrastructure disguised as an LST") **chỉ đọc được qua summary** vì bị bot checkpoint chặn — và **một trong bốn chân của nó ("buyback mỗi hai giờ phân phối cho staker") xung đột trực tiếp với KIP-5**, còn chân "equity perps thành thị trường nghìn tỷ" thì chính tác giả thừa nhận là điều kiện sống-còn của luận điểm ([4Pillars](https://research.4pillars.io/en/research/kntq-thesis-17x-heavily-coded)). Không tìm thấy thảo luận tiếng Việt hay tiếng Hàn nào về KNTQ. Không có tiền lệ nào trong lịch sử crypto cho đúng cấu trúc này (points holder được quyền mua giá cố định, không lock, cửa sổ ngắn) — **bản thân việc không có tiền lệ là một phát hiện**, và nó có nghĩa mọi phát biểu kiểu "giá claim luôn thành hỗ trợ" là không có cơ sở dữ liệu.

---

## Kết luận

Ba ngày dữ liệu on-chain đã **đảo ngược câu hỏi mặc định**. Câu chuyện mà ai cũng kể là "50M token giá rẻ sắp đổ xuống đầu bạn". Thực tế đo được thì ngược: **38,6% pool đã được claim trong 12 giờ đầu và gần như toàn bộ đã bị bán ngay (24,5M bridge lên sổ lệnh trong 12 giờ, ~10–11M đã xả), bridge-in giờ chỉ bằng một phần ba baseline trước claim, 151 trong 200 claimer lớn nhất đã về số 0 — và giá vẫn đứng ở premium +15,9% sau tất cả.** Áp lực bán cơ học là chuyện đã xảy ra, không phải chuyện sắp xảy ra. Cái còn lại là **27,95M quyền mua cần $7,3M tiền mới để kích hoạt**, trong tay một nhóm mà median suất là $80, và nó sẽ dồn vào 48 giờ cuối rồi tắt vĩnh viễn lúc 19:00 VN ngày 11/10. Đó là một cấu hình để **mua một nhịp dìm có lịch trước**, không phải một cấu hình để tránh.

Nhưng đừng đổi một kèo giao dịch thành một luận điểm đầu tư. Hai sự thật nặng nhất trong báo cáo này không liên quan gì đến airdrop: **base của doanh thu đã mất ba phần tư (HYPE staked 50,07M → 12,47M) và vẫn giảm đơn điệu từng tháng, trong khi toàn bộ tăng trưởng doanh thu +105,5% là một bước nhảy take rate không lặp lại được**; và **31% supply thuộc nhóm có cost basis $0.0175–0.0233 bắt đầu chảy ra từ 27/11, ở nhịp $3,9M/tháng mà buyback chỉ bù 3,8%**. Giữa hai mốc đó là Elysium ngày 20/10 — catalyst duy nhất có khả năng thay thế value accrual mà KIP-5 đã lấy đi, nhưng hôm nay nó vẫn là testnet, chưa audit, và nguồn công khai còn mâu thuẫn về cả kiến trúc của nó. Vậy nên: vào ở 0.267–0.288, thêm sau 11/10 nếu giữ được 0.29, chốt vào tường ask 0.368–0.442 của chính con whale đang đỡ giá cho bạn, cắt dưới 0.2550, và **rời cuộc trước 20/11** — rồi hỏi lại câu hỏi cơ bản vào tháng 12 khi đã có hai tháng dữ liệu Elysium và một tháng dữ liệu unlock thật.

---

*Đây là phân tích dữ liệu, không phải lời khuyên đầu tư.*
