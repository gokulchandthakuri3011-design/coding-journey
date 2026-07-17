package Week2_OOP_Part1.Day9_Constructors;

/*
### Assignment 2: Circle with Constructor Chaining
Create a class `Circle` with field `radius` (double). Provide:
- A parameterized constructor `Circle(double radius)`.
- A no-arg constructor that chains to the parameterized one with radius `1.0`.
- A method `getArea()` that returns `Math.PI * radius * radius`.
- In `main`, create a circle with radius `5.0` and one with the default radius. Print both areas.
*/

public class Circle {
    double radius;

    // Parameterized constructor
    public Circle(double radius) {
        this.radius = radius;
    }

    // Non-arg constructor
    public Circle() {
        this(1.0);
    }
    
    // Method returns area
    public double getArea() {
        return Math.PI * radius * radius;
    }

    public static void main(String[] args) {
        // Circle with radius 5.0
        Circle circ1 = new Circle(5.0);
        System.out.println("Area of 1st Circle: " + String.format("%.2f", circ1.getArea()));

        // Circle with default radius (1.0)
        Circle circ2 = new Circle();
        System.out.println("Area of 2nd Circle: " + String.format("%.2f", circ2.getArea()));
    }
}
