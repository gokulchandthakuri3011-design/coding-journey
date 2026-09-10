"""
### Assignment 4: Custom Range-Like Class

Build a `SimpleRange` class that accepts `start`, `stop`, and an optional `step`.

Requirements:

1. Make it work in a `for` loop.
2. Stop before reaching `stop`, like Python's `range()`.
3. Support positive steps first, then add negative-step support.
4. Test an empty range and a step larger than the range.

Questions:

- What should happen when `step` is `0`?
- Should `SimpleRange` be its own iterator or return a new iterator each time? Explain your choice.
"""
class SimpleRange:

    def __init__(self, start, stop, step):
        self.start = start 
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.step == 0:
            raise ValueError("Step cannot be zero.")
        if (self.step > 0 and self.current >= self.stop) or (self.step < 0 and self.current <= self.stop):
            raise StopIteration
        value = self.current
        self.current += self.step
        return value

# Testing the SimpleRange Class
print("Testing SimpleRange with positive step:")
for number in SimpleRange(1, 10, 2):
    print(number)