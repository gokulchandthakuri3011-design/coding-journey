"""
### Assignment 1: Refined Word Frequency Counter
*Practice using `collections.Counter` to perform text analysis.*

1. Prompt the user or declare a paragraph of text:
   `text = "Python is an amazing programming language. Python is simple to learn and extremely readable. Learning Python opens up many doors in software engineering."`
2. Process the string:
   - Convert all words to lowercase.
   - Remove punctuation marks like periods `.`. (Hint: Use `text.replace(".", "")`).
   - Split the cleaned string into a list of words using `.split()`.
3. Create a `Counter` object from the word list to count frequencies.
4. Print the raw frequencies dictionary.
5. Print the **top 3 most common words** and their count using the `.most_common()` method in a clean format:
   ```text
   --- Top 3 Most Common Words ---
   1. word_a: count_a times
   2. word_b: count_b times
   3. word_c: count_c times
   ```
- **File:** `Day12_Task1.py`
"""

print("     Refined Word Frequency Counter     ")

from collections import Counter

# Declaring the paragraph of text
text = "Python is an amazing programming languag. Python is simple to learn and extremely readable. Learning Python opens up many doors in software engineering."

# Processing the string
cleaned_text = text.replace(".", "").lower().split() # Removed periods, converted to lowercase, and split into words

# Creating a Counter object to count frequencies
word_count = Counter(cleaned_text)

# Printing the raw frequencies dictionary
print("\n--- Raw Frequencies Dictionary ---")
print(word_count)

# Printing the top 3 most common words and their count
print("\n--- Top 3 Most Common Words ---")
for i, (word, count) in enumerate(word_count.most_common(3), start = 1): # Using enumerate to get the index for formatting
    print(f"{i}. {word}: {count} times")

