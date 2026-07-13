"""
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
"""

from operator import itemgetter 

# Creating an empty grade list
student_grades = []

# Creating a variable for Student Database
student_db = [
    {"id": 1, "name": "Alice", "gpa": 0, "grades": [90, 85, 92]},
    {"id": 2, "name": "Bob", "gpa": 0, "grades": [78, 82, 88]},
    {"id": 3, "name": "Arun", "gpa": 0, "grades": [93, 95, 97]},
    {"id": 4, "name": "Gokul", "gpa": 0, "grades": [92, 90, 100]},
    {"id": 5, "name": "Lalita", "gpa": 0, "grades": [80, 40, 100]},
    {"id": 6, "name": "Ram", "gpa": 0, "grades": [40, 50, 30]}
]

def display_menu():
    print("--- Menu Display ---")
    print("1. Add Student")
    print("2. Calculate Average")
    print("3. Calculate GPA")
    print("4. Display Top Student")
    print("5. Display Failed Student")
    print("6. Display All Students after Sorting")
    print("7. Exit the Program")
    return input("Enter your choice: ").strip()

def add_students():
    # Asking user for the name and grades (comma separated)
    name = input("Enter the name of the student: ").strip().capitalize()
    grades_input = input("Enter the grades (comma seperated): ").strip() # grades in 1 line seperated by comma

    # Convert grades input to list of integers
    try:
        grades = [int(g.strip()) for g in grades_input.split(",") if g.strip()]
    except ValueError:
        print("Invalid input. Please enter grades as numbers seperated by commas.")
        return

    if not grades:
        print("No valid grades entered.")
        return

    # Check if student exists
    found = False
    for student in student_db:
        if student["name"].strip().lower() == name.lower():
            found = True
            student["grades"].extend(grades)
            print(f"Grades added successfully to {student['name']}.")
            print(f"ID: {student['id']} - Name: {student['name']} - Grades: {student['grades']}")
            break

    # If student doesn't exists, add new student
    if not found:
        next_id = max(student["id"] for student in student_db) + 1 if student_db else 1

        new_student = {
            "id": next_id,
            "name": name,
            "gpa": 0,
            "grades": grades
        }

        student_db.append(new_student)
        print(f"New Student {name} added successfully with ID {next_id}.")


def calculate_average(): # Calculating average grade for each student
    for student in student_db:
        total_grade = sum(student["grades"])
        num_of_grades = len(student["grades"])
        average_grade = float(total_grade / num_of_grades) if num_of_grades else 0.0
        student["average_grade"] = average_grade
    print("Average Grade calculated and added to dict")


def calculate_gpa():
    # Assigning Grade Points to grades and calculating GPA for each student
    for student in student_db:
        grade_points = []
        for grade in student["grades"]:
            if 90 <= grade <= 100:
                grade_points.append(4.0)
            elif 80 <= grade <= 89:
                grade_points.append(3.5)
            elif 70 <= grade <= 79:
                grade_points.append(3.0)
            elif 60 <= grade <= 69:
                grade_points.append(2.5)
            elif 50 <= grade <= 59:
                grade_points.append(2.0)
            elif 40 <= grade <= 49:
                grade_points.append(1.5)
            else:
                grade_points.append(1.0)

        student["gpa"] = float(sum(grade_points) / len(grade_points)) if grade_points else 0.0
    print("Final GPA calculated and added successfully.")


def display_top():
    if not student_db:
        print("No students available.")
        return
    
    top_gpa = max(student["gpa"] for student in student_db)
    top_students = [s for s in student_db if s["gpa"] == top_gpa]

    print(f"Top GPA : {top_gpa:.2f}")
    for student in top_students:
        print(f"ID {student['id']} - {student['name']}")


def display_failed():
    if not student_db:
        print("No students available.")
        return

    failed_students = [student for student in student_db if student.get("average_grade", 0) < 70]
    if not failed_students:
        print("No failed students.")
        return

    print("--- Failed Students ---")
    for student in failed_students:
        print(f"ID: {student['id']} - {student['name']} - Average Grade: {student['average_grade']:.2f} - GPA: {student.get('gpa', 0):.2f}")


def display_sorted(by="gpa"):
    # Sorting student_db by GPA or name
    if not student_db:
        print("No students availabe.")
        return
    
    if by == "name":
        sorted_students = sorted(student_db, key = itemgetter("name"))
    else: 
        sorted_students = sorted(student_db, key = itemgetter("gpa"), reverse = True)

    print(f"--- Students Sorted by {by.capitalize()} ---")
    for student in sorted_students:
        print(f"ID {student['id']} - Name {student['name']} - GPA {student['gpa']:.2f}")


def exit_program():
    print("Thaks for using the program and good bye!")


def main():
    while True:
        user_choice = display_menu()
        if user_choice == "1":
            add_students()
        elif user_choice == "2":
            calculate_average()
        elif user_choice == "3":
            calculate_gpa()
        elif user_choice == "4":
            display_top()
        elif user_choice == "5":
            display_failed()
        elif user_choice == "6":
            display_sorted()
        elif user_choice == "7":
            exit_program()
            break
        else:
            print("Invlaid choice! Please try again")


if __name__ == "__main__":
    main()