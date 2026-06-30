# ex02 — ProportionBySport

## The big idea
Calculate what fraction of athletes of a given gender competed in a specific sport
during a given Olympic year. The tricky part: drop duplicates the right way so
team-sport players don't inflate the counts.

## Step-by-step logic
```
df
 → filter Year == year                       # only that games
 → filter Sex == gender                      # only that gender
 → drop_duplicates(subset=['Name','Sport'])  # each athlete counts once per sport
 → count rows (total athletes)
 → count rows where Sport == sport
 → return sport_count / total
```

## Why drop duplicates on (Name, Sport)?
An athlete in a team sport (e.g. basketball) has one row per game played, but
should count as a single participant. Dropping on `['Name', 'Sport']` collapses
those rows before counting.

## Key pandas calls
| Task | Code |
|---|---|
| Boolean filter | `df[(df['Year'] == year) & (df['Sex'] == gender)]` |
| Drop duplicates | `df.drop_duplicates(subset=['Name', 'Sport'])` |
| Count rows | `len(df)` or `df.shape[0]` |

## Quick test
```python
from FileLoader import FileLoader
from ProportionBySport import proportion_by_sport

loader = FileLoader()
data = loader.load('../data/athlete_events.csv')

print(proportion_by_sport(data, 2004, 'Tennis', 'F'))  # ~0.019
print(proportion_by_sport(data, 2016, 'Basketball', 'M'))
```
