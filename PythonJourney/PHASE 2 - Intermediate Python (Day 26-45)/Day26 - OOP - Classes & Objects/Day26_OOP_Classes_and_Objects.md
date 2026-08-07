# Day 26: OOP — Classes & Objects

## Goal
Understand the core ideas of Object-Oriented Programming (OOP) and how classes and objects work in Python.

## OOP Mind Map
```text
OOP
├── Class
├── Object
├── Attributes
├── Methods
├── Constructor (__init__)
├── self
├── Instance vs Class Variables
└── Special Methods (__str__, __repr__)
```

## What is OOP?
Object-Oriented Programming is a way of organizing code around real-world concepts.
Instead of writing separate variables and functions, you group related data and behavior into a single unit called a class.

### Why use OOP?
- Makes code easier to understand
- Helps organize large programs
- Encourages reuse
- Makes maintenance simpler

---

## 1. Class vs Object
A class is a blueprint.
An object is a real thing created from that blueprint.

### Example
```python
class Car:
    pass

my_car = Car()
print(my_car)
```

### Explanation
- `Car` is the class.
- `my_car` is an object created from the class.

---

## 2. Creating a Class
A class is created using the `class` keyword.

```python
class Dog:
    pass
```

### Example with attributes and methods
```python
class Dog:
    def bark(self):
        print("Woof!")
```

### Explanation
- `bark()` is a method inside the class.
- `self` is used so the method can access the object’s data.

---

## 3. Creating Objects
An object is created by calling the class like a function.

```python
class Dog:
    def bark(self):
        print("Woof!")

my_dog = Dog()
my_dog.bark()
```

### Important idea
Every object created from the same class has its own identity and can have its own data.

---

## 4. Attributes and Methods
Attributes store data.
Methods define behavior.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
```

### Example
```python
s1 = Student("Alice", 20)
s1.show_info()
```

### Explanation
- `name` and `age` are attributes.
- `show_info()` is a method.

---

## 5. The `__init__()` Constructor
The `__init__()` method runs automatically when an object is created.
It is used to initialize the object’s attributes.

```python
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Rahul")
print(p1.name)
```

### Key points
- `__init__()` is a special method.
- It helps set up the object when it is born.

---

## 6. Understanding `self`
`self` refers to the current object.
It helps the class access its own attributes and methods.

```python
class Book:
    def __init__(self, title):
        self.title = title

    def display(self):
        print(self.title)
```

### Example
```python
b1 = Book("Python Basics")
b1.display()
```

### Explanation
- `self.title` means “the title of this particular object.”

---

## 7. Instance Variables vs Class Variables
### Instance variables
These belong to each individual object.

```python
class Student:
    def __init__(self, name):
        self.name = name
```

### Class variables
These belong to the class itself and are shared by all objects.

```python
class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name
```

### Example
```python
s1 = Student("Asha")
s2 = Student("Ravi")
print(s1.school)
print(s2.school)
```

---

## 8. Special Methods: `__str__()` and `__repr__()`
These methods define how an object looks when printed.

```python
class Laptop:
    def __init__(self, brand):
        self.brand = brand

    def __str__(self):
        return f"Laptop({self.brand})"
```

### Example
```python
l1 = Laptop("Dell")
print(l1)
```

### Explanation
Without `__str__()`, Python would show a default object representation.

---

## 9. A Complete Example
```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}")
        else:
            print("Insufficient balance")

    def show_balance(self):
        print(f"Balance: {self.balance}")
```

### Usage
```python
account = BankAccount("Mina", 100)
account.deposit(50)
account.show_balance()
```

---

## Practice Questions
1. Create a class called `Car` with attributes `brand` and `year`.
2. Create an object of the `Car` class and print its attributes.
3. Write a `Student` class with `name`, `age`, and `grade`.
4. Add a method `display_info()` to the `Student` class.
5. Create a `BankAccount` class with `deposit()` and `withdraw()` methods.
6. Explain the difference between a class and an object.
7. What is the purpose of `self` in a class method?
8. What is the difference between an instance variable and a class variable?
9. Create a `Book` class and use `__str__()` to print a readable message.
10. Build a `Person` class that stores `name`, `age`, and `city`.

---

## Mini Assignment
Create a small program with these requirements:
- Define a `Product` class
- Store `name`, `price`, and `quantity`
- Add a method `total_price()` that returns the total cost
- Create 2 objects and print their details

---

## Summary
A class is a blueprint, and an object is an instance created from that blueprint. OOP helps you model real-world ideas in a structured and reusable way.
