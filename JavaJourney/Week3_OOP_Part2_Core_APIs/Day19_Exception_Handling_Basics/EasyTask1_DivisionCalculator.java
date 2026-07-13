package Week3_OOP_Part2_Core_APIs.Day19_Exception_Handling_Basics;

import java.util.InputMismatchException;

/*
**1. Division Calculator with Exception Handling**
   - Write a program that takes two numbers from the user and divides them
   - Handle `ArithmeticException` (division by zero)
   - Handle `InputMismatchException` (user enters non-integer)
   - Display appropriate error messages
*/

import java.util.Scanner;

public class EasyTask1_DivisionCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        try {
            System.out.print("Enter the numerator: ");
            int numerator = scanner.nextInt();
            System.out.print("Enter the denominator: ");
            int denominator = scanner.nextInt();
            int result = numerator / denominator;
            System.out.println("Result: " + result);
        }
        catch (ArithmeticException a) { // Incase user types 0 as denominator
            System.out.println("Error: Division by zero is not allowed: " + a.getMessage());
        }
        catch (InputMismatchException a) { // Incase user types non-integer value
            System.out.println("Error: Invalid input. Please enter integers only: " + a.getMessage());
        }
        finally {
            scanner.close();
        }
    }
}
