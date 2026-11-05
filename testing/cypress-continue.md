# Thực hành Cypress: 18 workflow cho Duck.ai

> **Đối tượng:** học viên đã làm xong bài 20 test case cơ bản
> **Trang thực hành:** https://duck.ai
> **Workflow là gì?** Một test mô phỏng **cả một hành trình** của người dùng qua nhiều bước, ví dụ "hỏi → nhận trả lời → mở chat mới → quay lại chat cũ", thay vì chỉ kiểm tra một chi tiết.
> **Kiến thức mới:** `cy.intercept` (chặn và giả lập API), alias `@`, `cy.wait('@alias')`, `.then()`, `.within()`, `.its()`, `.invoke()`, `onBeforeLoad`, hàm tiện ích dùng lại, nhiều khối `describe`.

---

## Mục lục

| Nhóm | Workflow | Nội dung |
|---|---|---|
| A. Hội thoại | WF01–WF08 | Hỏi đáp, xuống dòng, 2 lượt, tiêu đề chat, mất mạng, thử lại, dừng, gợi ý |
| B. Nút điều khiển | WF09–WF11 | Đổi model, chế độ Reasoning, Web Search |
| C. Thanh bên | WF12–WF16 | New Chat, tìm kiếm, đổi tên, ghim, xóa |
| D. Cài đặt | WF17 | Hộp thoại Settings |
| E. Người dùng mới | WF18 | Nút Ask và dòng điều khoản |

---

## 0. Chuẩn bị

### Cấu hình `cypress.config.js`

```js
const { defineConfig } = require('cypress')

module.exports = defineConfig({
  e2e: {
    defaultCommandTimeout: 10000,
    viewportWidth: 1280,
    viewportHeight: 800,
  },
})
```

| Dòng | Giải thích |
|---|---|
| `defaultCommandTimeout: 10000` | Mỗi lệnh chờ tối đa 10 giây (mặc định chỉ 4 giây). |
| `viewportWidth` / `viewportHeight` | Màn hình 1280×800. Khi màn hình **≤ 900px**, Duck.ai chuyển sang giao diện điện thoại và ẩn thanh bên. Hàm `openDuckAi` cũng tự đặt kích thước này, nên test vẫn đúng dù quên sửa config. |

Tạo file `cypress/e2e/duck_ai_workflows.cy.js` và chép code ở các mục bên dưới vào (hoặc dùng luôn file `.cy.js` đi kèm).

### Vì sao phải dùng câu trả lời giả?

Nếu test gửi câu hỏi **thật** tới AI thì sẽ gặp 4 vấn đề:

1. **Chậm:** mỗi câu trả lời mất vài giây.
2. **Không ổn định:** AI trả lời mỗi lần một khác, nên không viết được `should('contain', ...)`.
3. **Bị giới hạn:** gửi nhiều quá sẽ bị chặn.
4. **Không test được lỗi:** không thể bắt Duck.ai "mất mạng" theo ý mình.

Giải pháp là dùng `cy.intercept` để **chặn request** gửi tới `/duckchat/v1/chat` và **tự trả về câu trả lời giả**. Giao diện vẫn là Duck.ai thật, chỉ phần máy chủ AI là bị thay. Không câu hỏi nào trong bài này được gửi tới AI.

```
Trình duyệt (Duck.ai thật) ──POST /duckchat/v1/chat──X  Máy chủ AI
                                     │
                                     └──► cy.intercept trả về câu trả lời giả
```

### Bản đồ selector của Duck.ai

| Thành phần | Selector | Ghi chú |
|---|---|---|
| Ô nhập câu hỏi | `textarea[name="user-prompt"]` | Trang chủ: placeholder `Ask anything privately`. Trong chat: `Reply...` |
| Nút gửi | `[data-testid="duckai-chat-input"] button[type="submit"]` | Tên `Ask` **chỉ** khi người dùng chưa đồng ý điều khoản và ở trang chủ. Còn lại: `Send` |
| Nút dừng | `button[aria-label="Stop generating"]` | Chỉ bật khi AI đang trả lời |
| Tin nhắn người dùng | `[data-testid="user-message"]` | |
| Tin nhắn AI | `[id*="-assistant-message-"]:not([id^="heading-"])` | Không có data-testid nên lọc theo id |
| Dòng điều khoản dưới ô nhập | `[data-testid="duckai-tos-inline-disclaimer"]` | Chỉ hiện với người chưa đồng ý điều khoản |
| Thanh bên | `[data-testid="duckai-sidebar"]` | Danh sách chat: `[data-testid="ChatsList"]` |
| Một chat trong thanh bên | `[data-testid="ChatsList"] [title="Tên chat"]` | Bên trong có nút `menu` (⋯) và `Delete chat` |
| Chọn model | `[data-testid="model-picker-button"]` | Menu `aria-label="Choose a model"` |
| Chế độ trả lời | `[data-testid="duckai-reasoning-button"]` | Menu có 2 lựa chọn: `Reasoning`, `Fast` |
| Tools | `[data-testid="duckai-tools-button"]` | Menu `aria-label="Tools menu"` |
| API chat | `POST /duckchat/v1/chat` | Body JSON có `model`, `messages`, `reasoningEffort` |

>  **Thứ tự ưu tiên khi chọn selector:** `data-testid` → `aria-label` → `name` → chữ hiển thị. **Tránh** class kiểu `Pjdc_gGEjnjd_NraQ4DV`, vì chúng đổi mỗi lần Duck.ai cập nhật.

---

## 1. Phần dùng chung: hằng số và hàm tiện ích

