# ex03 — Generator (word splitter with options)

## The big idea
Write `generator(text, sep, option)` as a generator function that splits a
string and yields words one at a time, with optional transformations: plain,
shuffled, unique (deduplicated), or alphabetically ordered.

## Things to understand before coding

1. **`yield` makes a generator.** A function with `yield` doesn't execute its
   body when called — it returns a generator object. The body runs on each
   `next()` call. Use `return` (with no value) to stop early.

2. **Error yielding.** When input is invalid (not a string, bad option), yield
   `"ERROR"` then `return`. This keeps the function a generator even in the
   error path.

3. **`str.split(sep, maxsplit=-1)`.** Splits on `sep`; `-1` means no limit.
   Default `sep=" "` splits on single spaces.

4. **Shuffle (Fisher-Yates).** Walk from the last index down to 1; at each
   position `i` swap with a random index `j` in `[0, i]`. This produces a
   uniform random permutation. Do it on a copy so the original isn't mutated.
   ```python
   for i in range(len(lst) - 1, 0, -1):
       j = random.randint(0, i)
       lst[i], lst[j] = lst[j], lst[i]
   ```

5. **Unique (first-seen order).** `dict.fromkeys(iterable)` preserves insertion
   order and drops duplicates — cleaner than tracking a `seen` set manually.

6. **Ordered.** `sorted(lst)` returns a new alphabetically sorted list.

## Self-check
Run `python generator.py`. Verify:
- No option: all words in order.
- Shuffle: same words, different order each run.
- Ordered: alphabetical.
- Unique: `"du"` appears only once even though it appears twice in the text.
