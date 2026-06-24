from vector import Vector


def main():
    # ----- Construction -----
    print("=== Construction ===")
    a = Vector([[0.0, 1.0, 2.0, 3.0]])       # row vector
    b = Vector([[0.0], [1.0], [2.0], [3.0]])  # column vector
    c = Vector(3)                             # size -> [[0.0], [1.0], [2.0]]
    d = Vector((10, 16))                      # range -> [[10.0], ..., [15.0]]
    print("a =", a, "shape", a.shape)
    print("b =", b, "shape", b.shape)
    print("c =", c, "shape", c.shape)
    print("d =", d, "shape", d.shape)

    # Range with a > b must raise an explicit error
    try:
        Vector((16, 10))
    except ValueError as e:
        print("Vector((16, 10)) ->", e)

    # ----- Transpose -----
    print("\n=== Transpose ===")
    print("a.T() =", a.T(), "shape", a.T().shape)
    print("b.T() =", b.T(), "shape", b.T().shape)

    # ----- Dot product -----
    print("\n=== Dot product ===")
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
    print("v1.dot(v2) =", v1.dot(v2))          # 18.0
    v3 = Vector([[1.0, 3.0]])
    v4 = Vector([[2.0, 4.0]])
    print("v3.dot(v4) =", v3.dot(v4))          # 14.0

    # ----- Addition / Subtraction (same shape) -----
    print("\n=== Addition / Subtraction ===")
    x = Vector([[1.0], [2.0], [3.0]])
    y = Vector([[4.0], [5.0], [6.0]])
    print("x + y =", x + y)                    # [[5.0], [7.0], [9.0]]
    print("x - y =", x - y)                    # [[-3.0], [-3.0], [-3.0]]
    print("y - x =", y - x)                    # [[3.0], [3.0], [3.0]]

    # ----- Multiplication (mul & rmul) with a scalar float-----
    print("\n=== Multiplication (int) ===")
    v = Vector([[0.0], [1.0], [2.0], [3.0]])
    print("v * 5 =", v * 5)                    # [[0.0], [5.0], [10.0], [15.0]]
    print("5 * v =", 5 * v)                    # same (rmul)
    r = Vector([[0.0, 1.0, 2.0, 3.0]])
    print("r * 5 =", r * 5)

    # ----- Multiplication (mul & rmul) with a scalar int-----
    print("\n=== Multiplication (float) ===")
    v = Vector([[0.0], [1.0], [2.0], [3.0]])
    print("v * 5 =", v * 5.69)                    # [[0.0], [5.0], [10.0], [15.0]]
    print("5 * v =", 5.69 * v)                    # same (rmul)
    r = Vector([[0.0, 1.0, 2.0, 3.0]])
    print("r * 5 =", r * 5.42)

    # ----- Division (truediv) with a scalar -----
    print("\n=== Division ===")
    print("r / 2.0 =", r / 2.0)                # [[0.0, 0.5, 1.0, 1.5]]
    try:
        r / 0.0
    except ZeroDivisionError as e:
        print("r / 0.0 ->", e)

    # ----- rtruediv raises NotImplementedError -----
    # (Comment this block out to run the rest without interruption.)
    print("\n=== Scalar / Vector (rtruediv) ===")
    try:
        2.0 / r
    except NotImplementedError as e:
        print("2.0 / r ->", e)


if __name__ == "__main__":
    main()
