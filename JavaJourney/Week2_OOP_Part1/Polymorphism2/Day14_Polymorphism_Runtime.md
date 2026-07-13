# Day 14: Polymorphism (Runtime) in Java

Welcome to Day 14! Today we learn about **runtime polymorphism** in Java, also known as **method overriding** and **object casting**.

While compile-time polymorphism (Day 13) is resolved by the compiler, runtime polymorphism is resolved by the JVM at execution time. This is the heart of OOP flexibility.

---

## 1. What is Runtime Polymorphism?

Runtime polymorphism happens when the JVM decides which method to call at **runtime** based on the actual object type, not the reference type.

Key terms:
- **Method Overriding**: Subclass provides its own implementation of a parent class method.
- **Upcasting**: Treating a subclass object as its parent type.
- **Downcasting**: Treating a parent reference back as the subclass type.

This is also called **dynamic binding** or **late binding**.

---

## 2. Method Overriding

### Rules for Method Overriding
A method is overridden when:
1. The subclass has the **same method name** as the parent.
2. The **parameter list** is exactly the same.
3. The **return type** is the same (or a subtype in Java 16+, called covariant return).
4. The access modifier is **not more restrictive** than the parent's.
5. The method cannot be `static`, `final`, or `private`.

### Example: `Animal` and `Dog`

```java
class Animal {
    protected String name;

    public Animal(String name) {
        this.name = name;
    }

    public String makeSound() {
        return "Some generic sound";
    }

    public void displayInfo() {
        System.out.println("Name: " + name);
    }
}

class Dog extends Animal {
    private String breed;

    public Dog(String name, String breed) {
        // super(name) calls the parent class constructor to initialize the Animal name
        super(name);
        this.breed = breed;
    }

    // @Override indicates this method overrides a method from the parent class.
    @Override
    public String makeSound() {
        return "Woof!";
    }

    @Override
    public void displayInfo() {
        // Call parent's displayInfo() to reuse code (prints name)
        super.displayInfo();
        System.out.println("Breed: " + breed);
    }
}

class Cat extends Animal {
    public Cat(String name) {
        super(name);
    }

    @Override
    public String makeSound() {
        return "Meow!";
    }
}
```

```java
public class TestAnimals {
    public static void main(String[] args) {
        Animal myDog = new Dog("Buddy", "Golden Retriever"); // Reference type = Animal, actual type = Dog
        Animal myCat = new Cat("Whiskers"); // Reference type = Animal, actual type = Cat

        System.out.println(myDog.makeSound());  // Prints: Woof!
        System.out.println(myCat.makeSound());  // Prints: Meow!

        myDog.displayInfo();
        System.out.println("---");
        myCat.displayInfo();
    }
}
```

### Key Points
- The variable type is `Animal`, but the **actual object** is `Dog` or `Cat`.
- The JVM looks at the **actual object** at runtime and calls the correct method.
- This is why `myDog.makeSound()` prints "Woof!" even though the reference is `Animal`.

---

## 3. The `@Override` Annotation

The `@Override` annotation tells the compiler: *"This method should override a parent class method."*

### Why use it?
- **Safety**: If the parent method changes or you misspell the name, the compiler throws an error.
- **Readability**: It clearly signals intent to other developers.
- **Bug prevention**: Without it, you might accidentally create a new method instead of overriding.

### Example: Without `@Override` (Danger!)

```java
class Bird extends Animal {
    @Override
    public String makeSound() {
        return "Chirp!";
    }

    // If you misspell the method name:
    public String makeSoudn() {  // Typo! No @Override = no compiler warning
        return "Chirp!";
    }
}
```

Without `@Override`, the typo `makeSoudn` silently creates a brand new method instead of overriding. With `@Override`, the compiler catches this mistake.

---

## 4. Upcasting and Downcasting

### Upcasting (Automatic)

Upcasting means treating a subclass object as its parent type. This happens automatically in Java.

```java
Dog myDog = new Dog("Rex", "German Shepherd");
Animal myAnimal = myDog;  // Upcasting — automatic and safe
```

- **Always safe**: A `Dog` **is an** `Animal`.
- **Limitation**: You can only access methods defined in the parent class.

### Downcasting (Manual)

Downcasting means converting a parent reference back to the subclass type. This must be done explicitly.

```java
Animal myAnimal = new Dog("Rex", "German Shepherd");
// The object created is a Dog, but the variable type is Animal.
// This is upcasting: a subclass object is referenced by a parent type.
Dog myDog = (Dog) myAnimal;  // Downcasting — explicit, can fail!
// Downcasting converts the parent reference back to the subclass type.
// This is required when you want to use Dog-specific members.
```

- **Can fail** with `ClassCastException` if the object is not actually that subclass.
  - Example failure: if `myAnimal` referred to a `Cat`, casting to `Dog` would throw an error.
- Use `instanceof` to check before downcasting:

```java
if (myAnimal instanceof Dog) {
    // `instanceof` checks the real object type at runtime.
    Dog myDog = (Dog) myAnimal;
    // After the cast, myDog is a Dog reference again.
    System.out.println(myDog.breed);  // Now you can access Dog-specific fields
    // Access to Dog-only fields and methods is safe because the object is confirmed to be a Dog.
}
```

### Example: `BankAccount` Hierarchy

