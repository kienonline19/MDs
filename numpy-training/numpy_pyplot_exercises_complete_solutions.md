# NumPy and Pyplot Exercises - Complete Solutions

This guide solves all 26 exercises from `intro_exercises(2).pdf`.

General assumptions from the prompt:

- “Array” means a NumPy `ndarray`.
- When no data type is specified, NumPy's default floating-point type is used.
- Argument validation is intentionally omitted unless it helps explain an edge case.
- Slicing and vectorized NumPy operations are preferred over Python loops.
- The examples use modern NumPy and `np.random.default_rng()` where appropriate.

```python
import math
import random
import time

import matplotlib.pyplot as plt
import numpy as np
```

---

## Exercise 1 - NumPy integer types

### Requirements: input -> output

1. Input `100` -> one signed 16-bit NumPy scalar.
2. Input `100` -> one unsigned 16-bit NumPy scalar.
3. Compute and verify each type's minimum and maximum.
4. Reach each boundary, cross it, and observe wraparound.
5. Mix signed, unsigned, 16-bit, 64-bit, and Python integers.
6. Observe both the result value and result type.
7. Infer NumPy's type-promotion principle.

### Logic

- A signed 16-bit integer has range `-2**15` through `2**15 - 1`.
- An unsigned 16-bit integer has range `0` through `2**16 - 1`.
- Fixed-width integer arithmetic is modular: after the largest bit pattern, it cycles to the smallest.
- NumPy normally selects a common result type. A Python scalar is treated specially in modern NumPy and must fit the NumPy type involved.

```python
def show_operation(label, operation):
    """Execute a zero-argument function and show its result and type."""
    try:
        result = operation()
        print(f"{label}: value={result!r}, dtype={result.dtype}")
    except (OverflowError, TypeError) as error:
        print(f"{label}: {type(error).__name__}: {error}")


# Requirement 1: signed 16-bit value.
signed = np.int16(100)

# Requirement 2: unsigned 16-bit value.
unsigned = np.uint16(100)

# Requirement 3: manually calculate and then verify the ranges.
int16_min, int16_max = -(2**15), 2**15 - 1
uint16_min, uint16_max = 0, 2**16 - 1

assert (int16_min, int16_max) == (
    np.iinfo(signed.dtype).min,
    np.iinfo(signed.dtype).max,
)
assert (uint16_min, uint16_max) == (
    np.iinfo(unsigned.dtype).min,
    np.iinfo(unsigned.dtype).max,
)

# Requirement 4: reach and cross all boundaries.
print(np.int16(32766) + np.int16(1))    # 32767: reach maximum
print(np.int16(32767) + np.int16(1))    # -32768: cross maximum
print(np.int16(-32767) - np.int16(1))   # -32768: reach minimum
print(np.int16(-32768) - np.int16(1))   # 32767: cross minimum

print(np.uint16(65534) + np.uint16(1))  # 65535: reach maximum
print(np.uint16(65535) + np.uint16(1))  # 0: cross maximum
print(np.uint16(1) - np.uint16(1))      # 0: reach minimum
print(np.uint16(0) - np.uint16(1))      # 65535: cross minimum

# Requirements 5-6: mix types; display value and dtype.
show_operation("int16 + uint16", lambda: signed + unsigned)             # int32
show_operation("int16 + int64", lambda: signed + np.int64(100))        # int64
show_operation("uint16 + uint64", lambda: unsigned + np.uint64(100))   # uint64
show_operation("int64 + uint64", lambda: np.int64(100) + np.uint64(100))
show_operation("int16 + small Python int", lambda: signed + 1)
show_operation("int16 + large Python int", lambda: signed + 100_000)
show_operation("uint64 + huge Python int", lambda: np.uint64(1) + 10**100)

# Requirement 7: ask NumPy for the common result types.
print(np.result_type(np.int16, np.uint16))  # int32
print(np.result_type(np.int64, np.uint64))  # float64
```

`np.iinfo(dtype)` reports an integer type's limits. `np.result_type(...)` predicts type promotion. `int64 + uint64` becomes `float64` because no built-in NumPy integer type contains the complete ranges of both. Boundary tests may produce expected overflow warnings.

---

## Exercise 2 - NumPy array creation basics (I)

### Requirements: input -> output

- Integer list -> one-dimensional integer array and its `dtype`.
- Float list -> floating array and its `dtype`.
- Mixed integer/float list -> common floating type.
- Integer list with explicit float `dtype` -> floating array.
- Floats forced to `bool` -> `False` for zero and `True` for nonzero values.
- Strings mixed with numbers -> a common string type unless `object` is requested.
- Sets/dictionaries -> normally an `object` array.
- Preserve every element's original Python type -> explicitly use `dtype=object`.
- Empty list with no type -> empty `float64` array by default.

