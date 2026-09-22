# Lời giải 30 bài tập mảng Java — Bài 16 đến 45

Tài liệu này giải bộ bài `java_array_30_more_exercises_vi.md`. Mỗi bài gồm ý tưởng, giải thích logic/cú pháp, code Java và độ phức tạp.

```java
import java.util.Arrays;
```

Trong Eclipse, thêm `-ea` vào **VM arguments** để bật các test `assert`.

---

## Bài 16 — Đếm số dương, số âm và số 0

### Ý tưởng và logic

Duyệt từng phần tử và chia thành đúng một trong ba trường hợp: `> 0`, `< 0`, hoặc bằng 0. Ba biến đếm được trả về trong một mảng theo đúng thứ tự đề bài.

### Lời giải

```java
static int[] countPositiveNegativeZero(int[] nums) {
    int positive = 0;
    int negative = 0;
    int zero = 0;

    for (int number : nums) {
        if (number > 0) {
            positive++;
        } else if (number < 0) {
            negative++;
        } else {
            zero++;
        }
    }

    return new int[]{positive, negative, zero};
}
```

`else if` chỉ được kiểm tra khi `number > 0` sai. `else` cuối cùng chắc chắn là trường hợp `number == 0`.

**Độ phức tạp:** `O(n)` thời gian, `O(1)` bộ nhớ phụ.

---

## Bài 17 — Hiệu giữa max và min

### Ý tưởng và logic

Khởi tạo cả `minimum` và `maximum` bằng phần tử đầu tiên thay vì 0. Cách này đúng cả khi toàn bộ mảng là số âm.

### Lời giải

```java
static int maxMinDifference(int[] nums) {
    int minimum = nums[0];
    int maximum = nums[0];

    for (int number : nums) {
        if (number < minimum) {
            minimum = number;
        }
        if (number > maximum) {
            maximum = number;
        }
    }

    return maximum - minimum;
}
```

Hai `if` độc lập giúp mỗi phần tử có thể được so sánh với cả min và max.

**Độ phức tạp:** `O(n)` thời gian, `O(1)` bộ nhớ phụ.

---

## Bài 18 — Kiểm tra mảng tăng không giảm

### Ý tưởng và logic

Chỉ cần tìm một cặp liền kề bị giảm: `nums[i] < nums[i - 1]`. Nếu gặp cặp như vậy, trả về `false` ngay.

### Lời giải

```java
static boolean isNonDecreasing(int[] nums) {
    for (int i = 1; i < nums.length; i++) {
        if (nums[i] < nums[i - 1]) {
            return false;
        }
    }

    return true;
}
```

Vòng lặp bắt đầu từ index 1 vì mỗi phần tử cần được so sánh với phần tử trước đó. Mảng rỗng và mảng một phần tử không có cặp sai nên trả về `true`.

**Độ phức tạp:** `O(n)` thời gian, `O(1)` bộ nhớ.

---

## Bài 19 — Số lớn thứ hai phân biệt

### Ý tưởng và logic

Dùng hai biến `Integer` có thể nhận `null`:

- `largest`: giá trị lớn nhất đã gặp.
- `second`: giá trị lớn thứ hai phân biệt.

`null` biểu diễn trạng thái chưa có giá trị, vì mọi số `int`, kể cả `Integer.MIN_VALUE`, đều có thể xuất hiện trong mảng.

### Lời giải

```java
static int secondLargestDistinct(int[] nums) {
    Integer largest = null;
    Integer second = null;

    for (int number : nums) {
        if (largest == null || number > largest) {
            second = largest;
            largest = number;
        } else if (number != largest
                && (second == null || number > second)) {
            second = number;
        }
    }

    if (second == null) {
        throw new IllegalArgumentException("Need two distinct values");
    }

    return second;
}
```

Điều kiện `number != largest` loại bỏ phần tử trùng với số lớn nhất. `Integer` sẽ tự unbox khi so sánh với `int`.

**Độ phức tạp:** `O(n)` thời gian, `O(1)` bộ nhớ.

