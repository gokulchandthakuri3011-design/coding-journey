## Practice Questions
# 1. What is inheritance? Why is it useful?
# Answer: Its like subclass inheriting everything from the parent class as well as adding its own properties. It reduces code duplication and promotes code reusability.

# 2. Explain the difference between method overriding and the `super()` function.
# Answer: Method Overriding means child class implements a method from parent class with sam name, whereas 'super()' is used to call the parent class constructor or method from child class.

# 3. Write a parent class `Person` with `name` and `age`, and a child class `Student` that adds `grade`.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name,age)
        self.grade = grade

# 4. Create `Employee` (with `salary`) and `Manager` (adds `bonus`) classes. Use `super()` in `Manager.__init__`.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

# 5. What is MRO and how can you view it in Python?
# Answer: Method Resolution Order (MRO) is the order using *c3 linearization* algorithm to determine the order to search for a method in a hierarchy of classes. You can view it using the `__mro__` attribute or the `mro()` method.

# 6. Draw the diamond inheritance problem and explain how Python resolves it.
# Answer: The diamond inheritance problem occurs when a class inherits from two classes that have a common base class. For example:
#       A
#      / \
#     B   C
#      \ /
#       D
# In this case, class D inherits from both B and C, which both inherit from A. Python uses the C3 linearization algorithm to determine the method resolution order (MRO) and avoid ambiguity by ensuring that each class appears only once in the MRO.

# 7. Write an abstract class `Appliance` with an abstract method `turn_on()`, then create `Fan` and `Microwave` subclasses.
# Answer: 
from abc import ABC, abstractmethod
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class Fan(Appliance):
    def turn_on(self):
        print("Fan is now ON")

class Microwave(Appliance):
    def turn_on(self):
        print("Microwave is now on")

# 8. What is duck typing? Show an example where two unrelated classes work with the same function.
# Answer: Its a concept, where Python doesn't check "What an Object is(its class)" but "What an Object can do(its methods)".
# Example:
class Dog:
    def speak(self):
        print("Woof!")

class Meow_App:
    def speak(self):
        print("Meow!")

def sound(object):
    object.speak()

sound(Dog()) # Output: Woof!
sound(Meow_App()) # Output: Meow!

# 9. Is the following allowed? Explain what happens and why.

class Shape:
    def area(self):
        return 0

# Answer: Yes, this is allowed. The `Shape` class defines a method `area()` that returns 0. This can serve as a base class for other shapes (like Circle, Square, etc.) that will override the `area()` method to provide their specific implementations. The base class provides a default implementation, which can be useful for polymorphism.

# 10. Explain the difference between `is-a` and `has-a` relationships with examples.
"""Answer: 'is-a' refers to inheritance relationship
           'has-a' refers to composition relationship
Example of 'is-a': A Dog is an Animal (Dog inherits from Animal)
Example of 'has-a': A Car has an Engine (Car contains an instance of Engine)
"""

# 11. What will this print? Trace the MRO.
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass
print(D.__mro__)

# Answer: The ouput will be (<class'D'>, <class'B'>, <class'C'>, <class'A'>, <class'object'>)

# 12. Modify the `make_sound()` example so it also works with a `Robot` class that has a `speak()` method but is **not** a subclass of `Animal`.
class Robot:
    def speak(self):
        print("Beep Boop!")