# Lời giải 15 bài tập mảng Java

Tài liệu này giải chi tiết 15 bài trong bộ `java_array_15_exercises_vi.md`, gồm: duyệt mảng, counting, two pointers, recursion, binary search và sorting.

Để chạy các test mảng, cần import:

```java
import java.util.Arrays;
```

Trong Eclipse, bật `assert` bằng cách thêm `-ea` vào **Run Configurations → Arguments → VM arguments**.

---

## Bài 1 — Tính tổng các phần tử

### Phân tích

- **Input:** mảng số nguyên `nums`.
- **Output:** tổng của mọi phần tử.
- Khởi tạo `sum = 0` vì 0 là phần tử trung hòa của phép cộng.
- Duyệt từng số và cộng nó vào `sum`.
- Mảng rỗng không chạy vòng lặp nên kết quả tự nhiên là 0.

### Lời giải

```java
static int sumArray(int[] nums) {
    int sum = 0;

    for (int number : nums) {
        sum += number;
    }

    return sum;
}
```

### Độ phức tạp

- Thời gian: `O(n)` vì phải đọc tất cả phần tử.
- Bộ nhớ phụ: `O(1)`.

---

## Bài 2 — Đếm số chẵn và số lẻ

### Phân tích

Một số là số chẵn khi:

```java
number % 2 == 0
```

Điều kiện này đúng với cả số âm và số 0. Ta dùng hai biến đếm độc lập rồi trả về `{evenCount, oddCount}`.

### Lời giải

```java
static int[] countEvenOdd(int[] nums) {
    int evenCount = 0;
    int oddCount = 0;

    for (int number : nums) {
        if (number % 2 == 0) {
            evenCount++;
        } else {
            oddCount++;
        }
    }

    return new int[]{evenCount, oddCount};
}
```

### Độ phức tạp

- Thời gian: `O(n)`.
- Bộ nhớ phụ: `O(1)`; mảng kết quả luôn có đúng hai phần tử.

---

## Bài 3 — Đếm số lần xuất hiện của `target`

### Phân tích

Ta phải kiểm tra từng phần tử vì mảng chưa được đảm bảo sắp xếp. Mỗi khi phần tử bằng `target`, tăng `count` lên 1.

### Lời giải

```java
static int countOccurrences(int[] nums, int target) {
    int count = 0;

    for (int number : nums) {
        if (number == target) {
            count++;
        }
    }

    return count;
}
```

### Độ phức tạp

- Thời gian: `O(n)`.
- Bộ nhớ phụ: `O(1)`.

---

## Bài 4 — Thống kê tần suất các chữ số

### Phân tích

Mỗi phần tử chỉ có thể nằm trong khoảng `0..9`, nên tạo mảng đếm gồm 10 ô:

```text
index:      0 1 2 3 4 5 6 7 8 9
frequency:  ? ? ? ? ? ? ? ? ? ?
```

Khi gặp chữ số `digit`, dùng chính giá trị đó làm index:

```java
frequency[digit]++;
```

Ví dụ gặp số `3` thì tăng `frequency[3]`.

### Lời giải

```java
static int[] countDigits(int[] digits) {
    int[] frequency = new int[10];

    for (int digit : digits) {
        frequency[digit]++;
    }

    return frequency;
}
```

### Độ phức tạp

- Thời gian: `O(n)`.
- Bộ nhớ phụ: `O(1)` vì mảng đếm luôn có kích thước 10, không phụ thuộc `n`.

---

## Bài 5 — Đảo ngược mảng tại chỗ

### Phân tích two pointers

Đặt hai con trỏ:

- `left` bắt đầu ở đầu mảng.
- `right` bắt đầu ở cuối mảng.

Mỗi bước:

1. Đổi chỗ `nums[left]` và `nums[right]`.
2. Tăng `left`.
3. Giảm `right`.
4. Dừng khi hai con trỏ gặp hoặc vượt nhau.

Ví dụ:

```text
[1, 2, 3, 4]
 L        R

[4, 2, 3, 1]
    L  R

[4, 3, 2, 1]
```

### Lời giải

```java
static void reverseArray(int[] nums) {
    int left = 0;
    int right = nums.length - 1;

    while (left < right) {
        int temporary = nums[left];
        nums[left] = nums[right];
        nums[right] = temporary;

        left++;
        right--;
    }
}
```

### Độ phức tạp

- Thời gian: `O(n)`.
- Bộ nhớ phụ: `O(1)` vì chỉ dùng một biến tạm.

---

## Bài 6 — Kiểm tra mảng đối xứng

### Phân tích

So sánh các cặp phần tử đối xứng:

```text
nums[0] với nums[n - 1]
nums[1] với nums[n - 2]
...
```

Nếu chỉ một cặp khác nhau, có thể trả về `false` ngay. Nếu hai con trỏ gặp nhau mà chưa có cặp nào khác nhau, mảng đối xứng.

Mảng rỗng và mảng một phần tử đều được xem là đối xứng.

### Lời giải

