"""
### Assignment 2: Simple Grocery Total
1. Ask the user for the price of one item using `input()`.
2. Ask how many items they want to buy.
3. Convert the price to `float` and the quantity to `int`.
4. Calculate the total cost and print it.
"""
print("\n--------------------------------")
print("\n --- Simple Grocery Total --- \n")

# Asking user for input
price_per_item = float(input("Enter the price of item: "))
num_items = int(input("Enter the number of items they want to buy: "))
print(f"Price Per Item: ${price_per_item:.2f}")
print(f"Numbers of items to buy: {num_items}")
total_cost = price_per_item * num_items
print(f"\nTotal Cost for every items: ${total_cost:.2f}\n")
print("----------------------------------")
