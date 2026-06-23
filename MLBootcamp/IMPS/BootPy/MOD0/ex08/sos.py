"""Exercise 08: S.O.S

Description:
    Encode a string into Morse code.

Requirements:
    - The program supports space and alphanumeric characters.
    - An alphanumeric character is represented by dots (.) and dashes (-).
    - A space character is represented by a slash (/).
    - Complete morse characters are separated by a single space.
    - If more than one argument is provided, merge them into a single string
      with each argument separated by a single space character.
    - If no argument is provided, do nothing or print an usage.

Forbidden functions: None
"""

import sys

NESTED_MORSE = {
    "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
    "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
    "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..",
    "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
    "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
    "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
    "Y": "-.--",  "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",
    " ": "/",
}


def morse(text: str) -> str:
    text = text.upper()
    assert all(c in NESTED_MORSE for c in text), "argument contains invalid characters"
    return " ".join(NESTED_MORSE[c] for c in text)


def main():
    if len(sys.argv) == 1:
        return print("Usage: python sos.py <str1> <strN>")
    try:
        print(morse(" ".join(sys.argv[1:])))
    except:
        AssertionError
        print("Invalid characters in input")


if __name__ == "__main__":
    main()
