"""
### Assignment 2: Number Finder
Write a program that extracts all numbers from a sentence.

Example:

```python
text = "I have 3 apples, 12 oranges, and 9 bananas."
```

Questions:
- Which regex pattern would extract only numeric values?
- Why is `findall()` useful here?
"""
import re

def number_extractor(text, pattern):
    number_list = re.findall(pattern, text)
    if number_list:
        print(f"Numbers: {number_list}")
    else:
        print("There are no numbers in given text.")

def main():
    text = input("Enter a text with or without numerical values: ")
    pattern = r"\d+"
    print("-- Checking the Numbers Availability --\n")
    number_extractor(text, pattern)

if __name__ == "__main__":
    print("-- Number Finder --\n")
    main()