"""
### Assignment 3: Password Cleaner
1. Create a variable `password` and assign it a string with extra spaces.
2. Use `.strip()` to clean it.
3. Print the length of both the original and cleaned password.
"""
print("\n----------------------------")
print("--- Password Cleaner ---\n")

# Creating a varible for password
password = " Kakarot_Vegeta "
print(f"The length of original password is: {len(password)}\n")
password = password.strip()
print(f"The Passowrd after formatting is: {len(password)}")
print("\n-----------------------------")