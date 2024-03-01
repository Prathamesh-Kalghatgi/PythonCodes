from random import random
class BankAccount:
    def newaccount(self):
        Name = str(input("Enter your Name:"))
        self.Name =Name
        Contact_Number = int(input("Enter your contact number:"))
        self.Contact_Number
        Account_Number = (random)
        print("The Account Number is:",random())

    def __init__(self):
        self.balance = 0
        print("Hello! Welcome to the Deposit & Withdrawal Machine")

    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        self.balance += amount
        print("\nAmount Deposited:", amount)

    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\nYou Withdrew:", amount)
        else:
            print("\nInsufficient balance")

    def display(self):
        print("\nNet Available Balance =", self.balance)

# Create an object and execute the program
s = BankAccount()
s.newaccount()
s.deposit()
s.withdraw()
s.display()
