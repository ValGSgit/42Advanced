# ex07 — Komparator

## The big idea
Compare the distribution of a *numerical* variable across the categories of a
*categorical* variable. Three different views of the same comparison.

## Method comparison
| Method | Shows | Best for |
|---|---|---|
| `compare_box_plots` | One box per category, side by side | Comparing medians & spread |
| `density` | Overlaid KDE curves, one per category | Seeing distribution shape differences |
| `compare_histograms` | Overlapping histograms (alpha=0.5) | Raw count differences |

## Example intuition — Sex vs Height
- `compare_box_plots('Sex', 'Height')` → two box plots, one for M one for F
- `density('Sex', 'Height')` → two KDE curves on the same axes
- `compare_histograms('Sex', 'Height')` → two overlapping histograms

## Key pandas/matplotlib patterns

### Iterate over categories
```python
for cat, group in self.df.groupby(categorical_var):
    group[numerical_var].dropna().plot.kde(ax=ax, label=str(cat))
```

### Alpha for overlap
```python
.plot.hist(bins=30, alpha=0.5, label=str(cat))
```
`alpha=0.5` makes bars semi-transparent so overlapping histograms are both visible.

### sharey for box plots
```python
plt.subplots(..., sharey=True)  # all subplots share the same y-axis scale
```

## Quick test
```python
from FileLoader import FileLoader
from Komparator import Komparator

loader = FileLoader()
data = loader.load('../data/athlete_events.csv')
k = Komparator(data)

k.compare_box_plots('Sex', 'Height')
k.density('Sex', 'Age')
k.compare_histograms('Sex', 'Weight')
k.compare_box_plots('Medal', 'Age')   # age distribution by medal type
```

## Note on the bonus
To accept a list of numerical variables, wrap the body of each method in a
`for numerical_var in numerical_vars:` loop (or use an `if isinstance` check
to handle both single string and list inputs).
