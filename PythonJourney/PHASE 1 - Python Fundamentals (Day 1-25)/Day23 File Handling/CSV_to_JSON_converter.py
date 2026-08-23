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
import csv
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Reading CSV File and getting data as a Dict
def csv_reader():
    user_data = []
    with open(os.path.join(BASE_DIR, "employees.csv"),"r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            name = row.get("Name", "")
            department = row.get("Department", "")
            try:
                salary = int(row.get("Salary", 0))
            except ValueError:
                salary = None

            user_data.append({"Name": name, "Department": department, "Salary": salary})
    return user_data



# Writing JSON File
def json_writer(user_data):
    with open(os.path.join(BASE_DIR, "employees.json"), "w", newline="") as file:
        json.dump(user_data, file, indent=4)

# Reading JSON File for confirmation
def json_reader():
    with open(os.path.join(BASE_DIR, "employees.json"), "r") as file:
        reader = file.read()
        print(reader)

# Using main() to call the methods
print("\n ==== CSV -> JSON Converter === \n")
user_data = csv_reader()
print(user_data)
json_writer(user_data)
json_reader()


