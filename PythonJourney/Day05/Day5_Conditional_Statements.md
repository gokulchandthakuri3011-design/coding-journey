# 📅 Day 5: Conditional Statements (If/Else)

Welcome to Day 5! Today we will learn about **Control Flow**—specifically, how to make decisions in your code using conditional statements. Conditional statements allow your program to execute different blocks of code based on whether a condition is true or false.

## 1. The `if` Statement

The `if` statement is the most basic form of decision-making in Python. It executes a block of code only if a specified condition evaluates to `True`.

**Syntax:**
```python
if condition:
    # Code to execute if the condition is True
```

**Example:**
```python
age = 20
if age >= 18:
    print("You are eligible to vote.")
```

*Note: Python uses indentation (whitespace) to define code blocks. Make sure the code inside your `if` statement is indented!*

## 2. The `else` Statement

The `else` statement is used in conjunction with an `if` statement. It executes a block of code when the `if` condition evaluates to `False`.

**Syntax:**
```python
if condition:
    # Code to execute if the condition is True
else:
    # Code to execute if the condition is False
```

**Example:**
```python
temperature = 15

if temperature > 25:
    print("It's a warm day.")
else:
    print("It's a bit chilly.")
```

## 3. The `elif` Statement

What if you have more than two possibilities? The `elif` (short for "else if") statement allows you to check multiple conditions sequentially. You can have as many `elif` statements as you want between an `if` and an `else`.

**Syntax:**
```python
if condition1:
    # Code if condition1 is True
elif condition2:
    # Code if condition1 is False and condition2 is True
else:
    # Code if both condition1 and condition2 are False
```

**Example:**
```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
```

## 4. Nested `if` Statements

You can place an `if` statement inside another `if` statement. This is called nesting, and it's useful when you need to check a secondary condition only if the first condition is `True`.

**Example:**
```python
has_ticket = True
is_vip = False

if has_ticket:
    print("Welcome to the event!")
    if is_vip:
        print("Please head to the VIP lounge.")
    else:
        print("Please find your seat in the general area.")
else:
    print("You need a ticket to enter.")
```

---

## 🛠️ Practice Exercises

### Exercise 1: Even or Odd?
Write a program that asks the user for an integer and prints whether the number is even or odd.
*(Hint: Use the modulo operator `%`. A number is even if `number % 2 == 0`)*

### Exercise 2: Movie Age Restrictions
Write a program that asks for the user's age and tells them what kind of movies they can watch based on these rules:
- Under 13: "G and PG movies"
- 13 to 16: "PG-13 movies"
- 17 and older: "R-rated movies"

### Exercise 3: Number Positivity
Write a program that takes a number as input and checks if it is positive, negative, or zero using `if`, `elif`, and `else`.

Happy Coding!
