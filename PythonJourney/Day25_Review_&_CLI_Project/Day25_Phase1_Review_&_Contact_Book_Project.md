# Day 25: Phase 1 Review & Capstone CLI Project

> **Duration:** 1 hour (30 min review + 30 min practice)
> **Goal:** Review ALL Phase 1 topics and build the **Contact Book CLI App** — a capstone project that uses everything you've learned (variables, data structures, functions, file handling, and error handling).

---

## Table of Contents

1. [Why a Capstone Project?](#1-why-a-capstone-project)
2. [Phase 1 Topic Review](#2-phase-1-topic-review)
3. [Capstone Project: Contact Book CLI App](#3-capstone-project-contact-book-cli-app)
4. [Step-by-Step Build Plan](#4-step-by-step-build-plan)
5. [Code Walkthrough](#5-code-walkthrough)
6. [Extra Challenges](#6-extra-challenges)
7. [Phase 1 Self-Assessment Checklist](#7-phase-1-self-assessment-checklist)
8. [Summary](#8-summary)

---

## 1. Why a Capstone Project?

A capstone is a final project that combines everything you've learned into one real program. It's how you prove to yourself that you've actually **mastered** the material — not just memorized it.

The Contact Book CLI App tests:
- **Variables & Data Types** — storing contact info
- **Lists & Dictionaries** — organizing many contacts
- **Functions** — structuring the program cleanly
- **File Handling (JSON)** — saving data between runs
- **Error Handling** — surviving bad input and corrupted files
- **Loops & Conditionals** — building a working menu

If you can build this without looking up solutions, you're ready for Phase 2!

---

## 2. Phase 1 Topic Review

### 2.1 Days 1–7: Fundamentals
- Variables, data types (`int`, `float`, `str`, `bool`, `None`)
- Operators, type casting, `input()`, f-strings
- Conditionals (`if`/`elif`/`else`, `match`/`case`)
- Loops (`for`, `while`, `break`, `continue`, `range`)

```python
# Quick refresher
name = input("Your name: ").strip()
age = int(input("Your age: "))          # cast input
if age >= 18:
    print(f"{name} is an adult.")
else:
    print(f"{name} is a minor.")
```

### 2.2 Days 8–14: Data Structures
- **Lists** — ordered, changeable (`append`, `pop`, `sort`, comprehension)
- **Tuples** — ordered, immutable
- **Dictionaries** — key-value pairs (`.get()`, `.keys()`, `.values()`, `.items()`)
- **Sets** — unique, unordered (union, intersection)

```python
# A contact as a dictionary
contact = {"name": "Alice", "phone": "555-1234", "email": "alice@mail.com"}
print(contact.get("name"))   # Alice
print(contact.get("age", "N/A"))   # N/A (safe default)
```

### 2.3 Days 15–22: Functions & Modularity
- `def`, parameters (`*args`, `**kwargs`), `return`
- Scope, closures, lambdas, `map`/`filter`/`reduce`
- Custom modules, `if __name__ == "__main__":`

```python
def validate_phone(phone: str) -> bool:
    """Return True if phone contains only digits, dashes, and spaces."""
    allowed = set("0123456789- ")
    return all(c in allowed for c in phone)
```

### 2.4 Days 23–24: File Handling & Errors
- `with open(...)` for reading/writing
- JSON serialization (`json.dump`, `json.load`)
- `try`/`except`/`else`/`finally`, `raise`

```python
import json

def load_contacts(filename: str) -> list:
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []                       # fresh start
    except json.JSONDecodeError:
        return []                       # corrupted file -> don't crash
```

> **The capstone project combines ALL of these.** If any piece feels fuzzy, re-read that day's notes before starting.

---

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
```

---

## 4. Step-by-Step Build Plan

### Step 1: Plan the Data Model

Each contact is a **dictionary**:
```python
{
    "name": "Alice",
    "phone": "555-1234",
    "email": "alice@mail.com"
}
```

All contacts live in a **list**: `contacts = [...]`

### Step 2: Create the Storage Layer

Two functions — load and save:
```python
import json

FILENAME = "contacts.json"

def load_contacts() -> list:
    try:
        with open(FILENAME, "r") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Warning: contacts.json is corrupted. Starting fresh.")
        return []

def save_contacts(contacts: list) -> None:
    with open(FILENAME, "w") as f:
        json.dump(contacts, f, indent=4)
```

### Step 3: Create the Validation Layer

```python
def validate_name(name: str) -> bool:
    return bool(name.strip())

def validate_phone(phone: str) -> bool:
    allowed = set("0123456789-+ ")
    return bool(phone.strip()) and all(c in allowed for c in phone)

def validate_email(email: str) -> bool:
    return "@" in email and "." in email.split("@")[-1]

def get_valid_input(prompt: str, validator) -> str:
    while True:
        value = input(prompt).strip()
        if validator(value):
            return value
        print("  ❌ Invalid input. Please try again.")
```

### Step 4: Create the Menu Actions

```python
def add_contact(contacts: list) -> None:
    name = get_valid_input("Name: ", validate_name)
    phone = get_valid_input("Phone: ", validate_phone)
    email = get_valid_input("Email: ", validate_email)
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print(f"  ✅ {name} added.")

def view_contacts(contacts: list) -> None:
    if not contacts:
        print("  📭 No contacts yet. Add one!")
        return
    for i, c in enumerate(contacts, 1):
        print(f"  {i}. {c['name']} | {c['phone']} | {c['email']}")

def search_contacts(contacts: list) -> None:
    term = input("Search by name: ").strip().lower()
    results = [c for c in contacts if term in c["name"].lower()]
    if not results:
        print(f"  🔍 No contacts match '{term}'.")
    else:
        for c in results:
            print(f"  → {c['name']} | {c['phone']} | {c['email']}")
```

### Step 5: Build the Main Loop

```python
def main():
    contacts = load_contacts()
    while True:
        print_menu()
        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("  ❌ Invalid choice. Enter 1-6.")

if __name__ == "__main__":
    main()
```

> **Note:** `update_contact` and `delete_contact` are left as your challenge! See the patterns in the walkthrough below.

---

## 5. Code Walkthrough

### Why JSON for Storage?

| Format | Pros | Cons |
|---|---|---|
| Plain text | Simple | Hard to read back into structures |
| CSV | Good for spreadsheets | No nested data |
| **JSON** | Native `dict`/`list`, human-readable, Python built-in | A bit verbose |

JSON maps almost 1:1 to Python: `{}` → `dict`, `[]` → `list`, `"..."` → `str`. That's why it's the perfect pick for this project.

### Why validate input in a loop?

The `get_valid_input` pattern keeps asking until the data is good — no exceptions needed for normal bad input (Day 24 rule: use `if` for *expected* conditions).

### Why catch `json.JSONDecodeError`?

If the user (or an editor) corrupts `contacts.json`, a naive `json.load` would crash the program. Catching it means the app starts fresh instead of dying.

### Deleting a Contact (pattern to follow)

```python
def delete_contact(contacts: list) -> None:
    view_contacts(contacts)
    if not contacts:
        return
    try:
        index = int(input("Enter number to delete: ")) - 1
        removed = contacts.pop(index)
        save_contacts(contacts)
        print(f"  🗑️ Deleted {removed['name']}.")
    except (ValueError, IndexError):
        print("  ❌ Invalid number.")
```

**Updating a contact** follows the same idea: pick a number, then edit one field (name/phone/email) with the validators.

---

## 6. Extra Challenges

| Level | Challenge |
|---|---|
| Easy | Add a "View contact count" option that prints how many contacts exist |
| Easy | Sort contacts alphabetically by name when viewing |
| Medium | Add a "Favorites" boolean field and a menu option to show only favorites |
| Medium | Prevent duplicate names (warn before adding) |
| Hard | Split code into two files: `contact_book.py` (logic) and `main.py` (menu) |
| Hard | Add a `--reset` command-line flag that clears all contacts |

---

## 7. Phase 1 Self-Assessment Checklist

Check each box only if you can explain it AND use it without help:

- [ ] Variables, data types, and type casting
- [ ] Operators (`+`, `//`, `%`, `**`, comparisons, `and`/`or`/`not`)
- [ ] Strings, f-strings, slicing, and common string methods
- [ ] `if`/`elif`/`else` and `match`/`case`
- [ ] `for` and `while` loops, `break`, `continue`, `range()`
- [ ] Lists — methods, slicing, comprehensions
- [ ] Tuples — unpacking, when to use them
- [ ] Dictionaries — get/update/iterate, `.items()`
- [ ] Sets — unique values and set operations
- [ ] Functions — parameters, `*args`/`**kwargs`, `return`, type hints
- [ ] Scope — local, global, closures
- [ ] Lambdas and `map()`/`filter()`
- [ ] Custom modules and the `__name__ == "__main__"` guard
- [ ] File handling — `with`, read/write, CSV and JSON
- [ ] `try`/`except`/`else`/`finally`, raising exceptions
- [ ] **Built the Contact Book CLI App** from scratch

If you checked all boxes: **you've completed Phase 1 — Python Fundamentals!** 🎉

---

## 8. Summary

| Concept | Phase 1 Takeaway |
|---|---|
| Fundamentals | Syntax, variables, operators, control flow |
| Data Structures | Lists, tuples, dicts, sets — choose the right tool |
| Functions | Reusable, testable, modular code |
| Files | Read/write CSV & JSON for persistence |
| Errors | Expect the unexpected, handle it gracefully |
| **Capstone** | Contact Book CLI that ties it all together |

---

> **Tomorrow:** Day 26 — OOP: Classes & Objects. Get ready for Phase 2! 🟡
>
> **Remember:** The best way to review is to build. If you can write the Contact Book from a blank file, Phase 1 is officially complete. Happy coding! 🐍
