package Week1_Java_Basics.Day3_Operators_and_Input;

/*### Task 1: Basic Calculator
1. Declare two `double` variables, `num1` and `num2`, and assign them values.
2. Calculate and print the result of their addition, subtraction, multiplication, and division.
3. *Tip: Add clear text to your output, e.g., `System.out.println("Addition: " + (num1 + num2));*/

public class Day3_Task1 {
    public static void main(String[] args) {

        // Basic Calculator

        // Declaring and initializing 2 double variables
        double num1 = 10.5;
        double num2 = 5.2;

        // Performing Calculations
        double addition = num1 + num2;
        double subtraction = num1 - num2;
        double multiplication =  num1 * num2;
        double division = num1 / num2;
        double modulus = num1 % num2;

        // Printing results
        System.out.println("----- Basic Calculator -----");
        System.out.println("Addition: " + String.format("%.2f", (addition)));
        System.out.println("Subtraction: " + String.format("%.2f", (subtraction)));
        System.out.println("Multiplication: " + String.format("%.2f", (multiplication)));
        System.out.println("Division: " + String.format("%.2f", (division)));
        System.out.println("Modulus: " + String.format("%.2f", (modulus)));

    }

}
