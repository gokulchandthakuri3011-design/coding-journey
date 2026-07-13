# Day 10: Access Modifiers & Encapsulation (Java)

Welcome to Day 10! Today we dive into **Access Modifiers** and **Encapsulation** — two foundational pillars of Object-Oriented Programming (OOP) in Java. Together, they allow you to implement **data hiding** and secure your objects from unintended external interference.

---

## 1. What are Access Modifiers?

In Java, **Access Modifiers** are keywords used to define the visibility (accessibility) of classes, constructors, fields (variables), and methods. They control which other classes can see and use your class members.

Java provides four levels of access protection:
1. **`private`**
2. **Default** (no modifier keyword used)
3. **`protected`**
4. **`public`**

Here is the ultimate visibility table for Java access modifiers:

| Modifier | Same Class | Same Package | Subclass (Diff Package) | World (Anywhere) |
| :--- | :---: | :---: | :---: | :---: |
| **`private`** | ✅ Yes | ❌ No | ❌ No | ❌ No |
| **Default** (none) | ✅ Yes | ✅ Yes | ❌ No | ❌ No |
| **`protected`** | ✅ Yes | ✅ Yes | ✅ Yes | ❌ No |
| **`public`** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |

---

## 2. Deep Dive: The Four Access Levels

Let's look at how each of these modifiers behaves in practice.

### A. The `private` Modifier (Class-Level Access)
When a field or method is marked `private`, it can **only** be accessed within the class it is declared. No outside class, not even a subclass or a class in the same package, can touch it directly.

```java
public class User {
    private String password; // Hidden from the outside world

    public User(String password) {
        this.password = password; // Allowed: same class
    }
}

// In another class:
User user = new User("secret123");
// user.password = "hacked"; // ❌ COMPILE ERROR: password has private access in User
```

### B. Default Access (Package-Level Access)
If you do **not** write any access modifier keyword, Java assigns **default** access (sometimes called *package-private*). Members with default access are visible to all classes within the **same package**, but invisible to classes outside the package.

```java
class PackageHelper { // Default class
    int packageID = 101; // Default variable (no modifier keyword)

    void showMessage() { // Default method
        System.out.println("Hello from the package!");
    }
}
```

### C. The `protected` Modifier (Package & Subclass Access)
Members marked `protected` are accessible within the **same package** AND by **subclasses** in other packages (via inheritance using keyword **extends**). It is commonly used when you want parent-class variables to be directly usable by child classes but hidden from the general public.

```java
public class Vehicle {
    protected String brand = "Ford"; // Accessible by subclasses
}

public class Car extends Vehicle {
    public void printBrand() {
        System.out.println(this.brand); // ✅ Allowed because Car is a subclass of Vehicle
    }
}
```

### D. The `public` Modifier (Global Access)
Members marked `public` are visible to **every class in every package** across your entire project.

```java
public class Printer {
    public void print(String message) { // Anyone can call this method
        System.out.println(message);
    }
}
```

---

## 3. What is Encapsulation?

**Encapsulation** is the practice of wrapping data (variables) and code (methods) together as a single unit, and restricting direct access to some of the object's components. 

To achieve encapsulation in Java:
1. Declare the class variables as **`private`**.
2. Provide **`public` getter and setter** methods to view and modify the variables.

Think of encapsulation like a **capsule** or a protective shield that prevents direct access to data.

```
       +---------------------------------------------+
       |                  CLASS                      |
       |  +---------------------------------------+  |
       |  |          Private Variables            |  |
       |  |  (Hidden / Protected Internal State)  |  |
       |  +-------------------+-------------------+  |
       |                      |                      |
       |                      v                      |
       |  +---------------------------------------+  |
       |  |       Public Getters & Setters        |  |
       |  | (Controlled Doorway to the Outside)  |  |
       |  +-------------------+-------------------+  |
       +----------------------|----------------------+
                              |
                              v
                      [ Outside World ]
```

---

## 4. Why Use Encapsulation? (The Benefits)

Encapsulation offers several critical benefits for software engineering:

### 1. Data Control & Validation (Security)
If fields are public, anyone can set invalid values. With private fields and public setters, you can validate inputs before changing the data.
*   *Example:* Preventing a `BankAccount` balance from becoming negative or a `Student` GPA from exceeding 4.0.

### 2. Read-Only or Write-Only Fields
You can choose to provide only a getter (making the field read-only) or only a setter (making the field write-only).
*   *Example:* An `id` should be assigned once in the constructor. By providing a getter but **no setter**, you prevent the ID from ever being changed after creation.

