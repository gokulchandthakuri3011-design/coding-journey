"""
### Assignment 3: Infinite Stream Generator

Create a generator called `even_numbers()` that produces `2, 4, 6, ...` forever.

Use a loop to print only the first five values. Do not build a list containing infinite values.

Question:

- Why is a `break` necessary when consuming this generator?
"""

# Infinite Stream Generator
class EvenNumbersGenerator:
    def __init__(self, start=2):
        self.start = start
        self.current = start

    def even_numbers(self):
        """Generator that yields even numbers indefinitely."""
        while True:
            yield self.current
            self.current += 2

# Testing the even_numbers generator
print("Testing even_numbers generator:")
generator = EvenNumbersGenerator()
for i, number in enumerate(generator.even_numbers()):
    if i > 5: # Limiting to first 5 even numbers
        break
    print(number)
    
