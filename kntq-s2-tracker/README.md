# KNTQ Season-2 claim tracker

Theo dõi tiến độ claim của đợt phân phối kPoints cuối (Season 2) của Kinetiq: user có điểm được **mua**
KNTQ ở giá cố định **0.261331 USDC**, pool **50,000,000 KNTQ**, cửa sổ **2026-10-01 12:00 UTC → 2026-10-11 12:00 UTC**,
không lockup. Tất cả số liệu đọc trực tiếp on-chain (read-only), không ký giao dịch, không cần API key.

## Hợp đồng và địa chỉ (đã verify on-chain)

| Thành phần | Địa chỉ / giá trị |
|---|---|
| Claim contract (proxy `CKNTQ`) | `0x435bb7ea4eb481cb686606d089ea4dee4c6cc03b` |
| Implementation (verified source) | `0xedfd49704f6f0abafac376f35270c4c7585d40e9` |
| KNTQ ERC-20 (HyperEVM, 18dp) | `0x000000000000780555bd0bca3791f89f9542c2d6` |
| USDC thanh toán (HyperEVM, 6dp) | `0xb88339cb7199b77e23db6e890353e22632ba630f` |
| Pool tham chiếu KNTQ/USDC (Project X) | `0x99cb209d412cbf9f525b6002d2c975b52bd2bd08` |
| Block tạo proxy | 47,315,563 (2026-09-30 19:27 UTC) |
| `start()` / `end()` | 1790856000 / 1791720000 (2026-10-01 12:00 → 2026-10-11 12:00 UTC) |
| `quote(1e18)` | 0.261331 USDC / KNTQ |
| Spot pair HyperCore | `@334` (KNTQ/USDC), token index 124 |
| Event `Claimed(address,uint256,uint256)` | topic0 `0x987d620f307ff6b94d58743cb7a7509f24071586a77759b77c2d4e29f75a2f9a` |

Pool được nạp đúng 50,000,000 KNTQ trong 2 giao dịch từ `0x5bd9e766c0151dcfbc4246e5f8b3193c4beeaae4`
(100 KNTQ test ở block 47,339,847 + 49,999,900 KNTQ ở block 47,374,388). Contract **không** lưu tổng
đã claim, chỉ có mapping `claimed(address)` — nên phải cộng từ event `Claimed`.

## Files

- `tracker.py` — snapshot tăng dần (incremental): quét `eth_getLogs` từ block đã lưu trong `state.json`,
  cộng ví/claim/KNTQ/USDC, đọc `balanceOf` của contract, lấy giá spot HyperCore + giá pool HyperEVM,
  kiểm tra số dư 5 ví allocation (xem dưới), in JSON và ghi thêm một dòng vào `snapshots.csv`
  (kèm delta so với lần chạy trước).
- `series.py` — dựng lại toàn bộ đường cong claim theo giờ từ đầu (ghi `claim_series.json`).
- `state.json` — checkpoint (block cuối + bảng ví → [KNTQ, USDC, số lần claim]).
- `snapshots.csv` — chuỗi snapshot mỗi 2h; dòng đầu (12:16 UTC) được backfill từ `claim_series.json`
  (giá lấy từ Hyperliquid info API lúc 12:07 UTC), các dòng sau là số đo trực tiếp.
- `claim_series.json` — số claim / ví mới / KNTQ theo từng giờ UTC.

## Chạy

```bash
python3 tracker.py                 # snapshot incremental (mặc định ~2 phút, 1 lần mỗi 2h)
python3 tracker.py --reset         # quét lại từ block deploy
python3 tracker.py --eligible N    # có N ví eligible thì tính luôn % ví đã claim
python3 series.py [block_range]    # dựng lại đường cong theo giờ (mặc định 10,000 block/lần gọi)
```

RPC công khai dùng theo thứ tự fail-over: `hyperliquid-rpc.publicnode.com`, `rpc.hypurrscan.io`,
`rpc.hyperliquid.xyz/evm` (cap 1,000 block/`eth_getLogs`), `rpc.purroofgroup.com` (nhận 10,000 block).
Giá: `POST https://api.hyperliquid.xyz/info` (`allMids` → `@334`) và `slot0()` của pool trên HyperEVM.
`hyperevmscan.io` bị Cloudflare 403 từ sandbox này, nên không dùng explorer.

## Đọc số gì

- `pct_of_pool_claimed` — % của 50M đã được mua. Đây là thước đo áp lực bán tiềm năng đã được
  "kích hoạt": token claim ra là tự do bán ngay (không lock).
- `kntq_left_in_contract` — phần còn treo; nếu giá còn trên 0.2613 thì đây là nguồn cung chưa bán,
  và sẽ dồn về sát deadline.
- `premium_vs_claim_pct` — biên arbitrage. Trên ~0% là claim-rồi-bán có lời; về 0 nghĩa là quyền mua
  hết giá trị và lực bán cơ học biến mất.
- `new_wallets` / `claim_pace_kntq_per_h` / `projected_pct_at_deadline` — tốc độ claim trong 2h gần nhất
  và suy chiếu tuyến tính tới deadline.
- `alloc_*` / `alloc_moved` — số dư 5 ví allocation. Cột `alloc_moved` trống là bình thường; có chữ
  nghĩa là insider đã chuyển token, tín hiệu bearish mạnh nhất có thể đo được.

## Canh 5 ví allocation (không có vesting contract)

Deployer `0x51172933b60847085e2a959e860e2ec9e240ac09` chia 730M KNTQ vào đúng 5 địa chỉ trong 1 phút
lúc TGE (2025-11-27 12:07 UTC). Cả 5 đều là **EOA, không có code** — nghĩa là **không có vesting
contract hay timelock on-chain**, lịch unlock (cliff ~2026-11-27 + 24 tháng) chỉ là cam kết trong docs.

| Ví | Phân bổ | Số dư (2026-10-04 00:05 UTC) |
|---|---|---|
| `0x373e0b6b57818ac2bb3a3e55e31128d5f880d90e` | core contributors 23.5% | 235,000,000 (nguyên) |
| `0x9ef3b3a49ee9a2fd28a10f6e9407219e7ceca1a2` | investors 7.5% | 75,000,000 (nguyên) |
| `0xf50ad63714f10f4e96eeabd43d549c8232992b36` | foundation 10% | 100,000,000 (nguyên) |
| `0x5bd9e766c0151dcfbc4246e5f8b3193c4beeaae4` | growth 30% | 250,000,000 (đã chuyển 50M sang claim contract) |
| `0x4664b0453c7c483e2e262ca54351ade71b6be734` | liquidity 2% | 4,523,810 (đã deploy 15.48M) |

Tổng 660M = 66% supply nằm ở 5 EOA này. Mọi lệnh chuyển ra từ ví team/investor sẽ đi trước lệnh nạp
sàn vài phút đến vài giờ, nên đây là tín hiệu sớm đáng giá nhất.

Không phải lời khuyên đầu tư.
