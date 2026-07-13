package Week2_OOP_Part1.Day8_Classes_and_Objects;


/*
### Assignment 2: Circle with Constructor Chaining
Create a class `Circle` with field `radius` (double). Provide:
- A parameterized constructor `Circle(double radius)`.
- A no-arg constructor that chains to the parameterized one with radius `1.0`.
- A method `getArea()` that returns `Math.PI * radius * radius`.
- In `main`, create a circle with radius `5.0` and one with the default radius. Print both areas.
*/



public class Circle {
    // Field radius
    double radius;

    // Parameteized Constructor
    public Circle(double radius) {
        this.radius = radius;
    }

    // Non-argument Constructor
    public Circle() {
        this(1.0);
    }

    // Get Area Method
    public double getArea() {
        return Math.PI * radius * radius;  // Math.PI = PI Value
    }

    // Main Method
    public static void main(String[] args) {
        // Creating a circle obj
        Circle c1 = new Circle(5.0);

        // Displaying area formatted to 2 decimal places
        System.out.println("Area of circle: " + String.format("%.2f", c1.getArea()));

        System.out.println(); // Gap for easy reading

        // Creating default circle
        Circle c2 = new Circle();

        // Displaying default circle area formatted to 2 decimal places
        System.out.println("Area of Default Circle: " + String.format("%.2f", c2.getArea()));

    }
}
