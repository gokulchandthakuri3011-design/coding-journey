# Day 11: The `static` Keyword (Java)

Welcome to Day 11! Today we explore one of the most powerful and frequently used keywords in Java: **`static`**. 

Until now, we have been working with **instance members** (variables and methods) that belong to individual objects. But what if we want a variable or method that belongs to the **class itself** rather than any specific object? That's exactly what the `static` keyword does.

Let's dive in!

---

## 1. What is the `static` Keyword?

In Java, `static` is a non-access modifier used for memory management and declaring class-level members. When you apply `static` to a variable, method, or block, you are telling the Java Virtual Machine (JVM) that this member belongs to the **class template** itself, not to any individual instance (object) created from that template.

### The Big Picture: Class Level vs. Instance Level

Imagine a blueprint for building houses:
* **Instance Members (Non-Static):** The color of the house, the number of residents, or the lock on the front door. Every house (object) has its own unique copy of these.
* **Static Members:** The architect's name, the municipal building codes, or a shared neighborhood playground. There is only **one copy** of these, shared by all houses.

---

## 2. Memory Visualization: Heap vs. Metaspace/Method Area

To understand `static`, we must understand where Java stores things in memory:
* **Heap Memory:** This is where all objects (instances) live. Each object has its own unique set of instance variables.
* **Method Area / Metaspace:** This is where the JVM loads class templates, metadata, and **static variables**. It is allocated only once when the class is loaded.

```
       [ METHOD AREA / METASPACE ] (Shared Class Template)
       +---------------------------------------------+
       | Class: Student                              |
       |  - static int totalStudents = 3             | <--- ONLY ONE SHARED COPY
       +---------------------------------------------+
                              ^
                              | (Shared Access)
                              |
       [ HEAP MEMORY ] (Where Objects Live)
       +------------------+     +------------------+     +------------------+
       | Object 1 (s1)    |     | Object 2 (s2)    |     | Object 3 (s3)    |
       | - name: "Arun"   |     | - name: "Bina"   |     | - name: "Chetan" |
       | - studentID: 101 |     | - studentID: 102 |     | - studentID: 103 |
       +------------------+     +------------------+     +------------------+
```

---

## 3. Static Variables (Class Variables)

A **static variable** is a variable declared inside a class with the `static` keyword. 

### Key Characteristics:
1. **Shared Memory:** Only one copy of a static variable is created, regardless of how many objects are instantiated.
2. **Class-Level Access:** You can access static variables directly using the class name, without creating an object (`ClassName.variableName`).
3. **Lifecycle:** Created when the class is loaded into memory, and destroyed when the program terminates.

### Code Example: Implementing a Student Counter

In Day 10, we built a `Student` class. Let's see how we can use a `static` variable to automatically keep track of how many students have been registered:

```java
public class Student {
    // Instance variables (Each student gets their own unique copy)
    private String name;
    private String studentID;

    // Static variable (Shared by ALL students)
    public static int totalStudentsCount = 0; 

    // Constructor
    public Student(String name, String studentID) {
        this.name = name;
        this.studentID = studentID;
        
        // Every time a new Student is created, increment the shared counter!
        totalStudentsCount++; 
    }

    public void displayInfo() {
        System.out.println("Student: " + name + " | ID: " + studentID);
    }
}
```

### Accessing the Static Variable:
```java
public class Main {
    public static void main(String[] args) {
        // Before creating any students
        System.out.println("Total Students: " + Student.totalStudentsCount); // Prints: 0

        // Create objects
        Student s1 = new Student("Arun", "STU101");
        Student s2 = new Student("Bina", "STU102");

        // We can access it via the Class name directly
        System.out.println("Total Students: " + Student.totalStudentsCount); // Prints: 2
        
        // Note: You *can* access it via s1 or s2, but it is highly discouraged!
        // System.out.println(s1.totalStudentsCount); // Works, but gives a compiler warning!
    }
}
```

---

## 4. Static Methods

A **static method** is a method declared with the `static` keyword. Just like static variables, it belongs to the class rather than an object.

### Key Characteristics:
1. **Called without Objects:** You call static methods using the class name: `ClassName.methodName()`.
2. **Utility Focused:** Commonly used for utility or helper methods that don't need to read or modify an object's internal state (e.g., `Math.sqrt()`, `Arrays.sort()`).
3. **The Crucial Constraint (The Golden Rule of Static):**
   > [!IMPORTANT]
   > **Static methods CANNOT access instance variables or call instance methods directly.** They can only access other static members. Why? Because a static method is executed at the class level and does not know *which* object's instance variables to use!
4. **No `this` or `super`:** Since there is no object context, using `this` or `super` keywords inside a static method results in a compilation error.

### Code Example: Validating Static vs. Instance Access

```java
public class Calculator {
    private String modelName = "Standard Calc"; // Instance variable
    private static double PI = 3.14159;          // Static variable

    // Static Method
    public static double calculateAreaOfCircle(double radius) {
        // System.out.println(modelName); // ❌ COMPILE ERROR! Cannot make a static reference to the non-static field
        // greetUser();                  // ❌ COMPILE ERROR! Cannot call an instance method from a static context
        
        return PI * radius * radius;     // ✅ Allowed! Accessing static variable
    }

    // Instance Method
    public void greetUser() {
        System.out.println("Welcome to " + modelName); // ✅ Allowed! Instance method can access instance fields
        System.out.println("Value of PI is " + PI);    // ✅ Allowed! Instance methods CAN access static variables
    }
}
```

