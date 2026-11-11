# Danh sách nghĩa vụ tuân thủ và theo dõi thay đổi luật: kết luận có giới hạn (LIMITED)

## 1. Kết luận trước

**Hai phần của yêu cầu có mức khả thi khác nhau:**

1. **Danh sách nghĩa vụ tuân thủ:** Tôi chưa lập được danh sách có căn cứ pháp lý. Yêu cầu chưa nêu hoạt động kinh doanh, ngành, pháp nhân, địa bàn hay ngày áp dụng. Plugin cũng đang ở chế độ OFFLINE, nên tôi chưa truy xuất hay đọc văn bản gốc nào. Tôi không điền sẵn điều, khoản hay số hiệu văn bản nào, vì làm vậy sẽ là bịa nguồn. Phần dưới đây gồm khung sổ nghĩa vụ và trình tự xác minh cần thực hiện ngay.
2. **Tự động theo dõi thay đổi luật mỗi ngày:** Không thực hiện được. Plugin không đóng gói scheduler, MCP, API key hay cơ chế đồng bộ tự động. Bạn cũng xác nhận không có scheduler. Quy định của plugin chỉ cho phép kiểm tra theo yêu cầu (on-demand) và theo sự kiện (event-driven), **thủ công**. Việc theo dõi hằng ngày không được coi là đã bật. Tôi sẽ không gửi thông báo, nộp hồ sơ hay giám sát thay bạn.

## 2. Thông tin cần bổ sung

Chỉ nhóm này làm thay đổi đáng kể kết quả:

- Hoạt động kinh doanh cụ thể và pháp nhân chịu trách nhiệm.
- Ngành, địa bàn, quy mô, dòng dữ liệu, giấy phép hiện có.
- Ngày áp dụng và ngày rà soát.
- Các biện pháp kiểm soát hiện có.

## 3. Khung sổ nghĩa vụ (chưa có nội dung pháp lý)

Các cột này là cấu trúc, không phải kết luận. Các ô nguồn và ngày chỉ được điền sau khi đọc văn bản gốc.

| Nghĩa vụ | Nguồn (số hiệu, điều/khoản) | Điều kiện áp dụng | Hạn / mốc tính | Bằng chứng kiểm soát | Trạng thái | Rủi ro pháp lý | Tác động thương mại | Người phụ trách |
|---|---|---|---|---|---|---|---|---|
| (điền sau khi xác định hoạt động) | CHƯA XÁC MINH | | | | không áp dụng / tuân thủ / thiếu sót / chưa rõ | | | |

Trạng thái "tuân thủ" chỉ ghi khi có bằng chứng vận hành kiểm soát. Tự khai báo không đủ. "Chưa rõ" khác với "vi phạm". Rủi ro pháp lý và tác động thương mại được đánh giá riêng.

## 4. Trình tự xác minh thực hiện ngay

Đây là các bước dự kiến, **chưa phải đã tra cứu**:

1. Xác định hoạt động, pháp nhân, ngành, địa phương, ngày sự kiện và ngày rà soát.
2. Lấy văn bản gốc từ kênh chính thức: vbpl.vn, vanban.chinhphu.vn, congbao.chinhphu.vn hoặc cơ quan ban hành. Nguồn thứ cấp chỉ dùng để tìm manh mối.
3. Đọc đúng điều khoản và các văn bản sửa đổi, bổ sung, thay thế, bãi bỏ, quy định chuyển tiếp.
4. Xác định hiệu lực ở cấp điều khoản theo từng ngày sự kiện. Không mặc định áp dụng văn bản mới nhất. Bản hợp nhất không chứng minh hiệu lực hiện hành.
5. Ghi sổ nguồn (số hiệu, cơ quan ban hành, ngày ban hành, ngày có hiệu lực, điều khoản, URL, thời điểm truy xuất, trạng thái xác minh). Mọi nội dung chưa kiểm chứng ghi là CHƯA XÁC MINH.
6. So sánh biện pháp kiểm soát thực tế với từng nghĩa vụ, rồi xếp ưu tiên và giao người phụ trách.

Lưu ý: không tìm thấy một quy định không có nghĩa là quy định đó không tồn tại.

## 5. Theo dõi thay đổi luật: phương án thủ công

- **Kích hoạt theo sự kiện:** rà soát lại khi có thay đổi kinh doanh (hoạt động mới, địa bàn mới, loại dữ liệu mới), khi có thông tin về văn bản mới, hoặc khi đến mốc ngày quan trọng.
- **Cách thực hiện:** bạn tự đặt lịch nhắc hằng ngày hoặc hằng tuần ngoài plugin, rồi yêu cầu tôi chạy kiểm tra theo yêu cầu cho từng nghĩa vụ trong sổ. Mỗi lần kiểm tra đều đi qua bước xác minh nguồn và hiệu lực.
- **Muốn tự động thật:** cần một scheduler hoặc MCP adapter đã được xác minh về endpoint, xác thực, quyền dữ liệu, cách xử lý lỗi và bảo mật truy vấn. Hiện chưa có.

## 6. Kết quả rà soát chất lượng

- **Trạng thái: LIMITED.** Chưa thể xác nhận bất kỳ nghĩa vụ pháp lý nào là đã xác minh.
- Các điều đã nêu rõ trong câu trả lời: không có nguồn nào được truy xuất, không có scheduler, và không có kết luận nào được gắn nhãn đã xác minh.
- Bước tiếp theo: bạn cung cấp các thông tin ở mục 2, tôi sẽ lập sổ nghĩa nghĩa vụ có điều kiện và chạy trình tự ở mục 4.

MODE: OFFLINE
ROUTE: instructions, regulatory-compliance, vietnam-legal-research, legal-source-verification, legal-validity-verification, legal-quality-audit
