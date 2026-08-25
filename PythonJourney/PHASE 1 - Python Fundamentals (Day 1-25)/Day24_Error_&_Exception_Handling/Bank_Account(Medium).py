"""
### Assignment 3: Custom Exception Hierarchy (Medium)

Build a mini **Bank Account** system with:
- Custom exceptions: `BankError`, `InsufficientFundsError`, `InvalidAmountError`
- `BankAccount` class with `deposit()`, `withdraw()`, `get_balance()`
- `withdraw()` raises `InsufficientFundsError` with balance & requested amount
- Demo script that catches and prints user-friendly messages
"""

# Main (Base) for Custom Exceptions
class BankError(Exception):
    pass

# Custom Exception Inherited from Base Exception
class InsufficientFundsError(BankError):
    # A consructor that runs when exception is created
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.deficitamount = amount - balance
        super().__init__(
            f"Cannot withdraw {amount}. The balance is: {balance}. "
            f"Deficit by: {self.deficitamount}"
        )

# Custom Exception Inherited from Base Exception
class InvalidAmountError(BankError):
    def __init__(self, amount):
        self.amount = amount
        super().__init__(f"Invalid amount: {amount}, Amount can't be negative.")


# Blueprint holding data and validation together. Without it you have to write validation everytime 
class BankAccount:
    # Setting Starting Balance
    def __init__(self, balance=0): 
        self.balance = balance

    # Validating Amount and adding to Balance    
    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError(amount)
        self.balance += amount
        return self.balance

    # Validating Amount and withdrawing
    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError(amount)
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

    # Getting current Balance
    def get_balance(self):
        return self.balance


if __name__ == "__main__":
    # Instantiating an object with balance = 1000
    account = BankAccount(1000)
    print(f"Account created with balance: {account.get_balance()}")

    print("\n--- Test 1: Valid Deposit ---")
    try:
        account.deposit(500)
    except BankError as e:
        print(f"Error: {e}")
    else:
        print(f"Deposit successful! New balance: {account.get_balance()}")
    finally:
        print("Transaction recorded.\n")

    print("--- Test 2: Valid Withdrawal ---")
    try:
        account.withdraw(300)
    except BankError as e:
        print(f"Error: {e}")
    else:
        print(f"Withdrawal successful! New balance: {account.get_balance()}")
    finally:
        print("Transaction recorded.\n")

    print("--- Test 3: Insufficient Funds ---")
    try:
        account.withdraw(5000)
    except InsufficientFundsError as e:
        print(f"Error: {e}")
        print(f"You need {e.deficitamount} more.") # 'e' is instant of 'InsufficientFundsError' that sotres deficitamount
    else:
        print(f"Withdrawal successful! New balance: {account.get_balance()}")
    finally:
        print("Transaction recorded.\n")

    print("--- Test 4: Negative Deposit ---")
    try:
        account.deposit(-100)
    except InvalidAmountError as e:
        print(f"Error: {e}")
    else:
        print(f"Deposit successful! New balance: {account.get_balance()}")
    finally:
        print("Transaction recorded.\n")

    print("--- Test 5: Negative Withdrawal ---")
    try:
        account.withdraw(-50)
    except InvalidAmountError as e:
        print(f"Error: {e}")
    else:
        print(f"Withdrawal successful! New balance: {account.get_balance()}")
    finally:
        print("Transaction recorded.\n")

    print(f"Final balance: {account.get_balance()}")
        