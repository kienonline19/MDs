# 15 bài tập mảng Java — Dễ đến trung bình

Các chủ đề: **duyệt mảng, counting, two pointers, recursion, binary search và sorting**.

## Cách sử dụng test

Các bài sử dụng `assert`. Trong Eclipse, để bật kiểm tra `assert`:

1. Chọn **Run → Run Configurations...**.
2. Chọn chương trình Java đang chạy.
3. Mở tab **Arguments**.
4. Nhập `-ea` vào **VM arguments**.
5. Nhấn **Apply → Run**.

Khi test mảng, thêm import:

```java
import java.util.Arrays;
```

Không sử dụng `Arrays.sort()` trong những bài yêu cầu tự cài đặt thuật toán sắp xếp.

---

## Bài 1 — Tính tổng các phần tử

**Mức độ:** Dễ  
**Chủ đề:** Duyệt mảng

Viết hàm trả về tổng tất cả phần tử trong mảng số nguyên.

**Ràng buộc:**

- `0 <= nums.length <= 1000`
- `-10^4 <= nums[i] <= 10^4`
- Tổng luôn nằm trong phạm vi `int`.

```java
static int sumArray(int[] nums) {
    return 0;
}

assert sumArray(new int[]{1, 2, 3, 4}) == 10;
assert sumArray(new int[]{-3, 5, -2}) == 0;
assert sumArray(new int[]{}) == 0;
assert sumArray(new int[]{7}) == 7;
```

---

## Bài 2 — Đếm số chẵn và số lẻ

**Mức độ:** Dễ  
**Chủ đề:** Counting

Trả về mảng gồm hai phần tử:

- `result[0]`: số lượng số chẵn.
- `result[1]`: số lượng số lẻ.

Số âm vẫn được xác định chẵn/lẻ bằng toán tử `%`.

**Ràng buộc:**

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

```java
static int[] countEvenOdd(int[] nums) {
    return null;
}

assert Arrays.equals(countEvenOdd(new int[]{1, 2, 3, 4, 6}), new int[]{3, 2});
assert Arrays.equals(countEvenOdd(new int[]{-2, -1, 0}), new int[]{2, 1});
assert Arrays.equals(countEvenOdd(new int[]{}), new int[]{0, 0});
```

---

## Bài 3 — Đếm số lần xuất hiện của một giá trị

**Mức độ:** Dễ  
**Chủ đề:** Counting

Cho mảng `nums` và số nguyên `target`. Hãy đếm số lần `target` xuất hiện trong mảng.

**Ràng buộc:**

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i], target <= 10^9`

```java
static int countOccurrences(int[] nums, int target) {
    return 0;
}

assert countOccurrences(new int[]{1, 2, 2, 3, 2}, 2) == 3;
assert countOccurrences(new int[]{1, 2, 3}, 5) == 0;
assert countOccurrences(new int[]{7, 7, 7}, 7) == 3;
assert countOccurrences(new int[]{}, 1) == 0;
```

---

## Bài 4 — Thống kê tần suất các chữ số

**Mức độ:** Dễ  
**Chủ đề:** Frequency array / Counting

Mảng đầu vào chỉ chứa các chữ số từ `0` đến `9`. Trả về mảng `frequency` có độ dài 10, trong đó `frequency[x]` là số lần chữ số `x` xuất hiện.

**Ràng buộc:**

- `0 <= digits.length <= 10^5`
- `0 <= digits[i] <= 9`

```java
static int[] countDigits(int[] digits) {
    return null;
}

assert Arrays.equals(
    countDigits(new int[]{1, 2, 1, 0, 9, 1}),
    new int[]{1, 3, 1, 0, 0, 0, 0, 0, 0, 1}
);
assert Arrays.equals(countDigits(new int[]{}), new int[10]);
```

**Yêu cầu độ phức tạp:** `O(n)` thời gian và `O(1)` bộ nhớ phụ vì mảng đếm luôn có đúng 10 phần tử.

---

## Bài 5 — Đảo ngược mảng tại chỗ

**Mức độ:** Dễ  
**Chủ đề:** Two pointers

Đảo ngược thứ tự các phần tử ngay trên mảng đầu vào. Không tạo mảng kết quả mới.

**Ràng buộc:**

- `0 <= nums.length <= 10^5`
- Mảng có thể chứa bất kỳ số nguyên nào.

```java
static void reverseArray(int[] nums) {
}

