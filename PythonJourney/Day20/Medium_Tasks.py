"""
### Medium
4. Create a program that uses `math` to calculate the area of a circle given its radius.
5. Make a small guessing game where the computer picks a random number between 1 and 20.
6. Write a program that uses `datetime` to print the current date and time in a nice format.
"""

# Program to calculate the area of a circle
import math
radius = float(input("Enter the radius: "))
area = math.pi * radius * radius
print(f"The area of circle with radius({radius}) is: {area:.2f}")

# Programs picking random number between 1 & 20
import random
random_num = random.randint(1,20)
print(f"The randomally picked number 1-20 is: {random_num}")

# Program printing the current date & time
from datetime import datetime
current = datetime.now()
print(f"Current Date & Time: {current.strftime('%Y-%m-%d %H:%M:%S')}")
