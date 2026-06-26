# ex05 — TinyStatistician

## The big idea
Implement basic statistics **by hand** (no numpy/statistics helpers that compute
mean/median/var/std for you). You may still accept a `numpy.ndarray` as input —
just don't call its stat methods. Every method returns a `float`, or `None` for
an empty input.

## The formulas

Let `x` have `m` elements, mean `µ`.

- **mean**  `µ = (Σ xᵢ) / m`  — one for-loop summing, divide by count.

- **median** — sort a copy, then:
  - odd count -> the middle element,
  - even count -> average of the two middle elements.
  Return as float.

- **quartiles** (the subject's variant) -> `[Q1, Q3]` where
  `Q1` is the value at index `m * 1/4` and `Q3` at index `m * 3/4` of the
  **sorted** data, using `int(...)` to pick the index. Check it reproduces the
  expected `[10.0, 59.0]` for `[1, 42, 300, 10, 59]` (sorted: 1,10,42,59,300;
  indices int(5*0.25)=1 -> 10, int(5*0.75)=3 -> 59). Return floats.

- **var** (population variance)
  `σ² = (1/m) Σ (xᵢ − µ)²`  — loop, accumulate squared deviations, divide by m.
  (This matches the expected `12279.44`; note it's `/m`, not `/(m-1)`.)

- **std**  `σ = sqrt(var)`  — reuse var, take the square root (`x ** 0.5`).

## Things to keep in mind
- **Empty check first.** `if len(x) == 0: return None` (works for list or
  ndarray via `len`). Do this in every method.
- **Use for-loops** for mean / var / std (the subject says so explicitly).
- **Don't mutate the input** when sorting — sort a copy: `sorted(x)` returns a
  new list.
- **Return floats.** Cast with `float(...)` where needed so `42` prints `42.0`.
- Inputs are assumed valid (numeric) — no need to guard against bad types.

## Self-check (from the subject)
```
a = [1, 42, 300, 10, 59]
mean -> 82.4
median -> 42.0
quartile -> [10.0, 59.0]
var -> 12279.439999999999
std -> 110.81263465868862
```
Note: the subject's example calls `tstat.quartile(a)`. Define the method to
match whichever name you turn in (`quartile` or `quartiles`) — be consistent.
