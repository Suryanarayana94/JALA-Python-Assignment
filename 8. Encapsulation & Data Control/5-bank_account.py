# Bank account system
class BankAccount:
    def __init__(self, holder, balance=0):
        self.account_holder = holder
        self.balance = balance if balance >= 0 else 0
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited", amount, "New balance:", self.balance)
        else:
            print("Deposit amount must be positive")
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
        elif amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print("Withdrew", amount, "New balance:", self.balance)

acc = BankAccount("Alice", 100)
acc.deposit(50)
acc.withdraw(30)
acc.withdraw(200)
acc.deposit(-10)
