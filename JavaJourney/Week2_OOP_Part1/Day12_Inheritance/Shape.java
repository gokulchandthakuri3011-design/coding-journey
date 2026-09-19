/*
5. Create a `Shape` superclass with a method `double area()` that returns `0`.
   Add a `Rectangle` subclass with `width` and `height` and override `area()`.
   Create a `Square` subclass of `Rectangle` and use constructor chaining with `super(...)`.
*/

package Week2_OOP_Part1.Day12_Inheritance;

public class Shape {
    public double area() {
        return 0;
    }
}

class Rectangle extends Shape {
    double width;
    double height;

    Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }

    @Override
    public double area() {
        return width * height;
    }
}

class Square extends Rectangle {
    Square(double side) {
        super(side, side); // constructor chaining
    }
}

class Main {
    public static void main(String[] args) {
        Shape s = new Shape();
        Rectangle rec = new Rectangle(4, 6);
        Square sqr = new Square(6);

        System.out.println("Shape area: " + s.area());
        System.out.println("Rectangle area: " + rec.area());
        System.out.println("Square area: " + sqr.area());
    }
}
