"""
### Project 1: Refactor "Guess the Number" Game
Refactor the Guess the Number game so that:
- The secret number generation is in its own function
- User input is handled by a separate function
- Guess checking logic is isolated
- The game loop runs through a main `play_game()` function
- Add an option to choose difficulty (easy: 1-50, medium: 1-100, hard: 1-200)
"""
import random


def secret_num_gen(choice):
    ranges = {"1": 50, "2": 100, "3": 200} # A dict mapping each choice to its max number
    high = ranges.get(choice, 100) # .get(choice, 100) returns 50 or 100 or 200 based on choice and incase of invalid choice returns default (100)
    return random.randint(1, high)


def get_user_guess(choice):
    prompts = {"1": "1-50", "2": "1-100", "3": "1-200"}
    prompt = prompts.get(choice, "1-100")

    while True:
        try:
            guess = int(input(f"Enter a number in range({prompt}): "))
            return guess

        except ValueError:
            print("Please enter a valid number.")


def check_guess(secret_num, guess):
    if guess < secret_num:
        return "low"
    elif guess > secret_num:
        return "high"
    else:
        return "correct"


def game_difficulty_menu():
    print("\n   Game Difficulty Menu   ")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-200)")

    while True:
        choice = input("Enter difficulty (1-Easy, 2-Medium, 3-Hard): ")
        if choice in ("1", "2", "3"):
            return choice
        print("Invalid choice. Please enter 1, 2, or 3.")


def play_game():
    print("\n     Guess The Number     ")
    choice = game_difficulty_menu()
    secret = secret_num_gen(choice)
    attempt = 0

    while True:
        guess = get_user_guess(choice)
        attempt += 1
        result = check_guess(secret, guess)

        if result == "low":
            print("Too low!")
        elif result == "high":
            print("Too high!")
        else:
            print(f"Correct guess in {attempt} attempt{'s' if attempt > 1 else ''}!") # Ternary operator
            break # syntax: value_if_true if condition else value_if_false


if __name__ == "__main__":
    play_game()
