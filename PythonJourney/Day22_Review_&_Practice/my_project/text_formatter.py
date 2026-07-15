"""Text Formatter"""

def to_uppercase(text):
    return text.upper()

def to_lowercase(text):
    return text.lower()

def capitalize_words(text):
    return text.title()

def word_count(text):
    return len(text.split())

def char_count(text, char):
    return text.lower().count(char.lower())

def repeat_text(text, times):
    return " ".join([text] * times)

if __name__ == "__main__":
    print("\n  Running text_formatter Module tests..  ")
    sample = "lEarning Python"
    char = 'n'
    times = 3
    print(to_uppercase(sample))
    print(to_lowercase(sample))
    print(capitalize_words(sample))
    print(word_count(sample))
    print(char_count(sample, char))
    print(repeat_text(capitalize_words(sample), times))