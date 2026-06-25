"""Exercise 01: Rev Alpha

Description:
    Make a program that takes a string as argument, reverses it,
    swaps its letters case and prints the result.

Requirements:
    - If more than one argument is provided, merge them into a single string
      with each argument separated by a single space character.
    - If no argument is provided, do nothing or print an usage.

Forbidden functions: None
"""

import sys

def main():
    if len(sys.argv) > 1:
        user_input = sys.argv[1:]
    else:
        return print("Usage: python exec.py <str1> <str2> <str69> <etc>")
    merged = " ".join(user_input)
    theStr = merged[::-1].swapcase() #reverse the whole string, then swap case
    print(theStr)


if __name__ == "__main__":
    main()
