/*
Project D — Student Scores Analyzer
- Objectives: arrays, loops, methods, aggregation (sum/avg/max/min), input validation.
- Requirements:
  - Read N student names and scores (N from user), store in parallel arrays or a simple `Student` class.
  - Compute average, highest, lowest, and count of passing/failing students using methods.
  - Print a formatted report.
- Guiding questions (covering all topics):
  - How do you allocate and iterate arrays for dynamic N?
  - Which methods did you write for calculations and why?
  - How do you handle invalid numeric input and re-prompt the user?
  - How would you refactor to use a `Student` class instead of parallel arrays?
- Extensions: sort students by score; save report to a file; compute grade distribution.
- Deliverables: `StudentAnalyzer.java`, optional `Student.java`, README.
*/

package Week1_Java_Basics.Week1_Practice_Review;
import java.util.Scanner;

public class StudentAnalyzer {
    public static void main(String[] args) {

      Scanner scanner = new Scanner(System.in);

      // Asking user how many students are there in class
      int num = 0;
      while (true) {
        System.out.print("Enter the number of students: ");
        if (scanner.hasNextInt()) {
          num = scanner.nextInt();
          if (num > 0) break;
          System.out.println("Please enter a positive number!");
        } else {
          System.out.println("Please enter a valid number!");
          scanner.next(); // eats the invalid input(buffer cleaner)
        }
      }
      scanner.nextLine(); // eats the stray newline(buffer cleaner)

      // Creating 2 parallel arrays to store student names and grades
      String[] names = new String[num];
      double[] scores = new double[num];
      for (int i = 0; i < num; i++) {
        names[i] = getNames(scanner, i);
        scores[i] = getScores(scanner, i);
      }

      // Calling methods 
      double average = findAverage(scores);
      double highestScore = findMax(scores);
      double lowestScore = findMin(scores);
      int passedNumStudents = findPassed(scores);
      int failedNumStudents = scores.length - passedNumStudents;

      // Print formatted report
      System.out.println("\n========== Student Scores Report ==========");
      System.out.printf("%-15s %-10s%n", "Name", "Score");
      System.out.println("-------------------------------------------");
      for (int i = 0; i < num; i++) {
        System.out.printf("%-15s %-10.2f%n", names[i], scores[i]);
      }
      System.out.println("-------------------------------------------");
      System.out.printf("Average Score:  %.2f%n", average);
      System.out.printf("Highest Score:  %.2f%n", highestScore);
      System.out.printf("Lowest Score:   %.2f%n", lowestScore);
      System.out.printf("Passed:         %d%n", passedNumStudents);
      System.out.printf("Failed:         %d%n", failedNumStudents);
      System.out.println("===========================================");
    }

    // Methods to get Arrays data
    public static String getNames(Scanner scanner, int index) {
      String name;
      while (true) {
        System.out.print("Enter name for student " + (index + 1) + ": ");
        name = scanner.nextLine().trim();
        if (!name.isEmpty()) break;
        System.out.println("Name cannot be empty. Please try again.");
      }
      return name;
    }

    public static double getScores(Scanner scanner, int index) {
      double score;
      while (true) {
        System.out.print("Enter score for student " + (index + 1) + ": ");
        if (scanner.hasNextDouble()) {
          score = scanner.nextDouble();
          scanner.nextLine();
          if (score >= 0 && score <= 100) break;
          System.out.println("Score must be between 0 and 100. Please try again.");
        } else {
          System.out.println("Please enter a valid number!");
          scanner.next();
        }
      }
      return score;
    }

    // Method to find average, highest, lowest & number of passing/failing students
    public static double findAverage(double[] arr) {
      double sumScore = 0;
      for (double score: arr) {
        sumScore += score;
      }
      return sumScore/arr.length;
    }

    public static double findMax(double[] arr) {
      double highest = arr[0];
      for (int i=0; i<arr.length; i++) {
        if (arr[i] > highest) {
          highest = arr[i];
        }
      }
      return highest;
    }

    public static double findMin(double[] arr) {
      double lowest = arr[0];
      for (int i=0; i<arr.length; i++) {
        if (arr[i] < lowest) {
          lowest = arr[i];
        }
      }
      return lowest;
    }

    public static int findPassed(double[] arr){
      int count = 0;
      for (double score: arr) {
        if (score >= 60) {
          count++;
        }
      }
      return count;
    }

}