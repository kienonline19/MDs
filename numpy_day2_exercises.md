# 30 Bài Tập NumPy: Các Phép Toán Học

*Từ cơ bản đến nâng cao nhẹ — kèm đáp án và giải thích ngắn gọn.*

## Phần 1: Phép toán element-wise và với số vô hướng (Bài 1–6)

**Bài 1.** Cho `a = np.array([1, 2, 3, 4])` và `b = np.array([10, 20, 30, 40])`. Tính `a + b`, `a - b`, `a * b`, `a / b`.

<details>
<summary>Đáp án</summary>

```python
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
print(a + b)   # [11 22 33 44]
print(a - b)   # [-9 -18 -27 -36]
print(a * b)   # [10 40 90 160]
print(a / b)   # [0.1 0.1 0.1 0.1]
```
> Các phép toán được thực hiện **theo từng phần tử tương ứng** (element-wise), không phải phép toán ma trận.
</details>

**Bài 2.** Cho `a = np.array([2, 5, 9, 14])`. Tính phần dư khi chia cho 4 (`%`) và phần nguyên khi chia cho 4 (`//`).

<details>
<summary>Đáp án</summary>

```python
a = np.array([2, 5, 9, 14])
print(a % 4)    # [2 1 1 2]
print(a // 4)   # [0 1 2 3]
```
> `%` trả về phần dư, `//` trả về thương nguyên (làm tròn xuống), áp dụng cho từng phần tử.
</details>

**Bài 3.** Cho `a = np.array([1, 2, 3])`. Tính `a + 10`, `a * 3`, `a ** 2`.

<details>
<summary>Đáp án</summary>

```python
a = np.array([1, 2, 3])
print(a + 10)   # [11 12 13]
print(a * 3)    # [3 6 9]
print(a ** 2)   # [1 4 9]
```
> Khi thực hiện phép toán giữa mảng và một số đơn (scalar), NumPy "phát" (broadcast) số đó ra để áp dụng cho mọi phần tử — không cần vòng lặp.
</details>

**Bài 4.** Cho hai mảng 2D `m1 = np.array([[1, 2], [3, 4]])` và `m2 = np.array([[10, 20], [30, 40]])`. Tính `m1 + m2` và `m1 * m2` (element-wise, không phải nhân ma trận).

<details>
<summary>Đáp án</summary>

```python
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[10, 20], [30, 40]])
print(m1 + m2)
# [[11 22] [33 44]]
print(m1 * m2)
# [[10 40] [90 160]]
```
> Với mảng 2D, các phép toán `+`, `-`, `*`, `/` vẫn hoạt động theo từng phần tử tại cùng vị trí, giống hệt mảng 1D.
</details>

**Bài 5.** Cho `a = np.array([-3, -1, 0, 2, 5])`. Tính giá trị tuyệt đối của từng phần tử.

<details>
<summary>Đáp án</summary>

```python
a = np.array([-3, -1, 0, 2, 5])
print(np.abs(a))   # [3 1 0 2 5]
```
> `np.abs()` là một ufunc, áp dụng lên từng phần tử độc lập và trả về mảng mới cùng kích thước.
</details>

**Bài 6.** Cho `a = np.array([7, 12, 25])` và `b = np.array([2, 5, 4])`. Tính `a // b` và giải thích tại sao kết quả khác với `a / b`.

<details>
<summary>Đáp án</summary>

```python
a = np.array([7, 12, 25])
b = np.array([2, 5, 4])
print(a // b)   # [3 2 6]
print(a / b)    # [3.5 2.4 6.25]
```
> `/` luôn trả về kết quả kiểu số thực (float), kể cả khi chia hết. `//` chỉ lấy phần nguyên của phép chia (làm tròn xuống), nên mất đi phần dư.
</details>

## Phần 2: Ufuncs và làm tròn (Bài 7–12)

**Bài 7.** Cho `a = np.array([1, 4, 9, 16, 25])`. Tính căn bậc hai của từng phần tử.

<details>
<summary>Đáp án</summary>

```python
a = np.array([1, 4, 9, 16, 25])
print(np.sqrt(a))   # [1. 2. 3. 4. 5.]
```
> `np.sqrt()` áp dụng công thức căn bậc hai lên từng phần tử, luôn trả về kiểu float.
</details>

