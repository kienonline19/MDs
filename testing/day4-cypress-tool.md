- Cypress là một công cụ (framework viết bằng JS) kiểm thử web tự động (end-to-end testing) (test được cả hai API và giao diện)
- Viết test bằng JS hay Typescript (không phải Python/Java/C#) sử dụng các hàm/lệnh của Cypress Framework
- Code test viết bằng js sử dụng cypress được chạy trong trình duyệt qua sự điều phối của nodejs (nodejs làm nhiều việc chứ không phải chỉ chuyển tiếp code test lên trình duyệt)

- [Trang chủ](https://www.cypress.io/#create)
- Cypress rất phù hợp để test Web AI Chat
- Cypress chủ yếu làm việc trên 1 tab

- Các bước cài đặt Cypress:
1. Cài Node.JS (https://nodejs.org/en/download)

2. Khởi tạo dự án => chạy các lệnh sau theo thứ tự trong cmd:
+ d: (di chuyển vào ổ D trên laptop/pc nếu có)
+ mkdir cypress-ai-test (tạo thư mục dự án)
+ cd cypress-ai-test (di chuyển vào thư mục vừa tạo)
+ npm init -y (tạo nhanh package.json: file json chứa thông tin (tên, phiên bản dự án) và cấu hình (danh sách thư viện cần dùng, lệnh chạy dự án và test) của dự án NodeJS (javascript runtime env))
+ package.json: ghi tên, phiên bản thư viện, code của thư viện được cài trong node_modules
+ -y = --yes (bỏ qua các câu hỏi về tên dự án, phiên bản, mô tả để điền mặc định)
+ npm: công cụ quản lý, cài đặt các gói/thư viện/framework js khi cài NodeJS có sẵn luôn npm (Node Package Manager)

3. Cài cypress vào dự án bằng npm 
+ npm install cypress --save-dev

4. Mở giao diện Cypress và tạo bài test đầu tiên:
+ npx cypress open
+ Khi cửa sổ Cypress hiện lên, chọn E2E Testing => bấm Continue.
+ Chọn trình duyệt muốn chạy (như Chrome) => bấm Start E2E Testing.
+ Chọn Create new spec để tạo file test mẫu (ví dụ: ai-chat.cy.js). Toàn bộ code test của bạn sẽ nằm trong thư mục cypress/e2e/.