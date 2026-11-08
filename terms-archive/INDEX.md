# Kho điều khoản liên quan

Thư mục này lưu bản sao các điều khoản của bên thứ ba liên quan đến nguồn gốc và quyền đối với nội dung dự án. Các file PDF thuộc bản quyền của chủ sở hữu điều khoản; chúng chỉ được giữ **cục bộ** làm bằng chứng và bị loại khỏi Git bằng `.gitignore` (chỉ `INDEX.md` được đưa lên Git). Cập nhật 2026-11-04. Lưu ý: tên file `openai-terms-2026-01-01.pdf` là Terms of Use (hiệu lực 2026-01-01, bản Wayback chụp 2026-10-16); `openai-terms-2026-10-16.pdf` là Service Terms (ngày cập nhật 2026-10-16).

## Đã lưu

| File | Nguồn | Phiên bản và thời điểm | SHA-256 | Dùng cho |
|---|---|---|---|---|
| `openai-terms-2026-01-01.pdf` (12 trang) | Wayback Machine: https://web.archive.org/web/20261016141108/https://openai.com/policies/terms-of-use/ | OpenAI Terms of Use, Published và Effective 2026-01-01, bản lưu chụp 2026-10-16 14:11:08 UTC; Nhà phát hành in thành PDF ngày 2026-11-04 | `83e1e2b8e0d277fb9ebfaa1dced2b6d280aa0a042cdd51ace43d4457e1bafb3a` | Quyền đối với Output của ChatGPT (biểu trưng, nội dung soạn bằng ChatGPT/Codex). Xem `PROVENANCE-LOGO.md` và `PROVENANCE-AI-CONTENT.md` |
| `openai-terms-2026-10-16.pdf` (10 trang) | https://openai.com/policies/service-terms/ (in từ trang chính thức 2026-11-04 19:35 giờ VN) | OpenAI **Service Terms**, trang ghi "Updated: October 16, 2026" (đúng ngày mốc của logo) | `c95c3001d8a56c5cacdb53fbab9054033ca65748b10295378f9ce88cd83678c2` | Mục 4 "Codex and Code Generation": Output của tính năng sinh mã, gồm OpenAI Codex, có thể chịu giấy phép bên thứ ba, kể cả mã nguồn mở |
| `anthropic-terms.pdf` (14 trang) | https://www.anthropic.com/legal/consumer-terms (PDF) | Consumer Terms of Service, Effective Oct 8, 2025, lưu 2026-11-04 | `7222642462bf559fa450982aa75ad4c7d3c1ed5c24e6e1517d7b4cf9f22806d4` | Tài khoản Claude Pro; quyền với Output của file do Claude soạn |

## Chưa lưu

| Điều khoản | Nguồn đề xuất | Lý do cần | Ghi chú |
|---|---|---|---|
| Giấy phép Apache 2.0, CC BY 4.0 | Đã nằm ở thư mục gốc (`LICENSE-Apache-2.0.txt`, `LICENSE-CC-BY-4.0.txt`) | Giấy phép của dự án | Không thuộc kho này vì đã là một phần của giấy phép dự án |

## Quy tắc

1. Mỗi file đặt tên `<nhà-cung-cấp>-<loại-điều-khoản>-<ngày-hiệu-lực-hoặc-ngày-lưu>.pdf` và ghi hàng mới trong bảng "Đã lưu" với SHA-256.
2. Ưu tiên bản lưu có ngày (Wayback) hoặc PDF in từ trang chính thức, kèm URL và ngày tải.
3. Không đưa PDF lên kho công khai. Nếu cần chứng minh sau này, giữ file gốc ngoài Git và dùng SHA-256 trong bảng này.
