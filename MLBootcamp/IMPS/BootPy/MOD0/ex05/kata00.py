kata = (19, 42, 21)


def main():
    ups = sum(1 for x in kata if isinstance(x, int))
    if ups != 3:
        return print("A value was not a number")
    return print(f"The numbers are: {kata[0]}, {kata[1]}, {kata[2]}")

if __name__ == "__main__":
    main()