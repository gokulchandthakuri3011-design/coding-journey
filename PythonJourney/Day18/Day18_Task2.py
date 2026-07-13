"""
### Hard
6. Write a function `make_multiplier(factor)` that
   returns a closure which multiplies any given number by `factor`.
   Then create `double` and `triple` from it and demonstrate they work independently.
"""
def make_multiplier(factor):
    # Return a closure that multiplies a number by the given factor
    def multiplier(number):
        return number * factor
    return multiplier

# Create double and triple functions using the closure
double = make_multiplier(2) # Here, we are creating a closure that multiplies by 2
triple = make_multiplier(3)

# Demonstrate that double and triple work independently by calling double and triple with different numbers
print(double(5))
print(triple(5))

# Note: Insted of creating a closure
# print(make_multiplier(2)(5)) # This will print 10 but we are not creating a closure here, we are just calling the function directly with the argument 5.