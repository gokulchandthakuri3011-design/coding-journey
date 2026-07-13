# Day 12: Inheritance

## What is inheritance?
Inheritance is a way for one class to reuse fields and methods from another class.
A subclass (child) extends a superclass (parent) and automatically gets its accessible behavior.
This helps avoid duplicated code and makes related classes easier to manage.

## Key concepts

* `extends` - used to create a subclass from a superclass.
* Superclass (parent) - the class being extended.
* Subclass (child) - the class that extends the superclass.
* `super` - used to call the parent class constructor or parent class methods.
* Constructor chaining - a subclass constructor can call `super(...)` to initialize parent fields.

## Simple example

In Java:

* `class Animal { ... }` is a superclass.
* `class Dog extends Animal { ... }` is a subclass.

The `Dog` class inherits public and protected fields and methods from `Animal`.

Example behavior:
* `Animal` may have a `name` field and a `makeSound()` method.
* `Dog` can add its own `breed` field and still use `name` and `makeSound()` from `Animal`.

## Using `super`

When a subclass constructor starts, it can call `super(...)` to run the parent constructor first.
This is important when the parent class has fields that must be initialized.

Example:

```
class Person {
    String name;

    Person(String name) {
        this.name = name;
    }
}

class Student extends Person {
    int grade;

    Student(String name, int grade) {
      super(name); // calls the Person constructor to initialize the inherited name field
        this.grade = grade;
    }
}
```

Here `super(name)` calls the parent (Person) constructor with the provided `name`, ensuring the inherited `name` field is initialized before the `Student` constructor continues.

## Why inheritance matters

* Reuse common code in one place (the superclass).
* Model real-world relationships (e.g., `Car` is a `Vehicle`).
* Make code easier to extend and maintain.

## Assignment questions

1. Create a `Vehicle` class with fields `make`, `model`, and `year`, plus a `displayInfo()` method.
   Then create a `Car` subclass that adds `numDoors` and uses `super(...)` in its constructor.
   Finally, override `displayInfo()` in `Car` to include the door count.

2. Build a `Person` superclass with `name` and `age` fields and a `introduce()` method.
   Create a `Teacher` subclass that adds `subject` and a `teach()` method.
   In `Teacher`, call `super.introduce()` from a new method.

3. Design an `Animal` superclass with a `species` field and a `makeSound()` method.
   Create a `Dog` subclass that overrides `makeSound()` to print a dog-specific sound.
   Add a constructor in `Dog` that calls `super(species)`.

4. Create a `Device` superclass with `brand` and `powerOn()` method.
   Create a `Phone` subclass with a `callNumber(String number)` method.
   Use `super` to access a superclass method or field from inside `Phone`.

5. Create a `Shape` superclass with a method `double area()` that returns `0`.
   Add a `Rectangle` subclass with `width` and `height` and override `area()`.
   Create a `Square` subclass of `Rectangle` and use constructor chaining with `super(...)`.

## Practical notes

* Inheritance is one of the four main OOP concepts.
* For Day 12, focus on `extends` and `super`.
* Keep your parent class simple and reusable.
* Use inheritance when classes share a clear "is-a" relationship.
