# ex03 — Text Analyzer (character counting)

## The big idea
Count how many characters in a string fall into each category: uppercase,
lowercase, punctuation, spaces, and all printable characters.

## Things to understand before coding

1. **`string` module.** `import string` gives you `string.punctuation` — a
   ready-made string of all punctuation characters (`!"#$%&'()*+,-./:;<=>?@...`).
   Use it instead of hard-coding.

2. **Generator expressions with `sum()`.** The cleanest pattern:
   ```python
   ups = sum(1 for c in text if c.isupper())
   ```
   This is more readable than a for-loop counter.

3. **String methods to know.**
   - `c.isupper()` / `c.islower()` — alphabetic case
   - `c.isspace()` — space, tab, newline, etc.
   - `c.isprintable()` — everything that renders visibly (spaces included)
   - `c in string.punctuation` — punctuation check

4. **Optional prompt input.** If `obj is None`, call `input(...)` to ask the
   user. `isinstance(obj, str)` guards against non-string arguments.

5. **Calling from CLI vs import.** The `main()` reads from `sys.argv[1]` and
   passes it to `text_analyzer()`. The function itself can also be called
   directly in a REPL or another module.

## Self-check
```
python count.py "Hello World!"
# The text contains 12 printable character(s):
# - 2 upper letter(s)
# - 8 lower letter(s)
# - 1 punctuation mark(s)
# - 1 space(s)
```
