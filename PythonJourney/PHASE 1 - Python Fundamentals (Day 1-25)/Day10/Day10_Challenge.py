"""
## Challenge: Zip It, Unpack It

*Combine tuples, `zip()`, and unpacking.*

1. Create two lists:
   ```python
   students = ["Alice", "Bob", "Charlie", "Diana"]
   scores = [88, 92, 79, 95]
   ```
2. Use `zip()` to pair them into a list of tuples.
3. Print the zipped list.
4. Sort the list of tuples by score (descending). *Hint: use `sorted()` with a `key` function, or a lambda.*
5. Unpack the top scorer into `top_student, top_score` and print the winner.
- **File:** `Day10_Challenge.py`
"""
# Creating 2 lists:
students = ["Alice", "Bob", "Charlie", "Diana"]
scores = [88, 92, 79, 95]

# Using zip() to pair them into a list of tuples
students_scores = list(zip(students, scores))
print(students_scores)

# Sorting the new list of tuples in descending order 
sorted_by_score = sorted(students_scores, key=lambda pair: pair[1], reverse=True)
print("\n --- Sorted List --- ")
print(f"{sorted_by_score}")

# Unpacking top_scorer and top_score
top_scorer, top_score = sorted_by_score[0]
print(f"Top scorer: {top_scorer}")
print(f"Top Score: {top_score}")