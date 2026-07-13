package Week2_OOP_Part1.Day8_Classes_and_Objects;


/*
### Assignment 2: Rectangle Calculator
Create a class named `Rectangle` with:
- **Instance Variables:** `length` (double) and `width` (double).
- **Methods:**
  - `calculateArea()` which calculates and prints the area (`length * width`).
  - `calculatePerimeter()` which calculates and prints the perimeter (`2 * (length + width)`).
- **In your `Main` class:** Create a `Rectangle` object, set its length to `10.5` and width to `5.5`,
    and call both methods to display the results.
*/


public class Rectangle {

  // Creating Instance Variables length and width
  double length;
  double width;

  // Creating Method calculateArea()
  public void calculateArea() {
    System.out.println("Area of rectangle: " + length * width);
  }

  // Creating Method calculatePerimeter()
  public void calculatePerimeter() {
    System.out.println("Perimeter of rectangle: " + 2 * (length + width));
  }

  // Creating a Main Method 
  public static void main(String[] args) {
    // Creating an object named rect1
    Rectangle rect1 = new Rectangle();
    rect1.length = 10.5;
    rect1.width = 5.5;

    // Calling method 
    rect1.calculateArea();
    rect1.calculatePerimeter();
  }
}
