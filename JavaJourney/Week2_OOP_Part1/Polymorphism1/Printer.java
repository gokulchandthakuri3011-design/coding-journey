package Week2_OOP_Part1.Polymorphism1;


/*
### Question 2: Overload a `print` method
Create a class `Printer` with overloaded methods:
- `print(String text)`
- `print(int number)`
- `print(double value)`
- `print(String text, int copies)`
*/

public class Printer {
    // Instance Variables
    String text;
    int number;
    double value;
    int copies;

    // Methods Overloading
    public void print_info(String text) {
        System.out.println("Text: " + text);
    }

    public void print_info(int number) {
        System.out.println("Number: " + number);
    }

    public void print_info(double value) {
        System.out.println("Value: " + value);
    }

    public void print_info(String text, int copies) {
        System.out.println("Text: " + text);
        System.out.println("Copies: " + copies);
    } 
}

class Info extends Printer {
    public static void main(String[] args) {
        Printer myInfo = new Printer();
        myInfo.print_info("Gokul");
        myInfo.print_info(11);
        myInfo.print_info(59.9);
        myInfo.print_info("Arun", 2);
    }
}