# Problem 1: Bank Account System
# -------------------------------

class BankAccount:
    """Base class for bank account"""

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance  # encapsulated (private variable)

    def deposit(self, amount):
        """Method to deposit money"""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        """Method to withdraw money"""
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        """Getter method for balance"""
        return self.__balance


class SavingsAccount(BankAccount):
    """Savings account with interest"""

    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        """Calculate interest on current balance"""
        interest = self.get_balance() * self.interest_rate / 100
        return interest


class CurrentAccount(BankAccount):
    """Current account with minimum balance requirement"""

    def __init__(self, account_number, balance, min_balance):
        super().__init__(account_number, balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        """Override withdraw to maintain minimum balance"""
        if self.get_balance() - amount >= self.min_balance:
            super().withdraw(amount)
        else:
            print("Cannot withdraw: Minimum balance requirement not maintained")


# ----------- Testing -----------
print("\n--- Bank Account Test ---")

savings = SavingsAccount("SA123", 10000, 5)
savings.deposit(2000)
print("Interest:", savings.calculate_interest())

current = CurrentAccount("CA456", 15000, 5000)
current.withdraw(12000)  # should fail
current.withdraw(8000)   # should pass
