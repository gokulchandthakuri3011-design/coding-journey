import calculator
import text_formatter

def main():
    # --- Calculator Section ---
    print("\n=== Calculator ===")
    a = 10
    b = 3
    print(f"{a} + {b} = {calculator.add(a, b)}")
    print(f"{a} - {b} = {calculator.subtract(a, b)}")
    print(f"{a} x {b} = {calculator.multiply(a, b)}")
    print(f"{a} / {b} = {calculator.division(a, b)}")
    print(f"{a} % {b} = {calculator.modulo(a, b)}")
    print()

    # --- Text Formatter Section ---
    print("\n=== Text Formatter ===")
    sample = "aRun Giri meDizin"
    char = 'i'
    times = 3
    print(f"Original: {sample}")
    print(f"Uppercase: {text_formatter.to_uppercase(sample)}")
    print(f"Lowercase: {text_formatter.to_lowercase(sample)}")
    print(f"Title Case: {text_formatter.capitalize_words(sample)}")
    print(f"Word Count: {text_formatter.word_count(sample)}")
    print(f"Count of {char} in {sample}: {text_formatter.char_count(sample, char)}")
    print(f"Text Repetition {times} times: {text_formatter.repeat_text(text_formatter.capitalize_words(sample),times)}")

if __name__ == "__main__":
    main()