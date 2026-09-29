# YT Pendle đang trả giá quá cao cho Cores của Tori

Với giá ngày 28/09/2026, **không nên mua YT-trUSD** (implied APY 9.01%, tức khoảng **$0.0084 cho mỗi 1,000 Cores** ở lệnh $1k), còn YT-strUSD chỉ đáng một vị thế đầu cơ nhỏ dành cho người đã chấp nhận rủi ro tín dụng của Tori. Vấn đề cốt lõi là thời điểm: Tori chưa cam kết token nào (docs ghi Cores "are not a promise of any token or payment"), xác suất TGE xảy ra trước ngày đáo hạn Pendle 26/11/2026 chỉ khoảng **3%**, nên Cores tích qua YT sẽ bị pha loãng thêm 4–9 tháng trên nền **157.5 tỷ Cores đã phát hành** cộng 2.2–3.5 tỷ Cores mới mỗi ngày. Ở kịch bản cơ sở (snapshot 31/03/2027 với khoảng 654 tỷ Cores, 5% nguồn cung cho Cores, FDV $75M tương đương 1.0x TVL, chiết khấu hiện thực hóa 25%), **1,000 Cores chỉ đáng khoảng $0.004**, nghĩa là YT-trUSD lỗ khoảng 50% ngay cả khi token ra đời. Gán xác suất 15% bull / 30% base / 20% bear / 35% không có token, EV là **−23% cho YT-trUSD không khóa**, **+15% nếu khóa YT (45x)**, và từ −1% đến +6% trên vốn cho YT-strUSD nếu APY strUSD giữ quanh 10.5%; nhưng khoảng 80% EV nằm trong một kịch bản bull chỉ có xác suất 15%, và mô phỏng Monte Carlo cho xác suất có lãi của YT-trUSD chỉ **8–17%**. Bản thân Tori là sản phẩm thật (TVL khoảng $73M, strUSD trả 10–11% từ carry thị trường tiền tệ mới nổi có phòng hộ FX, peg giữ chặt), nhưng quy mô chỉ bằng khoảng 1/3 trung vị các vụ TGE stablecoin năm 2026, rủi ro lưu ký off-chain cao, và dự án đến đúng lúc trend yield-dollar/points đã nguội khiến FDV/TVL lúc TGE nén từ 5–7x (2024) về khoảng 1x. Giá YT hiện tại ngầm đòi FDV khoảng **$150–240M** mới hòa vốn, gấp 2–3 lần kịch bản cơ sở. Chỉ nên cân nhắc mua khi YT-trUSD implied về ≤ khoảng 6.8% (có khóa), khi YT-strUSD implied hiệu dụng ≤ khoảng 11.1–11.6% đi kèm APY strUSD ≥ 10.5%, hoặc khi Tori công bố ngày kết thúc Season 1 hay tokenomics.

> **Lưu ý:** Đây là phân tích để tham khảo, không phải lời khuyên tài chính. Mọi số liệu thị trường là snapshot ngày **28/09/2026** (Pendle lúc 11:42 UTC, leaderboard Tori lúc 11:44 UTC). Hôm nay là 29/09/2026 nên thời gian tới đáo hạn đã ngắn đi khoảng 1 ngày so với T = 58.51 ngày dùng trong các bảng. Các ngưỡng tính theo implied APY ở phần khuyến nghị gần như không phụ thuộc thời gian, nên vẫn áp dụng được. Báo cáo dùng dấu chấm cho số thập phân. "B" là tỷ, "M" là triệu. Những con số ghi "tính toán" là phép tính của báo cáo trên dữ liệu có nguồn đi kèm.

## Tori là một bàn carry TradFi $73M, không phải "Ethena thứ hai"

