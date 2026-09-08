# Decorators

## 1. What Is a Higher-Order Function?

In Python, functions are objects. You can store them in variables, pass them to other functions, and return them from functions.

A **higher-order function** is a function that accepts another function as an argument or returns a function.

```python
def greet(name):
    return f"Hello, {name}!"


def run_function(function, value):
    return function(value)


print(run_function(greet, "Ava"))  # Hello, Ava!
```

The function `run_function()` receives `greet` as an argument and calls it later.

## 2. Inner Functions and Closures

A function defined inside another function is called an **inner function**.

```python
def make_greeter(message):
    def greet(name):
        return f"{message}, {name}!"

    return greet


friendly_greeter = make_greeter("Welcome")
print(friendly_greeter("Ben"))  # Welcome, Ben!
```

The inner function remembers the value of `message` even after `make_greeter()` has finished. This remembered value is called a **closure**.

## 3. What Is a Decorator?

A **decorator** is a function that adds behavior to another function without changing the original function's code.

A decorator usually:

1. Receives a function.
2. Defines a wrapper function.
3. Adds behavior before or after the original function runs.
4. Returns the wrapper function.

```python
def announce(function):
    def wrapper():
        print("The function is starting.")
        function()
        print("The function has finished.")

    return wrapper


def say_hello():
    print("Hello!")


say_hello = announce(say_hello)
say_hello()
```

Output:

```text
The function is starting.
Hello!
The function has finished.
```

The line `say_hello = announce(say_hello)` replaces the original function with the decorated wrapper.

## 4. The `@decorator` Syntax

Python provides shorter syntax for applying a decorator:

```python
def announce(function):
    def wrapper():
        print("The function is starting.")
        function()
        print("The function has finished.")

    return wrapper


@announce
def say_hello():
    print("Hello!")


say_hello()
```

This:

```python
@announce
def say_hello():
    print("Hello!")
```

means the same as:

```python
def say_hello():
    print("Hello!")


say_hello = announce(say_hello)
```

The decorator is applied when Python creates the function, before you call it.

## 5. Decorating Functions with Arguments

A decorator should usually accept `*args` and `**kwargs` so it can work with functions that have different parameters.

```python
def log_call(function):
    def wrapper(*args, **kwargs):
        print(f"Calling {function.__name__}")
        result = function(*args, **kwargs)
        print(f"Result: {result}")
        return result

    return wrapper


@log_call
def add(first, second):
    return first + second


add(3, 4)
```

- `*args` collects positional arguments.
- `**kwargs` collects keyword arguments.
- `function(*args, **kwargs)` passes them to the original function.
- The wrapper returns the original result so callers can still use it.

## 6. Preserving Function Metadata with `functools.wraps`

Without extra help, the wrapper replaces the original function's name and docstring:

```python
print(add.__name__)  # wrapper
```

Use `functools.wraps` to preserve the original metadata:

```python
from functools import wraps


def log_call(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Calling {function.__name__}")
        result = function(*args, **kwargs)
        print(f"Result: {result}")
        return result

    return wrapper
```

Now `add.__name__` remains `"add"`, and its docstring is preserved.

Use `@wraps(function)` whenever you write a function decorator.

## 7. Decorators That Accept Arguments

To configure a decorator, add another function layer:

```python
from functools import wraps


def repeat(times):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = function(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat(3)
def greet():
    print("Hello!")


greet()
```

There are three layers:

1. `repeat(times)` receives the decorator setting.
2. `decorator(function)` receives the function being decorated.
3. `wrapper(*args, **kwargs)` runs whenever the decorated function is called.

The syntax `@repeat(3)` first calls `repeat(3)`, which produces a decorator.

## 8. A Practical Timing Decorator

The `time.perf_counter()` function can measure how long a function takes to run.

```python
from functools import wraps
from time import perf_counter


def measure_time(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = function(*args, **kwargs)
        duration = perf_counter() - start
        print(f"{function.__name__} took {duration:.6f} seconds")
        return result

    return wrapper


@measure_time
def calculate_total(limit):
    return sum(range(1, limit + 1))


print(calculate_total(1_000_000))
```

