"""
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

### Remember:
- open("grades.csv") looks for the file in your current working directory, not the script's folder.
- To always find files relative to the script, use:
    import os
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
- __file__ → script's path
- os.path.abspath(__file__) → full absolute path
- os.path.dirname(...) → strips filename, keeps only the folder
- os.path.join(BASE_DIR, "grades.csv") → builds the correct full path
"""
import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Reading and calculating data from csv file
def grade_calc():
    with open(os.path.join(BASE_DIR, "grades.csv"), "r", newline="") as file:
        reader = csv.reader(file)

        # Printing the header
        header = next(reader)
        print(header)

        results = []
        for line in reader:
            student_info = list(line)
            name = student_info[0]
            average = sum(int(x) for x in student_info[1:])/len(student_info[1:])
            if average >= 90:
                grade = "A"
            elif average >= 80:
                grade = "B"
            elif average >= 70:
                grade = "C"
            elif average >= 60:
                grade = "D"
            else:
                grade = "F"

            results.append([name, round(average, 2), grade])
            print(f"{name}: {average:.2f} → {grade}")

    # Writing results to new file
    new_file(results)

def new_file(results):
    with open(os.path.join(BASE_DIR, "results.csv"), "w", newline="") as file:
        writer = csv.writer(file)

        # Writing header
        writer.writerow(["Name", "Average", "Grade"])

        # Writing data
        for row in results:
            writer.writerow(row)

grade_calc()