---

## Bài 20 — Giá trị xuất hiện nhiều nhất

### Ý tưởng và logic

Đếm tần suất bằng mảng 101 phần tử. Sau đó duyệt giá trị từ nhỏ đến lớn. Chỉ cập nhật khi tần suất **lớn hơn** tần suất tốt nhất; nếu bằng nhau, giá trị nhỏ hơn đã được giữ lại.

### Lời giải

```java
static int mostFrequentValue(int[] nums) {
    int[] frequency = new int[101];

    for (int number : nums) {
        frequency[number]++;
    }

    int bestValue = 0;
    int bestFrequency = -1;

    for (int value = 0; value <= 100; value++) {
        if (frequency[value] > bestFrequency) {
            bestFrequency = frequency[value];
            bestValue = value;
        }
    }

    return bestValue;
}
```

**Độ phức tạp:** `O(n + 101) = O(n)` thời gian, `O(101) = O(1)` bộ nhớ.

---

## Bài 21 — Giao duy nhất của hai mảng đã sắp xếp

### Ý tưởng và logic

Dùng `i` duyệt `a`, `j` duyệt `b`:

- Nếu `a[i] < b[j]`, tăng `i`.
- Nếu `a[i] > b[j]`, tăng `j`.
- Nếu bằng nhau, đó là phần tử chung; chỉ ghi nếu chưa có trong kết quả.

### Lời giải

```java
static int[] uniqueIntersection(int[] a, int[] b) {
    int[] temporary = new int[Math.min(a.length, b.length)];
    int i = 0;
    int j = 0;
    int size = 0;

    while (i < a.length && j < b.length) {
        if (a[i] < b[j]) {
            i++;
        } else if (a[i] > b[j]) {
            j++;
        } else {
            if (size == 0 || temporary[size - 1] != a[i]) {
                temporary[size] = a[i];
                size++;
            }
            i++;
            j++;
        }
    }

    return Arrays.copyOf(temporary, size);
}
```

`Arrays.copyOf(temporary, size)` loại bỏ các ô thừa chưa dùng ở cuối mảng tạm.

**Độ phức tạp:** `O(a.length + b.length)` thời gian, `O(min(a.length, b.length))` cho kết quả tạm.

---

## Bài 22 — Cặp có tổng bằng target

### Ý tưởng và logic

Vì mảng tăng dần:

- Tổng quá nhỏ → tăng `left` để lấy số lớn hơn.
- Tổng quá lớn → giảm `right` để lấy số nhỏ hơn.

Dùng `long` cho tổng để tránh overflow khi cộng hai số `int`.

### Lời giải

```java
static boolean hasPairWithSum(int[] nums, int target) {
    int left = 0;
    int right = nums.length - 1;

    while (left < right) {
        long sum = (long) nums[left] + nums[right];

        if (sum == target) {
            return true;
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }

    return false;
}
```

`left < right` đảm bảo hai phần tử nằm ở hai index khác nhau.

**Độ phức tạp:** `O(n)` thời gian, `O(1)` bộ nhớ.

---

## Bài 23 — Trộn hai mảng đã sắp xếp

### Ý tưởng và logic

So sánh phần tử hiện tại của hai mảng, ghi phần tử nhỏ hơn vào kết quả. Khi một mảng đã hết, chép phần còn lại của mảng kia.

### Lời giải

```java
static int[] mergeSortedArrays(int[] a, int[] b) {
    int[] result = new int[a.length + b.length];
    int i = 0;
    int j = 0;
    int write = 0;

    while (i < a.length && j < b.length) {
        if (a[i] <= b[j]) {
            result[write++] = a[i++];
        } else {
            result[write++] = b[j++];
        }
    }

    while (i < a.length) {
        result[write++] = a[i++];
    }
    while (j < b.length) {
        result[write++] = b[j++];
    }

    return result;
}
```

`result[write++] = a[i++]` dùng index hiện tại trước, sau đó mới tăng cả hai index.

