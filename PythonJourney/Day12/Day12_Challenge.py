"""
## ⚡ Challenge: Inventory Merger
*Combine advanced dictionaries and default values to merge datasets.*

You are managing inventory for two branches of a retail store. The branch inventory data is stored in two dictionaries:
```python
branch_1 = {"laptop": 5, "keyboard": 10, "mouse": 15, "monitor": 7}
branch_2 = {"keyboard": 8, "mouse": 12, "headset": 10, "printer": 4}
```

Write a program that merges these two inventories.
1. Use `collections.defaultdict` with standard integers, or use a standard dictionary with a smart loop (or the `.get()` method), to combine all stock levels.
2. If an item exists in both branches, their quantities should be **added together**.
3. If an item exists in only one branch, it should be added with its current quantity.
4. Print a clean report of the combined inventory sorted alphabetically by product name.
   ```text
   --- Combined Store In
   ```
- **File:** `Day12_Challenge.py`
"""

from collections import defaultdict

# 2 Dictionaries are
branch_1 = {"laptop" : 5, "keyboard" : 10, "mouse" : 15, "monitor" : 7}
branch_2 = {"keyboard" : 8, "mouse" : 12, "headset" : 10, "printer" : 4}

# Combining items from both dictionaries using defaultdict
combined_inventory = defaultdict(int)  # int is called to provide default value 0 for missing keys
for item, quantity in branch_1.items():
    combined_inventory[item] += quantity

for item, quantity in branch_2.items():
    combined_inventory[item] += quantity

# Sorting the combined inventory by key name
sorted_inventory = dict(sorted(combined_inventory.items()))

# Printing the sorted inventorry
print("--- Combined Store Inventory ---")
for item, quantity in sorted_inventory.items():
    print(f"{item} : {quantity}")
