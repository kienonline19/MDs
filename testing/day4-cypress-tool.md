## Tổng quan về Cypress

- Cypress là một công cụ (framework viết bằng JS) kiểm thử web tự động (end-to-end testing) (test được cả hai API và giao diện)
- Viết test bằng JS hay Typescript (không phải Python/Java/C#) sử dụng các hàm/lệnh của Cypress Framework
- Code test viết bằng js sử dụng cypress được chạy trong trình duyệt qua sự điều phối của nodejs (nodejs làm nhiều việc chứ không phải chỉ chuyển tiếp code test lên trình duyệt)
- Cypress rất phù hợp để test Web AI Chat
- Cypress chủ yếu làm việc trên 1 tab

### Tài liệu tham khảo về Cypress

1. [Trang chủ](https://www.cypress.io/#create)
2. https://learn.cypress.io/real-world-examples
3. https://docs.cypress.io/app/get-started/why-cypress

### Cài đặt và thực hành bài test đầu tiên

**Các bước cài đặt Cypress:**

1. Cài Node.JS (https://nodejs.org/en/download)
2. Khởi tạo dự án => chạy các lệnh sau theo thứ tự trong cmd:

   - `d:` (di chuyển vào ổ D trên laptop/pc nếu có)
   - `mkdir cypress-ai-test` (tạo thư mục dự án)
   - `cd cypress-ai-test` (di chuyển vào thư mục vừa tạo)
   - `npm init -y` (tạo nhanh package.json: file json chứa thông tin (tên, phiên bản dự án) và cấu hình (danh sách thư viện cần dùng, lệnh chạy dự án và test) của dự án NodeJS (javascript runtime env))
   - `package.json`: ghi tên, phiên bản thư viện, code của thư viện được cài trong `node_modules`
   - `-y` = `--yes` (bỏ qua các câu hỏi về tên dự án, phiên bản, mô tả để điền mặc định)
   - `npm`: công cụ quản lý, cài đặt các gói/thư viện/framework js khi cài NodeJS có sẵn luôn npm (Node Package Manager)

3. Cài cypress và typescript vào dự án bằng npm

   - `npm install cypress --save-dev`
   - `npm install typescript --save-dev`

4. Mở giao diện Cypress và tạo bài test đầu tiên:

   - `npx cypress open`
   - Khi cửa sổ Cypress hiện lên, chọn E2E Testing => bấm Continue.
   - Chọn trình duyệt muốn chạy (như Chrome) => bấm Start E2E Testing.
   - Chọn Create new spec để tạo file test mẫu (ví dụ: `ai-chat.cy.js`). Toàn bộ code test của bạn sẽ nằm trong thư mục `cypress/e2e/`.

### Thực hành tìm hiểu dự án mẫu của cypress team trên github:

- Link: https://github.com/cypress-io/cypress-realworld-app/

1. `git clone https://github.com/cypress-io/cypress-realworld-app.git`
2. `cd cypress-realworld-app`
3. `npm install -g yarn`
4. `yarn install`
5. `yarn dev` (để nó chạy không tắt và mở thêm 1 terminal mới gõ lệnh)
6. `yarn cypress:open` (password của hầu hết các user: s3cret - xem users ở `data/database.json`)
7. `yarn cypress:run` (chạy ngầm toàn bộ test)

**Chạy với extension Cypress Test Explorer với cấu hình sau:**

- **Tests Directory:** `cypress/tests`
- **Cypress Command:** `yarn cypress`
- Các ô khác để trống

**Fix lỗi + cảnh báo (nếu có):**

1. Thêm `"ignoreDeprecations": "6.0"` vào `tsconfig.json` (thư mục root)
2. Kill port bị chiếm dụng khi backend gặp lỗi => run: `npx kill-port 3001`

## Thực hành viết test với cypress để kiểm thử web AI chat

**Các trang web có thể dùng cypress test:**

1. https://duck.ai/
2. https://chat.webllm.ai/
3. https://zalt.me/tools/free-ai-chat-online
4. https://github.com/mckaywrigley/chatbot-ui
5. https://github.com/ChatGPTNextWeb/NextChat

**Sử dụng vscode với extension và comment đặc biệt sau để chạy cypress test:**

1. Cypress Test Explorer

   - Ô **Tests Directory:** gõ vào `cypress-ai-test/cypress/e2e`
   - Ô **Cypress Project:** gõ vào `cypress-ai-test`
   - Các ô khác để nguyên
   - Run test mặc định chạy ngầm ở chế độ ẩn trình duyệt (headless), muốn mở trình duyệt nhìn thấy từng thao tác thì bấm Debug Test

2. comment ở đầu mỗi file js viết cypress test bên trong (để tự động gợi ý trong vscode cho cypress):

   ```js
   /// <reference types="cypress" />
   ```

3. Cấu hình gợi ý code cypress không cần nhớ cú pháp bằng cách tạo file `jsconfig.json` trong thư mục cypress project rồi dán đoạn cấu hình sau vào file đó

   - tự động bật gợi ý câu lệnh của cypress trong các file js ở thư mục hiện tại và các thư mục con bên trong

   ```json
   {
     "compilerOptions": {
       "types": ["cypress"]
     },
     "include": ["**/*.js"]
   }
   ```

## Thực hành với duck.ai

### Khung sườn của bài Test (`describe` và `it`)

```javascript
describe('Duck.ai', () => {
    it('Select a model, submits a question, and verifies the answer', () => {
        // ... (các bước test sẽ nằm ở đây)
    })
})
```

**Giải thích:** `describe` gom nhóm toàn bộ các bài test liên quan đến trang Duck.ai. Hàm `it` đại diện cho một kịch bản test cụ thể (chọn model, hỏi và xác nhận câu trả lời).

**Tài liệu tham khảo:** [Writing Your First End-to-End Test](https://docs.cypress.io/guides/end-to-end-testing/writing-your-first-end-to-end-test)

---

### Bước 1: Mở trang web (`cy.visit`)

```javascript
// 1. Open the website
/* cy.visit('https://duck.ai/', { -- Ghi đè biến webdriver ngay trước khi web chạy
    onBeforeLoad(win) {
        Object.defineProperty(win.navigator, 'webdriver', {
            get: () => undefined,
        });
    },
}); */
cy.visit('https://duck.ai/');
```

**Giải thích:** Lệnh `cy.visit` điều khiển trình duyệt truy cập vào URL được chỉ định. Phần comment nhiều dòng `/* ... */` của bạn lưu lại kỹ thuật dùng `onBeforeLoad` can thiệp vào đối tượng `window` (`win`) của trình duyệt để xóa dấu vết `webdriver` trước khi trang kịp tải (giúp qua mặt CAPTCHA chống Bot). Lệnh `cy.visit` đang mở bên dưới là cách truy cập thông thường.

**Tài liệu tham khảo:** [cy.visit()](https://docs.cypress.io/api/commands/visit) | [Catalog of Events (onBeforeLoad)](https://www.google.com/search?q=https://docs.cypress.io/api/events/catalog-of-events%23Window-Before-Load)

---

### Bước 2 & 3: Tương tác với danh sách Dropdown (`cy.get`, `cy.contains`, `.click`)

```javascript
// 2. Open the model list
cy.get('[data-testid="model-picker-button"]').should('be.visible').click();

// 3. Select Mistral Small 4
cy.contains('[role="menuitemradio"]', 'Mistral').click();
```

**Giải thích:**

- Bước 2 dùng `cy.get` để tìm nút bấm theo thuộc tính `data-testid` (đây là thực hành tốt nhất trong Cypress), kiểm tra nút đã hiển thị (`be.visible`) rồi click để mở menu thả xuống.
- Bước 3 dùng `cy.contains` để tìm một phần tử có thuộc tính `role="menuitemradio"` và hiển thị chính xác chữ `Mistral` trên màn hình rồi click vào nó.

**Tài liệu tham khảo:** [cy.get()](https://docs.cypress.io/api/commands/get) | [cy.contains()](https://docs.cypress.io/api/commands/contains) | [Best Practices: Selecting Elements](https://www.google.com/search?q=https://docs.cypress.io/guides/references/best-practices%23Selecting-Elements)

---

### Bước 4: Kiểm tra trạng thái UI - Assertion (`.should`)

```javascript
// 4. Verify the correct model is selected
cy.get('[data-testid="model-picker-button"]').should('contain.text', 'Mistral');
```

**Giải thích:** Sau khi chọn model ở bước 3, lệnh `.should('contain.text', 'Mistral')` hoạt động như một "trạm kiểm soát" để đảm bảo rằng tên model đã được cập nhật thành công trên chính nút bấm đó. Test sẽ thất bại (đỏ) nếu chữ Mistral không xuất hiện.

**Tài liệu tham khảo:** [cy.should()](https://docs.cypress.io/api/commands/should) | [Assertions Reference (Chai)](https://docs.cypress.io/guides/references/assertions)

---

### Bước 5: Gõ văn bản mô phỏng người thật (`.type`)

```javascript
// 5. Enter question
/*
    <textarea name="user-prompt" aria-label="Ask anything privately" class="Pjdc_gGEjnjd_NraQ4DV ir13N7GbOMQ1hsegKnJz" rows="1" inputmode="text" autocomplete="off" placeholder="Ask anything privately" style="height: 56px;"></textarea>
*/
cy.get('textarea[name="user-prompt"]')
    .should('be.visible')
    .type(
        'Join the words CYPRESS and OK with an underscore. ' +
        'Reply with only the result, without formatting.', { delay: 50 } // ms - giống người thật 10ms: giống máy
    );
```

**Giải thích:** Đoạn HTML trong comment cho thấy bạn phân tích thẻ `<textarea>` rất chuẩn xác để lấy ra thuộc tính `name="user-prompt"`. Lệnh `.type()` sẽ tiến hành gõ đoạn text vào ô này. Tham số `{ delay: 50 }` bắt trình duyệt nghỉ 50ms giữa mỗi lần gõ phím đúng như comment của bạn đã ghi, giúp tránh bị hệ thống chặn vì gõ quá nhanh.

**Tài liệu tham khảo:** [cy.type() Options](https://www.google.com/search?q=https://docs.cypress.io/api/commands/type%23Arguments)

---

### Bước 6: Bấm nút Gửi an toàn

```javascript
// 6. Click Send Button
cy.get('button[aria-label="Ask"]')
    .should('not.be.disabled')
    .click();
```

**Giải thích:** Tìm nút bấm bằng thuộc tính `aria-label`. Việc chèn thêm `.should('not.be.disabled')` là rất cẩn thận, nó buộc Cypress phải chờ cho đến khi ô nhập liệu nhận diện được chữ đã gõ và mở khóa nút Gửi thì mới thực hiện lệnh `.click()`.

**Tài liệu tham khảo:** [State Assertions (disabled / enabled)](https://www.google.com/search?q=https://docs.cypress.io/guides/references/assertions%23State)

---

### Bước 7: Chờ phản hồi từ AI (`timeout` và `Regex`)

```javascript
// 7. Wait up to 60 seconds to see the answer
cy.contains(/^CYPRESS_OK$/, { timeout: 60000 }).should('be.visible'); // timeout (ms) 1s = 1000ms
```

**Giải thích:** Khối lệnh này sử dụng Biểu thức chính quy (Regex: `/^CYPRESS_OK$/`) để yêu cầu Cypress tìm một thành phần trên trang chứa nội dung khớp 100% với chuỗi "CYPRESS_OK" (không thừa, không thiếu ký tự nào). Vì AI cần thời gian phản hồi, `{ timeout: 60000 }` ghi đè thời gian chờ mặc định (4s) thành 60 giây, giúp bài test không bị báo lỗi vội vàng.

**Tài liệu tham khảo:** [Timeouts in Cypress](https://www.google.com/search?q=https://docs.cypress.io/guides/core-concepts/time-out) | [Regular Expressions with cy.contains](https://www.google.com/search?q=https://docs.cypress.io/api/commands/contains%23Regular-Expression)

### Giải thích thêm về code trong comment

#### Mục đích của đoạn code này là gì?

Khi Cypress (hay bất kỳ công cụ test tự động nào) mở trình duyệt lên, nó sẽ tự động gắn một "cái mác" vào trình duyệt có tên là biến `navigator.webdriver = true`.

Các trang web như Duck.ai lập trình sẵn một lớp bảo vệ: Ngay khi web vừa tải, nó sẽ kiểm tra biến này. Nếu thấy `true`, nó biết ngay đây là Bot và sẽ chặn lại (bắt giải CAPTCHA con vịt). Đoạn code này dùng để **giấu cái mác đó đi** trước khi trang web kịp kiểm tra.

---

#### Phân tích chi tiết từng dòng lệnh

```javascript
cy.visit('https://duck.ai/', {
    onBeforeLoad(win) {
        Object.defineProperty(win.navigator, 'webdriver', {
            get: () => undefined,
        });
    },
});
```

##### 1. Mở rộng tùy chọn của lệnh `cy.visit`

```javascript
cy.visit('https://duck.ai/', { ... });
```

**Giải thích:** Bình thường `cy.visit('URL')` chỉ nhận 1 tham số là đường dẫn. Tuy nhiên, nó có thể nhận tham số thứ 2 là một `{ object }` chứa các tùy chọn cài đặt (options). Ở đây, ta mở ra một object để thêm kịch bản can thiệp vào quá trình tải trang.

##### 2. Sự kiện `onBeforeLoad(win)`

```javascript
onBeforeLoad(win) { ... }
```

**Giải thích:** Đây là một hàm (function) đặc biệt của Cypress. Nó sẽ được kích hoạt vào khoảnh khắc **màn hình trình duyệt vừa mở ra, nhưng CHƯA CÓ một dòng code JavaScript nào của trang Duck.ai kịp chạy**.

- Tham số `win`: Đại diện cho đối tượng `window` của trình duyệt đang mở (chứa toàn bộ thông tin về trình duyệt, tab hiện tại).

**Ví dụ thực tế:** Giống như việc bạn (trình duyệt) bước vào cửa một tòa nhà (trang web). `onBeforeLoad` là khoảnh khắc bạn vừa đẩy cửa bước vào, còn bảo vệ (code của web) thì chưa kịp nhìn thấy bạn.

##### 3. Căn thiệp biến hệ thống bằng `Object.defineProperty`

```javascript
Object.defineProperty(win.navigator, 'webdriver', { ... });
```

**Giải thích:** Bạn không thể viết lệnh đơn giản như `win.navigator.webdriver = undefined` được, vì biến `webdriver` được trình duyệt khóa lại ở chế độ **chỉ đọc (read-only)**. Hàm `Object.defineProperty` là lệnh quyền năng nhất trong JavaScript dùng để **cưỡng chế định nghĩa lại** một thuộc tính, bất chấp việc nó bị khóa.

- Tham số 1 (`win.navigator`): Đối tượng chứa biến cần sửa (thông tin nhân trình duyệt).
- Tham số 2 (`'webdriver'`): Tên của biến muốn sửa.
- Tham số 3 (`{ ... }`): Cấu hình mới cho biến đó.

##### 4. Đánh lừa bằng hàm `get` (Getter)

```javascript
get: () => undefined,
```

**Giải thích:** Thay vì gán một giá trị tĩnh, ta định nghĩa một hàm `get` (getter). Mỗi khi trang Duck.ai hỏi: **"Này trình duyệt, biến webdriver của mày đang là gì thế?"**, hàm `get` này sẽ được gọi và lập tức trả lời là `undefined` (Không có).

**Ví dụ thực tế:**

- **Bình thường Cypress:** Bị dán sẵn cái băng rôn trên trán ghi "TÔI LÀ ROBOT" (`true`). Bảo vệ web nhìn thấy -> Chặn.
- **Dùng đoạn code này:** Ngay trước khi bảo vệ kịp nhìn (`onBeforeLoad`), ta gắn một máy phản hồi tự động (`Object.defineProperty`). Khi bảo vệ hỏi "Có phải robot không?", máy tự động trả lời "Không biết, không thấy gì cả" (`undefined`). Bảo vệ web tưởng là người thật -> Cho qua.

---

#### Tóm tắt lại quá trình thực thi:

1. Cypress ra lệnh truy cập Duck.ai.
2. Duck.ai trả về khung HTML trắng.
3. **Cypress nhảy vào chặn lại (`onBeforeLoad`), lén sửa thông tin trình duyệt (`undefined`).**
4. Duck.ai bắt đầu chạy JavaScript để kiểm tra.
5. Duck.ai thấy biến webdriver là `undefined` (giống y hệt một người dùng lướt web bình thường).
6. Duck.ai tải giao diện chat mà không hiện CAPTCHA.

#### Tài liệu tham khảo để đọc thêm

- **Về `onBeforeLoad` trong Cypress:** [cy.visit() Options - onBeforeLoad](https://www.google.com/search?q=https://docs.cypress.io/api/commands/visit%23Arguments)
- **Về `Object.defineProperty` (JavaScript cơ bản):** [MDN Web Docs - Object.defineProperty()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)
- **Về cách hoạt động của biến `webdriver`:** [MDN Web Docs - Navigator: webdriver](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/webdriver)
