# String Manipulation in Java

## 1. String Basics

```java
// s1 is a string literal. The JVM stores literals in the String Pool (a shared area).
// If another literal "Hello" appears elsewhere, the same pooled object is reused.
String s1 = "Hello";              // String literal (stored in String pool)

// s2 explicitly creates a new String object on the heap, separate from the pool.
// Even though its content equals "Hello", s2 != s1 when compared with ==.
String s2 = new String("Hello");  // new object (heap memory)
```

### Type Casting and String Conversion
Type casting is mainly for primitive data types, not for strings.

```java
int x = 10;
double y = x;          // automatic widening
int z = (int) 9.99;    // manual narrowing
```

You cannot do something like `(int) "10"`. For strings, use parsing methods instead:

```java
int n = Integer.parseInt("10");
double d = Double.parseDouble("3.14");
String s = String.valueOf(42);
```

## 2. Important String Methods

| Method | Description | Example |
|---|---|---|
| `length()` | Returns number of characters | `"Hi".length()` → `2` |
| `charAt(i)` | Character at index `i` | `"Hi".charAt(1)` → `'i'` |
| `substring(i, j)` | Substring from `i` to `j-1` | `"Hello".substring(1, 4)` → `"ell"` |
| `substring(i)` | Substring from `i` to end | `"Hello".substring(2)` → `"llo"` |
| `equals(s)` | Compares content | `"Hi".equals("hi")` → `false` |
| `equalsIgnoreCase(s)` | Case-insensitive compare | `"Hi".equalsIgnoreCase("hi")` → `true` |
| `toLowerCase()` | Converts to lowercase | `"Hello".toLowerCase()` → `"hello"` |
| `toUpperCase()` | Converts to uppercase | `"Hello".toUpperCase()` → `"HELLO"` |
| `contains(s)` | Checks if substring exists | `"Hello".contains("ell")` → `true` |
| `startsWith(s)` | Checks prefix | `"Hello".startsWith("He")` → `true` |
| `endsWith(s)` | Checks suffix | `"Hello".endsWith("lo")` → `true` |
| `indexOf(s)` | First index of substring | `"Hello".indexOf("l")` → `2` |
| `replace(a, b)` | Replaces all `a` with `b` | `"Hello".replace("l", "x")` → `"Hexxo"` |
| `trim()` | Removes leading/trailing spaces | `" Hi ".trim()` → `"Hi"` |
| `split(regex)` | Splits into array by delimiter | `"a,b,c".split(",")` → `["a","b","c"]` |
| `toCharArray()` | Converts to `char[]` | `"Hi".toCharArray()` → `['H','i']` |
| `isEmpty()` | Checks if length is 0 | `"".isEmpty()` → `true` |
| `isBlank()` | Checks if blank (Java 11+) | `"  ".isBlank()` → `true` |

## 3. String Immutability

Strings are **immutable** — once created, they cannot be changed.

```java
String s = "Hello";
s.toUpperCase();
System.out.println(s); // "Hello" — original unchanged!
```

Every method that seems to modify a string actually **returns a new string**:

```java
String s = "Hello";
String t = s.toUpperCase(); // Must capture the return value
System.out.println(t);       // "HELLO"
```

**Why immutable?**
- Thread-safe (can be shared across threads)
- Enables String pool (memory optimization)
- Secure (no tampering, used in class loading)

## 4. String Comparison — Don't Use `==`

```java
String a = "Hello";
String b = "Hello";
String c = new String("Hello");

System.out.println(a == b);      // true (same literal, String pool)
System.out.println(a == c);      // false (different objects)
System.out.println(a.equals(c)); // true (same content)
```

**Rule:** Always use `.equals()` to compare string **content**.

## 5. StringBuilder — Mutable Strings

`String` creates a new object every time you modify it. `StringBuilder` is **mutable** — it modifies in-place, which is faster for heavy manipulation.

```java
StringBuilder sb = new StringBuilder("Hello");

sb.append(" World");       // Adds to end
sb.insert(5, " Java");     // Inserts at index 5
sb.replace(0, 5, "Hi");    // Replaces range
sb.delete(2, 4);           // Deletes range
sb.reverse();              // Reverses
sb.toString();             // Convert back to String
```

**When to use StringBuilder?**
- Concatenating many strings in a loop
- Frequent insertions/deletions

```java
// Inefficient (creates many String objects)
String s = "";
for (int i = 0; i < 1000; i++) {
    s += i;  // New String each iteration!
}

// Efficient (modifies in place)
StringBuilder sb = new StringBuilder();
for (int i = 0; i < 1000; i++) {
    sb.append(i);
}
String s = sb.toString();
```

## 6. String Concatenation

```java
String s = "Hello" + " " + "World";  // + operator (creates new strings)
String t = "Hello".concat(" World");  // concat() method
```

For simple cases, `+` is fine. In loops, **always use `StringBuilder`** (see §5).

## 7. String Formatting

String formatting lets you build a string using placeholders, then fill them with values.

