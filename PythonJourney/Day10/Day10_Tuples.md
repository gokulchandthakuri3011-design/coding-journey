# Day 10: Tuples

Welcome to Day 10! So far you've mastered **lists** — ordered, changeable collections. Today we look at **tuples**, which are like lists' disciplined cousin: ordered and **immutable** (unchangeable after creation).

---

## Concept Notes

---

### 1. What is a Tuple?

A tuple is an ordered, **immutable** collection of items. Once created, you cannot add, remove, or replace items.

Tuples are created by placing comma-separated values inside parentheses `()`.

```python
# Creating a tuple
coordinates = (10, 20)
colors = ("red", "green", "blue")

# Parentheses are optional — commas make the tuple!
point = 4, 5
print(type(point))  # <class 'tuple'>

# A single-element tuple needs a trailing comma
single = (42,)
print(type(single))  # <class 'tuple'>

# Without the comma, it's just a number in parentheses
not_a_tuple = (42)
print(type(not_a_tuple))  # <class 'int'>
```

---

### 2. Accessing Items

Tuple indexing and slicing work **exactly** like lists.

```python
fruits = ("apple", "banana", "cherry", "date")

print(fruits[0])    # apple
print(fruits[-1])   # date
print(fruits[1:3])  # ('banana', 'cherry')
```

---

### 3. Immutability in Action

Tuples cannot be changed after creation. Trying to do so raises a `TypeError`.

```python
coordinates = (10, 20)
# This will cause an error:
coordinates[0] = 15
# TypeError: 'tuple' object does not support item assignment
```

But if a tuple contains a **mutable** object (like a list), that object itself can be changed.

```python
nested = (1, 2, [3, 4])
nested[2].append(5)
print(nested)  # (1, 2, [3, 4, 5])  — the list inside changed!
```

---

### 4. Tuple Methods

Tuples only have two built-in methods since they cannot be modified:

| Method | Description | Example |
| :--- | :--- | :--- |
| `.count(item)` | Returns how many times an item appears. | `t.count(3)` |
| `.index(item)` | Returns the index of the first occurrence. | `t.index(3)` |

```python
scores = (88, 92, 75, 92, 70)

print(scores.count(92))   # 2
print(scores.index(75))   # 2
```

You can also use `len()`, `max()`, `min()`, and `sum()` on tuples, just like lists.

```python
print(len(scores))    # 5
print(max(scores))    # 92
print(min(scores))    # 70
print(sum(scores))    # 417
```

---

### 5. Tuple Unpacking

Tuple unpacking lets you assign each element of a tuple to a separate variable in one line.

```python
point = (3, 7)
x, y = point
print(x)  # 3
print(y)  # 7
```

This is especially useful for swapping values:

```python
a = 10
b = 20
a, b = b, a  # Swap! Python unpacks (20, 10) automatically
print(a)     # 20
print(b)     # 10
```

You can unpack when looping through a list of tuples too:

```python
locations = [(40.7128, -74.0060), (51.5074, -0.1278), (35.6762, 139.6503)]
for lat, lon in locations:
    print(f"Latitude: {lat}, Longitude: {lon}")
```

---

### 6. When to Use Tuples vs Lists

| Scenario | Use Tuple | Use List |
| :--- | :---: | :---: |
| Data should never change (e.g., days of week) | ✅ | ❌ |
| You need to add/remove items | ❌ | ✅ |
| Dictionary keys or set items | ✅ | ❌ |
| Returning multiple values from a function | ✅ | ❌ |
| Homogeneous data (all same type, e.g., all ints) | Depends | ✅ |
| Heterogeneous data (mixed types, e.g., `(name, age, height)`) | ✅ | ✅ |
| Performance/memory critical code (tuples are slightly lighter) | ✅ | ❌ |

**Rule of thumb:** Use a tuple when the data is a **fixed collection** that logically belongs together and shouldn't change. Use a list when the collection needs to **grow, shrink, or reorder**.

---

### 7. Named Tuples

Regular tuples use numeric indices — `coord[0]`, `coord[1]` — which can be hard to read. `namedtuple` from the `collections` module lets you name each position.

```python
from collections import namedtuple

# Define a named tuple type
Point = namedtuple("Point", ["x", "y"])  # Creates a new tuple type called Point with fields x & y

# Create instances
p = Point(10, 20)   # Creates an instances - butit is still tuple
print(p.x)          # 10  — access by name!
print(p.y)          # 20
print(p[0])         # 10  — still works by index too
print(p)            # Point(x=10, y=20)

# Unpacking still works
x, y = p
```

