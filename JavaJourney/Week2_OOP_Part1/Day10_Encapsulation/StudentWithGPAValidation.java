package Week2_OOP_Part1.Day10_Encapsulation;


/*
### Assignment 1: Student Class with GPA Validation
Create a class `Student` with the following private fields:
- `name` (String)
- `gpa` (double)
- `studentID` (String)

Provide the following:
1. A parameterized constructor that initializes all three fields (use the setter inside the constructor to validate the GPA).
2. Getter and setter for `name`.
3. Getter and setter for `gpa` — the setter **must** validate that `gpa` is between `0.0` and `4.0` (inclusive). If it's outside this range, print an error and do not update the field.
4. Getter for `studentID`, but **no setter** (making the ID read-only).
5. In your `main` method:
   - Create a student with a valid GPA (e.g., `3.8`) and print their details.
   - Try to set an invalid GPA (e.g., `5.2` or `-1.0`) and observe the validation message.
   - Verify that you cannot change the `studentID` after creation.
*/

public class StudentWithGPAValidation {
    // Private Fields
    private String name;
    private double gpa;
    private String studentID;

    // Parameterized constructor initializing 3 fields
    public StudentWithGPAValidation(String name, double gpa, String studentID) {
        this.name = name;
        this.studentID = studentID;

        // Setter to validte GPA
        setGPA(gpa);
    }

    // Getter and Setter for name

    // 1. Getter
    public String getName() {
        return name;
    }

    // 2. Setter
    public void setName(String name) {
        this.name = name;
    }

    // Getter and Setter for GPA
    // 1.Getter
    public double getGPA() {
        return gpa;
    }

    // 2. Setter to validate GPA
    public void setGPA(double gpa) {
        if (gpa >= 0.0 && gpa <= 4.0) {
            this.gpa = gpa;
        } else {
            System.out.println("Invalid GPA");
        }
    }

    // Getter for studentID (Read-only)
    public String getStudentID() {
        return studentID;
    }

    // Main Method
    public static void main(String[] args) {
        // Creating a student with valid GPA
        StudentWithGPAValidation student = new StudentWithGPAValidation("Arun", 3.8, "STU123");
        // Priinting Details
        System.out.println(student.getName());
        System.out.println(student.getGPA());
        System.out.println(student.getStudentID());

        // Try to set an invalid GPA
        student.setGPA(5.2);
        student.setGPA(-1.0);

        // Verifying Read Only access to studentID
        student.getStudentID();
        
    }
}

