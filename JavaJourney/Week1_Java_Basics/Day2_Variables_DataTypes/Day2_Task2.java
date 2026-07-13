/*
### Exercise 2: The Swapping Challenge
This is a classic programming puzzle!
1. Create an `int` variable named `a` and set it to `10`.
2. Create an `int` variable named `b` and set it to `20`.
3. **Your Goal:** Write code that swaps the values of `a` and `b`, so that when you print them out, `a` is 20 and `b` is 10. 
*/ 

package Week1_Java_Basics.Day2_Variables_DataTypes;

public class Day2_Task2 {
    public static void main(String[] args) {
        
        // Creating variable a and b
        int a = 10;
        int b = 20;

        // Creating a temporary variable to hold the value of a during the swap
        int temp = a; // temp now holds the values of a (10)
        a = b;        // a now holds the value of b (20)
        b = temp;     // b now holds the value of temp (10)

        // Printing the swapped values
        System.out.println("Value of a after swapping: " + a); // Should print 20
        System.out.println("Value of b after swapping: " + b); // Should print 10
    }
    
}