---

## 5. Static Blocks (Static Initializers)

What if you have a static variable that requires complex logic or calculations to initialize? You can use a **static block**.

A static block is a block of code with the keyword `static` and no method name. It is executed **exactly once** when the JVM first loads the class into memory, even before the `main` method runs or any constructor is called.

```java
public class Configuration {
    public static String defaultTheme;
    public static int maxUsersAllowed;

    // Static Block
    static {
        System.out.println("Static initialization block running...");
        // Imagine loading these configurations from a database or a file
        defaultTheme = "Dark Mode";
        maxUsersAllowed = 500;
    }

    public static void main(String[] args) {
        System.out.println("Main method running!");
        System.out.println("Theme: " + defaultTheme);
    }
}
```

**Output:**
```text
Static initialization block running...
Main method running!
Theme: "Dark Mode"
```

---

## 💡 Summary Comparison: Static vs. Instance

| Feature | Instance Variables & Methods (Non-Static) | Static Variables & Methods |
| :--- | :--- | :--- |
| **Who owns it?** | The **Object** (Instance) | The **Class** itself |
| **How is memory allocated?** | Multiple times (once for every object created in the Heap) | Exactly once (when the class is loaded in the Method Area) |
| **How do you access it?** | Via object reference: `objName.method()` | Directly via class name: `ClassName.method()` |
| **Can access static members?** | ✅ Yes, directly | ✅ Yes, directly |
| **Can access instance members?**| ✅ Yes, directly | ❌ No, must instantiate an object first |
| **Can use `this` and `super`?** | ✅ Yes | ❌ No (Compile-time error) |

---

## 🏋️ Assignments

### Assignment 1: Automated ID Generator for `Student`
Let's build upon your Day 10 `Student` class:
1. Add a private static variable `studentCounter` that starts at `1000`.
2. Add an instance variable `uniqueID` (String).
3. In your constructor, increment the `studentCounter` and construct a custom `uniqueID` for the student (e.g., `"STUDENT-" + studentCounter`).
4. Provide a public **static getter** `getTotalStudentsCount()` to retrieve the current count of enrolled students.
5. In your `main` method:
   - Create 3 students: `"Arun"`, `"Bina"`, and `"Chetan"`.
   - Print their details and verify that they have automatically received unique, consecutive IDs (`STUDENT-1001`, `STUDENT-1002`, `STUDENT-1003`).
   - Call the static getter to print the final student count.

### Assignment 2: Static Utility Helper (`MathUtility`)
Create a utility class named `MathUtility` designed for quick math operations:
1. Define a public static final constant `E = 2.71828`.
2. Write the following static methods:
   - `public static int add(int a, int b)`: Returns the sum of a and b.
   - `public static double square(double num)`: Returns `num * num`.
   - `public static double power(double base, int exponent)`: Returns base raised to the power of exponent using a simple loop.
3. In the `main` method, test each method **without instantiating** the `MathUtility` class.
4. Try to write an instance variable inside the class (like `int totalOperationsRun`), try to increment it inside your static `add()` method, and write down in comments the exact compile-time error you see and why it happens.

### Assignment 3: Bank Account Class with Global Control
Create a class `BankAccount` containing:
1. Instance fields: `accountHolder` (String), `balance` (double).
2. Static fields: `bankName` (String, e.g., `"National Bank"`), and `interestRate` (double, e.g., `0.05` for 5%).
3. Add a parameterized constructor.
4. Provide standard getters and setters.
5. Provide a public **static setter** `public static void setInterestRate(double newRate)` to update the interest rate for the entire bank.
6. Add an instance method `calculateYearlyInterest()` that returns `balance * interestRate`.
7. In your `main` method:
   - Instantiate 2 accounts: `Alice` with a balance of `1000.0`, and `Bob` with a balance of `2000.0`.
   - Print their yearly interest (Alice should get `50.0`, Bob should get `100.0`).
   - The Central Bank decides to raise rates! Call the static setter to update `interestRate` to `0.07` (7%).
   - Recalculate and print their yearly interest again. Observe how the change instantly updated all instances!

### 🏆 Bonus Challenge: The Singleton Design Pattern
The **Singleton Pattern** is a famous software design pattern that ensures a class has only one instance and provides a global point of access to it. It relies heavily on `static`.
Create a class `DatabaseConnection`:
1. Create a `private static DatabaseConnection instance;` field.
2. Create a **private constructor** (so no outside class can write `new DatabaseConnection()`).
3. Create a public **static method** `public static DatabaseConnection getInstance()`:
   - Inside this method, check if `instance` is `null`.
   - If it is `null`, create the single instance: `instance = new DatabaseConnection();`.
   - Return the `instance`.
4. In your `main` method, try to call `DatabaseConnection.getInstance()` twice and store them in `conn1` and `conn2`. Compare them using `if (conn1 == conn2)`. If it prints `"Same Instance!"`, you successfully implemented your first advanced design pattern!