**Độ phức tạp:** `O(a.length + b.length)` thời gian và bộ nhớ kết quả.

---

## Bài 24 — Bình phương đã sắp xếp

### Ý tưởng và logic

Giá trị tuyệt đối lớn nhất luôn ở một trong hai đầu mảng. So sánh bình phương ở hai đầu và ghi giá trị lớn hơn từ cuối mảng kết quả về đầu.

### Lời giải

```java
static int[] sortedSquares(int[] nums) {
    int[] result = new int[nums.length];
    int left = 0;
    int right = nums.length - 1;
    int write = nums.length - 1;

    while (left <= right) {
        int leftSquare = nums[left] * nums[left];
        int rightSquare = nums[right] * nums[right];

        if (leftSquare > rightSquare) {
            result[write] = leftSquare;
            left++;
        } else {
            result[write] = rightSquare;
            right--;
        }
        write--;
    }

    return result;
}
```

Theo ràng buộc `|nums[i]| <= 10^4`, bình phương tối đa là `10^8`, vẫn nằm trong `int`.

**Độ phức tạp:** `O(n)` thời gian, `O(n)` cho mảng kết quả.

---

## Bài 25 — Xóa target tại chỗ

### Ý tưởng và logic

`read` đọc mọi phần tử; `write` chỉ di chuyển khi gặp phần tử cần giữ. Vì đọc từ trái sang phải, thứ tự được giữ nguyên.

### Lời giải

```java
static int removeTarget(int[] nums, int target) {
    int write = 0;

    for (int read = 0; read < nums.length; read++) {
        if (nums[read] != target) {
            nums[write] = nums[read];
            write++;
        }
    }

    return write;
}
```

Giá trị trả về `write` vừa là số phần tử còn lại, vừa là index trống tiếp theo.

**Độ phức tạp:** `O(n)` thời gian, `O(1)` bộ nhớ phụ.

---

## Bài 26 — Xoay trái `k` bước

### Ý tưởng và logic

Với `k` đã chuẩn hóa bằng `k %= n`:

1. Đảo đoạn `[0, k - 1]`.
2. Đảo đoạn `[k, n - 1]`.
3. Đảo toàn bộ mảng.

Ví dụ `{1,2,3,4,5}`, `k=2`:

```text
{2,1,3,4,5} → {2,1,5,4,3} → {3,4,5,1,2}
```

### Lời giải

```java
static void rotateLeft(int[] nums, int k) {
    if (nums.length == 0) {
        return;
    }

    k %= nums.length;
    reverseRange(nums, 0, k - 1);
    reverseRange(nums, k, nums.length - 1);
    reverseRange(nums, 0, nums.length - 1);
}

static void reverseRange(int[] nums, int left, int right) {
    while (left < right) {
        int temporary = nums[left];
        nums[left] = nums[right];
        nums[right] = temporary;
        left++;
        right--;
    }
}
```

Phải kiểm tra mảng rỗng trước phép `% nums.length` để tránh chia cho 0.

**Độ phức tạp:** `O(n)` thời gian, `O(1)` bộ nhớ.

---

## Bài 27 — Diện tích chứa nước lớn nhất

### Ý tưởng và logic

Diện tích bị giới hạn bởi cột thấp hơn. Nếu giữ cột thấp và di chuyển cột cao vào trong, chiều rộng giảm nhưng giới hạn chiều cao không thể tăng. Vì vậy phải di chuyển con trỏ ở phía thấp hơn.

### Lời giải

```java
static int maxWaterArea(int[] height) {
    int left = 0;
    int right = height.length - 1;
    int maximum = 0;

    while (left < right) {
        int width = right - left;
        int limitedHeight = Math.min(height[left], height[right]);
        int area = width * limitedHeight;
        maximum = Math.max(maximum, area);

        if (height[left] <= height[right]) {
            left++;
        } else {
            right--;
        }
    }

    return maximum;
}
```

**Độ phức tạp:** `O(n)` thời gian, `O(1)` bộ nhớ.

---

