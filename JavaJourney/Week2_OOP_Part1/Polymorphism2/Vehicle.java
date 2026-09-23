/*
4. **Vehicle Rental**: Create a `Vehicle` superclass with `rentPerDay` and a `calculateRentalCost(int days)` method.
Create `Car` (rent = $50/day) and `Truck` (rent = $100/day) subclasses.
Use downcasting to access a `getCargoCapacity()` method on `Truck` objects. 
*/

package Week2_OOP_Part1.Polymorphism2;

public class Vehicle {
    protected double rentPerDay;

    public Vehicle(double rentPerDay) {
        this.rentPerDay = rentPerDay;
    }

    public void calculateRentalCost(int days) {
        System.out.println("Total Rental Cost: $" + (days * rentPerDay));
    }
}

class Car extends Vehicle {
    public Car() {
        super(50);
    }

    @Override
    public void calculateRentalCost(int days) {
        double total = rentPerDay * days;
        System.out.println("Total Car Rental Cost: $" + total + " including fee: $" + rentPerDay + "/days");
    }
}

class Truck extends Vehicle {
    private double cargoCapacity;

    public Truck(double cargoCapacity) {
        super(100);
        this.cargoCapacity = cargoCapacity;
    }

    public double getCargoCapacity() {
        return cargoCapacity;
    }

    @Override
    public void calculateRentalCost(int days) {
        double total = rentPerDay * days;
        System.out.println("Total Truck Rental Cost: $" + total + " including fee: $" + rentPerDay + "/days");
    }
}

class Vehicletest {
    public static void main(String[] args) {
        Vehicle veh1 = new Car();
        Vehicle veh2 = new Truck(250);

        veh1.calculateRentalCost(5);
        veh2.calculateRentalCost(6);

        if (veh2 instanceof Truck) {
            Truck myTruck = (Truck) veh2;
            System.out.println("The Cargo Capacity of Truck is: " + myTruck.getCargoCapacity() + " cubic meters");
        }
    }
}
