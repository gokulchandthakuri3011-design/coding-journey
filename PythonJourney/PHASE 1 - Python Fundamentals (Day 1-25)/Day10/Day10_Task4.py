"""
### Assignment 4: Inventory Tracker

*Practice tuples + lists working together.*

You manage a small warehouse. Each item is stored as a tuple: `(item_id, name, quantity, price)`.

1. Create an inventory list with at least 5 items (e.g., `(101, "Widget", 50, 0.99)`).
2. Write a function `total_value(inventory)` that loops through the inventory and returns the total value (sum of quantity * price for each item).
3. Write a function `find_item(inventory, item_id)` that searches by ID and returns the item tuple, or `None` if not found.
4. Write a function `restock(inventory, item_id, amount)` that returns a **new list** with the quantity of the given item updated (remember — tuples are immutable, so you need to create a new tuple).
5. Test all three functions and print the results.
- **File:** `Day10_Task4.py`
"""
from collections import namedtuple

item = namedtuple('Item', ['item_id', 'name', 'quantity', 'price'])
item1 = item(101, "Widget", 50, 0.99)
item2 = item(102, "Gadget", 30, 1.49)
item3 = item(103, "Medicine", 20, 2.99)
item4 = item(104, "Tool", 15, 5.99)
item5 = item(105, "Accessory", 100, 0.49)

# Creating an inventory list with 5 items
inventory = [item1, item2, item3, item4, item5]

# Function to return the total value of the inventory
def total_value(inventory):
    total = 0
    for item in inventory:
        total += item.quantity * item.price
    return total

# Function to find an item by its ID
def find_item(inventory, item_id):
    for item in inventory:
        if item.item_id == item_id:
            return item
    return None

# function to restock an item by its ID and return a new inventory list
def restock(inventory, item_id, amount):
    new_inventory = []
    for item in inventory:
        if item.item_id == item_id:
            # Create a new tuple with updated quantity
            updated_item = item._replace(quantity=item.quantity + amount)
            new_inventory.append(updated_item)
        else:
            new_inventory.append(item)
    return new_inventory

# Testing the functions
def main():
    print(f"\nInventory: {inventory}")
    item_id = int(input("Enter item ID to find: "))
    amount = int(input("Enter amount to restock: "))
    print(f"\nTotal inventory value: ${total_value(inventory):.2f}")
    found_item = find_item(inventory, item_id)
    if found_item:
        print(f"\nFound item: {found_item}")
    else:
        print(f"\nItem not found. Please check the ID and try again.")
    print(f"\n--- Restocking an item ---")
    new_inventory = restock(inventory, item_id, amount)
    print(f"\nNew inventory after restocking: {new_inventory}")

if __name__ == "__main__":
    main()