```java
int age = 25;
double score = 92.5;

// String.format returns a formatted string.
String msg = String.format("Age: %d, Score: %.1f", age, score); // "Age: 25, Score: 92.5"

// System.out.printf prints the formatted string directly to output.
System.out.printf("Age: %d, Score: %.1f%n", age, score);       // Same, prints directly

// Java 15+ instance method that formats the string itself.
String s = "Hello %s!".formatted("World");                      // "Hello World!"
```

### How They Work

| Method | Type | How It Works |
|---|---|---|
| `String.format()` | Static method on `String` class | Takes a format string + arguments, **returns** a new formatted `String`. Use when you need the result as a variable. |
| `System.out.printf()` | Instance method on `PrintStream` | Takes a format string + arguments, **prints directly** to console (or wherever `System.out` points). Does not return a string. |
| `.formatted()` | Instance method on `String` (Java 15+) | Called **on the format string itself**, takes arguments, **returns** a new formatted `String`. Cleaner syntax than `String.format()`. |

**Key difference:** `format()` and `.formatted()` **return** a string; `printf()` **prints** to output.

| Specifier | Meaning | Example |
|---|---|---|
| `%s` | String | `"Hi %s".formatted("Tom")` → `"Hi Tom"` |
| `%d` | Integer | `"Age: %d".formatted(20)` → `"Age: 20"` |
| `%f` | Float/double | `"%.2f".formatted(3.14159)` → `"3.14"` |
| `%c` | Character | `"%c".formatted('A')` → `"A"` |
| `%b` | Boolean | `"%b".formatted(true)` → `"true"` |
| `%n` | Newline | `"A%nB"` → `"A\nB"` |
| `%05d` | Zero-padded int | `"%05d".formatted(7)` → `"00007"` |
| `%5s` | Width 5, right-aligned | `"%5s".formatted("Hi")` → `"  Hi"` |

## 8. Other Useful String Methods

| Method | Description | Example |
|---|---|---|
| `concat(s)` | Appends string | `"A".concat("B")` → `"AB"` |
| `join(delim, parts...)` | Joins multiple strings | `String.join(",", "a","b","c")` → `"a,b,c"` |
| `repeat(n)` | Repeats string (Java 11+) | `"Ha".repeat(3)` → `"HaHaHa"` |
| `valueOf(x)` | Converts primitive to String | `String.valueOf(42)` → `"42"` |
| `compareTo(s)` | Lexicographic comparison | `"a".compareTo("b")` → negative |
| `compareToIgnoreCase(s)` | Case-insensitive compare | `"A".compareToIgnoreCase("a")` → `0` |
| `matches(regex)` | Checks if matches regex | `"123".matches("\\d+")` → `true` |
| `strip()` | Unicode-aware trim (Java 11+) | `" Hi ".strip()` → `"Hi"` |
| `stripLeading()` | Strips leading whitespace | `" Hi".stripLeading()` → `"Hi"` |
| `stripTrailing()` | Strips trailing whitespace | `"Hi ".stripTrailing()` → `"Hi"` |

`strip()` is preferred over `trim()` for modern Java — it handles Unicode whitespace correctly.

## 9. StringBuffer vs StringBuilder

| Feature | StringBuilder | StringBuffer |
|---|---|---|
| Thread-safe | No (faster) | Yes (synchronized) |
| Speed | Fast | Slower |
| Use case | Single thread | Multiple threads |

---

# Assignment Questions

### Easy
1. Write a method `countVowels(String s)` that returns the number of vowels (`a, e, i, o, u`) in a string.

2. Write a method `reverseString(String s)` that returns the reversed version of a string.

3. Write a method `isPalindrome(String s)` that checks if a string reads the same forwards and backwards (e.g., `"racecar"`, `"madam"`).

### Medium
4. Write a method `countWords(String s)` that returns the number of words in a sentence (words are separated by spaces).

5. Write a method `removeDuplicates(String s)` that returns a new string with consecutive duplicate characters removed. Example: `"aabbcc"` → `"abc"`.

6. Write a method `capitalizeWords(String s)` that capitalizes the first letter of each word. Example: `"hello world"` → `"Hello World"`.

7. Write a method `mostFrequentChar(String s)` that returns the character that appears most frequently in the string.

### Hard
8. Write a method `compressString(String s)` that performs basic run-length encoding. Example: `"aaabbc"` → `"a3b2c1"`. If the compressed string is longer than the original, return the original.

9. Write a method `areAnagrams(String a, String b)` that checks if two strings are anagrams (contain the same characters in any order). Example: `"listen"` and `"silent"` → `true`.

10. Write a method `longestSubstringWithoutRepeating(String s)` that returns the length of the longest substring without repeating characters. Example: `"abcabcbb"` → `3` (substring `"abc"`).

### Bonus (Use StringBuilder)
11. Write a method `mergeAlternately(String a, String b)` that merges two strings alternately. Example: `"abc"` and `"pqr"` → `"apbqcr"`. If one is longer, append the remaining characters. **Must use StringBuilder.**

12. Write a method `expandString(String s)` where a number after a character means repeat it that many times. Example: `"a3b2c"` → `"aaabbc"`. **Must use StringBuilder.**
