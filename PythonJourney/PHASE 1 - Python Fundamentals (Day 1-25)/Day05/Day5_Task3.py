"""
### Exercise 3: Number Positivity
Write a program that takes a number as input and checks if it is positive, negative, or zero using `if`, `elif`, and `else`.
"""
print("\n --- Number Positicity --- \n")

# Asking user for number
num = int(input("Enter a number('+','-' or 0): "))

# Checking the number
if num < 0:
    print(f"The number {num} is negative.")
elif num > 0:
    print(f"The number {num} is positive.")
else:
    print(f"The number {num} is 0.")

print("\n----------------------------")