int[] a = {1, 2, 3, 4};
reverseArray(a);
assert Arrays.equals(a, new int[]{4, 3, 2, 1});

int[] b = {1, 2, 3};
reverseArray(b);
assert Arrays.equals(b, new int[]{3, 2, 1});

int[] c = {};
reverseArray(c);
assert Arrays.equals(c, new int[]{});
```

**Yêu cầu:** `O(n)` thời gian và `O(1)` bộ nhớ phụ.

---

## Bài 6 — Kiểm tra mảng đối xứng

**Mức độ:** Dễ  
**Chủ đề:** Two pointers

Mảng đối xứng nếu đọc từ trái sang phải giống đọc từ phải sang trái. Trả về `true` nếu mảng đối xứng, ngược lại trả về `false`.

```java
static boolean isPalindrome(int[] nums) {
    return false;
}

assert isPalindrome(new int[]{1, 2, 3, 2, 1});
assert isPalindrome(new int[]{7, 7});
assert isPalindrome(new int[]{});
assert !isPalindrome(new int[]{1, 2, 3});
assert !isPalindrome(new int[]{1, 2});
```

**Yêu cầu:** Không đảo ngược mảng và không tạo bản sao của mảng.

---

## Bài 7 — Di chuyển tất cả số 0 về cuối

**Mức độ:** Trung bình dễ  
**Chủ đề:** Two pointers

Di chuyển tất cả số `0` về cuối mảng, đồng thời giữ nguyên thứ tự tương đối của các phần tử khác `0`. Thay đổi trực tiếp mảng đầu vào.

Ví dụ:

```text
[0, 1, 0, 3, 12] → [1, 3, 12, 0, 0]
```

```java
static void moveZeros(int[] nums) {
}

int[] a = {0, 1, 0, 3, 12};
moveZeros(a);
assert Arrays.equals(a, new int[]{1, 3, 12, 0, 0});

int[] b = {1, 2, 3};
moveZeros(b);
assert Arrays.equals(b, new int[]{1, 2, 3});

int[] c = {0, 0, 0};
moveZeros(c);
assert Arrays.equals(c, new int[]{0, 0, 0});
```

**Yêu cầu:** `O(n)` thời gian, `O(1)` bộ nhớ phụ và không dùng sorting.

---

## Bài 8 — Xóa phần tử trùng trong mảng đã sắp xếp

**Mức độ:** Trung bình  
**Chủ đề:** Two pointers

Cho mảng `nums` đã được sắp xếp tăng dần. Hãy đưa các giá trị khác nhau về đầu mảng và trả về số lượng giá trị khác nhau `k`.

Sau khi hàm chạy, `k` phần tử đầu tiên của `nums` phải chứa các giá trị khác nhau theo thứ tự tăng dần. Các phần tử sau vị trí `k - 1` không cần quan tâm.

```java
static int removeDuplicates(int[] nums) {
    return 0;
}

int[] a = {1, 1, 2};
int k1 = removeDuplicates(a);
assert k1 == 2;
assert Arrays.equals(Arrays.copyOf(a, k1), new int[]{1, 2});

int[] b = {0, 0, 1, 1, 1, 2, 2, 3};
int k2 = removeDuplicates(b);
assert k2 == 4;
assert Arrays.equals(Arrays.copyOf(b, k2), new int[]{0, 1, 2, 3});

int[] c = {};
assert removeDuplicates(c) == 0;
```

**Yêu cầu:** `O(n)` thời gian và `O(1)` bộ nhớ phụ.

---

## Bài 9 — Tính tổng mảng bằng đệ quy

**Mức độ:** Trung bình dễ  
**Chủ đề:** Recursion

Viết hàm đệ quy tính tổng các phần tử từ vị trí `index` đến cuối mảng. Không sử dụng vòng lặp.

**Ràng buộc:**

- `0 <= nums.length <= 1000` để tránh vượt giới hạn ngăn xếp.
- Khi gọi lần đầu: `index = 0`.

```java
static int recursiveSum(int[] nums, int index) {
    return 0;
}

