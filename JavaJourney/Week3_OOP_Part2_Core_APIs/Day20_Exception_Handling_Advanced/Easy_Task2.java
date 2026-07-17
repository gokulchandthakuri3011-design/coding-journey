package Week3_OOP_Part2_Core_APIs.Day20_Exception_Handling_Advanced;

/*
**2. File Reader with throws**
- `readFirstLine(String path) throws FileNotFoundException`
- Call from main with try-catch; test existing and missing files
*/

import java.io.FileNotFoundException;
import java.io.File;
import java.util.Scanner;

public class Easy_Task2 {
    public static void readFirstLine(String path) throws FileNotFoundException {
        File file = new File(path);
        Scanner scanner = new Scanner(file); // Here Scanner class throw the exception automatically so we don't need (throw new......)
        if (scanner.hasNextLine()) {
            System.out.println("First Line: " + scanner.nextLine());
        }
        scanner.close();
    }

    public static void main(String[] args) {
        // Testing existing file
        try {
            readFirstLine("Week3_OOP_Part2_Core_APIs/Day20_Exception_Handling_Advanced/Easy_Task1.java");
        } catch (FileNotFoundException e) {
            System.out.println("Error: " + e.getMessage());
        }

        // Testing missing file
        try {
            readFirstLine("randomFile.txt");
        } catch (FileNotFoundException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
