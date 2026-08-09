package Week1_Java_Basics.Day3_Operators_and_Input;

/*
### Task 3: Grade Evaluator
1. Declare an `int` variable named `score` and assign it a value between 0 and 100.
2. Write boolean expressions to check the following and print the results:
   * Is the score a passing grade? (Let's say passing is 60 or higher)
   * Is the score an 'A' grade? (90 or higher)
   * Is the score invalid? (Less than 0 OR greater than 100)
*/

public class Day3_Task3 {
    public static void main(String[] args) {

        System.out.println("---- Grade Evaluator ----");
        int score = 78;

        // Checking the grade using boolean
        boolean isPassingGrade = (score >= 60);
        boolean isScoreA = (score >= 90);
        boolean isScoreInvalid = (score < 0 || score > 100);

        // Printing the result
        System.out.println("Is Student Pass or Fail: " + isPassingGrade);
        System.out.println("Is the score A: " + isScoreA);
        System.out.println("Is the score invalid: " + isScoreInvalid);
    }

}
