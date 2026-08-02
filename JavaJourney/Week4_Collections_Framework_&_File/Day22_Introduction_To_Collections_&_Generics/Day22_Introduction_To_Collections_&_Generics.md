# Day 22 — Introduction to Collections & Generics

## Quick Overview
- Collections store groups of objects (Lists, Sets, Maps).  
- Generics add compile-time type safety: `List<String>` prevents accidental mixing of types.

## Common Interfaces
- `List` (ordered, duplicates) — `ArrayList`, `LinkedList`  
- `Set` (unique elements) — `HashSet`, `TreeSet`  
- `Map` (key → value) — `HashMap`, `TreeMap`

## Streams Snapshot
- Create: `collection.stream()`  
- Intermediate: `filter`, `map`, `flatMap`, `sorted`  
- Terminal: `collect`, `forEach`, `reduce`, `count`

## Tiny Example
```java
List<String> names = List.of("Ana","Bob","Cara");
List<String> cNames = names.stream()
    .filter(s -> s.startsWith("C"))
    .collect(Collectors.toList());
```

## Mind Map
```mermaid
graph LR
  A[Day22: Collections & Generics]
  A --> B[List\n(ArrayList,LinkedList)]
  A --> C[Set\n(HashSet,TreeSet)]
  A --> D[Map\n(HashMap,TreeMap)]
  A --> E[Generics\nList<T>, Map<K,V>]
  A --> F[Streams\nfilter,map,collect]
```

## Exercises
1. Create a `List<Integer>` and use streams to produce a `List<String>` of even numbers.  
2. Count unique words from a list of sentences using `flatMap` and `Collectors.toSet()`.
