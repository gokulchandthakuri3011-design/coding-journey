"""
### Assignment 2: Generator Function

Write a `fibonacci_generator(limit)` function that yields the first `limit` Fibonacci numbers.

Questions:

- Where does the generator pause?
- How much code would be needed to return the same values in a list?
- What happens when `limit` is `0`?
"""

class FibonacciGenerator:
    def __init__(self, limit):
        self.limit = limit
        self.a , self.b = 0, 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        value = self.a
        self.a , self.b = self.b, self.a + self.b
        self.count += 1
        return value

# Testing the FibonacciGenerator with a for loop
for number in FibonacciGenerator(10):
    print(number)

# Testing using manual next() calls
fib_gen = FibonacciGenerator(5)
try:
    while True:
        print(next(fib_gen))
except StopIteration:
    print("Generator exhausted.")