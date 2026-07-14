package Week3_OOP_Part2_Core_APIs.Day20_Exception_Handling_Advanced;

/*
**1. Age Validator**
- Create `InvalidAgeException extends Exception`
- Method `validateAge(int age)` throws it if age < 18 or > 120
- Test with valid and invalid inputs
*/

class InvalidAgeException extends Exception {
    private int age;

    public InvalidAgeException(int age) {
        super("Invalid Age: " + age); // Custom message stored in parent constructor later which gets printed by (e.getmessage())
        this.age = age; // Store the invalid age
    }

    public static void validateAge(int age) throws InvalidAgeException {
        if (age < 18 || age > 120) {
            throw new InvalidAgeException(age); // Throws exception
        }
    }
}

public class Easy_Task1 {
    public static void main(String[] args) {
        // Test with valid ages
        try {
            InvalidAgeException.validateAge(25); // Static method call
            System.out.println("Age 25 is valid");
        } catch (InvalidAgeException e) {
            System.out.println(e.getMessage());
        }
        // Test with invalid ages (too young)
        try {
            InvalidAgeException.validateAge(16);
            System.out.println("Age 16 is valid");
        } catch (InvalidAgeException e) {
            System.out.println(e.getMessage());
        }
        // Test with invalid ages (too old)
        try {
            InvalidAgeException.validateAge(125);
            System.out.println("Age 125 is valid");
        } catch (InvalidAgeException e) {
            System.out.println(e.getMessage());
        }
    }
}
