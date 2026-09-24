"""
### Assignment 1: Word Frequency Counter

1. Create a sentence.
2. Use `Counter` to count how many times each word appears.
3. Print the word counts.
4. Also print the most common word.

**File:** `Day33_Task1.py`
"""
from collections import Counter
import string

sentence = "Hallo, ich bin Kakarot und auch heißt Son Goku. Ich bin der haupt Charakter von 'Dragon Ball Z' Serie."
words = []
for word in sentence.split():
    cleaned = word.strip(string.punctuation)
    if cleaned:
        words.append(cleaned.lower())

count = Counter(words)
print(count)
print(f"The most common word is: {count.most_common(1)}")