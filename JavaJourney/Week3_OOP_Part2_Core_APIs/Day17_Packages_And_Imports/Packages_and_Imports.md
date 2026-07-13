# Day 17 — Packages & Imports in Java

## 1. What is a Package?

A **package** in Java is a namespace that groups related classes and interfaces together. Think of it like folders on your computer — it keeps your code organized and prevents naming conflicts.

### Why use packages?

| Reason | Explanation |
|--------|-------------|
| **Organization** | Group related classes (e.g., all banking classes in `com.example.bank`) |
| **Avoid name clashes** | Two classes with the same name can exist in different packages |
| **Access control** | Packages work with access modifiers to control visibility |
| **Reusability** | Easily share a package of classes across projects |

### Naming Convention

- Use **reverse domain name** convention: `com.company.project`
- All lowercase
- Example: `com.learningjava.day17`

```java
// File: BankAccount.java
package com.example.bank;

public class BankAccount {
    private String accountNumber;
    private double balance;

    public BankAccount(String accountNumber, double balance) {
        this.accountNumber = accountNumber;
        this.balance = balance;
    }

    public void deposit(double amount) {
        this.balance += amount;
    }

    public void withdraw(double amount) {
        if (amount <= balance) {
            this.balance -= amount;
        }
    }
}
```

---

## 2. Declaring a Package

The `package` statement must be the **very first line** in a Java source file (comments before it are allowed).

```java
// This is a comment (allowed)
package com.example.myapp;  // MUST be the first non-comment line

public class MyClass {
    // class body
}
```

### Directory Structure

The package name must match the directory structure:

```
project-root/
└── src/
    └── com/
        └── example/
            └── myapp/
                └── MyClass.java
```

---

## 3. Importing Classes

The `import` statement allows you to use classes from other packages without writing their full qualified name.

### Three Ways to Import

#### a) Import a Specific Class

```java
import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);  // No need for full name
        ArrayList<String> list = new ArrayList<>();
    }
}
```

#### b) Import All Classes from a Package (Wildcard)

```java
import java.util.*;  // Imports ALL classes from java.util

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<String> list = new ArrayList<>();
        HashMap<String, Integer> map = new HashMap<>();
    }
}
```

> ⚠️ **Best Practice:** Prefer importing specific classes over wildcards. Wildcards can make code harder to read and may slightly impact compile time.

#### c) No Import Needed — `java.lang`

Classes in `java.lang` (like `String`, `System`, `Math`, `Integer`) are **automatically imported**. You never need to import them.

---

## 4. Static Imports

You can import **static members** (fields and methods) of a class.

```java
import static java.lang.Math.*;

public class MathExample {
    public static void main(String[] args) {
        double sqrt = sqrt(16);        // Instead of Math.sqrt(16)
        double max = max(10, 20);      // Instead of Math.max(10, 20)
        int random = (int) random();   // Instead of Math.random()
    }
}
```

```java
import static java.lang.System.out;

public class Greeting {
    public static void main(String[] args) {
        out.println("Hello from static import!");  // Instead of System.out.println()
    }
}
```

> ⚠️ **Best Practice:** Use static imports sparingly. They can reduce readability if overused.

---

## 5. Import Order Convention

Standard import order (as per Oracle and most style guides):

1. **Java's own imports** (e.g., `java.*`)
2. **Third-party imports** (e.g., `org.*`, `com.*`)
3. **Your project's imports**

```java
// 1. Java's own imports
import java.util.ArrayList;
import java.util.Scanner;

// 2. Third-party imports
import org.apache.commons.lang3.StringUtils;

// 3. Project's own imports
import com.example.myapp.models.User;
import com.example.myapp.utils.Helper;
```

---

## 6. Key Points to Remember

| Concept | Key Point |
|---------|-----------|
| `package` statement | Must be the first line (after comments) |
| One package per file | A file can declare only one package |
| Default package | If no package is declared, the class goes into the "default package" (avoid this in real projects) |
| `import` statement | Must come after `package` and before class definition |
| `java.lang` | Automatically imported — no import needed |
| Wildcard `*` | Imports all classes but prefer specific imports |
| Static import | Imports static members — use sparingly |
| Circular imports | Java does NOT allow circular dependencies between packages |

---

## 7. Commonly Used Packages

| Package | What it Contains |
|---------|-----------------|
| `java.lang` | Core classes (`String`, `System`, `Math`, `Integer`, etc.) — auto-imported |
| `java.util` | Utility classes (`Scanner`, `ArrayList`, `HashMap`, `Date`, `Calendar`) |
| `java.io` | Input/Output classes (`File`, `FileReader`, `FileWriter`, `BufferedReader`) |
| `java.net` | Networking classes (`URL`, `HttpURLConnection`, `Socket`) |
| `java.sql` | Database connectivity (`Connection`, `Statement`, `ResultSet`) |
| `java.time` | Date and time API (`LocalDate`, `LocalTime`, `LocalDateTime`) |
| `java.text` | Formatting and parsing (`SimpleDateFormat`, `NumberFormat`) |
| `java.awt` | Abstract Window Toolkit (GUI components — older) |
| `javax.swing` | Swing GUI components (older GUI toolkit) |