Tori là synthetic dollar hai token. **trUSD** là đồng dollar gốc và không sinh lời. **strUSD** là vault ERC-4626: tỷ giá so với trUSD tăng dần theo phần thưởng, và muốn unstake phải chờ **7 ngày**. Mint và redeem trực tiếp theo NAV chỉ mở cho địa chỉ đã KYC và nằm trong whitelist, phí 10 bps mỗi chiều. Người dùng thường chỉ mua được trUSD trên thị trường thứ cấp ([Docs: strUSD](https://docs.tori.finance/products/strusd); [Docs: Minting & Redemption](https://docs.tori.finance/resources/institutional)). Nguồn lợi suất không đến từ funding perp crypto như Ethena. Nó là một bàn giao dịch TradFi được đưa lên chain. Theo feed solvency ngày 28/09/2026, dự trữ là **$75.32M so với 74.89M trUSD lưu hành (tỷ lệ 100.58%)**, phân bổ như sau: **70.3% "Money Markets"**, 11.4% thanh khoản on-chain, 9.5% "FX Collateral" và 8.8% arbitrage delta-neutral trên *cổ phiếu*. Khoảng 90.5% tài sản gửi ở "regulated custodian banks" không nêu tên ([Tori solvency API](https://app.tori.finance/api/solvency)). RockawayX, đơn vị quản lý Ecosystem Vault, mô tả mảng money market là "selected emerging-market money markets", với phần FX được phòng hộ về USD bằng hợp đồng kỳ hạn ([RockawayX](https://www.rockawayx.com/insights/rockawayx-tori-ecosystem-vault-investment-thesis-risk-disclosure)). Serenity Research gọi đây là "the bank carry trade on-chain" ([Serenity Research](https://serenityresearch.substack.com/p/serenity-premium-tori-finance-and)).

APY thực nhận của strUSD thấp dần theo thời gian. Tháng 3 dự án quảng cáo "~15%", lúc launch ngày 27/07 là "12%". Tỷ giá on-chain cho thấy APY bình quân từ khi ra mắt khoảng **10.5%**. Ngày 28/09, app Tori hiển thị **10.21%**, feed solvency là 11.17%, còn Pendle tính ra 11.18% ([Tori /api/apy](https://app.tori.finance/api/apy); [Tori solvency API](https://app.tori.finance/api/solvency); [PANews](https://panews.io/articles/019d24a9-7508-7621-9040-5569a9715caf); [The Defiant](https://thedefiant.io/news/press-releases/tori-brings-institutional-trades-on-chain-fills-50m-before-launch)). Dù vậy, mức này vẫn gấp khoảng 2 lần sUSDe, vốn chỉ có bình quân 30 ngày 4.86% ([Ethena yields API](https://ethena.fi/api/yields/protocol-and-staking-yield)). Lợi suất của Tori cũng gần như không tương quan với tâm lý thị trường crypto. Đó là lợi thế thật trong giai đoạn funding thấp.

TVL tăng theo từng bậc. Vault pre-deposit $50M đầy trong 7 ngày cuối tháng 6. Sau đó TVL lên $66.2M vào cuối tháng 8 và **$73.06M vào ngày 28/09/2026** (tăng 10.4% trong 30 ngày) ([DefiLlama](https://api.llama.fi/protocol/tori-finance)). Nhưng chất lượng TVL mới là điểm cần xem kỹ. Ecosystem Vault (etrUSD) do RockawayX quản lý có supply 44.08M, tương đương khoảng **59% trUSD lưu hành** ([etrUSD](https://etherscan.io/address/0x6f20aE2C98c2D34e6A57f3411f2C5Af92E32592d)). Khoảng **10.77M trUSD (14% nguồn cung)** vừa vào Silo unstake trong các ngày 21–25/09 và sẽ hết cooldown quanh 29/09–01/10 ([Silo](https://etherscan.io/address/0xF7c0d8853E69DCD37ee7599c6280d2632F3360B4)). Cores cũng tập trung: 10 ví lớn nhất nắm 34% tổng Cores, 100 ví lớn nhất nắm 62% ([Tori leaderboard API](https://app.tori.finance/api/leaderboard)). Cộng đồng thì rất nhỏ, với 6,163 follower trên X, 819 thành viên Discord, và 42 cùng 12 thành viên ở hai nhóm Telegram tiếng Trung và tiếng Hàn ([fxtwitter](https://api.fxtwitter.com/tori_finance); [Discord](https://discord.gg/torifinance)). Nói cách khác, đây là một cơ sở vốn do cá voi dẫn dắt và có động cơ farm điểm, loại vốn thường rút đi sau TGE.

Về đội ngũ và nguồn vốn: Tori có một vòng seed do **Delphi Ventures dẫn dắt**, không công bố số tiền hay định giá. Founder Samed Düzçay công khai danh tính ([X: Tommy Shaughnessy](https://x.com/Shaughnessy119/status/2036549390886903837)). Không có quỹ đầu tư nào gắn với sàn giao dịch. Phía rủi ro, pharos.watch chấm trUSD **C- (54/100)** vì ngân hàng lưu ký không nêu tên, mint/redeem có permission, không có price feed on-chain, và dòng tài sản bảo chứng đi tới **BiLira Pro và địa chỉ nạp Binance**. Trong khi đó homepage của Tori lại ghi tài sản được lưu ký tại BitGo, Anchorage và Cactus ([pharos.watch](https://pharos.watch/stablecoin/trusd-tori/)). Ngày 17/09/2026, Tori còn phải đăng rằng dự án "not affected in any way by the fund wind-downs, forced selling and volatility in local markets" ([X @tori_finance](https://x.com/tori_finance/status/2100523360946176201)). Đây là dấu hiệu rằng rủi ro đuôi của Tori nằm ở FX thị trường mới nổi và ở lưu ký, không nằm ở smart contract.

### Tori nhỏ hơn mọi dự án cùng nhóm đã TGE

| Dự án | TGE | TVL/stablecoin lúc TGE | FDV (đóng cửa ngày TGE) | FDV/TVL lúc TGE | Diễn biến đến 28/09/2026 |
|---|---|---|---|---|---|
| Ethena ENA | 02/04/2024 | $1.56B | $11.6B | ~7.4x | −66% so với TGE; hiện ~0.8x USDe |
| Usual USUAL | 18/12/2024 | $875M | $4.16B | ~4.8x | −98.5% |
| Elixir ELX | 07/03/2025 | ~$300M | $389M | ~1.3x | −99.7%, deUSD đã đóng cửa |
| Resolv RESOLV | 10/06/2025 | $351M | $351M | ~1.0x | −95%, USR bị exploit tháng 3/2026 |
| Falcon FF | 29/09/2025 | $1.90B | $2.81B | ~1.5x | −54%, hiện ~1.1x |
| OpenEden EDEN | 30/09/2025 | $235M (USDO) | $398M | ~1.7x | −85% |
| Unitas UP | 13/03/2026 | $81M | $80M | ~1.0x | 3.3x so với ngày đầu |
| USD.AI CHIP | 22/04/2026 | $283M | $636M | ~2.25x | 0.70x |
| Solstice SLX | 25/05/2026 | $401M | $298M | ~0.74x | 0.22x |
| Re RE | 18/06/2026 | $258M | $647M | ~2.5x | 0.71x |
| Cap CAP | 26/06/2026 | $221M | $246M | ~1.1x | 2.25x |
| **Tori (chưa có token)** | — | **$73M** | — | — | — |

Nguồn: giá đóng cửa từ [Gate API](https://api.gateio.ws/api/v4/spot/candlesticks?currency_pair=ENA_USDT&interval=1d), nguồn cung stablecoin từ [DefiLlama stablecoins](https://stablecoins.llama.fi/stablecoins?includePrices=false), nhóm TGE năm 2026 từ [CoinGecko markets API](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=cap-4,plasma,stable-2,unitas,chip-2,solstice,re,river,stbl). Các hệ số là tính toán của báo cáo trên những dữ liệu này.

Bảng trên cho thấy hai điều. Thứ nhất, **FDV/TVL lúc TGE đã nén mạnh**: nhóm 2024 ở 5–7x, nhóm 2025 ở 1–1.7x, và nhóm yield-dollar 2026 có trung vị khoảng **1.1x** với biên 0.7–2.5x. Thứ hai, **FDV lúc TGE của nhóm 2026 có trung vị $298M**, nhưng những dự án này có TVL $81–401M. Tori với $73M nằm ở đáy nhóm và giống Unitas nhất (USDu $81M, FDV ngày đầu $80M). Sau TGE, trung vị của FDV sau 30 ngày chia FDV ngày đầu là 0.79x ([CoinGecko market_chart](https://api.coingecko.com/api/v3/coins/solstice/market_chart?vs_currency=usd&days=365&interval=daily)).

### Trend stablecoin đã nguội ở mảng points, chưa chết ở mảng thanh toán

Phần "yield-dollar + points + Pendle" của câu chuyện stablecoin đã hạ nhiệt rõ ràng. Pendle TVL giảm từ $13.39B (19/09/2025) xuống **$1.26B, tức −91%** ([DefiLlama Pendle](https://api.llama.fi/protocol/pendle)). USDe giảm từ $14.82B xuống $4.94B ([DefiLlama USDe](https://stablecoins.llama.fi/stablecoin/146)). Nhóm stablecoin sinh lời mất **$3.5B (−15%) trong Q2/2026**, lần giảm đầu tiên sau gần ba năm tăng liên tục ([Cointelegraph](https://cointelegraph.com/news/yield-bearing-stablecoins-lose-3-5-billion-q2)), và Ethena đã dừng hẳn ưu đãi ENA cho người stake USDe ([Crypto Briefing](https://cryptobriefing.com/ethena-ends-usde-token-incentives/)). Sự cố trong cùng phân khúc cũng dày lên: Neutrl mở redeem ở mức **0.51 USDC mỗi NUSD** ([The Crypto Times](https://www.cryptotimes.io/2026/09/18/neutrl-opens-nusd-snusd-redemptions-as-on-chain-rate-reads-0-51/)), Apyx hoãn TGE vô thời hạn khoảng ngày 23/09/2026 ([PANews](https://panews.io/articles/01a0cef7-c910-768e-9d43-2194fd1a5897)), còn Cap cắt Stabledrop từ $12M xuống $4.2M và chỉ bù lỗ cho người giữ YT, với kết quả "none turned a profit" ([The Defiant](https://thedefiant.io/news/defi/cap-cuts-its-stabledrop-airdrop-to-usd4-2m-from-usd12m-as-backlash-mounts)).

Vẫn có dấu hiệu ở chiều ngược lại. Tổng stablecoin đạt $311.5B, sát đỉnh $320.3B ([DefiLlama](https://stablecoins.llama.fi/stablecoincharts/all)). USDe tăng 21% trong 30 ngày và Pendle TVL đã hồi 27% từ đáy tháng 6. Thị trường chung đang ở pha hồi trong một con gấu lớn: BTC $83k, thấp hơn đỉnh 33% ([CoinGecko](https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=365&interval=daily)), chỉ số altseason 56/100 ([CryptoRank](https://cryptorank.io/news/feed/b29a4-the-altcoin-season-index-is-at-56-and-that-number-does-not-mean-altseason)), và khoảng 85–93% token ra mắt gần đây đang dưới giá TGE ([CoinDesk](https://www.coindesk.com/business/2026/01/06/why-crypto-s-new-token-issues-are-falling-flat-and-what-comes-next); [Bitget/CryptoRank](https://www.bitget.com/news/detail/12560605525394)).

Đánh giá tiềm năng: Tori có một sản phẩm khác biệt thật (lợi suất gấp đôi sUSDe và không tương quan với crypto) cùng bộ khung trông khá chuẩn tổ chức (audit Sherlock và Nethermind, proof-of-reserves Accountable, curator RockawayX). Nhưng dự án đang ở quy mô "Unitas", không phải "Falcon". Nó ra mắt đúng lúc thị trường định giá lại toàn phân khúc về mức khoảng 1x TVL. Rủi ro đuôi lại là loại mà thị trường vừa chứng kiến xảy ra năm nay (Neutrl, Resolv, Elixir). Trần định giá của Tori vì vậy phụ thuộc gần như hoàn toàn vào việc TVL có tăng mạnh trước TGE hay không.

## TGE nhiều khả năng rơi vào năm 2027, sau ngày đáo hạn Pendle

Nguồn chính thức gần như không cho gì. Season 1 bắt đầu ngày 23/06/2026. Cores dùng để làm gì thì "has not been announced yet". "Future seasons will define how the protocol recognizes it" ([Docs: General FAQ](https://docs.tori.finance/faq/general); [Docs: Cores](https://docs.tori.finance/resources/cores)). App còn có dòng chữ "Post-launch, no date committed" ([app.tori.finance](https://app.tori.finance/activities)). Hiện chưa có token, chưa có tokenomics, chưa có ngày kết thúc Season 1, không có dấu hiệu niêm yết Binance hay pre-market, và Tori cũng không có thị trường nào trên Whales Market, Hyperliquid hay Aevo ([Whales Market API](https://api.whales.market/v2/tokens?search=tori); [Hyperliquid API](https://api.hyperliquid.xyz/info)).

Polymarket là tín hiệu thị trường duy nhất, và nó rất mỏng: thị trường đặt **39%** cho việc có token trước 31/12/2026 (khối lượng khoảng $7.5K, lần khớp cuối 0.34), 57.5% trước 30/06/2027 và 66.5% trước 31/12/2027, trong khi mốc 30/09/2026 không có giao dịch nào ([Polymarket](https://polymarket.com/event/will-tori-launch-a-token-by)).

Các dự án tương tự cho khung tham chiếu về độ dài chiến dịch điểm trước TGE (với Falcon, Solstice và USD.AI, con số là khoảng thời gian từ khi có dữ liệu TVL/nguồn cung đến TGE):

| Dự án | Độ dài chiến dịch trước TGE |
|---|---|
| Ethena | 6 tuần |
| Usual | 132 ngày đến pre-market, 161 ngày đến spot |
| Falcon | khoảng 189 ngày |
| OpenEden | khoảng 6.5 tháng |
| Solstice | khoảng 236 ngày |
| Resolv | 9 tháng |
| USD.AI | khoảng 338 ngày |

Nguồn: [Bitcoin.com](https://news.bitcoin.com/ethena-details-ena-airdrop-for-shard-holders-announces-bitcoin-sats-campaign/), [Coinspeaker](https://www.coinspeaker.com/binance-introduces-usual-launchpool-pre-market-trading-soon/), [DefiLlama USDf](https://stablecoins.llama.fi/stablecoin/246), [OpenEden](https://openeden.com/news/openseason-next-phase-bills-points-eden-rewards/), [Resolv docs](https://docs.resolv.xyz/litepaper/resolv-token/resolv-token-airdrop), [DefiLlama Solstice](https://api.llama.fi/protocol/solstice).

Áp các độ dài này vào ngày bắt đầu 23/06/2026, TGE của Tori rơi vào khoảng 02/11/2026 (132 ngày), 29/12/2026 (189 ngày), 14/02/2027 (236 ngày) đến 27/05/2027 (338 ngày). Báo cáo kéo ước tính về phía muộn hơn các mốc này vì ba lý do. Thứ nhất, các dự án thành công đều báo trước vài tuần: Resolv mở đăng ký từ 9–25/05 rồi mới TGE ngày 10/06, OpenEden kết thúc Bills ngày 15/09 và TGE ngày 30/09, còn Tori hiện chưa có bước chuẩn bị nào như vậy. Thứ hai, các dự án thường TGE lúc TVL ở gần đỉnh (ENA, USUAL, FF và ELX đều như vậy), nên với TVL chỉ $73M, Tori có động cơ kéo dài chiến dịch để tăng TVL trước. Thứ ba, thị trường đang phạt các dự án ra mắt vội, và Apyx vừa hoãn TGE.

Chuỗi tin tăng trưởng trong tháng 9 cũng không đủ làm thay đổi kết luận này. Tori mở Monad và Pharos, được BitGo hỗ trợ, dịch app sang 9 ngôn ngữ và mở cộng đồng tiếng Trung, tiếng Hàn ([X @tori_finance](https://x.com/tori_finance/status/2097961000964350270)). Những việc này khớp với một kịch bản chuẩn bị TGE, nhưng cũng khớp y hệt với việc chuẩn bị Season 2.

| Kịch bản | Snapshot Cores (giả định) | TGE (giả định) | Xác suất | Lập luận |
|---|---|---|---|---|
| **Bull** | 31/12/2026 | khoảng 15/02/2027 | 15% | Season 1 dài khoảng 190 ngày như Falcon/OpenEden; tận dụng nhịp hồi thị trường tháng 9 |
| **Base** | 31/03/2027 | khoảng 01/06/2027 | 30% | Season 1 dài khoảng 9 tháng như Resolv; cần thêm thời gian để tăng TVL |
| **Bear** | 30/06/2027 (S1 kéo dài hoặc gộp với S2) | khoảng 31/10/2027 | 20% | Thị trường xấu, trì hoãn giống Apyx |
| **Không có token đến hết 2027** | — | — | 35% | Không có cam kết; Polymarket đặt 33.5% |

Xác suất tích lũy theo mốc thời gian, so với Polymarket:

| Mốc thời gian | Ước tính của báo cáo | Polymarket (28/09/2026) |
|---|---|---|
| TGE trước 26/11/2026 (ngày đáo hạn Pendle) | **khoảng 3%** | mốc 30/09 không có giao dịch |
| TGE trước 31/12/2026 | khoảng 10% | 39% |
| TGE trước 30/06/2027 | khoảng 45% | 57.5% |
| TGE trước 31/12/2027 | khoảng 65% | 66.5% |

Ước tính của báo cáo nghiêng bear hơn Polymarket ở các mốc gần, và điều đó là có chủ đích. Hệ quả trực tiếp cho người mua YT là: **dòng Cores từ YT dừng lại ngày 26/11/2026, nhưng giá trị của chúng được quyết định ở một snapshot muộn hơn nhiều.** Trong kịch bản cơ sở, 125 ngày giữa đáo hạn và snapshot 31/03/2027 sẽ in thêm khoảng 340 tỷ Cores (với 2.7 tỷ Cores mỗi ngày). Con số này lớn hơn toàn bộ khoảng 300 tỷ Cores tồn tại vào ngày đáo hạn.

## FDV hợp lý nằm trong khoảng $30–180M, kịch bản cơ sở khoảng $75M

Có ba mỏ neo cho FDV của Tori.

Thứ nhất là **FDV/TVL của các dự án tương tự**: nhóm 2026 có trung vị khoảng 1.1x. Sau TGE, thị trường định giá lại theo mức TVL còn giữ được. CAP và RE giữ TVL và đứng ở 1.2–1.9x; SLX mất 46% TVL và rơi xuống 0.31x ([DefiLlama Solstice](https://api.llama.fi/protocol/solstice)).

Thứ hai là **TVL mà Tori có thể mang vào TGE**. Hiện tại là $73M. Có hai lực kéo xuống: 14% nguồn cung đang nằm chờ trong Silo, và 59% supply gắn với một vault duy nhất. Có một lực kéo lên: tính năng mới trên Monad, Pharos và BitGo.

Thứ ba là **Polymarket** "FDV above ___ one day after launch". Sau khi chia cho xác suất 66.5% có token, thị trường này ngầm cho khoảng **41% FDV trên $50M, 34% trên $100M và 29% trên $200M**. Trung vị ngầm định vì thế dưới $50M. Tuy nhiên tổng khối lượng giao dịch chỉ khoảng $16.7K, nên đây là tín hiệu yếu ([Polymarket FDV](https://polymarket.com/event/tori-finance-fdv-above-one-day-after-launch)). Báo cáo không tìm thấy KOL hay nhà phân tích nào công bố ước tính FDV cho Tori. Phần định giá trong báo cáo của Serenity nằm sau paywall.

| Kịch bản | TVL lúc TGE | FDV/TVL | FDV (đóng cửa ngày TGE) | Chiết khấu khi hiện thực hóa* | Căn cứ |
|---|---|---|---|---|---|
| Bull | khoảng $100M | khoảng 1.8x | **$180M** | 10% | RE 2.5x, CHIP 2.25x; Polymarket: P(>$200M \| có token) ≈ 29% |
| Base | khoảng $75M | khoảng 1.0x | **$75M** | 25% | Trung vị 2026 khoảng 1.1x; Unitas $80M với $81M TVL; FDV sau 30 ngày bằng 0.79x ngày đầu |
| Bear | khoảng $60M | khoảng 0.5x | **$30M** | 40% | SLX 0.31–0.74x; trung vị Polymarket dưới $50M; tiền lệ FF cho chọn bỏ 50% airdrop |

\*Chiết khấu gộp các yếu tố: vesting hoặc forfeiture (FF: nhận 30% ngay và vest 70%, hoặc bỏ 50% để nhận ngay; EDEN: "Starting Portion" 20–80%), giá sụt trong vài tuần đầu (RESOLV −35% sau 7 ngày, SLX −23% sau 30 ngày), và trượt giá khi bán ([Tokenomist FF](https://tokenomist.ai/falcon-finance-ff); [OpenEden](https://openeden.com/news/openseason-next-phase-bills-points-eden-rewards/)).

Phần nguồn cung dành cho người giữ điểm ở mùa đầu tiên của các dự án tương tự:

| Dự án | % nguồn cung cho điểm mùa đầu |
|---|---|
| ENA S1 | 5% |
| USUAL | 7.5% |
| EDEN | 7.5% |
| RESOLV | 10% |
| ELX | 8% |
| FF | khoảng 5% public, nằm trong quỹ cộng đồng 8.3% |
| SLX | 7.5% |
| CHIP | 3% |
| STABLE | khoảng 2.5% |

Nguồn: [DL News](https://www.dlnews.com/articles/defi/ethena-500m-airdrop-leads-defi-project-to-plan-the-next-one/), [CoinGecko](https://www.coingecko.com/learn/what-is-usual-crypto-rwa-usual-airdrop), [ChainCatcher](https://www.chaincatcher.com/en/article/2180331), [Falcon](https://falcon.finance/news/introducing-ff-tokenomics), [Solstice docs](https://docs.solstice.finance/solstice-for-users/slx/tokenomics), [Coin Gabbar](https://www.coingabbar.com/en/crypto-currency-news/usd-ai-airdrop-chip-token-coinlist-sale-tge-march-2026-details).

Báo cáo chọn **8% / 5% / 3%** cho bull / base / bear. Có một phép kiểm tra chéo: ở kịch bản cơ sở, quỹ Cores thực nhận là $2.81M trên TVL bình quân khoảng $75M trong 281 ngày của Season 1. Con số đó tương đương khoảng **4.9%/năm trên vốn gửi**. Mức này nằm giữa biên 3–11%/năm mà các airdrop stablecoin 2026 thực trả tại giá TGE: Solstice 8.4–10.9%, USD.AI 2.7–5.8%, Cap 3.4% (tính toán; [tổng hợp comps](https://thedefiant.io/news/defi/cap-cuts-its-stabledrop-airdrop-to-usd4-2m-from-usd12m-as-backlash-mounts)). Vậy kịch bản cơ sở không hề bi quan quá mức so với những gì các dự án cùng nhóm thực sự đã trả.

## 157.5 tỷ Cores đã phát hành, và mỗi ngày có thêm khoảng 2.2–2.5 tỷ

### Cơ chế Cores và điểm mỗi ngày

"Nx" trong app Tori nghĩa là N Cores cho mỗi $1, hoặc mỗi 1 đơn vị tài sản cơ sở, mỗi ngày. Bảng hệ số được publish lúc launch ngày 27/07/2026 và vẫn đang áp dụng ([app bundle](https://app.tori.finance/_next/static/immutable/chunks/2k0jyeo_ewi3n.js)). API points của Pendle xác nhận các hệ số của thị trường Pendle dưới dạng "points-per-asset": YT-trUSD là 30, LP trUSD 45, YT-strUSD 6, LP strUSD 9 ([Pendle points API](https://api-v2.pendle.finance/core/v1/markets/points-market?chainId=1)).

| Hoạt động | Cores/$/ngày | Ghi chú |
|---|---|---|
| Giữ trUSD | 25x | Không có yield |
| Stake strUSD | 5x | APY khoảng 10.2–11.2% |
| Ecosystem Vault (etrUSD) | 35x | apy7d 5.96%, rút mất 7 ngày |
| Curve/Fluid trUSD-USDC, Curve frxUSD-trUSD | 30x | |
| Morpho: cho vay USDC | 10x | |
| PT (thế chấp trên Morpho) | **0x** | "No Cores on PT" |
| **YT-trUSD** | **30x trên mỗi YT** | 1 YT = 1 trUSD notional |
| **YT-trUSD khóa (YT-Lock)** | **45x** | "Once locked, YT cannot be withdrawn" |
| LP trUSD (Pendle) | 45x, chỉ tính trên phần SY | Khoảng 36 Cores/$/ngày (SY chiếm 80.2% pool) |
| **YT-strUSD** | **6x trên mỗi YT** | Vẫn nhận yield strUSD |
| YT-strUSD khóa | 9x | Vẫn claim được yield |
| LP strUSD (Pendle) | 9x, chỉ tính trên phần SY | Khoảng 6.9 Cores/$/ngày |
| Referral | +10% Cores của người được mời | Không giới hạn; người mua không được hưởng |

Công thức: **Cores/ngày = Σ(quy mô vị thế × hệ số) × boost ví (nếu có) + 10% Cores của người được giới thiệu**. Với YT, hệ số áp trên toàn bộ notional, không phải trên số tiền bỏ ra mua YT. Vì vậy **$1,000 mua YT-trUSD (lệnh $1k, nhận 67,952 YT) cho khoảng 2.04 triệu Cores/ngày, hay 3.06 triệu Cores/ngày nếu khóa**. So sánh: giữ $1,000 trUSD chỉ cho 25,000 Cores/ngày. Tính đến đáo hạn, $1,000 YT-trUSD mang lại **119.3 triệu Cores (178.9 triệu nếu khóa)**. $1,000 YT-strUSD cho 339 nghìn Cores/ngày (508 nghìn nếu khóa), tổng **19.8 triệu (29.8 triệu nếu khóa)** (tính toán từ [Pendle convert API](https://api-v2.pendle.finance/core/v2/sdk/1/convert)). Một vị thế $1k YT-trUSD chỉ chiếm khoảng **0.08% lượng Cores phát hành mỗi ngày**.

Có hai cách đọc hệ số cần kiểm tra. Cách thứ nhất là 30 Cores cho mỗi YT mỗi ngày. Cách thứ hai là 30 Cores cho mỗi $ bỏ ra mua YT, và nếu vậy YT sẽ tệ hơn khoảng 73 lần. Dữ liệu on-chain ủng hộ cách đọc thứ nhất. Ví 0x6b28fb12 giữ 499.5k YT-trUSD và có 0.816B Cores, tương đương khoảng **54 ngày** nắm giữ ở 30 Cores/YT/ngày. Ví 0x3b561a4e khóa 301.7k lYT-trUSD và có 0.67B Cores, tương đương khoảng **49 ngày** ở 45x. Thị trường Pendle mới mở khoảng 63–71 ngày, nên cả hai mức đều hợp lý (tính toán từ [leaderboard](https://app.tori.finance/api/leaderboard) và [Ethplorer lYT-trUSD](https://api.ethplorer.io/getTopTokenHolders/0x10b2487173d9f7087c8bdce9e70fd135212a8d7d?apiKey=freekey&limit=10)).

### Tổng cung Cores và lạm phát điểm

Ngày 28/09/2026 lúc 11:44 UTC, leaderboard công khai báo **157,501,782,271 Cores trên 6,467 ví**. Bình quân từ ngày đầu là 1.62B/ngày ([Tori leaderboard API](https://app.tori.finance/api/leaderboard)). Ước tính từ dưới lên, lấy quy mô từng venue nhân với hệ số, ra khoảng **2.43B/ngày trước khi trừ phần tính trùng**. Con số làm việc là 2.0–2.5B/ngày, trung tâm khoảng 2.2B. Riêng Ecosystem Vault đã chiếm khoảng 1.56B/ngày ($44.65M × 35) ([Tori /api/vault/info](https://app.tori.finance/api/vault/info)). Để lường trước rủi ro, bảng dưới đây cố ý dùng dải rộng và nghiêng về phía phát hành nhiều. Các nguồn có thể đẩy tốc độ phát hành lên gồm: TVL tăng, venue hệ số cao mới (YT-Lock 45x, Monad), boost chiến dịch, referral, và khả năng Season 2 tăng tốc độ phát hành để kéo TVL.

**Tổng Cores lưu hành, đơn vị tỷ Cores = 157.5 + r × số ngày kể từ 28/09/2026**

| Tốc độ phát hành r (tỷ/ngày) | 26/11/2026 (+59 ngày) | 31/12/2026 (+94) | 31/03/2027 (+184) | 30/06/2027 (+275) | 30/09/2027 (+367) |
|---|---|---|---|---|---|
| 2.0 | 275.5 | 345.5 | 525.5 | 707.5 | 891.5 |
| 2.5 | 305.0 | 392.5 | 617.5 | 845.0 | 1,075.0 |
| 3.0 | 334.5 | 439.5 | 709.5 | 982.5 | 1,258.5 |
| 3.5 | 364.0 | 486.5 | 801.5 | 1,120.0 | 1,442.0 |
| 4.0 | 393.5 | 533.5 | 893.5 | 1,257.5 | 1,625.5 |

Mâu thuẫn về tốc độ thời pre-deposit không làm thay đổi bảng này. Docs ghi "2x boost, 30 Cores per dollar per day", còn các trang tracker đọc thành 60 ([Docs: Pre-Deposit](https://docs.tori.finance/resources/pre-deposit); [usethebitcoin](https://usethebitcoin.com/airdrop/tori-finance/)). Tổng Cores hiện tại được đo trực tiếp, nên không phụ thuộc vào cách đọc nào. Ngoài ra, cách đọc 60 không khớp dữ liệu. Nếu pre-deposit trả 60/$/ngày, riêng giai đoạn đó đã phát 90–102 tỷ Cores. Phần còn lại sau launch khi ấy chỉ khoảng 0.9–1.1 tỷ/ngày, trong khi riêng vault 35x đã phát khoảng 1.56 tỷ/ngày.

### Giá trị của 1,000 Cores

Công thức: **$/1,000 Cores = X × FDV × (1 − h) / C × 1,000**. Trong đó X là % nguồn cung dành cho Cores, h là chiết khấu khi hiện thực hóa, và C là tổng Cores lúc snapshot. Sau đó chiết khấu thêm theo thời gian đến ngày TGE với lãi suất 10.5%/năm, bằng chi phí cơ hội của strUSD.

| Kịch bản | Snapshot | r (tỷ/ngày) | C (tỷ Cores) | X | FDV | h | Quỹ thực nhận | **$/1,000 Cores** | Sau chiết khấu thời gian | Xác suất |
|---|---|---|---|---|---|---|---|---|---|---|
| Bull | 31/12/2026 | 2.2 | 364.3 | 8% | $180M | 10% | $12.96M | **$0.0356** | $0.0342 | 15% |
| Base | 31/03/2027 | 2.7 | 654.3 | 5% | $75M | 25% | $2.81M | **$0.00430** | $0.00402 | 30% |
| Bear | 30/06/2027 | 3.5 | 1,120 | 3% | $30M | 40% | $0.54M | **$0.00048** | $0.00043 | 20% |
| Không có token | — | — | — | — | — | — | $0 | **$0** | $0 | 35% |
| **Kỳ vọng theo xác suất** | | | | | | | | $0.00672 | **$0.00643** | |

Kỳ vọng $0.0064 này **80% đến từ kịch bản bull**. Kịch bản bull lại là một "góc thuận lợi" trong đó snapshot sớm, FDV cao và tỷ lệ phân bổ lớn cùng xảy ra một lúc. Để kiểm tra điểm yếu này, báo cáo chạy mô phỏng Monte Carlo 200,000 lần, trong đó các biến được rút ngẫu nhiên và không bị ép cùng thuận lợi. Xác suất có token là 65%. Ngày snapshot theo phân phối tam giác 64/185/460 ngày tính từ 28/09. TVL lúc TGE theo lognormal với trung vị $75M và σ = 0.45. FDV/TVL theo lognormal với trung vị 1.0x và σ = 0.6. Tốc độ phát hành bằng TVL bình quân nhân với k, trong đó k phân phối đều từ 30 đến 45 Cores/$/ngày. X theo phân phối tam giác 2/5/9%, còn h phân phối đều từ 5% đến 45%.

Kết quả: **giá trị kỳ vọng $0.0030/1,000 Cores, trung vị $0.0018**. Nếu chỉ xét các trường hợp có token: bình quân $0.0046, trung vị $0.0033, p10 $0.0012, p90 $0.0093. FDV có điều kiện của mô phỏng có trung vị $75M (p10 $29M, p90 $196M). Tổng Cores lúc snapshot có trung vị 792 tỷ.

Hai con số tham chiếu từ thị trường đều cao hơn các ước tính trên. Giá YT-trUSD giữa ngày 28/09 ngầm định **$0.0078/1,000 Cores**. RockawayX ghi "Points APY 8.73%" cho Phase 1 (pre-deposit), tương đương **$0.0080/1,000 Cores** ở tốc độ 30/$/ngày hoặc $0.0040 ở 60/$/ngày ([RockawayX](https://www.rockawayx.com/insights/rockawayx-tori-ecosystem-vault-investment-thesis-risk-disclosure)). Cả hai mức cao hơn kịch bản cơ sở khoảng 80–90% và gấp 2.6 lần kỳ vọng Monte Carlo, và RockawayX lại là bên có lợi ích trực tiếp khi định giá điểm cao.

**Độ nhạy của $/1,000 Cores theo FDV và tổng Cores lúc snapshot (X = 5%, h = 25%, chưa chiết khấu thời gian)**

| C lúc snapshot | FDV $30M | $50M | $75M | $100M | $150M | $200M | $300M |
|---|---|---|---|---|---|---|---|
| 346 tỷ | 0.00326 | 0.00543 | 0.00814 | 0.01085 | 0.01628 | 0.02171 | 0.03256 |
| 393 tỷ | 0.00287 | 0.00478 | 0.00717 | 0.00955 | 0.01433 | 0.01911 | 0.02866 |
| 654 tỷ | 0.00172 | 0.00287 | 0.00430 | 0.00573 | 0.00860 | 0.01146 | 0.01719 |
| 845 tỷ | 0.00133 | 0.00222 | 0.00333 | 0.00444 | 0.00666 | 0.00888 | 0.01331 |
| 1,120 tỷ | 0.00100 | 0.00167 | 0.00251 | 0.00335 | 0.00502 | 0.00670 | 0.01004 |

Đổi X thì giá trị đổi tuyến tính: X = 3% nhân 0.6, X = 8% nhân 1.6, X = 10% nhân 2.0. Muốn vượt chi phí $0.0084 của YT-trUSD ở kịch bản pha loãng cơ sở (654 tỷ Cores, X = 5%), cần FDV khoảng $150M. Đó là mức FDV/TVL khoảng 2x, chỉ thấy ở những TGE tốt nhất năm 2026.

## Giá YT hiện tại đòi FDV $150–240M mới hòa vốn

### Cơ chế định giá và phần yield trả về

Cả hai thị trường Tori trên Pendle đều ở Ethereum và cùng đáo hạn **26/11/2026**. Tính từ 28/09 lúc 11:42 UTC, còn T = 58.51 ngày, tức t = 0.16031 năm ([Pendle API](https://api-v2.pendle.finance/core/v1/markets/all)). Giá YT theo implied APY là **YT = 1 − (1 + implied)^(−t)**, tính bằng trUSD. Với YT-strUSD, phần yield trả về sau phí Pendle 5% là **yield-back mỗi YT = 0.95 × [(1 + u)^t − 1]**, trong đó u là APY strUSD thực nhận. Công thức này tái tạo được ytRoi của Pendle (−5.27% so với con số API −5.25%), còn nếu bỏ phí 5% thì ra −0.29%, sai hẳn, nên có thể khẳng định phí 5% đang áp lên yield ([Pendle Docs: Fees](https://docs.pendle.finance/pendle-v2/ProtocolMechanics/Mechanisms/Fees)). **Chi phí ròng mỗi $1,000 = 1,000 − N × yield-back × p**, với N là số YT nhận được và p = $0.9999 là giá trUSD; **$/1,000 Cores = chi phí ròng / (N × hệ số × T) × 1,000**.

| Chỉ số (28/09/2026) | YT-strUSD | YT-trUSD |
|---|---|---|
| Giá YT (giữa) | $0.017184 | $0.013731 |
| Implied APY | 11.42% | 9.01% |
| Underlying APY (phần yield trả về) | 11.18% theo Pendle (app Tori: 10.21%) | **0%** |
| Implied APY hiệu dụng khi vào lệnh $1k | khoảng 11.78% | khoảng 9.69% |
| Thanh khoản / volume 24h | $7.20M / $72.9K | $2.57M / $35.7K |
| Cores mỗi YT mỗi ngày | 6 (khóa: 9) | 30 (khóa: 45) |
| Tỷ lệ YT đã khóa | 16.6% | **54.3%** |

Nguồn: [Pendle strUSD data](https://api-v2.pendle.finance/core/v2/1/markets/0xac028348c46d3455899a2b9b50077c11960eaddb/data), [Pendle trUSD data](https://api-v2.pendle.finance/core/v2/1/markets/0xfcf009cb3135da12a6eb1f73f3ee05392a7bc947/data), [Tori /api/apy](https://app.tori.finance/api/apy).

YT không hề đắt lên khi thời gian trôi qua. Implied APY của YT-trUSD lên đỉnh 14.04% ngày 28/07, chạm đáy 8.04% ngày 13/08, và hiện ở 9.01%. Phần YT-strUSD trả thêm so với underlying đã co từ +1.78 điểm % (03/08) xuống **+0.24 điểm %** ([Pendle history](https://api-v2.pendle.finance/core/v2/1/markets/0xfcf009cb3135da12a6eb1f73f3ee05392a7bc947/historical-data?time_frame=day)). Thị trường không cho thấy dấu hiệu đang đặt cược vào một TGE sắp tới.

### Chi phí mỗi 1,000 Cores

**YT-trUSD (không có yield trả về, chi phí ròng luôn bằng $1,000)**

| Quy mô lệnh | YT nhận/$1k | Cores/ngày | Tổng Cores đến đáo hạn | $/1k Cores | Nếu trừ 5% Cores | Khóa 45x | Khóa + trừ 5% |
|---|---|---|---|---|---|---|---|
| Giá giữa | 72,829 | 2.18M | 127.8M | 0.00782 | 0.00823 | 0.00521 | 0.00549 |
| $1k | 67,952 | 2.04M | 119.3M | **0.00838** | 0.00882 | **0.00559** | 0.00588 |
| $10k | 49,435 | 1.48M | 86.8M | 0.01152 | 0.01213 | 0.00768 | 0.00809 |
| $50k | 30,543 | 0.92M | 53.6M | 0.01865 | 0.01963 | 0.01243 | 0.01309 |

**YT-strUSD, lệnh $1k (56,496 YT; 19.83M Cores, hoặc 29.75M nếu khóa)**

| APY strUSD thực nhận u | Yield trả về | Chi phí ròng | $/1k Cores (6x) | $/1k Cores (khóa 9x) |
|---|---|---|---|---|
| 11.18% (Pendle 7 ngày) | $919.6 | $80.4 | **0.00406** | 0.00270 |
| 10.51% (bình quân 30 ngày) | $866.7 | $133.3 | **0.00672** | 0.00448 |
| 10.21% (app Tori 7 ngày) | $842.9 | $157.1 | 0.00792 | 0.00528 |
| 9.0% (yield bị nén) | $746.5 | $253.5 | 0.01278 | 0.00852 |
| 7.83% (−30%) | $652.2 | $347.8 | 0.01754 | 0.01169 |
| 5.59% (−50%) | $470.0 | $530.0 | 0.02672 | 0.01781 |
| 0% (có sự cố) | $0 | $1,000 | 0.05042 | 0.03361 |

Khi tăng quy mô lệnh YT-strUSD, trượt giá ăn mạnh vào hiệu quả. Ở u = 10.51%, lệnh $10k tốn $0.00874/1k Cores; lệnh $50k tốn $0.02628 do price impact khoảng 30%. Muốn chi phí ròng về 0, strUSD phải đạt APY **12.21%** với lệnh $1k và 12.72% với lệnh $10k. YT-strUSD rẻ hơn YT-trUSD trên mỗi Core khi u ≥ khoảng 10.1% (so sánh ở cùng lệnh $1k). APY 7 ngày mà chính app Tori báo, 10.21%, đang nằm đúng tại ngưỡng này.

**So với các cách khác để nhận Cores (mỗi $1,000, trong 58.5 ngày; chi phí cơ hội tính so với giữ strUSD ở 11.18%)**

| Chiến lược | Cores/ngày | Tổng Cores | Yield nhận được | Chi phí cơ hội | $/1k Cores | Giá trị Cores kỳ vọng (ở $0.0064/1k) | Rủi ro gốc |
|---|---|---|---|---|---|---|---|
| Giữ strUSD (5x) | 5,000 | 0.29M | +$17.1 | 0 | khoảng 0 | $1.9 | Toàn bộ $1,000 |
| LP strUSD trên Pendle | 6,899 | 0.40M | +$17.4 | −$0.3 | khoảng 0 | $2.6 | Toàn bộ |
| Ecosystem Vault (35x, APY 5.96%) | 35,000 | 2.05M | +$9.3 | $7.8 | 0.0038 | $13.2 | Toàn bộ, rút mất 7 ngày |
| LP trUSD trên Pendle | 36,100 | 2.11M | +$4.2 | $13.0 | 0.0061 | $13.6 | Toàn bộ |
| Giữ trUSD (25x) | 25,000 | 1.46M | 0 | $17.1 | 0.0117 | $9.4 | Toàn bộ |
| YT-strUSD $1k, u = 10.51% (6x / khóa 9x) | 339k / 508k | 19.8M / 29.8M | $866.7 trả về | $133.3 | 0.0067 / 0.0045 | $127 / $191 | Khoảng $1,000, phụ thuộc APY |
| YT-trUSD $1k (30x / khóa 45x) | 2.04M / 3.06M | 119.3M / 178.9M | 0 | $1,000 | 0.0084 / 0.0056 | $767 / $1,150 | $1,000, về 0 khi đáo hạn |

Tính toán từ [Pendle API](https://api-v2.pendle.finance/core/v2/1/markets/0xac028348c46d3455899a2b9b50077c11960eaddb/data) và [bảng hệ số của app](https://app.tori.finance/_next/static/immutable/chunks/2k0jyeo_ewi3n.js). Các chiến lược không dùng Pendle còn tiếp tục tích Cores sau 26/11 cho tới snapshot. Đó là một lợi thế mà bảng này chưa tính vào.

### Lợi nhuận kỳ vọng theo từng kịch bản

ROI tính trên $1,000 vốn bỏ vào: **(yield trả về + tổng Cores × giá trị/1,000 Cores đã chiết khấu thời gian) / 1,000 − 1**.

| Công cụ | Bull (15%) | Base (30%) | Bear (20%) | Không token (35%) | **EV** | EV nếu Pendle trừ 5% Cores |
|---|---|---|---|---|---|---|
| YT-trUSD, giá giữa (tham chiếu) | +338% | −49% | −94% | −100% | −18% | −22% |
| **YT-trUSD $1k** | +308% | −52% | −95% | −100% | **−23%** | −27% |
| **YT-trUSD $1k khóa 45x** | +513% | −28% | −92% | −100% | **+15%** | +9% |
| YT-trUSD $10k | +197% | −65% | −96% | −100% | −44% | −47% |
| YT-trUSD $10k khóa | +346% | −48% | −94% | −100% | −16% | −21% |
| YT-trUSD $50k | +84% | −78% | −98% | −100% | −66% | −67% |
| YT-strUSD $1k, u = 11.18% | +60% | 0% | −7% | −8% | +5% | +4% |
| YT-strUSD $1k khóa, u = 11.18% | +94% | +4% | −7% | −8% | +11% | +10% |
| **YT-strUSD $1k, u = 10.51%** | +55% | −5% | −12% | −13% | **−1%** | −1% |
| **YT-strUSD $1k khóa, u = 10.51%** | +89% | −1% | −12% | −13% | **+6%** | +5% |
| YT-strUSD $1k, u = 10.21% | +52% | −8% | −15% | −16% | −3% | −4% |
| YT-strUSD $1k, u = 9.0% | +43% | −17% | −24% | −25% | −13% | −13% |
| YT-strUSD $1k, u = 7.83% | +33% | −27% | −34% | −35% | −22% | −23% |
| YT-strUSD $10k, u = 10.51% | +49% | −9% | −16% | −17% | −4% | −5% |
| YT-strUSD $50k, u = 10.51% | +11% | −32% | −37% | −38% | −28% | −29% |

Monte Carlo cho bức tranh xấu hơn, vì nó không cho phép "góc bull" xảy ra thường xuyên. Với **YT-trUSD $1k**, xác suất có lãi là **8.1%**, ROI trung bình −65% và trung vị −78%; nếu khóa, xác suất có lãi là **16.8%**, ROI trung bình −47% và trung vị −67%; lệnh $10k chỉ còn 3.9% cơ hội có lãi. Với **YT-strUSD $1k**, khi u phân phối chuẩn quanh 10.51% (σ = 1.2 điểm %) cộng thêm 3% xác suất có sự cố làm u rơi vào khoảng −5% đến +5%, xác suất có lãi là **23%** và ROI trung bình −10% (khóa: 31% và −7%). Nếu u xoay quanh 11.18%, xác suất có lãi tăng lên 38% (khóa: **45%**), ROI trung bình −5% (khóa: −2%, với khoảng p10–p90 từ −18% đến +18%).

Hai cách tính khác nhau về dấu của EV, nhưng thống nhất ở hình dạng phân phối. **YT-trUSD là một tấm vé số**: khoảng 80–90% khả năng mất gần hết vốn, bù lại bằng một phần nhỏ khả năng lãi 3–5 lần. **YT-strUSD là một kèo gần như đồng xu**: rủi ro giảm bị chặn ở khoảng −10% đến −25% nếu APY giữ 9–10.5%, nhưng sẽ mất gần hết nếu Tori gặp sự cố.

**FDV hòa vốn, với điều kiện có token (chưa chia cho xác suất 65%)**

| Công cụ | $/1k Cores | Mức pha loãng bull (364 tỷ Cores, 8%, h = 10%) | Mức pha loãng base (654 tỷ, 5%, h = 25%) | Mức pha loãng bear (1,120 tỷ, 3%, h = 40%) |
|---|---|---|---|---|
| YT-trUSD, giá giữa | 0.00782 | $41M | $146M | $543M |
| YT-trUSD $1k | 0.00838 | $44M | **$156M** | $582M |
| YT-trUSD $1k khóa | 0.00559 | $29M | **$104M** | $388M |
| YT-trUSD $10k | 0.01152 | $61M | $215M | $800M |
| YT-strUSD $1k, u = 11.18% | 0.00406 | $21M | $76M | $281M |
| YT-strUSD $1k khóa, u = 11.18% | 0.00270 | $14M | $50M | $188M |
| YT-strUSD $1k, u = 10.51% | 0.00672 | $35M | $125M | $466M |
| YT-strUSD $1k khóa, u = 10.51% | 0.00448 | $24M | $84M | $311M |
| YT-strUSD $1k, u = 9.0% | 0.01278 | $67M | $238M | $887M |
| YT-strUSD $10k, u = 10.51% | 0.00874 | $46M | $163M | $606M |

Đọc bảng này từ góc thị trường: ở mức pha loãng cơ sở, giá giữa của YT-trUSD ngầm định **FDV khoảng $146M nếu chắc chắn có token, hoặc khoảng $225M sau khi điều chỉnh theo xác suất 65% có token**. Với người mua ở lệnh $1k, hai con số này là **$156M và $241M**. Chúng cao gấp 2–3 lần FDV cơ sở $75M. Theo Polymarket, xác suất FDV vượt $200M chỉ khoảng 29%. Ngay cả người khóa YT, tức nhóm đã chiếm 54% YT-trUSD, cũng đang ngầm trả cho FDV khoảng $104–160M.

## Những ẩn số có thể lật ngược kết luận

| Ẩn số | Bằng chứng hiện có | Nếu giả định sai | Tác động lên kết luận |
|---|---|---|---|
| Pre-deposit trả 30 hay 60 Cores/$/ngày | Docs ghi "2x boost, 30 Cores per dollar per day". Tổng leaderboard khớp với 30: pre-deposit khoảng 45–51 tỷ, phần sau launch khoảng 1.7 tỷ/ngày ([Docs](https://docs.tori.finance/resources/pre-deposit)) | Nếu là 60, tốc độ sau launch chỉ 0.9–1.1 tỷ/ngày, mâu thuẫn với riêng vault đã phát khoảng 1.56 tỷ/ngày | **Gần như không đổi**, vì C hiện tại đo trực tiếp. Chỉ đổi cách đọc "Points APY" của RockawayX ($0.0080 so với $0.0040). Có thể tự kiểm tra bằng cách gọi `/api/leaderboard` hai lần cách nhau 24 giờ |
| "points-per-asset" của Pendle có đúng là theo YT, theo ngày | App mô tả "Nx" là Cores/$/ngày và ghi "Cores on your YT balance". Hai ví YT lớn khớp với 49–54 ngày nắm giữ | Nếu tính trên số $ bỏ ra mua YT, YT-trUSD nhận ít hơn khoảng 73 lần | Nếu sai thì **tuyệt đối không mua**. Bằng chứng hiện nghiêng mạnh về cách đọc theo YT, theo ngày |
| Hệ số YT-Lock 45x/9x | Chỉ thấy trong bundle JS của app, không có docs; "Once locked, YT cannot be withdrawn" ([app](https://app.tori.finance/activities)) | Tori hạ hệ số hoặc không ghi nhận phần boost | YT-trUSD khóa: EV từ +15% về −23%. YT-strUSD khóa: từ +6% về −1% |
| Pendle trừ 5% trên Cores | Pendle docs ghi 5% "including points", do đối tác tự trừ; Tori không nói hệ số là trước hay sau phí | Nếu có trừ | EV giảm khoảng 4 điểm % (xem cột cuối bảng ROI) |
| Không có cam kết token | "Not a promise of any token or payment" lặp lại trong nhiều trang docs | P(không token) bằng 20% / 35% / 50% | YT-trUSD $1k: EV −6% / −23% / −41%. Khóa: +42% / +15% / −12%. YT-strUSD khóa (u = 10.51%): +10% / +6% / +1% |
| Xác suất bull | Mới chỉ có một nhịp hồi thị trường tháng 9 | P(bull) bằng 5% / 10% / 20% | YT-trUSD $1k khóa: −45% / −15% / +45%. Toàn bộ phần EV dương phụ thuộc vào đuôi này |
| Đáo hạn Pendle trước TGE | Ước tính P(TGE trước 26/11) khoảng 3% | Mỗi tháng Season 1 kéo dài thêm in khoảng 75–100 tỷ Cores | Đã tính trong các kịch bản. Đây là **nguyên nhân chính** khiến YT đắt |
| TVL tập trung, làn sóng unstake | 10.77M trUSD nằm trong Silo; etrUSD chiếm khoảng 59% supply; 10 ví lớn nhất giữ 34% Cores | Silo bị redeem ra ngoài, vault rút vốn, TVL xuống $55–60M | FDV dịch về kịch bản bear. Tốc độ phát hành Cores cũng giảm và bù lại được một phần. APY strUSD có thể dao động khi phải gỡ vị thế |
| Carry EM-FX và lưu ký | 70.3% nằm ở money markets; ngân hàng lưu ký không nêu tên; pharos chấm C-; `reportLoss()` không có giới hạn ([pharos.watch](https://pharos.watch/stablecoin/trusd-tori/)) | Có sự cố: APY âm, trUSD mất peg | YT-strUSD mất gần toàn bộ, FDV về gần 0. YT-trUSD lỗ tối đa đúng bằng phí mua YT. Người giữ strUSD, trUSD hoặc LP mất cả gốc |
| Thiết kế lại cách phân phối | Tiền lệ Cap: cắt $12M xuống $4.2M, người giữ YT chỉ được bù lỗ | Tori giảm hoặc loại Cores qua Pendle, lọc sybil, chặn khu vực (Mỹ, EU/EEA đã bị hạn chế) | Thêm rủi ro phía giảm mà mô hình chưa định lượng |
| Cấu trúc các season | Docs chỉ nói "future seasons" | Nếu Season 1 kết thúc sớm (31/12/2026) và Season 2 có quỹ riêng | **Tích cực**: pha loãng dừng ở khoảng 350–390 tỷ Cores. Chỉ riêng yếu tố này đã đẩy base lên gần mức pha loãng bull |

Tóm lại, các ẩn số quan trọng nhất là: hệ số khóa, xác suất có token, và ngày kết thúc Season 1. Chuyện pre-deposit trả 30 hay 60 gần như không quan trọng, còn cách đọc "theo YT, theo ngày" đã có bằng chứng on-chain khá mạnh. Một thông báo chính thức về ngày kết thúc Season 1 là sự kiện duy nhất có thể thay đổi mạnh bài toán trong vài tuần tới.

## Khuyến nghị: đứng ngoài YT-trUSD, chỉ vào YT-strUSD với quy mô nhỏ

Với giá ngày 28/09/2026, khuyến nghị đầu tiên là **không mua YT-trUSD**: không khóa thì EV âm trong mọi cách tính, còn khóa thì EV chỉ dương nhờ một kịch bản bull 15% và xác suất có lãi theo mô phỏng dưới 17%. **YT-strUSD là lựa chọn duy nhất gần giá hợp lý**, nhưng chỉ cho vị thế đầu cơ nhỏ, không quá 0.5–1% danh mục, chia lệnh $1k–5k và đặt limit order (cả hai thị trường đều hỗ trợ). Nên khóa (9x) nếu chấp nhận được việc không rút ra được: yield vẫn claim được và YT về 0 lúc đáo hạn, nên khóa chỉ mất quyền bán sớm, đổi lại thêm rủi ro hợp đồng lYT vốn có thể nâng cấp qua timelock của Tori. Điều kiện tiên quyết là bạn sẵn sàng giữ strUSD, vì bản chất vị thế này là cược APY strUSD giữ ≥ khoảng 10.5% trong 58 ngày với đòn bẩy khoảng 56 lần.

Vốn lớn ($50k trở lên) không nên đi qua YT vì trượt giá 30–58%. Nếu đã tin tín dụng của Tori, giữ strUSD hoặc LP strUSD cho Cores gần như miễn phí, còn Ecosystem Vault cho Cores với giá khoảng $0.0038/1k; đổi lại, toàn bộ vốn gốc chịu rủi ro. Người tin YT đang bị định giá quá cao có thể đứng ở phía đối diện: PT-strUSD khóa lợi suất cố định 11.42%, cao hơn APY thực nhận khoảng 10.5%, tức là "bán Cores" cho người mua YT, nhưng vẫn chịu toàn bộ rủi ro gốc.

Vùng giá hợp lý tính theo **implied APY hiệu dụng**, tức đã gồm phí và trượt giá. Báo cáo đã kiểm tra các ngưỡng này với T = 58.5, 45 và 30 ngày, và chúng gần như không đổi theo thời gian:

| Công cụ | Implied hiện tại (28/09) | Hòa vốn theo EV kịch bản ($0.0064/1k) | Hòa vốn theo kịch bản cơ sở ($0.0040/1k) | Hòa vốn theo Monte Carlo ($0.0030/1k) | Hành động |
|---|---|---|---|---|---|
| YT-trUSD 30x | 9.01% giữa / 9.69% ở lệnh $1k | ≤ 7.3% | ≤ 4.5% | ≤ 3.35% | Không mua |
| YT-trUSD khóa 45x | như trên | ≤ 11.2% | **≤ 6.8%** | ≤ 5.1% | Chỉ mua khi ≤ khoảng 6.8% |
| YT-strUSD 6x (kỳ vọng u = 10.51%) | 11.42% giữa / 11.78% ở lệnh $1k | ≤ 11.7% | ≤ 11.1% | ≤ 10.9% | Chờ |
| YT-strUSD khóa 9x (kỳ vọng u = 10.51%) | như trên | ≤ 12.5% | **≤ 11.6%** | ≤ 11.2% | Sát vùng mua; vào nhỏ bằng limit |
| YT-strUSD khóa 9x (kỳ vọng u = 11.18%) | như trên | ≤ 13.2% | ≤ 12.3% | ≤ 11.9% | Trong vùng mua, nếu tin APY ≥ 11.2% |

Các ngưỡng không đổi theo thời gian vì cả giá YT lẫn lượng Cores còn lại đều giảm cùng tỷ lệ theo số ngày tới đáo hạn. Hệ quả thực tế là **chờ đợi không làm bạn trả đắt hơn cho mỗi Core**. Chờ chỉ làm giảm tổng số Cores tối đa bạn có thể gom. Đổi lại, bạn có thêm thông tin: ngày kết thúc Season 1, dòng tiền từ Silo, xu hướng APY.

Tín hiệu quan trọng nhất cần theo dõi là **thông báo chính thức** về ngày kết thúc Season 1, snapshot, tokenomics hoặc niêm yết qua Binance Wallet/Alpha/HODLer. Nếu Season 1 kết thúc trước hoặc ngay sau 26/11/2026, mức pha loãng sẽ về gần kịch bản bull và YT-trUSD khóa trở nên hấp dẫn, nhưng giá YT cũng sẽ tăng ngay lập tức. Sau đó là mốc 31/12/2026 trên Polymarket (tăng rõ rệt lên trên 60% kèm khối lượng thật là tín hiệu đáng kể), số phận của **10.77M trUSD trong Silo** trong tuần 29/09–05/10/2026 (được stake lại hay bị redeem ra ngoài), và TVL trên DefiLlama (trên $100M là tốt, dưới $60M là xấu). Với YT-strUSD, APY 7 ngày trên app Tori là biến số quyết định: dưới 10% thì vị thế lỗ ở mọi kịch bản trừ bull. Cuối cùng, nên theo dõi tốc độ tăng `totalPoints` trên leaderboard (trên 3 tỷ/ngày thì cần tính lại), việc Pendle niêm yết kỳ đáo hạn mới năm 2027 (dấu hiệu Season 1 kéo dài), tin tức FX thị trường mới nổi (đặc biệt là đồng lira Thổ Nhĩ Kỳ) và mọi sự kiện `reportLoss`.

### Checklist rủi ro

| Rủi ro | Theo dõi ở đâu | Ngưỡng cảnh báo / hành động |
|---|---|---|
| Không có token, hoặc Tori đổi luật Cores | [Docs: Cores](https://docs.tori.finance/resources/cores), X @tori_finance | Câu chữ trong docs thay đổi; Season 2 được công bố mà không nói Season 1 kết thúc |
| TGE trễ, Cores bị pha loãng | [/api/leaderboard](https://app.tori.finance/api/leaderboard) | Phát hành trên 3 tỷ/ngày; Season 1 kéo dài quá 31/03/2027 |
| APY strUSD giảm (lỗ cho YT-strUSD) | [/api/apy](https://app.tori.finance/api/apy), underlying APY trên Pendle | APY 7 ngày dưới 10% thì không mua thêm |
| Rút vốn tập trung, TVL giảm | [Silo](https://etherscan.io/address/0xF7c0d8853E69DCD37ee7599c6280d2632F3360B4), [DefiLlama](https://api.llama.fi/protocol/tori-finance) | Silo bị redeem ra ngoài; TVL dưới $60M |
| Sự cố lưu ký hoặc FX thị trường mới nổi | [Solvency feed](https://app.tori.finance/api/solvency), [pharos.watch](https://pharos.watch/stablecoin/trusd-tori/) | Tỷ lệ bảo chứng dưới 100%; có `reportLoss`; lệch peg trên 0.5% |
| Hợp đồng YT-Lock (có thể nâng cấp, không rút được) | [Docs: Roles](https://docs.tori.finance/security/roles) | Có đề xuất nâng cấp bất thường trong timelock 24 giờ |
| Thanh khoản YT mỏng | [Pendle API](https://api-v2.pendle.finance/core/v1/markets/all) | Lệnh trên $2k (YT-trUSD) hoặc trên $10k (YT-strUSD) thì dùng limit order |
| Phân phối bị thiết kế lại | Thông báo của Tori; tiền lệ Cap | Tori loại hoặc giảm Cores từ Pendle |
| Pháp lý / khu vực | [Docs: Market Landscape](https://docs.tori.finance/resources/comparison) | Cư trú tại Mỹ hoặc EU/EEA thì không đủ điều kiện |
| Mạo danh, phishing | [t.me/tori_finance](https://t.me/s/tori_finance) là tài khoản chiếm tên, không phải của Tori; ticker TORI trùng với Teritori | Chỉ dùng link lấy từ tori.finance |

## Kết luận

Chỗ định giá sai trên Pendle không nằm ở tổng giá trị Cores. Giá YT-trUSD định giá toàn bộ Cores của Season 1 tại ngày đáo hạn ở mức khoảng $2.2–2.3M, không xa quỹ $2.8M thực nhận trong kịch bản cơ sở. Chỗ sai nằm ở **khoảng thời gian giữa ngày 26/11/2026 và snapshot thật sự**. Trong khoảng đó, số Cores lưu hành có thể tăng từ 1.2 lần đến gần 4 lần, trong khi YT đã ngừng tích điểm. Người mua YT hôm nay thực chất đang mua một quyền chọn trên một sự kiện (công bố TGE) mà ngày hết hạn của nó (26/11) rơi trước chính sự kiện đó, nhưng lại trả giá như thể sự kiện đã cận kề. Vì các ngưỡng mua tính theo implied APY không phụ thuộc thời gian, **chiến lược tốt nhất là chờ**. Hoặc thị trường hạ implied APY xuống vùng 6.8% (YT-trUSD khóa) hay khoảng 11% (YT-strUSD), hoặc Tori công bố ngày kết thúc Season 1 và xóa đi ẩn số lớn nhất trong mô hình.

Rộng hơn, Tori cho thấy chu kỳ "points → Pendle → TGE" năm 2026 đã khác hẳn năm 2024. Sản phẩm có thể tốt hơn, với lợi suất thật gấp đôi sUSDe, nhưng hệ số định giá đã nén về khoảng 1x TVL. Vốn đi farm nhỏ hơn 10 lần, và rủi ro đuôi (Neutrl, Resolv, Cap) đã được thị trường trả giá bằng tiền thật. Trong môi trường đó, YT không còn là cách rẻ nhất để có airdrop. Nó là cách đắt nhất để mua một kịch bản bull. Còn người đã chấp nhận rủi ro tín dụng của Tori thì nhận Cores "miễn phí" ngay khi giữ strUSD.
