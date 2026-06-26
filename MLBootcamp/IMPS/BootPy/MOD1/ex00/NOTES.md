# ex00 — OOP: Recipe and Book

## The big idea
Introduce **classes** as blueprints for objects. Two classes work together:
- `Recipe` — holds data for one dish (name, level, time, ingredients, type).
- `Book` — acts as a container, grouping recipes by type.

## Things to understand before coding

1. **`__init__` is the constructor.** It runs automatically when you call
   `Recipe(...)`. Use it to store validated attributes on `self`.

2. **Validation in `__init__`.** Check each argument's type and range before
   storing. Raise `ValueError` with a clear message if invalid. Use
   `isinstance(x, bool)` to reject booleans when you want a plain `int`
   (because `bool` is a subclass of `int` in Python).

3. **`__str__`.** Called by `str(obj)` and `print(obj)`. Return a formatted
   string — the subject specifies exactly which fields to include and in what
   order.

4. **`datetime.now()`.** `from datetime import datetime` lets you record the
   creation and last-update timestamps on the Book.

5. **Nested dict for recipes.** `Book.recipes_list` stores three lists under
   the keys `"starter"`, `"lunch"`, `"dessert"`. Adding a recipe appends to
   the correct list using `recipe.recipe_type` as the key.

6. **`get_recipe_by_name`.** Must search all three sub-lists (loop over
   `.values()` of the dict). Return `None` if not found.

7. **Type guard in `add_recipe`.** Reject anything that isn't a `Recipe`
   instance with `isinstance(recipe, Recipe)`.

## Self-check
Run `python test.py` — you should see:
- `str(tourte)` printed with all fields.
- Successful lookups and a "not found" case.
- An error message for `add_recipe("not a recipe")` (not a crash).
- `last_update` changes after adding recipes.
