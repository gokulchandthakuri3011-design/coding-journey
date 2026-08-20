"""
## 6. Mini Project Idea
Build a simple “Student Score Analyzer” that:
- takes a list of scores
- calculates the average
- finds the highest and lowest score
- prints whether the class passed overall
"""
# Average Score Calculator
def average_calculator(scores):
    average = sum(scores)/len(scores)
    return average

# Highest and lowest scores finder
def high_low_scores(scores):
    highest = max(scores)
    lowest = min(scores)
    return highest, lowest

# Checks wether class passed or not
def class_pass_checker(average):
    if average >= 60:
        return f"In overall Class passed."
    else:
        return f"In overall Class didn't passed!"

# Main class to take input and call function respectively
def main():
    print("\n --- Student Score Analyzer --- \n")
    scores = list(map(int, input("Enter scores seperated by space: ").split())) #split() breaks input by spaces, and map converts each into integer before wrapping in list()
    print()

    # Calling Average Calculator
    average = average_calculator(scores)
    print(f"The Average Score of class is: {average}")
    print()

    # Calling highest and lowest score calculator
    highest, lowest = high_low_scores(scores)
    print(f"The Highest score is: {highest}")
    print(f"The lowest score is: {lowest}")
    print()

    # Calling wether class passed or not checker
    result = class_pass_checker(average)
    print(f"With the {average} {result}")
    print()

    print("---------------------------")

if __name__ == "__main__":
    main()