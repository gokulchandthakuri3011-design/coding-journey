"""
### Challenge: Grade Checker
Write a program that asks for a test score from `0` to `100` and prints one of these messages:
- `Excellent` for `90` or above
- `Good` for `70` to `89`
- `Needs improvement` for `50` to `69`
- `Failing` for below `50`
Use comparison operators and `if` / `elif` / `else` statements.
"""

# Day 3 Challenge: Grade Checker

# Ask user for test score
score_input = input("Enter your test score (0 - 100): ")
score = float(score_input)

# Check grade using comparison and conditional statements
print("\n----- Score Evaluation -----")
if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Good")
elif score >= 50:
    print("Needs improvement")
else:
    print("Failing")
print("----------------------------")
