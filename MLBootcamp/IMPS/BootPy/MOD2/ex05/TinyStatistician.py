class TinyStatistician:
    """Basic statistics implemented by hand (no stat helper functions).

    Every method takes a list or numpy.ndarray, returns a float, or None for an
    empty input. Inputs are assumed numeric / well-formed.
    """

    def mean(self, x):
        """µ = (Σ xᵢ) / m. Use a for-loop. Return float, or None if empty.

        HINT: total = 0; loop x adding each; return total / len(x).
        """
        # TODO: your code here
        pass

    def median(self, x):
        """Middle value of the sorted data (avg of the two middles if even).

        HINT: s = sorted(x); n = len(s); pick s[n//2] (odd) or average the two
        central elements (even). Return float.
        """
        # TODO: your code here
        pass

    def quartiles(self, x):
        """Return [Q1, Q3] as floats.

        HINT: s = sorted(x); Q1 = s[int(len(s) * 0.25)],
        Q3 = s[int(len(s) * 0.75)]. Return them as floats in a list.
        """
        # TODO: your code here
        pass

    def var(self, x):
        """Population variance σ² = (1/m) Σ (xᵢ − µ)². Use a for-loop.

        HINT: compute the mean first, then accumulate (xi - mean) ** 2,
        divide by len(x).
        """
        # TODO: your code here
        pass

    def std(self, x):
        """Standard deviation σ = sqrt(var). Use a for-loop (reuse var).

        HINT: return self.var(x) ** 0.5 (handle the empty -> None case).
        """
        # TODO: your code here
        pass


if __name__ == "__main__":
    tstat = TinyStatistician()
    a = [1, 42, 300, 10, 59]
    print(tstat.mean(a))        # 82.4
    print(tstat.median(a))      # 42.0
    print(tstat.quartiles(a))   # [10.0, 59.0]
    print(tstat.var(a))         # 12279.439999999999
    print(tstat.std(a))         # 110.81263465868862
