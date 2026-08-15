package Week1_Java_Basics.Day6_Arrays;


/*
### Assignment 1: Array Sum and Average
Write a program that:
- Declares an array of 5 integers
- Calculates and prints the sum of all elements
- Calculates and prints the average of all elements

**Example:**
```
Array: [10, 20, 30, 40, 50]
Sum: 150
Average: 30.0
*/

import java.util.Scanner;
import java.util.Arrays;

public class Day6_Task1 {
    public static void main(String[] args) {

        // Array Sum and Average

        // Declaring variables to hold the sum and average
        int sum = 0;
        double average = 0.0;

        // Declaring an array of 5 integers
        int[] numbers = new int[5];

        // Taking input from the user
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter 5 integers: ");

        // Filling the array with user input
        for (int i = 0; i < numbers.length; i++) {
            numbers[i] = scanner.nextInt();
        }

        // Calculating the sum
        for (int num : numbers) {
            sum += num;
        }

        // Calculating the average
        average = (double) sum / numbers.length;

        // Printing the results
        System.out.println("Array: " + Arrays.toString(numbers)); // Using Arrays.toString to print the array
        System.out.println("Sum: " + sum);
        System.out.println("Average: " + String.format("%.2f", average));

        // Closing the scanner
        scanner.close();
    }
    
}
