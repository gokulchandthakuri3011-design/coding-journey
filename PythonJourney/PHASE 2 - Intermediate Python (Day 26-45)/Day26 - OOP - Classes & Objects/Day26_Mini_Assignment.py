"""
## Mini Assignment
Create a small program with these requirements:
- Define a `Product` class
- Store `name`, `price`, and `quantity`
- Add a method `total_price()` that returns the total cost
- Create 2 objects and print their details
"""
# Creating a class 'Product'
class Product:

    # Storing attributes
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return f" Total Price of Product {self.name} is: {self.price * self.quantity}"

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

# Creating 2 objects and printing their details
product1 = Product("Philips Trimmer", 75, 1)
product2 = Product("Stainless Topf", 44, 1)
print(product1) # Here it prints (<__main__.Product object at 0x10919ffd0>)
print(product2)

print(product1.total_price())
print(product2.total_price())