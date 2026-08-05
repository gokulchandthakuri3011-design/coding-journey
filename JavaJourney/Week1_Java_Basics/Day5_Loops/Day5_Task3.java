/*
### Exercise 3: Even Numbers Only
Write a loop that prints only even numbers from 2 to 20. 
Use either `if` inside the loop or step by 2.
*/

package Week1_Java_Basics.Day5_Loops;

public class Day5_Task3 {
    public static void main(String[] args) {
        System.out.println(" Even Numbers Only ");

        for (int i=2; i<=20; i++) {
            if (i % 2 == 0) {
                System.out.println(i);
            } 
        }
    }
}
