"""
### Challenge
7. Create a script that uses `os` to list all files and folders in the current directory.
8. Build a small tool that takes a list of names and uses `zip()` to combine them with a list of ages.
9. Write a program that uses `len()`, `sum()`, `max()`, and `min()` together to analyze a list of test scores.
"""

# Listing all files and folders in the current directory
import os
path = os.getcwd() # Returns current directory path as string
files = sorted(os.listdir(path)) # Sorts the files & folders in that directory in ascending order
print(f"Current Directory: {path}\n")
for i, file in enumerate(files):
    print(f"{i}: {file}")

# Using zip() to combile names and ages
names = ["Arun", "Gokul", "Lalita", "Hitesh", "Aastha"]
ages = [22, 22, 21, 22, 21]
for name, age in zip(names, ages):
    print(f"{name}: {age}")

# Using built-in functions to analyze the list of scores
scores = [87, 90, 67, 76, 98, 45, 50]
average = sum(scores)/len(scores)
maximum_score = max(scores)
minimum_score = min(scores) 
print(f"Average score is: {average}")
print(f"The maximum score is: {maximum_score}")
print(f"The minimum score is: {minimum_score}")