```java
static boolean isPalindrome(int[] nums) {
    int left = 0;
    int right = nums.length - 1;

    while (left < right) {
        if (nums[left] != nums[right]) {
            return false;
        }

        left++;
        right--;
    }

    return true;
}
```

### Độ phức tạp

- Thời gian: `O(n)`.
- Bộ nhớ phụ: `O(1)`.

---

## Bài 7 — Di chuyển số 0 về cuối

### Phân tích two pointers đọc/ghi

Ta sử dụng:

- Vòng `for` để **đọc** từng phần tử.
- `write` là vị trí tiếp theo để **ghi** một số khác 0.

Với `[0, 1, 0, 3, 12]`:

```text
Đọc 0  → bỏ qua
Đọc 1  → ghi tại index 0
Đọc 0  → bỏ qua
Đọc 3  → ghi tại index 1
Đọc 12 → ghi tại index 2
```

Mảng tạm thời trở thành `[1, 3, 12, 3, 12]`. Sau đó điền số 0 từ `write = 3` đến hết mảng.

Cách này giữ nguyên thứ tự của `1, 3, 12`.

### Lời giải

```java
static void moveZeros(int[] nums) {
    int write = 0;

    // Đưa tất cả số khác 0 về phía trước.
    for (int number : nums) {
        if (number != 0) {
            nums[write] = number;
            write++;
        }
    }

    // Điền 0 vào các vị trí còn lại.
    while (write < nums.length) {
        nums[write] = 0;
        write++;
    }
}
```

### Độ phức tạp

- Thời gian: `O(n)`.
- Bộ nhớ phụ: `O(1)`.

---

## Bài 8 — Xóa phần tử trùng trong mảng đã sắp xếp

### Phân tích

Điểm quan trọng: mảng đã sắp xếp nên các giá trị giống nhau nằm cạnh nhau.

- `read` duyệt các phần tử từ trái sang phải.
- `write` chỉ vị trí sẽ ghi giá trị khác nhau tiếp theo.
- `nums[write - 1]` là giá trị khác nhau gần nhất đã giữ lại.

Ban đầu giữ `nums[0]`, vì vậy `write = 1`.

Với `[0, 0, 1, 1, 2]`:

```text
read gặp 0: giống giá trị trước → bỏ qua
read gặp 1: khác 0 → ghi vào index 1
read gặp 1: giống giá trị trước → bỏ qua
read gặp 2: khác 1 → ghi vào index 2
```

Ba phần tử đầu trở thành `[0, 1, 2]`, nên trả về `3`.

### Lời giải

```java
static int removeDuplicates(int[] nums) {
    if (nums.length == 0) {
        return 0;
    }

    int write = 1;

    for (int read = 1; read < nums.length; read++) {
        if (nums[read] != nums[write - 1]) {
            nums[write] = nums[read];
            write++;
        }
    }

    return write;
}
```

### Độ phức tạp

- Thời gian: `O(n)`.
- Bộ nhớ phụ: `O(1)`.

---

## Bài 9 — Tính tổng bằng đệ quy

### Phân tích đệ quy

Bài toán tại `index` được viết thành:

```text
tổng từ index
= nums[index] + tổng từ index + 1
```

**Base case:** khi `index` đã ra ngoài mảng, không còn phần tử nào để cộng nên trả về 0.

Với `[1, 2, 3]`:

```text
recursiveSum(nums, 0)
= 1 + recursiveSum(nums, 1)
= 1 + 2 + recursiveSum(nums, 2)
= 1 + 2 + 3 + recursiveSum(nums, 3)
= 1 + 2 + 3 + 0
```

### Lời giải

```java
static int recursiveSum(int[] nums, int index) {
    if (index >= nums.length) {
        return 0;
    }

    return nums[index] + recursiveSum(nums, index + 1);
}
```

### Độ phức tạp

- Thời gian: `O(n)`.
- Call stack: `O(n)`.
- Giới hạn `n <= 1000` giúp giảm nguy cơ `StackOverflowError`.

---

## Bài 10 — Tìm giá trị lớn nhất bằng đệ quy

### Phân tích

**Base case:** khi đang ở phần tử cuối cùng, giá trị lớn nhất của đoạn chỉ có một phần tử chính là phần tử đó.

Ở mỗi bước:

1. Gọi đệ quy để tìm giá trị lớn nhất của phần mảng bên phải.
2. So sánh kết quả đó với `nums[index]`.

Không nên khởi tạo giá trị lớn nhất bằng 0 vì mảng có thể chỉ chứa số âm.

### Lời giải

```java
static int recursiveMax(int[] nums, int index) {
    if (index == nums.length - 1) {
        return nums[index];
    }

    int maximumOfRest = recursiveMax(nums, index + 1);
    return Math.max(nums[index], maximumOfRest);
}
```

### Độ phức tạp

- Thời gian: `O(n)`.
- Call stack: `O(n)`.

Hàm giả định mảng không rỗng và `index` hợp lệ, đúng theo ràng buộc của đề.

