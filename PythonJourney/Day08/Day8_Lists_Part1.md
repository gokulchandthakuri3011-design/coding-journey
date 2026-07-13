# Day 8: Lists (Part 1) - Introduction, Indexing, and Slicing

Welcome to Week 2 of your Python Journey! This week we are diving into **Data Structures**. So far, you've learned how to store single pieces of data in variables (like one number or one string). Data structures allow you to store and manage *multiple* pieces of data together.

The most common and versatile data structure in Python is the **List**.

---

## 📝 Concept Notes

### 1. What is a List?
A list is an ordered, changeable collection of items. Think of it like a shopping list or a playlist.
Lists are created by placing comma-separated values inside square brackets `[]`.

```python
# Creating a list of strings
fruits = ["apple", "banana", "cherry"]

# Creating a list of numbers
scores = [95, 87, 92, 100]
```

### 2. Lists Can Hold Mixed Data Types
Unlike some other programming languages, Python lists don't care what type of data you put in them. You can mix strings, integers, floats, and booleans in a single list!

```python
mixed_list = ["Alice", 25, 5.5, True]
print(mixed_list)
```

### 3. Accessing Items: Indexing
Lists are *ordered*, which means every item has a specific numbered position, called its **index**. 
**Crucial Rule:** In Python, indexing starts at `0`, not `1`.

```python
colors = ["red", "green", "blue", "yellow"]
# Index:    0        1        2         3

print(colors[0])  # Output: red
print(colors[2])  # Output: blue
```

**Negative Indexing:**
Python also allows you to count backward from the end of the list using negative numbers. `-1` refers to the last item, `-2` to the second to last, etc.

```python
colors = ["red", "green", "blue", "yellow"]
print(colors[-1]) # Output: yellow
print(colors[-3]) # Output: green
```

### 4. Extracting Subsets: Slicing
You can extract a specific portion (or "slice") of a list by specifying a start index and an end index, separated by a colon `:`.
*Syntax:* `list_name[start_index : end_index]`
**Note:** The `end_index` is *exclusive* (it goes up to, but does not include, that index).

```python
animals = ["cat", "dog", "bird", "fish", "lion", "tiger"]
# Index:     0      1       2       3       4        5

# Get items from index 1 to 3 (includes 1, 2, 3)
subset1 = animals[1:4]
print(subset1)  # Output: ['dog', 'bird', 'fish']

# If you leave out the start index, it defaults to the beginning (0)
subset2 = animals[:3] 
print(subset2)  # Output: ['cat', 'dog', 'bird']

# If you leave out the end index, it goes all the way to the end
subset3 = animals[3:]
print(subset3)  # Output: ['fish', 'lion', 'tiger']
```

---

## 💻 Practice Assignments

Create a new Python file (e.g., `Day8_Task1.py`) and try out these exercises.

### Assignment 1: The Basics
1. Create a list named `favorite_movies` containing the titles of 5 of your favorite movies.
2. Print the entire list.
3. Print the very first movie in your list.
4. Print the very last movie in your list using negative indexing.

### Assignment 2: Slicing Practice
1. Create a list of numbers from 1 to 10: `numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
2. Slice the list to print the first 5 numbers.
3. Slice the list to print the last 3 numbers.
4. Slice the list to print the numbers `[4, 5, 6, 7]`.

### Assignment 3: The Mixed Bag
1. Create a list named `user_profile` that contains the following information in this exact order:
   * First Name (String)
   * Age (Integer)
   * Is a student? (Boolean)
   * Height in meters (Float)
2. Use an f-string to print a sentence using the data from the list by accessing its indexes. 
   *(Example output: "My name is Alice, I am 25 years old, student status is True, and I am 1.65 meters tall.")*

---

### 💡 Daily Routine Checklist (Day 8):
- [ ] Read the notes on list creation, indexing, and slicing.
- [ ] Complete Assignment 1.
- [ ] Complete Assignment 2.
- [ ] Complete Assignment 3.
