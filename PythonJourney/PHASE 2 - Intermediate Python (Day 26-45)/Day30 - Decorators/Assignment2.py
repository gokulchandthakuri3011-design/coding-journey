"""
### Assignment 2: Login Authentication Simulator

Create a decorator named `require_authentication`.

Requirements:

1. Accept a function that requires authentication.
2. Check whether the username and password are correct.
3. Call the original function only when authentication succeeds.
4. Return an access-denied message when authentication fails.
5. Preserve the original function's metadata.
6. Test the decorator with a `view_dashboard(username, password)` function.

Questions:

- What happens when authentication fails?
-> The protected functin is not called.

- Why should the protected function not run after failed authentication?
-> To protect and prevent from unauthorized access, as the fuction might have some private or imp data

- How could a real application replace hard-coded credentials?
-> Real appliction stores users data securely.
"""

from functools import wraps


# Creating Decorator
def require_authentication(function):
    valid_username = "Songoku"
    valid_password = "UltraInstinct8"

    @wraps(function)
    def wrapper(username, password, *args, **kwargs):
        if username == valid_username and password == valid_password:
            return function(username, password, *args, **kwargs)
        return "Access Denied! Wrong Entry!"

    return wrapper


@require_authentication
def view_dashboard(username, password):
    return f"Welcome {username}! You are logged in."


def main():
    username = input("Enter correct User Id: ")
    password = input("Enter the correct Password: ")
    print(view_dashboard(username, password))


if __name__ == "__main__":
    print("-- Validating User Id & Password --\n")
    main()