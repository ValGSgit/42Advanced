# ex09 — Secret number (guessing game)

## The big idea
Generate a secret random integer in [1, 99] and let the user guess it. After
each wrong guess tell them "Too high!" or "Too low!". Count attempts and
celebrate when they get it right. Allow `"exit"` to quit early.

## Things to understand before coding

1. **`random.randint(a, b)`.** Returns a random integer N such that `a <= N <= b`
   (both endpoints inclusive). Import: `from random import randint`.

2. **Input loop.** A `while True` loop is the right structure: keep asking until
   the user guesses correctly or types `"exit"`. Use `break` for both exit
   conditions.

3. **`int()` validation.** `int(user_input)` raises `ValueError` on non-numeric
   input. Catch it and `continue` the loop instead of crashing.

4. **Attempt counter.** Increment only on valid numeric guesses (after the
   try/except), not on invalid inputs or `"exit"`.

5. **Special cases.**
   - First try: print a special message (`attempts == 1`).
   - Secret is 42: print the Douglas Adams reference before the congratulation.

6. **No `sys.argv` here.** Everything comes from `input()` inside the loop.

## Self-check
Run `python guess.py` and play through a few rounds:
- Verify "Too high!" / "Too low!" messages.
- Verify attempt count in the winning message.
- Verify the Douglas Adams message triggers when secret == 42 (keep restarting
  until you hit it, or temporarily hardcode `secret_number = 42` to test).
