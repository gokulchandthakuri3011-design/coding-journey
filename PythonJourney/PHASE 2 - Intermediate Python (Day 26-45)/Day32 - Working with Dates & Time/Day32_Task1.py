"""
### Assignment 1: Current Date Display

1. Import `date` from the `datetime` module.
2. Get today’s date.
3. Print the date in the format `YYYY-MM-DD`.
4. Also print the day, month, and year separately.

**File:** `Day32_Task1.py`
"""
from datetime import date

today = date.today()
formatted_date = today.strftime("%Y-%m-%d")
print(f"Today is: {formatted_date}")