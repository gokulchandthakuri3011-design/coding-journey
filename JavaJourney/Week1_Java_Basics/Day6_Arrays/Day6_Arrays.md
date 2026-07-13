# Day 6: Arrays

## What are Arrays?

An **array** is a collection of elements of the same data type stored in contiguous memory locations. Arrays allow you to store multiple values in a single variable and access them using an index.

### Key Characteristics:
- **Fixed size**: Once created, the size cannot be changed
- **Index-based**: Elements are accessed using indices (0-based indexing)
- **Same data type**: All elements must be of the same type
- **Reference type**: Arrays are objects in Java

---

## Array Declaration and Initialization

### Method 1: Declare and Initialize Separately
```java
int[] numbers;                      // Declaration only
numbers = new int[5];               // Initialize with size 5
```

### Method 2: Declare and Initialize Together
```java
int[] numbers = new int[5];         // Array of size 5
String[] names = new String[3];     // Array of 3 strings
double[] prices = new double[10];   // Array of 10 doubles
```

### Method 3: Initialize with Values
```java
int[] numbers = {10, 20, 30, 40, 50};
String[] fruits = {"Apple", "Banana", "Orange"};
double[] temperatures = {98.6, 99.1, 98.4};
```

---

## Accessing Array Elements

Arrays use **zero-based indexing**:

```java
int[] scores = {85, 90, 78, 92, 88};

System.out.println(scores[0]);      // Output: 85
System.out.println(scores[2]);      // Output: 78
System.out.println(scores[4]);      // Output: 88

scores[1] = 95;                     // Change element at index 1
```

---

## Array Properties

```java
int[] numbers = {10, 20, 30, 40, 50};

System.out.println(numbers.length);  // Output: 5 (length property)
```

---

## Iterating Through Arrays

### Using for Loop
```java
int[] numbers = {10, 20, 30, 40, 50};

for (int i = 0; i < numbers.length; i++) {
    System.out.println(numbers[i]);
}
```

### Using Enhanced for Loop (for-each)
```java
int[] numbers = {10, 20, 30, 40, 50};

for (int num : numbers) {   // Like (for num in numbers) where :- in, and num- gets each element at a time
    System.out.println(num);
}
```

---

## Common Array Operations

### Finding the Sum
```java
int[] numbers = {10, 20, 30, 40, 50};
int sum = 0;

for (int num : numbers) {
    sum += num;
}

System.out.println("Sum: " + sum);  // Output: Sum: 150
```

### Finding the Average
```java
int[] numbers = {10, 20, 30, 40, 50};
double average = 0;

for (int num : numbers) {
    average += num;
}

average = average / numbers.length;
System.out.println("Average: " + average);  // Output: Average: 30.0
```

### Finding Maximum and Minimum
```java
int[] numbers = {10, 50, 30, 80, 20};
int max = numbers[0];
int min = numbers[0];

for (int num : numbers) {
    if (num > max) max = num;
    if (num < min) min = num;
}

System.out.println("Max: " + max);  // Output: Max: 80
System.out.println("Min: " + min);  // Output: Min: 10
```

---

## Multi-Dimensional Arrays

### 2D Array
```java
// Declaration and initialization
int[][] matrix = new int[3][3];

// Initialize with values
int[][] matrix = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};

// Access elements
System.out.println(matrix[0][1]);  // Output: 2
System.out.println(matrix[2][2]);  // Output: 9

// Iterate through 2D array
for (int i = 0; i < matrix.length; i++) {   // Row
    for (int j = 0; j < matrix[i].length; j++) {    // Column
        System.out.println(matrix[i][j]);
    }
}
```

---

## Common Array Methods (java.util.Arrays)

```java
import java.util.Arrays;

int[] numbers = {50, 10, 30, 20, 40};

// Sort array
Arrays.sort(numbers);
System.out.println(Arrays.toString(numbers));  // Output: [10, 20, 30, 40, 50]
// Problem: When you try to print an array directly, you get something like [I@1b6d3586 (memory address)
// Solution: Arrays.toString() converts the array into a readable string format


// Binary search (array must be sorted)
int index = Arrays.binarySearch(numbers, 30);
System.out.println(index);  // Output: 2


// Copy array
int[] copy = Arrays.copyOf(numbers, numbers.length);


// Fill array
int[] arr = new int[5];
Arrays.fill(arr, 10);  // All elements become 10


// Compare arrays
int[] arr1 = {1, 2, 3};
int[] arr2 = {1, 2, 3};
System.out.println(Arrays.equals(arr1, arr2));  // Output: true
```

---

## Important Notes

⚠️ **Array Index Out of Bounds**: Accessing an index outside the valid range causes `ArrayIndexOutOfBoundsException`

⚠️ **Null Pointer Exception**: Accessing elements of a null array causes `NullPointerException`

✅ **Best Practice**: Always check array bounds before accessing elements

---

## Assignments

### Assignment 1: Array Sum and Average
Write a program that:
- Declares an array of 5 integers
- Calculates and prints the sum of all elements
- Calculates and prints the average of all elements

### Assignment 2: Find Largest and Smallest
Write a program that:
- Takes an array of integers as input
- Finds and prints the largest number
- Finds and prints the smallest number

### Assignment 3: Array Reversal
Write a program that:
- Takes an array of integers
- Reverses the array (hint: swap elements from both ends)
- Prints the reversed array

### Assignment 4: Count Occurrences
Write a program that:
- Takes an array of integers and a target number
- Counts how many times the target number appears in the array
- Prints the count

### Challenge Assignment: Grade Calculator
Write a program that:
- Takes an array of student marks (0-100)
- Counts the number of students in each grade: A, B, C, D, F
- Prints the count for each grade
