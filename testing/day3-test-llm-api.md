# Buổi 6: Test API cho hệ thống AI (LLM API)

## 1. LLM API khác API thường ở đâu?

| Đặc điểm | REST API thường | LLM API |
|---|---|---|
| Kết quả | Xác định (cùng input → cùng output) | **Không xác định**: cùng prompt có thể ra câu trả lời khác |
| Thời gian phản hồi | Vài chục đến vài trăm ms | Vài giây đến vài chục giây, phụ thuộc độ dài output |
| Kiểu trả về | JSON một lần | JSON hoặc **streaming (SSE)**, trả từng mảnh |
| Chi phí | Theo request | Theo **token** (input + output) |
| Giới hạn | Rate limit theo request | Rate limit theo request **và** token/phút, cộng giới hạn context |

**Nguyên tắc vàng:** không assert nội dung câu trả lời chính xác từng chữ. Hãy test **cấu trúc, hành vi và ràng buộc**: format, status code, field bắt buộc, `finish_reason`, usage, header, thời gian.

## 2. Chuẩn bị (chọn 1 provider)

| Lựa chọn | Ưu điểm | Endpoint |
|---|---|---|
| **Ollama (chạy local)** | Miễn phí, không cần key, phù hợp lớp đông | `http://localhost:11434/v1/chat/completions` |
| **Groq** (free tier) | Nhanh, rate limit thấp nên **dễ demo lỗi 429** | `https://api.groq.com/openai/v1/chat/completions` |
| **Gemini** (free tier) | Có endpoint tương thích OpenAI | `https://generativelanguage.googleapis.com/v1beta/openai/chat/completions` |
| OpenAI / Anthropic | Chuẩn công nghiệp | Cần key trả phí |

Cả ba lựa chọn đầu dùng **chung format OpenAI-compatible**, nên một bộ test chạy được cho cả ba. Tên model thay đổi thường xuyên, vì vậy hãy tra trong console/docs của provider.

**Postman Collection** `LLM-Lab`:

```
base_url = <api-url>
api_key  = <key trên tài khoản>
model    = <tên model lấy từ console>
```

## 3. Thực hành

**Postman gửi câu hỏi đến LLM chạy trên máy qua Ollama**. Dưới đây là từng bước trên **Windows**.

**1. Cài Ollama**

