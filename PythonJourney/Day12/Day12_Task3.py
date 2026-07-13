"""
### Assignment 3: List Duplicate Remover
*Practice using sets to remove duplicates and analyze performance/ordering.*

1. Create a list with several duplicates: `numbers = [5, 2, 8, 2, 9, 5, 1, 8, 10, 2]`
2. **Method 1 (Unordered):**
   - Convert `numbers` to a set, then convert it back to a list.
   - Print the resulting list and observe its order compared to the original.
3. **Method 2 (Order-Preserving):**
   - Implement an order-preserving duplicate remover.
   - Create an empty set called `seen` and an empty list called `unique_numbers`.
   - Loop through the original `numbers` list. If a number is not in `seen`, add it to `seen` and append it to `unique_numbers`.
   - Print the final `unique_numbers` list and verify that the original order is preserved.
4. Add a print statement explaining why looking up elements in a set (`number not in seen`) is extremely efficient compared to looking up elements in a list.
- **File:** `Day12_Task3.py`
"""
# List Duplicate Remover

# Creating a list with several duplicates
numbers = [5, 2, 8, 2, 9, 5, 1, 8, 10, 2]

# Method 1 (Unordered)
unique_numbers_unordered = list(set(numbers)) # Convert to set and back to list
print("Unique numbers (unordered):", unique_numbers_unordered)

# method 2 (Order-Preserving)
seen = set() # Create an empty set to track seen numbers
unique_numbers_ordered = [] # Create an empty list to store unique numbers in order

# Loopthorugh the original numbers list
for number in numbers:
    if number not in seen: # Check if the number has not been seen before
        seen.add(number) # Add the number to the seeen set
        unique_numbers_ordered.append(number) # Append the number to the unique_numbers_ordered list

# Print the final unique_numbers_ordered list
print(f"Unique numbers (order-preserving): {unique_numbers_ordered}")

# Explanation of efficiency
print("Looking up elements in a set is extremely efficient because sets are implemented as hash tables")

