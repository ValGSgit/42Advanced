# ex02 — The Odd, the Even and the Zero

## The big idea
Read exactly one CLI argument, parse it as an integer, and print whether it is
zero, even, or odd. Reject anything that isn't a single valid integer.

## Things to understand before coding

1. **Argument count guard.** `len(sys.argv) == 2` means exactly one argument
   was provided (the script name is `sys.argv[0]`). More or fewer → usage/error.

2. **Parsing with try/except.** `int(s)` raises `ValueError` if `s` is not a
   valid integer literal. Wrap it to catch non-numeric input gracefully.

3. **Order of checks.** Check zero first (`num == 0`), then even (`num % 2 == 0`),
   then odd — because 0 passes the even check too (`0 % 2 == 0`).

4. **`%` (modulo).** Returns the remainder after division. If `num % 2 == 0`
   the number divides evenly by 2 → even.

## Self-check
```
python whois.py 0      # Is Zero
python whois.py 4      # Is Even
python whois.py 3      # Is weird, in other words odd
python whois.py abc    # AssertionError: argument is not an integer
python whois.py 1 2    # usage message
```
