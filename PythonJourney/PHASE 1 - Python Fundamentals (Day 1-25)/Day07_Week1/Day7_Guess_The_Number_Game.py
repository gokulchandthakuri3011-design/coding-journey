"""
## 🎯 Main Task: "Guess the Number" Game

Your primary project for today is to build a classic "Guess the Number" game. This will test your ability to use variables, loops, conditional statements, and user input all together.

### The Rules:
1.  The program should randomly select a number between 1 and 100. *(Hint: You will need to use `import random` and `random.randint(1, 100)` at the top of your file to generate the secret number).*
2.  The user should be prompted to guess the number.
3.  If the user's guess is too high, the program should print "Too high! Try again."
4.  If the user's guess is too low, the program should print "Too low! Try again."
5.  If the user guesses correctly, the program should congratulate them and tell them how many attempts it took.
6.  The game should continue looping until the user guesses the correct number.
"""
import random
secret_number = random.randint(1, 100) # Includes Num 1-100 including both 1 & 100
attempts = 0
print("\n --- Guess The Number Game --- \n")

# Start the game loop
while True:
    
    # Prompt the user for their guess
    guess = int(input("Guess the number between 1 and 100: "))
    attempts += 1 # Increase the attempt count

    # Check if the guess is correct
    if guess < secret_number:
        print(f"Too low! Try again.")
    elif guess > secret_number:
        print(f"Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts!")
        break # Exit the loop when the guess is correct
print("-------------------------------")

