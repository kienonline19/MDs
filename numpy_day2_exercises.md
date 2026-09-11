# 40 Bài Tập NumPy: Các Phép Toán Học

*Từ cơ bản đến nâng cao nhẹ.*

## Phần 1: Phép toán element-wise và với số vô hướng (Bài 1–8)

**Bài 1.** Cho hai mảng sau, tính `a + b`, `a - b`, `a * b`, `a / b`.

```python
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
```

**Bài 2.** Cho mảng sau, tính phần dư khi chia cho 4 (`%`) và phần nguyên khi chia cho 4 (`//`).

```python
a = np.array([2, 5, 9, 14])
```

**Bài 3.** Cho mảng sau, tính `a + 10`, `a * 3`, `a ** 2`.

```python
a = np.array([1, 2, 3])
```

**Bài 4.** Cho hai mảng 2D sau, tính `m1 + m2` và `m1 * m2` (element-wise, không phải nhân ma trận).

```python
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[10, 20], [30, 40]])
```

**Bài 5.** Cho mảng sau, tính giá trị tuyệt đối của từng phần tử.

```python
a = np.array([-3, -1, 0, 2, 5])
```

**Bài 6.** Cho hai mảng sau, tính `a // b` và giải thích tại sao kết quả khác với `a / b`.

```python
a = np.array([7, 12, 25])
b = np.array([2, 5, 4])
```
> Gợi ý: `/` luôn trả về kiểu float; `//` chỉ giữ lại phần nguyên của phép chia.

**Bài 7.** Cho mảng sau, tính `a ** 3` (lập phương từng phần tử).

```python
a = np.array([1, 2, 3, 4, 5])
```

**Bài 8.** Cho hai mảng sau, tính `a % b`.

```python
a = np.array([100, 200, 300])
b = np.array([3, 7, 11])
```

## Phần 2: Ufuncs và làm tròn (Bài 9–16)

**Bài 9.** Cho mảng sau, tính căn bậc hai của từng phần tử.

```python
a = np.array([1, 4, 9, 16, 25])
```
> Gợi ý: dùng `np.sqrt()`.

**Bài 10.** Cho mảng sau, tính `e^a` (số mũ tự nhiên) bằng `np.exp()`.

```python
a = np.array([1, 2, 3])
```

**Bài 11.** Cho mảng sau, tính log tự nhiên (`np.log`) và log cơ số 10 (`np.log10`) của mảng.

```python
a = np.array([1, 10, 100, 1000])
```

**Bài 12.** Cho mảng sau, làm tròn từng phần tử đến 2 chữ số thập phân.

```python
a = np.array([3.14159, 2.71828, 1.41421])
```
> Gợi ý: dùng `np.round(array, decimals)`.

**Bài 13.** Cho mảng sau, so sánh kết quả của `np.floor(a)` và `np.ceil(a)`.

```python
a = np.array([3.2, 3.5, 3.9, -2.3])
```
> Gợi ý: để ý cách hai hàm xử lý số âm.

**Bài 14.** Cho mảng góc sau, tính `np.sin()` và `np.cos()` của mảng này.

```python
angles = np.array([0, np.pi/2, np.pi])
```
> Gợi ý: các hàm lượng giác trong NumPy nhận đầu vào là radian, không phải độ.

**Bài 15.** Cho mảng sau, tính căn bậc hai và log cơ số 2 (`np.log2`) của từng phần tử.

```python
a = np.array([8, 27, 64, 125])
```

**Bài 16.** Cho mảng sau, tính `np.abs(a)` rồi làm tròn kết quả đó đến số nguyên gần nhất bằng `np.round()`.

```python
a = np.array([-5.7, 2.3, -1.1, 4.8])
```
> Gợi ý: `np.round()` không truyền `decimals` sẽ làm tròn đến số nguyên gần nhất.

## Phần 3: Hàm tổng hợp (Aggregate) (Bài 17–24)

**Bài 17.** Cho mảng sau, tính tổng, trung bình, giá trị nhỏ nhất và lớn nhất.

