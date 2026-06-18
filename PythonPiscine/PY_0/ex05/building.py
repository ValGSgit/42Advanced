import sys
import string


def count_chars(text: str) -> None:
    """Count and print upper, lower, punctuation, space, and digit characters."""
    # TODO: count each category in text and print:
    # "The text contains <total> characters:"
    # "<n> upper letters"
    # "<n> lower letters"
    # "<n> punctuation marks"
    # "<n> spaces"
    # "<n> digits"
    #
    # Hint: char.isupper(), char.islower(), char.isdigit(), char.isspace()
    # Hint: char in string.punctuation  (import string at top)
    pass


def main():
    """Entry point: take one string arg or prompt for input."""
    # TODO:
    # 1. If more than one argument: print AssertionError
    # 2. If no argument: prompt "What is the text to count?\n" and read input()
    # 3. Call count_chars on the string
    pass


if __name__ == "__main__":
    main()

# Test by running:
#   python building.py "Hello World!"
# Expected:
#   The text contains 12 characters:
#   2 upper letters
#   8 lower letters
#   1 punctuation marks
#   1 spaces
#   0 digits
