package Week1_Java_Basics.Day5_Loops;


/*
### Practice Exercise 5.2
Print the multiplication table (1-10) for a given number.

**Sample:**
```
Enter a number: 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50
*/
 import java.util.Scanner;

public class MultiplicationTable {
    public static void main(String[] args) {

        // Scanner Object
        Scanner scanner = new Scanner(System.in); // System.in is where the input data is coming from i.e, keyboard

        // Prompting user for input number
        System.out.print("Enter a number of choice: ");
        int num = scanner.nextInt();

        // Statement to print the multiplication table from 1 to 10
        System.out.println("Multiplication Table of " + num);

        // Using For loop 
        for (int i = 1; i <= 10; i++) {
            int result = num * i;
            System.out.println(num + " x " + i + " = " + result);
        }

        // Scanner close
        scanner.close();
    }   
}
