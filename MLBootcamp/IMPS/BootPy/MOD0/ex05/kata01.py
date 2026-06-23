"""Exercise 05: The right format - kata01

Description:
    Display a dictionary in the specified format.

Requirements:
    - The kata variable is always a dictionary and can only be filled with strings.
    - Format: "<Language> was created by <Creator>"

Forbidden functions: None
"""

# Put this at the top of your kata01.py file
kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

def main():
    for language, creator in kata.items():
        print(f"{language} was created by {creator}")

if __name__ == "__main__":
    main()