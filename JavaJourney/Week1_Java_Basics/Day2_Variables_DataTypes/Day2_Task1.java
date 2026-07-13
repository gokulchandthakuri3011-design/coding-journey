/*
### Exercise 1: Create a User Profile
Write a program that stores your personal information in variables and then prints it out in a formatted way.
1. Create a `String` variable for your full name.
2. Create an `int` variable for your age.
3. Create a `double` variable for your height in meters (e.g., 1.75).
4. Create a `boolean` variable representing whether you like coffee (`true` or `false`).
5. Create a `char` variable for your favorite letter.
6. Use `System.out.println()` to print a profile summary to the console using your variables.

*Example Output:*
```text
--- User Profile ---
Name: John Doe
Age: 28
Height: 1.82m
Likes Coffee: true
Favorite Letter: J
```
*/

package Week1_Java_Basics.Day2_Variables_DataTypes;

public class Day2_Task1 {
    public static void main(String[] args) {

        // Exercise 1: Creating a user profile
        String name = "Gokul Chand";
        int age = 22;
        double height = 5.10; // in feet
        boolean likesCoffee = true;
        char favouriteLetter = 'L';

        // Displaying the user profile
        System.out.println("-----User Profile-----");
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Height: " + height + " feet");
        System.out.println("Likes Coffee: " + likesCoffee);
        System.out.println("Favourite Letter: " + favouriteLetter);
    }
}
