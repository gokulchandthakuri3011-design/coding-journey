# Day 15: Abstraction

## What is Abstraction?

Abstraction is the concept of **hiding complex implementation details** and showing only the essential features of an object. It lets you focus on **what** an object does rather than **how** it does it.

**Real-world analogy**: When you drive a car, you use the steering wheel, accelerator, and brakes. You don't need to understand how the engine, transmission, or fuel injection system works internally. The pedals and steering wheel **abstract away** the complexity of the car's inner workings.

In Java, abstraction is achieved through:
- **Abstract classes** — partial abstraction (can mix abstract + concrete methods)
- **Interfaces** — full abstraction (all methods abstract by default, covered on Day 16)

---

## Why Use Abstraction?

1. **Reduces complexity** — Users of your class only see what they need.
2. **Improves maintainability** — You can change internal implementation without affecting code that uses your class.
3. **Forces a contract** — Subclasses are required to implement specific behaviors.
4. **Encourages code reuse** — Common code lives in the abstract class; each subclass provides its own specialized behavior.

---

## Abstract Classes

An abstract class is a class declared with the `abstract` keyword. It sits between a fully concrete class and an interface — it can have **both** implemented methods and methods without a body.

```java
abstract class Animal {
    protected String name;

    // Constructor — yes, abstract classes CAN have constructors!
    public Animal(String name) {
        this.name = name;
    }

    // Abstract method — no body, just a declaration ending with semicolon.
    // Every concrete subclass MUST override this.
    public abstract void makeSound();

    // Concrete method — has a body, inherited as-is by subclasses.
    public void sleep() {
        System.out.println(name + " is sleeping");
    }
}
```

### Key Rules — Explained

| Rule | Why? |
|---|---|
| Cannot be instantiated (`new Animal(...)` fails) | An abstract class is incomplete by design — it has methods with no body. Creating an object from it would let you call methods that don't exist. |
| Can have constructors | The constructor is called via `super()` from the subclass to initialize shared fields. You never call `new` on the abstract class itself. |
| Can have fields, concrete/static/final methods | This is what makes abstract classes more powerful than interfaces — they can hold state and provide shared code. |
| Subclass **must** override all abstract methods | Otherwise the subclass would still be incomplete (abstract itself). The compiler enforces this. |

### Detailed Example: Shape Hierarchy

```java
abstract class Shape {
    protected String color;

    public Shape(String color) {
        this.color = color;
    }

    // Every shape must be able to calculate its area, but the formula differs.
    // So we declare it abstract and let each subclass define it.
    public abstract double getArea();

    // All shapes can display their color the same way — concrete method.
    public void displayColor() {
        System.out.println("Color: " + color);
    }
}

class Circle extends Shape {
    private double radius;

    public Circle(String color, double radius) {
        super(color);  // calls Shape's constructor to set the color
        this.radius = radius;
    }

    @Override
    public double getArea() {
        return Math.PI * radius * radius;  // πr²
    }
}

class Rectangle extends Shape {
    private double width, height;

    public Rectangle(String color, double width, double height) {
        super(color);
        this.width = width;
        this.height = height;
    }

    @Override
    public double getArea() {
        return width * height;
    }
}
```

```java
public class TestShapes {
    public static void main(String[] args) {
        // Shape s = new Shape("red");  // ❌ Compile error — cannot instantiate

        Shape s1 = new Circle("Red", 5.0); // Upcasting
        Shape s2 = new Rectangle("Blue", 4.0, 6.0); // Upcasting

        // Runtime polymorphism — correct getArea() is called based on actual object
        System.out.println("Circle area: " + s1.getArea());   // 78.5398...
        System.out.println("Rectangle area: " + s2.getArea()); // 24.0

        s1.displayColor();  // Color: Red (inherited concrete method)
        s2.displayColor();  // Color: Blue
    }
}
```

### What happens step-by-step?

1. `Shape s1 = new Circle("Red", 5.0);` — Upcasting: reference is `Shape`, object is `Circle`.
2. `s1.getArea()` — Compiler checks `Shape` has `getArea()` ✅. JVM sees actual object is `Circle`, calls `Circle`'s overridden `getArea()`.
3. `s1.displayColor()` — `Shape` provides a concrete `displayColor()`; `Circle` didn't override it, so the inherited version runs.