## Bài 28 — Đếm target bằng đệ quy

### Ý tưởng và logic

Base case: `index` đã ra ngoài mảng thì còn 0 lần xuất hiện. Mỗi lời gọi đóng góp 1 nếu phần tử hiện tại bằng target, ngược lại đóng góp 0.

### Lời giải

```java
static int recursiveCount(int[] nums, int target, int index) {
    if (index >= nums.length) {
        return 0;
    }

    int currentCount = nums[index] == target ? 1 : 0;
    return currentCount
            + recursiveCount(nums, target, index + 1);
}
```

`condition ? 1 : 0` là toán tử ba ngôi: điều kiện đúng nhận 1, sai nhận 0.

**Độ phức tạp:** `O(n)` thời gian và `O(n)` call stack.

---

## Bài 29 — Đối xứng bằng đệ quy

### Ý tưởng và logic

- Nếu `left >= right`, đã kiểm tra xong → `true`.
- Nếu hai đầu khác nhau → `false`.
- Nếu bằng nhau, thu nhỏ vào đoạn bên trong.

### Lời giải

```java
static boolean recursivePalindrome(
        int[] nums, int left, int right) {
    if (left >= right) {
        return true;
    }
    if (nums[left] != nums[right]) {
        return false;
    }

    return recursivePalindrome(nums, left + 1, right - 1);
}
```

**Độ phức tạp:** `O(n)` thời gian, `O(n)` call stack trong cách ký hiệu Big-O.

---

## Bài 30 — Đảo mảng bằng đệ quy

### Ý tưởng và logic

Đổi hai đầu rồi gọi đệ quy cho đoạn bên trong. Base case `left >= right` xử lý cả đoạn một phần tử và đoạn rỗng.

### Lời giải

```java
static void recursiveReverse(int[] nums, int left, int right) {
    if (left >= right) {
        return;
    }

    int temporary = nums[left];
    nums[left] = nums[right];
    nums[right] = temporary;

    recursiveReverse(nums, left + 1, right - 1);
}
```

`return;` kết thúc hàm `void` mà không trả về dữ liệu.

**Độ phức tạp:** `O(n)` thời gian, `O(n)` call stack.

---

## Bài 31 — Binary search bằng đệ quy

### Ý tưởng và logic

Mỗi lời gọi loại bỏ một nửa đoạn tìm kiếm. `left > right` nghĩa là đoạn rỗng nên target không tồn tại.

### Lời giải

```java
static int recursiveBinarySearch(
        int[] nums, int target, int left, int right) {
    if (left > right) {
        return -1;
    }

    int mid = left + (right - left) / 2;

    if (nums[mid] == target) {
        return mid;
    }
    if (nums[mid] < target) {
        return recursiveBinarySearch(
                nums, target, mid + 1, right);
    }
    return recursiveBinarySearch(nums, target, left, mid - 1);
}
```

**Độ phức tạp:** `O(log n)` thời gian, `O(log n)` call stack.

---

## Bài 32 — Kiểm tra sorted bằng đệ quy

### Ý tưởng và logic

Khi `index >= length - 1`, không còn cặp nào để so sánh. Nếu cặp hiện tại giảm, trả về `false`; nếu không, kiểm tra cặp kế tiếp.

### Lời giải

```java
static boolean recursiveIsSorted(int[] nums, int index) {
    if (index >= nums.length - 1) {
        return true;
    }
    if (nums[index] > nums[index + 1]) {
        return false;
    }

    return recursiveIsSorted(nums, index + 1);
}
```

Với mảng rỗng, `nums.length - 1 == -1`, nên `index = 0` thỏa base case ngay.

**Độ phức tạp:** `O(n)` thời gian, `O(n)` call stack.

---

## Bài 33 — Vị trí chèn

### Ý tưởng và logic

Tìm index đầu tiên có giá trị `>= target` bằng khoảng nửa mở `[left, right)`. Ban đầu `right = nums.length`, cho phép đáp án nằm ngay sau phần tử cuối.

### Lời giải