---

## Bài 11 — Binary search cơ bản

### Phân tích

Binary search chỉ áp dụng trực tiếp khi mảng đã sắp xếp.

Không gian tìm kiếm ban đầu:

```text
[left........................right]
```

Mỗi vòng lặp:

- Nếu `nums[mid] == target`: tìm thấy.
- Nếu `nums[mid] < target`: target chỉ có thể ở bên phải, đặt `left = mid + 1`.
- Nếu `nums[mid] > target`: target chỉ có thể ở bên trái, đặt `right = mid - 1`.

Dùng `left <= right` vì khi `left == right`, vẫn còn đúng một phần tử cần kiểm tra.

### Lời giải

```java
static int binarySearch(int[] nums, int target) {
    int left = 0;
    int right = nums.length - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return -1;
}
```

### Vì sao tính `mid` như trên?

```java
int mid = left + (right - left) / 2;
```

Cách này tránh nguy cơ `left + right` bị tràn số nguyên khi hai giá trị rất lớn.

### Độ phức tạp

- Thời gian: `O(log n)`.
- Bộ nhớ phụ: `O(1)`.

---

## Bài 12 — Tìm vị trí xuất hiện đầu tiên

### Phân tích

Khác binary search thông thường, khi tìm thấy `target` ta chưa được dừng vì có thể còn một `target` khác ở bên trái.

Khi `nums[mid] == target`:

1. Lưu `mid` vào `answer`.
2. Tiếp tục tìm bên trái bằng `right = mid - 1`.

Điều kiện `nums[mid] >= target` có thể gộp hai trường hợp:

- Bằng target: ghi nhận kết quả và tìm trái.
- Lớn hơn target: chỉ cần tìm trái.

### Lời giải

```java
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

### Ví dụ

```text
nums   = [1, 2, 2, 2, 3]
target = 2

Tìm thấy 2 ở index 2 → answer = 2, tiếp tục tìm trái
Tìm thấy 2 ở index 1 → answer = 1, tiếp tục tìm trái
Kết thúc → trả về 1
```

### Độ phức tạp

- Thời gian: `O(log n)`.
- Bộ nhớ phụ: `O(1)`.

---

## Bài 13 — Insertion sort

### Ý tưởng

Chia mảng thành hai phần:

```text
[phần đã sắp xếp | phần chưa sắp xếp]
```

Ở mỗi bước:

1. Lấy `current = nums[i]`.
2. Dịch các phần tử lớn hơn `current` sang phải.
3. Chèn `current` vào khoảng trống phù hợp.

Ví dụ chèn `2` vào `[3, 5]`:

```text
[3, 5, 2]
       current

[3, 5, 5]  // dịch 5
[3, 3, 5]  // dịch 3
[2, 3, 5]  // chèn 2
```

### Lời giải

```java
static void insertionSort(int[] nums) {
    for (int i = 1; i < nums.length; i++) {
        int current = nums[i];
        int j = i - 1;

        while (j >= 0 && nums[j] > current) {
            nums[j + 1] = nums[j];
            j--;
        }

        nums[j + 1] = current;
    }
}
```

### Độ phức tạp

- Tốt nhất: `O(n)` khi mảng đã tăng dần.
- Xấu nhất: `O(n²)` khi mảng giảm dần.
- Bộ nhớ phụ: `O(1)`.
- Đây là thuật toán stable vì chỉ dịch phần tử khi `nums[j] > current`, không dịch khi bằng nhau.

---

## Bài 14 — Counting sort

### Phân tích

Counting sort không so sánh từng cặp phần tử. Nó đếm xem mỗi giá trị xuất hiện bao nhiêu lần.

Ví dụ:

```text
nums = [2, 0, 2, 1]

value:      0 1 2
frequency:  1 1 2
```

Sau đó ghi lại:

```text
0 một lần, 1 một lần, 2 hai lần
→ [0, 1, 2, 2]
```

`write` chỉ vị trí tiếp theo cần ghi vào `nums`.

### Lời giải

```java
static void countingSort(int[] nums, int maxValue) {
    int[] frequency = new int[maxValue + 1];

    // Đếm tần suất.
    for (int number : nums) {
        frequency[number]++;
    }

    // Ghi lại mảng theo thứ tự tăng dần.
    int write = 0;

    for (int value = 0; value <= maxValue; value++) {
        while (frequency[value] > 0) {
            nums[write] = value;
            write++;
            frequency[value]--;
        }
    }
}
```

### Độ phức tạp

Gọi `k = maxValue + 1`:

- Thời gian: `O(n + k)`.
- Bộ nhớ phụ: `O(k)`.

Counting sort phù hợp khi khoảng giá trị không quá lớn. Nếu chỉ có vài phần tử nhưng `maxValue` cực lớn, mảng `frequency` sẽ lãng phí bộ nhớ.

---

## Bài 15 — Merge sort bằng đệ quy

### Phần 1: Chia mảng

`mergeSort()` liên tục chia đoạn hiện tại thành hai nửa:

```text
[5, 2, 4, 1]
     /       \
  [5, 2]   [4, 1]
   /  \     /  \
 [5] [2]  [4] [1]
