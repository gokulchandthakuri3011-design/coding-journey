# Day 24: Error & Exception Handling in Python

> **Duration:** 1 hour (30 min reading + 30 min practice)
> **Goal:** Learn how to catch, handle, and raise exceptions so your programs don't crash unexpectedly

---

## Table of Contents

1. [Why Error Handling?](#1-why-error-handling)
2. [Syntax Errors vs Runtime Exceptions](#2-syntax-errors-vs-runtime-exceptions)
3. [The `try`/`except` Block](#3-the-tryexcept-block)
4. [Catching Specific Exceptions](#4-catching-specific-exceptions)
5. [The `else` and `finally` Blocks](#5-the-else-and-finally-blocks)
6. [Catching Multiple Exceptions](#6-catching-multiple-exceptions)
7. [Raising Exceptions (`raise`)](#7-raising-exceptions-raise)
8. [Exception Chaining (`raise ... from`)](#8-exception-chaining-raise--from)
9. [Creating Custom Exception Classes](#9-creating-custom-exception-classes)
10. [Common Built-in Exceptions](#10-common-built-in-exceptions)
11. [Practical Patterns](#11-practical-patterns)
12. [Best Practices Summary](#12-best-practices-summary)
13. [Quick Reference Cheat Sheet](#13-quick-reference-cheat-sheet)
14. [Practice Assignments](#14-practice-assignments)

---

## 1. Why Error Handling?

So far, if your program encounters a problem (like dividing by zero or opening a missing file), it **crashes immediately**. The user sees an ugly error message and the program stops.

Error handling lets you:
- **Catch problems** before they crash the program
- **Show friendly messages** to the user instead of raw error tracebacks
- **Recover gracefully** (e.g., use a default value, retry an operation)
- **Clean up resources** (close files, database connections) even when errors occur

**Think of it this way:** Without error handling, one bad input kills your whole program. With error handling, your program can say "Oops, that didn't work — let me try something else" and keep running.

---

## 2. Syntax Errors vs Runtime Exceptions

Python has two main types of errors:

### Syntax Errors (Parse Time)

These happen **before** the program runs. Python can't even understand your code.

```python
# Missing colon
if x > 5
    print("hello")

# Mismatched parentheses
print("hello"

# Indentation error
if True:
print("hello")
```

**Syntax errors must be fixed in the code.** They can't be caught with `try/except` because the program never starts running.

### Runtime Exceptions (Execution Time)

These happen **while** the program is running. The code is syntactically correct, but something goes wrong during execution.

```python
# This is valid syntax, but crashes at runtime
x = 10
result = x / 0          # ZeroDivisionError!

# This is also valid syntax
my_list = [1, 2, 3]
print(my_list[10])      # IndexError!

# And this
name = "Gokul"
print(name + 5)         # TypeError!
```

**Runtime exceptions CAN be caught and handled** using `try/except`.

### Quick Comparison

| | Syntax Errors | Runtime Exceptions |
|---|---|---|
| **When caught** | Before program runs | While program runs |
| **Can fix at runtime?** | No — must edit code | Yes — can catch & handle |
| **Example** | Missing `:`, bad indentation | Division by zero, file not found |
| **Can use `try/except`?** | No | Yes |

---

## 3. The `try`/`except` Block

The basic structure for handling errors:

```python
try:
    # Code that might cause an error
    risky_code()
except:
    # Code that runs if an error occurs
    handle_error()
```

### How It Works

1. Python **tries** to run the code inside `try`
2. If everything goes fine, it **skips** the `except` block
3. If an error occurs, Python **jumps** to the `except` block
4. The program **continues** after the `except` block (doesn't crash!)

### Example: Simple Division

```python
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    result = numerator / denominator
    print(f"Result: {result}")
except:
    print("Something went wrong!")

print("Program continues running!")
```

**Run 1:**
```
Enter numerator: 10
Enter denominator: 2
Result: 5.0
Program continues running!
```

**Run 2:**
```
Enter numerator: 10
Enter denominator: 0
Something went wrong!
Program continues running!
```

The program didn't crash! It caught the error and kept going.

### Accessing the Exception Object

Use `as` to capture the exception and see what went wrong:

```python
try:
    result = 10 / 0
except Exception as e:
    print(f"Error type: {type(e).__name__}")
    print(f"Error message: {e}")
```

**Output:**
```
Error type: ZeroDivisionError
Error message: division by zero
```

> **Warning:** Avoid using a bare `except:` without specifying the exception type. It catches **everything**, including `KeyboardInterrupt` (Ctrl+C) and `SystemExit`, which you usually don't want to catch.

```python
# BAD - catches everything
try:
    risky()
except:
    print("error")

# GOOD - catches only what you expect
try:
    risky()
except ValueError:
    print("bad value")
```

---

## 4. Catching Specific Exceptions

Instead of catching all errors, catch **only the ones you expect**. This is safer and makes debugging easier.

```python
try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print(f"Result: {result}")
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
```

**Run 1:**
```
Enter a number: hello
That's not a valid number!
```

**Run 2:**
```
Enter a number: 0
You can't divide by zero!
```

**Run 3:**
```
Enter a number: 5
Result: 20.0
```

### Why Catch Specific Exceptions?

1. **You know what went wrong** — specific error messages help users
2. **You don't hide bugs** — catching `Exception` might mask unrelated errors
3. **Better debugging** — you can log the exact problem

```python
# BAD - hides what actually went wrong
try:
    do_something()
except:
    print("error occurred")

# GOOD - you know exactly what happened
try:
    do_something()
except FileNotFoundError:
    print("File not found. Check the path.")
except PermissionError:
    print("You don't have permission to access this file.")
except ValueError as e:
    print(f"Invalid value: {e}")
```

---

## 5. The `else` and `finally` Blocks

Python's error handling has two optional blocks: `else` and `finally`.

### The `else` Block

Runs **only if** the `try` block succeeds (no exception occurred).

```python
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid number!")
else:
    # This runs ONLY if no exception occurred in try
    print(f"You entered: {num}")
    result = 100 / num
    print(f"100 / {num} = {result}")
```

**Why use `else`?** It keeps your `try` block small and focused on code that might fail. Code that should only run on success goes in `else`.

```python
# WITHOUT else (less clear)
try:
    f = open("data.txt")
    content = f.read()
    print(content)            # This won't fail, so why is it in try?
except FileNotFoundError:
    print("File not found!")

# WITH else (cleaner)
try:
    f = open("data.txt")
    content = f.read()
except FileNotFoundError:
    print("File not found!")
else:
    print(content)            # Only runs if file was successfully read
```

### The `finally` Block

**Always runs**, whether an exception occurred or not. Perfect for cleanup.

```python
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
else:
    print(content)
finally:
    print("Done! (This always runs)")
```

**Common use cases for `finally`:**
- Closing files
- Closing database connections
- Releasing locks
- Printing a "done" message

```python
file = None
try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found!")
finally:
    if file:
        file.close()
        print("File closed.")
```

### The Full `try`/`except`/`else`/`finally` Structure

```python
try:
    # Code that MIGHT fail
    risky_operation()
except SpecificError as e:
    # Runs if the specific error occurs
    handle_error(e)
except AnotherError:
    # Runs if a different error occurs
    handle_other_error()
else:
    # Runs ONLY if no exception occurred
    do_success_work()
finally:
    # ALWAYS runs (cleanup)
    cleanup_resources()
```

**Execution flow:**

```
try block runs
    |
    +--> Success --> else block runs --> finally block runs
    |
    +--> Exception --> except block runs --> finally block runs
```

---

## 6. Catching Multiple Exceptions

### Option 1: Separate `except` Blocks

```python
try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print(f"Result: {result}")
except ValueError:
    print("Invalid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except KeyboardInterrupt:
    print("\nProgram interrupted by user.")
```

### Option 2: Tuple of Exceptions

Catch multiple exceptions with the same handler:

```python
try:
    num = int(input("Enter a number: "))
    result = 100 / num
except (ValueError, ZeroDivisionError) as e:
    # Handles BOTH ValueError and ZeroDivisionError
    print(f"Input error: {e}")
```

### Option 3: Catch All Exceptions (Use Sparingly)

```python
try:
    risky_operation()
except Exception as e:
    # Catches all non-system exceptions
    print(f"Something went wrong: {e}")
```

> **Remember:** Always prefer catching specific exceptions over catching `Exception`. Only use `Exception` as a last resort (e.g., a top-level handler in a large application).

### Exception Hierarchy

Exceptions form a hierarchy. Catching a parent also catches its children:

```python
# BaseException
#   +-- KeyboardInterrupt
#   +-- SystemExit
#   +-- Exception
#         +-- ValueError
#         +-- TypeError
#         +-- ZeroDivisionError
#         +-- FileNotFoundError
#         +-- IOError
#         +-- ...
```

So catching `Exception` catches `ValueError`, `TypeError`, `FileNotFoundError`, etc. But it does NOT catch `KeyboardInterrupt` or `SystemExit`.

---

## 7. Raising Exceptions (`raise`)

You can **deliberately trigger** an exception using `raise`. This is useful when:

- Validating input in functions
- Enforcing business rules
- Signaling that something went wrong

### Basic `raise` Syntax

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Age seems unrealistic!")
    print(f"Age set to {age}")

# Usage
try:
    set_age(-5)
except ValueError as e:
    print(f"Error: {e}")     # Error: Age cannot be negative!
```

### Raising Exceptions in Functions

```python
def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if amount > balance:
        raise ValueError(f"Insufficient funds: balance={balance}, requested={amount}")
    return balance - amount

# Usage
try:
    new_balance = withdraw(100, 200)
except ValueError as e:
    print(f"Transaction failed: {e}")
```

### Re-raising Exceptions

If you catch an exception but want it to propagate up:

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Logging the error...")
    raise    # Re-raises the same exception
```

---

## 8. Exception Chaining (`raise ... from`)

When you raise a new exception based on another, **chain them** to preserve the original traceback.

```python
try:
    result = 10 / 0
except ZeroDivisionError as original:
    raise ValueError("Cannot perform calculation") from original
```

**Output:**
```
Traceback (most recent call last):
  ...
ZeroDivisionError: division by zero

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  ...
ValueError: Cannot perform calculation
```

### Why Chain Exceptions?

1. **Preserves context** — you can see the original error AND the new one
2. **Helps debugging** — developers know what actually went wrong
3. **Professional practice** — shows the chain of events

### Without Chaining (Bad)

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    raise ValueError("Cannot perform calculation")
# Original traceback is lost!
```

### With Chaining (Good)

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    raise ValueError("Cannot perform calculation") from e
# Original traceback is preserved!
```

---

## 9. Creating Custom Exception Classes

For domain-specific errors, create your own exception classes. Always inherit from `Exception`.

### Basic Custom Exception

```python
class AppError(Exception):
    """Base exception for our application."""
    pass
```

### Custom Exceptions with Details

```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.deficit = amount - balance
        super().__init__(
            f"Cannot withdraw {amount}: balance is {balance} "
            f"(short by {self.deficit})"
        )

class InvalidAmountError(Exception):
    def __init__(self, amount):
        self.amount = amount
        super().__init__(f"Invalid amount: {amount}. Must be positive.")

class AccountNotFoundError(Exception):
    def __init__(self, account_id):
        self.account_id = account_id
        super().__init__(f"Account not found: {account_id}")
```

### Using Custom Exceptions

```python
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError(amount)
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

# Usage
account = BankAccount(100)

try:
    account.withdraw(-10)
except InvalidAmountError as e:
    print(f"Error: {e}")
    # Error: Invalid amount: -10. Must be positive.

try:
    account.withdraw(200)
except InsufficientFundsError as e:
    print(f"Error: {e}")
    # Error: Cannot withdraw 200: balance is 100 (short by 100)
    print(f"You need {e.deficit} more.")
```

### Custom Exception Hierarchy

```python
class BankError(Exception):
    """Base exception for all bank-related errors."""
    pass

class InsufficientFundsError(BankError):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: {balance} < {amount}")

class InvalidAmountError(BankError):
    def __init__(self, amount):
        self.amount = amount
        super().__init__(f"Invalid amount: {amount}")

class AccountNotFoundError(BankError):
    def __init__(self, account_id):
        self.account_id = account_id
        super().__init__(f"Account not found: {account_id}")
```

Now you can catch all bank errors with one handler:

```python
try:
    account.withdraw(500)
except BankError as e:
    print(f"Bank error: {e}")   # Catches any bank-related error
```

---

## 10. Common Built-in Exceptions

| Exception | When It Occurs | Example |
|-----------|---------------|---------|
| `ValueError` | Wrong value (correct type) | `int("abc")`, `int("3.14")` |
| `TypeError` | Wrong type | `"2" + 2`, `len(5)`, `None.append(1)` |
| `ZeroDivisionError` | Division by zero | `10 / 0`, `10 // 0` |
| `FileNotFoundError` | File doesn't exist | `open("missing.txt")` |
| `FileExistsError` | File already exists (in `x` mode) | `open("existing.txt", "x")` |
| `PermissionError` | No access rights | `open("/root/file.txt")` |
| `IndexError` | Index out of range | `[1,2,3][10]` |
| `KeyError` | Dictionary key not found | `{"a": 1}["b"]` |
| `AttributeError` | Object has no attribute | `None.append(1)` |
| `ImportError` | Module import fails | `import missing_module` |
| `StopIteration` | Iterator exhausted | `next(iter([]))` |
| `NameError` | Variable not defined | `print(unknown_var)` |
| `RecursionError` | Too much recursion | Infinite recursive function |
| `OverflowError` | Number too large | `math.exp(1000)` |
| `KeyboardInterrupt` | User presses Ctrl+C | Interrupting a running program |
| `SystemExit` | `sys.exit()` called | Exiting the program |

### How to Remember Which Exception to Catch

Think about **what operation fails**:
- Converting input? → `ValueError`
- Accessing list/string position? → `IndexError`
- Dictionary key? → `KeyError`
- File operations? → `FileNotFoundError`, `PermissionError`
- Math operations? → `ZeroDivisionError`
- Calling methods? → `AttributeError`, `TypeError`

---

## 11. Practical Patterns

### Pattern 1: Crash-Proof Input

```python
def get_int(prompt: str) -> int:
    """Keep asking until user enters a valid integer."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer. Try again.")

def get_float(prompt: str) -> float:
    """Keep asking until user enters a valid float."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number. Try again.")

# Usage
age = get_int("Enter your age: ")
price = get_float("Enter price: $")
```

### Pattern 2: Robust File Reader

```python
import json

def read_json_config(path: str) -> dict:
    """Read a JSON config file with graceful error handling."""
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Config file '{path}' not found. Using defaults.")
        return {}
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in '{path}'") from e

# Usage
config = read_json_config("settings.json")
```

### Pattern 3: Retry with Backoff

```python
import time
from functools import wraps

def retry(max_attempts=3, delay=1, backoff=2):
    """Retry a function on failure with exponential backoff."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise
                    print(f"Attempt {attempt} failed: {e}. "
                          f"Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry(max_attempts=3, delay=1, backoff=2)
def fetch_data(url):
    import random
    if random.random() < 0.7:
        raise ConnectionError("Network timeout")
    return {"status": "ok"}

# Usage
try:
    data = fetch_data("https://api.example.com")
except ConnectionError:
    print("Failed after 3 attempts.")
```

### Pattern 4: Safe File Operations

```python
def safe_write(path: str, content: str) -> bool:
    """Write to file safely, returning success/failure."""
    try:
        with open(path, "w") as f:
            f.write(content)
        return True
    except PermissionError:
        print(f"Permission denied: {path}")
        return False
    except OSError as e:
        print(f"Write error: {e}")
        return False

# Usage
if safe_write("output.txt", "Hello"):
    print("File saved!")
else:
    print("Could not save file.")
```

### Pattern 5: Context Manager for Timing

```python
import time
from contextlib import contextmanager

@contextmanager
def timer(label: str):
    """Time a block of code."""
    print(f"⏱ {label} started")
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        print(f"⏱ {label} finished in {elapsed:.4f}s")

# Usage
with timer("Sort list"):
    data = sorted(range(1000000, 0, -1))
```

---

## 12. Best Practices Summary

| Do | Don't |
|----|-------|
| Catch specific exceptions (`except ValueError`) | Use bare `except:` |
| Use `else` for success-only code | Put success code in `try` |
| Use `finally` for cleanup (close files, locks) | Forget to clean up resources |
| Use `raise ... from` for exception chaining | Raise generic `Exception` |
| Create custom exceptions for domain errors | Use exceptions for normal control flow |
| Keep `try` blocks small and focused | Put entire program in one `try` |
| Document what exceptions a function raises | Surprise callers with unexpected errors |

### When to Use `try/except` vs `if` Checks

```python
# Use if check for EXPECTED conditions
if key in my_dict:
    value = my_dict[key]

# Use try/except for UNEXPECTED failures
try:
    value = my_dict[key]
except KeyError:
    value = default_value

# Both work, but the if check is clearer for expected cases
```

**Rule of thumb:** Use `if` for things you **expect** might happen. Use `try/except` for things that **shouldn't** happen but could (errors, failures, external problems).

---

## 13. Quick Reference Cheat Sheet

```
ERROR HANDLING CHEAT SHEET
==========================

BASIC STRUCTURE
    try:
        risky()
    except SpecificError as e:
        handle(e)
    except (Err1, Err2) as e:
        handle(e)
    else:
        success()
    finally:
        cleanup()

RAISE AN EXCEPTION
    raise ValueError("bad input")

EXCEPTION CHAINING
    try:
        risky()
    except OriginalError as e:
        raise NewError("msg") from e

CUSTOM EXCEPTION
    class MyError(Exception):
        def __init__(self, msg, code):
            super().__init__(msg)
            self.code = code

CONTEXT MANAGER (decorator style)
    from contextlib import contextmanager

    @contextmanager
    def my_cm():
        setup()
        try:
            yield resource
        finally:
            teardown()

CONTEXT MANAGER (class style)
    class MyCM:
        def __enter__(self):
            setup()
            return self
        def __exit__(self, exc_type, exc_val, exc_tb):
            cleanup()

COMMON EXCEPTIONS
    ValueError      - int("abc"), int("3.14")
    TypeError       - "2" + 2, len(5)
    ZeroDivisionError - 10 / 0
    FileNotFoundError - open("missing.txt")
    IndexError      - [1,2,3][10]
    KeyError        - {"a":1}["b"]
    AttributeError  - None.append(1)
    ImportError      - import missing
```

---

## 14. Practice Assignments

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
```

---

### Assignment 2: Robust File Reader (Easy)

Create `read_json_config(path: str) -> dict` that:
- Returns `{}` if file doesn't exist
- Raises `ValueError` with a clear message if JSON is invalid
- Uses `with` statement for file handling
- Uses exception chaining (`raise ... from`)

---

### Assignment 3: Custom Exception Hierarchy (Medium)

Build a mini **Bank Account** system with:
- Custom exceptions: `BankError`, `InsufficientFundsError`, `InvalidAmountError`
- `BankAccount` class with `deposit()`, `withdraw()`, `get_balance()`
- `withdraw()` raises `InsufficientFundsError` with balance & requested amount
- Demo script that catches and prints user-friendly messages

---

### Assignment 4: Crash-Proof Contact Manager (Medium)

Create a program that:
- Asks user for contacts (name, phone, email)
- Validates each field:
  - Name: non-empty
  - Phone: digits only (allow dashes and spaces)
  - Email: must contain `@` and `.`
- Keeps asking until valid input is provided
- Stores contacts in a list and displays them at the end

---

### Assignment 5: Retry Decorator (Advanced)

Write a `@retry(max_attempts=3, delay=1, backoff=2)` decorator that:
- Retries the function on any `Exception`
- Waits `delay * backoff**(attempt-1)` seconds between retries
- Re-raises the last exception if all attempts fail
- Test it with a function that fails randomly (use `random.random()`)

---

### Assignment 6: Multi-File Merger with Error Handling (Hard)

Create a program that:
1. Takes multiple filenames as input
2. Merges their contents into a single file
3. Adds a header before each file's content showing the filename
4. Handles missing files gracefully (skip and warn, don't crash)
5. Handles permission errors gracefully
6. Reports a summary at the end (files merged, files skipped, total lines)

**Expected Output:**
```
Enter filename (or 'done'): file1.txt
Enter filename (or 'done'): missing.txt
  Warning: 'missing.txt' not found. Skipping.
Enter filename (or 'done'): file2.txt
Enter filename (or 'done'): done

=== MERGE SUMMARY ===
Files merged: 2
Files skipped: 1
Total lines: 45
Output saved to: merged.txt
```

---

## Summary

| Concept | What You Learned |
|---------|------------------|
| Syntax Errors | Caught at parse time, must fix in code |
| Runtime Exceptions | Caught during execution with `try/except` |
| `try/except` | Catch and handle errors |
| `else` | Run code only on success |
| `finally` | Always run (cleanup) |
| `raise` | Manually trigger exceptions |
| `raise ... from` | Chain exceptions, preserve traceback |
| Custom Exceptions | Create domain-specific error classes |
| Best Practices | Catch specific exceptions, keep `try` small |

---

> **Tomorrow:** Day 25 - Phase 1 Review & Capstone CLI Project - Build a Contact Book CLI App that uses everything you've learned!

---

> **Remember:** Error handling is about writing code that doesn't crash when things go wrong. Start with the easy assignments and work your way up. Happy coding! 🐍
