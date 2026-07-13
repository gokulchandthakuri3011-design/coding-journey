# Day 13: Polymorphism (Compile-Time) in Java

Welcome to Day 13! Today we learn about **compile-time polymorphism** in Java, also known as **method overloading** and **constructor overloading**.

Polymorphism means "many forms." In Java, compile-time polymorphism happens when the compiler picks which method or constructor to call based on the arguments you pass, before the program runs. That choice is fixed during compilation, not at runtime.

---

## 1. What is Compile-Time Polymorphism?

Compile-time polymorphism happens when the Java compiler selects the correct method to call based on the method signature during compilation.

Key terms:
- **Method Overloading**: Same method name, different parameter list.
- **Constructor Overloading**: Same class name, different constructor parameter list.

This is also called **static binding** or **early binding**.

---

## 2. Method Overloading

### Rules for Method Overloading
A method is overloaded when:
1. The method name is the same.
2. The parameter list is different by:
   - number of parameters, or
   - type of parameters, or
   - order of parameters.
3. Return type may be same or different.
4. Access modifier can be same or different.

### Not Overloading
You cannot overload methods by only changing the return type.

Example that does NOT work:
```java
public int calculate(int a, int b) { return a + b; }
public double calculate(int a, int b) { return a + b + 0.0; }
```
This fails because the parameter list is identical.

### Example: `MathHelper` with Overloaded Methods
```java
public class MathHelper {
    public int add(int a, int b) {
        return a + b;
    }

    public double add(double a, double b) {
        return a + b;
    }

    public int add(int a, int b, int c) {
        return a + b + c;
    }

    public String add(String a, String b) {
        return a + b;
    }
}
```

```java
public class TestMathHelper {
    public static void main(String[] args) {
        MathHelper helper = new MathHelper();
        System.out.println(helper.add(2, 3));
        System.out.println(helper.add(2.5, 3.5));
        System.out.println(helper.add(1, 2, 3));
        System.out.println(helper.add("Hello", " World"));
    }
}
```

### Why Overload Methods?
- Makes code easier to read.
- Lets you use the same name for related operations.
- Avoids creating many different method names for similar tasks.

---

## 3. Constructor Overloading

Constructor overloading uses the same class name with different parameter lists.

This allows you to create objects in different ways.

### Example: `Book` Class with Overloaded Constructors
```java
public class Book {
    private String title;
    private String author;
    private double price;

    public Book() {
        this.title = "Unknown";
        this.author = "Unknown";
        this.price = 0.0;
    }

    public Book(String title, String author) {
        this.title = title;
        this.author = author;
        this.price = 0.0;
    }

    public Book(String title, String author, double price) {
        this.title = title;
        this.author = author;
        this.price = price;
    }

    public void displayInfo() {
        System.out.println("Title: " + title);
        System.out.println("Author: " + author);
        System.out.println("Price: $" + price);
    }
}
```

```java
public class TestBook {
    public static void main(String[] args) {
        Book defaultBook = new Book();
        Book twoArgBook = new Book("Java Basics", "A. Author");
        Book fullBook = new Book("Advanced Java", "B. Writer", 39.99);

        defaultBook.displayInfo();
        System.out.println("---");
        twoArgBook.displayInfo();
        System.out.println("---");
        fullBook.displayInfo();
    }
}
```

### Why Overload Constructors?
- Allows flexible object creation.
- Supports default values and optional data.
- Lets different callers supply different levels of information.

---

## 4. How the Compiler Chooses the Method

The compiler matches the call to the method signature by looking at:
1. method name
2. argument types
3. number of arguments
4. order of arguments

The compiler selects the best match and binds that method call during compilation.

### Example: Ambiguity and Conversion
```java
public class OverloadDemo {
    public void show(int x) {
        System.out.println("int: " + x);
    }

    public void show(double x) {
        System.out.println("double: " + x);
    }

    public static void main(String[] args) {
        OverloadDemo demo = new OverloadDemo();
        demo.show(5);      // Uses show(int)
        demo.show(5.0);    // Uses show(double)
        demo.show('A');    // char can convert to int, so uses show(int)
    }
}
```

If two overloaded methods are equally good matches, the compiler reports an error.

---

## 5. Concepts Map

### Compile-Time Polymorphism Map

1. Polymorphism
   - Compile-Time
     - Method Overloading
     - Constructor Overloading
   - Runtime
     - Method Overriding
     - Upcasting / Downcasting

> Note: This page is focused on compile-time polymorphism. The runtime concepts listed above belong to the next topic and are explained in Day 14.
> 
> - **Runtime polymorphism** means the method choice happens while the program runs, not while it is being compiled.
> - **Method overriding** is when a subclass provides its own version of a parent class method.
> - **Upcasting** means using a subclass object as if it were its parent type.
> - **Downcasting** means converting a parent reference back to a subclass type.

2. Overloaded Member Types
   - Methods
   - Constructors

3. Method Signature Differences
   - Number of parameters
   - Type of parameters
   - Order of parameters

4. Why Use It?
   - Cleaner API
   - Better readability
   - Flexible usage

---

## 6. Notes and Tips

- **Method signature** means method name + parameter list.
- **Return type is not part of the signature**.
- Overloading is not the same as overriding.
- Overloading happens within the same class or in a subclass.
- If a subclass overloads a method, the parent method remains available.
- You can overload static methods too.

---

## 7. Assignment Questions

### Question 1: Create an `Invoice` class
Write an `Invoice` class with:
- `productName` (String)
- `quantity` (int)
- `unitPrice` (double)

Provide three constructors:
1. `Invoice()` sets default values.
2. `Invoice(String productName, int quantity)` sets name and quantity, default price `0.0`.
3. `Invoice(String productName, int quantity, double unitPrice)` sets all fields.

Add a method `calculateTotal()` that returns `quantity * unitPrice`.
Then create a test class to build all three invoice types and print their totals.

### Question 2: Overload a `print` method
Create a class `Printer` with overloaded methods:
- `print(String text)`
- `print(int number)`
- `print(double value)`
- `print(String text, int copies)`

In `main`, call each method and show the difference in output.

### Question 3: Create a `Calculator` class with overloaded `multiply` methods
Write a class with these methods:
- `multiply(int a, int b)`
- `multiply(int a, int b, int c)`
- `multiply(double a, double b)`

Test all versions in `main`.

### Question 4: Identify valid overloads
Which of these method signatures are valid overloads?
1. `public void show(int a)`
2. `public int show(int a)`
3. `public void show(double a)`
4. `public void show(int a, int b)`
5. `public void show(int a)`

Explain your answer.

### Question 5: Constructor overloading with a `Student` example
Create a `Student` class with fields:
- `name` (String)
- `grade` (int)
- `school` (String)

Provide these constructors:
- `Student()` with default values.
- `Student(String name)`.
- `Student(String name, int grade)`.
- `Student(String name, int grade, String school)`.

Then create objects using each constructor and print the student information.

---

## 8. Quick Practice

Use these method calls and decide which overloaded method is chosen:

1. `demo.print(5);`
2. `demo.print(5.0);`
3. `demo.print("Hi", 2);`
4. `demo.calculate(2, 3.0);`

Explain each choice in a short comment.

---

## 9. Summary

Compile-time polymorphism is a powerful tool for writing readable and flexible Java code. Today’s focus was on using the same method or constructor name with different parameter lists so the compiler can choose the correct version before the program runs.

Good work! Keep practicing with different overloaded signatures until the rules feel natural.
