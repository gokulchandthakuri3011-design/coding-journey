/*
### Exercise 5: Guessing Game Starter
Create a `do-while` loop that asks the user to enter a number from 1 to 5. 
If the number is not valid, the loop should ask again. 
For now, just simulate the user input by assigning a value to a variable and changing it until the loop condition becomes false.
*/

package Week1_Java_Basics.Day5_Loops;

public class Day5_Task5 {
    public static void main(String[] args) {
        int guess = 0;
        do {
            // simulating the user entering a value 
            guess = 8; // change this next time to something valid
            System.out.println("Guess: " + guess);
        } while (guess >=1 || guess <=5);
    }
}
