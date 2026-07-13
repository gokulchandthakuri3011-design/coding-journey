"""
### Assignment 2: Age Checker
1. Ask the user for their age.
2. Convert the answer to an integer.
3. Print whether the user is old enough to vote (`18` or older).
4. Print whether the user is a teenager (age between `13` and `19` inclusive).
"""

# Day 3: Age Checker

# 1. Ask the user for their age & 2. Convert to integer
age_input = input("Enter your age: ")
age = int(age_input)

# 3. Check voting eligibility
can_vote = age >= 18

# 4. Check if they are a teenager
is_teenager = 13 <= age <= 19

# Print the results
print("----- Age Checker Results -----")
print(f"Age entered: {age}")
print(f"Old enough to vote (18 or older): {can_vote}")
print(f"Is a teenager (13 to 19 inclusive): {is_teenager}")
print("-------------------------------")
