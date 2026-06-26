# ex01 — Rev Alpha (string reversal + swapcase)

## The big idea
Take CLI arguments, merge them into one string, **reverse** it, then **swap
the case** of every letter (uppercase → lowercase and vice-versa).

```
python exec.py "Hello World"  →  "DLROw OLLEh"
python exec.py Hello World    →  "DLROw OLLEh"   (two args merged)
```

## Things to understand before coding

1. **`sys.argv`.** `sys.argv[0]` is the script name; `sys.argv[1:]` is the
   list of user-provided arguments. Check `len(sys.argv) > 1` to know if
   anything was passed.

2. **Merging multiple args.** `" ".join(sys.argv[1:])` collapses the list into
   a single string with spaces between each argument.

3. **Reversing a string.** Python slice `s[::-1]` returns the string backwards.
   Step `-1` means start at the end and move left.

4. **`.swapcase()`.** Built-in string method; no imports needed.
   `"Hello".swapcase()` → `"hELLO"`.

5. **Order matters.** Reverse first, then swapcase — or swapcase first then
   reverse; both give the same result since the operations are independent.

## Self-check
```
python exec.py "Hello World"
# expected: DLROw OLLEh
python exec.py
# expected: usage message (no crash)
```
