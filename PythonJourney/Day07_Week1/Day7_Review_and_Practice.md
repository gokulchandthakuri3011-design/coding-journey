# Day 7: Review & Practice

Welcome to Day 7! Today marks the end of Week 1 in your Python learning journey. We've covered the fundamental building blocks of Python. Now, it's time to consolidate that knowledge through hands-on practice.

---

## 📚 Week 1 Quick Recap

Before we jump into the assignments, let's briefly review the core concepts you've learned:

1.  **Variables & Data Types (Day 2):** Storing data using `int` (integers), `float` (decimals), `str` (text), and `bool` (True/False).
2.  **Operators (Day 3):** Performing calculations (`+`, `-`, `*`, `/`), comparing values (`==`, `!=`, `<`, `>`), and combining conditions (`and`, `or`, `not`).
3.  **User Input & Strings (Day 4):** Getting data from the user using `input()`, converting between data types (e.g., `int()`), and formatting strings using f-strings (`f"Hello {name}"`).
4.  **Conditional Statements (Day 5):** Making decisions in your code using `if`, `elif`, and `else` blocks.
5.  **Loops (Day 6):** Repeating actions using `while` and `for` loops, and controlling the flow with `break` and `continue`.

---

## 🎯 Main Task: "Guess the Number" Game

Your primary project for today is to build a classic "Guess the Number" game. This will test your ability to use variables, loops, conditional statements, and user input all together.

### The Rules:
1.  The program should randomly select a number between 1 and 100. *(Hint: You will need to use `import random` and `random.randint(1, 100)` at the top of your file to generate the secret number).*
2.  The user should be prompted to guess the number.
3.  If the user's guess is too high, the program should print "Too high! Try again."
4.  If the user's guess is too low, the program should print "Too low! Try again."
5.  If the user guesses correctly, the program should congratulate them and tell them how many attempts it took.
6.  The game should continue looping until the user guesses the correct number.

### Example Output:
```text
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Enter your guess: 50
Too high! Try again.

Enter your guess: 25
Too low! Try again.

Enter your guess: 37
Congratulations! You guessed the number in 3 attempts!
```

---

## 🚀 Additional Practice Assignments

Once you finish the main task, tackle these extra challenges to further sharpen your skills.

### Assignment 1: The FizzBuzz Challenge
This is a famous programming interview question!
*   Write a program that prints the numbers from 1 to 50 using a loop.
*   For multiples of **3**, print `"Fizz"` instead of the number.
*   For multiples of **5**, print `"Buzz"` instead of the number.
*   For numbers which are multiples of **both 3 and 5**, print `"FizzBuzz"`.

### Assignment 2: Interactive Calculator
Build a program that asks the user for two numbers and an arithmetic operation to perform on them.
1.  Ask the user for the first number (convert to `float`).
2.  Ask the user for the second number (convert to `float`).
3.  Ask the user to enter an operator (`+`, `-`, `*`, `/`).
4.  Use `if`, `elif`, and `else` to perform the selected operation and print the result.
5.  *Bonus:* Make sure the program doesn't crash if the user tries to divide by zero! Print a helpful error message instead.

### Assignment 3: Password Strength Checker
Create a simple program that validates a user's password based on specific criteria.
1.  Ask the user to enter a new password.
2.  Check the following conditions using `if/else` and string methods:
    *   It must be at least 8 characters long (use `len()`).
    *   It must not contain the word "password" (case-insensitive).
3.  If the password meets the criteria, print `"Password accepted."`
4.  If it fails, use a loop to keep asking them for a password until they provide a valid one.

---

### 💡 Daily Routine Checklist (Day 7):
- [ ] Read through the Week 1 recap.
- [ ] Complete the "Guess the Number" game.
- [ ] Attempt at least one of the additional practice assignments.
- [ ] Pat yourself on the back for completing Week 1! 🎉
