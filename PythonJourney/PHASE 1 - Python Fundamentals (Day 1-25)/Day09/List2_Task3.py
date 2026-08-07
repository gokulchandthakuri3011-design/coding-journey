"""
### Assignment 3: List Comprehension Magic
*Practice writing list comprehensions.*

1. Create a list of numbers from `1` to `20` using `range()`.
2. Use a list comprehension to create a new list containing only the **odd** numbers.
3. Use a list comprehension to create a list of the **squares** of numbers from `1` to `10`.
4. Given this list of words: `words = ["python", "is", "awesome", "and", "fun"]`, use a list comprehension to create a new list containing only the words that have **more than 3 letters**.
5. Print all three new lists.
- **File:** `Day9_Task3.py`
"""

# Creating a list of numbers 1-20
numbers = list(range(1, 21))

# Odd numbers list
odd_num = [num for num in numbers if num % 2 != 0]

# Squares of numbers 1-10
square_num = [num ** 2 for num in range(1, 11)]

# List with only words with more than 3 letters
words = ["python", "is", "awesome", "and", "fun"]
new_words = [word for word in words if len(word) > 3]

# Printing all new lists
print(f"List of numbers (1-20): {numbers}")
print(f"Odd Numbers list (1-20): {odd_num}")
print(f"List of squares of numbers (1-10): {square_num}")
print(f"List of words containing more than 3 letters: {new_words}")