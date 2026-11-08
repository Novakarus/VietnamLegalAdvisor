# Báo cáo kiểm thử vòng 4 — Vietnam Legal Advisor 0.70.0

Thực hiện và chấm điểm bởi **Claude** (Anthropic; mã mô hình cấu hình `claude-sonnet-5-5`, mô hình thực tế phục vụ có thể khác), ngày 2026-11-04. Gói ứng viên: `Vietnam-Legal-Advisor-0.70.0.zip`, SHA-256 `ebbd7e606fe3d4c0de6a74194ede4f4726b3e6d5607aed39fed37c001eedb839`.

## Kết quả
- Hành vi: 22/22 PASS sơ bộ (AI chấm; điểm 3–4 trên sáu tiêu chí; tổng từ 20 đến 24). Vòng 3 do Codex thực hiện, giữ ở `tests/history/0.69.3/round3-results.json` và `tests/runs/2026-10-21-round3/`.
- Kỹ thuật: kiểm tra tĩnh PASS, nhất quán khớp, hồi quy kỹ thuật 14/14.
- `run_integrity.py`: **FAIL, 2 lỗi** (từ 25 lỗi ở lần chạy đầu). Vòng này không dùng để nghiệm thu chính thức.

## Cách chạy (lần chạy lại)
22 phiên con Claude Code cô lập, mỗi ca một phiên, chỉ có công cụ Read và Edit (không web, shell); mọi phiên chỉ gọi Read (5–9 lần) trên file trong `plugin/` và `tests/fixtures.md` (R02, C01, D01, V01, V02). Mã mô hình do host báo: `claude-sonnet-5-5`. Transcript nguyên bản và SHA-256 theo từng ca nằm trong `evidence/<ID>/transcript.jsonl` và `run_manifest.json`. Phiên con không được cấp `must_include`/`must_not`.

## Hạn chế còn lại (ghi theo thực tế)
1. Người chạy và người chấm cùng họ mô hình (Claude); không có người chấm khác hãng, không có luật sư. (Lỗi integrity.)
2. Không chạy trên host sản phẩm thật; plugin được đọc từ file. (Lỗi integrity.)
3. Phiên con dùng prompt hệ thống của loại agent cấu hình status line, khác prompt host thật; người điều phối đã từng thấy `cases.json`.
4. Không có ca live với văn bản chính thức và đáp án do luật sư soạn; mọi ca là `controlled-fixture`.
5. Có 8 ca ghi lỗi nhỏ (xem `results.json`), ví dụ D01 ghi MODE OFFLINE dù đọc fixtures.
