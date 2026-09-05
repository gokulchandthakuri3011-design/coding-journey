"""
### Easy
3. Write a `Circle` class with a `radius` property and a validating setter (rejects negative values).
"""

class Circle:
    def __init__(self, radius):
        self.radius = radius 

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

# Example usage:
c = Circle(4)
print(c.radius) # Output: 4
c.radius = -5
print(c.radius) # Output: 5