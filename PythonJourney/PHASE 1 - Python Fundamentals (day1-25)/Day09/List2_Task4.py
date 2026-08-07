"""
### Assignment 4: Shopping Cart System
*Combine multiple list skills in a real-world scenario.*

Build a simple shopping cart program:

1. Create an empty list called `cart`.
2. Create a list of available items with their prices as tuples: 
   ```python
   shop = [("Apple", 0.99), ("Milk", 1.49), ("Bread", 2.50), ("Eggs", 3.99), ("Butter", 4.50)]
   ```
3. Display the available items to the user (numbered list).
4. Ask the user to enter item names to add to the cart (one at a time).
5. Keep a loop running until the user types `"done"`.
6. If the item is found in `shop`, add its name to `cart` and confirm.
7. If the item is not found, print `"Item not available."`.
8. When done, print the final `cart` list and the total number of items in it.
- **File:** `Day9_Task4.py`
"""

print("\n--- Welcome To The Shopping Cart System ---\n")

# Creating an empty list 'cart' holds user selected items
cart = []

# Creating a list of available items with their prices as tuples
shop = [("Apple", 0.99), ("Milk", 1.49), ("Bread", 2.50), ("Eggs", 3.99), ("Butter", 4.50)]

# Displaying the availabe items with thier price to the user
print("\n-- Available Items --\n")
for i, items in enumerate(shop, start=1):
    print(f"{i}. {items[0]} --> ${items[1]:.2f}")

# Loop to taje user input until they enter 'done'
while True:
    choice = input("\nEnter the item name to add to your cart (or type 'done' to finish): ").strip()
    if choice.lower() == "done":
        break

    found = False
    for items in shop:
        if choice.lower() == items[0].lower():
            cart.append(items[0])
            print(f"{items[0]} added to your cart.")
            found = True
            break

    if not found:
        print("Item not available.")

# Displaying the final cart and total number of items
print("\n--- Your Shopping Cart ---\n")
if cart:
    for i, item in enumerate(cart, start=1):
        print(f"{i}. {item}")
    print(f"\nTotal number of items in your cart: {len(cart)}")