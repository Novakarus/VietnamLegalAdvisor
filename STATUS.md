# Trạng thái dự án — nguồn duy nhất

Đây là nơi duy nhất ghi trạng thái hiện hành. Các file `CHANGES-*.md`, `releases/*/RELEASE.md`, `tests/runs/*` là hồ sơ lịch sử tại thời điểm tạo; nếu mâu thuẫn với file này thì file này đúng. `scripts/check_consistency.py` kiểm tra các số liệu dưới đây khớp với manifest, `release.json` và `tests/results.json`.

Phiên bản hiện hành: 0.70.0
Trạng thái: CANDIDATE
Sẵn sàng phát hành công khai: không
Cập nhật: 2026-11-04

## Các trạng thái và điều kiện chuyển

| Trạng thái | Ý nghĩa | Điều kiện để vào |
|---|---|---|
| DRAFT | Đang sửa, chưa kiểm thử hành vi | Có thay đổi trong `plugin/` |
| CANDIDATE | Đã đóng gói, chạy kiểm thử hành vi vòng mới | Tăng phiên bản, `validate.py` đạt, đóng gói ZIP và ghi SHA-256 |
| FROZEN_LOCAL_RELEASE_CANDIDATE | ZIP đã kiểm thử được giữ nguyên byte | Đã có bản ghi kết quả và `release.json` |
| ACCEPTED | Đủ điều kiện nghiệm thu, chưa công bố | Toàn bộ "cổng nghiệm thu" bên dưới |
| RELEASED | Đã công bố công khai | ACCEPTED + Nhà phát hành duyệt Điều khoản và giấy phép |

Chỉ chuyển trạng thái bằng cách sửa file này cùng `release.json`. Không nâng trạng thái dựa trên chấm điểm AI sơ bộ.

## Quy tắc phiên bản

1. Mọi thay đổi trong `plugin/` (kể cả chỉ sửa chỉ dẫn) tạo phiên bản mới và phải kiểm thử lại các ca bị ảnh hưởng cộng một ca đối chứng. Không mang PASS từ phiên bản trước sang.
2. Thay đổi ngoài `plugin/` (tài liệu, script, giấy phép, website) không tăng phiên bản plugin và không làm đổi SHA-256 của gói đã đóng băng. Ghi vào lịch sử Git, không ghi vào `CHANGES-*.md`.
3. `CHANGES-<phiên bản>.md` chỉ viết một lần tại thời điểm sửa và không sửa lại; thêm mục "Kết quả kiểm thử" ở bản ghi lịch sử khác nếu cần.
4. Không đóng gói lại ZIP của phiên bản đã đóng băng. Muốn thay đổi gói, tạo phiên bản mới.

## Trạng thái bản 0.70.0

- Ứng viên (2026-11-04): Nhà phát hành đánh số lại từ 0.69.4 qua 0.7.1 thành 0.70.0 (0.70.0 lớn hơn 0.69.3 theo semver). Thêm `plugin/LICENSE.md` (thông báo giấy phép CC BY 4.0, có hiệu lực từ 2026-11-04). Không đổi nội dung kỹ năng. Xem `history/history/CHANGES-0.70.0.md`. Thứ tự thực tế: 0.69.3 (đóng băng) → 0.70.0 (hiện hành); không còn bản nào mang số 0.69.4 hoặc 0.7.1.
- Đã đóng gói: `dist/Vietnam-Legal-Advisor-0.70.0.zip` (SHA-256 trong file `.sha256` cạnh nó). Kiểm tra tĩnh đạt.
- Kiểm thử hành vi: **chưa chạy** (22 ca NOT_RUN).
- Nghiệm thu chính thức: chưa.

## Bản 0.69.3 (đã gỡ khỏi repo, 2026-11-08)

- Nhà phát hành quyết định gỡ gói, trang phát hành và báo cáo của 0.69.3 khỏi repo; chỉ giữ hồ sơ kiểm thử vòng 1–3 (do Codex thực hiện) làm lịch sử. ZIP đã đóng băng có SHA-256 `40120521e43173191ab4babbc93180445fef33fb819f9d24ed2c25fb31dd7fa6`.
- Kiểm thử hành vi vòng 3: 22/22 PASS do AI chấm sơ bộ; kiểm tra tĩnh 109/109 (trước nhập hồ sơ) và 131/131 (sau nhập hồ sơ); hồi quy kỹ thuật 14/14. Hồ sơ ở `tests/history/0.69.3/round3-results.json` và `tests/runs/2026-10-21-round3/`.

## Khoảng cách so với Protocol v2

Vòng 4 (Claude, 2026-11-04) chạy lại bằng 22 phiên con Claude Code cô lập (một phiên mỗi ca; chỉ công cụ Read/Edit, không web/shell nên OFFLINE được chặn về kỹ thuật; mã mô hình `claude-sonnet-5-5` do host báo; transcript nguyên bản và SHA-256 theo từng ca; người chạy không được cấp `must_include`/`must_not`). Kết quả: 22/22 PASS sơ bộ; `run_integrity.py` còn FAIL 2 lỗi: (1) người chấm là Claude, cùng họ mô hình với bên chạy; (2) chưa chạy trên host sản phẩm thật với plugin đã cài. Ngoài ra vẫn thiếu luật sư rà soát và ca live có đáp án. Hạn chế: phiên con dùng prompt hệ thống của loại agent cấu hình status line; người điều phối đã từng thấy `cases.json`.

Vòng 3 (Codex):

Kết quả chạy `python tests/run_integrity.py tests/runs/2026-10-21-round3` ngày 2026-11-03: **FAIL**. Vòng 3 không đạt vì không có `run_manifest.json`, không có mã mô hình chính xác, người chấm cùng họ mô hình với bên chạy (cả hai thuộc hệ Codex/OpenAI), chặn OFFLINE chỉ bằng chỉ dẫn, không chạy trên host thật, và không có transcript nguyên bản. ZIP ứng viên khớp SHA-256. Vòng 4 phải đạt Protocol v2 (xem `tests/EVALUATION.md`).


