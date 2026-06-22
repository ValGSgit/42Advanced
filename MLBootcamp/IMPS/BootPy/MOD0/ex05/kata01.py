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