package Week1_Java_Basics.Day3_Operators_and_Input;

/*
ask 2: The Even/Odd Checker
1. Declare an `int` variable named `myNumber`.
2. Use the modulus operator (`%`) to determine if the number is even or odd. 
   *(Hint: An even number leaves a remainder of 0 when divided by 2.)*
3. Print a boolean expression that evaluates to `true` if the number is even.
*/


public class Day3_Task2 {
    public static void main(String[] args) {

        // The Even/Odd Checker

        // Declaring and initializing an int variable
        int myNumber = 15;

        // Checking if the number is even
        boolean isEven = (myNumber % 2 == 0);

        // Printing the result
        System.out.println("Is " + myNumber + " an even number? " + isEven);

    }
    
}
