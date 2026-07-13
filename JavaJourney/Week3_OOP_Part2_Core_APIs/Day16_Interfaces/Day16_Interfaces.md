# Day 16: Interfaces

## 📚 What is an Interface?

An **interface** in Java is a blueprint of a class. It represents a **contract** that implementing classes must follow. Think of it as a set of rules — if a class says it "implements" an interface, it must provide implementations for all the methods defined in that interface.

### Key Points:
- Interfaces are declared using the `interface` keyword.
- By default, all methods in an interface are **abstract** (no body) and **public**.
- By default, all fields are **public, static, and final** (constants).
- A class can implement **multiple interfaces** (achieving multiple inheritance behavior).

---

## 🛠️ Defining an Interface

```java
// Define an interface
interface Drawable {
    // Constants (public, static, final by default)
    int MAX_SIZE = 100;
    
    // Abstract methods (public, abstract by default)
    void draw();
    void resize(int factor);
}
```

### Implementing an Interface

```java
class Circle implements Drawable {
    private double radius;
    
    @Override
    public void draw() {
        System.out.println("Drawing a circle with radius: " + radius);
    }
    
    @Override
    public void resize(int factor) {
        radius *= factor;
    }
}
```

---

## 🔑 Key Concepts

### 1. Multiple Inheritance with Interfaces
A class can implement **multiple interfaces**, which is how Java achieves multiple inheritance:

```java
interface Flyable {
    void fly();
}

interface Swimmable {
    void swim();
}

class Duck implements Flyable, Swimmable {
    @Override
    public void fly() {
        System.out.println("Duck is flying!");
    }
    
    @Override
    public void swim() {
        System.out.println("Duck is swimming!");
    }
}
```

### 2. Default Methods (Java 8+)
Interfaces can have **default methods** with implementations:

```java
interface Logger {
    void log(String message);
    
    // Default method with implementation
    default void logError(String error) {
        System.out.println("ERROR: " + error);
    }
}
```

### 3. Static Methods in Interfaces (Java 8+)
Interfaces can also have **static methods**:

```java
interface MathOperations {
    static int add(int a, int b) {
        return a + b;
    }
}
// Called as: MathOperations.add(5, 3)
```

### 4. Interface vs Abstract Class

| Feature | Interface | Abstract Class |
|---------|-----------|----------------|
| Methods | All abstract (except default/static) | Can have abstract and concrete methods |
| Variables | Only constants (public static final) | Any type of variable |
| Inheritance | Multiple interfaces allowed | Single class inheritance only |
| Constructor | None | Can have constructors |
| Use Case | Define capabilities/behaviors | Share code among related classes |

---

## 🌍 Real-World Analogy: Interface as a "Job Description"

Think of an **interface** like a **job description** at a company:

| Java Concept | Real-World Analogy |
|---|---|
| **Interface** | A job posting (e.g., "Software Engineer") |
| **Abstract methods** | The required skills listed in the job description (e.g., "Must know Java", "Must know Git") |
| **Implementing class** | A person applying for the job |
| **`implements` keyword** | The person saying "I accept this job role" |
| **Method body** | How that person actually does the work (each person has their own style) |

### The Analogy in Action:

```
Job Posting (Interface) "Drawable":
  ✅ Must be able to draw()
  ✅ Must be able to resize(factor)

Person A — "Circle" (implements Drawable):
  → "I draw by using a compass and calculating radius."
  → "I resize by scaling the radius proportionally."

Person B — "Rectangle" (implements Drawable):
  → "I draw by measuring width and height with a ruler."
  → "I resize by scaling both width and height."
```

**Key takeaway:** The interface doesn't care *how* the work gets done — only *that* it gets done. Different classes implement the same contract in their own way. This is why interfaces enable **flexibility** and **polymorphism** in code.

### Another Analogy: Electrical Outlet

An **interface** is like a **wall electrical outlet**:

- The outlet defines a **standard shape and voltage** (the contract).
- Any device (TV, lamp, charger) can plug in — as long as it matches the outlet.
- The outlet doesn't care what device is plugged in; it just provides power.
- You can **swap devices** without changing the wall.

