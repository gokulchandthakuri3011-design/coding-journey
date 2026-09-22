"""
### Assignment 2: Birthday Countdown

1. Ask the user to enter their birth date in `YYYY-MM-DD` format.
2. Convert the input into a date object.
3. Get today’s date.
4. Calculate how many days old they are.
5. Print a message like:

```text
You are 7300 days old.
```

**File:** `Day32_Task2.py`
"""
from datetime import datetime, date

user_birthdate = input("Enter your birthdate in Y-M-D: ")
birth_date = datetime.strptime(user_birthdate, "%Y-%m-%d").date()
today = date.today()
Days_diff = today - birth_date
print(f"You are {Days_diff.days} days old.")