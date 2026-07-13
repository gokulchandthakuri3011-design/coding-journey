package Week1_Java_Basics.Day7_Methods;


/* 
## Assignments
1. Write a method named `addNumbers` that takes two `int` values, adds them, and returns the sum.
2. Write a method named `isEven` that takes one `int` and returns `true` when the number is even and `false` when it is odd.
3. Write a method named `convertToUpper` that takes a `String` and returns the same text in uppercase.
4. Write a method named `calculateArea` that takes `double width` and `double height`, then returns the area of a rectangle.
5. Write a method named `printCountdown` that prints numbers from `5` down to `1` using a loop.
6. Write a method named `maxOfThree` that takes three integers and returns the largest one.
7. Create a program with `main` that calls each method and prints its result.
*/

import java.util.Scanner;

public class Method_Task1 {

    public static void main(String[] args) {
        // Testing the methods

        // Get user inputs for Methods
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter first number for addition: ");
        int num1 = scanner.nextInt();
        System.out.print("Enter second number for addition: ");
        int num2 = scanner.nextInt();
        System.out.print("Enter a number to check if it's even: ");
        int evenCheckNum = scanner.nextInt();
        scanner.nextLine(); // Consume the newline left by nextInt()
        System.out.print("Enter a string to convert to uppercase: ");
        String text = scanner.nextLine();
        System.out.print("Enter length of the rectangle: ");
        double length = scanner.nextDouble();
        System.out.print("Enter width of the rectangle: ");
        double width = scanner.nextDouble();
        System.out.print("Enter first number for the max of three: ");
        int maxNum1 = scanner.nextInt();
        System.out.print("Enter second number for the max of three: ");
        int maxNum2 = scanner.nextInt();
        System.out.print("Enter third number for the max of three: ");
        int maxNum3 = scanner.nextInt();

        // Calling methods and printing results
        int sum = addNumbers(num1, num2); // Method 1: Adding 2 Numbers
        System.out.println("Sum: " + sum);

        String evenCheckResult = isEven(evenCheckNum); // Method 2: Even Check
        System.out.println("Even Check: " + evenCheckResult);

        String upperText = convertToUpper(text); // Method 3: Convert to Uppercase
        System.out.println("Uppercase: " + upperText);

        double area = calculateArea(length, width); // Method 4: Area of Rectangle
        System.out.println("Area of Rectangle: " + area);

        // System.out.println(printCountdown()); // Causes an error bcz the method is void type and System.out.println() expects a return value.
        printCountdown(); // Method 5: Countdown from 5 to 1

        int max = maxOfThree(maxNum1, maxNum2, maxNum3); // Method 6: Max of Three Numbers
        System.out.println("Maximum of three numbers: " + max);

        scanner.close();

    }

    // Method to add two numbers
    public static int addNumbers(int a, int b) {
        return a + b;
    }

    // Method to check if a number is even
    public static String isEven(int num) {
        if (num % 2 == 0) {
            return num + " is even.";
        } else {
            return num + " is odd.";
        }

    }

    // Method to convert a string to uppercase
    public static String convertToUpper(String text) {
        return text.toUpperCase();
    }

    // Method to calculate the area of a rectangle
    public static double calculateArea(double length, double width) {
        return length * width;
    }

    // Method to print countdown from 5 to 1
    public static void printCountdown() {
        for (int i = 5; i >= 1; i--) {
            System.out.println(i);
        }
    }

    // Method to find the maximum of three numbers
    public static int maxOfThree(int num1, int num2, int num3) {
        return Math.max(num1, Math.max(num2, num3));
    }

}
