# Day 8: Classes and Objects (Java)

Welcome to Week 2 of your Java Learning Journey! This week introduces the core of Java: **Object-Oriented Programming (OOP)**. 

Today we're focusing on the fundamental building blocks of OOP: **Classes** and **Objects**.

---

## 1. What is a Class? What is an Object?

### Class: The Blueprint
A **Class** is a template, blueprint, or prototype that defines the state (data/variables) and behavior (methods/functions) of objects of a certain type. It's an abstract concept.

*   *Analogy:* Think of a class as a blueprint for a house. The blueprint itself is not a house you can live in; it's a design.

### Object: The Real Thing
An **Object** is an instance of a class. It is a physical reality (in memory) created based on the blueprint defined by the class. 

*   *Analogy:* If the class is the house blueprint, an object is a real house built using that blueprint. You can build multiple houses (objects) from the same blueprint (class). Each house can have its own specific color or owner, but they all follow the same basic structure.

---

## 2. Creating Classes and Instantiating Objects

### Defining a Class
To create a class in Java, use the `class` keyword followed by the class name (usually Capitalized).

```java
// Dog.java
public class Dog {
    // 1. Fields (State / Data)
    String breed;
    int age;
    String color;

    // 2. Methods (Behavior)
    public void bark() {
        System.out.println("Woof! Woof!");
    }

    public void displayInfo() {
        System.out.println("This dog is a " + color + " " + breed + " and is " + age + " years old.");
    }
}
```

### Instantiating an Object
To create an object from a class, we use the `new` keyword. This process is called **instantiation**.

```java
// Main.java
public class Main {
    public static void main(String[] args) {
        Dog myDog = new Dog();

        myDog.breed = "Golden Retriever";
        myDog.age = 3;
        myDog.color = "Golden";

        myDog.bark();          // Output: Woof! Woof!
        myDog.displayInfo();

        Dog anotherDog = new Dog();
        anotherDog.breed = "Pug";
        anotherDog.age = 5;
        anotherDog.color = "Fawn";
        anotherDog.displayInfo();
    }
}
```

---

## 3. Instance Variables vs. Local Variables

### Instance Variables (Fields)
*   **Where are they declared?** Inside a class, but outside any method, constructor, or block.
*   **What are they?** They represent the attributes or state of an object.
*   **Scope:** Accessible by all methods within the class.
*   **Lifespan:** Created when an object is instantiated, destroyed when the object is garbage collected.
*   **Default Values:** `0` for `int`, `null` for objects, `false` for `boolean`.

### Local Variables
*   **Where are they declared?** Inside a method, constructor, or block.
*   **Scope:** Only visible within the method or block where declared.
*   **Lifespan:** Created when the block is entered, destroyed when it exits.
*   **Default Values:** None — you **must** initialize before use.

```java
public class VariableExample {
    int instanceVar; // instance variable — defaults to 0

    public void myMethod() {
        int localVar = 10; // local variable — must be initialized

        System.out.println("Instance Var: " + instanceVar); // 0
        System.out.println("Local Var: " + localVar);       // 10
    }
}
```

---

## 💡 Summary
*   **Classes** are templates. **Objects** are instances created from classes.
*   Use the `new` keyword to create objects.
*   **Instance variables** belong to an object and store its state.
*   **Local variables** are temporary and exist only within a specific method or block.

## 🏋️ Practice Task
1. Create a class named `Car` with instance variables for `make` (String), `model` (String), and `year` (int).
2. Add a method named `startEngine()` that prints "Vroom! Engine started."
3. In your `Main` class, create two different `Car` objects, set their properties, and call `startEngine()` for both.

---

## 📝 Assignments

### Assignment 1: Student Class (Simple)
Create a class named `Student` with:
- **Instance Variables:** `name` (String), `rollNumber` (int), and `marks` (double).
- **Method:** `displayStudentInfo()` that prints the student's name, roll number, and marks.
- **In `Main`:** Create two `Student` objects, set their fields, and call `displayStudentInfo()` on both.

### Assignment 2: Rectangle Calculator
Create a class named `Rectangle` with:
- **Instance Variables:** `length` (double) and `width` (double).
- **Methods:** `calculateArea()` and `calculatePerimeter()`.
- **In `Main`:** Create a `Rectangle` with length `10.5` and width `5.5`, and call both methods.

### Assignment 3: Smartphone Battery Tracker
Create a class named `Smartphone` with:
- **Instance Variables:** `brand` (String), `model` (String), and `batteryLevel` (int).
- **Methods:** `charge(int amount)` and `checkBattery()`.
- **In `Main`:** Create a `Smartphone`, charge it, then check the battery.
