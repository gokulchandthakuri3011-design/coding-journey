# Smart To-Do List Manager (with category tagging and priority levels)
# Using list, tuple, dictionary, functions and sets.
"""
## 🏆 Stretch Challenges (Optional)
If you complete the tasks above, try adding these advanced features:
1. **Persistent Storage (JSON)**: Research Python's `json` module.
   Write functions to save the `database` list to a `data.json` file when exiting, and load it automatically 
"""

from datetime import datetime # datetime is used to get current date and time.
import json # file format storing data as text(readable & portable)-saves list/dict to a file and load them back

# Initialize list (database)
to_do_list = []  # An empty list to hold all the task dictionaries

# Define the set of active tags
active_tags = {"Work", "Personal", "Study", "Shopping"}


def display_menu():
    """Displays the main menu options."""
    print("\n--- Smart To-Do List Menu ---")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Search Tasks")
    print("4. Delete Task")
    print("5. Manage Categories(Tags)")
    print("6. Exit")
    # Return the user's menu choice so callers can decide what to do next.
    return input("Enter your choice (1-6): ")


def add_task():
    """Adds a new task to the list."""
    # Asking user for the task title
    title = input("Enter the task title: ")
    # Checking if the input is empty/whitespace and returning so that user can re-enter.
    if not title.strip():  # strip() removes any whitespace from the string
        print("Task title cannot be empty. Please try again.")
        return # exits the current function skipping the rest of code and returns to where the function was called with None

    # Displaying the available tags and asking user to choose one.
    print("\nAvailable Categories:")
    # Convert set to a list so it has a consistent order during this menu render
    tags_list = list(active_tags)
    for i, tag in enumerate(tags_list, start=1):
        print(f"{i}. {tag}")

    choice = input(f"Enter your category (1-{len(tags_list)}): ")
    # Checking if choice is valid and is numeric
    if not choice.isdigit() or int(choice) not in range(1, len(tags_list) + 1):  # isdigit() checks if the input string consists of digits only
        print("Invalid category. Defaulting to 'Uncategorized'")
        category = "Uncategorized"
    else:
        category = tags_list[int(choice) - 1]

    # Retrieve the current local date 
    current_date = datetime.now() # datetime.now() returns the current local date and time as a datetime object.
                                  # We can then access the day, month, and year attributes to store them in our task dictionary.
    # Store date as an immutable tuple (day, month, year)
    date = (current_date.day, current_date.month, current_date.year)

    # Appending the dictionary to the list
    to_do_list.append({"Title": title, "Category": category, "Date": date})
    print("Task added successfully!")


def view_tasks():
    """Displays all tasks in a neat list."""
    # Checking if the list is empty
    if not to_do_list:
        print("No Tasks found!")
        return

    # Displaying tasks in a neat table
    print("\n--- All Tasks ---")
    print("-" * 50)
    for i, task in enumerate(to_do_list, start=1):
        day, month, year = task["Date"]  # Unpacking the tuple within the Date key in dict
        print(f"{i}. {task['Category']} / {task['Title']} - {day}/{month}/{year}")


def search_tasks():
    """Searches for tasks matching a keyword in title or category."""
    # Asking user for search query
    query = input("Enter keyword to search in title or category: ").lower().strip()
    if not query:
        print("Search query cannot be empty.")
        return

    # Searching for tasks that match the query
    found_tasks = [task for task in to_do_list if query in task["Title"].lower() or query in task["Category"].lower()]

    # Checking if the list is empty
    if not found_tasks:
        print("No matching tasks found!")
        return

    # Displaying the found tasks
    print("\n--- Search Results ---")
    for i, task in enumerate(found_tasks, start=1):
        day, month, year = task["Date"]
        print(f"{i}. {task['Category']} / {task['Title']} - {day}/{month}/{year}")


def delete_task():
    """Deletes a task by index."""
    # Listing all tasks first
    view_tasks()

    # Asking user to enter task number to delete
    choice = input("Enter the number of the task to delete: ")
    # Checking if user entered a valid numeric choice
    if choice.isdigit() and int(choice) in range(1, len(to_do_list) + 1):
        # Removing the task from the list               
        deleted_task = to_do_list.pop(int(choice) - 1)
        print(f"Task '{deleted_task['Title']}' deleted successfully!")
    else:
        print("Invalid choice. Please try again.")


def add_category():
    """Adds a new category to the active tags set."""
    category = input('Enter new category name: ').strip()
    if not category:
        print("Category name cannot be empty. Please try again.")
        return
    # Case-insensitive duplicate checking
    if category.lower() in {tag.lower() for tag in active_tags}:
        print("Category already exists.")
        return
    
    active_tags.add(category)
    print(f"Category '{category}' added successfully!")


def view_categories():
    """Displays all current categories."""
    print("\n--- Active Categories ---")
    for i, tag in enumerate(active_tags, start=1):
        print(f"{i}. {tag}")


def delete_category():
    """Deletes a category from active tags."""
    if not active_tags:
        print("No categories to delete.")
        return

    view_categories()
    choice = input("Enter the category number to delete: ")
    if choice.isdigit() and int(choice) in range(1, len(active_tags) + 1):
        tags_list = list(active_tags)
        category_to_remove = tags_list[int(choice) - 1]
        active_tags.remove(category_to_remove)
        print(f"Category '{category_to_remove}' deleted successfully!")
    else:
        print("Invalid choice. Please try again.")


def manage_categories():
    """Runs the category management sub-menu."""
    while True:
        print("\n--- Manage Categories ---")
        print("1. Add Category")
        print("2. View All Categories")
        print("3. Delete Category")
        print("4. Back to Main Menu")
        
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            add_category()
        elif choice == "2":
            view_categories()
        elif choice == "3":
            delete_category()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


def exit_program():
    """Prints thank you message on exit."""
    save_tasks()
    print("Thank You for using Smart To-Do List Manager!")

def save_tasks():
    """Saves the to-do-list to a JSON file."""
    with open('data.json', 'w') as f: # opens a file (data.json) in write mode('w')
        json.dump(to_do_list, f) # converts list into JSON format & writes it to the file
                                 # to_do_list - what to save, f - the file to write to

def load_tasks():
    """Loads the to_do_list from a JSON file."""
    global to_do_list # Allows function to modify the global var(to-do_list)
    try:
        with open('data.json', 'r') as f: # Opens the file in read mode('r')
            to_do_list = json.load(f) # Read JSON from the file and convert it back to a list
    except FileNotFoundError: # if file doesn't exists, creates an empty list
        to_do_list = []        


def main():
    """Main program entry point: loop and dispatch menu choices."""
    load_tasks() 
    while True:
        user_choice = display_menu()
        if user_choice == "1":
            add_task()
        elif user_choice == "2":
            view_tasks()
        elif user_choice == "3":
            search_tasks()
        elif user_choice == "4":
            delete_task()
        elif user_choice == "5":
            manage_categories()
        elif user_choice == "6":
            exit_program()
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__": # This line checks if the script is being run directly (as the main program) rather than imported as a module in another script. 
    main()
