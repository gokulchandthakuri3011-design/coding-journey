"""
10. **Recursive palindrome checker:** Write `is_palindrome(s)` that returns `True` if `s` reads the same forwards and backwards, 
      using recursion (no loops, no `s[::-1]`).
    - **Hint:** Compare first and last characters. If they match, recurse on the middle substring.
"""
def is_palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])

word = input("Enter a word for Palindrome check: ")
print(f"Is {word} Palindrome?: {is_palindrome(word)}")


"""
11. **Pipeline:** Write a function `pipeline(*funcs)` that takes any number of functions and returns a new function that chains them.
    ```python
    add_one = lambda x: x + 1
    double  = lambda x: x * 2
    square  = lambda x: x ** 2

    f = pipeline(add_one, double, square)
    print(f(3))  # ((3+1)*2)^2 = 64
"""
def pipeline(*funcs):
    def inner(x):
        result = x
        for func in funcs:
            result = func(result)
        return result
    return inner

add_one = lambda x: x + 1
double = lambda x: x * 2
square = lambda x: x ** 2
funcs = pipeline(add_one, double, square)
print(funcs(2)) 


"""
12. **Recursive list reversal:** Write `reverse_list(lst)` that returns a reversed copy of a list using recursion (no `lst[::-1]` or `list.reverse()`).
    - **Hint:** Base case: empty list or single element. Recursive case: last element + reverse of the rest.
"""