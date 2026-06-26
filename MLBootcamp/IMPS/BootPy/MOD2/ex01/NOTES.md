# ex01 — *args and **kwargs

## The big idea
You want a function that accepts **any** number of positional and keyword
arguments and turns each of them into an attribute on an object.

- `*args`   collects extra **positional** arguments into a **tuple**.
- `**kwargs` collects extra **keyword** arguments into a **dict**.

```python
def f(*args, **kwargs):
    ...
f(7)                 # args = (7,)            kwargs = {}
f(1, 2, a=10)        # args = (1, 2)          kwargs = {"a": 10}
```

## Things to understand before coding

1. **Dynamic attributes.** You don't know the attribute names in advance, so you
   can't write `obj.x = 1`. Use the string-based versions:
   - `setattr(obj, "name", value)`  ==  `obj.name = value`
   - `getattr(obj, "name")`          ==  `obj.name`
   - `hasattr(obj, "name")`          -> True/False

2. **Naming the positionals.** The expected output names them `var_0`, `var_1`,
   ... so build the name with `f"var_{i}"` while looping with `enumerate(args)`.

3. **Keywords keep their own name.** Loop `kwargs.items()` and setattr each.

4. **The conflict case.** Look at the example that prints `ERROR`:
   `what_are_the_vars(42, a=10, var_0="world")`. The positional already created
   `var_0`, and the keyword tries to set `var_0` again -> return **None**.
   `hasattr` is your friend for detecting that.

5. **Modify the instance, not the class.** Do the setattr on `obj` (the instance
   you create inside the function), never on `ObjectC` itself.

## Self-check
Run `python main.py` and compare against the expected output in the subject.
The 6th call must print `ERROR` / `end`.
