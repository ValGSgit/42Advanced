# Python Piscine for Data Science — Complete Self-Learning Guide

## Global Rules (apply to ALL modules from PY_0 ex05 onward)

```python
def main():
    # your tests and error handling here
    pass

if __name__ == "__main__":
    main()
```

- **No global variables** — everything inside functions
- **No bare imports** — always `import numpy as np`, never `from pandas import *`
- **All functions/classes/methods must have a `__doc__` docstring**
- **No uncaught exceptions** — every exception must be handled
- **Code style**: `pip install flake8` then run `flake8 yourfile.py` before submitting
- **Python version**: 3.10

---

## PY_0 — Starting (Python Basics)

### Concepts to learn before starting

#### 1. Python Data Structures
The 4 core collections you must know cold:

```python
# List — ordered, mutable, allows duplicates
my_list = ["Hello", "World"]
my_list[1] = "France"          # modify by index

# Tuple — ordered, IMMUTABLE
my_tuple = ("Hello", "World")
my_tuple = ("Hello", "France") # must reassign entirely

# Set — unordered, unique values, use {} with NO key:value
my_set = {"Hello", "World"}
my_set = {"Hello", "France"}   # must reassign, no indexing

# Dict — key:value pairs
my_dict = {"Hello": "World"}
my_dict["Hello"] = "France"    # modify by key
```

#### 2. Type system
```python
type(42)          # <class 'int'>
type("hi")        # <class 'str'>
type(3.14)        # <class 'float'>
type(None)        # <class 'NoneType'>
type(True)        # <class 'bool'>

# isinstance check
isinstance(42, int)         # True
isinstance("hi", (int, str)) # True  — check multiple types at once
```

#### 3. sys.argv — command line arguments
```python
import sys

# sys.argv[0] = script name
# sys.argv[1] = first argument passed
# len(sys.argv) = number of items (1 = no args)

args = sys.argv[1:]          # all args except script name
```

#### 4. Assertions
```python
# assert <condition>, "message if false"
assert len(sys.argv) == 2, "more than one argument is provided"
assert arg.lstrip('-').isdigit(), "argument is not an integer"
```

#### 5. String methods
```python
s = "Hello World! 123"
s.isupper()      # False
s.islower()      # False
s.isdigit()      # False
s.isspace()      # False
s.ispunctuation? # no built-in — use: import string; string.punctuation

import string
for char in s:
    if char.isupper():    ...
    elif char.islower():  ...
    elif char.isdigit():  ...
    elif char.isspace():  ...
    elif char in string.punctuation: ...
```

#### 6. Functions and type hints
```python
def my_function(param: any) -> int:
    """This is the docstring — required from ex05 onward."""
    return 42
```

#### 7. Modules and imports
```python
import time
import datetime

# time since epoch
time.time()                    # float: seconds since Jan 1, 1970

# datetime formatting
from datetime import datetime
now = datetime.now()
now.strftime("%b %d %Y")       # "Oct 21 2022"

# scientific notation
f"{num:.2e}"                   # "1.67e+09"
```

#### 8. float special values
```python
import math
math.isnan(float("nan"))   # True
# NaN is a float, not None!
# "Null" types: None, float("nan"), 0, "", False
```

#### 9. List comprehensions and lambda
```python
# List comprehension
squares = [x**2 for x in range(10)]
filtered = [x for x in my_list if condition(x)]

# Lambda — anonymous function
double = lambda x: x * 2

# Filter (built-in)
result = list(filter(lambda x: len(x) > 4, words))

# Re-implement filter with list comprehension:
def ft_filter(function, iterable):
    """Filter elements from iterable based on function."""
    return [x for x in iterable if function(x)]
```

#### 10. Dictionaries deep dive
```python
MORSE = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    # ...
}

# Lookup
MORSE.get("A", "?")   # safe lookup with default

# Build output
result = " ".join(MORSE[c.upper()] for c in text if c.upper() in MORSE)
```

