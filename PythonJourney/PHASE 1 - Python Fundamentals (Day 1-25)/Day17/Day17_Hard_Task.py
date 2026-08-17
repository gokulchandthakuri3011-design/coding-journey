"""
### Hard
7. Write a function `categorize(numbers)` that returns a dictionary with keys `"positive"`, `"negative"`, and `"zero"`, each containing a list of the respective numbers.
8. Write a function `make_greeting(greeting_type)` that returns a function. If `greeting_type` is `"formal"`, return a function that prints `"Dear {name}, ..."`. If `"casual"`, return a function that prints `"Hey {name}!"`.
9. Write a function `safe_divide(a, b)` that returns the result of `a / b` if `b != 0`, or returns `None` if `b == 0`. Use type hints: `-> Optional[float]`.
10. Write a function `transform(data, operation)` that takes a list and a string (`"upper"`, `"lower"`, `"reverse"`), and returns a new list transformed accordingly. Return `None` if the operation is invalid.
"""
# Returning a dict with '+'ve, '-'ve and 0 keys with their list as values
def categorize(numbers):
    neg_num = []
    pos_num = []
    zero = []
    for num in numbers:
        if num < 0:
            neg_num.append(num)
        elif num > 0:
            pos_num.append(num)
        else:
            zero.append(num)
    return {"positive": pos_num, "negative": neg_num, "zero": zero}

# Greeting user based on greeting type
def make_greeting(greeting_type):
    if greeting_type == "formal":
        def greeting(name):
            return f"Dear {name}, Guten Morgen!"
    if greeting_type == "casual":
        def greeting(name):
            return f"Hey {name}, wie geht's?"
    return greeting

# Function returning a division
from typing import Optional
def safe_divide(a,b) -> Optional[float]:
    if b != 0:
        return a/b
    else:
        return None

# String manipulation 
def transform(data, operation):
    transformed = []
    for item in data:
        if operation == "upper":
            transformed.append(item.upper())
        elif operation == "lower":
            transformed.append(item.lower())
        elif operation == "reverse":
            transformed = data[::-1]
    return transformed

# Providing input
def main():
    numbers = [0,1,2,3,-1,-2,-3,-4,5,0,0.-4-2-1,1,2,3]
    print(categorize(numbers))

    greet = make_greeting("casual")
    print(greet("Arun"))

    safe_division = safe_divide(9,5)
    print(f"{safe_division:.2f}")

    data = ["Hallo", "wie", "geht's", "mir", "geht", "es", "sehr", "gut"]
    print(transform(data, "upper"))
    print(transform(data, "reverse"))

if __name__ == "__main__":
    main()
