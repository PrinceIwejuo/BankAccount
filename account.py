class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        self.int_rate = 0.01

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        self.int_rate
        return self

checking = BankAccount(0.01, 5000 )
saving = BankAccount(0.08, 25000 )

checking.deposit(200).deposit(150).deposit(300).withdraw(100).yield_interest().display_account_info()

saving.deposit(5000).deposit(2000).withdraw(100).withdraw(100).withdraw(200).withdraw(400).yield_interest().display_account_info()
