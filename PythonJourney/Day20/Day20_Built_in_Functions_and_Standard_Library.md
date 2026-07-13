# Day 20: Built-in Functions & Standard Library

## Goal
Learn how to use Python's most useful built-in functions and import modules from the standard library to build better programs.

---

## 1. Built-in Functions
Built-in functions are available in Python without importing anything.

### Common built-in functions
- `len()` → returns the length of a string, list, tuple, or dictionary
- `sum()` → adds all values in an iterable
- `max()` → returns the largest value
- `min()` → returns the smallest value
- `any()` → returns `True` if at least one value is truthy
- `all()` → returns `True` if all values are truthy
- `zip()` → combines multiple iterables element by element
- `enumerate()` → gives both the index and value while looping

### Example
```python
numbers = [10, 20, 30, 40]

print(len(numbers))      # 4
print(sum(numbers))      # 100
print(max(numbers))      # 40
print(min(numbers))      # 10
```

### Example with `any()` and `all()`
```python
values = [True, False, True]
print(any(values))   # True
print(all(values))   # False
```

### Example with `zip()`
```python
names = ["Alice", "Bob", "Charlie"]
ages = [22, 25, 30]

for name, age in zip(names, ages):
    print(name, age)
```

### Example with `enumerate()`
```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

---

## 2. Standard Library Modules
Python comes with many built-in modules that help you solve real-world problems.

### `math`
Used for mathematical operations.

```python
import math

print(math.pi)
print(math.sqrt(16))
print(math.factorial(5))
```

### `random`
Used to generate random values.

```python
import random

print(random.randint(1, 10))
print(random.choice(["rock", "paper", "scissors"]))
```

### `datetime`
Used to work with dates and times.

```python
from datetime import datetime

now = datetime.now()
print(now)
print(now.strftime("%Y-%m-%d %H:%M:%S"))
```

### `sys`
Used to interact with the Python runtime.

```python
import sys

print(sys.version)
print(sys.platform)
```

### `os`
Used to interact with the operating system.

```python
import os

print(os.getcwd())
print(os.listdir())
```

---

## 3. Why These Are Important
Built-in functions and standard library modules help you:
- write shorter code
- solve problems faster
- avoid reinventing the wheel
- build useful real-world programs

---

## 4. Practice Examples
### Example 1: Find average of a list
```python
numbers = [10, 20, 30, 40]
average = sum(numbers) / len(numbers)
print(average)
```

### Example 2: Check if all numbers are positive
```python
nums = [2, 5, 8, 10]
print(all(n > 0 for n in nums))
```

### Example 3: Create a simple random number game
```python
import random

secret = random.randint(1, 10)
print(secret)
```

---

## 5. Assignment Questions
### Easy
1. Write a program that takes a list of numbers and prints the minimum, maximum, and sum.
2. Use `any()` and `all()` to check whether a list contains at least one positive number and whether all numbers are positive.
3. Write a program that uses `enumerate()` to print each item in a list with its index.

### Medium
4. Create a program that uses `math` to calculate the area of a circle given its radius.
5. Make a small guessing game where the computer picks a random number between 1 and 20.
6. Write a program that uses `datetime` to print the current date and time in a nice format.

### Challenge
7. Create a script that uses `os` to list all files and folders in the current directory.
8. Build a small tool that takes a list of names and uses `zip()` to combine them with a list of ages.
9. Write a program that uses `len()`, `sum()`, `max()`, and `min()` together to analyze a list of test scores.

---

## 6. Mini Project Idea
Build a simple “Student Score Analyzer” that:
- takes a list of scores
- calculates the average
- finds the highest and lowest score
- prints whether the class passed overall

---

## 7. Summary
By the end of Day 20, you should be able to:
- use basic built-in functions confidently
- import and use common standard library modules
- solve small problems using Python's ready-made tools
