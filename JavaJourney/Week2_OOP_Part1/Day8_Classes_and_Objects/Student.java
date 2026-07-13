package Week2_OOP_Part1.Day8_Classes_and_Objects;


/*
### Assignment 1: Student Class (Simple)
Create a class named `Student` with:
- **Instance Variables:** `name` (String), `rollNumber` (int), and `marks` (double).
- **Method:** `displayStudentInfo()` that prints the student's name, roll number, and marks.
- **In your `Main` class:** Create two `Student` objects, set their fields directly in `main`,
    and call `displayStudentInfo()` on both to print their details.
*/

public class Student {
    
    // Creating Instance Variables
    String name;
    int rollNumber;
    double marks;

    // Creating Method to display Student Info (non-static instance method)
    public void displayStudentInfo() {
        System.out.println("Displaying Student Information:");
        System.out.println("Name: " + name);
        System.out.println("Roll Number: " + rollNumber);
        System.out.println("Marks: " + marks);
    }

    // Creating Main Method
    public static void main(String[] args) {
        // Creating 1st Student Object
        Student s1 = new Student();
        s1.name = "Arun";
        s1.rollNumber = 1;
        s1.marks = 94.5;

        // Creating 2nd Student Object
        Student s2 = new Student();
        s2.name = "Gokul";
        s2.rollNumber = 2;
        s2.marks = 95.6;

        // Calling displayStudentInfo() method on both objects
        s1.displayStudentInfo();
        s2.displayStudentInfo();
    }
}
