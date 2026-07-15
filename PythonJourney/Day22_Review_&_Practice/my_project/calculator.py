"""Calculator"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def division(a, b):
    if b == 0:
        print("Division by Zero not possible!")
    return a / b

def modulo(a, b):
    if b == 0:
        print("Modulo division by Zero not possible!")
    return a % b

if __name__ == "__main__":
    print("\n  Running calculator Module tests..  ")
    print(add(8, 2))
    print(subtract(8, 2))
    print(multiply(8, 2))
    print(division(8, 2))
    print(modulo(8, 2))