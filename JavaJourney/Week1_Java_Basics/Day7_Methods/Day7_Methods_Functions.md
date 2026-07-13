# Java Methods (Functions)

## What is a Method?
- A method is a block of code that performs a specific task.
- In Java, methods are functions defined inside a class.
- Methods help organize code, avoid repetition, and make programs easier to read.

## Method Parts
- **Return type**: the type of value the method gives back. Use `void` when it does not return anything.
- **Method name**: the label used to call the method.
- **Parameters**: input values passed into the method inside parentheses.
- **Method body**: code inside `{}` that runs when the method is called.

Example:
```java
public int add(int a, int b) {
    int result = a + b;
    return result;
}
```

## Why Use Methods?
- Reuse code without copying and pasting.
- Break problems into smaller, easier steps.
- Make code easier to test and debug.
- Give meaningful names to actions.

## Types of Methods
1. **Void methods**
   - Do not return a value.
   - Example: `printMessage()`.
2. **Return methods**
   - Return a value using the `return` keyword.
   - Example: `int multiply(int x, int y)`.
3. **Methods with parameters**
   - Receive input values to use inside the method.
   - Example: `void greet(String name)`.
4. **Methods without parameters**
   - Do not require any input.
   - Example: `double getPi()`.

## Declaring vs Calling a Method
- **Declare**: write the method inside a class.
- **Call**: execute the method from `main` or another method.

Example:
```java
public class Example {
    public static void main(String[] args) {
        sayHello();
    }

    public static void sayHello() {
        System.out.println("Hello, Java!");
    }
}
```

## Method Syntax
```java
[access modifier] [static] returnType methodName(parameterList) {
    // method body
}
```
- `public` is an access modifier that makes the method visible from other classes.
- `static` means the method belongs to the class, not an object instance.
- `parameterList` can be empty or include one or more parameters.

## Notes
- Java methods are always inside a class.
- The `main` method is also a method: `public static void main(String[] args)`.
- Use meaningful names: `calculateSum`, `printReport`, `isEven`.
- A method can call another method.
- A return type must match the value returned.
- If a method uses `return` early, the rest of the code after that statement does not run.

## Examples
### Example 1: Void method
```java
public static void printStars() {
    System.out.println("*****");
}
```

### Example 2: Method with return value
```java
public static int square(int number) {
    return number * number;
}
```

### Example 3: Method with multiple parameters
```java
public static double average(int a, int b, int c) {
    return (a + b + c) / 3.0;
}
```

## Best Practices
- Keep methods short and focused.
- One method should do one clear job.
- Avoid very long methods with many tasks.
- Use comments for tricky logic.
- Prefer returning values instead of using global variables.

## Practice Assignments
Use these assignments to practice methods, arrays, loops, conditions, and `Scanner` input together. Each task should be solved using helper methods and array processing loops.

1. Student Score Analyzer
   - Read an integer `n` for how many scores you will enter.
   - Read `n` exam scores into an `int[] scores` array.
   - Write `double calculateAverage(int[] arr)` to compute the average using a loop.
   - Write `int findMax(int[] arr)` to return the highest score.
   - Write `int countPassing(int[] arr, int passingScore)` to return how many scores are >= `passingScore`.
   - In `main`, print the average, highest score, and passing count.

2. Search and Reverse Array
   - Read an integer `n`, then read `n` integers into an `int[] numbers` array.
   - Read one additional integer `target`.
   - Write `int findIndex(int[] arr, int target)` to return the first index of `target` or `-1` if not found.
   - Write `int[] reverseArray(int[] arr)` to return a new array with elements in reverse order.
   - In `main`, print the target index and the reversed array.

3. Even/Odd Array Processor
   - Read an integer `n`, then read `n` numbers into an `int[] data` array.
   - Write `int sumEven(int[] arr)` to return the sum of even values.
   - Write `int sumOdd(int[] arr)` to return the sum of odd values.
   - Write `int[] filterGreaterThan(int[] arr, int limit)` to return a new array of values greater than `limit`.
   - In `main`, print the even sum, odd sum, and values greater than a chosen limit.

4. Simple Array Statistics Menu
   - Read an integer `n`, then read `n` integers into an `int[] values` array.
   - Write `int findMin(int[] arr)` and `int findMax(int[] arr)`.
   - Write `int sumArray(int[] arr)`.
   - Write `void printArray(int[] arr)` to display all values.
   - In `main`, use a simple menu loop to let the user choose: show min, show max, show sum, show all values, or exit.

### Helpful Notes
- Use `Scanner` in `main` to read input once and pass arrays/values into methods.
- Each method should do one job: calculate, find, filter, or print.
- Use `for` loops to process arrays, not one method doing everything.
- Keep method names descriptive and easy to call from `main`.
