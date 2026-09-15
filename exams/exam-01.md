# Đề Bài Tập Thuật Toán Python — Bộ 2 (Dễ → Khó vừa)

Chủ đề: **toán học, hai con trỏ, sắp xếp, tìm kiếm nhị phân, đệ quy + tổng tiền tố**.

---

## Bài 1 (Dễ) — Số Armstrong [Toán học]

**Đề bài:** Viết hàm kiểm tra một số nguyên không âm `n` có phải là **số Armstrong** hay không — tức là tổng các chữ số của nó, mỗi chữ số được nâng lên lũy thừa bằng số lượng chữ số, bằng chính số đó.
(Ví dụ: `153 = 1³ + 5³ + 3³`.)

**Ràng buộc:** `0 <= n <= 10^7`. Các số có 1 chữ số (0–9) luôn là số Armstrong.

```python
def is_armstrong(n: int) -> bool:
    pass


assert is_armstrong(153) == True
assert is_armstrong(9474) == True
assert is_armstrong(123) == False
assert is_armstrong(9) == True
assert is_armstrong(0) == True
assert is_armstrong(9475) == False
assert is_armstrong(370) == True
```

---

## Bài 2 (Dễ–Trung bình) — Loại bỏ phần tử trùng lặp trong mảng đã sắp xếp [Hai con trỏ]

**Đề bài:** Cho một mảng số nguyên đã sắp xếp tăng dần (có thể chứa phần tử trùng lặp). Viết hàm dùng kỹ thuật **hai con trỏ** (một con trỏ đọc `read`, một con trỏ ghi `write`) để loại bỏ các phần tử trùng lặp ngay trong mảng, chỉ giữ lại mỗi giá trị một lần, và trả về mảng kết quả. Không dùng `set()` hay `dict` để khử trùng.

**Ràng buộc:** mảng đầu vào đã sắp xếp tăng dần; `0 <= len(arr) <= 10^5`.

```python
def remove_duplicates(arr: list) -> list:
    pass


assert remove_duplicates([1, 1, 2]) == [1, 2]
assert remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == [0, 1, 2, 3, 4]
assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
assert remove_duplicates([]) == []
assert remove_duplicates([5, 5, 5, 5]) == [5]
```

---

## Bài 3 (Trung bình) — Sắp xếp theo tần suất xuất hiện [Sắp xếp]

**Đề bài:** Cho một mảng số nguyên, hãy sắp xếp lại mảng sao cho phần tử có **tần suất xuất hiện cao hơn đứng trước**; nếu hai phần tử có tần suất bằng nhau, phần tử có **giá trị nhỏ hơn đứng trước**.

**Ràng buộc:** `0 <= len(arr) <= 10^5`; các phần tử có thể âm, dương hoặc bằng 0.

```python
def frequency_sort(arr: list) -> list:
    pass


assert frequency_sort([1, 1, 2, 2, 2, 3]) == [2, 2, 2, 1, 1, 3]
assert frequency_sort([4, 4, 4, 5, 5, 6]) == [4, 4, 4, 5, 5, 6]
assert frequency_sort([1, 2, 3]) == [1, 2, 3]
assert frequency_sort([]) == []
assert frequency_sort([7, 7, 8, 8, 9]) == [7, 7, 8, 8, 9]
```

---

## Bài 4 (Trung bình–Khó) — Tìm một đỉnh cực đại [Tìm kiếm nhị phân]

**Đề bài:** Một "đỉnh" là phần tử lớn hơn (các) phần tử liền kề của nó (phần tử ở biên chỉ cần lớn hơn phần tử liền kề duy nhất). Cho một mảng, tìm chỉ số của một đỉnh bằng **tìm kiếm nhị phân trong O(log n)** (không được duyệt tuyến tính).

**Ràng buộc:** `1 <= len(arr) <= 10^5`; không có hai phần tử liền kề bằng nhau; các test case dưới đây đều là mảng đơn đỉnh (unimodal — chỉ tăng rồi giảm, hoặc tăng/giảm hoàn toàn) để đảm bảo kết quả duy nhất, dễ chấm tự động.

```python
def find_peak(arr: list) -> int:
    pass


assert find_peak([1, 3, 5, 4, 2]) == 2
assert find_peak([1, 2, 3, 4, 5]) == 4
assert find_peak([5, 4, 3, 2, 1]) == 0
assert find_peak([1, 2, 1]) == 1
assert find_peak([1]) == 0
```

---

## Bài 5 (Khó) — Chỉ số cân bằng [Đệ quy + Tổng tiền tố]

**Đề bài:** **Chỉ số cân bằng** của một mảng là chỉ số `i` mà tổng các phần tử bên trái bằng tổng các phần tử bên phải (biên coi như tổng bằng 0). Trả về chỉ số nhỏ nhất thỏa mãn, hoặc `-1` nếu không tồn tại.

**Yêu cầu:** tính tổng toàn mảng bằng một **hàm đệ quy** (không dùng `sum()`, không dùng vòng lặp cho phần này), sau đó duyệt mảng một lần với tổng bên trái chạy dần (`right_sum = total - left_sum - giá_trị_hiện_tại`) để tìm đáp án trong O(n).

**Ràng buộc:** `0 <= len(arr) <= 10^5`; phần tử có thể âm, dương hoặc bằng 0; cần xử lý đúng mảng rỗng và mảng chỉ có 1 phần tử.

```python
def equilibrium_index(arr: list) -> int:
    pass


assert equilibrium_index([-7, 1, 5, 2, -4, 3, 0]) == 3
assert equilibrium_index([1, 2, 3]) == -1
assert equilibrium_index([0]) == 0
assert equilibrium_index([1, 2, 3, 4, 3, 2, 1]) == 3
assert equilibrium_index([]) == -1
```

---

## Đáp Án Tham Khảo

```python
# Bài 1 — Số Armstrong (Toán học)
def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == n


# Bài 2 — Loại bỏ phần tử trùng lặp (Hai con trỏ)
def remove_duplicates(arr):
    if not arr:
        return []
    write = 0
    for read in range(1, len(arr)):
        if arr[read] != arr[write]:
            write += 1
            arr[write] = arr[read]
    return arr[:write + 1]


# Bài 3 — Sắp xếp theo tần suất (Sắp xếp)
from collections import Counter

def frequency_sort(arr):
    counts = Counter(arr)
    return sorted(arr, key=lambda x: (-counts[x], x))


# Bài 4 — Tìm đỉnh cực đại (Tìm kiếm nhị phân)
def find_peak(arr):
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < arr[mid + 1]:
            lo = mid + 1
        else:
            hi = mid
    return lo


# Bài 5 — Chỉ số cân bằng (Đệ quy + Tổng tiền tố)
def equilibrium_index(arr):
    def total_sum_recursive(index):
        if index == len(arr):
            return 0
        return arr[index] + total_sum_recursive(index + 1)

    total = total_sum_recursive(0)
    left_sum = 0
    for i, val in enumerate(arr):
        right_sum = total - left_sum - val
        if left_sum == right_sum:
            return i
        left_sum += val
    return -1
```

---

## Gợi Ý Chấm Điểm

| Bài | Chủ đề | Độ khó | Điểm đề xuất |
|---|---|---|---|
| 1 | Toán học | Dễ | 15 |
| 2 | Hai con trỏ | Dễ–Trung bình | 20 |
| 3 | Sắp xếp | Trung bình | 20 |
| 4 | Tìm kiếm nhị phân | Trung bình–Khó | 20 |
| 5 | Đệ quy + Tổng tiền tố | Khó | 25 |
| **Tổng** | | | **100** |