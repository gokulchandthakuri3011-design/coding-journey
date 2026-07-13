# 📅 Day 9: Lists (Part 2) — Operations & Methods

Welcome to Day 9! Yesterday you learned how to **create** lists, **index** into them, and **slice** them. Today we go deeper — you will learn how to actively **modify**, **search**, **sort**, and use the powerful **list comprehension** syntax.

By the end of today, you will be able to write dynamic, real-world programs that manipulate collections of data efficiently.

---

## 📝 Concept Notes

---

### 1. Modifying Lists — Add & Remove Items

Lists in Python are **mutable**, which means you can change their content after creation.

#### ➕ Adding Items

| Method | Description | Example |
| :--- | :--- | :--- |
| `.append(item)` | Adds a single item to the **end** of the list. | `fruits.append("mango")` |
| `.insert(index, item)` | Inserts an item at a **specific position**. | `fruits.insert(1, "kiwi")` |
| `.extend(iterable)` | Appends **all items** from another list (or any iterable) to the end. | `fruits.extend(["grape", "lime"])` |

```python
fruits = ["apple", "banana", "cherry"]

fruits.append("mango")
print(fruits)  # ['apple', 'banana', 'cherry', 'mango']

fruits.insert(1, "kiwi")
print(fruits)  # ['apple', 'kiwi', 'banana', 'cherry', 'mango']

fruits.extend(["grape", "lime"])
print(fruits)  # ['apple', 'kiwi', 'banana', 'cherry', 'mango', 'grape', 'lime']
```

> **Note:** `.append()` vs `.extend()` — `append(["a", "b"])` adds the whole list as **one item** (creating a nested list), while `extend(["a", "b"])` adds each item **individually**.

---

#### ➖ Removing Items

| Method | Description | Example |
| :--- | :--- | :--- |
| `.remove(item)` | Removes the **first occurrence** of the specified item. Raises `ValueError` if not found. | `fruits.remove("banana")` |
| `.pop(index)` | Removes and **returns** the item at the given index. Defaults to the **last item** if no index is given. | `fruits.pop(0)` |
| `.clear()` | Removes **all items** from the list, leaving an empty list `[]`. | `fruits.clear()` |

```python
scores = [10, 25, 30, 25, 50]

scores.remove(25)   # Removes the FIRST 25
print(scores)       # [10, 30, 25, 50]

popped = scores.pop()  # Removes and returns the last item
print(popped)          # 50
print(scores)          # [10, 30, 25]

scores.clear()
print(scores)          # []
```

---

### 2. Finding Items — Searching a List

| Method / Operator | Description | Example |
| :--- | :--- | :--- |
| `item in list` | Returns `True` if item exists in the list. | `"apple" in fruits` |
| `.index(item)` | Returns the **index** of the first occurrence. Raises `ValueError` if not found. | `fruits.index("apple")` |
| `.count(item)` | Returns how many times an item **appears** in the list. | `scores.count(25)` |

```python
animals = ["cat", "dog", "bird", "dog", "fish"]

print("dog" in animals)       # True
print("tiger" in animals)     # False

print(animals.index("bird"))  # 2
print(animals.count("dog"))   # 2
```

---

### 3. Sorting & Reversing Lists

#### `.sort()` — Sorts the list **in place** (modifies the original list)
```python
numbers = [5, 2, 9, 1, 7]

numbers.sort()                   # Ascending order (default)
print(numbers)                   # [1, 2, 5, 7, 9]

numbers.sort(reverse=True)       # Descending order
print(numbers)                   # [9, 7, 5, 2, 1]

words = ["banana", "apple", "cherry"]
words.sort()                     # Alphabetical order
print(words)                     # ['apple', 'banana', 'cherry']
```

#### `sorted()` — Returns a **new sorted list** (does NOT modify the original)
```python
original = [5, 2, 9, 1, 7]
sorted_list = sorted(original)

print(original)     # [5, 2, 9, 1, 7]  ← unchanged
print(sorted_list)  # [1, 2, 5, 7, 9]  ← new list
```

> **Key Difference:** Use `.sort()` when you want to permanently reorder the list. Use `sorted()` when you need a sorted copy and want to keep the original intact.

#### `.reverse()` — Reverses the list **in place**
```python
items = [1, 2, 3, 4, 5]
items.reverse()
print(items)  # [5, 4, 3, 2, 1]
```

---

### 4. Copying Lists — Shallow Copy

**Do NOT copy a list with `=`!** This does not create a new list — both variables point to the **same** list in memory.

```python
# ❌ WRONG — This creates an alias, not a copy!
original = [1, 2, 3]
alias = original
alias.append(99)
print(original)  # [1, 2, 3, 99] — original is changed too!

# ✅ CORRECT — Use .copy() to create an independent copy
original = [1, 2, 3]
copy = original.copy()
copy.append(99)
print(original)  # [1, 2, 3]      — original is safe
print(copy)      # [1, 2, 3, 99]  — only copy is changed
```

You can also use `list(original)` or the slice `original[:]` to create a copy:

```python
copy2 = list(original)
copy3 = original[:]
```

---

### 5. List Comprehensions — Pythonic & Powerful ⚡

A **list comprehension** is a concise, single-line way to create a new list by applying an expression to each item in an existing iterable, optionally filtering items with a condition.

