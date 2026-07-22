# Day 23: File Handling in Python

> **Duration:** 1 hour (30 min reading + 30 min practice)
> **Goal:** Learn how to read, write, and manage files using Python

---

## Table of Contents

1. [Why File Handling?](#1-why-file-handling)
2. [File Access Modes](#2-file-access-modes)
3. [Opening and Closing Files](#3-opening-and-closing-files)
4. [Reading Files](#4-reading-files)
5. [Writing Files](#5-writing-files)
6. [The `with` Statement](#6-the-with-statement)
7. [Working with CSV Files](#7-working-with-csv-files)
8. [Working with JSON Files](#8-working-with-json-files)
9. [Common Mistakes to Avoid](#9-common-mistakes-to-avoid)
10. [Quick Reference Cheat Sheet](#10-quick-reference-cheat-sheet)
11. [Practice Assignments](#11-practice-assignments)

---

## 1. Why File Handling?

So far, all the data we've worked with disappears when the program ends. Files let us **save data permanently** on the computer. This is useful for:

- Saving user settings/configuration
- Logging events (what happened and when)
- Processing large datasets (CSV, JSON)
- Storing results for later use

**Think of it this way:** Variables are like a whiteboard (erased when you leave), files are like a notebook (stays until you throw it away).

---

## 2. File Access Modes

When opening a file, you must tell Python **how** you want to access it.

| Mode | Name | Description |
|------|------|-------------|
| `'r'` | Read | Opens file for reading. File **must exist**. This is the default. |
| `'w'` | Write | Opens file for writing. **Creates** new file OR **overwrites** existing content. |
| `'a'` | Append | Opens file for writing. **Creates** new file OR **adds to end** of existing file. |
| `'x'` | Exclusive Create | Creates a new file. **Fails** if file already exists. |
| `'r+'` | Read + Write | Opens for both reading and writing. File **must exist**. |
| `'b'` | Binary | Add to any mode for binary files (e.g., `'rb'`, `'wb'`). Used for images, videos, etc. |

### Quick Example of Each Mode:

```python
# 'r' - Read mode (file must exist)
file = open("data.txt", "r")

# 'w' - Write mode (overwrites everything!)
file = open("data.txt", "w")

# 'a' - Append mode (adds to the end)
file = open("data.txt", "a")

# 'x' - Create mode (fails if file exists)
file = open("data.txt", "x")

# 'r+' - Read and Write (file must exist)
file = open("data.txt", "r+")
```

> **Warning:** Be careful with `'w'` mode! It deletes ALL existing content in the file.

---

## 3. Opening and Closing Files

### Basic Syntax

```python
# Open a file
file = open("filename.txt", "mode")

# Always close when done!
file.close()
```

### Why Close a File?

When you close a file:
- All changes are saved to disk
- The system frees up resources
- Other programs can access the file

> **Problem:** If an error happens before `file.close()`, the file stays open. That's why we use the `with` statement (covered in Section 6).

### Example: Opening and Closing

```python
# Opening a file for writing
file = open("hello.txt", "w")
file.write("Hello, World!")
file.close()

# Opening a file for reading
file = open("hello.txt", "r")
content = file.read()
print(content)  # Output: Hello, World!
file.close()
```

---

## 4. Reading Files

Python gives you three main ways to read file contents:

### 4.1 `read()` - Read the entire file

```python
file = open("hello.txt", "r")
content = file.read()       # Reads EVERYTHING as one string
print(content)
file.close()
```

**Good for:** Small files where you need all the content at once.

### 4.2 `readline()` - Read one line at a time

```python
file = open("hello.txt", "r")
line1 = file.readline()     # Reads first line
line2 = file.readline()     # Reads second line
print(line1)
print(line2)
file.close()
```

**Good for:** Processing files line by line, or when you only need the first few lines.

### 4.3 `readlines()` - Read all lines into a list

```python
file = open("hello.txt", "r")
lines = file.readlines()    # Returns a list of lines
print(lines)                # ['Hello, World!\n', 'Second line\n', 'Third line']
file.close()
```

**Good for:** When you need each line as a separate item in a list.

### 4.4 Iterating Over a File (Most Memory-Efficient)

```python
file = open("hello.txt", "r")
for line in file:
    print(line.strip())     # strip() removes the extra \n
file.close()
```

**Good for:** Large files. This doesn't load the entire file into memory.

### Reading Example - Putting It All Together

Let's say `data.txt` contains:
```
Name: Gokul
Age: 25
City: Dhangadhi
```

```python
# Method 1: read() - Get everything
file = open("data.txt", "r")
all_text = file.read()
print(all_text) # It prints exactly how it is in the file
file.close()

# Method 2: readline() - Get one line
file = open("data.txt", "r")
first_line = file.readline()       # "Name: Gokul\n"
second_line = file.readline()      # "Age: 25\n"
print(first_line.strip())          # "Name: Gokul"
file.close()

# Method 3: readlines() - Get a list
file = open("data.txt", "r")
all_lines = file.readlines()       # ['Name: Gokul\n', 'Age: 25\n', 'City: Chennai\n']
print(all_lines[0].strip())        # "Name: Gokul"
file.close()

# Method 4: for loop (Best for large files)
file = open("data.txt", "r")
for line in file:
    print(line.strip())
file.close()
```

---

## 5. Writing Files

### 5.1 `write()` - Write a string to the file

```python
file = open("output.txt", "w")
file.write("First line\n")
file.write("Second line\n")
file.write("Third line\n")
file.close()
```

**Remember:**
- `write()` does NOT add a newline automatically. You must add `\n` yourself.
- `'w'` mode overwrites the file. Use `'a'` to add to the end.

### 5.2 `writelines()` - Write a list of strings

```python
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]

file = open("output.txt", "w")
file.writelines(lines)      # Writes all strings at once
file.close()
```

**Note:** `writelines()` also does NOT add newlines. Each string in the list should already have `\n` at the end.

### 5.3 Append Mode (`'a'`)

```python
# First, let's create a file
file = open("log.txt", "w")
file.write("Log entry 1\n")
file.close()

# Now append to it (adds to the end, doesn't delete)
file = open("log.txt", "a")
file.write("Log entry 2\n")
file.write("Log entry 3\n")
file.close()

# Read to verify
file = open("log.txt", "r")
print(file.read())
file.close()

# Output:
# Log entry 1
# Log entry 2
# Log entry 3
```

---

## 6. The `with` Statement

The `with` statement is the **recommended way** to work with files. It automatically closes the file, even if an error occurs.

### Without `with` (Old Way - Don't Use)

```python
file = open("data.txt", "r")
try:
    content = file.read()
    print(content)
finally:
    file.close()        # Must remember to close manually
```

### With `with` (Recommended Way)

```python
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
# File is automatically closed here! Even if an error happens.
```

### Reading with `with`

```python
# Read entire file
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# Read line by line
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())

# Read into a list
with open("data.txt", "r") as file:
    lines = file.readlines()
    print(lines)
```

### Writing with `with`

```python
# Write to file (overwrites)
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is written using 'with'\n")

# Append to file
with open("log.txt", "a") as file:
    file.write("New log entry\n")
```

> **Best Practice:** ALWAYS use `with` when working with files. It's safer and cleaner.

---

## 7. Working with CSV Files

CSV (Comma-Separated Values) is a common file format for storing tabular data. Python has a built-in `csv` module to handle it.

### What is a CSV File?

```
Name,Age,City
Gokul,22,Dhangadhi
Priya,22,Bangalore
Arun,22,Dhangadhi
```

### 7.1 Reading a CSV File

```python
import csv

# Reading with csv.reader
with open("students.csv", "r") as file:
    reader = csv.reader(file) # Creates a CSV reader obj, allowing to interate over rows and each row returned as a list of strings
    
    # Skip header row (optional)
    header = next(reader) # next() gets the first row from the reader and advances the iterator, so the for loop starts from the next row
    print("Columns:", header)
    
    # Read each row
    for row in reader:
        print(row)       # ['Gokul', '25', 'Chennai']
```

### 7.2 Reading CSV as Dictionaries

```python
import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file) # Here DictReader() converts first line header to dict-keys and each line data becomes respective values to key(key-value) -> so each row is itself dictionary
    
    for row in reader:
        print(row["Name"], "is", row["Age"], "years old")
        # Gokul is 25 years old
        # Priya is 22 years old
```

### 7.3 Writing a CSV File
# In short: csv.writerow() is smarter than file.write() — it knows CSV rows need line breaks, so it adds them for you.
```python
import csv

# Writing a new CSV
with open("output.csv", "w", newline="") as file: # newline="" is a Windows-specific fix to prevent double line breaks in CSV files. It's safe to use on all platforms.
    writer = csv.writer(file)
    
    # Write header
    writer.writerow(["Name", "Age", "City"])
    
    # Write data rows
    writer.writerow(["Gokul", "25", "Chennai"])
    writer.writerow(["Priya", "22", "Bangalore"])

# Writing using dictionaries
with open("output.csv", "w", newline="") as file:
    columns = ["Name", "Age", "City"]
    writer = csv.DictWriter(file, fieldnames=columns)
    
    writer.writeheader()                    # Writes: Name,Age,City
    writer.writerow({"Name": "Gokul", "Age": 25, "City": "Chennai"})
    writer.writerow({"Name": "Priya", "Age": 22, "City": "Bangalore"})
```

> **Short Note:** `csv.DictWriter` converts dictionaries to CSV rows. The `fieldnames` parameter is required — it's a list of column names that tells the writer which keys to extract from each dictionary and in what order to place them in the CSV. For example, `fieldnames=["Name", "Age"]` means: extract `"Name"` key first, then `"Age"` key, and write them as `value1,value2`. Without `fieldnames`, the writer doesn't know how to map your dictionary data to CSV columns.

> **Note:** On Windows, add `newline=""` when writing CSV to avoid extra blank lines.

---

## 8. Working with JSON Files

JSON (JavaScript Object Notation) is a popular format for storing structured data. Python has a built-in `json` module.

### What is a JSON File?

```json
{
    "name": "Gokul",
    "age": 25,
    "hobbies": ["coding", "reading", "gaming"],
    "address": {
        "city": "Chennai",
        "state": "Tamil Nadu"
    }
}
```

### 8.1 Reading JSON Files

```python
import json

# Load JSON from a file
with open("data.json", "r") as file:
    data = json.load(file)        # Converts JSON to Python dict/list

print(data["name"])               # "Gokul"
print(data["hobbies"])            # ['coding', 'reading', 'gaming']
print(data["address"]["city"])    # "Chennai"
```

### 8.2 Writing JSON Files

```python
import json

# Python data
user = {
    "name": "Gokul",
    "age": 25,
    "hobbies": ["coding", "reading", "gaming"],
    "active": True
}

# Write to JSON file
with open("user.json", "w") as file:
    json.dump(user, file, indent=4)    # indent for pretty formatting

# Verify by reading it back
with open("user.json", "r") as file:
    print(file.read())
```

**Output:**
```json
{
    "name": "Gokul",
    "age": 25,
    "hobbies": [
        "coding",
        "reading",
        "gaming"
    ],
    "active": true
}
```

### 8.3 JSON to String and Back

```python
import json

# Python dict to JSON string
data = {"name": "Gokul", "age": 25}
json_string = json.dumps(data)
print(json_string)        # '{"name": "Gokul", "age": 25}'

# JSON string back to Python dict
parsed_data = json.loads(json_string)
print(parsed_data["name"])   # "Gokul"
```

### Quick Comparison: `json.load()` vs `json.loads()`

| Function | What it does | Input |
|----------|-------------|-------|
| `json.load()` | Read JSON from a **file** | File object |
| `json.loads()` | Parse JSON from a **string** | String |
| `json.dump()` | Write Python data to a **file** | File object |
| `json.dumps()` | Convert Python data to a **JSON string** | String |

> **Memory trick:** The **s** in `loads`/`dumps` stands for **string**.

---

## 9. Common Mistakes to Avoid

### Mistake 1: Forgetting to Close Files
```python
# BAD - File might not close properly
file = open("data.txt", "r")
content = file.read()
# Oops, we forgot file.close()!

# GOOD - Use with statement
with open("data.txt", "r") as file:
    content = file.read()
# Automatically closed!
```

### Mistake 2: Not Handling File Not Found
```python
# BAD - Program crashes if file doesn't exist
with open("missing.txt", "r") as file:
    content = file.read()

# GOOD - Handle the error (we'll learn try/except in Day 24)
# For now, just make sure the file exists!
```

### Mistake 3: Using Wrong Mode
```python
# Trying to read a file that doesn't exist
with open("missing.txt", "r") as file:  # Error!
    content = file.read()

# Using 'w' when you meant 'a' (overwrites everything!)
with open("log.txt", "w") as file:      # Deletes old content!
    file.write("New entry\n")
```

### Mistake 4: Forgetting `\n` in write()
```python
# BAD - All text on one line
with open("output.txt", "w") as file:
    file.write("Line 1")
    file.write("Line 2")
# Output: Line 1Line 2

# GOOD - Add newlines
with open("output.txt", "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
# Output:
# Line 1
# Line 2
```

---

## 10. Quick Reference Cheat Sheet

```
FILE OPERATIONS CHEAT SHEET
============================

OPENING FILES
    open("file.txt", "r")     - Read only
    open("file.txt", "w")     - Write (overwrites)
    open("file.txt", "a")     - Append (adds to end)
    open("file.txt", "x")     - Create (fails if exists)
    open("file.txt", "r+")    - Read and Write

READING
    file.read()               - Read entire file as string
    file.readline()           - Read one line
    file.readlines()          - Read all lines as list
    for line in file:         - Iterate line by line

WRITING
    file.write("text")        - Write a string
    file.writelines([...])    - Write list of strings

WITH STATEMENT (ALWAYS USE THIS)
    with open("file.txt", "r") as f:
        content = f.read()

CSV MODULE
    import csv
    csv.reader(file)          - Read CSV rows as lists
    csv.DictReader(file)      - Read CSV rows as dicts
    csv.writer(file)          - Write CSV rows from lists
    csv.DictWriter(file)      - Write CSV rows from dicts

JSON MODULE
    import json
    json.load(file)           - Read JSON from file
    json.loads(string)        - Parse JSON from string
    json.dump(data, file)     - Write JSON to file
    json.dumps(data)          - Convert to JSON string
```

---

## 11. Practice Assignments

### Assignment 1: File Log Generator (Easy)

Create a program that asks the user for their name and activity, then saves it to a log file with a timestamp.

**Expected Output in `activity_log.txt`:**
```
2024-01-15 10:30:00 - Gokul - Started Python learning
2024-01-15 11:00:00 - Gokul - Completed file handling practice
```

**Hints:**
- Use `datetime` module for timestamp
- Use append mode (`'a'`) so entries don't overwrite
- Use `with` statement

---

### Assignment 2: CSV Grade Processor (Medium)

Create a program that:
1. Reads a CSV file (`grades.csv`) with columns: Name, Math, Science, English
2. Calculates the average for each student
3. Writes results to a new CSV file (`results.csv`) with columns: Name, Average, Grade

**Grade Scale:**
- Average >= 90: Grade A
- Average >= 80: Grade B
- Average >= 70: Grade C
- Average >= 60: Grade D
- Average < 60: Grade F

**Sample `grades.csv`:**
```
Name,Math,Science,English
Gokul,85,92,88
Priya,78,85,90
Arun,92,88,95
```

---

### Assignment 3: JSON System Configuration Loader (Medium)

Create a program that:
1. Reads a JSON config file (`config.json`) containing app settings
2. Displays all settings to the user
3. Allows the user to update a setting
4. Saves the updated settings back to the JSON file

**Sample `config.json`:**
```json
{
    "app_name": "MyApp",
    "version": "1.0.0",
    "theme": "dark",
    "font_size": 14,
    "auto_save": true
}
```

---

### Assignment 4: Word Counter (Medium)

Create a program that:
1. Reads a text file
2. Counts the total number of words, lines, and characters
3. Finds the most common word
4. Writes a report to a new file

**Expected Report Output:**
```
=== WORD COUNT REPORT ===
Total Lines: 15
Total Words: 120
Total Characters: 750
Most Common Word: "the" (appeared 12 times)
```

---

### Assignment 5: CSV to JSON Converter (Hard)

Create a program that:
1. Reads any CSV file
2. Converts each row to a dictionary
3. Writes all dictionaries as a JSON array to a new file
4. Handle edge cases (empty files, missing data)

**Input `employees.csv`:**
```
Name,Department,Salary
Gokul,Engineering,75000
Priya,Design,68000
Arun,Marketing,62000
```

**Output `employees.json`:**
```json
[
    {"Name": "Gokul", "Department": "Engineering", "Salary": 75000},
    {"Name": "Priya", "Department": "Design", "Salary": 68000},
    {"Name": "Arun", "Department": "Marketing", "Salary": 62000}
]
```

---

### Assignment 6: Multi-File Merger (Hard)

Create a program that:
1. Takes multiple text files as input
2. Merges their contents into a single file
3. Adds a header before each file's content showing the filename
4. Handles missing files gracefully

**Expected Output in `merged.txt`:**
```
===== FILE: file1.txt =====
Content of file1...

===== FILE: file2.txt =====
Content of file2...
```

---

## Summary

| Concept | What You Learned |
|---------|------------------|
| File Modes | `r`, `w`, `a`, `x`, `r+`, `b` |
| Reading | `read()`, `readline()`, `readlines()`, for loop |
| Writing | `write()`, `writelines()` |
| Best Practice | Always use `with` statement |
| CSV | `csv.reader`, `csv.writer`, `csv.DictReader`, `csv.DictWriter` |
| JSON | `json.load()`, `json.dump()`, `json.loads()`, `json.dumps()` |

---

> **Tomorrow:** Day 24 - Error & Exception Handling - Learn how to handle errors gracefully so your programs don't crash!

---

> **Remember:** Practice makes perfect! Try solving at least 2-3 assignments today. Start with the easy ones and work your way up. Happy coding! 🐍
