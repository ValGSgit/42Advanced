#zip() used to combine multiple iterable objects 
#(such as lists, tuples, or strings) into a single iterable of tuples

class Vector:
    def __init__(self, values):
        # Builds a vector from one of four accepted inputs and stores it in a
        # canonical form: self.values is always a list of rows, and self.shape
        # is (rows, cols). The chain of isinstance checks dispatches on the type
        # of `values` to figure out which construction the caller intended.

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

        # From here `values` is a non-empty list. Two layouts are possible: a
        # list of lists (already nested), or a flat list of numbers.
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
        # A row vector is [[a, b, c]], so the single inner list IS the data.
        # A column vector is [[a], [b], [c]], so we pull the lone element out of
        # each row. Either way the caller gets a plain 1-D list to iterate over.
        if self.shape[0] == 1:  # row vector
            return list(self.values[0])

        return [row[0] for row in self.values]  # column vector

    def dot(self, other):
        """Produces a dot product between two vectors of the same shape."""
        # Guard clauses first: both operands must be Vectors of identical shape.
        if not isinstance(other, Vector):
            raise NotImplementedError(
                "Dot product is only defined between two vectors."
            )
        if self.shape != other.shape:
            raise ValueError("Dot product requires vectors of the same shape.")
        # Flatten both to 1-D, pair up matching elements with zip, multiply each
        # pair, and sum the products: a*x + b*y + c*z ...
        return sum(x * y for x, y in zip(self._flatten(), other._flatten()))

    def T(self):
        """Return the transpose: column vector -> row vector, or vice versa."""
        # Transposing just rewraps the data: a row [[a, b, c]] becomes one inner
        # list per element [[a],[b],[c]], and a column does the reverse. Returns
        # a brand-new Vector; the original is left untouched.
        if self.shape[0] == 1:  # row -> column
            return Vector([[x] for x in self.values[0]])
        return Vector([[row[0] for row in self.values]])  # column -> row

    def __add__(self, other):
        """Add two vectors of the same shape element-wise."""
        # Invoked by `self + other`. After the type/shape guards, the nested
        # comprehension walks both vectors in lockstep: the outer zip pairs rows,
        # the inner zip pairs elements within those rows, summing each pair. The
        # result keeps the same nested layout, so Vector(result) preserves shape.
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
        # Reflected add: Python calls this for `other + self` when other's own
        # __add__ doesn't know how to handle a Vector. Addition is commutative,
        # so we just delegate to __add__.
        return self.__add__(other)

    def __sub__(self, other):
        """Subtract two vectors of the same shape element-wise."""
        # Invoked by `self - other`. Same lockstep zip-of-zips as __add__, but it
        # subtracts each paired element instead of adding. Unlike addition this
        # is NOT commutative, so order matters (see __rsub__).
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
        # Reflected subtract for `other - self`. Because subtraction isn't
        # commutative we must compute other - self (not self - other), so we
        # delegate to other.__sub__(self) to keep the operand order correct.
        if not isinstance(other, Vector):
            raise NotImplementedError(
                "Subtraction is only defined between two vectors."
            )
        return other.__sub__(self)

    def __truediv__(self, scalar):
        """Division of a vector by a scalar (only with scalars)."""
        # Invoked by `self / scalar`. Rejects non-numbers and zero, then divides
        # every element by the scalar via a nested comprehension that walks each
        # row. The shape is unchanged, so we wrap the result back in a Vector.
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
        # Reflected divide for `scalar / self`. Dividing a number by a vector has
        # no meaning here, so we always raise rather than return a value.
        raise NotImplementedError(
            "Division of a scalar by a Vector is not defined here."
        )

    def __mul__(self, scalar):
        """Multiply a vector by a scalar (only scalars)."""
        # Invoked by `self * scalar`. Scales every element by the scalar with the
        # same per-row comprehension pattern; shape stays the same.
        if not isinstance(scalar, (int, float)):
            raise NotImplementedError(
                "A vector can only be multiplied by a scalar."
            )
        result = [[x * scalar for x in row] for row in self.values]
        return Vector(result)

    def __rmul__(self, scalar):
        """Multiply a vector by a scalar (only scalars)."""
        # Reflected multiply for `scalar * self`. Scalar multiplication is
        # commutative, so we simply reuse __mul__.
        return self.__mul__(scalar)

    # https://stackoverflow.com/questions/1436703/what-is-the-difference-between-str-and-repr
    def __str__(self):
        # Called by str()/print(). Returns a human-readable view of the raw data.
        return "Vector(%s)" % self.values

    def __repr__(self):
        # Called by repr() and the interactive prompt. Here it mirrors __str__ so
        # the object looks the same however it is displayed.
        return "Vector(%s)" % self.values
