"""
### Hard
8. Write a function `flexible_operation(a, b, /, *args, operation="add", **kwargs)` that:
   - Takes two required positional-only args `a`, `b`.
   - Accepts extra positional args via `*args`.
   - Has a keyword-only `operation` parameter (default `"add"`).
   - Accepts extra keyword args via `**kwargs`.
   - If `operation` is `"add"`, sum all numbers. If `"multiply"`, multiply all.
   - Print any extra kwargs as metadata.
"""

def flexible_operation(a, b, /, *args, operation="add", **kwargs):
    if operation == "add":
        result = a + b
    elif operation == "multiply":
        result = a * b
    for x in args:
        if operation == "add":
            result += x
        elif operation == "multiply":
            result *= x

    if kwargs:
        print(f"Metadata: {kwargs}")
    return result

# Calling the functions
print(f"Sum: {flexible_operation(2,3)}")
print(f"Sum: {flexible_operation(1,2, 1,2,3,4)}")
print(f"Multiply: {flexible_operation(1,2, 1,2,3,4, operation = 'multiply')}")
flexible_operation(0,0, name = 'Arun', age = 22)