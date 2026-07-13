# 📅 Day 4: User Input, Type Casting & String Manipulation

Welcome to Day 4! Today we combine two powerful Python skills: reading input from the user, converting values between types, and manipulating text with strings.

## 🧠 1. Getting User Input with `input()`

The `input()` function lets the program pause and wait for user text. Whatever the user types is always returned as a string.

```python
name = input("What is your name? ")
print("Hello, " + name + "!")
```

> Important: `input()` always returns a string, even when the user types numbers.

## 🔢 2. Why Type Casting Matters

Because `input()` returns text, you must convert user input into numbers before doing math.

Common casts:
- `int(value)` converts to an integer
- `float(value)` converts to a floating-point number
- `str(value)` converts to a string
- `bool(value)` converts to a boolean (careful with empty strings)

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
print(num1 + num2)  # Example: if inputs are 2 and 3, output is 23

# Convert to integers first:
result = int(num1) + int(num2)
print(result)  # Output: 5
```

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

## 🛠️ 4. Handy String Methods

Strings come with built-in methods that let you change text.

```python
text = "  Python is AMAZING!  "
print(text.lower())   # "  python is amazing!  "
print(text.upper())   # "  PYTHON IS AMAZING!  "
print(text.strip())   # "Python is AMAZING!"
print(text.replace("AMAZING", "FUN"))  # "  Python is FUN!  "
```

## 💬 5. F-Strings

F-strings are a clean way to insert variables into text.

```python
name = "Alex"
age = 20
print(f"Hello {name}, you are {age} years old.")
```

---

## 💻 Practice Exercises

### Assignment 1: Favorite Number Calculator
1. Ask the user for their favorite number using `input()`.
2. Convert that input into an integer.
3. Add `10` to that number and print the result.
4. Use an f-string to show the original number and the new number.

Example output:
```
Your favorite number is 7.
Ten more than that is 17.
```

### Assignment 2: Simple Grocery Total
1. Ask the user for the price of one item using `input()`.
2. Ask how many items they want to buy.
3. Convert the price to `float` and the quantity to `int`.
4. Calculate the total cost and print it.

### Assignment 3: Password Cleaner
1. Create a variable `password` and assign it a string with extra spaces.
2. Use `.strip()` to clean it.
3. Print the length of both the original and cleaned password.

### Assignment 4: Ticket Formatter
1. Create variables: `movie_title`, `time`, `ticket_price`.
2. Use an f-string to build a ticket string.
3. Print the ticket.
