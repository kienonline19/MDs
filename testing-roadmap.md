# Lộ Trình Học Testing 10 Buổi

## Buổi 1 — Nhập môn Testing & Tư duy kiểm thử
- Testing là gì, vì sao quan trọng (functional vs non-functional)
- Test case, test plan, bug report cơ bản
- **Thực hành:** Viết 5 test case cho 1 form đăng nhập đơn giản

## Buổi 2 — Testing cơ bản cho hệ thống AI/Chatbot
- Đặc thù khi test AI: output không cố định (non-deterministic)
- Các loại lỗi thường gặp: hallucination, sai ngữ cảnh, trả lời lệch chủ đề
- **Thực hành:** Thử chat với 1 chatbot AI, ghi lại 5 case lỗi

## Buổi 3 — Thiết kế Test Case cho AI Mode
- Kỹ thuật viết prompt test: happy path, edge case, adversarial (prompt injection nhẹ)
- Bộ tiêu chí đánh giá: độ chính xác, độ liên quan, an toàn (safety), giọng điệu
- **Thực hành:** Xây dựng checklist 15 tiêu chí đánh giá 1 chatbot

## Buổi 4 — Giới thiệu API & Postman
- REST API là gì: method (GET/POST/PUT/DELETE), status code, JSON
- Cài đặt Postman, tạo Collection, Environment
- **Thực hành:** Gọi thử 1 API công khai (vd: weather API), xem response

## Buổi 5 — API Testing cơ bản với Postman
- Viết request có params, headers, body
- Kiểm tra response: status code, schema, dữ liệu trả về
- **Thực hành:** Test đầy đủ CRUD cho 1 API mẫu (vd: JSONPlaceholder)

## Buổi 6 — Test API cho hệ thống AI (LLM API)
- Đặc thù: test API gọi model AI (vd: chat completion endpoint)
- Kiểm tra: format response, streaming, timeout, token limit, lỗi rate-limit
- **Thực hành:** Gọi thử 1 API chatbot/LLM bằng Postman, kiểm tra response

## Buổi 7 — Viết Test Script tự động trong Postman
- Postman Tests tab: dùng JavaScript (pm.test, pm.expect)
- Assertion cơ bản: status code, response time, giá trị field
- **Thực hành:** Viết 5 script test tự động cho các API đã học

## Buổi 8 — Kịch bản test nâng cao cho AI workflow
- Test chuỗi hội thoại nhiều bước (multi-turn conversation)
- Test edge case: input rỗng, input độc hại, input đa ngôn ngữ
- **Thực hành:** Xây bộ test 10 kịch bản cho 1 luồng chatbot hỗ trợ khách hàng

## Buổi 9 — Tự động hóa & Chạy hàng loạt
- Postman Collection Runner, Newman (CLI)
- Kết hợp dữ liệu test từ file CSV/JSON (data-driven testing)
- **Thực hành:** Chạy 1 collection với 5 bộ dữ liệu khác nhau

## Buổi 10 — Tổng kết & Dự án thực hành
- Ghép toàn bộ kiến thức: test case AI + API test tự động
- Viết báo cáo test (test report) chuyên nghiệp
- **Thực hành cuối khóa:** Test toàn diện 1 chatbot AI qua API (10-15 test case + script tự động)

