"""
date_utils.py - A utility module for date calculations using datetime.
"""
from datetime import datetime


def day_difference(date1: str, date2: str, fmt: str = "%Y-%m-%d") -> int: # here -> int tells the return will be int
   """Calculate the number of days between two date strings."""
   d1 = datetime.strptime(date1, fmt)
   d2 = datetime.strptime(date2, fmt)
   return abs((d2 - d1).days) # returns + ve value


def format_date(date: str, input_fmt: str = "%Y-%m-%d", output_fmt: str = "%Y-%m-%d %H-%M-%S") -> str:
   """Reformat a date string from one format to another."""
   return datetime.strptime(date, input_fmt).strftime(output_fmt)


def leap_year_checker(year: int) -> bool:
   """Check if a given year is a leap year."""
   return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


if __name__ == "__main__":
   date1 = "2026-7-25"
   date2 = "2003-11-30"
   date = "2003-11-30"
   year = 2026
   print(f"There are {day_difference(date1, date2)} days between {date1} and {date2}.")
   print(f"The {date} is formatted as: {format_date(date)}")
   print(f"The given year {year} is leap year: {leap_year_checker(year)}")
