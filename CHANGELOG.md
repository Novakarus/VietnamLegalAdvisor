# Lịch sử thay đổi

## 0.70.0 — ứng viên (CANDIDATE), chưa công khai — 04/11/2026

Đánh số lại từ 0.69.3 (đóng băng). Cập nhật giấy phép (Apache-2.0 cho mã, CC BY 4.0 cho tài liệu và nội dung plugin; logo, bằng chứng kiểm thử và đầu ra AI cũng CC BY 4.0 trong phạm vi Nhà phát hành có quyền), hồ sơ nguồn gốc nội dung AI và logo, lưu trữ điều khoản bên thứ ba. Kiểm thử Protocol v2 vòng 4: 22 phiên Claude cô lập, 22/22 PASS sơ bộ do AI chấm; `tests/run_integrity.py` còn 2 lỗi (người chấm cùng hãng, chưa chạy trên host thật), nên chưa nghiệm thu chính thức. Thêm `scripts/import_host_run.py` và `tests/HOST_RUNBOOK.md` cho vòng chạy trên host thật. `validate.py` bỏ qua phép so ZIP khi không có `dist/` (CI) và ghi cảnh báo. Website chỉ còn nguồn `docs/` (GitHub Pages phục vụ từ /docs); bỏ bản sao ở thư mục gốc, `sync_site.py` và workflow `release.yml`. Gỡ bản 0.69.3 (gói, trang phát hành, báo cáo) khỏi repo; giữ hồ sơ kiểm thử vòng 1–3.

## 0.69.3 — cập nhật plugin 22/10/2026

Làm rõ Q01: xác minh nguồn sai, nếu được chứng minh, là lỗi critical; tách lỗi đã xác nhận khỏi tuyên bố chưa có bằng chứng. Không suy từ công cụ tìm kiếm không khả dụng sang kết luận đã có xác minh giả.

## 0.69.2

Bổ sung so sánh cấu trúc có điều kiện khi thiếu dữ kiện; quy trình xác minh ngay trong câu trả lời offline; bản đồ giả thuyết và chứng cứ cho phản biện; kiểm tra thực chất bước phản biện và chất lượng đầu ra.

## Công bố nguồn và website — 22/10/2026

Công khai nguồn, tài liệu và kiểm thử tóm tắt. Giấy phép và website được công bố riêng; gói plugin 0.69.3 đã kiểm thử giữ nguyên, không thêm giấy phép vào ZIP lịch sử. Nguồn plugin/LICENSE.md là tài liệu mới bên cạnh 20 tệp gốc, không thay đổi chỉ dẫn kỹ năng.

## Chi tiết từng lần sửa

Bản ghi chi tiết (chỉ là lịch sử, không phải trạng thái hiện hành; trạng thái nằm trong `STATUS.md`): [0.69.2](history/CHANGES-0.69.2.md) · [0.69.3](history/CHANGES-0.69.3.md) · [0.70.0](history/CHANGES-0.70.0.md).
