package Week2_OOP_Part1.Day8_Classes_and_Objects;


/*
1.  Create a class named `Car` with instance variables for `make` (String), `model` (String), and `year` (int).
2.  Add a method named `startEngine()` that prints a message like "Vroom! Engine started."
3.  In your `Main` class, create two different `Car` objects, set their properties, and call the `startEngine()` method for both.
*/

public class Car {
    String make;
    String model;
    int year;

    void startEngine() {
        System.out.println("Vroom! Engine started.");
    }

    public static void main(String[] args) {
        // Creating first Car object
        Car car1 = new Car(); // Create an instance of Car
        car1.make = "Koeingsegg";
        car1.model = "Agera RS";
        car1.year = 2017;
        // Calling the method for the first car
        car1.startEngine();

        // Creating second Car object
        Car car2 = new Car(); // Create another instance of Car
        car2.make = "Pagani";
        car2.model = "Huayara";
        car2.year = 2016;
        // Calling the method for the second car
        car2.startEngine();
    }
}