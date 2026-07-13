package Week2_OOP_Part1.Day11_Static_Keyword;


/*
### Assignment 2: Static Utility Helper (`MathUtility`)
Create a utility class named `MathUtility` designed for quick math operations:
1. Define a public static final constant `E = 2.71828`.
2. Write the following static methods:
   - `public static int add(int a, int b)`: Returns the sum of a and b.
   - `public static double square(double num)`: Returns `num * num`.
   - `public static double power(double base, int exponent)`:
      Returns base raised to the power of exponent using a simple loop.
3. In the `main` method, test each method **without instantiating** the `MathUtility` class.
4. Try to write an instance variable inside the class (like `int totalOperationsRun`),
   try to increment it inside your static `add()` method,
   and write down in comments the exact compile-time error you see and why it happens.
*/


public class MathUtility {
    // defining a static final constant E
    public static final double E = 2.71828;

    // Trying to define an instance variable 
    // int totalOperationRun; // This will cause a compile-time error when accessed in static methods
    
    // Static Methods

    // Method to add two integers
    public static int add(int a, int b) {
        return a + b;
        // totalOperationRun++; // Static method can't access instance variable
        // Compile-time error: non-static variable totalOperationRun cannot be referenced from a static context
    }

    // Method to calculate the square of a double
    public static double square(double num) {
        return num * num;
    }

    // Method to calculate the power of a double raised to an integer exponent
    public static double power(double base, int exponent) {
        // Using a simple loop to calculate power
        double result = 1.0;
        for (int i = 0; i < exponent; i++) {
            result *= base;
        }
        return result;
    }

    // Main method to test static methods without instantiation
    public static void main(String[] args) {
        // Testing the add method
        int sum = MathUtility.add(5, 10);
        System.out.println("Sum: " + sum);

        // Testing the square method
        double squaredValue = MathUtility.square(4.5);
        System.out.println("Squared Value: " + squaredValue);

        // Testing the power method
        double powerValue = MathUtility.power(2.0, 3);
        System.out.println("Power Value: " + powerValue);
    }
}
