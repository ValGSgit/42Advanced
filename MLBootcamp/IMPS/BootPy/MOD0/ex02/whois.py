import sys

def main():
    if len(sys.argv) == 2:
        user_input = sys.argv[1]
    else:
        return print("Usage: python exec.py <Single argument required>")
    oof = str(user_input)
    try:
        num = int(oof)
        if int(num) % 2 == 0:
            print("Is Even")
        else:
            print("Is weird, in other words odd")
    except ValueError:
        return print("AssertionError: argument is not an integer")
    


if __name__ == "__main__":
    main()