# Day 3: Operators in Java

## Overview
Operators in Java are special symbols used to perform operations on variables and values. They are essential for manipulating data and controlling the flow of a program.

## 1. Arithmetic Operators
Used to perform common mathematical operations.

| Operator | Name | Description | Example |
|---|---|---|---|
| `+` | Addition | Adds two values | `a + b` |
| `-` | Subtraction | Subtracts one value from another | `a - b` |
| `*` | Multiplication | Multiplies two values | `a * b` |
| `/` | Division | Divides one value by another | `a / b` |
| `%` | Modulus | Returns the division remainder | `a % b` |

**Example:**
```java
int x = 10;
int y = 3;

System.out.println(x + y); // 13
System.out.println(x - y); // 7
System.out.println(x * y); // 30
System.out.println(x / y); // 3 (Integer division drops the decimal)
System.out.println(x % y); // 1 (10 divided by 3 is 3, remainder 1)
```

## 2. Relational (Comparison) Operators
Used to compare two values. They always return a `boolean` (`true` or `false`).

| Operator | Name | Example |
|---|---|---|
| `==` | Equal to | `a == b` |
| `!=` | Not equal to | `a != b` |
| `>` | Greater than | `a > b` |
| `<` | Less than | `a < b` |
| `>=` | Greater than or equal to | `a >= b` |
| `<=` | Less than or equal to | `a <= b` |

**Example:**
```java
int a = 5;
int b = 8;

System.out.println(a == b); // false
System.out.println(a != b); // true
System.out.println(a > b);  // false
System.out.println(a <= b); // true
```

## 3. Logical Operators
Used to combine multiple boolean expressions.

| Operator | Name | Description | Example |
|---|---|---|---|
| `&&` | Logical AND | Returns `true` if BOTH statements are `true` | `x < 5 &&  x < 10` |
| `\|\|` | Logical OR | Returns `true` if ONE of the statements is `true` | `x < 5 \|\| x < 4` |
| `!` | Logical NOT | Reverses the result, returns `false` if the result is `true` | `!(x < 5 && x < 10)` |

**Example:**
```java
int age = 20;
boolean hasLicense = true;

// AND (both must be true)
System.out.println(age >= 18 && hasLicense); // true

// OR (at least one must be true)
System.out.println(age > 65 || age < 18); // false

// NOT (reverses the boolean)
System.out.println(!hasLicense); // false
```

## 4. Input with Scanner
Use `Scanner` to read values typed by the user in the console.

```java
import java.util.Scanner;

public class InputExample {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your name: ");
        String name = scanner.nextLine();

        System.out.print("Enter your age: ");
        int age = scanner.nextInt();

        System.out.println("Hello " + name + ", you are " + age + " years old.");
        scanner.close();
    }
}
```

- `nextLine()` reads a full line of text.
- `nextInt()` reads an integer.
- `nextDouble()` reads a decimal number.
- Always import `java.util.Scanner` at the top of the file.

---

## 💻 Practice Assignments

Create a new Java class named `OperatorPractice` and complete the following tasks inside the `main` method:

### Task 1: Basic Calculator
1. Declare two `double` variables, `num1` and `num2`, and assign them values.
2. Calculate and print the result of their addition, subtraction, multiplication, and division.
3. *Tip: Add clear text to your output, e.g., `System.out.println("Addition: " + (num1 + num2));`*

### Task 2: The Even/Odd Checker
1. Declare an `int` variable named `myNumber`.
2. Use the modulus operator (`%`) to determine if the number is even or odd. 
   *(Hint: An even number leaves a remainder of 0 when divided by 2.)*
3. Print a boolean expression that evaluates to `true` if the number is even.

### Task 3: Grade Evaluator
1. Declare an `int` variable named `score` and assign it a value between 0 and 100.
2. Write boolean expressions to check the following and print the results:
   * Is the score a passing grade? (Let's say passing is 60 or higher)
   * Is the score an 'A' grade? (90 or higher)
   * Is the score invalid? (Less than 0 OR greater than 100)

### Task 4: Eligibility Check
1. You are checking if someone is eligible for a special discount. 
2. They are eligible if they are a student (`boolean isStudent = true;`) OR if they are a senior citizen (`int age = 68;` - consider senior as 65 or older).
3. Write a logical expression using `||` to check eligibility and print the `boolean` result.

### Task 5: User Input Practice
1. Use `Scanner` to read a user's `name` and `favoriteNumber` from the console.
2. Print a greeting that includes the name and the number.
3. Example output: `Hello Maya, your favorite number is 8.`
