# 30 bài tập mảng Java tiếp theo — Bài 16 đến 45

Đây là phần tiếp theo của bộ 15 bài tập mảng Java. Các bài tăng dần từ dễ đến trung bình khá, bao gồm **counting, two pointers, recursion, binary search, sorting, prefix sum và sliding window**.

## Cách chạy test

Thêm import sau vào đầu file Java:

```java
import java.util.Arrays;
```

Trong Eclipse, bật `assert` bằng cách thêm `-ea` vào:

```text
Run → Run Configurations → Arguments → VM arguments
```

Không sử dụng `Arrays.sort()` trong các bài yêu cầu tự cài đặt thuật toán sắp xếp.

---

## Bài 16 — Đếm số dương, số âm và số 0

**Mức độ:** Dễ  
**Chủ đề:** Counting

Trả về mảng gồm ba phần tử:

- `result[0]`: số lượng số dương.
- `result[1]`: số lượng số âm.
- `result[2]`: số lượng số 0.

**Ràng buộc:**

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

```java
static int[] countPositiveNegativeZero(int[] nums) {
    return null;
}

assert Arrays.equals(
    countPositiveNegativeZero(new int[]{-2, 0, 5, -1, 7, 0}),
    new int[]{2, 2, 2}
);
assert Arrays.equals(
    countPositiveNegativeZero(new int[]{}),
    new int[]{0, 0, 0}
);
```

**Yêu cầu:** `O(n)` thời gian và `O(1)` bộ nhớ phụ.

---

## Bài 17 — Hiệu giữa phần tử lớn nhất và nhỏ nhất

**Mức độ:** Dễ  
**Chủ đề:** Duyệt mảng

Cho mảng không rỗng. Trả về:

```text
giá trị lớn nhất - giá trị nhỏ nhất
```

**Ràng buộc:**

- `1 <= nums.length <= 10^5`
- `-10^6 <= nums[i] <= 10^6`

```java
static int maxMinDifference(int[] nums) {
    return 0;
}

assert maxMinDifference(new int[]{4, 2, 9, -1}) == 10;
assert maxMinDifference(new int[]{5}) == 0;
assert maxMinDifference(new int[]{-8, -3, -10}) == 7;
```

Không dùng sorting. Chỉ duyệt mảng một lần.

---

## Bài 18 — Kiểm tra mảng tăng không giảm

**Mức độ:** Dễ  
**Chủ đề:** Duyệt mảng

Trả về `true` nếu với mọi index hợp lệ:

```text
nums[i] <= nums[i + 1]
```

Hai phần tử bằng nhau vẫn được xem là đúng thứ tự.

```java
static boolean isNonDecreasing(int[] nums) {
    return false;
}

assert isNonDecreasing(new int[]{1, 2, 2, 5});
assert isNonDecreasing(new int[]{});
assert isNonDecreasing(new int[]{7});
assert !isNonDecreasing(new int[]{1, 3, 2});
```

**Yêu cầu:** Dừng sớm ngay khi tìm thấy một cặp sai thứ tự.

---

## Bài 19 — Tìm số lớn thứ hai phân biệt

**Mức độ:** Trung bình dễ  
**Chủ đề:** Duyệt mảng

Tìm giá trị lớn thứ hai **khác** giá trị lớn nhất. Nếu không tồn tại hai giá trị phân biệt, phát sinh:

```java
throw new IllegalArgumentException("Need two distinct values");
```

```java
static int secondLargestDistinct(int[] nums) {
    return 0;
}

assert secondLargestDistinct(new int[]{4, 9, 2, 9, 7}) == 7;
assert secondLargestDistinct(new int[]{-5, -2, -8}) == -5;
assert secondLargestDistinct(new int[]{1, 2}) == 1;
```

**Yêu cầu:**

- Không dùng sorting.
- `O(n)` thời gian và `O(1)` bộ nhớ phụ.
- Cẩn thận khi mảng chứa `Integer.MIN_VALUE`.