assert recursiveSum(new int[]{1, 2, 3, 4}, 0) == 10;
assert recursiveSum(new int[]{5, -2, 7}, 0) == 10;
assert recursiveSum(new int[]{}, 0) == 0;
assert recursiveSum(new int[]{10, 20, 30}, 1) == 50;
```

Hãy xác định rõ:

- Base case là gì?
- Mỗi lần gọi đệ quy, `index` thay đổi như thế nào?

---

## Bài 10 — Tìm giá trị lớn nhất bằng đệ quy

**Mức độ:** Trung bình  
**Chủ đề:** Recursion

Tìm phần tử lớn nhất trong một mảng không rỗng bằng đệ quy. Không sử dụng vòng lặp và không dùng Stream API.

`index` là vị trí bắt đầu tìm kiếm; lời gọi đầu tiên truyền `index = 0`.

**Ràng buộc:**

- `1 <= nums.length <= 1000`

```java
static int recursiveMax(int[] nums, int index) {
    return 0;
}

assert recursiveMax(new int[]{3, 9, 2, 7}, 0) == 9;
assert recursiveMax(new int[]{-8, -3, -10}, 0) == -3;
assert recursiveMax(new int[]{42}, 0) == 42;
assert recursiveMax(new int[]{1, 5, 10, 4}, 2) == 10;
```

---

## Bài 11 — Binary search cơ bản

**Mức độ:** Trung bình dễ  
**Chủ đề:** Binary search

Cho mảng số nguyên đã được sắp xếp tăng dần và một `target`. Trả về vị trí của `target`; nếu không tồn tại, trả về `-1`.

Các phần tử trong mảng không trùng nhau.

```java
static int binarySearch(int[] nums, int target) {
    return -1;
}

assert binarySearch(new int[]{1, 3, 5, 7, 9}, 1) == 0;
assert binarySearch(new int[]{1, 3, 5, 7, 9}, 7) == 3;
assert binarySearch(new int[]{1, 3, 5, 7, 9}, 6) == -1;
assert binarySearch(new int[]{}, 5) == -1;
```

**Yêu cầu:** `O(log n)` thời gian. Nên tính `mid` bằng:

```java
int mid = left + (right - left) / 2;
```

---

## Bài 12 — Tìm vị trí xuất hiện đầu tiên

**Mức độ:** Trung bình  
**Chủ đề:** Binary search

Cho mảng đã sắp xếp tăng dần và có thể chứa phần tử trùng nhau. Trả về vị trí đầu tiên của `target`; nếu không tồn tại, trả về `-1`.

Không được dừng ngay khi tìm thấy `target`; cần tiếp tục tìm về phía bên trái.

```java
static int firstOccurrence(int[] nums, int target) {
    return -1;
}

assert firstOccurrence(new int[]{1, 2, 2, 2, 3}, 2) == 1;
assert firstOccurrence(new int[]{5, 5, 5}, 5) == 0;
assert firstOccurrence(new int[]{1, 2, 3}, 4) == -1;
assert firstOccurrence(new int[]{}, 1) == -1;
```

**Yêu cầu:** `O(log n)` thời gian.

---

## Bài 13 — Cài đặt insertion sort

**Mức độ:** Trung bình  
**Chủ đề:** Sorting

Sắp xếp mảng tăng dần bằng thuật toán insertion sort. Thay đổi trực tiếp mảng đầu vào.

Không sử dụng `Arrays.sort()` hoặc bất kỳ hàm sắp xếp có sẵn nào.

```java
static void insertionSort(int[] nums) {
}

int[] a = {5, 2, 4, 6, 1, 3};
insertionSort(a);
assert Arrays.equals(a, new int[]{1, 2, 3, 4, 5, 6});

