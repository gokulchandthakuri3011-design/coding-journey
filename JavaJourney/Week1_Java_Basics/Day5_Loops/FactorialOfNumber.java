package Week1_Java_Basics.Day5_Loops;


/*
### Practice Exercise 5.4
Find the factorial of a number using a loop.

**Sample:**
```
Enter a number: 5
Factorial: 120
```
*/

import java.util.Scanner;

public class FactorialOfNumber {

    // Method to calculate the factorial of a number
    // We use 'long' because factorials grow very quickly and would overflow an 'int' above 12!
    public static long calculateFactorial(int num) {
        long factorial = 1;
        for (int i = 1; i <= num; i++) {
            factorial *= i;
        }
        return factorial;
    }

    public static void main(String[] args) {

        // Scanner Object
        Scanner scanner = new Scanner(System.in);

        // Prompting user for input
        System.out.print("Enter a non-negative integer: ");

        // Check if the input is a valid integer
        if (scanner.hasNextInt()) {
            int num = scanner.nextInt();

            // Check if the number is negative
            if (num < 0) {
                System.out.println("Error: Factorial is not defined for negative numbers.");
            } else {
                // Call the method to calculate factorial
                long result = calculateFactorial(num);
                System.out.println("Factorial of " + num + " = " + result);
            }
        } else {
            System.out.println("Error: Please enter a valid integer.");
        }

        // Closing Scanner
        scanner.close();
    }    
}
