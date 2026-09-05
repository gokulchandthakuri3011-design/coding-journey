"""
### Easy
1. Write a `@staticmethod` `is_valid_mail(email)` on a `User` class that returns `True` if the email contains `"@"`.
2. Write a `@classmethod` `from_string(cls, s)` on a `User` class that takes `"name:age"` and returns a new `User`.
"""

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def is_valid_mail(email):
        return '@' in email

    @classmethod
    def from_string(cls, s):
        name, age = s.split(':')
        return cls(name, int(age))

c = User.from_string("Alice:30")
print(c.name)
print(c.age)

# Since is_valid_mail is a static method not bound to an instance attribute, we can call it directly on the class itself.
print(User.is_valid_mail("alice@example.com"))
