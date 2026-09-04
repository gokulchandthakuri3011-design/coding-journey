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

package Week2_OOP_Part1.Day9_Constructors;

public class Book {
    String title;
    String author;
    String isbn;
    boolean isAvailable;

    // Constructor with all parameters
    public Book(String title, String author, String isbn) {
        this.title = title;
        this.author = author;
        this.isbn = isbn;
        this.isAvailable = true; // Default to available
    }

    // Constructor with title and author only
    public Book(String title, String author) {
        this(title, author, "N/A"); // Default isbn to "N/A"
    }

    // Method to borrow the book
    public void borrowBook() {
        if (isAvailable) {
            isAvailable = false;
            System.out.println(title + " has been borrowed.");
        } else {
            System.out.println(title + " is currently not avilable for borrowing.");
        }
    }

    // Method to return the book
    public void returnBook() {
        if (!isAvailable) {
            isAvailable = true;
            System.out.println(title + " has been returned.");
        } else {
            System.out.println(title + " was not borrowed.");
        }
    }

    // Method to display the status of the book
    public void displayStatus() {
        System.out.println("Tile: " + title);
        System.out.println("Author: " + author);
        System.out.println("ISBN: " + isbn);
        System.out.println("Avaialablity: " + (isAvailable ? "Available" : "Not Available"));
    }

    // Main method to test the Book Class
    public static void main(String[] args) {
        // Creating 2 Books
        Book book1 = new Book("Harry Potter", "J.K. Rowling", "978-0747532743");
        Book book2 = new Book("Avengers: Endgame", "Stan Lee", "978-1302900000");

        // Displaying initial status of both books
        System.out.println("---- Book Library System ----");
        System.out.println();
        System.out.println("Initial Status of Books:");
        System.out.println();
        book1.displayStatus();
        System.out.println();
        book2.displayStatus();
        System.out.println();

        // Borrowing book1
        System.out.println("Borrowing Book 1:");
        book1.borrowBook();
        System.out.println();
        // Displaying status after borrowing book1
        System.out.println("Status of Books after borrowing Book 1:");
        System.out.println();
        book1.displayStatus();
        System.out.println();
        // Returning book1
        System.out.println("Returning Book 1:");
        book1.returnBook();
        System.out.println();
        // Displaying status after returning book1
        System.out.println("Status of Books after returning Book 1:");
        System.out.println();
        book1.displayStatus();
        System.out.println();
        
    }
}
