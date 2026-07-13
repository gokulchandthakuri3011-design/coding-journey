package Week2_OOP_Part1.Day11_Static_Keyword;


/*
### Assignment 1: Automated ID Generator for `Student`
Let's build upon your Day 10 `Student` class:
1. Add a private static variable `studentCounter` that starts at `1000`.
2. Add an instance variable `uniqueID` (String).
3. In your constructor, increment the `studentCounter` and construct a custom `uniqueID` for the student (e.g., `"STUDENT-" + studentCounter`).
4. Provide a public **static getter** `getTotalStudentsCount()` to retrieve the current count of enrolled students.
5. In your `main` method:
   - Create 3 students: `"Arun"`, `"Bina"`, and `"Chetan"`.
   - Print their details and verify that they have automatically received unique, consecutive IDs (`STUDENT-1001`, `STUDENT-1002`, `STUDENT-1003`).
   - Call the static getter to print the final student count.
*/

public class StudentStatic {
    // private static variable with value 1000
    private static int studentCounter = 1000;
    private static int totalStudents = 0;

    // instance variable
    private String uniqueID;
    private String name;

    // Constructor
    public StudentStatic(String name) {
        this.name = name;

        // inrement the static counter first
        studentCounter++;
        totalStudents++;

        // Constructing uniqueId
        this.uniqueID = name + "-"  + studentCounter;
    }

    // Static getter method
    public static int getTotalStudentsCount() {
        return totalStudents;
    }

    // public getter for uniqueID
    public String getUniqueID() {
        return uniqueID;
    }

    // public getter for name
    public String getName() {
        return name;
    }

    // Main method
    public static void main(String[] args) {

        // Creating 3 students
        StudentStatic s1 = new StudentStatic("Arun");
        StudentStatic s2 = new StudentStatic("Gokul");
        StudentStatic s3 = new StudentStatic("Lalita");

        // Printing Student Details
        System.out.println("Student 1: " + s1.getName() + " ID: " + s1.getUniqueID());
        System.out.println("Student 2: " + s2.getName() + " ID: " + s2.getUniqueID());
        System.out.println("Student 3: " + s3.getName() + " ID: " + s3.getUniqueID());

        // Calling static method to print total count of students
        System.out.println("Total Students enrolled: " + StudentStatic.getTotalStudentsCount());
    }
}
