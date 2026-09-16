/*
4. Create a `Device` superclass with `brand` and `powerOn()` method.
   Create a `Phone` subclass with a `callNumber(String number)` method.
   Use `super` to access a superclass method or field from inside `Phone`.
*/
package Week2_OOP_Part1.Day12_Inheritance;

public class Device {
    // Field
    protected String brand;

    // Constructor
    public Device(String brand) {
        this.brand = brand;
    }

    // Method
    public void powerOn() {
        System.out.println("The device from this " + brand + " is on.");
    }
}

class Phone extends Device {
    private String number;

    public Phone(String brand, String number) {
        super(brand);
        this.number = number;
    }

    public void callNumber(String number) {
        System.out.println("Calling to this " + number);
    }

    public void showDeviceInfo() {
        System.out.println("Phone brand: " + super.brand);
        super.powerOn();
    }

    // Main
    public static void main(String[] args) {
        Phone myPhone = new Phone("Apple", "+49 123456789");
        myPhone.showDeviceInfo();
        myPhone.callNumber(myPhone.number);

    }
}
// static main: use an object such as myPhone.
// Non-static subclass method: use super directly.