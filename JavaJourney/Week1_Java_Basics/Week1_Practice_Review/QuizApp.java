/*
Project C — Quiz & Decision Maker
- Objectives: arrays, loops, input, conditionals, methods, basic scoring or branching logic.
- Requirements:
  - Represent 3–5 questions and accepted answers in arrays.
  - Ask the user questions, collect answers, compute a score or choose a result based on responses.
  - Print a final result with feedback.
- Guiding questions (covering all topics):
  - How are questions and answers stored and accessed in arrays?
  - Which loop did you use to iterate questions and why?
  - How do you compare `String` answers correctly?
  - Which methods encapsulate asking a question, validating an answer, and scoring?
- Extensions: load questions from a file; randomize questions; add timed answers.
- Deliverables: `QuizApp.java`, optional `questions.txt`, README.
*/
package Week1_Java_Basics.Week1_Practice_Review;

import java.util.Scanner;

public class QuizApp {
    public static void main(String[] args) {
      Scanner scanner = new Scanner(System.in);

      // Introducing 2 parallel arrays (questions & answers)
      String[] questions = {"What is the name of your country?", "Capital Of Nepal", "Highest Mountain of Nepal", "Birthplace","Main Festival in Nepal"};
      String[] answers = {"Nepal", "Kathmandu", "Mount Everest", "Kailali", "Dashain & Tihar"};

      // A list to hold user answers
      String [] userAnswers = new String[questions.length];
      for (int i = 0; i < questions.length; i++) {
        askQuestions(questions[i]);
        userAnswers[i] = getUserAnswer(scanner);
      }

      // A list to hold the validity of answers
      boolean [] answersValidity = new boolean[questions.length];
      for (int i = 0; i < answers.length; i++) {
        answersValidity[i] = checkAnswer(answers[i],userAnswers[i]);
      }
      
      System.out.println("\n ==== Quiz App ==== \n");
      for (int i = 0; i < questions.length; i++) {
        printResult(i, questions[i], answers[i], userAnswers[i], answersValidity[i]);
        System.out.println();
      }
      System.out.println("Closing Program ............");
      scanner.close();
    }

    // Asking user questions
    public static void askQuestions(String question) {
      System.out.println(question);
      System.out.print("Your answers: ");
    }
    

    // Getting user answers
    public static String getUserAnswer(Scanner scanner) {
      return scanner.nextLine().trim();
    }

    // Checking user answers
    public static boolean checkAnswer(String answer, String userAnswer) {
      return answer.equalsIgnoreCase(userAnswer);
    }

    // Printing user answers validity
    public static void printResult(int i, String question, String answer, String useranswer, boolean answervalid) {
      System.out.println("Question to User: " + i + ". " + question);
      System.out.println("User Answer: " + useranswer);
      System.out.println("Original Answer: " + answer);
      System.out.println("Is the User Ans True?: " + answervalid);
    }


}
