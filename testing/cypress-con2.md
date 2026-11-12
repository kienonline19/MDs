# Tuần 8 – Cypress trung cấp (1)

> **Mục tiêu**
> 1. Viết **custom command** `cy.login()` và dùng **Page Object**.
> 2. Dùng `cy.intercept` (theo dõi, giả lập request) và `cy.request` (gọi API trực tiếp).
>
> **Trang thực hành**
> - Đăng nhập: https://the-internet.herokuapp.com/login (tài khoản `tomsmith` / `SuperSecretPassword!`). Duck.ai không có chức năng đăng nhập nên dùng trang này.
> - `cy.intercept`: https://duck.ai
> - `cy.request`: https://jsonplaceholder.typicode.com (API giả, miễn phí). API chat của duck.ai cần mã bảo mật nên không gọi trực tiếp được.

---

## 0. Cấu trúc thư mục

```
cypress/
├── e2e/
│   ├── week8_login.cy.js     ← Phần 1, 2
│   └── week8_api.cy.js       ← Phần 3, 4
├── pages/
│   └── LoginPage.js          ← Page Object (tự tạo thư mục này)
└── support/
    ├── commands.js           ← Custom command
    └── e2e.js                ← có sẵn dòng: import './commands'
```

> Mở `cypress/support/e2e.js`, kiểm tra có dòng `import './commands'`. Thiếu dòng này thì Cypress không biết `cy.login()`.

---

## Phần 1 — Custom command `cy.login()`

**Vấn đề:** Test nào cũng phải đăng nhập, lặp lại 4 dòng giống nhau. **Giải pháp:** gói 4 dòng đó thành **một lệnh mới** `cy.login()`.

### `cypress/support/commands.js`

```js
Cypress.Commands.add('login', (username = 'tomsmith', password = 'SuperSecretPassword!') => {
  cy.visit('https://the-internet.herokuapp.com/login')
  cy.get('#username').type(username)
  cy.get('#password').type(password, { log: false })
  cy.get('button[type="submit"]').click()
})
```

| Dòng | Giải thích |
|---|---|
| `Cypress.Commands.add('login', ...)` | Tạo lệnh mới tên `login`. Sau đó gọi bằng `cy.login()`. |
| `username = 'tomsmith'` | **Giá trị mặc định.** Gọi `cy.login()` không truyền gì thì dùng tài khoản đúng. |
| `{ log: false }` | Không in mật khẩu ra cột lệnh của Cypress. |

### Dùng trong test (`week8_login.cy.js`)

```js
it('L01 - Đăng nhập đúng bằng cy.login()', () => {
  cy.login()

  cy.url().should('include', '/secure')
  cy.get('#flash').should('contain', 'You logged into a secure area!')
})

it('L02 - Đăng nhập sai bằng cy.login()', () => {
  cy.login('wronguser', 'wrongpass')

  cy.url().should('include', '/login')
  cy.get('#flash').should('contain', 'Your username is invalid!')
})

it('L03 - Đăng nhập rồi đăng xuất', () => {
  cy.login()
  cy.get('a[href="/logout"]').click()

  cy.url().should('include', '/login')
  cy.get('#flash').should('contain', 'You logged out of the secure area!')
})
```

| Dòng | Giải thích |
|---|---|
| `cy.login()` | Một dòng thay cho 4 dòng đăng nhập. |
| `cy.login('wronguser', 'wrongpass')` | Truyền tài khoản khác để test trường hợp sai. |
| `#flash` | Khung thông báo màu xanh/đỏ của trang sau khi đăng nhập. |

---

## Phần 2 — Page Object

**Vấn đề:** Selector `#username`, `#password`… nằm rải rác trong nhiều test. Trang đổi giao diện thì phải sửa khắp nơi. **Giải pháp:** gom selector và thao tác của **một trang** vào **một file**.

### `cypress/pages/LoginPage.js`

```js
class LoginPage {
  visit() {
    cy.visit('https://the-internet.herokuapp.com/login')
  }

  typeUsername(username) {
    cy.get('#username').type(username)
  }

  typePassword(password) {
    cy.get('#password').type(password)
  }

  submit() {
    cy.get('button[type="submit"]').click()
  }

  message() {
    return cy.get('#flash')
  }
}

export default new LoginPage()
```

