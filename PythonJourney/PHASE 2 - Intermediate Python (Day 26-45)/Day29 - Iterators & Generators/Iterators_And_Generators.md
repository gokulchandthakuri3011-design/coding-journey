 # Iterators and Generators

## 1. What Is an Iterable?

An **iterable** is an object whose items can be visited one at a time. Lists, tuples, strings, dictionaries, and sets are common iterables.

```python
names = ["Ava", "Ben", "Chloe"]

for name in names:
	print(name)
```

`iter()` gets an iterator from an iterable:

```python
names = ["Ava", "Ben", "Chloe"]
name_iterator = iter(names)

print(next(name_iterator))  # Ava
print(next(name_iterator))  # Ben
```

`next()` asks for the next item. When no items remain, Python raises `StopIteration`.

## 2. The Iterator Protocol

An iterator follows two rules:

- `__iter__()` returns the iterator object itself.
- `__next__()` returns the next value or raises `StopIteration`.

```python
class CountUp:
	def __init__(self, stop):
		self.current = 1
		self.stop = stop

	def __iter__(self):
		return self

	def __next__(self):
		if self.current > self.stop:
			raise StopIteration

		value = self.current
		self.current += 1
		return value


for number in CountUp(3):
	print(number)  # 1, 2, 3
```

An iterator keeps its current position. Once it is exhausted, it cannot normally be restarted; create a new iterator when needed.

## 3. Custom Iterable Classes

An object can be an iterable without being its own iterator. Its `__iter__()` method can return a fresh iterator each time:

```python
class Countdown:
	def __init__(self, start):
		self.start = start

	def __iter__(self):
		current = self.start
		while current > 0:
			yield current
			current -= 1


for number in Countdown(3):
	print(number)  # 3, 2, 1
```

This design allows the same `Countdown` object to be iterated over again from the beginning.

## 4. Generator Functions and `yield`

A function containing `yield` is a **generator function**. Calling it returns a generator object, but its body does not run until values are requested.

```python
def square_numbers(limit):
	for number in range(1, limit + 1):
		yield number ** 2


for square in square_numbers(4):
	print(square)  # 1, 4, 9, 16
```

Each `yield` pauses the function. The next call to `next()` resumes it from that point. Generators produce values lazily, so they are useful for large or endless data streams.

## 5. Generator Expressions

A generator expression looks like a list comprehension but uses parentheses:

```python
squares = (number ** 2 for number in range(1, 5))
print(next(squares))  # 1
```

| List comprehension | Generator expression |
| --- | --- |
| `[x * 2 for x in values]` | `(x * 2 for x in values)` |
| Creates all values immediately | Creates values when requested |
| Uses more memory for large data | Uses less memory |
| Can be indexed and reused | Must be consumed in order |

Use a list when you need all results repeatedly. Use a generator when processing one result at a time or working with a large data source.

## 6. Infinite Generators

An infinite generator has no natural stopping point. It must contain a condition in the consumer to stop reading values.

```python
def numbers_from(start=1):
	number = start
	while True:
		yield number
		number += 1


for number in numbers_from(10):
	print(number)
	if number == 12:
		break
```

Without the `break`, this loop would continue forever.

## 7. Key Points

- An iterable can provide an iterator with `iter()`.
- An iterator produces one item at a time with `next()`.
- `StopIteration` signals that an iterator is finished.
- `yield` pauses a generator and remembers its state.
- Generators reduce memory usage by producing values lazily.
- Always give infinite generators a clear stopping condition when consuming them.

## Assignments

### Assignment 1: Custom Iterator

Create a `CountdownIterator` class that counts from a starting number down to `1`.

Requirements:

1. Implement `__iter__()` and `__next__()`.
2. Raise `StopIteration` after returning `1`.
3. Test it with a `for` loop and with manual `next()` calls.

Questions:

- What happens when you call `next()` after the iterator is exhausted?
- Why must `__next__()` update the current value?

### Assignment 2: Generator Function

Write a `fibonacci_generator(limit)` function that yields the first `limit` Fibonacci numbers.

Questions:

- Where does the generator pause?
- How much code would be needed to return the same values in a list?
- What happens when `limit` is `0`?

### Assignment 3: Infinite Stream Generator

Create a generator called `even_numbers()` that produces `2, 4, 6, ...` forever.

Use a loop to print only the first five values. Do not build a list containing infinite values.

Question:

- Why is a `break` necessary when consuming this generator?

### Assignment 4: Custom Range-Like Class

Build a `SimpleRange` class that accepts `start`, `stop`, and an optional `step`.

Requirements:

1. Make it work in a `for` loop.
2. Stop before reaching `stop`, like Python's `range()`.
3. Support positive steps first, then add negative-step support.
4. Test an empty range and a step larger than the range.

Questions:

- What should happen when `step` is `0`?
- Should `SimpleRange` be its own iterator or return a new iterator each time? Explain your choice.

### Assignment 5: Memory Comparison

Create a list comprehension and a generator expression that both produce the squares from `1` to `1,000,000`.

Questions:

- Which one stores all values immediately?
- Which one is better when you only need to calculate the total once?
- Use `sys.getsizeof()` to compare the objects and explain the result.
