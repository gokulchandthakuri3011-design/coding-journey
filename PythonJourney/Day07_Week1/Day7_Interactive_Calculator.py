"""
### Assignment 2: Interactive Calculator
Build a program that asks the user for two numbers and an arithmetic operation to perform on them.
1.  Ask the user for the first number (convert to `float`).
2.  Ask the user for the second number (convert to `float`).
3.  Ask the user to enter an operator (`+`, `-`, `*`, `/`).
4.  Use `if`, `elif`, and `else` to perform the selected operation and print the result.
5.  *Bonus:* Make sure the program doesn't crash if the user tries to divide by zero! Print a helpful error message instead.
"""

# Prompting the user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /, %): ")

# Performing the operation based on user input
if operator == '+':
    result = num1 + num2
    print(f"The result of {num1} + {num2} is: {result}")
elif operator == '-':
    result = num1 - num2
    print(f"The result of {num1} - {num2} is: {result}")
elif operator == '*':
    result = num1 * num2
    print(f"The result of {num1} * {num2} is: {result}")
elif operator == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed:")
    else:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is: {result}")
elif operator == '%':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        rresult = num1 % num2
        print(f"The result of {num1} % {num2} is: {rresult}")
else:
    print("Invalid Operator. Please use one of the following: +, -, *, /, %.")