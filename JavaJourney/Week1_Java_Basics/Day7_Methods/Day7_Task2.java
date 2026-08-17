/*
2. Search and Reverse Array
   - Read an integer `n`, then read `n` integers into an `int[] numbers` array.
   - Read one additional integer `target`.
   - Write `int findIndex(int[] arr, int target)` to return the first index of `target` or `-1` if not found.
   - Write `int[] reverseArray(int[] arr)` to return a new array with elements in reverse order.
   - In `main`, print the target index and the reversed array 
*/
package Week1_Java_Basics.Day7_Methods;

import java.util.Scanner;
import java.util.Arrays;

public class Day7_Task2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] numbers = null; // Only declaring an array not initializing so it doesn#t takes memory
        // Getting the length of an array from user
        System.out.print("Enter the length of arrax in numbers: ");

        // Checking if the input is +ve int
        if (scanner.hasNextInt()) {
            int n = scanner.nextInt();
            if (n >= 0) {
                // Now intializing the array for numbers
                numbers = new int[n];
                System.out.print("Enter the numbers: ");
                for (int i = 0; i < n; i++) {
                    numbers[i] = scanner.nextInt();
                }
            } else {
                System.out.println("Enter a '+' ve integer");
            }
        } else {
            System.out.println("Invalid input. Please enter a vlid int.");
            scanner.next(); // Clears the invalid input 
        }
        // Getting a target number
        int target = 0;
        System.out.print("Enter a number whose index you want to know: ");
        if (scanner.hasNextInt()) {
            target = scanner.nextInt();
        }

        // Calling and printing
        int result = findIndex(numbers, target);
        System.out.println("The index of " + target + " is: " + result);


        int[] result1 = reverseArray(numbers);
        System.out.println("The reversed array of " + Arrays.toString(numbers) + " is: " + Arrays.toString(result1));

        // Closing scanner
        scanner.close();
    }

    // Function to find index of target
    public static int findIndex(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target) {
                return i;
            }
        }
        return -1;
    }

    // Function to get the reverse array
    public static int[] reverseArray(int[] arr) {
        int[] reversed = new int[arr.length];
        for (int i = 0; i < arr.length; i++) {
            reversed[i] = arr[arr.length -1 - i];
        }
        return reversed;
    }
}
