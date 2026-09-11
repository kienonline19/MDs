# 40 Bài Tập NumPy: Các Phép Toán Học

*Từ cơ bản đến nâng cao nhẹ — kèm lời giải và giải thích ngắn gọn.*

## Phần 1: Phép toán element-wise và với số vô hướng (Bài 1–8)

**Bài 1.** Cho hai mảng sau, tính `a + b`, `a - b`, `a * b`, `a / b`.

```python
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
```

*Lời giải:*
```python
print(a + b)   # [11 22 33 44]
print(a - b)   # [-9 -18 -27 -36]
print(a * b)   # [10 40 90 160]
print(a / b)   # [0.1 0.1 0.1 0.1]
```
> Các phép toán được thực hiện theo từng phần tử tương ứng (element-wise), không phải phép toán ma trận.

**Bài 2.** Cho mảng sau, tính phần dư khi chia cho 4 (`%`) và phần nguyên khi chia cho 4 (`//`).

```python
a = np.array([2, 5, 9, 14])
```

*Lời giải:*
```python
print(a % 4)    # [2 1 1 2]
print(a // 4)   # [0 1 2 3]
```
> `%` trả về phần dư, `//` trả về thương nguyên (làm tròn xuống), áp dụng cho từng phần tử.

**Bài 3.** Cho mảng sau, tính `a + 10`, `a * 3`, `a ** 2`.

```python
a = np.array([1, 2, 3])
```

*Lời giải:*
```python
print(a + 10)   # [11 12 13]
print(a * 3)    # [3 6 9]
print(a ** 2)   # [1 4 9]
```
> Khi thực hiện phép toán giữa mảng và một số đơn (scalar), NumPy "phát" (broadcast) số đó ra để áp dụng cho mọi phần tử — không cần vòng lặp.

**Bài 4.** Cho hai mảng 2D sau, tính `m1 + m2` và `m1 * m2` (element-wise, không phải nhân ma trận).

```python
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[10, 20], [30, 40]])
```

*Lời giải:*
```python
print(m1 + m2)
# [[11 22] [33 44]]
print(m1 * m2)
# [[10 40] [90 160]]
```
> Với mảng 2D, các phép toán `+`, `-`, `*`, `/` vẫn hoạt động theo từng phần tử tại cùng vị trí, giống hệt mảng 1D.

**Bài 5.** Cho mảng sau, tính giá trị tuyệt đối của từng phần tử.

```python
a = np.array([-3, -1, 0, 2, 5])
```

*Lời giải:*
```python
print(np.abs(a))   # [3 1 0 2 5]
```
> `np.abs()` là một ufunc, áp dụng lên từng phần tử độc lập và trả về mảng mới cùng kích thước.

**Bài 6.** Cho hai mảng sau, tính `a // b` và giải thích tại sao kết quả khác với `a / b`.

```python
a = np.array([7, 12, 25])
b = np.array([2, 5, 4])
```

*Lời giải:*
```python
print(a // b)   # [3 2 6]
print(a / b)    # [3.5 2.4 6.25]
```
> `/` luôn trả về kết quả kiểu số thực (float), kể cả khi chia hết. `//` chỉ lấy phần nguyên của phép chia (làm tròn xuống), nên mất đi phần dư.

**Bài 7.** Cho mảng sau, tính `a ** 3` (lập phương từng phần tử).

```python
a = np.array([1, 2, 3, 4, 5])
```

*Lời giải:*
```python
print(a ** 3)   # [  1   8  27  64 125]
```
> Lũy thừa cũng là phép toán element-wise: mỗi phần tử được nâng lên số mũ 3 một cách độc lập.

**Bài 8.** Cho hai mảng sau, tính `a % b`.

```python
a = np.array([100, 200, 300])
b = np.array([3, 7, 11])
```

*Lời giải:*
```python
print(a % b)   # [1 4 3]
```
> Mỗi phần tử của `a` được chia lấy dư với phần tử tương ứng của `b`: 100 % 3 = 1, 200 % 7 = 4, 300 % 11 = 3.

## Phần 2: Ufuncs và làm tròn (Bài 9–16)

**Bài 9.** Cho mảng sau, tính căn bậc hai của từng phần tử.

```python
a = np.array([1, 4, 9, 16, 25])
```

*Lời giải:*
```python
print(np.sqrt(a))   # [1. 2. 3. 4. 5.]
```
> `np.sqrt()` áp dụng công thức căn bậc hai lên từng phần tử, luôn trả về kiểu float.

**Bài 10.** Cho mảng sau, tính `e^a` (số mũ tự nhiên) bằng `np.exp()`.

