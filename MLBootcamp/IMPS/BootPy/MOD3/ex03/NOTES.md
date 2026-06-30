# ex03 — ColorFilter

## The big idea
Apply colour transformations to float32 images (shape `H × W × 3`, values in
`[0.0, 1.0]`) using only the specific operators the subject allows for each method.

## Method-by-method breakdown

### `invert`
- Allowed: `.copy`, `+`, `-`, `=`
- Formula: `result = 1 - array`  (flips each channel around 0.5)

### `to_blue`
- Allowed: `.copy`, `.zeros`, `.shape`, `.dstack`, `=`
- Strategy: build two zero planes, keep the blue channel, stack them:
  `np.dstack((zeros, zeros, array[:,:,2]))`

### `to_green`
- Allowed: `.copy`, `*`, `=`
- Strategy: multiply R and B channels by 0 in place.

### `to_red`
- Allowed: `.copy`, `to_green`, `to_blue`, `-`, `+`, `=`
- Strategy: `red = array - green_version - blue_version`
  (removing green and blue leaves only red)

### `to_celluloid`
- Allowed: `.copy`, `.arange`, `.linspace`, `.min`, `.max`, `=`, `<=`, `>`, `&`
- Strategy: create N thresholds with `np.linspace(min, max, N+1)`, then for each
  band set all pixels in that band to the lower threshold value.
- Need **at least 4 thresholds** (so 4 shades).

### `to_grayscale`
- Allowed: `.sum`, `.shape`, `.reshape`, `.broadcast_to`, `.astype`, `*`, `/`, `=`
- `'mean'/'m'`: weights = `[1/3, 1/3, 1/3]`
- `'weight'/'w'`: weights from kwargs `r_weight`, `g_weight`, `b_weight`
- Multiply channels by weights, sum along channel axis → shape `(H, W)`.
- Reshape to `(H, W, 1)` then `broadcast_to` shape `(H, W, 3)`.

## Broadcasting refresher
```python
# array[:,:,:3] has shape (H, W, 3)
# weights has shape (3,)
# NumPy broadcasts: (H,W,3) * (3,) → (H,W,3)  ✓
gray = (array[:,:,:3] * weights).sum(axis=2)   # shape (H, W)
gray = gray.reshape(H, W, 1)                   # shape (H, W, 1)
gray = np.broadcast_to(gray, (H, W, 3))        # shape (H, W, 3)
```

## Quick test
```python
import sys; sys.path.insert(0, '../ex01')
from ImageProcessor import ImageProcessor
from ColorFilter import ColorFilter

imp = ImageProcessor()
arr = imp.load("your_image.png")

cf = ColorFilter()
imp.display(cf.invert(arr))
imp.display(cf.to_blue(arr))
imp.display(cf.to_green(arr))
imp.display(cf.to_red(arr))
imp.display(cf.to_celluloid(arr))
imp.display(cf.to_grayscale(arr, 'm'))
imp.display(cf.to_grayscale(arr, 'weight', r_weight=0.2, g_weight=0.3, b_weight=0.5))
```
