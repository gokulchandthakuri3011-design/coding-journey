"""
### Assignment 3: Password and Access
1. Ask the user for a secret code.
2. Check if the code equals `openSesame`.
3. Print `Access granted` when it matches, otherwise print `Access denied`.
4. Add a second check that also requires a second boolean variable `is_admin` to be `True`.
"""

# Day 3: Password and Access Checker

# 1. Ask the user for a secret code
secret_code = input("Enter the secret code: ")

# 2. Check if it matches 'openSesame'
code_matches = secret_code == "openSesame"

print("\n--- Basic Access Check ---")
if code_matches:
    print("Access granted")
else:
    print("Access denied")

# 4. Double check requiring is_admin to be True
is_admin = True # Simulated admin status
print("\n--- Admin Access Check (Requires Admin Status) ---")
print(f"Admin Status: {is_admin}")
if code_matches and is_admin:
    print("Access granted (Admin)")
else:
    print("Access denied")
