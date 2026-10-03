# Saturn YT: cược nhỏ, đợi giá rẻ hơn

## Cập nhật 3/10/2026: Monad YT-USDat rẻ hơn, nhưng point cũng bị pha loãng hơn

**Kết luận không đổi về hướng: vẫn chỉ đáng một vị thế nhỏ, nhưng pool ưu tiên chuyển sang Monad YT-USDat.** Ở implied APY 8.83% hiện tại, $1,000 Monad YT-USDat cho kỳ vọng +14%, trung vị −14% và xác suất lỗ 58% (28/9: +12% / −19% / 60%). Mua thử được khi implied APY ≤ 8% (trung vị −5%). Vào đủ quy mô khi ≤ 7% (trung bình +42%, trung vị +8%). ETH YT-USDat (9.23%, không có MON) giờ kém hơn: kỳ vọng ~0%, trung vị −27%. Dữ liệu chi tiết nằm trong [ghi chú cập nhật](../research_notes/Phân%20tích%20Saturn%20credit%20YT%20Pendle/update_2026-10-03.md). Phần phân tích gốc ngày 28–29/9 giữ nguyên bên dưới.

**Những gì đã thay đổi trong 5 ngày:**

- **Giá YT Monad giảm, nhưng số point mỗi đô gần như không đổi.**
  - Implied APY lên đỉnh 9.89–9.91% ngày 1–2/10 rồi về 8.83%. Giá YT giảm từ $0.02532 (28/9) xuống $0.02349, tức −7.2%; khoảng 4.5% trong đó là do thời gian trôi.
  - Báo giá thật cho $1,000 ra 40,786 YT, nhiều hơn 7% so với 28/9. Nhưng cửa sổ point S2 cũng ngắn đi 6.9% (còn 66.8 ngày), nên số point mỗi đô gần như đứng yên: ~77.6M point cho $1,000 đến 8/12 ([Pendle API](https://api-v2.pendle.finance/core/v1/143/markets/0x88c5d8a908834e44b421cb67aec9a931782f9538)).
- **"Yield gần 6%" là 3% USDC cộng 2.63% MON, và phần MON hiện chỉ chắc chắn đến 15/10.**
  - Pendle trả thêm cho riêng YT Monad USDat 1,508,348 MON (~$47.7k) trong 14 ngày (1/10–15/10). Đợt trước là 1.02M MON (17/9–1/10) ([Pendle markets/all](https://api-v2.pendle.finance/core/v1/markets/all?limit=100)).
  - Với $1,000, phần MON đã xác nhận chỉ đáng ~$32. Nếu được gia hạn đến 8/12 hoặc 14/1 ở APR ~2%, thêm ~$115–190.
  - Người mua YT vẫn trả implied APY 8.83% cộng ~4.4% chi phí khớp lệnh. Chưa tính point, Pendle ghi long-yield APY là −77.7%/năm.
- **Point bị pha loãng mạnh hơn dự kiến.**
  - Ngày 30/9 Saturn airdrop 24.8 tỷ Orbital Points ("Season 2 loyalty make-good") cho 2,680 ví. Tất cả đều có trên 1 triệu điểm S1, và mỗi ví nhận đúng ~20% số điểm S2 của mình. Đây là boost +20% cho người giữ S1, trả bù hồi tố ([Merkl](https://api.merkl.xyz/v4/campaigns?creatorAddress=0x80c6a512B548229226C0676d6fdbAfF81d325990&items=100&page=0)).
  - Tổng điểm người dùng S2 lên 192.8 tỷ (28/9: 150.2 tỷ). Nguồn cung YT-USDat tăng lên 47.2M trên Monad (+9.7%) và 23.7M trên Ethereum (+17.9%).
  - Dự phóng tổng S2 tại 8/12 nâng từ 397 lên **~453 tỷ** (biên độ 420–553 tỷ). Do đó 1M điểm chỉ còn đáng ~$11.0 ở FDV $100M, thay vì $12.6.
- **Rủi ro hạn mức ngân sách nhẹ hơn mình đã viết.**
  - Theo tài liệu Merkl, ngân sách chiến dịch FIX_APR là trần tính dồn: hết thì kết thúc sớm ([Merkl docs](https://docs.merkl.xyz/merkl-mechanisms/distributions)).
  - Phần còn lại đủ trả 30× cho trung bình ~71.8M YT trên Monad và ~39.0M YT trên Ethereum đến 8/12. Nếu nguồn cung YT tăng như 5 ngày qua, ngân sách Ethereum có thể cạn khoảng 30/11 và Monad khoảng 6/12.
- **Thị trường dự đoán dời kỳ vọng TGE ra sau.**
  - Polymarket "ra token trước 31/12/2026" giảm từ 0.74 xuống ~0.62 (mua 0.55 / bán 0.68). Mức "trước 30/6/2027" là 0.795.
  - Thang FDV nhích lên: >$200M 0.50, >$300M 0.37 theo giá giữa, thanh khoản mỏng ([Polymarket](https://gamma-api.polymarket.com/public-search?q=saturn)).
  - Mình chỉnh phân phối TGE thành ~20% trước 15/11, 15% từ 16/11 đến 7/12, 30% trong khoảng 8–31/12 và **35% trượt sang 2027**. FDV cơ sở giữ ở ~$150M.
- **Nền tảng nhích lên.** TVL $152.8M (+4%), USDat $90.2M (+6%). STRC về $99.41, gần mệnh giá, và tỷ giá sUSDat lên 1.0398. Chưa có thông báo tokenomics.

| $1,000, ngày 3/10 | Monad YT-USDat | ETH YT-USDat |
|---|---|---|
| Implied APY · số YT mua được | 8.83% · 40,786 | 9.23% · 39,243 |
| Point S2 đến 8/12 | 77.6M | 74.7M |
| Chi phí ròng (USDC đến snapshot, MON đến 15/10) | $758 | $798 |
| $ / 1M point (khoảng) | $9.76 ($8.30–12.47) | $10.68 ($9.23–13.39) |
| FDV hòa vốn thô | $75–113M | $84–121M |
| FDV hòa vốn điều chỉnh rủi ro, đủ S2 / TGE 15/11 | $109–164M / $137–206M | $121–176M / $153–222M |
| Bi quan / cơ sở / lạc quan | −89% / +13% / +262% | −92% / +6% / +226% |
| Monte Carlo: trung bình / trung vị / P(lỗ) | +14% / −14% / 58% | 0% / −27% / 65% |

| Implied APY Monad YT-USDat | 6% | 7% | 8% | 8.83% (hiện tại) | 10% |
|---|---|---|---|---|---|
| MC trung bình / trung vị | +65% / +25% | +42% / +8% | +25% / −5% | +14% / −14% | +1% / −23% |

**Hành động đề xuất:**
- Đặt lệnh giới hạn mua Monad YT-USDat ở implied APY ≤ 8% (giá YT ≤ ~$0.0214) cho phần thử. Phần chính đặt ở ≤ 7% (≤ ~$0.0188).
- Giữ tổng vị thế ≤ 1–2% danh mục, mỗi lệnh ≤ $10k (trượt giá $10k ~5.8%; $50k ~37%).
- Theo dõi ba tín hiệu:
  - MON có được gia hạn sau 15/10 không.
  - Nguồn cung YT so với ngân sách Merkl còn lại.
  - Saturn có công bố tokenomics/ngày TGE không. TGE trước 15/11 làm FDV hòa vốn lên $137–206M.

---

## Phân tích gốc (dữ liệu 28–29/9/2026)

Trong bảy pool YT của Saturn trên Pendle, chỉ có **YT-USDat (Ethereum hoặc Monad)** có chi phí điểm đủ rẻ để cân nhắc, và ngay cả pool này cũng chỉ đáng một **vị thế nhỏ**. Ở implied APY hiện tại là 8.98%, mức cao nhất trong lịch sử pool, $1,000 mua được khoảng 39,150 YT. Số YT đó kiếm khoảng **1.12 triệu Orbital Points mỗi ngày**, tức **~80 triệu điểm** đến khi Season 2 kết thúc vào 8/12/2026. Chi phí ròng là $675–1,000 tùy khoản thưởng USDC 3% còn kéo dài bao lâu, tương đương **$8.4–12.5 cho mỗi 1 triệu điểm**. Sau khi trừ phí Pendle 5%, trượt giá, áp lực bán và vesting, cùng xác suất không có token, FDV hòa vốn thực tế là **$98–145 triệu** nếu Season 2 chạy đủ. Nếu TGE rơi vào giữa tháng 11 và Season 2 bị cắt sớm theo tỷ lệ, con số này lên **$122–180 triệu**. Kịch bản cơ sở của tôi, vốn nghiêng về phía bi quan, đặt FDV ngày TGE quanh **$150 triệu**; trung vị trên Polymarket là khoảng $207 triệu. Mô phỏng Monte Carlo cho $1,000 YT-USDat trên Ethereum cho **lợi nhuận kỳ vọng +15%, nhưng trung vị là −17% và xác suất lỗ là 59%**. Đây là một tấm vé số có kỳ vọng dương mỏng chứ không phải cơ hội rõ ràng. Nếu vào lệnh ở implied APY ≤7%, kỳ vọng tăng lên +46% và trung vị lên +5%. TGE của token STRN được công bố là "Q4 2026". Kịch bản trung tâm của tôi là **đầu đến giữa tháng 12/2026**, với khoảng 45% khả năng TGE trước 8/12 và khoảng 25% khả năng trượt sang 2027. Bối cảnh chung không thuận lợi. Nguồn cung stablecoin đi ngang, không có TGE stablecoin nào trong Q3/2026, và bốn trong năm dự án so sánh chính đã mất 71–96% so với giá mở cửa. Bản thân Saturn chỉ có TVL $147 triệu, giảm 31% từ đỉnh, và khoảng ba phần tư lượng USDat lưu hành đang nằm trong Pendle. Nên tránh YT-sUSDat, YT-USDat trên BNB và YT-srUSDat.

*Quy ước: số liệu dùng dấu chấm thập phân và dấu phẩy phân cách hàng nghìn; ngày viết theo ngày/tháng. Dữ liệu thị trường Pendle, Merkl và on-chain được chốt vào 28–29/9/2026. Các phép tính, kịch bản và xác suất không kèm nguồn là ước tính của tôi, được dựng từ các số liệu có trích dẫn.*

## Saturn là lớp bọc STRC $147 triệu, sống chủ yếu nhờ dòng vốn săn điểm

Saturn (tài khoản X @saturn_credit, tên hiển thị "Saturn Foundation", đăng ký tại Cayman) phát hành hai token. Token thứ nhất là **USDat**, một stablecoin mint có cấp phép. USDat được bảo chứng 1:1 bằng $M của M0 cho đến 19/8/2026; từ ngày đó toàn bộ phần bảo chứng chuyển sang **PYUSDx**, một lớp bọc PYUSD của PayPal/Paxos ([Yearn risk report](https://github.com/yearn/risk-score/blob/master/reports/report/saturn-usdat.md); [Crowdfund Insider](https://www.crowdfundinsider.com/2026/09/308714-paypal-moonpay-and-m0-take-pyusdx-live-as-devs-launch-pyusd-backed-stablecoins/)). Từ khoảng 9/9, USDat trả **3% APR** dưới dạng thưởng ([Coinfomania](https://coinfomania.com/saturn-credit-announces-3-apr-for-usdat-whale-activity/); [Pendle API](https://api-v2.pendle.finance/core/v2/1/markets/0x4ccf6deb3d1895373f604b418ff55d8adae8b846/data)). Token thứ hai là **sUSDat**, một vault ERC-4626 nắm 100% cổ phiếu ưu đãi vĩnh viễn STRC của Strategy. NAV của sUSDat được định giá theo giá thị trường của STRC, và việc rút tiền đi qua hàng chờ 3–7 ngày, trong đó Saturn bán STRC trên thị trường thứ cấp ([Saturn docs](https://saturncredit.gitbook.io/saturn-docs/solution/susdat-overview/staking-and-unstaking-process)). STRC hiện trả cổ tức **12%/năm** ([SEC 8-K](https://www.sec.gov/Archives/edgar/data/0001050446/000119312526377583/mstr-20260831.htm)). Tuy vậy, giá STRC đã rơi xuống đáy trong phiên **$71.25 vào tháng 6/2026** ([Yahoo Finance](https://query1.finance.yahoo.com/v8/finance/chart/STRC?range=6mo&interval=1wk); [CoinDesk](https://www.coindesk.com/markets/2026/06/18/strategy-s-strc-preferred-stock-hits-a-record-low-below-par)). Trong đợt đó, tỷ giá sUSDat giảm **15.7%**, từ 1.0094 (15/5) xuống 0.8511 (1/7). Tính từ khi ra mắt đến 28/9, sUSDat chỉ tăng **3.05%, tương đương khoảng 6.3%/năm**, thấp hơn nhiều so với các con số APY 13.6–16.4% đang được quảng bá ([hợp đồng sUSDat](https://etherscan.io/address/0xD166337499E176bbC38a1FBd113Ab144e5bd2Df7)). Ngày 4/6, Saturn tuyên bố sản phẩm "không bị ảnh hưởng" ([Bitget News](https://www.bitget.com/news/detail/12560605443262)). Câu đó đúng với peg của USDat nhưng sai với NAV của sUSDat, và đây là một điểm trừ về độ tin cậy của đội ngũ.

Về quy mô, TVL trên DefiLlama tăng từ $33 triệu (9/4) lên **đỉnh $214.1 triệu (9/6)**, rồi giảm còn **$146.9 triệu (28/9)**. Trong con số hiện tại có $85.0 triệu PYUSDx và $61.9 triệu STRC ([DefiLlama](https://api.llama.fi/protocol/saturn)). NAV của sUSDat co từ $105.9 triệu (22/5) xuống $66.1 triệu, và lượng STRC nắm giữ giảm 23% so với con số Saturn công bố hồi tháng 8 ([sUSDat contract](https://etherscan.io/address/0xD166337499E176bbC38a1FBd113Ab144e5bd2Df7); [Saturn docs S2](https://saturncredit.gitbook.io/saturn-docs/overview/orbital-points-season-2)). Ngược lại, USDat hồi phục sau khi có APR 3% và thông báo TGE: lưu hành đạt **$84.8 triệu**, trong đó Monad ($45.1 triệu) đã vượt Ethereum ($39.7 triệu) ([DefiLlama stablecoins](https://stablecoins.llama.fi/stablecoin/400)).

Điểm đáng lo nhất là thành phần của dòng vốn này. Nguồn cung YT-USDat kỳ hạn 14/1/2027 là **20.13 triệu trên Ethereum** và **43.02 triệu trên Monad** ([Etherscan](https://etherscan.io/token/0x480c3c9470fa4bbda030f6396fa4b17adefc1ce0); [Monadscan](https://monadscan.com/token/0x5aff25c86c7cb739e554be8904b32047738b7440)). Mỗi YT tương ứng với 1 USDat bị khóa trong Pendle. Như vậy khoảng **63 triệu, tức ~74% USDat lưu hành, đang nằm trong Pendle**; riêng trên Monad tỷ lệ này là ~95%. Ngoài ra còn $23.9 triệu PT-USDat làm tài sản thế chấp trên Morpho Monad ([DefiLlama yields](https://yields.llama.fi/pools)). Tôi suy ra rằng phần lớn cầu USDat là cầu săn điểm, nên có thể rút mạnh sau snapshot hoặc sau ngày đáo hạn 14/1. Tiền lệ gần nhất là USDO của OpenEden, giảm 62% trong 60 ngày sau TGE ([DefiLlama USDO](https://stablecoins.llama.fi/stablecoin/241)).

Đội ngũ gồm Kevin Li (CEO) và Ellis Osborn. Số vốn công bố chỉ khoảng **$2.8 triệu**: vòng pre-seed $800K từ YZi Labs và Sora ([Bitcoin Magazine](https://bitcoinmagazine.com/press-releases/saturn-raises-800k-from-yzi-labs-and-sora-ventures-to-build-usdat-a-11-yield-bearing-stablecoin-protocol-backed-by-strategys-digital-credit)), vòng seed $2M do The Spartan Group dẫn cùng Anchorage và Susquehanna ([PANews](https://panews.io/articles/019e053a-b407-7429-8c0e-4c1f9d4d90e8)), cộng thêm một khoản đầu tư chiến lược không công bố số tiền từ Ondo ([CryptoRank](https://cryptorank.io/insights/deals/saturn-protocol-strategic-2026-08-13)). Không có định giá nào được công bố. Về rủi ro kỹ thuật, Yearn chấm **3.15/5 ("Medium Risk")** và ghi nhận rằng năm bản audit đã công bố đều không bao quát kiến trúc PYUSDx đang chạy ([Yearn PR #455](https://github.com/yearn/risk-score/pull/455)). Innora đã công khai lỗi Critical SAT-001, có thể đóng băng tới ~$35.7 triệu, và lỗi High SAT-002, nhưng chưa có phản hồi công khai nào từ Saturn. Saturn cũng không có bug bounty ([Innora](https://gist.github.com/sgInnora/b70ad98327649ed4ab976a122f45e485)).

Cần phân biệt tổng lợi suất Saturn tạo ra với phần giao thức thực sự giữ lại. Theo ước tính của tôi, tổng lợi suất tạo ra khoảng **$11 triệu/năm**, gồm khoảng $3.6 triệu từ dự trữ USDat (lợi suất T-bill 4.24% trên $85 triệu, [FRED](https://fred.stlouisfed.org/series/DGS3MO)) và khoảng $7.4 triệu cổ tức STRC (12% trên $62 triệu). Ở FDV $150 triệu, bội số là khoảng 14 lần tổng phí, tương đương ENA (18.6×) và RESOLV (13×) lúc TGE, và thấp hơn nhiều so với USUAL (88×) hay EDEN (72×). Tuy nhiên, gần như toàn bộ khoản này được trả lại cho người nắm giữ. Phần giao thức giữ lại chỉ khoảng **$1–2 triệu/năm**: khoảng $1 triệu chênh lệch giữa lợi suất T-bill và 3% trả cho người giữ USDat, cộng khoảng $0.8 triệu từ phí 10% trên lợi suất sUSDat, khoản phí hiện đang được hoàn lại toàn bộ ([Saturn docs](https://saturncredit.gitbook.io/saturn-docs/operations-and-governance/fees-and-risk-reserve)). Vì vậy, định giá STRN sẽ dựa vào kỳ vọng tăng trưởng nhiều hơn là dòng tiền hiện tại. Về cộng đồng, thread TGE ngày 25/9 đạt ~144k lượt xem, cao bất thường so với một tài khoản 12.9k follower ([fxtwitter](https://api.fxtwitter.com/saturn_credit/status/2103290807847645584)). Nội dung từ KOL chủ yếu là hướng dẫn cày điểm, và kênh Discord/Telegram không truy cập được vì yêu cầu đăng nhập.

## Các stablecoin đã TGE cho thấy STRN khó được định giá trên ~1× TVL

Năm dự án so sánh chính đều mở cửa ở **1.8–5.5 lần nguồn cung stablecoin** tại thời điểm TGE. Đến nay, bốn trong năm dự án đã mất 71–96% so với giá mở cửa; chỉ Ethena giữ được tương đối (−54%). Lứa TGE nửa đầu 2026 được định giá dè dặt hơn nhiều (khoảng 1.3× TVL) và cũng giữ giá tốt hơn.

| Dự án | TGE | Stablecoin/TVL lúc TGE | FDV mở cửa/ngày 1 | FDV/TVL | Airdrop điểm | Hiện tại so với mở cửa |
|---|---|---|---|---|---|---|
| Ethena (ENA) | 4/2024 | $1.56B | $8.55B | 5.5× | 5% (S1) | −54% |
| Usual (USUAL) | 11/2024 | $375M | $1.45B | 3.9× | 8.5% | −96% |
| Resolv (RESOLV) | 6/2025 | $217M | $384M | 1.8× | 10% (S1) | −95% |
| OpenEden (EDEN) | 9/2025 | $235M | $843M | 3.6× | 7.5% | −93% |
| Falcon (FF) | 9/2025 | $1.90B | $4.53B | 2.4× | ≤8.3% (gồm cả sale) | −71% |
| Unitas (UP) | 3/2026 | $81M | $72M | 0.9× | n/d | +224% |
| USD.AI (CHIP) | 4/2026 | $284M | $612M | 2.2× | 3% | −30% |
| Solstice (SLX) | 5/2026 | $398M | $207M | 0.5× | ~7.5–8% | −61% |
| Re (RE) | 6/2026 | $258M | $437M | 1.7× | n/d | +1% |
| Cap (CAP) | 6/2026 | $221M | $289M | 1.3× | stabledrop cUSD | +93% |
| **Saturn (STRN)** | **Q4/2026 (dự kiến)** | **$147M TVL; USDat $85M** | **Polymarket trung vị ~$207M; cơ sở của tôi ~$150M** | **~1.0×** | **5% S1 + 5% S2** | — |

Nguồn: năm dòng đầu dùng giá mở cửa là VWAP giờ đầu trên Binance ([Binance klines ENA](https://data-api.binance.vision/api/v3/klines?symbol=ENAUSDT&interval=1d), [USUAL](https://data-api.binance.vision/api/v3/klines?symbol=USUALUSDT&interval=1d), [RESOLV](https://data-api.binance.vision/api/v3/klines?symbol=RESOLVUSDT&interval=1d), [EDEN](https://data-api.binance.vision/api/v3/klines?symbol=EDENUSDT&interval=1d), [FF](https://data-api.binance.vision/api/v3/klines?symbol=FFUSDT&interval=1d)) và nguồn cung lấy từ [DefiLlama stablecoins](https://stablecoins.llama.fi/stablecoin/146). Lứa 2026 dùng giá đóng cửa ngày đầu (DefiLlama/Gate) và so với giá DefiLlama đầu tiên ([DefiLlama coins](https://coins.llama.fi/chart/coingecko:cap-4); [re.xyz](https://re.xyz/insights/re-tge-launch); [usd.ai](https://usd.ai/insights/chip-is-live); [MEXC News](https://www.mexc.com/news/1112452)).

Bảng này cho thấy một quy luật rõ: dự án nào có nguồn cung **tiếp tục tăng sau TGE** thì giữ được FDV, còn dự án TGE khi nguồn cung đã co lại thì giảm mạnh nhất. Ethena và Falcon tăng nguồn cung trong 1–3 tháng sau TGE nhờ các mùa điểm tiếp theo. Ngược lại, Resolv TGE khi USR đã giảm 63% từ đỉnh ([DefiLlama USR](https://stablecoins.llama.fi/stablecoin/197)), còn USDO của OpenEden mất 94% kể từ TGE ([DefiLlama USDO](https://stablecoins.llama.fi/stablecoin/241)). Saturn gần với nhóm thứ hai hơn: TVL đã giảm 31% từ đỉnh, và phần tăng trưởng gần đây đến từ YT săn điểm. Theo Memento Research, stablecoin là một trong những nhóm tệ nhất năm 2025 với mức giảm trung bình **−70%**. Các dự án TGE trên $1 tỷ FDV có **0%** xác suất tăng giá sau niêm yết, trong khi nhóm $25–200 triệu có tỷ lệ tăng giá 40% ([Memento](https://mementoresearch.com/state-of-2025-token-launches-year-in-review); [The Defiant](https://thedefiant.io/news/research-and-opinion/token-launches-with-low-fdvs-vastly-outperformed-hyped-debuts-in-2025-memento-research)).

Xu hướng stablecoin đang chững lại, và dữ liệu ủng hộ nhận định đó. Tổng nguồn cung stablecoin USD đi ngang quanh **$300–318 tỷ từ tháng 10/2025** và hiện ở $311.5 tỷ ([DefiLlama](https://stablecoins.llama.fi/stablecoincharts/all)). Tháng 6/2026 chứng kiến mức giảm theo tháng lớn nhất trong bốn năm, $7.7 tỷ ([CoinDesk](https://www.coindesk.com/markets/2026/07/12/stablecoin-market-cap-has-shrunk-by-usd10-billion-since-may-but-analyst-sees-no-reason-to-panic)). Nhóm stablecoin sinh lợi co lại mạnh nhất: USDe giảm 66% từ đỉnh, USD0 giảm 66%, USDf giảm 41%, còn USR gần như biến mất ([DefiLlama stablecoins](https://stablecoins.llama.fi/stablecoins)). Ethena cũng dừng ưu đãi token cho USDe từ cuối tháng 9 ([CryptoBriefing](https://cryptobriefing.com/ethena-ends-usde-token-incentives/)). Trong Q3/2026 không có TGE stablecoin nào được ghi nhận. Avant trượt khỏi mục tiêu giữa tháng 9 ([Bitget News](https://www.bitget.com/news/detail/12560605409666)), Apyx hoãn TGE dự kiến 13/10 ([ChainCatcher](https://www.chaincatcher.com/en/article/2291854)), và infiniFi dời sang Q4 ([PR Newswire](https://www.prnewswire.com/news-releases/infinifi-raises-3m-ahead-of-q4-tge-302887464.html)). Bối cảnh vĩ mô cũng bất lợi cho định giá. Fed tăng lãi suất 25bp lên 3.75–4.00% vào 16/9 ([Federal Reserve](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm)), lợi suất 10 năm đạt 5.18% ([FRED](https://fred.stlouisfed.org/series/DGS10)), và BTC dù hồi mạnh từ vùng $60k vẫn thấp hơn 22.6% so với cùng kỳ năm trước ([Fortune](https://fortune.com/article/price-of-bitcoin-09-25-2026/)).

Để suy ra FDV, tôi đối chiếu ba nguồn. Nguồn thứ nhất là thị trường dự đoán: Polymarket "Saturn FDV one day after launch" có giá Yes là 0.885 cho mốc >$50M, 0.65 cho >$100M, 0.46 cho >$200M và 0.26 cho >$300M ([Polymarket](https://gamma-api.polymarket.com/public-search?q=saturn)). Sau khi chia cho xác suất ra token, thị trường này ngụ ý **trung vị ~$207 triệu, khoảng tứ phân vị $96–331 triệu**. Tuy nhiên tổng khối lượng giao dịch chỉ khoảng $21.6k, và các mốc >$200M và >$300M đã giảm 6 và 12 điểm trong một tháng. Nguồn thứ hai là bội số so sánh: $147 triệu TVL nhân với trung vị FDV/TVL 1.27× của tám nhà phát hành stablecoin gần đây cho ra **~$186–192 triệu**, với biên độ $53–315 triệu. Nguồn thứ ba là các yếu tố riêng của Saturn kéo định giá xuống: TVL đang co, doanh thu nhỏ, rủi ro tập trung vào STRC, và vốn gọi được rất nhỏ. Kết hợp lại, tôi đặt **FDV ngày TGE cơ sở ~$150 triệu (khoảng 1× TVL)**, bi quan $50–80 triệu và lạc quan $250–350 triệu. Trong mô phỏng, tôi dùng phân phối lognormal với trung vị $140 triệu, khoảng tứ phân vị $79–247 triệu và trung bình ~$200 triệu, tức cố ý thấp hơn Polymarket khoảng 30%. Sau TGE còn có áp lực bán: trung vị d30 của 12 dự án 2025–2026 là −20%, và của rổ token được farm là −41% ([DefiLlama coins](https://coins.llama.fi/chart/coingecko:ethena)).

## TGE nhiều khả năng rơi vào đầu tháng 12, nhưng Season 2 có 45% khả năng bị cắt sớm

Thông tin chính thức duy nhất là thread của @saturn_credit ngày 25/9. Thread này có năm điểm chính: "$STRN / TGE: Q4 2026"; tối đa 5% tổng cung dành cho Season 2; nếu TGE diễn ra trước 8/12 thì Season 2 "sẽ kết thúc ngay trước đó" và phần phân bổ bị cắt theo tỷ lệ thời gian đã chạy; Season 3 bắt đầu ngay sau snapshot; tokenomics sẽ được công bố sau ([X thread](https://x.com/saturn_credit/status/2103290807847645584)). Polymarket phản ứng mạnh với thông báo này: xác suất ra token trước 31/12/2026 tăng từ khoảng 0.20 lên **0.74**, và trước 30/6/2027 là 0.90 ([Polymarket](https://gamma-api.polymarket.com/public-search?q=saturn)).

Tôi đưa ra phân phối thời điểm TGE dựa trên bốn lập luận. Thứ nhất, việc Saturn tự đưa điều khoản cắt sớm vào thông báo cho thấy đội ngũ nghiêm túc giữ lựa chọn TGE trước 8/12. Thứ hai, đến 25/9 tokenomics, tổng cung và cơ chế claim đều chưa được công bố. Chuỗi công bố tokenomics, rồi sàn niêm yết, rồi claim thường mất 4–8 tuần, nên TGE sớm nhất thực tế là khoảng đầu đến giữa tháng 11. Thứ ba, dự án tương đồng nhất là Apyx, cũng dựa vào STRC, đã hoãn TGE với lý do STRC trải qua đợt giảm "sâu nhất và dài nhất" ([ChainCatcher](https://www.chaincatcher.com/en/article/2291854)). STRC vẫn dưới mệnh giá và chương trình ATM của Strategy đang tạm dừng ([CoinDesk](https://www.coindesk.com/markets/2026/09/01/strategy-spends-usd635m-buying-back-strc-as-perpetual-preferred-stock-lags-usd100-par)). Thứ tư, năm 2026 có nhiều vụ hoãn TGE với lý do điều kiện thị trường (Avant, Apyx, OpenSea).

| Khung TGE | Xác suất (ước tính) | Hệ quả với người mua YT hôm nay |
|---|---|---|
| Trước 15/11 (snapshot khoảng 1/11–15/11) | ~30% | Chỉ nhận 32–48 ngày điểm S2 thay vì 71.7 ngày; pool S2 còn 68–80% của 5% |
| 16/11–7/12 | ~15% | Mất tới khoảng 23 ngày điểm; pool còn khoảng 81–99% |
| 8/12–31/12 | ~30% | Nhận đủ Season 2 và đủ 5%; khoảng 36 ngày điểm S3 trước ngày đáo hạn 14/1 |
| Trượt sang 2027 | ~25% | Vẫn đủ S2 (kết thúc 8/12), nhưng chờ token lâu hơn và rủi ro định giá, thay đổi luật cao hơn |

Tổng xác suất TGE trong năm 2026 theo bảng trên là 75%, khớp với mức 74% của Polymarket. Kịch bản trung tâm là **đầu đến giữa tháng 12/2026**. Tôi cố ý đặt trọng số cao cho TGE sớm vì đây là kịch bản bất lợi nhất với người mua YT: YT đã trả tiền cho quyền lợi đến 14/1, nhưng điểm Season 2 dừng sớm.

## Mỗi YT-USDat nhận 30 điểm/ngày và chia nhau 5% nguồn cung

Trong chương trình điểm, 1× nghĩa là 1 điểm cho mỗi $1 mỗi ngày, tính theo thời gian nắm giữ trên Merkl. YT-USDat có hệ số **30×** trên cả ba chain, YT-sUSDat là 10×, YT-srUSDat là 15×, LP USDat 15×, Curve 25× và giữ USDat 5× ([Saturn Allocations](https://saturncredit.gitbook.io/saturn-docs/overview/allocations); [Merkl campaigns](https://api.merkl.xyz/v4/campaigns?creatorAddress=0x80c6a512B548229226C0676d6fdbAfF81d325990&items=100&page=0)). Một điểm kỹ thuật quan trọng: điểm của YT được tính trên **1 USDat danh nghĩa cho mỗi YT**, không tính trên giá thị trường của YT. Merkl định giá YT theo USDat, và phân phối thực tế cũng xác nhận điều này. Ví dụ, một ví nắm 3.24 triệu YT đang nhận khoảng 97 triệu điểm/ngày ([Merkl rewards](https://api.merkl.xyz/v4/rewards/?chainId=1&campaignId=0xc1e3cc5480ae78be877d38dc1058a6b2cbc0d82d074e71f4ded2122df849eb81&items=100)). Giao diện Merkl hiển thị "TVL" của YT theo giá thị trường nên đánh giá thấp lượng điểm thật khoảng 40 lần ([Merkl opportunity](https://api.merkl.xyz/v4/opportunities/13354597549279540508)). Pendle thu **5% toàn bộ lợi suất của YT, kể cả điểm** ([Pendle docs](https://docs.pendle.finance/pendle-v2/ProtocolMechanics/Mechanisms/Fees)). Vì vậy tôi tính **28.5 điểm/YT/ngày** cho người mua mới, không có boost.

Season 1 (Gravity Points, 8/4–8/8/2026) đã khép lại với khoảng **474–497 tỷ điểm** trên 8,100 ví, dành tối đa 5% "nguồn cung ban đầu" ([Merkl Gravity total](https://api.merkl.xyz/v4/rewards/token/total?chainId=1&address=0xD223bbdd0421E394C0df9dFfe568f1dADfFd6f85); [Bitget News](https://www.bitget.com/news/detail/12560605400930)). Season 2 (Orbital Points, 9/8–8/12/2026) dành tối đa 5% "tổng cung" và đang có **~150–156 tỷ điểm** trên 8,002 ví ([Merkl Orbital total](https://api.merkl.xyz/v4/rewards/token/total?chainId=1&address=0x10710501778b7FAf9e478f36FaE0B286C028eDE8)). Tốc độ phát hành hiện tại là khoảng **2.8 tỷ điểm/ngày ở hệ số gốc, và 2.8–3.4 tỷ/ngày khi tính cả boost**. Boost gồm +20% cho các ví có hơn 1 triệu điểm S1, +10% cho người giới thiệu và +5% cho người được giới thiệu ([Saturn S2 docs](https://saturncredit.gitbook.io/saturn-docs/overview/orbital-points-season-2); [Gravity terms](https://saturn.credit/legal/gravity-program)). Nếu tốc độ này giữ nguyên, tổng điểm S2 vào 8/12 sẽ ở mức **350–400 tỷ**, tức lượng điểm gấp khoảng 2.3–2.6 lần so với hiện nay. Riêng YT-USDat đã chiếm **60.7% số điểm S2** tính đến nay, 10 ví lớn nhất nắm 41.4%, và ví lớn nhất nắm 12.5% ([Merkl leaderboard](https://api.merkl.xyz/v4/rewards/token/?chainId=1&address=0x10710501778b7FAf9e478f36FaE0B286C028eDE8&items=100&page=0)). Nói cách khác, thị trường YT-USDat quyết định phần lớn nền kinh tế điểm của Saturn. Người mua YT-USDat mới không có boost S1 sẽ bị pha loãng bởi những người cày lâu năm có boost.

Quy tắc cắt sớm theo tỷ lệ có một tính chất ít người để ý. **Giá trị mỗi điểm gần như không đổi theo ngày TGE**, vì pool token và tổng điểm cùng co lại theo tỷ lệ. Ở FDV $100 triệu với tốc độ phát hành cơ sở, mỗi 1 triệu điểm đáng $12.87 nếu snapshot vào 1/11, $12.74 nếu vào 15/11 và $12.60 nếu vào 8/12 (tính toán của tôi). Thứ bị cắt là **số điểm của người mua YT**. Nếu TGE giữa tháng 11, người mua hôm nay chỉ nhận 53 triệu điểm thay vì 80 triệu cho mỗi $1,000, trong khi giá YT đã trả không đổi.

Hạn mức ngân sách trên Merkl là rủi ro pha loãng thứ hai. Chiến dịch YT-USDat trên Ethereum có ngân sách 97 tỷ điểm cho 121.5 ngày, tức khoảng 798 triệu/ngày. Mức đó chỉ đủ trả 30× cho **~26.6 triệu YT**, trong khi nguồn cung hiện là 20.1 triệu (76% hạn mức). Trên Monad, ngân sách 194 tỷ đủ cho **~53.0 triệu YT**, và nguồn cung hiện là 43.0 triệu (81%) ([Merkl campaigns](https://api.merkl.xyz/v4/campaigns?creatorAddress=0x80c6a512B548229226C0676d6fdbAfF81d325990&items=100&page=0)). Tiền lệ đã có: ba chiến dịch YT-USDat kỳ hạn tháng 8 trên Ethereum đều trả đúng 100% ngân sách, tức đã chạm trần, và Saturn phải bơm thêm 94 tỷ điểm vào ngày 15/6. Nếu nguồn cung YT vượt hạn mức, số điểm mỗi YT nhận được sẽ giảm tỷ lệ thuận. Trong kịch bản bi quan, tôi dùng hệ số 0.92.

Season 3 là phần thưởng khó định giá nhất. Nếu S2 kết thúc 8/12, YT còn khoảng 36 ngày đến đáo hạn; nếu TGE sớm, con số này là 60–75 ngày. Tỷ lệ phân bổ, hệ số và việc YT có tiếp tục đủ điều kiện ở S3 hay không đều chưa được công bố. Điểm S3 cũng sẽ được chia *sau* TGE, khi token đã giao dịch và thường đã giảm giá. Vì vậy tôi định giá mỗi điểm S3 bằng 0–60% điểm S2, với mức cơ sở 30%.

### Đối chiếu các con số mâu thuẫn giữa các ghi chú

| Vấn đề | Các con số khác nhau | Con số tôi dùng và lý do |
|---|---|---|
| FDV hòa vốn của YT-USDat | ~$55M (ghi chú điểm) so với ngụ ý $12.5/1M điểm (ghi chú Pendle) | **$67–99M thô; $98–145M sau điều chỉnh rủi ro**. Con số $55M dùng giá giữa sổ, bỏ qua phí Pendle 5% và trượt giá ~2%, và giả định USDC 3% chạy đến đáo hạn. Đó là trường hợp tốt nhất, không phải trường hợp kỳ vọng. |
| Quy tắc cắt sớm Season 2 | Một ghi chú xem là "nguồn cộng đồng, chưa xác minh" | **Chính thức**: câu chữ được lấy nguyên văn từ thread @saturn_credit ngày 25/9 ([X](https://x.com/saturn_credit/status/2103290807847645584)) và được KuCoin, ChainCatcher, Bloomingbit đưa lại. |
| Thưởng USDC 3% cho YT-USDat | Chương trình $32k ($8k/tuần) chạy 27/8–27/9 ([TradingView](https://www.tradingview.com/news/coinmarketcal:9fe81b1c1094b:0-pendle-usdat-yt-incentives-support-the-rollover-27-aug-2026-to-27-sep-2026/)) so với APR 3% của USDat từ 9/9 | Tôi cho rằng đây là **APR 3% của chính USDat chảy qua cho YT**. Lý do: khoản thưởng bắt đầu đúng ngày 9/9, xuất hiện ở cả Ethereum lẫn Monad, và vẫn hiển thị 3.00% vào 28/9, sau khi chương trình $32k đã hết ([Pendle history](https://api-v2.pendle.finance/core/v3/1/markets/0x4ccf6deb3d1895373f604b418ff55d8adae8b846/historical-data?time_frame=day)). Không có tài liệu chính thức nào nói nó kéo dài bao lâu, nên tôi mô hình ba nhánh: dừng ngay 25%, kéo dài đến snapshot 35%, kéo dài đến đáo hạn 40%. Pool BNB hiện không có khoản thưởng này. |
| Đỉnh TVL | $214.1M theo DefiLlama; ~$248M theo Saturn; "$220M+ tiền gửi" theo CryptoTimes | **$214.1M** vì dữ liệu kiểm chứng được. Con số tự báo cáo có thể đã gồm các lớp bọc hoặc đếm trùng. |
| Phí YT của Pendle | 5% (tài liệu Pendle) so với 3% (nguồn thứ cấp) | **5%** theo tài liệu gốc ([Pendle docs](https://docs.pendle.finance/pendle-v2/ProtocolMechanics/Mechanisms/Fees)). Nếu thực tế là 3%, chi phí mỗi điểm giảm khoảng 2%. |
| Tổng điểm S2 hiện tại | 150.2 tỷ (cấp token) so với 156.1 tỷ (tổng theo từng chiến dịch) | **153 tỷ**, lấy điểm giữa. |
| APY của sUSDat | 13.6–16.4% (DefiLlama/Pendle) so với 6.3–6.4%/năm thực tế | Kịch bản 0% / 8% / 12%. Con số quảng bá bị thổi phồng bởi đợt STRC hồi về mệnh giá. |
| Điểm LP tính trên toàn bộ giá trị hay chỉ phần SY | Chưa rõ trong ghi chú Pendle | **Toàn bộ giá trị LP**: TVL trên Merkl bằng thanh khoản pool ([Merkl](https://api.merkl.xyz/v4/opportunities/6928984681703931525)). |
| YT-srUSDat trên Monad | Tài liệu chỉ liệt kê Ethereum; Merkl có chiến dịch trên Monad | Nhiều khả năng có điểm nhưng chưa được xác nhận; tôi loại khỏi khuyến nghị. |

## YT-USDat cho điểm rẻ hơn YT-sUSDat 4–6 lần

Bảng dưới dùng báo giá khớp được thật từ API convert của Pendle cho lệnh $1,000 (đã gồm phí swap và trượt giá), phí Pendle 5%, và giả định người mua không có boost ([Pendle convert API](https://api-v2.pendle.finance/core/v3/sdk/1/convert); [Pendle market API](https://api-v2.pendle.finance/core/v1/1/markets/0x4ccf6deb3d1895373f604b418ff55d8adae8b846)).

| Pool (hệ số) | Thanh khoản pool | Implied APY | Giá YT | YT/$1k khớp được | Điểm/ngày/$1k | Điểm đến 8/12 (71.7 ngày) | Điểm nếu snapshot 15/11 (47.7 ngày) |
|---|---|---|---|---|---|---|---|
| ETH YT-USDat (30×) | $1.96M | 8.98% | $0.02502 | 39,151 | **1.116M** | **80.0M** | 53.2M |
| Monad YT-USDat (30×) | $1.47M | 9.10% | $0.02532 | 38,125 | 1.087M | 77.9M | 51.8M |
| BNB YT-USDat (30×) | $0.04M | 8.29% | $0.02317 | không khớp được $1k ($500 → 14,882) | 0.848M* | 60.8M* | 40.5M* |
| ETH YT-sUSDat (10×) | $1.35M | 12.92% | $0.03506 | 27,470 | 0.261M | 18.7M | 12.4M |
| Monad YT-sUSDat (10×) | $1.61M | 17.41% | $0.04605 | 21,223 | 0.202M | 14.5M | 9.6M |
| ETH YT-srUSDat (15×) | $0.23M | 10.20% | $0.02821 | 31,648 (trượt giá −10.7%) | 0.451M | 32.3M | 21.5M |
| Monad YT-srUSDat (15×?) | $0.36M | 10.41% | $0.02875 | 32,325 | 0.461M? | 33.0M? | — |

*BNB được quy đổi từ lệnh $500. Nguồn thị trường: [Pendle Monad USDat](https://api-v2.pendle.finance/core/v1/143/markets/0x88c5d8a908834e44b421cb67aec9a931782f9538), [Pendle Monad sUSDat](https://api-v2.pendle.finance/core/v1/143/markets/0x22c2967cc989c313c8c3f205468a11f40f0a95f7), [Pendle markets/all](https://api-v2.pendle.finance/core/v1/markets/all?limit=100).*

Bảng thứ hai tính phần lợi suất/thưởng mà YT nhận lại (sau phí 5%), chi phí ròng, chi phí cho mỗi 1 triệu điểm và FDV hòa vốn. Có hai loại FDV hòa vốn. "Thô" là FDV ngày TGE để giá trị điểm S2 vừa bằng chi phí ròng, với giả định S2 chạy đủ, phát hành cơ sở 3.4 tỷ/ngày (tổng 397 tỷ điểm), phân bổ 5%, không chiết khấu và không tính S3. "Điều chỉnh rủi ro" thêm chiết khấu vesting và áp lực bán 30%, xác suất không có token 15%, và giá trị điểm S3 bằng 30% điểm S2.

| Pool | Giả định lợi suất/thưởng | Nhận lại | Chi phí ròng/$1k | $/1M điểm (đến 8/12) | $/1M điểm (snapshot 15/11) | FDV hòa vốn thô | FDV hòa vốn điều chỉnh rủi ro (đủ S2 / TGE 15/11) |
|---|---|---|---|---|---|---|---|
| ETH YT-USDat | USDC dừng ngay | $0 | $1,000 | $12.50 | $18.79 | $99M | $145M / $180M |
| ETH YT-USDat | USDC đến snapshot | $217 | $783 | $9.79 | $16.08 | $78M | $114M / $141M |
| ETH YT-USDat | USDC đến 14/1 | $325 | $675 | $8.43 | $12.68 | $67M | $98M / $122M |
| Monad YT-USDat | USDC dừng ngay / đến snapshot / đến 14/1 | $0 / $211 / $317 | $1,000 / $789 / $683 | $12.84 / $10.13 / $8.77 | $19.29 / $16.59 / $13.18 | $102M / $80M / $70M | Đủ S2: $149M / $118M / $102M; TGE 15/11: $185M / $146M / $126M |
| BNB YT-USDat ($500) | không có USDC | $0 | $500 cho 30.4M điểm | $16.44 | $24.71 | $131M | $191M / $237M |
| ETH YT-sUSDat | lợi suất 0% / 6.4% / 8% / 12% | $0 / $481 / $598 / $886 | $1,000 / $519 / $402 / $114 | $53.4 / $27.7 / $21.5 / $6.1 | $80.3 (lợi suất 0%) | $424M / $220M / $170M / $48M | $620M / $322M / $249M / $71M (đủ S2) |
| Monad YT-sUSDat | 0% / 6.4% / 8% / 12% | $0 / $372 / $462 / $684 | $1,000 / $628 / $538 / $316 | $69.2 / $43.4 / $37.1 / $21.8 | $104 (lợi suất 0%) | $549M / $345M / $295M / $173M | $803M / $504M / $432M / $253M (đủ S2) |
| ETH YT-srUSDat | 6% / 7.5% / 8.11% | $520 / $647 / $698 | $480 / $353 / $302 | $14.8 / $10.9 / $9.3 | $46.5 (lợi suất 0%) | $118M / $87M / $74M | $172M / $127M / $108M (đủ S2) |

Hai kết luận rút ra từ các bảng trên. Thứ nhất, **YT-sUSDat không phải công cụ cày điểm mà là cược đòn bẩy vào NAV của STRC**. Với hệ số chỉ 10× và giá YT cao hơn, chi phí mỗi điểm đắt gấp 4–6 lần YT-USDat, trừ khi STRC giữ được lợi suất ~12%. Rủi ro này đã từng xảy ra: YT-sUSDat kỳ hạn tháng 8 nhận **0% lợi suất từ cuối tháng 5 đến khi đáo hạn**. Nguyên nhân là tỷ giá sUSDat nằm dưới đỉnh cũ, và YT của Pendle chỉ tích lũy lợi suất khi chỉ số vượt đỉnh ghi nhận trước đó. Hiện tỷ giá vẫn thấp hơn đỉnh 22/9 khoảng 0.25% ([Pendle history sUSDat](https://api-v2.pendle.finance/core/v3/1/markets/0x91bc86899c8391b6caaf26535b9cd82efe49a189/historical-data?time_frame=day)). Thứ hai, **YT-USDat đang ở mức đắt nhất lịch sử của nó**. Implied APY trên Ethereum đã đi từ 5.00% lúc mở pool, qua 6.1–6.9% trong tháng 8 và đầu tháng 9, lên 8.98% hiện nay. Đợt tăng này xảy ra khi thanh khoản pool giảm từ $5.94 triệu xuống $1.96 triệu trong giai đoạn 17–27/9 ([Pendle history](https://api-v2.pendle.finance/core/v3/1/markets/0x4ccf6deb3d1895373f604b418ff55d8adae8b846/historical-data?time_frame=day)). Quy mô lệnh cũng làm chi phí tăng. Trên Ethereum, trượt giá là −2.1% cho $1k, −7.4% cho $10k và −16% cho $50k. Trên Monad, lệnh $50k trượt tới −44% ([Pendle convert API](https://api-v2.pendle.finance/core/v3/sdk/143/convert)).

Với người có nhiều vốn, có những cách lấy điểm rẻ hơn mà vẫn giữ được gốc (tính toán của tôi dựa trên hệ số chính thức). **LP Curve USDC/USDat (25×)** cho 1.79 triệu điểm trên mỗi $1,000 đến 8/12. Chi phí cơ hội so với T-bill 4.24% hoặc PT 9% chỉ khoảng **$4.5–9.7 cho mỗi 1 triệu điểm**, nhưng cần khoảng $44.6k vốn để có cùng số điểm mỗi ngày với $1k YT. **Giữ USDat (5×, kèm 3% APR)** tốn khoảng $6.8 cho mỗi 1 triệu điểm so với T-bill. **LP Pendle USDat (15× tính trên toàn bộ giá trị LP)** trả 9.31% APY cộng điểm, tức người cung cấp thanh khoản được trả tiền để cày điểm ([DefiLlama yields](https://yields.llama.fi/pools); [Saturn S2 docs](https://saturncredit.gitbook.io/saturn-docs/overview/orbital-points-season-2)). YT chỉ hợp lý với người vốn nhỏ muốn đòn bẩy điểm và chấp nhận mất toàn bộ số tiền bỏ vào.

## Ma trận kịch bản cho kỳ vọng dương mỏng nhưng trung vị lỗ

Các tham số dưới đây được đặt rộng và nghiêng về phía bi quan. Chúng dựa trên lịch sử các chương trình điểm cày qua Pendle. Theo Keyrock, 88% airdrop giảm giá, phần lớn trong 15 ngày đầu ([Keyrock](https://keyrock.com/airdrops-in-the-barren-desert/)). Điểm Renzo chỉ hiện thực hóa khoảng 27% mức giá trước TGE ([Ouroboros](https://ouroborosresearch.substack.com/p/ouroboros-market-update-3-renzo-airdrop)). Ethena S4 chỉ cho claim ngay 1.5% trong tổng 3.5% ([AirdropAlert](https://airdropalert.com/airdrops/ethena-season-4/)). Cap cắt stabledrop từ $12 triệu xuống $4.2 triệu ([The Defiant](https://thedefiant.io/news/defi/cap-cuts-its-stabledrop-airdrop-to-usd4-2m-from-usd12m-as-backlash-mounts)). SLX giảm hơn 40% chỉ trong vài giờ khi người nhận airdrop đồng loạt bán ([MEXC News](https://www.mexc.com/news/1112452)). Cũng có những trường hợp mất trắng: Level đóng cửa mà không phát token ([Bitget News](https://www.bitget.com/news/detail/12560604988048)), còn Resolv bị hack $80 triệu ([CoinDesk](https://www.coindesk.com/markets/2026/03/23/resolv-stablecoin-drops-70-after-usd80-million-exploit-after-attacker-mints-usr)). Các cơ chế vesting cho ví lớn cũng đáng chú ý. Usual khóa 90% phần của 1.5% ví lớn nhất ([Usual blog](https://usual.money/blog/airdrop-the-genesis-of-ownership)), còn Re trả phần của ví lớn dần trong 3 năm ([re.xyz](https://re.xyz/insights/re-tge-launch)). Điều này liên quan trực tiếp đến người mua YT: một vị thế $10k YT-USDat sẽ kiếm khoảng 0.76 tỷ điểm, đủ để lọt vào nhóm khoảng 100 ví đứng đầu S2 (hiện chỉ có 28 ví trên 1 tỷ điểm), và do đó có thể bị xếp vào nhóm "cá voi" nếu Saturn áp dụng vesting theo tầng.

| Tham số | Bi quan | Cơ sở | Lạc quan | Phân phối Monte Carlo |
|---|---|---|---|---|
| Snapshot S2 / TGE | 15/11 (47.7 ngày điểm) | 8/12 (71.7 ngày) | 8/12 | 10% 1/11; 20% 15/11; 15% 1/12; 30% 8/12; 25% 8/12 nhưng TGE trượt sang 2027 (thêm −20% giá trị) |
| Tốc độ phát hành S2 (tổng điểm lúc snapshot) | 4.5 tỷ/ngày (368 tỷ lúc 15/11; 476 tỷ nếu 8/12) | 3.4 tỷ/ngày (397 tỷ) | 2.8 tỷ/ngày (354 tỷ) | Đều trong khoảng 2.8–5.0 tỷ/ngày |
| Phân bổ S2 ("tối đa 5%") | 4% | 5% | 5% | 80% xác suất là 5%, 20% là 4% |
| FDV ngày TGE | $60M | $150M | $300M | Lognormal trung vị $140M, σ = 0.85 |
| Chiết khấu vesting và áp lực bán | 50% | 30% | 10% | Đều trong khoảng 15–50% |
| Xác suất không có token, sự cố hoặc bị loại | 25% | 15% | 7% | 15% |
| Hệ số hạn mức Merkl | 0.92 | 1.00 | 1.00 | Đều trong khoảng 0.90–1.00 |
| Giá trị điểm S3 so với S2 | 0% | 30% | 60% | Đều trong khoảng 0–50% |
| Thưởng USDC 3% (pool USDat) | Dừng ngay | Đến snapshot | Đến 14/1 | 25% / 35% / 40% |
| Lợi suất sUSDat / srUSDat cho YT | 0% / 5% | 8% / 7.5% | 12% / 8.1% | sUSDat: 0–12% lệch về 0; srUSDat: đều 5–8.1% |

Xác suất 15% không có token hoặc gặp sự cố được ghép từ ba nguồn rủi ro: khoảng 11% thị trường cho rằng Saturn không ra token trước 2028 ([Polymarket](https://gamma-api.polymarket.com/public-search?q=saturn)); rủi ro hợp đồng thông minh, vì kiến trúc PYUSDx chưa được audit và các lỗi Innora chưa được xác nhận đã sửa; và rủi ro bị loại theo điều khoản, vì Saturn giữ quyền "giảm, đảo ngược hoặc hủy" điểm, chặn Mỹ, EEA và UK, và có thể yêu cầu KYC ([Gravity terms](https://saturn.credit/legal/gravity-program)). Rủi ro STRC tác động đến YT-USDat một cách gián tiếp. USDat được bảo chứng bằng PYUSDx chứ không phải STRC, nên một cú sập kiểu tháng 6 không xóa gốc của YT-USDat (YT vốn không có gốc). Thay vào đó, nó làm tăng khả năng hoãn TGE theo kiểu Apyx và kéo FDV xuống.

**Ma trận ROI cho $1,000 ETH YT-USDat**, theo FDV ngày TGE, ngày snapshot và mức pha loãng. Các tham số cố định: chiết khấu 30%, xác suất 0 là 15%, S3 bằng 30% S2, USDC đến snapshot, phân bổ 5%.

| FDV ngày TGE | Snapshot 1/11 (264 tỷ) | Snapshot 15/11 (315 tỷ) | 8/12, pha loãng thấp (354 tỷ) | 8/12, cơ sở (397 tỷ) | 8/12, pha loãng cao (476 tỷ) | 8/12, rất cao (583 tỷ) |
|---|---|---|---|---|---|---|
| $50M | −67% | −58% | −40% | −44% | −50% | −55% |
| $75M | −55% | −44% | −20% | −27% | −35% | −43% |
| $100M | −43% | −30% | −1% | −9% | −21% | −31% |
| $150M | −19% | −2% | +38% | **+25%** | +8% | −8% |
| $200M | +4% | +25% | +76% | +60% | +37% | +15% |
| $300M | +51% | +81% | +154% | +129% | +94% | +62% |
| $400M | +98% | +136% | +231% | +197% | +152% | +109% |

Ma trận cho thấy người mua YT-USDat ở giá hiện tại cần đồng thời **FDV ≥ $150 triệu và Season 2 chạy gần đủ** để có lãi đáng kể. Nếu TGE rơi vào đầu tháng 11, cần FDV khoảng $200 triệu chỉ để hòa vốn. Mỗi mức pha loãng thêm khoảng 80 tỷ điểm lấy đi khoảng 15–20 điểm phần trăm ROI.

**Kết quả theo kịch bản xác định và theo Monte Carlo** (200,000 lượt mô phỏng, dùng giá khớp thật ở từng quy mô lệnh):

| Pool, quy mô | Bi quan | Cơ sở | Lạc quan | MC trung bình | MC trung vị | P(lỗ) | P(lỗ >50%) | P10 / P90 |
|---|---|---|---|---|---|---|---|---|
| ETH YT-USDat $1k | −90% | +25% | +301% | **+15%** | **−17%** | 59% | 28% | −78% / +140% |
| ETH YT-USDat $10k | −91% | +18% | +280% | +9% | −21% | 62% | 30% | −80% / +127% |
| ETH YT-USDat $50k | — | — | — | −1% | −29% | 66% | 34% | −81% / +105% |
| Monad YT-USDat $1k | −91% | +22% | +291% | +12% | −19% | 60% | 29% | −79% / +133% |
| Monad YT-USDat $10k | −91% | +18% | +280% | +9% | −21% | 62% | 30% | −79% / +127% |
| BNB YT-USDat $500 | −93% | −5% | +205% | −12% | −37% | 71% | 39% | −84% / +82% |
| ETH YT-sUSDat $1k | −98% | −16% | +75% | −36% | −31% | 77% | 36% | −100% / +19% |
| Monad YT-sUSDat $1k | −98% | −35% | +35% | −50% | −47% | 93% | 45% | −100% / −8% |
| ETH YT-srUSDat $1k | −53% | +7% | +119% | −5% | −17% | 69% | 4% | −43% / +46% |

Cấu trúc lợi nhuận của YT-USDat giống một quyền chọn mua. Kỳ vọng dương, nhưng phần lớn đến từ một đuôi phải dày: FDV $300 triệu trở lên, không pha loãng và không bị vesting. Trong khi đó, kết quả thường gặp nhất là lỗ vừa phải đến lỗ nặng. YT-srUSDat có đuôi trái nhẹ nhất vì lợi suất tranche senior hoàn lại phần lớn vốn, nhưng pool chỉ $0.23 triệu và trượt giá 10.7% ngay ở lệnh $1k. YT-sUSDat có kỳ vọng âm trong mọi phân phối hợp lý.

**Ngưỡng giá vào lệnh.** Bảng dưới áp cùng phân phối Monte Carlo cho các mức implied APY khác nhau của YT-USDat trên Ethereum ($1k, chi phí khớp lệnh khoảng 2.1%):

| Implied APY | Giá YT | YT/$1k | MC trung bình | MC trung vị | P(lỗ) |
|---|---|---|---|---|---|
| 5% | $0.0143 | 68,650 | +102% | +46% | 33% |
| 6% | $0.0170 | 57,563 | +70% | +22% | 41% |
| **7%** | **$0.0197** | **49,643** | **+46%** | **+5%** | **47%** |
| 8% | $0.0224 | 43,702 | +29% | −7% | 54% |
| 9% (hiện tại) | $0.0251 | 39,081 | +15% | −17% | 59% |
| 10% | $0.0277 | 35,383 | +4% | −25% | 64% |
| 12% | $0.0328 | 29,836 | −12% | −37% | 71% |

Thời gian chờ cũng có giá. Nếu đợi thêm 14 ngày mà implied APY không đổi, kỳ vọng ở mức 7% giảm từ +46% xuống +38% và trung vị giảm từ +5% xuống −1%. Lý do là cửa sổ điểm S2 co nhanh hơn thời gian còn lại đến đáo hạn. Vì vậy ngưỡng vào lệnh nên siết dần theo thời gian: **≤7% vào cuối tháng 9, ≤6.5% vào giữa tháng 10**.

## Khuyến nghị: chỉ vào vị thế nhỏ YT-USDat khi implied APY ≤7%

**Kết luận theo từng pool.** YT-USDat trên Ethereum là lựa chọn ưu tiên: pool sâu nhất ($1.96 triệu), giá điểm rẻ nhất ($8.4–12.5 cho mỗi 1 triệu điểm) và còn dư 24% hạn mức Merkl. YT-USDat trên Monad là lựa chọn thay thế tương đương, dùng để chia nhỏ lệnh. Với cả hai pool, đánh giá là **"vị thế nhỏ"**: ở 8.98% hiện tại chỉ nên vào một phần thử rất nhỏ hoặc đứng ngoài, và chỉ tăng lên đủ quy mô khi implied APY ≤7% (giá YT ≤ ~$0.020). Pool này đã giao dịch trong vùng 6.1–6.9% trong phần lớn tháng 8 và đầu tháng 9, nên mức giá đó không phải là không tưởng; đặt lệnh giới hạn trên Pendle là cách phù hợp để chờ. **Tránh** YT-sUSDat trên cả hai chain (kỳ vọng −36% đến −50%, điểm đắt gấp 4–6 lần và chịu rủi ro STRC trực tiếp), YT-USDat trên BNB (không khớp được lệnh $1k và không có thưởng USDC) và YT-srUSDat (pool quá mỏng, lại chưa chắc có điểm trên Monad).

**Quy mô vị thế.** Kelly tối ưu trong mô hình là khoảng 16% vốn ở mức giá hiện tại và khoảng 30% ở implied APY 7%. Tuy nhiên các tham số đầu vào là chủ quan và có thể sai lệch lớn, nên tôi dùng khoảng 1/10 Kelly. Cụ thể: **tổng vị thế YT Saturn không quá 1–2% danh mục**, và chỉ dùng số tiền có thể chấp nhận mất 100%. Mỗi pool không nên vượt quá **$5–10k** để giữ trượt giá dưới khoảng 7%. Nếu lớn hơn, chia lệnh giữa Ethereum và Monad. Với vốn trên khoảng $20k, LP Curve USDC/USDat hoặc giữ USDat cho điểm với chi phí tương đương hoặc rẻ hơn mà vẫn giữ được gốc. Người có hơn 1 triệu điểm Gravity từ S1 được boost 20%, giúp chi phí mỗi 1 triệu điểm giảm từ $12.50 xuống khoảng $10.42 và FDV hòa vốn giảm khoảng 17%.

**Điều kiện vào lệnh và kế hoạch thoát.** Chỉ vào lệnh khi hội đủ các điều kiện sau: implied APY ≤7%; Pendle API vẫn hiển thị thưởng USDC 3%; nguồn cung YT vẫn dưới hạn mức Merkl; và chưa có thông báo TGE trước giữa tháng 11. Nếu TGE được chốt trước 15/11, FDV hòa vốn điều chỉnh rủi ro tăng lên $122–180 triệu và nên dừng mua thêm. Tại snapshot S2, cần đánh giá lại. Nếu Season 3 có phân bổ rõ ràng, tiếp tục giữ YT đến 14/1 để nhận USDC và điểm S3. Nếu không, bán YT nếu thị trường còn giá mua. Sau TGE, nên bán phần lớn token nhận được trong vài ngày đầu nếu không bị vesting. Lý do là lứa TGE 2025 đạt đỉnh ngay trong giờ giao dịch đầu tiên, và trung vị d30 của các token được farm là −41%.

| Tín hiệu cần theo dõi | Nguồn | Ngưỡng hành động |
|---|---|---|
| Implied APY của YT-USDat | [Pendle API](https://api-v2.pendle.finance/core/v1/1/markets/0x4ccf6deb3d1895373f604b418ff55d8adae8b846) | ≤7% (≤6.5% từ giữa tháng 10): mua; >10%: không mua |
| Ngày TGE/snapshot | [@saturn_credit](https://x.com/saturn_credit/status/2103290807847645584) | TGE trước 15/11: giảm quy mô và dừng mua |
| Tokenomics: tổng cung, % S2, vesting cho ví lớn, định nghĩa "initial" và "total supply" | @saturn_credit | S2 <5% hoặc vesting nặng: không mua thêm, cân nhắc bán |
| Nguồn cung YT so với hạn mức Merkl (Ethereum 26.6M, Monad 53M) | [Etherscan](https://etherscan.io/token/0x480c3c9470fa4bbda030f6396fa4b17adefc1ce0), [Monadscan](https://monadscan.com/token/0x5aff25c86c7cb739e554be8904b32047738b7440) | Vượt hạn mức mà không được bơm thêm ngân sách: điểm/YT <30 |
| Tổng Orbital Points và tốc độ phát hành | [Merkl API](https://api.merkl.xyz/v4/rewards/token/total?chainId=1&address=0x10710501778b7FAf9e478f36FaE0B286C028eDE8) | >4.5 tỷ/ngày kéo dài: dùng cột pha loãng cao trong ma trận |
| Thưởng USDC 3% trên YT | [Pendle history](https://api-v2.pendle.finance/core/v3/1/markets/0x4ccf6deb3d1895373f604b418ff55d8adae8b846/historical-data?time_frame=day) | Về 0: chi phí ròng lên $1,000/$1k |
| Giá và cổ tức STRC | [Yahoo Finance](https://query1.finance.yahoo.com/v8/finance/chart/STRC?range=6mo&interval=1wk), [SEC](https://www.sec.gov/Archives/edgar/data/0001050446/000119312526377583/mstr-20260831.htm) | STRC <$95 hoặc cắt cổ tức: rủi ro hoãn TGE kiểu Apyx |
| Polymarket FDV | [Polymarket](https://polymarket.com/event/saturn-fdv-above-one-day-after-launch-20260623191408697) | Giá Yes cho mốc >$200M dưới 0.35: hạ kỳ vọng xuống kịch bản cơ sở hoặc bi quan |
| Niêm yết Binance Alpha/HODLer hoặc pre-market | Thông báo sàn | Có niêm yết: hỗ trợ kịch bản lạc quan |
| Kết quả TGE của Apyx | [ChainCatcher](https://www.chaincatcher.com/en/article/2291854) | FDV/TVL của Apyx là điểm neo gần nhất cho STRN |
| Sự cố bảo mật, peg USDat, độ lệch pool Curve | [Yearn](https://github.com/yearn/risk-score/blob/master/reports/report/saturn-usdat.md) | Bất kỳ sự cố nào: thoát |

## Kết luận

Thị trường YT-USDat định giá điểm Saturn ở mức ngụ ý FDV hòa vốn quanh $67–99 triệu. Con số này nghe có vẻ rẻ so với trung vị ~$207 triệu trên Polymarket, và đó là lý do nhiều KOL gọi đây là "cách nhanh nhất để gom điểm". Nhưng khoảng chênh gấp 4 lần giữa Polymarket và mức hòa vốn thô ~$55 triệu biến mất gần hết khi tính đủ các chi phí thật: phí Pendle 5%, trượt giá, khả năng TGE cắt ngắn Season 2, pha loãng do lượng YT tăng, vesting cho ví lớn, và xác suất 15% không có gì cả. Sau các điều chỉnh đó, lợi thế còn lại mỏng đến mức kết quả nhạy với vài điểm phần trăm implied APY. Kết luận thực tế vì vậy không phải "mua" hay "tránh", mà là **mua ở giá nào**: dưới 7% implied APY thì đây là một quyền chọn có kỳ vọng dương đáng giữ với quy mô nhỏ, còn trên 9% thì người mua đang trả tiền cho câu chuyện hơn là cho con số.

Câu hỏi định giá lớn hơn là liệu Saturn có tránh được số phận của OpenEden và Resolv hay không. Hai dự án này TGE khi nguồn cung stablecoin đã co lại 21% và 63% so với đỉnh, rồi mất hơn 90% giá trị token. Bài học từ các dự án so sánh là tăng trưởng nguồn cung sau TGE quyết định giá token nhiều hơn bội số lúc niêm yết. Saturn đang có dấu hiệu giống nhóm thua: TVL giảm 31% từ đỉnh, ~74% USDat nằm trong các vị thế săn điểm, và phần doanh thu giữ lại chỉ khoảng $1–2 triệu/năm. Điều có thể đảo ngược bức tranh là tăng trưởng thật sau TGE, từ tích hợp PYUSDx, STRCon của Ondo, và việc STRC trở lại mệnh giá. Nếu những tín hiệu đó xuất hiện trước snapshot, ma trận sẽ dịch sang cột lạc quan. Chừng nào chưa có, người mua YT nên coi đây là một cược nhỏ với kỷ luật vào lệnh chặt chẽ.