| Dòng | Giải thích |
|---|---|
| `class LoginPage { ... }` | Một "khuôn" mô tả trang đăng nhập. Mỗi hàm là một thao tác trên trang. |
| `message() { return cy.get('#flash') }` | Có `return` để viết tiếp `.should(...)` trong test. |
| `export default new LoginPage()` | Tạo sẵn một đối tượng và xuất ra để file test dùng. |

### Dùng trong test

```js
import loginPage from '../pages/LoginPage'

describe('Tuần 8 - Page Object LoginPage', () => {
  beforeEach(() => {
    loginPage.visit()
  })

  it('L04 - Đăng nhập đúng bằng Page Object', () => {
    loginPage.typeUsername('tomsmith')
    loginPage.typePassword('SuperSecretPassword!')
    loginPage.submit()

    loginPage.message().should('contain', 'You logged into a secure area!')
  })

  it('L05 - Sai mật khẩu bằng Page Object', () => {
    loginPage.typeUsername('tomsmith')
    loginPage.typePassword('123456')
    loginPage.submit()

    loginPage.message().should('contain', 'Your password is invalid!')
  })
})
```

| Dòng | Giải thích |
|---|---|
| `import loginPage from '../pages/LoginPage'` | Lấy Page Object vào file test. `../` là lùi ra một thư mục (từ `e2e` ra `cypress`). |
| `loginPage.typeUsername('tomsmith')` | Đọc như câu tiếng Anh, không thấy selector nào trong test. |

### So sánh nhanh

| | Custom command | Page Object |
|---|---|---|
| Viết ở đâu | `support/commands.js` | `pages/TênTrang.js` |
| Gọi thế nào | `cy.login()` | `loginPage.submit()` |
| Hợp với | Việc lặp lại ở **nhiều trang** (đăng nhập, xóa dữ liệu) | Mọi thao tác trên **một trang** |

---

## Phần 3 — `cy.intercept` trên duck.ai

`cy.intercept` **đứng giữa** trình duyệt và máy chủ. Nó làm được 2 việc:

- **Theo dõi** request: xem trang gửi gì, nhận gì.
- **Giả lập** câu trả lời: không cần máy chủ thật.

### I01 – Theo dõi request

```js
it('I01 - Theo dõi request khi mở trang', () => {
  cy.intercept('GET', '**/duckchat/v1/status').as('status')

  cy.visit('https://duck.ai')

  cy.wait('@status').its('response.statusCode').should('eq', 200)
})
```

| Dòng | Giải thích |
|---|---|
| `cy.intercept('GET', '**/duckchat/v1/status')` | Theo dõi request GET tới địa chỉ này. Không truyền câu trả lời nên request vẫn đi tới máy chủ thật. `**` khớp mọi phần phía trước. |
| `.as('status')` | Đặt tên gọi tắt. **Phải khai báo trước** `cy.visit`. |
| `cy.wait('@status')` | Chờ request đó xảy ra. |
| `.its('response.statusCode')` | Lấy mã trạng thái máy chủ trả về. `200` = thành công. |

### I02 – Giả lập câu trả lời của AI

```js
it('I02 - Giả lập câu trả lời của AI', () => {
  cy.intercept('POST', '**/duckchat/v1/chat', {
    statusCode: 200,
    headers: { 'content-type': 'text/event-stream' },
    body:
      'data: {"action":"success","role":"assistant","message":"Xin chào từ Cypress!","created":1,"id":"stub","model":"gpt-6-luna"}\n\n' +
      'data: [DONE]\n\n',
  }).as('chat')

  cy.visit('https://duck.ai', {
    onBeforeLoad(win) {
      win.localStorage.setItem('duckaiHasAgreedToTerms', 'true')
      win.localStorage.setItem('duckaiSurveyDismissed', 'true')
    },
  })
  cy.get('textarea[name="user-prompt"]').type('Hello{enter}')

  cy.wait('@chat').its('request.body.messages.0.content.0.text').should('eq', 'Hello')
  cy.contains('Xin chào từ Cypress!').should('be.visible')
})
```

