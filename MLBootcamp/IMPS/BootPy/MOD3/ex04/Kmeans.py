import sys
import numpy as np
import csv


class KmeansClustering:

    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid
        self.max_iter = max_iter
        self.centroids = []

    def fit(self, X):
        """Initialise centroids randomly from X, then iterate until convergence."""
        # Pick ncentroid random rows as starting centroids
        indices = np.random.choice(X.shape[0], self.ncentroid, replace=False)
        self.centroids = X[indices].copy()

        for _ in range(self.max_iter):
            labels = self.predict(X)

            new_centroids = np.array([
                X[labels == k].mean(axis=0) if (labels == k).any() else self.centroids[k]
                for k in range(self.ncentroid)
            ])

            if np.allclose(new_centroids, self.centroids):
                break
            self.centroids = new_centroids

    def predict(self, X):
        """Return cluster index for each row in X (L2 distance)."""
        # distances shape: (n_samples, ncentroid)
        distances = np.array([
            np.linalg.norm(X - c, axis=1) for c in self.centroids
        ]).T
        return np.argmin(distances, axis=1)


def parse_args(argv):
    params = {}
    for arg in argv:
        if '=' in arg:
            key, value = arg.split('=', 1)
            params[key] = value
    return params


def load_csv(filepath):
    """Load solar_system_census CSV, return feature matrix and header."""
    with open(filepath, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    features = ['height', 'weight', 'bone_density']
    X = np.array([[float(row[feat]) for feat in features] for row in rows])
    return X, features


REGION_HINTS = {
    # ncentroid=4 case: match cluster to homeland by centroid characteristics.
    # Belt: tallest, lowest bone density
    # Mars: taller than Earth
    # Earth: medium
    # Venus: slenderest (lowest weight relative to height)
    4: ["Venus", "Earth", "Mars", "Belt"]
}


def identify_region(centroids):
    """
    Heuristic: sort clusters by height to guess homeland (ncentroid=4 only).
    Belt → tallest+lowest bone density, Venus → lowest weight/height ratio.
    """
    n = len(centroids)
    if n != 4:
        return [f"Cluster {i}" for i in range(n)]

    # height is index 0, weight index 1, bone_density index 2
    order = np.argsort(centroids[:, 0])  # sort by height ascending
    labels = [""] * n
    labels[order[0]] = "Venus"     # shortest → Venus (slender)
    labels[order[1]] = "Earth"
    labels[order[2]] = "Mars"
    labels[order[3]] = "Belt"      # tallest → Belt
    return labels


def main():
    params = parse_args(sys.argv[1:])
    filepath = params.get('filepath', '../resources/solar_system_census.csv')
    max_iter = int(params.get('max_iter', 20))
    ncentroid = int(params.get('ncentroid', 5))

    X, features = load_csv(filepath)

    km = KmeansClustering(max_iter=max_iter, ncentroid=ncentroid)
    km.fit(X)

    labels = km.predict(X)
    regions = identify_region(km.centroids)

    print("\nCentroid coordinates (height, weight, bone_density):")
    for i, (c, region) in enumerate(zip(km.centroids, regions)):
        count = int((labels == i).sum())
        print(f"  Centroid {i} [{region}]: {c}  —  {count} individuals")

    # Optional scatter plots (3 pairs of features)
    try:
        import matplotlib.pyplot as plt
        pairs = [(0, 1, 'height', 'weight'),
                 (0, 2, 'height', 'bone_density'),
                 (1, 2, 'weight', 'bone_density')]
        colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red',
                  'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray']

        fig, axes = plt.subplots(1, 3, figsize=(15, 5))
        for ax, (xi, yi, xl, yl) in zip(axes, pairs):
            for k in range(ncentroid):
                mask = labels == k
                ax.scatter(X[mask, xi], X[mask, yi],
                           c=colors[k % len(colors)],
                           label=regions[k], alpha=0.5, s=10)
                ax.scatter(km.centroids[k, xi], km.centroids[k, yi],
                           c=colors[k % len(colors)], marker='X', s=200,
                           edgecolors='black')
            ax.set_xlabel(xl)
            ax.set_ylabel(yl)
            ax.legend()
        plt.tight_layout()
        plt.show()
    except Exception:
        pass


if __name__ == "__main__":
    main()
