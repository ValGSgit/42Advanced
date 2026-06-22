import sys

def wakawaka(a: int, b: int):
    if a == 0 or b == 0:
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