```python
# Requirement 1: integer list.
integers = [1, 2, 3]
a_int = np.array(integers)
print(a_int, a_int.dtype)

# Requirement 2: floating-point list.
floats = [1.0, 2.5, 3.0]
a_float = np.array(floats)
print(a_float, a_float.dtype)

# Requirement 3: mixed numeric values are converted to a common type.
mixed_numbers = np.array([1, 2.0, 3])
print(mixed_numbers, mixed_numbers.dtype)  # usually float64

# Requirement 4: force floating-point storage for integer input.
forced_float = np.array([1, 2, 3], dtype=float)
print(forced_float, forced_float.dtype)

# Requirement 5: force floats to bool; zero is False, nonzero is True.
forced_bool = np.array([0.0, 1.5, -2.0], dtype=bool)
print(forced_bool)  # [False, True, True]

# Requirement 6: strings cause values to be converted to strings.
with_strings = np.array([1, 2.5, "three"])
print(with_strings, with_strings.dtype)
print(type(with_strings[0]))
print(isinstance(with_strings[0], str))  # True for np.str_ too

# Requirement 7: arbitrary objects require object storage.
with_objects = np.array([{1, 2}, {"name": "Ada"}], dtype=object)
print(with_objects, with_objects.dtype)

# Requirement 8: prevent implicit conversion of mixed values.
preserved = np.array([1, 2.0, 3], dtype=object)
print([type(value) for value in preserved])

# Requirement 9: empty input defaults to float64.
empty = np.array([])
print(empty, empty.dtype)
```

`np.array(data, dtype=...)` creates an array and optionally forces its element type. An ordinary homogeneous NumPy array has one `dtype`; only an `object` array can retain unrelated Python object types.

---

## Exercise 3 - NumPy array creation basics (II)

### Requirements and logic

Input `n` first produces one-dimensional arrays of `n` ones using several data types. It then produces an `n x n` integer matrix and observes multiplication by an integer and a float.

```python
def one_arrays(n):
    """Create length-n arrays of ones using the requested element types."""
    # Requirement 1: default floating-point ones.
    floats = np.ones(n)

    # Requirement 2: signed 64-bit integer ones.
    ints64 = np.ones(n, dtype=np.int64)

    # Requirement 3: signed 32-bit integer ones.
    ints32 = np.ones(n, dtype=np.int32)

    # Requirement 4: boolean ones; numeric 1 converts to True.
    booleans = np.ones(n, dtype=bool)

    # Requirement 5: string ones; each 1 is converted to "1".
    strings = np.ones(n, dtype=str)

    # Requirement 6: inspect array dtype and first-element type.
    for array in (floats, ints64, ints32, booleans, strings):
        first_type = type(array[0]) if n else None
        print(array, array.dtype, first_type)

    return floats, ints64, ints32, booleans, strings


def one_matrix(n):
    """Create an n x n integer matrix and demonstrate type promotion."""
    # Requirement 7: n x n integer matrix of ones.
    matrix = np.ones((n, n), dtype=np.int32)

    # Requirement 8: integer multiplication normally preserves integer dtype.
    integer_product = matrix * 3

    # Requirement 9: float multiplication promotes the result to floating point.
    float_product = matrix * 3.5

    print(integer_product.dtype, float_product.dtype)
    return matrix, integer_product, float_product
```

`np.ones(shape, dtype=...)` creates an array filled with values equivalent to `1`. A tuple such as `(n, n)` specifies a two-dimensional shape.

---

## Exercise 4 - Some broadcasting basics

### Input -> output

Input `n` -> a one-dimensional integer array of length `n` filled with `-1`.

```python
def minus_ones_v1(n):
    # Requirement: use the dedicated full-array constructor.
    return np.full(n, -1, dtype=int)


def minus_ones_v2(n):
    # Requirement: broadcast multiplication across an array of ones.
    return -np.ones(n, dtype=int)


def minus_ones_v3(n):
    # Requirement: subtract one from every broadcasted zero.
    return np.zeros(n, dtype=int) - 1


def minus_ones_v4(n):
    # Requirement: repeat the scalar value n times.
    return np.repeat(-1, n)
```

Broadcasting applies a scalar operation such as `* -1` or `- 1` to every array element without a Python loop.

---

## Exercise 5 - Reading out array chunks

### Input -> output and logic

Input is a list of length `n`. Convert it to an array, split at `n // 2`, put the middle value in the second half when `n` is odd, join the halves, and return an equal but independent array.

```python
def split_and_join(values):
    """Split an array into two views, rejoin them, verify, and return the copy."""
    # Requirement 1: convert the input list to a one-dimensional array.
    original = np.array(values)
    middle = len(original) // 2

    # Requirement 2: first half in one slicing expression.
    first = original[:middle]

    # Requirement 3: second half, including the middle item when length is odd.
    second = original[middle:]

    # Requirement 4: '+' performs elementwise addition, not concatenation.
    # first + second may fail for unequal shapes or add values for equal shapes.

    # Requirement 5: concatenate the halves horizontally.
    joined = np.hstack((first, second))

    # Requirement 6: verify elementwise equality with an assertion.
    assert (joined == original).all()
    assert np.array_equal(joined, original)

    # Requirement 7: joined is equal, but it is not the same object.
    assert joined is not original

    # Requirement 8: slices are views whose .base refers to original storage.
    print(first.base is original, second.base is original)

    return joined


# View experiment required by the prompt.
a = np.array([1, 2, 3, 4, 5])
first_half = a[: len(a) // 2]
first_half[0] = 99
print(a)                    # original changed
print(first_half.base is a) # True
```

`np.hstack()` creates a new concatenated array. `==` returns an array of booleans, so `.all()` reduces it to one boolean. `np.array_equal(a, b)` directly checks shape and element equality. `is` checks object identity, not value equality.

---

## Exercise 6 - Slicing in strides (I)

