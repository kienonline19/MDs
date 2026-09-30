# Java OOP — 10 Exercises on 2D Arrays

## Shared class requirements

Implement all ten exercises as **instance methods** in a class named `Matrix`.

- Store the matrix in a `private final int[][] data` field.
- Provide `public Matrix(int[][] values)`. Copy every input row so modifying the caller's array cannot change the object.
- Reject null, empty, null-row, or jagged input with `IllegalArgumentException`.
- Provide `public int[][] toArray()` that returns a deep copy, never the internal array.
- Provide `public String toString()` to display the matrix contents.
- Methods operate on the current object's data; do not pass the matrix as a method parameter.
- Exercises 4 and 5 modify the current object. Exercises 3 and 6 return a new `Matrix` object. All other exercises leave the object unchanged.
- Use `public class MatrixSolutions` for the runnable program. Place the non-public `Matrix` class in the same file, `MatrixSolutions.java`.
- Only the program entry point `main` needs to be static. Do not make the ten exercise methods static.

**Input constraints:** 1–100 rows and columns; integer values and targets from −10,000 to 10,000. Exercise 10 uses only 0 and 1. Assume numeric bounds are respected; the constructor must validate matrix shape. Indices start at zero. Duplicates are allowed. “Nondecreasing” permits equal adjacent values.

Search ordering conditions are preconditions for the relevant methods; do not sort or scan the entire matrix to validate them before searching. Complexity targets apply to method calls after object construction.

**Example object usage:**

```java
Matrix matrix = new Matrix(new int[][] {{3, 1}, {4, 2}});
int[] sums = matrix.rowSums();
matrix.sortRows();
System.out.println(matrix);
```

## Exercise 1 — Sum Each Row

**Level:** Easy

Return an array containing the sum of each row. Do not modify the current object.

**Required method:**

```java
public int[] rowSums()
```

**Example (current object → result):**

```text
{{1, 2, 3}, {4, 5, 6}} → {6, 15}
```

## Exercise 2 — Find the First Occurrence

**Level:** Easy

Return {row, column} for the first occurrence of target in row-major order: scan rows from top to bottom and each row from left to right. Return {-1, -1} if target is absent. Do not modify the current object.

**Required method:**

```java
public int[] findFirst(int target)
```

**Example (current object → result):**

```text
{{5, 2, 5}, {1, 5, 9}}, target = 5 → {0, 0}
```

## Exercise 3 — Transpose a Rectangular Matrix

**Level:** Easy

Return a new `Matrix` object whose rows are the original columns. An R × C input produces a C × R output. Do not modify the current object.

**Required method:**

```java
public Matrix transpose()
```

**Example (current object → result):**

```text
{{1, 2, 3}, {4, 5, 6}} → {{1, 4}, {2, 5}, {3, 6}}
```

## Exercise 4 — Sort Every Row

**Level:** Easy–Medium

Sort each row independently in nondecreasing order, within the current object. Implement insertion sort yourself; do not call Arrays.sort. Values must stay in their original rows.

**Required method:**

```java
public void sortRows()
```

**Example (current object → result):**

```text
{{3, 1, 2}, {9, 7, 8}} → {{1, 2, 3}, {7, 8, 9}}
```

## Exercise 5 — Sort Every Column

**Level:** Easy–Medium

Sort each column independently from top to bottom in nondecreasing order, within the current object. Implement selection sort yourself; do not call Arrays.sort. Values must stay in their original columns.

**Required method:**

```java
public void sortColumns()
```

**Example (current object → result):**

```text
{{9, 2}, {3, 8}, {6, 1}} → {{3, 1}, {6, 2}, {9, 8}}
```

## Exercise 6 — Sort All Matrix Values

**Level:** Medium

Return a new `Matrix` object of the same dimensions with all values sorted in nondecreasing row-major order. Do not modify the current object. Arrays.sort is allowed in this exercise.

**Required method:**

```java
public Matrix sortAll()
```

**Example (current object → result):**

```text
{{9, 1, 4}, {3, 8, 2}} → {{1, 2, 3}, {4, 8, 9}}
```

## Exercise 7 — Search Independently Sorted Rows

**Level:** Medium

Each row is sorted in nondecreasing order, but there is no ordering guarantee between different rows. Return true if target exists, otherwise false. Use binary search within each row. Do not modify the current object.

**Required method:**

```java
public boolean searchRows(int target)
```

**Example (current object → result):**

```text
{{1, 4, 9}, {2, 6, 8}}, target = 6 → true
```

## Exercise 8 — Binary Search a Globally Sorted Matrix

**Level:** Medium

Each row is sorted in nondecreasing order, and the first value of every row after the first is greater than the last value of the preceding row. Return whether target exists using one binary search. Do not allocate a flattened array or modify the current object.

**Required method:**

```java
public boolean searchGlobal(int target)
```

**Example (current object → result):**

```text
{{1, 3, 5}, {7, 9, 11}}, target = 9 → true
```

## Exercise 9 — Search a Row-and-Column Sorted Matrix

**Level:** Medium

Every row is sorted left to right and every column is sorted top to bottom, both in nondecreasing order. Rows may overlap in value. Return whether target exists using O(R + C) time and O(1) auxiliary space. Do not modify the current object.

**Required method:**

```java
public boolean searchStaircase(int target)
```

**Example (current object → result):**

```text
{{1, 4, 7}, {2, 5, 8}, {3, 6, 9}}, target = 6 → true
```

## Exercise 10 — Find the Row with the Most Ones

**Level:** Medium

The matrix contains only 0 and 1. Every row is sorted, so all zeros come before all ones. Return the index of the row containing the most ones. Break ties by choosing the smallest row index. Return -1 if the matrix has no ones. Use binary search to find the first 1 in each row.

**Required method:**

```java
public int rowWithMostOnes()
```

**Example (current object → result):**

```text
{{0, 0, 1}, {0, 1, 1}, {0, 1, 1}} → 1
```

