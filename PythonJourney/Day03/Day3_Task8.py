"""
### Assignment 4: Weather Advice
1. Ask the user for the current temperature.
2. Convert it to an integer.
3. Use `and`, `or`, and `not` to print advice:
   - If the temperature is below `0`, print `It is freezing!`
   - If the temperature is `20` or above, print `It is warm today.`
   - Otherwise, print `The weather is normal.`
"""

# Day 3: Weather Advice

# 1. Ask for temperature & 2. Convert to integer
temp_input = input("Enter current temperature in Celsius: ")
temp = int(temp_input)

print("\n----- Weather Forecast & Advice -----")
print(f"Current Temperature: {temp}°C")

# 3. Using boolean conditions for advice
if temp < 0:
    print("It is freezing!")
elif temp >= 20:
    print("It is warm today.")
else:
    # This matches when temp is between 0 (inclusive) and 20 (exclusive)
    print("The weather is normal.")

# Demonstrating combined logic using 'not' or 'and' / 'or'
is_extreme = temp < 0 or temp > 35
if not is_extreme:
    print("Weather is safe for outdoor activities.")
else:
    print("Warning: Extreme temperature detected!")
print("-------------------------------------")
