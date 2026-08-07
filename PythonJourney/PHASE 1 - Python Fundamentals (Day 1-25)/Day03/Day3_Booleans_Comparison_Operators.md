# � Day 3: Operators & Booleans

Welcome to Day 3! Today we will learn about **Operators**. Operators are special symbols in Python that carry out arithmetic or logical computation. The value that the operator operates on is called the operand.

---

## 📋 Table of Contents

1. [Arithmetic Operators](#1-arithmetic-operators)
2. [Assignment Operators](#2-assignment-operators)
3. [Booleans](#3-booleans)
4. [Comparison Operators](#4-comparison-operators)
5. [Logical Operators](#5-logical-operators)
6. [Practice Assignments](#-practice-assignments)

---

## 1. Arithmetic Operators

Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, etc.

| Operator | Name | Description | Example (`x = 10`, `y = 3`) | Result |
| :---: | :--- | :--- | :--- | :--- |
| `+` | Addition | Adds values on either side of the operator. | `x + y` | `13` |
| `-` | Subtraction | Subtracts right hand operand from left hand operand. | `x - y` | `7` |
| `*` | Multiplication | Multiplies values on either side of the operator. | `x * y` | `30` |
| `/` | Division | Divides left hand operand by right hand operand (always results in a float). | `x / y` | `3.333...` |
| `//`| Floor Division | Divides and returns the integer part of the quotient (rounds down). | `x // y` | `3` |
| `%` | Modulus | Divides left hand operand by right hand operand and returns the remainder. | `x % y` | `1` |
| `**`| Exponentiation | Performs exponential (power) calculation on operators. | `x ** y` | `1000` |

### Code Examples:
```python
a = 15
b = 4

print("Addition:", a + b)        # 19
print("Subtraction:", a - b)     # 11
print("Multiplication:", a * b)  # 60
print("Division:", a / b)        # 3.75
print("Floor Division:", a // b) # 3
print("Modulus:", a % b)         # 3
print("Exponentiation:", a ** b) # 50625
```

---

## 2. Assignment Operators

Assignment operators are used to assign values to variables.

| Operator | Example | Equivalent to | Description |
| :---: | :--- | :--- | :--- |
| `=` | `x = 5` | `x = 5` | Assigns value of right side expression to left side operand |
| `+=` | `x += 5` | `x = x + 5` | Adds right operand to left operand and assigns the result to left |
| `-=` | `x -= 5` | `x = x - 5` | Subtracts right operand from left operand and assigns the result to left |
| `*=` | `x *= 5` | `x = x * 5` | Multiplies right operand with left operand and assigns the result to left |
| `/=` | `x /= 5` | `x = x / 5` | Divides left operand with right operand and assigns the result to left |
| `%=` | `x %= 5` | `x = x % 5` | Takes modulus using two operands and assigns the result to left |
| `//=` | `x //= 5` | `x = x // 5` | Performs floor division on operators and assigns value to left |
| `**=` | `x **= 5` | `x = x ** 5` | Performs exponential calculation and assigns value to left |

### Code Examples:
```python
x = 10
print("Initial x:", x) # 10

x += 5  # Same as x = x + 5
print("After x += 5:", x) # 15

x -= 3  # Same as x = x - 3
print("After x -= 3:", x) # 12

x *= 2  # Same as x = x * 2
print("After x *= 2:", x) # 24
```

---

## 3. Booleans

A boolean is a value that can only be `True` or `False`.

- `True` means the condition is correct.
- `False` means the condition is not correct.

Example:
```python
is_raining = True
is_sunny = False
```

### Boolean values from expressions

Many expressions in Python return a boolean value automatically.

```python
print(5 > 3)    # True
print(2 == 4)   # False
print(7 != 5)   # True
```

---

## 4. Comparison Operators

Comparison operators compare two values and return a boolean.

| Operator | Name | Description |
| :---: | :--- | :--- |
| `==` | Equal to | Returns True if both values are equal |
| `!=` | Not equal to | Returns True if values are different |
| `>` | Greater than | Returns True if left is greater than right |
| `<` | Less than | Returns True if left is less than right |
| `>=` | Greater than or equal to | Returns True if left is greater than or equal to right |
| `<=` | Less than or equal to | Returns True if left is less than or equal to right |

### Examples:
```python
print(10 == 10)   # True
print(10 != 10)   # False
print(4 < 8)      # True
print(9 >= 9)     # True
print(3 <= 2)     # False
```

### Common Comparison Patterns

#### Compare numbers
```python
age = 16
print(age >= 18)  # False
```

#### Compare text
```python
name = "Sam"
print(name == "Sam")   # True
print(name != "Alex")  # True
```
*Note: String comparisons check the exact text, including capitalization.*

---

## 5. Logical Operators

Logical operators let you combine comparison expressions.

| Operator | Description |
| :---: | :--- |
| `and` | Returns `True` only if **both** conditions are `True` |
| `or` | Returns `True` if **at least one** condition is `True` |
| `not` | **Reverses** the boolean value |

### Examples:
```python
age = 20
has_ticket = True

print(age >= 18 and has_ticket)  # True (both are True)
print(age < 18 or has_ticket)     # True (one is True)
print(not has_ticket)             # False (reverses True to False)
```

### Truth Tables

**`and` — Both must be True:**
| A | B | A and B |
|---|---|---------|
| True | True | **True** |
| True | False | False |
| False | True | False |
| False | False | False |

**`or` — At least one must be True:**
| A | B | A or B |
|---|---|--------|
| True | True | **True** |
| True | False | **True** |
| False | True | **True** |
| False | False | False |

**`not` — Reverses the value:**
| A | not A |
|---|-------|
| True | **False** |
| False | **True** |

---

## 💡 6. Using Booleans in Decision Making

Booleans are most useful when you want your program to make decisions (which we will deep dive into on Day 5).

```python
temperature = 12
if temperature < 15:
    print("Wear a jacket.")
else:
    print("No jacket needed.")
```

---

## 📝 Practice Assignments

Now it's your turn to practice! Create your Python files (following the `Day3_TaskY.py` format) and try to solve the following problems:

### Assignment 1: The Bill Splitter
Imagine you and two friends went to a restaurant. 
- The total bill came to **$85**.
- You want to leave a **15%** tip.
- You need to split the total cost (bill + tip) evenly among the **3** of you.
- **File:** `Day3_Task1.py`

### Assignment 2: Rectangle Math
- Create two variables: `length` and `width`. Assign them the values `10` and `5` respectively.
- Calculate the **area** of the rectangle (`length * width`) and store it in a variable called `area`.
- Calculate the **perimeter** of the rectangle (`2 * (length + width)`) and store it in a variable called `perimeter`.
- Print both the area and the perimeter with descriptive messages.
- **File:** `Day3_Task2.py`

### Assignment 3: Time Converter
- Create a variable called `total_minutes` and set it to `135`.
- Using floor division (`//`) and modulus (`%`), calculate how many **hours** and remaining **minutes** this represents.
- Print the result in the format: `135 minutes is X hours and Y minutes.`
- **File:** `Day3_Task3.py`

### Assignment 4: Bank Account Simulation
- Create a variable `balance` and set it to `500`.
- You deposit `$150` (Use the `+=` operator to update the balance).
- You withdraw `$40` (Use the `-=` operator to update the balance).
- Your investments double your current balance (Use the `*=` operator to multiply the balance by `2`).
- Print the final balance after each operation to track the changes.
- **File:** `Day3_Task5.py`

### Assignment 5: Age Verifier
- Create a variable `age` and set it to `17`.
- Use a comparison operator to check if the person is `18` or older.
- Store the result in a boolean variable called `is_adult`.
- Print `is_adult`.
- **File:** `Day3_Task4.py`

### Assignment 6: Leap Year Checker
- Create a variable `year` and set it to `2024`.
- A year is a leap year if it's divisible by 4 **AND** (not divisible by 100 **OR** divisible by 400).
- Use logical operators to check this condition.
- Store the result in a boolean variable called `is_leap_year`.
- Print `is_leap_year`.
- **File:** `Day3_Task6.py`

### Assignment 7: Grade Calculator
- Create a variable `score` and set it to `85`.
- Use comparison and logical operators to assign a grade:
  - `A`: score >= 90
  - `B`: score >= 80 and score < 90
  - `C`: score >= 70 and score < 80
  - `D`: score >= 60 and score < 70
  - `F`: score < 60
- Print the grade.
- **File:** `Day3_Task7.py`

### Assignment 8: Number Classifier
- Create a variable `number` and set it to `7`.
- Use comparison and logical operators to check:
  - Is the number positive, negative, or zero?
  - Is the number even or odd?
- Print both results.
- **File:** `Day3_Task8.py`
