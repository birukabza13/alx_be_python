class BankAccount:


    def __init__(self, account_balance = 0) -> None:
        self.account_balance = account_balance
    

    def deposit(self, amount):
        self.account_balance+=amount
    
    def withdraw(self, amount):
        if amount > self.account_balance:
            return False
        self.account_balance-=amount
        return False

    def display(self):
        print(f"Current Balance: {self.account_balance}")