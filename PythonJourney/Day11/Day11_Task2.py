"""
### Assignment 2: Inventory Management Tracker

*Practice modifying dictionaries and looping through elements.*

You are managing stock levels for a small grocery store.
1. Create a dictionary `grocery_stock` with the following items and quantities:
   - `"bread"`: 15
   - `"milk"`: 8
   - `"eggs"`: 30
   - `"butter"`: 5
2. The store receives a restock! Update the quantity of `"milk"` by adding `10` more, and `"butter"` by adding `5` more.
3. The store has run out of `"bread"`. Delete the `"bread"` key-value pair from the dictionary.
4. Add a new item `"cheese"` with a quantity of `12`.
5. Print a clean, formatted report of the final inventory using a loop and `.items()`.
   *(Example Output)*:
   ```text
   --- Final Grocery Stock ---
   milk: 18 in stock
   eggs: 30 in stock
   butter: 10 in stock
   cheese: 12 in stock
   ---------------------------
   ```
- **File:** `Day11_Task2.py`
"""

# Creating the initial grocery stock dictionary
grocery_stock = {
    "bread": 15,
    "milk": 8,
    "eggs": 30,
    "butter": 5
}

# Updating the stock for milk and butter
grocery_stock["milk"] += 10  # Adding 10 more to milk
grocery_stock["butter"] += 5 # Adding 5 more to butter

# Bread is out of stock, removing it from the dictionary
del grocery_stock["bread"]

# Adding a new item cheese with quantity 12
grocery_stock["cheese"] = 12

# Printing the final inventory report
print("--- Final Grocery Stock ---")
for item, quantity in grocery_stock.items():
    print(f"{item}: {quantity} in stock")
print("---------------------------")