#### 11. Generators and yield
```python
# yield makes a generator function — it "pauses" and returns a value
def ft_tqdm(lst: range) -> None:
    """Clone of tqdm progress bar."""
    total = len(lst)
    for i, elem in enumerate(lst):
        # print progress bar to stderr
        percent = (i + 1) / total
        bar_len = os.get_terminal_size().columns - 30
        filled = int(bar_len * percent)
        bar = "=" * filled + ">" + " " * (bar_len - filled - 1)
        print(f"\r{int(percent*100)}%|{bar}| {i+1}/{total}", end="", flush=True)
        yield elem
    print()
```

#### 12. Creating a Python Package (ex09)
File structure needed:
```
ex09/
├── ft_package/
│   ├── __init__.py       # makes it a package
│   └── your_module.py    # actual code
├── setup.py              # OR pyproject.toml
├── README.md
└── LICENSE
```

`pyproject.toml` (modern way):
```toml
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.backends.legacy:build"

[project]
name = "ft_package"
version = "0.0.1"
description = "A sample test package"
authors = [{name = "eagle", email = "eagle42.fr"}]
license = {text = "MIT"}
```

Build and install:
```bash
pip install build
python -m build           # creates dist/ folder
pip install ./dist/ft_package-0.0.1.tar.gz
pip show -v ft_package    # verify
```

---

### PY_0 Exercise Checklist

| Exercise | File | Key concept |
|----------|------|-------------|
| ex00 | `Hello.py` | list/tuple/set/dict indexing and modification |
| ex01 | `format_ft_time.py` | `time.time()`, `datetime`, f-strings, scientific notation |
| ex02 | `find_ft_type.py` | `type()`, function with return value, module guard |
| ex03 | `NULL_not_found.py` | `None`, `float("nan")`, `math.isnan()`, falsy values |
| ex04 | `whatis.py` | `sys.argv`, `assert`, `% 2` for odd/even |
| ex05 | `building.py` | `sys.argv`, `input()`, `string` module, char classification |
| ex06 | `ft_filter.py` + `filterstring.py` | list comprehensions, `lambda`, custom filter |
| ex07 | `sos.py` | dict lookup, `sys.argv`, Morse code table |
| ex08 | `Loading.py` | `yield`, `os.get_terminal_size()`, progress bar |
| ex09 | package files | `pyproject.toml`, `__init__.py`, `pip install`, `pip show` |

---

## PY_1 — Array (NumPy + Image Processing)

### Concepts to learn before starting

#### 1. NumPy basics
```python
import numpy as np

# Create arrays
arr = np.array([1, 2, 3])
arr2d = np.array([[1, 2], [3, 4]])

# Shape
arr2d.shape       # (2, 2) — (rows, cols)
arr2d.ndim        # 2

# Data types
arr.dtype         # dtype('int64')
```

#### 2. NumPy math with lists (ex00 — BMI)
```python
# Works element-wise on lists of ints/floats
heights = [1.71, 1.15]
weights = [165.3, 38.4]

# BMI = weight / height²
# Convert to numpy arrays to do element-wise math
h = np.array(heights)
w = np.array(weights)
bmi = w / (h ** 2)       # returns list of floats

# apply_limit: True if bmi > limit
result = [b > limit for b in bmi]   # or use np.array(bmi) > limit
```

#### 3. Type validation
```python
def give_bmi(height, weight):
    """..."""
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("Inputs must be lists")
    if len(height) != len(weight):
        raise ValueError("Lists must be same size")
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise TypeError("Elements must be int or float")
```

#### 4. 2D array slicing (ex01)
```python
import numpy as np

family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
arr = np.array(family)

arr.shape          # (4, 2)
arr[0:2]           # rows 0 and 1 — shape (2, 2)
arr[1:-2]          # row 1 to second-to-last

# Slicing syntax: arr[start:end]  (end is exclusive)
# Negative index: arr[-1] = last row
```

#### 5. Loading images as NumPy arrays (ex02–05)
```python
# Option 1: matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread("landscape.jpg")   # returns np.ndarray shape (H, W, 3)
print(img.shape)   # e.g. (257, 450, 3) — height, width, RGB channels
print(img)

# Option 2: PIL/Pillow
from PIL import Image
import numpy as np
img = np.array(Image.open("landscape.jpg"))
```