```js
// Bỏ qua lỗi JavaScript của chính trang duck.ai (không phải lỗi của test)
Cypress.on('uncaught:exception', () => false)

// ===== 1. Hằng số & selector dùng chung =====

const URL = 'https://duck.ai'
const CHAT_API = '**/duckchat/v1/chat'
const FATAL_ERROR = 'Oops! Something went wrong'

const SEL = {
  input: 'textarea[name="user-prompt"]',
  submit: '[data-testid="duckai-chat-input"] button[type="submit"]',
  stop: 'button[aria-label="Stop generating"]',
  userMsg: '[data-testid="user-message"]',
  aiMsg: '[id*="-assistant-message-"]:not([id^="heading-"])',
  sidebar: '[data-testid="duckai-sidebar"]',
  chatList: '[data-testid="ChatsList"]',
  modelBtn: '[data-testid="model-picker-button"]',
  reasoningBtn: '[data-testid="duckai-reasoning-button"]',
  toolsBtn: '[data-testid="duckai-tools-button"]',
  disclaimer: '[data-testid="duckai-tos-inline-disclaimer"]',
}

// ===== 2. Hàm tiện ích =====

// Tạo mã ngắn để tên chat không trùng nhau
const uid = () => Date.now().toString().slice(-6)

// Tạo câu trả lời giả theo định dạng stream (SSE) mà duck.ai dùng
function sseResponse(parts, title, model = 'gpt-6-luna') {
  let body = ''
  if (title) {
    body += `data: [CHAT_TITLE:${title}]\n\n`
  }
  parts.forEach((text) => {
    const frame = { action: 'success', role: 'assistant', message: text, created: 1, id: 'stub', model }
    body += `data: ${JSON.stringify(frame)}\n\n`
  })
  body += 'data: [DONE]\n\n'
  return {
    statusCode: 200,
    headers: { 'content-type': 'text/event-stream' },
    body,
  }
}

// Chặn request gửi chat và trả về câu trả lời giả
function stubChat(parts, title) {
  cy.intercept('POST', CHAT_API, (req) => {
    req.reply(sseResponse(parts, title, req.body.model))
  }).as('chat')
}

// Kiểm tra duck.ai không bị sập (màn hình "Oops! Something went wrong")
function expectNoCrash() {
  cy.contains(FATAL_ERROR).should('not.exist')
}

// Mở duck.ai ở trạng thái sạch và ổn định
// agreed = true  → người dùng đã đồng ý điều khoản
// agreed = false → người dùng mới, chưa đồng ý
function openDuckAi({ agreed = true } = {}) {
  cy.viewport(1280, 800)
  cy.visit(URL, {
    onBeforeLoad(win) {
      // Xóa lịch sử chat cũ → mỗi test bắt đầu với danh sách chat trống
      win.indexedDB.deleteDatabase('savedAIChatData')

      // Tắt banner khảo sát, popup hướng dẫn và quảng cáo
      win.localStorage.setItem('duckaiSurveyDismissed', 'true')
      win.localStorage.setItem('duckaiChatLimitIncreaseSeen', 'true')
      win.localStorage.setItem(
        'duckaiProductTourChecklist',
        JSON.stringify({ version: '1', dismissed: true, howDuckAiWorksDismissed: true, recentChatsTipSeen: true }),
      )
      win.localStorage.setItem(
        'duckaiRetentionBrowserPromo',
        JSON.stringify({ dismissed: true, firstShown: true, newChatsSinceShown: 0, learnMoreChatId: null }),
      )
      win.localStorage.setItem(
        'aichatPromoDismissal',
        JSON.stringify({ promoReleaseDate: '2026-01-05', showHistory: {}, dismissedPromos: [], suppressedUntil: '2099-12-31' }),
      )

      // Đã đồng ý điều khoản hay chưa
      if (agreed) {
        win.localStorage.setItem('duckaiHasAgreedToTerms', 'true')
      } else {
        win.localStorage.removeItem('duckaiHasAgreedToTerms')
      }
    },
  })
  cy.get(SEL.input).should('be.visible')
}

// Gõ câu hỏi rồi bấm nút gửi
function ask(text) {
  cy.get(SEL.input).type(text)
  cy.get(SEL.submit).should('be.enabled').click()
}

// Tìm một chat trong thanh bên theo tiêu đề
function chatItem(title) {
  return cy.get(`${SEL.chatList} [title="${title}"]`)
}

// Tạo nhanh một chat có tiêu đề cho trước
function createChat(title) {
  stubChat(['Câu trả lời mẫu'], title)
  ask('Tao chat mau')
  cy.wait('@chat')
  chatItem(title).should('be.visible')
}

// Mở menu "..." của một chat trong thanh bên
// (chờ còn đúng 1 ô chat có tên này, vì hiệu ứng ghim có thể tạm hiện 2 ô)
function openChatMenu(title) {
  chatItem(title)
    .should('have.length', 1)
    .within(() => {
      cy.get('button[aria-label="menu"]').click({ force: true })
    })
}
```

| Dòng / Hàm | Giải thích |
|---|---|
| `Cypress.on('uncaught:exception', () => false)` | Bỏ qua lỗi JavaScript của chính trang Duck.ai, để test không fail vì lỗi không phải của mình. |
| `URL`, `CHAT_API`, `FATAL_ERROR` | Gom địa chỉ và chữ cố định vào hằng số, khi đổi chỉ sửa một chỗ. `**` trong `'**/duckchat/v1/chat'` khớp với bất kỳ tên miền nào phía trước. |
| `const SEL = {...}` | Gom mọi selector vào một object. Trong test viết `SEL.input` thay vì cả chuỗi dài. Khi Duck.ai đổi giao diện, chỉ cần sửa ở đây. |
| `uid()` | Lấy 6 số cuối của thời gian hiện tại, để mỗi tên chat là duy nhất. |
| `sseResponse(parts, title, model)` | Tạo câu trả lời giả. Duck.ai nhận câu trả lời dạng **stream**: từng dòng `data: {...}`, kết thúc bằng `data: [DONE]`. `parts` là mảng các đoạn chữ, Duck.ai tự ghép lại. `title` (không bắt buộc) tạo dòng `[CHAT_TITLE:...]` để đặt tên chat. `model = 'gpt-6-luna'` là giá trị **mặc định**, dùng khi không truyền tham số. |
| `headers: { 'content-type': 'text/event-stream' }` | Báo cho trình duyệt đây là stream. Thiếu dòng này, Duck.ai sẽ báo lỗi. |
| `cy.intercept('POST', CHAT_API, (req) => {...})` | Chặn mọi request POST tới API chat. Truyền **hàm** để đọc được `req.body.model` (model mà trang đang dùng) rồi trả lời bằng đúng model đó. |
| `req.reply(...)` | Trả câu trả lời giả cho request vừa chặn. |
| `.as('chat')` | Đặt **tên gọi tắt** (alias) cho request. Sau đó dùng `cy.wait('@chat')` để chờ, hoặc `cy.get('@chat.all')` để đếm số lần gọi. |
| `expectNoCrash()` | Kiểm tra trang **không** hiện "Oops! Something went wrong" (màn hình Duck.ai bị sập). |
| `cy.viewport(1280, 800)` | Cố định kích thước màn hình. |
| `cy.visit(URL, { onBeforeLoad(win) {...} })` | `onBeforeLoad` chạy **trước** khi code của trang chạy. Mọi thứ ghi vào `localStorage` ở đây có hiệu lực ngay khi trang khởi động. |
| `win.indexedDB.deleteDatabase('savedAIChatData')` | Xóa cơ sở dữ liệu chứa lịch sử chat, để mỗi test bắt đầu với danh sách chat trống. Chỉ ảnh hưởng trình duyệt của Cypress, không đụng tới Chrome bạn dùng hằng ngày. |
| `duckaiSurveyDismissed`, `duckaiChatLimitIncreaseSeen`, `duckaiProductTourChecklist`, `duckaiRetentionBrowserPromo`, `aichatPromoDismissal` | Đánh dấu "đã xem" cho banner khảo sát, popup giới hạn chat, phần hướng dẫn, quảng cáo trình duyệt và thẻ quảng cáo. Nếu không tắt, chúng có thể **che nút** khiến Cypress không click được. `JSON.stringify` đổi object thành chuỗi, vì `localStorage` chỉ lưu chuỗi. |
| `duckaiHasAgreedToTerms` | `agreed: true` thì ghi cờ "đã đồng ý điều khoản". `agreed: false` thì xóa cờ để giả làm người dùng mới. |
| `ask(text)` | Gõ câu hỏi, chờ nút gửi bật lên rồi bấm. |
| `chatItem(title)` | Trả về ô chat có tiêu đề `title` trong thanh bên. Có `return` nên viết tiếp được: `chatItem(t).should(...)`. |
| `createChat(title)` | Tạo nhanh một chat có tên cho trước. Dùng ở WF13–WF16. |
| `openChatMenu(title)` | Mở menu ⋯ của một chat. `.should('have.length', 1)` chờ tới khi còn đúng 1 ô chat có tên đó rồi mới `.within()`. `{ force: true }` cho phép click cả khi nút chỉ hiện lúc rê chuột. |

