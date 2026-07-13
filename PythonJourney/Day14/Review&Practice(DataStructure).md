# Day 14: Review & Practice (Data Structures)

## 📚 Topics Covered

### 1. Recap of Week 2 Data Structures

#### Lists
- **Ordered, mutable** collection of items
- Access by index: `list[0]`
- Methods: `append()`, `remove()`, `pop()`, `insert()`, `sort()`, `reverse()`

#### Tuples
- **Ordered, immutable** collection of items
- Cannot be modified after creation
- Use for: constant data, dictionary keys, function returns
- More memory efficient than lists

#### Dictionaries
- **Unordered, mutable** key-value pairs
- Access by key: `dict['key']`
- Methods: `keys()`, `values()`, `items()`, `get()`, `pop()`

#### Sets
- **Unordered, unique** items collection
- No duplicates allowed
- Methods: `add()`, `remove()`, `union()`, `intersection()`, `difference()`

---

### 2. Nested Data Structures

**Nested structures are data structures inside other data structures.**

#### Lists of Dictionaries
```python
students = [
    {"name": "Alice", "age": 20, "gpa": 3.8},
    {"name": "Bob", "age": 21, "gpa": 3.5},
    {"name": "Charlie", "age": 19, "gpa": 3.9}
]

# Accessing nested data
print(students[0]["name"])  # Output: Alice
```

#### Dictionaries of Lists
```python
grades = {
    "Alice": [90, 85, 92],
    "Bob": [78, 82, 88],
    "Charlie": [95, 93, 97]
}

# Accessing nested data
print(grades["Alice"][0])  # Output: 90
```

#### Lists of Lists (2D Arrays)
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing nested data
print(matrix[0][1])  # Output: 2
```

---

### 3. Complexity & Performance Considerations

| Operation | List | Dictionary | Set | Tuple |
|-----------|------|-----------|-----|-------|
| **Access** | O(n) | O(1) | O(1) | O(n) |
| **Search** | O(n) | O(1) | O(1) | O(n) |
| **Insert** | O(n) | O(1) | O(1) | N/A (immutable) |
| **Delete** | O(n) | O(1) | O(1) | N/A (immutable) |
| **Memory** | More | More | More | Least |

**When to use what:**
- **List:** When you need ordered, mutable data and frequent iteration
- **Dictionary:** When you need fast lookups by key
- **Set:** When you need unique items and fast membership testing
- **Tuple:** When you need immutable, constant data (use as dict keys)

---

## ✏️ Practice Questions

### Q1: Nested Data Structure - Student Database
```python
# Given this nested structure:
students = [
    {"name": "Alice", "age": 20, "grades": [90, 85, 92, 88]},
    {"name": "Bob", "age": 21, "grades": [78, 82, 88, 85]},
    {"name": "Charlie", "age": 19, "grades": [95, 93, 97, 96]}
]

# Questions:
# a) Extract Alice's second grade
# b) Calculate average grade for Bob
# c) Find student with highest average grade
# d) Add a new student to the database
```

### Q2: Complexity Analysis
```python
# Which is more efficient for finding duplicate words in a large text?
# Option A: Using a list
# Option B: Using a set
# Explain your answer with complexity analysis.
```

### Q3: Dictionary vs List
```python
# You have 10,000 phone numbers and need to look up a person by their phone number.
# Should you use a list or dictionary? Why?

# List approach: contacts = [("Alice", "555-1234"), ("Bob", "555-5678")]
# Dictionary approach: contacts = {"555-1234": "Alice", "555-5678": "Bob"}

# Compare performance for 1000 lookups.
```

### Q4: Nested Dictionary Practice
```python
# Create a nested structure for storing course information:
# - Course name, instructor, students enrolled with their grades
# 
# Example format:
courses = {
    "Python101": {
        "instructor": "John Doe",
        "students": {"Alice": 85, "Bob": 92, "Charlie": 78}
    },
    "DataScience": {
        "instructor": "Jane Smith",
        "students": {"Alice": 88, "Bob": 75}
    }
}

# Questions:
# a) Get Alice's grade in Python101
# b) Get all students in DataScience course
# c) Calculate average grade for Python101
# d) Add a new course
```

---

## 🎯 Main Assignment: Student Database Manager

### Objective
Build a **Student Database Manager** that stores student information with grades and calculates averages.

### Requirements
1. **Data Structure:** Use nested dictionaries/lists
   ```python
   students_db = [
       {"id": 1, "name": "Alice", "gpa": 3.8, "grades": [90, 85, 92]},
       {"id": 2, "name": "Bob", "gpa": 3.5, "grades": [78, 82, 88]}
   ]
   ```

2. **Functions to Implement:**
   - `add_student(name, grades)` - Add new student
   - `calculate_average(student_id)` - Calculate average grade
   - `calculate_gpa(grades)` - Convert grades to GPA (A=4.0, B=3.0, etc.)
   - `get_top_student()` - Find student with highest GPA
   - `get_failing_students()` - Find students with average < 70
   - `display_all_students()` - Display formatted report

3. **Bonus Features:**
   - Save to JSON file
   - Sort by GPA or name
   - Update student grades
   - Search by name

### Example Output
```
--- Student Database Report ---
1. Alice - GPA: 3.8, Average: 89
2. Bob - GPA: 3.5, Average: 82
3. Charlie - GPA: 3.9, Average: 95

Top Student: Charlie (GPA: 3.9)
Failing Students: None
```

---

## 💡 Key Takeaways

✅ **Nested structures** allow you to organize complex, real-world data  
✅ **Choose the right data structure** based on your access patterns  
✅ **Dictionaries** are O(1) for lookups, much faster than lists for large datasets  
✅ **Sets** are perfect for membership testing and removing duplicates  
✅ **Understand complexity** to write efficient code at scale  

