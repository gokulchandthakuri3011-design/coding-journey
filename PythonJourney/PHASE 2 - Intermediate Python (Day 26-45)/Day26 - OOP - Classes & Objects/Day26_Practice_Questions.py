"""
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
"""
# 1. 'Car' class
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def show_info(self):
        print(f"Car's Brand: {self.brand}")
        print(f"Car's Manufactured Date: {self.year}")

car1 = Car("BMW", 1940)
car1.show_info()

# 2. 'Student' class
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Student's Name: {self.name}")
        print(f"Student's Age: {self.age}")
        print(f"Student's Grade: {self.grade}")

# 3. 'BankAccount' class
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} is deposited.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn")
        else:
            print("Insufficient Balance")

# 4. Create objects and use the classes
car2 = Car("Toyota", 2018)
car2.show_info()

student1 = Student("Asha", 15, "Grade 9")
student1.display_info()

account = BankAccount(100)
account.deposit(50)
account.withdraw(30)
account.withdraw(200)

# 5. Difference between a class and an object
print("\nQ5. Class vs Object:")
print("A class is a blueprint or template that defines the structure and behavior.")
print("An object is a real instance created from that blueprint, with its own data.")

# 6. Purpose of 'self' in a class method
print("\nQ6. Purpose of 'self':")
print("'self' refers to the current object. It lets a method access the object's")
print("own attributes and methods (e.g., self.balance refers to this object's balance).")

# 7. Difference between an instance variable and a class variable
print("\nQ7. Instance variable vs Class variable:")
print("An instance variable belongs to each individual object and is set in __init__.")
print("A class variable belongs to the class and is shared by all objects.")

class StudentWithClassVar:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

s1 = StudentWithClassVar("Asha")
s2 = StudentWithClassVar("Ravi")
print(f"Class variable: {s1.school} and {s2.school}")
print(f"Instance variable: {s1.name} and {s2.name}")

# 8. 'Book' class with __str__()
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book('{self.title}' by {self.author})"

book1 = Book("Python Basics", "Guido")
print(f"\nQ8. {book1}")

# 9. 'Person' class that stores name, age, and city
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def display_info(self):
        print(f"{self.name} is {self.age} years old and lives in {self.city}.")

print("\nQ9:")
person1 = Person("Mina", 25, "Chennai")
person1.display_info()