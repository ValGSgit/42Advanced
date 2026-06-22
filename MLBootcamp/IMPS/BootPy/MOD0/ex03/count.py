import string
import sys

def text_analyzer(obj=None):
    """takes a single string argument and displays
the total number of printable characters, and respectively : the number of upper-case
characters, lower-case characters, punctuation characters and spaces.
• If None or nothing is provided, the user is prompted to provide a string.
• If the argument is not a string, print an error message"""
    if obj is None:
        obj = input("What is the text to analyze? ")
    if not isinstance(obj, str):
        print("Input is not a string")
        return

    ups = sum(1 for x in obj if x.isupper())
    downs = sum(1 for x in obj if x.islower())
    punks = sum(1 for x in obj if x in string.punctuation)
    spaces = sum(1 for x in obj if x.isspace())
    prints = sum(1 for x in obj if x.isprintable())

    print(f"The text contains {prints} printable character(s):")
    print(f"- {ups} upper letter(s)")
    print(f"- {downs} lower letter(s)")
    print(f"- {punks} punctuation mark(s)")
    print(f"- {spaces} space(s)")


def main():
    if len(sys.argv) == 2:
        user_input = sys.argv[1]
    else:
        return print("Usage: python count.py <Single argument required>")
    text_analyzer(user_input)

if __name__ == "__main__":
    main()
