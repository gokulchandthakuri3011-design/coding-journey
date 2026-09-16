"""
### Assignment 5: Memory Comparison

Create a list comprehension and a generator expression that both produce the squares from `1` to `1,000,000`.

Questions:

- Which one stores all values immediately?
-> The list comprehension stores all values immediately in memory.

- Which one is better when you only need to calculate the total once?
-> the generator expression is better because it calculates values lazily and saves memory. The list comprehension is better only when you need all values stored and reused.

- Use `sys.getsizeof()` to compare the objects and explain the result.
"""

# Memory Comparison Assignment

# List comprehension that produces squares from 1 to 1,000,000
squares_list = [x**2 for x in range(1,1000001)]
print(sum(squares_list))  # Calculate the total of squares using list comprehension

# Generator expression that produces squares from 1 to 1,000,000
squares_generator = (x**2 for x in range(1,1000001))
print(sum(squares_generator))  # Calculate the total of squares using generator expression

# Using sys.getsizeof() to compare the memory size of the list and generator objects
import sys

print("Memory size of list comprehension:", sys.getsizeof(squares_list))
print("Memory size of generator expression:", sys.getsizeof(squares_generator))