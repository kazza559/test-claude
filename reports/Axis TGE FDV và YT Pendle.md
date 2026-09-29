# YT-USDx chỉ đáng mua như một vé số nhỏ

Axis (axis.to, @AxisFDN) thực chất là một quỹ arbitrage trung lập thị trường đặt tài sản trên CEX, gói dưới dạng synthetic dollar USDx/sUSDx. Quy mô chỉ khoảng **$56M TVL**, gọi vốn **$5M** và **chưa công bố token**. Trong bối cảnh FDV các TGE stablecoin năm 2026 đã co lại còn vài trăm triệu USD và narrative đang thoái trào, ước tính thiên bear của báo cáo này là: **TGE sớm nhất khoảng Q2 2027 (xác suất tích lũy tới giữa 2027 khoảng 50%), FDV lúc ra mắt trong khoảng $50–300M, kịch bản base khoảng $120M**, và có khoảng **30% xác suất Coordinates Season 1 không mang lại gì**. Với YT-USDx (24x, không có yield), $1,000 mua được khoảng **57M Coordinates** tới ngày đáo hạn 3/12/2026, hòa vốn ở **$17.5 cho 1M points**. Kỳ vọng có trọng số xác suất sau khi trừ hao hụt khi bán là khoảng **+$265 trên $1,000**, nhưng con số này **đến gần hết từ kịch bản bull 8%**. Ở trường hợp điển hình (median) nhà đầu tư vẫn **lỗ 45–100%**. YT-sUSDx (6x) thực chất là cược rằng APY của sUSDx giữ trên **~20.5%** cho tới đáo hạn. Ở mức giá hiện tại, giá trị kỳ vọng của nó **âm nhẹ (≈ −$6 đến −$99 trên $1,000)**. Khuyến nghị cụ thể: chỉ mua YT-USDx với quy mô nhỏ (≤$2–3k, tốt nhất khi implied APY xuống ≤13%), **chưa mua YT-sUSDx** cho tới khi implied APY ≤15% trong lúc APY thực vẫn trên 20%. Các vị thế tiền lớn nên cân nhắc PT hoặc chiến lược dùng yield của PT để mua YT.

## Axis là quỹ arbitrage CEX quy mô $56M khoác áo synthetic dollar

