# Question: Create a class BankAccount with a private attribute _balance. Add methods deposit(amount) and withdraw(amount). Make sure that withdrawals don’t allow the balance to go below zero.
while True:
    class BankAccount:
        def __init__(self, balance=0):
            self._balance = balance

        def deposit(self, amount):
            if amount > 0:
                self._balance += amount
            else:
                print("Deposit amount must be positive")

        def withdraw(self, amount):
            if 0 < amount <= self._balance:
                self._balance -= amount
            else:
                print("Insufficient funds or invalid amount")

        def get_balance(self):
            return self._balance

# Test
    account = BankAccount()
    account.deposit(int(input("enter a number for deposit ammount :- ")))
    account.withdraw(int(input("enter a value to withdraw ammount :- ")))  # Outputs: "Insufficient funds or invalid amount"
    account.withdraw(int(input("enter again value to deposit amount again :- ")))   
    print(account.get_balance())  # Outputs: 120
