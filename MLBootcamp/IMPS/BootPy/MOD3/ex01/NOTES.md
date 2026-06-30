# ex01 — ImageProcessor

## The big idea
A thin wrapper around matplotlib that loads a PNG into a float32 NumPy array
(shape `H × W × 3`, values in `[0.0, 1.0]`) and displays it in a window.
Every upstream exercise (ex02–ex04) imports this class.

## Key calls
| Task | Call |
|---|---|
| Read PNG → array | `matplotlib.image.imread(path)` |
| Convert uint8→float32 | `arr.astype(np.float32) / 255.0` |
| Display array as image | `plt.imshow(array); plt.show()` |

## Error handling
- `FileNotFoundError` (file doesn't exist) → print message, return `None`
- `OSError` (exists but not a valid image / empty) → print message, return `None`

## Array shape to keep in mind
```
arr.shape  →  (height, width, channels)   # channels = 3 for RGB, 4 for RGBA
```
The subject prints `width x height` in the success message.

## Quick test
```python
from ImageProcessor import ImageProcessor
imp = ImageProcessor()

arr = imp.load("no_such_file.png")   # prints exception, arr is None
print(arr)

# put any PNG in this folder and try:
arr = imp.load("test.png")           # prints "Loading image of dimensions W x H"
print(arr.shape, arr.dtype)          # e.g. (200, 200, 3) float32
imp.display(arr)                     # opens a window
```