---

## Bài 20 — Giá trị xuất hiện nhiều nhất

**Mức độ:** Trung bình dễ  
**Chủ đề:** Frequency array / Counting

Mảng không rỗng chỉ chứa giá trị từ `0` đến `100`. Trả về giá trị có tần suất lớn nhất. Nếu nhiều giá trị có cùng tần suất, trả về giá trị nhỏ nhất.

```java
static int mostFrequentValue(int[] nums) {
    return -1;
}

assert mostFrequentValue(new int[]{2, 1, 2, 3, 1, 2}) == 2;
assert mostFrequentValue(new int[]{4, 4, 5, 5}) == 4;
assert mostFrequentValue(new int[]{7}) == 7;
```

**Gợi ý:** Dùng mảng đếm có 101 phần tử.

---

## Bài 21 — Giao duy nhất của hai mảng đã sắp xếp

**Mức độ:** Trung bình  
**Chủ đề:** Two pointers

Cho hai mảng đã sắp xếp tăng dần, có thể chứa phần tử trùng. Trả về mảng gồm các giá trị xuất hiện trong cả hai mảng; mỗi giá trị chỉ xuất hiện một lần trong kết quả.

```java
static int[] uniqueIntersection(int[] a, int[] b) {
    return null;
}

assert Arrays.equals(
    uniqueIntersection(
        new int[]{1, 1, 2, 3, 5},
        new int[]{1, 2, 2, 4, 5}
    ),
    new int[]{1, 2, 5}
);
assert Arrays.equals(
    uniqueIntersection(new int[]{1, 2}, new int[]{3, 4}),
    new int[]{}
);
```

**Yêu cầu:** `O(a.length + b.length)` thời gian. Không dùng `HashSet`.

---

## Bài 22 — Kiểm tra cặp có tổng bằng target

**Mức độ:** Trung bình dễ  
**Chủ đề:** Two pointers

Cho mảng đã sắp xếp tăng dần. Trả về `true` nếu tồn tại hai phần tử ở hai index khác nhau có tổng bằng `target`.

```java
static boolean hasPairWithSum(int[] nums, int target) {
    return false;
}

assert hasPairWithSum(new int[]{1, 2, 4, 6, 10}, 8);  // 2 + 6
assert hasPairWithSum(new int[]{-5, -2, 0, 3, 8}, 3); // -5 + 8
assert !hasPairWithSum(new int[]{1, 2, 4}, 8);
assert !hasPairWithSum(new int[]{5}, 10);
```

**Yêu cầu:** `O(n)` thời gian, `O(1)` bộ nhớ phụ và không dùng nested loops.

---

## Bài 23 — Trộn hai mảng đã sắp xếp

**Mức độ:** Trung bình dễ  
**Chủ đề:** Two pointers

Cho hai mảng tăng dần. Trả về một mảng mới chứa toàn bộ phần tử của cả hai mảng theo thứ tự tăng dần. Giữ nguyên phần tử trùng.

```java
static int[] mergeSortedArrays(int[] a, int[] b) {
    return null;
}

assert Arrays.equals(
    mergeSortedArrays(new int[]{1, 3, 5}, new int[]{2, 4, 6}),
    new int[]{1, 2, 3, 4, 5, 6}
);
assert Arrays.equals(
    mergeSortedArrays(new int[]{1, 1}, new int[]{1, 2}),
    new int[]{1, 1, 1, 2}
);
assert Arrays.equals(
    mergeSortedArrays(new int[]{}, new int[]{2, 3}),
    new int[]{2, 3}
);
```

**Yêu cầu:** `O(a.length + b.length)` thời gian.

---

## Bài 24 — Bình phương của mảng đã sắp xếp

**Mức độ:** Trung bình  
**Chủ đề:** Two pointers

Cho mảng số nguyên đã sắp xếp tăng dần, có thể chứa số âm. Trả về mảng bình phương của các phần tử, cũng theo thứ tự tăng dần.

