# ex03 — Json issues (a context manager class)

## The big idea
A **context manager** is anything you can use with `with`. The point is
*guaranteed cleanup*: whatever happens inside the block, the file gets closed.

```python
with CsvReader('good.csv') as file:   # __enter__ runs, its return -> `file`
    ...                               # your work
# __exit__ runs here, even on exception -> close the file
```

You implement it with three dunder methods:
- `__init__(self, ...)`  — store the settings (filename, sep, header, skips).
- `__enter__(self)`      — open + read + parse; return `self` (or None on error).
- `__exit__(self, exc_type, exc_value, traceback)` — close the file.

## Things to understand before coding

1. **`__enter__` returns the bound value.** Returning `self` lets the caller do
   `file.getdata()`. Returning `None` lets the caller do `if file is None: ...`
   (used for the corrupted / missing-file cases).

2. **Parsing.** Read lines, `strip("\n")`, split each on `self.sep` -> a list of
   fields. Build a list of those row-lists.

3. **Validating "not corrupted".** Every record must have the **same number of
   fields**. Take the width of the first row; if any row differs -> return None.
   (`bad.csv` here has a short row and a too-long row to test this.)

4. **File not found.** Wrap `open()` in try/except `FileNotFoundError` (or OSError)
   and return None.

5. **header / skip_top / skip_bottom.**
   - If `header` is True, the first parsed row is the header; the rest is body.
   - Then slice the body: drop `skip_top` rows from the front and `skip_bottom`
     from the back -> `body[skip_top : len(body) - skip_bottom]`.

6. **getdata / getheader.** Just return the parsed body and the header
   (header is None when `self.header` is False).

7. **Closing.** Keep the file handle on `self` in `__enter__`; close it in
   `__exit__`. Watch out: if you read everything into memory in `__enter__`, you
   could also close immediately there — either is fine as long as it closes.

## Self-check
`python csvreader.py` -> good.csv prints header + rows; bad.csv prints
"File is corrupted".
