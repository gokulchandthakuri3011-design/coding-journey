# Day 19: Exception Handling Basics

## 📌 Learning Goals
By the end of this day, you will understand:
- What exceptions are and why they occur
- The difference between errors and exceptions
- How to handle exceptions gracefully using `try`, `catch`, and `finally` blocks
- How to prevent programs from crashing unexpectedly
- Best practices for exception handling

---

## 🔍 What is an Exception?

An **exception** is an event that disrupts the normal flow of a program. It's an error condition that occurs during program execution.

### Examples of Exceptions:
- **Division by zero:** `int result = 10 / 0;`
- **Null Pointer Exception:** Accessing a method on a null object
- **Array Index Out of Bounds:** Accessing an array element that doesn't exist
- **NumberFormatException:** Converting an invalid string to a number
- **File Not Found Exception:** Trying to open a file that doesn't exist

### Why Handle Exceptions?
Without exception handling, your program would **crash** and stop executing. Exception handling allows you to:
1. **Prevent crashes** — Continue execution gracefully
2. **Provide feedback** — Tell users what went wrong
3. **Log errors** — Record what happened for debugging
4. **Clean up resources** — Release files, connections, etc.

---

## 🛡️ Exception Hierarchy

```
Throwable (parent of all errors and exceptions)
├── Error (serious problems - usually can't be recovered)
│   ├── OutOfMemoryError
│   ├── StackOverflowError
│   └── ...
└── Exception (problems your program should handle)
    ├── Checked Exceptions (must handle - will cover Day 20)
    │   ├── IOException
    │   ├── FileNotFoundException
    │   └── ...
    └── Unchecked Exceptions (don't have to handle)
        ├── NullPointerException
        ├── ArrayIndexOutOfBoundsException
        ├── ArithmeticException
        ├── NumberFormatException
        └── ...
```

---

## 💡 The try-catch-finally Block

### Basic Syntax:

```java
try {
    // Code that might throw an exception
    int result = 10 / 0;  // This will throw ArithmeticException
    System.out.println("Result: " + result);
} 
catch (ArithmeticException e) {
    // Code to handle the exception
    System.out.println("Error: Cannot divide by zero!");
    System.out.println("Exception message: " + e.getMessage()); // e points to the exception object created by Java; getMessage() is a method of the Exception class, and gets the error message 
} 
finally {
    // Code that ALWAYS runs, whether exception occurred or not
    System.out.println("Calculation complete.");
}
```

### Output:
```
Error: Cannot divide by zero!
Exception message: / by zero
Calculation complete.
```

---

## 🔑 Key Components Explained

### 1️⃣ **try Block**
- Contains code that **might throw an exception**
- If an exception occurs, execution immediately jumps to the `catch` block
- If no exception occurs, `catch` is skipped and code continues

```java
try {
    int x = Integer.parseInt("abc");  // This throws NumberFormatException
    System.out.println(x);  // This line is SKIPPED
}
```

### 2️⃣ **catch Block**
- Catches specific exceptions that occur in the `try` block
- You can have **multiple `catch` blocks** for different exception types
- Executed only if the matching exception occurs

```java
catch (NumberFormatException e) {
    System.out.println("Please enter a valid number!");
}
catch (Exception e) {
    System.out.println("An error occurred: " + e);
}
```

**Important:** Order matters! Java checks `catch` blocks from top to bottom. A broad catch like `Exception` should come after more specific ones, otherwise it may catch everything and prevent the specific catch from running.

```java
try {
    int x = Integer.parseInt("abc");
}
catch (Exception e) {
    System.out.println("Something went wrong");
}
catch (NumberFormatException e) {
    System.out.println("Please enter a valid number!");
}
```

This is wrong because the first `catch` catches `NumberFormatException` too, so the second `catch` is never reached.

```java
try {
    int x = Integer.parseInt("abc");
}
catch (NumberFormatException e) {
    System.out.println("Please enter a valid number!");
}
catch (Exception e) {
    System.out.println("Something went wrong");
}
```

This is correct because the specific exception is handled first, and the general one is used as a backup.

### 3️⃣ **finally Block**
- **Always executes**, whether exception occurred or not
- Used for **cleanup** (closing files, releasing resources)
- Optional (you can have try-catch without finally)

```java
try {
    // risky code
}
catch (Exception e) {
    // handle error
}
finally {
    System.out.println("This ALWAYS runs!");
}
```

---

## 📋 Common Exception Types

