# Day 27: OOP — Inheritance & Polymorphism

## Goal
Learn how inheritance and polymorphism help you build reusable and flexible object-oriented programs, and understand how Python resolves methods when classes are connected by inheritance.

## Inheritance & Polymorphism Mind Map
```text
Inheritance & Polymorphism
├── Inheritance
│   ├── Parent / Base / Super class
│   ├── Child / Derived / Sub class
│   ├── Single inheritance
│   ├── Multiple inheritance
│   ├── Multilevel inheritance
│   └── Method overriding
├── super()
│   └── Calling parent methods & __init__
├── MRO (Method Resolution Order)
│   ├── C3 linearization
│   ├── .mro() and __mro__
│   └── Diamond problem
├── Abstract Base Classes (ABC)
│   ├── ABC class
│   ├── @abstractmethod
│   └── Enforcing a common interface
├── Polymorphism
│   ├── Same interface, different behavior
│   ├── Duck typing ("if it walks like a duck...")
│   ├── Method overriding (runtime polymorphism)
│   └── Operator overloading / built-in functions
└── is-a vs has-a relationship
```

---

## 1. What is Inheritance?
Inheritance lets a **child class** reuse attributes and methods from a **parent class**. The child "is-a" specialized version of the parent.

### Key idea
- Parent class = general blueprint (e.g., `Animal`)
- Child class = specialized blueprint (e.g., `Dog`, `Cat`)
- Child gets everything the parent has, plus its own extras.

### Example
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Dog(Animal):
    pass  # inherits everything from Animal

d = Dog("Buddy")
print(d.name)    # Buddy  (from parent)
print(d.speak()) # Some sound (inherited)
```

### Explanation
- `class Dog(Animal):` means `Dog` inherits from `Animal`.
- We did not write `__init__` or `speak` in `Dog`, yet `Dog` has them. That is inheritance in action.

---

## 2. Method Overriding
A child class can **replace** a parent method with its own implementation.

### Example
```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

print(Dog().speak())  # Woof!  (overridden)
print(Cat().speak())  # Meow!  (overridden)
```

### Key points
- The method name and signature stay the same; only the body changes.
- Overriding is how we give each child its own personality.

---

## 3. The `super()` Function
`super()` lets a child class call a method from its parent class. This avoids repeating parent logic.

### Example 1 — calling parent `__init__`
```python
class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name)   # sets self.name using parent logic
        self.can_fly = can_fly
```

### Example 2 — extending a parent method
```python
class Dog(Animal):
    def speak(self):
        return "Woof!"

    def greet(self):
        return f"{super().speak()}! I am {self.name}."
```

### Key points
- `super().__init__(...)` runs the parent constructor before adding child-specific attributes.
- It works without writing the parent class name, so it is safe with multiple inheritance.

---

## 4. Types of Inheritance

### 4.1 Single inheritance
One child, one parent.
```python
class Car(Vehicle):   # Car inherits from one parent
    pass
```

### 4.2 Multilevel inheritance
A child becomes a parent of another class.
```python
class Animal: pass
class Mammal(Animal): pass
class Dog(Mammal): pass   # Dog → Mammal → Animal
```

### 4.3 Multiple inheritance
One child inherits from two or more parents.
```python
class Flyer:
    def fly(self):
        return "Flying"

class Swimmer:
    def swim(self):
        return "Swimming"

class Duck(Flyer, Swimmer):
    pass

d = Duck()
print(d.fly())   # Flying
print(d.swim())  # Swimming
```

### Caution
Multiple inheritance is powerful but can create confusion when both parents define the same method. Python resolves this using the MRO (next section).

---

## 5. Method Resolution Order (MRO)
MRO is the order Python follows to find a method when it is not found in the current class. Python uses the **C3 linearization** algorithm.

### Example
```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print(D.mro())
# [<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>]
```

### The diamond problem
```text
        A
       / \
      B   C
       \ /
        D
```
Python solves this by visiting each ancestor only once, in a consistent order (left-to-right, depth-first), and every class appears **once** in the MRO.

### Key points
- `ClassName.mro()` returns the search order as a list.
- `ClassName.__mro__` returns the same as a tuple.
- If a method exists in multiple parents, the one that appears **first** in the MRO wins.

---

## 6. Abstract Base Classes (ABCs)
An ABC defines a **contract/interface**: what methods a subclass *must* implement, without saying how.

### Example
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
```

### Usage
```python
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius
```

### Key points
- A class marked with `@abstractmethod` **cannot be instantiated** directly:
  ```python
  Shape()  # TypeError: Can't instantiate abstract class Shape
  ```
