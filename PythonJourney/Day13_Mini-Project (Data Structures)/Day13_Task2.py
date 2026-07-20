# 2. **Option B: Advanced Contact Book** (with relationship tags and duplicate prevention)
# In this task, 
# you will enhance the contact book application by allowing users to manage categories (tags) for their contacts.
# Users should be able to add, view, and delete categories,
# and the application should prevent duplicate category names (case-insensitive).
# The main menu will also include an option to manage categories.

# An empty list to store contacts
contacts = []

# A set to store unique category names (case-insensitive) (relationship tags)
categories = {"Family", "Friends", "Work", "Other"}

import sys # "sys" is Python built-in-library module

def display_menu():
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Delete Contact")
    print("4. Manage Categories")
    print("5. Exit")

def add_contact():
    # Get contact details from the user
    name = input("Enter contact name: ").strip()
    try:
        phone = int(input("Enter contact phone number: ").strip())
    except ValueError: # if users types non digits the "except" prevents error and lets print()
        print("Invalid phone number. Please enter digits only.")
        return
    email = input("Enter contact email: ").strip()
    category = input("Enter contact category (Family, Friends, Work, Other): ").strip()

    # Validate category
    if category.capitalize() not in categories:
        print("Invalid category. Please choose from Family, Friends, Work, or Other.")
        return
    

    # Add the contact to the contacts list
    contacts.append({"name": name, "phone": phone, "email": email, "category": category.capitalize()})
    print("Contact added successfully!")

def view_contacts():
    # Check if the contacts list is empty
    if not contacts:
        print("No contacts to display.")
        return
    
    # Displaying the contacts based on user input
    # Ask the user if to display all contacts or search by name/category
    choice = input("Do you want to view all contacts (yes/no)? ").strip().lower()
    if choice == "yes":
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Category: {contact['category']}")
    elif choice == "no":
        criteria = input("Search by name or category? (enter 'name' or 'category'): ").strip().lower()
        if criteria not in ("name", "category"):
            print(f"Invalid criteria: {criteria}")
            return

        search_value = input(f"Enter the {criteria} to search for: ").strip().lower()
        found = False
        for i, contact in enumerate(contacts, start=1):
            if ((criteria == "name" and search_value == contact["name"].lower()) or
                (criteria == "category" and search_value == contact["category"].lower())):
                print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Category: {contact['category']}")
                found = True

        if not found:
            print(f"No contacts found for {criteria}: {search_value}")

def delete_contact():
    # Check if the contacts list is empty
    if not contacts:
        print("No contacts to delete.")
        return
    
    # Displaying the contacts with index numbers
    for i, contact in enumerate(contacts, start = 1):
        print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Category: {contact['category']}")

    # Get the index of the contact to delete from the user
    index = int(input("Enter the index number of the contact to delete: ").strip())
    if 1 <= index <= len(contacts):
        deleted_contact = contacts.pop(index - 1)
        print(f"Contact {deleted_contact['name']} deleted successfully!")
    else:
        print("Invalid index. Please try again.")
        return
    
def manage_categories():
    print("\n--- Manage Categories ---")
    print("1. Add Category")
    print("2. View Categories")
    print("3. Delete Category")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        new_category = input("Enter new category name: ").strip()
        if new_category.capitalize() in categories:
            print("Category already exists. Please choose a different name.")
        else:
            categories.add(new_category.capitalize())
            print("Category added successfully!")
    elif choice == "2":
        print("Categories:")
        for category in sorted(categories):
            print(category)
    elif choice == "3":
        category_to_delete = input("Enter the category name to delete: ").strip()
        if category_to_delete.capitalize() not in categories:
            print("Category not found. Please try again.")
            return
        categories.remove(category_to_delete.capitalize())
        print("Category deleted successfully!")
    else:
        print("Invalid choice. Please try again.")
        return
    
def exit_program():
    print("Exiting the program. Goodbye!")
    sys.exit() # sys.exit() exits the whole program by breaking the main loop

# Main loop to run the contact book application
while True:
    display_menu()
    user_choice = input("Enter your choice: ").strip()
    if user_choice == "1":
        add_contact()
    elif user_choice == "2":
        view_contacts()
    elif user_choice == "3":
        delete_contact()
    elif user_choice == "4":
        manage_categories()
    elif user_choice == "5":
        exit_program()
    else:
        print("Invalid choice. Please try again.")
