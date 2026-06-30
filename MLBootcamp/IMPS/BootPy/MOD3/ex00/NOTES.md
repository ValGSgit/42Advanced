# ex00 — NumPyCreator

## The big idea
Practice converting different Python data structures into NumPy arrays.
Each method wraps one (or two) NumPy calls.

## Key NumPy functions used
| Method | NumPy call |
|---|---|
| `from_list` | `np.array(lst)` |
| `from_tuple` | `np.array(tpl)` |
| `from_iterable` | `np.array(list(itr))` |
| `from_shape` | `np.full(shape, value)` |
| `random` | `np.random.random(shape)` |
| `identity` | `np.eye(n)` |

## Gotchas to understand
- **Jagged list** (`[[1,2,3],[6,4]]`) → NumPy builds a 1-D array of Python lists
  (dtype=object). Return `None` in that case.
- `from_list` must reject non-list input (e.g. a tuple passed to it → `None`).
- `from_tuple` must reject non-tuple input.
- Mixed-type lists (`[1,'a',2]`) are fine — NumPy upcasts to string (U21). Return it.
- The `dtype` bonus arg is just forwarded to `np.array(..., dtype=dtype)` or
  `np.full(..., dtype=dtype)`.

## Quick test
```python
from NumPyCreator import NumPyCreator
npc = NumPyCreator()

print(npc.from_list([[1,2,3],[6,3,4]]))    # 2-D array
print(npc.from_list([[1,2,3],[6,4]]))       # None (jagged)
print(npc.from_tuple(("a","b","c")))        # 1-D string array
print(npc.from_tuple(["a","b","c"]))        # None (list, not tuple)
print(npc.from_iterable(range(5)))          # [0 1 2 3 4]
print(npc.from_shape((3,5)))                # 3×5 zeros
print(npc.from_shape((3,5), 7))             # 3×5 sevens
print(npc.random((3,5)))                    # 3×5 floats in [0,1)
print(npc.identity(4))                      # 4×4 identity matrix
```
