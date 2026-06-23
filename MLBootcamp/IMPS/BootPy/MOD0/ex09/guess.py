"""Exercise 09: Secret number

Description:
    Interactive guessing game where the user must find a random number between 1 and 99.
    The program tells the user if their guess is too high or too low.

Requirements:
    - Import random module with randint function to get a random number.
    - Count the number of trials and print when user wins.
    - Game ends when user finds the secret number or types 'exit'.
    - If user discovers the secret number on the first try, tell them!
    - If the secret number is 42, make a reference to Douglas Adams.

Forbidden functions: None
"""

from random import randint


def main():
    """Main guessing game function."""
    secret_number = randint(1, 99)
    attempts = 0
    
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!")
    
    while True:
        user_input = input("What's your guess between 1 and 99?\n>> ")
        
        if user_input == "exit":
            print("Goodbye!")
            break
        
        try:
            guess = int(user_input)
        except ValueError:
            print("That's not a number.")
            continue
        
        attempts += 1
        
        if guess == secret_number:
            if secret_number == 42:
                print("The answer to the ultimate question of life, the universe and everything is 42.")
                if attempts == 1:
                    print("Congratulations! You got it on your first try!")
                else:
                    print(f"Congratulations, you've got it!")
                    print(f"You won in {attempts} attempts!")
            else:
                if attempts == 1:
                    print("Congratulations! You got it on your first try!")
                else:
                    print("Congratulations, you've got it!")
                    print(f"You won in {attempts} attempts!")
            break
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Too low!")


if __name__ == "__main__":
    main()
