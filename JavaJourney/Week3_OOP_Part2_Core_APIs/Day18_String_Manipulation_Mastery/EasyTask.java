package Week3_OOP_Part2_Core_APIs.Day18_String_Manipulation_Mastery;

/*
### Easy
1. Write a method `countVowels(String s)` that returns the number of vowels (`a, e, i, o, u`) in a string.

2. Write a method `reverseString(String s)` that returns the reversed version of a string.

3. Write a method `isPalindrome(String s)` that checks if a string reads the same forwards and backwards 
   (e.g., `"racecar"`, `"madam"`).
*/

import java.util.Scanner;

public class EasyTask {
    // Method to count the number of vowels in a string
    public static int countVowels(String s) {
        int count = 0;
        for (char c : s.toLowerCase().toCharArray()) {
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                count++;
            }
        }
        return count;
    }

    // Method to reverse a string
    public static String reverseString(String s) {
        StringBuilder reversed = new StringBuilder(); // Alternative Methods
        for (int i = s.length() - 1; i >= 0; i--) {   // Using StringBuilder for effective string manipulation
            reversed.append(s.charAt(i));             // return new StringBuilder(s).reverse().toString();
        }
        return reversed.toString();
    }

    // Method to check if a string is a palindrome
    public static boolean isPalindrome(String s) {
        String lower = s.toLowerCase();
        String reversed = reverseString(lower);
        return lower.equals(reversed);
    }

    // Main method to test the above methods
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a string: ");
        String input = scanner.nextLine();

        int vowelCount = countVowels(input);
        System.out.printf("Number of vowels in '%s': %d%n", input, vowelCount);

        String reversed = reverseString(input);
        System.out.printf("Reversed String: %s%n", reversed);

        boolean palindromeCheck = isPalindrome(input);
        System.out.printf("Is '%s' a palindrome? %b%n", input, palindromeCheck);

        // Close the scanner
        scanner.close();
    }
}