- Any subclass that does not implement all abstract methods also cannot be instantiated.
- ABCs force every subclass to follow the same interface, making code predictable.

---

## 7. Polymorphism
Polymorphism means "many forms": different classes share the **same method name** but each behaves **differently**. The calling code does not care which exact class it is working with.

### Example — shared interface
```python
def make_sound(animal):
    print(animal.speak())

make_sound(Dog("Buddy"))   # Woof!
make_sound(Cat("Milo"))    # Meow!
make_sound(Bird("Tweety")) # (inherited "Some sound")
```

### Explanation
- `make_sound()` only needs an object with a `speak()` method.
- It works with any class that provides `speak()` — you can add new animal types without touching `make_sound`.

---

## 8. Duck Typing
Duck typing is polymorphism in its purest Pythonic form: *"If it walks like a duck and quacks like a duck, then it must be a duck."* What matters is that the object has the required method, **not** its class.

### Example
```python
class Duck:
    def sound(self):
        return "Quack!"

class AlarmClock:
    def sound(self):
        return "Ring ring!"

def announce(obj):
    print(obj.sound())

announce(Duck())        # Quack!
announce(AlarmClock())  # Ring ring!  (no inheritance needed)
```

### Key point
- `AlarmClock` is unrelated to `Duck`, but it still works because it has a `sound()` method.
- Python checks for the **method**, not the **class**.

---

## 9. Polymorphism with Built-in Functions & Operators
Python itself uses polymorphism everywhere.

```python
print(len("hello"))   # 5  (str)
print(len([1, 2, 3])) # 3  (list)

print(3 + 4)          # 7   (int)
print("3" + "4")      # "34" (str)
```
Same function/operator, different types, different results.

---

## 10. is-a vs has-a
- **is-a** (inheritance): `Dog is an Animal` → use inheritance.
- **has-a** (composition): `Car has an Engine` → use an attribute.
```python
class Engine:
    pass

class Car:
    def __init__(self):
        self.engine = Engine()   # composition
```

---

## 11. A Complete Example
```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return f"{self.name} is driving on roads."

class Bike(Vehicle):
    def move(self):
        return f"{self.name} is riding on two wheels."

class Boat(Vehicle):
    def move(self):
        return f"{self.name} is sailing on water."

def travel(vehicle):
    print(vehicle.move())

travel(Car("Tesla"))
travel(Bike("Royal Enfield"))
travel(Boat("Titanic"))
```

---

## Practice Questions
1. What is inheritance? Why is it useful?
2. Explain the difference between method overriding and the `super()` function.
3. Write a parent class `Person` with `name` and `age`, and a child class `Student` that adds `grade`.
4. Create `Employee` (with `salary`) and `Manager` (adds `bonus`) classes. Use `super()` in `Manager.__init__`.
5. What is MRO and how can you view it in Python?
6. Draw the diamond inheritance problem and explain how Python resolves it.
7. Write an abstract class `Appliance` with an abstract method `turn_on()`, then create `Fan` and `Microwave` subclasses.
8. What is duck typing? Show an example where two unrelated classes work with the same function.
9. Is the following allowed? Explain what happens and why.
   ```python
   class Shape:
       def area(self):
           return 0
   ```
10. Explain the difference between `is-a` and `has-a` relationships with examples.
11. What will this print? Trace the MRO.
    ```python
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(B, C): pass
    print(D.__mro__)
    ```
12. Modify the `make_sound()` example so it also works with a `Robot` class that has a `speak()` method but is **not** a subclass of `Animal`.

---

## Mini Assignment
Build a small **Library System**:
- Create a base class `LibraryItem` with `title`, `year`, and an abstract `describe()` method.
- Create `Book` (adds `author`, `pages`) and `DVD` (adds `director`, `duration`) subclasses.
- Each subclass implements `describe()` with its own text.
- Create a list of items (mix of books and DVDs) and print the description of each using a single loop.
- Add one extra item type of your choice (e.g., `Magazine`) without changing the loop.

---

## Mini Challenge
Create a `Vehicle` base class and subclasses `Car` and `Bike`, each with a `move()` method. Then:
1. Use an abstract `move()` so subclasses must implement it.
2. Use `super()` in at least one subclass to extend the parent `__init__`.
3. Write a single function that accepts any vehicle and prints `"<name> moves by: <move result>"`.
4. Print the MRO of each subclass and explain the order.

---

## Summary
Inheritance lets a child class reuse and extend a parent's attributes and methods, while `super()` and the MRO keep multi-level and multiple inheritance clean. ABCs enforce a consistent interface, and polymorphism — especially duck typing — lets the same code work with many different classes. Together they make code DRY (Don't Repeat Yourself), flexible, and easy to extend.
