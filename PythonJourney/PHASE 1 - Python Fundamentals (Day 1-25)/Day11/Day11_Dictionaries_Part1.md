# Day 11: Dictionaries (Part 1) — Key-Value Pairs

Welcome to Day 11! Today we are exploring **dictionaries**, one of the most powerful, flexible, and widely used data structures in Python. 

So far, you have learned about lists and tuples, which store ordered collections of items accessed by their numeric position (indices like `0`, `1`, `2`, etc.). A **Dictionary**, on the other hand, stores data in **key-value pairs**. Instead of using a number to find a value, you use a custom **key** (like a word in a real dictionary or a name in a phone book).

---

## 📝 Concept Notes

---

### 1. What is a Dictionary?

A dictionary is an collection of items stored as `key: value` pairs. 
- **Keys** must be **unique** and of an **immutable** (unchangeable/hashable) data type, such as strings, integers, floats, or tuples. 
- **Values** can be of **any** data type (strings, integers, lists, tuples, or even other dictionaries) and can be duplicated.

Dictionaries are created using curly braces `{}` with keys and values separated by a colon `:`.

```python
# Creating an empty dictionary
empty_dict = {}

# A dictionary representing a user profile
user = {
    "username": "coder_dan",
    "email": "dan@example.com",
    "age": 24,
    "is_active": True
}
print(user)
print(type(user))  # <class 'dict'>
```

> [!NOTE]
> Starting in Python 3.7+, dictionaries maintain the **insertion order** of their keys. This means when you loop through or print a dictionary, the items will appear in the order you added them.

---

### 2. Accessing Values: Brackets vs `.get()`

There are two primary ways to access the value associated with a key:

#### A. Using Square Brackets `dict[key]`
This is the standard and most direct way to retrieve a value.

```python
student = {"name": "Sophia", "grade": "A", "age": 18}

print(student["name"])   # Output: Sophia
print(student["grade"])  # Output: A
```
⚠️ **Warning:** If you try to access a key that does **not** exist using square brackets, Python will raise a `KeyError` and crash the program.

```python
# This raises a KeyError:
print(student["height"]) 
# KeyError: 'height'
```

#### B. Using the `.get(key, default)` Method
To avoid crashes when a key might be missing, use the `.get()` method. 
- If the key exists, it returns the value.
- If the key does not exist, it returns `None` (instead of crashing).
- You can also provide a custom **default value** to return if the key is missing.

```python
student = {"name": "Sophia", "grade": "A", "age": 18}

# Key exists
print(student.get("name"))       # Output: Sophia

# Key does not exist (returns None by default)
print(student.get("height"))     # Output: None

# Key does not exist (returns custom default)
print(student.get("height", "Not Specified"))  # Output: Not Specified
```

---

### 3. Modifying & Adding Key-Value Pairs

Dictionaries are **mutable**, meaning you can add, change, or remove items after creation.

#### Adding and Updating
Both adding a new key and updating an existing one use the same assignment syntax: `dict[key] = value`.
- If the key is already in the dictionary, its value is **updated**.
- If the key is not in the dictionary, a new key-value pair is **created**.

```python
inventory = {"apples": 10, "bananas": 5}

# Update an existing key
inventory["apples"] = 12 

# Add a new key-value pair
inventory["oranges"] = 8

print(inventory)  # Output: {'apples': 12, 'bananas': 5, 'oranges': 8}
```

#### Deleting Key-Value Pairs
You can remove items from a dictionary using:
1. **`del dict[key]`**: Permanently deletes the key-value pair. Throws `KeyError` if the key doesn't exist.
2. **`dict.pop(key)`**: Removes the key and returns its value. Throws `KeyError` if the key doesn't exist, unless a default value is provided: `dict.pop(key, default)`.

```python
inventory = {"apples": 12, "bananas": 5, "oranges": 8}

# Remove using del
del inventory["bananas"]

# Remove and capture the value using pop()
removed_apples = inventory.pop("apples")

print(inventory)       # Output: {'oranges': 8}
print(removed_apples)  # Output: 12
```

---

### 4. Essential Dictionary Methods

Python provides three essential methods to retrieve "views" of a dictionary's keys, values, or items.

