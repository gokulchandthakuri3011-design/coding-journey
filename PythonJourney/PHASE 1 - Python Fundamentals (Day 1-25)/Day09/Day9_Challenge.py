"""
## 🚀 Challenge: Top 3 Scores

*This challenge combines searching, sorting, and slicing.*

1. Create a list of 10 player scores (you can make them up).
2. Use `.sort()` to sort them in **descending** order (highest first).
3. Slice the sorted list to get the **Top 3** scores.
4. Use a list comprehension to create a new list where each score from the **original** unsorted list is **doubled**.
5. Print the Top 3 scores and the doubled scores list.
- **File:** `Day9_Challenge.py`
"""

# Creating a list of 10 players
scores = [89,67,98,100,95,69,80,75,55,40]
original_scores = scores.copy()

# Sorting them in descending order
scores.sort(reverse=True)

# Getting top 3 scores
top_3_scores = scores[0:3]

# Creating a new list using list comprehension
doubled_scores = [score * 2 for score in original_scores]

# Printing our lists
print("\n --- Top 3 Scores ---\n")
print(f"The Original Scores List: {original_scores}")
print(f"Sorted Scores List: {scores}")
print(f"Top 3 Scores: {top_3_scores}")
print(f"Doubled Scored List: {doubled_scores}")