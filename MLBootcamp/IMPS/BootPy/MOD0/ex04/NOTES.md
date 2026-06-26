# ex04 — Elementary (arithmetic operations)

## The big idea
Take exactly two integers A and B from the CLI and print five arithmetic
results: Sum, Difference, Product, Quotient, and Remainder.

## Things to understand before coding

1. **Two-argument guard.** `len(sys.argv) == 3` means exactly two arguments
   were provided. Handle fewer, more, and non-integers as separate error cases.

2. **Division by zero.** Before computing quotient and remainder, check `b == 0`
   and substitute an error message string instead of crashing.
   ```python
   quot = "ERROR (division by zero)" if b == 0 else a / b
   rem  = "ERROR (modulo by zero)"   if b == 0 else a % b
   ```

3. **`/` vs `//`.** The subject uses true division (`/`) so `7 / 2` → `3.5`,
   not integer division.

4. **Parsing integers.** `int(s)` raises `ValueError` on floats and strings.
   Wrap both conversions in a single try/except and print an error message.

5. **f-string formatting.** Use `\t` or spaces to align the labels neatly, or
   just separate them with newlines — match the subject's expected output.

## Self-check
```
python operations.py 10 3
# Sum:        13
# Difference: 7
# Product:    30
# Quotient:   3.3333333333333335
# Remainder:  1

python operations.py 5 0
# Quotient:   ERROR (division by zero)
# Remainder:  ERROR (modulo by zero)
```
