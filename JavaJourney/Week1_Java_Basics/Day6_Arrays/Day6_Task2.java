package Week1_Java_Basics.Day6_Arrays;


/*
### Assignment 2: Find Largest and Smallest
Write a program that:
- Takes an array of integers as input
- Finds and prints the largest number
- Finds and prints the smallest number
- Prints the count of each

**Example:**
```
Array: [15, 45, 30, 90, 10]
Largest: 90
Smallest: 10
*/ 
import java.util.Arrays;

public class Day6_Task2 {
    public static void main(String[] args) {

        // Largest and Smallest number in an array

        // Sample array of integers
        int[] numbers = {15, 45, 30, 90, 10};

        // Initialize largest and smallest with the first element of the array
        int largest = numbers[0];
        int smallest = numbers[0];

        // iterate through the array to find largest and smallest
        for (int i = 1; i < numbers.length; i++) {
            if (numbers[i] > largest) {
                largest = numbers[i];
            } else if (numbers[i] < smallest) {
                smallest = numbers[i];
            }
        }

        // Print the results
        System.out.println("Array: " + Arrays.toString(numbers));
        System.out.println("Largest: " + largest);
        System.out.println("Smallest: " + smallest);
    }

}
