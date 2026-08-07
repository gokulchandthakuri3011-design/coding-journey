"""
### Assignment 4: Bank Account Simulation
- Create a variable `balance` and set it to `500`.
- You deposit `$150` (Use the `+=` operator to update the balance).
- You withdraw `$40` (Use the `-=` operator to update the balance).
- Your investments double your current balance (Use the `*=` operator to multiply the balance by `2`).
- Print the final balance after each operation to track the changes.
"""

# Day 3: Bank Account Simulation Practice

balance = 500.0
print("----- Bank Account Statement -----")
print(f"Initial Balance: ${balance:.2f}")

# Deposit $150
balance += 150.0
print(f"Deposited $150.00. Current Balance: ${balance:.2f}")

# Withdraw $40
balance -= 40.0
print(f"Withdrew $40.00. Current Balance: ${balance:.2f}")

# Double the balance
balance *= 2.0
print(f"Investments doubled! Final Balance: ${balance:.2f}")
print("----------------------------------")
