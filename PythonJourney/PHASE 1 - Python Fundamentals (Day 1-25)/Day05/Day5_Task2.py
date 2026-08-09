"""
### Exercise 2: Movie Age Restrictions
Write a program that asks for the user's age and tells them what kind of movies they can watch based on these rules:
- Under 13: "G and PG movies"
- 13 to 16: "PG-13 movies"
- 17 and older: "R-rated movies"
"""
print("\n --- Movie Age Restriction --- \n")

# Asking for user age
age = int(input("Enter your age: "))

# Checking the age for movie category
if age < 13:
    print("You can only watch G & PG movies.")
if 13 >= age <= 16:
    print("You can watch PG-13 movies:")
if age >= 17:
    print("You can watch R-rated movies.")

print("\n---------------------------------")