```python
a = np.array([1, 2, 3])
```

*Lời giải:*
```python
print(np.exp(a))   # [2.718 7.389 20.086]
```
> `np.exp(x)` tính $e^x$ cho từng phần tử — hàm này thường dùng trong các công thức tăng trưởng, xác suất, và các hàm kích hoạt trong học máy.

**Bài 11.** Cho mảng sau, tính log tự nhiên (`np.log`) và log cơ số 10 (`np.log10`) của mảng.

```python
a = np.array([1, 10, 100, 1000])
```

*Lời giải:*
```python
print(np.log(a))     # [0. 2.303 4.605 6.908]
print(np.log10(a))   # [0. 1. 2. 3.]
```
> `np.log()` mặc định là log tự nhiên (cơ số $e$), khác với `np.log10()` (cơ số 10) và `np.log2()` (cơ số 2).

**Bài 12.** Cho mảng sau, làm tròn từng phần tử đến 2 chữ số thập phân.

```python
a = np.array([3.14159, 2.71828, 1.41421])
```

*Lời giải:*
```python
print(np.round(a, 2))   # [3.14 2.72 1.41]
```
> `np.round(array, decimals)` làm tròn từng phần tử đến số chữ số thập phân chỉ định.

**Bài 13.** Cho mảng sau, so sánh kết quả của `np.floor(a)` và `np.ceil(a)`.

```python
a = np.array([3.2, 3.5, 3.9, -2.3])
```

*Lời giải:*
```python
print(np.floor(a))   # [ 3.  3.  3. -3.]
print(np.ceil(a))    # [ 4.  4.  4. -2.]
```
> `np.floor()` luôn làm tròn xuống (về phía âm vô cực), `np.ceil()` luôn làm tròn lên (về phía dương vô cực) — kể cả với số âm.

**Bài 14.** Cho mảng góc sau, tính `np.sin()` và `np.cos()` của mảng này.

```python
angles = np.array([0, np.pi/2, np.pi])
```

*Lời giải:*
```python
print(np.sin(angles))   # [0.000e+00 1.000e+00 1.225e-16]
print(np.cos(angles))   # [ 1.000e+00  6.123e-17 -1.000e+00]
```
> Các hàm lượng giác nhận đầu vào là radian, không phải độ. Giá trị gần 0 nhưng không tuyệt đối bằng 0 là do sai số dấu phẩy động, không phải lỗi tính toán.

**Bài 15.** Cho mảng sau, tính căn bậc hai và log cơ số 2 (`np.log2`) của từng phần tử.

```python
a = np.array([8, 27, 64, 125])
```

*Lời giải:*
```python
print(np.sqrt(a))   # [ 2.828  5.196  8.    11.180]
print(np.log2(a))   # [3.    4.755 6.    6.966]
```
> `np.sqrt()` và `np.log2()` đều là ufuncs áp dụng độc lập lên từng phần tử; chỉ những phần tử là lũy thừa đúng của 2 (như 8, 64) mới cho log2 là số nguyên tròn.

**Bài 16.** Cho mảng sau, tính `np.abs(a)` rồi làm tròn kết quả đó đến số nguyên gần nhất bằng `np.round()`.

```python
a = np.array([-5.7, 2.3, -1.1, 4.8])
```

*Lời giải:*
```python
b = np.abs(a)
print(np.round(b))   # [6. 2. 1. 5.]
```
> `np.abs()` loại bỏ dấu âm trước, sau đó `np.round()` không truyền `decimals` sẽ mặc định làm tròn đến số nguyên gần nhất.

## Phần 3: Hàm tổng hợp (Aggregate) (Bài 17–24)

**Bài 17.** Cho mảng sau, tính tổng, trung bình, giá trị nhỏ nhất và lớn nhất.

```python
a = np.array([4, 8, 15, 16, 23, 42])
```

*Lời giải:*
```python
print(np.sum(a))    # 108
print(np.mean(a))   # 18.0
print(np.min(a))    # 4
print(np.max(a))    # 42
```
> Đây là các hàm tổng hợp cơ bản nhất, mỗi hàm rút gọn cả mảng thành một giá trị duy nhất.

**Bài 18.** Cho mảng 2D sau, tính tổng theo từng cột (`axis=0`) và tổng theo từng hàng (`axis=1`).

```python
m = np.array([[1, 2, 3], [4, 5, 6]])
```

*Lời giải:*
```python
print(np.sum(m, axis=0))   # [5 7 9]
print(np.sum(m, axis=1))   # [6 15]
```
> `axis=0` "đi xuống" theo các hàng, cộng các giá trị cùng cột. `axis=1` "đi ngang" theo các cột, cộng các giá trị cùng hàng.