```java
static int searchInsertPosition(int[] nums, int target) {
    int left = 0;
    int right = nums.length;

    while (left < right) {
        int mid = left + (right - left) / 2;

        if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }

    return left;
}
```

Khi vòng lặp kết thúc, `left == right` và đó chính là vị trí chèn.

**Độ phức tạp:** `O(log n)` thời gian, `O(1)` bộ nhớ.

---

## Bài 34 — Vị trí xuất hiện cuối cùng

### Ý tưởng và logic

Khi tìm thấy target, lưu index vào `answer` nhưng tiếp tục tìm bên phải bằng `left = mid + 1`.

### Lời giải

```java
static int lastOccurrence(int[] nums, int target) {
    int left = 0;
    int right = nums.length - 1;
    int answer = -1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (nums[mid] <= target) {
            if (nums[mid] == target) {
                answer = mid;
            }
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return answer;
}
```

`answer = -1` biểu diễn chưa tìm thấy.

**Độ phức tạp:** `O(log n)` thời gian, `O(1)` bộ nhớ.

---

## Bài 35 — Khoảng xuất hiện của target

### Ý tưởng và logic

Chạy binary search hai lần: một lần nghiêng trái để tìm index đầu, một lần nghiêng phải để tìm index cuối.

### Lời giải

```java
static int[] searchRange(int[] nums, int target) {
    return new int[]{
        firstOccurrence(nums, target),
        lastOccurrence(nums, target)
    };
}

static int firstOccurrence(int[] nums, int target) {
    int left = 0;
    int right = nums.length - 1;
    int answer = -1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (nums[mid] >= target) {
            if (nums[mid] == target) {
                answer = mid;
            }
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return answer;
}
```

Hàm `lastOccurrence()` sử dụng lời giải Bài 34.

**Độ phức tạp:** `O(log n)` thời gian, `O(1)` bộ nhớ.

---

## Bài 36 — Đếm bằng binary search

### Ý tưởng và logic

Nếu `first == -1`, target không tồn tại. Ngược lại số phần tử trong đoạn đóng `[first, last]` là `last - first + 1`.

### Lời giải

```java
static int countOccurrencesBinary(int[] nums, int target) {
    int first = firstOccurrence(nums, target);

    if (first == -1) {
        return 0;
    }

    int last = lastOccurrence(nums, target);
    return last - first + 1;
}
```

Hàm sử dụng hai helper của Bài 34–35.

**Độ phức tạp:** `O(log n)` thời gian, `O(1)` bộ nhớ.

---

## Bài 37 — Căn bậc hai lấy phần nguyên

### Ý tưởng và logic

Binary search trên tập đáp án `0..n`. Nếu `mid² <= n`, `mid` là đáp án hợp lệ tạm thời và ta thử tìm giá trị lớn hơn. Nếu `mid² > n`, tìm bên trái.

### Lời giải

```java
static int sqrtFloor(int n) {
    int left = 0;
    int right = n;
    int answer = 0;

    while (left <= right) {
        int mid = left + (right - left) / 2;
        long square = (long) mid * mid;

        if (square <= n) {
            answer = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return answer;
}
```

Ép `(long) mid` trước phép nhân để phép nhân được thực hiện bằng `long`, tránh overflow.

**Độ phức tạp:** `O(log n)` thời gian, `O(1)` bộ nhớ.

---

## Bài 38 — Tìm trong mảng xoay

### Ý tưởng và logic

Trong mỗi vòng lặp, ít nhất một trong hai nửa `[left, mid]` hoặc `[mid, right]` được sắp xếp. Xác định nửa sorted, kiểm tra target có nằm trong khoảng giá trị của nửa đó không, rồi loại bỏ nửa còn lại.

### Lời giải

```java
static int searchRotated(int[] nums, int target) {
    int left = 0;
    int right = nums.length - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (nums[mid] == target) {
            return mid;
        }

        if (nums[left] <= nums[mid]) {
            // Nửa trái được sắp xếp.
            if (nums[left] <= target && target < nums[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        } else {
            // Nửa phải được sắp xếp.
            if (nums[mid] < target && target <= nums[right]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
    }

    return -1;
}
```