The decorator measures the function without adding timing code to the function itself.

## 9. A Practical Authentication Decorator

A decorator can check a condition before allowing a function to run.

```python
from functools import wraps


def require_login(function):
    @wraps(function)
    def wrapper(is_logged_in, *args, **kwargs):
        if not is_logged_in:
            return "Please log in first."
        return function(is_logged_in, *args, **kwargs)

    return wrapper


@require_login
def view_profile(is_logged_in, username):
    return f"Profile for {username}"


print(view_profile(False, "Ava"))  # Please log in first.
print(view_profile(True, "Ava"))   # Profile for Ava
```

The decorator performs a common check before the protected function runs.

In a real application, authentication should use a trusted session or security system. This example is only for learning how decorators control access.

## 10. Class Decorators

A class decorator receives a class and returns a class. It can add or modify class behavior.

```python
def add_label(cls):
    cls.label = "Learning Python"
    return cls


@add_label
class Course:
    pass


course = Course()
print(course.label)  # Learning Python
```

The decorator syntax is equivalent to:

```python
Course = add_label(Course)
```

Class decorators are useful when you want to apply the same change to many classes.

## 11. Decorator Order

When multiple decorators are used, Python applies them from the bottom upward:

```python
@first
@second
def task():
    pass
```

This is equivalent to:

```python
task = first(second(task))
```

The order matters because each decorator receives the result of the decorator below it.

## 12. Common Mistakes

- Forgetting to return the wrapper from the decorator.
- Forgetting to return the original function's result.
- Not using `*args` and `**kwargs` when the decorated function accepts arguments.
- Forgetting `@wraps(function)`, which loses useful metadata.
- Calling the function while decorating it instead of returning a wrapper.
- Applying decorators in an order that changes the intended behavior.

## 13. Key Points

- Functions can be passed around like other Python values.
- A higher-order function accepts or returns another function.
- A decorator adds behavior without editing the decorated function directly.
- `@decorator` is shorthand for replacing a function with a decorated version.
- `*args` and `**kwargs` make decorators flexible.
- `functools.wraps` preserves the original function's name and docstring.
- Decorators can accept settings by using three nested function layers.
- Class decorators receive and return classes.

## Assignments

### Assignment 1: Execution Time Logger

Create a decorator named `log_execution_time`.

Requirements:

1. Use `time.perf_counter()` to record the start and end times.
2. Print the decorated function's name and execution time.
3. Support positional and keyword arguments.
4. Return the original function's result.
5. Use `functools.wraps`.
6. Test it with a function that calculates the sum of squares from `1` to a given limit.

Questions:

- Why should the timer surround the call to the original function?
- What problem does `@wraps` solve?
- Why are `*args` and `**kwargs` useful here?

### Assignment 2: Login Authentication Simulator

Create a decorator named `require_authentication`.

Requirements:

1. Accept a function that requires authentication.
2. Check whether the username and password are correct.
3. Call the original function only when authentication succeeds.
4. Return an access-denied message when authentication fails.
5. Preserve the original function's metadata.
6. Test the decorator with a `view_dashboard(username, password)` function.

Questions:

- What happens when authentication fails?
- Why should the protected function not run after failed authentication?
- How could a real application replace hard-coded credentials?

### Assignment 3: Repeat Decorator

Create a decorator factory named `repeat(times)`.

Requirements:

1. Accept the number of repetitions as an argument.
2. Run the decorated function that many times.
3. Pass arguments through to the decorated function.
4. Return the last result.
5. Test it with a greeting function.

### Assignment 4: Class Decorator

Create a class decorator named `add_version`.

Requirements:

1. Accept a class as an argument.
2. Add a `version` attribute to the class.
3. Add a method named `show_version()`.
4. Apply the decorator to a `Report` class.
5. Create an object and test the new attribute and method.

### Assignment 5: Decorator Investigation

Create two simple decorators that print messages before and after a function runs.

Apply both decorators to one function and observe the order of the output.

Questions:

- Which decorator runs first before the function?
- Which decorator runs first after the function?
- How does the order change when you swap the decorator lines?
