/* 
3. **Payment System**: Create a `Payment` superclass with a `processPayment(double amount)` method.
Create `CreditCardPayment` (adds 2% fee) and `PayPalPayment` (adds $1 fixed fee) subclasses.
Write a `processAll(Payment[] payments)` method that processes each payment using runtime polymorphism.
*/

package Week2_OOP_Part1.Polymorphism2;

public class Payment {
    protected double amount;

    public Payment(double amount) {
        this.amount = amount;
    }

    public void processPayment(double amount) {
        System.out.println("Processing payment: $" + amount);
    }
}

class CreditCardPayment extends Payment {
    public CreditCardPayment(double amount) {
        super(amount);
    }

    @Override
    public void processPayment(double amount) {
        double fee = amount * 0.02;
        double total = amount + fee;
        System.out.println("Credit Card total: $" + total + " (fee: $" + fee + ")");
    }
}

class PayPalPayment extends Payment {
    public PayPalPayment(double amount) {
        super(amount);
    }

    @Override
    public void processPayment(double amount) {
        double fee = 1.0;
        double total = amount + fee;
        System.out.println("PayPal total: $" + total + " (fee: $" + fee + ")");
    }
}

class AllPaymentTest {
    public static void main(String[] args) {
        Payment[] payments = new Payment[3];

        payments[0] = new Payment(200);
        payments[1] = new CreditCardPayment(300);
        payments[2] = new PayPalPayment(400);

        for (Payment paym : payments) {
            paym.processPayment(paym.amount);
        }
    }
}