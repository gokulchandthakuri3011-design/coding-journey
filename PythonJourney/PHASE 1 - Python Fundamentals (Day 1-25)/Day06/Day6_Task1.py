"""
Write a program that keeps asking the user for numbers until they type done.
- Use a while loop.
- Use continue to skip empty input.
- Use break to stop when the user types done.
- Print the total sum and count of valid numbers.
"""

# Initializing variables 
total_sum = 0.0
count = 0

# Loop to get user input
while True:
    user_input = input("Enter a number (or type 'done' to finish): ")

    # Check for 'done' to break the loop
    if user_input.lower() == 'done':
        break

    # Check for empty input
    if user_input.strip() == '':
        print("Empty input, please enter a valid number.")
        continue

    # Try to convert input to a float and update total sum and count
    number = float(user_input)
    total_sum += number
    count += 1

# Print the total sum and count of valid numbers
print(f"Total sum: {total_sum}")
print(f"Count of valid numbers: {count}")    