| Dòng | Giải thích |
|---|---|
| Tham số thứ 3 `{ statusCode, headers, body }` | Có tham số này thì Cypress **không gửi** request tới máy chủ mà tự trả lời. |
| `body: 'data: {...}\n\ndata: [DONE]\n\n'` | Duck.ai nhận câu trả lời theo dạng stream: từng dòng `data:`, kết thúc bằng `[DONE]`. |
| `onBeforeLoad` + `localStorage` | Giả làm người đã đồng ý điều khoản và tắt banner khảo sát, để gõ Enter là gửi ngay. |
| `its('request.body...')` | Kiểm tra **câu hỏi** trang đã gửi đi. |
| `cy.contains('Xin chào từ Cypress!')` | Kiểm tra trang hiển thị câu trả lời giả. |

---

## Phần 4 — `cy.request`: gọi API trực tiếp

`cy.request` gửi request **không qua giao diện**, giống Postman. Nhanh, dùng để test API hoặc chuẩn bị dữ liệu.

```js
const API = 'https://jsonplaceholder.typicode.com'

it('R01 - GET một bài viết', () => {
  cy.request(`${API}/posts/1`).then((res) => {
    expect(res.status).to.eq(200)
    expect(res.body.id).to.eq(1)
    expect(res.body).to.have.property('title')
  })
})

it('R02 - GET danh sách bài viết', () => {
  cy.request(`${API}/posts`).its('body').should('have.length', 100)
})

it('R03 - POST tạo bài viết mới', () => {
  cy.request('POST', `${API}/posts`, { title: 'Học Cypress', body: 'Tuần 8', userId: 1 }).then((res) => {
    expect(res.status).to.eq(201)
    expect(res.body.title).to.eq('Học Cypress')
    expect(res.body).to.have.property('id')
  })
})

it('R04 - GET bài không tồn tại trả về 404', () => {
  cy.request({ url: `${API}/posts/99999`, failOnStatusCode: false }).its('status').should('eq', 404)
})
```

| Dòng | Giải thích |
|---|---|
| `cy.request(url)` | Mặc định là `GET`. |
| `.then((res) => {...})` | `res` là câu trả lời: `res.status` (mã trạng thái), `res.body` (dữ liệu). |
| `to.have.property('title')` | Dữ liệu **có** trường `title`. |
| `.its('body').should('have.length', 100)` | Viết gọn: lấy `body` rồi kiểm tra có 100 phần tử. |
| `cy.request('POST', url, {...})` | Gửi `POST` kèm dữ liệu. `201` = đã tạo mới. JSONPlaceholder là API giả nên dữ liệu không được lưu thật. |
| `failOnStatusCode: false` | Mặc định, mã 4xx/5xx làm test fail ngay. Tắt đi để **tự kiểm tra** lỗi 404. |

### `cy.intercept` khác `cy.request` thế nào?

| | `cy.intercept` | `cy.request` |
|---|---|---|
| Ai gửi request | **Trang web** gửi | **Cypress** tự gửi |
| Có cần giao diện | Có | Không |
| Dùng để | Theo dõi / giả lập request của trang | Test API, tạo dữ liệu nhanh |

---

## Chạy test

```bash
npx cypress open
npx cypress run --spec "cypress/e2e/week8_*.cy.js"
```

---

## Bài tập

1. **BT1:** Viết custom command `cy.openDuckAi()` mở duck.ai ở trạng thái đã đồng ý điều khoản (gói phần `cy.visit` + `onBeforeLoad` của I02), rồi viết lại I02 dùng lệnh mới.
2. **BT2:** Viết Page Object `DuckAiPage` có các hàm `visit()`, `ask(text)`, `lastAnswer()`.
3. **BT3:** Dùng `cy.intercept` trả về `{ forceNetworkError: true }` cho API chat, kiểm tra duck.ai hiện thông báo lỗi `[role="alert"]`.
4. **BT4:** Dùng `cy.request` gọi `GET ${API}/users`, kiểm tra có 10 người và người đầu tiên có trường `email`.
5. **BT5 (nâng cao):** Đăng nhập **không qua giao diện**:

   ```js
   cy.request({
     method: 'POST',
     url: 'https://the-internet.herokuapp.com/authenticate',
     form: true,
     body: { username: 'tomsmith', password: 'SuperSecretPassword!' },
   })
   cy.visit('https://the-internet.herokuapp.com/secure')
   ```

   Kiểm tra trang `/secure` hiện nút Logout. So sánh tốc độ với `cy.login()`.
