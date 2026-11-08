# Thông báo bên thứ ba

Cập nhật 2026-11-04; Nhà phát hành đã duyệt. Chưa phải xác nhận pháp lý.

## Thành phần phụ thuộc

| Thành phần | Dùng ở đâu | Có được phân phối cùng plugin không | Giấy phép |
|---|---|---|---|
| Pillow (`scripts/requirements.txt`: `Pillow>=11.0.0,<13`) | `scripts/validate.py` (kiểm tra ảnh PNG) | Không. Chỉ là phụ thuộc phát triển, không nằm trong `plugin/` | Giấy phép riêng của Pillow (kiểu HPND/MIT-CMU). Xem gói Pillow tại thời điểm cài đặt |

## Kết quả sàng lọc `plugin/`

Tìm kiếm các từ khóa bản quyền, giấy phép, "third-party", "©" trong `plugin/` chỉ trả về một cụm từ pháp lý thông thường trong `investment-and-ma/SKILL.md` ("third-party consents") và file ảnh biểu trưng. Không tìm thấy mã hay văn bản có thông báo giấy phép khác. Đây là sàng lọc từ khóa, không phải rà soát nội dung.

## Những điều chưa xác nhận (Nhà phát hành cần trả lời)

1. **Biểu trưng** `vietnam-legal-advisor-icon-v4.png`: chi tiết nguồn gốc, lời nhắc, tài khoản cá nhân tại Việt Nam, điều khoản OpenAI ngày 2026-10-16 (bản lưu Wayback kèm hash) nằm trong [PROVENANCE-LOGO.md](PROVENANCE-LOGO.md). Do GPT-6 Astra tạo qua ChatGPT của OpenAI. Chưa cấp phép.
2. **Nội dung có hỗ trợ AI**: plugin được đóng gói cho nền tảng có manifest `com.openai`, và các lượt kiểm thử dùng subagent Codex. Cần xác nhận điều khoản của nhà cung cấp mô hình về quyền đối với đầu ra khi cấp phép lại.
3. **Văn bản pháp luật Việt Nam**: plugin không đóng gói văn bản pháp luật (`knowledge-index.json` rỗng). Nếu sau này đóng gói, cần kiểm chứng quy định hiện hành về quyền tác giả đối với văn bản quy phạm pháp luật trước khi tuyên bố trạng thái.
4. **Bằng chứng kiểm thử** (`tests/runs/`): chứa đầu ra mô hình và gói zip; chưa cấp phép.

## Rà soát mã (2026-11-04)

Đã đọc toàn bộ `scripts/validate.py` (189 dòng), `scripts/package.py` (49), `tests/run_technical.py` (52) và `tests/validate.py` (6), do ChatGPT/Codex soạn theo Nhà phát hành. Kết quả:

- Chỉ dùng thư viện chuẩn của Python và Pillow (qua API công khai). Logic gắn chặt với cấu trúc dự án (13 kỹ năng, 22 ca kiểm thử, manifest, SHA-256 của gói).
- Có hai thủ thuật phổ biến, đều là cách viết thông dụng: mở ảnh bằng Pillow rồi `verify()` và tải lại để kiểm tra PNG; đóng gói ZIP với mốc thời gian cố định (1980-01-01) và quyền file cố định để ZIP tái lập được.
- Không thấy tiêu đề bản quyền, ghi chú giấy phép, tên tác giả khác hay đoạn mã trông như sao chép nguyên khối.

Giới hạn: đây là đọc thủ công, không có công cụ so khớp mã nguồn mở. Không chứng minh được không có sự trùng hợp; chỉ cho thấy không có dấu hiệu rõ ràng. Mã do Claude viết (`scripts/check_consistency.py`, `tests/run_integrity.py`) không nằm trong rà soát này và được khai báo ở `PROVENANCE-AI-CONTENT.md`.

## Văn bản giấy phép chép nguyên văn

- `LICENSE-Apache-2.0.txt`: bản của gói `common-licenses` (Debian), SHA-256 `cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30`.
- `LICENSE-CC-BY-4.0.txt`: bản từ kho `spdx/license-list-data`, SHA-256 `d557539df68e771cc1eedcc91d13f70fca930e508d11eedcafa4b15db49e3744`.