| Method | Description | Example Output |
| :--- | :--- | :--- |
| `.keys()` | Returns a view object containing all the keys. | `dict_keys(['apples', 'oranges'])` |
| `.values()` | Returns a view object containing all the values. | `dict_values([12, 8])` |
| `.items()` | Returns a view of tuple pairs `(key, value)`. | `dict_items([('apples', 12), ('oranges', 8)])` |

These view objects automatically update when the dictionary changes and are perfect for looping!

```python
car = {"brand": "Tesla", "model": "Model 3", "year": 2023}

# 1. Loop through keys
print("Keys:")
for key in car.keys():
    print(key)

# 2. Loop through values
print("\nValues:")
for value in car.values():
    print(value)

# 3. Loop through items (Unpacking key-value tuples)
print("\nItems:")
for key, value in car.items():
    print(f"{key}: {value}")
```

---

## 💻 Practice Assignments

Create a new Python file under the `C:\PythonJourney` directory for each assignment.

---

### Assignment 1: Phone Book Database

*Practice dictionary creation, updating, and safe value retrieval.*

1. Create a dictionary called `phone_book` containing the names and phone numbers of 3 friends. (Example: `"Alice": "555-0199"`).
2. Print the entire phone book.
3. Add a new contact to the phone book: `"David"` with the number `"555-0244"`.
4. Update the phone number of the first contact you created to a new number.
5. Ask the user to input a name to search for.
6. Use the `.get()` method to search the phone book.
   - If the contact exists, print `"Phone number: <number>"`.
   - If the contact does not exist, print `"Contact not found in phone book."`.
- **File:** `Day11_Task1.py`

---

### Assignment 2: Inventory Management Tracker

*Practice modifying dictionaries and looping through elements.*

You are managing stock levels for a small grocery store.
1. Create a dictionary `grocery_stock` with the following items and quantities:
   - `"bread"`: 15
   - `"milk"`: 8
   - `"eggs"`: 30
   - `"butter"`: 5
2. The store receives a restock! Update the quantity of `"milk"` by adding `10` more, and `"butter"` by adding `5` more.
3. The store has run out of `"bread"`. Delete the `"bread"` key-value pair from the dictionary.
4. Add a new item `"cheese"` with a quantity of `12`.
5. Print a clean, formatted report of the final inventory using a loop and `.items()`.
   *(Example Output)*:
   ```text
   --- Final Grocery Stock ---
   milk: 18 in stock
   eggs: 30 in stock
   butter: 10 in stock
   cheese: 12 in stock
   ---------------------------
   ```
- **File:** `Day11_Task2.py`

---

### Assignment 3: Student Profile Manager

*Practice nested dictionaries and accessing deeper values.*

1. Create a dictionary representing a `student_profile` containing:
   - `"name"`: "Liam"
   - `"age"`: 17
   - `"courses"`: A list containing `"Math"`, `"Science"`, `"History"`
   - `"grades"`: A dictionary containing `"Math": 90`, `"Science": 85`, `"History": 88`
2. Print the student's name and age.
3. Access and print the second course in the `"courses"` list (`"Science"`).
4. Access and print the student's grade in `"Math"`.
5. Calculate and print the average grade of the student using the grades in the `"grades"` sub-dictionary. *(Hint: Use `sum()` and `len()` on `grades.values()`)*.
- **File:** `Day11_Task3.py`

---

## ⚡ Challenge: Word Frequency Counter

*Practice implementing real-world text processing using a dictionary.*

1. Prompt the user to enter a sentence:
   *(Example: "python is fun and learning python is easy")*
2. Clean and process the sentence: convert it to lowercase and split it into a list of words using `.split()`.
3. Create an empty dictionary called `word_counts`.
4. Loop through the list of words:
   - If the word is already a key in `word_counts`, increment its value by `1`.
   - If the word is not in `word_counts`, add it with a value of `1`.
5. Print the final counts of each word in a clean format.
- **File:** `Day11_Challenge.py`

---

### 📋 Daily Routine Checklist (Day 11):

- [x] Read all concept notes on dictionary basics, keys, values, and methods.
- [x] Complete Assignment 1: Phone Book Database.
- [x] Complete Assignment 2: Inventory Management Tracker.
- [x] Complete Assignment 3: Student Profile Manager.
- [x] Attempt the Challenge: Word Frequency Counter.
