**CI/CD** là viết tắt của **Continuous Integration / Continuous Delivery (hoặc Continuous Deployment)**. Đây là cách tự động hóa quá trình từ lúc lập trình viên viết code đến lúc phần mềm chạy trên môi trường thật.

## CI – Continuous Integration (Tích hợp liên tục)

Mỗi khi lập trình viên đẩy code lên github repo chung của cả nhóm (ví dụ `git push` lên GitHub), hệ thống sẽ **tự động**:

- Build (biên dịch) project
- Chạy các bài test (unit test, integration test)
- Kiểm tra chất lượng code (lint, format, phân tích bảo mật)

Mục đích là phát hiện lỗi **sớm và nhỏ**, thay vì để nhiều người viết code riêng lẻ hàng tuần rồi mới ghép lại và gặp "merge conflict".

## CD – Continuous Delivery / Deployment

Sau khi CI thành công, phần CD sẽ đưa code đi tiếp:

- **Continuous Delivery**: code luôn ở trạng thái *sẵn sàng* để phát hành. Hệ thống tự động đóng gói và triển khai lên môi trường staging, nhưng việc đưa lên production vẫn cần **một người bấm nút duyệt**.
- **Continuous Deployment**: tự động hoàn toàn. Nếu mọi test đều qua, code được **đẩy thẳng lên production** mà không cần ai duyệt.

## Luồng điển hình (pipeline)

```
Viết code → Push lên Git → Build → Test → Đóng gói (Docker image...) 
→ Deploy staging → (Duyệt) → Deploy production → Giám sát
```

## Ví dụ cụ thể

Một project Python trên GitHub dùng **GitHub Actions**: mỗi lần push, workflow sẽ cài thư viện, chạy `pytest` và `flake8`. Nếu có test thất bại, pull request bị đánh dấu đỏ và không được merge. Khi merge vào nhánh `main`, workflow khác sẽ tự build Docker image và deploy lên server.

## Công cụ phổ biến

GitHub Actions, GitLab CI/CD, Jenkins, CircleCI, Azure DevOps, và ArgoCD (cho Kubernetes).

## Lợi ích chính

- Phát hiện bug sớm, giảm rủi ro khi phát hành
- Phát hành nhanh và thường xuyên hơn (nhiều lần mỗi ngày thay vì vài tháng một lần)
- Giảm thao tác thủ công dễ sai sót
- Tạo thói quen viết test cho cả nhóm

Workflow file của GitHub Actions dùng định dạng **YAML** (đuôi `.yml` hoặc `.yaml`), và phải đặt trong thư mục **`.github/workflows/`** ở gốc repository thì GitHub mới nhận diện được. Ví dụ: `.github/workflows/ci.yml`.

YAML là định dạng dữ liệu dạng văn bản, dùng **thụt lề bằng dấu cách** (không dùng tab) để thể hiện cấu trúc phân cấp, gần giống cách Python dùng thụt lề.

Ví dụ một workflow CI đơn giản cho project Python:

```yaml
name: Python CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Cài Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Cài thư viện
        run: pip install -r requirements.txt

      - name: Chạy test
        run: pytest
```

Các khóa chính:

- **`name`**: tên workflow, hiển thị trong tab Actions
- **`on`**: sự kiện kích hoạt (push, pull_request, lịch chạy `schedule`, chạy tay `workflow_dispatch`...)
- **`jobs`**: các công việc cần làm; mặc định các job chạy song song
- **`runs-on`**: loại máy chạy (Ubuntu, Windows, macOS)
- **`steps`**: các bước tuần tự trong một job. `uses` gọi một action có sẵn, còn `run` chạy lệnh shell

Các công cụ CI/CD khác cũng chủ yếu dùng YAML, ví dụ GitLab CI (`.gitlab-ci.yml`) và Azure Pipelines (`azure-pipelines.yml`). Riêng Jenkins là ngoại lệ, dùng `Jenkinsfile` viết bằng Groovy.

Lỗi hay gặp nhất khi mới viết là **thụt lề sai** hoặc dùng tab, khiến workflow báo lỗi cú pháp.

Trong CI/CD, bạn không dùng giao diện Collection Runner của Postman mà dùng **Newman**, công cụ dòng lệnh của Postman để chạy collection. Newman hỗ trợ file dữ liệu CSV qua tham số `-d` (hoặc `--iteration-data`), nên workflow YAML chỉ cần cài Newman rồi gọi lệnh.

## Cấu trúc thư mục gợi ý

```
repo/
├── .github/workflows/api-test.yml
└── postman/
    ├── my-api.postman_collection.json
    ├── staging.postman_environment.json
    └── users.csv
```

Collection và environment được export từ Postman (Export → Collection v2.1).

## File CSV

Dòng đầu là tên biến, mỗi dòng sau là **một lần lặp** (iteration):

```csv
username,password,expectedStatus
alice,123456,200
bob,wrongpass,401
,123456,400
```

Trong Postman, request dùng biến bằng `{{username}}`, còn trong tab Tests (script) đọc bằng `pm.iterationData`:

```javascript
pm.test("Status code đúng như mong đợi", function () {
    const expected = Number(pm.iterationData.get("expectedStatus"));
    pm.response.to.have.status(expected);
});
```

