"""
## Practice questions
1. Write a function `square(number)` that returns the square of its input.
2. Create `is_even(number)` that returns `True` if the number is even and `False` otherwise.
3. Build `area_rectangle(width, height)` to compute the area of a rectangle.
4. Define `full_name(first, last)` that returns the full name in one string.
5. Write `convert_to_celsius(fahrenheit)` and `convert_to_fahrenheit(celsius)`.
6. Create `greet_user(name, age)` to print a greeting message.
7. Make a function `average(numbers)` that returns the average of a list of numbers.
8. Write a function `count_vowels(text)` that counts vowel letters in a string.
9. Build `get_larger(a, b)` that returns the larger of two values.
10. Create `print_menu()` that prints a simple program menu and does not return a value.
"""


def square(number):
    return number ** 2

def is_even(number):
    return number % 2 == 0

def area_rectangle(width, height):
    return width * height

def full_name(first, last):
    return f"{first} {last}"

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def convert_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def greet_user(name, age):
    print(f"Hello {name}, you are {age} years old!")

def average(numbers):
    return sum(numbers) / len(numbers)

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def get_larger(a, b):
    return a if a > b else b

def print_menu():
    print("===== MENU =====")
    print("1. Option One")
    print("2. Option Two")
    print("3. Exit")
    print("================")

if __name__ == "__main__":
    print(square(4))
    print(is_even(7))
    print(area_rectangle(5, 3))
    print(full_name("John", "Doe"))
    print(convert_to_celsius(100))
    print(convert_to_fahrenheit(37))
    greet_user("Alice", 25)
    print(average([10, 20, 30, 40]))
    print(count_vowels("Hello World"))
    print(get_larger(15, 8))
    print_menu()
