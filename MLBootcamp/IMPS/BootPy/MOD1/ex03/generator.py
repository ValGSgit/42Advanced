import random

def generator(text, sep=" ", option=None):
    """
    Splits the text according to sep value and yields the substring
    """
    options = [ "shuffle", "unique", "ordered"]
    if text is None or not isinstance(text, str):
        yield "ERROR"
        return
    if option is not None and option not in options:
        yield "ERROR"
        return
    splitted = text.split(sep=sep, maxsplit=-1)
    if option is None:
        for word in splitted:
            yield word
    elif option == "shuffle":
        """Walks from last to first mixing a random previous number"""
        shuffled = list(splitted)
        for i in range(len(shuffled) - 1, 0, -1):
            j = random.randint(0, i)
            shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
        for word in shuffled:
            yield word
    elif option == "unique":
        """Each word once, keeping first-seen order"""
        for word in dict.fromkeys(splitted):
            yield word
    elif option == "ordered":
        """Alphabetically"""
        for word in sorted(splitted):
            yield word
        

def main():
    text = "Le Lorem Ipsum est simplement du du faux texte."
    print("======No option=====")
    for word in generator(text, sep=" "):
        print(word)

    print("======Shuffle=====")
    for word in generator(text, sep=" ", option="shuffle"):
        print(word)
    
    print("======Ordered=====")
    for word in generator(text, sep=" ", option="ordered"):
        print(word)

    print("======Unique=====")
    for word in generator(text, sep=" ", option="unique"):
        print(word)
    return 0

if __name__ == "__main__":
    main()