>  Cypress tự xóa `localStorage`, cookie và `sessionStorage` trước mỗi test, nhưng **không xóa IndexedDB**. Duck.ai lưu lịch sử chat trong IndexedDB, nên ta phải tự xóa trong `onBeforeLoad`. `cy.reload()` **không** chạy lại `onBeforeLoad`, nên chat tạo trong cùng một test vẫn còn sau khi tải lại trang (WF16 cần điều này).

### Cấu trúc file: 2 khối `describe`

```js
describe('Duck.ai - Workflow cho người dùng đã đồng ý điều khoản', () => {
  beforeEach(() => { openDuckAi() })                    // đã đồng ý
  // WF01–WF17
})

describe('Duck.ai - Workflow cho người dùng mới', () => {
  beforeEach(() => { openDuckAi({ agreed: false }) })   // chưa đồng ý
  // WF18
})
```

`beforeEach` chỉ áp dụng cho các test **bên trong** `describe` chứa nó. Muốn hai nhóm test bắt đầu ở hai trạng thái khác nhau thì tách thành hai `describe`.

---

## 2. Nhóm A — Hội thoại

### WF01 – Hỏi một câu và nhận câu trả lời

**Kịch bản:** Gõ câu hỏi → bấm gửi → Duck.ai gửi request → AI trả lời → trang chuyển sang chế độ chat.

```js
it('WF01 - Hỏi một câu và nhận câu trả lời', () => {
  const question = 'What is Cypress?'
  stubChat(['Cypress là ', 'công cụ kiểm thử web.'])

  ask(question)

  cy.wait('@chat').then(({ request }) => {
    expect(request.headers['content-type']).to.include('application/json')
    expect(request.body.messages[0].role).to.eq('user')
    expect(request.body.messages[0].content[0].text).to.eq(question)
  })

  cy.get(SEL.userMsg).should('contain', question)
  cy.get(SEL.aiMsg).should('contain', 'Cypress là công cụ kiểm thử web.')
  cy.location('search').should('include', 'chatID=')
  cy.get(SEL.submit).should('have.attr', 'aria-label', 'Send')
})
```

| Dòng | Giải thích |
|---|---|
| `stubChat([...])` | Chuẩn bị câu trả lời giả gồm 2 đoạn, giống AI đang stream từng phần. **Phải gọi trước** khi gửi câu hỏi. |
| `cy.wait('@chat').then(({ request }) => {` | Chờ Duck.ai gửi request, rồi lấy request đó ra kiểm tra. `({ request })` là cú pháp lấy riêng thuộc tính `request`. |
| `expect(...).to.include('application/json')` | `expect` là cách kiểm tra bên trong `.then()`. Request phải gửi dạng JSON. |
| `request.body.messages[0].role` | Body có mảng `messages`. Phần tử đầu là tin nhắn của người dùng (`role: 'user'`). |
| `request.body.messages[0].content[0].text` | Nội dung câu hỏi phải **đúng bằng** câu đã gõ. |
| `cy.get(SEL.aiMsg).should('contain', '...')` | Câu trả lời hiện đầy đủ, đã ghép 2 đoạn. |
| `cy.location('search').should('include', 'chatID=')` | `search` là phần `?...` của URL. Khi có chat mới, Duck.ai thêm `?chatID=...`. |
| `should('have.attr', 'aria-label', 'Send')` | Trong chat, nút gửi có tên `Send`. |

### WF02 – Shift+Enter xuống dòng, Enter để gửi

**Kịch bản:** Gõ dòng 1 → Shift+Enter → gõ dòng 2 → kiểm tra **chưa gửi** → Enter → request chứa đủ 2 dòng.

```js
it('WF02 - Shift+Enter xuống dòng, Enter để gửi', () => {
  stubChat(['Đã nhận 2 dòng.'])

  cy.get(SEL.input).type('Line 1{shift}{enter}')
  cy.get(SEL.input).type('Line 2')
  cy.get(SEL.input).should('have.value', 'Line 1\nLine 2')
  cy.get('@chat.all').should('have.length', 0)

  cy.get(SEL.input).type('{enter}')

  cy.wait('@chat').its('request.body.messages.0.content.0.text').should('eq', 'Line 1\nLine 2')
  cy.get(SEL.aiMsg).should('contain', 'Đã nhận 2 dòng.')
  cy.get(SEL.input).should('have.value', '')
})
```

| Dòng | Giải thích |
|---|---|
| `.type('Line 1{shift}{enter}')` | `{shift}` giữ phím Shift, `{enter}` bấm Enter. Shift+Enter tạo dòng mới. Hết lệnh `.type` thì Cypress tự nhả Shift. |
| `should('have.value', 'Line 1\nLine 2')` | `\n` là ký tự xuống dòng. |
| `cy.get('@chat.all').should('have.length', 0)` | `@chat.all` là **tất cả** lần request `chat` đã xảy ra. Độ dài 0 nghĩa là chưa gửi gì. |
| `.its('request.body.messages.0.content.0.text')` | `.its()` đi sâu vào object theo đường dẫn. Số `0` là phần tử đầu của mảng. |
| `should('have.value', '')` | Sau khi gửi, ô nhập được xóa trống. |

### WF03 – Hội thoại 2 lượt hỏi đáp

**Kịch bản:** Hỏi câu 1 → nhận trả lời → chờ AI trả lời xong → hỏi câu 2 → request lần 2 mang theo lịch sử → có 2 cặp hỏi–đáp trên màn hình.

