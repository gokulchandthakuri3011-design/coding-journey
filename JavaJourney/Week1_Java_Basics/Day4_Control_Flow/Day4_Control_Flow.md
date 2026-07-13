# Day 4: Control Flow (Conditionals)

Welcome to Day 4! Today we are learning how to make our Java programs make decisions. Up until now, our code has executed sequentially, line by line. Control flow statements allow us to change that path based on specific conditions.

## 1. The `if` Statement

The `if` statement is the most basic control flow statement. It tells the program to execute a certain section of code *only if* a particular test evaluates to `true`.

**Syntax:**
```java
if (condition) {
    // code to execute if condition is true
}
```

**Example:**
```java
int temperature = 30;

if (temperature > 25) {
    System.out.println("It's a hot day!");
}
```

## 2. The `else` Statement

You can use an `else` statement to execute a block of code if the `if` condition evaluates to `false`.

**Syntax:**
```java
if (condition) {
    // code if condition is true
} else {
    // code if condition is false
}
```

**Example:**
```java
boolean isRaining = false;

if (isRaining) {
    System.out.println("Take an umbrella.");
} else {
    System.out.println("Enjoy the weather!");
}
```

## 3. The `else if` Statement

When you have more than two possible conditions, you can use `else if` to chain multiple tests together.

**Syntax:**
```java
if (condition1) {
    // code if condition1 is true
} else if (condition2) {
    // code if condition1 is false AND condition2 is true
} else {
    // code if both condition1 and condition2 are false
}
```

**Example:**
```java
int score = 85;

if (score >= 90) {
    System.out.println("Grade: A");
} else if (score >= 80) {
    System.out.println("Grade: B");
} else if (score >= 70) {
    System.out.println("Grade: C");
} else {
    System.out.println("Grade: F");
}
```

## 4. The `switch` Statement

The `switch` statement is an alternative to a long `if-else-if` chain, especially when you are testing the same variable against different exact values (like integers, chars, or Strings).

**Syntax:**
```java
switch (variableToTest) {
    case value1:
        // code if variableToTest == value1
        break; // Important! Stops executing further cases
    case value2:
        // code if variableToTest == value2
        break;
    default:
        // code if none of the cases match
}
```

**Example:**
```java
int dayOfWeek = 3;
String dayName;

switch (dayOfWeek) {
    case 1: dayName = "Monday"; break;
    case 2: dayName = "Tuesday"; break;
    case 3: dayName = "Wednesday"; break;
    case 4: dayName = "Thursday"; break;
    case 5: dayName = "Friday"; break;
    case 6: dayName = "Saturday"; break;
    case 7: dayName = "Sunday"; break;
    default: dayName = "Invalid Day"; break;
}
System.out.println("Day " + dayOfWeek + " is " + dayName);
```
> **Note:** The `break` keyword is crucial. Without it, execution will "fall through" and execute the code in subsequent cases even if they don't match!

## 5. The Ternary Operator

The ternary operator is a compact way to write a simple `if-else` expression in one line.

**Syntax:**
```java
result = condition ? valueIfTrue : valueIfFalse;
```

**Example:**
```java
int number = 10;
String type = (number % 2 == 0) ? "Even" : "Odd";
System.out.println(type); // prints "Even"
```

**When to use it:**
* Use the ternary operator when you need to choose between two values based on a condition.
* Avoid it when the logic becomes complex; a full `if-else` block is easier to read.

---

## 💻 Day 4 Practice Assignments

Create a new file named `Day4.java` and write the code for the following tasks within your `main` method.

### Task 1: Even or Odd Checker
Write a program that declares an integer variable `number` and assigns it a value. Use an `if-else` statement (and the modulo operator `%` from Day 3) to print whether the number is "Even" or "Odd".

### Task 2: Discount Calculator
You are writing software for a store. Declare a `double` variable `purchaseAmount`.
* If the amount is $100 or more, apply a 20% discount.
* If the amount is between $50 and $99.99, apply a 10% discount.
* If the amount is less than $50, no discount is applied.
Calculate and print the final price the customer needs to pay.

### Task 3: Simple Calculator using `switch`
Declare two `double` variables `num1` and `num2`, and a `char` variable `operator` (e.g., '+', '-', '*', '/'). 
Use a `switch` statement based on the `operator` variable to perform the corresponding mathematical operation and print the result. Handle the case of dividing by zero (using an `if` statement inside the division case) and provide a `default` case for invalid operators.

Happy coding! Once you've tried these, feel free to ask if you need hints or want to review your solutions.
