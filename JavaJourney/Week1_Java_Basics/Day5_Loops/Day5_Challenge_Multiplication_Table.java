/*
### Challenge: Multiplication Table
Use a nested loop to print the multiplication table for 1 through 5.

**Example output:**
```
1 x 1 = 1
1 x 2 = 2
...
5 x 5 = 25
```
*/

package Week1_Java_Basics.Day5_Loops;

public class Day5_Challenge_Multiplication_Table {
    public static void main(String[] args) {
        System.out.println(" --Multiplication Table-- ");
        for (int x=1; x<=5; x++) {
            System.out.println("Multiplication Table of " + x);
            for (int y=1; y<=10; y++) {
                System.out.println(x + " x " + y + " = " + x*y);
            }
        }
    }
}
