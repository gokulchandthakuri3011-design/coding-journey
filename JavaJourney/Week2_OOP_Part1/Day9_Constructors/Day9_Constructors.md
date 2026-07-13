# Day 9: Constructors (Java)

Welcome to Day 9! Today we learn about **Constructors** — special methods that initialize objects when they are created.

---

## 1. What is a Constructor?

A **constructor** is a block of code that runs when you create an object using the `new` keyword. It sets the initial state of an object.

### Rules:
- Constructor name **must** match the class name exactly.
- It has **no return type** (not even `void`).
- It is called **automatically** when you do `new ClassName()`.
- You can have multiple constructors via **overloading**.

```java
public class Student {
    String name;
    int age;

    // Constructor
    public Student() {
        System.out.println("A new Student object is created!");
    }
}
```

---

## 2. Default Constructor

If you **don't** define any constructor in your class, Java provides a **default constructor** (no parameters, no body) for free.

```java
public class Car {
    String model;
    int year;

    // No constructor defined — Java supplies: public Car() { }
}

// Usage:
Car c = new Car();  // Works because of the default constructor
c.model = "Toyota"; // We must set fields manually
```

**Important:** Once you define **any** constructor, the default constructor is **no longer provided**.

---

## 3. Parameterized Constructors

A constructor that takes arguments lets you set field values **at the moment of creation**.

```java
public class Student {
    String name;
    int age;

    // Parameterized constructor
    public Student(String studentName, int studentAge) {
        name = studentName;
        age = studentAge;
    }
}

// Usage:
Student s1 = new Student("Alice", 20);
Student s2 = new Student("Bob", 22);
```

Each object is fully initialized in one line — no separate `.name = ...` assignments needed.

---

## 4. The `this` Keyword

`this` refers to the **current object**. Use it when parameters have the same name as instance variables.

```java
public class Student {
    String name;
    int age;

    public Student(String name, int age) {
        this.name = name;   // this.name = instance variable
        this.age = age;     // age on right = parameter
    }
}
```

`this` can also be used to call another constructor from within a constructor (constructor chaining):

```java
public class Rectangle {
    int width;
    int height;

    // Full constructor
    public Rectangle(int width, int height) {
        this.width = width;
        this.height = height;
    }

    // Default constructor — chains to the full constructor
    public Rectangle() {
        this(1, 1);  // Calls Rectangle(int, int) with defaults
    }
}
```

> `this()` must be the **first statement** inside a constructor.

---

## 5. Constructor Overloading

Like methods, constructors can be overloaded — same name, different parameter lists.

```java
public class Book {
    String title;
    String author;
    int pages;

    // 3-arg constructor
    public Book(String title, String author, int pages) {
        this.title = title;
        this.author = author;
        this.pages = pages;
    }

    // 2-arg constructor (pages unknown)
    public Book(String title, String author) {
        this(title, author, 0);   // chain to 3-arg
    }


    // No-arg constructor
    public Book() {
        this("Unknown", "Unknown", 0);  // chain to 3-arg
    }
}
```

---

## 💡 Summary

| Concept | Key Point |
|---------|-----------|
| **Default constructor** | Provided by Java only if you write **no** constructors |
| **Parameterized constructor** | Lets you initialize fields at object creation |
| **`this` keyword** | Refers to current object; disambiguates fields from parameters |
| **Constructor chaining** | `this(args...)` calls another constructor in the same class |
| **Overloading** | Multiple constructors with different parameter lists |

---

## 🏋️ Assignments

### Assignment 1: Employee Class
Create a class `Employee` with fields `name` (String), `id` (int), and `salary` (double). Provide:
- A parameterized constructor that sets all three fields.
- A no-arg constructor that defaults name to `"Unknown"`, id to `0`, and salary to `30000.0`.
- A method `displayDetails()` that prints all fields.
- In `main`, create one employee using each constructor and call `displayDetails()`.

### Assignment 2: Circle with Constructor Chaining
Create a class `Circle` with field `radius` (double). Provide:
- A parameterized constructor `Circle(double radius)`.
- A no-arg constructor that chains to the parameterized one with radius `1.0`.
- A method `getArea()` that returns `Math.PI * radius * radius`.
- In `main`, create a circle with radius `5.0` and one with the default radius. Print both areas.

### Assignment 3: Book Library System
Create a class `Book` with fields `title`, `author`, `isbn` (String), and `isAvailable` (boolean).
- Provide constructors:
  - `Book(String title, String author, String isbn)` — sets isAvailable to `true` by default.
  - `Book(String title, String author)` — isbn defaults to `"N/A"`.
- Add a method `borrowBook()` that sets `isAvailable` to `false`.
- Add a method `returnBook()` that sets `isAvailable` to `true`.
- Add a method `displayStatus()` that prints all fields.
- In `main`, create two books, borrow one, and display both statuses.

### Bonus Challenge: Bank Account
Create a class `BankAccount` with fields `accountNumber` (String), `accountHolder` (String), and `balance` (double).
- Constructor 1: `BankAccount(String accountNumber, String accountHolder, double balance)`.
- Constructor 2: `BankAccount(String accountNumber, String accountHolder)` — balance defaults to `0.0`.
- Method `deposit(double amount)` — adds to balance.
- Method `withdraw(double amount)` — subtracts if sufficient funds, else prints "Insufficient balance".
- Method `displayAccount()` — prints account details.
- In `main`, create two accounts, perform some deposits/withdrawals, and display them.
