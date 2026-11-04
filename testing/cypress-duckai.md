# 20 Test Case Cypress cơ bản cho Duck.ai

> **Đối tượng:** người mới bắt đầu học Cypress
> **Trang thực hành:** https://duck.ai
> **Mục tiêu:** làm quen với `cy.visit`, `cy.get`, `cy.url`, `cy.location`, `cy.title`, `.type`, `.clear`, `.click`, `cy.viewport` và câu lệnh kiểm tra `.should(...)`

---

## 0. Chuẩn bị

### Cài đặt

```bash
npm init -y
npm install cypress --save-dev
npx cypress open
```

| Lệnh | Giải thích |
|---|---|
| `npm init -y` | Tạo file `package.json` cho dự án (cờ `-y` = đồng ý mọi mặc định). |
| `npm install cypress --save-dev` | Cài Cypress vào dự án, ghi vào mục `devDependencies` (công cụ dùng khi phát triển). |
| `npx cypress open` | Mở giao diện Cypress. Lần đầu nó sẽ tự tạo thư mục `cypress/` và file `cypress.config.js`. |

### Cấu hình `cypress.config.js`

```js
const { defineConfig } = require('cypress')

module.exports = defineConfig({
  e2e: {
    defaultCommandTimeout: 10000,
  },
})
```

| Dòng | Giải thích |
|---|---|
| `const { defineConfig } = require('cypress')` | Lấy hàm `defineConfig` từ thư viện Cypress. |
| `module.exports = defineConfig({...})` | Xuất cấu hình để Cypress đọc. |
| `e2e: {...}` | Cấu hình cho loại test end-to-end (test như người dùng thật). |
| `defaultCommandTimeout: 10000` | Mỗi lệnh được chờ tối đa 10 giây (mặc định chỉ 4 giây). Duck.ai tải bằng JavaScript nên cần chờ lâu hơn một chút. |

### Tạo file test

Tạo file `cypress/e2e/duck_ai_basic.cy.js`. Đuôi `.cy.js` là bắt buộc để Cypress nhận ra đây là file test.

---

## 1. Khung chung của file test

```js
Cypress.on('uncaught:exception', () => false)

describe('Duck.ai - Test cơ bản cho người mới', () => {
  beforeEach(() => {
    cy.visit('https://duck.ai')
  })

  // ... 20 test case nằm ở đây ...
})
```

| Dòng | Giải thích |
|---|---|
| `Cypress.on('uncaught:exception', () => false)` | Nếu trang duck.ai có lỗi JavaScript riêng của nó, Cypress mặc định sẽ cho test **fail**. Dòng này bảo Cypress "bỏ qua lỗi của trang", vì ta đang test hành vi chứ không test code nội bộ của họ. |
| `describe('...', () => { ... })` | Nhóm các test lại với nhau. Chuỗi đầu tiên là tên nhóm, hiện trong báo cáo. |
| `beforeEach(() => { ... })` | Đoạn code bên trong chạy **trước mỗi** test case. Nhờ vậy test nào cũng bắt đầu từ trang chủ, không phụ thuộc nhau. |
| `cy.visit('https://duck.ai')` | Mở trang duck.ai trong trình duyệt của Cypress. |

>  **Quy tắc vàng:** mỗi test case viết theo mẫu **Tìm → (Hành động) → Kiểm tra**.

---

## 2. Nhóm 1 — Mở trang & URL

### TC01 – Mở trang thành công

```js
it('TC01 - Mở trang thành công', () => {
  cy.get('body').should('be.visible')
})
```

| Dòng | Giải thích |
|---|---|
| `it('TC01 - ...', () => {` | Khai báo **một** test case. Chuỗi là tên test, hàm mũi tên chứa các bước. |
| `cy.get('body')` | Tìm phần tử `<body>` của trang bằng CSS selector. |
| `.should('be.visible')` | Kiểm tra phần tử đang **hiển thị** trên màn hình. Nếu không → test fail. |
| `})` | Kết thúc test case. |

### TC02 – URL chứa "duck.ai"

```js
it('TC02 - URL chứa "duck.ai"', () => {
  cy.url().should('include', 'duck.ai')
})
```

| Dòng | Giải thích |
|---|---|
| `cy.url()` | Lấy địa chỉ URL hiện tại của trang. |
| `.should('include', 'duck.ai')` | Kiểm tra URL **có chứa** chuỗi `duck.ai`. |

### TC03 – Trang dùng HTTPS

```js
it('TC03 - Trang dùng giao thức HTTPS', () => {
  cy.location('protocol').should('eq', 'https:')
})
```

