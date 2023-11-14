class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def calculate_interest(self):
        pass

class SavingsAccount(Account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def calculate_interest(self):
        interest_rate = 0.1
        interest = self.balance * interest_rate
        self.balance += interest

class CheckingAccount(Account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def calculate_interest(self):
        interest_rate = 0.5
        interest = self.balance * interest_rate
        self.balance += interest

def main():
    accounts = [SavingsAccount(1, 100), CheckingAccount(2, 200)]
    for account in accounts:
        account.deposit(100)
        account.calculate_interest()
        print(account.balance)
        account.withdraw(300)
        print(account.balance)
if __name__ == "__main__":
    main()