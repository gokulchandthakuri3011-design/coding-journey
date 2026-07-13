package Week3_OOP_Part2_Core_APIs.Day19_Exception_Handling_Basics;

/*
**4. Multiple Exception Handling**
   - Create a program that:
     - Takes a string from input
     - Takes an index from input
     - Prints the character at that index in the string
   - Handle `NumberFormatException` (if index is not a number)
   - Handle `StringIndexOutOfBoundsException` (if index is out of bounds)
   - Display appropriate messages for each error
*/

import java.util.Scanner;

public class MediumTask4_MultipleExceptions {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a string: ");
        String inputString = scanner.nextLine();

        System.out.print("Enter an index: ");
        String indexInput = scanner.nextLine();

        try {
            // Integer.parseInt(indexInput) converts the input string to an int.
            // If the value is not a valid integer, it throws NumberFormatException.
            int index = Integer.parseInt(indexInput);

            // scanner.nextInt() reads the next integer directly from input.
            // If the user enters a non-integer value, it causes InputMismatchException.
            char character = inputString.charAt(index);
            System.out.println("Character at index " + index + ": " + character);
        }
        catch (NumberFormatException e) {
            System.out.println("Error: The index must be a valid integer.");
            System.out.println("Exception message: " + e.getLocalizedMessage());
        }
        catch (StringIndexOutOfBoundsException e) {
            System.out.println("Error: The index is out of bounds for the string.");
            System.out.println("Exception message: " + e.getMessage());
        }
        finally {
            scanner.close();
        }
    }
}
