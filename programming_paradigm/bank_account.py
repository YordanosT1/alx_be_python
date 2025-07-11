#Task 0. Create a Simple Bank Account Class
#create class
class  BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance #atribute defined
    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False
        
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")

