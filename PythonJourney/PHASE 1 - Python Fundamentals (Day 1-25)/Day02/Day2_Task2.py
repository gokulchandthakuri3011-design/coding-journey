"""
### Assignment 2: Coffee Shop Order
1. **Store Order Details**: Create variables for a coffee order:
   - `customer_name` (string, e.g., "Gokul")
   - `coffee_type` (string, e.g., "Latte")
   - `quantity` (integer, e.g., 2)
   - `price_per_cup` (float, e.g., 4.50)
   - `is_takeaway` (boolean, e.g., True)
2. **Calculate Total**: Create a variable called `total_cost` that multiplies `quantity` by `price_per_cup`.
3. **Print Receipt**: Print out a nice summary of the order for the customer, including the `total_cost`.
4. **Type Check**: Pick two variables from your order and print their data types using `type()`.
"""

# Coffee Shop Order Details

# Creating variables for the coffee order
customer_name = "Gokul"
coffee_type = "Normal Coffee"
quantity = 2
price_per_cup = 4.50 # Price per cup in dollars
is_takeaway = True

# Calculating total cost
total_cost = quantity * price_per_cup

# Printing the receipt
print("----- Coffee Shop Receipt -----")
print(f"Customer Name: {customer_name}")
print(f"Coffee Type: {coffee_type}")
print(f"Quantity: {quantity}")
print(f"Price per Cup: ${price_per_cup:.2f}")          # Using f-string with formatting 
print(f"Total Cost: ${total_cost:.2f}")
print(f"Takeaway: {'Yes' if is_takeaway else 'No'}")   # Using a ternary operator
print("------------------------------")

# Type Check
print("\n----- Data Types Checked -----")
print(f"Type of customer_name: {type(customer_name)}")
print(f"Type of quantity: {type(quantity)}")
print("------------------------------")