Ví dụ:

```text
[-4, -1, 0, 3, 10] → [0, 1, 9, 16, 100]
```

```java
static int[] sortedSquares(int[] nums) {
    return null;
}

assert Arrays.equals(
    sortedSquares(new int[]{-4, -1, 0, 3, 10}),
    new int[]{0, 1, 9, 16, 100}
);
assert Arrays.equals(
    sortedSquares(new int[]{-3, -2, -1}),
    new int[]{1, 4, 9}
);
```

**Ràng buộc:** `-10^4 <= nums[i] <= 10^4`.  
**Yêu cầu:** `O(n)` thời gian; không tạo mảng bình phương rồi sorting.

---

## Bài 25 — Xóa target tại chỗ

**Mức độ:** Trung bình dễ  
**Chủ đề:** Two pointers đọc/ghi

Xóa mọi phần tử bằng `target` bằng cách đưa các phần tử cần giữ về đầu mảng. Trả về số phần tử còn lại `k`. Chỉ `k` phần tử đầu tiên được tính là kết quả.

```java
static int removeTarget(int[] nums, int target) {
    return 0;
}

int[] a = {3, 2, 2, 3, 4};
int k1 = removeTarget(a, 3);
assert k1 == 3;
assert Arrays.equals(Arrays.copyOf(a, k1), new int[]{2, 2, 4});

int[] b = {1, 1, 1};
int k2 = removeTarget(b, 1);
assert k2 == 0;
```

**Yêu cầu:** Giữ nguyên thứ tự tương đối; `O(n)` thời gian và `O(1)` bộ nhớ phụ.

---

## Bài 26 — Xoay mảng sang trái `k` bước

**Mức độ:** Trung bình  
**Chủ đề:** Two pointers / Reversal

Thay đổi trực tiếp mảng để xoay sang trái `k` vị trí.

```text
[1, 2, 3, 4, 5], k = 2
→ [3, 4, 5, 1, 2]
```

```java
static void rotateLeft(int[] nums, int k) {
}

int[] a = {1, 2, 3, 4, 5};
rotateLeft(a, 2);
assert Arrays.equals(a, new int[]{3, 4, 5, 1, 2});

int[] b = {1, 2, 3};
rotateLeft(b, 5);
assert Arrays.equals(b, new int[]{3, 1, 2});

int[] c = {};
rotateLeft(c, 4);
assert Arrays.equals(c, new int[]{});
```

**Ràng buộc:** `k >= 0`.  
**Yêu cầu:** `O(n)` thời gian và `O(1)` bộ nhớ phụ. Xử lý `k > nums.length` và mảng rỗng.

---

## Bài 27 — Diện tích chứa nước lớn nhất

**Mức độ:** Trung bình khá  
**Chủ đề:** Two pointers

Mỗi phần tử `height[i]` là chiều cao của một đường thẳng đứng tại vị trí `i`. Chọn hai đường để tạo vùng chứa nước lớn nhất.

Diện tích giữa `left` và `right`:

```text
min(height[left], height[right]) * (right - left)
```

```java
static int maxWaterArea(int[] height) {
    return 0;
}

assert maxWaterArea(new int[]{1, 8, 6, 2, 5, 4, 8, 3, 7}) == 49;
assert maxWaterArea(new int[]{1, 1}) == 1;
assert maxWaterArea(new int[]{5}) == 0;
assert maxWaterArea(new int[]{}) == 0;
```

**Ràng buộc:** `0 <= height[i] <= 10^4`.  
**Yêu cầu:** `O(n)` thời gian; mỗi bước di chuyển con trỏ ở phía có chiều cao nhỏ hơn.

---

## Bài 28 — Đếm target bằng đệ quy

**Mức độ:** Trung bình dễ  
**Chủ đề:** Recursion

Đếm số lần `target` xuất hiện từ `index` đến cuối mảng. Không dùng vòng lặp.

