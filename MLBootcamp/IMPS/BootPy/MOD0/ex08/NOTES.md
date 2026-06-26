# ex08 — S.O.S (Morse code encoder)

## The big idea
Encode a string into International Morse Code. Letters and digits map to dots
and dashes; spaces become `/`; complete characters are space-separated.

```
python sos.py SOS   →   ... --- ...
python sos.py Hello World   →   .... . .-.. .-.. --- / .-- --- .-. .-..
```

## Things to understand before coding

1. **Dict lookup table.** Store the mapping in a module-level dict constant
   `NESTED_MORSE`. Keys are uppercase letters `"A"–"Z"`, digits `"0"–"9"`, and
   `" "` (space → `"/"`). Look up each character: `NESTED_MORSE[c]`.

2. **Normalise to uppercase.** `text.upper()` before encoding so the user can
   type lowercase freely.

3. **`assert` for validation.** `assert all(c in NESTED_MORSE for c in text)`
   raises `AssertionError` if any character has no Morse equivalent. Catch it
   in `main()` and print a user-friendly error.

4. **`" ".join(...)`.** Join the encoded characters with a single space.
   A generator expression works perfectly:
   ```python
   " ".join(NESTED_MORSE[c] for c in text)
   ```

5. **Merging multi-word input.** Same as ex01: `" ".join(sys.argv[1:])` turns
   multiple CLI args into one string with spaces preserved.

## Self-check
```
python sos.py SOS
# ... --- ...
python sos.py "Hello World"
# .... . .-.. .-.. --- / .-- --- .-. .-.. -..
python sos.py "Hello@"
# Invalid characters in input
```
