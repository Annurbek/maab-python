class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Insufficient funds.")

    def view_account(self):
        return f"Account Number: {self.account_number}, Name: {self.name}, Balance: {self.balance}"


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, initial_deposit):
        account_number = len(self.accounts) + 1
        account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = account
        return account

    def get_account(self, account_number):
        return self.accounts.get(account_number)

bank = Bank()

acc1 = bank.create_account("Annurbek", 1000)
print(acc1.view_account())
acc1.deposit(500)
acc1.withdraw(200)
acc1.withdraw(2000)
