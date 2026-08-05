"""
## 3. Capstone Project: Contact Book CLI App

### Requirements

| Requirement | Skills Used |
|---|---|
| Save contacts in a **JSON file** | File handling, JSON |
| **Fully validate** user input | Conditionals, functions |
| **Gracefully handle** exceptions | `try`/`except` |
| Structure code using **functions** | Modular design |
| Clean **CLI menu** | Loops, conditionals |

### Features

- Add a new contact (validated name, phone, email)
- View all contacts (numbered list)
- Search contacts by name
- Update an existing contact
- Delete a contact
- Persist everything to `contacts.json` so data survives restart

### Sample Menu

```
==========================================
        📇 CONTACT BOOK (CLI)
==========================================
  1. Add contact
  2. View all contacts
  3. Search contacts
  4. Update contact
  5. Delete contact
  6. Exit
==========================================
Choose an option (1-6):
"""

import json
from pathlib import Path

# Creating a contact list to store contacts
contacts = []

# Creating a path to the contacts.json file
contacts_file = str(Path("contacts.json"))

# Showing the menu to the user and asking for input
def show_menu():
    print("="*40)
    print("     💾 CONTACT BOOK (CLI)     ")
    print("="*40)
    print(" 1. Add contact")
    print(" 2. View all contacts")
    print(" 3. Search contact")
    print(" 4. Update contact")
    print(" 5. Delete contact")
    print(" 6. Exit")

# Asking user for choice and validating it
def get_user_choice():
    while True:
        try:
            choice = int(input("Choose an option (1-6): "))
            if choice < 1 or choice > 6:
                raise ValueError("Choice must be between 1 & 6.")
            return choice
        except ValueError as e:
            print(f"Invalid input: {e} Please try again:")

# Getting user input for contact details and validating it
def get_contact_details(choice: int) -> dict:
    contact = {}
    if choice == 1: # Add contact
        contact["name"] = input("Enter name: ").strip()
        contact["phone"] = input("Enter phone number: ").strip()
        contact["email"] = input("Enter email address: ").strip()
    elif choice == 4: # Update contact
        contact["name"] = input("Enter new name (leave blank to keep current): ").strip()
        contact["phone"] = input("Enter new phone number (leave blank to keep current): ").strip()
        contact["email"] = input("Enter new email address (leave blank to keep current): ").strip()
    return contact

# Adding a new contact
def add_contact():
    contact = get_contact_details(1)
    if contact["name"] and contact["phone"] and contact["email"]:
        contacts.append(contact)
        save_contacts(contacts_file, contacts)
        print(f"Contact {contact['name']} added successfully.")
    else:
        print("All fields are required. Contact not added.")

# Viewing all contacts
def view_contacts():
    if contacts:
        print("\n   All Contacts   \n")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print("No contacts found.")

# Searching for a contact by name
def search_contact():
    if not contacts:
        print("No contacts available to search.")
        return

    search_name = input("Enter name to search: ").strip().lower()
    found_contact = [contact for contact in contacts if search_name in contact["name"].lower()]
    if found_contact:
        print("\n Search Results: \n")
        for index, contact in enumerate(found_contact, start=1):
            print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print(f"No contacts found with name containing '{search_name}'.")

# Updating an existing contact
def update_contact():
    if not contacts:
        print("No contacts available to update.")
        return

    view_contacts()
    contact = get_contact_details(4)
    while True:
        try:
            contact_index = int(input("Enter the index of the contact to update: ")) - 1
            if 0 <= contact_index < len(contacts):
                changed = False
                if contact["name"]:
                    contacts[contact_index]["name"] = contact["name"]
                    changed = True
                if contact["phone"]:
                    contacts[contact_index]["phone"] = contact["phone"]
                    changed = True
                if contact["email"]:
                    contacts[contact_index]["email"] = contact["email"]
                    changed = True

                if changed:
                    save_contacts(contacts_file, contacts)
                    print(f"Contact at index {contact_index + 1} updated successfully.")
                else:
                    print("No changes were made to the contact.")
                break
            else:
                raise IndexError("Index out of range")
        except (ValueError, IndexError) as e:
            print(f"Error: {e}. Please enter a valid index.")
            retry = input("Wanna try again updating the existing contacts? (y/n): ").strip().lower()
            if retry != 'y':
                break

# Deleting a contact
def delete_contact():
    if not contacts:
        print("No contacts available to delete.")
        return

    view_contacts()
    while True:
        user_input = input("Enter the index of the contact to delete (or 'n' to cancel): ").strip().lower()
        if user_input in ('n', 'c', 'q'):
            print("Delete cancelled.")
            break
        try:
            index_to_del = int(user_input) - 1
            if 0 <= index_to_del < len(contacts):
                deleted_contact = contacts.pop(index_to_del)
                save_contacts(contacts_file, contacts)
                print(f"{deleted_contact['name']} successfully deleted.")
                break
            else:
                raise IndexError("Index out of range")
        except ValueError:
            print("Invalid input. Enter a contact index number or 'n' to cancel.")
        except IndexError as e:
            print(f"Error: {e}. Please enter a valid index.")
            retry = input("If you wanna retry? (y/n): ").strip().lower()
            if retry != 'y':
                break

# Saving contacts to the JSON file
def save_contacts(path: str, contacts_list: list):
    try:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(contacts_list, file, indent=4)
    except Exception as e:
        print(f"Error saving contacts: {e}")
    else:
        print(f"Contacts saved to {path}.")

# Reading contacts from the JSON file
def load_contacts(path: str) -> list:
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as e:
        print(f"Error: {e}. Starting with an empty contact list.")
        return []
        
def main():
    global contacts
    contacts = load_contacts(contacts_file)
    while True:
        show_menu()
        choice = get_user_choice()
        if choice == 1:
            add_contact()
        elif choice == 2:
            view_contacts()
        elif choice == 3:
            search_contact()
        elif choice == 4:
            update_contact()
        elif choice == 5:
            delete_contact()
        elif choice == 6:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()