"""
1. Write a module `math_utils.py` with functions `is_even(n)`, `is_odd(n)`, and `square(n)`. Import and use them in a separate script.
"""

def is_even(n):
    if n % 2 == 0:
        return f"{n} is even."
    return f"{n} is not even."
    
def is_odd(n):
    if n % 2 != 0:
        return f"{n} is odd."
    return f"{n} is not odd!"
    
def square(n):
    return f"Square of {n} is: {n * n}"

if __name__ == "__main__":
    print(is_even(144))
    print(is_odd(9))
    print(square(4))