```

**Base case:** `left >= right` nghĩa là đoạn có tối đa một phần tử, nên đã được sắp xếp.

Sau khi sắp xếp hai nửa, gọi `merge()` để trộn chúng lại.

```java
static void mergeSort(int[] nums, int left, int right) {
    if (left >= right) {
        return;
    }

    int mid = left + (right - left) / 2;

    mergeSort(nums, left, mid);
    mergeSort(nums, mid + 1, right);
    merge(nums, left, mid, right);
}
```

### Phần 2: Trộn hai nửa đã sắp xếp

Ta có hai đoạn:

```text
[left ... mid] và [mid + 1 ... right]
```

Sử dụng ba con trỏ:

- `first`: đọc nửa trái.
- `second`: đọc nửa phải.
- `write`: ghi vào mảng tạm.

Mỗi lần lấy phần tử nhỏ hơn giữa `nums[first]` và `nums[second]`. Khi một nửa đã hết, chép toàn bộ phần còn lại của nửa kia.

```java
static void merge(int[] nums, int left, int mid, int right) {
    int[] temporary = new int[right - left + 1];

    int first = left;
    int second = mid + 1;
    int write = 0;

    while (first <= mid && second <= right) {
        if (nums[first] <= nums[second]) {
            temporary[write] = nums[first];
            first++;
        } else {
            temporary[write] = nums[second];
            second++;
        }
        write++;
    }

    while (first <= mid) {
        temporary[write] = nums[first];
        first++;
        write++;
    }

    while (second <= right) {
        temporary[write] = nums[second];
        second++;
        write++;
    }

    // Chép đoạn đã trộn về đúng vị trí trong nums.
    for (int i = 0; i < temporary.length; i++) {
        nums[left + i] = temporary[i];
    }
}
```

### Vì sao mảng rỗng vẫn an toàn?

Lời gọi:

```java
mergeSort(nums, 0, nums.length - 1);
```

Với mảng rỗng, `right = -1`. Điều kiện `left >= right` là `0 >= -1`, nên hàm trả về ngay và không truy cập mảng.

### Độ phức tạp

- Mỗi tầng đệ quy trộn tổng cộng `n` phần tử.
- Có khoảng `log n` tầng.
- Thời gian: `O(n log n)` trong mọi trường hợp.
- Bộ nhớ phụ: `O(n)` cho các mảng tạm.
- Call stack: `O(log n)`.

---

## Chương trình test tổng hợp

Đặt các hàm trên vào cùng một class rồi sử dụng `main()` dưới đây. Nhớ bật `-ea`.

```java
public static void main(String[] args) {
    assert sumArray(new int[]{1, 2, 3, 4}) == 10;
    assert sumArray(new int[]{-3, 5, -2}) == 0;

    assert Arrays.equals(
        countEvenOdd(new int[]{1, 2, 3, 4, 6}),
        new int[]{3, 2}
    );

    assert countOccurrences(new int[]{1, 2, 2, 3, 2}, 2) == 3;

    assert Arrays.equals(
        countDigits(new int[]{1, 2, 1, 0, 9, 1}),
        new int[]{1, 3, 1, 0, 0, 0, 0, 0, 0, 1}
    );

    int[] reversed = {1, 2, 3, 4};
    reverseArray(reversed);
    assert Arrays.equals(reversed, new int[]{4, 3, 2, 1});

    assert isPalindrome(new int[]{1, 2, 3, 2, 1});
    assert !isPalindrome(new int[]{1, 2, 3});

    int[] moved = {0, 1, 0, 3, 12};
    moveZeros(moved);
    assert Arrays.equals(moved, new int[]{1, 3, 12, 0, 0});

    int[] unique = {0, 0, 1, 1, 1, 2, 2, 3};
    int k = removeDuplicates(unique);
    assert k == 4;
    assert Arrays.equals(
        Arrays.copyOf(unique, k),
        new int[]{0, 1, 2, 3}
    );

    assert recursiveSum(new int[]{1, 2, 3, 4}, 0) == 10;
    assert recursiveMax(new int[]{-8, -3, -10}, 0) == -3;

    assert binarySearch(new int[]{1, 3, 5, 7, 9}, 7) == 3;
    assert binarySearch(new int[]{1, 3, 5, 7, 9}, 6) == -1;

    assert firstOccurrence(new int[]{1, 2, 2, 2, 3}, 2) == 1;

    int[] insertion = {5, 2, 4, 6, 1, 3};
    insertionSort(insertion);
    assert Arrays.equals(insertion, new int[]{1, 2, 3, 4, 5, 6});

    int[] counted = {4, 2, 2, 8, 3, 3, 1};
    countingSort(counted, 8);
    assert Arrays.equals(counted, new int[]{1, 2, 2, 3, 3, 4, 8});

    int[] merged = {5, 2, 4, 1, 3};
    mergeSort(merged, 0, merged.length - 1);
    assert Arrays.equals(merged, new int[]{1, 2, 3, 4, 5});

    System.out.println("All 15 exercises passed!");
}
```

Nếu Console hiển thị:

```text
All 15 exercises passed!
```

thì toàn bộ test đã chạy thành công. Nếu một điều kiện sai, Java sinh `AssertionError` tại test tương ứng.

## Giải thích cú pháp và luồng logic từng bài

Phần này tập trung vào hai câu hỏi:

1. **Cú pháp Java đó có nghĩa gì?**
2. **Máy tính thực hiện các dòng code theo thứ tự nào?**

### Bài 1 — Cú pháp và logic tính tổng

#### Cú pháp quan trọng

```java
int sum = 0;
```

- `int`: kiểu số nguyên 32-bit.
- `sum`: tên biến.
- `=`: phép gán giá trị bên phải cho biến bên trái.
- `0`: giá trị khởi tạo. Nếu không khởi tạo biến cục bộ, Java không cho phép sử dụng nó.

```java
for (int number : nums)
```

Đây là enhanced `for`, đọc là: **với mỗi số `number` nằm trong mảng `nums`**.

```java
sum += number;
```

Là cách viết ngắn của:

```java
sum = sum + number;
```

```java
return sum;
```

Kết thúc hàm và gửi giá trị `sum` về nơi đã gọi hàm.

#### Luồng logic

Với `nums = {2, 5, -1}`:

| Lần lặp | `number` | `sum` trước | `sum` sau |
|---:|---:|---:|---:|
| Ban đầu | — | — | 0 |
| 1 | 2 | 0 | 2 |
| 2 | 5 | 2 | 7 |
| 3 | -1 | 7 | 6 |

Cuối cùng hàm trả về `6`.

---

### Bài 2 — Cú pháp và logic đếm chẵn/lẻ

#### Cú pháp quan trọng

```java
number % 2
```

`%` lấy phần dư của phép chia. Nếu chia hết cho 2 thì phần dư bằng 0.

```java
if (number % 2 == 0)
```

- `if`: chạy khối code khi điều kiện đúng.
- `==`: so sánh hai giá trị; không phải phép gán.
- `else`: chạy khi điều kiện của `if` sai.

```java
evenCount++;
```

Là cách viết ngắn của:

```java
evenCount = evenCount + 1;
```

```java
return new int[]{evenCount, oddCount};
```

- `int[]`: kiểu mảng số nguyên.
- `new int[]{...}`: tạo một mảng mới và điền sẵn các phần tử.
- Vị trí 0 chứa số lượng số chẵn, vị trí 1 chứa số lượng số lẻ.

#### Luồng logic

Với `{1, 2, 4}`:

1. `1 % 2 != 0` → tăng `oddCount`.
2. `2 % 2 == 0` → tăng `evenCount`.
3. `4 % 2 == 0` → tăng `evenCount`.
4. Trả về `{2, 1}`.

---

### Bài 3 — Cú pháp và logic đếm `target`

#### Cú pháp quan trọng

```java
static int countOccurrences(int[] nums, int target)
```

- `static`: có thể gọi hàm trực tiếp từ `main()` mà không cần tạo object.
- `int` trước tên hàm: hàm phải trả về một số nguyên.
- `int[] nums`: tham số mảng đầu vào.
- `int target`: giá trị cần tìm.

```java
if (number == target)
```

So sánh giá trị phần tử hiện tại với `target`. Vì cả hai là `int`, dùng `==` là đúng.

#### Luồng logic

Với `nums = {2, 1, 2, 2}` và `target = 2`:

```text
2 == 2 → count = 1
1 == 2 → sai, count vẫn bằng 1
2 == 2 → count = 2
2 == 2 → count = 3
```

Không thể dừng tại lần tìm thấy đầu tiên vì bài yêu cầu đếm tất cả lần xuất hiện.

---

### Bài 4 — Cú pháp và logic mảng tần suất

#### Cú pháp quan trọng

```java
int[] frequency = new int[10];
```

Tạo mảng 10 số nguyên. Java tự đặt giá trị ban đầu của tất cả phần tử là 0.

```java
frequency[digit]++;
```

Giá trị `digit` được dùng làm index. Nếu `digit = 7`, dòng này tương đương:

```java
frequency[7] = frequency[7] + 1;
```

Vì thế đề phải đảm bảo `digit` nằm trong `0..9`; nếu là `10` hoặc `-1`, chương trình sẽ phát sinh `ArrayIndexOutOfBoundsException`.

#### Luồng logic

Với `{1, 3, 1}`:

1. Gặp `1` → `frequency[1]` từ 0 thành 1.
2. Gặp `3` → `frequency[3]` từ 0 thành 1.
3. Gặp `1` → `frequency[1]` từ 1 thành 2.

Kết quả chứa `2` ở index 1 và `1` ở index 3.

---

### Bài 5 — Cú pháp và logic đảo mảng

#### Cú pháp quan trọng

```java
static void reverseArray(int[] nums)
```

`void` nghĩa là hàm không trả về giá trị. Hàm thay đổi trực tiếp nội dung của mảng được truyền vào.

```java
int right = nums.length - 1;
```

- `nums.length`: số phần tử của mảng.
- Vì index bắt đầu từ 0 nên index cuối là `length - 1`.

```java
while (left < right)
```

Tiếp tục lặp khi vẫn còn một cặp phần tử chưa đổi chỗ. Nếu dùng `left <= right`, phần tử chính giữa có thể tự đổi với chính nó; không sai kết quả nhưng thừa thao tác.

Ba dòng đổi chỗ:

```java
int temporary = nums[left];
nums[left] = nums[right];
nums[right] = temporary;
```

Phải giữ giá trị bên trái trong `temporary`; nếu gán trực tiếp, giá trị cũ sẽ bị mất.

#### Luồng logic

Với `{10, 20, 30, 40}`:

1. `left = 0`, `right = 3`: đổi 10 với 40.
2. `left = 1`, `right = 2`: đổi 20 với 30.
3. `left = 2`, `right = 1`: điều kiện sai, kết thúc.

---

### Bài 6 — Cú pháp và logic kiểm tra đối xứng

#### Cú pháp quan trọng

```java
static boolean isPalindrome(int[] nums)
```

`boolean` cho biết hàm trả về `true` hoặc `false`.

```java
if (nums[left] != nums[right]) {
    return false;
}
```

- `!=`: kiểm tra hai giá trị khác nhau.
- `return false`: kết thúc hàm ngay lập tức. Đây gọi là **early return**.

```java
return true;
```

Dòng này chỉ chạy khi vòng lặp đã kiểm tra xong mà không gặp cặp nào khác nhau.

#### Luồng logic

Với `{1, 2, 1}`:

1. So sánh index 0 và 2: `1 == 1`.
2. Di chuyển hai con trỏ vào giữa.
3. `left == right`, vòng lặp dừng.
4. Trả về `true`.

Với `{1, 2, 3}`, cặp đầu tiên `1 != 3`, nên trả về `false` ngay.

---

### Bài 7 — Cú pháp và logic di chuyển số 0

#### Cú pháp quan trọng

```java
int write = 0;
```

`write` không phải giá trị trong mảng; nó là index cho biết ô tiếp theo để ghi số khác 0.

```java
if (number != 0) {
    nums[write] = number;
    write++;
}
```

Chỉ khi gặp số khác 0 mới ghi và di chuyển `write`. Vì đọc từ trái sang phải, thứ tự tương đối của các số khác 0 được giữ nguyên.

```java
while (write < nums.length)
```

Sau khi gom số khác 0, vòng `while` điền số 0 vào phần còn lại.

#### Luồng logic

Với `{0, 5, 0, 2}`:

| Đọc | Hành động | `write` | Phần đầu mảng có ý nghĩa |
|---:|---|---:|---|
| 0 | Bỏ qua | 0 | `[]` |
| 5 | Ghi vào index 0 | 1 | `[5]` |
| 0 | Bỏ qua | 1 | `[5]` |
| 2 | Ghi vào index 1 | 2 | `[5, 2]` |

Cuối cùng điền 0 vào index 2 và 3 → `{5, 2, 0, 0}`.

---

### Bài 8 — Cú pháp và logic xóa trùng

#### Cú pháp quan trọng

```java
if (nums.length == 0) {
    return 0;
}
```

Đây là guard clause xử lý trường hợp đặc biệt trước, tránh truy cập `nums[0]` khi mảng rỗng.

```java
for (int read = 1; read < nums.length; read++)
```

- Bắt đầu `read = 1` vì phần tử index 0 luôn là giá trị khác nhau đầu tiên.
- `read++` tăng index sau mỗi lần lặp.

```java
nums[read] != nums[write - 1]
```

So sánh phần tử đang đọc với giá trị khác nhau gần nhất đã ghi. Không nhất thiết so với `nums[read - 1]`, vì phần đầu mảng đang được ghi đè dần.

#### Luồng logic

Với `{1, 1, 2, 2, 3}`:

```text
Ban đầu: giữ 1, write = 1
read = 1: gặp 1 trùng → bỏ qua
read = 2: gặp 2 mới   → nums[1] = 2, write = 2
read = 3: gặp 2 trùng → bỏ qua
read = 4: gặp 3 mới   → nums[2] = 3, write = 3
```

`write = 3` vừa là số lượng phần tử khác nhau, vừa là index của ô trống tiếp theo.

---

### Bài 9 — Cú pháp và logic tổng đệ quy

#### Cú pháp quan trọng

```java
recursiveSum(nums, index + 1)
```

Hàm gọi lại chính nó nhưng với `index` lớn hơn 1. Mỗi lời gọi xử lý một phần tử ít hơn.

```java
if (index >= nums.length) {
    return 0;
}
```

Đây là base case. Không có nó, hàm tiếp tục gọi mãi cho đến khi lỗi stack hoặc truy cập ngoài mảng.

```java
return nums[index] + recursiveSum(nums, index + 1);
```

Java phải tính lời gọi bên phải trước rồi mới hoàn thành phép cộng của lời gọi hiện tại.

#### Luồng logic và call stack

Với `{4, 6}`:

```text
sum(0)
└── 4 + sum(1)
        └── 6 + sum(2)
                └── 0       // base case
