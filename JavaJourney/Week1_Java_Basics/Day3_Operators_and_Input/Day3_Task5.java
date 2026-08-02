/*
### Task 5: User Input Practice
1. Use `Scanner` to read a user's `name` and `favoriteNumber` from the console.
2. Print a greeting that includes the name and the number.
3. Example output: `Hello Maya, your favorite number is 8.`
*/

package Week1_Java_Basics.Day3_Operators_and_Input;
import java.util.Scanner;

public class Day3_Task5 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Prompting user for their name
        System.out.print("Enter your name: ");
        String name = scanner.nextLine();

        // Prompting user for their favourite number
        System.out.print("Enter your favourite number: ");
        int favNumber = scanner.nextInt();

        // Printing the greeting message
        System.out.println("Hello " + name + ", your favourite number is " + favNumber + " .");

        // Closing the scanner
        scanner.close();
    }
}