```python
a = np.array([4, 8, 15, 16, 23, 42])
```

**Bài 18.** Cho mảng 2D sau, tính tổng theo từng cột (`axis=0`) và tổng theo từng hàng (`axis=1`).

```python
m = np.array([[1, 2, 3], [4, 5, 6]])
```
> Gợi ý: `axis=0` đi xuống theo hàng (kết quả theo cột), `axis=1` đi ngang theo cột (kết quả theo hàng).

**Bài 19.** Cho mảng sau, tìm chỉ số (index) của phần tử nhỏ nhất và lớn nhất.

```python
a = np.array([10, 2, 33, 4, 55])
```
> Gợi ý: dùng `np.argmin()` và `np.argmax()`, khác với `np.min()`/`np.max()`.

**Bài 20.** Cho mảng sau, tính độ lệch chuẩn (`std`) và phương sai (`var`) của mảng.

```python
a = np.array([2, 4, 6, 8, 10])
```

**Bài 21.** Cho mảng sau, tính tích của tất cả các phần tử (`np.prod`) và tổng tích lũy (`np.cumsum`).

```python
a = np.array([1, 2, 3, 4])
```

**Bài 22.** Cho mảng điểm thi sau (mỗi hàng là điểm 3 môn của 1 học sinh), tính điểm trung bình của mỗi học sinh (theo hàng).

```python
scores = np.array([[7, 8, 6], [9, 5, 10], [4, 7, 8]])
```
> Gợi ý: cần lấy trung bình theo hàng — dùng `axis=1`.

**Bài 23.** Với mảng `scores` ở Bài 22, tìm học sinh có điểm trung bình cao nhất bằng cách kết hợp `np.mean()` với `np.argmax()`.

> Gợi ý: tính mảng trung bình trung gian trước, rồi mới dùng `argmax` trên mảng đó.

**Bài 24.** Cho mảng sau, không dùng vòng lặp, đếm xem có bao nhiêu phần tử âm trong mảng.

```python
a = np.array([5, -2, 8, -9, 3])
```
> Gợi ý: kết hợp mảng boolean (`a < 0`) với `np.sum()`.

## Phần 4: So sánh và Đại số tuyến tính (Bài 25–32)

**Bài 25.** Cho hai mảng sau, so sánh từng phần tử bằng `>`, và kiểm tra xem hai mảng có hoàn toàn giống nhau không bằng `np.array_equal()`.

```python
a = np.array([1, 5, 3, 8])
b = np.array([2, 5, 1, 9])
```

**Bài 26.** Cho hai ma trận sau, tính `m1 * m2` (element-wise) và `m1 @ m2` (nhân ma trận), so sánh sự khác biệt.

```python
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])
```
> Gợi ý: `*` không phải là phép nhân ma trận — đừng nhầm với `@`.

**Bài 27.** Cho ma trận sau, tính ma trận chuyển vị (transpose) của nó và so sánh `shape` trước/sau.

```python
m = np.array([[1, 2, 3], [4, 5, 6]])
```
> Gợi ý: dùng `.T`.

**Bài 28.** Cho ma trận vuông sau, tính định thức (determinant) và ma trận nghịch đảo (inverse) của nó.

```python
m = np.array([[4, 2], [1, 3]])
```
> Gợi ý: dùng `np.linalg.det()` và `np.linalg.inv()`.

**Bài 29.** Giải hệ phương trình tuyến tính sau bằng `np.linalg.solve()`: $3x + y = 9$ và $x + 2y = 8$.

```python
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
```

**Bài 30.** Cho ma trận sau, tính tổng các phần tử trên đường chéo chính (main diagonal) của một ma trận bằng `np.trace()`.

```python
m = np.array([[5, 1, 2], [0, 3, 4], [0, 0, 6]])
```

**Bài 31.** Cho hai mảng sau, so sánh chúng bằng `==` và bằng `np.array_equal()`, giải thích vì sao hai kết quả có ý nghĩa khác nhau.

