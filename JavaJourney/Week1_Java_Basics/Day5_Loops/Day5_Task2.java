package Week1_Java_Basics.Day5_Loops;


/*
### Exercise 2: Sum of Numbers
Use a loop to calculate the sum of the numbers from 1 to 20.
Print the final result.
*/

public class Day5_Task2 {
    public static void main(String[] args) {

        // Sum of Numbers
        
        // Initialize sum variable
        int sum = 0;

        // Loop from 1 to 20 and add each number to sum
        for (int i = 1; i <= 20; i++) {
            sum += i; // sum = sum + i
        }

        // Print the final result
        System.out.println("The sum of numbers from 1 - 20 is: " + sum);
    }
}
