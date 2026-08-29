# 🔧 OOP Advanced Features — Notes (Day 28)

> **Topics covered:** Class/Static methods, Encapsulation, Properties, Operator overloading, Memory optimization.

---

## 1. Class Methods vs Static Methods

- **Instance methods:** receive `self` (the instance).
- **Class methods** (`@classmethod`): receive `cls` (the class itself). Often used as alternative constructors.

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @classmethod
    def from_string(cls, data):
        brand, model = data.split("-")
        return cls(brand, model)   # creates a new instance

c = Car.from_string("Toyota-Corolla")
```

- **Static methods** (`@staticmethod`): receive neither `self` nor `cls`. Used for utility functions that relate to the class logically but don't need instance/class data.

```python
class MathUtils:
    @staticmethod
    def is_even(n):
        return n % 2 == 0
```

**Key difference summary:**

| Type | First arg | When to use |
|------|-----------|-------------|
| Instance method | `self` | Needs instance state |
| Class method | `cls` | Needs class state / alternative constructor |
| Static method | none | Utility, no class/instance state |

---

## 2. Encapsulation

Controlling access to data to keep the internal state safe.

- **Public** — accessible everywhere: `self.name`
- **Protected** (convention, `_` prefix) — "internal use", not enforced: `self._value`
- **Private** (`__` prefix) — name-mangled to `_ClassName__value`, harder to access accidentally:

```python
class Bank:
    def __init__(self, amount):
        self.__balance = amount      # private -> self._Bank__balance

    def deposit(self, n):
        self.__balance += n

b = Bank(100)
print(b._Bank__balance)   # 100 (mangled, but still accessible)
```

> Encapsulation is about convention and protecting the object's invariants — not absolute security.

---

## 3. Properties — `@property`

Getters and setters with validation, using a clean attribute-like syntax instead of `get_()`/`set_()` methods.

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):                  # getter
        return self._radius

    @radius.setter
    def radius(self, value):           # setter
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):                    # computed property (read-only)
        return 3.14159 * self.radius ** 2
```

Now usage is natural:

```python
c = Circle(5)
c.radius = 7      # uses setter
print(c.area)     # uses property
```

- **Uses:** validation, computed values, lazy loading, read-only attributes.

---

## 4. Magic / Dunder Methods — Operator Overloading

Special methods (double underscore) that let you define behavior for operators and built-ins.

```python
class Money:
    exchange_rate = 1.0

    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):                 # +
        return Money(self.amount + other.amount)

    def __eq__(self, other):                  # ==
        return self.amount == other.amount

    def __lt__(self, other):                  # <
        return self.amount < other.amount

    def __len__(self):                        # len()
        return int(self.amount)

    def __getitem__(self, key):               # obj[key]
        return self.amount

    def __str__(self):                        # print()
        return f"${self.amount:.2f}"

    def __repr__(self):                       # debugging
        return f"Money({self.amount})"
```

**Common dunder methods:**

| Method | Operator / Built-in |
|--------|---------------------|
| `__add__` | `+` |
| `__sub__` | `-` |
| `__mul__` | `*` |
| `__truediv__` | `/` |
| `__eq__`, `__ne__` | `==`, `!=` |
| `__lt__`, `__gt__`, `__le__`, `__ge__` | `<`, `>`, `<=`, `>=` |
| `__getitem__`, `__setitem__` | `obj[key]` |
| `__len__` | `len()` |
| `__contains__` | `in` |
| `__str__`, `__repr__` | `str()`, `print()`, debugging |

> **Note:** With `@dataclass`, many of these (`__eq__`, `__repr__`, etc.) are generated automatically.

---

## 5. Memory Optimization — `__slots__`

By default, each object has a `__dict__` to store attributes (memory heavy). `__slots__` declares a fixed set of attributes, saving significant memory when creating many instances.

```python
class Point:
    __slots__ = ("x", "y")     # only these attributes allowed

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
p.z = 3   # AttributeError: 'Point' object has no attribute 'z'
```

- **Benefits:** less memory, faster attribute access.
- **Trade-offs:** cannot add new attributes, no `__dict__` (unless also listed in `__slots__`).
- **Use when:** creating thousands/millions of instances (e.g., data records, table rows).

---

## 6. Quick Reference — Property vs Classmethod vs Staticmethod

```python
class Employee:
    company = "ACME"                         # class variable

    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @staticmethod
    def is_valid_name(name):                 # utility, no self/cls
        return bool(name.strip())

    @classmethod
    def from_string(cls, s):                 # alternative constructor
        name, salary = s.split(",")
        return cls(name, float(salary))

    @property
    def salary(self):                        # getter
        return self._salary

    @salary.setter
    def salary(self, value):                 # setter with validation
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value

    def __repr__(self):                      # debug representation
        return f"Employee({self.name!r}, {self.salary!r})"
```

---

> **Practice ideas:** Currency/Money class with arithmetic, custom dictionary-like class, a validation-driven `__slots__` data class.