```python
def split_even_odd_indices(values):
    """Return views containing values at even and odd indices."""
    # Requirement 1: create the original one-dimensional array.
    original = np.array(values)

    # Requirement 2: all even indices in one slicing expression.
    even_indices = original[::2]

    # Requirement 3: all odd indices in one slicing expression.
    odd_indices = original[1::2]

    # Requirement 4: demonstrate that both results are views.
    print(even_indices.base is original, odd_indices.base is original)
    return original, even_indices, odd_indices


original, evens, odds = split_even_odd_indices([10, 20, 30, 40, 50])
evens[0] = 999
print(original)  # original[0] also becomes 999
```

The slice syntax is `start:stop:step`. A step of `2` selects every second item. Basic slicing returns views, so mutations share memory.

---

## Exercise 7 - Slicing in strides (II)

### Input -> output

Input is a nonempty list. Outputs include the reversed whole array, reversed halves, reversed even/odd-index elements, and a double-reversed view.

```python
def advanced_slices(values):
    """Produce every reversed slice requested in Exercise 7."""
    # Requirement 1: create the source array.
    a = np.array(values)
    n = len(a)
    middle = n // 2

    # Point 1: reverse the entire array.
    reversed_all = a[::-1]

    # Point 2: easy two-step versions of both reversed halves.
    first_half_reversed_2_steps = a[:middle][::-1]
    second_half_reversed_2_steps = a[middle:][::-1]

    # Point 2: robust direct expressions; special case handles n == 1.
    first_half_reversed = a[middle - 1::-1] if middle else a[:0]
    second_half_reversed = a[:middle - 1:-1] if middle else a[::-1]

    assert np.array_equal(first_half_reversed, first_half_reversed_2_steps)
    assert np.array_equal(second_half_reversed, second_half_reversed_2_steps)

    # Point 3: easy two-step versions.
    even_reversed_2_steps = a[::2][::-1]
    odd_reversed_2_steps = a[1::2][::-1]

    # Point 3: one slice each, with no if statement.
    # Largest even index is selected by -1 for odd n and -2 for even n.
    even_reversed = a[-2 + n % 2::-2]

    # Largest odd index is selected by -1 for even n and -2 for odd n.
    odd_reversed = a[-1 - n % 2::-2]

    assert np.array_equal(even_reversed, even_reversed_2_steps)
    assert np.array_equal(odd_reversed, odd_reversed_2_steps)

    # Point 4: reverse the reversed view.
    double_reversed = reversed_all[::-1]
    assert np.array_equal(double_reversed, a)
    assert double_reversed is not a

    # It is still a view: mutation changes the original.
    old_value = a[0]
    double_reversed[0] = old_value + 1
    assert a[0] == old_value + 1

    # a[:] has the same essential properties: equal, not identical, and a view.
    equivalent_view = a[:]

    # Requirement: inspect .base for all slicing results.
    for result in (
        reversed_all,
        first_half_reversed,
        second_half_reversed,
        even_reversed,
        odd_reversed,
        double_reversed,
        equivalent_view,
    ):
        print(result, "base:", result.base)

    return {
        "reversed_all": reversed_all,
        "first_half_reversed": first_half_reversed,
        "second_half_reversed": second_half_reversed,
        "even_reversed": even_reversed,
        "odd_reversed": odd_reversed,
        "double_reversed": double_reversed,
    }
```

A negative slice step walks backward. The stop position is excluded, and negative indices make edge cases subtle. `.base` identifies the underlying object/storage owner; `np.shares_memory(x, a)` is an even clearer sharing check.

---

## Exercise 8 - Indexing with lists (I)

```python
def first_middle_last(values):
    """Return a copy containing the first, middle, and last elements."""
    # Requirement 1: create an array from an odd-length, nonempty list.
    original = np.array(values)
    n = len(original)

    # Requirement 2: list-based advanced indexing with three positions.
    selected = original[[0, n // 2, n - 1]]

    # Requirement 3: verify advanced indexing creates a copy, not a view.
    before = original.copy()
    probe = selected.copy()
    probe[0] = probe[0] + 1
    assert np.array_equal(original, before)
    assert not np.shares_memory(selected, original)

    return selected


print(first_middle_last([4, 6, 1, 2, 0, 7, 9]))
print(first_middle_last([5]))  # initially [5, 5, 5]

# Repetition and an output longer than the input are valid.
a = np.array([10, 20, 30])
print(a[[2, 0, 1, 0, 0, 1]])
```

Indexing with a list or integer array is called advanced indexing. It creates a copy, unlike ordinary slicing.

---

## Exercise 9 - Indexing with lists (II)

```python
def random_selection(values, m, rng=None):
    """Randomly select m values with replacement from a nonempty list."""
    # Requirement 1: create the original array.
    original = np.array(values)
    n = len(original)

    # Requirement 2: create/reuse a modern random-number generator.
    rng = np.random.default_rng() if rng is None else rng

    # Requirement 3: make m random indices in [0, n).
    indices = rng.integers(0, n, size=m)

    # Requirement 4: use the integer array for advanced indexing.
    result = original[indices]

    # Requirement 5: output length must be m for n<m, n==m, and n>m.
    assert len(result) == m
    return result


print(random_selection([10, 20], 5))       # n < m
print(random_selection([10, 20, 30], 3))   # n == m
print(random_selection([10, 20, 30, 40], 2)) # n > m
```

