package Week2_OOP_Part1.Day9_Constructors;


/*
### Assignment 1: Employee Class
Create a class `Employee` with fields `name` (String), `id` (int), and `salary` (double). Provide:
- A parameterized constructor that sets all three fields.
- A no-arg constructor that defaults name to `"Unknown"`, id to `0`, and salary to `30000.0`.
- A method `displayDetails()` that prints all fields.
- In `main`, create one employee using each constructor and call `displayDetails()`.
*/

public class Employee {
    // Fields
    String name;
    int id;
    double salary;

    // Parameterized constructor
    public Employee(String name, int id, double salary) {
        this.name = name;
        this.id = id;
        this.salary = salary;
    }

    // No-arg constructor
    public Employee() {
        this.name = "Unknown";
        this.id = 0;
        this.salary = 30000.0;
    }

    // Method to display details
    public void displayDetails() {
        System.out.println("Name : " + name);
        System.out.println("ID : " + id);
        System.out.println("Salary : " + salary);
    }
    
    // Main method to test the Employee class
    public static void main(String[] args) {
        // Create an employee using the parameterized constructor
        Employee emp1 = new Employee("Alice", 101, 50000.0);
        emp1.displayDetails();

        System.out.println(); // Just for better readability
        
        // Create an employee using the no-arg constructor
        Employee emp2 = new Employee();
        emp2.displayDetails();
    }
}
