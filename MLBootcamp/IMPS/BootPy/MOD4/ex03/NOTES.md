# ex03 — HowManyMedals

## The big idea
For a given athlete name, aggregate their medal counts by year.
The subject output includes years where the athlete competed but won zero medals
(e.g. 1998 with {'G':0,'S':0,'B':0}) — include all years they appear in the dataset,
not just medal-winning years.

## Wait — the subject shows 1998 with zeros
That means the function should include every year the athlete competed, not just
medal years. Adjust the filter: filter by name only (no medal filter), then within
each year count medals.

## Revised logic
```python
athlete = df[df['Name'] == name]          # all rows for this athlete
for year, group in athlete.groupby('Year'):
    result[year] = {
        'G': (group['Medal'] == 'Gold').sum(),
        'S': (group['Medal'] == 'Silver').sum(),
        'B': (group['Medal'] == 'Bronze').sum(),
    }
```
`Medal` is NaN for non-medal events, so `== 'Gold'` on NaN → False automatically.

## Key pandas calls
| Task | Code |
|---|---|
| Filter by athlete name | `df[df['Name'] == name]` |
| Group by year | `df.groupby('Year')` |
| Count matching values | `(group['Medal'] == 'Gold').sum()` |
| Check for NaN | `df['Medal'].notna()` |

## Quick test
```python
from FileLoader import FileLoader
from HowManyMedals import how_many_medals

loader = FileLoader()
data = loader.load('../data/athlete_events.csv')

print(how_many_medals(data, 'Kjetil Andr Aamodt'))
# Expected:
# {1992: {'G': 1, 'S': 0, 'B': 1},
#  1994: {'G': 0, 'S': 2, 'B': 1},
#  1998: {'G': 0, 'S': 0, 'B': 0},
#  2002: {'G': 2, 'S': 0, 'B': 0},
#  2006: {'G': 1, 'S': 0, 'B': 0}}
```
