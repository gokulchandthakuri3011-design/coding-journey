"""
### Assignment 4: Crash-Proof Contact Manager (Medium)

Create a program that:
- Asks user for contacts (name, phone, email)
- Validates each field:
  - Name: non-empty
  - Phone: digits only (allow dashes and spaces)
  - Email: must contain `@` and `.`
- Keeps asking until valid input is provided
- Stores contacts in a list and displays them at the end
"""
class ContactError(Exception):
    pass

# Custom Exception class to handle invalid name
class InvalidNameError(ContactError):
    def __init__(self, name):
        self.name = name
        super().__init__(f"Name cannot be empty!")

# Custom Exception class to handle invalid numbers
class InvalidPhoneError(ContactError):
    def __init__(self, phone):
        self.phone = phone
        super().__init__(f"Phone number doesn't contain these {phone} characters!")

# Custom Exception class to handle invalid email
class InvalidEmailError(ContactError):
    def __init__(self, email):
        self.email = email
        super().__init__(f"{email} has wrong format!")

class ContactManager:
    # A constructor to initialize data
    def __init__(self, contacts=None):
        self.contacts = contacts if contacts else []

    # Validating Name
    def validate_name(self, name):
        if name.strip() == "":
            raise InvalidNameError(name)
        return name

    # Validating Phone Numbers
    def validate_phone(self, phone):
        phone_clean = phone.replace("-", "").replace(" ", "")
        if not phone_clean.isdigit():
            raise InvalidPhoneError(phone)
        return phone_clean

    # Validating Email Adress
    def validate_email(self, email):
        if "@" not in email or "." not in email:
            raise InvalidEmailError(email)
        return email

    # Adding Contacts
    def add_contacts(self, name, phone, email):
        try:
            self.person_name = self.validate_name(name)
            self.person_phone = self.validate_phone(phone)
            self.person_email = self.validate_email(email)
        except ContactError as e:
            raise 
        else:
            self.contacts.append({"name": self.person_name, "phone": self.person_phone, "email": self.person_email})

    # Displaying Contacts
    def display_contacts(self):
        for i, contact in enumerate(self.contacts, start=1):
            print(f"{i}. {contact}")

if __name__ == "__main__":
    cm = ContactManager()
    while True:
        try:
            name = input("Enter the contact person name: ")
            phone = input("Enter the contact person number: ")
            email = input("Enter the contact person email: ")
            cm.add_contacts(name, phone, email)
        except ContactError as e:
            print(f"Error: {type(e).__name__}")
            print(f"Error message: {e}")
        else:
            cm.display_contacts()
            another = input("Add another contact? (y/n): ").lower()
            if another != 'y':
                print("Closing Program ......")
                break
        
