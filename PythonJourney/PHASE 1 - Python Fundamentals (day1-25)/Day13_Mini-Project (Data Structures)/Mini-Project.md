# 📝 Day 13 Mini-Project: Console-Based Data Manager

## 🎯 Project Goal
Synthesize everything you have learned about Python's core data structures (**Lists, Tuples, Dictionaries, and Sets**) to build a robust, interactive command-line interface (CLI) application. 

You can choose one of the following two project options:
1. **Option A: Smart To-Do List Manager** (with category tagging and priority levels)
2. **Option B: Advanced Contact Book** (with relationship tags and duplicate prevention)

---

## 📚 Notes: Synthesizing Data Structures
To build a clean and professional program, you will use all four core collections together:

| Data Structure | How to Use It in This Project | Example Representation |
| :--- | :--- | :--- |
| **Dictionary** 📖 | Represents a single entity (a task or a contact) with key-value properties. | `{"name": "Alice", "phone": "555-0199", "email": "alice@email.com"}` |
| **List** 📋 | Stores the collection of all entities sequentially. | `contacts = [dict1, dict2, dict3]` |
| **Set** 🎯 | Maintains a collection of unique tags or categories (no duplicates). | `tags = {"Work", "Personal", "Urgent"}` |
| **Tuple** 🔒 | Stores immutable, fixed-format data (e.g., creation date, GPS coordinates). | `created_at = (2026, 6, 13)` |

---

## 🛠️ Project Requirements

Your program must implement the following operations:
1. **Add**: Insert a new item/contact, validating that inputs are correct and duplicates are handled.
2. **View**: Display the items in a clean, formatted text table.
3. **Search**: Search by name or description.
4. **Update**: Update task status (e.g., mark as completed) or edit contact details.
5. **Delete**: Remove an item/contact safely.
6. **Unique Tag Management**: Allow assigning category tags (using a `set` to prevent duplicate tags on an item).

---

## 📐 CLI Program Architecture
A good command-line program runs in a **continuous loop**, presenting a menu, taking user input, executing the corresponding action, and then returning to the menu until the user chooses to exit.

Here is the general execution flow:
```text
[Start Program]
       │
       ▼
 ┌───────────┐
 │ Main Loop │◄─────────────────────────────┐
 └─────┬─────┘                              │
       │                                    │
       ▼                                    │
 ┌───────────┐                              │
 │ Show Menu │                              │
 └─────┬─────┘                              │
       │                                    │
       ▼                                    │
 ┌───────────┐                              │
 │ Get Input │                              │
 └─────┬─────┘                              │
       │                                    │
       ├─► [1] Add    ──► (Process Add)    ─┤
       ├─► [2] View   ──► (Process View)   ─┤
       ├─► [3] Search ──► (Process Search) ─┤
       ├─► [4] Delete ──► (Process Delete) ─┤
       └─► [5] Exit   ──► [End Program]
```

---

## 📋 Assignment Questions & Step-by-Step Plan

Implement the project by answering the following programming tasks. Create a new file named `Day13_Task1.py` and write your code step-by-step:

### 🔍 Task 1: Define the Data Model
* **Goal:** Decide how your program will store data using Python's collections.
* **Instructions:**
  1. Initialize an empty list called `database` which will hold all your records (each record will be a dictionary).
  2. Initialize a set called `active_tags` containing three starting categories: `{"Work", "Personal", "Study"}`.
  3. Think about how to structure a single entry:
     - Name/Title: **String**
     - Tags: **Set** or **String** (representing the category)
     - Created Date: **Tuple** (e.g., `(2026, 6, 13)`)

### 🔍 Task 2: Build the Main Menu Loop
* **Goal:** Present options to the user and loop indefinitely until they choose to exit.
* **Instructions:**
  1. Write a function `show_menu()` that prints out 6 options:
     - `1. Add Entry`
     - `2. View All Entries`
     - `3. Search Entries`
     - `4. Delete Entry`
     - `5. Manage Categories (Tags)`
     - `6. Exit`
  2. Implement a `while True` loop that repeatedly calls `show_menu()`, prompts the user for their choice (`1` to `6`), and routes it to the appropriate function.
  3. Ensure that if the user enters `6`, the program prints a goodbye message and terminates cleanly.

### 🔍 Task 3: Implement the "Add Entry" Feature
* **Goal:** Create a function to take user input, validate it, package it into a dictionary, and append it to your list.
* **Instructions:**
  1. Ask the user for the name/title of the entry. If they enter nothing or only whitespace, print an error message and return.
  2. Display the available tags (`active_tags`) and ask them to choose one. If the chosen tag isn't in `active_tags`, default the category to `"Uncategorized"`.
  3. Retrieve the current local date (using Python's `datetime` module) and store it as an immutable tuple: `(year, month, day)`.
  4. Create a dictionary representing the entry (keys: `"title"`, `"tag"`, `"date"`) and append it to your `database` list.

### 🔍 Task 4: Implement the "View All" Feature
* **Goal:** Print out a neatly formatted table or numbered list of the entries.
* **Instructions:**
  1. Check if the `database` list is empty. If it is, print `"No entries found."` and return.
  2. Loop through `database` using `enumerate(..., start=1)` to output numbered entries.
  3. For each entry, unpack the date tuple `(year, month, day)` and display a formatted string showing the index, category, title, and creation date.

### 🔍 Task 5: Implement the "Search" Feature
* **Goal:** Find specific entries by matching a search term against names or tags.
* **Instructions:**
  1. Prompt the user for a search query.
  2. Perform a case-insensitive search by checking if the search query is contained within either the entry's `"title"` or its `"tag"`.
  3. Print out all matching entries. If no matches exist, print a message stating so.

### 🔍 Task 6: Implement the "Delete" Feature
* **Goal:** Remove an entry by its index, with proper error and boundary checks.
* **Instructions:**
  1. First, print out the numbered list of all entries (reusing your View function).
  2. Ask the user for the number of the entry they want to delete.
  3. Implement exception handling (`try-except`) to catch cases where the user types non-numeric characters (handling `ValueError`).
  4. Check if the entered index is within the boundaries of the database list. If valid, pop the entry and print a confirmation message; otherwise, print an error.

### 🔍 Task 7: Manage Categories (Sets)
* **Goal:** Add new unique tags to your global set.
* **Instructions:**
  1. Display the current unique tags inside `active_tags`.
  2. Prompt the user to enter a new tag.
  3. Add it to the `active_tags` set (note how sets handle duplicate detection automatically).

---

## 🏆 Stretch Challenges (Optional)
If you complete the tasks above, try adding these advanced features:
1. **Persistent Storage (JSON)**: Research Python's `json` module. Write functions to save the `database` list to a `data.json` file when exiting, and load it automatically 