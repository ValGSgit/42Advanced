# ex00 — FileLoader

## The big idea
A thin wrapper around `pd.read_csv` that prints dataset dimensions and exposes
`head`/`tail` for quick previewing. Every subsequent exercise copies this file
into its own folder and uses it.

## Key pandas calls
| Task | Call |
|---|---|
| Load CSV | `pd.read_csv(path)` |
| Shape (rows, cols) | `df.shape` → `(32561, 15)` |
| First n rows | `df.head(n)` |
| Last n rows | `df.tail(n)` |

## Gotchas
- `display(df, 0)` → do nothing (neither head nor tail makes sense).
- No exceptions should escape the class — wrap everything in try/except.
- `n` is negative → pass `-n` to `tail()`, e.g. `df.tail(-n)`.

## Quick test
```python
from FileLoader import FileLoader
loader = FileLoader()
data = loader.load('../data/adult_data.csv')   # prints "Loading dataset of dimensions 32561 x 15"
loader.display(data, 5)     # first 5 rows
loader.display(data, -3)    # last 3 rows
loader.display(data, 0)     # no output
loader.load('bad_path.csv') # no crash, returns None
```
