from abc import *
from random import *
import datetime
import sys
#exit()
#Banking Application


class Bank:
    history=[]
    @staticmethod
    def createAccountNumber():
        Account_No="3366"
        for i in range(8):
           Account_No=Account_No+str(randint(0,7))
        return Account_No

    @classmethod
    def addEntry(cls,msg):
        Bank.history.append(msg)

    @staticmethod
    def displayHistory():
        for i in Bank.history:
            print(i)
            print("#"*40)

class Account(ABC):
    @abstractmethod
    def accountBalance(self):
        pass


class SavingsAccount(Account):
    def __init__(self,name,balance,minimum_balance):
        self.account_number=Bank.createAccountNumber()
        self.name=name
        self.balance=balance
        self.minimum_balance=minimum_balance

    def accountBalance(self):
        print("The Account Balance of {} is {}".format(self.name,self.balance))

    def depositAmount(self):
        amount=int(input("Enter the amount to deposit:"))
        if amount<0:
            print("Please enter a valid amount")
            sys.exit()
        else:
            self.balance=self.balance+amount
        Bank.addEntry("The amount of RS.{} is credited to your Bank Account No {}".format(amount,self.account_number))

        print("The total balance in my Account {} is {}".format(self.account_number,self.balance))

    def withdraw(self):
        amount = int(input("Enter the amount to withdraw:"))  # 2000
        if amount < 0:
            print("Please enter a valid amount")
            sys.exit()
        else:
            self.balance = self.balance - amount
        Bank.addEntry("The amount of RS.{} is debited to your Bank Account No {}".format(amount, self.account_number))

        print("The total balance in my Account {} is {}".format(self.account_number, self.balance))


    def getAccountInfo(self):
        print("Account No",self.account_number)
        print("Account Holder Name:",self.name)
        print("Account Balance",self.balance)


class CurrentAccount(Account):
    def __init__(self,name,balance,minimum_balance):
        self.account_number=Bank.createAccountNumber()
        self.name=name
        self.balance=balance
        self.minimum_balance=minimum_balance

    def accountBalance(self):
        print("The Account Balance of {} is {}".format(self.name, self.balance))

    def depositAmount(self):
        amount = int(input("Enter the amount to deposit:"))
        if amount < 0:
            print("Please enter a valid amount")
            sys.exit()
        else:
            self.balance = self.balance + amount
        Bank.addEntry("The amount of RS.{} is credited to your Bank Account No {}".format(amount, self.account_number))

        print("The total balance in my Account {} is {}".format(self.account_number, self.balance))

    def withdraw(self):
        amount = int(input("Enter the amount to withdraw:"))  # 2000
        if amount < 0:
            print("Please enter a valid amount")
            sys.exit()
        else:
            self.balance = self.balance - amount
        Bank.addEntry("The amount of RS.{} is debited to your Bank Account No {}".format(amount, self.account_number))

        print("The total balance in my Account {} is {}".format(self.account_number, self.balance))

    def getAccountInfo(self):
        print("Account No", self.account_number)
        print("Account Holder Name:", self.name)
        print("Account Balance", self.balance)

print("**!!**!!**!!**!!Welcome to RAISING BANK!!**!!**!!**!!**")
print("s-Savings Account\nc-Current Account")
option=input("Do you want to create a Savings Account or Current Account,please type s to create Savings"
      "Account and c to create Current Account:").lower()


while option not in ['s','c']:
    option=input("Please enter the proper option i.e either s or c")

if option=="s":
    ename=input("Enter the Customer Name:")
    ebalance=int(input("Enter the Balance:"))
    s=SavingsAccount(ename,ebalance,500)
    print("Savings Account with A/C no {} having the customer name {} is created successfully on {}".format(s.account_number,s.name,datetime.datetime.now()))
    while True:
        print("b-Balance\nd-Deposit\nw-Withdraw\nm-Mini Statement\ni-Account Information")
        option=input("Please select any of the above options:")
        if option=="b":
            s.accountBalance()
        elif option=="d":
            s.depositAmount()
        elif option=="w":
            s.withdraw()
        elif option=="i":
            s.getAccountInfo()
        elif option=="m":
            Bank.displayHistory()
        else:
            sys.exit()
    s.exit()
elif option=="c":
    ename = input("Enter the Company Name:")
    ebalance = int(input("Enter the Balance:"))
    c = CurrentAccount(ename, ebalance, 10000)
    print("Current Account with A/C no {} having the customer name {} is created successfully on {}".format(
    c.account_number, c.name, datetime.datetime.now()))

    while True:
        print("b-Balance\nd-Deposit\nw-Withdraw\nm-Mini Statement\ni-Account Information")
        option=input("Please select any of the above options:")
        if option=="b":
            c.accountBalance()
        elif option=="d":
            c.depositAmount()
        elif option=="w":
            c.withdraw()
        elif option=="i":
            c.getAccountInfo()
        elif option=="m":
            Bank.displayHistory()
        else:
            sys.exit()








































































