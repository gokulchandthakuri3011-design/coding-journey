"""
### Assignment 1: Favorite Number Calculator
1. Ask the user for their favorite number using `input()`.
2. Convert that input into an integer.
3. Add `10` to that number and print the result.
4. Use an f-string to show the original number and the new number.

Example output:
```
Your favorite number is 7.
Ten more than that is 17.
"""
print("\n --- Favourite Number Calculator --- \n")

# Asking user for their favourite number
fav_num = int(input("Enter your favourite number: "))
print(f"User Favourite Number is: {fav_num}")
fav_num += 10
print(f"User Favourite Number after adding 10 is: {fav_num}")