**Bài 8.** Cho `a = np.array([1, 2, 3])`. Tính `e^a` (số mũ tự nhiên) bằng `np.exp()`.

<details>
<summary>Đáp án</summary>

```python
a = np.array([1, 2, 3])
print(np.exp(a))   # [2.718 7.389 20.086]
```
> `np.exp(x)` tính $e^x$ cho từng phần tử — hàm này thường dùng trong các công thức tăng trưởng, xác suất, và các hàm kích hoạt trong học máy (như softmax).
</details>

**Bài 9.** Cho `a = np.array([1, 10, 100, 1000])`. Tính log tự nhiên (`np.log`) và log cơ số 10 (`np.log10`) của mảng.

<details>
<summary>Đáp án</summary>

```python
a = np.array([1, 10, 100, 1000])
print(np.log(a))     # [0. 2.303 4.605 6.908]
print(np.log10(a))   # [0. 1. 2. 3.]
```
> `np.log()` mặc định là log tự nhiên (cơ số $e$), khác với `np.log10()` (cơ số 10) và `np.log2()` (cơ số 2) — cần chọn đúng hàm theo yêu cầu bài toán.
</details>

**Bài 10.** Cho `a = np.array([3.14159, 2.71828, 1.41421])`. Làm tròn từng phần tử đến 2 chữ số thập phân.

<details>
<summary>Đáp án</summary>

```python
a = np.array([3.14159, 2.71828, 1.41421])
print(np.round(a, 2))   # [3.14 2.72 1.41]
```
> `np.round(array, decimals)` làm tròn từng phần tử đến số chữ số thập phân chỉ định, theo quy tắc làm tròn "ngân hàng" (round half to even) của NumPy.
</details>

**Bài 11.** Cho `a = np.array([3.2, 3.5, 3.9, -2.3])`. So sánh kết quả của `np.floor(a)` và `np.ceil(a)`.

<details>
<summary>Đáp án</summary>

```python
a = np.array([3.2, 3.5, 3.9, -2.3])
print(np.floor(a))   # [ 3.  3.  3. -3.]
print(np.ceil(a))    # [ 4.  4.  4. -2.]
```
> `np.floor()` luôn làm tròn **xuống** (về phía âm vô cực), `np.ceil()` luôn làm tròn **lên** (về phía dương vô cực) — kể cả với số âm, đây là điểm hay gây nhầm lẫn.
</details>

**Bài 12.** Cho một mảng góc `angles = np.array([0, np.pi/2, np.pi])`. Tính `np.sin()` và `np.cos()` của mảng này.

<details>
<summary>Đáp án</summary>

```python
angles = np.array([0, np.pi/2, np.pi])
print(np.sin(angles))   # [0.000e+00 1.000e+00 1.225e-16]
print(np.cos(angles))   # [ 1.000e+00  6.123e-17 -1.000e+00]
```
> Các hàm lượng giác nhận đầu vào là **radian**, không phải độ. Giá trị gần 0 nhưng không tuyệt đối bằng 0 (ví dụ `1.225e-16`) là do sai số dấu phẩy động (floating-point), không phải lỗi tính toán.
</details>

## Phần 3: Hàm tổng hợp (Aggregate) (Bài 13–20)

**Bài 13.** Cho `a = np.array([4, 8, 15, 16, 23, 42])`. Tính tổng, trung bình, giá trị nhỏ nhất và lớn nhất.

<details>
<summary>Đáp án</summary>

```python
a = np.array([4, 8, 15, 16, 23, 42])
print(np.sum(a))    # 108
print(np.mean(a))   # 18.0
print(np.min(a))    # 4
print(np.max(a))    # 42
```
> Đây là các hàm tổng hợp cơ bản nhất, mỗi hàm rút gọn cả mảng thành một giá trị duy nhất.
</details>

**Bài 14.** Cho mảng 2D `m = np.array([[1, 2, 3], [4, 5, 6]])`. Tính tổng theo từng cột (`axis=0`) và tổng theo từng hàng (`axis=1`).

<details>
<summary>Đáp án</summary>

