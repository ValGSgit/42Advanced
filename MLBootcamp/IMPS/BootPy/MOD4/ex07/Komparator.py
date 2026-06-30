import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class Komparator:

    def __init__(self, df):
        self.df = df

    def compare_box_plots(self, categorical_var, numerical_var):
        """
        One box plot per category of categorical_var, showing the distribution
        of numerical_var within that category.
        """
        categories = self.df[categorical_var].dropna().unique()
        fig, axes = plt.subplots(1, len(categories),
                                 figsize=(4 * len(categories), 5), sharey=True)
        if len(categories) == 1:
            axes = [axes]
        for ax, cat in zip(axes, sorted(categories)):
            subset = self.df[self.df[categorical_var] == cat][numerical_var].dropna()
            subset.plot.box(ax=ax)
            ax.set_title(str(cat))
            ax.set_xlabel(categorical_var)
        plt.suptitle(f'{numerical_var} by {categorical_var}')
        plt.tight_layout()
        plt.show()

    def density(self, categorical_var, numerical_var):
        """
        Overlaid KDE curves for numerical_var, one curve per category of categorical_var.
        """
        fig, ax = plt.subplots(figsize=(8, 5))
        for cat, group in self.df.groupby(categorical_var):
            group[numerical_var].dropna().plot.kde(ax=ax, label=str(cat))
        ax.set_title(f'Density of {numerical_var} by {categorical_var}')
        ax.set_xlabel(numerical_var)
        ax.legend()
        plt.tight_layout()
        plt.show()

    def compare_histograms(self, categorical_var, numerical_var):
        """
        Separate histogram per category, all on the same figure (overlapping, colour-coded).
        """
        fig, ax = plt.subplots(figsize=(8, 5))
        for cat, group in self.df.groupby(categorical_var):
            group[numerical_var].dropna().plot.hist(
                ax=ax, bins=30, alpha=0.5, label=str(cat))
        ax.set_title(f'{numerical_var} by {categorical_var}')
        ax.set_xlabel(numerical_var)
        ax.legend()
        plt.tight_layout()
        plt.show()
