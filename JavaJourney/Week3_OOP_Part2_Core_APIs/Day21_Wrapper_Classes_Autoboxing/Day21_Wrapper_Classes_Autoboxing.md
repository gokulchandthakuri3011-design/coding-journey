# Day 21: Wrapper Classes & Autoboxing

**Time: ~60 min** (15 read → 35 practice → 10 review)

---

## 🧠 Mind Map

```
                        PRIMITIVE TYPES              WRAPPER CLASSES
                        ──────────────              ───────────────
                        int          ←──────────→    Integer
                        double       ←──────────→    Double
                        boolean      ←──────────→    Boolean
                        char         ←──────────→    Character
                        long         ←──────────→    Long
                        float        ←──────────→    Float
                        byte         ←──────────→    Byte
                        short        ←──────────→    Short

                              AUTOBOXING / UNBOXING
                              ──────────────────────
                        int x = 10;
                        Integer obj = x;    ← autoboxing (auto wrap)
                        int y = obj;        ← unboxing (auto unwrap)
```

```
    WHY WRAPPER CLASSES?               KEY FEATURES
    ────────────────────               ────────────
    1. Collections need Objects       Integer.MAX_VALUE → 2147483647
       (ArrayList<Integer>, not       Integer.MIN_VALUE → -2147483648
        ArrayList<int>)               Double.isNaN(val) → true/false

    2. Can be NULL                    Integer.parseInt("123") → 123
       (primitives can't)             Integer.toHexString(255) → "ff"

    3. Utility methods                Double.compare(d1, d2) → int
       (parsing, conversion, etc)     Boolean.TRUE / Boolean.FALSE
```

---

## 1. What Are Wrapper Classes? — "Primitives in Object clothing"

Java has 8 primitive types (`int`, `double`, etc.) that are **not objects**. But sometimes you need objects — like when using Collections, generics, or `null`.

**Wrapper classes** are objects that **wrap** a primitive value inside an object.

```java
// Primitive — simple, fast, can't be null
int num = 42;

// Wrapper — object, can be null, has utility methods
Integer obj = 42;  // autoboxing (auto-wrapping)
```

### Primitive to Wrapper Mapping

| Primitive | Wrapper Class | Size |
|-----------|---------------|------|
| `byte` | `Byte` | 1 byte |
| `short` | `Short` | 2 bytes |
| `int` | `Integer` | 4 bytes |
| `long` | `Long` | 8 bytes |
| `float` | `Float` | 4 bytes |
| `double` | `Double` | 8 bytes |
| `char` | `Character` | 2 bytes |
| `boolean` | `Boolean` | ~1 byte |

> **Note:** `Integer`, `Character`, `Boolean`, `Long`, `Float`, `Double`, `Byte`, `Short` — all are objects in `java.lang` package (no import needed).

---

## 2. Autoboxing & Unboxing — "Automatic wrapping and unwrapping"

**Autoboxing** = primitive → wrapper object (automatic)
**Unboxing** = wrapper object → primitive (automatic)

```java
// AUTOBOXING — primitive to wrapper (automatic)
Integer a = 100;          // int 100 → Integer(100)
Double b = 3.14;          // double 3.14 → Double(3.14)
Boolean c = true;         // boolean true → Boolean(true)
Character d = 'A';        // char 'A' → Character('A')

// UNBOXING — wrapper to primitive (automatic)
int x = a;                // Integer(100) → int 100
double y = b;             // Double(3.14) → double 3.14
boolean z = c;            // Boolean(true) → boolean true
char ch = d;              // Character('A') → char 'A'
```

### Autoboxing in Action

```java
// Works with arithmetic — Java auto-unboxes, computes, auto-boxes back
Integer a = 10;
Integer b = 20;
Integer sum = a + b;  // a unboxes to int, b unboxes to int, sum = 30, then auto-boxed to Integer

// Works with comparisons
Integer x = 5;
Integer y = 10;
if (x < y) {  // auto-unbox to compare
    System.out.println("x is smaller");
}

// Works with method calls
ArrayList<Integer> list = new ArrayList<>(); // <> is Diamond operator that tells java to figure out the type from lift side of '=' and i.e. here Integer(Obj) that only takes int
list.add(42);    // autoboxing: int 42 → Integer(42)
int val = list.get(0);  // unboxing: Integer(42) → int 42
```

---

## 3. Manual Conversion Methods — "Explicit wrapping and unwrapping"

```java
// Primitive → Wrapper (manual)
Integer a = Integer.valueOf(100);      // recommended
Integer b = new Integer(100);          // deprecated, avoid

// Wrapper → Primitive (manual)
int x = a.intValue();                  // works for all wrappers
double d = Double.valueOf(3.14).doubleValue();
```

### String Conversion

