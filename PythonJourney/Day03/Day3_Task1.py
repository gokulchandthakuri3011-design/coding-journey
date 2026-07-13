"""
### Assignment 1: The Bill Splitter
Imagine you and two friends went to a restaurant. 
- The total bill came to **$85**.
- You want to leave a **15%** tip.
- You need to split the total cost (bill + tip) evenly among the **3** of you.
"""

# Initializing the variables
total_bill = 85.0
tip_percentage = 0.15
number_of_people = 3

# Calculating the tip amount
tip_amount = total_bill * tip_percentage

# Calculating the total cost (bill + tip)
total_cost = total_bill + tip_amount

# Calculating the amount each person needs to pay
amount_per_person = total_cost / number_of_people

# Printing the bill details
print("----- Bill Details -----")
print(f"Total Bill: ${total_bill:.2f}") 
print(f"Tip Percentage: {tip_percentage * 100:.0f}%")
print(f"Tip Amount: ${tip_amount:.2f}")
print(f"Total Cost: ${total_cost:.2f}")
print(f"Amount per Person: ${amount_per_person:.2f}")
print("------------------------")
