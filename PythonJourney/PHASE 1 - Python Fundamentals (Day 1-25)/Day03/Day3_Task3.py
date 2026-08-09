"""
### Assignment 3: Time Converter
- Create a variable called `total_minutes` and set it to `135`.
- Using floor division (`//`) and modulus (`%`), calculate how many **hours** and remaining **minutes** this represents.
- Print the result in the format: `135 minutes is X hours and Y minutes.
"""

# Time Converter

# Creating a variable for total minutes
total_minutes = 135

# Calculating hours and remaining minutes
hours = total_minutes // 60 # Floor Division(//) divides and rounds down to nearest int
remaining_minutes = total_minutes % 60

# Printing the result
print(f"{total_minutes} minutes is {hours} hours and {remaining_minutes} minutes.")
