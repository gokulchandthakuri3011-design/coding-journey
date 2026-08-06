# Day 22 — Collections & Generics (Beginner)

## Goal
Give a simple, beginner-friendly view of what Collections and Generics are, show the common syntax, and list the usual methods so you can start using them.

## What is a Collection?
- A Collection is an object that groups multiple elements into a single unit (provided by `java.util`).
- Collections grow/shrink dynamically and include helpful methods like `add`, `remove`, `contains`, and `size`.

## Collections vs arrays (quick)
- Arrays: fixed length, simple, good for primitives or fixed buffers (e.g., `int[]`, `String[]`).
- Collections: dynamic, richer API, type-safe with Generics (e.g., `List`, `Set`, `Map`).

## Common interfaces & simple syntax
- `List<E>` — ordered, allows duplicates. Example: `List<String> list = new ArrayList<>();`
- `Set<E>` — no duplicates. Example: `Set<Integer> set = new HashSet<>();`
- `Map<K,V>` — key → value pairs. Example: `Map<String,Integer> map = new HashMap<>();`

Common methods you'll use:
- `add(e)`, `remove(e)`, `contains(e)`, `size()` — for `Collection`/`List`/`Set`.
- `get(index)` — for `List` only.
- `put(key,value)`, `get(key)`, `containsKey(key)`, `keySet()` — for `Map`.

## What are Generics?
- Generics let you declare the type a collection holds: `List<String>` means the list holds `String` objects.
- Benefits: compile-time checks and no casts when retrieving items.

Simple generic examples:
```java
List<String> names = new ArrayList<>();
names.add("Ana");
String first = names.get(0);

Map<String,Integer> counts = new HashMap<>();
counts.put("apple", 2);
int c = counts.get("apple");
```

Generic class (one-line):
```java
class Box<T> { T value; Box(T v){value=v;} T get(){return value;} }
```

## Very short note on wildcards
- `List<? extends T>` — read-only as `T` (use when you only need to read/iterate).
- `List<? super T>` — you can add `T` instances (use when you need to add elements).

## Tiny beginner exercises
1. Create `List<String> colors`, add three names, print the first item.
2. Create `Set<Integer> ids`, add numbers with duplicates, print `size()` (duplicates removed).
3. Create `Map<String,String> phonebook`, add two entries, and retrieve a value by key.

If you'd like, I can now:
- Add simple runnable `.java` example files under an `examples/` folder.
- Or further shorten any section and add step-by-step screenshots.

---
Edited for beginner clarity.
