"""
### Assignment 2: Slicing Practice
1. Create a list of numbers from 1 to 10: `numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
2. Slice the list to print the first 5 numbers.
3. Slice the list to print the last 3 numbers.
4. Slice the list to print the numbers `[4, 5, 6, 7]`.
"""
# Step 1: Creating the list of numbers from 1 to 10
numbers = [1,2,3,4,5,6,7,8,9,10]

# Step 2: Slicing the list to print the first 5 numbers
first_five = numbers[:5]
print("First 5 numbers: ", first_five)

# Step 3: Slicing the list to print the last 3 numbers
last_three = numbers[-3:]
print(f"Last 3 numbers: {last_three}")

# Step 4: Slicing the list to print the numbers [4,5,6,7]
middle_numbers = numbers[3:7]
print(f"Middle numbers: {middle_numbers}")
