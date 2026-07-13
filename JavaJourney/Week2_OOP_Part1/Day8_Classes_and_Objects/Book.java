package Week2_OOP_Part1.Day8_Classes_and_Objects;


/*
### Assignment 3: Book Library System
Create a class `Book` with fields `title`, `author`, `isbn` (String), and `isAvailable` (boolean).
- Provide constructors:
  - `Book(String title, String author, String isbn)` — sets isAvailable to `true` by default.
  - `Book(String title, String author)` — isbn defaults to `"N/A"`.
- Add a method `borrowBook()` that sets `isAvailable` to `false`.
- Add a method `returnBook()` that sets `isAvailable` to `true`.
- Add a method `displayStatus()` that prints all fields.
- In `main`, create two books, borrow one, and display both statuses.
*/


public class Book {

    // Fields
    String title;
    String author;
    String isbn;
    boolean isAvailable;

    // 1st Constructor sets isAvailable to 'true' by default
    public Book(String title, String author, String isbn) {
        this.title = title;
        this.author = author;
        this.isbn = isbn;
        this.isAvailable = true;
    }

    // 2nd Constructor - ISBN = 'N/A'
    public Book(String title, String author) {
        this.title = title;
        this.author = author;
        this.isbn = "N/A";
    }

    // Method - 'borrowBook' -sets isAvailable to false
    public void borrowBook() {
        isAvailable = false;
    }

    // Method - 'returnBook' -sets isAvailable to true
    public void returnBook() {
        isAvailable = true;
    }

    // Method - displayStatus - prints all fields
    public void displayStatus() {
        System.out.println("Title: " + title);
        System.out.println("Author: " + author);
        System.out.println("ISBN: " + isbn);
        System.out.println("Status: " + isAvailable);
        System.out.println();
    }

    // Main Method
    public static void main(String[] args) {
        // Create 2 books
        Book book1 = new Book("Java", "Arun", "12345");
        Book book2 = new Book("Python", "Gokul", "4321");

        // Borrow one book
        book1.borrowBook();
        book2.borrowBook();

        // Display both books
        book1.displayStatus();
        book2.displayStatus();
    }
}
