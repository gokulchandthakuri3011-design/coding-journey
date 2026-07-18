"""
### Project 3: Refactor "Interactive Calculator"
Refactor the calculator so that:
- Each operation (add, subtract, multiply, divide) is its own function
- A dispatcher function calls the correct operation based on user choice
- Division by zero is handled inside the divide function
- The calculator loop is managed by a `run_calculator()` function
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        print("Division by Zero not possible!\n")

def modulo(a, b):
    if b != 0:
        return a % b
    else:
        print("Division by Zero not possible!\n")

def dispatch(operator, a, b):
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
        "%": modulo
    }
    if operator in operations:
        return operations[operator](a, b)
    else:
        print("Invalid operations choice by user. Try again.\n")

def run_calculator():
    print("=== Interactive Calculator ===")
    print("Operators: + - * / %")
    print("Type 'quit' to exit\n")

    while True:
        # Asking user's input
        user_input = input("Enter first number (or 'quit'): ").strip()
        if user_input == "quit":
            print("Goodbye!")
            break

        try:
            a = float(user_input)
        except ValueError:
            print("Invalid number, try again./n")
            continue

        operator = input("Enter operator (+, -, *, /, %): ").strip()

        second_input = input("Enter second number: ").strip()
        try:
            b = float(second_input)
        except ValueError:
            print("Invalid number, try again.\n")
            continue

        result = dispatch(operator, a, b)
        if result is not None:
            print(f"{a} {operator} {b} = {result}\n")


if __name__ == "__main__":
    run_calculator()