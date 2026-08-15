# 📅 Day 12: Dictionaries (Part 2) & Sets

Welcome to Day 12! Yesterday, you mastered the basics of Python dictionaries, including key-value pairs, basic access, and essential methods. Today, we are taking your data structure skills to the next level. 

We will cover:
1. **Advanced Dictionary Operations:** Iterating dynamically and using dictionary comprehensions.
2. **The `collections` Module:** Powering up your code with `defaultdict` and `Counter`.
3. **Sets:** Understanding unordered collections of unique items and performing powerful mathematical set operations (union, intersection, and difference).

By the end of today, you will have a comprehensive toolkit for handling complex, unstructured, and unique datasets efficiently.

---

## 📝 Concept Notes

---

### 1. Iterating through Dictionaries (Deep Dive)

As you saw in Day 11, you can loop through keys, values, or key-value pairs. Let's look at best practices and a classic pitfall.

#### A. Standard Iteration
```python
user_scores = {"Alice": 85, "Bob": 92, "Charlie": 78}

# Iterating over keys (default behavior if no method is called)
for name in user_scores:
    print(name)  # Prints: Alice, Bob, Charlie

# Iterating over key-value pairs using .items() (Most Common & Pythonic)
for name, score in user_scores.items():
    print(f"{name} scored {score} points.")
```

#### ⚠️ The Iteration Mutation Trap
A very common source of bugs in Python is attempting to **add or remove elements** from a dictionary while iterating directly over it.

```python
# ❌ THIS WILL RAISE AN ERROR: RuntimeError: dictionary changed size during iteration
scores = {"Alice": 45, "Bob": 92, "Charlie": 38}

for name, score in scores.items():
    if score < 50:
        del scores[name]  # Throws RuntimeError!
```

#### ✅ How to Avoid the Trap
If you need to modify the dictionary keys during iteration, iterate over a **copy** of the keys or dictionary items (e.g., using `list()`), or use a dictionary comprehension to build a new one.

```python
scores = {"Alice": 45, "Bob": 92, "Charlie": 38}

# Iterate over a list of keys instead of the active view
for name in list(scores.keys()):
    if scores[name] < 50:
        del scores[name]

print(scores)  # Output: {'Bob': 92} — Safe and successful!
```

---

### 2. Dictionary Comprehensions ⚡

Just like list comprehensions, **dictionary comprehensions** allow you to create new dictionaries from an iterable in a single, concise, and optimized line of code.

#### Syntax:
```python
new_dict = {key_expression: value_expression for item in iterable if condition}
```

#### A. Simple Transformation (e.g., Squaring Numbers)
```python
# Traditional loop
squares = {}
for x in range(1, 6):
    squares[x] = x ** 2

# ✨ Dictionary Comprehension
squares = {x: x ** 2 for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

#### B. Filtering Dictionary Elements
Suppose you want to extract only the passing scores (50 or above) from a dictionary.
```python
all_scores = {"Alice": 45, "Bob": 92, "Charlie": 78, "David": 49}

passing_scores = {name: score for name, score in all_scores.items() if score >= 50}
print(passing_scores)  # Output: {'Bob': 92, 'Charlie': 78}
```

#### C. Swapping Keys and Values (Dictionary Inversion)
Sometimes you need to reverse a dictionary so that the values become keys and keys become values.
```python
original = {"A": 1, "B": 2, "C": 3}

inverted = {value: key for key, value in original.items()}
print(inverted)  # Output: {1: 'A', 2: 'B', 3: 'C'}
```

---

### 3. The `collections` Module: `defaultdict` & `Counter` 🛠️

Python's built-in `collections` module provides specialized container datatypes that offer alternatives to standard built-in containers.

#### A. `defaultdict`
A standard dictionary throws a `KeyError` if you search for a key that does not exist. A `defaultdict` overcomes this by automatically initializing a **default value** when a non-existent key is accessed.

You must pass a **callable factory** (like `int`, `list`, `float`, or a custom function) to define what the default value should be.

```python
from collections import defaultdict

# 1. Default to Integer (0)
# Perfect for counters!
student_groups = defaultdict(int)
student_groups["Math"] += 1  # No KeyError! Automatically starts Math at 0, then adds 1.
print(student_groups["Math"])  # Output: 1
print(student_groups["Science"])  # Output: 0 (accessed, so it initialized to default)