### 3. Hiding Internal Complexity (Abstraction)
The outside world doesn't need to know how your class stores or calculates data; they just need to call the public methods.
*   *Example:* A class might store a name as `firstName` and `lastName` internally, but provide a public `getFullName()` method.

---

## 5. Implementing Getters and Setters

Getters and Setters are standard methods used to retrieve and update private field values:
*   **Getter (Accessor):** A public method that returns the value of a private variable. Usually named `getVariableName()`.
*   **Setter (Mutator):** A public method that takes a parameter and assigns it to a private variable. Usually named `setVariableName()`.

Let's look at a class that implements encapsulation with validation:

```java
public class Person {
    private String name; // Private field
    private int age;     // Private field

    // Constructor
    public Person(String name, int age) {
        this.name = name;
        setAge(age); // Call setter to ensure validation runs during creation!
    }

    // Getter for Name
    public String getName() {
        return name;
    }

    // Setter for Name
    public void setName(String name) {
        this.name = name;
    }

    // Getter for Age
    public int getAge() {
        return age;
    }

    // Setter for Age (with validation)
    public void setAge(int age) {
        if (age >= 0) {
            this.age = age; // Update only if valid
        } else {
            System.out.println("Warning: Age cannot be negative. Value unchanged.");
        }
    }
}
```

---

## 💡 Summary

| Concept | Key Point |
| :--- | :--- |
| **`private`** | Hides variables and methods from outside access (Core of Encapsulation). |
| **`public`** | Exposes entry points (like getters/setters) to other classes. |
| **Encapsulation** | Wrapping variables and methods together; using private fields + public methods. |
| **Getter Methods** | Safely read private data from an object. |
| **Setter Methods** | Safely write/modify private data, with optional validation logic. |

---

## 🏋️ Assignments

### Assignment 1: Student Class with GPA Validation
Create a class `Student` with the following private fields:
- `name` (String)
- `gpa` (double)
- `studentID` (String)

Provide the following:
1. A parameterized constructor that initializes all three fields (use the setter inside the constructor to validate the GPA).
2. Getter and setter for `name`.
3. Getter and setter for `gpa` — the setter **must** validate that `gpa` is between `0.0` and `4.0` (inclusive). If it's outside this range, print an error and do not update the field.
4. Getter for `studentID`, but **no setter** (making the ID read-only).
5. In your `main` method:
   - Create a student with a valid GPA (e.g., `3.8`) and print their details.
   - Try to set an invalid GPA (e.g., `5.2` or `-1.0`) and observe the validation message.
   - Verify that you cannot change the `studentID` after creation.

### Assignment 2: Smart Thermostat System
Create a class `Thermostat` with the following:
- A private field `temperature` (double) that defaults to `70.0`.
- A getter method `getTemperature()`.
- A setter method `setTemperature(double temp)` that ensures the temperature is kept within a safe range of `50.0` to `90.0` degrees Fahrenheit.
- If an invalid temperature is passed, print a warning message (e.g., `"Unsafe temperature requested! Keeping current temperature."`) and do not update the field.
- In your `main` method, instantiate a thermostat, change the temperature to `75.5`, print the reading, then try to change it to `110.0` and verify the safety guard works.

### Assignment 3: Encapsulated Bank Account
Create a class `BankAccount` with:
- Private fields: `accountNumber` (String), `accountHolder` (String), and `balance` (double).
- Provide:
  - A constructor that initializes `accountNumber` and `accountHolder`. The `balance` should default to `0.0`.
  - Getters for `accountNumber` and `balance` (no setters for these! They must be protected).
  - Getter and Setter for `accountHolder`.
  - A public method `deposit(double amount)` that increases the balance if the amount is greater than `0`.
  - A public method `withdraw(double amount)` that decreases the balance if the amount is greater than `0` AND the account has sufficient funds.
- Test your class in `main` by performing valid and invalid deposits and withdrawals, and checking the balance only via the getter.

### Bonus Challenge: Employee Payroll Record
Create a class `Employee` with private fields: `name` (String), `hourlyRate` (double), and `hoursWorked` (int).
- The class should have a parameterized constructor.
- Add getters and setters for all fields.
  - `hourlyRate` must be at least `15.00` (minimum wage). If lower is provided, automatically set it to `15.00`.
  - `hoursWorked` must be between `0` and `80` (maximum 80 hours per pay period). Do not update if invalid.
- Add a public method `calculateSalary()` that returns the total salary (`hourlyRate * hoursWorked`). If `hoursWorked` exceeds `40`, pay double-time (`2.0 * hourlyRate`) for the overtime hours!
- In `main`, test an employee with regular hours and one with overtime hours, and verify all validations and calculations are correct.