**Bài 19.** Cho mảng sau, tìm chỉ số (index) của phần tử nhỏ nhất và lớn nhất.

```python
a = np.array([10, 2, 33, 4, 55])
```

*Lời giải:*
```python
print(np.argmin(a))   # 1
print(np.argmax(a))   # 4
```
> `argmin`/`argmax` trả về vị trí của giá trị nhỏ nhất/lớn nhất, khác với `min`/`max` trả về chính giá trị đó.

**Bài 20.** Cho mảng sau, tính độ lệch chuẩn (`std`) và phương sai (`var`) của mảng.

```python
a = np.array([2, 4, 6, 8, 10])
```

*Lời giải:*
```python
print(np.std(a))   # 2.828...
print(np.var(a))   # 8.0
```
> Phương sai đo mức độ phân tán của dữ liệu quanh giá trị trung bình; độ lệch chuẩn là căn bậc hai của phương sai, cùng đơn vị với dữ liệu gốc.

**Bài 21.** Cho mảng sau, tính tích của tất cả các phần tử (`np.prod`) và tổng tích lũy (`np.cumsum`).

```python
a = np.array([1, 2, 3, 4])
```

*Lời giải:*
```python
print(np.prod(a))     # 24
print(np.cumsum(a))   # [ 1  3  6 10]
```
> `np.prod()` nhân tất cả phần tử thành một số duy nhất. `np.cumsum()` trả về mảng cùng kích thước, mỗi phần tử là tổng cộng dồn từ đầu đến vị trí đó.

**Bài 22.** Cho mảng điểm thi sau (mỗi hàng là điểm 3 môn của 1 học sinh), tính điểm trung bình của mỗi học sinh (theo hàng).

```python
scores = np.array([[7, 8, 6], [9, 5, 10], [4, 7, 8]])
```

*Lời giải:*
```python
print(np.mean(scores, axis=1))   # [7. 8. 6.333...]
```
> Vì mỗi học sinh nằm trên một hàng riêng, cần lấy trung bình theo hàng — tức `axis=1`.

**Bài 23.** Với mảng `scores` ở Bài 22, tìm học sinh có điểm trung bình cao nhất bằng cách kết hợp `np.mean()` với `np.argmax()`.

*Lời giải:*
```python
avg = np.mean(scores, axis=1)
best_student = np.argmax(avg)
print(best_student)   # 1 (học sinh thứ hai, chỉ số 1)
```
> Kỹ thuật phổ biến: tính một mảng trung gian (`avg`), rồi dùng `argmax` trên mảng đó để tìm vị trí giá trị lớn nhất.

**Bài 24.** Cho mảng sau, không dùng vòng lặp, đếm xem có bao nhiêu phần tử âm trong mảng.

```python
a = np.array([5, -2, 8, -9, 3])
```

*Lời giải:*
```python
count_negative = np.sum(a < 0)
print(count_negative)   # 2
```
> `a < 0` tạo mảng boolean; khi cộng tổng, NumPy coi `True = 1` và `False = 0`, nên tổng chính là số lượng phần tử thỏa điều kiện.

## Phần 4: So sánh và Đại số tuyến tính (Bài 25–32)

**Bài 25.** Cho hai mảng sau, so sánh từng phần tử bằng `>`, và kiểm tra xem hai mảng có hoàn toàn giống nhau không bằng `np.array_equal()`.

```python
a = np.array([1, 5, 3, 8])
b = np.array([2, 5, 1, 9])
```

*Lời giải:*
```python
print(a > b)                    # [False False  True False]
print(np.array_equal(a, b))     # False
```
> `>` trả về mảng boolean so sánh từng cặp phần tử. `np.array_equal()` trả về một giá trị boolean duy nhất, chỉ `True` khi toàn bộ mảng giống hệt nhau.

**Bài 26.** Cho hai ma trận sau, tính `m1 * m2` (element-wise) và `m1 @ m2` (nhân ma trận), so sánh sự khác biệt.

```python
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])
```

*Lời giải:*
```python
print(m1 * m2)
# [[ 5 12] [21 32]]
print(m1 @ m2)
# [[19 22] [43 50]]
```
> `*` nhân từng phần tử tại cùng vị trí. `@` thực hiện phép nhân ma trận thực sự: phần tử `[i,j]` của kết quả là tích vô hướng của hàng `i` trong `m1` và cột `j` trong `m2`.

**Bài 27.** Cho ma trận sau, tính ma trận chuyển vị (transpose) của nó và so sánh `shape` trước/sau.