Named tuples are great for data that benefits from **self-documenting field names** (like coordinates, database rows, or configuration values).

```python
Person = namedtuple("Person", ["name", "age", "city"])
alice = Person("Alice", 30, "New York")
print(f"{alice.name} is {alice.age} years old from {alice.city}")
```

---

### 8. Returning Multiple Values from a Function

Python functions can return multiple values by returning a tuple — and the caller can unpack it immediately.

```python
def get_min_max(numbers):
    return min(numbers), max(numbers)

low, high = get_min_max([10, 3, 8, 15, 2])
print(f"Lowest: {low}, Highest: {high}")
```

This is a very common and elegant pattern in Python.

---

## Practice Assignments

Create a new Python file for each assignment.

---

### Assignment 1: GPS Coordinate Tracker

*Practice creating, accessing, and unpacking tuples.*

1. Create a tuple `coord1` with latitude `40.7128` and longitude `-74.0060` (New York).
2. Create a second tuple `coord2` with latitude `34.0522` and longitude `-118.2437` (Los Angeles).
3. Print the latitude of `coord1` and the longitude of `coord2` using index access.
4. Unpack `coord1` into variables `lat` and `lon` and print a formatted string.
5. Create a list called `trip` containing both coordinate tuples.
6. Loop through `trip`, unpack each tuple, and print `"Location: lat, lon"`.
- **File:** `Day10_Task1.py`

---

### Assignment 2: The Immutable Menu

*Practice tuple creation and errors.*

1. Create a tuple `menu` with the following breakfast items: `"pancakes"`, `"waffles"`, `"omelette"`, `"cereal"`, `"fruit bowl"`.
2. Print the menu.
3. Print the first and last item using positive and negative indexing.
4. Print the number of items on the menu using `len()`.
5. Check if `"coffee"` is on the menu and print the result.
6. Try to change the second item to `"french toast"` using assignment. Wrap it in a `try/except` block so the program doesn't crash.
7. Print `"Tuples are immutable!"` in the `except` block.
- **File:** `Day10_Task2.py`

---

### Assignment 3: Student Grade Tracker

*Practice named tuples and returning multiple values.*

1. Define a named tuple `Student` with fields `name`, `subject`, and `grade`.
2. Create at least 4 student instances with different data.
3. Store them in a list called `students`.
4. Loop through the list and print each student's info in a formatted sentence.
5. Write a function `get_grade_stats(grades)` that accepts a list of numeric grades and returns a tuple of `(average, highest, lowest)`.
6. Test the function with the grades from your students. Unpack and print the results.
- **File:** `Day10_Task3.py`

---

### Assignment 4: Inventory Tracker

*Practice tuples + lists working together.*

You manage a small warehouse. Each item is stored as a tuple: `(item_id, name, quantity, price)`.

1. Create an inventory list with at least 5 items (e.g., `(101, "Widget", 50, 0.99)`).
2. Write a function `total_value(inventory)` that loops through the inventory and returns the total value (sum of quantity * price for each item).
3. Write a function `find_item(inventory, item_id)` that searches by ID and returns the item tuple, or `None` if not found.
4. Write a function `restock(inventory, item_id, amount)` that returns a **new list** with the quantity of the given item updated (remember — tuples are immutable, so you need to create a new tuple).
5. Test all three functions and print the results.
- **File:** `Day10_Task4.py`

---

## Challenge: Zip It, Unpack It

*Combine tuples, `zip()`, and unpacking.*

1. Create two lists:
   ```python
   students = ["Alice", "Bob", "Charlie", "Diana"]
   scores = [88, 92, 79, 95]
   ```
2. Use `zip()` to pair them into a list of tuples.
3. Print the zipped list.
4. Sort the list of tuples by score (descending). *Hint: use `sorted()` with a `key` function, or a lambda.*
5. Unpack the top scorer into `top_student, top_score` and print the winner.
- **File:** `Day10_Challenge.py`

---

### Daily Routine Checklist (Day 10):

- [ ] Read all concept notes (especially immutability and tuple unpacking).
- [ ] Complete Assignment 1: GPS Coordinate Tracker.
- [ ] Complete Assignment 2: The Immutable Menu.
- [ ] Complete Assignment 3: Student Grade Tracker.
- [ ] Complete Assignment 4: Inventory Tracker.
- [ ] Attempt the Challenge: Zip It, Unpack It.
