package Week1_Java_Basics.Week1_Practice_Review;


/*
Project A — Personal Profile App
- Objectives: practice input, variables, conditionals, methods, and simple output formatting.
- Requirements:
  - Read user's name, age, city, and favorite letter.
  - Validate age (non-negative) and handle empty name input.
  - Print a formatted profile and a short message (e.g., birthday or age-based category).
- Guiding questions (covering all topics):
  - How do you compile and run the program from the command line?
  - Which types did you choose for each input and why?
  - How do you validate input and handle invalid values?
  - Which helper methods did you create and what do they return?
- Extensions: save profile to a simple text file; allow multiple profiles in an array and print a summary.
- Deliverables: `ProfileApp.java`, optional `profiles.txt`, small README describing usage.
*/

import java.util.Scanner;

public class ProfileApp {
  
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    // Use helper methods (instead of calling scanner.nextLine()/nextInt() here)
    // Encapsulate prompting: put the prompt, input reading, and validation
    // into separate helper methods so main() remains simple and each
    // input's logic is isolated and reusable.
    String name = readValidName(scanner);
    int age = readValidAge(scanner);
    String city = readCity(scanner);
    char favLetter = readFavoriteLetter(scanner);

    String message = getAgeMessage(age);

    displayInfo(name, age, city, favLetter, message);

    scanner.close();
  }

  private static String readValidName(Scanner scanner) {
    while (true) { // Keep asking until valid
      System.out.print("Enter user's name: ");
      String name = scanner.nextLine().trim(); // .trim() removes leading/trailing spaces
      if (validateName(name)) { // ✓ Valid input
        return name; // Exit loop - return the valid name
      }
      System.out.println("name cannot be empty. Please enter a valid name.");
      // Loop continues - ask again
    }
  }

  private static int readValidAge(Scanner scanner) {
  while (true) { 
    System.out.print("Enter user's age: ");
    if (!scanner.hasNextInt()) { // Checks whether the next token in input is an integer (only looks ahead)
      System.out.println("Please enter a valid whole number for age.");
      scanner.nextLine(); // Reads and discards the rest of the current input line
      continue;
    }
    int age = scanner.nextInt();
    scanner.nextLine(); // consume newline left by nextInt()
    if (validateAge(age)) {
      return age;
    }
    System.out.println("Age must be a positive number. Please enter again.");
  }
}

private static String readCity(Scanner scanner) {
  System.out.print("Enter user's city: ");
  return scanner.nextLine().trim();
}

private static char readFavoriteLetter(Scanner scanner) {
  while (true) {
    System.out.print("Enter user's favorite letter: ");
    String input = scanner.nextLine().trim();
    if (input.isEmpty()) {
      System.out.println("Please enter at least one letter.");
      continue;
    }
    return input.charAt(0); // Takes and returns the character at index 0 from the entered String
  }
}

public static boolean validateName(String name) {
  return name != null && !name.trim().isEmpty(); // prevents NullPointException and checks if resulting String has length 0
}

public static boolean validateAge(int age) {
  return age >= 0;
}

public static String getAgeMessage(int age) {
  if (age < 13) {
    return "You are a young explorer with a bright future!";
  } else if (age < 18) {
    return "You are a teenager with lots of energy and learning ahead.";
  } else if (age < 30) {
    return "You are a young adult with many opportunities.";
  } else {
    return "You have valuable experience and a strong story to share.";
  }
}


public static void displayInfo(String name, int age, String city, char favLetter, String message) {
  System.out.println();
  System.out.println("----- Personal Profile -----");
  System.out.println("Name        : " + name);
  System.out.println("Age       : " + age);
  System.out.println("City        : " + city);
  System.out.println("Favourite Letter: " + favLetter);
  System.out.println();
  System.out.println("Message   : " + message);
  System.out.println("----------------------------");
  }
}
