# ex04 — SpatioTemporalData

## The big idea
Two inverse lookups on the Olympics dataset: city→years and year→city.
Both are simple filter + unique operations.

## Method logic

### `when(location)` → list of years
```python
df[df['City'] == location]['Year'].unique()
```
Sort descending so the most recent games come first (matches subject output).

### `where(year)` → list of cities
```python
df[df['Year'] == year]['City'].unique()
```
Returns a list — there's usually one city per year but `.unique()` handles edge cases.

## Key pandas calls
| Task | Code |
|---|---|
| Filter by column value | `df[df['City'] == location]` |
| Unique values | `['Year'].unique()` |
| Convert to list | `.tolist()` |

## Quick test
```python
from FileLoader import FileLoader
from SpatioTemporalData import SpatioTemporalData

loader = FileLoader()
data = loader.load('../data/athlete_events.csv')
sp = SpatioTemporalData(data)

print(sp.where(1896))      # ['Athina']
print(sp.where(2016))      # ['Rio de Janeiro']
print(sp.when('Athina'))   # [2004, 1906, 1896]
print(sp.when('Paris'))    # [1924, 1900]
```
