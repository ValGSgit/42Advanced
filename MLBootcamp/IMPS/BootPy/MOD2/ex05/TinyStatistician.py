class TinyStatistician:
    """Basic statistics implemented by hand (no stat helper functions).

    Every method takes a list or numpy.ndarray, returns a float, or None for an
    empty input. Inputs are assumed numeric / well-formed.
    """

    def mean(self, x):
        """µ = (Σ xᵢ) / m. Use a for-loop. Return float, or None if empty.

        HINT: total = 0; loop x adding each; return total / len(x).
        """
        if len(x) == 0:
            return None
        total = 0
        for num in x:
            total += num
        return total / len(x)

    def median(self, x):
        """Middle value of the sorted data (avg of the two middles if even).

        HINT: s = sorted(x); n = len(s); pick s[n//2] (odd) or average the two
        central elements (even). Return float.
        """
        if len(x) == 0:
            return None
        s = sorted(x)
        n = len(s)
        if n % 2 == 0:
            avg = (s[n // 2 - 1] + s[n // 2]) / 2.0
        else:
            avg = float(s[n // 2])
        return avg


    def quartiles(self, x):
        """Return [Q1, Q3] as floats.

        HINT: s = sorted(x); Q1 = s[int(len(s) * 0.25)],
        Q3 = s[int(len(s) * 0.75)]. Return them as floats in a list.
        """
        if len(x) == 0:
            return None
        s = sorted(x)
        Q1 = float(s[int(len(s) * 0.25)])
        Q3 = float(s[int(len(s) * 0.75)])
        return [Q1, Q3]

    def var(self, x):
        """Population variance σ² = (1/m) Σ (xᵢ − µ)². Use a for-loop.

        HINT: compute the mean first, then accumulate (xi - mean) ** 2,
        divide by len(x).
        """
        mean = self.mean(x)
        if mean is None:
            return None
        total = 0
        for num in x:
            total += (num - mean) ** 2
        return total / len(x)

    def std(self, x):
        """Standard deviation σ = sqrt(var). Use a for-loop (reuse var).

        HINT: return self.var(x) ** 0.5 (handle the empty -> None case).
        """
        v = self.var(x)
        if v is None:
            return None
        return v ** 0.5


if __name__ == "__main__":
    tstat = TinyStatistician()
    a = [1, 42, 300, 10, 59]
    print(tstat.mean(a))        # 82.4
    print(tstat.median(a))      # 42.0
    print(tstat.quartiles(a))   # [10.0, 59.0]
    print(tstat.var(a))         # 12279.439999999999
    print(tstat.std(a))         # 110.81263465868862
