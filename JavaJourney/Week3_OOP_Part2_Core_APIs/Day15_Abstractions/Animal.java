package Week3_OOP_Part2_Core_APIs.Day15_Abstractions;


/*
1. **Abstract Animal**: Create an abstract class `Animal` with:
   - A `String name` field and a constructor
   - An abstract method `void makeSound()`
   - A concrete method `void eat(String food)` that prints `"[name] is eating [food]"`
   - Create `Dog` (prints "Woof!") and `Cat` (prints "Meow!") subclasses
   - In `main()`, create an `Animal[]` array, store both, and call `makeSound()` and `eat()` on each 
*/

public abstract class Animal {
    protected String name;

    // Constructor
    public Animal (String name) {
        this.name = name;
    }

    // Abstract method
    public abstract void makeSound();

    // Concrete Method
    public void eat(String food) {
        System.out.println(name + " is eating " + food);
    }
}

class Dog extends Animal {

    public Dog(String name) {
        super(name);
    }

    @Override
    public void makeSound() {
        System.out.println("Woof!");
    }
}

class Cat extends Animal {
    
    public Cat(String name) {
        super(name);
    }

    @Override
    public void makeSound() {
        System.out.println("Meow!");
    }
}

class testAnimal {
    public static void main(String[] args) {
        // Upcasting
        Animal a1 = new Dog("Montu");
        Animal a2 = new Cat("Billi");

        // Runtimepolymorphism - correct makeSound is called based on object
        a1.eat("Dog Food"); // That's why we had to pass arguments here
        a1.makeSound();
        a2.eat("Cat Food");
        a2.makeSound();
    }
}
