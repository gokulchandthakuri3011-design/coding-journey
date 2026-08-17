package Week1_Java_Basics.Day7_Methods;


/*
1. Student Score Analyzer
   - Read an integer `n` for how many scores you will enter.
   - Read `n` exam scores into an `int[] scores` array.
   - Write `double calculateAverage(int[] arr)` to compute the average using a loop.
   - Write `int findMax(int[] arr)` to return the highest score.
   - Write `int countPassing(int[] arr, int passingScore)` to return how many scores are >= `passingScore`.
   - In `main`, print the average, highest score, and passing count.
*/

import java.util.Scanner;

public class Day7_Task1 {

    // Main method to get input and call the other methods
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // Creating a Scanner Obj to read input
        int[] scores = null; // Declare array outside the if block
        System.out.print("Enter the number of scores: ");
        // Check if the input is an  positive integer
        if (scanner.hasNextInt()) {
            // Read the number of scores
            int n = scanner.nextInt();
            if (n >= 0) {
                scores = new int[n]; // Creating an array to hold the scores
                System.out.print("Enter the scores: ");
                // Read scores into the array
                for (int i = 0; i < n; i++) {
                    scores[i] = scanner.nextInt();
                }
            } else {
                System.out.println("Please enter a non-negative integer for the number of scores.");
                scanner.next(); // Clear the invalid input
            }
        } else {
            System.out.println("Invalid input. Please enter an integer for the number of scores. ");
            scanner.next(); // Clear the invalid input
        }
        // Calling the methods to print the average, highest score, and passing count
        System.out.println("Average score: " + calculateAverage(scores));
        System.out.println("Highest score: " + findMax(scores));

        // Assuming a passing score of 60
        System.out.println("Number of passing scores (>= 60): " + countPassing(scores));

        // Closing the scanner
        scanner.close();
    }

    // Method to calculate the average score
    public static double calculateAverage(int[] arr) {
        if (arr.length == 0) {
            return 0; // Avoid division by zero
        }
        int sum = 0;
        for (int score : arr) {
            sum += score; // Summing up the socres
        }
        return (double) sum / arr.length; // Returning the average
    }

    // Method to find the maximum score
    public static int findMax(int[] arr) {
        if (arr.length == 0) {
            return 0; // Return 0 if the array is empty
        }
        int max = arr[0]; // Initialize max with the first element
        for (int score : arr) {
            if (score > max) {
                max = score; // Update max if higher score is found
            }
        }
        return max;
    }
    
    // Method to count how many scores are passing
    public static int countPassing(int[] arr) {
        int passingCount = 0;
        for (int score : arr) {
            if (score >= 60) {
                passingCount++; // Increment the count if the score is passing
            }
        }
        return passingCount;
    }
}
