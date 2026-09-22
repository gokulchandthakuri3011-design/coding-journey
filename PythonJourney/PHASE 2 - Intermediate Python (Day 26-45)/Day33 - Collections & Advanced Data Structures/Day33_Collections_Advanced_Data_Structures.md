# Day 33: Collections & Advanced Data Structures

Welcome to Day 33! Today we will learn about Python collections and a few advanced data structures that help us solve real-world problems more efficiently.

So far, you have learned about lists, tuples, sets, and dictionaries. Now we will go one step further and explore specialized structures like `deque`, `Counter`, `defaultdict`, `OrderedDict`, and `namedtuple`.

---

## 📝 Concept Notes

---

### 1. What is a Collection?

A collection is a container that stores multiple items together. Python has built-in collections like:

- list
- tuple
- set
- dict

Python also provides a powerful module called `collections` that gives extra data structures for specific use cases.

---

### 2. `collections.deque`

`deque` stands for double-ended queue.

It is useful when you need to add or remove items from both ends efficiently.

```python
from collections import deque

queue = deque(["A", "B", "C"])
queue.append("D")
queue.appendleft("Z")

print(queue)
```

Output:

```python
deque(['Z', 'A', 'B', 'C', 'D'])
```

`deque` is faster than a normal list for frequent insertions/deletions at both ends.

---

### 3. `collections.Counter`

`Counter` is used to count the frequency of items in a collection.

```python
from collections import Counter

letters = ['a', 'b', 'a', 'c', 'a', 'b']
count = Counter(letters)

print(count)
print(count['a'])
```

Output:

```python
Counter({'a': 3, 'b': 2, 'c': 1})
3
```

This is very useful for word frequency analysis, inventory counting, and statistics.

---

### 4. `collections.defaultdict`

A `defaultdict` is a dictionary that gives a default value for a missing key.

```python
from collections import defaultdict

scores = defaultdict(int)
scores['math'] += 5
scores['science'] += 3

print(scores)
```

Output:

```python
{'math': 5, 'science': 3}
```

It prevents `KeyError` when a key does not exist yet.

---

### 5. `collections.OrderedDict`

`OrderedDict` keeps insertion order of keys.

```python
from collections import OrderedDict

data = OrderedDict()
data['first'] = 1
data['second'] = 2

print(data)
```

In modern Python, regular dictionaries already preserve insertion order, but `OrderedDict` is still useful in older or more specialized code.

---

### 6. `collections.namedtuple`

A `namedtuple` behaves like a tuple but gives names to each element.

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)

print(p)
print(p.x, p.y)
```

Output:

```python
Point(x=10, y=20)
10 20
```

This is helpful when you want readable data records without creating a full class.

---

### 7. Priority Queue using `heapq`

A priority queue allows us to process items by priority.

```python
import heapq

items = [5, 2, 9, 1, 7]
heapq.heapify(items)
print(items)

heapq.heappush(items, 3)
print(heapq.heappop(items))
```

`heapq` is useful for scheduling, shortest path logic, and task prioritization.

---

### 8. Binary Search with `bisect`

The `bisect` module helps us insert and find values in sorted lists efficiently.

```python
import bisect

numbers = [1, 3, 5, 7]
index = bisect.bisect_left(numbers, 5)
print(index)
```

This helps in searching sorted data quickly without scanning the whole list.

---

### 9. Why These Structures Matter

Advanced data structures help us:

- handle large amounts of data efficiently
- organize priorities
- count repeated values
- avoid unnecessary complexity
- simulate real-world problem solving

These are used in many real applications like task schedulers, web queues, dashboards, and analytics tools.

---

## 💻 Practice Assignments

Create a new Python file under the `C:\PythonJourney` folder for each assignment.

---

### Assignment 1: Word Frequency Counter

1. Create a sentence.
2. Use `Counter` to count how many times each word appears.
3. Print the word counts.
4. Also print the most common word.

**File:** `Day33_Task1.py`

---

### Assignment 2: Task Queue Simulation

1. Create a `deque` with some tasks such as `"Read"`, `"Write"`, `"Code"`.
2. Add a new task to the left or right.
3. Remove tasks from the left and print the queue.
4. Explain in comments which end is used for FIFO and which is used for LIFO-like behavior.

**File:** `Day33_Task2.py`

---

### Assignment 3: Student Score Tracker

1. Create a `defaultdict(int)` for student marks.
2. Add scores for 5 students.
3. Print each student’s total.
4. Show how a missing key gets a default value of `0`.

**File:** `Day33_Task3.py`

---

### Assignment 4: Priority Task Manager

1. Use `heapq` to create a list of tasks with priorities.
2. Push tasks in different orders.
3. Print the tasks in priority order.

Example idea:

```python
tasks = [(2, "Review code"), (1, "Reply to email"), (3, "Prepare presentation")]
```

**File:** `Day33_Task4.py`

---

## ✅ Quick Review Questions

1. What is the main difference between a list and a `deque`?
2. What does `Counter` help you do?
3. Why is `defaultdict` useful?
4. What is a `namedtuple`?
5. What is the purpose of `heapq`?
6. When would you use `bisect`?

---

## 🧠 Short Summary

Python’s collection tools and advanced data structures make code more efficient and cleaner. They help us solve problems like counting data, storing priority tasks, and organizing structured information without writing too much custom logic.

Today’s focus is understanding when to use the right structure for the job.
