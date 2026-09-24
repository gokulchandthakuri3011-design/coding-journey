"""
### Assignment 2: Task Queue Simulation

1. Create a `deque` with some tasks such as `"Read"`, `"Write"`, `"Code"`.
2. Add a new task to the left or right.
3. Remove tasks from the left and print the queue.
4. Explain in comments which end is used for FIFO and which is used for LIFO-like behavior.

**File:** `Day33_Task2.py`
"""

from collections import deque

# deque supports efficient operations from both ends
# Left end is used for queue-like FIFO behavior with popleft()
# Right end is used for stack-like LIFO behavior with pop()

tasks = deque(["Read", "Write", "Code"])
print(f"Initial queue: {tasks}")

# Add new tasks to both ends
# append() adds to the right, appendleft() adds to the left

tasks.append("Practice")
tasks.appendleft("Learn")
print(f"Queue after adding tasks: {tasks}")

# FIFO behavior: remove from the left
first_task = tasks.popleft()
print(f"Removed from the left: {first_task}")
print(f"Queue after popleft(): {tasks}")

# LIFO-like behavior: remove from the right
last_task = tasks.pop()
print(f"Removed from the right: {last_task}")
print(f"Final queue: {tasks}")