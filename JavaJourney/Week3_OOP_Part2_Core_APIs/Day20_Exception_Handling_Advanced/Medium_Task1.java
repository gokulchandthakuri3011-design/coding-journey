
/*
**1. Age Validator**
- Create `InvalidAgeException extends Exception`
- Method `validateAge(int age)` throws it if age < 18 or > 120
- Test with valid and invalid inputs
*/

class InvalidAgeException extends Exception {
    private int age;

    public InvalidAgeException(int age) {
        super("Invalid Age: " + age);
        this.age = age;
    }

    public static void validateAge(int age) {
        if (age < 18 || age > 120) {
            throw new InvalidAgeException(age);
        }
    }

    public static void main(String[] args) {

    }
}