| Exception | Cause | Example |
|-----------|-------|---------|
| `ArithmeticException` | Math error | `10 / 0` |
| `NullPointerException` | Accessing null object | `String s = null; s.length();` |
| `ArrayIndexOutOfBoundsException` | Invalid array index | `arr[arr.length]` |
| `NumberFormatException` | Invalid number string | `Integer.parseInt("abc")` |
| `ClassCastException` | Invalid type casting | `Object o = "hello"; Integer i = (Integer) o;` |
| `StringIndexOutOfBoundsException` | Invalid string index | `str.charAt(100)` when str is small |

---

## 💻 Practical Examples

### Example 1: Handling Division by Zero

```java
public class DivisionExample {
    public static void main(String[] args) {
        System.out.print("Enter divisor: ");
        Scanner sc = new Scanner(System.in);
        
        try {
            int dividend = 20;
            int divisor = sc.nextInt();  // User enters 0
            int result = dividend / divisor;
            System.out.println("Result: " + result);
        }
        catch (ArithmeticException e) {
            System.out.println("Error: Cannot divide by zero!");
        }
        catch (InputMismatchException e) {
            System.out.println("Error: Please enter a valid integer!");
        }
        finally {
            sc.close();
            System.out.println("Scanner closed.");
        }
    }
}
```

### Example 2: Handling Number Format Exception

```java
public class NumberFormatExample {
    public static void main(String[] args) {
        String[] numbers = {"10", "20", "abc", "30"};
        
        for (String num : numbers) {
            try {
                int value = Integer.parseInt(num);
                System.out.println("Converted: " + value);
            }
            catch (NumberFormatException e) {
                System.out.println("Error converting '" + num + "': Not a valid number");
            }
        }
    }
}
```

**Output:**
```
Converted: 10
Converted: 20
Error converting 'abc': Not a valid number
Converted: 30
```

### Example 3: Handling Null Pointer Exception

```java
public class NullPointerExample {
    public static void main(String[] args) {
        String name = null;
        
        try {
            System.out.println("Length: " + name.length());  // NullPointerException
        }
        catch (NullPointerException e) {
            System.out.println("Error: name is null!");
        }
    }
}
```

### Example 4: Multiple catch Blocks

```java
public class MultipleCatchExample {
    public static void main(String[] args) {
        try {
            String input = "abc";
            int number = Integer.parseInt(input);  // NumberFormatException
            int[] arr = {1, 2, 3};
            System.out.println(arr[10]);  // ArrayIndexOutOfBoundsException
        }
        catch (NumberFormatException e) {
            System.out.println("Error: Invalid number format!");
        }
        catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Error: Array index out of bounds!");
        }
        catch (Exception e) {
            System.out.println("An unexpected error occurred: " + e.getMessage());
        }
        finally {
            System.out.println("Program finished.");
        }
    }
}
```

---

## 📍 Exception Information Methods

```java
try {
    // code that throws exception
}
catch (Exception e) {
    e.printStackTrace();          // Prints full stack trace
    e.getMessage();               // Returns error message
    e.toString();                 // Returns exception type + message
    e.getClass().getName();       // Returns just the exception class name
}
```

**Example:**
```java
try {
    int x = 10 / 0;
}
catch (ArithmeticException e) {
    System.out.println(e.getMessage());      // Output: / by zero
    System.out.println(e.getClass().getName()); // Output: java.lang.ArithmeticException
}
```

---

## ⚠️ Best Practices

1. **Be Specific** — Catch specific exceptions, not just generic `Exception`
   ```java
   // ❌ Bad
   catch (Exception e) { }
   
   // ✅ Good
   catch (NumberFormatException e) { }
   ```

2. **Don't Catch and Ignore** — Always handle the error meaningfully
   ```java
   // ❌ Bad
   catch (Exception e) {
       // Do nothing
   }
   
   // ✅ Good
   catch (Exception e) {
       System.out.println("Error: " + e.getMessage());
   }
   ```

3. **Catch in Order** — Catch specific exceptions before general ones
   ```java
   // ❌ Wrong
   catch (Exception e) { }
   catch (NumberFormatException e) { }  // Never reached!
   
   // ✅ Correct
   catch (NumberFormatException e) { }
   catch (Exception e) { }
   ```

4. **Use finally for Cleanup** — Always close resources
   ```java
   Scanner sc = null;
   try {
       sc = new Scanner(System.in);
       // use scanner
   }
   finally {
       if (sc != null) {
           sc.close();
       }
   }
   ```

