### REST API là gì: method (GET/POST/PUT/DELETE), status code, JSON
### Cài đặt Postman, tạo Collection, Environment
### Thực hành: Gọi thử 1 API công khai (vd: weather API), xem response

- REST API (Web API) là cách để các ứng dụng giao tiếp, trao đổi dữ liệu với nhau qua internet (bằng giao thức http/https)

- REST API = URL (endpoint) + HTTP Method + dữ liệu request/response

- HTTP là bộ quy tắc giúp trình duyệt hay app trao đổi dữ liệu với máy chủ qua internet 
+ Mô hình client-server
1. Client: trình duyệt hay ứng dụng phần mềm bắn 1 request (HTTP Request) đến server
2. Server: tiếp nhận request, xử lý và phản hồi (HTTP Response - có thể là các đoạn mã HTML, CSS, JS, JSON, ảnh, ...)

- Cấu trúc 1 HTTP Request
+ Method: hành động muốn thực hiện (GET, POST, PUT, DELETE, ...)
+ URL/Path: tài nguyên muốn truy cập
+ Headers: thông tin bổ sung (loại dữ liệu, xác thực ...)
+ Body (nếu có): dữ liệu gửi kèm (xuất hiện trong POST, PUT, PATCH), ví dụ khi submit form đăng ký tài khoản sử dụng POST sẽ có dữ liệu về username password gửi đi

- HTTP Methods: cho server biết client muốn thực hiện hành động gì với tài nguyên ?

1. GET: lấy dữ liệu

2. POST: Tạo dữ liệu mới hay thực hiện 1 hành động (gọi nhiều lần có thể tạo ra các bản ghi khác nhau)

3. PUT: Thay thế toàn bộ tài nguyên bằng dữ liệu mới (gọi nhiều lần với cùng data -> dữ liệu không đổi)

4. PATCH: Chỉ cập nhật 1 số trường của tài nguyên, không cần gửi toàn bộ dữ liệu

5. DELETE: xóa tài nguyên được chỉ định

- Cấu trúc 1 HTTP Response = trạng thái + dữ liệu kết quả server gửi về cho client
+ Status code: mã trạng thái cho biết kết quả xử lý
1. 200 OK - Thành công
2. 201 Created - tạo mới thành công
3. 400 Bad Request - request không hợp lệ
4. 401 - chưa login hay xác thực thất bại
5. 404 Not Found - không tìm thấy
6. 500 Internal Server Error - lỗi server
7. 403 - đã xác định được danh tính nhưng không có quyền

- Một số điểm lưu ý quan trọng: 

* **HTTP là stateless: mỗi request là độc lập, không liên quan đến nhau, server không tự nhớ request trước đó (đây là lý do vì sao cần cookie/token/session để duy trì login)**

* **HTTPS = HTTP + mã hóa (SSL (lỗi thời rồi)/TLS (hiện đại đang được tin dùng)) để bảo mật dữ liệu truyền đi**

* **HTTP là nền tảng để xây dựng REST API**

- Cookie: 1 mẩu dữ liệu nhỏ server gửi về sau khi request lần đầu và được lưu ở trình duyệt (client), khi có cookie thì gửi lần tiếp theo server sẽ biết mình là ai ? giải quyết vấn đề của HTTP là stateless

- Cookie để làm gì ?
1. Duy trì trạng thái login

2. Lưu giỏ hàng trên các sàn thương mại điện tử

3. Ghi nhớ ngôn ngữ hay giao diện trên các website

4. Theo dõi hành vi người dùng

- Token: 1 chuỗi ký tự server cấp cho client để nhận dạng người dùng hay giới hạn quyền truy cập

- Session (phiên làm việc): 1 cách lưu trạng thái người dùng ở phía server, giúp server "nhớ" được thông tin của client qua nhiều request khác nhau

- JSON là định dạng văn bản có cấu trúc dùng để lưu trữ và trao đổi dữ liệu giữa các hệ thống
- REST API thường dùng JSON để client và server gửi dữ liệu cho nhau

#### Test API với Postman

- Link tải Postman trên windows: https://www.postman.com/downloads/
- Hướng dẫn cài đặt postman: https://learning.postman.com/docs/getting-started/installation/install-app

- Cài và continue with Google
- Mở một working dir để làm việc trên nó

- Collection trong postman là tập hợp các HTTP Request liên quan đến nhau được gom nhóm lại để dễ quản lý
- Environment: nơi tạo các biến sử dụng khi thực hiện request

- Hướng dẫn tạo và sử dụng môi trường trong postman: https://learning.postman.com/docs/use/send-requests/variables/managing-environments

- Tạo và chỉnh sửa biến trong 1 môi trường: https://learning.postman.com/docs/use/send-requests/variables/environment-variables

- Sử dụng free online REST API: https://jsonplaceholder.typicode.com dùng cho thực hành và kiểm thử

![ảnh minh họa request đầu tiên với postman](Images/request00.png)