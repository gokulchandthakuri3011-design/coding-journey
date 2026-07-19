"""
2. Write a module `temp_converter.py` with functions `celsius_to_fahrenheit(c)`, `fahrenheit_to_celsius(f)`, and `celsius_to_kelvin(c)`.
   Test conversions in a separate script.
"""

def celsius_to_fahrenheit(c):
    return (c * 1.8) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) / 1.8

def celsius_to_kelvin(c):
    return c + 273.15

if __name__ == "__main__":
    print(celsius_to_fahrenheit(37))
    print(fahrenheit_to_celsius(98))
    print(celsius_to_kelvin(0))
    