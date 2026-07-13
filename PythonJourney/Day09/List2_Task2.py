"""
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
"""

print("--- Grade Organiser ---")
print() # Blank line for easy reding output

# 1. Creating a list called grade
grade = [72, 95, 88, 60, 95, 78, 55, 95, 81, 68]

print("List of grades: ", grade)

# 2. Number of items in the list
number_of_items = len(grade)
print(f"Number of items in the list: {number_of_items}")

# 3. Highest and lowest grade
highest_grade = max(grade)
lowest_grade = min(grade)
print(f"Highest grade: {highest_grade}")
print(f"Lowest grade: {lowest_grade}")

# 4. Average grade
average_grade = float(sum(grade)) / number_of_items
print(f"Average grade: {average_grade}")

# 5. Sort the grades in ascending order and print the sorted list
grade.sort()
print(f"Sorted grades in ascending order: {grade}")

# 6. Count how many times the grade 95 appears in the list
count = grade.count(95)
print(f"The grade 95 appears {count} tiems in the list.")

# 7. Check if the grade 100 is in the list and print the boolean result
grade_check = 100 in grade
print(f"Is the grade 100 in the list?: {grade_check}")

print()

print("--- End of the assignment ---")
