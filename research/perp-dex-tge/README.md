# Perp DEX TGE research (snapshot 2026-11-18)

Báo cáo chính: [`reports/Phân tích perp DEX - pattern TGE và định giá.md`](../../reports/Phân%20tích%20perp%20DEX%20-%20pattern%20TGE%20và%20định%20giá.md)

## Files

- `tools/polymarket_fdv_ladder.py`: kéo ladder "FDV above ___ one day after launch" của một event Polymarket,
  dựng lại median FDV ngụ ý theo thời gian. Chỉ dùng API công khai và thư viện chuẩn Python.
- `data/polymarket_calibration.csv`: median Polymarket ở các mốc T-90/T-30/T-7/T-2 so với FDV D1 thực tế
  (Lighter, edgeX, Backpack, GRVT, Paradex, cộng Monad và MegaETH để đối chiếu).
- `data/post_tge_paths.csv`: giá D1/D7/D30/D90/D180, đáy và đỉnh (theo ngày sau TGE) của LIT, EDGE, BP, DIME, GRVT.

## Chạy

```bash
python3 research/perp-dex-tge/tools/polymarket_fdv_ladder.py variational-fdv-above-one-day-after-launch 14 0.97
```

```bash
python3 research/perp-dex-tge/tools/polymarket_fdv_ladder.py extended-fdv-above-one-day-after-launch 14 0.9
```

Tham số thứ 3 (tùy chọn) là xác suất token launch trước hạn của kèo; khi có, script in thêm median có điều kiện.

Hiệu chỉnh lịch sử (5 perp DEX, 2025–2026): median ở T-30 cao hơn FDV D1 thực tế ở 4/5 trường hợp
(sai số trung vị khoảng −42%); ở T-2 vẫn cao hơn ở 4/5 trường hợp (khoảng −30%).

Không phải lời khuyên đầu tư.
