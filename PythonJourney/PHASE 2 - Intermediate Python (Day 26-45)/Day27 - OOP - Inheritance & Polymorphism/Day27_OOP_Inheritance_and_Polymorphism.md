# Day 27: OOP — Inheritance & Polymorphism

## Goal
Learn how inheritance and polymorphism help you build reusable and flexible object-oriented programs.

## Topics Covered
- Single and multiple inheritance
- Method overriding and the `super()` function
- Method Resolution Order (MRO)
- Abstract Base Classes (ABCs) using the `abc` module
- Polymorphism (duck typing in Python)
- Practice: Shape class hierarchy, animal speaking behaviors

## 1. Inheritance
Inheritance allows a class to reuse attributes and methods from another class.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"
```

## 2. `super()`
The `super()` function lets a child class call methods from its parent class.

```python
class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)
```

## 3. Method Overriding
A child class can replace a parent method with its own implementation.

```python
class Cat(Animal):
    def speak(self):
        return "Meow!"
```

## 4. Method Resolution Order (MRO)
Python determines which method to use when inheritance is involved.

```python
print(Dog.mro())
```

## 5. Abstract Base Classes (ABCs)
ABCs define a common interface for subclasses.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
```

## 6. Polymorphism
Polymorphism means different classes can share the same interface but behave differently.

```python
def make_sound(animal):
    print(animal.speak())

make_sound(Dog("Buddy"))
make_sound(Cat("Milo"))
```

## Practice Tasks
- Create a `Shape` hierarchy with `Circle`, `Rectangle`, and `Triangle` classes.
- Build an `Animal` class hierarchy with different `speak()` behaviors.
- Use `super()` in a subclass to extend parent behavior.

## Mini Challenge
Create a `Vehicle` base class and subclasses such as `Car` and `Bike`, each with a `move()` method.

## Summary
Inheritance helps avoid repetition, while polymorphism makes code more flexible and easier to extend.
