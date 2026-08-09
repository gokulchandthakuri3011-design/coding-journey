package Week1_Java_Basics.Day3_Operators_and_Input;

/*
### Task 4: Eligibility Check
1. You are checking if someone is eligible for a special discount. 
2. They are eligible if they are a student (`boolean isStudent = true;`) OR if they are a senior citizen (`int age = 68;` - consider senior as 65 or older).
3. Write a logical expression using `||` to check eligibility and print the `boolean` result.
*/

public class Day3_Task4 {
    public static void main(String[] args) {
        System.out.println("---- Eligibility Checker ----");
        boolean isStudent = true;
        int age = 68;

        // Checking eligibility for special discount
        boolean isEligible = (isStudent == true) || (age >= 65);
        System.out.println("Is the person eligible for a special discount?: " + isEligible);
    }
}
