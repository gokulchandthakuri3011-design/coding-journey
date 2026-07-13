# Parameters & Arguments

## 1. Positional vs Keyword Arguments

### Positional Arguments
- Matched by position — the order matters.
```python
def describe_pet(animal, name):
    print(f"{name} is a {animal}")

describe_pet("dog", "Buddy")  # Buddy is a dog
```

### Keyword Arguments
- Matched by parameter name — order does not matter.
```python
describe_pet(animal="cat", name="Whiskers")  # Whiskers is a cat
describe_pet(name="Whiskers", animal="cat")  # same result
```

### Subnotes
- Positional arguments must come before keyword arguments in a call.
- Keyword arguments make code more readable when there are many parameters.
- You can mix them: `describe_pet("dog", name="Rex")`.

---

## 2. Default Parameters
- Assign a default value in the function definition.
- The parameter becomes optional when calling.

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Aisha")           # Hello, Aisha!
greet("Aisha", "Hi")     # Hi, Aisha!
```

### Subnotes
- Default parameters are evaluated **once** at function definition time.
- Avoid using mutable defaults like `[]` or `{}` — use `None` instead.
- Parameters with defaults must come after parameters without defaults.

```python
def bad_append(item, lst=[]):  # BAD — shared list across calls
    lst.append(item)
    return lst

def good_append(item, lst=None):  # GOOD
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

---

## 3. Arbitrary Arguments (`*args` and `**kwargs`)

### `*args` — variable number of positional arguments
- Captures extra positional arguments as a tuple.
```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))  # 10
```

### `**kwargs` — variable number of keyword arguments
- Captures extra keyword arguments as a dictionary.
```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Bob", age=30, city="NYC")
```

### Subnotes
- `args` and `kwargs` are convention names — you can use any name after `*` or `**`.
- `*args` must come before `**kwargs`.
- You can use both together: `def func(*args, **kwargs)`.
- Unpacking works in reverse too: `func(*list_arg)` and `func(**dict_arg)`.

---

## 4. Positional-Only and Keyword-Only Parameters

### Positional-Only (`/`)
- Parameters before `/` must be passed positionally (cannot use keyword).
```python
def divide(a, b, /):
    return a / b

divide(10, 2)   # OK
# divide(a=10, b=2)  # ERROR
```

### Keyword-Only (`*`)
- Parameters after `*` must be passed as keyword arguments.
```python
def safe_divide(a, b, *, precision=2):
    result = a / b
    return round(result, precision)

safe_divide(10, 3)              # OK
safe_divide(10, 3, precision=4) # OK
# safe_divide(10, 3, 4)         # ERROR
```

### Combined
```python
def func(pos_only, /, pos_or_kw, *, kw_only):
    pass
```

### Subnotes
- Positional-only (`/`) was added in Python 3.8.
- Keyword-only (`*`) was added in Python 3.0.
- Use positional-only when the parameter name is not meaningful.
- Use keyword-only to force clarity in function calls.

---

## 5. Type Hints in Function Definitions
- Annotate parameter and return types for clarity and tooling support.

```python
def add(x: int, y: int) -> int:
    return x + y

def greet(name: str, age: int = 18) -> str:
    return f"{name} is {age} years old"
```

### Subnotes
- Type hints are **not enforced** at runtime — they are for developers and tools (mypy, linters, IDE autocomplete).
- Use `from typing import ...` for complex types (`List`, `Dict`, `Optional`, `Union`, `Tuple`).
- Modern Python (3.9+) allows built-in generics: `list[int]`, `dict[str, int]`.

```python
from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    # returns a name or None
    ...
```

---

## 6. Parameter Passing — Summary

| Concept | Syntax | Purpose |
|---|---|---|
| Positional | `def f(a, b)` | Order matters |
| Keyword | `f(a=1, b=2)` | Named arguments |
| Default | `def f(a=0)` | Optional parameters |
| `*args` | `def f(*args)` | Variable positional |
| `**kwargs` | `def f(**kwargs)` | Variable keyword |
| Positional-only | `def f(a, /)` | Force positional |
| Keyword-only | `def f(*, a)` | Force keyword |
| Type hints | `def f(a: int) -> str` | Type annotations |

---

## 7. Assignment Questions

### Easy
1. Write a function `multiply(a, b)` that returns the product of two numbers. Call it using both positional and keyword arguments.
2. Create a function `welcome(name, message="Welcome")` that prints a greeting. Test it with and without the `message` argument.
3. Write a function `average(*numbers)` that returns the average of any number of arguments.

### Medium
4. Write a function `create_profile(**kwargs)` that prints a person's profile details. Call it with different keyword arguments.
5. Create a function `calculate(a, b, /, operation="add")` that performs addition or subtraction. The first two params must be positional-only.
6. Write a function `format_text(*, text, uppercase=False)` where both params are keyword-only. If `uppercase` is True, return the text in uppercase.
7. Create a function `build_url(base, *paths, **params)` that joins base URL with path segments and appends query parameters from `**params`.

### Hard
8. Write a function `flexible_operation(a, b, /, *args, operation="add", **kwargs)` that:
   - Takes two required positional-only args `a`, `b`.
   - Accepts extra positional args via `*args`.
   - Has a keyword-only `operation` parameter (default `"add"`).
   - Accepts extra keyword args via `**kwargs`.
   - If `operation` is `"add"`, sum all numbers. If `"multiply"`, multiply all.
   - Print any extra kwargs as metadata.

9. Write a function `safe_function` that takes another function and its arguments (`*args`, `**kwargs`), calls it, wraps it in a try-except, and returns either the result or an error message.

10. Create a function `register_user(name, /, age=18, *, email, country="Unknown")` with type hints. It should print a summary. Demonstrate all parameter types in one call.
