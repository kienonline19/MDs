## Tổng quan về Cypress
- Cypress là một công cụ (framework viết bằng JS) kiểm thử web tự động (end-to-end testing) (test được cả hai API và giao diện)
- Viết test bằng JS hay Typescript (không phải Python/Java/C#) sử dụng các hàm/lệnh của Cypress Framework
- Code test viết bằng js sử dụng cypress được chạy trong trình duyệt qua sự điều phối của nodejs (nodejs làm nhiều việc chứ không phải chỉ chuyển tiếp code test lên trình duyệt)
- Cypress rất phù hợp để test Web AI Chat
- Cypress chủ yếu làm việc trên 1 tab

#### Tài liệu tham khảo về Cypress 
1. [Trang chủ](https://www.cypress.io/#create)
2. https://learn.cypress.io/real-world-examples
3. https://docs.cypress.io/app/get-started/why-cypress

#### Cài đặt và thực hành bài test đầu tiên
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

#### Thực hành tìm hiểu dự án mẫu của cypress team trên github:
- Link: https://github.com/cypress-io/cypress-realworld-app/

1. git clone https://github.com/cypress-io/cypress-realworld-app.git
2. cd cypress-realworld-app
3. npm install -g yarn
4. yarn install
5. yarn dev (để nó chạy không tắt và mở thêm 1 terminal mới gõ lệnh)
6. yarn cypress:open (password của hầu hết các user: s3cret - xem users ở data/database.json)
7. yarn cypress:run (chạy ngầm toàn bộ test)

- Chạy với extension Cypress Test Explorer với cấu hình sau:
+ Tests Directory: cypress/tests
+ Cypress Command: yarn cypress
+ Các ô khác để trống


## Thực hành viết test với cypress để kiểm thử web AI chat

- Các trang web có thể dùng cypress test:
1. https://duck.ai/
2. https://chat.webllm.ai/
3. https://zalt.me/tools/free-ai-chat-online
4. https://github.com/mckaywrigley/chatbot-ui
5. https://github.com/ChatGPTNextWeb/NextChat

- Sử dụng vscode với extension và comment đặc biệt sau để chạy cypress test:
1. Cypress Test Explorer

- Ô Tests Directory: gõ vào cypress-ai-test/cypress/e2e
- Ô Cypress Project: gõ vào cypress-ai-test
- Các ô khác để nguyên

- Run test mặc định chạy ngầm ở chế độ ẩn trình duyệt (headless), muốn mở trình duyệt nhìn thấy từng thao tác thì bấm Debug Test

2. comment ở đầu mỗi file js viết cypress test bên trong (để tự động gợi ý trong vscode cho cypress):
```js
/// <reference types="cypress" />
```
3. Cấu hình gợi ý code cypress không cần nhớ cú pháp bằng cách tạo file jsconfig.json trong thư mục cypress project rồi dán đoạn cấu hình sau vào file đó
- tự động bật gợi ý câu lệnh của cypress trong các file js ở thư mục hiện tại và các thư mục con bên trong
```json
{
  "compilerOptions": {
    "types": ["cypress"]
  },
  "include": ["**/*.js"]
}
```

