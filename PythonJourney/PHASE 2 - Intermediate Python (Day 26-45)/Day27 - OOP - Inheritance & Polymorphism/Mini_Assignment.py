"""
## Mini Assignment
Build a small **Library System**:
- Create a base class `LibraryItem` with `title`, `year`, and an abstract `describe()` method.
- Create `Book` (adds `author`, `pages`) and `DVD` (adds `director`, `duration`) subclasses.
- Each subclass implements `describe()` with its own text.
- Create a list of items (mix of books and DVDs) and print the description of each using a single loop.
- Add one extra item type of your choice (e.g., `Magazine`) without changing the loop.
"""

class LibraryItem:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def describe(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Book(LibraryItem):
    def __init__(self, title, year, author, pages):
        super().__init__(title, year)
        self.author = author
        self.pages = pages

    def describe(self):
        return f"Book: '{self.title}' by {self.author}, {self.pages} pages, published in {self.year}."

class DVD(LibraryItem):
    def __init__(self, title, year, director, duration):
        super().__init__(title, year)
        self.director = director
        self.duration = duration

    def describe(self):
        return f"DVD: '{self.title}' directed by {self.director}, duration {self.duration} minutes, released in {self.year}."

# Creating a list of library items, printing their descriptions using single loop and adding a new item type (Magazine)
class Magazine(LibraryItem):
    def __init__(self, title, year, issue_number):
        super().__init__(title, year)
        self.issue_number = issue_number

    def describe(self):
        return f"Magazine: '{self.title}', Issue {self.issue_number}, published in {self.year}."

def main():
    library_items = [
        Book("The Great Gatsby", 1925, "F. Scott Fitzgerald", 218),
        DVD("Inception", 2010, "Christopher Nolan", 148),
        Magazine("National Geographic", 2021, 5)
    ]
    for item in library_items:
        print(item.describe())

if __name__ == "__main__":
    main()

