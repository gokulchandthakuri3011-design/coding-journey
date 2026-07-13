"""
### Assignment 3: The Mixed Bag
1. Create a list named `user_profile` that contains the following information in this exact order:
   * First Name (String)
   * Age (Integer)
   * Is a student? (Boolean)
   * Height in meters (Float)
2. Use an f-string to print a sentence using the data from the list by accessing its indexes. 
   *(Example output: "My name is Alice, I am 25 years old, student status is True, and I am 1.65 meters tall.")*
"""

# 1. Creating a list named 'user_profile' with the specified information
user_profile = []

# Getting user input for each piece of information
first_name = input("Enter your first name: ")
age = int(input("Enter your age: "))
is_Student = input("Are you a student? (yes/no): ").lower() == 'yes'
height = float(input("Enter your height in meters: "))

# Adding data to the list
user_profile.append(first_name)
user_profile.append(age)
user_profile.append(is_Student)
user_profile.append(height)

# 2. Using an f-string to print a sentence using the data from the list
print(f"My name is {user_profile[0]}, I am {user_profile[1]} years old, student status is {user_profile[2]}, and I am {user_profile[3]} meters tall.")