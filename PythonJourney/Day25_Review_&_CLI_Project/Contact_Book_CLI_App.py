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
contacts_file = Path("contacts.json")

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
            print(f"Invalid input: {e}. Please try again:")

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

# Reading contacts from the JSON file
def load_contacts(path: str) -> list:
    try:
        with open(path, "r", encoding="utf-8") as file:
    except FileNotFoundError as e:
        print(f"Error: {e}. Starting with an empty contact list.")
        return []
    except json.JSONDecodeError as e:
        print(f"Error: {e}. Starting with an empty contact list.")
        return []
    else:
        return json.load(file)

# Saving contacts to the JSON file
def save_contacts(path: str, contacts: list):
    try:
        with open(path, "w") as file:
    except Exception as e:
        print(f"Error saving contacts: {e}")
    else:
        json.dump(contacts, file, indent=4)
        print(f"Contacts saved to {path}.")

# Adding a new contact
def add_contact(contacts: list):

