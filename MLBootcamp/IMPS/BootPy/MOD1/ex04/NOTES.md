# ex04 — Evaluator (static methods, zip vs enumerate)

## The big idea
Compute a weighted sum of word lengths: each word's length is multiplied by
its corresponding coefficient. Implement it two ways — one using `zip`, one
using `enumerate` — to understand both iteration tools.

```
coefs  = [1.0, 2.0, 1.0, 4.0, 0.5]
words  = ["Le", "Lorem", "Ipsum", "est", "simple"]
result = 1.0*2 + 2.0*5 + 1.0*5 + 4.0*3 + 0.5*6 = 34.0
```

## Things to understand before coding

1. **`@staticmethod`.** A method that belongs to the class logically but
   doesn't receive `self` or `cls`. Call it as `Evaluator.zip_evaluate(...)`.
   Use it when the method doesn't need any instance or class state.

2. **`zip(coefs, words)`.** Pairs up elements from two iterables in lockstep,
   stopping at the shorter one. Returns tuples: `(coef, word)`.
   ```python
   for coef, word in zip(coefs, words):
       count += coef * len(word)
   ```

3. **`enumerate(words, start=0)`.** Yields `(index, element)` pairs. Use the
   index to look up the matching coefficient:
   ```python
   for i, word in enumerate(words, 0):
       count += coefs[i] * len(word)
   ```

4. **Length mismatch → return -1.** If `len(coefs) != len(words)`, return `-1`
   instead of crashing. `zip` silently truncates; you must check explicitly.

5. **When to use which.**
   - `zip` — when you already have two equal-length iterables; cleanest syntax.
   - `enumerate` — when you need the index for reasons beyond pairing two lists.

## Self-check
Run `python eval.py`. Expected output: `34.0` then `-1` (lengths differ).
