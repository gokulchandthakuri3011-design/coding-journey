"""
### Easy

1. **Lambda basics:** Write a lambda that returns the cube of a number. Use it with `map` to cube `[1, 2, 3, 4, 5]`.

2. **Filter evens:** Use `filter` and a lambda to get only even numbers from `[10, 15, 20, 25, 30]`.

3. **Reduce to product:** Use `reduce` to find the product of `[1, 2, 3, 4, 5]`.

4. **Function as object:** Assign `str.upper` to a variable called `to_upper`, then call it with `"hello"`.
"""

# Lambda returning cube of a number using 'map'
numbers = [1, 2, 3, 4, 5]
cubed_numbers = list(map(lambda x: x ** 3, numbers))
print(f"Cubed numbers: {cubed_numbers}")

# Filter even numbers using 'filter' and a lambda
numbers_to_filter = [10, 15, 20, 25, 30, 35, 3, 4, 9, 40]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers_to_filter))
print(f"Even numbers: {even_numbers}")

# Reduce to product using 'reduce'
# Importing reduce from functools
from functools import reduce
numbers_to_reduce = [1, 2, 3, 4, 5]
product = reduce(lambda a, b: a * b, numbers_to_reduce)
print(f"Product of numbers: {product}")

# Function as object: Assigning str.upper to a variable and calling it
to_upper = str.upper
result = to_upper("hello")
print(f"Uppercase result: {result}")
