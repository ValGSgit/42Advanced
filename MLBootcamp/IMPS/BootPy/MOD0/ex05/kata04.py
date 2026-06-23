"""Exercise 05: The right format - kata04

Description:
    Display formatted numbers in various formats.

Requirements:
    - The kata variable contains: 2 non-negative integers (up to 2 digits each),
      1 decimal, 1 integer, 1 decimal.
    - Format with specific precision and scientific notation as required.

Forbidden functions: None
"""

# Put this at the top of your kata04.py file
kata = (0, 4, 132.42222, 10000, 12345.67)

def main():
    return print(f"module_{kata[0]:02}, ex_{kata[1]:02} : {kata[2]:.2f}, {kata[3]:.2e}, {kata[4]:.2e}")

if __name__ == "__main__":
    main()