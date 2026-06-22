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
