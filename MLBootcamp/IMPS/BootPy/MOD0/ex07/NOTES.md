# ex07 — Filter words (list comprehension + string stripping)

## The big idea
Given a string S and an integer N, return all words in S whose length (after
stripping punctuation) is strictly greater than N.

```
python filterwords.py "Hello, world!" 4
# ["Hello", "world"]
```

## Things to understand before coding

1. **`string.punctuation`.** `import string` gives a constant containing all
   punctuation characters. Use `word.strip(string.punctuation)` to remove
   leading/trailing punctuation from each word (e.g. `"Hello,"` → `"Hello"`).

2. **`.split()` vs `.split(" ")`.** `str.split()` (no argument) splits on any
   whitespace and discards empty strings. `str.split(" ")` splits only on
   literal spaces and can produce empty strings. Use the no-arg form for
   robustness.

3. **List comprehension.**
   ```python
   [word.strip(string.punctuation)
    for word in S.split()
    if len(word.strip(string.punctuation)) > N]
   ```
   Strip inside both the condition and the output so the returned word is clean.

4. **Argument validation.** Require exactly 2 arguments; convert N with `int()`
   and catch `ValueError` for non-integer input.

## Self-check
```
python filterwords.py "Hello, world! Bye." 3
# ['Hello', 'world']
python filterwords.py "Too many args" 2 extra
# ERROR
```
