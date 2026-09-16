/*
3. Design an `Animal` superclass with a `species` field and a `makeSound()` method.
   Create a `Dog` subclass that overrides `makeSound()` to print a dog-specific sound.
   Add a constructor in `Dog` that calls `super(species)`.
*/

package Week2_OOP_Part1.Day12_Inheritance;

public class Animal {
    private String species;

    // Constructor
    public Animal(String species) {
        this.species = species;
    }

    // Method to make sound
    public void makeSound() {
        System.out.println(species + " is my Pet and makes sound.");
    }
}

class Dog extends Animal {
    String sound;

    // Constructor
    public Dog(String species, String sound) {
        super(species);
        this.sound = sound;
    }

    // Overriding makeSound() method
    @Override 
    public void makeSound() {
        super.makeSound();
        System.out.println("Dog makes: " + sound + " sound.");
    }

    // Main method
    public static void main(String[] args) {
        Dog myDog = new Dog("Golden Retriever", "Woof..Woof...Woo..!");
        myDog.makeSound();
    }
}
