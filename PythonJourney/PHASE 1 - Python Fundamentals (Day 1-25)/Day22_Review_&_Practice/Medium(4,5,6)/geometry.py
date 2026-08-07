"""
4. Create a two-file project: `geometry.py` (circle area, rectangle area, triangle area) 
   and `main.py` that imports and uses all functions in a menu-driven program.
"""
import math

def circle_area(radius):
    return math.pi * radius * radius

def rectangle_area(length, breadth):
    return length * breadth

def triangle_area(base, height):
    return base * height * 0.5

if __name__ == "__main__":
    radius = 4
    length = 6
    breadth = 3
    base = 5
    height = 4
    print(f"The Area of Circle is: {circle_area(radius):.2f}")
    print(f"The Area of Rectangle is: {rectangle_area(length, breadth):.2f}")
    print(f"The Area of Triangle is: {triangle_area(base, height):.2f}")