#### 6. Displaying images (ex03–05)
```python
import matplotlib.pyplot as plt

plt.imshow(img)
plt.show()

# With axis labels (zoom exercise):
fig, ax = plt.subplots()
ax.imshow(img, cmap="gray")
plt.show()
# The axis ticks appear automatically when you use imshow
```

#### 7. Image slicing / zoom (ex03)
```python
# Image array shape: (height, width, channels)
# To "zoom" = take a sub-section
# arr[row_start:row_end, col_start:col_end]

zoomed = img[200:600, 200:600]          # square crop
zoomed_gray = img[200:600, 200:600, 0]  # single channel → grayscale

print(f"New shape after slicing: {zoomed.shape}")
```

#### 8. Transpose (ex04) — DO IT MANUALLY, no library
```python
# Transpose: rows become columns
# For a 2D array: arr[i][j] → arr[j][i]

# Manual transpose with list comprehension:
def manual_transpose(arr):
    """Transpose a 2D array manually."""
    rows, cols = arr.shape
    transposed = [[arr[r][c] for r in range(rows)] for c in range(cols)]
    return np.array(transposed)

# OR using nested loops:
result = np.zeros((cols, rows), dtype=arr.dtype)
for i in range(rows):
    for j in range(cols):
        result[j][i] = arr[i][j]
```

#### 9. Color filters (ex05)
```python
# Image is shape (H, W, 3) — R, G, B channels at index 0, 1, 2
# Operations allowed per filter:

# invert (=, +, -, *): 255 - pixel
inverted = 255 - img

# red (=, *): zero out G and B channels
red = img.copy()
red[:, :, 1] = 0   # G = 0
red[:, :, 2] = 0   # B = 0

# green (=, -): zero out R and B
green = img.copy()
green[:, :, 0] = 0
green[:, :, 2] = 0

# blue (=): zero out R and G
blue = img.copy()
blue[:, :, 0] = 0
blue[:, :, 1] = 0

# grey (=, /): average of RGB
grey = img.mean(axis=2).astype(np.uint8)  # or (R+G+B)/3
```

---

### PY_1 Exercise Checklist

| Exercise | File | Key concept |
|----------|------|-------------|
| ex00 | `give_bmi.py` | numpy element-wise math, type validation, zip |
| ex01 | `array2D.py` | `np.array`, `.shape`, array slicing `[start:end]` |
| ex02 | `load_image.py` | `mpimg.imread` or PIL, print shape and pixel data |
| ex03 | `zoom.py` | image slicing, `plt.imshow`, grayscale, axis display |
| ex04 | `rotate.py` | manual matrix transpose (no `.T` allowed) |
| ex05 | `pimp_image.py` | numpy array arithmetic per channel, color filters |

---

## PY_2 — DataTable (Pandas + Matplotlib)

### Concepts to learn before starting

#### 1. Pandas basics
```python
import pandas as pd

# Load a CSV
df = pd.read_csv("life_expectancy_years.csv", index_col=0)

# Inspect
print(df.shape)        # (195, 302) — rows, cols
print(df)              # full display

# Access a row by label (country name)
france = df.loc["France"]          # Series of years
years = france.index               # column names (years as strings)
values = france.values             # numpy array of values
```

#### 2. Handling missing values and column types
```python
# CSV columns might be strings like "1800", "1801"...
# Convert to int/float for plotting
years = [int(y) for y in df.columns]

# Drop NaN values
series = df.loc["France"].dropna()
```

#### 3. Matplotlib line plots (ex01 — life expectancy)
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(years, values, label="France")
ax.set_title("France Life expectancy Projections")
ax.set_xlabel("Year")
ax.set_ylabel("Life expectancy")
ax.legend()
plt.show()
```

#### 4. Multi-line plot (ex02 — population)
```python
# Plot two countries on same axes
df_pop = pd.read_csv("population_total.csv", index_col=0)

# Filter years 1800–2050
cols_1800_2050 = [c for c in df_pop.columns if 1800 <= int(c) <= 2050]
subset = df_pop[cols_1800_2050]

france = subset.loc["France"]
belgium = subset.loc["Belgium"]
years = [int(y) for y in cols_1800_2050]

ax.plot(years, france.values, label="France")
ax.plot(years, belgium.values, label="Belgium")
ax.legend()

