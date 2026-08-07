"""
### Assignment 1: The FizzBuzz Challenge
This is a famous programming interview question!
*   Write a program that prints the numbers from 1 to 50 using a loop.
*   For multiples of **3**, print `"Fizz"` instead of the number.
*   For multiples of **5**, print `"Buzz"` instead of the number.
*   For numbers which are multiples of **both 3 and 5**, print `"FizzBuzz"`.
"""

# FIXED VERSION - Reset result for each iteration
for i in range(1, 51):
    result = ""  # Reset result for each number
    
    # Checking if the number is a multiple of 3  
    if i % 3 == 0:
        result += "Fizz"
    # Checking if the number is a multiple of 5
    if i % 5 == 0:
        result += "Buzz"
    
    # Print the result or the number
    if result:           # If result is not empty, considered (True)
        print(result)
    else:                # If result is empty, considered (False)
        print(i)

# ALTERNATIVE VERSION - Using if-elif-else structure
""" for i in range(1, 51):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i) """
