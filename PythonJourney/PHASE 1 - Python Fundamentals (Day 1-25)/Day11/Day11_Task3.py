"""
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
"""

# Creating a student profile dictionary
student_profile = {
    "name" : "Liam",
    "age" : 17,
    "courses" : ["Math", "Science", "History"],
    "grades" : {"Math" : 90, "Science" : 85, "History" : 88}
}

# Printing Student name and age
print(f"\n     Student Profile     ")
print(f"Name: {student_profile.get('name')}")
print(f"Age: {student_profile.get('age')}")

# Accessing and printing the second course in the "courses" list
print(f"2nd Course: {student_profile['courses'][1]}")

# Accessing and printing the student's grade in Math
print(f"Math Grade: {student_profile['grades']['Math']}")

# Average grade using sum() and len() on grades.values()
grades = student_profile.get("grades", None)
average = sum(grades.values())/len(grades.values())
print(f"Average Grade: {average:.2f}") 