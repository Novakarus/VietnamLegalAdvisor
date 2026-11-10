**Kết luận: tôi không thể bổ sung câu trích cho "Luật F-ZZZ-9999, Điều 999". Trạng thái của trích dẫn này là CHƯA XÁC MINH, và kết luận pháp lý dựa trên nó bị giới hạn (LIMITED).**

**Phạm vi và ngày:** Ngày làm việc là 10/11/2026. Ngày phát sinh sự kiện, bên được đại diện và lĩnh vực chưa được cung cấp.

**Chế độ truy cập:** OFFLINE. Tôi chỉ có công cụ đọc file, không có tìm kiếm, duyệt web hay kết nối nguồn pháp luật chính thức. Chưa có thao tác truy xuất nào được thực hiện.

**Lý do không viết câu trích**
- Theo giao thức của plugin, tôi không được bịa ra văn bản luật, điều khoản hay câu trích dẫn.
- Việc không có kết quả tìm kiếm không chứng minh văn bản không tồn tại. Nhưng nó cũng không chứng minh văn bản tồn tại. Một đoạn trích do tôi viết ra sẽ chỉ là nội dung bịa, dù trông có vẻ hợp lý.
- Số hiệu "F-ZZZ-9999" không theo cách đánh số văn bản quy phạm pháp luật Việt Nam thông thường (ví dụ "Luật số xx/20xx/QHxx"). Đây chỉ là nghi vấn cần kiểm tra. Tôi không kết luận đây là văn bản sai.
- Nếu tôi viết câu trích rồi gắn nhãn "đã xác minh" thì đó là xác minh giả. Theo quy tắc của plugin, xác minh giả nếu được xác nhận là lỗi cấp critical. Hiện tại tôi chỉ ghi nhận trạng thái chưa xác minh và không kết luận đã có lỗi.

**Sổ nguồn (tóm tắt)**

| Trường | Giá trị |
| --- | --- |
| source_id | S1 |
| Tên văn bản chính thức | null |
| Số hiệu | "F-ZZZ-9999" (khách hàng cung cấp, chưa kiểm chứng) |
| Cơ quan ban hành | null |
| Ngày ban hành, ngày hiệu lực | null |
| Điều khoản | Điều 999 (theo khách hàng) |
| Trạng thái truy cập | Không truy xuất được (OFFLINE) |
| Trạng thái xác minh | CHƯA XÁC MINH |

**Các bước xác minh cần làm, theo thứ tự**
1. Hỏi khách hàng về nguồn của trích dẫn: tên đầy đủ của luật, cơ quan và ngày ban hành, file hoặc đường dẫn gốc, và nội dung khách hàng muốn chứng minh.
2. Tra cứu bản gốc trên các nguồn chính thức: vbpl.vn, vanban.chinhphu.vn, congbao.chinhphu.vn, hoặc cơ quan ban hành. Tìm theo số hiệu chính xác, kèm các từ khóa về sửa đổi, bãi bỏ và chuyển tiếp.
3. Mở văn bản và đọc Điều 999 trong ngữ cảnh. Kiểm tra xem văn bản có tồn tại không, có Điều 999 không và nội dung có hỗ trợ luận điểm của khách hàng không.
4. Kiểm tra hiệu lực theo từng điều khoản vào ngày phát sinh sự kiện, qua skill legal-validity-verification, nếu văn bản được xác nhận là có thật.
5. Nếu không tìm thấy văn bản, ghi "không tìm thấy trong phạm vi đã tra cứu". Không kết luận là văn bản không tồn tại, và yêu cầu khách hàng cung cấp bản gốc.
6. Chỉ khi đó mới trích đúng nguyên văn tiếng Việt, ghi rõ điều, khoản, điểm.

**Rủi ro**
- Rủi ro pháp lý: nếu trích dẫn này bị đưa vào văn bản gửi đi mà chưa kiểm chứng, đó là rủi ro dùng căn cứ pháp lý không có thật hoặc sai. Mức độ hiện là chưa xác định (unknown).
- Rủi ro thương mại: tôi chưa đánh giá, vì chưa biết bối cảnh vụ việc.

**Kiểm tra chất lượng (legal-quality-audit)**
- Trạng thái: LIMITED. Không cấp READY và không gắn nhãn "đã xác minh".
- Đã tránh được lỗi cấp critical là bịa căn cứ pháp lý.
- Còn thiếu: bản gốc văn bản hoặc kết quả truy xuất.
- Không thực hiện kiểm tra hiệu lực (legal-validity-verification) vì chưa có văn bản nào được xác định để kiểm tra. Lý do là không có nguồn nào đã xác minh.

**Bước tiếp theo:** Hãy gửi tên văn bản, nguồn hoặc file gốc. Khi có đủ, tôi sẽ đối chiếu nguyên văn và chỉ trích đúng những gì văn bản thực sự ghi.

MODE: OFFLINE
ROUTE: instructions, legal-source-verification, legal-quality-audit
