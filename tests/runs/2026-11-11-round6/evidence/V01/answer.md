# Kết luận

**Hồ sơ nộp ngày 15/02/2030, xét ngày 15/03/2030 áp dụng Điều 2 của F-A (cũ), tức hồ sơ gồm tài liệu X và Y. Không cần tài liệu Z.**

Các căn cứ đều lấy từ `/home/claude/vla-r6/tests/fixtures.md`. Đây là bộ dữ liệu giả lập để kiểm thử, **không phải pháp luật Việt Nam**. Kết luận chỉ có giá trị trong phạm vi file này.

## Phạm vi và các mốc ngày

| Mốc | Ngày |
|---|---|
| F-A ban hành / có hiệu lực | 01/01/2030 / 01/02/2030 |
| F-B ban hành / có hiệu lực | 10/02/2030 / 01/03/2030 |
| Ngày nộp hồ sơ (sự kiện xác định luật áp dụng) | 15/02/2030 |
| Ngày xét hồ sơ | 15/03/2030 |

## Phân tích

1. **Ngày nộp 15/02/2030.** F-A đã có hiệu lực từ 01/02/2030. F-B mới ban hành, chưa có hiệu lực, vì hiệu lực từ 01/03/2030. Tại ngày nộp, Điều 2 F-A yêu cầu X và Y.
2. **Ngày xét 15/03/2030.** F-B đã có hiệu lực. Điều 1 F-B thay Điều 2 F-A bằng yêu cầu X, Y và Z. Tuy nhiên, Điều 2 F-B (chuyển tiếp) quy định hồ sơ nộp trước 01/03/2030 tiếp tục theo Điều 2 F-A cũ. Hồ sơ nộp ngày 15/02/2030 thuộc diện này.
3. **Điều 3 F-A (lưu giữ hồ sơ hai năm).** F-B chỉ thay Điều 2, và fixture không nêu Điều 3 bị bãi bỏ. Vì vậy Điều 3 vẫn còn hiệu lực. Chưa có sự kiện nào cho thấy phải áp dụng Điều 3 trong câu hỏi này.

## Bảng trạng thái theo điều khoản

| Điều khoản | Phiên bản | Hiệu lực | Sự kiện | Chuyển tiếp | Trạng thái |
|---|---|---|---|---|---|
| F-A Điều 2 (cũ) | gốc | từ 01/02/2030 | nộp 15/02/2030 | Điều 2 F-B giữ áp dụng cho hồ sơ nộp trước 01/03/2030 | Áp dụng (X, Y) |
| F-B Điều 1 (Điều 2 mới) | thay thế | từ 01/03/2030 | xét 15/03/2030 | Không áp dụng cho hồ sơ nộp trước 01/03/2030 | Không áp dụng cho hồ sơ này |
| F-A Điều 3 | gốc | từ 01/02/2030 | không có | Không có quy định bãi bỏ | Còn hiệu lực |

## Rủi ro, giả định và giới hạn

- **Giả định:** "Nộp" là ngày hồ sơ được tiếp nhận hợp lệ. Nếu cơ quan coi hồ sơ nộp ngày khác, ví dụ nộp bổ sung sau 01/03/2030, kết luận có thể đổi. Cần xác nhận bằng bằng chứng về ngày nộp.
- **Rủi ro pháp lý:** thấp trong phạm vi fixture, vì quy tắc chuyển tiếp rõ ràng. Rủi ro thực tế là hồ sơ bị yêu cầu Z nếu bị tính là nộp lại hoặc sửa đổi sau 01/03/2030. Điều này chưa được fixture trả lời.
- **Phạm vi nguồn:** đây là chế độ DOCUMENT_ONLY. Chỉ dựa trên file được cung cấp, đúng phiên bản đó. Tôi không khẳng định văn bản có thật, đầy đủ hay còn hiệu lực ngoài file. Không có truy xuất nguồn chính thức. Không có văn bản sửa đổi, đính chính hay bãi bỏ nào khác ngoài F-A và F-B trong file.
- **Kiểm tra chất lượng:** không phát hiện lỗi critical hay major. Vì nguồn chỉ là tài liệu cung cấp, tôi xếp mức LIMITED về tính xác thực công khai.

## Bước tiếp theo

1. Xác nhận ngày nộp thực tế bằng chứng từ tiếp nhận.
2. Xác nhận hồ sơ không bị nộp lại hoặc sửa đổi sau 01/03/2030.
3. Nếu dùng cho tình huống thực, tra văn bản chính thức tương ứng tại nguồn chính thức.

MODE: DOCUMENT_ONLY
ROUTE: instructions, vietnam-legal-research, legal-source-verification, legal-validity-verification, legal-quality-audit
