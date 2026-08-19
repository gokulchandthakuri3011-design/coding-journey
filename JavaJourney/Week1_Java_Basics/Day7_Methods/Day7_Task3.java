/*
3. Even/Odd Array Processor
   - Read an integer `n`, then read `n` numbers into an `int[] data` array.
   - Write `int sumEven(int[] arr)` to return the sum of even values.
   - Write `int sumOdd(int[] arr)` to return the sum of odd values.
   - Write `int[] filterGreaterThan(int[] arr, int limit)` to return a new array of values greater than `limit`.
   - In `main`, print the even sum, odd sum, and values greater than a chosen limit.
*/

package Week1_Java_Basics.Day7_Methods;
import java.util.Scanner;
import java.util.Arrays;

public class Day7_Task3 {
   public static void main(String[] args) {
      Scanner scanner = new Scanner(System.in);
      int[] data = null;

      // Asking user for the length of Data array
      System.out.print("Enter the length for data array: ");
      if (scanner.hasNextInt()) {
         int n = scanner.nextInt();

         if (n > 0) {
            // Initializing the Array
            data = new int[n];
            System.out.print("Enter " + n + " datas for the array: ");
            for (int i = 0; i < data.length; i++) {
               data[i] = scanner.nextInt();
            }
         } else {
            System.out.println("Enter a positive number for Array length.");
         }
      } else {
         System.out.println("Enter correct data type i.e; int here: ");
      }

      // Askking for the limit
      int limit = 0;
      System.out.print("Enter the number with whom you wanna compare the data in array: ");
      if (scanner.hasNextInt()) {
         limit = scanner.nextInt();
      }

      // Calling and printing
      int evenSum = sumEven(data);
      System.out.println("Sum of Even Numbers in given Array: " + evenSum);

      int oddSum = sumOdd(data);
      System.out.println("Sum of Odd Numbers in given Array: " + oddSum);

      int[] resultArray = filterGreaterThan(data, limit);
      System.out.println("The New Array with Data greater than " + limit + " is: " + Arrays.toString(resultArray));
      scanner.close();
   }


   // int sumEven(int[] arr)` to return the sum of even values
   public static int sumEven(int[] arr) {
      int evenSum = 0;
      for (int data: arr) {
         if (data % 2 == 0) {
            evenSum += data;
         }
      }
      return evenSum;
   }


   // int sumOdd(int[] arr)` to return the sum of odd values
   public static int sumOdd(int[] arr) {
      int oddSum = 0;
      for (int data: arr) {
         if (data % 2 != 0) {
            oddSum += data;
         }
      }
      return oddSum;
   }


   // int[] filterGreaterThan(int[] arr, int limit)` to return a new array of values greater than `limit`
   public static int[] filterGreaterThan(int[] arr, int limit) {
      int count = 0;
      for (int data: arr) {
         if (data > limit) {
            count++;
         }
      }
      int[] newArray = new int[count];
      int index = 0;
      for (int data: arr) {
         if (data > limit) {
            newArray[index] = data;
            index++;
         }
      }
      return newArray;
   }
}
