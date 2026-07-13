# Day 18: Variable Scope

## 1. Local vs Global Variables

- **Local variable**: defined inside a function, accessible only within that function.
- **Global variable**: defined at the top level of a module, accessible everywhere.

```python
x = 10          # global

def foo():
    y = 5       # local to foo
    print(x)    # can read global
    print(y)

foo()
print(x)        # 10
# print(y)      # NameError — y is local
```

- Local variables are created when the function runs and destroyed when it returns.
- Python looks up variables in this order: **LEGB** — Local → Enclosing → Global → Built-in.

---

## 2. The `global` Keyword

- Used inside a function to **reassign** a global variable (not just read it).
- Generally **avoid** `global` — it makes code hard to debug and test.

```python
count = 0

def increment():
    global count
    count += 1   # modifies the global `count`

increment()
print(count)     # 1
```

- Without `global`, `count += 1` would create a **new local** variable named `count`, leaving the global unchanged.

> **Rule of thumb:** Pass values as arguments and return results instead of relying on `global`.

---

## 3. The `nonlocal` Keyword

- Used inside **nested functions** to refer to a variable in the enclosing (outer) function's scope.
- Unlike `global`, it doesn't reach all the way to the module level — only one level up.

```python
def outer():
    msg = "Hello"

    def inner():
        nonlocal msg
        msg = "World"   # modifies outer's `msg`

    inner()
    print(msg)          # "World"

outer()
```

- Without `nonlocal`, assigning to `msg` inside `inner` would create a new local `msg` in `inner`.
- Works for any enclosing scope level (not just the immediate outer function).

---

## 4. Closures

- A **closure** is a nested function that **remembers** the variables from its enclosing scope even after that scope has finished executing.

```python
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

double = make_multiplier(2)
print(double(5))       # 10 — remembers n=2
```

**Argument mapping:**
- `make_multiplier(2)` → `2` is passed to parameter **`n`** (enclosing scope)
- `double(5)` → `5` is passed to parameter **`x`** (inner function)

**Chaining calls (no intermediate variable):**
You can skip the `double = make_multiplier(2)` step and call the returned function immediately:

```python
print(make_multiplier(2)(5))   # 10 — works! make_multiplier(2) returns a function, then (5) calls it
```

> ⚠️ **Common mistake:** `make_multiplier(2(5))` is a **syntax error**. Python reads this as "call `2` with argument `5`", but `2` is an integer, not a function. The correct syntax is `make_multiplier(2)(5)` — two separate sets of parentheses.

- Three conditions for a closure:
  1. There is a nested function.
  2. The nested function references a variable from the enclosing scope.
  3. The enclosing function returns the nested function.

- Use cases: counter factories, partial application, decorators.

---

## Summary Table

| Concept | Scope Level | Keyword Needed? | Modifies Variable In |
|---------|------------|----------------|---------------------|
| Local variable | Function | No | Current function |
| Global (read) | Module | No | — |
| Global (write) | Module | `global` | Module top-level |
| Enclosing (write) | Outer function | `nonlocal` | Immediately enclosing scope |
| Closure | Nested function | No (reads only) | Enclosing scope captured |

---

# Assignment Questions

### Easy
1. What will this code print? Explain why.

```python
x = 5
def func():
    x = 10
func()
print(x)
```

2. What is the difference between a local variable and a global variable?

### Medium
3. Fix the bug in this code so it prints `1 2 3` without using `return`:

```python
count = 0
def increment():
    count += 1

for _ in range(3):
    increment()
    print(count, end=" ")
```

4. Write a function `make_counter()` that returns a closure. Each call to the returned function should increment and return a counter starting from 0.

```python
counter = make_counter()
print(counter())  # 0
print(counter())  # 1
print(counter())  # 2
```

5. What does this code print? Explain the LEGB lookup.

```python
a = "global"
def outer():
    a = "outer"
    def inner():
        a = "inner"
        print(a)
    inner()
    print(a)
outer()
print(a)
```

### Hard
6. Write a function `make_multiplier(factor)` that returns a closure which multiplies any given number by `factor`. Then create `double` and `triple` from it and demonstrate they work independently.

7. What will this print and why?
# It won't be printing any number but 'LocalVariableBoundError' because assigning x has happened after print(x) statements and we didn't use keyword 'global' to reference x, whose value is 5 outside the function.

```python
def func():
    print(x)
    x = 10

x = 5
func()
```

8. Rewrite this code to avoid the `global` keyword entirely, using only function parameters and return values.

```python
total = 0
def add_to_total(n):
    global total
    total += n

add_to_total(5)
add_to_total(10)
print(total)
```

> **What if we initialize `total = 0` inside the function and `return total` instead?**
>
> ```python
> def add_to_total(n):
>     total = 0          # creates a NEW local variable each call
>     total += n
>     return total
>
> print(add_to_total(5))   # 5
> print(add_to_total(10))  # 10
> ```
>
> **This does NOT work as intended.** Each call to `add_to_total` creates a fresh local `total = 0`, so the value never accumulates across calls. The function simply returns `n` each time. To accumulate values without `global`, you must pass the current total as a parameter and return the updated value:
>
> ```python
> def add_to_total(total, n):
>     return total + n
>
> total = 0
> total = add_to_total(total, 5)   # 5
> total = add_to_total(total, 10)  # 15
> print(total)                     # 15
> ```

9. Explain in your own words: what is a closure? Give a real-world scenario where you would use one instead of a class.
