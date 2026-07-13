# Day 5: Loops in Java

Welcome to Day 5! Today we are learning how to repeat actions in Java so your program can do work more efficiently.

## 📝 Study Notes

### 1. Why Use Loops?
Loops allow your program to run the same block of code more than once without writing the same lines repeatedly. This is useful when you need to:
* Process a list of items
* Count up or down
* Repeat a task until a condition changes

### 2. The `for` Loop
The `for` loop is usually used when you know how many times you want to repeat something.

**Syntax:**
```java
for (initialization; condition; update) {
    // code to repeat
}
```

**Example:**
```java
for (int i = 1; i <= 5; i++) {
    System.out.println("Count: " + i);
}
```

What happens here?
* `int i = 1` starts the loop counter at 1
* `i <= 5` is the condition to keep looping
* `i++` increases `i` by 1 each time

### 3. The `while` Loop
A `while` loop repeats code as long as a condition stays true. Use it when you do not know exactly how many repetitions you need ahead of time.

**Syntax:**
```java
while (condition) {
    // code to repeat
}
```

**Example:**
```java
int n = 1;
while (n <= 5) {
    System.out.println("Number: " + n);
    n++;
}
```

> Important: Always make sure the condition can become false, otherwise the loop may never stop.

### 4. The `do-while` Loop
A `do-while` loop runs the loop body first, then checks the condition. This means the code runs at least once.

**Syntax:**
```java
do {
    // code to repeat
} while (condition);
```

**Example:**
```java
int x = 1;
do {
    System.out.println("Step: " + x);
    x++;
} while (x <= 3);
```

### 5. Loop Control: `break` and `continue`
* `break` stops the loop immediately and exits it.
* `continue` skips the rest of the current loop iteration and goes to the next one.

**Example:**
```java
for (int i = 1; i <= 10; i++) {
    if (i == 5) {
        break; // stop the loop when i equals 5
    }
    if (i % 2 == 0) {
        continue; // skip even numbers
    }
    System.out.println(i);
}
```

### 6. Common Loop Patterns
* Count from 0 to 9: `for (int i = 0; i < 10; i++) { ... }`
* Count down: `for (int i = 5; i > 0; i--) { ... }`
* Repeat until a user enters a stop word
* Search through a list of values using a loop and `if`

---

## 💻 Assignments
Create a new Java file for these exercises, for example `Day5Loops.java`.

### Exercise 1: Print a Sequence
Write a `for` loop that prints the numbers from 1 to 10, each on its own line.

### Exercise 2: Sum of Numbers
Use a loop to calculate the sum of the numbers from 1 to 20. Print the final result.

### Exercise 3: Even Numbers Only
Write a loop that prints only even numbers from 2 to 20. Use either `if` inside the loop or step by 2.

### Exercise 4: `while` Loop Practice
Use a `while` loop to print the following message 5 times:
```
Hello, Java learner!
```

### Exercise 5: Guessing Game Starter
Create a `do-while` loop that asks the user to enter a number from 1 to 5. If the number is not valid, the loop should ask again. For now, just simulate the user input by assigning a value to a variable and changing it until the loop condition becomes false.

### Exercise 6: `break` and `continue`
Write a loop from 1 to 10. Inside the loop:
* if the number is 3, use `continue` to skip printing it.
* if the number is 8, use `break` to stop the loop entirely.

### Challenge: Multiplication Table
Use a nested loop to print the multiplication table for 1 through 5.

**Example output:**
```
1 x 1 = 1
1 x 2 = 2
...
5 x 5 = 25
```

---

## ✅ Study Tips
* Start with simple loops and print values to understand how the counter changes.
* If a loop is not ending, check the condition and the update step.
* Use comments to explain what each loop is doing.
* Practice each loop type (`for`, `while`, `do-while`) so you can choose the right one.

Happy coding! Keep practicing loops and soon you will feel much more comfortable repeating tasks with Java.
