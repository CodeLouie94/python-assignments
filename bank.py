class BankAccount:
    all_accts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

    @classmethod
    def print_all_accts_info(cls):
        for acct in cls.all_accts:
            acct.display_account_info()


account1 = BankAccount(0.07, 0)
account2 = BankAccount(0.05, 400)

account1.deposit(100).deposit(50).deposit(25).withdraw(
    150
).yield_interest().display_account_info()

account2.deposit(666).deposit(150).withdraw(99).withdraw(
    50
).yield_interest().display_account_info()

BankAccount.print_all_accts_info()
# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
