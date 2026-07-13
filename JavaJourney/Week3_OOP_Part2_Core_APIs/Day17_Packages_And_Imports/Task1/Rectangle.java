package Week3_OOP_Part2_Core_APIs.Day17_Packages_And_Imports.Task1;

public class Rectangle {
    public double length;
    public double width;

    public Rectangle(double length, double width) {
        this.length = length;
        this.width = width;
    }

    public void rectangleArea() {
        double area = length * width;
        System.out.println("Area of rectangle with " + length + " & " + width + " : " + area);
    }

    public void rectanglePerimeter() {
        double perimeter = 2 * (length + width);
        System.out.println("Perimeter of rectangle with " + length + " & " + width + " : " + perimeter);
    }
    
}
