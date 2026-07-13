# Day 20: Exception Handling Advanced

**Time: ~60 min** (15 read → 35 practice → 10 review)

---

## 🧠 Mind Map

```
                        java.lang.Throwable
                              │
              ┌───────────────┴───────────────┐
         java.lang.Error              java.lang.Exception
      (JVM problems, don't catch)            │
                                      ┌──────┴──────┐
                                   CHECKED        UNCHECKED
                                 (compile-time)   (runtime)
                                      │               │
                               Must handle       Optional to handle
                               or declare        (programming bugs)
                                      │               │
                               IOException     NullPointerException
                               SQLException    ArithmeticException
                               ParseException  NumberFormatException
                                              IllegalArgumentException
```

```
    KEYWORDS              TECHNIQUES
    ────────              ──────────
    throw  → creates &    try-with-resources → auto-cleanup
             throws an          try (Resource r = ...) { }
             exception          Resource must implement AutoCloseable

    throws → declares in   Multi-catch → same handler for
             method signature  catch (A | B e) { }
             what CAN go wrong
```

---

## 1. Checked vs Unchecked — "Compile-time warning vs runtime crash"

**Checked** = The compiler **forces** you to handle it (like a file might not exist, network might be down — things outside your control).

```java
// This WON'T COMPILE without handling:
FileReader f = new FileReader("data.txt");  // compiler ERROR

// Option A: handle it
try {
    FileReader f = new FileReader("data.txt");
} catch (FileNotFoundException e) {
    System.out.println("File missing!");
}

// Option B: declare it (push responsibility to caller)
public void loadConfig() throws FileNotFoundException {
    FileReader f = new FileReader("data.txt");
}
```

**Unchecked** = Bugs in your code (null pointer, divide by zero). Compiler won't warn you — you just fix the bug.

| | Checked | Unchecked |
|--|---------|-----------|
| **When** | Compile-time | Runtime |
| **Rule** | Must handle or declare with `throws` | Compiler won't force you |
| **Cause** | External (file missing, network down) | Bugs (null, bad logic) |
| **Examples** | `IOException`, `FileNotFoundException`, `SQLException` | `NullPointerException`, `ArithmeticException`, `ArrayIndexOutOfBoundsException` |

---

## 2. `throw` vs `throws` — "Creating an exception vs declaring one can happen"

```
throw   → INSIDE a method → creates & throws an exception NOW
throws  → IN METHOD SIGNATURE → declares it CAN happen in future
```

```java
// "throws" = warning label on the method
public void withdraw(double amount) throws InsufficientFundsException {
    if (amount > balance) {
        // "throw" = actually throwing the exception right now
        throw new InsufficientFundsException(balance - amount);
    }
    balance -= amount;
}
```

**Exception Propagation** — exceptions bubble UP the call stack until caught:

```
main() → withdraw() → checkBalance()
                           │
                    InsufficientFundsException thrown here
                           │
                    checkBalance() catches?  NO → goes up
                           │
                    withdraw() catches?  NO → goes up
                           │
                    main() catches?  YES → handled
```

---

## 3. Custom Exceptions — "Your own meaningful error types"

Instead of generic `Exception`, create exceptions that describe **exactly** what went wrong:

```java
// Checked — callers MUST handle it
class InsufficientFundsException extends Exception {
    private double deficit;

    public InsufficientFundsException(double deficit) {
        super("Short by: $" + deficit);  // meaningful message
        this.deficit = deficit;
    }

    public double getDeficit() { return deficit; }
}

// Usage
public void withdraw(double amount) throws InsufficientFundsException {
    if (amount > balance)
        throw new InsufficientFundsException(amount - balance);
    balance -= amount;
}
```

**When to extend `Exception` vs `RuntimeException`:**

| | extends `Exception` | extends `RuntimeException` |
|--|---|---|
| **Rule** | Caller **must** handle or declare | Optional — it's a bug |
| **Cause** | Payment failed, file missing, invalid config | Null passed, bad argument, logic error |
| **Meaning** | "Something external went wrong" | "The programmer made a mistake" |

---

## 4. Exception Chaining — "Wrapping low-level errors in meaningful ones"

