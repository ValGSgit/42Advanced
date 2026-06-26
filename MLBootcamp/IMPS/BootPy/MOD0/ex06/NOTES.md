# ex06 — The Cookbook (dict manipulation)

## The big idea
Build an interactive CLI menu that manages a dictionary of recipes. Each
recipe is itself a dict with `ingredients`, `meal`, and `prep_time` keys.

```python
cookbook = {
    "Sandwich": {"ingredients": [...], "meal": "lunch", "prep_time": 10},
    ...
}
```

## Things to understand before coding

1. **Nested dicts.** `cookbook["Sandwich"]["ingredients"]` navigates two
   levels. Accessing an inner key always goes through the outer key first.

2. **Dict iteration patterns.**
   - `cookbook.keys()` — iterate only over recipe names
   - `cookbook.items()` — iterate over `(name, recipe_dict)` pairs
   - `cookbook.values()` — iterate over the inner dicts

3. **Case-insensitive lookup.** Compare `.lower()` versions when searching by
   name so `"sandwich"` matches `"Sandwich"`. Never mutate the stored key.

4. **Deleting from a dict while iterating.** Iterating `cookbook.keys()` while
   deleting raises a `RuntimeError`. Fix: iterate `list(cookbook.keys())` which
   creates a snapshot copy first.

5. **Input loop for ingredients.** Ask for one ingredient per line; break when
   the user enters an empty string. This is the idiomatic way to collect a
   variable-length list from stdin.

6. **Menu loop structure.** A `while True` loop that reads a choice, dispatches
   to the right function, and breaks only when the user picks "Quit".

## Self-check
Run `python recipe.py` and test each option (1–5). Verify:
- Adding a recipe, then printing it, shows the new entry.
- Deleting a recipe, then printing the cookbook, omits it.
- Invalid option prints "Sorry, this option does not exist."
