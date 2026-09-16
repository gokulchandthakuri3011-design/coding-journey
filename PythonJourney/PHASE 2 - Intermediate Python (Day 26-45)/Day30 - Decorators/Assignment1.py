"""
### Assignment 1: Execution Time Logger

Create a decorator named `log_execution_time`.

Requirements:

1. Use `time.perf_counter()` to record the start and end times.
2. Print the decorated function's name and execution time.
3. Support positional and keyword arguments.
4. Return the original function's result.
5. Use `functools.wraps`.
6. Test it with a function that calculates the sum of squares from `1` to a given limit.

Questions:

- Why should the timer surround the call to the original function?
-> To accurately measure the execution time of the original function
- What problem does `@wraps` solve?
-> Preserves the Original function's Metadata (like name, docstring) when it is decorated.
- Why are `*args` and `**kwargs` useful here?
-> They allow the decorator to accept any number of positional and keyword arguments, making it flexible to decorate functions with different signatures.
"""

from functools import wraps
from time import perf_counter


# Defining the decorator function
def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = perf_counter() # Record the start time
        result = func(*args, **kwargs) # Call the original function
        end_time = perf_counter() # Record the end time
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.6f} seconds")
        return result # Return the original function's result
    return wrapper

# TEsting the decorator with a function that calculates the sum of squares from 1 to a given limit
@log_execution_time
def sum_of_squares(limit):
    return sum(i ** 2 for i in range(1, limit + 1))

# Example usage
if __name__ == "__main__":
    limit = 10000
    result = sum_of_squares(limit)
    print(f"Sum of squares from 1 to {limit} is: {result}")
