# yfinance trong Python — Ví dụ thực hành và 15 bài tập có lời giải

**Ngôn ngữ:** Python · **Trình độ:** cơ bản → trung bình · **Ngày đối chiếu tài liệu:** 01/10/2026

Tài liệu gồm hướng dẫn cài đặt, 8 ví dụ, 15 đề bài và lời giải ở cuối. Bạn nên làm đề trước khi đọc lời giải. Các mã chứng khoán chỉ được dùng làm dữ liệu cho bài tập lập trình.

## Mục lục

1. [Chuẩn bị môi trường](#1-chuan-bi)
2. [Hiểu dữ liệu và cú pháp](#2-kien-thuc)
3. [8 ví dụ sử dụng](#3-vi-du)
4. [15 bài tập](#4-bai-tap)
5. [Lời giải](#5-loi-giai)
6. [Lỗi thường gặp](#6-loi-thuong-gap)
7. [Nguồn tham khảo](#7-nguon)

<a id="1-chuan-bi"></a>

## 1. Chuẩn bị môi trường

### 1.1. yfinance là gì?

`yfinance` là thư viện Python lấy dữ liệu từ Yahoo Finance: lịch sử giá, thông tin doanh nghiệp, cổ tức và báo cáo tài chính. Đây là dự án mã nguồn mở độc lập, không phải SDK chính thức do Yahoo phát hành. Trang dự án mô tả mục đích nghiên cứu, học tập và lưu ý dữ liệu Yahoo Finance dành cho sử dụng cá nhân; xem điều khoản nguồn nếu dùng cho mục đích khác. [S1]

Trong các ví dụ thông thường dưới đây, bạn không cần tự cung cấp API key, URL hay gọi `requests.get()`. Thư viện xử lý việc giao tiếp với dịch vụ và thường trả về đối tượng pandas hoặc `dict`.

```python
import yfinance as yf

stock = yf.Ticker("AAPL")
df = stock.history(period="1mo", auto_adjust=True)
print(df.head())
```

`yf.Ticker("AAPL")` tạo đối tượng đại diện cho mã Apple. Việc gọi `history()` yêu cầu dữ liệu lịch sử. Tạo đối tượng thành công chưa chứng minh mã đó hợp lệ hay dữ liệu tải được.

### 1.2. Cài đặt trên Windows

Mở **Command Prompt (CMD)** trong thư mục bài tập rồi chạy:

```bat
py -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install --upgrade yfinance pandas matplotlib
```

Nếu máy không nhận lệnh `py`, dùng `python -m venv .venv`. Trong Thonny hoặc VS Code, chọn đúng trình thông dịch của `.venv`; cài thư viện bằng Python nào thì chạy bài bằng Python đó.

Kiểm tra phiên bản đang dùng:

```bat
python -c "import sys, yfinance, pandas; print(sys.executable); print('yfinance:', yfinance.__version__); print('pandas:', pandas.__version__)"
```

Tạo `main.py`, dán một ví dụ vào rồi chạy:

```bat
python main.py
```

Không đặt tên file là `yfinance.py`, `pandas.py` hoặc `matplotlib.py` vì có thể che khuất thư viện thật.

### 1.3. Cách học và chạy mã

- **Phần ví dụ:** mỗi khối ví dụ có đủ import và chạy riêng được.
- **Phần lời giải:** chép khối **Thiết lập chung** trước, sau đó chép lời giải và lệnh gọi của bài cần chạy vào cùng file. Các bài không yêu cầu chạy lời giải bài trước.
- Các thao tác tải dữ liệu cần Internet. Dữ liệu thật có thể rỗng hoặc thay đổi; không kiểm tra bằng cách khẳng định một giá thị trường phải bằng một hằng số.
- Các đoạn mã đã được kiểm tra cú pháp và phần xử lý dữ liệu được kiểm tra bằng dữ liệu giả lập. Chưa xác minh tải trực tiếp từ Yahoo trong môi trường biên soạn.

<a id="2-kien-thuc"></a>

## 2. Hiểu dữ liệu và cú pháp

### 2.1. Các đối tượng hay dùng

| Cú pháp | Mục đích | Kết quả thường gặp |
|---|---|---|
| `yf.Ticker("AAPL")` | Làm việc với một mã | Đối tượng `Ticker` |
| `stock.history(...)` | Lấy lịch sử giá một mã | `DataFrame` |
| `yf.download(["AAPL", "MSFT"], ...)` | Tải giá nhiều mã | `DataFrame`, cần kiểm tra rỗng/`None` |
| `stock.info` | Lấy thông tin tổng quan | `dict`, có thể thiếu trường |
| `yf.Search("Apple").quotes` | Tìm mã từ tên/từ khóa | Danh sách `dict` |
| `stock.get_dividends(period="5y")` | Lấy cổ tức trong khoảng được yêu cầu | `Series` |
| `stock.get_income_stmt(pretty=True)` | Lấy báo cáo kết quả kinh doanh | `DataFrame` |

Tham khảo API tương ứng ở [S2]–[S6]. Các mã ví dụ: `AAPL` (Apple), `MSFT` (Microsoft), `GOOGL` (Alphabet). Ticker phải đúng quy ước Yahoo Finance; không phải tên công ty viết tùy ý.

### 2.2. Tham số lịch sử giá

| Tham số | Ví dụ | Cách hiểu |
|---|---|---|
| `period` | `"1mo"`, `"6mo"`, `"1y"` | Khoảng lịch sử cần lấy |
| `interval` | `"1d"`, `"5m"`, `"1wk"` | Độ dài mỗi nến/dòng dữ liệu |
| `start` | `"2025-01-01"` | Cận đầu, được tính vào khoảng |
| `end` | `"2026-01-01"` | Cận cuối, **không** được tính vào khoảng |
| `auto_adjust` | `True` / `False` | Có tự điều chỉnh OHLC hay không |
| `actions` | `True` | Kèm dữ liệu sự kiện như cổ tức, chia tách |
| `timeout` | `15` | Giới hạn chờ một yêu cầu, tính bằng giây |

Ví dụ `period="1mo", interval="1d"` nghĩa là lấy khoảng một tháng gần đây, mỗi dòng một phiên ngày; không phải lấy một dòng mỗi tháng. `1m` là một phút, `1mo` là một tháng. Dùng `period` **hoặc** cặp `start/end` trong bài này để dễ kiểm soát. [S2, S3]

### 2.3. Các cột và pandas

| Cột/cú pháp | Ý nghĩa |
|---|---|
| `Open`, `High`, `Low`, `Close` | Giá mở cửa, cao nhất, thấp nhất, đóng cửa trong nến |
| `Volume` | Khối lượng giao dịch |
| `Adj Close` | Giá đóng cửa điều chỉnh, thường có khi `auto_adjust=False` |
| `Dividends`, `Stock Splits` | Sự kiện cổ tức/chia tách khi được trả về |
| `df.index` | Nhãn thời gian của các dòng |
| `df["Close"]` | Chọn một cột, thường là `Series` với bảng một mã |
| `df[["Open", "Close"]]` | Chọn nhiều cột, giữ kiểu `DataFrame` |
| `df.iloc[-1]` | Dòng cuối theo vị trí |
| `df.loc[mask, columns]` | Lọc dòng bằng điều kiện và chọn cột |
| `df.empty` | Bảng có một trục không có phần tử; không phát hiện bảng toàn `NaN` |
| `dropna()` | Loại dữ liệu thiếu theo quy tắc được chỉ định |

**Quy ước giá:** các bài phân tích dùng `auto_adjust=True` và cột `Close` đã điều chỉnh. Khi `auto_adjust=False`, đừng gọi `Close` là giá hoàn toàn chưa từng được điều chỉnh: dữ liệu nguồn Yahoo vẫn có quy ước điều chỉnh riêng, ví dụ đối với chia tách. Không trộn hai chế độ giá khi so sánh. [S3, S8]

**Ngày giao dịch:** một tháng không nhất thiết có 30 dòng. Cuối tuần/ngày nghỉ thường không có phiên cổ phiếu. Dòng cuối của dữ liệu mới nhất có thể thuộc phiên đang diễn ra; nó không luôn là giá đóng cửa cuối cùng của một phiên đã hoàn tất.

**Cột nhiều cấp:** `yf.download()` mặc định có thể trả về `MultiIndex`. Với `group_by="column"`, `data["Close"]` là bảng có các cột ticker. Không áp dụng máy móc cách chọn cột của `Ticker.history()` cho mọi kết quả `download()`. [S2]

<a id="3-vi-du"></a>

## 3. Tám ví dụ sử dụng

### Ví dụ 1 — Tìm mã bằng tên công ty

```python
import yfinance as yf

matches = yf.Search("Apple", max_results=5, news_count=0).quotes
for item in matches:
    print(item.get("symbol"), item.get("shortname"), item.get("exchange"))
if not matches:
    print("Không có kết quả tìm kiếm.")
```

`max_results` là số kết quả tối đa. `.get()` đọc giá trị trong `dict` và trả `None` nếu khóa không tồn tại. Kiểm tra tên/sàn giao dịch trước khi chọn mã. [S5]

### Ví dụ 2 — Xem thông tin doanh nghiệp

```python
import yfinance as yf

stock = yf.Ticker("MSFT")
info = stock.info
for key in ["symbol", "longName", "sector", "currency", "marketCap"]:
    print(f"{key}: {info.get(key)}")
```

`info` là thuộc tính nên viết `stock.info`, không phải `stock.info()`. `marketCap` là vốn hóa; kiểm tra đồng tiền và loại tài sản trước khi diễn giải. Trường có thể thiếu hoặc mang giá trị `None`.

### Ví dụ 3 — Tải lịch sử một tháng

```python
import yfinance as yf

df = yf.Ticker("AAPL").history(
    period="1mo", interval="1d", auto_adjust=True, timeout=15
)
if df is None or df.empty:
    raise RuntimeError("Chưa tải được lịch sử AAPL.")

print(df[["Open", "High", "Low", "Close", "Volume"]].tail())
print("Số dòng:", len(df))
print("Kiểu chỉ mục:", type(df.index))
```

`tail()` lấy 5 dòng cuối. Không suy ra mã bị hủy niêm yết chỉ vì một lần tải thất bại.

### Ví dụ 4 — Chọn ngày và xem hai loại Close

```python
import yfinance as yf

df = yf.Ticker("AAPL").history(
    start="2025-01-01", end="2026-01-01",
    interval="1d", auto_adjust=False, timeout=15
)
if df is None or df.empty:
    raise RuntimeError("Không có dữ liệu trong khoảng đã chọn.")

columns = [c for c in ["Close", "Adj Close"] if c in df.columns]
print(df[columns].head())
```

Khoảng này lấy dữ liệu trong năm 2025, không bao gồm ngày 01/01/2026. Ngày đầu thực tế phụ thuộc lịch giao dịch.

### Ví dụ 5 — Tải nhiều mã và đọc MultiIndex

```python
import yfinance as yf

data = yf.download(
    ["AAPL", "MSFT", "GOOGL"], period="3mo", interval="1d",
    auto_adjust=True, group_by="column", multi_level_index=True,
    progress=False, threads=False, timeout=15
)
if data is None or data.empty:
    raise RuntimeError("Tải nhiều mã thất bại.")

print(data.columns)
close = data["Close"]
print(close.tail())
print("Số giá hợp lệ mỗi mã:")
print(close.count())
```

Một mã có thể tải lỗi trong khi các mã khác thành công. Kiểm tra từng cột; bảng tổng không rỗng chưa có nghĩa mọi mã đều đầy đủ.

### Ví dụ 6 — Cổ tức và chia tách

```python
import yfinance as yf

stock = yf.Ticker("AAPL")
dividends = stock.get_dividends(period="5y")
splits = stock.get_splits(period="5y")
print("Cổ tức được trả về:")
print(dividends)
print("Sự kiện chia tách được trả về:")
print(splits)
```

Chuỗi rỗng có thể do không có sự kiện trong kỳ hoặc do dữ liệu không khả dụng. Tổng cổ tức trên một cổ phiếu không phải tổng thu nhập của nhà đầu tư và không phải tỷ suất cổ tức.

### Ví dụ 7 — Báo cáo tài chính

```python
import yfinance as yf

stock = yf.Ticker("MSFT")
income = stock.get_income_stmt(freq="yearly", pretty=True)
if income is None or income.empty:
    raise RuntimeError("Chưa có báo cáo kết quả kinh doanh.")

print("Tên các chỉ tiêu:", income.index.tolist())
print("Các kỳ báo cáo:", income.columns.tolist())
print(income.head())
```

Bảng này có **hàng là chỉ tiêu**, **cột là kỳ báo cáo**; khác với bảng lịch sử giá. `freq="quarterly"` lấy theo quý. `pretty=True` yêu cầu tên hàng dễ đọc. [S6]

### Ví dụ 8 — Giá trong ngày và múi giờ Việt Nam

```python
import yfinance as yf

df = yf.Ticker("AAPL").history(
    period="5d", interval="5m", auto_adjust=True,
    prepost=False, timeout=15
)
if df is None or df.empty:
    raise RuntimeError("Chưa tải được giá trong ngày.")
if df.index.tz is None:
    raise ValueError("Chỉ mục thiếu múi giờ; cần xác định nguồn trước khi chuyển.")

local = df.tz_convert("Asia/Ho_Chi_Minh")
print(local[["Close", "Volume"]].tail())
```

`tz_convert()` đổi cách biểu diễn cùng một thời điểm. Dữ liệu intraday có giới hạn lịch sử theo Yahoo/interval; dùng khoảng ngắn và không giả định mọi interval đều tải được nhiều năm. Một nến thiếu không đồng nghĩa giá bằng 0. [S3]

<a id="4-bai-tap"></a>

## 4. Mười lăm bài tập

### Bài 1 — Tìm kiếm ticker · Dễ

Viết `search_symbols(keyword, limit=5)` trả về danh sách `dict` có ba khóa: `symbol`, `name`, `exchange`.

- Tìm bằng `yf.Search`, không tải tin tức.
- Chấp nhận tên công ty như `"Microsoft"`.
- Bỏ kết quả không có symbol, ưu tiên `shortname`, dự phòng bằng `longname`.
- Từ khóa rỗng hoặc limit không dương: báo `ValueError`.

**Kết quả:** danh sách tối đa `limit` phần tử; không có kết quả thì trả `[]`. **Gợi ý:** `.strip()`, `.get()`, vòng lặp.

### Bài 2 — Hồ sơ công ty · Dễ

Viết `company_profile(symbol)` trả `dict` với `symbol`, `name`, `sector`, `country`, `currency`, `market_cap`.

- Chỉ đọc `info` một lần.
- Không tự thay dữ liệu thiếu bằng 0; dùng `None`.
- Thử với `AAPL` và `MSFT`.

**Kết quả:** dictionary có đúng các khóa trên. **Gợi ý:** ánh xạ tên khóa của Yahoo sang tên bạn muốn.

### Bài 3 — Lịch sử giá theo năm · Dễ

Viết `history_for_year(symbol, year)` trả bảng OHLCV trong năm đã chọn.

- Dùng ngày bắt đầu 01/01 của năm và cận cuối 01/01 năm kế tiếp.
- Dùng giá điều chỉnh, sắp ngày tăng dần.
- Chỉ giữ `Open`, `High`, `Low`, `Close`, `Volume`; loại dòng thiếu các trường này.
- Không có dòng hợp lệ: báo lỗi rõ ràng.

**Thử:** `history_for_year("AAPL", 2025)`. **Gợi ý:** `start/end`, `dropna(subset=...)`.

### Bài 4 — Thống kê một mã · Dễ

Viết `price_summary(symbol, period="6mo")` tính từ các dòng đủ OHLCV:

- Số phiên quan sát; ngày đầu và cuối.
- Close đầu/cuối, Close trung bình, High lớn nhất, Low nhỏ nhất.
- Tổng Volume.

**Kết quả:** một `dict`. **Gợi ý:** `iloc`, `mean`, `max`, `min`, `sum`. High lớn nhất khác Close lớn nhất.

### Bài 5 — Lọc phiên tăng từ mở cửa · Dễ–trung bình

Viết `filter_up_days(symbol, threshold_pct=2.0)` trên dữ liệu 6 tháng.

Tính `IntradayPct = (Close / Open - 1) * 100`. Trả các phiên có `IntradayPct >= threshold_pct`, sắp tỷ lệ giảm dần, giữ `Open`, `Close`, `Volume`, `IntradayPct`.

**Gợi ý:** loại Open không dương trước khi chia. Đây là biến động mở–đóng cùng phiên, không phải lợi suất giữa hai phiên.

### Bài 6 — Lợi suất giữa các phiên · Trung bình

Viết `daily_returns(symbol, period="6mo")` trả bảng có `Close`, `Return`, `ReturnPct`, `Growth`.

- `Return[t] = Close[t] / Close[t-1] - 1`.
- `ReturnPct = Return * 100`.
- `Growth = Close / Close đầu tiên`, bắt đầu ở 1.
- Giữ `NaN` của Return ở dòng đầu; không tự điền giá thiếu.

**Gợi ý:** `pct_change(fill_method=None)`. Nếu dữ liệu có khoảng trống, tỷ lệ so với dòng trước là tỷ lệ qua khoảng trống đó, không nhất thiết đúng một phiên.

### Bài 7 — SMA và biểu đồ · Trung bình

Viết `moving_average_chart(symbol, window=20)` lấy lịch sử một năm, thêm cột `SMA`, vẽ Close và SMA, lưu thành `<symbol>_sma.png`.

- `window` phải là số nguyên dương.
- Có đủ `window` giá hợp lệ mới tính SMA.
- Hàm trả bảng chứa Close/SMA và đường dẫn ảnh.

**Gợi ý:** `rolling(window, min_periods=window).mean()`. Window tính theo dòng/phiên quan sát, không phải ngày lịch.

### Bài 8 — Tải nhiều mã · Trung bình

Viết `download_close(symbols, period="6mo")` trả bảng giá đóng cửa điều chỉnh: index là ngày, mỗi cột là một mã.

- Dùng `yf.download`, `group_by="column"`, `multi_level_index=True`.
- Chuẩn hóa chữ hoa, bỏ ticker trùng nhưng giữ thứ tự đầu vào.
- Phát hiện mã không có giá hợp lệ; không âm thầm bỏ mã tải lỗi.
- Giữ `NaN` của từng ngày để người gọi quyết định xử lý.

**Thử:** `["AAPL", "msft", "AAPL", "GOOGL"]`. **Gợi ý:** chọn nhóm `Close`, rồi `reindex(columns=...)`.

### Bài 9 — So sánh trên cùng mốc thời gian · Trung bình

Viết `compare_symbols(symbols)` lấy Close một năm, chỉ giữ những ngày **mọi mã đều có giá**.

- Chuẩn hóa mỗi chuỗi về 100 ở ngày chung đầu tiên.
- Tính `ReturnPct = (giá cuối / giá đầu - 1) * 100` trên cùng hai ngày.
- Trả bảng chuẩn hóa và bảng xếp hạng giảm dần.
- Cần ít nhất hai ngày chung.

**Gợi ý:** `dropna(how="any")`, phép chia theo cột. Không so sánh giá tuyệt đối để kết luận mã nào tăng mạnh hơn.

### Bài 10 — Khối lượng đột biến · Trung bình

Viết `volume_spikes(symbol, window=20, factor=2.0)` trên lịch sử một năm.

- Tính khối lượng trung bình của **window phiên trước**, không bao gồm phiên đang xét.
- Chọn phiên có Volume ≥ `factor × PreviousAvgVolume`.
- Trả `Volume`, `PreviousAvgVolume`, `VolumeRatio`, sắp tỷ số giảm dần.
- Loại mẫu so sánh bằng 0; window nguyên dương, factor dương.

**Gợi ý:** `Volume.shift(1).rolling(window).mean()`.

### Bài 11 — Tổng cổ tức theo năm · Trung bình

Viết `dividends_by_year(symbol, period="5y")` lấy chuỗi cổ tức và tổng hợp theo năm có dữ liệu.

- Chỉ cộng các giá trị hợp lệ do API trả về.
- Trả `DataFrame` có index `Year`, cột `DividendPerShare`.
- Chuỗi rỗng: trả bảng rỗng đúng cấu trúc, không khẳng định doanh nghiệp không trả cổ tức.

**Gợi ý:** `series.groupby(series.index.year).sum()`. Năm đầu/cuối của khoảng trượt có thể chỉ bao phủ một phần năm.

### Bài 12 — Doanh thu, lợi nhuận và biên lợi nhuận · Trung bình

Viết `income_report(symbol)` dùng báo cáo năm với `pretty=True`.

- Chọn `Total Revenue`, `Net Income` sau khi kiểm tra chúng tồn tại.
- Chuyển thành bảng mỗi dòng một kỳ; sắp kỳ tăng dần.
- Tính `NetMarginPct = Net Income / Total Revenue * 100`.
- Doanh thu 0 hoặc dữ liệu thiếu: kết quả tỷ lệ là `NaN`.
- Trả bảng và mã tiền tệ báo cáo (`financialCurrency`, có thể thiếu).

**Gợi ý:** `.loc[...]`, `.T`, `.where(...)`. Kỳ tài chính không nhất thiết trùng năm dương lịch.

### Bài 13 — Intraday và múi giờ · Trung bình

Viết `intraday_in_vietnam(symbol)` tải 5 ngày gần đây, nến 5 phút; đổi index sang `Asia/Ho_Chi_Minh`.

- Chỉ lấy giờ giao dịch thông thường (`prepost=False`).
- Nếu index thiếu múi giờ: báo lỗi, không tự gắn UTC.
- Trả 10 dòng cuối với Close và Volume.

**Gợi ý:** `.tz_convert(...)`. Đổi múi giờ không tạo thêm dữ liệu hay thay đổi giá.

### Bài 14 — Lưu dữ liệu để luyện tập offline · Trung bình

Viết `load_or_fetch(symbol, year, folder="data", refresh=False)`:

- Dùng lịch sử ngày theo năm cố định với giá điều chỉnh.
- Nếu CSV tồn tại và `refresh=False`, đọc từ CSV, không gọi Yahoo.
- Nếu chưa có file hoặc yêu cầu refresh, tải và lưu OHLCV.
- Khi lưu, chuyển index thành ngày không kèm múi giờ, giữ ngày theo sàn; khi đọc phải khôi phục `DatetimeIndex`.
- Tên file thể hiện symbol, year và chế độ `adjusted`; kiểm tra cấu trúc khi đọc.

**Gợi ý:** `Path`, `to_csv`, `read_csv(parse_dates=...)`. Đây là snapshot cho bài tập; dữ liệu điều chỉnh cũ có thể thay đổi sau sự kiện mới, nên cho phép refresh.

### Bài 15 — Lớp tổng hợp theo dõi nhiều mã · Trung bình+

Viết lớp `MarketWorkbook(symbols, period="1y")` có:

- `load()`: gọi tải nhiều mã một lần, giữ bảng Close trong đối tượng.
- `summary()`: dùng những ngày chung có đủ giá; trả `StartDate`, `EndDate`, `FirstClose`, `LastClose`, `ReturnPct`, `DailyVolPct` theo ticker. `DailyVolPct` là độ lệch chuẩn mẫu của lợi suất từng bước × 100, **không** thường niên hóa.
- `export(folder="report")`: lưu bảng Close và bảng thống kê thành hai CSV, trả đường dẫn.
- Gọi thống kê trước `load()`: báo `RuntimeError`; dữ liệu quá ngắn: báo lỗi.
- Gọi `summary()` nhiều lần không tải lại dữ liệu.

**Gợi ý:** `self`, phương thức, lưu `DataFrame` vào thuộc tính. Đây là bài tổng hợp tải API → xử lý pandas → xuất kết quả.

<a id="5-loi-giai"></a>

## 5. Lời giải

### Thiết lập chung — chép trước lời giải bài bạn muốn chạy

Các hàm dưới đây giúp lời giải tập trung vào nội dung từng bài. Nếu đổi các mã ví dụ sang mã thị trường khác, kiểm tra lịch giao dịch, đồng tiền và dữ liệu thiếu trước khi so sánh.

```python
# COMMON_SETUP
from pathlib import Path
import math
import re

import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

OHLCV = ["Open", "High", "Low", "Close", "Volume"]


def clean_symbol(symbol):
    if not isinstance(symbol, str) or not symbol.strip():
        raise ValueError("symbol phải là chuỗi không rỗng.")
    return symbol.strip().upper()


def clean_symbols(symbols):
    if isinstance(symbols, str):
        symbols = [symbols]
    result = list(dict.fromkeys(clean_symbol(s) for s in symbols))
    if not result:
        raise ValueError("Danh sách mã không được rỗng.")
    return result


def positive_int(value, name):
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} phải là số nguyên dương.")


def year_bounds(year):
    if isinstance(year, bool) or not isinstance(year, int) or not 1900 <= year <= 9998:
        raise ValueError("year phải là số nguyên trong [1900, 9998].")
    return f"{year}-01-01", f"{year + 1}-01-01"


def require_table(df, label):
    if df is None or df.empty:
        raise ValueError(f"{label}: không có dữ liệu; kiểm tra mã, khoảng ngày và kết nối.")
    return df


def fetch_history(symbol, *, period=None, start=None, end=None, interval="1d"):
    symbol = clean_symbol(symbol)
    if period is not None and (start is not None or end is not None):
        raise ValueError("Chọn period hoặc start/end, không dùng cả hai trong hàm này.")
    if (start is None) != (end is None):
        raise ValueError("Cần cung cấp cả start lẫn end.")

    params = dict(interval=interval, auto_adjust=True, actions=True,
                  prepost=False, timeout=15, raise_errors=True)
    if start is not None:
        params.update(start=start, end=end)
    else:
        params["period"] = period or "1mo"

    df = yf.Ticker(symbol).history(**params)
    return require_table(df, symbol).sort_index()


def clean_ohlcv(df):
    missing = [c for c in OHLCV if c not in df.columns]
    if missing:
        raise ValueError(f"Thiếu cột OHLCV: {missing}")
    result = df[OHLCV].apply(pd.to_numeric, errors="coerce")
    result = result.dropna(subset=OHLCV).sort_index().copy()
    return require_table(result, "OHLCV hợp lệ")


def valid_close(df):
    if "Close" not in df.columns:
        raise ValueError("Thiếu cột Close.")
    close = pd.to_numeric(df["Close"], errors="coerce").dropna()
    if close.empty or (close <= 0).any():
        raise ValueError("Cần có giá Close hợp lệ và dương.")
    return close.sort_index()


def fetch_close_table(symbols, period="6mo"):
    symbols = clean_symbols(symbols)
    data = yf.download(
        symbols, period=period, interval="1d", auto_adjust=True,
        group_by="column", multi_level_index=True,
        progress=False, threads=False, timeout=15
    )
    require_table(data, "Tải nhiều mã")
    if not isinstance(data.columns, pd.MultiIndex):
        raise ValueError("Cần cấu trúc MultiIndex; kiểm tra phiên bản yfinance.")
    if "Close" not in data.columns.get_level_values(0):
        raise ValueError("Kết quả tải thiếu nhóm Close.")
    close = data["Close"].reindex(columns=symbols)
    close = close.apply(pd.to_numeric, errors="coerce").sort_index()
    failed = close.columns[close.isna().all()].tolist()
    if failed:
        raise ValueError(f"Các mã chưa có giá hợp lệ: {failed}")
    if (close <= 0).any().any():
        raise ValueError("Bảng có giá không dương; cần kiểm tra nguồn.")
    return close.dropna(how="all")
```

**Giải thích:** `*` trong `fetch_history` buộc các tham số sau nó phải truyền bằng tên. `raise_errors=True` giúp lỗi của `history()` trở thành ngoại lệ để chương trình xử lý. Với `download()`, vẫn kiểm tra từng cột vì kết quả có thể chỉ tải thành công một phần. `dict.fromkeys()` loại trùng và giữ thứ tự. [S2, S3]

### Lời giải bài 1

```python
def search_symbols(keyword, limit=5):
    if not isinstance(keyword, str) or not keyword.strip():
        raise ValueError("Từ khóa không được rỗng.")
    positive_int(limit, "limit")
    quotes = yf.Search(keyword.strip(), max_results=limit, news_count=0).quotes
    result = []
    for item in quotes:
        if item.get("symbol"):
            result.append({
                "symbol": item["symbol"],
                "name": item.get("shortname") or item.get("longname"),
                "exchange": item.get("exchange"),
            })
    return result[:limit]


print(search_symbols("Microsoft"))
```

`a or b` chọn `b` nếu `a` không có giá trị hữu ích trong ngữ cảnh này. Kết quả tìm kiếm phụ thuộc dịch vụ, vì vậy không khẳng định MSFT luôn ở vị trí đầu tiên.

### Lời giải bài 2

```python
def company_profile(symbol):
    symbol = clean_symbol(symbol)
    info = yf.Ticker(symbol).info
    return {
        "symbol": info.get("symbol") or symbol,
        "name": info.get("longName") or info.get("shortName"),
        "sector": info.get("sector"),
        "country": info.get("country"),
        "currency": info.get("currency"),
        "market_cap": info.get("marketCap"),
    }


print(company_profile("AAPL"))
```

Chú ý `shortName` trong `info` khác chữ hoa/thường với `shortname` trong kết quả Search. Dữ liệu thiếu không được biến thành vốn hóa bằng 0. Nếu API phát sinh ngoại lệ, hàm để ngoại lệ truyền lên nơi gọi.

### Lời giải bài 3

```python
def history_for_year(symbol, year):
    start, end = year_bounds(year)
    df = fetch_history(symbol, start=start, end=end)
    return clean_ohlcv(df)


df = history_for_year("AAPL", 2025)
print(df.head())
print(df.tail())
assert all(df.index.year == 2025)
assert df.index.is_monotonic_increasing
assert df.columns.tolist() == OHLCV
```

Vì `end` là cận không bao gồm, dùng 01/01 năm tiếp theo để không bỏ mất phiên 31/12 nếu ngày đó có giao dịch. Nếu chọn năm đang diễn ra, chỉ nhận dữ liệu đã có.

### Lời giải bài 4

```python
def price_summary(symbol, period="6mo"):
    df = clean_ohlcv(fetch_history(symbol, period=period))
    return {
        "sessions": len(df),
        "first_date": str(df.index[0].date()),
        "last_date": str(df.index[-1].date()),
        "first_close": float(df["Close"].iloc[0]),
        "last_close": float(df["Close"].iloc[-1]),
        "mean_close": float(df["Close"].mean()),
        "highest_high": float(df["High"].max()),
        "lowest_low": float(df["Low"].min()),
        "total_volume": int(df["Volume"].sum()),
    }


print(price_summary("AAPL"))
```

`iloc[0]` và `iloc[-1]` chọn theo vị trí sau khi dữ liệu đã được sắp ngày. Thống kê chỉ đại diện những dòng hợp lệ đã nhận, không đảm bảo mọi phiên của thị trường đều hiện diện.

### Lời giải bài 5

```python
def filter_up_days(symbol, threshold_pct=2.0):
    if not math.isfinite(threshold_pct) or threshold_pct < 0:
        raise ValueError("threshold_pct phải hữu hạn và không âm.")
    df = clean_ohlcv(fetch_history(symbol, period="6mo"))
    df = df.loc[df["Open"] > 0].copy()
    df["IntradayPct"] = (df["Close"] / df["Open"] - 1) * 100
    columns = ["Open", "Close", "Volume", "IntradayPct"]
    return df.loc[df["IntradayPct"] >= threshold_pct, columns].sort_values(
        "IntradayPct", ascending=False
    )


print(filter_up_days("MSFT", 2.0))
```

`df["IntradayPct"] >= threshold_pct` tạo Series Boolean để lọc dòng. Không có phiên thỏa điều kiện thì trả bảng rỗng là kết quả hợp lệ, không phải lỗi API.

### Lời giải bài 6

```python
def daily_returns(symbol, period="6mo"):
    close = valid_close(fetch_history(symbol, period=period))
    if len(close) < 2:
        raise ValueError("Cần ít nhất hai giá Close.")
    result = close.to_frame("Close")
    result["Return"] = close.pct_change(fill_method=None)
    result["ReturnPct"] = result["Return"] * 100
    result["Growth"] = close / close.iloc[0]
    return result


result = daily_returns("AAPL")
print(result.head())
print("Thay đổi cả khoảng (%):", (result["Growth"].iloc[-1] - 1) * 100)
```

`pct_change()` trả tỷ lệ dạng thập phân: `0.02` tương ứng `2%`. Dòng đầu không có giá trước đó nên Return là `NaN`. Growth bằng `1.15` nghĩa là chuỗi giá điều chỉnh tăng 15% từ mốc đầu; đây không phải mô phỏng đầy đủ tài khoản có phí và thuế. [S7]

Không cộng các phần trăm ngày để tìm thay đổi cả khoảng: tăng 10% rồi giảm 10% tạo hệ số `1.1 × 0.9 = 0.99`, tức giảm 1%.

### Lời giải bài 7

```python
def moving_average_chart(symbol, window=20):
    positive_int(window, "window")
    symbol = clean_symbol(symbol)
    close = valid_close(fetch_history(symbol, period="1y"))
    if len(close) < window:
        raise ValueError("Không đủ giá cho cửa sổ SMA.")
    result = close.to_frame("Close")
    result["SMA"] = close.rolling(window, min_periods=window).mean()

    safe_name = re.sub(r"[^A-Za-z0-9._-]", "_", symbol)
    path = Path(f"{safe_name}_sma.png")
    fig, ax = plt.subplots(figsize=(10, 5))
    result.plot(ax=ax, linewidth=1.4)
    ax.set_title(f"{symbol}: adjusted Close and SMA({window})")
    ax.set_xlabel("Date")
    ax.set_ylabel("Adjusted price (quote currency)")
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)
    return result, path


result, image_path = moving_average_chart("AAPL", 20)
print(result.tail())
print("Đã lưu:", image_path.resolve())
```

Với SMA20, 19 dòng đầu chưa đủ dữ liệu nên là `NaN`. Trung bình ở dòng thứ 20 gồm dòng đang xét và 19 dòng trước. Lưu rồi đóng figure giúp chạy lại nhiều lần không giữ các cửa sổ đồ thị không cần thiết. [S9]

### Lời giải bài 8

```python
def download_close(symbols, period="6mo"):
    return fetch_close_table(symbols, period)


close = download_close(["AAPL", "msft", "AAPL", "GOOGL"])
print(close.tail())
print("Số dòng thiếu mỗi mã:")
print(close.isna().sum())
assert close.columns.tolist() == ["AAPL", "MSFT", "GOOGL"]
```

Toàn bộ bước tải và xử lý `MultiIndex` nằm trong `fetch_close_table` của thiết lập chung. `reindex(columns=symbols)` vừa giữ thứ tự vừa tạo cột `NaN` cho mã bị thiếu, giúp phát hiện lỗi. Chưa xóa các ngày thiếu một vài mã để tránh che giấu tình trạng dữ liệu.

### Lời giải bài 9

```python
def compare_symbols(symbols):
    common = fetch_close_table(symbols, "1y").dropna(how="any")
    if len(common) < 2:
        raise ValueError("Cần ít nhất hai ngày có giá cho mọi mã.")
    first = common.iloc[0]
    last = common.iloc[-1]
    normalized = common.div(first, axis="columns") * 100
    ranking = ((last / first - 1) * 100).rename("ReturnPct").to_frame()
    ranking["StartDate"] = str(common.index[0].date())
    ranking["EndDate"] = str(common.index[-1].date())
    return normalized, ranking.sort_values("ReturnPct", ascending=False)


normalized, ranking = compare_symbols(["AAPL", "MSFT", "GOOGL"])
print(normalized.head())
print(ranking)
```

`axis="columns"` căn từng giá trị của Series `first` với cột cùng tên. Mọi mã bắt đầu ở 100 nên so sánh được phần trăm thay đổi. Khi dùng mã ở nhiều sàn, giao điểm ngày có thể làm mất nhiều dòng; cần hiểu sự khác nhau về lịch giao dịch.

### Lời giải bài 10

```python
def volume_spikes(symbol, window=20, factor=2.0):
    positive_int(window, "window")
    if not math.isfinite(factor) or factor <= 0:
        raise ValueError("factor phải hữu hạn và dương.")
    df = fetch_history(symbol, period="1y")
    if "Volume" not in df.columns:
        raise ValueError("Thiếu cột Volume.")
    volume = pd.to_numeric(df["Volume"], errors="coerce")
    volume = volume.where(volume >= 0)
    if volume.notna().sum() < window + 1:
        raise ValueError("Cần ít nhất window + 1 khối lượng hợp lệ.")
    baseline = volume.shift(1).rolling(window, min_periods=window).mean()
    result = pd.DataFrame({"Volume": volume, "PreviousAvgVolume": baseline})
    result["VolumeRatio"] = volume / baseline.where(baseline > 0)
    return result.loc[result["VolumeRatio"] >= factor].sort_values(
        "VolumeRatio", ascending=False
    )


print(volume_spikes("AAPL", window=20, factor=2.0))
```

`shift(1)` đưa khối lượng của phiên trước vào vị trí hiện tại trước khi tính rolling. Nếu bỏ `shift(1)`, phiên khối lượng lớn sẽ tự kéo mức tham chiếu lên. NaN trong cửa sổ làm baseline thiếu; không được tự hiểu là khối lượng bằng 0.

### Lời giải bài 11

```python
def dividends_by_year(symbol, period="5y"):
    dividends = yf.Ticker(clean_symbol(symbol)).get_dividends(period=period)
    empty = pd.DataFrame(
        {"DividendPerShare": pd.Series(dtype="float64")},
        index=pd.Index([], name="Year", dtype="int64")
    )
    if dividends is None or dividends.empty:
        return empty
    dividends = pd.to_numeric(dividends, errors="coerce").dropna()
    if dividends.empty:
        return empty
    result = dividends.groupby(dividends.index.year).sum().sort_index()
    result.index.name = "Year"
    return result.rename("DividendPerShare").to_frame()


result = dividends_by_year("AAPL")
if result.empty:
    print("Không có dữ liệu cổ tức được trả về trong khoảng yêu cầu.")
else:
    print(result)
```

Không chèn năm vắng mặt với giá trị 0 vì chưa phân biệt được không có sự kiện và thiếu dữ liệu. Kết quả cộng số tiền trên mỗi cổ phiếu theo dữ liệu nguồn; không nhân với số cổ phiếu đang nắm giữ và không tự suy ra lợi nhuận đầu tư.

### Lời giải bài 12

```python
def income_report(symbol):
    stock = yf.Ticker(clean_symbol(symbol))
    income = stock.get_income_stmt(freq="yearly", pretty=True)
    require_table(income, "Báo cáo kết quả kinh doanh")
    metrics = ["Total Revenue", "Net Income"]
    missing = [name for name in metrics if name not in income.index]
    if missing:
        raise ValueError(f"Báo cáo thiếu các chỉ tiêu: {missing}")

    result = income.loc[metrics].T.copy()
    result.index = pd.to_datetime(result.index)
    result = result.sort_index().apply(pd.to_numeric, errors="coerce")
    result.index.name = "PeriodEnd"
    revenue = result["Total Revenue"]
    result["NetMarginPct"] = result["Net Income"] / revenue.where(revenue != 0) * 100
    currency = stock.info.get("financialCurrency")
    return result, currency


report, currency = income_report("MSFT")
print("Đồng tiền báo cáo:", currency)
print(report)
```

`.T` hoán đổi hàng và cột. `where(revenue != 0)` thay doanh thu 0 bằng `NaN` trước phép chia. Ví dụ toán học: doanh thu 1.000, lợi nhuận 200 thì biên lợi nhuận là 20%. `financialCurrency` nói về báo cáo, có thể khác đồng tiền niêm yết.

### Lời giải bài 13

```python
def intraday_in_vietnam(symbol):
    df = fetch_history(symbol, period="5d", interval="5m")
    if not isinstance(df.index, pd.DatetimeIndex) or df.index.tz is None:
        raise ValueError("Chỉ mục phải là thời gian đã có múi giờ.")
    missing = [c for c in ["Close", "Volume"] if c not in df.columns]
    if missing:
        raise ValueError(f"Thiếu cột: {missing}")
    local = df.tz_convert("Asia/Ho_Chi_Minh")
    return local[["Close", "Volume"]].tail(10)


print(intraday_in_vietnam("AAPL"))
```

Thiết lập chung đã đặt `prepost=False`. Không dùng `tz_localize("UTC")` lên dữ liệu không rõ múi giờ gốc: thao tác đó gán nghĩa mới cho nhãn thời gian thay vì chuyển đúng thời điểm.

### Lời giải bài 14

```python
def load_or_fetch(symbol, year, folder="data", refresh=False):
    symbol = clean_symbol(symbol)
    start, end = year_bounds(year)
    # Giới hạn tên để dùng an toàn và nhất quán làm tên file trong bài này.
    if not re.fullmatch(r"[A-Z0-9.^=_-]+", symbol):
        raise ValueError("Mã chứa ký tự không hỗ trợ cho tên file bài tập.")
    directory = Path(folder)
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f"{symbol}_{year}_1d_adjusted.csv"

    if path.exists() and not refresh:
        df = pd.read_csv(path, index_col="Date", parse_dates=["Date"])
        if not isinstance(df.index, pd.DatetimeIndex):
            raise ValueError("CSV có ngày không hợp lệ; thử refresh=True.")
        if df.index.hasnans or df.index.has_duplicates:
            raise ValueError("CSV có ngày thiếu/trùng; thử refresh=True.")
        if df.index.tz is not None or not (df.index.year == year).all():
            raise ValueError("CSV không đúng quy ước ngày/năm; thử refresh=True.")
        return clean_ohlcv(df)

    df = clean_ohlcv(fetch_history(symbol, start=start, end=end))
    # Đây là dữ liệu ngày: bỏ tz nhưng giữ ngày theo sàn, không đổi sang UTC.
    if df.index.tz is not None:
        df.index = df.index.tz_localize(None)
    df.index = df.index.normalize()
    df.index.name = "Date"
    df.to_csv(path, index_label="Date", encoding="utf-8")
    return df


first = load_or_fetch("AAPL", 2025)
second = load_or_fetch("AAPL", 2025)  # Đọc CSV nếu lần đầu đã lưu thành công.
print(second.tail())
```

Hàm chủ động lưu quy ước ngày đơn giản vì bài chỉ dùng nến ngày. Không dùng cách bỏ múi giờ này cho bài intraday. CSV được lưu trong thư mục làm việc của chương trình. Muốn lấy bản mới: `load_or_fetch("AAPL", 2025, refresh=True)`.

### Lời giải bài 15

```python
class MarketWorkbook:
    def __init__(self, symbols, period="1y"):
        self.symbols = clean_symbols(symbols)
        self.period = period
        self.close = None

    def load(self):
        # Xóa dữ liệu cũ để lần tải lỗi không bị hiểu là đã tải mới thành công.
        self.close = None
        self.close = fetch_close_table(self.symbols, self.period)
        return self.close.copy()

    def summary(self):
        if self.close is None:
            raise RuntimeError("Cần gọi load() thành công trước summary().")
        common = self.close.dropna(how="any")
        if len(common) < 3:
            raise ValueError("Cần ít nhất ba ngày chung để có hai mức lợi suất.")
        returns = common.pct_change(fill_method=None).iloc[1:]
        first, last = common.iloc[0], common.iloc[-1]
        result = pd.DataFrame({
            "FirstClose": first,
            "LastClose": last,
            "ReturnPct": (last / first - 1) * 100,
            "DailyVolPct": returns.std(ddof=1) * 100,
        })
        result["StartDate"] = str(common.index[0].date())
        result["EndDate"] = str(common.index[-1].date())
        result.index.name = "Symbol"
        columns = ["StartDate", "EndDate", "FirstClose", "LastClose",
                   "ReturnPct", "DailyVolPct"]
        return result[columns].sort_values("ReturnPct", ascending=False)

    def export(self, folder="report"):
        summary = self.summary()
        directory = Path(folder)
        directory.mkdir(parents=True, exist_ok=True)
        prices_path = directory / "adjusted_close.csv"
        summary_path = directory / "summary.csv"
        self.close.to_csv(prices_path, index_label="Date", encoding="utf-8")
        summary.to_csv(summary_path, index_label="Symbol", encoding="utf-8")
        return prices_path, summary_path


book = MarketWorkbook(["AAPL", "MSFT", "GOOGL"])
book.load()
print(book.summary())
for path in book.export():
    print("Đã lưu:", path.resolve())
```

`self.close` là trạng thái của đối tượng; các phương thức dùng lại dữ liệu đã tải. `ddof=1` tính độ lệch chuẩn mẫu. Khi chuỗi không thiếu phiên, `DailyVolPct` mô tả biến động lợi suất ngày trong mẫu. Nếu lọc ngày chung tạo khoảng trống, đó là biến động giữa các quan sát còn lại; phải kiểm tra dữ liệu trước khi gọi nó là biến động đúng một ngày.

### Tự kiểm tra phép tính mà không cần Internet

Khối sau dùng **dữ liệu giả lập**, không phải giá thật. Nó giúp bạn kiểm tra công thức mà không phụ thuộc Yahoo.

```python
import pandas as pd
from math import isclose

close = pd.Series([100.0, 110.0, 99.0])
r = close.pct_change(fill_method=None)
assert pd.isna(r.iloc[0])
assert isclose(r.iloc[1], 0.10)
assert isclose(r.iloc[2], -0.10)
assert isclose(close.iloc[-1] / close.iloc[0] - 1, -0.01)

sma = close.rolling(2, min_periods=2).mean()
assert pd.isna(sma.iloc[0])
assert isclose(sma.iloc[1], 105.0)
assert isclose(sma.iloc[2], 104.5)

volume = pd.Series([100.0, 200.0, 600.0])
previous_avg = volume.shift(1).rolling(2, min_periods=2).mean()
assert isclose(previous_avg.iloc[2], 150.0)
assert isclose(volume.iloc[2] / previous_avg.iloc[2], 4.0)

print("Các kiểm tra công thức đều đạt.")
```

<a id="6-loi-thuong-gap"></a>

## 6. Lỗi thường gặp và cách kiểm tra

| Hiện tượng | Cần kiểm tra | Cách xử lý |
|---|---|---|
| `ModuleNotFoundError: yfinance` | Đúng interpreter chưa? | Chạy `python -m pip install yfinance` bằng Python đang chạy file |
| `KeyError: 'Adj Close'` | Đang dùng `auto_adjust=True`? | Dùng Close điều chỉnh, hoặc yêu cầu `auto_adjust=False` rồi kiểm tra cột |
| `KeyError` khi đọc nhiều mã | `data.columns` có phải MultiIndex? | In cấu trúc cột và chọn đúng nhóm `Close` |
| Bảng rỗng/toàn NaN | Mã, ngày, kết nối, giới hạn nguồn | Kiểm tra từng mã và thu hẹp khoảng; không tính tiếp trên bảng rỗng |
| Không có cuối tuần | Lịch giao dịch của tài sản | Không tự thêm giá 0 vào ngày nghỉ |
| Số dòng không bằng số ngày | Khoảng lịch khác số phiên | Đếm các quan sát nhận được; không assert số phiên tùy ý |
| HTTP 429/rate limit | Gọi quá nhiều hoặc nguồn giới hạn | Dừng, đợi rồi thử lại; dùng dữ liệu đã lưu, tránh vòng lặp gọi liên tục |
| `info` thiếu trường | Từng tài sản có dữ liệu khác nhau | Dùng `.get()`, giữ None, không mặc định bằng 0 |
| Giá thay đổi khi tải lại | Phiên chưa kết thúc hoặc điều chỉnh lịch sử | Ghi rõ thời điểm tải, tham số, chế độ điều chỉnh |
| Sai giờ intraday | Múi giờ của index | Kiểm tra `.index.tz`; dùng `tz_convert` khi đã biết tz |
| CSV đọc xong không có DatetimeIndex | Chưa parse cột ngày | Dùng `parse_dates`, `index_col`, kiểm tra lại dtype |

Cách bắt lỗi tại nơi chạy chương trình, sau khi đã chép thiết lập chung và lời giải bài 3:

```python
try:
    result = history_for_year("AAPL", 2025)
    print(result.tail())
except Exception as exc:
    print(f"Không hoàn thành: {type(exc).__name__}: {exc}")
```

Bắt `Exception` ở điểm chạy chính giúp bài học hiển thị thông báo thay vì dừng bằng traceback dài. Khi phát triển hoặc cần sửa lỗi, để ngoại lệ hiện đầy đủ; đừng dùng `except: pass` vì sẽ giấu vấn đề.

<a id="7-nguon"></a>

## 7. Nguồn tham khảo chính thức

Các hướng dẫn được đối chiếu ngày **01/10/2026**. Code ví dụ, đề bài và lời giải được biên soạn cho tài liệu này; tên trường và khả năng cung cấp dữ liệu có thể phụ thuộc phiên bản/thị trường.

- **[S1]** [yfinance trên PyPI — giới thiệu và cài đặt](https://pypi.org/project/yfinance/)
- **[S2]** [yfinance.download — tham số và MultiIndex](https://ranaroussi.github.io/yfinance/reference/api/yfinance.download.html)
- **[S3]** [PriceHistory.history — ngày, interval, điều chỉnh và ngoại lệ](https://ranaroussi.github.io/yfinance/reference/yfinance.price_history.html)
- **[S4]** [Ticker — thông tin, cổ tức và các phương thức](https://ranaroussi.github.io/yfinance/reference/api/yfinance.Ticker.html)
- **[S5]** [Search & Lookup — tìm mã](https://ranaroussi.github.io/yfinance/reference/yfinance.search.html)
- **[S6]** [get_income_stmt — báo cáo kết quả kinh doanh](https://ranaroussi.github.io/yfinance/reference/api/yfinance.Ticker.get_income_stmt.html)
- **[S7]** [pandas.Series.pct_change — tỷ lệ thay đổi](https://pandas.pydata.org/docs/reference/api/pandas.Series.pct_change.html)
- **[S8]** [Mã nguồn yfinance — xử lý lịch sử giá](https://github.com/ranaroussi/yfinance/blob/main/yfinance/scrapers/history.py)
- **[S9]** [pandas.DataFrame.rolling — cửa sổ trượt](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html)
