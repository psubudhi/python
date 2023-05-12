class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance.")

# Test the class
account = BankAccount(1000)
print(account.balance)  # Output: 1000
account.deposit(500)
print(account.balance)  # Output: 1500
account.withdraw(200)
print(account.balance)  # Output: 1300
account.withdraw(1500)  # Output: Insufficient balance.