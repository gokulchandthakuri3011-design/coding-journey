package Week1_Java_Basics.Day4_Control_Flow;

/*
### Practice Exercise 4.2
Age Category: Take an age and print if the person is a child (< 13),
teenager (13-19), adult (20-64),
or senior (65+).
*/

import java.util.Scanner;

public class AgeCategory {
    
    public static void main(String[] args) {

        // Creating an object of Scanner
        Scanner scanner = new Scanner(System.in);

        // Prompting the user for input
        System.out.print("Enter your age: ");

        // Check if the input is a valid integer
        if (scanner.hasNextInt()) {
            int age = scanner.nextInt();

            // Check if the age is negative
            if (age < 0) {
                System.out.println("Error: Age cannot be negative.");
            } else {
                // Determine the age group using Ternary Operator
                String ageGroup = (age < 13) ? "Child" 
                                : (age <= 19) ? "Teenager" 
                                : (age <= 64) ? "Adult" 
                                : "Senior";

                // Grammatical check: "an Adult" vs "a Child/Teenager/Senior"
                String article = ageGroup.equals("Adult") ? "an" : "a"; // Using ternary operator for grammatical correctness
                System.out.println("The person is " + article + " " + ageGroup);
            }
        } else {
            System.out.println("Error: Please enter a valid integer for age.");
        }

        // Closing the scanner
        scanner.close();
    }
}
