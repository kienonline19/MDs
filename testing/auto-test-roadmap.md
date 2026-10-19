**Tuần 1 – Tư duy automation + HTML cơ bản**
- Học: khi nào nên automation, test pyramid, môi trường test, test data.
- Viết lại 5 test case manual cho rõ bước, dữ liệu và kết quả mong đợi.
https://viblo.asia/p/how-to-write-test-cases-huong-dan-cach-viet-testcases-eW65GRY9lDO
- Bắt đầu HTML: thẻ, cây DOM, form.

**Tuần 2 – Attribute + CSS selector**
- Học `id`, `class`, `name`, `data-*`.
- Học selector: `.class`, `#id`, `[attr=value]`, cha–con, `:nth-child`.
- Bài tập: Luyện tập trên CSS Diner (https://flukeout.github.io/), rồi viết selector cho mọi phần tử của một trang login.

**Tuần 3 – DevTools (F12)**
- Elements: inspect phần tử, Ctrl+F để thử selector.
- Console: dùng `$$('...')` để kiểm tra selector chỉ khớp 1 phần tử.
- Network: xem request/response, status code, JSON.
- Thử Cypress: `cy.visit` + `cy.get().click()` với selector tự tìm.

**Tuần 4 – JavaScript (1)**
- Cài Node.js, npm, VS Code.
- Học biến, kiểu dữ liệu, string, if/else, vòng lặp, function, arrow function.

**Tuần 5 – JavaScript (2)**
- Học array, object, JSON, `import`/`export`, khái niệm bất đồng bộ (async).
- Bài tập: xử lý danh sách user, đọc dữ liệu JSON.

**Tuần 6 – Cypress cơ bản (1)**
- Cài đặt, nắm cấu trúc thư mục.
- Học `describe`/`it`, `visit`, `get`, `click`, `type`, `should`.
- Tự viết từ file trắng 2–3 test case của tuần 1 trên SauceDemo.

**Tuần 7 – Cypress cơ bản (2)**
- Học `beforeEach`, fixtures (dữ liệu test), nhiều loại assertion.
- Hiểu vì sao Cypress tự retry và chạy theo hàng đợi lệnh.
- Hoàn thành automation cả 5 test case.

**Tuần 8 – Cypress trung cấp (1)**
- Học custom command (`cy.login()`) và Page Object.
- Dùng `cy.intercept` và `cy.request` để test API.

**Tuần 9 – Cypress trung cấp (2)**
- Cấu hình môi trường (`baseUrl`, env), xử lý test flaky, report.
- Chạy test trên GitHub Actions.
- (Tùy chọn) chuyển project sang TypeScript.

**Quy tắc mỗi bài:** viết test case → làm tay với F12 → tìm selector → chuyển thành lệnh Cypress → thêm `should()`.