```java
static int recursiveCount(int[] nums, int target, int index) {
    return 0;
}

assert recursiveCount(new int[]{2, 1, 2, 3, 2}, 2, 0) == 3;
assert recursiveCount(new int[]{2, 1, 2, 3, 2}, 2, 2) == 2;
assert recursiveCount(new int[]{}, 5, 0) == 0;
```

**Ràng buộc:** `nums.length <= 1000`.

---

## Bài 29 — Kiểm tra đối xứng bằng đệ quy

**Mức độ:** Trung bình  
**Chủ đề:** Recursion + Two pointers

Kiểm tra đoạn mảng từ `left` đến `right` có đối xứng không. Không dùng vòng lặp.

```java
static boolean recursivePalindrome(int[] nums, int left, int right) {
    return false;
}

int[] a = {1, 2, 3, 2, 1};
assert recursivePalindrome(a, 0, a.length - 1);

int[] b = {1, 2, 3};
assert !recursivePalindrome(b, 0, b.length - 1);

int[] c = {};
assert recursivePalindrome(c, 0, c.length - 1);
```

Xác định base case khi `left >= right`.

---

## Bài 30 — Đảo ngược mảng bằng đệ quy

**Mức độ:** Trung bình  
**Chủ đề:** Recursion + Two pointers

Đảo ngược trực tiếp đoạn mảng `[left, right]`. Không dùng vòng lặp và không tạo mảng mới.

```java
static void recursiveReverse(int[] nums, int left, int right) {
}

int[] a = {1, 2, 3, 4};
recursiveReverse(a, 0, a.length - 1);
assert Arrays.equals(a, new int[]{4, 3, 2, 1});

int[] b = {};
recursiveReverse(b, 0, b.length - 1);
assert Arrays.equals(b, new int[]{});
```

**Gợi ý:** Đổi hai đầu rồi gọi lại với `left + 1` và `right - 1`.

---

## Bài 31 — Binary search bằng đệ quy

**Mức độ:** Trung bình  
**Chủ đề:** Recursion + Binary search

Cho mảng đã sắp xếp tăng dần và không có phần tử trùng. Trả về index của `target`, hoặc `-1` nếu không tồn tại.

```java
static int recursiveBinarySearch(
        int[] nums, int target, int left, int right) {
    return -1;
}

int[] nums = {1, 3, 5, 7, 9};
assert recursiveBinarySearch(nums, 7, 0, nums.length - 1) == 3;
assert recursiveBinarySearch(nums, 2, 0, nums.length - 1) == -1;
assert recursiveBinarySearch(new int[]{}, 1, 0, -1) == -1;
```

**Base case:** `left > right`.  
**Yêu cầu:** `O(log n)` thời gian và `O(log n)` call stack.

---

## Bài 32 — Kiểm tra mảng đã sắp xếp bằng đệ quy

**Mức độ:** Trung bình dễ  
**Chủ đề:** Recursion

Trả về `true` nếu mảng tăng không giảm. `index` là vị trí của phần tử đầu tiên trong cặp cần so sánh.

```java
static boolean recursiveIsSorted(int[] nums, int index) {
    return false;
}

assert recursiveIsSorted(new int[]{1, 2, 2, 5}, 0);
assert !recursiveIsSorted(new int[]{1, 4, 3}, 0);
assert recursiveIsSorted(new int[]{7}, 0);
assert recursiveIsSorted(new int[]{}, 0);
```

**Gợi ý:** Nếu `index >= nums.length - 1`, không còn cặp nào cần kiểm tra.

---

## Bài 33 — Tìm vị trí chèn

**Mức độ:** Trung bình dễ  
**Chủ đề:** Binary search

Cho mảng tăng dần gồm các giá trị phân biệt. Nếu `target` tồn tại, trả về index của nó. Nếu không, trả về index mà tại đó có thể chèn `target` để mảng vẫn tăng dần.

