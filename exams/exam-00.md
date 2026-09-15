# Python Basic Algorithm Exam — 5 Exercises (Easy → Hard) — v5

Each exercise includes: problem statement, function signature, and input/output test cases.

---

## Exercise 1 (Easy) — Sum of Multiples

**Task:** Write a function that returns the sum of all natural numbers below `n` that are multiples of 3 or 5.

```python
def sum_multiples(n: int) -> int:
    pass
```

**Test Cases:**

| Input | Output |
|---|---|
| `n=10` | `23` |
| `n=15` | `45` |
| `n=20` | `78` |
| `n=1` | `0` |
| `n=1000` | `233168` |

---

## Exercise 2 (Easy–Medium) — Can Form Palindrome

**Task:** Write a function that checks whether the characters of a given string **can be rearranged** to form a palindrome (not just whether it already is one). Ignore case and spaces.

```python
def can_form_palindrome(s: str) -> bool:
    pass
```

**Test Cases:**

| Input | Output |
|---|---|
| `"civic"` | `True` |
| `"ivicc"` | `True` |
| `"hello"` | `False` |
| `"aabbcc"` | `True` |
| `"aabbc"` | `True` |
| `"aabbcd"` | `False` |
| `"A man a plan a canal Panama"` | `True` |

---

## Exercise 3 (Medium) — Second Largest Number

**Task:** Write a function that finds the second largest distinct number in a list. If it doesn't exist, return `None`.

```python
def second_largest(numbers: list):
    pass
```

**Test Cases:**

| Input | Output |
|---|---|
| `[10, 5, 8, 20, 3]` | `10` |
| `[5, 5, 5]` | `None` |
| `[1]` | `None` |
| `[4, 1, 7, 7, 2]` | `4` |

---

## Exercise 4 (Medium–Hard) — First and Last Position in Sorted Array

**Task:** Given a **sorted** list that may contain duplicates, find the first and last index of a target value using binary search (not linear scan). Return `(-1, -1)` if the target is not found. Must run in O(log n) time.

```python
def search_range(arr: list, target: int) -> tuple:
    pass
```

**Test Cases:**

| Input | Output |
|---|---|
| `arr=[5,7,7,8,8,10], target=8` | `(3, 4)` |
| `arr=[5,7,7,8,8,10], target=6` | `(-1, -1)` |
| `arr=[], target=0` | `(-1, -1)` |
| `arr=[1,1,1,1], target=1` | `(0, 3)` |
| `arr=[1,2,3], target=3` | `(2, 2)` |

---

## Exercise 5 (Hard) — Flatten a Nested List (Recursive)

**Task:** Write a **recursive** function that flattens an arbitrarily nested list of integers into a single flat list, preserving left-to-right order. The nesting depth is not known in advance (could be several levels deep), so the solution must handle arbitrary depth — no fixed number of loops.

```python
def flatten(nested_list: list) -> list:
    pass
```

**Test Cases:**

| Input | Output |
|---|---|
| `[1, [2, 3], [4, [5, 6]], 7]` | `[1, 2, 3, 4, 5, 6, 7]` |
| `[[1, 2], [3, 4]]` | `[1, 2, 3, 4]` |
| `[]` | `[]` |
| `[1, [2, [3, [4, [5]]]]]` | `[1, 2, 3, 4, 5]` |
| `[[], [1], [], [2, []]]` | `[1, 2]` |

---

## Answer Key (Reference Solutions)

```python
# Exercise 1
def sum_multiples(n):
    return sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0)

# Exercise 2
from collections import Counter

def can_form_palindrome(s):
    cleaned = s.lower().replace(" ", "")
    counts = Counter(cleaned)
    odd_count = sum(1 for c in counts.values() if c % 2 != 0)
    return odd_count <= 1

# Exercise 3
def second_largest(numbers):
    distinct = sorted(set(numbers), reverse=True)
    return distinct[1] if len(distinct) > 1 else None

# Exercise 4
def search_range(arr, target):
    def find_bound(is_first):
        lo, hi = 0, len(arr) - 1
        result = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] == target:
                result = mid
                if is_first:
                    hi = mid - 1
                else:
                    lo = mid + 1
            elif arr[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return result
    return (find_bound(True), find_bound(False))

# Exercise 5 — Flatten Nested List
def flatten(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))   # recursive call on the sub-list
        else:
            result.append(item)            # base case: not a list, keep as-is
    return result
```

**How Exercise 5's recursion works:** for each element, if it's itself a list, `flatten` calls itself on that sub-list and merges the result in; if it's a plain value, that's the base case and it gets appended directly. The recursion naturally handles any depth of nesting without the function needing to know how deep it goes in advance.

---

## Grading Suggestion

| Exercise | Difficulty | Suggested Points |
|---|---|---|
| 1 | Easy | 15 |
| 2 | Easy–Medium | 20 |
| 3 | Medium | 20 |
| 4 | Medium–Hard | 20 |
| 5 | Hard (recursive) | 25 |
| **Total** | | **100** |