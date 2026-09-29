# 10 SymPy Exercises — Exact Symbolic Mathematics

**Level:** Beginner to intermediate  
**Library:** SymPy only  
**Topics:** Exact arithmetic, algebra, equations, derivatives, and integrals

## Theory and setup

SymPy manipulates symbolic expressions and can preserve exact fractions, radicals, and constants. Exact inputs matter: use `sp.Rational(1, 3)`, `sp.sqrt(2)`, and `sp.pi` instead of decimal approximations. SymPy also supports numerical approximations when requested; not every symbolic problem has a closed-form solution.

Install with `python -m pip install sympy`, then start with:

~~~python
import sympy as sp

x, y = sp.symbols("x y", real=True)
~~~

Keep answers exact unless an approximation is explicitly requested. Use `**` for powers and `sp.Eq(left, right)` to construct equations. Print clearly labeled results for each task.

## 1. Exact fractions and radicals — Easy

**Theory:** Fractions and radicals can be represented exactly.

Calculate:
- a = 1/3 + 1/6 − 1/8
- b = √72 − √8 + √2
- c = a + b

**Tasks:**
1. Build the fractions with exact rational numbers.
2. Simplify and print a, b, and c.
3. Separately display c to 12 significant digits.
4. Explain why plain Python `1/3` does not create an exact SymPy rational.

**Hints:** `sp.Rational(p, q)`, `sp.sqrt(n)`, `sp.simplify(expr)`, `sp.N(expr, 12)`.

## 2. Expand and factor a polynomial — Easy

**Theory:** Expansion and factorization give equivalent polynomial forms.

Given P(x) = (x − 2)(x + 3)(2x − 1):

1. Expand P(x).
2. Factor the expanded expression.
3. Evaluate P(1/2) exactly.
4. Verify equivalence by simplifying the difference between the original and expanded expressions.

**Hints:** `sp.expand(expr)`, `sp.factor(expr)`, `expr.subs(x, value)`.

## 3. Simplification and domain restrictions — Easy

**Theory:** Cancelling factors does not remove restrictions from the original expression's domain.

Given R(x) = (x² − 9)/(x² − x − 6):

1. Factor the numerator and denominator.
2. Find every real value excluded from the original domain.
3. Simplify R(x) by cancelling common factors.
4. Evaluate both forms at x = 4.
5. Explain why the simplified formula does not make every originally excluded value valid.

**Hints:** `sp.factor()`, `sp.cancel()`, `sp.solveset(denominator, x, domain=sp.S.Reals)`.

## 4. Solve a linear equation exactly — Easy

**Theory:** A solution makes the two sides of an equation equal.

Solve (2x − 1)/3 + (x + 2)/4 = 5/6.

1. Construct the equation with `sp.Eq`.
2. Solve over the real numbers.
3. Keep the solution as an exact fraction.
4. Substitute it into both sides and verify that their difference simplifies to zero.

**Hints:** `sp.Eq(lhs, rhs)`, `sp.Rational(5, 6)`, `sp.solveset(eq, x, domain=sp.S.Reals)`.

## 5. Solve a quadratic with irrational roots — Medium

**Theory:** Exact solutions can contain radicals.

Solve 2x² − 3x − 1 = 0.

1. Find both real roots in exact form.
2. Verify each root by substitution.
3. Calculate the sum and product of the roots.
4. Check these against −b/a and c/a.
5. Only after finding the exact roots, display 8-significant-digit approximations.

**Hints:** `sp.solve(expr, x)`, `sp.simplify()`, `sp.N()`.

## 6. Solve simultaneous equations — Medium

**Theory:** A system's solution must satisfy all equations simultaneously.

Solve:
- 2x + 3y = 7
- 4x − y = 5

1. Construct both symbolic equations.
2. Solve simultaneously for x and y.
3. Keep both values exact.
4. Substitute the solution into each equation and check that both residuals are zero.

**Hints:** `sp.solve([eq1, eq2], (x, y), dict=True)`, `expr.subs(solution)`.

**Deliverable:** A solution dictionary and two residual checks.

## 7. Derivatives and a tangent line — Medium

**Theory:** The first derivative gives tangent slope; differentiating again gives the second derivative.

Given f(x) = x³ − 3x² + 2x + 1:

1. Calculate f′(x) and f″(x).
2. Find f(2) and f′(2).
3. Construct the tangent line y = f(2) + f′(2)(x − 2).
4. Verify that the line passes through (2, f(2)) and has the same slope as f at x = 2.

**Hints:** `sp.diff(f, x)`, `sp.diff(f, x, 2)`, `.subs()`, `sp.expand()`.

## 8. Product rule and chain rule — Medium

**Theory:** Symbolic differentiation handles products and composed functions.

Given g(x) = (x² + 1)e^(2x) and h(x) = sin(x²):

1. Compute g′(x) and h′(x) with SymPy.
2. Independently construct the derivative of g using the product rule.
3. Independently construct the derivative of h using the chain rule.
4. Verify that each manually constructed derivative matches SymPy's result by simplifying their difference.
5. Evaluate g′(0) and h′(√(π/2)) exactly.

**Hints:** `sp.exp()`, `sp.sin()`, `sp.cos()`, `sp.diff()`, `sp.simplify()`, `sp.pi`.

## 9. Indefinite integration and a constant — Medium

**Theory:** Antiderivatives of the same function differ by an additive constant.

Given f(x) = 6x² − 4x + 3:

1. Compute one antiderivative.
2. Add a symbolic constant C to express the general antiderivative F(x).
3. Determine C using F(0) = 5.
4. Differentiate the resulting F(x) and verify that it equals f(x).
5. Verify the initial condition.

**Hints:** `sp.integrate(f, x)`, `sp.symbols("C")`, `sp.solve()`, `sp.diff()`.

**Note:** SymPy's indefinite integration does not automatically append the arbitrary constant.

## 10. Definite integral versus geometric area — Challenge

**Theory:** A definite integral is signed. Total geometric area counts regions above and below the horizontal axis positively.

Given f(x) = x² − 1 on [−2, 2]:

1. Find all zeros in the interval.
2. Determine the sign of f on the subintervals separated by those zeros.
3. Compute the signed integral from −2 to 2.
4. Compute total geometric area by splitting at the zeros and changing the sign of integrals over intervals where f is negative.
5. Explain why the signed integral and total area differ. Keep both answers exact.

**Hints:** `sp.solve(f, x)`, `sp.integrate(f, (x, lower, upper))`.

## Completion checklist

- Use exact inputs and symbolic expressions.
- Approximate only when explicitly requested.
- Check equation solutions by substitution.
- Preserve original domain restrictions.
- Check antiderivatives by differentiation.
- Distinguish signed integral from total geometric area.

## Official references

- [SymPy tutorials](https://docs.sympy.org/latest/tutorials/index.html)
- [Exact numbers and common pitfalls](https://docs.sympy.org/latest/explanation/gotchas.html)
- [Differentiation and integration](https://docs.sympy.org/latest/tutorial/calculus.html)

