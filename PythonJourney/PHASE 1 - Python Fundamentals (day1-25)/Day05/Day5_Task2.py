"""
### Assignment 2: Simple Grocery Total
1. Ask the user for the price of one item using `input()`.
2. Ask how many items they want to buy.
3. Convert the price to `float` and the quantity to `int`.
4. Calculate the total cost and print it.

Example output:
```
Price per item: 4.50
Quantity: 3
Total cost: 13.5
"""

# Simple Grocery Total

# Asking the user for the price of one item
price_per_item = float(input("Price per item: "))

# Asking how many items they want to buy
quantity = int(input("Quantity of items: "))

# Calculating the total cost
total_cost = price_per_item * quantity

# Printing the total cost
print(f"---- Simple Grocery Total ----")
print(f"Price per item: {price_per_item}")
print(f"Quantity: {quantity}")
print(f"Total cost: {total_cost}")
