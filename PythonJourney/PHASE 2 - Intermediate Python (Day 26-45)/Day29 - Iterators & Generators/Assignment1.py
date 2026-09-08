"""
### Assignment 1: Custom Iterator

Create a `CountdownIterator` class that counts from a starting number down to `1`.

Requirements:

1. Implement `__iter__()` and `__next__()`.
2. Raise `StopIteration` after returning `1`.
3. Test it with a `for` loop and with manual `next()` calls.

Questions:

- What happens when you call `next()` after the iterator is exhausted?
-> It raises a 'StopIteration' exception, indicating that there are no more items to iterate over

- Why must `__next__()` update the current value?
-> Becuase it would otherwise return the same value repeatedly, preventing the countdown from progressing.
"""

class CountdownIterator:
    def __init__(self, start, stop=1):
        self.current = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

# Testing the CountdownIterator with a for loop
print("Testing CountdownIterator with a for loop:")
for number in CountdownIterator(5):
    print(number)

# Testing the CountdownIterator with manual next() calls
print("\nTesting CountdownIterator with manual next() calls:")
countdown = CountdownIterator(4)
try:
    while True:
        print(next(countdown))
except StopIteration:
    print("Iterator exhausted.")