| Dòng | Giải thích |
|---|---|
| `cy.location('protocol')` | Lấy riêng phần **giao thức** của URL (`http:` hoặc `https:`). |
| `.should('eq', 'https:')` | `eq` = equal, kiểm tra **bằng chính xác** `https:` (chú ý có dấu `:`). |

### TC04 – Tên miền đúng

```js
it('TC04 - Tên miền đúng là duck.ai', () => {
  cy.location('hostname').should('eq', 'duck.ai')
})
```

| Dòng | Giải thích |
|---|---|
| `cy.location('hostname')` | Lấy phần **tên miền** của URL, ví dụ `duck.ai`. |
| `.should('eq', 'duck.ai')` | Kiểm tra tên miền đúng bằng `duck.ai`. |

### TC05 – Đường dẫn là trang chủ

```js
it('TC05 - Đường dẫn là trang chủ "/"', () => {
  cy.location('pathname').should('eq', '/')
})
```

| Dòng | Giải thích |
|---|---|
| `cy.location('pathname')` | Lấy phần **đường dẫn** sau tên miền. Trang chủ có đường dẫn là `/`. |
| `.should('eq', '/')` | Kiểm tra đang ở trang chủ. |

>  **So sánh:** `include` = "có chứa", `eq` = "bằng chính xác".

---

## 3. Nhóm 2 — Tiêu đề & thẻ meta

Các thẻ này nằm trong phần `<head>` của trang, người dùng không nhìn thấy nhưng rất quan trọng cho Google và mạng xã hội.

### TC06 – Tiêu đề chứa "Duck.ai"

```js
it('TC06 - Tiêu đề trang chứa "Duck.ai"', () => {
  cy.title().should('include', 'Duck.ai')
})
```

| Dòng | Giải thích |
|---|---|
| `cy.title()` | Lấy nội dung thẻ `<title>` — chữ hiện trên tab trình duyệt. |
| `.should('include', 'Duck.ai')` | Kiểm tra tiêu đề có chứa `Duck.ai`. |

### TC07 – Tiêu đề chứa "DuckDuckGo"

```js
it('TC07 - Tiêu đề trang chứa "DuckDuckGo"', () => {
  cy.title().should('include', 'DuckDuckGo')
})
```

| Dòng | Giải thích |
|---|---|
| `cy.title().should('include', 'DuckDuckGo')` | Giống TC06, chỉ đổi chữ cần tìm. Bài tập: thử đổi thành `'Google'` để thấy test **fail** trông thế nào. |

### TC08 – Có thẻ meta description

```js
it('TC08 - Có thẻ meta description', () => {
  cy.get('meta[name="description"]').should('exist')
})
```

| Dòng | Giải thích |
|---|---|
| `cy.get('meta[name="description"]')` | Tìm thẻ `<meta>` có thuộc tính `name="description"`. Cú pháp `[thuộc_tính="giá_trị"]` gọi là **attribute selector**. |
| `.should('exist')` | Kiểm tra phần tử **tồn tại** trong HTML. Dùng `exist` thay vì `be.visible` vì thẻ meta không bao giờ hiển thị. |

### TC09 – Meta description có chữ "privately"

```js
it('TC09 - Meta description có chữ "privately"', () => {
  cy.get('meta[name="description"]')
    .should('have.attr', 'content')
    .and('include', 'privately')
})
```

| Dòng | Giải thích |
|---|---|
| `cy.get('meta[name="description"]')` | Tìm thẻ meta description. |
| `.should('have.attr', 'content')` | Kiểm tra thẻ có thuộc tính `content`. Sau dòng này, Cypress "cầm" **giá trị** của `content` để kiểm tra tiếp. |
| `.and('include', 'privately')` | `.and` giống `.should`, dùng để nối thêm điều kiện: giá trị `content` phải chứa `privately`. |

### TC10 – Có meta viewport

```js
it('TC10 - Có meta viewport cho điện thoại', () => {
  cy.get('meta[name="viewport"]')
    .should('have.attr', 'content')
    .and('include', 'width=device-width')
})
```

| Dòng | Giải thích |
|---|---|
| `cy.get('meta[name="viewport"]')` | Tìm thẻ meta viewport — thẻ giúp trang hiển thị vừa màn hình điện thoại. |
| `.should('have.attr', 'content')` | Lấy giá trị thuộc tính `content`. |
| `.and('include', 'width=device-width')` | Kiểm tra trang đặt chiều rộng theo thiết bị. |

### TC11 – Link canonical

```js
it('TC11 - Link canonical trỏ về https://duck.ai/', () => {
  cy.get('link[rel="canonical"]').should('have.attr', 'href', 'https://duck.ai/')
})
```

