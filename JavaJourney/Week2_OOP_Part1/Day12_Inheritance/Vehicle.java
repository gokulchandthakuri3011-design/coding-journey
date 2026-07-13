package Week2_OOP_Part1.Day12_Inheritance;


/*
1. Create a `Vehicle` class with fields `make`, `model`, and `year`, plus a `displayInfo()` method.
   Then create a `Car` subclass that adds `numDoors` and uses `super(...)` in its constructor.
   Finally, override `displayInfo()` in `Car` to include the door count.
*/

public class Vehicle {
    // Fields
    private String make;
    private String model;
    private int year;

    // Constructor
    public Vehicle(String make, String model, int year) {
        this.make = make;
        this.model = model;
        this.year = year;
    }

    // Method
    public void displayInfo() {
        System.out.println("Make: " + make);
        System.out.println("Model: " + model);
        System.out.println("Year: " + year);
    }
}

// Subclass Car extends Vehicle
class Car extends Vehicle {
    private int numDoors;

    // Constructor accepts vehicle details and number of doors
    public Car(String make, String model, int year, int numDoors) {
        super(make, model, year); // Calls Vehicle constructor to initialize fields
        this.numDoors = numDoors;
    }

    // Override displayInfo() method from Vehicle class to include doors
    public void displayInfo() {
        super.displayInfo(); // Call the parent class method to display info
        System.out.println("Number of Doors: " + numDoors);
    }

    // Main method for testing
    public static void main(String[] args) {
        Car myCar = new Car("Toyata", "Corolla", 2020, 4);
        myCar.displayInfo();
    }
}

// Simple test runner for Vehicle/Car
// class TestVehicle {
//     public static void main(String[] args) {
//         Car myCar = new Car("Toyota", "Corolla", 2020, 4);
//         myCar.displayInfo();
//     }
// }

