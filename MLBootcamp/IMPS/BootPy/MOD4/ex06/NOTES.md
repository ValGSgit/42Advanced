# ex06 — MyPlotLib

## The big idea
Four standard statistical visualisations, each accepting a list of feature names.
Only numerical features are plotted — skip non-numeric ones silently.

## Method-to-plot map
| Method | Plot type | Key call |
|---|---|---|
| `histogram` | Bar histogram | `series.plot.hist(bins=30)` |
| `density` | KDE curve | `series.plot.kde()` |
| `pair_plot` | Scatter matrix | `sns.pairplot(df[features])` |
| `box_plot` | Box & whisker | `series.plot.box()` |

## Checking for numeric dtype
```python
import pandas as pd
pd.api.types.is_numeric_dtype(data[feature])  # True for int/float columns
```
This guards against accidentally passing 'Name' or 'Sport' as a feature.

## Subplots pattern used in histogram / density / box_plot
```python
fig, axes = plt.subplots(1, n_features, figsize=(5 * n_features, 4))
# If n_features == 1, axes is a single Axes, not a list — wrap it:
if n_features == 1:
    axes = [axes]
for ax, feature in zip(axes, num_features):
    data[feature].dropna().plot.hist(ax=ax, ...)
plt.tight_layout()
plt.show()
```

## Quick test
```python
from FileLoader import FileLoader
from MyPlotLib import MyPlotLib

loader = FileLoader()
data = loader.load('../data/athlete_events.csv')
mpl = MyPlotLib()

features = ['Age', 'Height', 'Weight']
mpl.histogram(data, features)
mpl.density(data, features)
mpl.pair_plot(data, features)
mpl.box_plot(data, features)
```

## Libraries
- `matplotlib.pyplot` — all plots except pair plot
- `seaborn` — `pairplot` (handles the diagonal histograms automatically)
- `pandas` plot methods — thin wrappers around matplotlib, very concise
