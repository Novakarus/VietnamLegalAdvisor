> **LỊCH SỬ — không phải trạng thái hiện hành.** Ghi lại thời điểm chỉnh sửa. Trạng thái hiện hành nằm trong `STATUS.md`.

# Candidate 0.70.0 — thông báo giấy phép trong gói, chưa kiểm thử

Lưu 2026-11-04. Thay đổi so với 0.69.3 (đã đóng băng, giữ nguyên trong `releases/0.69.3/` và `dist/`):

- Nâng phiên bản ở hai manifest lên 0.70.0.
- Thêm `plugin/LICENSE.md` (CC BY 4.0, loại trừ biểu trưng, tên dự án và nội dung bên thứ ba). Có hiệu lực từ 2026-11-04.
- `scripts/package.py` cho phép file `LICENSE.md` ở gốc gói.
- Không đổi nội dung kỹ năng, hướng dẫn hay biểu trưng.

Lưu ý (ghi lúc tạo bản): `tests/results.json` khi đó ghi 0.70.0 là NOT_RUN; kết quả vòng 4 chạy sau đó, xem `STATUS.md`; hồ sơ vòng 3 của 0.69.3 ở `tests/history/0.69.3/round3-results.json`. Theo quy tắc phiên bản trong `STATUS.md`, cần kiểm thử lại theo Protocol v2 trước khi coi là ứng viên đã kiểm thử.
