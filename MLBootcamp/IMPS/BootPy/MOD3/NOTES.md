# Module 03 — NumPy

## Module goal
Learn to manipulate multi-dimensional arrays (vectors/matrices) and perform
mathematical operations on them using the NumPy library.

## Exercise map
| Exercise | File | Topic |
|---|---|---|
| ex00 | `NumPyCreator.py` | Creating arrays from lists, tuples, iterables, shapes, random, identity |
| ex01 | `ImageProcessor.py` | Loading PNGs → float32 arrays; displaying with matplotlib |
| ex02 | `ScrapBooker.py` | Array slicing: crop, thin, juxtapose, mosaic |
| ex03 | `ColorFilter.py` | Broadcasting: invert, colour channel filters, cel-shading, grayscale |
| ex04 | `Kmeans.py` | K-means clustering from scratch on biometric dataset |

## Dependency chain
```
ex01 (ImageProcessor)
   └──> ex03 (ColorFilter)  ← needs load/display from ex01
```
ex00, ex02, ex04 are independent.

## Key NumPy concepts per exercise
- **ex00**: `np.array`, `np.full`, `np.random.random`, `np.eye`
- **ex01**: `mpimg.imread`, dtype normalisation (uint8 → float32 / 255)
- **ex02**: array slicing `arr[r:r+h, c:c+w]`, `np.delete`, `np.concatenate`, `np.tile`
- **ex03**: broadcasting `(H,W,3) * (3,)`, `np.dstack`, `np.linspace`, `np.broadcast_to`
- **ex04**: `np.linalg.norm`, `np.argmin`, array indexing with boolean masks

## Setup
```bash
pip install numpy matplotlib pillow
```
Both are already installed in this environment.

## Resources
- Dataset: `resources/solar_system_census.csv`  (run `resources/generate_dataset.py` to regenerate)
- Subject PDF: Module03_Numpy.pdf

## Running ex04
```bash
cd ex04
python Kmeans.py filepath=../resources/solar_system_census.csv ncentroid=4 max_iter=30
```
