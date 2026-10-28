# Custom exception InsufficientBalanceError
class InsufficientBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient balance")
        self.balance -= amount
        print("Withdrew", amount, "Remaining:", self.balance)

acc = BankAccount(100)
try:
    acc.withdraw(150)
except InsufficientBalanceError as e:
    print("Error:", e)
acc.withdraw(40)