`rng.integers(low, high, size=m)` includes `low` and excludes `high`. Repeated indices are allowed, so sampling is with replacement. The older equivalent is `np.random.randint(0, n, size=m)`.

---

## Exercise 10 - Indexing with masks (I)

The prompt says “non-negative” but uses `a > 0` and an example containing only positive values. Mathematically, non-negative means `>= 0`. Both interpretations are shown.

```python
def select_non_negative(values):
    """Return an independent array containing values greater than or equal to 0."""
    # Requirement 1: create a one-dimensional array.
    original = np.array(values)

    # Requirement 2: compare the complete array with zero.
    positive_mask = original > 0
    print(positive_mask)

    # Requirement 3: true non-negative selection in one indexing expression.
    result = original[original >= 0]

    # Requirement 4: boolean advanced indexing creates a copy.
    assert not np.shares_memory(result, original)
    return result


def select_strictly_positive(values):
    """Match the prompt's a > 0 wording and its positive-only example."""
    a = np.array(values)
    return a[a > 0]


values = [3, -1, -2, 0, 5, 6, -3, 8]
print(select_non_negative(values))    # includes 0
print(select_strictly_positive(values)) # excludes 0
```

A vectorized comparison creates a Boolean mask with one Boolean per input element. `a[mask]` keeps only positions where the mask is `True` and returns a copy.

---

## Exercise 11 - Indexing with masks (II)

```python
def probabilistic_selection(values, r, rng=None):
    """Independently retain each input value with probability r."""
    # Requirement 1: convert the list to an array.
    original = np.array(values)
    n = len(original)
    rng = np.random.default_rng() if rng is None else rng

    # Requirement 2: generate n values in [0.0, 1.0).
    random_values = rng.random(n)

    # Requirement 3: make a Boolean mask by comparing each random value with r.
    mask = random_values < r

    # Requirement 4: use the mask to select elements.
    result = original[mask]

    # Requirement 5: summing Booleans counts True values.
    assert len(result) == mask.sum()
    return result


def average_selected_length(values, r, iterations=1000, seed=None):
    """Estimate the expected selected length over repeated experiments."""
    # Requirement 6: call the first function repeatedly with the same inputs.
    rng = np.random.default_rng(seed)
    lengths = np.array([
        len(probabilistic_selection(values, r, rng))
        for _ in range(iterations)
    ])

    # Requirement 7: compare measured average with theoretical n*r.
    measured = lengths.mean()
    expected = len(values) * r
    print("Measured average:", measured)
    print("Expected average:", expected)
    return measured, expected


# Requirement 8: boundary probabilities.
data = np.array([1, 2, 3, 4])
assert len(probabilistic_selection(data, 0)) == 0
all_selected = probabilistic_selection(data, 1)
assert np.array_equal(all_selected, data)
assert all_selected is not data
assert not np.shares_memory(all_selected, data)

average_selected_length(list(range(7)), 0.49, iterations=10_000, seed=1)
```

`rng.random(n)` generates `n` uniform values from `[0, 1)`. Since `P(random_value < r) = r`, the expected output length is `n * r`, even when that value is not an integer.

---

## Exercise 12 - Automatic conversions

### Logic

An array has one fixed `dtype`. Assignment converts the incoming value to that existing type; it does not normally change the array's type. Modern NumPy often raises `OverflowError` rather than silently accepting an out-of-range Python integer.

```python
def try_assignment(array, index, value):
    """Attempt an assignment and report either the converted array or its error."""
    try:
        array[index] = value
        print(array, array.dtype)
    except (OverflowError, ValueError, TypeError) as error:
        print(type(error).__name__, error)


# Requirement 1: assign integers into a floating-point array.
floats = np.array([0.0, 0.0, 0.0])
try_assignment(floats.copy(), 0, 7)       # becomes 7.0
try_assignment(floats.copy(), 0, 10**100) # rounded float if representable

# A float64 maximum is roughly 1.7976931348623157e308.
# Larger floating values become infinity or may raise during conversion.
print(np.finfo(np.float64).max)
try_assignment(floats.copy(), 0, 10**400)

# Requirement 2: assign floats into an integer array; fractional part truncates.
integers = np.array([0, 0, 0], dtype=np.int64)
try_assignment(integers.copy(), 0, 3.9)   # usually 3
try_assignment(integers.copy(), 0, -3.9)  # usually -3

# Requirement 3: out-of-range value into int16.
small_integers = np.zeros(3, dtype=np.int16)
try_assignment(small_integers.copy(), 0, 40_000)

# Requirement 4: infinity and NaN cannot be represented as ordinary integers.
try_assignment(integers.copy(), 0, np.inf)
try_assignment(integers.copy(), 0, np.nan)

# Requirement 5: experiment with bool conversion.
booleans = np.zeros(4, dtype=bool)
try_assignment(booleans.copy(), 0, 0)      # False
try_assignment(booleans.copy(), 0, -2.5)   # True

numeric = np.zeros(3, dtype=np.int16)
try_assignment(numeric.copy(), 0, True)    # 1
try_assignment(numeric.copy(), 0, False)   # 0
```

`np.finfo(np.float64).max` reports the largest finite `float64`. Integer-to-float conversions can lose precision well before infinity because float64 has only about 15-17 significant decimal digits.

---

## Exercise 13 - Assigning with slices

