/*
2. **Vehicle System**: Create an abstract class `Vehicle` with:
   - Fields `String brand` and `int speed`
   - A constructor to set both
   - An abstract method `void accelerate()` (each vehicle accelerates differently)
   - A concrete method `void displayInfo()` that prints brand and speed
   - Create `Car` (accelerate prints "Car is speeding up") and `Motorcycle` (accelerate prints "Motorcycle is revving")
   - Test with upcasting
*/
package Week3_OOP_Part2_Core_APIs.Day15_Abstractions;

public abstract class Vehicle {
    protected String brand;
    protected int speed;

    public Vehicle(String brand, int speed) {
        this.brand = brand;
        this.speed = speed;
    }

    // Abstract method
    public abstract void accelerate();

    public void displayInfo() {
        System.out.println("Vehicles Brand: " + brand );
        System.out.println("Vehicle's Speed: " + speed);
    }
}

class Car extends Vehicle {

    public Car(String brand, int speed) {
        super(brand, speed);
    } 
    @Override 
    public void accelerate() {
        System.out.println("Car is speeding up!");
    }
}

class Motorcycle extends Vehicle {
    public Motorcycle(String brand, int speed) {
        super(brand, speed);
    }

    @Override 
    public void accelerate() {
        System.out.println("Motorcycle is revving!");
    }
}

class MainTesting {
    public static void main(String[] args) {
        Vehicle veh1 = new Car("BMW", 250);
        Vehicle veh2 = new Motorcycle("Yamaha", 300);

        veh1.displayInfo();
        veh1.accelerate();
        veh2.displayInfo();
        veh2.accelerate();
    }
}