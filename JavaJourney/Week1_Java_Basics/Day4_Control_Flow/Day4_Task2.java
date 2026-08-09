package Week1_Java_Basics.Day4_Control_Flow;

/*
### Task 2: Discount Calculator
You are writing software for a store. Declare a `double` variable `purchaseAmount`.
* If the amount is $100 or more, apply a 20% discount.
* If the amount is between $50 and $99.99, apply a 10% discount.
* If the amount is less than $50, no discount is applied.
Calculate and print the final price the customer needs to pay.
*/

public class Day4_Task2 {
    public static void main(String[] args) {

        // Discount Calculator
        System.out.println("--- Discount Calculator ---");

        // Declare a double variable purchaseAmount
        double purchaseAmount = 120.0; // Example purchase amount

        // Calculate the final price based on the discount rules
        double finalPrice;
        if (purchaseAmount >= 100) {
            finalPrice = purchaseAmount * 0.80; // Apply 20% discount
        } else if (purchaseAmount >= 50 && purchaseAmount < 100) {
            finalPrice = purchaseAmount * 0.90; // Apply 10% discount
        } else {
            finalPrice = purchaseAmount; // No discount
        }
        System.out.println("Final price to pay: $" + finalPrice);
    }
}
