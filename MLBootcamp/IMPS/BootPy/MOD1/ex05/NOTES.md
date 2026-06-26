# ex05 — The Bank (account corruption detection and repair)

## The big idea
A `Bank` manages `Account` objects. An account is considered **corrupted** if
any of several structural rules are violated. `transfer()` refuses to move
money between corrupted accounts; `fix_account()` repairs them.

## Corruption rules (all must pass for an account to be valid)

| rule                                    | check                                   |
|-----------------------------------------|-----------------------------------------|
| Odd number of attributes                | `len(account.__dict__) % 2 != 0`        |
| No attribute starting with `'b'`        | no key in `__dict__` starts with `'b'`  |
| Has a `zip`- or `addr`-starting attr    | at least one such key exists            |
| Has `name`, `id`, and `value`           | all three keys present                  |
| `name` is str, `id` is int, `value` is int/float |                                |

## Things to understand before coding

1. **`__dict__`.** Every instance stores its attributes in a plain dict at
   `instance.__dict__`. You can read, add, and delete attributes through it
   directly using `setattr` / `delattr` / `hasattr`.

2. **`**kwargs` in `Account.__init__`.** `self.__dict__.update(kwargs)` is a
   one-liner that mass-sets any keyword argument as an instance attribute.
   This is why accounts can have arbitrary extra attributes (and become corrupt).

3. **`fix_account` strategy.**
   1. Drop all `'b'`-prefix attributes with `delattr`.
   2. Add an `addr` attribute if no zip/addr attribute exists.
   3. If the count is still even, add a `fixed = True` attribute to make it odd.
   4. Return `not self.is_corrupt(account)` to confirm the fix succeeded.

4. **Transfer guards.**
   - Both names must be strings; amount must be a non-negative number.
   - Both accounts must exist and pass `is_corrupt`.
   - Sender must have enough funds (`sender.value >= amount`).
   - Same-account transfer is valid (return True, move nothing).

5. **`is_corrupt` returns a list of issues.** An empty list means valid.
   Check `if self.is_corrupt(account):` (empty list is falsy).

## Self-check
Run `python banking_test1.py`, `banking_test2.py`, `banking_test3.py` and
`banking_test_issues.py`. All transfers should return the value described in
the test comments; `fix_account` should make corrupted accounts transferable.
