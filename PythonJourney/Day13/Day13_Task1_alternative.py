from collections import defaultdict

# Day 13 Alternative: To-Do List Using Day 12 Topics
# This version uses dictionaries, sets, and defaultdict from collections.
# It avoids datetime and complex task records, keeping the focus on Day 12 skills.

tasks_by_category = defaultdict(list)
active_categories = set()


def display_menu():
    print("\n--- Simple To-Do Manager ---")
    print("1. Add a task")
    print("2. View tasks by category")
    print("3. View all categories")
    print("4. View task counts")
    print("5. Exit")
    return input("Choose an option (1-5): ")


def add_task():
    title = input("Enter task title: ").strip()
    if not title:
        print("Task title cannot be empty.")
        return

    category = input("Enter category for this task: ").strip()
    if not category:
        category = "Uncategorized"

    active_categories.add(category)
    tasks_by_category[category].append(title)
    print(f"Added task '{title}' under category '{category}'.")


def view_tasks_by_category():
    if not tasks_by_category:
        print("No tasks have been added yet.")
        return

    print("\n--- Tasks by Category ---")
    for category, tasks in tasks_by_category.items():
        print(f"\n{category} ({len(tasks)} task{'s' if len(tasks) != 1 else ''})")
        for index, task in enumerate(tasks, start=1):
            print(f"  {index}. {task}")


def view_categories():
    if not active_categories:
        print("No categories have been added yet.")
        return

    print("\n--- Active Categories ---")
    for index, category in enumerate(active_categories, start=1):
        print(f"{index}. {category}")


def view_task_counts():
    if not tasks_by_category:
        print("No tasks have been added yet.")
        return

    print("\n--- Task Counts by Category ---")
    for category, tasks in tasks_by_category.items():
        print(f"{category}: {len(tasks)}")


def main():
    while True:
        choice = display_menu()
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks_by_category()
        elif choice == "3":
            view_categories()
        elif choice == "4":
            view_task_counts()
        elif choice == "5":
            print("Thank you for using the Simple To-Do Manager!")
            break
        else:
            print("Invalid option. Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