```

Kết quả quay ngược trở lại:

```text
sum(2) = 0
sum(1) = 6 + 0 = 6
sum(0) = 4 + 6 = 10
```

---

### Bài 10 — Cú pháp và logic tìm max đệ quy

#### Cú pháp quan trọng

```java
if (index == nums.length - 1)
```

Base case xảy ra tại phần tử cuối. Giá trị lớn nhất của một đoạn chỉ có một phần tử là chính phần tử đó.

```java
int maximumOfRest = recursiveMax(nums, index + 1);
```

Biến này lưu giá trị lớn nhất của toàn bộ phần mảng nằm bên phải `index`.

```java
Math.max(nums[index], maximumOfRest)
```

`Math.max(a, b)` trả về giá trị lớn hơn giữa `a` và `b`.

#### Luồng logic

Với `{3, 8, 2}`:

```text
max(2) = 2
max(1) = Math.max(8, 2) = 8
max(0) = Math.max(3, 8) = 8
```

Base case không trả về 0 vì nếu mảng là `{-8, -3}`, 0 không tồn tại trong mảng nhưng lại lớn hơn mọi phần tử.

---

### Bài 11 — Cú pháp và logic binary search

#### Cú pháp quan trọng

```java
int left = 0;
int right = nums.length - 1;
```

Đoạn tìm kiếm là đoạn đóng `[left, right]`, tức là bao gồm cả hai đầu.

```java
while (left <= right)
```

Khi `left == right`, đoạn vẫn còn một phần tử nên phải tiếp tục kiểm tra.

```java
int mid = left + (right - left) / 2;
```

Phép chia hai số nguyên bỏ phần thập phân. Ví dụ `5 / 2 == 2`.

```java
left = mid + 1;
right = mid - 1;
```

Không giữ lại `mid` vì đã kiểm tra và biết `nums[mid]` không phải đáp án. Nếu gán `left = mid` hoặc `right = mid`, vòng lặp có thể không thu nhỏ và chạy vô hạn.

#### Luồng logic

Với `{1, 3, 5, 7, 9}`, tìm `7`:

| `left` | `right` | `mid` | `nums[mid]` | Hành động |
|---:|---:|---:|---:|---|
| 0 | 4 | 2 | 5 | `5 < 7`, tìm bên phải |
| 3 | 4 | 3 | 7 | Tìm thấy, trả về 3 |

---

### Bài 12 — Cú pháp và logic tìm vị trí đầu tiên

#### Cú pháp quan trọng

```java
int answer = -1;
```

`-1` là sentinel value, biểu diễn trạng thái chưa tìm thấy.

```java
if (nums[mid] >= target)
```

Nếu phần tử giữa bằng hoặc lớn hơn target, vị trí đầu tiên không thể nằm bên phải `mid`; ta thu hẹp sang trái.

```java
if (nums[mid] == target) {
    answer = mid;
}
right = mid - 1;
```

Khi tìm thấy:

1. Lưu một đáp án tạm thời.
2. Không `return` ngay.
3. Tiếp tục tìm bên trái xem có index nhỏ hơn không.

#### Luồng logic

Với `{1, 2, 2, 2, 5}`, tìm `2`:

```text
mid = 2: thấy 2 → answer = 2, tìm trái
mid = 0: thấy 1 → tìm phải
mid = 1: thấy 2 → answer = 1, tìm trái
kết thúc → trả về 1
```

---

### Bài 13 — Cú pháp và logic insertion sort

#### Cú pháp quan trọng

```java
for (int i = 1; i < nums.length; i++)
```

Bắt đầu từ index 1 vì đoạn chỉ chứa `nums[0]` đã được xem là sắp xếp.

```java
int current = nums[i];
int j = i - 1;
```

- `current`: giá trị cần chèn.
- `j`: duyệt ngược phần đã sắp xếp bên trái.

```java
while (j >= 0 && nums[j] > current)
```

`&&` là AND logic và có short-circuit:

- Java kiểm tra `j >= 0` trước.
- Nếu sai, Java không đọc `nums[j]`, nhờ đó tránh index `-1`.

```java
nums[j + 1] = nums[j];
```

Dịch phần tử lớn hơn sang phải, không phải đổi chỗ liên tục.

```java
nums[j + 1] = current;
```

Sau vòng `while`, `j` đang ở ngay bên trái vị trí cần chèn, nên vị trí đúng là `j + 1`.

#### Luồng logic

Với `{5, 2, 4}`:

```text
i = 1, current = 2: dịch 5 → chèn 2 → {2, 5, 4}
i = 2, current = 4: dịch 5 → chèn 4 → {2, 4, 5}
```

---

### Bài 14 — Cú pháp và logic counting sort

#### Cú pháp quan trọng

```java
new int[maxValue + 1]
```

Cần `+1` vì nếu `maxValue = 8`, ta cần các index từ 0 đến 8, tổng cộng 9 ô.

```java
for (int value = 0; value <= maxValue; value++)
```

Duyệt `value` tăng dần đảm bảo kết quả được sắp xếp tăng dần.

```java
while (frequency[value] > 0)
```

Nếu một giá trị xuất hiện nhiều lần, phải ghi nó nhiều lần. Sau mỗi lần ghi:

```java
frequency[value]--;
```

`--` giảm biến đi 1.

#### Luồng logic

Với `{2, 0, 2, 1}`:

```text
frequency = {1, 1, 2}