```python
m = np.array([[1, 2, 3], [4, 5, 6]])
```

*Lời giải:*
```python
print(m.shape)     # (2, 3)
print(m.T)
# [[1 4] [2 5] [3 6]]
print(m.T.shape)   # (3, 2)
```
> Chuyển vị đổi hàng thành cột và ngược lại, nên `shape` cũng bị đảo ngược.

**Bài 28.** Cho ma trận vuông sau, tính định thức (determinant) và ma trận nghịch đảo (inverse) của nó.

```python
m = np.array([[4, 2], [1, 3]])
```

*Lời giải:*
```python
print(np.linalg.det(m))   # 10.0
print(np.linalg.inv(m))
# [[ 0.3 -0.2] [-0.1  0.4]]
```
> Định thức khác 0 nghĩa là ma trận khả nghịch. Nếu định thức bằng 0, `np.linalg.inv()` sẽ báo lỗi vì ma trận đó suy biến (singular).

**Bài 29.** Giải hệ phương trình tuyến tính sau bằng `np.linalg.solve()`: $3x + y = 9$ và $x + 2y = 8$.

```python
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
```

*Lời giải:*
```python
x = np.linalg.solve(A, b)
print(x)   # [2. 3.]
```
> Hệ phương trình được viết dưới dạng ma trận $Ax = b$. `np.linalg.solve()` giải trực tiếp và chính xác hơn so với `inv(A) @ b`.

**Bài 30.** Cho ma trận sau, tính vết (trace) bằng `np.trace()`.

```python
m = np.array([[5, 1, 2], [0, 3, 4], [0, 0, 6]])
```

*Lời giải:*
```python
print(np.trace(m))   # 14
```
> `np.trace()` chỉ cộng các phần tử trên đường chéo chính: 5 + 3 + 6 = 14.

**Bài 31.** Cho hai mảng sau, so sánh chúng bằng `==` và bằng `np.array_equal()`, giải thích vì sao hai kết quả có ý nghĩa khác nhau.

```python
a = np.array([3, 6, 9])
b = np.array([3, 6, 10])
```

*Lời giải:*
```python
print(a == b)                # [ True  True False]
print(np.array_equal(a, b))  # False
```
> `==` trả về một mảng boolean so sánh từng cặp phần tử. `np.array_equal()` gộp toàn bộ kết quả đó lại thành một giá trị duy nhất — chỉ `True` khi *tất cả* các phần tử đều khớp.

**Bài 32.** Cho ma trận sau, dùng `np.dot()` để nhân `m` với chính nó, sau đó dùng `np.matmul()` để kiểm tra lại kết quả có giống nhau không.

```python
m = np.array([[2, 0], [0, 2]])
```

*Lời giải:*
```python
print(np.dot(m, m))
# [[4 0] [0 4]]
print(np.matmul(m, m))
# [[4 0] [0 4]]
```
> Với mảng 2D, `np.dot()` và `np.matmul()` cho kết quả giống hệt nhau — cả hai đều thực hiện phép nhân ma trận chuẩn.

## Phần 5: Broadcasting nâng cao (Bài 33–40)

**Bài 33.** Cho ma trận và vector sau, tính `m + v` và giải thích vì sao phép cộng này hợp lệ dù hai mảng khác kích thước.

```python
m = np.array([[1, 2, 3], [4, 5, 6]])   # shape (2,3)
v = np.array([10, 20, 30])              # shape (3,)
```

*Lời giải:*
```python
print(m + v)
# [[11 22 33] [14 25 36]]
```
> NumPy so sánh kích thước hai mảng từ phải sang trái: chiều cuối của `m` là 3, khớp với chiều duy nhất của `v`. `v` được nhân bản thành 2 hàng để cộng với từng hàng của `m`.

**Bài 34.** Cho ma trận `m` ở Bài 33 và vector cột sau, tính `m + col` và giải thích kết quả.

```python
col = np.array([[100], [200]])   # shape (2,1)
```

*Lời giải:*
```python
print(m + col)
# [[101 102 103] [204 205 206]]
```
> `col` có shape `(2,1)` — chiều cuối là 1 được broadcast để khớp với chiều cuối của `m` (3); chiều đầu (2) khớp trực tiếp với `m`. Mỗi hàng của `m` được cộng với đúng một giá trị tương ứng trong `col`.

**Bài 35.** Cho mảng nhiệt độ theo độ C sau, không dùng vòng lặp, chuyển toàn bộ sang độ F bằng công thức $F = C \times 9/5 + 32$.

```python
celsius = np.array([0, 20, 37, 100])
```

