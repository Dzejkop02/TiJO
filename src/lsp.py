# Naruszona zasada LSP

class BankAccount:
    def __init__(self, min_balance=0):
        self._balance = 0
        self._min_balance = min_balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance - amount >= self._min_balance:
            self._balance -= amount
        else:
            raise Exception(f"Cannot withdraw: balance cannot go below {self._min_balance}")

    def get_balance(self):
        return self._balance


class SavingsAccount(BankAccount):
    def __init__(self):
        super().__init__(min_balance=100)


def perform_transaction(account: BankAccount, deposit_amount, withdraw_amount):
    account.deposit(deposit_amount)
    account.withdraw(withdraw_amount)
    print(f"Balance after transaction: {account.get_balance()}")


# Usage
regular_account = BankAccount()
savings_account = SavingsAccount()

perform_transaction(regular_account, 500, 200)  # Works
perform_transaction(savings_account, 500, 450)  # Exception!
