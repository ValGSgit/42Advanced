import sys

NESTED_MORSE = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}


def main():
    """Encode a string argument to Morse code."""
    # TODO:
    # 1. Assert exactly 1 argument, and it contains only alphanumeric + space chars
    #    Print "AssertionError: the arguments are bad" if not
    # 2. Encode each character using NESTED_MORSE
    # 3. Separate morse codes with a single space
    # 4. Print the result
    pass


if __name__ == "__main__":
    main()

# Test by running:
#   python sos.py "sos"      -> ... --- ...
#   python sos.py "SOS"      -> ... --- ...
#   python sos.py "h$llo"    -> AssertionError: the arguments are bad
#   python sos.py            -> AssertionError: the arguments are bad