# 2. Default to List ([])
# Perfect for grouping elements!
subjects_by_student = defaultdict(list)
subjects_by_student["Liam"].append("Physics")
subjects_by_student["Liam"].append("Calculus")
print(subjects_by_student["Liam"])  # Output: ['Physics', 'Calculus']
```

#### B. `Counter`
`Counter` is a subclass of `dict` designed specifically for counting hashable objects. It is extremely fast and convenient.

```python
from collections import Counter

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

# Count occurrences of elements automatically
word_counts = Counter(words)
print(word_counts)  # Output: Counter({'apple': 3, 'banana': 2, 'cherry': 1})

# Access count of a specific item (returns 0 if not found, no KeyError)
print(word_counts["banana"])  # Output: 2
print(word_counts["orange"])  # Output: 0

# Get the most common items (returns a list of key-value tuples)
top_two = word_counts.most_common(2)
print(top_two)  # Output: [('apple', 3), ('banana', 2)]
```

---

### 4. What is a Set? 🔴

A **set** is an unordered collection of **unique** elements. 

Key properties of sets:
- **No Duplicates:** If you add a duplicate item to a set, it is silently ignored.
- **Unordered:** Sets do not keep track of insertion order, so you cannot index or slice them (e.g., `my_set[0]` will raise a `TypeError`).
- **Fast Lookups:** Sets use hashing internally, making membership tests (`item in my_set`) extremely fast ($O(1)$ constant time complexity) compared to lists ($O(n)$ linear time).
- **Mutable Set, Immutable Elements:** You can add/remove elements from a set, but the elements inside the set must be **immutable** (e.g., strings, numbers, tuples). You cannot put a list or a dictionary inside a set.
#### Creating Sets
```python
# Creating a set with curly braces
fruits = {"apple", "banana", "cherry", "apple"}  # Note the duplicate "apple"
print(fruits)  # Output: {'banana', 'cherry', 'apple'} (order may vary, duplicates removed)

# ⚠️ WARNING: Creating an empty set
# {} creates an empty DICTIONARY. You MUST use set() to create an empty set!
empty_dict = {}
print(type(empty_dict))  # <class 'dict'>

empty_set = set()
print(type(empty_set))   # <class 'set'>
```

#### Modifying Sets
| Method | Description |
| :--- | :--- |
| `.add(item)` | Adds a single item to the set. |
| `.remove(item)` | Removes the item. Raises `KeyError` if the item is not found. |
| `.discard(item)` | Safely removes the item. Does **not** raise an error if not found. |
| `.pop()` | Removes and returns an arbitrary element (since it is unordered). An **arbitrary element** means you cannot predict or control which element will be removed—it could be any element from the set. |
| `.clear()` | Removes all elements, leaving the set empty. |

```python
names = {"Alice", "Bob"}
names.add("Charlie")
names.add("Alice")  # Duplicate, ignored

names.remove("Bob")
names.discard("David")  # Safely does nothing since "David" isn't in the set

print(names)  # Output: {'Alice', 'Charlie'}
```

---

### 5. Set Operations (Venn Diagram Magic) 🎡

Sets are exceptionally powerful because of their mathematical operations, which are perfect for finding commonalities or differences between datasets.

Let's assume we have two sets:
```python
math_students = {"Liam", "Sophia", "Noah", "Emma"}
science_students = {"Noah", "Emma", "Olivia", "Ava"}
```

#### A. Union (`union()` or `|`)
Combines elements from both sets, removing duplicates. Representing all unique students enrolled in either class.
```python
all_students = math_students.union(science_students)
# OR using the operator:
all_students = math_students | science_students

print(all_students)  
# Output: {'Liam', 'Sophia', 'Noah', 'Emma', 'Olivia', 'Ava'}
```

#### B. Intersection (`intersection()` or `&`)
Finds only the elements that exist in **both** sets. Representing students taking both classes.
```python
both_classes = math_students.intersection(science_students)
# OR using the operator:
both_classes = math_students & science_students

print(both_classes)  # Output: {'Noah', 'Emma'}
```

#### C. Difference (`difference()` or `-`)
Returns elements in the first set that are **not** in the second set. Representing students taking math but not science.
```python
math_only = math_students.difference(science_students)
# OR using the operator:
math_only = math_students - science_students

print(math_only)  # Output: {'Liam', 'Sophia'}
```

#### D. Symmetric Difference (`symmetric_difference()` or `^`)
Returns elements that are in **either** of the sets, but **not both**. Representing students taking exactly one of the classes.
```python
one_class_only = math_students.symmetric_difference(science_students)
# OR using the operator:
one_class_only = math_students ^ science_students

