# ex05 — The right format (f-string katas)

## The big idea
Five small files that each practice a different f-string formatting trick.
No user input — just format a hardcoded `kata` variable and print it.

## The five katas

| file      | what it formats                            | key trick                       |
|-----------|--------------------------------------------|---------------------------------|
| kata00.py | tuple of 3 integers                        | `f"The {len(kata)} numbers..."` |
| kata01.py | dict of language → creator                 | loop `.items()`                 |
| kata02.py | 5-int tuple (Y, M, D, H, Min)              | `{val:02}` / `{val:04}` padding |
| kata03.py | string centered with dashes to 42 chars    | `{s:->42}`                      |
| kata04.py | mixed numbers (fixed, scientific notation) | `{f:.2f}`, `{n:.2e}`            |

## Things to understand before coding

1. **f-string format spec after `:`.** The format spec goes after the colon
   inside `{}`:
   - `{n:02}` — zero-pad to width 2
   - `{f:.2f}` — 2 decimal places, float notation
   - `{f:.2e}` — 2 decimal places, scientific notation (`1.32e+02`)
   - `{s:->42}` — right-align with `-` fill, total width 42

2. **Fill character.** `{value:FILL>WIDTH}` pads with FILL character on the
   left (`>`), right (`<`), or center (`^`). In kata03 `{kata[:42]:->42}` fills
   with dashes from the left.

3. **Iterating a dict.** `for key, value in d.items()` unpacks both at once —
   no need to look up `d[key]` separately.

4. **`isinstance` guard (kata00).** Before printing, confirm every element is
   an `int`; if not, print an error and return early.

## Self-check
```
python kata00.py   # The 3 numbers are: 19, 42, 21
python kata01.py   # Python was created by Guido van Rossum  (+ Ruby, PHP)
python kata02.py   # 09/25/2019 03:30
python kata03.py   # --------------------------The right format
python kata04.py   # module_00, ex_04 : 132.42, 1.00e+04, 1.23e+04
```