Các dấu `<` và `<=` được chọn để không xét lại `mid`, vì `mid` đã được kiểm tra ở đầu vòng lặp.

**Độ phức tạp:** `O(log n)` thời gian, `O(1)` bộ nhớ.

---

## Bài 39 — Selection sort

### Ý tưởng và logic

Tại vị trí `i`, tìm index của phần tử nhỏ nhất trong đoạn `[i, n - 1]`, rồi đổi nó với `nums[i]`.

### Lời giải

```java
static void selectionSort(int[] nums) {
    for (int i = 0; i < nums.length - 1; i++) {
        int minimumIndex = i;

        for (int j = i + 1; j < nums.length; j++) {
            if (nums[j] < nums[minimumIndex]) {
                minimumIndex = j;
            }
        }

        int temporary = nums[i];
        nums[i] = nums[minimumIndex];
        nums[minimumIndex] = temporary;
    }
}
```

Dù mảng đã sắp xếp, vòng trong vẫn tìm min của toàn bộ đoạn còn lại, nên vẫn `O(n²)`.

**Độ phức tạp:** `O(n²)` thời gian, `O(1)` bộ nhớ.

---

## Bài 40 — Bubble sort có dừng sớm

### Ý tưởng và logic

Mỗi vòng đưa phần tử lớn nhất chưa sắp xếp về cuối. Nếu không có lần đổi chỗ nào, mảng đã sorted và có thể dừng.

### Lời giải

```java
static void bubbleSort(int[] nums) {
    for (int end = nums.length - 1; end > 0; end--) {
        boolean swapped = false;

        for (int i = 0; i < end; i++) {
            if (nums[i] > nums[i + 1]) {
                int temporary = nums[i];
                nums[i] = nums[i + 1];
                nums[i + 1] = temporary;
                swapped = true;
            }
        }

        if (!swapped) {
            break;
        }
    }
}
```

`!swapped` nghĩa là `swapped == false`.

**Độ phức tạp:** tốt nhất `O(n)`, trung bình/xấu nhất `O(n²)`, bộ nhớ `O(1)`.

---

## Bài 41 — Sắp xếp 0, 1, 2

### Ý tưởng và bất biến

Ba con trỏ tạo bốn vùng:

```text
[0 ... low-1]      toàn số 0
[low ... mid-1]    toàn số 1
[mid ... high]     chưa xử lý
[high+1 ... n-1]   toàn số 2
```

### Lời giải

```java
static void sortColors(int[] nums) {
    int low = 0;
    int mid = 0;
    int high = nums.length - 1;

    while (mid <= high) {
        if (nums[mid] == 0) {
            swap(nums, low, mid);
            low++;
            mid++;
        } else if (nums[mid] == 1) {
            mid++;
        } else {
            swap(nums, mid, high);
            high--;
        }
    }
}

static void swap(int[] nums, int i, int j) {
    int temporary = nums[i];
    nums[i] = nums[j];
    nums[j] = temporary;
}
```

Sau khi đổi số 2 với `nums[high]`, không tăng `mid` vì giá trị vừa chuyển về `mid` chưa được kiểm tra.

**Độ phức tạp:** `O(n)` thời gian, `O(1)` bộ nhớ.

---

## Bài 42 — Xây dựng prefix sum

### Ý tưởng và logic

`prefix[i]` lưu tổng của `i` phần tử đầu tiên. Đặt `prefix[0] = 0` giúp công thức truy vấn đoạn không cần xử lý riêng đoạn bắt đầu từ index 0.

### Lời giải

```java
static long[] buildPrefixSum(int[] nums) {
    long[] prefix = new long[nums.length + 1];

    for (int i = 0; i < nums.length; i++) {
        prefix[i + 1] = prefix[i] + nums[i];
    }

    return prefix;
}
```

