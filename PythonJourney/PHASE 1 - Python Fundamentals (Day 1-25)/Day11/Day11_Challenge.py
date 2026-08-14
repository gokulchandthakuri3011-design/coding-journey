"""
## ⚡ Challenge: Word Frequency Counter

*Practice implementing real-world text processing using a dictionary.*

1. Prompt the user to enter a sentence:
   *(Example: "python is fun and learning python is easy")*
2. Clean and process the sentence: convert it to lowercase and split it into a list of words using `.split()`.
3. Create an empty dictionary called `word_counts`.
4. Loop through the list of words:
   - If the word is already a key in `word_counts`, increment its value by `1`.
   - If the word is not in `word_counts`, add it with a value of `1`.
5. Print the final counts of each word in a clean format.
- **File:** `Day11_Challenge.py`
"""

print("\n --- Word Frequency Counter --- \n")

# Prompting user for input (suppose this as user prompt)
user_input = "Python is fun and learning python is easy."

# Converting the prompt to list
list_of_words = user_input.lower().split()

# Empty Dictionary for words counts
word_counts = {}

# Looping through the list
for word in list_of_words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

# Printing the words with their count
for key, value in word_counts.items():
    print(f"{key}: {value}")
print("\n ------------------------------- \n")