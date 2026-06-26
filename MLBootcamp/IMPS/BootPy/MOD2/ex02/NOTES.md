# ex02 — The logger (decorators)

## The big idea
A **decorator** is a function that takes a function and returns a *new* function
that usually does something extra around the original. `@log` above a method is
just sugar for `method = log(method)`.

```python
def log(function):
    def wrapper(*args, **kwargs):
        # ...before...
        result = function(*args, **kwargs)   # call the real method
        # ...after...
        return result
    return wrapper
```

## Things to understand before coding

1. **Why `*args, **kwargs` in wrapper.** The wrapper replaces the method, so it
   must accept whatever the method accepts — including `self` and arguments like
   `add_water(70)`. Forwarding `*args, **kwargs` passes them straight through.

2. **Timing.** Capture `start = time.time()` before the call, `time.time()-start`
   after. The subject shows two units: print **seconds** (`s`) when the duration
   is >= 1 second, otherwise **milliseconds** (`ms`). Multiply by 1000 for ms.

3. **The username.** "the username from environment variables is written" ->
   `os.environ.get("USER")` (the `$USER` shell variable). Use `.get(..., default)`
   so it doesn't crash if missing.

4. **The function name.** `function.__name__` gives `"start_machine"`. The log
   shows `Start Machine`: replace `_` with space and `.title()` it.

5. **The 20-char field.** "the length between ':' and '[' is 20." So the segment
   holding the name (a leading space + the name) is left-justified to width 20:
   `f"{f' {name}':<20}"`. Conclusion to draw: it makes every `[ exec-time ... ]`
   line up in a neat column regardless of the method name length.

6. **Appending to the file.** Open `machine.log` in **append** mode `"a"` so each
   call adds a line instead of overwriting. `with open(...) as f:` closes it.

7. **`functools.wraps`** (optional but nice): put `@wraps(function)` on wrapper so
   the decorated method keeps its real name/docstring.

## Self-check
Run `python logger.py`, then look at `machine.log`. Each line should read like:
`(youruser)Running: Start Machine          [ exec-time = 0.001 ms ]`
