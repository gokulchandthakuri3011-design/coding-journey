"""
### Assignment 2: Even Number Printer
Write a `for` loop using `range()` to print even numbers from 2 to 20.
- Use `continue` to skip odd numbers.
"""
print("\n --- Even Number Printer --- \n")
for i in range(1, 21):
    if i % 2 != 0:
        continue
    print(f"Even Number: {i}")
print("\n ---------------------------")