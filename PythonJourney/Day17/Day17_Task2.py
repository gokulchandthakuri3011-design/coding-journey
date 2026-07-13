"""
### Medium
4. Write a function `min_max(numbers)` that returns both the minimum and maximum of a list. Use tuple unpacking to capture both values.
5. Write a function `swap(a, b)` that returns the values swapped. Test: `b, a = swap(1, 2)`.
6. Write a function `count_vowels(text)` that returns the number of vowels in the string.
"""

def min_max(numbers):
    """Returns the minimum and maximum of a list."""
    min_val = numbers[0]
    max_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
        else:
            max_val = num
    return min_val, max_val

def swap(a, b):
    """Returns the values swapped."""
    a, b = b, a
    return a, b

def count_vowels(text):
    """Returns the number of vowels in the string."""
    vowels = 'aeiouAEIOU'
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Test cases
if __name__ == "__main__":
    # Test min_max function
    numbers = [3, 1, 4, 1, 5, 6, 2, 0, 9]
    minimum, maximum = min_max(numbers) # Tuple unpacking
    print(f"Minimum: {minimum}, Maximum: {maximum}")

    # Test swap function
    a, b = "Gokul", "Chand"
    x, y = swap(a, b) # Tuple unpacking
    print(f"Swapped values: a = {x}, b = {y}")

    # Test count_vowels function
    text = "Hallo, wie geht's dir?"
    print(f"Number of vowels in '{text}': {count_vowels(text)}")