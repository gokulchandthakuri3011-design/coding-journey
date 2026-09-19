# Day 31: Regular Expressions (Regex)

## 1. What is Regular Expression?

A regular expression, or regex, is a pattern used to search, match, and manipulate text.

Python provides the built-in `re` module for this.

```python
import re

text = "My email is hello@example.com"
match = re.search(r"[a-z]+@[a-z]+\.[a-z]+", text)

if match:
    print("Email found:", match.group())
```

Regex is very useful when you want to:

- validate email addresses
- check phone numbers
- find repeated patterns in text
- replace unwanted characters
- extract values from strings

---

## 2. Why Use Regex?

Without regex, you would need many manual checks and string operations.
Regex helps you work with patterns instead of exact text.

Example:

```python
text = "Contact me at 98765-43210"
pattern = r"\d{5}-\d{5}"

result = re.search(pattern, text)
print(result.group())
```

This finds a 5-digit number, a hyphen, and another 5-digit number.

---

## 3. Important Regex Symbols

Here are the most common pattern rules:

- `.` → matches any character except newline
- `*` → zero or more repetitions
- `+` → one or more repetitions
- `?` → zero or one repetition
- `\d` → digit (`0-9`)
- `\w` → word character (letters, digits, underscore)
- `\s` → whitespace
- `[]` → a character class
- `^` → start of string
- `$` → end of string
- `|` → OR
- `{m,n}` → repeat between `m` and `n` times

Examples:

```python
import re

print(re.search(r"\d+", "Age is 25"))
print(re.search(r"[A-Z]+", "HELLO WORLD"))
print(re.search(r"hello|world", "hello there"))
```

---

## 4. Common Regex Functions in Python

### `re.search()`
Finds the first match anywhere in the string.

```python
import re

text = "The code is 4567"
match = re.search(r"\d+", text)
print(match.group())
```

### `re.match()`
Checks only at the beginning of the string.

```python
import re

text = "Python123"
print(re.match(r"Python", text))
```

### `re.findall()`
Returns all matching parts as a list.

```python
import re

text = "Numbers: 12, 34, 56"
print(re.findall(r"\d+", text))
```

### `re.sub()`
Replaces matching text.

```python
import re

text = "My phone is 123-456-7890"
new_text = re.sub(r"\D", "", text)
print(new_text)
```

This removes non-digit characters.

---

## 5. Example: Validating Email

```python
import re

email = "student@example.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")
```

This checks:

- letters/numbers before `@`
- domain name after `@`
- dot and domain extension at the end

---

## 6. Example: Phone Number Validation

```python
import re

phone = "+1-555-123-4567"
pattern = r"^\+?\d{1,3}-?\d{3}-?\d{3}-?\d{4}$"

if re.match(pattern, phone):
    print("Valid phone number")
else:
    print("Invalid phone number")
```

---

## 7. Example: Extracting Data from Text

```python
import re

text = "Order ID: 1001, Customer: John, Amount: $45.60"
ids = re.findall(r"Order ID: (\d+)", text)
print(ids)
```

This pattern extracts only the order ID.

---

## 8. Raw Strings in Regex

In Python, regex patterns are usually written as raw strings:

```python
pattern = r"\d+"
```

This avoids escaping issues with backslashes.

Without `r`, you would need to write:

```python
pattern = "\\d+"
```

Raw strings are easier to read and safer for regex.

---

## 9. Common Use Cases in Real Life

Regular expressions are often used in:

- form validation
- searching for user IDs or codes
- parsing log files
- cleaning data
- checking password rules
- extracting names and dates from text

---

## 10. Important Notes

- Regex is powerful, but it can become hard to read if patterns are too complex.
- Always test small patterns before using them in a large project.
- Use simple patterns first and keep them readable.
- For very complex parsing, sometimes a combination of regex + logic is better.

---

## 11. Key Points

- Regex helps match text patterns.
- The `re` module provides search and validation tools.
- `search()`, `match()`, `findall()`, and `sub()` are the most common functions.
- Patterns use special symbols like `\d`, `\w`, `*`, `+`, and `[]`.
- Regex is very useful for validation and data extraction.

---

## Assignment Questions

### Assignment 1: Email Validator
Write a Python script that checks whether a user-entered email is valid using regex.

Questions:
- What part of the email pattern ensures there is a `@` symbol?
- Why is the `^` and `$` important in the pattern?

### Assignment 2: Number Finder
Write a program that extracts all numbers from a sentence.

Example:

```python
text = "I have 3 apples, 12 oranges, and 9 bananas."
```

Questions:
- Which regex pattern would extract only numeric values?
- Why is `findall()` useful here?

### Assignment 3: Password Checker
Create a regex pattern that checks whether a password:

- has at least 8 characters
- contains at least one uppercase letter
- contains at least one digit

Questions:
- Why is `+` useful in password validation?
- How would you make the rule stricter?

### Assignment 4: Remove Extra Spaces
Write a regex-based solution that removes extra spaces from a paragraph and replaces them with single spaces.

Questions:
- Which function is better for this: `search()` or `sub()`?
- Why is replacing repeated whitespace easier with regex?

### Assignment 5: Find Words Starting with a Letter
Write a program that finds all words beginning with a capital letter in a text.

Questions:
- How can `[]` help define a letter range?
- What is the difference between `match()` and `search()` in this case?

---

## Quick Practice Tasks

1. Write a regex to match a date in the form `DD/MM/YYYY`.
2. Validate a username that contains only letters and numbers.
3. Extract all hashtags from a sentence like `#python #coding #learning`.
4. Replace all repeated spaces in a sentence with one space.
5. Find all words in a string using `findall()`.

---

## Mini Challenge

Create a small program that:

- asks the user for a phone number
- validates it using regex
- prints either `Valid` or `Invalid`

Bonus: add email validation in the same program.

---

## Summary

Regex is a compact and powerful way to work with patterns in text. In Python, the `re` module gives you tools to match, validate, replace, and extract data. Practice with small examples first, and you will quickly see how useful it becomes.
