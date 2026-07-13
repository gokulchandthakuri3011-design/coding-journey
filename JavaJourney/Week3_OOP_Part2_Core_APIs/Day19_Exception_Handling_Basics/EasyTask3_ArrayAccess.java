package Week3_OOP_Part2_Core_APIs.Day19_Exception_Handling_Basics;

/*
**3. Array Access Validator**
   - Create an array of 5 integers
   - Ask user for an index to access
   - Handle `ArrayIndexOutOfBoundsException`
   - Display the element or an error message
*/

import java.util.Scanner;

public class EasyTask3_ArrayAccess {
    public static void main(String[] args) {
        int[] number = {1,2,3,4,5};
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter an index to access (0-4): ");
        try {
            int index = scanner.nextInt();
            System.out.print("Element at index " + index + ": " + number[index]);
        }
        catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Error: Index out of bounds. Please enter a valid index (0-4).");
            System.out.println("Exception Type: " + e.getMessage());
        }
        catch (Exception e) {
            System.out.println("Error: Invalid input. Please enter an integer index.");
            // getSimpleName() returns just the class name (e.g., InputMismatchException)
            // getName() returns the fully qualified name (e.g., java.util.InputMismatchException)
            System.out.println("Exception Type: " + e.getClass().getSimpleName());
        }
        finally {
            scanner.close();
        }
    }
}
