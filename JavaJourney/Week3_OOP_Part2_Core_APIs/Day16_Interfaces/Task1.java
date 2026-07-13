package Week3_OOP_Part2_Core_APIs.Day16_Interfaces;


/*
### **Q1: Basic Interface Implementation**
Create an interface `Printable` with a method `print()`.
Implement it in classes `Document` and `Photo`.
Each class should print a different message.
*/

interface Printable {
    void print(); // abstract by default
}

class Document implements Printable {
    @Override
    public void print() {
        System.out.println("These are Arun's Documents.");
        System.out.println("These are Grade 9 & 10 Documents.");
    }
}

class Photo implements Printable {
    @Override
    public void print() {
        System.out.println("These are Lalita's Photos.");
        System.out.println("These Photos are from Grade 9 and 10.");
    }
}

// class with a main method
public class Task1 {
    public static void main(String[] args) {
        Document doc = new Document();
        Photo photo = new Photo();

        doc.print();
        photo.print();
    }
}
