package Week2_OOP_Part1.Day12_Inheritance;


/*
2. Build a `Person` superclass with `name` and `age` fields and a `introduce()` method.
   Create a `Teacher` subclass that adds `subject` and a `teach()` method.
   In `Teacher`, call `super.introduce()` from a new method.
*/

public class Person {
    // Fields
    protected String name;
    protected int age;

    // Constructor
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Method
    public void introduce() {
        System.out.println("Hello, my name is " + name + " and I am " + age + " years old.");
    }
}

// Subclass Teacher extends Person
class Teacher extends Person {
    private String subject;

    // Constructor accepts person details and subject
    public Teacher(String name, int age, String subject) {
        super(name, age); // Calls Person constructor to initialize fields
        this.subject = subject;
    }

    // Method to introduce and teach overriding the Parent class introduce() method
    public void introduceAndTeach() {
        super.introduce(); // Call the parent class method to introduce
        System.out.println("I teach " + subject + ".");
    }

    // Main method for testing
    public static void main(String[] args) {
        Teacher myTeacher = new Teacher("Lalita", 21, "Biology");
        myTeacher.introduceAndTeach();
    }
}
