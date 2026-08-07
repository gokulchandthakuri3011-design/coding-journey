"""
### Assignment 1: The Dynamic Task List
*Practice adding and removing items from a list.*

1. Create an empty list called `task_list`.
2. Use `.append()` to add the following tasks:
   - `"Buy groceries"`
   - `"Do laundry"`
   - `"Study Python"`
   - `"Go for a walk"`
3. Print the current task list.
4. Use `.insert()` to add `"Call the dentist"` at index `1`.
5. Print the list again and check the new order.
6. You have completed the laundry. Use `.remove()` to delete `"Do laundry"`.
7. The last task is done for the day. Use `.pop()` to remove it and print what was removed.
8. Print the final task list.
"""

# Step 1: Create an empty list called task_list
task_list = []

# Step 2: Use .append() to add tasks
task_list.append("Buy groceries")
task_list.append("Do laundry")
task_list.append("Study Python")
task_list.append("Go for a walk")

# Step 3: Print the current task list
print("Current task list: ", task_list)

# Step 4: Use .insert() to add "Call the dentist" at index 1
task_list.insert(1, "Call the dentist")

# Step 5: Print the list again and check the new order
print("Updated task list: ", task_list)

# Step 6: Use .remove() to delete "Do laundry"
task_list.remove("Do laundry")

# Step 7: Use .pop() to remove the last task and print what was removed
removed_task = task_list.pop()  # This will remove the last task, which is "Go for a walk"
print("Removed task: ", removed_task)

# Step 8: Print the final task list
print("Final task list: ", task_list)