---

## When to Use an Abstract Class?

| Use an abstract class when... | Instead use an interface when... |
|---|---|
| Subclasses share common **state** (fields like `color`, `name`) | You only need a **contract** with no shared state |
| Subclasses share **partial implementation** (some methods are the same) | Every implementing class would write everything from scratch |
| You want a **template** that subclasses fill in | You need classes from different hierarchies to share a capability |
| The classes are **closely related** in a hierarchy | The classes are **unrelated** but need to do the same thing |

### Examples

- **Good for abstract class**: `Vehicle` → `Car`, `Truck`, `Motorcycle` — all have `speed`, `fuel`, `drive()` might differ but `displayInfo()` is shared.
- **Not good for abstract class**: `Flyable` — `Airplane`, `Bird`, `Drone` share no common state; use an interface instead.

---

## Common Pitfalls

| Mistake | Why it's wrong |
|---|---|
| Instantiating an abstract class | Compiler error — the class is incomplete |
| Forgetting `@Override` in subclass | You might accidentally define a new method instead of overriding |
| Making everything abstract | If all methods are abstract, use an interface instead |
| Using abstract when implementation won't vary | If every subclass would have the same implementation, just use a concrete class |

---

## Concepts Map

```
Abstraction
│
├── What: Hide complexity, show essentials
│
├── How: abstract keyword
│
├── Abstract Class Rules
│   ├── Cannot instantiate
│   ├── Can have constructors
│   ├── Can have fields + concrete + abstract methods
│   └── Subclass must implement all abstract methods
│
├── When to use
│   ├── Shared state + partial implementation
│   ├── Closely related classes
│   └── Template design pattern
│
└── Key takeaway
    └── Abstract classes let you DEFINE what subclasses must do
        while also PROVIDING shared code they can use.
```

---

## Practice Questions

1. **Abstract Animal**: Create an abstract class `Animal` with:
   - A `String name` field and a constructor
   - An abstract method `void makeSound()`
   - A concrete method `void eat(String food)` that prints `"[name] is eating [food]"`
   - Create `Dog` (prints "Woof!") and `Cat` (prints "Meow!") subclasses
   - In `main()`, create an `Animal[]` array, store both, and call `makeSound()` and `eat()` on each 

2. **Vehicle System**: Create an abstract class `Vehicle` with:
   - Fields `String brand` and `int speed`
   - A constructor to set both
   - An abstract method `void accelerate()` (each vehicle accelerates differently)
   - A concrete method `void displayInfo()` that prints brand and speed
   - Create `Car` (accelerate prints "Car is speeding up") and `Motorcycle` (accelerate prints "Motorcycle is revving")
   - Test with upcasting

3. **Appliance**: Create an abstract class `Appliance` with:
   - A `String brand` field
   - An abstract method `void turnOn()`
   - A concrete method `void plugIn()` that prints "Plugged into outlet"
   - Create `Fan` (turnOn prints "Fan is spinning") and `TV` (turnOn prints "TV is displaying")
   - Test both

4. **Bank Account System**: Create an abstract class `BankAccount` with:
   - Fields `String accountNo` and `double balance`
   - Constructor, getters for both fields
   - Abstract method `void withdraw(double amount)` (withdrawal logic differs)
   - Concrete method `void deposit(double amount)` that adds to balance and prints the new balance
   - Create `SavingsAccount` (withdraw only if balance >= amount, else print insufficient) and `CheckingAccount` (allows overdraft up to $500)
   - Test depositing and withdrawing from both

5. **Employee Salary Calculator**: Create an abstract class `Employee` with:
   - Fields `String name` and `int id`
   - Constructor
   - Abstract method `double calculateSalary()`
   - Concrete method `void displayInfo()` that prints name, id, and salary
   - Create `FullTimeEmployee` (has `double monthlySalary`, `calculateSalary()` returns monthlySalary) and `PartTimeEmployee` (has `int hoursWorked` and `double hourlyRate`, `calculateSalary()` returns hours * rate)
   - Create an array, store both types, calculate and display salaries
