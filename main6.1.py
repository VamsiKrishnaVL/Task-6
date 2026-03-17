# Problem 1: Bank Account
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self._balance = balance  # encapsulation

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self._balance


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self._balance * self.interest_rate / 100


class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance, min_balance):
        super().__init__(account_number, balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if self._balance - amount >= self.min_balance:
            self._balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Cannot withdraw: Minimum balance requirement not met")


