/*
### Question 5: Constructor overloading with a `Student` example
Create a `Student` class with fields:
- `name` (String)
- `grade` (int)
- `school` (String)

Provide these constructors:
- `Student()` with default values.
- `Student(String name)`.
- `Student(String name, int grade)`.
- `Student(String name, int grade, String school)`.

Then create objects using each constructor and print the student information.
*/
package Week2_OOP_Part1.Polymorphism1;

public class Student {
    String name;
    int grade;
    String school;

    // Constructor Overloading
    public Student() {
        this.name = "Unknown";
        this.grade = 0;
        this.school = "Unknown";
    }

    public Student(String name) {
        this.name = name;
        this.grade = 0;
        this.school = "Unknown";
    }

    public Student(String name, int grade) {
        this.name = name;
        this.grade = grade;
        this.school = "Unknow";
    }

    public Student(String name, int grade, String school) {
        this.name = name;
        this.grade = grade;
        this.school = school;
    }
}

class StudentMain {
    public static void main(String[] args) {
        Student s1 = new Student();
        Student s2 = new Student("Gokul");
        Student s3 = new Student("Derya", 12);
        Student s4 = new Student("Emily", 13, "HNU");

        // Printing Info using diff Objects
        System.out.println("Name: " + s1.name + " Grade: " + s1.grade + " School: " + s1.school);
        System.out.println("Name: " + s2.name + " Grade: " + s2.grade + " School: " + s2.school);
        System.out.println("Name: " + s3.name + " Grade: " + s3.grade + " School: " + s3.school);
        System.out.println("Name: " + s4.name + " Grade: " + s4.grade + " School: " + s4.school);
    }
}
