"""Exercise 04: Elementary

Description:
    Write a program that takes two integers A and B as arguments and
    prints the result of the following operations:
    Sum (A+B), Difference (A-B), Product (A*B), Quotient (A/B), Remainder (A%B)

Requirements:
    - If more or less than two arguments are provided or if one of the
      arguments is not an integer, print an error message.
    - If no argument is provided, do nothing or print an usage.
    - If an operation is impossible, print an error message instead of
      a numerical result.

Forbidden functions: None
"""

import sys

def wakawaka(a: int, b: int):
    if b == 0:
        quot = "ERROR (division by zero)"
        rem = "ERROR (modulo by zero)"
    else:
        quot = a / b
        rem = a % b
    print(f"Sum:\t{a + b}\nDifference:{a - b}\nProduct:{a * b}\nQuotient:{quot}\nRemainder:{rem}\n")
    return 0

def main():
    if len(sys.argv) == 3:
        n1 = sys.argv[1]
        n2 = sys.argv[2]
    elif len(sys.argv) > 3:
        return print("Too many arguments")
    else:
        return print("Usage: python operations.py <n1> <n2>")
    oof = str(n1)
    foo = str(n2)
    try:
        num1 = int(oof)
        num2 = int(foo)
        wakawaka(num1, num2)
    except ValueError:
        return print("AssertionError: argument is not an integer")
    

if __name__ == "__main__":
    main()