class Vector:
    def __init__(self, values):
        # Vector(int) -> column vector [[0.0], [1.0], ..., [n-1.0]]
        if isinstance(values, int):
            if values <= 0:
                raise ValueError("size must be a positive integer")
            self.values = [[float(i)] for i in range(values)]
            self.shape = (values, 1)
            return

        # Vector((a, b)) -> column vector [[a], [a+1], ..., [b-1]]
        if isinstance(values, tuple):
            if len(values) != 2 or not all(isinstance(x, int) for x in values):
                raise ValueError("range must be a tuple of 2 integers")
            a, b = values
            if a > b:
                raise ValueError(
                    "invalid range: first value (%d) is greater than second (%d)"
                    % (a, b)
                )
            self.values = [[float(i)] for i in range(a, b)]
            self.shape = (b - a, 1)
            return

        if not isinstance(values, list) or len(values) == 0:
            raise ValueError("values must be a non-empty list")

        if all(isinstance(v, list) for v in values):  # if all values are lists
            # one list with only numbers -> row vector [[1, 2, 3]]
            if len(values) == 1 and all(
                isinstance(x, (int, float)) for x in values[0]
            ):
                if len(values[0]) == 0:
                    raise ValueError("values must be a non-empty vector")
                self.values = [[float(x) for x in values[0]]]
                self.shape = (1, len(values[0]))
            # every inner list has exactly one number -> column vector [[1], [2]]
            elif all(
                len(v) == 1 and isinstance(v[0], (int, float)) for v in values
            ):
                self.values = [[float(v[0])] for v in values]
                self.shape = (len(values), 1)
            else:
                raise ValueError("values must be a row or column vector")
        elif all(isinstance(x, (int, float)) for x in values):
            self.values = [[float(x) for x in values]]
            self.shape = (1, len(values))
        else:
            raise ValueError(
                "values must be a list of floats or a list of lists of floats"
            )

    def _flatten(self):
        """Return the vector elements as a flat list of floats."""
        if self.shape[0] == 1:  # row vector
            return list(self.values[0])
        return [row[0] for row in self.values]  # column vector

    def dot(self, other):
        """Produces a dot product between two vectors of the same shape."""
        if not isinstance(other, Vector):
            raise NotImplementedError(
                "Dot product is only defined between two vectors."
            )
        if self.shape != other.shape:
            raise ValueError("Dot product requires vectors of the same shape.")
        return sum(x * y for x, y in zip(self._flatten(), other._flatten()))

    def T(self):
        """Return the transpose: column vector -> row vector, or vice versa."""
        if self.shape[0] == 1:  # row -> column
            return Vector([[x] for x in self.values[0]])
        return Vector([[row[0] for row in self.values]])  # column -> row

    def __add__(self, other):
        """Add two vectors of the same shape element-wise."""
        if not isinstance(other, Vector):
            raise NotImplementedError(
                "Addition is only defined between two vectors."
            )
        if self.shape != other.shape:
            raise ValueError("Addition requires vectors of the same shape.")
        result = [
            [a + b for a, b in zip(row_a, row_b)]
            for row_a, row_b in zip(self.values, other.values)
        ]
        return Vector(result)

    def __radd__(self, other):
        """Add only if vectors of the same shape."""
        return self.__add__(other)

    def __sub__(self, other):
        """Subtract two vectors of the same shape element-wise."""
        if not isinstance(other, Vector):
            raise NotImplementedError(
                "Subtraction is only defined between two vectors."
            )
        if self.shape != other.shape:
            raise ValueError("Subtraction requires vectors of the same shape.")
        result = [
            [a - b for a, b in zip(row_a, row_b)]
            for row_a, row_b in zip(self.values, other.values)
        ]
        return Vector(result)

    def __rsub__(self, other):
        """Subtract only if vectors of the same shape (other - self)."""
        if not isinstance(other, Vector):
            raise NotImplementedError(
                "Subtraction is only defined between two vectors."
            )
        return other.__sub__(self)

    def __truediv__(self, scalar):
        """Division of a vector by a scalar (only with scalars)."""
        if not isinstance(scalar, (int, float)):
            raise NotImplementedError(
                "A vector can only be divided by a scalar."
            )
        if scalar == 0:
            raise ZeroDivisionError("division by zero.")
        result = [[x / scalar for x in row] for row in self.values]
        return Vector(result)

    def __rtruediv__(self, scalar):
        """Division of a scalar by a vector is not defined."""
        raise NotImplementedError(
            "Division of a scalar by a Vector is not defined here."
        )

    def __mul__(self, scalar):
        """Multiply a vector by a scalar (only scalars)."""
        if not isinstance(scalar, (int, float)):
            raise NotImplementedError(
                "A vector can only be multiplied by a scalar."
            )
        result = [[x * scalar for x in row] for row in self.values]
        return Vector(result)

    def __rmul__(self, scalar):
        """Multiply a vector by a scalar (only scalars)."""
        return self.__mul__(scalar)

    # https://stackoverflow.com/questions/1436703/what-is-the-difference-between-str-and-repr
    def __str__(self):
        return "Vector(%s)" % self.values

    def __repr__(self):
        return "Vector(%s)" % self.values
