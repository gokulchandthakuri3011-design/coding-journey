"""
### Easy
1. Write a function `square(n)` that returns the square of a number. Test with integers and floats.
2. Write a function `is_even(n)` that returns `True` if `n` is even, `False` otherwise.
3. Write a function `greet(name)` that prints `"Hello, {name}!"` and returns `None`. Print the return value.
"""

# Function for squaring the numbers
def square(n):
    return n * n

# Function to check even or odd
def is_even(n):
    if n % 2 == 0:
        return True
    return False

# Function for greetings
def greet(name):
    print(f"Hello, {name}!")
    return None

# Calling each functions
print(square(2))
print(square(2.5))
n = 3
print(f"Is {n} Even: {is_even(n)}")
print(greet("Lalita"))
