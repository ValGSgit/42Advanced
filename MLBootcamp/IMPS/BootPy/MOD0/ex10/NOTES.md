# ex10 — Loading! (progress bar generator)

## The big idea
Write `ft_progress(lst)` as a **generator** that yields each element of `lst`
one at a time while printing an updating progress bar to the terminal.

```python
for elem in ft_progress(range(3333)):
    sleep(0.005)
```

## Things to understand before coding

1. **Generators with `yield`.** A function containing `yield` becomes a
   generator. Each call to `next()` (or each iteration of `for`) runs the
   function body until the next `yield`, pauses, and hands the value to the
   caller. The local state (variables, loop counter) is preserved between calls.

2. **`\r` (carriage return).** `print(..., end="")` with `\r` at the start of
   the string overwrites the current line in the terminal instead of starting a
   new one. This is what makes the bar animate in place.

3. **Timing with `time.time()`.** Capture `start = time()` before the loop.
   Inside the loop: `elapsed = time() - start`. To estimate remaining time:
   ```
   eta = elapsed / (i + 1) * (total - i - 1) + elapsed
   ```
   (current rate × remaining items, from current elapsed as base)

4. **Bar construction.**
   ```python
   bar_len = 40
   filled = int(bar_len * percent)
   bar = "=" * filled + ">" + " " * (bar_len - filled - 1)
   ```
   The `>` is the leading edge; spaces fill the rest.

5. **`enumerate(lst)`.** Gives `(index, element)` pairs so you know both `i`
   (for percent calculation) and `elem` (to yield to the caller).

## Self-check
```
python loading.py
```
You should see a single line updating in place, showing ETA, percentage, bar,
and elapsed time. After the loop it prints the final sum.
