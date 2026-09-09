/*
### Assignment 3: Bank Account Class with Global Control
Create a class `BankAccount` containing:
1. Instance fields: `accountHolder` (String), `balance` (double).
2. Static fields: `bankName` (String, e.g., `"National Bank"`), and `interestRate` (double, e.g., `0.05` for 5%).
3. Add a parameterized constructor.
4. Provide standard getters and setters.
5. Provide a public **static setter** `public static void setInterestRate(double newRate)` to update the interest rate for the entire bank.
6. Add an instance method `calculateYearlyInterest()` that returns `balance * interestRate`.
7. In your `main` method:
   - Instantiate 2 accounts: `Alice` with a balance of `1000.0`, and `Bob` with a balance of `2000.0`.
   - Print their yearly interest (Alice should get `50.0`, Bob should get `100.0`).
   - The Central Bank decides to raise rates! Call the static setter to update `interestRate` to `0.07` (7%).
   - Recalculate and print their yearly interest again. Observe how the change instantly updated all instances!
*/

package Week2_OOP_Part1.Day11_Static_Keyword;

public class BankAccount {
    // Instance Fields
    private String accountHolder;
    private double balance;

    // Static Fields
    private static String bankName = "Deutsche Bank";
    private static double interestRate = 0.05; // 5%

    // Parameterized Constructor
    public BankAccount(String accountHolder, double balance) {
        this.accountHolder = accountHolder;
        this.balance = balance;
    }

    // Getters and Setters
    public String getAccountHolder() {
        return accountHolder;
    }

    public double getBalance() {
        return balance;
    }

    public static String getBankName() {
        return bankName;
    }

    public static double getInterestRate() {
        return interestRate;
    }

    public static void setInterestRate(double newRate) {
        interestRate = newRate;
    }

    // Instance Method to calculate yearly interest
    public double calculateYearlyInterest() {
        return balance * interestRate;
    }

    // Main Method
    public static void main(String[] args) {
        // Instantiate 2 accounts
        BankAccount aliceAcc = new BankAccount("Alice", 1000.0);
        BankAccount bobAcc = new BankAccount("Bob", 2000.0);

        // Printing their yearly interest
        System.out.println(" --- Yearly Interest Before Rate Change --- ");
        System.out.println("Alice's Yearly Interest: " + aliceAcc.calculateYearlyInterest());
        System.out.println("Bob's Yearly Interest: " + bobAcc.calculateYearlyInterest());

        // Change in Interest Rate from 5% - 8%
        BankAccount.setInterestRate(0.08); // 8%
        System.out.println();

        // Printing their yearly interest after rate change
        System.out.println(" --- Yearly Interest After Rate Change --- ");
        System.out.println("Alice's Yearly Interest: " + aliceAcc.calculateYearlyInterest());
        System.out.println("Bob's Yearly Interest: " + bobAcc.calculateYearlyInterest());
    }
}