| Dòng | Giải thích |
|---|---|
| `cy.get('link[rel="canonical"]')` | Tìm thẻ `<link>` có `rel="canonical"` — địa chỉ "chính thức" của trang. |
| `.should('have.attr', 'href', 'https://duck.ai/')` | Viết gọn: kiểm tra thuộc tính `href` **bằng đúng** `https://duck.ai/` (truyền 3 tham số thay vì dùng `.and`). |

### TC12 – Thẻ og:title

```js
it('TC12 - Thẻ og:title có giá trị "Duck.ai"', () => {
  cy.get('meta[property="og:title"]').should('have.attr', 'content', 'Duck.ai')
})
```

| Dòng | Giải thích |
|---|---|
| `cy.get('meta[property="og:title"]')` | Tìm thẻ Open Graph — tiêu đề hiện ra khi chia sẻ link lên Facebook, Zalo... Lưu ý thẻ này dùng `property`, không phải `name`. |
| `.should('have.attr', 'content', 'Duck.ai')` | Kiểm tra `content` đúng bằng `Duck.ai`. |

### TC13 – Thẻ html có thuộc tính lang

```js
it('TC13 - Thẻ <html> có thuộc tính lang', () => {
  cy.get('html').should('have.attr', 'lang')
})
```

| Dòng | Giải thích |
|---|---|
| `cy.get('html')` | Tìm thẻ gốc `<html>` của trang. |
| `.should('have.attr', 'lang')` | Chỉ kiểm tra thẻ **có** thuộc tính `lang` (ngôn ngữ trang), không quan tâm giá trị. Thuộc tính này giúp trình đọc màn hình cho người khiếm thị đọc đúng ngôn ngữ. |

>  **3 cách dùng `have.attr`:**
> - `should('have.attr', 'lang')` → chỉ cần có thuộc tính
> - `should('have.attr', 'href', 'abc')` → thuộc tính phải bằng `abc`
> - `should('have.attr', 'content').and('include', 'abc')` → thuộc tính phải chứa `abc`

---

## 4. Nhóm 3 — Ô nhập câu hỏi

Ô nhập câu hỏi của Duck.ai là một thẻ `<textarea>`.

### TC14 – Ô nhập hiển thị

```js
it('TC14 - Ô nhập câu hỏi hiển thị', () => {
  cy.get('textarea').should('be.visible')
})
```

| Dòng | Giải thích |
|---|---|
| `cy.get('textarea')` | Tìm thẻ `<textarea>` (ô nhập nhiều dòng). Cypress tự động chờ (tối đa 10 giây theo config) đến khi tìm thấy. |
| `.should('be.visible')` | Kiểm tra ô nhập đang hiện trên màn hình. |

### TC15 – Gõ chữ vào ô nhập

```js
it('TC15 - Gõ chữ vào ô nhập', () => {
  cy.get('textarea').type('Xin chào')
  cy.get('textarea').should('have.value', 'Xin chào')
})
```

| Dòng | Giải thích |
|---|---|
| `cy.get('textarea').type('Xin chào')` | Tìm ô nhập rồi **gõ** chữ `Xin chào`, giống người dùng gõ bàn phím từng ký tự. |
| `cy.get('textarea').should('have.value', 'Xin chào')` | Kiểm tra **giá trị** trong ô đúng bằng `Xin chào`. Với ô nhập, dùng `have.value` chứ không dùng `have.text`. |

### TC16 – Xóa nội dung trong ô nhập

```js
it('TC16 - Xóa nội dung trong ô nhập', () => {
  cy.get('textarea').type('abc')
  cy.get('textarea').clear()
  cy.get('textarea').should('have.value', '')
})
```

| Dòng | Giải thích |
|---|---|
| `cy.get('textarea').type('abc')` | Gõ `abc` vào ô. |
| `cy.get('textarea').clear()` | **Xóa sạch** nội dung trong ô. |
| `cy.get('textarea').should('have.value', '')` | Kiểm tra ô đã trống (giá trị là chuỗi rỗng `''`). |

### TC17 – Ô nhập có placeholder

```js
it('TC17 - Ô nhập có placeholder (chữ gợi ý)', () => {
  cy.get('textarea').should('have.attr', 'placeholder')
})
```

| Dòng | Giải thích |
|---|---|
| `cy.get('textarea').should('have.attr', 'placeholder')` | Placeholder là dòng chữ mờ gợi ý trong ô khi chưa gõ gì. Test kiểm tra ô có thuộc tính này. Bài tập: mở DevTools (F12), xem placeholder thật là gì, rồi viết thêm test kiểm tra đúng nội dung đó. |