Tải và cài: [Ollama cho Windows](https://ollama.com/download/windows).

Sau khi cài, mở Ollama. API mặc định chạy ở cổng 11434:

```text
http://localhost:11434
```

Ollama trên Windows có thể chạy nền. [Ollama](https://docs.ollama.com/windows)

Mở **CMD hoặc PowerShell mới**, kiểm tra phiên bản:

```cmd
ollama -v
```

**2. Tải một model để thử**

Chạy:

```cmd
ollama pull llama3.2:1b
```

Sau khi tải xong:

```cmd
ollama list
```

`pull` tải model; `list` liệt kê model đã có trên máy. [GitHub](https://github.com/ollama/ollama/blob/main/docs/cli.mdx)

Bài này dùng `llama3.2:1b`, một model nhỏ để thực hành API. [ollama.com](https://ollama.com/library/llama3.2%3A1b)

**3. Tạo Collection trong Postman**

Dùng **Postman desktop** trên cùng máy với Ollama.

Tạo collection tên:

```text
LLM-Lab
```

Trong **Variables** của collection, thêm và lưu:

| Variable | Value |
|---|---|
| `base_url` | `http://localhost:11434` |
| `model` | `llama3.2:1b` |

Trong **Authorization**, chọn **No Auth**. API local này không cần API key. [GitHub](https://github.com/ollama/ollama/blob/main/docs/api/introduction.mdx)

**4. Request đầu tiên: xem danh sách model**

Thêm request vào collection:

```http
GET {{base_url}}/api/tags
```

Không cần Body. Bấm **Send**.

Kết quả mong đợi: **200 OK**, JSON chứa mảng `models`. [Ollama](https://docs.ollama.com/api/tags)

Ví dụ rút gọn:

```json
{
  "models": [
    {
      "name": "llama3.2:1b"
    }
  ]
}
```

Nếu `models` rỗng, kiểm tra lại bước tải model.

**5. Gửi câu hỏi cho LLM**

Tạo request mới:

```http
POST {{base_url}}/api/generate
```

Chọn **Body → raw → JSON**, dán:

```json
{
  "model": "{{model}}",
  "prompt": "Explain what an API is in two short sentences.",
  "stream": false
}
```

Trong **Headers**, kiểm tra có:

| Key | Value |
|---|---|
| `Content-Type` | `application/json` |

Bấm **Send**.

Ý nghĩa các trường:

| Trường | Ý nghĩa |
|---|---|
| `model` | Model sẽ xử lý câu hỏi |
| `prompt` | Nội dung bạn muốn hỏi |
| `stream: false` | Trả về một JSON hoàn chỉnh, thuận tiện để test |

Câu trả lời nằm trong trường `response`; `done: true` cho biết quá trình sinh đã kết thúc. [Ollama](https://docs.ollama.com/api/generate)

Ví dụ minh họa rút gọn — câu trả lời thực tế có thể khác:

```json
{
  "model": "llama3.2:1b",
  "response": "An API lets applications communicate with each other. It defines how they exchange requests and responses.",
  "done": true
}
```

**6. Viết test tự động**

Trong request `/api/generate`, mở **Scripts → After response** và dán đoạn sau. Script chạy sau khi Postman nhận response. [Postman Docs](https://learning.postman.com/docs/tests-and-scripts/write-scripts/test-scripts/)

```javascript
pm.test("Status is 200", () => {
    pm.response.to.have.status(200);
});

pm.test("Content-Type is JSON", () => {
    pm.expect(pm.response.headers.get("Content-Type"))
        .to.include("application/json");
});

pm.test("Response contains a non-empty answer", () => {
    const data = pm.response.json();

    pm.expect(data.response).to.be.a("string");
    pm.expect(data.response.trim().length).to.be.above(0);
});

pm.test("Generation is complete", () => {
    const data = pm.response.json();

    pm.expect(data.done).to.equal(true);
});
```

Bấm **Send** lại rồi xem **Test Results**.

Các test này kiểm tra API hoạt động và có câu trả lời; **chưa đánh giá câu trả lời đúng kiến thức hay không**. Tránh kiểm tra nguyên văn câu trả lời vì LLM có thể diễn đạt khác nhau.

**7. Test hội thoại với `/api/chat`**

Tạo request mới:

```http
POST {{base_url}}/api/chat
```

Chọn **Body → raw → JSON**:

```json
{
  "model": "{{model}}",
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful programming teacher. Keep answers short."
    },
    {
      "role": "user",
      "content": "What is a Python list?"
    }
  ],
  "stream": false
}
```

Với endpoint này, câu trả lời nằm ở **`message.content`**. Mảng `messages` chứa lịch sử hội thoại bạn gửi cho model. [Ollama](https://docs.ollama.com/api/chat)

Test riêng cho chat:

```javascript
pm.test("Chat returns an answer", () => {
    pm.response.to.have.status(200);

    const data = pm.response.json();

    pm.expect(data.message.role).to.equal("assistant");
    pm.expect(data.message.content).to.be.a("string");
    pm.expect(data.message.content.trim().length).to.be.above(0);
    pm.expect(data.done).to.equal(true);
});
```

Để hỏi tiếp, gửi cả các lượt trước trong `messages`, ví dụ:

```json
{
  "model": "{{model}}",
  "messages": [
    {
      "role": "user",
      "content": "My name is Kien."
    },
    {
      "role": "assistant",
      "content": "Hello, Kien!"
    },
    {
      "role": "user",
      "content": "What is my name?"
    }
  ],
  "stream": false
}
```

**8. Nếu gặp lỗi**

| Hiện tượng | Cách xử lý |
|---|---|
| `ECONNREFUSED` | Mở Ollama; nếu server chưa chạy, chạy `ollama serve` |
| Chạy `serve` báo cổng đang được dùng | Có thể Ollama đã chạy nền; thử request `/api/tags` |
| `model not found` | Chạy `ollama list`; dùng đúng tên model hoặc tải lại |
| Response hiện nhiều JSON liên tiếp | Thêm `"stream": false` vào Body |
| Request timeout | Tăng **Request timeout** trong Postman Settings, ví dụ `300000` ms |
| Postman web không gọi được localhost | Dùng Postman desktop hoặc chọn Desktop Agent |

Postman hướng dẫn tăng timeout khi request cần nhiều thời gian và dùng Desktop Agent khi gọi API local từ bản web. [Postman Docs](https://learning.postman.com/docs/use/send-requests/response-data/troubleshooting-api-requests)

## **10 bài tập Ollama API bằng Postman**, từ dễ đến khó.

**Chuẩn bị chung**

Tạo collection `Ollama Exercises` với các biến:

| Variable | Value |
|---|---|
| `base_url` | `http://localhost:11434` |
| `model` | `llama3.2:1b` |

- Ollama đang chạy và model đã được tải.
- Authorization: **No Auth**.
- Request POST: **Body → raw → JSON**.
- Sử dụng `"stream": false`, ngoại trừ bài 8.
- Viết test trong **Scripts → Post-response**, đặt tên test bằng tiếng Anh.

---

**1. Xem danh sách model — Dễ**

**Endpoint:** `GET {{base_url}}/api/tags`

Yêu cầu:

- Gửi request lấy danh sách model đã tải.
- Viết test kiểm tra status `200`.
- Kiểm tra `models` là một mảng.
- Kiểm tra model trong biến `{{model}}` xuất hiện trong danh sách.

**Hoàn thành khi:** Các test đều PASS và bạn xác định được model có thể dùng. Endpoint này liệt kê các model local. [docs.ollama.com](https://docs.ollama.com/api/tags)

---

**2. Gửi câu hỏi đầu tiên — Dễ**

**Endpoint:** `POST {{base_url}}/api/generate`

Prompt:

```text
Explain what an API is in two short sentences.
```

Yêu cầu:

- Tự tạo Body gồm `model`, `prompt`, `stream`.
- Kiểm tra status `200`.
- Kiểm tra `response` là chuỗi không rỗng.
- Kiểm tra `done` bằng `true`.
- In câu trả lời vào Postman Console.

**Hoàn thành khi:** Nhận được câu trả lời và có ít nhất 3 test PASS.

---

**3. Tái sử dụng request bằng biến — Dễ**

**Endpoint:** `POST {{base_url}}/api/generate`

Yêu cầu:

- Tạo biến collection `question`.
- Dùng `{{question}}` trong trường `prompt`.
- Lần lượt thử 3 câu hỏi:

```text
What is a Python list?
What is a Java class?
What is an HTTP request?
```

- Chỉ thay giá trị biến, giữ nguyên cấu trúc Body.
- Lưu câu trả lời mới nhất vào biến collection `last_answer`.

**Hoàn thành khi:** Một request xử lý được cả 3 câu hỏi và biến `last_answer` được cập nhật.

---

**4. Tạo trợ lý dạy lập trình — Trung bình**

**Endpoint:** `POST {{base_url}}/api/chat`

System message:

```text
You are a programming teacher. Use simple English and short examples.
```

User message:

```text
Explain a for loop in Python.
```

Yêu cầu:

- Tạo mảng `messages` chứa hai role: `system`, `user`.
- Kiểm tra `message.role` bằng `"assistant"`.
- Kiểm tra `message.content` là chuỗi không rỗng.
- Đọc câu trả lời để đánh giá mức độ dễ hiểu và ví dụ.

**Hoàn thành khi:** Phân biệt được vị trí câu trả lời giữa hai endpoint:

| Endpoint | Trường chứa câu trả lời |
|---|---|
| `/api/generate` | `response` |
| `/api/chat` | `message.content` |

Đây là cấu trúc response được Ollama quy định. [docs.ollama.com](https://docs.ollama.com/api/generate)

---

**5. Hội thoại nhiều lượt — Trung bình**

**Endpoint:** `POST {{base_url}}/api/chat`

Yêu cầu:

1. Gửi câu: `"My name is Kien. I am learning Java."`
2. Lưu câu trả lời thực tế của model.
3. Gửi tiếp: `"What is my name, and what am I learning?"`
4. Request thứ hai phải chứa lịch sử theo thứ tự `user → assistant → user`.
5. Thử lại với chỉ câu hỏi cuối, không kèm lịch sử.
6. So sánh kết quả.

**Hoàn thành khi:** Khi được cung cấp lịch sử, model trả lời đúng tên và ngôn ngữ đang học. Ghi nhận nếu model trả lời sai; không sửa test chỉ để PASS.

**Gợi ý:** Bạn phải gửi lịch sử trong `messages` cho mỗi request cần ngữ cảnh. [docs.ollama.com](https://docs.ollama.com/api/chat)

---

**6. Kiểm thử dữ liệu không hợp lệ — Trung bình**

**Endpoint:** `POST {{base_url}}/api/generate`

Tạo 3 request riêng:

| Trường hợp | Dữ liệu thử | Status mong đợi |
|---|---|---:|
| Model không tồn tại | `"model": "nonexistent-practice-model:abc"` | `404` |
| Thiếu model | Bỏ trường `model` | `400` |
| JSON sai cú pháp | Bỏ một dấu phẩy giữa hai trường | `400` |

Yêu cầu:

- Kiểm tra status tương ứng.
- Kiểm tra response chứa `error` là chuỗi không rỗng.
- Không kiểm tra toàn bộ nguyên văn thông báo lỗi.

**Hoàn thành khi:** Cả 3 negative test PASS. Các mã lỗi và trường `error` dựa trên tài liệu Ollama. [Ollama](https://docs.ollama.com/api/errors)

---

**7. Trích xuất dữ liệu thành JSON — Khá**

**Endpoint:** `POST {{base_url}}/api/chat`

Dữ liệu đầu vào:

```text
Linh is 22 years old and studies Python and Java.
```

Kết quả yêu cầu:

```json
{
  "name": "Linh",
  "age": 22,
  "skills": ["Python", "Java"]
}
```

Yêu cầu:

- Dùng trường `format` với **JSON Schema**.
- Bắt buộc có `name`, `age`, `skills`.
- Quy định kiểu tương ứng: string, integer, array of strings.
- Parse JSON bên trong `message.content`.
- Kiểm tra cả kiểu dữ liệu và giá trị được trích xuất.

**Hoàn thành khi:** JSON hợp lệ, đủ trường và đúng dữ liệu đầu vào.

**Gợi ý:** Response HTTP là một JSON; `message.content` vẫn là chuỗi chứa JSON cần parse thêm. Ollama hỗ trợ truyền schema qua `format`. [Ollama](https://docs.ollama.com/capabilities/structured-outputs)

---

**8. Xử lý streaming response — Khó**

**Endpoint:** `POST {{base_url}}/api/generate`

Yêu cầu:

- Gửi cùng một prompt với `stream: false`, rồi `stream: true`.
- Quan sát sự khác nhau của response.
- Khi stream hoàn thành, đọc nội dung bằng `pm.response.text()`.
- Tách các dòng không rỗng và parse từng dòng JSON.
- Ghép các trường `response` theo đúng thứ tự.
- Kiểm tra bản ghi cuối có `done: true` trong trường hợp thành công.
- Phát hiện nếu có bản ghi chứa `error`.

**Hoàn thành khi:** In được câu trả lời đã ghép vào Console và phát hiện được lỗi nếu có.

**Gợi ý:** Streaming dùng NDJSON; không parse toàn bộ nội dung như một JSON duy nhất. Lỗi giữa stream có thể xuất hiện dù HTTP status đã là `200`. [Ollama](https://docs.ollama.com/api/errors)

---

**9. Kiểm thử timeout và thời gian phản hồi — Khó**

**Endpoint:** `POST {{base_url}}/api/generate`

Yêu cầu:

1. Dùng `stream: false`.
2. Đặt Request Timeout là `1000` ms và tạo request cần hơn 1 giây.
3. Ghi nhận lỗi timeout trong Postman.
4. Tăng timeout lên `120000` ms rồi gửi lại.
5. Thêm test yêu cầu response dưới `5000` ms.
6. Thử timeout `0` rồi hủy thủ công khi request đang chờ.

Lập bảng ghi nhận:

| Timeout cấu hình | Thời gian quan sát | Có HTTP response? | Test hiệu năng | Lỗi hoặc ghi chú |
|---|---|---|---|---|

**Hoàn thành khi:** Phân biệt được **request timeout**, **test hiệu năng FAIL**, và **hủy thủ công**.

Thời gian xử lý model thay đổi theo máy; không giả định request chắc chắn mất hơn 1 giây. Timeout `0` tắt giới hạn chờ của Postman. [learning.postman.com](https://learning.postman.com/docs/getting-started/installation/settings/general-settings)

---

**10. Tự động đánh giá model với nhiều dữ liệu — Nâng cao**

**Endpoint:** `POST {{base_url}}/api/chat`

Xây dựng bài kiểm tra **phân loại cảm xúc** với đầu ra:

```json
{
  "sentiment": "positive"
}
```

Tạo dữ liệu đầu vào gồm:

| text | expected |
|---|---|
| I love this product. | positive |
| This is terrible. | negative |
| The package arrived on Tuesday. | neutral |
| Excellent service! | positive |
| The app crashes every time I open it. | negative |
| The box contains three cables. | neutral |

Yêu cầu:

- Tạo file CSV hoặc JSON từ bảng trên.
- Dùng Collection Runner trên máy để chạy một lượt cho mỗi dòng.
- Dùng JSON Schema giới hạn `sentiment` trong `positive`, `negative`, `neutral`.
- Đọc kết quả mong đợi bằng `pm.iterationData.get("expected")`.
- Kiểm tra riêng: HTTP status, cấu trúc JSON, nhãn dự đoán và thời gian phản hồi.
- Tính tỷ lệ phân loại đúng:

$$
\text{Accuracy} = \frac{\text{Số câu phân loại đúng}}{\text{Tổng số câu}} \times 100\%
$$

**Hoàn thành khi:** Có báo cáo kết quả cả 6 câu, accuracy và các trường hợp sai. API trả `200` nhưng phân loại sai vẫn phải được ghi nhận là lỗi chất lượng model.

Postman hỗ trợ chạy collection với dữ liệu CSV/JSON và truy cập từng dòng qua `pm.iterationData`. [Postman Docs](https://learning.postman.com/docs/tests-and-scripts/running-collections/test-data/working-with-data-files)