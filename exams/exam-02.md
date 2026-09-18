# Python Basic Algorithm Exam — 5 Exercises (Easy → Hard)

Same topic categories as v5 (math, string, list, binary search, recursion), but with different problems. Each exercise includes: problem statement, constraints, function signature, and assert-based test cases.

---

## Exercise 1 (Easy) — Prime Number Check [Math]

**Task:** Write a function that checks whether a non-negative integer `n` is a prime number.

**Constraints:** `0 <= n <= 10^7`. `0` and `1` are not prime.

```python
def is_prime(n: int) -> bool:
    pass


assert is_prime(2) == True
assert is_prime(1) == False
assert is_prime(0) == False
assert is_prime(17) == True
assert is_prime(18) == False
assert is_prime(97) == True
```

---

## Exercise 2 (Easy–Medium) — First Non-Repeating Character [String]

**Task:** Write a function that returns the first character in a string that does not repeat anywhere else in the string. Return `None` if every character repeats (or the string is empty).

**Constraints:** `0 <= len(s) <= 10^5`; string contains printable ASCII characters.

```python
def first_non_repeating(s: str):
    pass


assert first_non_repeating("swiss") == 'w'
assert first_non_repeating("aabbcc") is None
assert first_non_repeating("aabbc") == 'c'
assert first_non_repeating("") is None
assert first_non_repeating("x") == 'x'
```

---

## Exercise 3 (Medium) — Find the Missing Number [List]

**Task:** You're given a list containing `n` distinct integers taken from the range `0` to `n` (inclusive) — so exactly one number in that range is missing from the list. Find and return the missing number.

**Constraints:** `1 <= len(arr) <= 10^5`; all elements distinct and within `[0, n]` where `n = len(arr)`.

```python
def find_missing_number(arr: list) -> int:
    pass


assert find_missing_number([3, 0, 1]) == 2
assert find_missing_number([0, 1]) == 2
assert find_missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
assert find_missing_number([0]) == 1
assert find_missing_number([1]) == 0
```

---

## Exercise 4 (Medium–Hard) — Search in a Rotated Sorted Array [Binary Search]

**Task:** An array that was originally sorted in ascending order has been **rotated** at some unknown pivot (e.g. `[0,1,2,4,5,6,7]` becomes `[4,5,6,7,0,1,2]`). Given such an array and a target value, find the index of the target using **binary search in O(log n)** time. Return `-1` if not found.

**Constraints:** `1 <= len(arr) <= 10^5`; all elements are distinct.

```python
def search_rotated(arr: list, target: int) -> int:
    pass


assert search_rotated([4,5,6,7,0,1,2], 0) == 4
assert search_rotated([4,5,6,7,0,1,2], 3) == -1
assert search_rotated([1], 1) == 0
assert search_rotated([1], 0) == -1
assert search_rotated([5,1,3], 5) == 0
assert search_rotated([6,7,1,2,3,4,5], 3) == 4
```

---

## Exercise 5 (Hard) — Generate All Permutations [Recursion]

**Task:** Write a **recursive** function that generates all permutations of a list of distinct elements. For each position, pick each remaining element as the next one, then recursively permute the rest. Order of the output: for each index `i` in the original list order, `arr[i]` is fixed as the current prefix element, followed by the permutations of the remaining elements (in that same recursive order).

**Constraints:** `0 <= len(arr) <= 8` (so `len(arr)!` permutations stays manageable); elements are distinct.

```python
def permutations(arr: list) -> list:
    pass


assert permutations([]) == [[]]
assert permutations([1]) == [[1]]
assert permutations([1, 2]) == [[1, 2], [2, 1]]
assert permutations([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
```

---

## Reference Solutions

```python
# Exercise 1 — Prime Number Check (Math)
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


# Exercise 2 — First Non-Repeating Character (String)
from collections import Counter

def first_non_repeating(s):
    counts = Counter(s)
    for ch in s:
        if counts[ch] == 1:
            return ch
    return None


# Exercise 3 — Find the Missing Number (List)
def find_missing_number(arr):
    n = len(arr)
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(arr)


# Exercise 4 — Search in a Rotated Sorted Array (Binary Search)
def search_rotated(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[lo] <= arr[mid]:            # left half is sorted
            if arr[lo] <= target < arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:                               # right half is sorted
            if arr[mid] < target <= arr[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


# Exercise 5 — Generate All Permutations (Recursion)
def permutations(arr):
    if len(arr) <= 1:
        return [arr[:]]
    result = []
    for i in range(len(arr)):
        rest = arr[:i] + arr[i + 1:]
        for p in permutations(rest):
            result.append([arr[i]] + p)
    return result
```

---

## Grading Suggestion

| Exercise | Topic | Difficulty | Suggested Points |
|---|---|---|---|
| 1 — Prime Number Check | Math | Easy | 15 |
| 2 — First Non-Repeating Character | String | Easy–Medium | 20 |
| 3 — Find the Missing Number | List | Medium | 20 |
| 4 — Search in a Rotated Sorted Array | Binary Search | Medium–Hard | 20 |
| 5 — Generate All Permutations | Recursion | Hard | 25 |
| **Total** | | | **100** |