```java
public void connectToService(String url) throws ConnectionException {
    try {
        URL serviceUrl = new URL(url);
    } catch (MalformedURLException e) {
        // Wrap technical error in YOUR meaningful error
        throw new ConnectionException("Failed to connect: " + url, e);
    }
}

// Caller gets a clear message AND can access the original cause:
try {
    connectToService("htp://bad-url");
} catch (ConnectionException e) {
    System.out.println(e.getMessage());           // "Failed to connect: htp://bad-url"
    System.out.println(e.getCause().getMessage()); // "no protocol: htp"
}
```

**Why chain?** Your code gets a clean, meaningful error. The original technical error is still accessible via `getCause()` for debugging.

---

## 5. Try-with-Resources — "Auto-cleanup"

Resources (files, DB connections, network sockets) **must be closed**. Old way was verbose and error-prone. New way is clean:

```java
// OLD WAY — messy, easy to forget close()
BufferedReader reader = null;
try {
    reader = new BufferedReader(new FileReader("data.txt"));
    // use reader
} finally {
    if (reader != null) {
        try { reader.close(); } catch (IOException ignored) {}
    }
}

// NEW WAY — auto-closes, even if exception occurs
try (BufferedReader reader = new BufferedReader(new FileReader("data.txt"))) {
    String line = reader.readLine();
    System.out.println(line);
}
// reader.close() called AUTOMATICALLY
```

**Multiple resources** close in **reverse** declaration order:
```java
try (FileWriter w = new FileWriter("out.txt");
     PrintWriter out = new PrintWriter(w)) {
    out.println("hello");
}
// closes: out → w
```

---

## 6. Multi-Catch — "One handler for multiple exception types"

```java
try {
    int val = Integer.parseInt(input);
    int elem = arr[index];
} catch (NumberFormatException | ArrayIndexOutOfBoundsException e) {
    // handles BOTH with same logic
    System.out.println("Input error: " + e.getMessage());
}
```

---

## Quick Recap — When to Use What

| Concept | Use When |
|---------|----------|
| **Checked exception** | External failure you can't prevent (file, network, DB) |
| **Unchecked exception** | Programming bug (null, bad logic) |
| **`throws`** | You don't want to handle it — let the caller decide |
| **`throw`** | You detect a problem and want to signal it immediately |
| **Custom exception** | Generic exceptions aren't descriptive enough |
| **Exception chaining** | Wrapping technical errors in meaningful business errors |
| **try-with-resources** | Working with files, connections, streams (anything `AutoCloseable`) |
| **Multi-catch** | Multiple exception types need the same handling logic |

---

## 📝 Assignments (Pick 3-4, ~35 min)

### Easy (pick 1)

**1. Age Validator**
- Create `InvalidAgeException extends Exception`
- Method `validateAge(int age)` throws it if age < 18 or > 120
- Test with valid and invalid inputs

**2. File Reader with throws**
- `readFirstLine(String path) throws FileNotFoundException`
- Call from main with try-catch; test existing and missing files

### Medium (pick 2)

**3. Bank Account**
- Create `OverdraftException extends Exception` with `getAmount()` method
- `withdraw(amount)` throws it when balance insufficient
- Main catches it and displays shortfall

**4. Exception Chaining**
- `connectToService()` tries to parse invalid URL
- Catch `MalformedURLException`, wrap in custom `ConnectionException`
- Main prints both message and cause via `getCause()`

### Hard (pick 1)

**5. Validation Framework**
- `EmptyFieldException`, `InvalidFormatException`, `OutOfRangeException`
- `UserValidator` with `validateName()`, `validateEmail()`, `validateAge()`
- Each throws its specific exception; main handles all three separately

**6. AutoCloseable Practice**
- Create `FileProcessor implements AutoCloseable` (opens file in constructor, logs on close)
- Use try-with-resources in main
- Wrap errors in custom `ProcessingException`
- Verify `close()` runs even when exception occurs

---

## ⏱️ Time Plan

| Activity | Time |
|----------|------|
| Read this guide | 15 min |
| Code 3-4 assignments | 35 min |
| Review & compare with examples | 10 min |

**Focus today:** `throw`/`throws` usage, custom exceptions, try-with-resources!
