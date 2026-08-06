/*
### Exercise 6: `break` and `continue`
Write a loop from 1 to 10. Inside the loop:
* if the number is 3, use `continue` to skip printing it.
* if the number is 8, use `break` to stop the loop entirely.
*/

package Week1_Java_Basics.Day5_Loops;

public class Day5_Task6 {
    public static void main(String[] args) {
        // Writing a loop from 1 to 10
        System.out.println(" --Numbers (1-10)-- ");
        for (int x = 1; x <= 10; x++) {
            if (x == 3) {
                continue;
            }
            if (x == 8) {
                break;
            }
            System.out.println(x);
        }
    }
}
