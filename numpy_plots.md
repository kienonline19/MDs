# NumPy Graph-Plotting Exercises

20 exercises for practicing data generation with **NumPy** and visualization with **Matplotlib**. Each exercise states the goal and gives a hint pointing to the relevant functions — try to write the code yourself before checking the solutions file.

> Setup used throughout:
> ```python
> import numpy as np
> import matplotlib.pyplot as plt
> ```

---

## Part 1 — Basics

### Exercise 1: Plot a Parabola
Plot `y = x^2` for `x` ranging from -10 to 10.

**Hint:** Use `np.linspace()` to generate evenly spaced x-values, then square them with NumPy's vectorized `**` operator. Plot with `plt.plot()`.

---

### Exercise 2: Sine and Cosine Together
On the same axes, plot `sin(x)` and `cos(x)` for `x` from `0` to `2π`, each with a different color and a legend.

**Hint:** `np.linspace(0, 2*np.pi, N)` for the x-axis, `np.sin()` / `np.cos()` for the curves, and `plt.legend()` with a `label=` set on each `plt.plot()` call.

---

### Exercise 3: Scatter Plot of Random Points
Generate 100 random `(x, y)` points and display them as a scatter plot.

**Hint:** `np.random.rand(100)` (or `np.random.uniform`) for both axes; use `plt.scatter()` instead of `plt.plot()`.

---

### Exercise 4: Bar Chart of Category Totals
Given 5 categories with random integer values between 10 and 100, draw a bar chart.

**Hint:** `np.random.randint(10, 100, size=5)` for the heights; `plt.bar()` takes category labels/positions and heights.

---

### Exercise 5: Histogram of a Normal Distribution
Generate 1000 samples from a normal distribution (mean 0, std 1) and plot a histogram with 30 bins.

**Hint:** `np.random.normal(loc=0, scale=1, size=1000)`; `plt.hist(data, bins=30)`.

---

### Exercise 6: Pie Chart
Given 4 named categories with arbitrary weights, draw a pie chart with percentage labels.

**Hint:** Weights don't need to sum to 1 — `plt.pie()` normalizes automatically. Use `autopct='%1.1f%%'` for percentage labels.

---

## Part 2 — Styling and Layout

### Exercise 7: 2×2 Subplot Grid
Plot `sin(x)`, `cos(x)`, `tan(x)`, and `x^2` in a 2×2 grid of subplots, each with its own title.

**Hint:** `plt.subplots(2, 2, figsize=(...))` returns a `fig` and a 2D array of `axes`; index into `axes[row, col]` and call `.plot()` / `.set_title()` on each.

---

### Exercise 8: Custom Line Styles and Markers
Plot 3 linear functions (`y = x`, `y = 2x`, `y = 0.5x`) with distinct line styles, colors, and markers.

**Hint:** `plt.plot()` accepts a format shorthand like `'r--o'`, or explicit `linestyle=`, `color=`, `marker=` keyword arguments.

---

### Exercise 9: Labeled Plot with Grid and Legend
Plot `y = x^3` with axis labels, a title, a grid, and a legend.

**Hint:** `plt.xlabel()`, `plt.ylabel()`, `plt.title()`, `plt.grid(True)`, `plt.legend()`.

---

### Exercise 10: Fill Between Two Curves
Plot `sin(x)` and `sin(x) + 0.5` over `[0, 2π]` and shade the region between them.

**Hint:** `plt.fill_between(x, y1, y2, alpha=...)` shades the area between two arrays evaluated at the same `x`.

---

## Part 3 — Scales and Coordinate Systems

### Exercise 11: Logarithmic Scale Plot
Plot `y = e^x` for `x` from 0 to 10 on a plot with a logarithmic y-axis, and compare it visually to a linear-scale version.

**Hint:** `np.exp()` for the data; `plt.yscale('log')` (or `plt.semilogy()`) switches the axis scale.

---

### Exercise 12: Polar Plot
Plot the rose curve `r = cos(3θ)` for `θ` from `0` to `2π` in polar coordinates.

**Hint:** `np.linspace(0, 2*np.pi, N)` for `θ`; create the axes with `plt.subplot(projection='polar')`, then `plot(theta, r)`.

---

### Exercise 13: 3D Surface Plot
Plot the surface `z = sin(sqrt(x^2 + y^2))` over a grid where `x` and `y` range from -5 to 5.

**Hint:** `np.meshgrid()` builds the 2D coordinate grids from two 1D arrays; the axes need `projection='3d'` and the surface is drawn with `ax.plot_surface()`.

---

### Exercise 14: Contour Plot
Draw filled contour lines for `z = x^2 - y^2` over a grid where `x, y ∈ [-5, 5]`.

**Hint:** Same `np.meshgrid()` setup as Exercise 13, then `plt.contourf()` (filled) or `plt.contour()` (lines only), with a colorbar via `plt.colorbar()`.

---

## Part 4 — Statistical and Specialized Plots

### Exercise 15: Error Bar Plot
Plot `y = sqrt(x)` for 10 points with random error bars (noise between 0.1 and 0.5).

**Hint:** `np.sqrt()` for the values, `np.random.uniform(0.1, 0.5, size=...)` for the error magnitudes, `plt.errorbar(x, y, yerr=...)`.

---

### Exercise 16: Stacked Bar Chart
Given 3 groups and 2 sub-series per group, draw a stacked bar chart.

**Hint:** Two calls to `plt.bar()` on the same x-positions; the second call needs `bottom=` set to the first series' values so the bars stack rather than overlap.

---

### Exercise 17: Heatmap with `imshow`
Generate a 10×10 array of random values and display it as a heatmap with a colorbar.

**Hint:** `np.random.rand(10, 10)` for the data; `plt.imshow(data, cmap='viridis')` followed by `plt.colorbar()`.

---

### Exercise 18: Cumulative Sum Plot
Generate 50 random steps (positive or negative) and plot their cumulative sum as a "random walk."

**Hint:** `np.random.choice([-1, 1], size=50)` (or random floats) for the steps, `np.cumsum()` to accumulate them, then a simple line plot.

---

### Exercise 19: Step Plot
Given hourly measurements over a day (24 values), plot them as a step function rather than a smooth line.

**Hint:** `np.arange(24)` for the x-axis; use `plt.step()` instead of `plt.plot()` to keep values constant between points.

---

### Exercise 20: Vector Field with `quiver`
Plot the vector field `(u, v) = (-y, x)` (a simple rotation field) over a grid where `x, y ∈ [-5, 5]`.

**Hint:** `np.meshgrid()` again for the grid points, compute `U = -Y` and `V = X` directly from the grid arrays, then `plt.quiver(X, Y, U, V)`.

---

## Tips for All Exercises
- Always generate your data with NumPy first, then hand the resulting arrays to Matplotlib — don't loop in pure Python where a NumPy vectorized operation will do.
- Call `plt.show()` at the end of each script to display the figure.
- Try changing `figsize`, colors, and resolution (number of points in `linspace`) to see how they affect the result.