# Format Y axis to show "60M" instead of 60000000:
import matplotlib.ticker as ticker
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{int(x/1e6)}M"))
```

#### 5. Scatter plot (ex03 — GDP vs life expectancy)
```python
df_life = pd.read_csv("life_expectancy_years.csv", index_col=0)
df_gdp = pd.read_csv("income_per_person_gdppercapita_ppp_inflation_adjusted.csv", index_col=0)

# Get values for year 1900
year = "1900"
life_1900 = df_life[year].dropna()
gdp_1900 = df_gdp[year].dropna()

# Align on common countries
common = life_1900.index.intersection(gdp_1900.index)
x = gdp_1900[common]
y = life_1900[common]

ax.scatter(x, y)
ax.set_xscale("log")         # log scale for GDP axis
ax.set_xlim(300, 10000)
ax.set_xticks([300, 1000, 10000])
ax.set_xticklabels(["300", "1k", "10k"])
ax.set_title("1900")
ax.set_xlabel("Gross domestic product")
ax.set_ylabel("Life Expectancy")
```

---

### PY_2 Exercise Checklist

| Exercise | Files | Key concept |
|----------|-------|-------------|
| ex00 | `load_csv.py` | `pd.read_csv`, `.shape`, error handling for bad path |
| ex01 | `load_csv.py`, `aff_life.py` | line plot, title, axis labels, `plt.show()` |
| ex02 | `load_csv.py`, `aff_pop.py` | multi-line plot, legend, year range 1800–2050 |
| ex03 | `load_csv.py`, `projection_life.py` | scatter plot, log scale x-axis, two CSVs |

---

## PY_3 — OOP (Object-Oriented Programming)

### Concepts to learn before starting

#### 1. Classes, `__init__`, and instance attributes
```python
class Dog:
    """Represents a dog."""

    def __init__(self, name: str, is_alive: bool = True):
        """Initialize dog with name and alive status."""
        self.name = name
        self.is_alive = is_alive

    def die(self):
        """Set the dog as dead."""
        self.is_alive = False

d = Dog("Rex")
print(d.__dict__)    # {'name': 'Rex', 'is_alive': True}
print(d.__doc__)     # "Represents a dog."
```

#### 2. Abstract classes (ex00)
```python
from abc import ABC, abstractmethod

class Character(ABC):
    """Abstract base class for characters."""

    @abstractmethod
    def die(self):
        """Abstract method — must be implemented by subclasses."""
        pass

class Stark(Character):
    """Stark family character."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize Stark character."""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Set character as dead."""
        self.is_alive = False

# Character("hodor")  → TypeError: Can't instantiate abstract class
ned = Stark("Ned")
ned.die()
print(ned.is_alive)  # False
```

#### 3. Inheritance and `__str__` / `__repr__` (ex01)
```python
class Baratheon(Character):
    """Baratheon family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize Baratheon."""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Set character as dead."""
        self.is_alive = False

    def __str__(self):
        """Return string for str() calls."""
        return f"({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self):
        """Return string for repr() calls."""
        return f"({self.family_name}, {self.eyes}, {self.hairs})"
```

#### 4. Class methods (factory pattern) (ex01)
```python
class Lannister(Character):
    """Lannister family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize Lannister."""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """..."""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """Create and return a Lannister instance."""
        return cls(first_name, is_alive)

# Usage:
jaine = Lannister.create_lannister("Jaine", True)
print(type(jaine).__name__)   # "Lannister"
```

#### 5. Multiple inheritance and the Diamond Problem (ex02)
```python
# King inherits from BOTH Baratheon and Lannister
class King(Baratheon, Lannister):
    """King — diamond inheritance."""
    pass

# Python uses C3 linearization (MRO) to resolve conflicts
# Check the MRO: King.__mro__
```

#### 6. Properties — `@property` and `@setter` (ex02)
```python
class King(Baratheon, Lannister):
    """King with settable attributes."""

    @property
    def eyes(self):
        """Eye color getter."""
        return self.__eyes

    @eyes.setter
    def eyes(self, value: str):
        """Eye color setter."""
        self.__eyes = value

    def get_eyes(self):
        """Return eye color."""
        return self.eyes

    def set_eyes(self, color: str):
        """Set eye color."""
        self.eyes = color
