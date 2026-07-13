package Week1_Java_Basics.Day4_Control_Flow;


/*
### Task 1: Even or Odd Checker
Write a program that declares an integer variable `number` and assigns it a value. 
Use an `if-else` statement (and the modulo operator `%` from Day 3) to print whether the number is "Even" or "Odd".
*/

public class Day4_Task1 {
    public static void main(String[] args) {

        // Even or Odd Checker

        // Declare an integer variable and assign it a value
        int number = 16; // You can change this value to test with different numbers

        // Using if-else statement to check if the number is even or odd
       /*  if (number % 2 == 0) {
            System.out.println("The number " + number + " is Even.");
        } else {
            System.out.println("The number " + number + " is Odd.");
        } */

        // using ternary operator to check if the number is even or odd
        String result = (number % 2 != 0) ? "Odd" : "Even";
        System.out.println("The number " + number + " is " + result + ".");
    }
    
}