```js
it('WF03 - Hội thoại 2 lượt hỏi đáp', () => {
  stubChat(['Thủ đô Việt Nam là Hà Nội.'])
  ask('Capital of Vietnam?')
  cy.wait('@chat')
  cy.get(SEL.aiMsg).should('have.length', 1).and('contain', 'Hà Nội')

  // Chờ AI trả lời xong hẳn rồi mới hỏi tiếp
  cy.get(SEL.stop).should('be.disabled')
  cy.get(SEL.input).should('have.attr', 'placeholder').and('include', 'Reply')

  stubChat(['Hà Nội có khoảng 8,5 triệu dân.'])
  ask('Population?')

  cy.wait('@chat').then(({ request }) => {
    const messages = request.body.messages
    expect(messages[messages.length - 1].content[0].text).to.eq('Population?')
    expect(messages.length).to.be.greaterThan(1)
  })

  cy.get(SEL.userMsg).should('have.length', 2)
  cy.get(SEL.aiMsg).should('have.length', 2)
  cy.get(SEL.aiMsg).last().should('contain', '8,5 triệu')
})
```

| Dòng | Giải thích |
|---|---|
| `.should('have.length', 1).and('contain', 'Hà Nội')` | Có đúng 1 tin nhắn AI và nó chứa "Hà Nội". |
| `cy.get(SEL.stop).should('be.disabled')` | Nút Stop tắt nghĩa là AI đã trả lời xong. Chờ tới lúc này mới hỏi tiếp, giống người dùng thật. |
| `should('have.attr', 'placeholder').and('include', 'Reply')` | Trong chat, chữ gợi ý đổi thành "Reply...". |
| `stubChat([...])` gọi lần 2 | Intercept khai báo **sau** được ưu tiên, nên lần hỏi thứ 2 nhận câu trả lời thứ 2. |
| `messages[messages.length - 1]` | Phần tử **cuối** của mảng là câu hỏi mới nhất. |
| `expect(messages.length).to.be.greaterThan(1)` | Request lần 2 gửi kèm lịch sử, nhờ vậy AI mới "nhớ" ngữ cảnh. |
| `.last()` | Lấy phần tử cuối trong các phần tử tìm được. |

### WF04 – AI đặt tiêu đề cho cuộc trò chuyện

**Kịch bản:** AI trả lời kèm tiêu đề → tab trình duyệt đổi tên → chat với tiêu đề đó xuất hiện trong thanh bên.

```js
it('WF04 - AI đặt tiêu đề cho cuộc trò chuyện', () => {
  const title = `Du lịch Đà Lạt ${uid()}`
  stubChat(['Đà Lạt đẹp nhất vào tháng 12.'], title)

  ask('Plan a trip to Da Lat')
  cy.wait('@chat')

  cy.title().should('eq', title)
  chatItem(title).should('be.visible').and('contain', title)
})
```

