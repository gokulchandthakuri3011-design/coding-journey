package Week2_OOP_Part1.Polymorphism2;


/*
1. **Shape Hierarchy**: Create a `Shape` superclass with an abstract-like `double area()` method (return 0).
    Create `Circle` (with `radius`) and `Rectangle` (with `width`, `height`) subclasses that override `area()`.
    Write a `printArea(Shape s)` method that uses runtime polymorphism to print the area of any shape.
*/

public class Shape {

    public double area() {
        return 0;
    }

    public void displayArea() {
        System.out.println("Area: " + this.area());
    }
}

class Circle extends Shape {
    double radius;
    double pie = 3.147;

    public Circle(double radius) {
        this.radius = radius;
    }
    @Override
    public double area() {
        return pie * radius * radius;
    }
    
    @Override
    public void displayArea() {
        System.out.println("Circle Area: " + this.area());
    }
}

class Rectangle extends Shape {
    double width;
    double height;

    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }
    @Override
    public double area() {
        return width * height;
    }
    
    @Override
    public void displayArea() {
        System.out.println("Rectangle Area: " + this.area());
    }
}

class Test {
    public static void main(String[] args) {
        // Upcasting 
        Shape shape1 = new Circle(4.0);
        Shape shape2 = new Rectangle(3.0, 5.0);

        // Call displayArea() - demonstrates runtime polymorphism
        System.out.println("Testing Polymorphism:");
        shape1.displayArea(); // Calls Circle's displayArea()
        shape2.displayArea(); // Calls Rectangle's displayArea()

        // Downcasting: casting Shape back to originaltype (with safety check)
        System.out.println("\nTesting Downcasting:");
        if (shape1 instanceof Circle) {
            Circle circle = (Circle) shape1;
            System.out.println("Circle radius: " + circle.radius);
            circle.displayArea();
        }

        if (shape2 instanceof Rectangle) {
            Rectangle rectangle = (Rectangle) shape2;
            System.out.println("Rectangle width: " + rectangle.width + ", height: " + rectangle.height);
            rectangle.displayArea();
        }
    }
}
