"""
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
"""