## Workflow YAML

```yaml
name: API Tests

on:
  push:
    branches: [main]
  pull_request:

jobs:
  api-test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Cài Node.js
        uses: actions/setup-node@v4
        with:
          node-version: "20"

      - name: Cài Newman và reporter HTML
        run: npm install -g newman newman-reporter-htmlextra

      - name: Chạy collection với dữ liệu CSV
        run: |
          newman run postman/my-api.postman_collection.json \
            -e postman/staging.postman_environment.json \
            -d postman/users.csv \
            -r cli,htmlextra,junit \
            --reporter-htmlextra-export reports/report.html \
            --reporter-junit-export reports/junit.xml

      - name: Lưu báo cáo
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: newman-report
          path: reports/
```

Giải thích các điểm quan trọng:

- **`-d postman/users.csv`**: tương đương chọn "Select File" trong Collection Runner. Số dòng dữ liệu quyết định số iteration.
- **`-r cli,htmlextra,junit`**: xuất kết quả ra console, báo cáo HTML dễ đọc và file JUnit XML (nhiều công cụ CI đọc được định dạng này).
- **`if: always()`**: vẫn upload báo cáo ngay cả khi test thất bại, vì đó chính là lúc cần xem báo cáo nhất.
- Nếu có test fail, Newman trả về exit code khác 0, nên job tự động bị đánh dấu đỏ.

## Lưu ý

- **Không commit mật khẩu hay API key thật** vào file environment hoặc CSV. Hãy lưu trong GitHub Secrets và truyền vào bằng `--env-var`:
  ```yaml
  run: newman run ... --env-var "apiKey=${{ secrets.API_KEY }}"
  ```
- CSV nên lưu dạng **UTF-8**, và giá trị đọc từ CSV luôn là chuỗi, nên cần ép kiểu khi so sánh số (như `Number(...)` ở trên).
- Postman cũng có công cụ chính thức mới hơn là **Postman CLI** (`postman collection run ... -d data.csv`), cho phép chạy collection trực tiếp từ workspace trên cloud bằng API key. Newman thì phù hợp hơn khi muốn lưu collection trong repo và không phụ thuộc tài khoản.

```yaml
name: API tests with Newman

# Chạy khi push/PR vào main, hoặc bấm chạy tay trong tab Actions
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  workflow_dispatch:

# Chỉ cấp quyền tối thiểu cho GITHUB_TOKEN
permissions:
  contents: read

# Push liên tiếp lên cùng nhánh thì hủy lần chạy cũ, chỉ giữ lần mới nhất
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

# Gom cấu hình vào một chỗ, đổi file/URL không cần sửa lệnh
env:
  BASE_URL: https://jsonplaceholder.typicode.com
  COLLECTION: "JSONPLaceholder CRUD.postman_collection.json"
  DATA_FILE: users_data.csv

jobs:
  api_tests:
    name: Run Postman collection
    runs-on: ubuntu-latest
    timeout-minutes: 10

    steps:
      - name: Checkout code
        uses: actions/checkout@v7

      - name: Setup Node.js
        uses: actions/setup-node@v7
        with:
          node-version: 22
          package-manager-cache: false   # repo không có package-lock.json

      - name: Install Newman and HTML reporter
        run: npm install --global newman newman-reporter-htmlextra

      - name: Check test files exist
        run: |
          test -f "$COLLECTION" || { echo "::error::Không tìm thấy collection: $COLLECTION"; exit 1; }
          test -f "$DATA_FILE"  || { echo "::error::Không tìm thấy data file: $DATA_FILE"; exit 1; }

      - name: Run Postman tests
        run: |
          mkdir -p reports
          newman run "$COLLECTION" \
            --env-var "baseUrl=$BASE_URL" \
            --iteration-data "$DATA_FILE" \
            --timeout-request 10000 \
            --delay-request 100 \
            --color on \
            --reporters cli,junit,htmlextra \
            --reporter-junit-export reports/junit.xml \
            --reporter-htmlextra-export reports/report.html \
            --reporter-htmlextra-title "JSONPlaceholder CRUD - Run #${{ github.run_number }}"

      # Luôn upload báo cáo, kể cả khi test fail (lúc đó mới cần xem nhất)
      - name: Upload test reports
        if: always()
        uses: actions/upload-artifact@v7
        with:
          name: newman-reports-${{ github.run_number }}
          path: reports/
          retention-days: 14

  deploy_demo:
    name: Deploy (demo)
    needs: api_tests
    # Chỉ deploy khi push vào main, không deploy từ pull request
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    timeout-minutes: 5
    environment: demo   # Có thể bật "Required reviewers" trong Settings > Environments để duyệt tay

    steps:
      - name: Simulate deploy
        run: |
          echo "API tests passed - deploying commit ${GITHUB_SHA::7}"
          {
            echo "## Deploy demo"
            echo "- Commit: \`${GITHUB_SHA::7}\`"
            echo "- Người push: ${{ github.actor }}"
            echo "- Kết quả: tests passed, deploy được phép"
          } >> "$GITHUB_STEP_SUMMARY"
```