# Module 04 — Pandas

## Module goal
Learn to load, filter, aggregate, and visualise large tabular datasets using Pandas
(and Matplotlib / Seaborn for plots).

## Exercise map
| Exercise | Files | Topic |
|---|---|---|
| ex00 | `FileLoader.py` | Load CSV → DataFrame; head/tail display |
| ex01 | `FileLoader.py`, `YoungestFellah.py` | Filter + min aggregation |
| ex02 | `FileLoader.py`, `ProportionBySport.py` | Filter + count + ratio; drop_duplicates |
| ex03 | `FileLoader.py`, `HowManyMedals.py` | groupby + value counts per athlete |
| ex04 | `FileLoader.py`, `SpatioTemporalData.py` | Two-way lookup (city↔year) |
| ex05 | `FileLoader.py`, `HowManyMedalsByCountry.py` | Country medals; team-sport deduplication |
| ex06 | `MyPlotLib.py` | histogram, density, pair_plot, box_plot |
| ex07 | `Komparator.py`, `MyPlotLib.py` | Compare distributions across categories |

## Datasets
| File | Rows × Cols | Used in |
|---|---|---|
| `data/adult_data.csv` | 32 561 × 15 | ex00 |
| `data/athlete_events.csv` | ~207 k × 15 | ex01–ex07 |

Regenerate with: `cd data && python generate_datasets.py`

## Key Pandas operations (progressive difficulty)
```
ex00  read_csv, shape, head, tail
ex01  boolean indexing, .min()
ex02  compound filter &, drop_duplicates, len()
ex03  groupby, value_counts via boolean sum
ex04  .unique(), .tolist()
ex05  .isin(), ~mask, pd.concat, .notna()
ex06  .plot.hist / .kde / .box, seaborn pairplot
ex07  groupby iteration, alpha overlapping histograms
```

## FileLoader is copied into every exercise folder
Each exercise imports it from its own directory. The implementation is identical
in all copies — edit one and copy if you make improvements.

## Setup
```bash
pip install pandas matplotlib seaborn
```
All three are already installed in this environment.
