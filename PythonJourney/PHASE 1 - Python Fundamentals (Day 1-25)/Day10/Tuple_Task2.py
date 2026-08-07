"""
### Assignment 2: The Immutable Menu

*Practice tuple creation and errors.*

1. Create a tuple `menu` with the following breakfast items: `"pancakes"`, `"waffles"`, `"omelette"`, `"cereal"`, `"fruit bowl"`.
2. Print the menu.
3. Print the first and last item using positive and negative indexing.
4. Print the number of items on the menu using `len()`.
5. Check if `"coffee"` is on the menu and print the result.
6. Try to change the second item to `"french toast"` using assignment. Wrap it in a `try/except` block so the program doesn't crash.
7. Print `"Tuples are immutable!"` in the `except` block.
- **File:** `Day10_Task2.py`
"""
# 1. Creating the tuple 'menu'.
menu = ("pancakes", "waffles", "omelette", "cereal", "fruit bowl")

# 2. Printing the menu.
print(menu)

# 3. Printing 1st & last items
print(menu[0]) # First item using +ve indexing
print(menu[-1]) # Last item using -ve indexing

# 4. Printing the number of items on the menu.
print(len(menu))

# 5. Checking if "coffee" is on the menu.
print("coffee" in menu)

# 6. Trying to change the second item to "french toast".
try:    # This will raise a TypeError since tuples are immutable.
    menu[1] = "french toast"  
except TypeError:    # Python jumps to this block when it encounters the error.
    # 7. Printing "Tuples are immutable!" in the except block.
    print("Tuples are immutable!")    # This message will be printed instead of crashing the program.
