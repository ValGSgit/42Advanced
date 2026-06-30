# ex01 — YoungestFellah

## The big idea
Filter a DataFrame by year and sex, then find the minimum age in each group.

## Key pandas operations
| Task | Code |
|---|---|
| Filter by column value | `df[df['Year'] == year]` |
| Filter by sex | `year_df[year_df['Sex'] == 'F']` |
| Minimum of a column | `['Age'].min()` |

## Chain of operations (mental model)
```
df
  → filter Year == 2004          # rows for that Olympic year
  → split by Sex == 'F' / 'M'
  → .min() on Age column
```

## Why `.min()` returns NaN for missing years
If no female athletes exist for that year, the filtered DataFrame is empty and
`.min()` returns `NaN`. That's the correct behaviour — no crash.

## Quick test
```python
from FileLoader import FileLoader
from YoungestFellah import youngest_fellah

loader = FileLoader()
data = loader.load('../data/athlete_events.csv')

print(youngest_fellah(data, 2004))   # e.g. {'f': 13.0, 'm': 14.0}
print(youngest_fellah(data, 1896))   # only men in 1896 → 'f' is NaN
```
