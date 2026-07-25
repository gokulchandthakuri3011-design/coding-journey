# Day 22: Review & Practice (Functions & Modularity)

## Goal
Review functions, scopes, and modular code design. Learn to create your own custom module files and import them in other scripts.

---

## 1. Functions Review
A function is a reusable block of code that performs a specific task.

### Defining and Calling
```python
def greet(name):
    return f"Hello, {name}!"

message = greet("Alice")
print(message)  # Hello, Alice!
```

### Parameters Recap
- **Positional arguments** — matched by order
- **Keyword arguments** — matched by name
- **Default parameters** — fallback values if not provided
- **`*args`** — collects extra positional arguments as a tuple
- **`**kwargs`** — collects extra keyword arguments as a dictionary

```python
def introduce(name, age=25, *hobbies, **details):
    print(f"{name}, age {age}")
    print(f"Hobbies: {hobbies}")
    print(f"Details: {details}")

introduce("Bob", 30, "reading", "gaming", city="Mumbai")
```

---

## 2. Variable Scope Review
Scope determines where a variable can be accessed.

### Local Scope
Variables created inside a function exist only within that function.
```python
def my_function():
    x = 10
    print(x)  # Works here

my_function()
# print(x)  # Error — x is not defined here
```

### Global Scope
Variables created outside any function are accessible everywhere.
```python
name = "Alice"

def say_hello():
    print(f"Hello, {name}")

say_hello()  # Works — uses global `name`
```

### The `global` Keyword
Use sparingly. It allows a function to modify a global variable.
```python
counter = 0

def increment():
    global counter
    counter += 1

increment()
print(counter)  # 1
```

### The `nonlocal` Keyword
Used in nested functions to modify a variable in the enclosing function.
```python
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
    inner()
    print(count)  # 1

outer()
```

### Closures
A closure is a function that remembers values from its enclosing scope.
```python
def multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

double = multiplier(2)
print(double(5))   # 10
print(double(10))  # 20
```

---

## 3. Modular Code Design
Modular code means breaking a program into separate, independent pieces.

### Why Modular?
- **Readability** — smaller pieces are easier to understand
- **Reusability** — same function used in multiple places
- **Maintainability** — fix bugs in one place, not everywhere
- **Testability** — test each function in isolation

### Modular Structure Pattern
```python
# --- Module 1: calculator.py ---
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
```

```python
# --- Module 2: text_formatter.py ---
def to_uppercase(text):
    return text.upper()

def to_lowercase(text):
    return text.lower()

def repeat_text(text, times):
    return text * times

def word_count(text):
    return len(text.split())
```

```python
# --- Main: main.py ---
import calculator
import text_formatter

result = calculator.add(10, 5)
print(result)  # 15

formatted = text_formatter.to_uppercase("hello world")
print(formatted)  # HELLO WORLD
```

---

## 4. Creating Custom Modules
Any `.py` file is automatically a module. You can import it by its filename (without `.py`).

### Directory Structure
```
my_project/
    calculator.py
    text_formatter.py
    main.py
```

### Import Methods
```python
# Import the entire module
import calculator
print(calculator.add(2, 3))

# Import specific functions
from calculator import add, subtract
print(add(2, 3))

# Import with an alias
import calculator as calc
print(calc.add(2, 3))

# Import all functions (not recommended for large modules)
from calculator import *
```

### Module `__all__` Control
In your module, define `__all__` to control what gets imported with `from module import *`.
```python
# calculator.py
__all__ = ['add', 'subtract', 'multiply']

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def _internal_helper():
    pass  # Not imported by `from calculator import *`
```

---

## 5. The `__name__` == `"__main__"` Guard
Every Python file has a special variable `__name__`. When a file is run directly, `__name__` is set to `"__main__"`. When it's imported, `__name__` is set to the module's name.

### Without Guard
```python
# calculator.py
def add(a, b):
    return a + b

print(add(2, 3))  # This runs even when calculator.py is imported
```

### With Guard
```python
# calculator.py
def add(a, b):
    return a + b

if __name__ == "__main__":
    # This block only runs when calculator.py is executed directly
    print(add(2, 3))
    print("Running calculator tests...")
```

### Why It Matters
- When you `import calculator` in `main.py`, the `print()` inside the guard **does not run**
- When you run `python calculator.py` directly, the guard **does run**
- This is the standard way to add test code or a CLI to a module without affecting imports

### Typical Usage
```python
# my_module.py
def helper_function():
    return "I help!"

def main():
    print("Running main logic...")
    result = helper_function()
    print(result)

if __name__ == "__main__":
    main()
```

### Purpose of Multi-File Structure with `if __name__ == "__main__"`
The 3-file structure (`calculator.py`, `text_formatter.py`, `main.py`) exists for **modularity** — each file handles one responsibility:
- `calculator.py` → math operations only
- `text_formatter.py` → text operations only  
- `main.py` → combines both and runs the full program

The `if __name__ == "__main__"` block in `calculator.py` and `text_formatter.py` is **for testing during development only**. Here's how it works:

**Scenario 1: Running `calculator.py` directly**
```bash
python calculator.py
```
Python executes `calculator.py` and sets `__name__` to `"__main__"`. So the condition `if __name__ == "__main__"` is `True`, and the test block runs.