---

## 8. Assignment Questions

### 🟢 Basic Level

**Q1.** Create a package called `com.learning.shapes` and define the following classes inside it:
- `Circle` with fields `radius` and methods `area()` and `perimeter()`
- `Rectangle` with fields `length` and `width` and methods `area()` and `perimeter()`

Write a separate `MainApp` class in a different package (`com.learning.app`) that imports and uses both classes.

**Q2.** Write a Java program that:
- Declares a package `com.learning.greetings`
- Contains a class `Greeting` with a method `sayHello(String name)` that prints "Hello, {name}!"
- Create another class in package `com.learning.app` that imports and uses `Greeting`

**Q3.** What is the difference between `import java.util.Scanner;` and `import java.util.*;`? When would you prefer one over the other?

---

### 🟡 Intermediate Level

**Q4.** Create a package `com.learning.library` with the following:
- A class `Book` with fields: `title`, `author`, `isbn`, `isBorrowed`
- A class `Library` that maintains a list of books and provides methods: `addBook()`, `borrowBook()`, `returnBook()`, `searchByTitle()`

Create a separate `MainApp` class that demonstrates the library system.

**Q5.** Write a program using **static import** to:
- Import `java.lang.Math.PI` as a constant `PI`
- Import `java.lang.Math.*` methods
- Calculate the area of a circle using `PI` and `Math.pow()`

**Q6.** Explain what happens if you declare two packages in the same Java file. What error does the compiler produce?

---

### 🔴 Advanced Level

**Q7.** Create a multi-package project for a **Student Management System**:

- **Package `com.learning.students.models`**:
  - `Student` class with fields: `id`, `name`, `grade`, `gpa`
  - `Grade` enum with values: `A`, `B`, `C`, `D`, `F`

- **Package `com.learning.students.services`**:
  - `StudentService` class with methods: `addStudent()`, `removeStudent()`, `getStudentById()`, `calculateAverageGPA()`

- **Package `com.learning.students.ui`**:
  - `StudentUI` class with a `main()` method that demonstrates the system

Write a `README.md` explaining the package structure and how the packages interact.

**Q8.** Create a package `com.learning.mathutils` with a class `MathUtils` containing static methods:
- `factorial(int n)`
- `fibonacci(int n)`
- `isPrime(int n)`
- `reverseNumber(int n)`

Use **static import** in a `MainApp` class to call these methods without the class name prefix.

**Q9.** (Critical Thinking) You have two classes with the same name `Date` — one in `java.sql` and one in `java.util`. If you need to use both in the same file, how would you handle this? Write a code example.

**Q10.** (Project) Build a **Banking System** with proper package organization:
- `com.learning.bank.models` — `Account`, `Customer`, `Transaction`
- `com.learning.bank.services` — `AccountService`, `TransactionService`
- `com.learning.bank.exceptions` — `InsufficientFundsException`, `InvalidAccountException`
- `com.learning.bank` — `Main` class

Demonstrate deposits, withdrawals, transfers, and error handling.

---

## 9. Quick Reference Cheat Sheet

```java
// ===== PACKAGE DECLARATION =====
package com.example.myapp;  // First line (after comments)

// ===== IMPORTS =====
import java.util.Scanner;          // Specific class
import java.util.*;                 // All classes (wildcard)
import static java.lang.Math.*;    // Static members

// ===== USING IMPORTED CLASSES =====
Scanner scanner = new Scanner(System.in);   // No package prefix needed
double result = Math.sqrt(25);              // java.lang auto-imported

// ===== DIRECTORY STRUCTURE =====
src/
└── com/
    └── example/
        └── myapp/
            └── MyClass.java
```

---

## 10. Common Mistakes to Avoid

1. ❌ Forgetting the `package` statement when required
2. ❌ Putting `package` after class definition (compiler error)
3. ❌ Using wildcard imports excessively (`import java.util.*;`)
4. ❌ Not matching directory structure to package name
5. ❌ Trying to declare multiple packages in one file
6. ❌ Forgetting that `java.lang` is auto-imported (unnecessary imports)
7. ❌ Overusing static imports (reduces readability)

---

## ✅ Learning Checklist

- [ ] I understand what a package is and why it's used
- [ ] I can declare a package in a Java file
- [ ] I can create the correct directory structure for a package
- [ ] I can import specific classes from a package
- [ ] I understand the difference between specific and wildcard imports
- [ ] I know that `java.lang` classes are auto-imported
- [ ] I can use static imports for methods and fields
- [ ] I can organize a multi-package project

---

*Next: Day 18 — Exception Handling*
