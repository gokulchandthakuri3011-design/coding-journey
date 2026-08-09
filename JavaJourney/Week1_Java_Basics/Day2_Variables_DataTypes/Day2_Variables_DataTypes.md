# Day 2: Variables & Data Types

Welcome to Day 2! Today we are learning how to store information in our programs. 

## 📝 Study Notes

### 1. What is a Variable?
Think of a variable as a **labeled box** in your computer's memory. You give the box a name, you tell Java what *type* of thing can fit inside the box, and then you can put data into it.

### 2. The Core Data Types
Java is a **strongly typed** language. This means you *must* declare what type of data a variable will hold before you can use it. 

Here are the 4 most common **primitive** (simple) data types you will use:
*   `int`: Stores whole numbers (e.g., `5`, `-10`, `1000`).
*   `double`: Stores decimal numbers (e.g., `3.14`, `-0.5`).
*   `boolean`: Stores only one of two values: `true` or `false`.
*   `char`: Stores a single character wrapped in single quotes (e.g., `'A'`, `'?'`, `'9'`).

And the most common **reference** (complex) data type:
*   `String`: Stores a sequence of text wrapped in double quotes (e.g., `"Hello World!"`). *Note: String starts with a capital 'S'!*

### 3. Declaring and Initializing Variables
There are two steps to making a variable:
1.  **Declaration:** Creating the box and giving it a name and a type.
2.  **Initialization:** Putting the first piece of data into the box.

```java
// Step 1: Declaration
int age; 

// Step 2: Initialization
age = 25; 

// Doing both at the same time (Most Common!)
double price = 19.99;
boolean isJavaFun = true;
char grade = 'A';
String name = "Alice";
```

### 4. Type Casting (Converting one data type to another)
Type casting means changing one data type into another.

**Implicit Casting (Widening)** — automatic, safe, no data loss. Happens when converting a *smaller* type to a *larger* type:
```java
int age = 25;
double ageAsDouble = age;      // int → double, automatic
long big = 1000;               // int literal fits into long
```
Order: `byte → short → int → long → float → double`

**Explicit Casting (Narrowing)** — manual, uses `(type)`, can lose data. Converting a *larger* type to a *smaller* one:
```java
double price = 9.99;
int roundedPrice = (int) price;   // 9 (decimal part dropped, not rounded!)

long huge = 4000000000L;
int small = (int) huge;           // 1410065408 (overflow! wraps around)
```

**Important notes**
- `(int)` **truncates**, it does NOT round — `(int) 3.99` is `3`, not `4`. For rounding use `Math.round(3.99)`.
- `char` ↔ numbers: `char letter = 'A'; int code = (int) letter; // 65 (ASCII)`
- `String` ↔ numbers (not a cast, done via methods):
  ```java
  int num = Integer.parseInt("123");
  String text = String.valueOf(123);   // or 123 + ""
  ```
- `boolean` cannot be cast to/from any numeric type.

> Narrowing can lose information, so `9.99` becomes `9` when cast to `int`.

### 5. Naming Rules (camelCase)
In Java, we use **camelCase** for naming variables. The first word is entirely lowercase, and every subsequent word starts with a capital letter. No spaces allowed!
*   ✅ Good: `firstName`, `playerScore`, `isGameOver`
*   ❌ Bad: `firstname`, `PlayerScore`, `is_game_over`

---

## 💻 Practice Exercises

Create a new Java file in your IDE (e.g., `Day2Practice.java`) to complete these exercises.

### Exercise 1: Create a User Profile
Write a program that stores your personal information in variables and then prints it out in a formatted way.
1. Create a `String` variable for your full name.
2. Create an `int` variable for your age.
3. Create a `double` variable for your height in meters (e.g., 1.75).
4. Create a `boolean` variable representing whether you like coffee (`true` or `false`).
5. Create a `char` variable for your favorite letter.
6. Use `System.out.println()` to print a profile summary to the console using your variables.

*Example Output:*
```text
--- User Profile ---
Name: John Doe
Age: 28
Height: 1.82m
Likes Coffee: true
Favorite Letter: J
```

### Exercise 2: The Swapping Challenge
This is a classic programming puzzle!
1. Create an `int` variable named `a` and set it to `10`.
2. Create an `int` variable named `b` and set it to `20`.
3. **Your Goal:** Write code that swaps the values of `a` and `b`, so that when you print them out, `a` is 20 and `b` is 10. 
*(Hint: You will need to create a third, temporary variable to hold one of the values while you swap them!)*

### Exercise 3: Spot the Bugs 🐞
Look at the following Java code snippet. There are **3 errors** related to variables and data types. Try to identify them without putting them in your IDE first!

```java
public class BugFinder {
    public static void main(String[] args) {
        int year = 2024.5; // Use double insted int
        string city = "New York"; // String is capitalized in Java (not lowercase 'string')
        boolean isValid = "true"; // Remove double quotation from true
        
        System.out.println(city + " in " + year);
    }
}
```

---
*Self-Correction / Review:* After you finish, take 5 minutes to add comments (`// your comment here`) to your code explaining *why* you chose specific data types for Exercise 1!