**Syntax:**
```
new_list = [expression for item in iterable if condition]
```

The `if condition` part is **optional**.

#### Basic Example — Squaring Numbers
```python
# Traditional loop approach
squares = []
for x in range(1, 6):
    squares.append(x ** 2)
print(squares)  # [1, 4, 9, 16, 25]

# ✨ List comprehension — one clean line!
squares = [x ** 2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]
```

#### With a Condition — Filtering Items
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get only even numbers
evens = [n for n in numbers if n % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]
```

#### Transforming Strings
```python
names = ["alice", "bob", "charlie", "david"]

# Capitalize each name
capitalized = [name.capitalize() for name in names]
print(capitalized)  # ['Alice', 'Bob', 'Charlie', 'David']
```

---

### 6. Useful Built-in Functions for Lists

| Function | Description | Example |
| :--- | :--- | :--- |
| `len(list)` | Returns the total number of items. | `len([1, 2, 3])` → `3` |
| `sum(list)` | Returns the sum of all numeric items. | `sum([1, 2, 3])` → `6` |
| `max(list)` | Returns the largest item. | `max([1, 5, 3])` → `5` |
| `min(list)` | Returns the smallest item. | `min([1, 5, 3])` → `1` |

```python
grades = [88, 92, 75, 96, 70]

print(f"Total students: {len(grades)}")   # 5
print(f"Highest grade: {max(grades)}")    # 96
print(f"Lowest grade: {min(grades)}")     # 70
print(f"Total points: {sum(grades)}")     # 421
print(f"Average grade: {sum(grades) / len(grades):.1f}")  # 84.2
```

---

## 💻 Practice Assignments

Work through these assignments in order. Create a new file for each one using the `Day9_TaskY.py` naming convention.

---

### Assignment 1: The Dynamic Task List
*Practice adding and removing items from a list.*

1. Create an empty list called `task_list`.
2. Use `.append()` to add the following tasks:
   - `"Buy groceries"`
   - `"Do laundry"`
   - `"Study Python"`
   - `"Go for a walk"`
3. Print the current task list.
4. Use `.insert()` to add `"Call the dentist"` at index `1`.
5. Print the list again and check the new order.
6. You have completed the laundry. Use `.remove()` to delete `"Do laundry"`.
7. The last task is done for the day. Use `.pop()` to remove it and print what was removed.
8. Print the final task list.
- **File:** `Day9_Task1.py`

---

### Assignment 2: Grade Organizer
*Practice sorting, counting, and searching.*

1. Create a list called `grades` with the following values: `[72, 95, 88, 60, 95, 78, 55, 95, 81, 68]`
2. Print the number of items in the list using `len()`.
3. Print the highest and lowest grade using `max()` and `min()`.
4. Print the average grade.
5. Sort the grades in **ascending** order and print the sorted list.
6. Count how many times the grade `95` appears in the list and print it.
7. Check if the grade `100` is in the list and print the boolean result.
- **File:** `Day9_Task2.py`

---

### Assignment 3: List Comprehension Magic
*Practice writing list comprehensions.*

1. Create a list of numbers from `1` to `20` using `range()`.
2. Use a list comprehension to create a new list containing only the **odd** numbers.
3. Use a list comprehension to create a list of the **squares** of numbers from `1` to `10`.
4. Given this list of words: `words = ["python", "is", "awesome", "and", "fun"]`, use a list comprehension to create a new list containing only the words that have **more than 3 letters**.
5. Print all three new lists.
- **File:** `Day9_Task3.py`

---

### Assignment 4: Shopping Cart System
*Combine multiple list skills in a real-world scenario.*

Build a simple shopping cart program:

1. Create an empty list called `cart`.
2. Create a list of available items with their prices as tuples: 
   ```python
   shop = [("Apple", 0.99), ("Milk", 1.49), ("Bread", 2.50), ("Eggs", 3.99), ("Butter", 4.50)]
   ```
3. Display the available items to the user (numbered list).
4. Ask the user to enter item names to add to the cart (one at a time).
5. Keep a loop running until the user types `"done"`.
6. If the item is found in `shop`, add its name to `cart` and confirm.
7. If the item is not found, print `"Item not available."`.
8. When done, print the final `cart` list and the total number of items in it.
- **File:** `Day9_Task4.py`

---

## 🚀 Challenge: Top 3 Scores

*This challenge combines searching, sorting, and slicing.*

1. Create a list of 10 player scores (you can make them up).
2. Use `.sort()` to sort them in **descending** order (highest first).
3. Slice the sorted list to get the **Top 3** scores.
4. Use a list comprehension to create a new list where each score from the **original** unsorted list is **doubled**.
5. Print the Top 3 scores and the doubled scores list.
- **File:** `Day9_Challenge.py`

---

### 💡 Daily Routine Checklist (Day 9):
- [ ] Read all concept notes carefully (especially the `.sort()` vs `sorted()` difference and the list copy trap).
- [ ] Complete Assignment 1: The Dynamic Task List.
- [ ] Complete Assignment 2: Grade Organizer.
- [ ] Complete Assignment 3: List Comprehension Magic.
- [ ] Complete Assignment 4: Shopping Cart System.
- [ ] Attempt the Challenge: Top 3 Scores.

Happy Coding! 🐍
