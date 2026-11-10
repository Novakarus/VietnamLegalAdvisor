**Kết luận ngắn:** Hồ sơ nộp ngày 15/02/2030 phải đáp ứng Điều 2 cũ của F-A, tức là tài liệu X và Y. Không cần tài liệu Z, kể cả khi xét ngày 15/03/2030.

**Lưu ý phạm vi:** F-A và F-B là tài liệu giả định trong fixtures.md, dùng để kiểm thử lập luận về thời điểm. Chúng không phải pháp luật Việt Nam và không được trích dẫn như căn cứ pháp lý thật. Kết luận dưới đây chỉ đúng trong phạm vi các fixture này.

**Chế độ truy cập:** Tôi chỉ có công cụ Read, không có tìm kiếm hay duyệt web. Vì vậy không có bước xác minh nguồn chính thức nào được thực hiện. Mọi nội dung đều dựa trên file fixtures.md do người dùng cung cấp. Tính xác thực và đầy đủ của file này là CHƯA XÁC MINH.

**Các mốc thời gian**

| Văn bản | Ban hành | Hiệu lực |
|---|---|---|
| F-A | 01/01/2030 | 01/02/2030 |
| F-B | 10/02/2030 | 01/03/2030 |
| Nộp hồ sơ (sự kiện) | 15/02/2030 | |
| Xét hồ sơ | 15/03/2030 | |

**Ma trận hiệu lực theo điều khoản**

| Điều khoản | Phiên bản | Khoảng hiệu lực | Sự kiện | Chuyển tiếp | Trạng thái |
|---|---|---|---|---|---|
| F-A Điều 2 (cũ) | X và Y | 01/02/2030 đến trước 01/03/2030. Sau đó vẫn áp dụng cho hồ sơ nộp trước 01/03/2030 theo F-B Điều 2. | Nộp ngày 15/02/2030, nằm trong khoảng hiệu lực | Hồ sơ nộp trước 01/03/2030 thì tiếp tục theo Điều 2 cũ | **Áp dụng**: cần X và Y |
| F-A Điều 2 (sửa bởi F-B Điều 1) | X, Y và Z | Từ 01/03/2030 | Ngày xét 15/03/2030 nằm trong hiệu lực của F-B, nhưng thời điểm nộp mới là mốc quyết định | Bị loại trừ vì hồ sơ nộp trước 01/03/2030 | **Không áp dụng** cho hồ sơ này |
| F-A Điều 3 (lưu trữ 2 năm) | Không bị sửa | Từ 01/02/2030 | Không liên quan trực tiếp đến thành phần hồ sơ | Không có | Vẫn còn hiệu lực trong phạm vi fixture, vì không fixture nào nêu bãi bỏ |

**Lập luận**
1. Ngày nộp 15/02/2030 nằm sau khi F-A có hiệu lực (01/02/2030) và trước khi F-B có hiệu lực (01/03/2030). Tại thời điểm nộp, chỉ có Điều 2 cũ của F-A đang có hiệu lực.
2. F-B Điều 2 là quy định chuyển tiếp. Hồ sơ nộp trước 01/03/2030 tiếp tục theo Điều 2 cũ của F-A. Ngày xét 15/03/2030 là sau khi F-B có hiệu lực, nhưng điều kiện chuyển tiếp dựa vào ngày nộp chứ không dựa vào ngày xét. Do đó không dùng yêu cầu bổ sung Z.
3. Điều 3 của F-A không bị F-B sửa hay bãi bỏ. Việc "không có fixture nào nêu bãi bỏ" chỉ có nghĩa trong phạm vi các fixture này. Nó không chứng minh Điều 3 còn hiệu lực trong thực tế.

**Rủi ro**
- **Rủi ro pháp lý (thấp trong phạm vi fixture):** Nếu cơ quan xét hồ sơ áp dụng nhầm Điều 2 mới, họ có thể đòi thêm Z. Khi đó có thể viện dẫn F-B Điều 2.
- **Rủi ro thương mại:** Việc chuẩn bị thêm Z không bắt buộc sẽ tốn chi phí và thời gian. Nên chuẩn bị Z chỉ khi muốn phòng ngừa.
- **Rủi ro chưa xác minh:** Nếu có văn bản khác ngoài fixture, chẳng hạn văn bản sửa đổi, đính chính hay hướng dẫn, thì kết luận có thể thay đổi.

**Kiểm tra chất lượng (legal-quality-audit)**
- Kết luận đầy đủ và nhất quán trong phạm vi fixture, không có điều khoản bịa đặt.
- Tình trạng: **LIMITED**. Chưa xác minh nguồn chính thức, vì không có công cụ truy cập. Nếu áp dụng cho văn bản thật thì chưa thể coi là đã xác minh.

**Bước tiếp theo**
1. Xác nhận ngày nộp 15/02/2030 bằng bằng chứng nộp hồ sơ, chẳng hạn biên nhận hoặc dấu tiếp nhận.
2. Nếu áp dụng cho văn bản thật, lấy bản gốc chính thức của văn bản gốc, văn bản sửa đổi và điều khoản chuyển tiếp. Sau đó kiểm tra lại hiệu lực theo từng điều khoản.
3. Xác định thời điểm bắt đầu tính hai năm lưu trữ, vì F-A Điều 3 không nêu mốc này.

MODE: DOCUMENT_ONLY
ROUTE: instructions, legal-source-verification, legal-validity-verification, legal-quality-audit

Ghi chú cho phiên chính: nên dùng tiếp agent statusline-setup nếu cần thay đổi dòng trạng thái. Người dùng có thể yêu cầu Claude tiếp tục điều chỉnh status line.
