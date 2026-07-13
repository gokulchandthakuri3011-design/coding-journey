package Week3_OOP_Part2_Core_APIs.Day17_Packages_And_Imports.Task1;

public class Circle {
    public double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    public void circleArea() {
        double area = Math.PI * radius * radius;
        System.out.println("Area of circle with radius " + radius + " : " + area);
    }

    public void circlePerimeter() {
        double perimeter = 2 * Math.PI * radius;
        System.out.println("Perimeter of circle with radius " + radius + " : " + perimeter);
    }
}
