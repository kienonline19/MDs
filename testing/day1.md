# Buổi 1 — API Testing cơ bản với Postman

> **API mẫu:** [JSONPlaceholder](https://jsonplaceholder.typicode.com): REST API giả lập, miễn phí, không cần đăng ký.
> **Sản phẩm cuối buổi:** 1 Postman Collection test đầy đủ CRUD cho `/posts`, chạy được bằng Collection Runner và Newman.

---

## 0. Mục tiêu buổi học

Sau buổi này,  có thể:

1. Phân biệt các thành phần của một HTTP request: **method, URL, path variable, query params, headers, body**.
2. Viết request GET / POST / PUT / PATCH / DELETE trong Postman.
3. Viết **test script** để kiểm tra tự động: status code, header, thời gian phản hồi, dữ liệu trả về, **JSON Schema**.
4. Dùng **biến** (environment/collection variable) để nối các request với nhau.
5. Chạy cả bộ test bằng **Collection Runner**, chạy data-driven với file CSV và chạy bằng **Newman** (dòng lệnh).

---

## 1. Chuẩn bị

### 1.1. Cài đặt

- Tải Postman Desktop: https://www.postman.com/downloads/ (hoặc dùng bản Web, nhưng bản Desktop ổn định hơn).
- Đăng nhập (miễn phí) để lưu Workspace.
- (Tùy chọn, dùng ở cuối buổi) Cài Node.js và Newman:

```bash
npm install -g newman
newman -v
```

### 1.2. Tạo Collection và biến

1. Bấm **New → Collection**, đặt tên: `Day1 - JSONPlaceholder CRUD`.
2. Chọn Collection vừa tạo → tab **Variables** → thêm biến:

| Variable  | Initial value                          |
|-----------|----------------------------------------|
| `baseUrl` | `https://jsonplaceholder.typicode.com` |

3. Bấm **Save** (Ctrl+S).

>  **Vì sao dùng biến `baseUrl`?** Trong dự án thật, cùng một bộ test sẽ chạy trên nhiều môi trường (dev, staging, production). Chỉ cần đổi `baseUrl`, không phải sửa từng request.

### 1.3. Nơi viết test trong Postman

Trong mỗi request có tab **Scripts** gồm 2 phần:

- **Before request**: chạy **trước** khi gửi request (chuẩn bị dữ liệu, sinh biến ngẫu nhiên…).
- **After response**: chạy **sau** khi nhận response (viết test).

Kết quả test xem ở tab **Test Results** trong khung response.

---

## 2. Lý thuyết nhanh

### 2.1. Phân tích một request

```
GET https://jsonplaceholder.typicode.com/posts/1/comments?_limit=2
│   └──────────── baseUrl ─────────────┘└─path───────────┘└─query─┘
method                                   path variable (parameter) = 1
```

| Thành phần        | Ví dụ                               | Dùng để làm gì                                 | Trong Postman       |
|-------------------|-------------------------------------|------------------------------------------------|---------------------|
| Method            | `GET`, `POST`, `PUT`, `PATCH`, `DELETE` | Hành động muốn thực hiện                    | Dropdown bên trái URL |
| Path variable     | `/posts/:id` → `/posts/1`           | Xác định **một** tài nguyên cụ thể             | Tab **Params → Path Variables** |
| Query params      | `?userId=1&_limit=5`                | Lọc, phân trang, sắp xếp                       | Tab **Params → Query Params** |
| Headers           | `Content-Type: application/json`    | Metadata: định dạng dữ liệu, xác thực, ngôn ngữ… | Tab **Headers**   |
| Body              | `{"title": "abc"}`                  | Dữ liệu gửi lên (thường với POST/PUT/PATCH)    | Tab **Body → raw → JSON** |

### 2.2. CRUD ↔ HTTP method

| CRUD   | Method   | Endpoint mẫu   | Status thành công thường gặp |
|--------|----------|----------------|------------------------------|
| Create | `POST`   | `/posts`       | `201 Created`                |
| Read   | `GET`    | `/posts`, `/posts/1` | `200 OK`               |
| Update (toàn bộ) | `PUT`   | `/posts/1` | `200 OK`                     |
| Update (một phần) | `PATCH` | `/posts/1` | `200 OK`                    |
| Delete | `DELETE` | `/posts/1`     | `200 OK` hoặc `204 No Content` |

### 2.3. Nhóm status code

| Nhóm | Ý nghĩa         | Ví dụ hay gặp |
|------|-----------------|---------------|
| 2xx  | Thành công      | 200, 201, 204 |
| 3xx  | Chuyển hướng    | 301, 304      |
| 4xx  | **Lỗi phía client** (request sai) | 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 429 Too Many Requests |
| 5xx  | **Lỗi phía server** | 500 Internal Server Error, 502, 503 |

### 2.4. Kiểm tra response gồm những gì?

Một bộ test API tốt thường kiểm tra 5 tầng:

1. **Status code**: có đúng mã mong đợi không?
2. **Headers**: `Content-Type` có phải JSON không?
3. **Hiệu năng**: thời gian phản hồi có trong ngưỡng không?
4. **Schema**: cấu trúc JSON (trường nào, kiểu gì, bắt buộc hay không) có đúng không?
5. **Dữ liệu**: giá trị có đúng logic nghiệp vụ không (VD: lọc `userId=1` thì mọi phần tử phải có `userId = 1`)?

### 2.5. Lưu ý quan trọng về JSONPlaceholder

JSONPlaceholder là API **giả lập**: GET/POST/PUT/PATCH/DELETE trả về response như thật nhưng **không lưu thay đổi** vào server. Tức là tạo bài viết mới xong, GET lại sẽ không thấy. Đây không phải lỗi mà là đặc điểm của API mẫu; ta sẽ tận dụng điều này để hiểu rõ hơn ở Bài 5.

Dữ liệu có sẵn: 100 `posts`, 500 `comments`, 100 `albums`, 5000 `photos`, 200 `todos`, 10 `users`.

---

## 3. Thực hành từng bước

> Tạo mỗi bài là **một request** trong Collection, đặt tên theo mẫu `01 - GET all posts`, `02 - GET posts by userId`,… để Runner chạy đúng thứ tự.

### Bài 1 — GET danh sách: test cơ bản

**Request**

- Method: `GET`
- URL: `{{baseUrl}}/posts`

Bấm **Send**, quan sát: status `200 OK`, thời gian (ms), dung lượng, body là mảng JSON.

**Scripts → After response**

```javascript
// 1. Status code
pm.test("Status code là 200", function () {
    pm.response.to.have.status(200);
});

// 2. Header
pm.test("Content-Type là application/json", function () {
    pm.expect(pm.response.headers.get("Content-Type")).to.include("application/json");
});

// 3. Hiệu năng
pm.test("Thời gian phản hồi dưới 2000ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(2000);
});

// 4 + 5. Cấu trúc và dữ liệu
const data = pm.response.json();

pm.test("Body là mảng gồm 100 bài viết", function () {
    pm.expect(data).to.be.an("array");
    pm.expect(data).to.have.lengthOf(100);
});

pm.test("Mỗi bài viết có đủ 4 trường userId, id, title, body", function () {
    data.forEach(function (post) {
        pm.expect(post).to.have.all.keys("userId", "id", "title", "body");
    });
});

pm.test("id là duy nhất", function () {
    const ids = data.map(p => p.id);
    pm.expect(new Set(ids).size).to.eql(ids.length);
});
```

**Giải thích**

- `pm.test(tên, hàm)`: định nghĩa một test case. Nếu bên trong có assertion sai thì test đó FAIL.
- `pm.response.to.have.status(200)`: assertion có sẵn của Postman.
- `pm.expect(...)`: dùng cú pháp của thư viện **Chai** (`to.be.an`, `to.have.lengthOf`, `to.include`, `to.eql`…).
- `pm.response.json()`: parse body thành object JavaScript.
- `to.have.all.keys(...)`: object phải có **đúng và đủ** các key này (thừa hoặc thiếu đều fail).

>  **Thử làm fail:** sửa `lengthOf(100)` thành `lengthOf(99)` → Send → xem thông báo lỗi ở Test Results. cần quen đọc thông báo lỗi, vì đó là thứ ta viết vào bug report.

---

### Bài 2 — Query params: lọc và giới hạn

**Request**

- Method: `GET`
- URL: `{{baseUrl}}/posts`
- Tab **Params → Query Params**:

| Key      | Value |
|----------|-------|
| `userId` | `1`   |

Postman tự sinh URL: `{{baseUrl}}/posts?userId=1`.

**After response**

```javascript
const data = pm.response.json();

pm.test("Status 200", () => pm.response.to.have.status(200));

pm.test("Trả về 10 bài viết của user 1", () => {
    pm.expect(data).to.have.lengthOf(10);
});

pm.test("Mọi bài viết đều thuộc userId = 1", () => {
    data.forEach(post => pm.expect(post.userId).to.eql(1));
});
```

**Mở rộng:** thêm query `_limit` = `3` (tick chọn cả 2 params), sửa test thành `lengthOf(3)`.

**Giải thích:** Test "mọi phần tử đều thuộc userId = 1" là **test dữ liệu theo logic nghiệp vụ**. Chỉ kiểm tra status 200 là chưa đủ: server có thể trả 200 nhưng lọc sai.

>  **Câu hỏi thảo luận:** Gọi `?userId=999` (user không tồn tại) thì server nên trả gì: `404` hay `200` với mảng rỗng `[]`? Thử và giải thích. *(Gợi ý: với API lọc danh sách, "không có kết quả" không phải lỗi.)*

---

### Bài 3 — Path variable: lấy một tài nguyên và tài nguyên lồng nhau

**3a. Lấy 1 bài viết**

- Method: `GET`
- URL: `{{baseUrl}}/posts/:id`
- Tab **Params → Path Variables**: `id` = `1`

```javascript
const post = pm.response.json();

pm.test("Status 200", () => pm.response.to.have.status(200));

pm.test("Trả về đúng bài viết id = 1", () => {
    pm.expect(post).to.be.an("object");
    pm.expect(post.id).to.eql(1);
});

pm.test("title và body là chuỗi không rỗng", () => {
    pm.expect(post.title).to.be.a("string").and.not.empty;
    pm.expect(post.body).to.be.a("string").and.not.empty;
});
```

**3b. Tài nguyên lồng nhau: comment của bài viết**

- URL: `{{baseUrl}}/posts/:id/comments`, `id` = `1`

```javascript
const comments = pm.response.json();

pm.test("Có 5 comment", () => pm.expect(comments).to.have.lengthOf(5));

pm.test("Mọi comment đều thuộc postId = 1", () => {
    comments.forEach(c => pm.expect(c.postId).to.eql(1));
});

pm.test("Email đúng định dạng cơ bản", () => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    comments.forEach(c => pm.expect(c.email).to.match(emailRegex));
});
```

**Giải thích:** Path variable dùng để **định danh** tài nguyên (`/posts/1`), còn query param dùng để **lọc/tùy chọn** (`/posts?userId=1`). 

---

### Bài 4 — Headers: gửi đi và kiểm tra nhận về

**Request**

- Method: `GET`
- URL: `{{baseUrl}}/users/1`
- Tab **Headers**, thêm:

| Key            | Value              |
|----------------|--------------------|
| `Accept`       | `application/json` |
| `X-Request-Id` | `{{$guid}}`        |

> `{{$guid}}` là **biến động** có sẵn của Postman: mỗi lần gửi sinh một UUID mới. Một số biến động khác: `{{$timestamp}}`, `{{$randomInt}}`, `{{$randomEmail}}`, `{{$randomFullName}}`.

**After response**

```javascript
pm.test("Response có header Content-Type", () => {
    pm.response.to.have.header("Content-Type");
});

pm.test("Content-Type chứa charset utf-8", () => {
    pm.expect(pm.response.headers.get("Content-Type")).to.include("utf-8");
});

const user = pm.response.json();

pm.test("User có địa chỉ và công ty (object lồng nhau)", () => {
    pm.expect(user).to.have.nested.property("address.city");
    pm.expect(user).to.have.nested.property("address.geo.lat");
    pm.expect(user).to.have.nested.property("company.name");
});

// In ra console để debug (View → Show Postman Console, hoặc Ctrl+Alt+C)
console.log("Request id đã gửi:", pm.request.headers.get("X-Request-Id"));
console.log("Tên user:", user.name);
```

**Giải thích**

- Header **gửi đi** (request headers) báo cho server biết client muốn gì; header **nhận về** (response headers) cho biết server trả gì.
- Header xác thực (`Authorization: Bearer <token>`) là loại header quan trọng nhất khi test API thật. JSONPlaceholder không yêu cầu xác thực, nhưng hãy mở tab **Authorization → Bearer Token** để làm quen; ta sẽ dùng nó ở Buổi 2.
- **Postman Console** là công cụ debug quan trọng: xem chính xác request đã gửi đi (URL sau khi thay biến, header, body).

---

### Bài 5 — POST: tạo mới (Create)

**Request**

- Method: `POST`
- URL: `{{baseUrl}}/posts`
- Tab **Body → raw → JSON**:

```json
{
    "title": "{{postTitle}}",
    "body": "Nội dung bài viết được tạo từ Postman",
    "userId": 1
}
```

> Khi chọn `raw → JSON`, Postman tự thêm header `Content-Type: application/json`. Nếu thiếu header này, nhiều server sẽ không hiểu body.

**Scripts → Before request** (sinh tiêu đề không trùng mỗi lần chạy)

```javascript
const title = "Bài test " + Date.now();
pm.collectionVariables.set("postTitle", title);
```

**Scripts → After response**

```javascript
pm.test("Status 201 Created", () => {
    pm.response.to.have.status(201);
});

const created = pm.response.json();
const sentBody = JSON.parse(pm.request.body.raw.replace("{{postTitle}}", pm.collectionVariables.get("postTitle")));

pm.test("Server trả về id mới (kiểu number)", () => {
    pm.expect(created.id).to.be.a("number");
});

pm.test("Dữ liệu trả về khớp dữ liệu đã gửi", () => {
    pm.expect(created.title).to.eql(sentBody.title);
    pm.expect(created.body).to.eql(sentBody.body);
    pm.expect(created.userId).to.eql(sentBody.userId);
});

// Lưu id để request sau dùng
pm.collectionVariables.set("newPostId", created.id);
console.log("Đã tạo post id:", created.id);
```

**Giải thích**

- `201 Created` là status chuẩn cho tạo mới thành công (không phải `200`).
- **Chaining (nối request):** lưu `id` vừa tạo vào biến `newPostId` để request sau dùng `{{newPostId}}`. Đây là kỹ thuật cốt lõi khi test luồng nghiệp vụ: *tạo → đọc → sửa → xóa*.

>  **Thí nghiệm "API giả lập":** Tạo thêm request `GET {{baseUrl}}/posts/{{newPostId}}`. Kết quả là **404**, vì JSONPlaceholder không lưu thật (id luôn là `101`).
>
> **Bài học:** Với API thật, bước "GET lại để xác nhận dữ liệu đã được lưu" là bắt buộc. Nếu chỉ tin vào response của POST, ta có thể bỏ sót lỗi server báo "thành công" nhưng không ghi vào database.

---

### Bài 6 — PUT: cập nhật toàn bộ (Update)

**Request**

- Method: `PUT`
- URL: `{{baseUrl}}/posts/1`
- Body (raw JSON):

```json
{
    "id": 1,
    "title": "Tiêu đề đã cập nhật bằng PUT",
    "body": "Nội dung đã cập nhật bằng PUT",
    "userId": 1
}
```

**After response**

```javascript
pm.test("Status 200", () => pm.response.to.have.status(200));

const updated = pm.response.json();

pm.test("Các trường đã được cập nhật", () => {
    pm.expect(updated.id).to.eql(1);
    pm.expect(updated.title).to.eql("Tiêu đề đã cập nhật bằng PUT");
    pm.expect(updated.body).to.eql("Nội dung đã cập nhật bằng PUT");
});
```

> Ở đây ta dùng `/posts/1` (có sẵn) thay vì `{{newPostId}}` vì bài 101 không tồn tại thật. Hãy thử PUT vào `/posts/101` và quan sát status trả về. Đây là một lỗi kiểu gì (4xx hay 5xx)? Server *nên* trả gì mới đúng?

---

### Bài 7 — PATCH: cập nhật một phần, so sánh với PUT

**Request**

- Method: `PATCH`
- URL: `{{baseUrl}}/posts/1`
- Body:

```json
{
    "title": "Chỉ sửa title bằng PATCH"
}
```

**After response**

```javascript
const patched = pm.response.json();

pm.test("Status 200", () => pm.response.to.have.status(200));

pm.test("title đã đổi", () => {
    pm.expect(patched.title).to.eql("Chỉ sửa title bằng PATCH");
});

pm.test("Các trường không gửi vẫn được giữ nguyên", () => {
    pm.expect(patched).to.have.property("body");
    pm.expect(patched).to.have.property("userId", 1);
});
```

>  **Thí nghiệm so sánh:** Nhân bản (Duplicate) request PUT ở Bài 6, sửa body **chỉ còn** `{"title": "Chỉ có title"}` rồi Send. Quan sát: trường `body` và `userId` còn trong response không?
>
> **Kết luận cần rút ra:** PUT = *thay thế toàn bộ* tài nguyên; PATCH = *chỉ sửa trường được gửi*. Nhầm hai method này là lỗi rất hay gặp khi phát triển frontend.

---

### Bài 8 — DELETE: xóa (Delete)

**Request**

- Method: `DELETE`
- URL: `{{baseUrl}}/posts/1`

**After response**

```javascript
pm.test("Status 200 hoặc 204", () => {
    pm.expect(pm.response.code).to.be.oneOf([200, 204]);
});

pm.test("Body rỗng", () => {
    // JSONPlaceholder trả về {} ; một số API khác trả body trống hoàn toàn (204)
    if (pm.response.code === 204) {
        pm.expect(pm.response.text()).to.be.empty;
    } else {
        pm.expect(pm.response.json()).to.eql({});
    }
});
```

**Giải thích:** `to.be.oneOf([...])` hữu ích khi đặc tả cho phép nhiều status hợp lệ. Trong dự án thật, hãy thống nhất với đội backend một con số cụ thể rồi test chặt.

---

### Bài 9 — Negative testing: test các trường hợp lỗi

Test không chỉ để xác nhận "chạy đúng" mà còn để xác nhận "**sai thì báo lỗi đúng cách**". Tạo folder `Negative` trong Collection với các request sau:

| # | Request                         | Kỳ vọng |
|---|---------------------------------|---------|
| 9a | `GET {{baseUrl}}/posts/99999`  | `404`   |
| 9b | `GET {{baseUrl}}/posts/abc`    | `404`   |
| 9c | `GET {{baseUrl}}/khong-ton-tai`| `404`   |

**After response** (dùng chung cho cả 3)

```javascript
pm.test("Status 404 Not Found", () => {
    pm.response.to.have.status(404);
});

pm.test("Không trả về dữ liệu", () => {
    pm.expect(pm.response.json()).to.eql({});
});
```

**Giải thích:** Một số tình huống negative khác nên có với API thật: thiếu trường bắt buộc (→ 400), sai kiểu dữ liệu (`"userId": "abc"` → 400), thiếu/sai token (→ 401), không có quyền (→ 403). JSONPlaceholder không validate nên sẽ không trả các lỗi này, nhưng  cần biết để áp dụng cho API thật.

---

### Bài 10 — Kiểm tra JSON Schema

Thay vì kiểm tra từng trường bằng tay, ta mô tả **cấu trúc mong đợi** bằng JSON Schema rồi cho Postman kiểm tra tự động.

**Request:** `GET {{baseUrl}}/posts/1`

**After response**

```javascript
const postSchema = {
    type: "object",
    required: ["userId", "id", "title", "body"],
    properties: {
        userId: { type: "integer", minimum: 1 },
        id:     { type: "integer", minimum: 1 },
        title:  { type: "string", minLength: 1 },
        body:   { type: "string", minLength: 1 }
    }
};

pm.test("Response đúng schema của Post", () => {
    pm.response.to.have.jsonSchema(postSchema);
});
```

**Áp dụng cho danh sách** (`GET {{baseUrl}}/posts`):

```javascript
const postListSchema = {
    type: "array",
    minItems: 1,
    items: {
        type: "object",
        required: ["userId", "id", "title", "body"],
        properties: {
            userId: { type: "integer" },
            id:     { type: "integer" },
            title:  { type: "string" },
            body:   { type: "string" }
        }
    }
};

pm.test("Danh sách đúng schema", () => {
    pm.response.to.have.jsonSchema(postListSchema);
});
```

**Giải thích các từ khóa schema**

| Từ khóa | Ý nghĩa |
|---------|---------|
| `type` | Kiểu dữ liệu: `object`, `array`, `string`, `integer`, `number`, `boolean`, `null` |
| `required` | Danh sách trường bắt buộc phải có |
| `properties` | Mô tả từng trường |
| `additionalProperties: false` | Không cho phép trường lạ ngoài danh sách |
| `items` | Schema cho từng phần tử của mảng |
| `minLength`, `minimum`, `minItems` | Ràng buộc độ dài / giá trị / số phần tử |

>  **Thử làm fail:** đổi `id: { type: "integer" }` thành `type: "string"` → xem thông báo lỗi. Sau đó đổi lại.
>
>  **Mẹo tái sử dụng:** Đặt schema vào **Collection → Scripts → Before request** dưới dạng `pm.collectionVariables.set("postSchema", JSON.stringify({...}))`, rồi trong từng request dùng `JSON.parse(pm.collectionVariables.get("postSchema"))`. Khi API đổi cấu trúc, chỉ cần sửa một chỗ.

---

### Bài 11 — Chạy cả bộ test: Collection Runner, data-driven, Newman

**11a. Collection Runner**

1. Chuột phải vào Collection → **Run collection**.
2. Kiểm tra thứ tự request (kéo thả nếu cần): POST → GET → PUT → PATCH → DELETE → Negative.
3. Bấm **Run**. Xem tổng số test pass/fail.

**11b. Data-driven testing với CSV**

Tạo file `users_data.csv`:

```csv
userId,expectedCount
1,10
2,10
5,10
11,0
```

Tạo request mới `GET {{baseUrl}}/posts?userId={{userId}}` với After response:

```javascript
const expected = Number(pm.iterationData.get("expectedCount"));
const data = pm.response.json();

pm.test(`userId=${pm.iterationData.get("userId")} có ${expected} bài viết`, () => {
    pm.expect(data).to.have.lengthOf(expected);
});
```

Trong Runner: chọn **Data → Select File → users_data.csv**. Postman tự chạy 4 vòng (iteration), mỗi vòng lấy 1 dòng.

```bash
newman run "JSONPLaceholder CRUD.postman_collection.json" --env-var "baseUrl=https://jsonplaceholder.typicode.com" -d users_data.csv -r cli,htmlextra
```

> **Giải thích:** Data-driven testing tách *dữ liệu test* khỏi *logic test*. Muốn thêm test case chỉ cần thêm dòng CSV, không cần viết thêm code.

**11c. Chạy bằng Newman (dòng lệnh)**

1. Chuột phải Collection → **Export** → lưu `Day1.postman_collection.json`.
2. Chạy:

```bash
newman run Day1.postman_collection.json

# Chạy kèm dữ liệu CSV
newman run Day1.postman_collection.json -d users_data.csv

# (Tùy chọn) Xuất báo cáo HTML đẹp
npm install -g newman-reporter-htmlextra
newman run Day1.postman_collection.json -r cli,htmlextra
```

> **Vì sao cần Newman?** Để đưa test API vào **CI/CD** (GitHub Actions, GitLab CI, Jenkins…): mỗi lần đẩy code, bộ test tự chạy, fail thì chặn deploy.

---

## 4. Bài tập về nhà

Tạo Collection `Day1 - Todos CRUD - <HọTên>` test tài nguyên **`/todos`** của JSONPlaceholder:

1. `GET /todos`: kiểm tra 200 todos, schema đúng (`userId`, `id`, `title`, `completed` kiểu **boolean**).
2. `GET /todos?completed=true`: mọi phần tử có `completed === true`.
3. `GET /todos?userId=1&completed=false`: kết hợp 2 điều kiện lọc.
4. `POST /todos`: tạo todo, kiểm tra 201 và dữ liệu khớp, lưu id vào biến.
5. `PATCH /todos/1`: đổi `completed` thành `true`.
6. `PUT /todos/1` và `DELETE /todos/1`.
7. Ít nhất 2 negative test.
8. Chạy bằng Runner **và** Newman, chụp ảnh kết quả.

---

## 5. Lỗi thường gặp

| Hiện tượng | Nguyên nhân | Cách xử lý |
|-----------|-------------|-----------|
| URL hiện `{{baseUrl}}` màu đỏ | Biến chưa khai báo hoặc sai tên | Kiểm tra tab Variables của Collection, bấm Save |
| POST trả dữ liệu thiếu trường đã gửi | Body chọn `Text` thay vì `JSON`, thiếu `Content-Type` | Body → raw → chọn **JSON** |
| `JSONError: Unexpected token` trong test | Gọi `pm.response.json()` khi body không phải JSON | Kiểm tra status/Content-Type trước khi parse |
| Test không chạy | Viết nhầm vào Before request | Chuyển sang **After response** |
| Biến không đổi giá trị | Dùng `pm.environment.set` nhưng chưa chọn Environment | Dùng `pm.collectionVariables.set` hoặc chọn Environment ở góc phải trên |
| Runner chạy sai thứ tự | Thứ tự request trong Collection chưa đúng | Kéo thả sắp xếp lại |

---

## 6. Cheat sheet `pm` hay dùng

```javascript
// Response
pm.response.code                       // 200
pm.response.status                     // "OK"
pm.response.responseTime               // ms
pm.response.json()                     // body -> object
pm.response.text()                     // body -> string
pm.response.headers.get("Content-Type")

// Assertion nhanh
pm.response.to.have.status(200);
pm.response.to.have.header("Content-Type");
pm.response.to.have.jsonSchema(schema);

// Chai
pm.expect(x).to.eql(y);                // so sánh sâu
pm.expect(x).to.be.a("string");
pm.expect(arr).to.have.lengthOf(3);
pm.expect(arr).to.include(5);
pm.expect(obj).to.have.property("id");
pm.expect(obj).to.have.nested.property("a.b.c");
pm.expect(n).to.be.below(1000);
pm.expect(n).to.be.oneOf([200, 204]);

// Biến
pm.collectionVariables.set("key", value);
pm.collectionVariables.get("key");
pm.environment.set("key", value);
pm.iterationData.get("column");        // dữ liệu CSV/JSON trong Runner

// Request hiện tại
pm.request.url.toString();
pm.request.headers.get("X-Request-Id");
pm.request.body.raw;
```

---

Điểm nhấn nên nhắc lại: *status 200 không có nghĩa là đúng*. Luôn kiểm tra dữ liệu và schema.
