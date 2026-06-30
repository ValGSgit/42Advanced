# ex05 — HowManyMedalsByCountry

## The big idea
Same structure as ex03 but grouped by country, with the added complexity that
team sports should only count one medal per team event (not one per player).

## The team-sport deduplication problem
In the dataset, every player on a gold-medal basketball team has their own row
with `Medal = 'Gold'`. Without deduplication, a 12-player team would add 12
gold medals. The fix: for team sports, deduplicate on `(Year, Sport, Event, Medal)`.

## Strategy
```
country rows
  ├── individual sports  →  keep all medal rows as-is
  └── team sports        →  drop_duplicates(['Year','Sport','Event','Medal'])
combine → filter Medal not NaN → groupby Year → count G/S/B
```

## Key pandas calls
| Task | Code |
|---|---|
| Filter team sports | `df[df['Sport'].isin(TEAM_SPORTS)]` |
| Exclude team sports | `df[~df['Sport'].isin(TEAM_SPORTS)]` |
| Deduplicate | `df.drop_duplicates(subset=[...])` |
| Combine DataFrames | `pd.concat([df1, df2])` |
| Filter non-NaN | `df[df['Medal'].notna()]` |

## Quick test
```python
from FileLoader import FileLoader
from HowManyMedalsByCountry import how_many_medals_by_country

loader = FileLoader()
data = loader.load('../data/athlete_events.csv')

result = how_many_medals_by_country(data, 'United States')
for year in sorted(result)[-5:]:
    print(year, result[year])
```
