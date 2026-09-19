"""
### Assignment 1: Email Validator
Write a Python script that checks whether a user-entered email is valid using regex.

Questions:
- What part of the email pattern ensures there is a `@` symbol?
- Why is the `^` and `$` important in the pattern?
"""

import re


# Checking whether a user-entered email is valid or not
def email_checker(email,pattern):
    validation = re.match(pattern, email)
    if validation:
        print(f"{email} is valid: {validation.group()}")
    else:
        print("Not a valid email!")

def main():
    print("--- Email Validator ---\n")
    email = input("Enter your email adress: ")
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    print("--- Validating Email ---\n")
    email_checker(email, pattern)

if __name__ == "__main__":
    main()