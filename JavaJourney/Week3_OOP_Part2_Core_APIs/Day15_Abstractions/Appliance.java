/*
3. **Appliance**: Create an abstract class `Appliance` with:
   - A `String brand` field
   - An abstract method `void turnOn()`
   - A concrete method `void plugIn()` that prints "Plugged into outlet"
   - Create `Fan` (turnOn prints "Fan is spinning") and `TV` (turnOn prints "TV is displaying")
   - Test both
*/
package Week3_OOP_Part2_Core_APIs.Day15_Abstractions;

public abstract class Appliance {
    String brand;

    public Appliance(String brand) {
        this.brand = brand;
    }

    public abstract void turnOn();

    public void plugIn() {
        System.out.println("Plugged into outlet.");
    }
}

class Fan extends Appliance {
    public Fan(String brand) {
        super(brand);
    }

    @Override 
    public void turnOn() {
        System.out.println("Fan is spinning.");
    }
}

class TV extends Appliance {
    public TV(String brand) {
        super(brand);
    }

    @Override 
    public void turnOn() {
        System.out.println("TV is displaying.");
    }
}

class TestMain {
    public static void main(String[] args) {
        Appliance appl1 = new Fan("Philips");
        Appliance appl2 = new TV("Sony");

        // Printing each object seperate message
        appl1.turnOn();
        appl2.turnOn();
    }
}