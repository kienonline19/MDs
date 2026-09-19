# Python Recursion Exercises — 10 Problems (Easy → Medium)

Each exercise includes: problem statement, constraints, function signature, and assert-based test cases you can copy directly.

---

## Exercise 1 (Easy) — Factorial

**Task:** Write a recursive function that computes `n!` (the factorial of a non-negative integer `n`).

**Constraints:** `0 <= n <= 20`.

```python
def factorial(n: int) -> int:
    pass


assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) == 120
assert factorial(10) == 3628800
```

---

## Exercise 2 (Easy) — Sum of Digits

**Task:** Write a recursive function that returns the sum of the digits of a non-negative integer `n`.

**Constraints:** `0 <= n <= 10^12`.

```python
def sum_of_digits(n: int) -> int:
    pass


assert sum_of_digits(0) == 0
assert sum_of_digits(9) == 9
assert sum_of_digits(12345) == 15
assert sum_of_digits(999) == 27
```

---

## Exercise 3 (Easy) — Power

**Task:** Write a recursive function that computes `x` raised to the power `n` (do not use `**` or `pow()`).

**Constraints:** `n >= 0` (integer exponent); `x` can be any real number.

```python
def power(x: float, n: int) -> float:
    pass


assert power(2, 10) == 1024
assert power(5, 0) == 1
assert power(3, 4) == 81
assert power(2, 1) == 2
assert power(1, 100) == 1
```

---

## Exercise 4 (Easy–Medium) — Reverse a String

**Task:** Write a recursive function that reverses a string (do not use slicing tricks like `s[::-1]` or a loop — build the reverse through recursive calls).

**Constraints:** `0 <= len(s) <= 1000`.

```python
def reverse_string(s: str) -> str:
    pass


assert reverse_string("hello") == "olleh"
assert reverse_string("") == ""
assert reverse_string("a") == "a"
assert reverse_string("racecar") == "racecar"
assert reverse_string("Python") == "nohtyP"
```

---

## Exercise 5 (Medium) — Greatest Common Divisor (Euclidean Algorithm)

**Task:** Write a recursive function that computes the greatest common divisor of two non-negative integers, using the Euclidean algorithm (`gcd(a, b) = gcd(b, a % b)`).

**Constraints:** `0 <= a, b`; not both zero.

```python
def gcd(a: int, b: int) -> int:
    pass


assert gcd(48, 18) == 6
assert gcd(17, 5) == 1
assert gcd(0, 5) == 5
assert gcd(100, 10) == 10
assert gcd(7, 7) == 7
```

---

## Exercise 6 (Medium) — Count Occurrences in a Nested List

**Task:** Write a recursive function that counts how many times `target` appears anywhere inside an arbitrarily nested list (the nesting depth is not known in advance).

**Constraints:** `0 <= len(nested_list) <= 10^4` total elements across all levels.

```python
def count_occurrences(nested_list: list, target) -> int:
    pass


assert count_occurrences([1, 2, [1, 3, [1, 1]], 4], 1) == 4
assert count_occurrences([], 5) == 0
assert count_occurrences([2, [3, [4]]], 5) == 0
assert count_occurrences([[1], [1], [1]], 1) == 3
```

---

## Exercise 7 (Medium) — Decimal to Binary

**Task:** Write a recursive function that converts a non-negative integer to its binary representation as a string (do not use `bin()` or any other built-in base-conversion function).

**Constraints:** `0 <= n <= 10^9`. Special case: `n = 0` should return `"0"` (not an empty string).

```python
def to_binary(n: int) -> str:
    pass


assert to_binary(0) == "0"
assert to_binary(5) == "101"
assert to_binary(10) == "1010"
assert to_binary(1) == "1"
assert to_binary(255) == "11111111"
```

---

## Exercise 8 (Medium) — Check If a List Is Sorted

**Task:** Write a recursive function that checks whether a list is sorted in non-decreasing order (do not use a loop, `sorted()`, or `all()`).

**Constraints:** `0 <= len(arr) <= 10^4`.