Axis do Coordinate Labs (Singapore) vận hành. Đội ngũ lõi đến từ quỹ quant Hàn Quốc Alphanonce: CEO Chris Kim, CIO Changsung Kim, CTO Justin Im, cùng COO Jimmy Xue (đồng sáng lập Velodrome) ([axis.to/about](https://axis.to/about)). USDx là "synthetic dollar over-collateralized" và bản thân không sinh yield. Yield được trả qua vault sUSDx (ERC-4626/7540), lấy từ arbitrage cross-venue, cross-currency, funding và OTC ([docs: What is Axis?](https://docs.axis.to/start-here/what-is-axis.md)). Điểm cốt lõi về rủi ro là tài sản bảo chứng **nằm trên các sàn tập trung**. Docs ghi rõ Axis "does **not** currently use off-exchange settlement or off-exchange custody" ([docs: Backing & Custody](https://docs.axis.to/backing-reserves-and-transparency/backing-custody-transparency.md)). Một review bên thứ ba dẫn số liệu data room cho thấy exposure tập trung ở Binance 19.8%, Bybit 13.5% và Upbit 13.3% ([HackMD review](https://hackmd.io/@DoMnolkQRGOjIqhl46A13A/rJ59uLvSfx)). Chỉ counterparty được whitelist mới được mint/redeem trực tiếp, với mức tối thiểu **$1M** ([docs: Eligibility](https://docs.axis.to/resources-and-legal/eligibility-and-onboarding.md)). Với người dùng nhỏ lẻ, peg của USDx vì vậy dựa vào khoảng $5M thanh khoản trên hai pool Curve.

Về traction, số liệu khá khiêm tốn và đang chững lại. Origin Vault (Season 0) đóng ngày 5/8 với **$67.25M từ 1,857 ví**, dưới mức cap $100M ([AxisFDN, 1/9/2026](https://x.com/AxisFDN/status/2094772784002154737)). Sau khi lock hết hạn ngày 4/9, TVL rơi từ $67.8M xuống đáy $54.3M, rồi hồi về **$56.3M** ([DefiLlama](https://api.llama.fi/protocol/axis)). On-chain ngày 28/9 ghi nhận USDx supply 56.36M, sUSDx giữ 36.08M USDx, tỷ giá 1.0296 ([Etherscan sUSDx](https://etherscan.io/address/0xEB892628D1E58BC475A6dCB7F5dBC4F591632AA4)). Số holder rất nhỏ: 686 ví USDx, 235 ví sUSDx và 732 người theo dõi Telegram ([Etherscan USDx](https://etherscan.io/token/0xa1fA7777974312f7d801A8880714a218F76233f8); [t.me/s/AxisFDN](https://t.me/s/AxisFDN)). APY của sUSDx hiện là **21.6%**, trung bình 30 ngày là 22.7% ([DefiLlama yields](https://yields.llama.fi/pools)). Tuy vậy, đây là con số được "quản lý": rewards "fully discretionary", và việc chia lợi nhuận giữa quỹ dự trữ và vault là "a decision, not a formula" ([docs: Reward Distribution](https://docs.axis.to/susdx-the-rewards-vault/reward-distribution.md)). Chỉ khoảng 64% USDx được stake, nên 21.6% trên sUSDx tương đương khoảng 13–14% trên toàn bộ tài sản bảo chứng, khớp với khung "10–20% net" mà Axis tự đưa ra ([docs: Origin Vault](https://docs.axis.to/origin-vault/origin-vault.md)).

Axis cũng có điểm mạnh thật. Track record gross của Alphanonce là 360.7% qua 77 tháng, dù dữ liệu 2025 còn "pending reconciliation" ([docs: Track Record](https://docs.axis.to/susdx-the-rewards-vault/how-axis-earns-yield/historical-track-record.md)). Dự án có ba bản audit, trong đó bản V2 do OpenZeppelin thực hiện, cùng Safe 3/5 và timelock 48h ([docs: Audits](https://docs.axis.to/backing-reserves-and-transparency/audits.md)). Nhóm backer gồm Galaxy, OKX Ventures, FalconX và GSR ([The Block](https://www.theblock.co/post/381215/axis-5-million-usd-round-galaxy-ventures-onchain-yield-protocol-usd-bitcoin-gold)). Mặt khác, vòng seed chỉ **$5M** nên cost basis của VC rất thấp, và đây sẽ là nguồn áp lực bán sau khi unlock. Kế hoạch từ tháng 12/2025 ("vault $1B, public token sale đầu 2026") đã trễ khoảng 4 tháng và chỉ đạt khoảng 7% mục tiêu. Tài liệu Discord chính thức không tìm thấy. Telegram chỉ repost link X, và chưa có bài chính thức nào nhắc tới token, TGE hay airdrop ([axis.to/insights](https://axis.to/insights)).

## Làn sóng TGE stablecoin 2026 nén FDV xuống vài trăm triệu

Các so sánh cho thấy một sự dịch chuyển chế độ định giá rất rõ. Năm 2024, Ethena ra mắt ở FDV khoảng **$9.6B** (khoảng 5x TVL) ([CoinDesk](https://www.coindesk.com/markets/2024/04/02/ethena-labs-ena-token-goes-live-start-trading-at-64-cents)). Làn sóng cuối 2025 gồm Falcon (~$6.7B lúc mở, giảm 75% trong ngày đầu) ([CCN](https://www.ccn.com/analysis/crypto/falcon-finance-ff-price-crashes-token-debut-what-lies-ahead/)) và OpenEden (~$551M, hiện −95.5% từ ATH) ([CoinGecko EDEN](https://www.coingecko.com/en/coins/openeden)). Resolv ra mắt ở khoảng $300M, tương đương 0.86x TVL, và hiện gần như vô giá trị sau vụ exploit tháng 3/2026 ([The Defiant](https://thedefiant.io/news/defi/resolv-stablecoin-protocol-s-token-debuts-at-usd300-million-valuation); [CoinDesk](https://www.coindesk.com/markets/2026/03/23/resolv-stablecoin-drops-70-after-usd80-million-exploit-after-attacker-mints-usr)). Usual hiện chỉ còn FDV **$29M**, −99.1% ([CoinGecko USUAL](https://www.coingecko.com/en/coins/usual)).

| Dự án (token) | TGE | FDV lúc ra mắt | FDV 28/9/2026 | Ghi chú |
|---|---|---|---|---|
| Unitas (UP) | 13/3/2026 | ~$59–80M | $267M | Chỉ những dự án FDV thấp mới giữ được giá |
| USD.AI (CHIP) | 30/3–21/4/2026 | $300M (sale) / ~$636M (ngày đầu) | $443M | −30% so với ngày đầu |
| Solstice (SLX) | 25/5/2026 | ~$298M | $66M | **−78%**, USX supply giảm một nửa trong tháng 9 |
| Re (RE) | 18/6/2026 | ~$640–647M | ~$461M | −29% |
| Cap (CAP) | 26/6/2026 | ~$246–320M (ICO floor $75M) | $554M | Stabledrop bị cắt 65% |

Nguồn: [CoinGecko API](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=falcon-finance-ff,resolv,usual,plasma,solstice,cap-4,unitas), [ICO Drops Unitas](https://icodrops.com/unitas/), [ICO Drops Cap](https://icodrops.com/cap-3/), [Crypto Briefing RE](https://cryptobriefing.com/binance-lists-re-token-seed-tag/).

Nhóm TGE năm 2026 có FDV lúc ra mắt trung vị khoảng **$300M** và FDV/TVL khoảng **1x hoặc thấp hơn**. Chỉ hai dự án ra mắt ở mức ≤$250M FDV hiện còn trên giá ngày đầu. Bối cảnh vĩ mô đang xấu đi. Nguồn cung yield-bearing stablecoin giảm hơn $3.5B (−15%) trong Q2 2026, và sUSDe riêng mảng này giảm 52% ([CoinMarketCap/CEX.IO](https://coinmarketcap.com/academy/article/yield-bearing-stablecoin-supply-falls-q2-2026-treasury-backed-growth)). Ethena ngừng hoàn toàn incentive cho USDe từ cuối tháng 9/2026 ([Crypto Briefing](https://cryptobriefing.com/ethena-ends-usde-token-incentives/)). TVL của Pendle giảm khoảng **91%** từ đỉnh, còn $1.26B ([DefiLlama Pendle](https://api.llama.fi/protocol/pendle)). Fed tăng lãi suất lên 3.75–4.00% ngày 16/9 ([CryptoDaily](https://cryptodaily.co.uk/2026/09/fed-rates-3-75-4-00-bitcoin-macro-shock)), và sUSDe chỉ còn trả khoảng 5% ([DefiLlama yields](https://yields.llama.fi/pools)). Nhiều synthetic dollar còn mất TVL ngay *trước* TGE: Neutrl −83%, infiniFi −76%, Apyx −41% kèm mất peg nhẹ ([DefiLlama stablecoins](https://stablecoins.llama.fi/stablecoins?includePrices=true)). Lịch TGE Q4 2026 cũng đang dày đặc với Apyx, Saturn, infiniFi, Neutrl và Variational ([KuCoin Saturn](https://www.kucoin.com/news/flash/saturn-plans-tge-in-q4-2026-allocates-up-to-5-supply-for-second-season); [Today in DeFi](https://news.todayindefi.com/p/airdrop-alpha-re-protocol-announced)).

Đặt vào khung này, Axis là một dự án rất nhỏ. TVL của nó bằng khoảng 1/5 Cap tại thời điểm TGE, 1/7 Re và 1/30 Falcon. Dự án chỉ có một chain, không có tích hợp với Morpho hay Aave, và lại nằm đúng trong nhóm "basis/arbitrage dollar" đang mất niềm tin sau các sự cố Stream/Elixir và Resolv. Luận điểm tích cực duy nhất về định giá đến từ chính các thương vụ 2026: một FDV thấp (≈TVL) có thể tạo ra lợi nhuận sau TGE, như Unitas và Cap đã làm. Tuy nhiên điều đó không nâng giá trị airdrop ngay tại thời điểm TGE.

## TGE sớm nhất Q2 2027, FDV kỳ vọng $50–300M

Chưa có tín hiệu nào cho thấy TGE sẽ diễn ra trong năm 2026. Season 1 chạy 90 ngày từ 4/9, tức kết thúc khoảng **3/12/2026** ([AxisFDN](https://x.com/AxisFDN/status/2094772784002154737)). Tài liệu data room được review bên thứ ba trích dẫn nêu mốc "Q1–Q2 2027" ([HackMD](https://hackmd.io/@DoMnolkQRGOjIqhl46A13A/rJ59uLvSfx)). Polymarket (rất mỏng, tổng khối lượng khoảng $8.7K) định giá **21.5%** cho khả năng có token trước 31/12/2026, **58.5%** trước 30/6/2027 và **61.5–64.5%** trước cuối 2027 ([Polymarket](https://polymarket.com/event/will-axis-launch-a-token-by-20260729144519159)). Ở các dự án yield-dollar, thời gian từ lúc bắt đầu points tới TGE có trung vị khoảng 7 tháng (dao động 5–12 tháng), và các mốc công bố thường trễ khoảng một quý. Dự án đã từng trễ một lần, và Dec 2025 PR còn nhắc tới một "public token sale", tức là có thể có thêm một bước trước airdrop. Vì vậy báo cáo này đặt xác suất thấp hơn Polymarket:

| Cửa sổ TGE | Xác suất (thiên bear) | Ý nghĩa với YT |
|---|---|---|
| Trước 31/12/2026 | ~8% | Snapshot sát ngày đáo hạn, ít pha loãng |
| Q1 2027 | ~17% | Kịch bản bull |
| Q2 2027 | ~25% | Kịch bản base |
| H2 2027 | ~15% | Bear: có thể có Season 2 chia chung pool |
| 2028+ / không bao giờ | ~35% | Gần như mất trắng phần points |

Như vậy **TGE trung vị rơi vào khoảng Q2–Q3 2027**, và khả năng có token trước giữa 2027 là khoảng 50%. Khoảng cách từ snapshot (~3/12/2026) đến TGE vì vậy là 3–7 tháng hoặc hơn. Trong quãng đó YT đã về 0, không còn gì để bán, và mọi thay đổi luật chơi (thêm Season 2, bán token, lọc sybil) đều đè lên points đã tích lũy.

Để ước tính FDV, báo cáo kết hợp ba nhóm dữ kiện: FDV/TVL của nhóm 2026 (≈0.5–1.5x), TVL của Axis (~$56M, có thể tăng nếu BTCx, GOLDx và Axis Prime được triển khai), và mức giá mà chính thị trường Pendle đang ngầm định. Với YT-USDx, thị trường đang định giá khoảng **$16.6–17.5 cho 1M Coordinates**. Nhân với tổng 86–160B points, toàn bộ pool airdrop Season 0+1 được định giá chỉ **$1.5–2.8M**. So sánh độc lập: lợi suất airdrop thực tế của các TGE stablecoin 2025 thường chỉ **5–15%/năm trên TVL** ở giá bán thực tế. Áp vào khoảng $60M TVL trong khoảng 4 tháng (Season 0+1), pool airdrop hợp lý nằm trong khoảng **$1.5–6M**. Từ đó ra bảng tham số:

| Tham số | Bear (40%) | Base (22%) | Bull (8%) | Zero (30%) |
|---|---|---|---|---|
| FDV lúc ra mắt | **$50M** ($30–80M) | **$120M** ($80–200M) | **$300M** ($200–500M) | Không có token / S1 không quy đổi / YT bị loại |
| % supply cho airdrop Season 0+1 | 3% (2–4%) | 4% (3–6%) | 7% (5–10%) | 0 |
| Giá trị pool airdrop | $1.5M | $4.8M | $21M | $0 |
| Tổng Coordinates tại snapshot | 160B (150–200B) | 120B (105–135B) | 95B (86–100B) | — |
| **$ trên 1M points** | **$9.4** | **$40** | **$221** | **$0** |
| Hệ số hiện thực hóa (bán dưới giá ngày đầu, vesting) | 0.5 | 0.7 | 0.8 | — |
| APY sUSDx tới 3/12 | 12% | 16% | 20% | 10% |

Các mức % airdrop được neo theo so sánh. Ethena dành 5% cho mỗi season ([crypto.news](https://crypto.news/ethena-labs-launch-ena-with-a-750m-airdrop-as-makerdao-grabs-usde/)). Usual dành 7.5% và Resolv 10% ([Usual](https://usual.money/blog/tge-roadmap-announcement); [Resolv Docs](https://docs.resolv.xyz/litepaper/using-resolv/resolv-points/seasons/season-1)). Falcon dành 2.5% public tại TGE ([Tokenomist](https://tokenomist.ai/falcon-finance-ff)), Apyx 4% + 6%, Saturn ≤5%. Trong kịch bản bear, 3% phản ánh khả năng pool bị chia cho Season 2 hoặc cho token sale. Trung bình có trọng số (chưa tính hiện thực hóa) là **$30/1M points**. Sau hệ số hiện thực hóa, con số này còn **$22/1M points**. Cả hai đều chỉ cao hơn mức hòa vốn hiện tại của YT-USDx ($17.5) một khoảng mỏng.

## Coordinates: 10x tương đương khoảng 10 points/$/ngày, và pool đang bị pha loãng

Season 0 có base rate công khai là **10 Coordinates/$/ngày**, nhân 2x cho $50M đầu tiên và 1.75x cho phần sau ([AxisFDN, 27/7](https://x.com/AxisFDN/status/2081726383240126870)). Season 1 dùng multiplier theo vị trí vốn. Vault ogUSDx được **10x**. Giữ USDx được 16x, giữ sUSDx 4x. Curve USDx/USDT LP được 20x, Curve USDx/sUSDx 10x. Trên Pendle, **YT-USDx được 24x**, LP USDx 20x, **YT-sUSDx 6x** và LP sUSDx 5x. Multiplier giữa các venue không cộng dồn ([bảng chính thức](https://pbs.twimg.com/media/HRIeu4WbcAAgBU6.png); [Pendle API](https://api-v2.pendle.finance/core/v2/markets/all?limit=100&skip=0)). Pendle thu **5%** trên points của YT ([Pendle docs: Fees](https://docs.pendle.finance/pendle-v2/ProtocolMechanics/Mechanisms/Fees)).

**Đối chiếu giả định base rate B của hai ghi chú.** Ghi chú về Pendle để B là ẩn số và tính toán theo đơn vị "x-$-day". Ghi chú về points suy ra **B ≈ 1** từ leaderboard: các ví có vị thế tròn ($100K, $120K, $125K, $200K) trong vault 10x tích lũy chính xác 993,092 và 1,986,185 points/ngày, tương đương **~9.93/$/ngày**. Ví số 1 tích lũy khoảng 142M/ngày, khớp với vị thế ~$14M ở mức 10x ([Axis leaderboard API](https://api.axis.to/api/v1/points/leaderboard)). Báo cáo này **dùng B = 1**, tức "Nx" tương đương N Coordinates/$/ngày. Điều quan trọng hơn là giá trị của YT phụ thuộc vào *thị phần* trong pool, không phụ thuộc vào con số points tuyệt đối. Nếu B áp dụng đồng đều cho mọi vị thế, nó triệt tiêu giữa tử số và mẫu số. Độ nhạy chỉ xuất hiện khi Axis tính Pendle theo một cơ sở khác:

| Giả định | Points/$1k YT-USDx | Tổng pool (base) | Thị phần/$1k | Tác động |
|---|---|---|---|---|
| **B = 1 đồng đều (dùng trong báo cáo)** | 57.0M | 120B | 0.048% | Chuẩn |
| B = 10 đồng đều | 570M | Season 1 cũng ×10 | Gần như không đổi | Không khớp dữ liệu leaderboard (vault sẽ phải hiện ~99/$/ngày) |
| B = 10 chỉ riêng cho Pendle | 570M | ~199B | ×6.0 | Upside hiếm, xác suất thấp |
| Axis giảm 50% điểm DeFi/Pendle (B_eff = 0.5) | 28.5M | ~115B | ×0.5 | Hòa vốn tăng gấp đôi lên ~$35/1M |

**Lạm phát points là rủi ro lớn nhất cho người vào muộn.** Ngày 28/9, API báo tổng **68.8B Coordinates trên 2,325 ví**, với tốc độ phát hành đo trực tiếp **~260M/ngày**. Phân phối tập trung cực mạnh: top-1 giữ 19.9%, top-10 45.6%, top-100 88.1%. Season 0 ước tính chiếm **70–80%** tổng số points ([Axis leaderboard API](https://api.axis.to/api/v1/points/leaderboard)). Trong top-100 có 66 ví hiển thị tốc độ tích lũy bằng 0, có thể vì họ đã chuyển sang Pendle hoặc Curve. Tổng hợp các vị thế đủ điều kiện (YT-USDx 4.36M × 24 ≈ 105M/ngày, YT-sUSDx ≈ 37M/ngày, Curve và LP khoảng 95–175M/ngày) cho thấy tốc độ phát hành thực có thể lên **0.5–0.65B/ngày**, nghĩa là points từ DeFi có thể đang được **ghi nhận hồi tố sau**. Vì thế mẫu số ở cuối Season 1 có thể là 86B trong trường hợp chỉ tính phần đang hiển thị, 108–118B nếu cộng hồi tố, và **150B+** nếu USDx tăng trưởng, có thêm venue hoặc có Season 2. Referral cộng thêm tới khoảng 20% trên phần points của người được giới thiệu. Tổng YT-USDx sẽ nhận khoảng 6.5B points, tương đương 5–7.5% pool. Axis đã từng cắt rate một lần (vault từ 20 xuống 10/$/ngày) và luôn nhắc rằng Coordinates "confer no entitlement to any token" ([AxisFDN](https://x.com/AxisFDN/status/2081726383240126870)).

## YT-USDx hòa vốn ở $17.5/1M points; YT-sUSDx là cược vào APY 20.5%

Các phép tính dùng giá khớp lệnh $1k ngày 28/9: YT-USDx **0.025785 USDx/YT**, YT-sUSDx **0.031872 USDx/YT** ([Pendle Hosted SDK](https://api-v2.pendle.finance/core/v3/sdk/1/convert)). Thời gian còn lại là **D = 64.5 ngày** (t = 0.1767 năm). Báo cáo giữ nguyên giá ngày 28/9 dù hôm nay đã bớt một ngày, nên kết quả thận trọng hơn thực tế khoảng 1.5%. Các công thức:

- Points/$1k = (1000/P) × M × 0.95 × D × B
- Yield YT-sUSDx/$1k = (1000/P) × 0.95 × [(1+APY)^t − 1]
- Chi phí ròng = 1000 − yield
- Hòa vốn $/pt = chi phí ròng / points
- FDV hòa vốn = ($/pt hòa vốn × tổng points) / % airdrop
- APY hòa vốn của YT-sUSDx = (1 + P/0.95)^(1/t) − 1
- Với YT-USDx, xấp xỉ $/1M hòa vốn ≈ ln(1+implied APY) × 10⁶ / (365 × 22.8). Công thức này hầu như không phụ thuộc thời gian còn lại, nên có thể đổi thẳng ngưỡng implied APY thành ngưỡng $/point.

| Chỉ số (khớp lệnh $1k) | YT-USDx | YT-sUSDx |
|---|---|---|
| YT nhận được | 38,782 | 31,375 |
| Points/ngày (net 5% phí) | ~884K | ~179K |
| Points tới 3/12 | **~57.0M** | **~11.5M** |
| Yield nhận lại | 0 (APY gốc 0%) | $506 @12% · $792 @16% · $976 @20% · $1,048 @21.6% |
| Chi phí ròng | **$1,000 (mất 100%)** | $397 @12% · $208 @16% · $24 @20% · −$48 @21.6% |
| $/1M points hòa vốn | **$17.5** (mid $16.9; lệnh $5k $18.8; lệnh $10k $20.1) | $34.4 @12% · $18.0 @16% · $2.1 @20% · miễn phí @≥20.5% |
| APY gốc hòa vốn (points = 0) | — | **20.5%** (mid 20.0%; lệnh $10k 21.0%) |
| Không có phí 5% của Pendle | Hòa vốn $16.7/1M | APY hòa vốn 19.4% |

Phí 5% của Pendle làm mức hòa vốn của YT-USDx tăng khoảng 5% và đẩy APY hòa vốn của YT-sUSDx lên thêm khoảng **1.1 điểm %**. Đây là khoản không nhỏ, vì biên lợi nhuận của YT-sUSDx vốn rất mỏng.

**FDV hòa vốn cho YT-USDx** (lệnh $1k, $17.5/1M), tính bằng triệu USD:

| Tổng points \ % airdrop | 2% | 3% | 4% | 5% | 7% | 10% |
|---|---|---|---|---|---|---|
| 95B | 83 | 56 | 42 | 33 | 24 | 17 |
| 120B | 105 | 70 | 53 | 42 | 30 | 21 |
| 160B | 140 | 93 | 70 | 56 | 40 | 28 |

Với YT-sUSDx, FDV hòa vốn phụ thuộc rất mạnh vào APY. Ở 12% APY, FDV hòa vốn là **$138M** (120B points, 3%) hoặc $83M (4%). Ở 16% APY, con số này giảm còn $72M hoặc $54M. Ở mức ≥20.5%, YT-sUSDx hòa vốn với FDV bằng 0.

**ROI trên $1,000 theo kịch bản** (giá trị points + yield − chi phí). Mỗi ô ghi hai số: số đầu là giá trị ở FDV lúc ra mắt, số trong ngoặc là sau hệ số hiện thực hóa.

| Kịch bản (trọng số) | $/1M | YT-USDx | YT-sUSDx |
|---|---|---|---|
| Zero (30%) | $0 | **−$1,000** | −$494 (yield 10%) |
| Bear (40%) | $9.4 | −$465 (−$733) | −$289 (−$343) |
| Base (22%) | $40 | +$1,281 (+$597) | +$254 (+$115) |
| Bull (8%) | $221 | +$11,607 (+$9,086) | +$2,526 (+$2,016) |
| **EV có trọng số** | $30 ($22) | **+$724 (+$265)** | **−$6 (−$99)** |
| EV nếu bỏ phần đóng góp của bull | | −$204 (−$462) | −$208 (−$260) |

Kết quả rất rõ. YT-USDx có EV dương **chỉ nhờ phần đuôi bull**: FDV ≥$300M, 7% airdrop, pool gọn. Trong khoảng **70% trường hợp**, người mua mất gần một nửa hoặc toàn bộ vốn. Đây là hồ sơ của một vé số, không phải một khoản đầu tư có edge ổn định. Thị trường (hòa vốn khoảng $17/1M) đang định giá gần với EV sau hiệu chỉnh của báo cáo ($22/1M), nên edge còn lại mỏng. YT-sUSDx thì gần như là một cược thuần vào yield. Thị trường đang ngầm định APY kỳ hạn khoảng **15.5%** cho sUSDx sau khi trừ phần giá trị points ([Pendle API](https://api-v2.pendle.finance/core/v1/1/markets/0x5e572498e9f83650f0ff24194999bddb4b390928)). Mức này thấp hơn nhiều so với 21.6% hiện tại, nhưng khớp với khung 10–20% của Axis và với mức 11.58% của ogUSDx. Nếu APY giữ trên 20.5%, YT-sUSDx cho points miễn phí. Nếu APY về khoảng 16%, người mua trả khoảng $208 để nhận khoảng 11.5M points, đắt hơn YT-USDx. Bằng chứng lịch sử cũng không ủng hộ: người mua YT thắng lớn ở Ethena S1–S2, nhưng phần lớn hòa hoặc lỗ ở Falcon, Resolv, Usual, Treehouse và Reservoir, và mất trắng ở Level (không có TGE) ([Coinlive](https://www.coinlive.com/news/in-depth-analysis-of-the-actual-return-of-the-pendle-yt); [Level docs](https://level-money.gitbook.io/level-documentation)).

## Thanh khoản mỏng và khoảng trống snapshot–TGE giới hạn quy mô vị thế

Thanh khoản là ràng buộc cứng. Pool YT-USDx chỉ có **$2.24M** thanh khoản và khoảng $19K volume/ngày. Price impact là 3.9% với lệnh $1k, 7.3% với $3k, 10.2% với $5k, 16.3% với $10k, và lệnh **$100k không có route**. Round-trip một vị thế $10k mất **34%**. Pool sUSDx sâu hơn ($5.86M): lệnh $10k chịu 4.3% impact, $30k chịu 10.7%, $100k chịu 29.6%, và round-trip $100k mất 51% ([Pendle Hosted SDK](https://api-v2.pendle.finance/core/v3/sdk/1/convert)). Hệ quả là quy mô hợp lý tối đa khoảng **$2–3k cho YT-USDx** và **$10k (tối đa $30k) cho YT-sUSDx**. YT-USDx trên thực tế là vị thế giữ tới đáo hạn, vì bán ra sớm tốn 4–21% slippage. Implied APY đang nằm trong dải AMM 6–27%. Nếu có tin xấu (cắt multiplier, snapshot sớm), implied có thể rơi khỏi dải này và thanh khoản AMM biến mất.

Thời điểm cũng là một bất lợi mang tính cấu trúc. Points chỉ tích lũy tới **3/12/2026 00:00 UTC**, khi YT đáo hạn, còn Season 1 kết thúc khoảng 14:00 UTC cùng ngày. TGE khả năng cao rơi vào Q2 2027 hoặc muộn hơn. Suốt 3–7 tháng giữa hai mốc, người giữ YT không có tài sản nào để hedge hay bán, trong khi Axis vẫn có thể thêm Season 2, thêm token sale, lọc sybil hoặc áp KYC cho airdrop (Axis đã loại người Mỹ). Rủi ro CEX custody vẫn luôn hiện diện. Một sự cố kiểu FTX hay việc Binance, Bybit hoặc Upbit đóng băng tài sản sẽ vừa xóa yield của sUSDx vừa làm tăng khả năng Coordinates không bao giờ được quy đổi. Theo Pendle, sUSDx còn có cooldown 7 ngày và "negative yield may occur" ([Pendle API marketInfo](https://api-v2.pendle.finance/core/v2/markets/all?limit=100&skip=0)). Ngoài ra, Season 0 nắm khoảng 75% pool và top-10 ví nắm 45.6%, nên người mua YT ở Season 1 chỉ đang tranh phần nhỏ còn lại, và một ví lớn (thậm chí có thể liên quan đến đội ngũ) có thể được ưu tiên khi phân bổ.

## Khuyến nghị hành động và tín hiệu cần theo dõi

**YT-USDx: mua nhỏ như vé số, không mua để đầu tư.** Với người chấp nhận mất toàn bộ khoản bỏ ra, giới hạn ở **$500–2,000, tối đa $3k**, tương đương ≤0.5–1% danh mục, và chia làm nhiều lệnh $500–1,000 để giảm impact. Ở implied APY 15% hiện tại (hòa vốn $17.5/1M), mức giá chỉ ở ngưỡng "chấp nhận được". Mức hấp dẫn là implied APY **≤13%** (mid khoảng 0.0214 USDx/YT tại D = 64.5, hòa vốn khoảng $15/1M). Mức rất hấp dẫn là **≤10.5%** (khoảng 0.0175, hòa vốn khoảng $12/1M). Không nên mua đuổi khi implied vượt 17–18% (hòa vốn khoảng $20/1M), vì khi đó cần cả FDV lẫn % airdrop cùng rơi vào kịch bản base-bull mới có lãi.

**YT-sUSDx: chưa mua.** APY hòa vốn 20.5% đòi hỏi vault giữ nguyên mức thưởng hào phóng hiện tại trong 64 ngày, trong khi thưởng hoàn toàn do đội ngũ quyết định và thị trường chỉ kỳ vọng khoảng 15.5%. Chỉ nên mua khi implied APY **≤15%** (APY hòa vốn khi đó khoảng 15.8%) *và* APY 7 ngày của sUSDx vẫn ≥20%, với quy mô ≤$10k.

**Các lựa chọn thay thế.** Người tin vào Axis nhưng muốn giới hạn rủi ro có thể mua **PT-sUSDx** với mức cố định khoảng 19% (khoảng $30 trên $1k trong 64.5 ngày), rồi dùng đúng phần lãi đó mua YT-USDx. $30 tương đương khoảng **1.7M points** trên mỗi $1k PT, nên points được tài trợ bằng yield chứ không bằng gốc. Tuy vậy, gốc vẫn chịu rủi ro custody CEX. Người đang giữ USDx có thể tiếp tục giữ trong ví ở mức 16x. Cách này rẻ hơn YT về rủi ro mất gốc nhưng đắt hơn tính theo points: chi phí cơ hội $16–34 cho mỗi 1M points so với lãi sUSDx. Người không muốn chịu rủi ro custody thì **không nên tham gia**.

| Tín hiệu | Nguồn | Diễn giải |
|---|---|---|
| Tokenomics, % airdrop, ngày TGE, Season 2, token sale | X @AxisFDN, axis.to/insights | Airdrop ≥5% cho S0+S1 và TGE ≤Q1 2027 → nâng lên base/bull. Có Season 2 chia chung pool hoặc token sale trước → cắt vị thế |
| Tổng Coordinates và tốc độ phát hành/ngày | api.axis.to/api/v1/points/leaderboard (đo lại hằng tuần) | Tổng vượt 120B trước tháng 12, hoặc tổng tăng vọt khi điểm DeFi được ghi nhận hồi tố → kịch bản bear |
| Ví giữ YT có được cộng points không | Leaderboard, app.axis.to/coordinates | Nếu tới giữa tháng 10 vẫn không thấy điểm Pendle → rủi ro YT bị loại tăng |
| Thay đổi multiplier (24x/6x) | Bài đăng của Axis, trường `points` trong Pendle API | Bị cắt → bán ngay, vì YT-USDx không có sàn yield |
| APY 7 ngày của sUSDx | DefiLlama, Pendle underlyingApy | Dưới 18% → YT-sUSDx lỗ. Trên 22% ổn định → YT-sUSDx thành "points miễn phí" |
| Implied APY của YT-USDx / YT-sUSDx | Pendle | ≤13% / ≤15% là vùng mua |
| Polymarket "Axis token by Jun 30, 2027" | polymarket.com | Trên 70% → tăng xác suất base. Dưới 40% → giảm |
| TVL / USDx supply | DefiLlama | Trên $150M → FDV base tăng. Dưới $45M → bear |
| Sự cố ở CEX và peg của USDx | CoinGecko, Curve | USDx dưới $0.99 hoặc tin đóng băng sàn → thoát ngay |

## Kết luận

Điểm mấu chốt là thị trường Pendle đang định giá toàn bộ pool Coordinates Season 0+1 chỉ ở mức **$1.5–2.8M**. Con số này tương đương với kịch bản bear của báo cáo, nghĩa là thị trường không hề ngây thơ về rủi ro của Axis. Edge của người mua YT-USDx không nằm ở chỗ thị trường định giá sai kịch bản trung bình, mà ở việc sở hữu một quyền chọn rẻ vào khả năng Axis vượt qua mô hình quỹ $56M (TVL tăng mạnh, TGE Q1 2027, listing lớn). Quyền chọn đó có giá trị thật, nhưng chỉ nên mua với số tiền sẵn sàng mất toàn bộ. YT-sUSDx, trái với ấn tượng "points miễn phí", thực chất là một cược đòn bẩy khoảng 32 lần vào quyết định chi thưởng tùy ý của chính đội ngũ Axis. Đó không phải là rủi ro nên trả tiền để gánh ở mức implied 19.3%.

Về dài hạn, việc Axis lệch khỏi lộ trình (vault $1B, token đầu 2026) và tốc độ phát hành points không có trần gợi ý rằng Season 1 sẽ không phải là season cuối. Kinh nghiệm từ Strata, Apyx và Level cho thấy ở năm 2026, cách thất bại phổ biến nhất của YT points là **TGE bị trì hoãn và pha loãng kéo dài** chứ không phải FDV thấp. Nhà đầu tư vì vậy nên coi thông báo tokenomics chính thức là điều kiện tiên quyết để tăng vị thế, thay vì đặt cược trước khi có nó.

*Tuyên bố miễn trừ: Báo cáo này chỉ nhằm mục đích nghiên cứu và thông tin, không phải lời khuyên đầu tư hay tài chính. Mọi con số về TGE, FDV, % airdrop và giá trị points là ước tính dựa trên giả định, có thể sai lệch lớn. Coordinates được Axis tuyên bố "không có giá trị tiền tệ và không đảm bảo quyền nhận token". YT có thể mất 100% giá trị, và USDx/sUSDx chịu rủi ro custody tập trung trên CEX. Dữ liệu tính đến 28/9/2026. Hãy tự nghiên cứu (DYOR) và chỉ đầu tư số tiền bạn chấp nhận mất.*
