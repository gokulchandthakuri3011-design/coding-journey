# Day 32: Working with Dates & Time

Welcome to Day 32! Today we will learn how Python handles dates and time. This is very useful in real-world programming, such as scheduling tasks, creating logs, working with birthdays, calculating time differences, and building reminder apps.

---

## 📝 Concept Notes

---

### 1. Python Date and Time Module

Python provides the `datetime` module for working with dates and times.

```python
import datetime

print(datetime.datetime.now())
```

This gives the current date and time.

---

### 2. Getting the Current Date

```python
from datetime import date

today = date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
```

This is useful when you need the current year, month, or day.

---

### 3. Getting the Current Time

```python
from datetime import datetime

now = datetime.now()
print(now.time())
```

This prints the current time part, such as hours, minutes, and seconds.

---

### 4. Creating a Specific Date

```python
from datetime import date

my_birthday = date(2005, 8, 20)
print(my_birthday)
```

You can create any date manually by passing year, month, and day.

---

### 5. Formatting Dates

The `strftime()` method helps convert a date or datetime into a readable string.

```python
from datetime import datetime

now = datetime.now()
print(now.strftime("%Y-%m-%d"))
print(now.strftime("%d/%m/%Y"))
print(now.strftime("%H:%M:%S"))
```

Common format codes:
- `%Y` = year (2026)
- `%m` = month (09)
- `%d` = day (21)
- `%H` = hour (24-hour format)
- `%M` = minutes
- `%S` = seconds

---

### 6. Parsing Strings into Dates

You can also convert a string into a date or datetime using `strptime()`.

```python
from datetime import datetime

date_string = "2026-09-21"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
print(parsed_date)
```

This is helpful when reading date values from user input or files.

---

### 7. Time Difference

You can calculate the difference between two dates or datetimes.

```python
from datetime import date

d1 = date(2026, 1, 1)
d2 = date(2026, 9, 21)

result = d2 - d1
print(result.days)
```

This gives the number of days between two dates.

---

### 8. Timedelta

`timedelta` is used to represent a duration of time.

```python
from datetime import datetime, timedelta

now = datetime.now()
future = now + timedelta(days=7)
print(future)
```

This is useful for adding or subtracting days, hours, or minutes.

---

### 9. Why This Matters

Dates and times are used in:
- birthdays and anniversaries
- appointment systems
- logs and reports
- reminder apps
- scheduling and automation

---

## 💻 Practice Assignments

Create a new Python file for each assignment under the `C:\PythonJourney` folder.

---

### Assignment 1: Current Date Display

1. Import `date` from the `datetime` module.
2. Get today’s date.
3. Print the date in the format `YYYY-MM-DD`.
4. Also print the day, month, and year separately.

**File:** `Day32_Task1.py`

---

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

---

### Assignment 3: Time Formatter

1. Get the current date and time.
2. Format it as:
   - `Date: 21/09/2026`
   - `Time: 14:35:20`
3. Print both values clearly.

**File:** `Day32_Task3.py`

---

### Assignment 4: Future Reminder

1. Ask the user for a number of days.
2. Add that many days to the current date using `timedelta`.
3. Print the future date.

Example:

```text
In 10 days, the date will be: 2026-09-30
```

**File:** `Day32_Task4.py`

---

## ✅ Quick Review Questions

1. What module is used for dates and times in Python?
2. What is the difference between `date` and `datetime`?
3. How do you format a date using `strftime()`?
4. How do you convert a string into a date object using `strptime()`?
5. What is `timedelta` used for?

---

## 🧠 Short Summary

Python’s `datetime` module makes it easy to work with current time, custom dates, formatted output, and date calculations. Learning these basics is very important for real projects like calendars, reminders, reports, and automation.
