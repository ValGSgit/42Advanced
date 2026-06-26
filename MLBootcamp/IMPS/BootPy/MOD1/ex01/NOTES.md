# ex01 — Inheritance: Game of Thrones families

## The big idea
Practice **class inheritance**. A parent class `GotCharacter` holds common
attributes (`first_name`, `is_alive`). Child classes `Stark` and `Lannister`
extend it with family-specific data and behaviour.

```
GotCharacter
├── Stark      (family_name, house_words, print_house_words, die)
└── Lannister  (family_name, house_words, print_house_words, die)
```

## Things to understand before coding

1. **`super().__init__(...)`.** The child's `__init__` must call the parent's
   `__init__` to initialise the shared attributes. If you skip this, `self.first_name`
   and `self.is_alive` won't exist.

2. **Inherited attributes.** Any attribute set on `self` in the parent's
   `__init__` is automatically available in the child. No need to redeclare.

3. **Default arguments.** `def __init__(self, first_name=None, is_alive=True):`
   lets you create a character without specifying every value:
   `Stark()` → name None, alive True.

4. **`die()` method.** Simply sets `self.is_alive = False`. The subject wants
   a method rather than direct attribute assignment so the behaviour can be
   overridden later.

5. **`__dict__`.** Every instance has a `__dict__` showing all its current
   attributes as a plain Python dict. Useful for debugging.

6. **`__doc__`.** The docstring of the class, accessible as `ClassName.__doc__`
   or `instance.__doc__`.

## Self-check
Uncomment the print blocks in `game.py` and run `python game.py`. Verify:
- `x.family_name` → `"Stark"`, `b.family_name` → `"Lannister"`
- `x.is_alive` starts `True`; after `x.die()` it's `False`.
- `x.__dict__` shows all instance attributes.
