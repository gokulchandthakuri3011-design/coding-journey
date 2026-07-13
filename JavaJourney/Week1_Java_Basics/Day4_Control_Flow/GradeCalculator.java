package Week1_Java_Basics.Day4_Control_Flow;


/*
Grade Calculator: Take a score (0-100) and print the corresponding grade (A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: below 60).

**Sample:**
```
Enter your score: 85
Your grade is: B
```
*/

import java.util.Scanner;


public class GradeCalculator {

    public static void main(String[] args) {
        
        // Creating a Scanner object to read user input
        Scanner scanner = new Scanner(System.in);

        // Prompting the user to enter the score
        System.out.print("Enter your score: ");
        int score = scanner.nextInt();

        // Calling the method to calculate and print the grade
        String grade = calculatedGrade(score);
        System.out.println("Your grade is: " + grade);

        // Closing the scanner
        scanner.close();
    }

    // method to calculate the grade based on score
    public static String calculatedGrade(int score) {

        // Validating the score input
        if (score < 0 || score > 100) {
            return "Invalid score. Please enter a score between 0 and 100.";
        } else if (score >= 90) {
            return "Grade A";
        } else if (score >= 80) {
            return "Grade B";
        } else if (score >= 70) {
            return "Grade C";
        } else if (score >= 60) {
            return "Grade D";
        } else {
            return "Grade F";
        }
    }

    
}
