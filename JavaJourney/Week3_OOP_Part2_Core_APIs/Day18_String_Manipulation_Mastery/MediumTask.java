package Week3_OOP_Part2_Core_APIs.Day18_String_Manipulation_Mastery;

/*
### Medium
4. Write a method `countWords(String s)` that returns the number of words in a sentence (words are separated by spaces).

5. Write a method `removeDuplicates(String s)` that returns a new string with consecutive duplicate characters removed. Example: `"aabbcc"` → `"abc"`.

6. Write a method `capitalizeWords(String s)` that capitalizes the first letter of each word. Example: `"hello world"` → `"Hello World"`.

7. Write a method `mostFrequentChar(String s)` that returns the character that appears most frequently in the string.
*/

import java.util.Scanner;

public class MediumTask {
    // Method to count the number of words in a sentence and return the count
    public static int countWords(String s) {
        if (s == null || s.trim().isEmpty()) { // null checks if variable 's' is pointed to 'no object'
            return 0;
        }
        String[] words = s.trim().split("\\s+");
        return words.length;
    }

    // Method to remove consecutive duplicate characters from a string and return the new string
    // Case-insensitive: treats 'A' and 'a' as the same character
    public static String removeDuplicates(String s) {
        if (s == null || s.isEmpty()) {
            return s;
        }
        // Convert to lowercase for comparison (but keep original case in output)
        String lower = s.toLowerCase();
        StringBuilder result = new StringBuilder();
        result.append(s.charAt(0));
        for (int i = 1; i < lower.length(); i++) {
            // Compare lowercase versions to detect duplicates
            if (lower.charAt(i) != lower.charAt(i - 1)) {
                result.append(s.charAt(i));
            }
        }
        return result.toString();
    }

    // Method to capitalize the first letter of each word in a string and return the new string
    public static String capitalizeWords(String s) {
        if (s == null || s.isEmpty()) {
            return s;
        }
        String[] words = s.split("\\s+");
        StringBuilder capitalized = new StringBuilder();
        for (String word : words) {
            if (!word.isEmpty()) {
                capitalized.append(word.toUpperCase());
            }
        }
        return capitalized.toString();
    }

    // Method to find the most frequent character in a string and return it
    // Case-insensitive: treats 'A' and 'a' as the same character
    // Only counts LETTERS (a-z), ignores spaces and special characters
    public static char mostFrequentChar(String s) {
        if (s == null || s.isEmpty()) {
            // '\0' is escape sequence: \ means "special character", 0 = null character (ASCII 0)
            // Invisible character returned when string is empty to signal "no result"
            return '\0';
        }
        // Convert to lowercase for case-insensitive comparison
        String lower = s.toLowerCase();
        // Create array with 26 slots (one for each letter a-z)
        // 'a'=97, 'z'=122, so we use index 0-25 mapping: a→0, b→1, ... z→25
        int[] frequency = new int[26]; 
        // Count how many times each LETTER appears (case-insensitive, ignore non-letters)
        for (int i = 0; i < lower.length(); i++) {
            char ch = lower.charAt(i);
            // Only count if it's a letter (a-z)
            if (ch >= 'a' && ch <= 'z') {
                // Map letter to index: 'a'→0, 'b'→1, ..., 'z'→25
                frequency[ch - 'a']++;
            }
            // Ignore spaces, punctuation, numbers, and special characters
        }
        // Find the letter with maximum count
        int maxFreq = 0;
        char mostFrequent = 'a';
        for (int i = 0; i < 26; i++) {
            // Compare each letter's count with current maximum
            if (frequency[i] > maxFreq) {
                maxFreq = frequency[i];
                mostFrequent = (char) ('a' + i);  // Convert index back to letter
            }
        }
        return mostFrequent;
    }

    // Main method to test the above methods
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a string: ");
        String input = scanner.nextLine();

        int wordCount = countWords(input);
        System.out.printf("Number of words in '%s': %d%n", input, wordCount);

        String noDuplicates = removeDuplicates(input);
        System.out.printf("String after removing duplicates: %s%n", noDuplicates);

        String capitalized = capitalizeWords(input);
        System.out.printf("Capitalized String: %s%n", capitalized);

        char mostFrequent = mostFrequentChar(input);
        System.out.printf("Most frequent character in '%s': %c%n", input, mostFrequent);

        // Close the scanner
        scanner.close();
    }
}
