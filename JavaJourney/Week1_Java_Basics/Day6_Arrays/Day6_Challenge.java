/*
### Challenge Assignment: Grade Calculator
Write a program that:
- Takes an array of student marks (0-100)
- Counts the number of students in each grade: A, B, C, D, F
- Prints the count for each grade
*/

package Week1_Java_Basics.Day6_Arrays;

import java.util.Scanner;

public class Day6_Challenge {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("---- Grade Calculator ---");

        // Creating an array for student scores
        int[] scores = new int[10];

        // Asking user for 10 student scores between (1-100)
        System.out.print("Enter the 10 student scores (1-100): ");

        // Initializing the array
        for (int i=0; i < scores.length; i++) {
            scores[i] = scanner.nextInt();
        }

        int countA = 0, countB = 0, countC = 0, countD = 0, countF = 0;

        for (int score : scores) {
            if (score >= 90) {
                countA++;
            } else if (score >= 80) {
                countB++;
            } else if (score >= 70) {
                countC++;
            } else if (score >= 60) {
                countD++;
            } else {
                countF++;
            }
        }

        System.out.println("Grade A: " + countA);
        System.out.println("Grade B: " + countB);
        System.out.println("Grade C: " + countC);
        System.out.println("Grade D: " + countD);
        System.out.println("Grade F: " + countF);

        scanner.close();
    }
}
