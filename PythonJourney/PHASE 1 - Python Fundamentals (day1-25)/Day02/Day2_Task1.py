"""
### Assignment 1: Create your profile
Create variables to store your `first_name` (string), `last_name` (string), `age` (integer), `height_in_meters` (float), and `likes_coding` (boolean). Print all variables and their types.
"""

# 1. Creating My Profile
first_name = "Gokul"
last_name = "Chand"
age = 22
height_in_meters = 1.75
likes_coding = True

# 2. Printing My Profile
print("----- User Profile -----")
print("First Name:", first_name)
print("Last Name:", last_name)
print("Age:", age)
print("Height (meters):", height_in_meters)
print("Likes Coding:", likes_coding)
print("------------------------")

# 3. Checking Data Types
print("\n----- Data Types -----")
print("Data type of first_name:", type(first_name))
print("Data type of last_name:", type(last_name))
print("Data type of age:", type(age))
print("Data type of height_in_meters:", type(height_in_meters))
print("Data type of likes_coding:", type(likes_coding))
print("----------------------")

# 4. Experiment with Different Data Types
# Adding first name and last name to create full name
full_name = first_name + " " + last_name
print("\nFull Name (Concatenated):", full_name)
