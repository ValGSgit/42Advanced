# ex02 — ScrapBooker

## The big idea
Four image-manipulation operations implemented purely with NumPy slicing and
concatenation. No loops needed — NumPy does the heavy lifting.

## Methods at a glance

### `crop(array, dim, position=(0,0))`
- `position = (row, col)` — top-left corner of the crop window
- `dim = (height, width)` — size of the output rectangle
- Slice: `array[row : row+height, col : col+width]`
- Return `None` if the window falls outside the array.

### `thin(array, n, axis)`
- `axis=0` → delete every n-th **column** (index n-1, 2n-1, 3n-1, …)
- `axis=1` → delete every n-th **row**
- Key call: `np.delete(array, indices, axis=...)`
- Build indices with `np.arange(n-1, size, n)`

### `juxtapose(array, n, axis)`
- Stick n copies side-by-side (`axis=1`) or top-to-bottom (`axis=0`)
- Key call: `np.concatenate([array] * n, axis=axis)`

### `mosaic(array, dim)`
- `dim = (rows, cols)` — how many times to tile in each direction
- Key call: `np.tile(array, (rows, cols))`

## Coordinate convention
```
(row, col) — row 0 is at the top, col 0 is at the left.
(1, 3) means: 1 row down, 3 columns right → second row, fourth column.
```

## Quick test
```python
import numpy as np
from ScrapBooker import ScrapBooker

spb = ScrapBooker()

arr1 = np.arange(0, 25).reshape(5, 5)
print(spb.crop(arr1, (3, 1), (1, 0)))
# array([[ 5], [10], [15]])

arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1, 9)
print(spb.thin(arr2, 3, 0))   # remove every 3rd column

arr3 = np.array([[1,2,3],[1,2,3],[1,2,3]])
print(spb.juxtapose(arr3, 3, 1))  # 3 × 9

print(spb.mosaic(arr3, (2, 3)))   # 6 × 9 grid
```