print(one_class_only)  # Output: {'Liam', 'Sophia', 'Olivia', 'Ava'}
```

---

## 💻 Practice Assignments

Create a new Python file under the `C:\PythonJourney` directory for each assignment.

---

### Assignment 1: Refined Word Frequency Counter
*Practice using `collections.Counter` to perform text analysis.*

1. Prompt the user or declare a paragraph of text:
   `text = "Python is an amazing programming language. Python is simple to learn and extremely readable. Learning Python opens up many doors in software engineering."`
2. Process the string:
   - Convert all words to lowercase.
   - Remove punctuation marks like periods `.`. (Hint: Use `text.replace(".", "")`).
   - Split the cleaned string into a list of words using `.split()`.
3. Create a `Counter` object from the word list to count frequencies.
4. Print the raw frequencies dictionary.
5. Print the **top 3 most common words** and their count using the `.most_common()` method in a clean format:
   ```text
   --- Top 3 Most Common Words ---
   1. word_a: count_a times
   2. word_b: count_b times
   3. word_c: count_c times
   ```
- **File:** `Day12_Task1.py`

---

### Assignment 2: Common Elements & Set Operations
*Practice converting lists to sets and applying set operations.*

You are given two lists representing subscriber emails for two different company newsletters:
```python
newsletter_a = ["dan@example.com", "alice@example.com", "emma@example.com", "bob@example.com", "charlie@example.com"]
newsletter_b = ["sophia@example.com", "bob@example.com", "liam@example.com", "emma@example.com", "olivia@example.com"]
```

Write a program that:
1. Converts both lists into sets.
2. Finds and prints the emails of subscribers who are subscribed to **both** newsletters. (Intersection)
3. Finds and prints the subscribers who are subscribed to **only** Newsletter A but not Newsletter B. (Difference)
4. Finds and prints the subscribers who are subscribed to **only one** of the newsletters, but not both. (Symmetric Difference)
5. Finds and prints the total number of unique subscribers across both newsletters. (Union)
- **File:** `Day12_Task2.py`

---

### Assignment 3: List Duplicate Remover
*Practice using sets to remove duplicates and analyze performance/ordering.*

1. Create a list with several duplicates: `numbers = [5, 2, 8, 2, 9, 5, 1, 8, 10, 2]`
2. **Method 1 (Unordered):**
   - Convert `numbers` to a set, then convert it back to a list.
   - Print the resulting list and observe its order compared to the original.
3. **Method 2 (Order-Preserving):**
   - Implement an order-preserving duplicate remover.
   - Create an empty set called `seen` and an empty list called `unique_numbers`.
   - Loop through the original `numbers` list. If a number is not in `seen`, add it to `seen` and append it to `unique_numbers`.
   - Print the final `unique_numbers` list and verify that the original order is preserved.
4. Add a print statement explaining why looking up elements in a set (`number not in seen`) is extremely efficient compared to looking up elements in a list.
- **File:** `Day12_Task3.py`


## ⚡ Challenge: Inventory Merger
*Combine advanced dictionaries and default values to merge datasets.*

You are managing inventory for two branches of a retail store. The branch inventory data is stored in two dictionaries:
```python
branch_1 = {"laptop": 5, "keyboard": 10, "mouse": 15, "monitor": 7}
branch_2 = {"keyboard": 8, "mouse": 12, "headset": 10, "printer": 4}
```

Write a program that merges these two inventories.
1. Use `collections.defaultdict` with standard integers, or use a standard dictionary with a smart loop (or the `.get()` method), to combine all stock levels.
2. If an item exists in both branches, their quantities should be **added together**.
3. If an item exists in only one branch, it should be added with its current quantity.
4. Print a clean report of the combined inventory sorted alphabetically by product name.
   ```text
   --- Combined Store In
   ```
- **File:** `Day12_Challenge.py`

---

### 📋 Daily Routine Checklist (Day 12):
- [xx] Read all concept notes on advanced dictionaries, `collections`, and sets.
- [x]Complete Assignment 1: Refined Word Frequency Counter.
- [x] Complete Assignment 2: Common Elements & Set Operations.
- [x] Complete Assignment 3: List Duplicate Remover.
- [x] Attempt the Challenge: Inventory Merger.

Keep going! Your Python data structure skills are now exceptionally strong! 🚀
