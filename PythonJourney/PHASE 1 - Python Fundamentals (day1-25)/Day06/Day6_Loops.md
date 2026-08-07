# 📅 Day 6: Loops

Today you will learn how to repeat actions in Python using `while` and `for` loops. Loops help your programs handle lists, repeat tasks, and process data one step at a time.

## 🌀 1. While Loops

A `while` loop repeats as long as a condition is `True`.

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### Avoiding infinite loops
An infinite loop happens when the loop condition never becomes `False`.

```python
while True:
    break  # stops the loop
```

## 🔁 2. For Loops

A `for` loop repeats over a sequence such as a list or a range of numbers.

```python
for i in range(5):
    print(i)
```

### Using `range()`
The `range()` function generates a sequence of numbers.

```python
for i in range(2, 10, 2):
    print(i)
```

## 🚦 3. Loop Control Statements

- `break` stops the loop immediately.
- `continue` skips the rest of the current loop iteration.
- `pass` does nothing but keeps the loop structure valid.

```python
for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)
```

## 🧩 Practice Exercises

### Assignment 1: Number Collector
Write a program that keeps asking the user for numbers until they type `done`. Use a `while` loop and `break`.
- Convert each valid input to `int`
- Ignore empty input with `continue`
- Print the total sum and count when finished.

### Assignment 2: Even Number Printer
Write a `for` loop using `range()` to print even numbers from 2 to 20.
- Use `continue` to skip odd numbers.

### Assignment 3: Simple Loop Menu
Write a program that shows a menu and repeats until the user types `quit`.
- Use `while True`.
- Use `break` to exit.
- Use `pass` as a placeholder for unsupported options.
