package Week1_Java_Basics.Week1_Practice_Review;

import java.util.Scanner;

public class BasicNumberToolbox {

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    // Read the two numbers once and reuse them inside the loop
    System.out.print("Enter the first number: ");
    double num1 = scanner.nextDouble();

    System.out.print("Enter the second number: ");
    double num2 = scanner.nextDouble();

    int choice;

    // Keep showing the menu until the user chooses to exit
    do {
      showMenu();

      System.out.print("Choose an operation (1-8): ");
      choice = scanner.nextInt();

      switch (choice) {
        case 1:
          add(num1, num2);
          break;
        case 2:
          subtract(num1, num2);
          break;
        case 3:
          multiply(num1, num2);
          break;
        case 4:
          divide(num1, num2);
          break;
        case 5:
          remainder(num1, num2);
          break;
        case 6:
          checkEvenOdd(num1, num2);
          break;
        case 7:
          compareNumbers(num1, num2);
          break;
        case 8:
          System.out.println("Exiting the program. Goodbye!");
          break;
        default:
          System.out.println("Invalid choice. Please select a valid option (1-8).");
      }

    } while (choice != 8); // Checks if the user wants to exit the loop

    scanner.close();
  }

  // Show the menu options to the user
  public static void showMenu() {
    System.out.println("\n=== Number Toolbox Menu ==="); // Here \n ia used to add a newline before the menu for the better readability
    System.out.println("1. Add");
    System.out.println("2. Subtract");
    System.out.println("3. Multiply");
    System.out.println("4. Divide");
    System.out.println("5. Remainder");
    System.out.println("6. Check Even/Odd");
    System.out.println("7. Compare Numbers");
    System.out.println("8. Exit");
  }

  public static void add(double num1, double num2) {
    double sum = num1 + num2;
    System.out.println("Sum: " + String.format("%.2f", sum));
  }

  public static void subtract(double num1, double num2) {
    // Use absolute value so the result is never negative
    double difference = Math.abs(num1 - num2); // Math.abs() is a built-in method returning absolute (positive) value of a number
    System.out.println("Difference: " + String.format("%.2f", difference));
  }

  public static void multiply(double num1, double num2) {
    double product = num1 * num2;
    System.out.println("Product: " + String.format("%.2f", product));
  }

  public static void divide(double num1, double num2) {
    if (num2 == 0) {
      System.out.println("Error: Division by zero is not allowed.");
    } else {
      // Works for both integers and decimals because the values are doubles
      double quotient = num1 / num2;
      System.out.println("Quotient: " + String.format("%.2f", quotient));
    }
  }

  public static void remainder(double num1, double num2) {
    if (num2 == 0) {
      System.out.println("Error: Division by zero is not allowed.");
    } else {
      double remainder = num1 % num2;
      System.out.println("Remainder: " + String.format("%.2f", remainder));
    }
  }

  public static void checkEvenOdd(double num1, double num2) {
    if (num1 == (int) num1 && num2 == (int) num2) {
      int a = (int) num1;
      int b = (int) num2;

      if (a % 2 == 0) {
        System.out.println(a + " is even.");
      } else {
        System.out.println(a + " is odd.");
      }

      if (b % 2 == 0) {
        System.out.println(b + " is even.");
      } else {
        System.out.println(b + " is odd.");
      }
    } else {
      System.out.println("Only whole numbers can be checked for even/odd.");
    }
  }

  public static void compareNumbers(double num1, double num2) {
    if (num1 > num2) {
      System.out.println("First number is greater.");
    } else if (num2 > num1) {
      System.out.println("Second number is greater.");
    } else {
      System.out.println("Both numbers are equal.");
    }
  }
}