```python
def is_sorted(arr: list) -> bool:
    pass


assert is_sorted([1, 2, 3, 4]) == True
assert is_sorted([1, 3, 2]) == False
assert is_sorted([]) == True
assert is_sorted([5]) == True
assert is_sorted([1, 1, 2, 2]) == True
assert is_sorted([2, 1]) == False
```

---

## Exercise 9 (Medium) — Tower of Hanoi (List of Moves)

**Task:** Write a recursive function that solves the Tower of Hanoi puzzle for `n` disks and returns the full sequence of moves as a list of `(from_peg, to_peg)` tuples, in the order they must be performed. Default peg names are `'A'` (source), `'C'` (target), `'B'` (auxiliary).

**Constraints:** `0 <= n <= 15`. `n = 0` means no disks, so the move list is empty.

```python
def hanoi_moves(n: int, source: str = 'A', target: str = 'C', auxiliary: str = 'B') -> list:
    pass


assert hanoi_moves(1) == [('A', 'C')]
assert hanoi_moves(2) == [('A', 'B'), ('A', 'C'), ('B', 'C')]
assert hanoi_moves(3) == [('A', 'C'), ('A', 'B'), ('C', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('A', 'C')]
assert len(hanoi_moves(4)) == 15
assert hanoi_moves(0) == []
```

---

## Exercise 10 (Medium) — Subsets (Power Set)

**Task:** Write a recursive function that generates all subsets (the power set) of a list. Use the "include or exclude the first element" recursive strategy: `subsets(arr) = subsets(rest)` combined with `[first] + s for each s in subsets(rest)`.

**Constraints:** `0 <= len(arr) <= 15` (so `2^len(arr)` subsets stays manageable); elements are distinct.

```python
def subsets(arr: list) -> list:
    pass


assert subsets([]) == [[]]
assert subsets([1]) == [[], [1]]
assert subsets([1, 2]) == [[], [2], [1], [1, 2]]
assert subsets([1, 2, 3]) == [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
```

---

## Reference Solutions

```python
# Exercise 1 — Factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


# Exercise 2 — Sum of Digits
def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)


# Exercise 3 — Power
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)


# Exercise 4 — Reverse a String
def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]


# Exercise 5 — GCD (Euclidean Algorithm)
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# Exercise 6 — Count Occurrences in a Nested List
def count_occurrences(nested_list, target):
    count = 0
    for item in nested_list:
        if isinstance(item, list):
            count += count_occurrences(item, target)
        elif item == target:
            count += 1
    return count


# Exercise 7 — Decimal to Binary
def to_binary(n):
    if n == 0:
        return "0"

    def helper(n):
        if n == 0:
            return ""
        return helper(n // 2) + str(n % 2)

    return helper(n)


# Exercise 8 — Check If a List Is Sorted
def is_sorted(arr):
    if len(arr) <= 1:
        return True
    if arr[0] > arr[1]:
        return False
    return is_sorted(arr[1:])


# Exercise 9 — Tower of Hanoi (List of Moves)
def hanoi_moves(n, source='A', target='C', auxiliary='B'):
    if n == 0:
        return []
    moves = hanoi_moves(n - 1, source, auxiliary, target)
    moves.append((source, target))
    moves += hanoi_moves(n - 1, auxiliary, target, source)
    return moves


# Exercise 10 — Subsets (Power Set)
def subsets(arr):
    if not arr:
        return [[]]
    first, rest = arr[0], arr[1:]
    without_first = subsets(rest)
    with_first = [[first] + s for s in without_first]
    return without_first + with_first
```

---

## Grading Suggestion

| Exercise | Difficulty | Suggested Points |
|---|---|---|
| 1 — Factorial | Easy | 8 |
| 2 — Sum of Digits | Easy | 8 |
| 3 — Power | Easy | 9 |
| 4 — Reverse a String | Easy–Medium | 10 |
| 5 — GCD | Medium | 10 |
| 6 — Count Occurrences in Nested List | Medium | 11 |
| 7 — Decimal to Binary | Medium | 11 |
| 8 — Is Sorted | Medium | 11 |
| 9 — Tower of Hanoi | Medium | 11 |
| 10 — Subsets (Power Set) | Medium | 11 |
| **Total** | | **100** |