Với `{2,4,-1}`, prefix lần lượt là `{0,2,6,5}`.

**Độ phức tạp:** `O(n)` thời gian, `O(n)` cho mảng kết quả.

---

## Bài 43 — Tổng đoạn bằng prefix sum

### Ý tưởng và logic

`prefix[right + 1]` là tổng từ index 0 đến `right`; `prefix[left]` là phần nằm trước `left`. Lấy hiệu sẽ còn đúng đoạn `[left, right]`.

### Lời giải

```java
static long rangeSum(long[] prefix, int left, int right) {
    return prefix[right + 1] - prefix[left];
}
```

`right + 1` xuất hiện vì định nghĩa `prefix[i]` chứa tổng của `i` phần tử đầu tiên, không phải tổng đến index `i`.

**Độ phức tạp:** `O(1)` cho mỗi truy vấn.

---

## Bài 44 — Equilibrium index

### Ý tưởng và logic

Tính `totalSum` trước. Khi đang ở index `i`:

```text
rightSum = totalSum - leftSum - nums[i]
```

Sau khi kiểm tra, thêm `nums[i]` vào `leftSum` để chuẩn bị cho index tiếp theo.

### Lời giải

```java
static int equilibriumIndex(int[] nums) {
    long totalSum = 0;
    for (int number : nums) {
        totalSum += number;
    }

    long leftSum = 0;

    for (int i = 0; i < nums.length; i++) {
        long rightSum = totalSum - leftSum - nums[i];

        if (leftSum == rightSum) {
            return i;
        }

        leftSum += nums[i];
    }

    return -1;
}
```

Phải kiểm tra trước khi cộng `nums[i]` vào `leftSum`, vì phần tử tại `i` không thuộc bên trái.

**Độ phức tạp:** `O(n)` thời gian, `O(1)` bộ nhớ.

---

## Bài 45 — Tổng lớn nhất của cửa sổ kích thước k

### Ý tưởng và logic

Tính tổng cửa sổ đầu tiên. Khi trượt sang phải một vị trí:

```text
tổng mới = tổng cũ
         - phần tử rời khỏi cửa sổ
         + phần tử mới đi vào
```

### Lời giải

```java
static long maxWindowSum(int[] nums, int k) {
    long currentSum = 0;

    for (int i = 0; i < k; i++) {
        currentSum += nums[i];
    }

    long maximumSum = currentSum;

    for (int i = k; i < nums.length; i++) {
        currentSum -= nums[i - k];
        currentSum += nums[i];
        maximumSum = Math.max(maximumSum, currentSum);
    }

    return maximumSum;
}
```

Khởi tạo `maximumSum` bằng tổng cửa sổ đầu tiên, không phải 0, vì mọi số có thể âm.

**Độ phức tạp:** `O(n)` thời gian, `O(1)` bộ nhớ.

---

## Tổng kết

| Nhóm | Bài | Kỹ thuật cốt lõi |
|---|---:|---|
| Duyệt/counting | 16–20 | Biến đếm, min/max, frequency array |
| Two pointers | 21–27 | Hai mảng, đọc/ghi, hai đầu, reversal |
| Recursion | 28–32 | Base case và thu nhỏ bài toán |
| Binary search | 33–38 | Lower bound, biên trái/phải, mảng xoay |
| Sorting | 39–41 | Selection, bubble, Dutch National Flag |
| Prefix/window | 42–45 | Tổng tích lũy và cập nhật cửa sổ |

Các lỗi cần tránh:

- Khởi tạo max/min bằng 0 khi mảng có thể chỉ chứa số âm.
- Dùng `left < right` thay vì `left <= right` sai ngữ cảnh trong binary search.
- Quên xử lý mảng rỗng trước phép `% nums.length`.
- Nhân hai số `int` rồi mới gán sang `long`; cần ép kiểu trước phép nhân.
- Tăng `mid` sau khi đổi với `high` trong Dutch National Flag.
- Khởi tạo tổng lớn nhất bằng 0 khi cửa sổ có thể toàn số âm.
