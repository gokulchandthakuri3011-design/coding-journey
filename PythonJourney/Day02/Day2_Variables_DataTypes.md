# 📅 Day 2: Variables & Data Types

Welcome to Day 2! Today we are looking at the foundational building blocks of any Python program: **Variables** and **Data Types**.

---

## 📦 1. What is a Variable?

Think of a variable as a labeled box or a container where you can store data. Once you store data in a variable, you can use that label to refer to the data later in your program.

### How to Create a Variable
In Python, you create a variable the moment you assign a value to it using the equals sign `=`.

```python
# Storing a name in a variable called "player_name"
player_name = "Alice"

# Storing a number in a variable called "score"
score = 100

# Printing the variables
print(player_name)
print(score)
```

### 🚨 Rules for Naming Variables:
1. Must start with a letter (a-z, A-Z) or an underscore (`_`).
2. Cannot start with a number.
3. Can only contain alpha-numeric characters and underscores (A-z, 0-9, and `_`).
4. **Case-sensitive**: `Age`, `age`, and `AGE` are three different variables.
5. Use **snake_case** for multi-word variables (e.g., `my_first_name = "John"`).

---

## 🗂️ 2. Basic Data Types

Data types specify what kind of data is stored in a variable. Python has 4 main basic types:

### 1. Integer (`int`)
Whole numbers without a decimal point. They can be positive or negative.
```python
age = 25
temperature = -5
```

### 2. Float (`float`)
Numbers that contain a decimal point.
```python
price = 19.99
pi = 3.14159
```

### 3. String (`str`)
A sequence of characters (text). Strings must be enclosed in single quotes `''` or double quotes `""`.
```python
greeting = "Hello, Python!"
letter = 'A'
```

### 4. Boolean (`bool`)
Represents one of two values: `True` or `False`. Used heavily for logic and decision making. *(Note: Must start with a capital T or F).*
```python
is_game_over = False
is_python_fun = True
```

---

## 🔍 3. Checking Data Types using `type()`

Sometimes you'll want to know what data type a variable is holding. You can use Python's built-in `type()` function to find out!

```python
x = 10
y = 10.5
z = "10"
is_active = True

print(type(x))         # Output: <class 'int'>
print(type(y))         # Output: <class 'float'>
print(type(z))         # Output: <class 'str'>
print(type(is_active)) # Output: <class 'bool'>
```
*Notice how `z` looks like a number, but because it is inside quotes, Python treats it as a String!*

---

## 💻 4. Practice Exercises

Spend your practice time today writing code for the following tasks:

### Assignment 1: Create your profile
Create variables to store your `first_name` (string), `last_name` (string), `age` (integer), `height_in_meters` (float), and `likes_coding` (boolean). Print all variables and their types.
- **File to create/modify:** `Day2_Task1.py`

### Assignment 2: Coffee Shop Order
Create variables for a coffee order:
- `customer_name` (string, e.g., "Gokul")
- `coffee_type` (string, e.g., "Latte")
- `quantity` (integer, e.g., 2)
- `price_per_cup` (float, e.g., 4.50)
- `is_takeaway` (boolean, e.g., True)
Calculate `total_cost` by multiplying `quantity` by `price_per_cup`. Print a nice summary receipt, including `total_cost` and type checks.
- **File to create/modify:** `Day2_Task2.py`