---

## 🎯 Key Takeaways

| Concept | Description |
|---------|-------------|
| **Exception** | An error condition that disrupts normal program flow |
| **try block** | Contains risky code that might throw an exception |
| **catch block** | Handles the exception if it occurs |
| **finally block** | Always executes, used for cleanup |
| **Multiple catches** | Handle different exception types differently |
| **Exception methods** | `getMessage()`, `printStackTrace()`, `getClass().getName()` |

---

## 📚 Assignment Questions

### Easy Tasks

**1. Division Calculator with Exception Handling**
   - Write a program that takes two numbers from the user and divides them
   - Handle `ArithmeticException` (division by zero)
   - Handle `InputMismatchException` (user enters non-integer)
   - Display appropriate error messages

**2. String to Integer Converter**
   - Take a string input from the user
   - Convert it to an integer using `Integer.parseInt()`
   - Handle `NumberFormatException`
   - Display the converted number or an error message

**3. Array Access Validator**
   - Create an array of 5 integers
   - Ask user for an index to access
   - Handle `ArrayIndexOutOfBoundsException`
   - Display the element or an error message

### Medium Tasks

**4. Multiple Exception Handling**
   - Create a program that:
     - Takes a string from input
     - Takes an index from input
     - Prints the character at that index in the string
   - Handle `NumberFormatException` (if index is not a number)
   - Handle `StringIndexOutOfBoundsException` (if index is out of bounds)
   - Display appropriate messages for each error

**5. Grade Calculator with Exception Handling**
   - Take marks for 5 subjects from the user
   - Calculate average
   - Display grade based on average
   - Handle `InputMismatchException` (non-integer input)
   - Handle `ArithmeticException` (if needed)
   - Use `finally` to display a completion message

**6. Null Pointer Handler**
   - Create a method that takes a String parameter
   - Check if the string is null using try-catch
   - Display the string's length or "String is null"
   - Test with both null and non-null values

### Hard Tasks

**7. Robust User Input System**
   - Create a method `getPositiveInteger(String prompt)` that:
     - Repeatedly asks for input until a valid positive integer is entered
     - Handles `InputMismatchException` and `NumberFormatException`
     - Returns only when valid input is received
   - Test the method with various invalid and valid inputs

**8. Calculator Application**
   - Build a calculator that performs: addition, subtraction, multiplication, division
   - Takes two numbers and an operation from the user
   - Handles all possible exceptions:
     - Invalid numbers
     - Invalid operation
     - Division by zero
   - Displays operation result or appropriate error message
   - Use `finally` to close the scanner

**9. File Name Extractor (Preview for Day 26)**
   - Take a file path as input (e.g., "document.pdf")
   - Extract the file name and extension
   - Handle cases where:
     - The string is null
     - The string is empty
     - The string has no dot (invalid format)
   - Display file name, extension, or error message

**10. Exception Analysis Program**
   - Create methods that intentionally throw different exceptions:
     - Method 1: Throws `ArithmeticException`
     - Method 2: Throws `NullPointerException`
     - Method 3: Throws `ArrayIndexOutOfBoundsException`
   - Call each method from main inside try-catch blocks
   - For each caught exception, display:
     - Exception type
     - Exception message
     - Suggested fix
     - Status message in finally

---

## 🔗 Connection to Next Day (Day 20)
On **Day 20: Exception Handling - Advanced**, you will learn:
- `throw` keyword — How to throw your own exceptions
- `throws` keyword — How to declare exceptions in method signatures
- Checked vs. Unchecked exceptions
- Creating custom exception classes

---

## 💾 Code Files to Create
Create the following Java files in this folder to complete the assignments:
- `EasyTask1_DivisionCalculator.java`
- `EasyTask2_StringToInteger.java`
- `EasyTask3_ArrayAccess.java`
- `MediumTask4_MultipleExceptions.java`
- `MediumTask5_GradeCalculator.java`
- `MediumTask6_NullPointerHandler.java`
- `HardTask7_RobustInput.java`
- `HardTask8_Calculator.java`
- `HardTask9_FileNameExtractor.java`
- `HardTask10_ExceptionAnalysis.java`

---

## ⏱️ Daily Time Breakdown
- **15-20 min:** Read this guide and understand the concepts
- **30-35 min:** Code the assignments (start with Easy, then Medium)
- **5-10 min:** Review your code, add comments, summarize what you learned

**Today's Focus:** Master `try-catch-finally` to handle exceptions gracefully!
