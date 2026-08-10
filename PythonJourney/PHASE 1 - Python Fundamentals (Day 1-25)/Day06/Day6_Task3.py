"""
### Assignment 3: Simple Loop Menu
Write a program that shows a menu and repeats until the user types `quit`.
- Use `while True`.
- Use `break` to exit.
- Use `pass` as a placeholder for unsupported options.
"""

print("/n --- Simple Menu Loop --- \n")
while True:
    print("--- Simple Menu ---")
    print("\n1. Table of Contents")
    print("\n2. Acknowledgement")
    print("\n3. Authors")
    print("\n4. Publishers")

    user_input = input("Enter 'quit' to exit the loop: ").strip()
    if user_input.lower() == "quit":
        break
    else:
        pass
print("\n --- Exiting The Loop ---")    