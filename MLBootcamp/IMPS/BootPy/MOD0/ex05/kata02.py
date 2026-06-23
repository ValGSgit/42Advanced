"""Exercise 05: The right format - kata02

Description:
    Display a date/time tuple in DD/MM/YYYY HH:MM format.

Requirements:
    - The kata variable is always a tuple that contains 5 non-negative integers.
    - First integer: up to 4 digits (year), rest: up to 2 digits each.
    - Format with leading zeros as needed.

Forbidden functions: None
"""

# Put this at the top of your kata02.py file
kata = (2019, 9, 25, 3, 30)

def main():
    return print(f"{kata[1]:02}/{kata[2]:02}/{kata[0]:04} {kata[3]:02}:{kata[4]:02}")

if __name__ == "__main__":
    main()
