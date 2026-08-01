"""
### Assignment 4: Word Counter (Medium)

Create a program that:
1. Reads a text file
2. Counts the total number of words, lines, and characters
3. Finds the most common word
4. Writes a report to a new file

**Expected Report Output:**
```
=== WORD COUNT REPORT ===
Total Lines: 15
Total Words: 120
Total Characters: 750
Most Common Word: "the" (appeared 12 times)
"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Reading the text file
def read_file():
    with open(os.path.join(BASE_DIR, "ICloud.txt"), "r") as file:
        reader = file.read()
        return reader

# Counting total words
def count_words(reader):
    words_lst = reader.split()
    return len(words_lst)

# Counting total lines
def count_lines(reader):
    lines = reader.splitlines()
    return len(lines)

# Counting total characters
def count_characters(reader):
    return len(reader)

# Finding the most common word
def most_common_word(reader):
    words_lst = reader.split()
    word_count = {}

    for word in words_lst:
        word = word.lower().strip('.,!?";:()[]{}') # Remove the punctuation and convert to lowercase
        if not word: # Skip empty strings
            continue
        word_count[word] = word_count.get(word, 0) + 1
    common_word, common_word_count = max(word_count.items(), key=lambda pair: pair[1])
    return common_word, common_word_count

# Writing the report to a new file
def write_report(total_lines, total_words, total_characters, common_word, common_word_count):
    with open(os.path.join(BASE_DIR, "word_count_report.txt"), "w") as report_file:
        report_file.write("=== WORD COUNT REPORT ===\n")
        report_file.write(f"Total Lines: {total_lines}\n")
        report_file.write(f"Total Words: {total_words}\n")
        report_file.write(f"Total Characters: {total_characters}\n")
        report_file.write(f'Most Common Word: "{common_word}" (appeared {common_word_count} times)\n')

def main():
    reader = read_file()
    total_lines = count_lines(reader)
    total_words = count_words(reader)
    total_characters = count_characters(reader)
    common_word, common_word_count = most_common_word(reader)

    print(f"Total Lines: {total_lines}")
    print(f"Total Words: {total_words}")
    print(f"Total Characters: {total_characters}")
    print(f'Most Common Word: "{common_word}" (appeared {common_word_count} times)')

    write_report(total_lines, total_words, total_characters, common_word, common_word_count)

if __name__ == "__main__":
    main()