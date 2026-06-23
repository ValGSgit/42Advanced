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
    theStr = ""
    for arg in reversed(user_input):
        if not arg == user_input[-1]:
            theStr += " "
        reversed_arg = arg[::-1] #start=0,stop=0,step=-1
        swapped_case = reversed_arg.swapcase()
        theStr += swapped_case
        
    print(theStr)


if __name__ == "__main__":
    main()
