package Week3_OOP_Part2_Core_APIs.Day19_Exception_Handling_Basics;

/*
**2. String to Integer Converter**
   - Take a string input from the user
   - Convert it to an integer using `Integer.parseInt()`
   - Handle `NumberFormatException`
   - Display the converted number or an error message
*/

import java.util.Scanner;

public class EasyTask2_StringToInteger {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a string to convert to integer: ");
        String input = scanner.nextLine();
        try {
            int number = Integer.parseInt(input);
            System.out.println("Converted number: " + number);
        }
        catch (NumberFormatException e) {
            System.out.println("Error: Invalid Input! Please enter a valid integer string.");
            System.out.println("Exception Message: " + e.getMessage());
        }
        finally {
            scanner.close();
        }
    }
}
