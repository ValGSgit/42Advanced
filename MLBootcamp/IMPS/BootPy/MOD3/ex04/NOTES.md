# ex04 — K-means Clustering

## The big idea
Implement K-means from scratch with NumPy (no sklearn/scipy allowed).
Apply it to recover the homelands of solar system citizens from biometric data.

## Algorithm steps
1. **Initialise** — randomly pick `ncentroid` rows from X as starting centroids.
2. **Assign** — for each point, find the nearest centroid (L2 distance).
3. **Update** — move each centroid to the mean of its assigned points.
4. Repeat steps 2–3 for `max_iter` iterations (or until centroids stop moving).

## Key NumPy calls
| Task | Call |
|---|---|
| Random initial centroids | `np.random.choice(n_rows, ncentroid, replace=False)` |
| L2 distance (all points to one centroid) | `np.linalg.norm(X - centroid, axis=1)` |
| Assign each point to nearest centroid | `np.argmin(distances, axis=1)` |
| New centroid = mean of cluster | `X[labels == k].mean(axis=0)` |
| Check convergence | `np.allclose(new_centroids, old_centroids)` |

## Distance choice
- **L1** (Manhattan): `np.sum(np.abs(X - c), axis=1)` — faster, less sensitive to outliers.
- **L2** (Euclidean): `np.linalg.norm(X - c, axis=1)` — the standard choice.
- Try both; results vary because K-means is sensitive to initialisation.

## Homeland heuristics (ncentroid=4)
| Homeland | Height | Weight | Bone density |
|---|---|---|---|
| Venus | low | low | medium |
| Earth | medium | medium | medium |
| Mars | high | medium | medium |
| Belt | very high | medium | very low |

Sort centroids by height to label them.

## Running the program
```bash
# from ex04/
python Kmeans.py filepath=../resources/solar_system_census.csv ncentroid=4 max_iter=30
```

## Dataset location
`../resources/solar_system_census.csv`
Columns: `height`, `weight`, `bone_density` (float values).
The `Index` column is ignored.

## Why results vary between runs
K-means picks random starting centroids — different starts → different final clusters.
Run multiple times and keep the best result (lowest total within-cluster variance).
Production libraries do this automatically (`n_init` parameter in sklearn).
