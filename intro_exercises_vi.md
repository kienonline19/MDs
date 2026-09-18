# Bài tập NumPy và pyplot

**Bản dịch tiếng Việt, hướng giải và mã Python minh họa**

Nguồn đề bài: `intro_exercises.pdf` do người dùng cung cấp, 10 trang, gồm 26 bài. Tài liệu PDF không kèm lời giải; các phần **Hướng giải**, **Mã minh họa** và **Lưu ý** dưới đây được biên soạn bổ sung. Giữ nguyên số thứ tự, các yêu cầu chính, câu hỏi mở rộng và ví dụ của đề. Những chỗ diễn đạt chưa chính xác hoặc phụ thuộc phiên bản được chú thích riêng, không sửa ngầm nội dung gốc.

## Hướng dẫn chung

**Dịch từ đề gốc:** Trong các bài tập này, “mảng” có nghĩa là `numpy.ndarray`. Nếu không chỉ định kiểu, hãy giả định kiểu số thực mặc định, thường là `np.float64`. Không cần kiểm tra tính hợp lệ của đối số. Hãy sử dụng slicing và các phương thức có sẵn của mảng nhiều nhất có thể; nói cách khác, cố gắng tránh vòng lặp `for`.

**Cách dùng phần lời giải:** Chạy phần import chung trước, sau đó chạy mã của từng bài. Các biến minh họa có thể được dùng lại giữa những khối mã trong cùng bài. Những hàm ở bài sau sử dụng hàm của bài trước sẽ được ghi rõ. Chỉ dùng vòng lặp khi đề yêu cầu, khi cần lặp thí nghiệm hoặc khi thuật toán có các bước thời gian nối tiếp.

```bash
python -m pip install numpy matplotlib
```

```python
import numpy as np
import matplotlib.pyplot as plt

print("NumPy:", np.__version__)
```

Quy ước của đề về kiểu mặc định không có nghĩa `np.array([1, 2])` tự tạo mảng số thực: hàm này suy luận kiểu nguyên từ dữ liệu. Các bài yêu cầu quan sát suy luận kiểu sẽ không ép `dtype=float`.

Các ví dụ được kiểm tra với NumPy 2.3.5. Đặc biệt, kết quả trộn kiểu và chuyển số ngoài miền biểu diễn có thể khác giữa NumPy 1.x và 2.x. Tài liệu tham khảo trực tuyến được đối chiếu ngày 17/09/2026.

Đã chạy 37 khối mã Python; khi kiểm tra tự động, tắt hoạt ảnh Game of Life bằng `show=False`. Đã đối chiếu các lát cắt trên nhiều độ dài, sàng với kết quả kiểm tra nguyên tố độc lập, luật Game of Life ở biên với cách tính từng ô, và mẫu gun với dữ liệu PDF. Các cảnh báo tràn số có chủ ý ở bài 1 là một phần của thí nghiệm.

## Mục lục