```python
def reverse_each_half(values):
    """Reverse each half in place; an odd middle element belongs to half two."""
    # Requirement 1: convert the list and find the split position.
    a = np.array(values)
    middle = len(a) // 2

    # Requirement 2: read, reverse, and assign the first half.
    a[:middle] = a[:middle][::-1]

    # Requirement 3: read, reverse, and assign the second half.
    a[middle:] = a[middle:][::-1]
    return a


def reverse_each_half_assignment_direction(values):
    """Equivalent version: reverse the destination slices instead."""
    a = np.array(values)
    middle = len(a) // 2

    # Requirement 4: source is normal; destination indexing is reversed.
    a[:middle][::-1] = a[:middle]
    a[middle:][::-1] = a[middle:]
    return a


def reverse_each_half_hstack(values):
    """Equivalent version that intentionally creates a temporary array."""
    a = np.array(values)
    middle = len(a) // 2

    # Requirement 5: hstack allocates a new combined array.
    temporary = np.hstack((a[:middle][::-1], a[middle:][::-1]))

    # Requirement 6: overwrite a's contents without rebinding variable a.
    a[:] = temporary
    return a


assert np.array_equal(reverse_each_half([3, 5, 6, 7, 8, 9]), [6, 5, 3, 9, 8, 7])
assert np.array_equal(reverse_each_half([3, 5, 6, 7, 8]), [5, 3, 8, 7, 6])
```

`a = new_array` makes the variable refer to another object. `a[:] = new_array` preserves the existing array and overwrites its elements, so other views of `a` still refer to the modified storage. Slice-assignment source and destination sizes must match unless a scalar is broadcast.

---

## Exercise 14 - Assigning with lists

```python
def assign_first_middle_last(values):
    """Assign 0, 1, and 2 to first, middle, and last positions."""
    a = np.array(values)
    n = len(a)

    # Requirement 1: perform all three assignments in one line.
    a[[0, n // 2, n - 1]] = [0, 1, 2]

    # Requirement 2: if n == 1, repeated writes occur and the final 2 wins.
    return a


def assign_middle_with_precedence(values):
    """Reorder repeated assignments so the middle value is written last."""
    a = np.array(values)
    n = len(a)

    # Requirement 3: no if; middle assignment is last and therefore wins for n==1.
    a[[0, n - 1, n // 2]] = [0, 2, 1]
    return a


assert np.array_equal(assign_first_middle_last([9, 9, 9, 9, 9]), [0, 9, 1, 9, 2])
assert np.array_equal(assign_first_middle_last([9]), [2])
assert np.array_equal(assign_middle_with_precedence([9]), [1])
```

When advanced-assignment indices repeat, assignments are processed in order and the last value for that position wins.

---

## Exercise 15 - Assigning with masks

```python
def make_all_positive(values):
    """Flip negative values in place and verify that no negatives remain."""
    a = np.array(values)

    # Requirement 1: construct the negative-value mask.
    negative = a < 0

    # Requirement 2: use masks for both reading and assignment.
    a[negative] = -a[negative]

    # Requirement 3: verify every value is non-negative using np.all.
    assert np.all(a >= 0)

    # Requirement 4: equivalent verification using np.any.
    assert not np.any(a < 0)
    return a
```

`np.all(condition)` is true only when every Boolean is true. `np.any(condition)` is true when at least one Boolean is true. This function behaves like integer/float absolute value; beware that the minimum fixed-width signed integer can overflow when negated.

---

## Exercise 16 - Broadcasted assignment (I)

```python
def alternating_v1(n):
    """Start with zeros and broadcast 1 into odd positions."""
    # Requirement 1: default float array.
    a = np.zeros(n)
    # Requirement 2: scalar-to-slice broadcasting.
    a[1::2] = 1
    return a


def alternating_v2(n):
    """Start with ones and broadcast 0 into even positions."""
    a = np.ones(n)
    a[::2] = 0
    return a
```

Assigning one scalar to a slice broadcasts the scalar across every selected position.

---

## Exercise 17 - Broadcasted assignment (II)

```python
def first_half_ones_float(n):
    """Return float ones in the first half and zeros in the second half."""
    # Requirement 1: create ones.
    a = np.ones(n)
    # Requirement 2: n//2 puts the odd middle element in the zero half.
    a[n // 2:] = 0
    return a


def first_half_ones_integer(n):
    """Integer variant."""
    a = np.ones(n, dtype=int)
    a[n // 2:] = 0
    return a


def first_half_ones_bool(n):
    """Boolean variant: True corresponds to 1; False corresponds to 0."""
    a = np.ones(n, dtype=bool)
    a[n // 2:] = False
    return a
```

For odd `n`, `n // 2` is the middle index, so assigning zeros from that index includes the middle element.

---

## Exercise 18 - Array creation, broadcasted functions, and plotting

```python
def plot_sine_cosine(n, filename="sine_cosine.png"):
    """Create requested angle arrays, plot sine/cosine, and save a PNG."""
    # Requirement 1: n regular points including 0 but excluding 2*pi.
    excluded_endpoint = np.linspace(0.0, 2 * np.pi, n, endpoint=False)

    # Requirement 2: n regular points including both 0 and 2*pi.
    included_endpoint = np.linspace(0.0, 2 * np.pi, n, endpoint=True)

    # Requirement 3: vectorized sine and cosine, one line each.
    sine = np.sin(included_endpoint)
    cosine = np.cos(included_endpoint)

    # Requirement 4: plot both curves on the same axes.
    plt.clf()
    plt.plot(included_endpoint, sine, label="sin")
    plt.plot(included_endpoint, cosine, label="cos")

    # Requirement 5: label the x-axis.
    plt.xlabel("radians")

    # Advanced requirement: label curves with a legend.
    plt.legend()

    # Advanced requirement: save the figure as PNG.
    plt.savefig(filename, dpi=150, bbox_inches="tight")
    return excluded_endpoint, included_endpoint
```

