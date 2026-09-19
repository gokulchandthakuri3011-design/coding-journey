/*
### Question 3: Create a `Calculator` class with overloaded `multiply` methods
Write a class with these methods:
- `multiply(int a, int b)`
- `multiply(int a, int b, int c)`
- `multiply(double a, double b)`

Test all versions in `main`.
*/
package Week2_OOP_Part1.Polymorphism1;

public class Calculator {
    public int multiply(int a, int b) {
        return a * b;
    }

    public int multiply(int a, int b, int c) {
        return a * b * c;
    }

    public double multiply(double a, double b) {
        return a * b;
    }
}

class CalculatorMain {
    public static void main(String[] args) {
        Calculator c1 = new Calculator();

        // Printing
        System.out.println("Product: " + c1.multiply(2,3));
        System.out.println("Product: " + c1.multiply(4,5,6));
        System.out.println("Product: " + c1.multiply(2.5,2.0));
    }
}
