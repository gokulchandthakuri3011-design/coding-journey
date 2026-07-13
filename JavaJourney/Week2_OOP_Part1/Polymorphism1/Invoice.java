package Week2_OOP_Part1.Polymorphism1;


/*
## Question 1: Create an `Invoice` class
Write an `Invoice` class with:
- `productName` (String)
- `quantity` (int)
- `unitPrice` (double)

Provide three constructors:
1. `Invoice()` sets default values.
2. `Invoice(String productName, int quantity)` sets name and quantity, default price `0.0`.
3. `Invoice(String productName, int quantity, double unitPrice)` sets all fields.

Add a method `calculateTotal()` that returns `quantity * unitPrice`.
Then create a test class to build all three invoice types and print their totals.
*/

public class Invoice {
    // Instance Variables
    String productName;
    int quantity;
    double unitPrice;

    // Constructors
    
    public Invoice() {
        this.productName = "Unknown";
        this.quantity = 0;
        this.unitPrice = 0.0;
    }

    public Invoice(String productName, int quantity) {
        this.productName = productName;
        this.quantity = quantity;
        this.unitPrice = 0.0;
    }

    public Invoice(String productName, int quantity, double unitPrice) {
        this.productName = productName;
        this.quantity = quantity;
        this.unitPrice = unitPrice;
    }

    // Method 
    public double calculateTotal() {
        return quantity * unitPrice;
    }
}

class Test {
    public static void main(String[] args) {
        Invoice ser1 = new Invoice();
        Invoice ser2 = new Invoice("Adidas", 4);
        Invoice ser3 = new Invoice("Puma", 2, 37.5);

        // Calling methods to print
        System.out.println(ser1.calculateTotal());
        System.out.println(ser2.calculateTotal());
        System.out.println(ser3.calculateTotal());

    }
}
