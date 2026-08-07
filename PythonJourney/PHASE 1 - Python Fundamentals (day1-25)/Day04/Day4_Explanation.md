# 📅 Day 4: User Input, Type Casting & String Manipulation

Welcome to Day 4! Today we combine three powerful Python skills: reading input from the user, converting values between types, and manipulating text with strings.

---

## 🧠 1. Getting User Input with `input()`

The `input()` function lets the program pause and wait for user text. Whatever the user types is always returned as a string.

```python
name = input("What is your name? ")
print("Hello, " + name + "!")
```

> **Important:** `input()` always returns a string, even when the user types numbers.

---

## 🔢 2. Why Type Casting Matters

Because `input()` returns text, you must convert user input into numbers before doing math.

Common type casts:
- `int(value)` converts to an integer
- `float(value)` converts to a floating-point number
- `str(value)` converts to a string
- `bool(value)` converts to a boolean (empty strings become `False`, non-empty become `True`)

```python
age = input("How old are you? ")
print(type(age))  # <class 'str'>

age_int = int(age)
print(type(age_int))  # <class 'int'>
```

### Example: Adding two numbers from user input

```python
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Without type casting, these are strings:
print(num1 + num2)  # Example: if inputs are 2 and 3, output is "23" (concatenation)

# Convert to integers first:
result = int(num1) + int(num2)
print(result)  # Output: 5
```

---

## 🔗 3. String Manipulation

Strings are sequences of characters. You can join text together and repeat it.

### Concatenation
Use the `+` operator to combine strings.

```python
greeting = "Hello"
name = "Alice"
message = greeting + ", " + name + "!"
print(message)  # Hello, Alice!
```

### Repetition
Use `*` to repeat a string.

```python
laugh = "Ha"
print(laugh * 3)  # HaHaHa
```

---

## 🛠️ 4. Handy String Methods

Strings come with built-in methods that let you clean and change text.

```python
text = "  Python is AMAZING!  "
print(text.lower())   # "  python is amazing!  "
print(text.upper())   # "  PYTHON IS AMAZING!  "
print(text.strip())   # "Python is AMAZING!"
print(text.replace("AMAZING", "FUN"))  # "  Python is FUN!  "
```

---

## 💬 5. F-Strings

F-strings are a clean, modern way to insert variables into text.

```python
name = "Alex"
age = 20
print(f"Hello {name}, you are {age} years old.")
```

---

## 💻 Practice Exercises

Solve these exercises by creating the corresponding `Day4_TaskY.py` files.

### Assignment 1: Favorite Number Calculator
1. Ask the user for their favorite number using `input()`.
2. Convert that input into an integer.
3. Add `10` to that number and print the result.
4. Use an f-string to show the original number and the new number.
- **File:** `Day4_Task1.py`

### Assignment 2: Simple Grocery Total
1. Ask the user for the price of one item using `input()`.
2. Ask how many items they want to buy.
3. Convert the price to `float` and the quantity to `int`.
4. Calculate the total cost and print it.
- **File:** `Day4_Task2.py`

### Assignment 3: Password Cleaner
1. Ask the user for their password, including leading/trailing spaces.
2. Use `.strip()` to clean it.
3. Print the length of both the original password and the cleaned password to show the difference.
- **File:** `Day4_Task3.py`

### Assignment 4: Ticket Formatter
1. Create variables: `movie_title` (string), `time` (string), and `ticket_price` (float).
2. Use an **f-string** to build a ticket string and print it.
   *Example Output: `Movie: The Matrix \| Time: 8:00 PM \| Price: $12.50`*
- **File:** `Day4_Task4.py`

### Assignment 5: The Shouty Greeter
1. Ask the user for their `first_name` and `last_name` with messy capitalization (e.g. "aLiCe").
2. Use string methods to fix both names to be entirely uppercase.
3. Print a welcome greeting using string concatenation.
- **File:** `Day4_Task5.py`