```python
m = np.array([[1, 2, 3], [4, 5, 6]])
print(np.sum(m, axis=0))   # [5 7 9]
print(np.sum(m, axis=1))   # [6 15]
```
> `axis=0` "đi xuống" theo các hàng, tức cộng các giá trị **cùng cột** lại với nhau → kết quả có độ dài bằng số cột. `axis=1` "đi ngang" theo các cột, cộng các giá trị **cùng hàng** → kết quả có độ dài bằng số hàng.
</details>

**Bài 15.** Cho `a = np.array([10, 2, 33, 4, 55])`. Tìm chỉ số (index) của phần tử nhỏ nhất và lớn nhất.

<details>
<summary>Đáp án</summary>

```python
a = np.array([10, 2, 33, 4, 55])
print(np.argmin(a))   # 1
print(np.argmax(a))   # 4
```
> `argmin`/`argmax` trả về **vị trí** của giá trị nhỏ nhất/lớn nhất, khác với `min`/`max` trả về chính giá trị đó.
</details>

**Bài 16.** Cho `a = np.array([2, 4, 6, 8, 10])`. Tính độ lệch chuẩn (`std`) và phương sai (`var`) của mảng.

<details>
<summary>Đáp án</summary>

```python
a = np.array([2, 4, 6, 8, 10])
print(np.std(a))   # 2.828...
print(np.var(a))   # 8.0
```
> Phương sai (`var`) đo mức độ phân tán của dữ liệu quanh giá trị trung bình; độ lệch chuẩn (`std`) chính là căn bậc hai của phương sai, cùng đơn vị với dữ liệu gốc nên dễ diễn giải hơn.
</details>

**Bài 17.** Cho `a = np.array([1, 2, 3, 4])`. Tính tích của tất cả các phần tử (`np.prod`) và tổng tích lũy (`np.cumsum`).

<details>
<summary>Đáp án</summary>

```python
a = np.array([1, 2, 3, 4])
print(np.prod(a))     # 24
print(np.cumsum(a))   # [ 1  3  6 10]
```
> `np.prod()` nhân tất cả các phần tử lại với nhau thành một số duy nhất. `np.cumsum()` trả về một mảng cùng kích thước, trong đó mỗi phần tử là **tổng cộng dồn** từ đầu đến vị trí đó.
</details>

**Bài 18.** Cho mảng điểm thi `scores = np.array([[7, 8, 6], [9, 5, 10], [4, 7, 8]])` (mỗi hàng là điểm 3 môn của 1 học sinh). Tính điểm trung bình của **mỗi học sinh** (theo hàng).

<details>
<summary>Đáp án</summary>

```python
scores = np.array([[7, 8, 6], [9, 5, 10], [4, 7, 8]])
print(np.mean(scores, axis=1))   # [7. 8. 6.333...]
```
> Vì mỗi học sinh nằm trên một hàng riêng và có 3 điểm (3 cột), cần lấy trung bình **theo hàng** — tức `axis=1`, để mỗi học sinh cho ra đúng một kết quả trung bình.
</details>

**Bài 19.** Với mảng `scores` ở Bài 18, tìm học sinh có điểm trung bình cao nhất bằng cách kết hợp `np.mean()` với `np.argmax()`.

<details>
<summary>Đáp án</summary>

```python
avg = np.mean(scores, axis=1)
best_student = np.argmax(avg)
print(best_student)   # 1 (học sinh thứ hai, chỉ số 1)
```
> Kỹ thuật phổ biến: tính một mảng trung gian (`avg`), rồi dùng `argmax` trên mảng trung gian đó để tìm vị trí giá trị lớn nhất — thay vì tìm trực tiếp trên dữ liệu gốc.
</details>

**Bài 20.** Cho `a = np.array([5, -2, 8, -9, 3])`. Không dùng vòng lặp, đếm xem có bao nhiêu phần tử âm trong mảng (gợi ý: `np.sum()` trên mảng boolean).

<details>
<summary>Đáp án</summary>

```python
a = np.array([5, -2, 8, -9, 3])
count_negative = np.sum(a < 0)
print(count_negative)   # 2
```
> `a < 0` tạo ra mảng boolean `[False, True, False, True, False]`. Khi cộng tổng (`np.sum`), NumPy tự động coi `True = 1` và `False = 0`, nên tổng chính là số lượng phần tử thỏa điều kiện.
</details>

