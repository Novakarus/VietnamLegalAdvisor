**Kết luận ngắn (chỉ trong phạm vi fixtures tổng hợp, không phải pháp luật Việt Nam):** hồ sơ nộp ngày 15/02/2030 và xét ngày 15/03/2030 vẫn theo Điều 2 cũ của F-A, tức là chỉ cần tài liệu X và Y. Tài liệu Z mà F-B bổ sung không áp dụng. Điều 3 của F-A (lưu giữ hồ sơ 2 năm) vẫn còn hiệu lực.

**Phạm vi và ngày**
- Sự kiện quyết định: ngày nộp hồ sơ, 15/02/2030.
- Ngày xét: 15/03/2030.
- Nguồn: chỉ có `tests/fixtures.md`, là bằng chứng giả định dùng để kiểm tra suy luận về thời điểm áp dụng. Nó không được dùng như căn cứ pháp lý thật.

**Dòng thời gian**
- F-A ban hành 01/01/2030 và có hiệu lực từ 01/02/2030.
- F-B ban hành 10/02/2030 và có hiệu lực từ 01/03/2030.
- Hồ sơ nộp ngày 15/02/2030, sau khi F-A có hiệu lực và trước khi F-B có hiệu lực.
- Ngày xét là 15/03/2030, khi F-B đã có hiệu lực.

**Ma trận hiệu lực theo điều khoản**

| Điều khoản | Phiên bản | Khoảng hiệu lực | Sự kiện | Chuyển tiếp | Kết luận |
|---|---|---|---|---|---|
| F-A Điều 2 (cũ: X và Y) | Gốc | 01/02/2030 đến trước 01/03/2030, rồi tiếp tục cho hồ sơ nộp trước 01/03/2030 | Nộp 15/02/2030 | F-B Điều 2 giữ lại Điều 2 cũ cho hồ sơ nộp trước 01/03/2030 | Áp dụng cho hồ sơ này: cần X và Y. |
| F-A Điều 2 (mới: X, Y và Z) theo F-B Điều 1 | Sửa đổi | Từ 01/03/2030 | Xét 15/03/2030 | Bị loại trừ vì hồ sơ nộp trước 01/03/2030 | Không áp dụng cho hồ sơ này. |
| F-A Điều 3 (lưu giữ 2 năm) | Gốc | Từ 01/02/2030 | Cả hai thời điểm | F-B chỉ thay Điều 2 và không có văn bản nào nêu bãi bỏ Điều 3 | Vẫn còn hiệu lực. |

**Lập luận**
1. Ngày xét (15/03/2030) không quyết định quy tắc áp dụng. Điều kiện chuyển tiếp của F-B dựa vào ngày nộp, không dựa vào ngày xét.
2. Vì nộp trước 01/03/2030, hồ sơ tiếp tục theo Điều 2 cũ của F-A (X và Y), kể cả khi được xét sau khi F-B có hiệu lực.
3. Cần tránh hai lỗi. Lỗi thứ nhất là áp văn bản mới nhất một cách tự động, tức đòi thêm Z. Lỗi thứ hai là cho rằng Điều 3 đã bị bãi bỏ chỉ vì F-B sửa Điều 2.

**Giới hạn và việc còn mở**
- Fixtures không nói thời điểm bắt đầu tính hai năm lưu giữ, đối tượng phải lưu giữ, hay việc Điều 3 có áp dụng cho hồ sơ này hay không. Tôi không suy đoán thêm các điểm đó.
- Kết luận được kiểm tra bằng văn bản fixtures đã cung cấp. Fixtures không chứng minh tính xác thực chính thức, vì chúng là dữ liệu giả định.
- Các công cụ thật không áp dụng ở đây vì không có công cụ tra cứu. Với văn bản pháp luật Việt Nam thật, cần lấy văn bản gốc từ nguồn chính thức, rà soát sửa đổi, bãi bỏ và quy định chuyển tiếp, rồi đối chiếu ngày hiệu lực theo từng điều khoản.

**Kiểm tra chất lượng:** kết luận đủ căn cứ trong phạm vi fixtures, nên đạt mức READY cho phạm vi giả định này. Đây không phải kết luận đã xác minh về luật Việt Nam thật. Không có yêu cầu đối kháng, vì đây không phải hợp đồng hay giao dịch cần thẩm định.

MODE: DOCUMENT_ONLY
ROUTE: instructions, legal-source-verification, legal-validity-verification, legal-quality-audit
