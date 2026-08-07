# Day 21: Mini-Project (Functions)

## Goal
Refactor previous projects to be fully driven by functions, focusing on code reuse, modularity, and clean program structure.

---

## 1. What is Refactoring?
Refactoring means restructuring existing code without changing its behavior. The goal is to make code:
- **Readable** — easier to understand at a glance
- **Reusable** — same logic used in multiple places
- **Maintainable** — bugs are easier to find and fix
- **Testable** — individual functions can be tested in isolation

---

## 2. Why Use Functions?
Without functions, code is written top-to-bottom in one long block. Functions help you:
- **Break problems into small pieces** — each function does one thing
- **Avoid repetition** — write once, call many times
- **Make code modular** — swap or update parts independently
- **Improve readability** — descriptive function names act as documentation

---

## 3. Modular Code Structure
A well-structured program follows this pattern:

```python
# --- Helper Functions ---
def get_user_input():
    ...

def process_data(data):
    ...

def display_result(result):
    ...

# --- Main Program ---
def main():
    data = get_user_input()
    result = process_data(data)
    display_result(result)

if __name__ == "__main__":
    main()
```

### Key Points
- `main()` acts as the entry point and controls the flow
- Each function handles one responsibility
- `if __name__ == "__main__"` ensures code runs only when executed directly (not when imported)

---

## 4. Before vs After Refactoring

### Before (all code in one block)
```python
import random

secret = random.randint(1, 100)
guess = 0
attempts = 0

print("Welcome to Guess the Number!")
print("I'm thinking of a number between 1 and 100.")

while guess != secret:
    guess = int(input("Your guess: "))
    attempts += 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"You got it in {attempts} attempts!")
```

### After (fully function-driven)
```python
import random

def get_secret_number(low=1, high=100):
    return random.randint(low, high)

def get_player_guess():
    while True:
        try:
            guess = int(input("Your guess: "))
            return guess
        except ValueError:
            print("Please enter a valid number.")

def check_guess(guess, secret):
    if guess < secret:
        return "low"
    elif guess > secret:
        return "high"
    else:
        return "correct"

def play_game():
    secret = get_secret_number()
    attempts = 0

    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = get_player_guess()
        attempts += 1
        result = check_guess(guess, secret)

        if result == "low":
            print("Too low!")
        elif result == "high":
            print("Too high!")
        else:
            print(f"You got it in {attempts} attempts!")
            break

if __name__ == "__main__":
    play_game()
```

### What changed?
| Aspect | Before | After |
|--------|--------|-------|
| Input handling | Inline | `get_player_guess()` |
| Game logic | Mixed with I/O | `check_guess()` |
| Entry point | No clear start | `play_game()` + `main` guard |
| Reusability | None | Functions can be imported and reused |

---

## 5. Tips for Refactoring
1. **Extract repeated code** into a function
2. **Name functions clearly** — `calculate_average()` not `calc()`
3. **Keep functions short** — ideally under 20 lines
4. **Minimize parameters** — aim for 3 or fewer
5. **One function = one job** (Single Responsibility Principle)
6. **Return values instead of printing** — let the caller decide what to do with results
7. **Use default parameters** for common values
8. **Add docstrings** to explain what each function does

---

## 6. Project Questions

### Project 1: Refactor "Guess the Number" Game
Refactor the Guess the Number game so that:
- The secret number generation is in its own function
- User input is handled by a separate function
- Guess checking logic is isolated
- The game loop runs through a main `play_game()` function
- Add an option to choose difficulty (easy: 1-50, medium: 1-100, hard: 1-200)

### Project 2: Refactor "FizzBuzz"
Convert FizzBuzz into a function-driven program:
- A function that checks if a number is fizz, buzz, fizzbuzz, or normal
- A function that runs FizzBuzz over a given range
- A main function that asks the user for the range and displays results

### Project 3: Refactor "Interactive Calculator"
Refactor the calculator so that:
- Each operation (add, subtract, multiply, divide) is its own function
- A dispatcher function calls the correct operation based on user choice
- Division by zero is handled inside the divide function
- The calculator loop is managed by a `run_calculator()` function

### Project 4: Refactor "Contact Book"
Refactor the Contact Book project from Week 2:
- `add_contact(contacts, name, phone)` — adds a new contact
- `search_contact(contacts, name)` — finds and returns a contact
- `delete_contact(contacts, name)` — removes a contact
- `display_contacts(contacts)` — prints all contacts
- `main()` — runs the CLI menu loop

### Project 5: Refactor "Password Strength Validator"
Refactor the password validator:
- `check_length(password)` — returns True if 8+ characters
- `check_uppercase(password)` — returns True if has uppercase letter
- `check_digit(password)` — returns True if has a digit
- `check_special(password)` — returns True if has special character
- `validate_password(password)` — calls all checks and returns overall strength

### Project 6: Build a Function-Driven Number Analyzer
Create a program that takes a list of numbers and:
- `get_numbers_from_user()` — collects numbers via input
- `calculate_average(numbers)` — returns the mean
- `find_median(numbers)` — returns the median
- `find_mode(numbers)` — returns the mode
- `display_statistics(numbers)` — prints all stats in a formatted report

### Challenge Project 7: Refactor a Previous Mini-Project
Pick any project from Days 1-20 and fully refactor it:
- Identify at least 5 pieces of logic that can become functions
- Create a clean `main()` entry point
- Ensure no code runs at the top level except the `main` guard
- Add docstrings to every function

---

## 7. Summary
By the end of Day 21, you should be able to:
- Refactor monolithic code into clean, modular functions
- Structure programs using a `main()` entry point pattern
- Apply the Single Responsibility Principle to function design
- Recognize when code should be extracted into a reusable function
- Use `if __name__ == "__main__"` to guard executable code