```java
static int searchInsertPosition(int[] nums, int target) {
    return 0;
}

assert searchInsertPosition(new int[]{1, 3, 5, 6}, 5) == 2;
assert searchInsertPosition(new int[]{1, 3, 5, 6}, 2) == 1;
assert searchInsertPosition(new int[]{1, 3, 5, 6}, 7) == 4;
assert searchInsertPosition(new int[]{1, 3, 5, 6}, 0) == 0;
assert searchInsertPosition(new int[]{}, 4) == 0;
```

**Yêu cầu:** `O(log n)` thời gian.

---

## Bài 34 — Tìm vị trí xuất hiện cuối cùng

**Mức độ:** Trung bình  
**Chủ đề:** Binary search

Cho mảng đã sắp xếp và có thể chứa giá trị trùng. Trả về index cuối cùng của `target`, hoặc `-1`.

```java
static int lastOccurrence(int[] nums, int target) {
    return -1;
}

assert lastOccurrence(new int[]{1, 2, 2, 2, 3}, 2) == 3;
assert lastOccurrence(new int[]{5, 5, 5}, 5) == 2;
assert lastOccurrence(new int[]{1, 2, 3}, 4) == -1;
assert lastOccurrence(new int[]{}, 1) == -1;
```

Khi tìm thấy, lưu đáp án rồi tiếp tục tìm bên phải.

---

## Bài 35 — Tìm khoảng xuất hiện của target

**Mức độ:** Trung bình  
**Chủ đề:** Binary search

Trả về `{firstIndex, lastIndex}` của `target` trong mảng đã sắp xếp. Nếu không tồn tại, trả về `{-1, -1}`.

```java
static int[] searchRange(int[] nums, int target) {
    return null;
}

assert Arrays.equals(
    searchRange(new int[]{1, 2, 2, 2, 3, 4}, 2),
    new int[]{1, 3}
);
assert Arrays.equals(
    searchRange(new int[]{1, 2, 3}, 5),
    new int[]{-1, -1}
);
assert Arrays.equals(
    searchRange(new int[]{7}, 7),
    new int[]{0, 0}
);
```

**Yêu cầu:** Dùng hai lần binary search; tổng thời gian `O(log n)`.

---

## Bài 36 — Đếm target bằng binary search

**Mức độ:** Trung bình  
**Chủ đề:** Binary search + Counting

Mảng đã sắp xếp và có thể chứa phần tử trùng. Đếm số lần `target` xuất hiện trong `O(log n)`.

```java
static int countOccurrencesBinary(int[] nums, int target) {
    return 0;
}

assert countOccurrencesBinary(new int[]{1, 2, 2, 2, 3}, 2) == 3;
assert countOccurrencesBinary(new int[]{5, 5, 5}, 5) == 3;
assert countOccurrencesBinary(new int[]{1, 2, 3}, 4) == 0;
assert countOccurrencesBinary(new int[]{}, 1) == 0;
```

**Gợi ý:** Nếu tìm thấy vị trí đầu `first` và cuối `last`, số lượng là `last - first + 1`.

---

## Bài 37 — Căn bậc hai lấy phần nguyên

**Mức độ:** Trung bình  
**Chủ đề:** Binary search trên đáp án

Cho số nguyên không âm `n`. Trả về số nguyên lớn nhất `x` sao cho:

```text
x * x <= n
```

```java
static int sqrtFloor(int n) {
    return 0;
}

assert sqrtFloor(0) == 0;
assert sqrtFloor(1) == 1;
assert sqrtFloor(8) == 2;
assert sqrtFloor(16) == 4;
assert sqrtFloor(2_147_483_647) == 46340;
```

**Ràng buộc:** `0 <= n <= Integer.MAX_VALUE`.  
**Lưu ý:** Dùng `long` khi tính `mid * mid` để tránh overflow.

---

## Bài 38 — Tìm target trong mảng xoay

**Mức độ:** Trung bình khá  
**Chủ đề:** Binary search