```java
// String → Primitive
int i = Integer.parseInt("123");
double d = Double.parseDouble("3.14");
boolean b = Boolean.parseBoolean("true");

// String → Wrapper
Integer i = Integer.valueOf("123");
Double d = Double.valueOf("3.14");

// Primitive → String
String s1 = String.valueOf(42);        // "42"
String s2 = Integer.toString(42);      // "42"
String s3 = 42 + "";                   // "42" (concatenation trick)
```

---

## 4. Important Utility Methods — "What wrappers give you for free"

### Integer Methods

```java
Integer num = 42;

// Useful constants
System.out.println(Integer.MAX_VALUE);    // 2147483647 
System.out.println(Integer.MIN_VALUE);    // -2147483648
// since int is 32-bit signed -> 32 bits = 2^32 total values and signed means half '-' ve & half '+' ve including 0 so range = -2^31 to 2^31 -1 ( 1 bit = sign , 31 bits = magnitude)

// String conversion
System.out.println(Integer.toHexString(255));  // "ff"
System.out.println(Integer.toBinaryString(10)); // "1010"
System.out.println(Integer.parseInt("123"));    // 123

// Comparison
int result = Integer.compare(10, 20);  // -1 (negative = first < second)
// Integer.compare(a, b) returns a negative value when a < b, zero when a == b, or a positive value when a > b.

// Bit operations
System.out.println(Integer.bitCount(7));      // 3 (number of 1-bits)
System.out.println(Integer.reverseBytes(1));   // flips bytes
```

### Double Methods

```java
Double d = 3.14;

System.out.println(Double.MAX_VALUE);    // 1.7976931348623157E308
System.out.println(Double.MIN_VALUE);    // 4.9E-324 (smallest positive)
System.out.println(Double.isNaN(d / 0)); // false (Infinity, not NaN) Nan -> undefined in Math(0/0)
System.out.println(Double.isInfinite(Double.POSITIVE_INFINITY)); // true Here POSITIVE_INFINITY -> ∞

double parsed = Double.parseDouble("3.14");
```

### Boolean Methods

```java
Boolean b = true;

System.out.println(b booleanValue());  // true (primitive)
System.out.println(Boolean.parseBoolean("TRUE"));  // true (case-insensitive)
System.out.println(Boolean.parseBoolean("yes"));   // false (only "true" returns true)
```

### Character Methods

```java
Character ch = 'A';

System.out.println(Character.isLetter(ch));      // true
System.out.println(Character.isDigit(ch));        // false
System.out.println(Character.isUpperCase(ch));    // true
System.out.println(Character.toLowerCase(ch));    // 'a'
System.out.println(Character.toUpperCase('b'));   // 'B'
System.out.println(Character.isLetterOrDigit('3')); // true
```

---

## 5. The Integer Cache — "Why Integer a == b can be tricky"

Java **caches** `Integer` objects from **-128 to 127**. This means two `Integer` variables with the same value in this range point to the **same object**.

```java
Integer a = 127;
Integer b = 127;
System.out.println(a == b);  // true (same cached object)

Integer c = 128;
Integer d = 128;
System.out.println(c == d);  // false (different objects!)

// ALWAYS use .equals() for Wrapper comparison
System.out.println(c.equals(d));  // true (same value)
```

**Why?** Performance — small integers are used frequently, so caching saves memory.

**Rule:** Never use `==` to compare wrapper objects. Always use `.equals()`.

```
    COMPARISON CHEAT SHEET
    ───────────────────────
    Primitive:   int a = 5;  int b = 5;   a == b  → true  ✅
    Wrapper:     Integer a = 5; Integer b = 5;
                 a == b       → depends on range ⚠️
                 a.equals(b)  → always correct ✅
```

---

## 6. Null Safety — "Wrapper's superpower and gotcha"

Wrappers can be `null`, primitives cannot. This is useful for representing "unknown" values but dangerous with autoboxing.

```java
// Primitives — can't be null
int x = null;  // COMPILE ERROR

// Wrappers — can be null
Integer y = null;

// DANGER: NullPointerException from unboxing
Integer a = null;
int b = a;  // RUNTIME ERROR! NullPointerException

// SAFE: Check before unboxing
Integer c = null;
if (c != null) {
    int d = c;  // safe
}
```

### Use case: Representing missing data

```java
// Using primitives — can't distinguish "age not set" from "age is 0"
int age = 0;

// Using wrappers — null means "not set"
Integer age = null;  // not set
Integer age = 25;    // set to 25
```

---

## 7. Autoboxing Pitfalls — "Watch out for these traps"

### Pitfall 1: Unexpected NullPointerException

```java
Boolean flag = null;
if (flag) {  // NullPointerException! Auto-unboxing null
    System.out.println("true");
}
```

### Pitfall 2: Performance in loops

```java
// BAD — autoboxing in tight loop (creates many objects)
Long sum = 0L;
for (long i = 0; i < 1000000; i++) {
    sum += i;  // unbox, add, auto-box each iteration!
}

// GOOD — use primitive
long sum = 0L;
for (long i = 0; i < 1000000; i++) {
    sum += i;  // no boxing overhead
}
```

