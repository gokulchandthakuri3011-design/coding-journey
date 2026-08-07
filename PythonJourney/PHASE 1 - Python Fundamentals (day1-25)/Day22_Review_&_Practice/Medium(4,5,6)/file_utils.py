"""
5. Build a `file_utils.py` module with functions to count lines, words, and characters in a text string. Write a main script that uses these functions.
"""
# Counting lines using splitlines() 
def counting_lines(text):
    lines = text.splitlines() # Here this -> breaks text wherever there's a newline and convert into a list of lines
    return len(lines)

# Counting words 
def counting_words(text):
    return len(text.split()) # Here this -> splits by spaces and creates list of words

# Counting characters
def counting_char(text):
    return len(text) # Returns total no. of characters including spaces

if __name__ == "__main__":
    text = """Hallo, mein Name ist Son Goku. Ich bin 22 Jahre alt und bin Student an der HNU.
              Ich arbeite gerade bei einer Bäckerei, also beginnt mein erstes Semester ab kommenden September.
              Ich komme aus Nepal und ich habe nicht so viele Fruenden, aber habe ich viele Relatives and Familienmitglieder.
              Ich habe einen BestFreund und er studiert Medizin in Pokhara, und gibt es eine Mädchen(Freundin), die ich mag, und sie auch studiert Medizin in Bangladesh.
              Sie beide sind auch Freund und wir haben zusammen in Klasse 9 und 10 studiert."""
    print(f"In the given text, there are {counting_lines(text)} lines.")
    print(f"In the given text, there are {counting_words(text)} words.")
    print(f"In the given text, there are {counting_char(text)} characters including spaces & punctuation.")