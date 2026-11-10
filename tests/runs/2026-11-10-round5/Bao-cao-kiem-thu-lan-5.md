# Báo cáo kiểm thử vòng 5 — Vietnam Legal Advisor 0.70.1

Ngày 2026-11-10. Gói ứng viên: `Vietnam-Legal-Advisor-0.70.1.zip`, SHA-256 `2d6bdad8971510252f12403b53cda784eef92a7103460c9dc6871943b66fc9b3` (lưu trong thư mục này).

## Kết quả
- Hành vi: 22/22 PASS sơ bộ (AI chấm). Tổng điểm 23–24 trên 24; không có lỗi critical hay major. 8 ca có lỗi nhỏ (xem `results.json`).
- Kiểm tra tĩnh: `scripts/validate.py` PASS.
- `tests/run_integrity.py`: **FAIL, 2 lỗi** (người chấm cùng hãng với bên chạy; không chạy trên host thật), giống vòng 4.

## Cách chạy
1. Thử trước trên Codex thật ở máy Nhà phát hành: Codex CLI 0.163.0, mô hình `gpt-5.6-terra`, sandbox chỉ đọc, mạng bị chặn, plugin 0.70.1 cài qua marketplace cục bộ, các plugin và connector khác tắt. Chỉ ca R01 chạy xong (trả lời đạt yêu cầu); sau đó tài khoản hết hạn mức Codex. Transcript R01 chỉ lưu cục bộ.
2. Theo quyết định của Nhà phát hành, chạy lại cả 22 ca bằng 22 phiên con Claude Code độc lập, mỗi ca một phiên, loại agent chỉ có công cụ Read và Edit (không web, không shell). Mã mô hình trong transcript: `claude-sonnet-5-5`. Plugin là nội dung giải nén từ ZIP ứng viên. Các ca R02, C01, D01, V01, V02 được đọc `tests/fixtures.md`. Phiên con không được cấp `must_include`/`must_not`. Mọi phiên chỉ gọi Read (5–9 lần) trên file của plugin và fixtures.
3. Chấm điểm: Claude Opus 5.5, theo `tests/EVALUATION.md` (sáu tiêu chí, 0–4).

## Lỗi nhỏ ghi nhận
- Không đọc SKILL.md của một skill trong tuyến dự kiến: R01 (legal-source-verification, legal-validity-verification), R03 (vietnam-legal-research), M01 (legal-due-diligence), A01 (legal-reasoning).
- MODE tự khai OFFLINE dù đã đọc fixtures: D01, V02.
- Câu thừa về "status line" do prompt hệ thống của loại agent: R01, V01, F01.
- L01: đối chiếu từng yếu tố chỉ ở mức phương pháp.
- V01: thứ tự ROUTE tự khai khác thứ tự đọc thực tế.

## Hạn chế (ghi theo thực tế)
1. Người chạy và người chấm cùng hãng (Claude); không có người chấm khác hãng, không có luật sư. (Lỗi integrity.)
2. Không chạy trên host sản phẩm thật. (Lỗi integrity.)
3. Người điều phối đồng thời là người chấm và đã thấy `cases.json` trước khi chạy.
4. Không có ca live với văn bản chính thức và đáp án do luật sư soạn; mọi ca là `controlled-fixture`.
