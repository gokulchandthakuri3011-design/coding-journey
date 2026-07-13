"""
Write a program that uses a for loop and range().
- Print numbers from 1 to 10.
- Skip multiples of 3 using continue.
- Stop the loop early when a number reaches 8 using break.
"""


# Loop through numbers from 1 to 10
for numbers in range(1, 11):
    # Skip multiples of 3
    if numbers % 3 == 0:
        continue
    # Stop the loop if the number reaches 8
    if numbers == 8:
        break
    # Print the current number
    print(numbers)