int[] b = {-1, 3, 0, -5};
insertionSort(b);
assert Arrays.equals(b, new int[]{-5, -1, 0, 3});

int[] c = {2, 2, 1};
insertionSort(c);
assert Arrays.equals(c, new int[]{1, 2, 2});
```

Sau khi làm xong, hãy tự trả lời:

- Trường hợp tốt nhất của insertion sort là gì?
- Độ phức tạp thời gian tốt nhất và xấu nhất là bao nhiêu?

---

## Bài 14 — Counting sort cho số nguyên không âm

**Mức độ:** Trung bình  
**Chủ đề:** Counting + Sorting

Cho mảng số nguyên không âm và giá trị lớn nhất cho phép `maxValue`. Sắp xếp mảng tăng dần bằng counting sort.

Các bước chính:

1. Tạo mảng đếm có kích thước `maxValue + 1`.
2. Đếm tần suất mỗi giá trị.
3. Ghi các giá trị trở lại mảng đầu vào theo thứ tự tăng dần.

**Ràng buộc:**

- `0 <= nums.length <= 10^5`
- `0 <= nums[i] <= maxValue <= 10^5`

```java
static void countingSort(int[] nums, int maxValue) {
}

int[] a = {4, 2, 2, 8, 3, 3, 1};
countingSort(a, 8);
assert Arrays.equals(a, new int[]{1, 2, 2, 3, 3, 4, 8});

int[] b = {0, 5, 0, 2};
countingSort(b, 5);
assert Arrays.equals(b, new int[]{0, 0, 2, 5});

int[] c = {};
countingSort(c, 0);
assert Arrays.equals(c, new int[]{});
```

**Độ phức tạp mục tiêu:** `O(n + k)` thời gian và `O(k)` bộ nhớ, với `k = maxValue + 1`.

---

## Bài 15 — Merge sort bằng đệ quy

**Mức độ:** Trung bình khá  
**Chủ đề:** Recursion + Sorting + Two pointers khi merge

Cài đặt merge sort để sắp xếp mảng tăng dần. Không sử dụng `Arrays.sort()`.

Chia bài toán thành hai hàm:

```java
static void mergeSort(int[] nums, int left, int right) {
}

static void merge(int[] nums, int left, int mid, int right) {
}
```

Trong đó:

- `mergeSort()` chia đoạn `[left, right]` thành hai nửa và gọi đệ quy.
- `merge()` trộn hai đoạn đã sắp xếp `[left, mid]` và `[mid + 1, right]`.
- Khi gọi lần đầu với mảng không rỗng: `mergeSort(nums, 0, nums.length - 1)`.

```java
int[] a = {5, 2, 4, 1, 3};
mergeSort(a, 0, a.length - 1);
assert Arrays.equals(a, new int[]{1, 2, 3, 4, 5});

int[] b = {-2, 8, 0, -2, 7};
mergeSort(b, 0, b.length - 1);
assert Arrays.equals(b, new int[]{-2, -2, 0, 7, 8});

int[] c = {1};
mergeSort(c, 0, c.length - 1);
assert Arrays.equals(c, new int[]{1});

int[] d = {};
mergeSort(d, 0, d.length - 1);
assert Arrays.equals(d, new int[]{});
```

**Yêu cầu độ phức tạp:**

- Thời gian: `O(n log n)`.
- Bộ nhớ phụ: `O(n)`.
- Base case phải xử lý được cả mảng một phần tử và mảng rỗng.

---

## Lộ trình đề xuất

| Giai đoạn | Bài | Kỹ năng chính |
|---|---:|---|
| Nền tảng | 1–4 | Duyệt mảng, điều kiện, đếm tần suất |
| Two pointers | 5–8 | Con trỏ trái/phải, con trỏ đọc/ghi |
| Recursion | 9–10 | Base case và thu nhỏ bài toán |
| Binary search | 11–12 | Không gian tìm kiếm và biên trái |
| Sorting | 13–15 | Insertion sort, counting sort, merge sort |

Nên hoàn thành từng bài theo thứ tự, tự phân tích **input → output**, xác định độ phức tạp rồi mới viết code.
