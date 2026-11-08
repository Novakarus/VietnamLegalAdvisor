**Kết luận ngắn (dữ liệu giả lập, không phải pháp luật Việt Nam)**

Tại ngày 15/02/2030, F-A đang có hiệu lực và F-B chưa có hiệu lực. Vì vậy, nếu hồ sơ nộp vào ngày này, hồ sơ chỉ cần tài liệu X và Y theo Điều 2 F-A. Điều 3 F-A (lưu giữ hồ sơ hai năm) vẫn áp dụng.

**Phạm vi và giả định**
- Ngày 15/02/2030 là ngày rà soát. Tôi giả định nó cũng là ngày phát sinh sự kiện (nộp hồ sơ), vì tin nhắn không nêu ngày nộp hồ sơ khác.
- Chỉ dùng `tests/fixtures.md`. Đây là bản cung cấp, chưa xác minh tính xác thực công khai.
- Không có nguồn chính thức nào được truy xuất.

**Dòng thời gian**
- 01/01/2030: F-A ban hành.
- 01/02/2030: F-A có hiệu lực.
- 10/02/2030: F-B ban hành.
- 15/02/2030: ngày xét.
- 01/03/2030: F-B có hiệu lực.

**Ma trận hiệu lực tại 15/02/2030**

| Điều khoản | Phiên bản | Khoảng hiệu lực | Chuyển tiếp | Tình trạng tại 15/02/2030 |
|---|---|---|---|---|
| F-A Điều 2 (hồ sơ cần X, Y) | Gốc | Từ 01/02/2030 tới trước 01/03/2030 | Hồ sơ nộp trước 01/03/2030 tiếp tục theo Điều 2 cũ (F-B Điều 2) | Đang áp dụng |
| F-B Điều 1 (thay Điều 2: X, Y, Z) | Thay thế | Từ 01/03/2030 | Không áp dụng cho hồ sơ nộp trước 01/03/2030 | Đã ban hành, chưa có hiệu lực |
| F-A Điều 3 (lưu giữ hai năm) | Gốc | Từ 01/02/2030 | Không có | Đang áp dụng. F-B chỉ thay Điều 2 và fixture không nêu Điều 3 bị bãi bỏ. |

**So sánh F-A và F-B**
- **Nội dung:** F-B chỉ sửa Điều 2 của F-A, thêm yêu cầu tài liệu Z. Các điều khác của F-A không bị F-B đụng tới.
- **Thời điểm có hiệu lực:** F-B ban hành ngày 10/02/2030 nhưng chỉ có hiệu lực từ 01/03/2030. Ngày ban hành khác ngày có hiệu lực, nên không được dùng văn bản mới nhất một cách mặc định.
- **Chuyển tiếp:** hồ sơ nộp trước 01/03/2030 vẫn theo Điều 2 cũ, tức X và Y. Điều này đúng cả khi quyết định được đưa ra sau 01/03/2030. Fixture chỉ nói về ngày nộp, không nói về ngày giải quyết.
- **Hồ sơ nộp từ 01/03/2030:** cần X, Y và Z.

**Rủi ro và mục còn mở**
- Việc F-B không sửa Điều 3 chỉ là suy luận từ văn bản cung cấp. Fixture ghi rõ không có điều khoản bãi bỏ Điều 3.
- Nếu ngày nộp thực tế khác 15/02/2030, cần xét lại theo mốc 01/03/2030.
- Đây là bài kiểm tra suy luận thời gian. Không dùng làm căn cứ pháp lý thực.

**Bước tiếp theo (nếu áp dụng cho văn bản thật)**
1. Xác định rõ ngày nộp hồ sơ.
2. Lấy văn bản gốc từ kênh công bố chính thức.
3. Đọc điều khoản sửa đổi, bãi bỏ và chuyển tiếp.
4. Đánh giá hiệu lực theo từng điều khoản.

**Kiểm tra chất lượng:** READY trong phạm vi fixture giả lập. Không nâng thành "đã xác minh" đối với pháp luật thực vì không có truy xuất nguồn.

MODE: DOCUMENT_ONLY
ROUTE: instructions, legal-validity-verification, vietnam-legal-research, legal-source-verification, legal-quality-audit
