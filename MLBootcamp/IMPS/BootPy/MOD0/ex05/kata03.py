"""Exercise 05: The right format - kata03

Description:
    Display a string centered with dashes to exactly 42 characters.

Requirements:
    - The kata variable is always a string whose length is not higher than 42.
    - Fill with dashes on the left to reach exactly 42 characters.

Forbidden functions: None
"""

# Put this at the top of your kata03.py file
kata = "The right format"

def main():
    that = f"{kata[:42]:->42}"
    return print(that, end = "")

if __name__ == "__main__":
    main()