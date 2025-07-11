# =========================
# task 1: Model a Farm
# =========================

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        return f"{self.name} is sleeping."

    def eat(self):
        return f"{self.name} is eating."

class Dog(Animal):
    def bark(self):
        return f"{self.name} says Woof!"

class Fish(Animal):
    def swim(self):
        return f"{self.name} is swimming."

class Bird(Animal):
    def fly(self):
        return f"{self.name} is flying."

class Monkey(Animal):
    def climb(self):
        return f"{self.name} is climbing."

def farm_demo():
    dog = Dog("Buddy", 3)
    fish = Fish("Nemo", 1)
    bird = Bird("Kiwi", 2)
    monkey = Monkey("George", 5)

    print(dog.eat())
    print(dog.bark())
    print(fish.sleep())
    print(fish.swim())
    print(bird.fly())
    print(monkey.climb())

# =========================
# task 2: Build a Bank Application
# =========================

import os

class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = int(account_number)
        self.name = name
        self.balance = float(balance)

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

    def to_line(self):
        return f"{self.account_number},{self.name},{self.balance}\n"

    @staticmethod
    def from_line(line):
        parts = line.strip().split(",")
        return Account(parts[0], parts[1], parts[2])

class Bank:
    def __init__(self, filename="accounts.txt"):
        self.accounts = {}
        self.filename = filename
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        account_number = self._generate_account_number()
        account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = account
        self.save_to_file()
        print("Account created successfully!")
        print(account.view_account())
        return account

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(account.view_account())
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
            self.save_to_file()
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.withdraw(amount)
            self.save_to_file()
        else:
            print("Account not found.")

    def save_to_file(self):
        with open(self.filename, "w") as f:
            for acc in self.accounts.values():
                f.write(acc.to_line())

    def load_from_file(self):
        if not os.path.exists(self.filename):
            return
        with open(self.filename, "r") as f:
            for line in f:
                acc = Account.from_line(line)
                self.accounts[acc.account_number] = acc

    def _generate_account_number(self):
        if not self.accounts:
            return 1
        return max(self.accounts.keys()) + 1

    def menu(self):
        while True:
            print("\nWelcome to the Bank Application!")
            print("1. Create account")
            print("2. View account")
            print("3. Deposit")
            print("4. Withdraw")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                name = input("Enter your name: ")
                try:
                    deposit = float(input("Enter initial deposit: "))
                except ValueError:
                    print("Invalid amount.")
                    continue
                self.create_account(name, deposit)
            elif choice == "2":
                try:
                    acc_num = int(input("Enter account number: "))
                except ValueError:
                    print("Invalid account number.")
                    continue
                self.view_account(acc_num)
            elif choice == "3":
                try:
                    acc_num = int(input("Enter account number: "))
                    amount = float(input("Enter deposit amount: "))
                except ValueError:
                    print("Invalid input.")
                    continue
                self.deposit(acc_num, amount)
            elif choice == "4":
                try:
                    acc_num = int(input("Enter account number: "))
                    amount = float(input("Enter withdrawal amount: "))
                except ValueError:
                    print("Invalid input.")
                    continue
                self.withdraw(acc_num, amount)
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# =========================
# Main menu for all tasks
# =========================

def main():
    while True:
        print("\nSelect a task to run:")
        print("1. Farm demo")
        print("2. Bank Application")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            farm_demo()
        elif choice == "2":
            bank = Bank()
            bank.menu()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
