# ex02 — Vector (dunder / magic methods)

## The big idea
Build a `Vector` class that supports row and column vectors with proper
arithmetic via **dunder methods** (`__add__`, `__sub__`, `__mul__`, etc.).
The canonical storage is always `self.values` (list of rows) + `self.shape`.

| shape     | example `values`               | meaning          |
|-----------|--------------------------------|------------------|
| `(1, n)`  | `[[1.0, 2.0, 3.0]]`           | row vector       |
| `(n, 1)`  | `[[1.0], [2.0], [3.0]]`       | column vector    |

## Things to understand before coding

1. **Four construction forms.**
   - `Vector(int)` → column `[[0.0], ..., [n-1.0]]`
   - `Vector((a, b))` → column range `[[a.0], ..., [b-1.0]]`
   - `Vector([[...]])` → row or column depending on nesting
   - `Vector([...])` → flat list → row vector

2. **`__add__` / `__sub__`.** Python calls `a + b` as `a.__add__(b)`. Use
   `zip` of rows and `zip` of elements within each row for element-wise ops.
   Reject mismatched shapes with `ValueError`.

3. **`__mul__` / `__rmul__`.** `v * 3` → `__mul__`; `3 * v` → `__rmul__`.
   Since scalar multiplication is commutative, `__rmul__` just calls `__mul__`.

4. **`__truediv__` / `__rtruediv__`.** `v / s` is valid; `s / v` is not
   (raise `NotImplementedError`). Guard against `scalar == 0`.

5. **`T()` transpose.** Row → column: wrap each element in its own list.
   Column → row: collect the lone element from each row into one list.

6. **`dot()`.** Flatten both vectors to 1-D, `zip` them together, multiply
   pairs, sum the results. Requires identical shapes.

7. **`__str__` / `__repr__`.** Both return `"Vector(%s)" % self.values` so
   the object looks the same in `print()` and in the REPL.

## Self-check
Run `python test.py` — all operations should print without exceptions and
match the expected outputs in the comments.
