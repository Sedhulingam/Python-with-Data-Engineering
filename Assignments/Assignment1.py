'''
Assignment -1 - Python. Submission date: 2nd Sep , push code in github and with screen shot  outputs

Assignment: Bank Account System (OOP in Python)
Problem Statement
You are required to build a Python program that simulates a Bank Account system using Object-Oriented Programming (OOP) concepts. The system should support different types of bank accounts and their basic operations.
Requirements

Create a base class BankAccount:
Attributes:
    account_number
    account_holder
    balance (default 0.0)
Methods:
    deposit(amount) → adds money to the account.
    withdraw(amount) → deducts money if sufficient balance is available.
    get_balance() → returns the current balance.
    __str__() → return account details in string format.
Create a subclass SavingsAccount (inherits BankAccount):
Extra Attribute:
    interest_rate
Extra Method:
    apply_interest() → increases balance based on interest rate.

Create another subclass CurrentAccount (inherits BankAccount):
Extra Attribute:
    overdraft_limit
Modify withdraw(amount) so that account holders can withdraw beyond their balance up to the overdraft limit.
Create a test program that:
Creates one savings account and one current account.
Performs deposit, withdrawal, and balance checks.
Demonstrates apply_interest() on savings.
Demonstrates overdraft facility on current account.

Tasks for You
Implement the code above.
Add exception handling (e.g., negative deposits or withdrawals).
Extend the system by adding another account type (e.g., Fixed Deposit Account with lock-in period).
Allow multiple accounts in a Bank class and implement transfer_funds() between two accounts
'''
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

class BankAccount:
    def __init__(self, name, actno, balance=0.0):
        self.name = name
        self.actno = actno
        self.balance = balance

    def get_balance(self):
        print(f"\nName    = {self.name}")
        print(f"Act No  = {self.actno}")
        print(f"Balance = {self.balance}")

    def deposit(self, amount):
        try:
            if amount <= 0:
                raise ValueError("\nDeposit amount must be positive.")
            self.balance += amount
        except ValueError as e:
            print(e)

    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive.")
            if self.balance >= amount:
                self.balance -= amount
            else:
                raise ValueError("Insufficient balance.")
        except ValueError as e:
            print(e)

    # def __str__(self):
    #     return (f"Account Type: BankAccount\n"
    #             f"Account Holder: {self.name}\n"
    #             f"Account Number: {self.actno}\n"
    #             f"Balance: {self.balance:.2f}")

class SavingsAccount(BankAccount):
    def __init__(self, name, actno, balance=0.0, interest_rate=0.05):
        super().__init__(name, actno, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest of {interest:.2f} added.")
        

    def __str__(self):
        return (f"Account Type: SavingsAccount\n"
                f"Account Holder: {self.name}\n"
                f"Account Number: {self.actno}\n"
                f"Interest Rate: {self.interest_rate*100:.2f}%\n"
                f"Balance: {self.balance:.2f}")
                

class CurrentAccount(BankAccount):
    def __init__(self, name, actno, balance=0.0, overdraft_limit=1000):
        super().__init__(name, actno, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive.")
            if self.balance + self.overdraft_limit >= amount:
                self.balance -= amount
            else:
                raise ValueError("Exceeded overdraft limit.\n")
        except ValueError as e:
            print(e)

    def __str__(self):
        return (f"Account Type: CurrentAccount\n"
                f"Account Holder: {self.name}\n"
                f"Account Number: {self.actno}\n"
                f"Balance: {self.balance:.2f}\n"
                f"Overdraft Limit: {self.overdraft_limit:.2f}")

class FixedDepositAccount(BankAccount):
    def __init__(self, name, actno, balance=0.0, lock_in_month=12):
        super().__init__(name, actno, balance)
        self.start_date = datetime.now()
        self.lock_in_period = relativedelta(months=lock_in_month)

    def withdraw(self, amount):
        try:
            maturity_date = self.start_date + self.lock_in_period
            if datetime.now() < maturity_date:
                raise Exception(f"Cannot withdraw before lock-in period ends on {maturity_date.strftime('%Y-%m-%d')}.")
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive.")
            super().withdraw(amount)
        except Exception as e:
            print(e)

    def __str__(self):
        lock_in_end_date = self.start_date + self.lock_in_period
        return (f"Account Type: FixedDepositAccount\n"
                f"Account Holder: {self.name}\n"
                f"Account Number: {self.actno}\n"
                f"Balance: {self.balance:.2f}\n"
                f"Lock-in Period (Months): {self.lock_in_period.months}\n"
                f"Start Date: {self.start_date.strftime('%Y-%m-%d')}\n"
                f"Maturity Date: {lock_in_end_date.strftime('%Y-%m-%d')}")

# ---- Savings Account ----
print("\n")
print("---- Savings Account ----")
s1 = SavingsAccount("Alice", 101, 5000)
print(s1)
s1.deposit(1000)
print("\n")
print(s1)
s1.withdraw(2000)
print("\n")
print(s1)
print("Total Interest Added to the Current Balance Calculation: ")
s1.apply_interest()

print("\n")
print(s1)
print("\n")
s1.deposit(-500)
print("\n")   
s1.withdraw(-1000)  
print("\n")

# ---- Current Account ----
print("---- Current Account ----")
c1 = CurrentAccount("Bob", 102, 3000)
print(c1)
print("\n")
c1.withdraw(3500)     
print(c1)
print("\n")
c1.withdraw(1000)     
print(c1)
c1.deposit(-500)     
print("\n")

# ---- Fixed Deposit Account ----
print("\n---- Fixed Deposit Account ----")
fd1 = FixedDepositAccount("Charlie", 103, 10000, lock_in_month=1)
print(fd1)
print("\n")
fd1.withdraw(5000)   
print("\n")
print(fd1)

print("\n")


