#%%
import math


""" def is_armstrong(n: int) -> bool:
    if n < 0:
        return False

    m = n
#     c = 1
#
#     while n > 9:
#         c += 1
#         n //= 10

    c = math.floor(math.log10(n)) + 1 if n else 1
    s = 0
#     n = m
    while n:
        s += (n % 10)**c
        n //= 10

    return s == m """


def is_armstrong(n):
    if n < 0:
        return False

    if n < 10:
        return True

    s, c, m = 0, math.floor(math.log10(n)) + 1 if n else 1, n

    while n:
        n, r = divmod(n, 10)
        s += r**c

        if s > m:
            return False
    return s == m


assert is_armstrong(153) == True
assert is_armstrong(9474) == True
assert is_armstrong(123) == False
assert is_armstrong(9) == True
assert is_armstrong(0) == True
assert is_armstrong(9475) == False
assert is_armstrong(370) == True
# %reset -f
globals().clear()

# %%
""" def remove_duplicates(arr: list) -> list:
    if not arr:
        return []

    res = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            res.append(arr[i])

    return res """

def remove_duplicates(arr: list) -> list:
    if not arr:
        return []

    slow = 1
    for fast in range(1, len(arr)):
        if arr[fast] != arr[fast-1]:
            arr[slow] = arr[fast]
            slow += 1

    return arr[:slow]


assert remove_duplicates([1, 1, 2]) == [1, 2]
assert remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == [0, 1, 2, 3, 4]
assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
assert remove_duplicates([]) == []
assert remove_duplicates([5, 5, 5, 5]) == [5]

# %%
def frequency_sort(arr: list) -> list:
    from collections import Counter

    s = Counter(arr)

    # ans = sorted(s.items(), key=lambda e: (-e[1], e[0]))

    # return sum([[x]*y for x, y in ans], [])

    # return sorted(arr, key=lambda x: (-s[x], x))

    res = arr.copy()

    for i in range(1, len(res)):
        key = res[i]
        j = i - 1

        while j >= 0 and (s[res[j]] < s[key] or (s[res[j]] == s[key] and res[j] > key)):
            res[j+1] = res[j]
            j -= 1

        res[j+1] = key

    return res

print(frequency_sort([1, 1, 2, 2, 2, 3]))
assert frequency_sort([1, 1, 2, 2, 2, 3]) == [2, 2, 2, 1, 1, 3]
assert frequency_sort([4, 4, 4, 5, 5, 6]) == [4, 4, 4, 5, 5, 6]
assert frequency_sort([1, 2, 3]) == [1, 2, 3]
assert frequency_sort([]) == []
assert frequency_sort([7, 7, 8, 8, 9]) == [7, 7, 8, 8, 9]
# %%
def find_peak(arr: list) -> int:
    lo, hi = 0, len(arr) - 1

    while lo < hi:
        m = (lo + hi)//2

        if arr[m] < arr[m+1]:
            lo = m + 1
        else:
            hi = m

    return lo


assert find_peak([1, 3, 5, 4, 2]) == 2
assert find_peak([1, 2, 3, 4, 5]) == 4
assert find_peak([5, 4, 3, 2, 1]) == 0
assert find_peak([1, 2, 1]) == 1
assert find_peak([1]) == 0

# %%
""" def equilibrium_index(arr: list) -> int:
    def sum_elements(idx):
        if idx == len(arr):
            return 0

        return arr[idx] + sum_elements(idx + 1)

    total = sum_elements(0)

    left = 0

    right = total

    for i, e in enumerate(arr):
        # right = total - left - e
        right -= e
        if left == right:
            return i
        left += e

    return -1 """
def equilibrium_index(arr: list) -> int:
    def solve(idx, left_sum):
        if idx == len(arr):
            return 0, -1

        right_sum, found_idx = solve(idx+1, left_sum + arr[idx])

        if left_sum == right_sum:
            found_idx = idx

        return right_sum + arr[idx], found_idx

    return solve(0, 0)[1]


assert equilibrium_index([-7, 1, 5, 2, -4, 3, 0]) == 3
assert equilibrium_index([1, 2, 3]) == -1
assert equilibrium_index([0]) == 0
assert equilibrium_index([1, 2, 3, 4, 3, 2, 1]) == 3
assert equilibrium_index([]) == -1


# %%
