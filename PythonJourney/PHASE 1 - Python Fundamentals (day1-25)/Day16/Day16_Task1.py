"""
### Easy
1. Write a function `multiply(a, b)` that returns the product of two numbers. Call it using both positional and keyword arguments.
2. Create a function `welcome(name, message="Welcome")` that prints a greeting. Test it with and without the `message` argument.
3. Write a function `average(*numbers)` that returns the average of any number of arguments.
"""

# Multiply Function
def multiply(a, b):
    return a*b

# Greeting Function
def welcome(name, message = "Welcome"):
    print(f"{message} {name}!")

# Average Function
def average(*numbers):
    return sum(numbers)/len(numbers)

if __name__ == "__main__":
    # Calling using 
    # Positional arguments
    print(multiply(2, 3))

    # Keyword arguments
    print(multiply(a = 3, b = 4))

    # Calling using
    # With 'message' argument
    welcome(name = "Arun", message = "Morgen")

    # Without 'message' argument
    welcome(name = "Lalita")

    print(average(1,2,3,4,5,6))