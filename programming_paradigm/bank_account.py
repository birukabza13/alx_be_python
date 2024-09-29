class BankAccount:


    def __init__(self, account_balance = 0) -> None:
        self.account_balance = account_balance
    

    def deposit(self, amount):
        self.account_balance+=amount
        print(f"Deposited: ${amount}")
    
    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient funds.")
            return False
        self.account_balance-=amount
        print(f"Withdrew: ${amount: .1f}")
        return True

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance: .2f}")