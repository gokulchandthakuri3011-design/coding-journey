"""
### Assignment 3: Student Grade Tracker

*Practice named tuples and returning multiple values.*

1. Define a named tuple `Student` with fields `name`, `subject`, and `grade`.
2. Create at least 4 student instances with different data.
3. Store them in a list called `students`.
4. Loop through the list and print each student's info in a formatted sentence.
5. Write a function `get_grade_stats(grades)` that accepts a list of numeric grades and returns a tuple of `(average, highest, lowest)`.
6. Test the function with the grades from your students. Unpack and print the results.
- **File:** `Day10_Task3.py`
"""
from collections import namedtuple

# Defining the named tuple 'Student'
student = namedtuple('Student', ['name', 'subject', 'grade'])

# Creating student instances
student1 = student("Arun", "Science", 98)
student2 = student("Gokul", "Maths", 97)
student3 = student("Rozy", "English", 99)
student4 = student("Lalita", "Nepali", 94)

# Storing students in list
students = [student1, student2, student3, student4]

# Looping through the list and printing each student's info
for s in students:
    print(f"{s.name} scored {s.grade} in {s.subject}.")

# Using function to to accept the list of numeric grades and return a tuple of average, highest and lowest
def get_grade_stats(grades):
    average_grades = sum(grades)/len(grades)
    highest_grade = max(grades)
    lowest_grade = min(grades)
    return average_grades, highest_grade, lowest_grade

grades = [int(g) for g in input("Enter the grades seperated by comma: ").split(",")]
average, highest, lowest = get_grade_stats(grades)
print(f"Average: {average}, Highest: {highest}, Lowest: {lowest}")