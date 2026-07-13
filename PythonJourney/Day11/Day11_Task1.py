"""
### Assignment 1: Phone Book Database

*Practice dictionary creation, updating, and safe value retrieval.*

1. Create a dictionary called `phone_book` containing the names and phone numbers of 3 friends. (Example: `"Alice": "555-0199"`).
2. Print the entire phone book.
3. Add a new contact to the phone book: `"David"` with the number `"555-0244"`.
4. Update the phone number of the first contact you created to a new number.
5. Ask the user to input a name to search for.
6. Use the `.get()` method to search the phone book.
   - If the contact exists, print `"Phone number: <number>"`.
   - If the contact does not exist, print `"Contact not found in phone book."`.
- **File:** `Day11_Task1.py`
"""

# Printing the task description
print("     Phone Book Database     ")

# Creating the phone book dictionary
phone_book = {
    "Arun": "555-0199",
    "Bella": "555-0123",
    "Charlie": "555-0456"
}

# Printing the entire phone book
print(f"Phone Book: {phone_book}")

# Adding a new contact to the phone book
phone_book["David"] = "555-0244"

# Updating the phone number of the first contact
phone_book["Arun"] = "555-0999"

# Asking the user to input a name to search for
search_name = input("Enter a name to search for: ")

# Using the .get() method to search the phone book
phone_number = phone_book.get(search_name)
if phone_number:
    print(f"Phone number: {phone_number}")
else:
    print("Contact not found in phone book.")

    