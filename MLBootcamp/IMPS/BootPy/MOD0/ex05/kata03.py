# Put this at the top of your kata03.py file
kata = "The right format"

def main():
    that = f"{kata[:42]:->42}"
    return print(that, end = "")

if __name__ == "__main__":
    main()