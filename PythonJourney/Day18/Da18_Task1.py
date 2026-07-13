"""
4. Write a function `make_counter()` that returns a closure. Each call to the returned function should increment and return a counter starting from 0.

```python
counter = make_counter()
print(counter())  # 0
print(counter())  # 1
print(counter())  # 2
"""
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count - 1
    return counter          # No () → returns the function itself (the closure)
    # If we wrote return counter() → it calls the function now and returns
    # the integer result (0), not the function. That would make make_counter()
    # return an int instead of a callable, causing "'int' object is not callable"

# NOTES: function name with vs without parentheses
# -----------------------------------------------
# counter   = the function itself (a callable object)
# counter() = CALL the function now, get its return value
#
# Example:
#   count = make_counter()    # count gets the inner function (callable)
#   print(count())            # calls that function → 0
#   print(count)              # prints the function object itself, not 0

count = make_counter()          # count holds the inner function (callable)
print(count())   # 0  → calls count, returns 0
print(count())   # 1  → calls count again, returns 1
print(count())   # 2  → calls count again, returns 2