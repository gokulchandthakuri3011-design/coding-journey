"""
### Assignment 2: Common Elements & Set Operations
*Practice converting lists to sets and applying set operations.*

You are given two lists representing subscriber emails for two different company newsletters:
```python
newsletter_a = ["dan@example.com", "alice@example.com", "emma@example.com", "bob@example.com", "charlie@example.com"]
newsletter_b = ["sophia@example.com", "bob@example.com", "liam@example.com", "emma@example.com", "olivia@example.com"]
```

Write a program that:
1. Converts both lists into sets.
2. Finds and prints the emails of subscribers who are subscribed to **both** newsletters. (Intersection)
3. Finds and prints the subscribers who are subscribed to **only** Newsletter A but not Newsletter B. (Difference)
4. Finds and prints the subscribers who are subscribed to **only one** of the newsletters, but not both. (Symmetric Difference)
5. Finds and prints the total number of unique subscribers across both newsletters. (Union)
- **File:** `Day12_Task2.py
"""

print("\n     Common Elements & Set Operations     ")

# Given lists of subscriber emails
newsletter_a = ["dan@example.com", "alice@example.com", "emma@example.com", "bob@example.com", "charlie@example.com"]
newsletter_b = ["sophia@example.com", "bob@example.com", "liam@example.com", "emma@example.com", "olivia@example.com"]

# Converting lists to sets
set_a = set(newsletter_a)
set_b = set(newsletter_b)

# Subscribers of both newsletters (Intersection)
intersection = set_a & set_b
print(f"Subscribers in both newsletters: {intersection}")

# Subscribers only in Newsletter A (Difference)
difference_a = set_a - set_b
print(f"Subscribers only in Newsletter A: {difference_a}")

# Subscribers to only one newsletter (Symmetric Difference)
symmetric_difference = set_a ^ set_b
print(f"Subscribers to only one newsletter: {symmetric_difference}")

# Total unique subscribers (Union)
union = set_a | set_b
print(f"Total unique subscribers across both newsletters: {len(union)}")