In Java:
- The **interface** = the outlet (standard contract).
- The **implementing class** = the device.
- The **method calls** = plugging in and using power.

This is why interfaces are powerful: they let you write code that works with *any* implementation, as long it follows the contract.

---

## ✅ Best Practices

1. **Use interfaces to define contracts** — when you want to specify "what" a class can do, not "how".
2. **Prefer interfaces over abstract classes** when multiple inheritance is needed.
3. **Keep interfaces small and focused** — follow the Single Responsibility Principle.
4. **Use default methods** to add functionality without breaking existing implementations.
5. **Name interfaces with adjectives** — e.g., `Readable`, `Writable`, `Comparable`.

---

## 📝 Assignment Questions

### **Q1: Basic Interface Implementation**
Create an interface `Printable` with a method `print()`. Implement it in classes `Document` and `Photo`. Each class should print a different message.

### **Q2: Multiple Interfaces**
Create two interfaces: `Playable` (with method `play()`) and `Pauseable` (with method `pause()`). Create a class `MediaPlayer` that implements both interfaces.

### **Q3: Default Methods**
Create an interface `Resizable` with:
- An abstract method `resize(double factor)`
- A default method `enlarge()` that calls `resize(1.5)`
- A default method `shrink()` that calls `resize(0.75)`

Implement this interface in a class `Image` with a `width` and `height` field.

### **Q4: Interface with Constants**
Create an interface `Constants` that defines:
- `PI = 3.14159`
- `EARTH_GRAVITY = 9.8`
- `LIGHT_SPEED = 299792458`

Create a class `PhysicsCalculator` that uses these constants to calculate:
- Area of a circle (using PI)
- Time to fall a certain distance (using EARTH_GRAVITY)

### **Q5: Complex Scenario — Shape System**
Create the following:

1. **Interface `Shape`** with methods:
   - `double area()`
   - `double perimeter()`
   - `String getName()`

2. **Classes**: `Circle`, `Rectangle`, `Triangle` — each implementing `Shape`.

3. **Interface `Colorable`** with method:
   - `void setColor(String color)`

4. **Class `ColoredCircle`** that implements both `Shape` and `Colorable`.

5. **Main class** that creates an array/list of `Shape` objects and calculates the total area of all shapes.

### **Q6: Static Methods in Interfaces**
Create an interface `MathUtils` with static methods:
- `max(int a, int b)` — returns the larger value
- `min(int a, int b)` — returns the smaller value
- `isEven(int n)` — returns true if even

Write a main program that tests all these methods.

### **Q7: Real-World Scenario — Payment System**
Create an interface `PaymentMethod` with:
- `boolean processPayment(double amount)`
- `String getPaymentType()`

Create classes: `CreditCard`, `PayPal`, `CryptoWallet` that implement `PaymentMethod`.

Create a `Store` class with a method `checkout(PaymentMethod payment, double amount)` that processes payment using any implementation.

### **Q8: Challenge — Event System**
Create an interface `EventListener` with method `onEvent(String event)`.

Create classes: `EmailNotifier`, `SMSNotifier`, `PushNotifier` that implement `EventListener`.

Create an `EventManager` class that:
- Allows registering multiple listeners
- Has a method `triggerEvent(String event)` that notifies all registered listeners

---

## 🎯 Learning Objectives Checklist

- [ ] Understand what an interface is and why it's useful
- [ ] Know how to define and implement an interface
- [ ] Understand multiple inheritance with interfaces
- [ ] Know the difference between abstract classes and interfaces
- [ ] Understand default and static methods in interfaces
- [ ] Can create interfaces with constants
- [ ] Can apply interfaces to real-world scenarios

---

## 💡 Quick Tips

- **Interface naming**: Use adjectives like `Readable`, `Writable`, `Comparable`, `Serializable`.
- **Multiple interfaces**: A class can implement many interfaces but extend only one class.
- **Default methods**: Allow you to add new methods to interfaces without breaking existing implementations.
- **Interfaces are contracts**: If you implement an interface, you MUST implement all its abstract methods.

---

*Next: Day 17 — Packages & Imports*
