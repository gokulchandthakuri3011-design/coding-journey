package Week1_Java_Basics.Day6_Arrays;


/*
### Assignment 3: Array Reversal
Write a program that:
- Takes an array of integers
- Reverses the array (hint: swap elements from both ends)
- Prints the reversed array

**Example:**
```
Original: [1, 2, 3, 4, 5]
Reversed: [5, 4, 3, 2, 1]
*/

import java.util.Arrays;
import java.util.Scanner;

public class Array_Task3 {
    public static void main(String[] args) {

        // Create a Scanner object to read user input
        Scanner scanner = new Scanner(System.in);

        // Prompt the user to enter the size of the array
        System.out.print("Enter the size of the array: ");
        int size = scanner.nextInt();

        // Create an array to hold the integers
        int[] array = new int[size];

        // Prompt the user to enter the elements of the array
        System.out.println("Enter the elements of the array: ");
        for (int i = 0; i < size; i++) {
            array[i] = scanner.nextInt();
        }

        // Print the original array
        System.out.println("original: " + Arrays.toString(array));

        // Creating a new reversed array
        int[] reversedArray = new int[size];

        // Initializing j for the reversed array
        int j = 0;

        // Iterating through original array but from end
        for (int i = size - 1; i >= 0; i--) {
            reversedArray[j] = array[i];
            j++;
        }

        // Print the reversed array
        System.out.println("Reversed: " + Arrays.toString(reversedArray));

        scanner.close();
    }

}