### Pitfall 3: Comparing with ==

```java
Integer a = 200;
Integer b = 200;
System.out.println(a == b);       // false! (outside cache range)
System.out.println(a.equals(b));  // true
```

### Pitfall 4: Modifying inside loops with autoboxing

```java
Integer x = 0;
for (int i = 0; i < 10; i++) {
    x++;  // unbox → increment → auto-box (new object each time!)
}
// Works but inefficient — use int, then wrap at the end
```

---

## Quick Recap — When to Use What

| Concept | Use When |
|---------|----------|
| **Primitive** | Performance-critical code, simple calculations, loop counters |
| **Wrapper** | Collections (`ArrayList<Integer>`), generics, `null` values, API boundaries |
| **Autoboxing** | Passing primitive to method/collection expecting wrapper |
| **Unboxing** | Getting value from wrapper to use in calculations |
| **`.equals()`** | Always compare wrapper objects with `.equals()`, never `==` |
| **`Integer.parseInt()`** | Converting String to int |
| **`String.valueOf()`** | Converting primitive to String |
| **Cache (-128 to 127)** | Be aware — `==` works for small values but don't rely on it |

---

## 📝 Assignments (Pick 3-4, ~35 min)

### Easy (pick 1)

**1. Wrapper Conversion Practice**
- Create variables: `int`, `double`, `boolean`, `char`
- Convert each to its wrapper class using autoboxing
- Convert each back to primitive using unboxing
- Print all values before and after conversion

**2. String to Number Converter**
- Take 3 strings from user: `"10"`, `"3.14"`, `"true"`
- Convert to `int`, `double`, `boolean` respectively using parse methods
- Print each converted value with its type

### Medium (pick 2)

**3. Integer Math with Wrappers**
- Create `ArrayList<Integer>` and add numbers: 10, 20, 30, 40, 50
- Use a loop to calculate the sum (watch for autoboxing!)
- Find the max and min using `Integer.compare()`
- Print sum, max, min

**4. Temperature Converter**
- Method `Double celsiusToFahrenheit(Double celsius)` — returns `celsius * 9/5 + 32`
- Method `Double fahrenheitToCelsius(Double fahrenheit)` — returns `(fahrenheit - 32) * 5/9`
- Test with wrapper `Double` values (including `null` — handle gracefully!)
- Use `Double.isNaN()` to validate results

**5. Character Classifier**
- Method `String classifyCharacter(Character ch)` — returns:
  - "Uppercase letter" if `Character.isUpperCase(ch)`
  - "Lowercase letter" if `Character.isLowerCase(ch)`
  - "Digit" if `Character.isDigit(ch)`
  - "Special character" otherwise
- Test with various `Character` wrapper values

### Hard (pick 1)

**6. Generic Stats Calculator**
- Method `double calculateAverage(ArrayList<Double> numbers)` — handles null elements gracefully
- Method `Double findMax(ArrayList<Double> numbers)` — returns null if list is empty
- Method `Double findMin(ArrayList<Double> numbers)` — returns null if list is empty
- Method `int countNulls(ArrayList<Double> numbers)` — counts null elements
- Test with list containing: `10.5, null, 20.0, null, 30.5, 15.0`

**7. Integer Cache Investigation**
- Create `Integer a = 127; Integer b = 127;` — print `a == b`
- Create `Integer c = 128; Integer d = 128;` — print `c == d`
- Create `Integer e = Integer.valueOf(200); Integer f = Integer.valueOf(200);` — print `e == f`
- Explain why results differ (write findings as comments)
- Create a method `boolean compareIntegers(Integer x, Integer y)` that uses `.equals()` and always returns correct result

**8. Wrapper Utility Class**
- Create a class `NumberUtils` with static methods:
  - `Integer safeParseInt(String s, Integer defaultValue)` — returns `defaultValue` if parsing fails
  - `Double safeParseDouble(String s, Double defaultValue)` — returns `defaultValue` if parsing fails
  - `Boolean safeParseBoolean(String s, Boolean defaultValue)` — returns `defaultValue` if parsing fails
  - `String formatWithCommas(Integer num)` — formats `1234567` as `"1,234,567"` using `String.format("%,d", num)`
- Test all methods with valid and invalid inputs

---

## ⏱️ Time Plan

| Activity | Time |
|----------|------|
| Read this guide | 15 min |
| Code 3-4 assignments | 35 min |
| Review & compare with examples | 10 min |

**Focus today:** Autoboxing/unboxing mechanics, `.equals()` vs `==`, null safety!

---

## 🔗 Connection to Next Day (Day 22)
On **Day 22: Introduction to Collections & Generics**, you will learn:
- What the Collections Framework is
- Using `ArrayList` with wrapper classes (this is why wrappers matter!)
- Basic Generics (`<T>`) for type safety
