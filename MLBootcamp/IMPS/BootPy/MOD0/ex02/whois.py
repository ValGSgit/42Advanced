"""Exercise 02: The Odd, the Even and the Zero

Description:
    Make a program that takes a number as argument, checks whether it is
    odd, even or zero, and prints the result.

Requirements:
    - If more than one argument is provided or if the argument is not
      an integer, print an error message.
    - If no argument is provided, do nothing or print an usage.

Forbidden functions: None
"""

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