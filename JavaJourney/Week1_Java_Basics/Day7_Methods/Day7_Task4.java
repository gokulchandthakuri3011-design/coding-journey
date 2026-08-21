/*
4. Simple Array Statistics Menu
   - Read an integer `n`, then read `n` integers into an `int[] values` array.
   - Write `int findMin(int[] arr)` and `int findMax(int[] arr)`.
   - Write `int sumArray(int[] arr)`.
   - Write `void printArray(int[] arr)` to display all values.
   - In `main`, use a simple menu loop to let the user choose: show min, show max, show sum, show all values, or exit.
*/

package Week1_Java_Basics.Day7_Methods;
import java.util.Scanner;

public class Day7_Task4 {
   public static void main(String[] args) {
      Scanner scanner = new Scanner(System.in);
      int[] values = null;

      // Asking user for the length of array
      System.out.print("Enter the length of the array: ");
      if (scanner.hasNextInt()) {
         int n = scanner.nextInt();
         values = new int[n];

         System.out.print("Enter " + n + " numbers of values: ");
         if (scanner.hasNextInt()) {
            for (int i = 0; i < n; i++) {
               values[i] = scanner.nextInt();
            }
            int choice = 0;
            do {
               System.out.println(" --- Menu Loop ---");
               System.out.println("1. Show Min");
               System.out.println("2. Show Max");
               System.out.println("3. Show Sum");
               System.out.println("4. Show All Values");
               System.out.println("5. Exit");
               System.out.print("Enter an option from (1-5): ");
               if (scanner.hasNextInt()) {
                  choice = scanner.nextInt();
                  switch (choice) {
                     case 1:
                        System.out.println("The minimum value: " + findMin(values));
                        break;
                     case 2:
                        System.out.println("The maximum value: " + findMax(values));
                        break;
                     case 3:
                        System.out.println("The sum of values: " + sumArray(values));
                        break;
                     case 4:
                        printArray(values);
                        break;
                     case 5:
                        System.out.println("The Program is closing......");
                        break;
                     default:
                        System.out.println("Incorrect Input!");
            }
         } else {
            scanner.next();
            System.out.println("Please choose an integer from range(1-5)!");
         }
      } while (choice != 5);
         } else {
            System.out.println("Please enter only integer values!");
         }
      } else {
         scanner.next();
         System.out.println("Please enter only integer!");
      }
      
      scanner.close();

   }

   // To find minimum
   public static int findMin(int[] arr) {
      int minimum = arr[0];
      for (int i = 0; i < arr.length; i++) {
         if (arr[i] < minimum) {
            minimum = arr[i];
         }
      }
      return minimum;
   }

   // To find maximum
   public static int findMax(int[] arr) {
      int maximum = arr[0];
      for (int i = 0; i < arr.length; i++) {
         if (arr[i] > maximum) {
            maximum = arr[i];
         }
      }
      return maximum;
   }

   // To find sum
   public static int sumArray(int[] arr) {
      int sum = 0;
      for (int value: arr) {
         sum += value;
      }
      return sum;
   }

   // To disply all values
   public static void printArray(int[] arr) {
      for (int i = 0; i < arr.length; i++) {
         System.out.println(i + ". " + arr[i]);
      }
   }
}
