"""
### Easy
1. Write a program that takes a list of numbers and prints the minimum, maximum, and sum.
2. Use `any()` and `all()` to check whether a list contains at least one positive number and whether all numbers are positive.
3. Write a program that uses `enumerate()` to print each item in a list with its index.
"""

# Program that prints min, max and sum 
number_lst = list(map(int, input("Enter the numbers (seperated by space): ").split()))
minimum = min(number_lst)
maximum = max(number_lst)
sum_of_numbers = sum(number_lst)
print(f"The minimum number is: {minimum}")
print(f"The maximum number is: {maximum}")
print(f"The sum of numbers is: {sum_of_numbers}")

# Program using any() & all() to check presence of positive numbers
if_only_one = any(n>0 for n in number_lst)
if_many = all(n>0 for n in number_lst)
print(f"The number list has at least 1 + ve number: {if_only_one}")
print(f"The number list has all positive numbers: {if_many}")

# Using enumerate() 
fruits = ["Apple", "Banana", "Cherry", "Orange", "Gauva"]
print("\n--- Fruits Index List ---")
for i, fruit in enumerate(fruits):
    print(f"{i}. {fruit}")