**Scenario 2: Importing `calculator` in `main.py`**
```python
import calculator  # Python runs calculator.py, but sets __name__ to "calculator"
```
When `main.py` imports `calculator`, Python still runs the code in `calculator.py`, but this time it sets `__name__` to `"calculator"` (the module name, which is the filename without `.py`). So the condition `if __name__ == "__main__"` becomes `"calculator" == "__main__"` → `False`, and the test block is skipped.

This means:
- You can run each module standalone to verify its functions work
- When `main.py` imports them, only the clean function definitions load — no test output
- You only need to run `python main.py` for the actual program

---

## 6. Multi-File Utility Package
Here is a complete example of a multi-file project using custom modules.

### File: `calculator.py`
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def modulo(a, b):
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a % b

if __name__ == "__main__":
    print("Running calculator module tests...")
    print(add(10, 5))       # 15
    print(subtract(10, 5))  # 5
    print(multiply(10, 5))  # 50
    print(divide(10, 5))    # 2.0
    print(modulo(10, 3))    # 1
```

### File: `text_formatter.py`
```python
def to_uppercase(text):
    return text.upper()

def to_lowercase(text):
    return text.lower()

def capitalize_words(text):
    return text.title()

def word_count(text):
    return len(text.split())

def char_count(text, char):
    return text.lower().count(char.lower())

def repeat_text(text, times):
    return " ".join(text * times)

if __name__ == "__main__":
    print("Running text_formatter module tests...")
    sample = "hello world from python"
    print(to_uppercase(sample))       # HELLO WORLD FROM PYTHON
    print(word_count(sample))         # 4
    print(char_count(sample, 'l'))    # 3
```

### File: `main.py`
```python
import calculator
import text_formatter

def main():
    # --- Calculator Section ---
    print("=== Calculator ===")
    print(f"10 + 5 = {calculator.add(10, 5)}")
    print(f"10 - 5 = {calculator.subtract(10, 5)}")
    print(f"10 * 5 = {calculator.multiply(10, 5)}")
    print(f"10 / 5 = {calculator.divide(10, 5)}")
    print(f"10 % 3 = {calculator.modulo(10, 3)}")
    print()

    # --- Text Formatter Section ---
    print("=== Text Formatter ===")
    sample = "hello world from python"
    print(f"Original:     {sample}")
    print(f"Uppercase:    {text_formatter.to_uppercase(sample)}")
    print(f"Lowercase:    {text_formatter.to_lowercase(sample)}")
    print(f"Title Case:   {text_formatter.capitalize_words(sample)}")
    print(f"Word Count:   {text_formatter.word_count(sample)}")
    print(f"Count of 'l': {text_formatter.char_count(sample, 'l')}")

if __name__ == "__main__":
    main()
```

### Directory Structure
```
my_project/
    calculator.py
    text_formatter.py
    main.py
```

---

## 7. Common Mistakes to Avoid

| Mistake | Fix |
|---------|-----|
| Importing `*` everywhere | Use explicit imports: `from module import func` |
| Running code outside functions in modules | Use `if __name__ == "__main__"` guard |
| Circular imports | Restructure code to avoid mutual dependencies |
| Naming files same as standard library (e.g., `math.py`) | Use unique, descriptive names |
| Hardcoding values in functions | Use parameters or constants |

---

## 8. Practice Questions

### Easy
1. Write a module `math_utils.py` with functions `is_even(n)`, `is_odd(n)`, and `square(n)`. Import and use them in a separate script.
2. Write a module `temp_converter.py` with functions `celsius_to_fahrenheit(c)`, `fahrenheit_to_celsius(f)`, and `celsius_to_kelvin(c)`. Test conversions in a separate script.
3. Write a module `string_utils.py` with `reverse_string(s)`, `is_palindrome(s)`, and `count_vowels(s)`. Test each function using `if __name__ == "__main__"`.

### Medium
4. Create a two-file project: `geometry.py` (circle area, rectangle area, triangle area) and `main.py` that imports and uses all functions in a menu-driven program.
5. Build a `file_utils.py` module with functions to count lines, words, and characters in a text string. Write a main script that uses these functions.
6. Create a `date_utils.py` module that uses the `datetime` standard library to calculate days between two dates, format dates, and check if a year is a leap year.

### Challenge
7. Build a multi-module calculator project: `operations.py`, `history.py` (stores past calculations in a list), and `main.py` that provides a CLI menu.
8. Create a `password_utils.py` module with functions for generating random passwords, checking password strength, and validating password format. Import and test in a main script.
9. Build a project with three modules: `student.py` (add, search, list students), `grade.py` (calculate average, find highest/lowest), and `main.py` that ties them together in a CLI interface.

---

## 9. Summary
By the end of Day 22, you should be able to:
- Review and confidently use functions, parameters, return values, and scope
- Understand local vs global vs nonlocal scope
- Recognize and use closures
- Create custom `.py` module files and import them in other scripts
- Use `if __name__ == "__main__"` to guard module-level code
- Structure a multi-file Python project with clean modularity
- Apply the Single Responsibility Principle to modular code design
