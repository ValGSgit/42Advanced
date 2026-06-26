# ex00 — map, filter, reduce

## The big idea
These three are the classic "functional" tools. Each takes **a function** plus
**an iterable** and walks the iterable applying that function.

| tool   | what it does                                   | result          |
|--------|------------------------------------------------|-----------------|
| map    | apply f to **every** element                   | iterable        |
| filter | keep elements where f(element) is **truthy**   | iterable        |
| reduce | **fold** the whole thing into one value        | a single value  |

## Things to understand before coding

1. **Lazy vs eager.** `map` and `filter` are *lazy* — calling them returns a
   generator object immediately and does no work until you iterate (that's why
   the examples print `<generator object ...>` and you must wrap with `list()`).
   The easiest way to be lazy is to write a **generator function** using
   `yield`. `reduce` is *eager* — it must consume everything to produce its one
   value, so it's a normal function that `return`s.

2. **Generators.** A function containing `yield` returns a generator. Each
   `next()` runs until the next `yield`. (You already used this in MOD0 ex10 /
   MOD1 ex03 — same tool.)

3. **`callable(x)`** tells you whether `x` can be called like a function. Useful
   for raising a `TypeError` when someone passes a non-function — that mirrors
   what the real built-ins do.

4. **reduce's fold.** Take the first element as the starting accumulator, then
   for each remaining element do `acc = f(acc, element)`. Think about what
   should happen on an **empty** iterable (the real `reduce` raises a TypeError).
   Look at `iter()` and `next()` to peel off that first element.

## Self-check
- `list(ft_map(lambda t: t + 1, [1,2,3]))` -> `[2, 3, 4]`
- `list(ft_filter(lambda d: not d % 2, [1,2,3,4]))` -> `[2, 4]`
- `ft_reduce(lambda u, v: u + v, list("Hello"))` -> `"Hello"`

Run a file directly: `python ft_map.py`