`np.linspace(start, stop, count, endpoint=...)` creates an exact requested number of regularly spaced values. `np.sin` and `np.cos` operate elementwise. `label=` records curve names and `plt.legend()` displays them. `plt.savefig()` writes the current figure.

---

## Exercise 19 - Normal random numbers

### Input -> output

Generate one million samples from a normal distribution with mean `0` and variance `1`, once using Python and once using vectorized NumPy; then compare execution time.

```python
def compare_normal_generation(count=1_000_000, seed=1):
    """Generate standard-normal samples by Python and NumPy and time both."""
    # Requirement 1: Python random module plus comprehension.
    random.seed(seed)
    start = time.time()
    python_values = [random.gauss(0.0, 1.0) for _ in range(count)]
    python_seconds = time.time() - start

    # Requirement 2: NumPy generation in one line, without a comprehension.
    rng = np.random.default_rng(seed)
    start = time.time()
    numpy_values = rng.normal(loc=0.0, scale=1.0, size=count)
    numpy_seconds = time.time() - start

    # Requirement 3: report the performance difference.
    print("Python seconds:", python_seconds)
    print("NumPy seconds:", numpy_seconds)
    print("Speed ratio:", python_seconds / numpy_seconds)
    return python_values, numpy_values
```

The normal distribution's `scale` is its standard deviation, not variance. Variance `1` therefore means `scale=1`. NumPy is faster because generation occurs in compiled vectorized code and produces compact array storage.

---

## Exercise 20 - Two-dimensional random arrays and statistics

```python
def demonstrate_even_subtable(rng=None):
    """Create one table, extract its even-indexed view, and show memory sharing."""
    rng = np.random.default_rng() if rng is None else rng

    # Requirement 1: 10 x 20 standard-normal array.
    table = rng.normal(0.0, 1.0, size=(10, 20))

    # Requirement 2: compute its mean in one line.
    full_mean = table.mean()

    # Requirement 3: select rows and columns whose indices are both even.
    subtable = table[::2, ::2]

    # Requirement 4: slicing produces a view.
    assert np.shares_memory(table, subtable)
    old = table[0, 0]
    subtable[0, 0] = old + 1
    assert table[0, 0] == old + 1

    # Requirement 5: .copy() obtains the opposite behavior.
    independent = table[::2, ::2].copy()
    assert not np.shares_memory(table, independent)

    # Requirement 6: mean of the subtable.
    subtable_mean = subtable.mean()
    return full_mean, subtable_mean


def plot_mean_histograms(iterations=1000, bins=40, seed=None):
    """Collect repeated means and compare their histogram distributions."""
    rng = np.random.default_rng(seed)

    # Requirement 7: collect both kinds of means in separate arrays.
    full_means = np.empty(iterations)
    subtable_means = np.empty(iterations)

    for i in range(iterations):
        table = rng.normal(0.0, 1.0, size=(10, 20))
        full_means[i] = table.mean()
        subtable_means[i] = table[::2, ::2].mean()

    # Requirement 8: clear previous plots.
    plt.clf()

    # Requirement 9: line-style, unfilled histograms with adjustable bins.
    plt.hist(full_means, bins=bins, density=True, histtype="step", label="200-value mean")
    plt.hist(subtable_means, bins=bins, density=True, histtype="step", label="50-value mean")

    # Extra requirement: analytical normal-density predictions.
    x = np.linspace(min(full_means.min(), subtable_means.min()),
                    max(full_means.max(), subtable_means.max()), 500)

    def normal_pdf(x_values, standard_deviation):
        """Evaluate the mean-zero Gaussian probability-density function."""
        coefficient = 1 / (standard_deviation * np.sqrt(2 * np.pi))
        return coefficient * np.exp(-(x_values**2) / (2 * standard_deviation**2))

    # Mean of k independent N(0,1) values has standard deviation 1/sqrt(k).
    plt.plot(x, normal_pdf(x, 1 / np.sqrt(200)), label="Theory: k=200")
    plt.plot(x, normal_pdf(x, 1 / np.sqrt(50)), label="Theory: k=50")
    plt.legend()
    return full_means, subtable_means
```

Increasing `bins` increases resolution but can make a finite sample histogram noisier. Increasing `iterations` produces smoother curves. The subtable contains `5 * 10 = 50` values, so its mean varies more than the full table's 200-value mean.

---

## Exercise 21 - More two-dimensional indexing patterns

```python
def zero_checkerboard_slices(a):
    """Use the minimal two basic-slice assignments."""
    # Requirement 1: even row + even column gives an even sum.
    a[::2, ::2] = 0

    # Requirement 2: odd row + odd column also gives an even sum.
    a[1::2, 1::2] = 0
    return a


def zero_checkerboard_one_line(a):
    """General one-line solution using a generated Boolean mask."""
    # Requirement 3: set positions where row_index + column_index is even.
    a[np.indices(a.shape).sum(axis=0) % 2 == 0] = 0
    return a


def zero_checkerboard_odd_columns_puzzle(a):
    """One-line puzzle solution for a contiguous non-view array with odd columns."""
    # Requirement 4: with odd column count, flat-index parity equals row+column parity.
    a.ravel()[::2] = 0
    return a
```

