package Week2_OOP_Part1.Day10_Encapsulation;


/*
### Assignment 2: Smart Thermostat System
Create a class `Thermostat` with the following:
- A private field `temperature` (double) that defaults to `70.0`.
- A getter method `getTemperature()`.
- A setter method `setTemperature(double temp)` that ensures the temperature is kept within a safe range of `50.0`
  to `90.0` degrees Fahrenheit.
- If an invalid temperature is passed, print a warning message (e.g., `"Unsafe temperature requested!
  Keeping current temperature."`) and do not update the field.
- In your `main` method, instantiate a thermostat, change the temperature to `75.5`, print the reading,
  then try to change it to `110.0` and verify the safety guard works.
*/


public class Thermostat {
    // private field with default value
    private double temperature = 70.0;

    // Constructor
    public Thermostat(double temperature) {
        // Calling setter to validate before setting the value
        setTemperature(temperature);
    }
    
    // Getter method
    public double getTemperature() {
        return temperature;
    }

    // Setter method
    public void setTemperature(double temperature) {
        if (temperature >= 50.0 && temperature <= 90.0) {
            this.temperature = temperature;
        } else {
            System.out.println("Unsafe temperature requested! Keeping current temp: " + this.temperature);
        }
    }

    // Main Method
    public static void main(String[] args) {
        // Instantiating Thermostat class
        Thermostat myHome = new Thermostat(75.5);

        // Calling getter method and printing the value
        System.out.println("Current temperature: " + myHome.getTemperature());

        // Trying to change the temperature to unsafe value
        myHome.setTemperature(110.0);

        // Verifying safety guard
        System.out.println("Final temperature: " + myHome.getTemperature());
    }
}
