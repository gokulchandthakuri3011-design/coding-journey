"""
3. Write a module `string_utils.py` with `reverse_string(s)`, `is_palindrome(s)`, and `count_vowels(s)`.
"""
def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return f"{s} is {'not ' if s.lower() != reverse_string(s.lower()) else ''}a palindrome."

def count_vowels(s):
    vowels = ('a', 'e', 'i', 'o', 'u')
    return sum(1 for char in s.lower() if char in vowels)

if __name__ == "__main__":
    print(reverse_string("Nickikcin"))
    print(is_palindrome("Nickikcin"))
    print(count_vowels("ArunGiri"))