Basic rectangular slicing cannot express both checkerboard groups in one ordinary slice, so two assignments are minimal in that restricted approach. Boolean masking can express the general rule in one assignment. The `ravel()` puzzle depends on contiguous storage and an odd column count.

---

## Exercise 22 - Stacking

```python
def stacking_exercise(n):
    """Build the requested list, 2-D stack, and flat concatenation."""
    # Requirement 1: list of n arrays; row i contains i through i+4.
    arrays = [np.arange(i, i + 5) for i in range(n)]

    # Requirement 2.1: make an n x 5 array, one input array per row.
    matrix = np.vstack(arrays) if n else np.empty((0, 5), dtype=int)

    # Requirement 2.2: concatenate all arrays into one length n*5 array.
    flattened = np.hstack(arrays) if n else np.array([], dtype=int)
    return arrays, matrix, flattened


arrays, matrix, flattened = stacking_exercise(3)
print(matrix)
print(flattened)
```

`np.arange(start, stop)` includes `start` and excludes `stop`. `np.vstack` stacks inputs as rows; `np.hstack` joins one-dimensional inputs end to end.

---

## Exercise 23 - Advanced broadcasting puzzle

```python
def broadcasting_table(n):
    """Produce Exercise 22's n x 5 matrix from two 1-D arrays in one line."""
    # Requirement: reshape the n-vector to (n, 1), then broadcast with shape (5,).
    return np.arange(n)[:, np.newaxis] + np.arange(5)
```

Shapes `(n, 1)` and `(5,)` broadcast to `(n, 5)`. Every row starting value is added to `[0, 1, 2, 3, 4]`. `[:, None]`, `.reshape(n, 1)`, and `np.expand_dims(..., 1)` are equivalent here.

---

## Exercise 24 - Sieve of Eratosthenes (I)

```python
def sieve_all_candidates(n):
    """Return a Boolean primality mask using every candidate up to sqrt(n-1)."""
    # Requirement 1: start by assuming every index is prime.
    prime = np.ones(n, dtype=bool)

    # Requirement 2: 0 and 1 are not prime.
    if n > 0:
        prime[0] = False
    if n > 1:
        prime[1] = False

    # Requirement 3: loop from 2 through floor(sqrt(n-1)), inclusive.
    upper = math.isqrt(n - 1) if n else 0
    for i in range(2, upper + 1):
        # Requirement 4: eliminate multiples starting at i**2 using a slice.
        prime[i**2:n:i] = False

    # Advanced requirement: obtain prime indices using arange + Boolean mask.
    prime_numbers = np.arange(n)[prime]
    return prime, prime_numbers


mask, primes = sieve_all_candidates(30)
print(primes)  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

Starting at `i**2` works because smaller multiples of `i` already have a smaller factor. `math.isqrt(x)` returns the exact integer floor of the square root without floating-point error. `np.flatnonzero(prime)` is a shorter alternative for extracting indices.

---

## Exercise 25 - Sieve of Eratosthenes (II)

```python
def sieve_prime_candidates(n):
    """True sieve: process only candidate indices still marked prime."""
    # Requirement 1: initialize the primality mask.
    prime = np.ones(n, dtype=bool)
    if n > 0:
        prime[0] = False
    if n > 1:
        prime[1] = False

    # Requirement 2: begin with the first prime candidate.
    i = 2

    # Requirement 3: only candidates with i**2 < n need processing.
    while i * i < n:
        prime[i * i:n:i] = False

        # Requirement 4: find the first True after i without a Python loop.
        # prime[i+1:] is a view; argmax returns the first True position.
        tail = prime[i + 1:]
        if not tail.any():
            break
        i += 1 + tail.argmax()

    return prime, np.flatnonzero(prime)


def compare_sieves(n=10**7):
    """Time the suboptimal and true sieve implementations."""
    start = time.time()
    mask1, primes1 = sieve_all_candidates(n)
    first_seconds = time.time() - start

    start = time.time()
    mask2, primes2 = sieve_prime_candidates(n)
    second_seconds = time.time() - start

    assert np.array_equal(mask1, mask2)
    assert np.array_equal(primes1, primes2)
    print("All candidates:", first_seconds)
    print("Prime candidates:", second_seconds)
    print("Speed ratio:", first_seconds / second_seconds)
