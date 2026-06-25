"""Exercise 05: The right format - kata00

Description:
    Display a tuple of integers in the specified format.

Requirements:
    - The kata variable is always a tuple and can only be filled with integers.
    - Display: "The 3 numbers are: 19, 42, 21"

Forbidden functions: None
"""

kata = (19, 42, 21)


def main():
    ups = sum(1 for x in kata if isinstance(x, int))
    if ups != 3:
        return print("A value was not a number")
    return print(f"The {len(kata)} numbers are: {kata[0]}, {kata[1]}, {kata[2]}")

if __name__ == "__main__":
    main()