# Q3. Create a class BankAccount with methods to deposit and withdraw money and a method to display balance.
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def display_balance(self):
        print(f"Balance: {self.balance}")

account = BankAccount()
account.deposit(45)
account.withdraw(50)
account.display_balance()
