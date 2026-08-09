/*
### Task 3: Simple Calculator using `switch`
Declare two `double` variables `num1` and `num2`, and a `char` variable `operator` (e.g., '+', '-', '*', '/'). 
Use a `switch` statement based on the `operator` variable to perform the corresponding mathematical operation and print the result.
Handle the case of dividing by zero (using an `if` statement inside the division case) and provide a `default` case for invalid operators.

Happy coding! Once you've tried these, feel free to ask if you need hints or want to review your solutions.
*/


package Week1_Java_Basics.Day4_Control_Flow;

import java.util.Scanner;

public class Day4_Task3 {
    public static void main(String[] args) {
        System.out.println("---- Simple Calculator ----");

        // Creating a Scanner obj to take input from user
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter first number: ");
        double num1 = scanner.nextDouble();

        System.out.print("Enter second number: ");
        double num2 = scanner.nextDouble();

        System.out.print("Enter an operator (+, -, *, /): ");
        char operator = scanner.next().charAt(0); /* scanner.next() — reads the next token (until whitespace) as a String. If the user types +, it returns "+".
                                                            2. .charAt(0) — gets the character at index 0 (the first char) of that String. So "+" becomes '+'.
                                                            3. char operator = ... — stores that single character in a char variable named operator. */

        double result;

        // Using switch statement to perform the operation based on the operator
        switch (operator) {
            case '+':
                result = num1 + num2;
                System.out.println("Result: " + result);
                break;
            case '-':
                result = num1 - num2;
                System.out.println("Result: " + result);
                break;
            case '*':
                result = num1 * num2;
                System.out.println("Result: " + result);
                break;
            case '/':
                if (num2 != 0) {
                    result = num1 / num2;
                    System.out.println("Result: " + result);
                } else {
                    System.out.println("Error: Division by zero is not allowed.");
                }
                break;
            default:
                System.out.println("Error: Invalid operator. Please use +, -, *, or /.");
        }
        scanner.close();
    }
}