```java
class BankAccount {
    protected String accountNumber;
    protected double balance;

    public BankAccount(String accountNumber, double balance) {
        this.accountNumber = accountNumber;
        this.balance = balance;
    }

    public void displayInfo() {
        System.out.println("Account: " + accountNumber + ", Balance: $" + balance);
    }

    public void withdraw(double amount) {
        if (amount <= balance) {
            balance -= amount;
            System.out.println("Withdrawn: $" + amount);
        } else {
            System.out.println("Insufficient funds!");
        }
    }
}

class SavingsAccount extends BankAccount {
    private double interestRate;

    public SavingsAccount(String accountNumber, double balance, double interestRate) {
        super(accountNumber, balance);
        this.interestRate = interestRate;
    }

    @Override
    public void displayInfo() {
        super.displayInfo();
        System.out.println("Interest Rate: " + interestRate + "%");
    }

    public void addInterest() {
        double interest = balance * (interestRate / 100);
        balance += interest;
        System.out.println("Interest added: $" + interest);
    }
}

class CheckingAccount extends BankAccount {
    private double overdraftLimit;

    public CheckingAccount(String accountNumber, double balance, double overdraftLimit) {
        super(accountNumber, balance);
        this.overdraftLimit = overdraftLimit;
    }

    @Override
    public void withdraw(double amount) {
        if (amount <= balance + overdraftLimit) {
            balance -= amount;
            System.out.println("Withdrawn: $" + amount);
        } else {
            System.out.println("Exceeds overdraft limit!");
        }
    }

    public double getOverdraftLimit() {
        return overdraftLimit;
    }
}
```

```java
public class TestBankAccounts {
    public static void main(String[] args) {
        // Upcasting: treating subclasses as BankAccount
        BankAccount account1 = new SavingsAccount("SA-001", 1000.0, 2.5);
        BankAccount account2 = new CheckingAccount("CA-002", 500.0, 200.0);

        // Runtime polymorphism: correct withdraw method is called
        account1.withdraw(300);   // Withdrawn: $300 (SavingsAccount logic)
        account2.withdraw(600);   // Withdrawn: $600 (CheckingAccount logic)

        account1.displayInfo();
        System.out.println("---");
        account2.displayInfo();

        // Downcasting: accessing subclass-specific methods
        if (account1 instanceof SavingsAccount) {
            SavingsAccount savings = (SavingsAccount) account1;
            savings.addInterest();  // Access SavingsAccount-specific method
        }

        if (account2 instanceof CheckingAccount) {
            CheckingAccount checking = (CheckingAccount) account2;
            System.out.println("Overdraft Limit: $" + checking.getOverdraftLimit());
        }
    }
}
```

---

## 5. How the JVM Resolves Method Calls

When you call a method on a reference:

1. The compiler checks that the method **exists** in the reference type.
2. At runtime, the JVM looks at the **actual object** the reference points to.
3. The JVM calls the method defined in the **actual object's class** (or closest ancestor that overrides it).

### Example: Resolution Flow

```java
Animal animal = new Dog("Max", "Labrador");
animal.makeSound();
// Step 1: Compiler sees Animal has makeSound() — OK
// Step 2: JVM sees actual object is Dog
// Step 3: JVM calls Dog's makeSound() — "Woof!"
```

---

## 6. Concepts Map

### Runtime Polymorphism Map

1. Polymorphism
   - Compile-Time (Static Binding)
     - Method Overloading
     - Constructor Overloading
   - Runtime (Dynamic Binding)
     - Method Overriding
     - Upcasting / Downcasting

2. Method Overriding
   - Same name, same parameters
   - Subclass provides new implementation
   - `@Override` annotation for safety

3. Casting
   - Upcasting: Subclass → Parent (automatic, safe)
   - Downcasting: Parent → Subclass (explicit, use `instanceof`)

4. Key Rule
   - JVM resolves the method based on the **actual object type** at runtime.

---

## Assignment Questions

1. **Shape Hierarchy**: Create a `Shape` superclass with an abstract-like `double area()` method (return 0). Create `Circle` (with `radius`) and `Rectangle` (with `width`, `height`) subclasses that override `area()`. Write a `printArea(Shape s)` method that uses runtime polymorphism to print the area of any shape.

2. **Employee System**: Create an `Employee` superclass with `name` and `salary` fields and a `calculateBonus()` method returning 5% of salary. Create `Manager` (bonus = 10%) and `Developer` (bonus = 7%) subclasses. Use upcasting to store both in an `Employee[]` array and calculate bonuses for all.

3. **Payment System**: Create a `Payment` superclass with a `processPayment(double amount)` method. Create `CreditCardPayment` (adds 2% fee) and `PayPalPayment` (adds $1 fixed fee) subclasses. Write a `processAll(Payment[] payments)` method that processes each payment using runtime polymorphism.

4. **Vehicle Rental**: Create a `Vehicle` superclass with `rentPerDay` and a `calculateRentalCost(int days)` method. Create `Car` (rent = $50/day) and `Truck` (rent = $100/day) subclasses. Use downcasting to access a `getCargoCapacity()` method on `Truck` objects.

5. **Game Characters**: Create a `GameCharacter` superclass with `name`, `health`, and `attack()` method. Create `Warrior` (physical attack), `Mage` (magic attack), and `Archer` (ranged attack) subclasses. Each overrides `attack()` to print a different attack message. Use an array of `GameCharacter` and call `attack()` on each.

---

## Practical Notes

- Runtime polymorphism is one of the four main OOP concepts.
- Always use `@Override` when overriding methods — it prevents subtle bugs.
- Upcasting is safe and automatic; downcasting requires `instanceof` checks.
- The JVM decides which method to call at runtime based on the **actual object**, not the reference type.
- Use runtime polymorphism when you want different objects to respond to the same method call in their own way.
