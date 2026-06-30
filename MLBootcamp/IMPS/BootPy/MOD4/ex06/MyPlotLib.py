import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class MyPlotLib:

    def histogram(self, data, features):
        """One histogram per numerical feature in the list."""
        num_features = [f for f in features if pd.api.types.is_numeric_dtype(data[f])]
        if not num_features:
            return
        fig, axes = plt.subplots(1, len(num_features), figsize=(5 * len(num_features), 4))
        if len(num_features) == 1:
            axes = [axes]
        for ax, feature in zip(axes, num_features):
            data[feature].dropna().plot.hist(ax=ax, bins=30, edgecolor='black')
            ax.set_title(feature)
            ax.set_xlabel(feature)
        plt.tight_layout()
        plt.show()

    def density(self, data, features):
        """Density (KDE) curve for each numerical feature."""
        num_features = [f for f in features if pd.api.types.is_numeric_dtype(data[f])]
        if not num_features:
            return
        fig, axes = plt.subplots(1, len(num_features), figsize=(5 * len(num_features), 4))
        if len(num_features) == 1:
            axes = [axes]
        for ax, feature in zip(axes, num_features):
            data[feature].dropna().plot.kde(ax=ax)
            ax.set_title(feature)
            ax.set_xlabel(feature)
        plt.tight_layout()
        plt.show()

    def pair_plot(self, data, features):
        """Scatter plot matrix; diagonal shows histograms."""
        num_features = [f for f in features if pd.api.types.is_numeric_dtype(data[f])]
        if not num_features:
            return
        sns.pairplot(data[num_features].dropna())
        plt.show()

    def box_plot(self, data, features):
        """One box plot per numerical feature."""
        num_features = [f for f in features if pd.api.types.is_numeric_dtype(data[f])]
        if not num_features:
            return
        fig, axes = plt.subplots(1, len(num_features), figsize=(4 * len(num_features), 5))
        if len(num_features) == 1:
            axes = [axes]
        for ax, feature in zip(axes, num_features):
            data[feature].dropna().plot.box(ax=ax)
            ax.set_title(feature)
        plt.tight_layout()
        plt.show()
