# Return Values

## 1. The `return` Statement

- The `return` statement sends a value back from a function to the caller.
- Without `return`, a function returns `None` by default.

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 8
```

### Subnotes
- `return` immediately exits the function — no code after it runs.
- You can return any data type: int, str, list, dict, tuple, etc.
- A function can have multiple `return` statements (e.g., in conditionals).

---

## 2. Returning Multiple Values

- Python allows returning multiple values using a tuple.

```python
def get_name_and_age():
    return "Alice", 25

name, age = get_name_and_age()  # tuple unpacking
print(name, age)  # Alice 25
```

### Subnotes
- Python automatically packs multiple return values into a tuple.
- Use tuple unpacking to assign each value to a variable.
- You can also return a named tuple or a dataclass for clarity.

```python
def get_coordinates():
    return 10.5, 20.3

x, y = get_coordinates()
```

---

## 3. Returning `None`

- If a function has no `return` statement, it implicitly returns `None`.
- A function with only `return` (no value) also returns `None`.

```python
def greet(name):
    print(f"Hello, {name}!")

result = greet("Bob")
print(result)  # None
```

### Subnotes
- Use `return` without a value to exit early: `if not valid: return`.
- Functions that only print or modify global state typically return `None`.
- Checking `if result is None` is a common pattern.

---

## 4. Returning Different Types

- A function can return different types depending on the path taken.

```python
def find_user(user_id):
    users = {1: "Alice", 2: "Bob"}
    if user_id in users:
        return users[user_id]
    return None  # or raise an exception

print(find_user(1))  # Alice
print(find_user(99))  # None
```

### Subnotes
- Use type hints (`Optional[str]`) to document possible return types.
- Returning `None` is common for "not found" scenarios.
- Alternatively, raise an exception instead of returning `None`.

```python
from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    ...
```

---

## 4.5. `Optional` — Type Hints for "Maybe Nothing"

- `Optional[T]` means a function can return **type `T` or `None`**.
- It is **purely documentation** — Python ignores it at runtime.
- It helps **IDEs**, **type checkers** (like `mypy`), and **readers** understand what to expect.

```python
from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    """Returns a name if found, or None if not."""
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

name = find_user(99)
# mypy warns: "None has no attribute 'upper'"
# print(name.upper())  # ❌ Would crash if name is None!
```

### Why use `Optional`?

| Without `Optional` | With `Optional` |
|---|---|
| `def find_user(user_id):` | `def find_user(user_id: int) -> Optional[str]:` |
| "What does it return? Maybe a string? Maybe nothing?" | "It returns a string or None — I'll handle that." |
| No IDE warnings | IDE warns: "You might get None here!" |
| Bugs only caught at runtime | `mypy` catches bugs before running |

### Key points
- `Optional[str]` is shorthand for `Union[str, None]`.
- It does **not** change program behavior — only improves clarity and safety.
- Use it when a function might return "nothing" (i.e., `None`) in some cases.

```python
from typing import Optional

def safe_divide(a: float, b: float) -> Optional[float]:
    if b == 0:
        return None  # can't divide by zero
    return a / b

result = safe_divide(10, 0)
if result is not None:
    print(result)  # safe — we checked for None first
```

---

## 5. Returning Functions (Higher-Order Functions)

- A function can return another function.

```python
def make_multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

double = make_multiplier(2)
print(double(5))  # 10
```

### Subnotes
- The inner function "remembers" the outer function's variables — this is called a **closure**.
- Useful for creating reusable, customized functions.
- Commonly used in decorators and functional programming.

---

## 6. Common Patterns

### Pattern 1: Early Return (Guard Clauses)
```python
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
```

### Pattern 2: Returning Collections
```python
def get_even_numbers(numbers):
    return [n for n in numbers if n % 2 == 0]
```

### Pattern 3: Returning a Dictionary
```python
def user_profile(name, age):
    return {"name": name, "age": age}
```

### Subnotes
- Early returns improve readability by handling edge cases first.
- Returning collections or dicts is common in data-processing functions.
- Always document what the function returns.

---

## 7. Summary Table

| Concept | Syntax | Example |
|---|---|---|
| Single return | `return value` | `return a + b` |
| Multiple returns | `return a, b` | `return x, y, z` |
| No return | (implicit) | `return None` |
| Early exit | `return` | `if error: return` |
| Return function | `return func` | `return inner()` |
| Type hint | `-> Type` | `-> Optional[str]` |

---

## 8. Assignment Questions

### Easy
1. Write a function `square(n)` that returns the square of a number. Test with integers and floats.
2. Write a function `is_even(n)` that returns `True` if `n` is even, `False` otherwise.
3. Write a function `greet(name)` that prints `"Hello, {name}!"` and returns `None`. Print the return value.

### Medium
4. Write a function `min_max(numbers)` that returns both the minimum and maximum of a list. Use tuple unpacking to capture both values.
5. Write a function `swap(a, b)` that returns the values swapped. Test: `b, a = swap(1, 2)`.
6. Write a function `count_vowels(text)` that returns the number of vowels in the string.

### Hard
7. Write a function `categorize(numbers)` that returns a dictionary with keys `"positive"`, `"negative"`, and `"zero"`, each containing a list of the respective numbers.
8. Write a function `make_greeting(greeting_type)` that returns a function. If `greeting_type` is `"formal"`, return a function that prints `"Dear {name}, ..."`. If `"casual"`, return a function that prints `"Hey {name}!"`.
9. Write a function `safe_divide(a, b)` that returns the result of `a / b` if `b != 0`, or returns `None` if `b == 0`. Use type hints: `-> Optional[float]`.
10. Write a function `transform(data, operation)` that takes a list and a string (`"upper"`, `"lower"`, `"reverse"`), and returns a new list transformed accordingly. Return `None` if the operation is invalid.
