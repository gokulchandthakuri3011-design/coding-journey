package Week1_Java_Basics.Day6_Arrays;


/*
### Assignment 4: Count Occurrences
Write a program that:
- Takes an array of integers and a target number
- Counts how many times the target number appears in the array
- Prints the count
*/

import java.util.Scanner;

public class Day6_Task4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Get the size of the array
        System.out.print("Enter the size of the array: ");
        int size = scanner.nextInt();

        // Create the array
        int[] numbers = new int[size];

        // Get the elements of the array
        System.out.println("Enter " + size + " integers:");
        for (int i = 0; i < size; i++) {
            numbers[i] = scanner.nextInt();
        }

        // Get the target number
        System.out.print("Enter the target number: ");
        int target = scanner.nextInt();

        // Count occurrences of the target number
        int count = 0;
        for (int num : numbers) {
            if (num == target) {
                count++;
            }
        }

        // Print the count
        System.out.println("The number " + target + " appears " + count + " times in the array.");

        // Close the scanner
        scanner.close();
    }    
}