value = 0: ghi 0 một lần
value = 1: ghi 1 một lần
value = 2: ghi 2 hai lần
```

Mảng kết quả là `{0, 1, 2, 2}`.

---

### Bài 15 — Cú pháp và logic merge sort

#### Cú pháp trong `mergeSort()`

```java
if (left >= right) {
    return;
}
```

`return;` trong hàm `void` kết thúc hàm mà không trả về dữ liệu. Điều kiện xử lý cả:

- Một phần tử: `left == right`.
- Mảng rỗng ban đầu: `left = 0`, `right = -1`.

```java
mergeSort(nums, left, mid);
mergeSort(nums, mid + 1, right);
```

Hai lời gọi lần lượt sắp xếp nửa trái và nửa phải. Java chạy xong lời gọi thứ nhất rồi mới chạy lời gọi thứ hai.

```java
merge(nums, left, mid, right);
```

Chỉ trộn sau khi cả hai nửa đã được sắp xếp.

#### Cú pháp trong `merge()`

```java
int[] temporary = new int[right - left + 1];
```

Số phần tử của đoạn đóng `[left, right]` là `right - left + 1`.

```java
while (first <= mid && second <= right)
```

Chỉ so sánh khi cả hai nửa vẫn còn phần tử.

```java
temporary[write++] = nums[first++];
```

Hậu tố `++` có nghĩa:

1. Dùng giá trị index hiện tại để đọc/ghi.
2. Sau đó mới tăng index lên 1.

Dòng trên tương đương:

```java
temporary[write] = nums[first];
write++;
first++;
```

```java
nums[left + i] = temporary[i];
```

Mảng tạm bắt đầu từ index 0, nhưng đoạn cần cập nhật trong `nums` bắt đầu từ `left`, nên phải dùng `left + i`.

#### Luồng logic

Với `{4, 1, 3, 2}`:

```text
Chia: {4, 1} và {3, 2}
Chia tiếp: {4}, {1}, {3}, {2}
Trộn: {4} + {1} → {1, 4}
Trộn: {3} + {2} → {2, 3}
Trộn: {1, 4} + {2, 3} → {1, 2, 3, 4}
```

Trong lần trộn cuối:

```text
so sánh 1 và 2 → lấy 1
so sánh 4 và 2 → lấy 2
so sánh 4 và 3 → lấy 3
nửa phải hết    → chép 4 còn lại
```

---

## Tổng kết các cú pháp thường gặp

| Cú pháp | Ý nghĩa |
|---|---|
| `int[] nums` | Biến tham chiếu đến mảng số nguyên |
| `nums.length` | Số phần tử của mảng |
| `nums[i]` | Phần tử tại index `i` |
| `==`, `!=` | Bằng, khác |
| `<`, `<=`, `>`, `>=` | Các phép so sánh |
| `&&` | AND logic, có short-circuit |
| `++`, `--` | Tăng hoặc giảm 1 |
| `+=` | Cộng rồi gán lại |
| `%` | Lấy phần dư |
| `return value` | Kết thúc hàm và trả về giá trị |
| `return;` | Kết thúc một hàm `void` |
| `new int[n]` | Tạo mảng `n` số nguyên, ban đầu đều bằng 0 |
| `static` | Gọi thành viên qua class, không cần object |
| `void` | Hàm không trả về giá trị |
| `boolean` | Kiểu `true` hoặc `false` |

## Tổng kết kỹ thuật

| Nhóm | Bài | Ý tưởng cần nhớ |
|---|---:|---|
| Duyệt và đếm | 1–4 | Mỗi phần tử được xử lý một lần; giá trị nhỏ có thể dùng làm index mảng đếm |
| Two pointers | 5–8 | Trái/phải hoặc đọc/ghi; thường đạt `O(n)` và `O(1)` bộ nhớ |
| Recursion | 9–10 | Base case phải dừng; lời gọi mới phải tiến gần base case |
| Binary search | 11–12 | Mảng phải sắp xếp; mỗi bước loại bỏ một nửa không gian tìm kiếm |
| Sorting | 13–15 | Insertion: chèn; counting: đếm; merge: chia rồi trộn |