```python
a = np.array([3, 6, 9])
b = np.array([3, 6, 10])
```
> Gợi ý: `==` so sánh từng phần tử; `np.array_equal()` gộp thành một kết quả duy nhất.

**Bài 32.** Cho ma trận sau, dùng `np.dot()` để nhân `m` với chính nó, sau đó dùng `np.matmul()` để kiểm tra lại kết quả có giống nhau không.

```python
m = np.array([[2, 0], [0, 2]])
```

## Phần 5: Broadcasting nâng cao (Bài 33–40)

**Bài 33.** Cho ma trận và vector sau, tính `m + v` và giải thích vì sao phép cộng này hợp lệ dù hai mảng khác kích thước.

```python
m = np.array([[1, 2, 3], [4, 5, 6]])   # shape (2,3)
v = np.array([10, 20, 30])              # shape (3,)
```
> Gợi ý: NumPy so sánh shape từ phải sang trái để quyết định có broadcast được hay không.

**Bài 34.** Cho ma trận `m` ở Bài 33 và vector cột sau, tính `m + col` và giải thích kết quả.

```python
col = np.array([[100], [200]])   # shape (2,1)
```

**Bài 35.** Cho mảng nhiệt độ theo độ C sau, không dùng vòng lặp, chuyển toàn bộ sang độ F bằng công thức $F = C \times 9/5 + 32$.

```python
celsius = np.array([0, 20, 37, 100])
```

**Bài 36.** Cho ma trận điểm và mảng trọng số sau (ứng với 3 môn học), tính điểm trung bình có trọng số của mỗi học sinh bằng phép nhân element-wise kết hợp `np.sum(axis=1)`.

```python
scores = np.array([[70, 80, 90], [60, 75, 85]])
weights = np.array([0.2, 0.3, 0.5])
```

**Bài 37.** Cho mảng giá sản phẩm và mảng thuế suất theo từng khu vực sau, tính giá sau thuế cho mỗi sản phẩm ở mỗi khu vực (kết quả mong đợi có shape `(3,3)`).

```python
prices = np.array([100, 250, 400])            # shape (3,)
tax_rates = np.array([[0.05], [0.10], [0.15]]) # shape (3,1)
```
> Gợi ý: tính `1 + tax_rates` trước, rồi nhân với `prices`.

**Bài 38.** Cho mảng nhiệt độ trong tuần và mảng hiệu chỉnh sau (3 ngày, 3 lần đo mỗi ngày), cộng `offset` vào từng hàng của `week` bằng broadcasting.

```python
week = np.array([[20, 22, 25], [18, 19, 21], [23, 24, 26]])
offset = np.array([1, -1, 0])
```

**Bài 39.** Cho mảng sau, dùng broadcasting để tạo bảng cửu chương từ 1 đến 5 của mảng này.

```python
a = np.array([1, 2, 3, 4, 5])
```
> Gợi ý: reshape `a` thành cột `(5,1)` rồi nhân với chính `a` dạng hàng `(5,)`.

**Bài 40.** Cho ma trận và số vô hướng sau, không dùng vòng lặp, tính mảng mới trong đó mỗi phần tử được nhân với `k` rồi cộng thêm chỉ số cột của nó.

```python
m = np.array([[1, 2], [3, 4], [5, 6]])   # shape (3,2)
k = 2
col_index = np.array([0, 1])
```
> Gợi ý: kết hợp phép nhân vô hướng (`m * k`) với broadcasting cùng `col_index`.

---

### Gợi ý sư phạm
- Các bài 26 và 33–40 là những bài dễ gây hiểu nhầm nhất (nhân element-wise vs. nhân ma trận, và broadcasting) — nên dành thời gian giảng kỹ và cho học sinh tự in `shape` ra để kiểm chứng trước khi tính.
- Có thể chia lớp làm hai nhóm: nhóm giải Phần 1–3 (cơ bản đến trung bình), nhóm giải Phần 4–5 (nâng cao hơn) nếu thời gian tiết học có hạn.