| Bài | Nội dung | Bài | Nội dung |
| --- | --- | --- | --- |
| [1](#bai-01) | Kiểu số nguyên | [14](#bai-14) | Gán bằng danh sách chỉ số |
| [2](#bai-02) | Tạo mảng và suy luận kiểu | [15](#bai-15) | Gán bằng mặt nạ |
| [3](#bai-03) | Mảng toàn số 1 | [16](#bai-16) | Dãy 0, 1 xen kẽ |
| [4](#bai-04) | Broadcasting cơ bản | [17](#bai-17) | Nửa đầu 1, nửa sau 0 |
| [5](#bai-05) | Tách và ghép hai nửa | [18](#bai-18) | Lấy mẫu, sin/cos và vẽ đồ thị |
| [6](#bai-06) | Slicing với bước nhảy | [19](#bai-19) | Sinh số ngẫu nhiên chuẩn |
| [7](#bai-07) | Slicing đảo chiều | [20](#bai-20) | Mảng 2D, trung bình, histogram |
| [8](#bai-08) | Đọc bằng danh sách chỉ số | [21](#bai-21) | Mẫu bàn cờ |
| [9](#bai-09) | Lấy mẫu bằng chỉ số ngẫu nhiên | [22](#bai-22) | Ghép mảng |
| [10](#bai-10) | Mặt nạ Boolean | [23](#bai-23) | Broadcasting hai mảng 1D |
| [11](#bai-11) | Chọn phần tử theo xác suất | [24](#bai-24) | Sàng Eratosthenes I |
| [12](#bai-12) | Chuyển kiểu khi gán | [25](#bai-25) | Sàng Eratosthenes II |
| [13](#bai-13) | Gán bằng slicing | [26](#bai-26) | Conway’s Game of Life |

## Thuật ngữ sử dụng

| Thuật ngữ | Nghĩa trong tài liệu |
| --- | --- |
| `dtype` | Kiểu dữ liệu của phần tử mảng |
| `shape` | Kích thước theo từng trục; ví dụ `(10, 20)` |
| index | Chỉ số, bắt đầu từ 0 |
| slicing | Lấy lát cắt bằng `start:stop:step`; không lấy vị trí `stop` |
| view | Mảng nhìn vào dữ liệu của mảng khác, không sao chép dữ liệu phần tử |
| copy | Bản sao có vùng dữ liệu riêng; với `dtype=object`, đối tượng bên trong vẫn có thể được dùng chung |
| mask | Mặt nạ Boolean dùng để chọn phần tử |
| scalar | Một giá trị đơn lẻ |
| broadcasting | Quy tắc kết hợp/gán dữ liệu có kích thước khác nhau nhưng tương thích |
| equal / identical | Bằng nhau về giá trị / là cùng một đối tượng Python |
| variance / standard deviation | Phương sai / độ lệch chuẩn |

<a id="bai-01"></a>
## 1. Các kiểu số nguyên của NumPy

### Đề bài

Tạo một biến lưu số `100` dưới dạng số nguyên 16 bit. Sau đó tạo một biến khác lưu `100` dưới dạng số nguyên **không dấu** 16 bit, thường viết tắt là `uint`. Dựa vào ghi chú bài giảng, tính giá trị nhỏ nhất và lớn nhất mà hai kiểu này có thể lưu. Kiểm chứng bằng cách thử tại các giới hạn: thực hiện phép toán chạm tới giới hạn, tiếp tục vượt giới hạn và quan sát hiện tượng giá trị quay vòng.

Thử kết hợp các kiểu số khác nhau, chẳng hạn cộng số nguyên có dấu với số nguyên không dấu. Quan sát cả giá trị và kiểu của kết quả. Thử thêm các kiểu nguyên 64 bit có dấu, không dấu và số nguyên Python thông thường, gồm cả số nhỏ lẫn số rất lớn. Nếu có thể, suy ra một nguyên tắc tổng quát, dù chưa hoàn toàn chặt chẽ, về cách chọn kiểu đầu ra khi các đầu vào khác kiểu.

### Hướng giải

Với `b` bit, số nguyên có dấu có miền `[-2**(b-1), 2**(b-1)-1]`; số nguyên không dấu có miền `[0, 2**b-1]`.

| Kiểu | Nhỏ nhất | Lớn nhất |
| --- | ---: | ---: |
| `np.int16` | -32768 | 32767 |
| `np.uint16` | 0 | 65535 |

Dùng hai toán hạng cùng kiểu để quan sát tràn số trong chính kiểu đó. Phân biệt phép toán bị tràn với việc chuyển một số Python ngoài miền sang kiểu NumPy: trường hợp thứ hai có thể phát sinh `OverflowError` trên NumPy 2.x.

### Mã minh họa

```python
x = np.int16(100)
y = np.uint16(100)
print(x, type(x), y, type(y))
print(np.iinfo(np.int16))
print(np.iinfo(np.uint16))

# Có thể xuất hiện RuntimeWarning: đây là hiện tượng đang được khảo sát.
print(np.int16(32766) + np.int16(1))   # 32767
print(np.int16(32767) + np.int16(1))   # -32768
print(np.int16(-32768) - np.int16(1))  # 32767
print(np.uint16(65534) + np.uint16(1)) # 65535
print(np.uint16(65535) + np.uint16(1)) # 0
print(np.uint16(0) - np.uint16(1))     # 65535

def show_sum(a, b):
    try:
        result = a + b
        print(repr(a), "+", repr(b), "=", repr(result), type(result))
    except (OverflowError, TypeError, ValueError) as exc:
        print(type(exc).__name__, str(exc))

show_sum(np.int16(100), np.uint16(100))
show_sum(np.int16(100), np.int64(100))
show_sum(np.int64(100), np.uint64(100))
show_sum(np.int16(100), 10)
show_sum(np.int16(100), 10**100)
show_sum(100, 10**100)
```

### Giải thích kết quả

Trên NumPy 2.x, `int16 + uint16` cho `int32`; `int64 + uint64` cho `float64`. Số thực này không biểu diễn chính xác mọi số nguyên 64 bit. Khi trộn với scalar Python, NumPy có thể giữ kiểu nguyên nhỏ và báo lỗi nếu scalar không vừa kiểu đó. Hai số `int` thuần Python không bị giới hạn ở 16 hay 64 bit. Đây là quy tắc của phép toán NumPy, không phải một quy tắc chung cho mọi phép cộng trong Python.

**Tham khảo:** [Giới hạn và kiểu dữ liệu NumPy](https://numpy.org/doc/stable/user/basics.types.html), [Quy tắc nâng kiểu](https://numpy.org/doc/stable/reference/arrays.promotion.html).

<a id="bai-02"></a>
## 2. Kiến thức cơ bản về tạo mảng NumPy I

### Đề bài

Viết một danh sách Python chứa các số nguyên rồi tạo mảng NumPy một chiều từ danh sách đó. Đọc kiểu phần tử của mảng bằng thuộc tính dành riêng cho việc này; gợi ý tên thuộc tính là viết tắt của “data type”.

Lặp lại với danh sách số thực. Sau đó thử danh sách trộn số nguyên và số thực, chẳng hạn `[1, 2.0, 3]`. Dự đoán kết quả rồi kiểm chứng.

Làm thế nào để bảo đảm kiểu phần tử là số thực ngay cả khi danh sách đầu vào chỉ chứa số nguyên? Nếu danh sách có số thực mà bạn ép kiểu phần tử thành `bool` thì sao?

Nếu danh sách có phần tử không phải số, chẳng hạn chuỗi, điều gì xảy ra? Hãy xem kỹ kết quả, lấy một phần tử bằng `a[0]`, kiểm tra bằng `type`, rồi dùng `isinstance` để xác định nó có phải một chuỗi hay không.

Nếu một hoặc nhiều phần tử là `set` hoặc `dict` thì sao? Từ kết quả đó, quay lại danh sách trộn số nguyên và số thực: trong tình huống muốn giữ nguyên kiểu từng phần tử, không chuyển kiểu ngầm, bạn làm thế nào?

Cuối cùng, nếu truyền danh sách rỗng vào hàm tạo mảng mà không chỉ định kiểu phần tử thì sao?

### Hướng giải và mã minh họa

```python
a = np.array([1, 2, 3])
b = np.array([1.5, 2.5, 3.5])
c = np.array([1, 2.0, 3])
print(a, a.dtype)
print(b, b.dtype)  # float64
print(c, c.dtype)  # [1. 2. 3.], float64

forced_float = np.array([1, 2, 3], dtype=float)
as_bool = np.array([0.0, -0.0, 0.5, -2.3], dtype=bool)
print(forced_float)
print(as_bool)     # [False False True True]

strings = np.array([1, "hello", 3.5])
print(strings, strings.dtype)
print(type(strings[0]))              # numpy.str_
print(isinstance(strings[0], str))    # True

containers = np.array([{1, 2}, {"name": "An"}])
print(containers.dtype)              # object
print(type(containers[0]))           # set
print(type(containers[1]))           # dict

preserved = np.array([1, 2.0, 3], dtype=object)
print(preserved.dtype)               # object
print(type(preserved[0]))            # int
print(type(preserved[1]))            # float

empty = np.array([])
print(empty.shape, empty.dtype)      # (0,), float64
```

Mảng số thông thường dùng chung một `dtype`, nên đầu vào `[1, 2.0, 3]` được chuyển sang số thực. Trong ví dụ trộn chuỗi, cả số cũng được chuyển thành chuỗi. `dtype=object` lưu tham chiếu đến đối tượng Python, cho phép giữ `int`, `float`, `set`, `dict` cùng một mảng. Đây không phải lựa chọn mặc định tốt cho tính toán số vì mất nhiều lợi ích của mảng số đồng nhất.

Với các số thực hữu hạn, `0.0` và `-0.0` chuyển thành `False`; giá trị khác 0 chuyển thành `True`.

**Tham khảo:** [Kiểu dữ liệu NumPy](https://numpy.org/doc/stable/user/basics.types.html).

<a id="bai-03"></a>
## 3. Kiến thức cơ bản về tạo mảng NumPy II

### Đề bài

Viết hàm nhận một đối số `n`, tạo mảng một chiều dài `n` gồm toàn số 1. Lần lượt tạo các phiên bản dùng số thực, số nguyên 64 bit, số nguyên 32 bit, Boolean và chuỗi. Với Boolean, giá trị nào tương đương 1? Mảng chuỗi toàn số 1 có nghĩa gì? Hãy đọc `dtype` của mảng và kiểu của phần tử đầu tiên.

Sau đó sửa hàm để tạo ma trận `n × n`, vẫn gồm toàn số 1, có kiểu nguyên. Quan sát kết quả khi nhân ma trận với một số nguyên, rồi với một số thực.

### Hướng giải và mã minh họa

`np.ones` nhận kích thước và kiểu dữ liệu. Mỗi hàm dưới đây chỉ nhận đối số `n` như đề yêu cầu.

```python
def ones_float(n):
    return np.ones(n, dtype=float)

def ones_int64(n):
    return np.ones(n, dtype=np.int64)

def ones_int32(n):
    return np.ones(n, dtype=np.int32)

def ones_bool(n):
    return np.ones(n, dtype=bool)

def ones_string(n):
    return np.ones(n, dtype=str)

def ones_matrix(n):
    return np.ones((n, n), dtype=np.int64)

print(ones_bool(3))                  # [ True True True]
print(ones_string(3))                # ['1' '1' '1']
s = ones_string(3)
print(s.dtype, type(s[0]))           # dtype chuỗi Unicode, numpy.str_

a = ones_matrix(2)
print(a * 3, (a * 3).dtype)          # Các phần tử bằng 3, kiểu int64
print(a * 2.5, (a * 2.5).dtype)      # Các phần tử bằng 2.5, kiểu float64
```

Chuỗi `'1'` khác số `1`: đó là ký tự biểu diễn số 1. Phép nhân ở đây tác động lên từng phần tử, không phải nhân hai ma trận. Chỉ đọc `a[0]` khi `n > 0`.

**Tham khảo:** [`np.ones`](https://numpy.org/doc/stable/reference/generated/numpy.ones.html).

<a id="bai-04"></a>
## 4. Một số kiến thức cơ bản về broadcasting

### Đề bài

Viết hàm nhận `n`, tạo mảng một chiều dài `n` chứa toàn số nguyên `-1`. Thực hiện việc tạo mảng trong một dòng. Có hàm riêng cho việc này, nhưng cũng có thể tận dụng quy tắc broadcasting đơn giản nhất. Có ít nhất bốn cách; bạn có tìm ra cả bốn không?

### Hướng giải và mã minh họa

```python
def minus_ones_1(n):
    return np.full(n, -1, dtype=int)

def minus_ones_2(n):
    return -np.ones(n, dtype=int)

def minus_ones_3(n):
    return np.zeros(n, dtype=int) - 1

def minus_ones_4(n):
    return np.ones(n, dtype=int) * -1

print(minus_ones_1(4))  # [-1 -1 -1 -1]
```

Ở cách 3 và 4, scalar được áp dụng cho mọi phần tử. Không cần tự tạo một mảng `-1` thứ hai để trừ hoặc nhân.

**Tham khảo:** [Broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html), [Các hàm tạo mảng liên quan trong tài liệu `ones`](https://numpy.org/doc/stable/reference/generated/numpy.ones.html).

<a id="bai-05"></a>
## 5. Đọc các phần của mảng

### Đề bài

Viết hàm nhận một danh sách dài `n`, chuyển nó thành mảng một chiều, rồi lấy nửa đầu và nửa sau, mỗi thao tác trong một dòng. Nếu `n` lẻ, phần tử chính giữa thuộc nửa sau.

Với danh sách Python, có thể dùng `+` để ghép hai nửa. Với mảng NumPy thì không thể dùng `+` theo nghĩa đó. Vì sao? Hãy thử cả đầu vào dài chẵn lẫn dài lẻ.

Tra cứu `np.hstack`, có thể đọc thêm `np.stack` và `np.vstack` dù chưa cần cho bài này. Dùng `hstack` ghép lại hai nửa và trả về kết quả.

Sau khi hoàn thành, dự đoán rồi kiểm chứng các câu hỏi sau:

1. Mảng kết quả là cùng một đối tượng với mảng ban đầu hay chỉ bằng nhau? Kiểm tra thế nào và khác biệt này có ý nghĩa gì?
2. Có thể dùng `==` để kiểm tra hai mảng bằng nhau không? Quan sát kết quả; tra `np.all` hoặc phương thức `.all()`, rồi dùng `assert` để kiểm tra trong hàm. Đọc thêm `np.array_equal`.
3. Hai nửa được tạo bằng slicing. Nếu sửa phần tử đầu của một nửa, mảng ban đầu có thay đổi không? In `.base` của hai nửa và xác định chúng trỏ đến đối tượng nào.

### Hướng giải và mã minh họa

```python
def split_and_join(values):
    a = np.array(values)
    k = len(a) // 2
    first = a[:k]
    second = a[k:]
    result = np.hstack((first, second))
    assert np.all(result == a)
    assert np.array_equal(result, a)
    assert result is not a
    return result

print(split_and_join([3, 5, 6, 7, 8]))  # [3 5 6 7 8]

a = np.array([10, 20, 30, 40, 50])
first, second = a[:2], a[2:]
joined = np.hstack((first, second))
print(first.base is a, second.base is a)  # True True
print(joined is a)                       # False
print(np.shares_memory(joined, a))       # False
first[0] = 999
print(a)                                # [999 20 30 40 50]
print(joined)                           # [10 20 30 40 50]

print(np.array([1, 2]) + np.array([3, 4]))     # [4 6]
print(np.array([1]) + np.array([2, 3]))        # [3 4], broadcasting
try:
    print(np.array([1, 2]) + np.array([3, 4, 5]))
except ValueError as exc:
    print(type(exc).__name__)                # Kích thước không tương thích
```

`==` trả về một mảng Boolean theo từng vị trí; `np.all` rút gọn thành một kết quả đúng/sai. `np.array_equal` kiểm tra cả kích thước lẫn giá trị; khác với `==`, nó không dựa vào broadcasting để so sánh hai kích thước khác nhau. Với dữ liệu có `NaN`, cân nhắc `np.array_equal(a, b, equal_nan=True)`.

Trong ví dụ này, slicing tạo view dùng chung dữ liệu với `a`. Hai mảng bằng nhau không nhất thiết là cùng đối tượng; hai đối tượng khác nhau vẫn có thể dùng chung bộ nhớ. `.base` có thể trỏ đến mảng gốc xa hơn trong chuỗi view, nên không luôn là mảng vừa được slicing trực tiếp.

**Tham khảo:** [`np.hstack`](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html), [`np.array_equal`](https://numpy.org/doc/stable/reference/generated/numpy.array_equal.html), [Indexing](https://numpy.org/doc/stable/user/basics.indexing.html).

<a id="bai-06"></a>
## 6. Slicing với bước nhảy I

### Đề bài

Viết hàm nhận danh sách dài `n`, giả sử `n > 0`, rồi chuyển thành mảng một chiều. Lấy các phần tử có chỉ số chẵn vào một mảng con, rồi lấy các phần tử có chỉ số lẻ vào một mảng con khác. Mỗi thao tác phải dùng đúng một biểu thức slicing trên một dòng.

Nếu thay đổi một trong hai mảng con thì mảng gốc có thay đổi không? Vì sao? Hãy kiểm chứng dự đoán bằng thí nghiệm.

### Hướng giải và mã minh họa

```python
def split_even_odd(values):
    a = np.array(values)
    even = a[::2]
    odd = a[1::2]
    return a, even, odd

a, even, odd = split_even_odd([10, 20, 30, 40, 50])
print(even)             # [10 30 50]
print(odd)              # [20 40]
even[0] = 999
print(a)                # [999 20 30 40 50]
print(even.base is a)   # True
```

“Chỉ số chẵn” là vị trí `0, 2, 4, ...`, không có nghĩa giá trị của phần tử là số chẵn. Hai kết quả đều là view. Dùng `.copy()` sau slicing nếu muốn có vùng dữ liệu riêng.

**Tham khảo:** [Slicing và bước nhảy](https://numpy.org/doc/stable/user/basics.indexing.html#slicing-and-striding).

<a id="bai-07"></a>
## 7. Slicing với bước nhảy II

### Đề bài

Viết hàm nhận danh sách dài `n`, chuyển thành mảng một chiều. Sau đó lấy các mảng con dưới đây bằng biểu thức slicing; không dùng phương thức của list hoặc mảng để thực hiện việc lấy và đảo:

1. Toàn bộ mảng theo thứ tự ngược. Ví dụ `[4, 3, 6, 8, 9]` được đọc từ `9` về `4`.
2. Nửa đầu đảo ngược, rồi nửa sau đảo ngược. Nếu `n` lẻ, phần tử giữa thuộc nửa sau. Trước tiên có thể tách như bài 5 rồi đảo như mục 1; sau đó tìm cách làm mỗi nửa bằng một slicing duy nhất. Hãy kiểm tra kỹ thay đổi tinh tế của chỉ số.
3. Các phần tử có chỉ số chẵn theo thứ tự ngược, rồi các phần tử có chỉ số lẻ theo thứ tự ngược. Trước tiên làm hai bước như bài 6 kết hợp mục 1; sau đó dùng một slicing cho mỗi kết quả. Trường hợp `n` lẻ phức tạp hơn vẻ ngoài. Có thể bắt đầu bằng biểu thức `if`, kiểm tra với độ dài chẵn và lẻ, rồi tìm cách không cần `if`.
4. Đảo ngược kết quả mục 1 một lần nữa. Kiểm tra bằng `np.array_equal`, rồi dùng `is` để kiểm tra hai mảng có cùng đối tượng hay không. Sửa kết quả và xem mảng ban đầu có thay đổi không. Dùng `.base` để giải thích. Tìm một slicing khác có cùng giá trị và đặc tính với mảng bị đảo hai lần.

Kiểm tra `.base` của kết quả ở các mục 1-3, kể cả khi làm hai bước, để xác định chúng có phải view hay không.

### Hướng giải

Đặt `k = n // 2`. Bước nhảy âm đọc từ phải sang trái. Chỉ số âm được tính từ cuối mảng; đặc biệt, `stop=-1` không đồng nghĩa với bỏ trống `stop` khi bước nhảy âm.

Các công thức sau dùng mốc âm để xử lý được cả mảng rỗng, mảng một phần tử và độ dài chẵn/lẻ. Phần dịch không bổ sung giả thiết `n > 0` vì đề bài 7 không nêu giả thiết đó.

### Mã minh họa

```python
def reverse_slices(values):
    a = np.array(values)
    n = len(a)
    k = n // 2

    whole = a[::-1]
    first = a[k - n - 1::-1]
    second = a[:k - n - 1:-1]
    even = a[-1 - (n + 1) % 2::-2]
    odd = a[-1 - n % 2::-2]
    twice = whole[::-1]

    # So sánh với cách hai bước dễ đọc hơn.
    assert np.array_equal(first, a[:k][::-1])
    assert np.array_equal(second, a[k:][::-1])
    assert np.array_equal(even, a[::2][::-1])
    assert np.array_equal(odd, a[1::2][::-1])
    assert np.array_equal(twice, a)
    assert twice is not a
    return a, whole, first, second, even, odd, twice

a, whole, first, second, even, odd, twice = reverse_slices([4, 3, 6, 8, 9])
print(whole)   # [9 8 6 3 4]
print(first)   # [3 4]
print(second)  # [9 8 6]
print(even)    # [9 6 4]
print(odd)     # [8 3]
print(whole.base is a, first.base is a, second.base is a)
print(even.base is a, odd.base is a, twice.base is a)
print(a[:len(a) // 2][::-1].base is a)

twice[0] = 100
print(a[0])    # 100
equivalent = a[:]  # Cùng thứ tự giá trị, là view mới của a.
```

Ví dụ `n=5`, `k=2`: `k-n-1=-4`, tương ứng vị trí `1`. Vì vậy `a[-4::-1]` lấy chỉ số `1, 0`, còn `a[:-4:-1]` lấy `4, 3, 2`.

Với chỉ số chẵn đảo ngược, điểm bắt đầu là `-1` nếu `n` lẻ, `-2` nếu `n` chẵn. Với chỉ số lẻ thì ngược lại. Hai công thức `% 2` mã hóa chính sự lựa chọn đó mà không cần `if`.

Không nên dùng máy móc `a[k-1::-1]`: khi `k=0`, `-1` trở thành phần tử cuối thay vì biểu diễn nửa đầu rỗng. Các slicing của bài này tạo view; view rỗng vẫn có thể có `.base`, dù không có phần tử nào để chia sẻ.

**Tham khảo:** [Quy tắc slicing với chỉ số âm](https://numpy.org/doc/stable/user/basics.indexing.html#slicing-and-striding).

<a id="bai-08"></a>
## 8. Truy cập bằng danh sách chỉ số I

### Đề bài

Viết hàm nhận danh sách dài `n`, với `n` lẻ và `n >= 1`. Chuyển thành mảng một chiều, rồi dùng một danh sách gồm ba chỉ số để lấy phần tử đầu, giữa và cuối. Ví dụ đầu vào `[4, 6, 1, 2, 0, 7, 9]` phải cho các giá trị `4, 2, 9`.

Kết quả có phải view không? Viết mã kiểm chứng.

Lưu ý: khi `n == 1`, cả ba vị trí trong danh sách chỉ số đều chỉ vào cùng phần tử. Điều đó hoàn toàn hợp lệ; kết quả vẫn có ba giá trị giống nhau. Chỉ số có thể lặp lại. Hãy thử mảng dài 3 với danh sách chỉ số `[2, 0, 1, 0, 0, 1]`: kết quả dài 6, lớn hơn mảng gốc.

### Hướng giải và mã minh họa

```python
def first_middle_last(values):
    a = np.array(values)
    return a[[0, len(a) // 2, len(a) - 1]]

print(first_middle_last([4, 6, 1, 2, 0, 7, 9]))  # [4 2 9]
print(first_middle_last([7]))                    # [7 7 7]

a = np.array([10, 20, 30])
b = a[[0, 1, 2]]
print(np.shares_memory(a, b))  # False
b[0] = 999
print(a)                      # [10 20 30]
print(a[[2, 0, 1, 0, 0, 1]])  # [30 10 20 10 10 20]
```

Đọc bằng danh sách chỉ số là advanced indexing, tạo bản sao dữ liệu. Điều này khác slicing. Với `dtype=object`, sao chép mảng không đồng nghĩa sao chép sâu các đối tượng bên trong.

**Tham khảo:** [Truy cập bằng mảng chỉ số nguyên](https://numpy.org/doc/stable/user/basics.indexing.html#integer-array-indexing).

<a id="bai-09"></a>
## 9. Truy cập bằng danh sách chỉ số II

### Đề bài

Viết hàm nhận hai đối số: một danh sách dài `n >= 1` và số nguyên không âm `m`, là độ dài mảng đầu ra. Chuyển danh sách thành mảng.

Tra hàm `randint` trong `np.random`, dùng nó tạo `m` số nguyên ngẫu nhiên thuộc `[0, n)`: có thể bằng 0 nhưng không được bằng `n`. Gợi ý: dùng đối số từ khóa `size` để mã rõ ràng hơn.

Dùng mảng chỉ số ngẫu nhiên đó để lấy phần tử từ mảng gốc. Kết quả phải dài `m`. Chạy hàm nhiều lần để quan sát các kết quả ngẫu nhiên; thử đủ các trường hợp `n < m`, `n == m`, `n > m`.

Lưu ý: bài trước dùng list Python làm chỉ số, bài này dùng mảng NumPy số nguyên. Cả hai cho cùng cơ chế truy cập; theo đề gốc, phiên bản mảng NumPy hiệu quả hơn một chút.

### Hướng giải và mã minh họa

```python
def sample_with_indices(values, m):
    a = np.array(values)
    indices = np.random.randint(0, len(a), size=m)
    return a[indices]

print(sample_with_indices([10, 20, 30], 5))  # Có thể lặp phần tử
print(sample_with_indices([10, 20, 30], 3))
print(sample_with_indices([10, 20, 30], 1))
print(sample_with_indices([10, 20, 30], 0))  # []

# Cách dùng Generator cho mã mới; tạo rng một lần ở ngoài hàm.
rng9 = np.random.default_rng(42)

def sample_with_generator(values, m):
    a = np.array(values)
    indices = rng9.integers(0, len(a), size=m)
    return a[indices]
```

Đây là lấy mẫu **có hoàn lại**: một vị trí có thể được chọn nhiều lần. Vì vậy `m` có thể lớn hơn `n`. Hai lần chạy ngẫu nhiên vẫn có thể tình cờ cho cùng kết quả; câu “mỗi lần cho kết quả khác” trong đề nên hiểu là kết quả không cố định. Tạo lại generator với cùng seed bên trong mỗi lần gọi sẽ lặp lại cùng chuỗi, nên không làm như vậy ở đây.

**Tham khảo:** [`np.random.randint`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html), [Generator và `integers`](https://numpy.org/doc/stable/reference/random/generator.html).

<a id="bai-10"></a>
## 10. Truy cập bằng mặt nạ I

### Đề bài

Viết hàm nhận danh sách dài `n`, có thể chứa cả số âm và số dương, rồi chuyển thành mảng một chiều. So sánh cả mảng với 0, chẳng hạn `a > 0`. Kết quả là gì? Hãy kiểm tra.

Dùng kết quả so sánh làm mặt nạ trong biểu thức truy cập, để lấy các phần tử **không âm**. Ví dụ `[3, -1, -2, 5, 6, -3, 8]` phải cho `3, 5, 6, 8`. Có thể thực hiện bằng một biểu thức truy cập không? Kết quả có phải view không? Viết mã kiểm chứng.

### Hướng giải và mã minh họa

**Chú thích về đề:** “Không âm” nghĩa là `>= 0`, bao gồm số 0. Biểu thức `a > 0` ở bước thăm dò chỉ chọn số dương. Ví dụ gốc không chứa 0 nên chưa làm lộ khác biệt này.

```python
def nonnegative(values):
    a = np.array(values)
    return a[a >= 0]

print(nonnegative([3, -1, -2, 5, 6, -3, 8]))  # [3 5 6 8]
print(nonnegative([-2, 0, 4]))                # [0 4]

a = np.array([-2, 0, 4])
print(a > 0)                   # [False False True]
print(a >= 0)                  # [False True True]
b = a[a >= 0]
print(np.shares_memory(a, b))   # False
b[0] = 99
print(a)                       # [-2 0 4]
```

Kết quả so sánh là mảng Boolean. Mặt nạ đánh dấu vị trí nào cần lấy bằng `True`. Đọc bằng mặt nạ tạo bản sao dữ liệu, không phải view.

**Tham khảo:** [Boolean indexing](https://numpy.org/doc/stable/user/basics.indexing.html#boolean-array-indexing).

<a id="bai-11"></a>
## 11. Truy cập bằng mặt nạ II

### Đề bài

Viết hàm nhận một danh sách dài `n` và số thực `r` từ 0 đến 1. Chuyển danh sách thành mảng. Tra hàm `random` trong `np.random`, dùng nó tạo `n` số thực ngẫu nhiên thuộc `[0.0, 1.0)`, gọi mảng đó là `s`.

So sánh `s < r` để tạo mặt nạ Boolean, rồi dùng mặt nạ lấy phần tử từ mảng ban đầu. Như vậy, mỗi phần tử được giữ với xác suất `r` và bị bỏ với xác suất `1-r`.

Kiểm tra rằng `r == 0` luôn cho kết quả rỗng, còn `r == 1` cho kết quả bằng về giá trị nhưng không cùng đối tượng với đầu vào. Kiểm tra độ dài kết quả bằng số lượng `True` trong mặt nạ. Gợi ý của đề: cộng các giá trị Boolean bằng cách xem `False` là 0, `True` là 1; với Boolean Python, `True + False == 1`, `True + True == 2`.

Viết thêm hàm thứ hai gọi lặp lại hàm đầu với cùng đối số. Hàm thứ hai nhận danh sách, `r` và số lần lặp, mặc định một số lớn như 1000. Tính độ dài trung bình của kết quả. Khi số lần lặp lớn, kiểm tra trung bình tiến gần `n*r`, kể cả khi `n*r` không nguyên, chẳng hạn 3.43. In cả trung bình quan sát được lẫn giá trị kỳ vọng để so sánh.

### Hướng giải và mã minh họa

```python
def select_with_probability(values, r):
    a = np.array(values)
    s = np.random.random(size=len(a))
    mask = s < r
    result = a[mask]
    assert len(result) == mask.sum()
    return result

def average_selected_length(values, r, iterations=1000):
    lengths = np.empty(iterations, dtype=int)
    for i in range(iterations):
        lengths[i] = len(select_with_probability(values, r))
    measured = lengths.mean()
    expected = len(values) * r
    print("Trung bình quan sát:", measured)
    print("Giá trị kỳ vọng:", expected)
    return measured

values = [10, 20, 30, 40, 50, 60, 70]
assert select_with_probability(values, 0).size == 0
assert np.array_equal(select_with_probability(values, 1), values)
average_selected_length(values, 0.49, iterations=10_000)  # Gần 3.43

a = np.array(values)
b = a[np.ones(len(a), dtype=bool)]
assert np.array_equal(a, b)
assert b is not a
assert not np.shares_memory(a, b)

mask = np.array([True, True, False])
print(mask.sum())                      # 2
print(np.bool_(True) + np.bool_(True)) # True, không phải số nguyên 2
```

Nếu `L` là số phần tử được chọn, thì `L` là tổng của `n` biến chỉ báo, mỗi biến có kỳ vọng `r`, nên `E[L] = n*r`. Trung bình thực nghiệm thường tiến gần giá trị này khi tăng số lần thử; không cần và không nên kiểm tra bằng dấu `==` với kỳ vọng.

**Lưu ý:** Dùng `mask.sum()` để đếm. Phép cộng từng phần tử của hai mảng Boolean NumPy không phải phép đếm số `True`; cũng không nên suy trực tiếp hành vi của `np.bool_ + np.bool_` từ `bool + bool` của Python.

**Tham khảo:** [`np.random.random`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random.html), [`np.sum`](https://numpy.org/doc/stable/reference/generated/numpy.sum.html).

<a id="bai-12"></a>
## 12. Chuyển kiểu tự động

### Đề bài

Tạo một mảng số thực, rồi gán số nguyên vào mảng. Điều gì xảy ra? Thử nhiều số nguyên khác nhau, kể cả số rất lớn, lớn hơn `1.8e308`. Vì sao đề nhắc mốc này, và điều gì xảy ra ở đó?

Làm ngược lại: tạo mảng số nguyên, gán số thực vào và quan sát. Dùng mảng số nguyên 16 bit, gán giá trị ngoài miền `np.int16`. Thử các giá trị đặc biệt `np.inf` biểu diễn vô cực và `np.nan` biểu diễn “không phải một số”.

Tiếp tục thử các tổ hợp khác, chẳng hạn Boolean ở cả vai trò nguồn và đích. Đề lưu ý rằng ngay cả khi bạn nghĩ đã hiểu chuyển đổi số nguyên, vẫn có thể gặp kết quả bất ngờ.

### Hướng giải

Khi gán, mảng không tự đổi `dtype` để phù hợp giá trị mới; giá trị được chuyển về kiểu đích hoặc thao tác thất bại. Số thực hữu hạn trong miền được gán vào mảng nguyên sẽ bị bỏ phần thập phân theo hướng về 0: `-2.9` thành `-2`, không phải `-3`.

`np.finfo(np.float64).max` xấp xỉ `1.7976931348623157e308`. Chú ý `1.8e308` đã là `inf` trong kiểu `float` Python thông thường; để thật sự thử một **số nguyên** lớn hơn ngưỡng này, dùng `10**309`.

### Mã minh họa

```python
def try_assign(dtype, value):
    a = np.zeros(1, dtype=dtype)
    try:
        a[0] = value
        print("dtype:", a.dtype, "nguồn:", repr(value), "kết quả:", a)
    except (OverflowError, ValueError, TypeError) as exc:
        print("dtype:", a.dtype, "nguồn:", repr(value),
              "lỗi:", type(exc).__name__, str(exc))

try_assign(np.float64, 7)
try_assign(np.float64, 2**53 + 1)
try_assign(np.float64, 10**309)
try_assign(np.float64, np.inf)
try_assign(np.float64, np.nan)

try_assign(np.int16, 3.9)
try_assign(np.int16, -2.9)
try_assign(np.int16, 40000)
try_assign(np.int16, np.inf)
try_assign(np.int16, np.nan)

try_assign(bool, 0)
try_assign(bool, -3)
try_assign(bool, np.nan)
try_assign(np.int16, True)
try_assign(np.float64, False)

print(np.finfo(np.float64).max)
print(1.8e308)  # inf

# Chuyển kiểu mảng bằng astype là một đường chuyển đổi khác.
print(np.array([40000], dtype=np.int64).astype(np.int16))  # [-25536]
```

### Kết quả cần hiểu

| Thao tác trên NumPy 2.3.5 | Kết quả |
| --- | --- |
| Gán `7` vào `float64` | `7.0` |
| Gán `2**53 + 1` vào `float64` | Bị làm tròn; không còn chính xác số nguyên ban đầu |
| Gán Python `int` bằng `10**309` vào `float64` | `OverflowError` |
| Gán `3.9`, `-2.9` vào `int16` | `3`, `-2` |
| Gán Python `int` bằng `40000` vào `int16` | `OverflowError` |
| Gán scalar `np.inf` vào `int16` | `OverflowError` |
| Gán scalar `np.nan` vào `int16` | `ValueError` |
| Gán `np.nan` vào Boolean | `True` |
| Gán `True` vào số nguyên | `1` |

Không suy rằng mọi cách chuyển kiểu ngoài miền đều cùng báo lỗi hoặc cùng quay vòng. Gán scalar Python và gọi `.astype()` trên mảng là hai đường chuyển đổi khác nhau. Việc bắt ngoại lệ ở đây phục vụ thí nghiệm của đề, không phải kiểm tra đầu vào cho mọi bài.

**Tham khảo:** [Kiểu dữ liệu và chuyển kiểu](https://numpy.org/doc/stable/user/basics.types.html), [NumPy 2.x và scalar Python](https://numpy.org/doc/stable/reference/arrays.promotion.html#detailed-behavior-of-python-scalars).

<a id="bai-13"></a>
## 13. Gán bằng slicing

### Đề bài

Slicing cũng dùng được ở vế trái phép gán, tương tự danh sách Python. Viết hàm nhận danh sách, chuyển thành mảng, lấy hai nửa như bài 5, đảo mỗi nửa như bài 7, rồi ghi các nửa đảo ngược trở lại mảng ban đầu.

Ví dụ `[3, 5, 6, 7, 8, 9]` thành `[6, 5, 3, 9, 8, 7]`. Nếu độ dài lẻ, phần tử giữa thuộc nửa sau: `[3, 5, 6, 7, 8]` thành `[5, 3, 8, 7, 6]`.

Thử thêm cách không đảo hai nửa ở vế phải, mà dùng slicing đảo chiều ở vế trái phép gán. Kiểm tra kết quả giống nhau.

Một cách khác là dùng `np.hstack` rồi gán vào `a[:]` để ghi đè cả mảng. Hãy hiểu rõ khác biệt giữa gán cho biến `a` và gán cho view `a[:]`. Vì sao dùng `hstack` lại tạo mảng tạm trung gian?

Lưu ý của đề: các phần được gán phải có kích thước phù hợp. Điều này cũng áp dụng cho gán bằng danh sách chỉ số và mặt nạ ở các bài sau; broadcasting là trường hợp ngoại lệ được học tiếp.

### Hướng giải và mã minh họa

```python
def reverse_halves(values):
    a = np.array(values)
    k = len(a) // 2
    first = a[:k]
    second = a[k:]
    a[:k] = first[::-1].copy()
    a[k:] = second[::-1].copy()
    return a

def reverse_halves_left_side(values):
    a = np.array(values)
    n = len(a)
    k = n // 2
    a[k - n - 1::-1] = a[:k].copy()
    a[:k - n - 1:-1] = a[k:].copy()
    return a

def reverse_halves_hstack(values):
    a = np.array(values)
    k = len(a) // 2
    a[:] = np.hstack((a[:k][::-1], a[k:][::-1]))
    return a

print(reverse_halves([3, 5, 6, 7, 8, 9]))  # [6 5 3 9 8 7]
print(reverse_halves([3, 5, 6, 7, 8]))     # [5 3 8 7 6]

a = np.array([1, 2, 3])
alias = a
a[:] = [4, 5, 6]
print(alias)     # [4 5 6], dữ liệu của cùng mảng đã đổi
a = np.array([7, 8, 9])
print(alias)     # [4 5 6], tên a nay trỏ sang đối tượng khác
```

Các `.copy()` làm rõ rằng giá trị nguồn được chụp lại trước khi ghi vào vùng dữ liệu chồng lấp. Trong phép đảo một lát cắt đơn giản này, NumPy cũng xử lý được dạng ngắn `a[:k] = a[:k][::-1]`.

`hstack` cần chứa toàn bộ dữ liệu ghép trong một mảng kết quả mới trước khi `a[:]` nhận các giá trị đó. Gán vào slicing không thay đổi độ dài của mảng NumPy. Diễn đạt tổng quát hơn của điều kiện kích thước là: vế phải phải broadcasting được về `shape` của phần đích.

**Tham khảo:** [Gán vào mảng qua chỉ số](https://numpy.org/doc/stable/user/basics.indexing.html#assigning-values-to-indexed-arrays), [`np.hstack`](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html).

<a id="bai-14"></a>
## 14. Gán bằng danh sách chỉ số

### Đề bài

Làm tương tự bài 8, nhưng lần này gán `0`, `1`, `2` lần lượt vào phần tử đầu, giữa, cuối rồi trả về mảng. Ví dụ `[9, 9, 9, 9, 9]` thành `[0, 9, 1, 9, 2]`. Phần gán chỉ được dùng một dòng.

Nếu danh sách dài 1, bạn đang gán ba giá trị khác nhau vào cùng một phần tử. Dự đoán rồi kiểm chứng kết quả.

Trong trường hợp `n == 1`, nếu muốn kết quả là `[1]`, tức ưu tiên giá trị dành cho vị trí giữa, hãy sửa biểu thức chỉ số thay vì dùng `if`.

### Hướng giải và mã minh họa

```python
def assign_first_middle_last(values):
    a = np.array(values)
    n = len(a)
    a[[0, n // 2, n - 1]] = [0, 1, 2]
    return a

# Cách thí nghiệm mà đề hướng tới: chuyển vị trí giữa ra cuối.
def assign_middle_last_experiment(values):
    a = np.array(values)
    n = len(a)
    a[[0, n - 1, n // 2]] = [0, 2, 1]
    return a

print(assign_first_middle_last([9, 9, 9, 9, 9]))  # [0 9 1 9 2]
print(assign_first_middle_last([9]))              # Quan sát thường gặp: [2]
print(assign_middle_last_experiment([9]))         # Quan sát thường gặp: [1]

# Cách bảo đảm kết quả, vẫn một dòng gán và không có if:
def assign_middle_priority(values):
    a = np.array(values)
    n = len(a)
    a[[0, n - 1, n // 2]] = [int(n == 1), 2 - int(n == 1), 1]
    return a

assert np.array_equal(assign_middle_priority([9]), [1])
assert np.array_equal(assign_middle_priority([9, 9, 9, 9, 9]), [0, 9, 1, 9, 2])
```

**Lưu ý quan trọng:** Tài liệu NumPy không bảo đảm thứ tự gán tổng quát khi advanced indexing có chỉ số lặp. Vì vậy, cách “đưa phần tử giữa ra cuối” đáp ứng ý tưởng thí nghiệm của đề, nhưng không phải bảo đảm tổng quát của API. Phiên bản cuối tránh phụ thuộc thứ tự: khi `n == 1`, cả ba giá trị nguồn đều là 1; khi `n > 1` và lẻ, chúng là `0, 2, 1` cho đầu, cuối, giữa.

Đọc `b = a[[...]]` tạo bản sao, nhưng **gán trực tiếp** `a[[...]] = ...` vẫn sửa `a`; hai thao tác không mâu thuẫn.

**Tham khảo:** [Gán và các lưu ý về advanced indexing](https://numpy.org/doc/stable/user/basics.indexing.html#detailed-notes).

<a id="bai-15"></a>
## 15. Gán bằng mặt nạ

### Đề bài

Tương tự bài 10, nhưng dùng một biểu thức có mặt nạ Boolean ở cả phần đọc và phần gán để làm các phần tử của mảng trở thành số dương.

Gợi ý: tạo mặt nạ các giá trị âm, đọc các giá trị đó, đổi dấu, rồi gán lại vào đúng vị trí bằng cùng mặt nạ.

Cuối cùng, dùng một dòng với `np.all` để kiểm tra tất cả giá trị lớn hơn hoặc bằng 0. Viết thêm phép kiểm tra tương đương bằng `np.any` để bảo đảm không có giá trị nào nhỏ hơn 0.

### Hướng giải và mã minh họa

**Chú thích:** Do số 0 không đổi và phép kiểm tra dùng `>= 0`, kết quả đúng ở đây là **không âm**, không phải mọi phần tử đều dương nghiêm ngặt.

```python
def make_nonnegative(values):
    a = np.array(values, dtype=float)
    a[a < 0] = -a[a < 0]
    assert np.all(a >= 0)
    assert not np.any(a < 0)
    return a

print(make_nonnegative([-3, 0, 2, -5]))  # [3. 0. 2. 5.]
```

Ở đây dùng kiểu số thực theo quy ước chung của đề. Nếu giữ kiểu nguyên có dấu độ rộng cố định, phải lưu ý trị tuyệt đối của giá trị nhỏ nhất có thể không biểu diễn được: chẳng hạn `-np.int16(-32768)` vẫn bị tràn. Hai phép kiểm tra trên tương đương với dữ liệu số thông thường không có `NaN`; nếu có `NaN`, phép so sánh với 0 có hành vi khác nên không còn tương đương.

**Tham khảo:** [Boolean indexing](https://numpy.org/doc/stable/user/basics.indexing.html#boolean-array-indexing), [Giới hạn kiểu số](https://numpy.org/doc/stable/user/basics.types.html).

<a id="bai-16"></a>
## 16. Gán bằng broadcasting I

### Đề bài

Viết hàm nhận `n`, trả về mảng một chiều dài `n` gồm 0 và 1 xen kẽ, bắt đầu bằng 0. Ví dụ `n == 7` cho:

```text
[0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0]
```

Phải sử dụng broadcasting: gán một scalar vào một lát cắt mảng. Thân hàm không quá ba dòng, tính cả `return`. Có ít nhất hai cách; hãy viết cả hai.

### Hướng giải và mã minh họa

```python
def alternating_zeros(n):
    a = np.zeros(n)
    a[1::2] = 1
    return a

def alternating_ones(n):
    a = np.ones(n)
    a[::2] = 0
    return a

print(alternating_zeros(7))  # [0. 1. 0. 1. 0. 1. 0.]
```

Cách đầu tạo toàn số 0 rồi sửa vị trí lẻ thành 1. Cách sau tạo toàn số 1 rồi sửa vị trí chẵn thành 0. Mỗi hàm có đúng ba câu lệnh trong thân hàm.

**Tham khảo:** [Broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html).

<a id="bai-17"></a>
## 17. Gán bằng broadcasting II

### Đề bài

Viết hàm nhận `n`, trả về mảng một chiều dài `n`, nửa đầu gồm toàn số 1 và nửa sau gồm toàn số 0. Nếu `n` lẻ, phần tử giữa phải là 0. Không quá ba dòng trong thân hàm, tính cả `return`.

Viết thêm các phiên bản trả về số nguyên và Boolean; với Boolean, hiểu `True == 1`, `False == 0`.

### Hướng giải và mã minh họa

```python
def half_float(n):
    a = np.zeros(n)
    a[:n // 2] = 1
    return a

def half_int(n):
    a = np.zeros(n, dtype=int)
    a[:n // 2] = 1
    return a

def half_bool(n):
    a = np.zeros(n, dtype=bool)
    a[:n // 2] = True
    return a

print(half_float(5))  # [1. 1. 0. 0. 0.]
print(half_int(5))    # [1 1 0 0 0]
print(half_bool(5))   # [True True False False False]
```

`n // 2` là số phần tử của nửa đầu. Chỉ số tại điểm chia bị loại khỏi slicing `:n//2`, nên phần tử giữa vẫn bằng 0 khi `n` lẻ.

**Tham khảo:** [Broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html), [`np.ones` và các hàm tạo mảng liên quan](https://numpy.org/doc/stable/reference/generated/numpy.ones.html).

<a id="bai-18"></a>
## 18. Tạo mảng, áp dụng hàm theo phần tử và vẽ đồ thị

### Đề bài

Tạo một mảng một chiều gồm các giá trị cách đều từ `0.0` tới `2π`, lấy `0.0` nhưng không lấy `2π`. Dùng biến `n` quyết định số khoảng chia. Viết trong một dòng bằng một hàm tạo mảng chuyên dụng.

Làm lại nhưng lần này lấy cả `2π` làm phần tử cuối, vẫn giữ tổng số phần tử như trước; do đó khoảng cách giữa các phần tử tăng lên. Vẫn viết một dòng. Đề gợi ý dùng một hàm tạo mảng chuyên dụng khác.

Tính cả `sin` và `cos` trên mảng vừa tạo, mỗi hàm trong một dòng, tận dụng khả năng áp dụng hàm trên mảng. Vẽ hai đường sin/cos chung một biểu đồ; nhãn trục x phải là `radians`.

Nâng cao: thêm chú giải để biết đường nào là sin, đường nào là cos, dùng đối số `label` và hàm `legend`; xem thêm ví dụ trong thư viện mẫu của Matplotlib.

Nâng cao: lưu hình PNG. Đề gốc gợi ý trong Spyder có thể đổi tùy chọn IPython Console để hiện đồ thị trong cửa sổ riêng thay vì inline, rồi khởi động lại kernel. Ngoài ra có thể dùng `savefig`, điều chỉnh độ phân giải bằng `dpi`.

### Hướng giải

Với `n >= 2`, mẫu loại đầu mút phải có `n` điểm và bước `2π/n`. Mẫu lấy cả hai đầu mút vẫn có `n` điểm nhưng chỉ còn `n-1` khoảng, nên bước là `2π/(n-1)`. Đây là cách hiểu nhất quán với yêu cầu giữ nguyên số phần tử của đề.

`np.sin(x)` và `np.cos(x)` tính theo từng phần tử bằng ufunc. Đề gọi đây là “function broadcasting”; chính xác hơn, broadcasting dùng khi cần kết hợp các kích thước đầu vào, còn hai hàm một đối số này áp dụng trực tiếp lên từng phần tử mảng.

### Mã minh họa

```python
n = 200
x_open = np.arange(n) * (2 * np.pi / n)
x_closed = np.linspace(0, 2 * np.pi, n)

# Một cách khác cho mẫu không lấy đầu mút, kiểm soát rõ số điểm:
x_open_alternative = np.linspace(0, 2 * np.pi, n, endpoint=False)

y_sin = np.sin(x_closed)
y_cos = np.cos(x_closed)

plt.figure(figsize=(8, 4))
plt.plot(x_closed, y_sin, label="sin(x)")
plt.plot(x_closed, y_cos, label="cos(x)")
plt.xlabel("radians")
plt.ylabel("Giá trị")
plt.title("Hàm sin và cos")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("sin_cos.png", dpi=150)
plt.show()
```

`np.arange(0, 2*np.pi, 2*np.pi/n)` cũng gần với gợi ý gốc, nhưng bước số thực có thể gây sai lệch số phần tử do làm tròn. `np.arange(n)` rồi nhân hệ số hoặc `np.linspace(..., endpoint=False)` kiểm soát số điểm rõ hơn. Lưu hình trước `plt.show()` giúp tránh việc một số môi trường đóng hoặc xóa figure trước khi lưu.

**Tham khảo:** [`np.arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html), [`np.linspace`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html), [Hướng dẫn pyplot](https://matplotlib.org/stable/tutorials/pyplot.html).

<a id="bai-19"></a>
## 19. Số ngẫu nhiên theo phân phối chuẩn

### Đề bài

Sinh một triệu số ngẫu nhiên từ phân phối chuẩn, còn gọi là Gaussian, với trung bình `0.0` và phương sai `1.0`, bằng hai cách:

1. Tạo list bằng module `random` của Python và list comprehension.
2. Tạo mảng NumPy một chiều bằng module ngẫu nhiên của NumPy trong một dòng, không dùng comprehension. Tự tra tài liệu để tìm hàm thích hợp.

Quan sát chênh lệch thời gian của hai cách. Có thể dùng module `time` và hàm `time()` để đo. Ví dụ gốc:

```python
import time

t0 = time.time()
# Gọi hàm cần đo tại đây.
t1 = time.time()
print(t1 - t0)
```

### Hướng giải và mã minh họa

`random.gauss` và `Generator.normal` nhận **độ lệch chuẩn**, không phải phương sai. Ở đây độ lệch chuẩn là căn bậc hai của 1, cũng bằng 1.

```python
import random
from time import perf_counter

n = 1_000_000
py_rng = random.Random(42)
np_rng = np.random.default_rng(42)

t0 = perf_counter()
python_values = [py_rng.gauss(0.0, 1.0) for _ in range(n)]
python_seconds = perf_counter() - t0

t0 = perf_counter()
numpy_values = np_rng.normal(loc=0.0, scale=1.0, size=n)
numpy_seconds = perf_counter() - t0

print("Python:", python_seconds, "giây")
print("NumPy:", numpy_seconds, "giây")
print("Tỉ số thời gian Python/NumPy:", python_seconds / numpy_seconds)
print("Trung bình, phương sai mẫu NumPy:",
      numpy_values.mean(), numpy_values.var())

# Cú pháp theo API np.random truyền thống của đề:
legacy_values = np.random.normal(0.0, 1.0, size=n)
```

NumPy xử lý cả khối dữ liệu bằng mã biên dịch, còn comprehension thực hiện nhiều lần gọi từ Python, nên thường nhanh hơn đáng kể. Tỉ lệ thực tế phụ thuộc máy, phiên bản và cách đo. `perf_counter()` phù hợp đo khoảng thời gian ngắn; không bao gồm thời gian in cả triệu giá trị vào phần cần đo. Cùng seed không có nghĩa hai thư viện sinh cùng một dãy.

**Tham khảo:** [`random.gauss`](https://docs.python.org/3/library/random.html#random.gauss), [`Generator.normal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.normal.html), [`time.perf_counter`](https://docs.python.org/3/library/time.html#time.perf_counter).

<a id="bai-20"></a>
## 20. Số ngẫu nhiên chuẩn, mảng hai chiều và thống kê

### Đề bài

Tạo mảng hai chiều `10 × 20` gồm số ngẫu nhiên Gaussian bằng NumPy như bài 19. Tính trung bình trong một dòng.

Lấy mảng con chỉ chứa các phần tử mà **cả chỉ số hàng lẫn chỉ số cột đều chẵn**. Ví dụ `[2, 4]`, `[0, 8]` hợp lệ; `[1, 2]`, `[3, 5]` không hợp lệ. Dùng một biểu thức chỉ số với hai slicing: một cho hàng và một cho cột, như bài 6.

Kết quả là mảng độc lập hay view? Kiểm tra bằng cách sửa mảng con và quan sát mảng đầu. Nếu muốn kết quả ngược lại thì làm thế nào? Gợi ý: gọi một phương thức mảng sau slicing. Tính trung bình của mảng con.

Viết hàm lặp lại các thao tác tạo mảng, tính trung bình toàn mảng và trung bình mảng con nhiều lần, chẳng hạn 1000 lần. Lưu kết quả vào hai mảng một chiều riêng biệt.

Vẽ histogram cho hai mảng trung bình. Gọi `plot` hoặc `hist` nhiều lần sẽ chồng hình, nên cần lệnh xóa figure giữa các lần thử. Kỳ vọng thấy hai dạng gần đường cong Gaussian. Tra tùy chọn `hist` để vẽ đường bậc thang không tô đầy cột và chồng hai histogram lên nhau. Thử tăng số `bins`: điều gì xảy ra, và làm thế nào để đường mượt hơn?

Mở rộng: nếu biết thống kê, hãy dự đoán dạng hai đường cong, vẽ đường lý thuyết lên histogram để kiểm chứng. Khi đó nên xem tùy chọn `density` của `hist`.

### Hướng giải

`a[::2, ::2]` chọn 5 hàng và 10 cột, có 50 phần tử; mảng đầy đủ có 200 phần tử. Thí nghiệm thay đổi view nên tách khỏi vòng lặp thống kê, để không làm sai phân phối của dữ liệu đang đo.

Nếu các phần tử độc lập, đều có phân phối chuẩn với trung bình 0, phương sai 1, thì trung bình của `m` phần tử có:

$$
E[\bar X]=0,\qquad \operatorname{Var}(\bar X)=\frac{1}{m},\qquad
\sigma_{\bar X}=\frac{1}{\sqrt m}.
$$

Vì thế độ lệch chuẩn của hai mảng trung bình lần lượt là `1/sqrt(200)` và `1/sqrt(50)`. Đường của mảng con rộng gấp 2 theo độ lệch chuẩn. Đây là phân phối chuẩn chính xác theo mô hình đầu vào chuẩn độc lập; histogram hữu hạn chỉ xấp xỉ đường lý thuyết.

### Mã minh họa

```python
rng20 = np.random.default_rng(42)
a = rng20.normal(0.0, 1.0, size=(10, 20))
mean_all = a.mean()
sub = a[::2, ::2]
mean_sub = sub.mean()
print(a.shape, sub.shape)              # (10, 20), (5, 10)
print(mean_all, mean_sub)
print(np.shares_memory(a, sub))        # True

sub[0, 0] = 999
print(a[0, 0])                        # 999.0
independent = a[::2, ::2].copy()
independent[0, 0] = -1
print(a[0, 0])                        # Vẫn là 999.0

def compare_sample_means(iterations=1000, bins=40, seed=42):
    rng = np.random.default_rng(seed)
    means_all = np.empty(iterations)
    means_sub = np.empty(iterations)

    for i in range(iterations):
        a = rng.normal(0.0, 1.0, size=(10, 20))
        means_all[i] = a.mean()
        means_sub[i] = a[::2, ::2].mean()

    low = min(means_all.min(), means_sub.min())
    high = max(means_all.max(), means_sub.max())
    edges = np.linspace(low, high, bins + 1)

    plt.figure(num="So sánh trung bình", figsize=(8, 4))
    plt.clf()
    plt.hist(means_all, bins=edges, density=True,
             histtype="step", label="Toàn mảng: 200 phần tử")
    plt.hist(means_sub, bins=edges, density=True,
             histtype="step", label="Mảng con: 50 phần tử")

    x = np.linspace(low, high, 500)
    sigma_all = 1 / np.sqrt(200)
    sigma_sub = 1 / np.sqrt(50)
    density_all = np.exp(-0.5 * (x / sigma_all)**2) / (sigma_all * np.sqrt(2*np.pi))
    density_sub = np.exp(-0.5 * (x / sigma_sub)**2) / (sigma_sub * np.sqrt(2*np.pi))
    plt.plot(x, density_all, "--", label="Lý thuyết: 200 phần tử")
    plt.plot(x, density_sub, "--", label="Lý thuyết: 50 phần tử")
    plt.xlabel("Trung bình mẫu")
    plt.ylabel("Mật độ xác suất")
    plt.legend()
    plt.tight_layout()
    plt.show()
    return means_all, means_sub

means_all, means_sub = compare_sample_means(iterations=10_000, bins=50)
```

`histtype="step"` tạo đường viền bậc thang, `density=True` chuẩn hóa diện tích histogram để so với mật độ lý thuyết. Tăng `bins` làm các khoảng hẹp hơn nhưng có thể khiến hình lởm chởm khi số mẫu chưa đủ. Muốn đường ổn định hơn, tăng số lần lặp và chọn số bin vừa phải. Hai trung bình lấy trong cùng một lần thử có tương quan vì dùng chung một phần dữ liệu; điều đó không làm sai hai phân phối riêng vừa suy ra.

**Tham khảo:** [`np.mean`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html), [`plt.hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html), [`Generator.normal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.normal.html).

<a id="bai-21"></a>
## 21. Các mẫu truy cập khác trên mảng hai chiều

### Đề bài

Cho một mảng hai chiều, hãy gán 0 cho mọi phần tử có tổng chỉ số hàng và cột là số chẵn. Ví dụ `[0, 0]`, `[2, 4]`, `[1, 1]`, `[1, 3]`. Có thể hình dung đây là mẫu bàn cờ.

Có thể làm tổng quát bằng một dòng không? Vì sao? Số thao tác ít nhất để làm được là bao nhiêu?

Câu đố thêm: giả sử số cột lẻ và mảng không phải view. Hãy làm trong một dòng.

### Hướng giải và mã minh họa

Tổng chẵn có hai trường hợp: hàng chẵn/cột chẵn và hàng lẻ/cột lẻ. Nếu chỉ dùng các lát cắt 2D trực tiếp, cách tổng quát là hai phép gán:

```python
a = np.ones((4, 6), dtype=int)
a[::2, ::2] = 0
a[1::2, 1::2] = 0
print(a)
```

```text
[[0 1 0 1 0 1]
 [1 0 1 0 1 0]
 [0 1 0 1 0 1]
 [1 0 1 0 1 0]]
```

Một cặp slicing độc lập cho hàng và cột không biểu diễn được việc cột cần chọn thay đổi theo tính chẵn/lẻ của hàng. Tuy nhiên, nếu cho phép tạo mặt nạ, đáp án tổng quát **có thể là một dòng gán**:

```python
a = np.ones((4, 6), dtype=int)
a[np.indices(a.shape).sum(axis=0) % 2 == 0] = 0
```

Vì vậy câu hỏi “ít nhất bao nhiêu thao tác” cần nêu rõ phạm vi: hai phép gán bằng slicing 2D đơn giản, hoặc một phép gán bằng mặt nạ nhưng có các phép tính tạo mặt nạ trung gian. Một dòng mã không có nghĩa chỉ có một thao tác tính toán.

Khi số cột `w` lẻ, chỉ số phẳng theo thứ tự hàng là `p = row*w + col`. Vì `w` lẻ nên `p` và `row+col` có cùng tính chẵn/lẻ:

```python
a = np.ones((4, 5), dtype=int)  # Mảng C-contiguous
a.ravel()[::2] = 0
```

**Chú thích về giả thiết gốc:** “Không phải view” chưa đủ bảo đảm `ravel()` dùng chung dữ liệu, vì mảng sở hữu dữ liệu vẫn có thể ở thứ tự Fortran. Cần thêm điều kiện bố trí phù hợp, chẳng hạn `a.flags.c_contiguous`. Một cách gán theo thứ tự hàng không phụ thuộc việc `ravel()` có tạo copy là:

```python
a = np.ones((4, 5), dtype=int, order="F")
a.flat[::2] = 0  # Đúng cho số cột lẻ; sửa trực tiếp a.
```

**Tham khảo:** [`np.ravel`](https://numpy.org/doc/stable/reference/generated/numpy.ravel.html), [`ndarray.flat`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flat.html).

<a id="bai-22"></a>
## 22. Ghép mảng

### Đề bài

Tạo một list Python chứa `n` mảng một chiều. Mỗi mảng có 5 phần tử: mảng đầu chứa từ 0 đến 4, mảng thứ hai từ 1 đến 5, mảng thứ ba từ 2 đến 6, v.v. Tạo list này trong một dòng. Gợi ý: dùng hàm tạo mảng đã gặp ở bài 18 và comprehension; có thể viết vòng lặp trước rồi chuyển sang comprehension.

Từ list đó, thực hiện mỗi yêu cầu sau trong một dòng, xem lại bài 5:

1. Tạo mảng hai chiều kích thước `n × 5`, hàng thứ `i` là mảng thứ `i` trong list. Với `n == 3`, kết quả là:

```text
[[0 1 2 3 4]
 [1 2 3 4 5]
 [2 3 4 5 6]]
```

2. Tạo mảng một chiều dài `n*5` bằng cách nối các mảng trong list. Với `n == 3`, kết quả là:

```text
[0 1 2 3 4 1 2 3 4 5 2 3 4 5 6]
```

### Hướng giải và mã minh họa

```python
n = 3  # Giả sử n >= 1 cho các hàm ghép bên dưới.
arrays = [np.arange(i, i + 5) for i in range(n)]
matrix = np.vstack(arrays)
flat = np.hstack(arrays)

print(matrix)
print(flat)

# Một cách tương đương cho ma trận:
matrix_alternative = np.stack(arrays, axis=0)
assert np.array_equal(matrix, matrix_alternative)
```

`vstack` đặt mỗi mảng một chiều thành một hàng. `hstack` nối các mảng một chiều theo thứ tự. Với đầu vào là các mảng 1D ở đây, `stack(..., axis=0)` cũng cho kết quả `n × 5`.

Nếu muốn mở rộng cho `n == 0`, cần quy định mảng rỗng có shape `(0, 5)` và `(0,)`; không gọi `vstack` hoặc `hstack` với list rỗng. Bài 23 tạo được shape `(0, 5)` tự nhiên bằng broadcasting.

**Tham khảo:** [`np.hstack` và liên kết tới `vstack`, `stack`](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html), [`np.arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html).

<a id="bai-23"></a>
## 23. Câu đố broadcasting nâng cao

### Đề bài

Tạo cùng kết quả với bài 22 mục 1, nhưng chỉ dùng hai mảng một chiều và một dòng mã. Tận dụng broadcasting cùng `reshape`, `newaxis` hoặc `expand_dims`; có nhiều biểu thức tương đương.

### Hướng giải và mã minh họa

Giá trị tại hàng `i`, cột `j` phải là `i+j`. Tạo mảng chỉ số hàng và chỉ số cột; biến mảng hàng từ shape `(n,)` thành `(n, 1)` để có thể cộng với mảng `(5,)`.

```python
n = 3
matrix = np.arange(n)[:, None] + np.arange(5)
print(matrix)

# Các cách viết tương đương, chọn một cách khi làm bài:
matrix_reshape = np.arange(n).reshape(n, 1) + np.arange(5)
matrix_expand = np.expand_dims(np.arange(n), axis=1) + np.arange(5)
assert np.array_equal(matrix, matrix_reshape)
assert np.array_equal(matrix, matrix_expand)
```

Broadcasting kết hợp `(n, 1)` và `(5,)` thành kết quả `(n, 5)`. Hai mảng nguồn được tạo là 1D; thêm trục kích thước 1 giúp diễn đạt phép cộng mọi cặp `i+j`, không cần vòng lặp hoặc list trung gian.

**Tham khảo:** [Broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html), [Thêm chiều bằng `newaxis`](https://numpy.org/doc/stable/user/basics.indexing.html#dimensional-indexing-tools).

<a id="bai-24"></a>
## 24. Sàng Eratosthenes I

### Đề bài

Cài đặt một phiên bản sàng Eratosthenes chưa tối ưu hoàn toàn:

1. Tạo mảng Boolean dài `n`, mọi phần tử là `True`.
2. Gán phần tử chỉ số 0 và 1 thành `False`.
3. Lặp qua tất cả số nguyên từ 2 đến `floor(sqrt(n-1))`, bao gồm giới hạn trên. Với mỗi `i`, gán `False` cho các vị trí là bội của `i`, bắt đầu từ `i**2`.

Mảng kết quả chỉ còn `True` ở vị trí tương ứng với số nguyên tố.

Nâng cao: lấy chỉ số của các số nguyên tố bằng một dòng dùng `arange` và mặt nạ Boolean. Có thể thay bằng `nonzero`, `flatnonzero`, hoặc kết hợp `argwhere` với `ravel`.

### Hướng giải và mã minh họa

Mảng dài `n` đại diện các số từ 0 đến `n-1`, nên bài tìm số nguyên tố **nhỏ hơn `n`**. Các bội nhỏ hơn `i*i` đã được xử lý bởi ước nhỏ hơn. `math.isqrt(n-1)` tính căn bậc hai nguyên chính xác, tránh dùng căn số thực rồi làm tròn.

```python
from math import isqrt

def sieve_v1(n):
    # Giả sử n >= 2 theo thao tác đặt chỉ số 0 và 1 của đề.
    prime = np.ones(n, dtype=bool)
    prime[:2] = False
    for i in range(2, isqrt(n - 1) + 1):
        prime[i * i::i] = False
    return prime

n = 30
mask = sieve_v1(n)
primes = np.arange(n)[mask]
print(primes)  # [2 3 5 7 11 13 17 19 23 29]

assert np.array_equal(primes, np.flatnonzero(mask))
assert np.array_equal(primes, np.nonzero(mask)[0])
assert np.array_equal(primes, np.argwhere(mask).ravel())
```

Phiên bản này vẫn xử lý cả `i` hợp số, chẳng hạn 4, 6, 8, dù các bội tương ứng đã bị loại trước đó. Đó là phần công việc dư mà bài 25 muốn giảm.

**Tham khảo:** [`np.flatnonzero`](https://numpy.org/doc/stable/reference/generated/numpy.flatnonzero.html). Liên kết thuật toán có sẵn trong PDF: [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes).

<a id="bai-25"></a>
## 25. Sàng Eratosthenes II — Nâng cao

### Đề bài

Làm lại bài 24 nhưng cài đặt sàng đúng theo mô tả trên Wikipedia hoặc tài liệu khác. Thay vì duyệt mọi chỉ số từ 2 tới khoảng căn bậc hai của `n`, hãy dùng vòng lặp `while`: bắt đầu `i=2`, sau mỗi lượt chọn `i` tiếp theo là chỉ số đầu tiên sau `i` hiện tại mà mảng vẫn có giá trị `True`.

Vì mảng là Boolean, có thể dùng `argmax` để tìm vị trí `True` đầu tiên. Nhưng phải tìm **sau chỉ số hiện tại**. Có thể làm mà không tạo bản sao và không thêm vòng lặp tìm kiếm không?

Đo chênh lệch thời gian với bài trước, dùng `n == 10**7` hoặc lớn hơn. Đề gốc nêu tốc độ có thể nhanh hơn khoảng 4-5 lần, lợi ích tăng khi `n` tăng. Có thể thử thêm phiên bản list Python và vòng lặp `for`; tác giả đề ghi nhận chậm hơn khoảng 30 lần trên máy của họ với `n == 10**7`.

### Hướng giải

Sau khi loại bội của một số nguyên tố, tìm vị trí `True` kế tiếp trên một view. Chỉ cần tìm trong phần còn lại tới giới hạn sàng; những số nguyên tố lớn hơn giới hạn không cần dùng để gạch bội.

`argmax` trả về vị trí của phần tử lớn nhất đầu tiên. Với Boolean, `True` lớn hơn `False`, nhưng nếu toàn `False`, hàm vẫn trả 0; nếu mảng rỗng thì báo lỗi. Vì vậy phải xử lý hai tình huống này, không thể coi mọi kết quả `argmax` đều là một số nguyên tố tiếp theo.

### Mã minh họa

```python
from math import isqrt

def sieve_v2(n):
    # Giả sử n >= 2, cùng quy ước với sieve_v1.
    prime = np.ones(n, dtype=bool)
    prime[:2] = False
    limit = isqrt(n - 1)
    i = 2

    while i <= limit:
        prime[i * i::i] = False
        candidates = prime[i + 1:limit + 1]  # View, không chép dữ liệu.
        if candidates.size == 0:
            break
        offset = int(candidates.argmax())
        if not candidates[offset]:          # Không còn True.
            break
        i = i + 1 + offset

    return prime

assert np.array_equal(sieve_v1(1000), sieve_v2(1000))
print(np.flatnonzero(sieve_v2(30)))

# Phiên bản Python thuần để tự so sánh.
def sieve_python(n):
    prime = [True] * n
    prime[0] = prime[1] = False
    for i in range(2, isqrt(n - 1) + 1):
        if prime[i]:
            for multiple in range(i * i, n, i):
                prime[multiple] = False
    return prime

from time import perf_counter

def measure_sieve(function, n, repeats=3):
    durations = []
    for _ in range(repeats):
        start = perf_counter()
        result = function(n)
        durations.append(perf_counter() - start)
        del result
    return min(durations)

# Chạy sau khi đã định nghĩa sieve_v1 ở bài 24.
n = 10**7
t1 = measure_sieve(sieve_v1, n)
t2 = measure_sieve(sieve_v2, n)
print("Phiên bản I:", t1, "giây")
print("Phiên bản II:", t2, "giây")
print("Tỉ số I/II:", t1 / t2)

# Bỏ dấu # nếu muốn đo cả bản Python thuần:
# tp = measure_sieve(sieve_python, n)
# print("Python thuần:", tp, "giây; tỉ số Python/II:", tp / t2)
```

Hai nhánh `if` trong vòng lặp xử lý trạng thái kết thúc thuật toán, không phải dò từng phần tử bằng Python. `argmax` thực hiện việc tìm kiếm; slicing tạo view.

Các con số 4-5 lần và 30 lần là quan sát được nêu trong đề, không phải cam kết hiệu năng. Không nên sửa hoặc chọn kết quả đo chỉ để khớp các con số đó. Giới hạn chính xác vẫn là `floor(sqrt(n-1))` vì phần tử cuối đại diện số `n-1`.

**Tham khảo:** [`np.argmax`](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html), [`time.perf_counter`](https://docs.python.org/3/library/time.html#time.perf_counter). Liên kết gốc: [Sàng Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes).

<a id="bai-26"></a>
## 26. Conway’s Game of Life — Rất nâng cao

### Đề bài

Cài đặt Conway’s Game of Life. Viết hàm nhận cấu hình ban đầu dưới dạng bảng 0 và 1, có thể dùng Boolean hoặc số nguyên, cùng số bước `n`. Hàm chạy trò chơi trong `n` bước và trả về cấu hình cuối cùng.

Luật gốc giả định một lưới vô hạn. Trong bài này, dùng lưới hữu hạn cho đơn giản và áp dụng luật thông thường ngay cả ở biên: ô ở cạnh chỉ có 5 hàng xóm, ô ở góc chỉ có 3 hàng xóm.

Gợi ý cho cách trực tiếp: dùng hai mảng, một cho cấu hình hiện tại, một cho cấu hình tiếp theo; sau mỗi bước, cập nhật cấu hình hiện tại bằng cấu hình tiếp theo. Cách nâng cao: tính bảng số hàng xóm trước, sau đó dùng các phép so sánh và toán tử Boolean `&`, `|`, `~` để cập nhật.

Vẽ cấu hình mỗi bước như một ảnh bằng `imshow`. Gọi `plt.clf()` trước mỗi hình mới để tránh tích lũy quá nhiều hình và làm chậm việc vẽ. Cách này phù hợp hơn khi không dùng chế độ inline; xem lưu ý bài 18. Dùng `plt.pause(0.05)` sau mỗi lần vẽ để nhìn thấy diễn biến.

Khi gỡ lỗi, bắt đầu với lưới nhỏ, cấu hình đơn giản và kiểm tra từng bước. Đề cung cấp cấu hình **glider**, **Gosper glider gun**, lưới ngẫu nhiên và hai cấu hình tạo bằng chỉ số phẳng để thử nghiệm. Các ví dụ được giữ ở phần dưới.

### Hướng giải

Mỗi ô có tối đa 8 hàng xóm gồm các ô tiếp giáp ngang, dọc và chéo. Luật chuyển trạng thái:

| Trạng thái hiện tại | Số hàng xóm sống | Trạng thái tiếp theo |
| --- | --- | --- |
| Sống | 2 hoặc 3 | Sống |
| Sống | Các giá trị khác | Chết |
| Chết | 3 | Sống |
| Chết | Các giá trị khác | Chết |

Nếu `alive` là mảng hiện tại và `neighbors` là số hàng xóm sống, thì trạng thái mới là `(neighbors == 3) | (alive & (neighbors == 2))`.

Đệm một viền 0 quanh lưới rồi cộng tám lát cắt lệch nhau để đếm hàng xóm. Các ô ngoài lưới được xem là chết; không nối biên trái với phải hoặc trên với dưới. Những ô ở biên vẫn có thể sống hoặc chết theo luật, không bị ép chết.

**Điểm cần chú ý:** Phải chuyển Boolean sang kiểu số nguyên trước khi cộng tám mảng; cộng trực tiếp các mảng Boolean không đếm được từ 0 đến 8 như mong muốn. Chọn `uint8` là đủ cho số hàng xóm tối đa 8.

### Mã minh họa

```python
def life_step(current):
    alive = np.asarray(current, dtype=bool)
    padded = np.pad(alive.astype(np.uint8), 1,
                    mode="constant", constant_values=0)

    neighbors = (
        padded[:-2, :-2] + padded[:-2, 1:-1] + padded[:-2, 2:]
        + padded[1:-1, :-2] + padded[1:-1, 2:]
        + padded[2:, :-2] + padded[2:, 1:-1] + padded[2:, 2:]
    )
    return (neighbors == 3) | (alive & (neighbors == 2))

def ex26_gameoflife(initial, n, show=True, delay=0.05):
    current = np.array(initial, dtype=bool, copy=True)

    def draw(step):
        plt.clf()
        plt.imshow(current, cmap="binary", vmin=0, vmax=1,
                   interpolation="nearest")
        plt.title(f"Game of Life - bước {step}")
        plt.xticks([])
        plt.yticks([])
        plt.pause(delay)

    if show:
        plt.figure(num="Game of Life", figsize=(6, 6))
        draw(0)

    for step in range(1, n + 1):
        current = life_step(current)
        if show:
            draw(step)

    return current
```

`show` và `delay` là đối số tùy chọn bổ sung; hàm vẫn gọi được với đúng hai đối số như đề. Khi chỉ tính kết quả hoặc kiểm thử, dùng `show=False`. Bản mã này không sửa trực tiếp cấu hình đầu vào. Mỗi thế hệ được tính hoàn toàn từ thế hệ cũ, bảo đảm cập nhật đồng thời.

### Kiểm tra trước khi chạy hình động

```python
# Khối 2x2 là cấu hình đứng yên.
block = np.zeros((4, 4), dtype=bool)
block[1:3, 1:3] = True
assert np.array_equal(life_step(block), block)

# Blinker đổi ngang/dọc và trở lại sau hai bước.
blinker = np.zeros((5, 5), dtype=bool)
blinker[2, 1:4] = True
vertical = np.zeros((5, 5), dtype=bool)
vertical[1:4, 2] = True
assert np.array_equal(life_step(blinker), vertical)
assert np.array_equal(ex26_gameoflife(blinker, 2, show=False), blinker)

# Ô đơn lẻ chết vì thiếu hàng xóm.
single = np.zeros((3, 3), dtype=bool)
single[0, 0] = True
assert not life_step(single).any()
assert np.array_equal(ex26_gameoflife(block, 0, show=False), block)
```

### Các cấu hình thử nghiệm trong đề gốc

**Glider:** giữ nguyên hướng và vị trí đặt mẫu trong PDF.

```python
n = 20
c = np.zeros((n, n), dtype=bool)
glider = np.array([
    [0, 0, 1],
    [1, 0, 1],
    [0, 1, 1],
])
m0, m1 = glider.shape
c[:m0, :m1] = glider
final_glider = ex26_gameoflife(c, 50)
```

Glider có thể di chuyển trên lưới, nhưng hành vi sẽ thay đổi khi chạm biên hữu hạn.

**Gosper glider gun:** ma trận gốc kích thước `11 × 38` được viết gọn bằng chuỗi từng hàng bên dưới. Ký tự `1` và `0` khớp từng ô của ma trận trong PDF; đây chỉ là thay đổi cách biểu diễn dữ liệu.

```python
gun_rows = [
    "00000000000000000000000000000000000000",
    "00000000000000000000000001000000000000",
    "00000000000000000000000101000000000000",
    "00000000000001100000011000000000000000",
    "00000000000010001000011000000000000110",
    "01100000000100000100011000000000000110",
    "01100000000100010110000101000000000000",
    "00000000000100000100000001000000000000",
    "00000000000010001000000000000000000000",
    "00000000000001100000000000000000000000",
    "00000000000000000000000000000000000000",
]
gun = np.frombuffer("".join(gun_rows).encode("ascii"), dtype=np.uint8)
gun = (gun == ord("1")).reshape(11, 38)

n = 50
c = np.zeros((n, n), dtype=bool)
m0, m1 = gun.shape
c[:m0, :m1] = gun
final_gun = ex26_gameoflife(c, 100)
```

**Cấu hình ngẫu nhiên:** mỗi ô có xác suất sống ban đầu là 0.2.

```python
c = np.random.rand(100, 100) < 0.2
final_random = ex26_gameoflife(c, 100)
```

**Cấu hình dùng chỉ số phẳng:** đề gợi ý tăng kích thước để quan sát diễn biến và tự giải thích cách khởi tạo.

```python
n = 200
c = np.zeros((n, n), dtype=bool)
c.ravel()[::n + 1] = 1
c.ravel()[n - 1::n - 1] = 1
final_cross = ex26_gameoflife(c, 1000)
```

Với mảng vuông lưu theo thứ tự hàng, bước `n+1` từ 0 chọn đường chéo chính. Bắt đầu ở `n-1` rồi bước `n-1` chọn đường chéo phụ và thêm góc dưới phải; góc này đã nằm trên đường chéo chính. Vì vậy cấu hình kết hợp là hình chữ X.

**Biến thể trong đề:** giữ nguyên các mốc slicing của PDF.

```python
n = 200
c = np.zeros((n, n), dtype=bool)
c.ravel()[n::n + 1] = 1
c.ravel()[n - 2:n**2 - 2*n + 1:n - 1] = 1
c.ravel()[1::n + 1] = 1
c.ravel()[2*n - 1::n - 1] = 1
plt.clf()
plt.imshow(c)
final_variation = ex26_gameoflife(c, 1000)
```

Các lát cắt này tạo các dải nằm sát hai đường chéo. Với các lệnh `ravel()` trong ví dụ, `c` vừa được tạo bởi `np.zeros` theo thứ tự C nên gán qua mảng phẳng sửa được dữ liệu gốc. Hình động 1000 bước với thời gian nghỉ 0.05 giây cần ít nhất khoảng 50 giây, chưa tính thời gian tính và vẽ; khi thử nhanh có thể giảm số bước hoặc dùng `show=False`.

**Tham khảo triển khai:** [`np.pad`](https://numpy.org/doc/stable/reference/generated/numpy.pad.html), [`plt.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html), [`np.ravel`](https://numpy.org/doc/stable/reference/generated/numpy.ravel.html).

**Các liên kết mô tả trò chơi có sẵn trong PDF:** [Conway’s Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life), [Glider](https://en.wikipedia.org/wiki/Glider_%28Conway%27s_Life%29), [Gun trong cellular automaton](https://en.wikipedia.org/wiki/Gun_%28cellular_automaton%29).

## Ghi chú về nguồn và các điểm đã làm rõ

Phần đề bài được dịch từ toàn bộ PDF đính kèm. Phần lời giải, giải thích và kiểm thử là nội dung bổ sung, không phải đáp án gốc của tác giả. Liên kết NumPy, Python và Matplotlib trỏ tới tài liệu chính thức; các liên kết Wikipedia được giữ dưới nhãn “liên kết gốc” vì có trong PDF.

| Bài | Điểm cần đọc kèm chú thích |
| --- | --- |
| 1, 12 | Tràn số trong phép toán khác với chuyển một scalar ngoài miền; NumPy 2.x có những trường hợp báo lỗi. |
| 5-8 | Bằng nhau, cùng đối tượng và dùng chung dữ liệu là ba khái niệm khác nhau. |
| 7 | Slicing đảo nửa đầu cần xử lý đúng khi nửa đầu rỗng. |
| 9 | Kết quả ngẫu nhiên có thể tình cờ lặp lại giữa hai lần chạy. |
| 10, 15 | Yêu cầu thực tế là không âm, bao gồm 0. |
| 11, 26 | Cộng Boolean Python và cộng Boolean NumPy không thể suy diễn giống nhau; dùng tổng rút gọn hoặc đổi sang kiểu nguyên để đếm. |
| 14 | Chỉ số lặp trong advanced assignment không có bảo đảm tổng quát về thứ tự gán. |
| 18 | Phân biệt số điểm và số khoảng khi lấy hoặc bỏ đầu mút. |
| 21 | Một dòng gán bằng mặt nạ làm được bài tổng quát; mẹo `ravel()` cần xét bố trí bộ nhớ. |
| 25 | `argmax` cần xử lý mảng rỗng/toàn False; tỉ lệ tăng tốc trong đề là số liệu tham khảo của tác giả. |
| 26 | Biên hữu hạn không cuộn vòng; mẫu gun viết gọn vẫn giữ nguyên tất cả ô của nguồn. |