| Dòng | Giải thích |
|---|---|
| `` `Du lịch Đà Lạt ${uid()}` `` | Chuỗi trong dấu backtick `` ` `` cho phép chèn biến bằng `${...}`. |
| `stubChat([...], title)` | Tham số thứ 2 khiến câu trả lời giả có thêm dòng `[CHAT_TITLE:...]`. |
| `cy.title().should('eq', title)` | Tab trình duyệt đổi tên thành tiêu đề chat. |
| `chatItem(title).should('be.visible')` | Tìm chat **theo tên**, không theo vị trí. Chat được ghim luôn nằm trên cùng, nên "chat đầu tiên" chưa chắc là chat mới. |

### WF05 – Mất mạng thì hiện thông báo lỗi

**Kịch bản:** Giả lập mất mạng → gửi câu hỏi → hiện thông báo lỗi và nút Try Again → câu hỏi của người dùng vẫn còn.

```js
it('WF05 - Mất mạng thì hiện thông báo lỗi', () => {
  cy.intercept('POST', CHAT_API, { forceNetworkError: true }).as('chat')

  ask('Hello')

  cy.wait('@chat')
  cy.get('[role="alert"]', { timeout: 15000 })
    .should('be.visible')
    .and('contain', 'problem with your connection')
  cy.contains('button', 'Try Again').should('be.visible')
  cy.get(SEL.userMsg).should('contain', 'Hello')
})
```

| Dòng | Giải thích |
|---|---|
| `{ forceNetworkError: true }` | Cypress **cắt kết nối**, giống hệt khi mất mạng. |
| `cy.get('[role="alert"]', { timeout: 15000 })` | `role="alert"` là vùng thông báo lỗi. Chờ riêng 15 giây vì Duck.ai tự thử lại một lần trước khi báo lỗi. |
| `.and('contain', 'problem with your connection')` | Đúng nội dung lỗi mạng. |

### WF06 – Lỗi lần đầu, bấm Try Again thì thành công

**Kịch bản:** Mất mạng → hiện lỗi → mạng "có lại" → bấm Try Again → nhận câu trả lời, thông báo lỗi biến mất.

```js
it('WF06 - Lỗi lần đầu, bấm Try Again thì thành công', () => {
  let shouldFail = true
  cy.intercept('POST', CHAT_API, (req) => {
    if (shouldFail) {
      req.reply({ forceNetworkError: true })
    } else {
      req.reply(sseResponse(['Lần này thì được rồi!'], null, req.body.model))
    }
  }).as('chat')

  ask('Retry me')
  cy.get('[role="alert"]', { timeout: 15000 }).should('be.visible')

  cy.then(() => {
    shouldFail = false
  })
  cy.contains('button', 'Try Again').click()

  cy.get(SEL.aiMsg).should('contain', 'Lần này thì được rồi!')
  cy.get('[role="alert"]').should('not.exist')
})
```

| Dòng | Giải thích |
|---|---|
| `let shouldFail = true` | Biến "công tắc" quyết định request lỗi hay thành công. |
| `cy.intercept('POST', CHAT_API, (req) => {...})` | Mỗi khi có request, hàm này chạy và tự quyết định cách trả lời. |
| `cy.then(() => { shouldFail = false })` | **Quan trọng:** lệnh Cypress chạy theo hàng đợi. Nếu viết thẳng `shouldFail = false`, dòng đó chạy **ngay lập tức**, trước cả khi câu hỏi được gửi. Bọc trong `cy.then` thì nó chạy đúng lượt. |
| `cy.get('[role="alert"]').should('not.exist')` | Thông báo lỗi đã biến mất. |

### WF07 – Bấm dừng khi AI đang trả lời

**Kịch bản:** AI trả lời chậm 3 giây → trong lúc chờ, nút Stop bật → bấm Stop → câu trả lời không bao giờ hiện.

```js
it('WF07 - Bấm dừng khi AI đang trả lời', () => {
  cy.intercept('POST', CHAT_API, { ...sseResponse(['Câu trả lời đến muộn']), delay: 3000 }).as('chat')

  cy.get(SEL.stop).should('be.disabled')
  ask('Slow question')

  cy.get(SEL.stop).should('be.enabled').click()
  cy.get(SEL.stop).should('be.disabled')

  cy.wait(4000)
  cy.contains('Câu trả lời đến muộn').should('not.exist')
})
```

| Dòng | Giải thích |
|---|---|
| `{ ...sseResponse([...]), delay: 3000 }` | `...` (spread) chép mọi thuộc tính của câu trả lời giả, rồi thêm `delay: 3000` để trả lời sau 3 giây. |
| `should('be.enabled').click()` | Đang chờ AI thì nút Stop bật, bấm vào để dừng. |
| `cy.wait(4000)` | Chờ cứng 4 giây, quá mốc 3 giây. Thông thường **không nên** dùng `cy.wait(số)`, nhưng ở đây cần chờ để chứng minh câu trả lời **không** đến. |

### WF08 – Dùng gợi ý có sẵn để bắt đầu chat

**Kịch bản:** Mở tab Chat Suggestions → có 4 gợi ý → bấm mũi tên → đổi sang 4 gợi ý khác → bấm một gợi ý → Duck.ai gửi luôn câu đó.

```js
it('WF08 - Dùng gợi ý có sẵn để bắt đầu chat', () => {
  stubChat(['Đây là kế hoạch cho bạn.'])

  cy.contains('[role="tab"]', 'Chat Suggestions').click()
  cy.contains('[role="tab"]', 'Chat Suggestions').should('have.attr', 'aria-selected', 'true')
  cy.get('[role="tabpanel"] li').should('have.length', 4)

  cy.get('[role="tabpanel"] li').first().invoke('text').then((firstBefore) => {
    cy.get('button[aria-label="Show next suggestions"]').click()
    cy.get('[role="tabpanel"] li').first().should('not.have.text', firstBefore)
  })

  cy.get('[role="tabpanel"] li button').first().invoke('text').then((suggestion) => {
    cy.get('[role="tabpanel"] li button').first().click()
    cy.wait('@chat').its('request.body.messages.0.content.0.text').should('include', suggestion.trim())
  })

  cy.location('search').should('include', 'chatID=')
  cy.get(SEL.aiMsg).should('contain', 'Đây là kế hoạch cho bạn.')
})
```

| Dòng | Giải thích |
|---|---|
| `cy.contains('[role="tab"]', 'Chat Suggestions')` | Tìm phần tử `role="tab"` chứa chữ "Chat Suggestions". |
| `should('have.attr', 'aria-selected', 'true')` | Tab đang được chọn. |
| `.invoke('text').then((firstBefore) => {` | Lấy chữ của gợi ý đầu tiên, đưa vào biến `firstBefore`. |
| `should('not.have.text', firstBefore)` | Sau khi bấm "next", gợi ý đầu tiên phải khác trước. |
| `.should('include', suggestion.trim())` | Câu gửi đi **chứa** câu gợi ý. Duck.ai còn tự thêm hướng dẫn phía sau, nên dùng `include` chứ không dùng `eq`. `.trim()` bỏ dấu cách thừa ở hai đầu. |

---

## 3. Nhóm B — Các nút điều khiển

### WF09 – Đổi model, tải lại trang, model vẫn được giữ

**Kịch bản:** Ghi nhớ model hiện tại → chọn model khác → tải lại trang → vẫn là model mới → request mang đúng mã model.

```js
it('WF09 - Đổi model, tải lại trang, model vẫn được giữ', () => {
  stubChat(['Xin chào từ model mới.'])

  cy.get(SEL.modelBtn).invoke('text').then((oldText) => {
    cy.get(SEL.modelBtn).click()
    cy.get(SEL.modelBtn).should('have.attr', 'aria-expanded', 'true')

    cy.get('[role="menu"][aria-label="Choose a model"] [role="menuitemradio"][aria-checked="false"]')
      .first()
      .invoke('attr', 'data-testid')
      .then((rowId) => {
        const modelId = rowId.replace('model-picker-row-', '')

        cy.get(`[data-testid="${rowId}"]`).click()
        cy.get(SEL.modelBtn).should('not.have.text', oldText)

        cy.reload()
        cy.get(SEL.modelBtn).should('not.have.text', oldText)

        ask('Which model are you?')
        cy.wait('@chat').its('request.body.model').should('eq', modelId)
      })
  })
})
```

| Dòng | Giải thích |
|---|---|
| `.invoke('text').then((oldText) => {` | Lưu tên model hiện tại. **Không** viết cứng tên model, vì Duck.ai thay model thường xuyên. |
| `should('have.attr', 'aria-expanded', 'true')` | `aria-expanded="true"` nghĩa là menu đang mở. |
| `[role="menuitemradio"][aria-checked="false"]` | Các lựa chọn **chưa được chọn**. Hai điều kiện viết liền nhau nghĩa là phải thỏa cả hai. |
| `.invoke('attr', 'data-testid')` | Lấy `data-testid`, ví dụ `model-picker-row-gpt-5.4-mini`. |
| `rowId.replace('model-picker-row-', '')` | Cắt phần đầu, còn lại mã model `gpt-5.4-mini`. |
| `cy.reload()` | Tải lại trang, giống bấm F5. |
| `.its('request.body.model').should('eq', modelId)` | Request gửi đi mang đúng mã model đã chọn. |

### WF10 – Chuyển sang chế độ Reasoning

**Kịch bản:** Mặc định là Fast → mở menu → chọn Reasoning → nút đổi chữ, menu đóng → request đã bật suy luận.

```js
it('WF10 - Chuyển sang chế độ Reasoning', () => {
  stubChat(['Đã suy nghĩ kỹ.'])

  cy.get(SEL.reasoningBtn).should('contain', 'Fast').click()
  cy.get('[role="menu"][aria-label="Reasoning mode"]').within(() => {
    cy.contains('[role="menuitemradio"]', 'Fast').should('have.attr', 'aria-checked', 'true')
    cy.contains('[role="menuitemradio"]', 'Reasoning').click()
  })

  cy.get(SEL.reasoningBtn).should('contain', 'Reasoning')
  cy.get(SEL.reasoningBtn).should('have.attr', 'aria-expanded', 'false')

  ask('Think carefully')
  cy.wait('@chat').its('request.body.reasoningEffort').should('not.eq', 'none')
})
```

| Dòng | Giải thích |
|---|---|
| `.should('contain', 'Fast').click()` | Kiểm tra đang ở Fast rồi click mở menu. Có thể nối `.click()` sau `.should()`. |
| `.within(() => {...})` | Mọi lệnh bên trong chỉ tìm **trong menu** này. |
| `should('have.attr', 'aria-expanded', 'false')` | Menu đã tự đóng sau khi chọn. |
| `its('request.body.reasoningEffort').should('not.eq', 'none')` | Ở chế độ Fast, `reasoningEffort` là `"none"`. Đổi sang Reasoning thì phải khác `"none"`. |

### WF11 – Bật rồi tắt Web Search trong menu Tools

**Kịch bản:** Chưa có nhãn Web Search → mở Tools → chọn Web Search → nhãn xuất hiện → bấm X trên nhãn → nhãn biến mất.

```js
it('WF11 - Bật rồi tắt Web Search trong menu Tools', () => {
  cy.get('button[aria-label="Remove Web Search"]').should('not.exist')

  cy.get(SEL.toolsBtn).click()
  cy.get(SEL.toolsBtn).should('have.attr', 'aria-expanded', 'true')
  cy.get('[role="menu"][aria-label="Tools menu"]').within(() => {
    cy.contains('[role="menuitemradio"]', 'Web Search').click()
  })

  cy.get('button[aria-label="Remove Web Search"]').should('be.visible').and('contain', 'Web Search')

  cy.get('button[aria-label="Remove Web Search"]').click()
  cy.get('button[aria-label="Remove Web Search"]').should('not.exist')
})
```

| Dòng | Giải thích |
|---|---|
| `button[aria-label="Remove Web Search"]` | Khi bật Web Search, cạnh ô nhập hiện một nhãn có nút X với aria-label này. |
| `.should('not.exist')` ở đầu | Kiểm tra trạng thái **ban đầu** trước khi thao tác. Thói quen tốt: biết chắc mình bắt đầu từ đâu. |

---

## 4. Nhóm C — Thanh bên và lịch sử chat

### WF12 – Tạo chat, bấm New Chat, rồi mở lại chat cũ

**Kịch bản:** Tạo chat → bấm New Chat → về trang chủ trống → click chat cũ → câu hỏi và câu trả lời cũ hiện lại.

```js
it('WF12 - Tạo chat, bấm New Chat, rồi mở lại chat cũ', () => {
  const title = `Chat cũ ${uid()}`
  stubChat(['Nội dung của chat cũ.'], title)
  ask('Old chat')
  cy.wait('@chat')
  cy.get(SEL.aiMsg).should('contain', 'Nội dung của chat cũ.')
  cy.location('search').should('include', 'chatID=')
  chatItem(title).should('be.visible')

  cy.contains(`${SEL.sidebar} button`, 'New Chat').click()

  cy.location('search').should('not.include', 'chatID')
  cy.get('h1').should('be.visible')
  cy.get(SEL.input).should('have.value', '')
  cy.get(SEL.submit).should('have.attr', 'aria-label', 'Send').and('be.disabled')
  cy.get(SEL.userMsg).should('not.exist')

  chatItem(title).should('have.length', 1).click()

  cy.location('search').should('include', 'chatID=')
  cy.get(SEL.userMsg).should('contain', 'Old chat')
  cy.get(SEL.aiMsg).should('contain', 'Nội dung của chat cũ.')
})
```

| Dòng | Giải thích |
|---|---|
| `` cy.contains(`${SEL.sidebar} button`, 'New Chat') `` | Chỉ tìm nút New Chat **trong thanh bên**, để chắc chắn bấm đúng nút. |
| `should('not.include', 'chatID')` | URL không còn `chatID`, nghĩa là đã về trang chủ. |
| `cy.get('h1').should('be.visible')` | Tiêu đề lớn của trang chủ hiện lại. Chỉ kiểm tra hiển thị, vì chữ bên trong thay đổi theo trạng thái ("Duck.ai, by DuckDuckGo" hoặc "All chats are private"). |
| `should('have.attr', 'aria-label', 'Send').and('be.disabled')` | Nút gửi tên "Send" (người dùng đã đồng ý điều khoản) và đang tắt (ô nhập trống). |
| `cy.get(SEL.userMsg).should('not.exist')` | Trang chủ không còn tin nhắn nào. |
| `chatItem(title).should('have.length', 1).click()` | Chắc chắn có đúng 1 chat tên đó rồi mới click. |

### WF13 – Tìm kiếm chat trong thanh bên

**Kịch bản:** Tạo chat → mở tìm kiếm → gõ một phần tên → thấy chat → gõ chữ vô nghĩa → "No results found" → đóng tìm kiếm → danh sách trở lại.

```js
it('WF13 - Tìm kiếm chat trong thanh bên', () => {
  const title = `Tim kiem ${uid()}`
  createChat(title)

  cy.get(`${SEL.sidebar} button[aria-label="Search chats"]`).click()
  cy.get('input[aria-label="Search chats"]').type(title.slice(0, 12))
  chatItem(title).should('be.visible')

  cy.get('input[aria-label="Search chats"]').clear().type('zzqqxx-khong-co')
  cy.get(SEL.chatList).should('contain', 'No results found')

  cy.get('button[aria-label="Close search"]').click()
  chatItem(title).should('be.visible')
})
```

| Dòng | Giải thích |
|---|---|
| `createChat(title)` | Dùng hàm tiện ích để có sẵn một chat. |
| `title.slice(0, 12)` | Lấy 12 ký tự đầu, để thử tìm theo **một phần** tên. |
| `.clear().type('zzqqxx-khong-co')` | Xóa ô rồi gõ chữ chắc chắn không khớp chat nào. |
| `should('contain', 'No results found')` | Duck.ai báo không tìm thấy. |

### WF14 – Đổi tên một chat

**Kịch bản:** Tạo chat → menu ⋯ → Rename → ô sửa tên hiện tên cũ → gõ tên mới + Enter → chỉ còn tên mới.

```js
it('WF14 - Đổi tên một chat', () => {
  const title = `Ten cu ${uid()}`
  const newTitle = `Ten moi ${uid()}`
  createChat(title)

  openChatMenu(title)
  cy.contains('[role^="menuitem"]', 'Rename').click()

  cy.get('input[name="edit-chat-title"]').should('have.value', title)
  cy.get('input[name="edit-chat-title"]').clear().type(`${newTitle}{enter}`)

  cy.get('input[name="edit-chat-title"]').should('not.exist')
  chatItem(newTitle).should('be.visible')
  chatItem(title).should('not.exist')
})
```

| Dòng | Giải thích |
|---|---|
| `cy.contains('[role^="menuitem"]', 'Rename')` | `^=` nghĩa là "**bắt đầu bằng**", khớp cả `menuitem` lẫn `menuitemradio`. |
| `input[name="edit-chat-title"]` | Ô sửa tên hiện ngay trong thanh bên. |
| `` .type(`${newTitle}{enter}`) `` | Gõ tên mới rồi Enter để lưu. |
| `chatItem(title).should('not.exist')` | Tên cũ không còn. |

### WF15 – Ghim rồi bỏ ghim một chat

**Kịch bản:** Tạo chat → Pin → có biểu tượng ghim → menu đổi thành "Remove Pin" → bỏ ghim → biểu tượng biến mất.

```js
it('WF15 - Ghim rồi bỏ ghim một chat', () => {
  const title = `Ghim ${uid()}`
  createChat(title)

  openChatMenu(title)
  cy.contains('[role^="menuitem"]', 'Pin').click()
  chatItem(title).should('have.length', 1)
  chatItem(title).find('[data-testid="ChatPinnedIcon"]').should('exist')

  openChatMenu(title)
  cy.contains('[role^="menuitem"]', 'Remove Pin').click()
  chatItem(title).should('have.length', 1)
  chatItem(title).find('[data-testid="ChatPinnedIcon"]').should('not.exist')
})
```

| Dòng | Giải thích |
|---|---|
| `chatItem(title).should('have.length', 1)` | Khi ghim, chat **chuyển chỗ** lên nhóm ghim. Ô cũ chạy hiệu ứng biến mất khoảng 0,2 giây, nên có lúc có 2 ô cùng tên. Dòng này chờ tới khi còn 1 ô. |
| `.find('[data-testid="ChatPinnedIcon"]')` | `.find()` tìm phần tử con **bên trong** ô chat, khác `cy.get()` tìm trên cả trang. |
| `.should('exist')` | Dùng `exist` vì icon nhỏ có thể không được tính là "visible". |

### WF16 – Xóa chat: máy tính xóa ngay, điện thoại hỏi xác nhận

**Kịch bản:**
- **Máy tính:** menu ⋯ → Delete Chat → chat **mất ngay**, không có hộp hỏi lại.
- **Điện thoại:** chuyển màn hình 375×812 → mở thanh bên → bấm biểu tượng xóa → hộp "Delete this chat?" → Cancel → chat còn → xóa lần nữa → Delete Chat → chat biến mất.

```js
it('WF16 - Xóa chat: máy tính xóa ngay, điện thoại hỏi xác nhận', () => {
  const quickTitle = `Xoa ngay ${uid()}`
  const confirmTitle = `Xoa co hoi ${uid()}`

  // Phần 1 — máy tính: xóa từ menu là mất ngay, không có hộp xác nhận
  createChat(quickTitle)
  openChatMenu(quickTitle)
  cy.contains('[role^="menuitem"]', 'Delete Chat').click()
  chatItem(quickTitle).should('not.exist')
  cy.contains('Delete this chat?').should('not.exist')

  // Phần 2 — điện thoại: bấm biểu tượng xóa thì hiện hộp "Delete this chat?"
  createChat(confirmTitle)
  cy.viewport(375, 812)
  cy.reload()
  cy.get(SEL.input).should('be.visible')
  expectNoCrash()
  cy.get('button[aria-label^="Show sidebar"]').click()

  chatItem(confirmTitle).should('have.length', 1).within(() => {
    cy.get('button[aria-label="Delete chat"]').click()
  })
  cy.contains('Delete this chat?').should('be.visible')
  cy.contains('button:visible', 'Cancel').click()
  cy.contains('Delete this chat?').should('not.exist')
  chatItem(confirmTitle).should('exist')

  chatItem(confirmTitle).within(() => {
    cy.get('button[aria-label="Delete chat"]').click()
  })
  cy.contains('Delete this chat?').should('be.visible')
  cy.contains('button:visible', 'Delete Chat').click()
  chatItem(confirmTitle).should('not.exist')
})
```

| Dòng | Giải thích |
|---|---|
| `cy.contains('Delete this chat?').should('not.exist')` | Chứng minh trên máy tính **không** có hộp xác nhận. Duck.ai chỉ hỏi lại khi màn hình ≤ 900px. |
| `cy.viewport(375, 812)` rồi `cy.reload()` | Chuyển sang kích thước điện thoại và tải lại trang để giao diện vẽ lại. |
| `expectNoCrash()` | Chắc chắn trang không bị sập sau khi tải lại. |
| `button[aria-label^="Show sidebar"]` | Trên điện thoại thanh bên ẩn, phải bấm nút này để mở. |
| `button[aria-label="Delete chat"]` | Trên điện thoại, mỗi chat có sẵn biểu tượng xóa cạnh nút ⋯. |
| `cy.contains('button:visible', 'Cancel')` | `:visible` chỉ lấy nút **đang hiển thị**. Ở ô nhập có một nút ẩn cũng tên "Cancel" (hủy đọc giọng nói), thiếu `:visible` có thể click nhầm. |

>  Với hộp xác nhận, luôn test đủ **cả hai nhánh**: Cancel (không có gì thay đổi) và Đồng ý (thay đổi thật sự).

---

## 5. Nhóm D — Cài đặt

### WF17 – Mở Settings, đổi giao diện, xem thông tin, đóng lại

**Kịch bản:** Settings & More → Settings → tab Appearance: đổi sang Dark → tab About & Legal: kiểm tra link → đóng hộp thoại.

```js
it('WF17 - Mở Settings, đổi giao diện, xem thông tin, đóng lại', () => {
  cy.get('button[aria-label="Settings & More"]').click()
  cy.get('button[aria-label="Settings & More"]').should('have.attr', 'aria-expanded', 'true')
  cy.get('[data-testid="settings-button"]').click()

  cy.get('[role="dialog"][aria-label="Duck.ai Settings"]').should('be.visible').within(() => {
    cy.get('input[role="switch"][aria-label="Chat History"]').should('be.checked')

    cy.contains('button', 'Appearance').click()
    cy.contains('button', 'System').should('have.attr', 'aria-pressed', 'true')
    cy.contains('button', 'Dark').click()
    cy.contains('button', 'Dark').should('have.attr', 'aria-pressed', 'true')
    cy.contains('button', 'System').should('have.attr', 'aria-pressed', 'false')

    cy.contains('button', 'About & Legal').click()
    cy.contains('a', 'Help Pages').should('have.attr', 'href').and('include', 'duckduckgo.com')

    cy.get('button[aria-label="close dialog"]').click()
  })

  cy.get('[role="dialog"][aria-label="Duck.ai Settings"]').should('not.exist')
})
```

| Dòng | Giải thích |
|---|---|
| `[data-testid="settings-button"]` | Mục "Settings" trong menu Settings & More. |
| `.should('be.visible').within(() => {` | Hộp thoại hiện, rồi làm mọi bước tiếp theo **bên trong** nó. |
| `input[role="switch"][aria-label="Chat History"]` | Công tắc lưu lịch sử. Bên dưới là một checkbox, nên dùng `be.checked`. |
| `aria-pressed` | Nút bật/tắt dùng `aria-pressed="true"` để báo đang được chọn. Chọn Dark thì System chuyển về `false`. |
| `should('have.attr', 'href').and('include', ...)` | Lấy `href` rồi kiểm tra có chứa tên miền. |
| `should('not.exist')` (ngoài `within`) | Kiểm tra bên ngoài `within`, vì hộp thoại đã biến mất. |

---

## 6. Nhóm E — Người dùng mới

### WF18 – Nút Ask bật/tắt theo nội dung ô nhập

**Kịch bản:** Người dùng chưa đồng ý điều khoản → ô trống thì nút Ask tắt → gõ chữ thì bật → xóa thì tắt lại → dưới ô nhập có dòng điều khoản, link đúng địa chỉ và mở tab mới.

```js
it('WF18 - Nút Ask bật/tắt theo nội dung ô nhập', () => {
  cy.get(SEL.input).should('have.attr', 'placeholder', 'Ask anything privately')
  cy.get(SEL.submit).should('have.attr', 'aria-label', 'Ask').and('be.disabled')

  cy.get(SEL.input).type('abc')
  cy.get(SEL.submit).should('be.enabled')

  cy.get(SEL.input).clear()
  cy.get(SEL.submit).should('be.disabled')

  cy.get(SEL.disclaimer).should('be.visible').and('contain', 'you agree')
  cy.get(`${SEL.disclaimer} a`)
    .should('have.attr', 'href', 'https://duckduckgo.com/duckai/privacy-terms')
    .and('have.attr', 'target', '_blank')
})
```

| Dòng | Giải thích |
|---|---|
| `openDuckAi({ agreed: false })` (trong `beforeEach`) | Mở trang ở trạng thái người dùng mới. Chỉ khi đó nút mới tên "Ask" và dòng điều khoản mới hiện. |
| `should('have.attr', 'placeholder', 'Ask anything privately')` | Đúng chữ gợi ý của ô nhập. |
| `.and('be.disabled')` / `should('be.enabled')` | Nút tắt khi ô trống, bật khi có chữ. |
| `.and('contain', 'you agree')` | Dòng "By clicking 'Ask' you agree…". |
| `` `${SEL.disclaimer} a` `` | Link nằm **bên trong** dòng điều khoản. Dấu cách giữa hai phần nghĩa là "bên trong". |
| `.and('have.attr', 'target', '_blank')` | `target="_blank"` nghĩa là mở tab mới. Cypress không theo được sang tab mới, nên chỉ kiểm tra thuộc tính, **không** click. |

---

## 7. Chạy test

```bash
npx cypress open
npx cypress run --spec cypress/e2e/duck_ai_workflows.cy.js
```

- `cypress open`: chạy có giao diện, xem từng bước. Phù hợp khi học.
- `cypress run`: chạy ngầm, in toàn bộ thông báo lỗi ra terminal và tự chụp ảnh vào `cypress/screenshots`.
- Muốn chạy riêng một workflow: đổi `it(` thành `it.only(`. Chạy xong nhớ đổi lại.

---

## 8. Những cái bẫy khi test một trang web thật

Bài này test một trang mà mình **không phải người làm ra**. Đây là những bẫy đã gặp khi viết bộ test, rất đáng để học viên biết:

| Bẫy | Ví dụ trong Duck.ai | Cách tránh |
|---|---|---|
| Trang phản ứng khác nhau **theo trạng thái người dùng** | Nút gửi tên "Ask" với người mới, "Send" với người đã đồng ý. Dòng điều khoản chỉ hiện với người mới. | Tự đặt trạng thái trong `onBeforeLoad`; tách `describe` cho từng loại người dùng. |
| Trang phản ứng khác nhau **theo kích thước màn hình** | Máy tính xóa chat ngay; điện thoại hỏi xác nhận. Màn hình ≤ 900px ẩn thanh bên. | Cố định `cy.viewport()`; test riêng cho điện thoại. |
| Popup, banner, quảng cáo **che nút** | Banner khảo sát "Help Us Improve" che nút mở thanh bên trên điện thoại. | Đọc class trong lỗi `covered by another element`, tìm ra đó là gì rồi tắt trong `openDuckAi`. |
| **Dữ liệu cũ** từ lần chạy trước | Lịch sử chat dồn lên qua mỗi lần chạy; chat ghim còn sót đẩy chat mới xuống. | Xóa IndexedDB trước mỗi test; tìm phần tử theo tên, không theo vị trí. |
| **Hiệu ứng chuyển động** | Khi ghim, có lúc có 2 ô chat cùng tên → lỗi `within() can only be called on a single element`. | Chờ `.should('have.length', 1)` trước `.within()`. |
| Kiểm tra **chữ trang trí** hay đổi | Tiêu đề `h1` lúc là "Duck.ai, by DuckDuckGo", lúc là "All chats are private". | Kiểm tra **hành vi** (URL, ô nhập trống, nút tắt) thay vì chữ trang trí. |
| Một lỗi **che** lỗi tiếp theo | Sửa xong dòng `h1` thì lỗi ở ngay dòng sau. | Khi sửa test, đọc kỹ các dòng **phía sau** dòng lỗi và tự hỏi: "dòng này giả định gì về trang?" |

---

## 9. Lỗi thường gặp

| Hiện tượng | Cách sửa |
|---|---|
| `cy.wait() timed out waiting for the 1st request to the route: 'chat'` | `stubChat` được gọi **sau** `ask`. Phải chặn request trước khi gửi. |
| `cy.within() can only be called on a single element` | Selector khớp nhiều hơn 1 phần tử. Thêm `.should('have.length', 1)` trước `.within()`. |
| `... is being covered by another element: <div class="...">` | Một popup hoặc banner che nút. Tìm class trong thông báo để biết đó là gì, rồi tắt trong `openDuckAi`. |
| Khung xem trước hiện "Oops! Something went wrong" | Duck.ai bị sập. Mở F12 → Console để đọc lỗi màu đỏ. |
| Nhóm C không thấy thanh bên | Màn hình quá hẹp (≤ 900px). Kiểm tra `cy.viewport(1280, 800)` trong `openDuckAi`. |
| Selector không tìm thấy dù trước đây vẫn chạy | Duck.ai vừa cập nhật giao diện. Mở F12, kiểm tra lại `data-testid` / `aria-label` rồi sửa trong `SEL`. |
| WF09 báo tên model không đổi | Có thể chỉ còn một model miễn phí. Mở menu bằng tay xem có bao nhiêu lựa chọn. |

---

## 10. Bài tập mở rộng

1. **BT1:** Viết workflow câu trả lời giả có Markdown (`**đậm**`, danh sách `- a`), kiểm tra trang hiển thị thẻ `<strong>` và `<li>`.
2. **BT2:** Giả lập lỗi máy chủ bằng `{ statusCode: 500, body: { type: 'ERR_SERVER' } }` và quan sát Duck.ai báo lỗi thế nào.
3. **BT3:** Chuyển `ask`, `stubChat`, `createChat` sang `cypress/support/commands.js` thành `cy.ask()`, `cy.stubChat()`, `cy.createChat()`.
4. **BT4:** Xóa dòng `duckaiSurveyDismissed` trong `openDuckAi`, chạy lại WF16 và quan sát banner khảo sát che nút thế nào. Đọc thông báo lỗi `covered by another element` của Cypress.
5. **BT5:** Viết workflow thu gọn thanh bên trên máy tính (nút `Hide sidebar` / `Show sidebar`), kiểm tra chiều rộng bằng `.invoke('outerWidth')`.