## Phần 4: So sánh và Đại số tuyến tính (Bài 21–26)

**Bài 21.** Cho `a = np.array([1, 5, 3, 8])` và `b = np.array([2, 5, 1, 9])`. So sánh từng phần tử bằng `>`, và kiểm tra xem hai mảng có hoàn toàn giống nhau không bằng `np.array_equal()`.

<details>
<summary>Đáp án</summary>

```python
a = np.array([1, 5, 3, 8])
b = np.array([2, 5, 1, 9])
print(a > b)                    # [False False  True False]
print(np.array_equal(a, b))     # False
```
> `>` trả về mảng boolean so sánh **từng cặp phần tử** tương ứng. `np.array_equal()` trả về **một giá trị boolean duy nhất**, chỉ `True` khi toàn bộ mảng giống hệt nhau cả về kích thước lẫn giá trị.
</details>

**Bài 22.** Cho hai ma trận `m1 = np.array([[1, 2], [3, 4]])` và `m2 = np.array([[5, 6], [7, 8]])`. Tính `m1 * m2` (element-wise) và `m1 @ m2` (nhân ma trận), so sánh sự khác biệt.

<details>
<summary>Đáp án</summary>

```python
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])
print(m1 * m2)
# [[ 5 12] [21 32]]
print(m1 @ m2)
# [[19 22] [43 50]]
```
> `*` nhân từng phần tử tại cùng vị trí (không liên quan gì đến đại số tuyến tính). `@` thực hiện phép nhân ma trận thực sự: phần tử `[i,j]` của kết quả là tích vô hướng của hàng `i` trong `m1` và cột `j` trong `m2`. Đây là lỗi rất phổ biến khi mới học NumPy.
</details>

**Bài 23.** Cho ma trận `m = np.array([[1, 2, 3], [4, 5, 6]])`. Tính ma trận chuyển vị (transpose) của nó và so sánh `shape` trước/sau.

<details>
<summary>Đáp án</summary>

```python
m = np.array([[1, 2, 3], [4, 5, 6]])
print(m.shape)     # (2, 3)
print(m.T)
# [[1 4] [2 5] [3 6]]
print(m.T.shape)   # (3, 2)
```
> Chuyển vị (`T`) đổi hàng thành cột và ngược lại, nên `shape` cũng bị đảo ngược từ `(2, 3)` thành `(3, 2)`.
</details>

**Bài 24.** Cho ma trận vuông `m = np.array([[4, 2], [1, 3]])`. Tính định thức (determinant) và ma trận nghịch đảo (inverse) của nó.

<details>
<summary>Đáp án</summary>

```python
m = np.array([[4, 2], [1, 3]])
print(np.linalg.det(m))   # 10.0
print(np.linalg.inv(m))
# [[ 0.3 -0.2] [-0.1  0.4]]
```
> Định thức khác 0 (ở đây là 10) nghĩa là ma trận **khả nghịch** (có ma trận nghịch đảo). Nếu định thức bằng 0, `np.linalg.inv()` sẽ báo lỗi vì ma trận đó là "suy biến" (singular).
</details>

**Bài 25.** Giải hệ phương trình tuyến tính: $3x + y = 9$ và $x + 2y = 8$, dùng `np.linalg.solve()`.

<details>
<summary>Đáp án</summary>

```python
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
x = np.linalg.solve(A, b)
print(x)   # [2. 3.]
```
> Hệ phương trình được viết lại dưới dạng ma trận $Ax = b$, trong đó mỗi hàng của `A` là hệ số của một phương trình. `np.linalg.solve()` giải trực tiếp và chính xác hơn nhiều so với việc tự tính bằng `inv(A) @ b`.
</details>

**Bài 26.** Cho ma trận `m = np.array([[5, 1, 2], [0, 3, 4], [0, 0, 6]])`. Tính vết (trace — tổng các phần tử trên đường chéo chính) bằng `np.trace()`.

<details>
<summary>Đáp án</summary>

