"""
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
"""

from datetime import datetime

# Asking user for the input (name and activity)
name = input("Enter your name: ")
activity = input("What you prefer to do? : ")
now = datetime.now()
time = now.strftime("%Y-%m-%d %H:%M:%S")

# Combining all into 1 String
info = time + " - " + name + " - " + activity

# Writing to file
with open("activity_log.txt", "a") as file:
    file.write(info + "\n")

print("Log saved successfully!")