```

`argmax()` returns the first position containing the maximum Boolean value (`True`). Checking `.any()` first avoids treating index `0` as a successful result when no `True` exists. Exact timing depends on NumPy version and hardware, so a fixed 4-5x speedup is not guaranteed.

---

## Exercise 26 - Conway's Game of Life

### Requirements: input -> output

- Input: a finite two-dimensional configuration of zero/one values and a step count.
- Each iteration counts up to eight in-bounds neighbors; edges naturally have fewer.
- A live cell survives with two or three neighbors.
- A dead cell becomes alive with exactly three neighbors.
- Output: the Boolean configuration after the requested number of steps.
- Optional plotting clears and redraws every step with a short pause.

```python
def count_neighbors(current):
    """Count in-bounds live neighbors for every cell without wraparound."""
    # Requirement 1: one integer neighbor count per cell.
    neighbors = np.zeros(current.shape, dtype=np.uint8)

    # Requirement 2: add the eight shifted neighboring regions.
    # Cells outside the finite array are never included.
    neighbors[1:, 1:] += current[:-1, :-1]   # upper-left neighbor
    neighbors[1:, :] += current[:-1, :]      # upper neighbor
    neighbors[1:, :-1] += current[:-1, 1:]   # upper-right neighbor
    neighbors[:, 1:] += current[:, :-1]      # left neighbor
    neighbors[:, :-1] += current[:, 1:]      # right neighbor
    neighbors[:-1, 1:] += current[1:, :-1]   # lower-left neighbor
    neighbors[:-1, :] += current[1:, :]      # lower neighbor
    neighbors[:-1, :-1] += current[1:, 1:]   # lower-right neighbor
    return neighbors


def game_of_life(initial, steps, display=False, pause=0.05):
    """Run finite-grid Conway's Game of Life and return the final state."""
    # Requirement 1: convert to bool and copy so input is not modified.
    current = np.array(initial, dtype=bool, copy=True)

    # Requirement 2: repeat the rules for the requested number of steps.
    for _ in range(steps):
        neighbors = count_neighbors(current)

        # Requirement 3: birth with exactly 3 neighbors.
        birth = (~current) & (neighbors == 3)

        # Requirement 4: survival with exactly 2 or 3 neighbors.
        survival = current & ((neighbors == 2) | (neighbors == 3))

        # Requirement 5: create the next configuration.
        next_state = birth | survival
        current = next_state

        # Requirement 6: optionally plot every new state.
        if display:
            plt.clf()
            plt.imshow(current, cmap="binary", interpolation="nearest")
            plt.pause(pause)

    # Requirement 7: return the final configuration.
    return current


# Prompt example: glider.
n = 20
configuration = np.zeros((n, n), dtype=bool)
glider = np.array([
    [0, 0, 1],
    [1, 0, 1],
    [0, 1, 1],
], dtype=bool)
rows, columns = glider.shape
configuration[:rows, :columns] = glider
final_configuration = game_of_life(configuration, 50, display=False)

# Prompt example: random starting state with about 20% live cells.
rng = np.random.default_rng()
random_configuration = rng.random((100, 100)) < 0.2
random_result = game_of_life(random_configuration, 100)
```

### Explanation of the prompt's diagonal `ravel()` examples

```python
n = 200
c = np.zeros((n, n), dtype=bool)

# Main diagonal: flattened indices 0, n+1, 2(n+1), ...
c.ravel()[::n + 1] = True

# Opposite diagonal: flattened indices n-1, 2(n-1), 3(n-1), ...
c.ravel()[n - 1::n - 1] = True
```

`ravel()` exposes the 2-D grid as a one-dimensional view when possible. A row-major `n x n` array moves one diagonal step by `n+1` flat positions and one anti-diagonal step by `n-1` positions. The variation in the prompt changes starting/stopping indices to draw shifted diagonal segments.

`plt.clf()` prevents artists from accumulating on the same figure, which would consume memory and slow every new frame. `plt.pause()` lets the graphical event loop render the updated image.

---

## Quick function reference

| Function or attribute | Purpose |
|---|---|
| `np.array(data, dtype=...)` | Convert data to an array, optionally forcing a type |
| `.dtype` | Read an array/scalar's NumPy data type |
| `np.iinfo(dtype)` | Integer type limits |
| `np.finfo(dtype)` | Floating-point type limits |
| `np.result_type(...)` | Predict a common promoted type |
| `np.ones`, `np.zeros`, `np.full` | Create initialized arrays |
| `np.arange` | Regular values using a step or integer range |
| `np.linspace` | An exact number of regularly spaced values |
| `np.hstack`, `np.vstack` | Join arrays horizontally or vertically |
| `np.array_equal` | One Boolean indicating exact shape/value equality |
| `np.all`, `np.any` | Reduce a Boolean array to one Boolean |
| `np.shares_memory` | Test whether arrays share underlying storage |
| `.copy()` | Create independent array storage |
| `.base` | Inspect the object behind a view |
| `rng.integers` | Generate random integer values |
| `rng.random` | Generate uniform floats in `[0, 1)` |
| `rng.normal` | Generate normally distributed values |
| `.mean()` | Compute an arithmetic mean |
| `.ravel()` | Flatten, returning a view when possible |
| `np.flatnonzero` | Return flat indices of nonzero/True values |
| `plt.plot`, `plt.hist`, `plt.imshow` | Plot lines, histograms, or images |
| `plt.clf()` | Clear the current figure |
| `plt.savefig()` | Save the current figure to a file |

## Important conceptual summary

1. A NumPy array has one `dtype`; conversions occur during creation and assignment.
2. Basic slicing normally creates a view; advanced list/mask indexing creates a copy.
3. Broadcasting applies compatible scalars/arrays without explicit Python loops.
4. Vectorized functions operate elementwise in compiled NumPy code.
5. Equality (`np.array_equal`) and identity (`is`) answer different questions.
6. Random experiments approach theoretical expectations as repetitions increase.
7. Fixed-width integer overflow, floating precision, and version-dependent conversion rules must be considered explicitly.