Mảng ban đầu tăng dần, gồm các giá trị phân biệt, sau đó bị xoay tại một vị trí chưa biết. Trả về index của `target`, hoặc `-1`.

```java
static int searchRotated(int[] nums, int target) {
    return -1;
}

assert searchRotated(new int[]{4, 5, 6, 7, 0, 1, 2}, 0) == 4;
assert searchRotated(new int[]{4, 5, 6, 7, 0, 1, 2}, 3) == -1;
assert searchRotated(new int[]{1}, 1) == 0;
assert searchRotated(new int[]{}, 5) == -1;
```

**Yêu cầu:** `O(log n)` thời gian. Trong mỗi vòng lặp, xác định nửa trái hay nửa phải đang được sắp xếp.

---

## Bài 39 — Selection sort

**Mức độ:** Trung bình dễ  
**Chủ đề:** Sorting

Sắp xếp trực tiếp mảng tăng dần bằng selection sort. Mỗi vòng ngoài tìm phần tử nhỏ nhất của đoạn chưa sắp xếp rồi đổi nó về đầu đoạn.

```java
static void selectionSort(int[] nums) {
}

int[] a = {64, 25, 12, 22, 11};
selectionSort(a);
assert Arrays.equals(a, new int[]{11, 12, 22, 25, 64});

int[] b = {-1, 3, 0, -5};
selectionSort(b);
assert Arrays.equals(b, new int[]{-5, -1, 0, 3});
```

Không dùng `Arrays.sort()`. Phân tích vì sao selection sort luôn là `O(n²)` kể cả khi mảng đã sắp xếp.

---

## Bài 40 — Bubble sort có dừng sớm

**Mức độ:** Trung bình  
**Chủ đề:** Sorting

Sắp xếp mảng tăng dần bằng bubble sort. Nếu một vòng duyệt không thực hiện lần đổi chỗ nào, dừng thuật toán ngay.

```java
static void bubbleSort(int[] nums) {
}

int[] a = {5, 1, 4, 2, 8};
bubbleSort(a);
assert Arrays.equals(a, new int[]{1, 2, 4, 5, 8});

int[] b = {1, 2, 3, 4};
bubbleSort(b);
assert Arrays.equals(b, new int[]{1, 2, 3, 4});
```

Sử dụng biến `swapped` để đạt thời gian tốt nhất `O(n)` với mảng đã sắp xếp.

---

## Bài 41 — Sắp xếp mảng chỉ chứa 0, 1 và 2

**Mức độ:** Trung bình khá  
**Chủ đề:** Dutch National Flag / Three pointers

Sắp xếp trực tiếp mảng chỉ chứa `0`, `1`, `2` trong một lần duyệt.

```java
static void sortColors(int[] nums) {
}

int[] a = {2, 0, 2, 1, 1, 0};
sortColors(a);
assert Arrays.equals(a, new int[]{0, 0, 1, 1, 2, 2});

int[] b = {2, 2, 1, 0};
sortColors(b);
assert Arrays.equals(b, new int[]{0, 1, 2, 2});
```

**Yêu cầu:**

- `O(n)` thời gian, `O(1)` bộ nhớ phụ.
- Không dùng sorting có sẵn.
- Dùng ba vùng được quản lý bởi `low`, `mid`, `high`.

---

## Bài 42 — Xây dựng mảng prefix sum

**Mức độ:** Trung bình dễ  
**Chủ đề:** Prefix sum

Tạo mảng `prefix` có độ dài `nums.length + 1`, trong đó:

```text
prefix[0] = 0
prefix[i + 1] = nums[0] + nums[1] + ... + nums[i]
```

Dùng `long[]` để hạn chế overflow khi tổng lớn.

```java
static long[] buildPrefixSum(int[] nums) {
    return null;
}

assert Arrays.equals(
    buildPrefixSum(new int[]{2, 4, -1, 3}),
    new long[]{0, 2, 6, 5, 8}
);
assert Arrays.equals(
    buildPrefixSum(new int[]{}),
    new long[]{0}
);
```

