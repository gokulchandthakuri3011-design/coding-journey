# Introduction to Functions

## What is a function?
- A function is a reusable block of code that performs a single task.
- Use `def` to define a function, then call it by name.
- Functions help make code shorter, easier to read, and easier to fix.

## Basic structure
```python
def say_hello():
    print("Hello, world!")

say_hello()
```
- `def` starts the definition.
- `say_hello` is the function name — lowercase with underscores.
- Parentheses `()` follow the name.
- The indented block inside is the function body.
- A function must be defined before it is called.
- Use `pass` as a placeholder for an empty body.

## Why use functions?
- Avoid repeating the same code.
- Break problems into smaller steps (modularization).
- Test each step separately.
- Share logic between different parts of a program.
- Each function should do **one thing** well (Single Responsibility Principle).

## Return values
- Use `return` to send a value back to the caller.
- Without `return`, a function returns `None`.

Example:
```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 8
```

## Pure functions vs side effects

| Pure Function | Side Effect |
|---|---|
| Returns the same output for the same input | Modifies something outside the function |
| No modification of external state | e.g., printing, modifying a global variable, writing to a file |
| Easy to test and reason about | Harder to debug and test |

```python
# Pure function
def add(a, b):
    return a + b

# Side effect
def greet(name):
    print(f"Hello, {name}")  # printing is a side effect
```
- Pure functions are preferred when possible — they are predictable.
- Side effects are sometimes necessary (e.g., I/O operations) but should be isolated.
- Functions with side effects are called **impure functions**.

## First-Class Functions
- In Python, functions are **first-class citizens**.
- They can be assigned to variables, passed as arguments, and returned from other functions.

```python
def square(x):
    return x ** 2

# Assign function to a variable
f = square
print(f(5))  # 25

# Pass function as an argument
def apply(func, value):
    return func(value)

print(apply(square, 4))  # 16
```
- Functions can be stored in data structures (lists, dicts, etc.)
- This enables higher-order functions and functional programming patterns.
- Built-in functions like `map()`, `filter()`, and `sorted()` accept functions as arguments.

## Common function rules
- Choose clear names: `calculate_average`, `print_report`, `get_data`.
- Keep functions short and focused on one job.
- Use comments or docstrings when needed.

## Quick reminder
- Define first, then call later.
- Use parameters for input and return for output.
- Keep functions reusable and clear.

## Practice questions
1. Write a function `square(number)` that returns the square of its input.
2. Create `is_even(number)` that returns `True` if the number is even and `False` otherwise.
3. Build `area_rectangle(width, height)` to compute the area of a rectangle.
4. Define `full_name(first, last)` that returns the full name in one string.
5. Write `convert_to_celsius(fahrenheit)` and `convert_to_fahrenheit(celsius)`.
6. Create `greet_user(name, age)` to print a greeting message.
7. Make a function `average(numbers)` that returns the average of a list of numbers.
8. Write a function `count_vowels(text)` that counts vowel letters in a string.
9. Build `get_larger(a, b)` that returns the larger of two values.
10. Create `print_menu()` that prints a simple program menu and does not return a value.
