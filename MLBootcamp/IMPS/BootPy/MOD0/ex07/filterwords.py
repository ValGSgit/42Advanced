import sys
import string

def filtah(S: str, N :int):
    """Removes punctuation marks for space splitted words if the stripped word is more than N"""
    return [word.strip(string.punctuation) for word in S.split() if len(word.strip(string.punctuation)) > N] #easy right?

def main():
    """In S, find WORDS longer than N while S not punctuation or space"""
    if len(sys.argv) != 3:
        return print("ERROR")
    try:
        dealwith = sys.argv[1]
        by = int(sys.argv[2])
    except ValueError:
        return print("ERROR")

    if not isinstance(dealwith, str):
        return print("ERROR")

    print(filtah(dealwith, by))

if __name__ == "__main__":
    main()