**Yêu cầu:** `O(n)` thời gian.

---

## Bài 43 — Tổng đoạn bằng prefix sum

**Mức độ:** Trung bình  
**Chủ đề:** Prefix sum

Cho mảng prefix được tạo theo Bài 42. Trả về tổng các phần tử trong đoạn đóng `[left, right]` của mảng gốc.

Công thức cần tự suy ra từ:

```text
prefix[right + 1] và prefix[left]
```

```java
static long rangeSum(long[] prefix, int left, int right) {
    return 0;
}

long[] prefix = buildPrefixSum(new int[]{2, 4, -1, 3, 5});
assert rangeSum(prefix, 0, 2) == 5;
assert rangeSum(prefix, 1, 3) == 6;
assert rangeSum(prefix, 4, 4) == 5;
```

**Ràng buộc:** `0 <= left <= right < prefix.length - 1`.  
**Yêu cầu:** Mỗi truy vấn chạy trong `O(1)`.

---

## Bài 44 — Tìm equilibrium index

**Mức độ:** Trung bình  
**Chủ đề:** Prefix sum / Running sum

Một index `i` là equilibrium index nếu tổng các phần tử bên trái bằng tổng các phần tử bên phải. Không tính `nums[i]` vào bên nào.

Trả về equilibrium index đầu tiên, hoặc `-1`.

```java
static int equilibriumIndex(int[] nums) {
    return -1;
}

assert equilibriumIndex(new int[]{1, 7, 3, 6, 5, 6}) == 3;
assert equilibriumIndex(new int[]{2, 1, -1}) == 0;
assert equilibriumIndex(new int[]{1, 2, 3}) == -1;
assert equilibriumIndex(new int[]{}) == -1;
```

**Yêu cầu:** `O(n)` thời gian và `O(1)` bộ nhớ phụ; dùng `long` cho tổng.

---

## Bài 45 — Tổng lớn nhất của cửa sổ kích thước `k`

**Mức độ:** Trung bình  
**Chủ đề:** Sliding window

Cho mảng và số nguyên `k`. Tìm tổng lớn nhất trong tất cả các đoạn con liên tiếp có đúng `k` phần tử.

```java
static long maxWindowSum(int[] nums, int k) {
    return 0;
}

assert maxWindowSum(new int[]{2, 1, 5, 1, 3, 2}, 3) == 9;
assert maxWindowSum(new int[]{-4, -2, -7, -1}, 2) == -6;
assert maxWindowSum(new int[]{5}, 1) == 5;
```

**Ràng buộc:**

- `1 <= k <= nums.length`
- `nums.length <= 10^5`

**Yêu cầu:**

- `O(n)` thời gian.
- Không tính lại tổng của toàn bộ cửa sổ ở mỗi vị trí.
- Khi trượt cửa sổ: trừ phần tử rời khỏi cửa sổ và cộng phần tử mới đi vào.

---

## Lộ trình đề xuất

| Giai đoạn | Bài | Nội dung |
|---|---:|---|
| Duyệt và counting | 16–20 | Điều kiện, min/max, tần suất |
| Two pointers | 21–27 | Hai mảng, đọc/ghi, reversal, tối ưu cặp |
| Recursion | 28–32 | Base case, thu nhỏ đoạn xử lý |
| Binary search | 33–38 | Biên trái/phải, tìm trên đáp án, mảng xoay |
| Sorting | 39–41 | Selection, bubble, Dutch National Flag |
| Prefix/sliding window | 42–45 | Tổng tích lũy, truy vấn đoạn, cửa sổ cố định |

Nên làm từng bài theo quy trình:

1. Xác định input và output.
2. Tự chạy tay một test nhỏ.
3. Viết brute force nếu chưa thấy cách tối ưu.
4. Cải thiện theo chủ đề của bài.
5. Chạy toàn bộ `assert`.
6. Tự ghi lại độ phức tạp thời gian và bộ nhớ.
