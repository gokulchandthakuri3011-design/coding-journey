"""
### Assignment 1: Safe Calculator (Easy)

Write a calculator that:
- Prompts for two numbers and an operator (`+`, `-`, `*`, `/`)
- Handles `ValueError` (bad numbers) and `ZeroDivisionError`
- Loops until user types `quit`
- Uses `try`/`except`/`else`/`finally` appropriately

**Expected Output:**
```
Enter first number (or 'quit'): 10
Enter operator (+, -, *, /): /
Enter second number: 0
Cannot divide by zero! Try again.

Enter first number (or 'quit'): 10
Enter operator (+, -, *, /): /
Enter second number: 2
Result: 5.0

Enter first number (or 'quit'): quit
Goodbye!
"""
def safe_calculator():
    # Prompting user for input until user types 'quit'
    attempt = 0
    while True:
        num1 = input("Enter first number (or 'quit'): ")
        if num1 == "quit":
            print("Goodbye!")
            break
        operand = input("Enter operator (+, -, *, /): ")
        num2 = input("Enter second number: ")
        try:
            a = int(num1)
            b = int(num2)
            if operand == "+":
                result = a + b
            elif operand == "-":
                result = a - b
            elif operand == "*":
                result = a * b
            elif operand == "/":
                result = a / b
            else:
                print(f"Please enter the correct operator!")
                continue
        except ValueError as e:
            print(f"Please enter correct number.")
            print(f"Error type: {e}")
        except ZeroDivisionError as e:
            print(f"Cannot divide by zero! Try again.")
            print(f"Error Type: {e}")
        else:
            print(f"Result: {result}")
        finally:
            attempt += 1
            print(f"Operation #{attempt} completed")

if __name__ == "__main__":
    safe_calculator()