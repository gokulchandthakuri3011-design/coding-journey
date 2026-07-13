package Week1_Java_Basics.Day4_Control_Flow;


import java.util.Scanner;

public class GradeCalculatorImproved {

    public static void main(String[] args) {
        
        // Creating a Scanner object to read user input
        Scanner scanner = new Scanner(System.in);
        int score = -1;

        // Loop until a valid integer score between 0 and 100 is entered
        while (true) {
            System.out.print("Enter your score (0-100): ");
            
            // 1. Check if the user's input is actually an integer
            if (scanner.hasNextInt()) {  // hasNextInt() prechecks if the next input is an integer
                score = scanner.nextInt();
                scanner.nextLine(); // Clear the remaining newline/buffer
                
                // 2. Validate if the score is in the correct range
                if (score >= 0 && score <= 100) {
                    break; // Exit the loop because the input is perfect!
                } else {
                    System.out.println("Error: Score must be between 0 and 100. Please try again.");
                }
            } else {
                // 3. Read and discard invalid input (like letters or command text)
                String invalidInput = scanner.nextLine();
                System.out.println("Error: '" + invalidInput + "' is not a valid integer. Please try again.");
            }
        }

        // Calling the method to calculate and print the grade
        String grade = calculatedGrade(score);
        System.out.println("Your grade is: " + grade);

        // Closing the scanner
        scanner.close();
    }

    // Method to calculate the grade based on score
    public static String calculatedGrade(int score) {
        if (score >= 90) {
            return "A";
        } else if (score >= 80) {
            return "B";
        } else if (score >= 70) {
            return "C";
        } else if (score >= 60) {
            return "D";
        } else {
            return "F";
        }
    }
}