```

#### 7. Operator overloading (ex03)
```python
class calculator:
    """Calculator that applies operations to a vector."""

    def __init__(self, lst: list):
        """Initialize with a list (vector)."""
        self.lst = list(lst)

    def __add__(self, scalar) -> None:
        """Add scalar to each element."""
        self.lst = [x + scalar for x in self.lst]
        print(self.lst)

    def __sub__(self, scalar) -> None:
        """Subtract scalar from each element."""
        self.lst = [x - scalar for x in self.lst]
        print(self.lst)

    def __mul__(self, scalar) -> None:
        """Multiply each element by scalar."""
        self.lst = [x * scalar for x in self.lst]
        print(self.lst)

    def __truediv__(self, scalar) -> None:
        """Divide each element by scalar."""
        if scalar == 0:
            print("Division by zero")
            return
        self.lst = [x / scalar for x in self.lst]
        print(self.lst)

# v1 = calculator([0, 1, 2, 3])
# v1 + 5   → calls __add__(5)
```

#### 8. Static methods and decorators (ex04)
```python
class calculator:
    """Calculator for vector operations."""

    @staticmethod
    def dotproduct(V1: list, V2: list) -> None:
        """Compute and print dot product of two vectors."""
        result = sum(a * b for a, b in zip(V1, V2))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list, V2: list) -> None:
        """Add two vectors element-wise."""
        result = [float(a + b) for a, b in zip(V1, V2)]
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list, V2: list) -> None:
        """Subtract V2 from V1 element-wise."""
        result = [float(a - b) for a, b in zip(V1, V2)]
        print(f"Sous Vector is: {result}")

# Called WITHOUT instantiation:
# calculator.dotproduct(a, b)
```

---

### PY_3 Exercise Checklist

| Exercise | File | Key concept |
|----------|------|-------------|
| ex00 | `S1E9.py` | `ABC`, `@abstractmethod`, `__init__`, `__dict__`, `__doc__` |
| ex01 | `S1E7.py` | Multi-inheritance, `__str__`, `__repr__`, `@classmethod` |
| ex02 | `DiamondTrap.py` | Diamond inheritance, `@property`, `@setter`, MRO |
| ex03 | `ft_calculator.py` | `__add__`, `__sub__`, `__mul__`, `__truediv__` |
| ex04 | `ft_calculator.py` | `@staticmethod`, dot product, vector addition/subtraction |

---

## Full Project Dependency Map

```
PY_0  →  Python fundamentals (required for ALL modules)
PY_1  →  numpy (pip install numpy matplotlib pillow)
PY_2  →  pandas + matplotlib (pip install pandas matplotlib seaborn)
PY_3  →  OOP concepts (no extra installs)
```

## Install all dependencies at once

```bash
pip install numpy matplotlib pillow pandas seaborn flake8
```

---

## Common Patterns to Memorize

### Error handling pattern
```python
def my_func(path: str):
    """Load something from path."""
    try:
        # do the thing
        pass
    except FileNotFoundError:
        print(f"Error: file '{path}' not found")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
```

### Full program template (from PY_0 ex05 onward)
```python
import sys


def do_something(arg: str) -> None:
    """Does something with arg."""
    # logic here
    pass


def main():
    """Entry point."""
    try:
        assert len(sys.argv) == 2, "wrong number of arguments"
        do_something(sys.argv[1])
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
```

### Module that can be imported OR run directly
```python
# When run: python myfile.py  → main() executes
# When imported: from myfile import my_func  → main() does NOT execute
# This is what the __name__ == "__main__" guard does
```

---

## Quick Reference: flake8 Common Errors

| Error | Meaning | Fix |
|-------|---------|-----|
| E302 | Expected 2 blank lines before function | Add 2 blank lines before `def` at module level |
| E303 | Too many blank lines | Remove extra blank lines |
| W291 | Trailing whitespace | Remove spaces at end of lines |
| E501 | Line too long (>79 chars) | Break line with `\` or parentheses |
| E711 | Comparison to None | Use `is None` not `== None` |
| F401 | Imported but unused | Remove unused import |

Run: `flake8 yourfile.py` — must show zero output to pass norminette.
