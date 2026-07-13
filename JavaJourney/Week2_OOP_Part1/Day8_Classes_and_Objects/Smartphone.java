package Week2_OOP_Part1.Day8_Classes_and_Objects;


/*
### Assignment 3: Smartphone Battery Tracker
Create a class named `Smartphone` with:
- **Instance Variables:** `brand` (String), `model` (String), and `batteryLevel` (int).
- **Methods:**
  - `charge(int amount)` that increases the `batteryLevel` by `amount`. (Optional: ensure it does not exceed 100).
  - `checkBattery()` that prints the smartphone's brand, model, and current battery level.
- **In your `Main` class:** Create a `Smartphone` object, set its brand to `"Samsung"`,
    model to `"Galaxy S24"`, and initial battery level to `40`. Call `charge(25)` to charge it,
    then call `checkBattery()` to verify the updated status.
*/


public class Smartphone {
    // Instance Variables
    String brand;
    String model;
    int batteryLevel;
    
    // Method: Charge Battery
    public void charge(int amount) {
        batteryLevel += amount;
        if (batteryLevel > 100) {
            batteryLevel = 100; // Cap at 100 as per instructions
            System.out.println("Battery is full now, Takeout the charger in time!");
        } else if (batteryLevel == 100) {
            System.out.println("Battery is full now.");
        } else {
            System.out.println("Charging... Current battery level is: " + batteryLevel + "%");
        }
    }

    // Method: Check Battery
    public void checkBattery() {
        System.out.println("Brand: " + brand);
        System.out.println("Model: " + model);
        System.out.println("Current Battery level: " + batteryLevel);
    }

    public static void main(String[] args) {
        // Creating an object of Smartphone class
        Smartphone sm1 = new Smartphone();
        sm1.brand = "Samsung";
        sm1.model = "Galaxy S24";
        sm1.batteryLevel = 40;

        // Calling methods
        sm1.charge(25);
        sm1.checkBattery();
    }
}