```python
m = np.array([[5, 1, 2], [0, 3, 4], [0, 0, 6]])
print(np.trace(m))   # 14
```
> `np.trace()` chỉ cộng các phần tử `[0,0], [1,1], [2,2]` (tức 5 + 3 + 6 = 14), bỏ qua toàn bộ các phần tử khác trong ma trận.
</details>

## Phần 5: Broadcasting nâng cao (Bài 27–30)

**Bài 27.** Cho ma trận `m = np.array([[1, 2, 3], [4, 5, 6]])` (shape `(2,3)`) và vector `v = np.array([10, 20, 30])` (shape `(3,)`). Tính `m + v` và giải thích vì sao phép cộng này hợp lệ dù hai mảng khác kích thước.

<details>
<summary>Đáp án</summary>

```python
m = np.array([[1, 2, 3], [4, 5, 6]])
v = np.array([10, 20, 30])
print(m + v)
# [[11 22 33] [14 25 36]]
```
> NumPy so sánh kích thước hai mảng **từ phải sang trái**: chiều cuối của `m` là 3, chiều cuối (duy nhất) của `v` cũng là 3 → khớp. `v` được "nhân bản" (broadcast) thành 2 hàng để cộng với từng hàng của `m` — không cần viết vòng lặp hay copy dữ liệu thủ công.
</details>

**Bài 28.** Cho ma trận `m` ở Bài 27 và vector cột `col = np.array([[100], [200]])` (shape `(2,1)`). Tính `m + col` và giải thích kết quả.

<details>
<summary>Đáp án</summary>

```python
col = np.array([[100], [200]])
print(m + col)
# [[101 102 103] [204 205 206]]
```
> Ở đây `col` có shape `(2,1)` — chiều cuối là 1, được broadcast để khớp với chiều cuối của `m` (là 3); đồng thời chiều đầu của `col` là 2, khớp với chiều đầu của `m`. Kết quả: mỗi hàng của `m` được cộng với đúng một giá trị tương ứng trong `col` (hàng 0 cộng 100, hàng 1 cộng 200).
</details>

**Bài 29.** Cho mảng nhiệt độ theo độ C: `celsius = np.array([0, 20, 37, 100])`. Không dùng vòng lặp, chuyển toàn bộ sang độ F bằng công thức $F = C \times 9/5 + 32$.

<details>
<summary>Đáp án</summary>

```python
celsius = np.array([0, 20, 37, 100])
fahrenheit = celsius * 9/5 + 32
print(fahrenheit)   # [ 32.  68.  98.6 212. ]
```
> Toàn bộ công thức được áp dụng cho **cả mảng cùng lúc** nhờ broadcasting với các số vô hướng (`9/5` và `32`) — đây là cách viết công thức toán học "tự nhiên" nhất trong NumPy, không cần `for`.
</details>

**Bài 30.** Cho ma trận điểm `scores = np.array([[70, 80, 90], [60, 75, 85]])` và một mảng trọng số `weights = np.array([0.2, 0.3, 0.5])` (ứng với 3 môn học). Tính điểm trung bình có trọng số của mỗi học sinh bằng phép nhân element-wise kết hợp `np.sum(axis=1)`.

<details>
<summary>Đáp án</summary>

```python
scores = np.array([[70, 80, 90], [60, 75, 85]])
weights = np.array([0.2, 0.3, 0.5])

weighted = scores * weights
result = np.sum(weighted, axis=1)
print(result)   # [83. 76.]
```
> `scores * weights` dùng broadcasting để nhân từng cột điểm với trọng số tương ứng (weights có shape `(3,)` khớp với chiều cuối của `scores`). Sau đó `np.sum(axis=1)` cộng dồn theo hàng để ra điểm trung bình có trọng số của từng học sinh — đây chính là ý tưởng cốt lõi đằng sau phép nhân ma trận - vector.
</details>

---

### Gợi ý sư phạm
- Các bài 22 và 27–30 là những bài **dễ gây hiểu nhầm nhất** (nhân element-wise vs. nhân ma trận, và broadcasting) — nên dành thời gian giảng kỹ và cho học sinh tự in `shape` ra để kiểm chứng trước khi tính.
- Có thể chia lớp làm hai nhóm: nhóm giải Phần 1–3 (cơ bản đến trung bình), nhóm giải Phần 4–5 (nâng cao hơn) nếu thời gian tiết học có hạn.