### TC18 – Click vào ô thì ô được focus

```js
it('TC18 - Click vào ô nhập thì ô được focus', () => {
  cy.get('textarea').click()
  cy.get('textarea').should('have.focus')
})
```

| Dòng | Giải thích |
|---|---|
| `cy.get('textarea').click()` | **Click** chuột vào ô nhập. |
| `cy.get('textarea').should('have.focus')` | Kiểm tra ô đang được **focus** (con trỏ nhấp nháy trong ô, sẵn sàng gõ). |

---

## 5. Nhóm 4 — Giao diện & màn hình

### TC19 – Hiển thị tốt trên điện thoại

```js
it('TC19 - Trang hiển thị tốt trên điện thoại', () => {
  cy.viewport('iphone-x')
  cy.visit('https://duck.ai')
  cy.get('textarea').should('be.visible')
})
```

| Dòng | Giải thích |
|---|---|
| `cy.viewport('iphone-x')` | Đổi kích thước màn hình giả lập thành iPhone X (375×812). Có thể dùng số: `cy.viewport(375, 812)`. |
| `cy.visit('https://duck.ai')` | Mở lại trang để trang tải theo kích thước mới (`beforeEach` đã mở trang ở kích thước máy tính). |
| `cy.get('textarea').should('be.visible')` | Kiểm tra trên điện thoại vẫn thấy ô nhập. |

### TC20 – Trang có ít nhất 1 nút bấm

```js
it('TC20 - Trang có ít nhất 1 nút bấm', () => {
  cy.get('button').should('have.length.greaterThan', 0)
})
```

| Dòng | Giải thích |
|---|---|
| `cy.get('button')` | Tìm **tất cả** thẻ `<button>` trên trang (có thể ra nhiều phần tử). |
| `.should('have.length.greaterThan', 0)` | Kiểm tra **số lượng** nút lớn hơn 0. Biến thể khác: `have.length`, `have.length.lessThan`. |

---

## 6. Chạy test

```bash
npx cypress open
```
→ chọn **E2E Testing** → chọn trình duyệt → click file `duck_ai_basic.cy.js`.

Hoặc chạy không giao diện:

```bash
npx cypress run --spec cypress/e2e/duck_ai_basic.cy.js
```

| Lệnh | Giải thích |
|---|---|
| `npx cypress open` | Chạy có giao diện, xem trực tiếp từng bước — phù hợp khi học. |
| `npx cypress run --spec ...` | Chạy ngầm trong terminal, chỉ chạy file được chỉ định bởi `--spec`. |

---

## 7. Lỗi thường gặp

| Hiện tượng | Nguyên nhân & cách sửa |
|---|---|
| TC14–TC19 fail: `Expected to find element: textarea` | Lần đầu vào, Duck.ai có thể hiện popup giới thiệu che ô nhập. Mở trang bằng tay, xem chữ trên nút (ví dụ "Get Started", "Agree"), rồi thêm vào `beforeEach` sau `cy.visit`: `cy.contains('button', 'Tên nút').click()` |
| Test fail vì lỗi JavaScript của trang | Kiểm tra đã có dòng `Cypress.on('uncaught:exception', () => false)` ở đầu file. |
| Test chạy chậm / timeout | Mạng chậm. Tăng `defaultCommandTimeout` trong `cypress.config.js`. |
| `have.value` fail dù đã gõ đúng | Kiểm tra có dấu cách thừa, hoặc tiếng Việt có dấu bị gõ sai. |

---

## 8. Tóm tắt lệnh đã học

| Lệnh | Tác dụng |
|---|---|
| `cy.visit(url)` | Mở trang |
| `cy.get(selector)` | Tìm phần tử |
| `cy.url()` | Lấy URL |
| `cy.location('protocol' / 'hostname' / 'pathname')` | Lấy từng phần của URL |
| `cy.title()` | Lấy tiêu đề trang |
| `.type(text)` | Gõ chữ |
| `.clear()` | Xóa chữ |
| `.click()` | Click |
| `cy.viewport(...)` | Đổi kích thước màn hình |
| `.should(...)` / `.and(...)` | Kiểm tra |

| Điều kiện kiểm tra | Ý nghĩa |
|---|---|
| `be.visible` | Đang hiển thị |
| `exist` | Có trong HTML |
| `eq` | Bằng chính xác |
| `include` | Có chứa |
| `have.attr` | Có thuộc tính |
| `have.value` | Giá trị ô nhập |
| `have.focus` | Đang được focus |
| `have.length.greaterThan` | Số lượng lớn hơn |
