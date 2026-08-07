"""
5. **Sort by last letter:** Given `["apple", "banana", "cherry", "date"]`, sort them by their **last** character using a lambda key.

6. **Celsius to Fahrenheit:** Use `map` and a lambda to convert `[0, 10, 20, 30, 40]` Celsius to Fahrenheit (`C * 9/5 + 32`).

7. **Recursive sum:** Write a recursive function `sum_to(n)` that returns the sum of 1 to n (no loops allowed).

8. **Custom higher-order:** Write a function `repeat(n, func, value)` that calls `func` on `value`, `n` times. Example: `repeat(3, lambda x: x * 2, 1)` should return `8` (double 1 → 2 → 4 → 8).

9. **Filter words by length:** Use `filter` and a lambda to keep only words longer than 4 characters from `["hi", "hello", "hey", "world", "go"]`.
"""

# Sorting by last letter
fruits = ["apple", "banana", "cherry", "date"]
fruits.sort(key = lambda fruit: fruit[-1]) 
print(f"Sorted by last letter: {fruits}")

# Celsius to Fahrenheit conversion
temperatures_celsius = [0, 10, 20, 30, 40]
temperature_fahrenheit = list(map(lambda c: c*9/5 + 32, temperatures_celsius))
print(f"Celsius to Fahrenheit: {temperature_fahrenheit}")

# Recursive sum function
def recursive_sum(n):
    if n <= 1:
        return n
    return n + recursive_sum(n-1)
n = int(input("Enter a number to calculate the sum from 1 to n: "))
print(f" Sum from 1 to {n}: {recursive_sum(n)}")

# Custom higher-order function
def repeat(n, func, value):
    result = value
    for _ in range(n):
        result = func(result)
    return result
n = int(input("Enter how many times to call the function {func}: "))
func = lambda x: x *2
value = int(input("Enter the number which you wanna use as arg in {func}: "))
print(repeat(n, func, value))

# Filtering words by length
words = ["hi", "hello", "hey", "world", "go"]
filtered_lst = list(filter(lambda word: len(word) > 4, words))
print(f"Words longer than 4 char: {filtered_lst}")