*Lời giải:*
```python
fahrenheit = celsius * 9/5 + 32
print(fahrenheit)   # [ 32.  68.  98.6 212. ]
```
> Toàn bộ công thức được áp dụng cho cả mảng cùng lúc nhờ broadcasting với các số vô hướng (`9/5` và `32`).

**Bài 36.** Cho ma trận điểm và mảng trọng số sau (ứng với 3 môn học), tính điểm trung bình có trọng số của mỗi học sinh bằng phép nhân element-wise kết hợp `np.sum(axis=1)`.

```python
scores = np.array([[70, 80, 90], [60, 75, 85]])
weights = np.array([0.2, 0.3, 0.5])
```

*Lời giải:*
```python
weighted = scores * weights
result = np.sum(weighted, axis=1)
print(result)   # [83. 76.]
```
> `scores * weights` dùng broadcasting để nhân từng cột điểm với trọng số tương ứng. `np.sum(axis=1)` cộng dồn theo hàng để ra điểm trung bình có trọng số của từng học sinh.

**Bài 37.** Cho mảng giá sản phẩm và mảng thuế suất theo từng khu vực sau, tính giá sau thuế cho mỗi sản phẩm ở mỗi khu vực (kết quả mong đợi có shape `(3,3)`).

```python
prices = np.array([100, 250, 400])            # shape (3,)
tax_rates = np.array([[0.05], [0.10], [0.15]]) # shape (3,1)
```

*Lời giải:*
```python
result = prices * (1 + tax_rates)
print(result)
# [[105.  262.5 420. ]
#  [110.  275.  440. ]
#  [115.  287.5 460. ]]
```
> `prices` (shape `(3,)`) và `1 + tax_rates` (shape `(3,1)`) được broadcast lẫn nhau: mỗi hàng của kết quả ứng với một khu vực (một mức thuế), mỗi cột ứng với một sản phẩm — tạo ra bảng giá đầy đủ `(3,3)` chỉ bằng một phép nhân.

**Bài 38.** Cho mảng nhiệt độ trong tuần và mảng hiệu chỉnh sau (3 ngày, 3 lần đo mỗi ngày), cộng `offset` vào từng hàng của `week` bằng broadcasting.

```python
week = np.array([[20, 22, 25], [18, 19, 21], [23, 24, 26]])
offset = np.array([1, -1, 0])
```

*Lời giải:*
```python
result = week + offset
print(result)
# [[21 21 25]
#  [19 18 21]
#  [24 23 26]]
```
> `offset` có shape `(3,)`, khớp với chiều cuối (số cột) của `week`, nên được cộng vào từng hàng theo đúng vị trí cột tương ứng.

**Bài 39.** Cho mảng sau, dùng broadcasting để tạo bảng cửu chương từ 1 đến 5 của mảng này (gợi ý: reshape `a` thành cột `(5,1)` rồi nhân với chính `a` dạng hàng `(5,)`).

```python
a = np.array([1, 2, 3, 4, 5])
```

*Lời giải:*
```python
table = a.reshape(5, 1) * a
print(table)
# [[ 1  2  3  4  5]
#  [ 2  4  6  8 10]
#  [ 3  6  9 12 15]
#  [ 4  8 12 16 20]
#  [ 5 10 15 20 25]]
```
> `a.reshape(5,1)` có shape `(5,1)`, còn `a` gốc có shape `(5,)`. Broadcasting kết hợp hai chiều này tạo thành mảng kết quả `(5,5)`, trong đó phần tử `[i,j]` chính là `(i+1) * (j+1)` — đây là kỹ thuật tạo bảng nhân/outer product kinh điển không cần vòng lặp.

**Bài 40.** Cho ma trận và số vô hướng sau, không dùng vòng lặp, tính mảng mới trong đó mỗi phần tử được nhân với `k` rồi cộng thêm chỉ số cột của nó (gợi ý: kết hợp phép nhân vô hướng với broadcasting cùng `np.array([0, 1])`).

```python
m = np.array([[1, 2], [3, 4], [5, 6]])   # shape (3,2)
k = 2
col_index = np.array([0, 1])
```

*Lời giải:*
```python
result = m * k + col_index
print(result)
# [[ 2  5]
#  [ 6  9]
#  [10 13]]
```
> `m * k` nhân mọi phần tử với 2. Sau đó `col_index` (shape `(2,)`) được broadcast để cộng thêm 0 vào cột 0 và 1 vào cột 1 của mọi hàng — kết hợp hai kiểu broadcasting (số vô hướng và vector hàng) trong cùng một biểu thức.
