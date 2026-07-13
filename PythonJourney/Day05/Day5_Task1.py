"""
### Exercise 1: Even or Odd?
# Day 5: Conditional Statements Practice
Write a program that asks the user for an integer.
prints whether the number is even or odd.
*(Hint: Use the modulo operator `%`. A number is even if `number % 2 == 0`)*
"""

# Getting user input
number = int(input("Enter an integer: "))

# Checking if the number is even or odd
if number % 2 == 0:
    print(f"{number} is even.")
else: 
    print(f"{number} is odd.")

