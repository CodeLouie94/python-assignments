class BankAccount:
    all_accts = []

    def __init__(self, name, int_rate, balance):
        self.name = name
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
        print(f"{self.name}  Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

    def transfer_moolah(self, name, transfer_amount, transferee):
        # print(f"{transfer_amount}$ transferred")
        self.balance -= transfer_amount
        transferee.balance += transfer_amount
        return self
        
        

    # @classmethod
    # def print_all_accts_info(cls):
    #     for acct in cls.all_accts:
    #         acct.display_account_info()


class User:
    def __init__(self, name):
        self.name = name
        self.account = {
            'Checking' : BankAccount(self.name, int_rate=.02, balance=0),
            'Savings' : BankAccount(self.name, int_rate=.02, balance=0)
        }
    # def make_deposit(self):
    #     self.account.deposit()
    #     return self
    # def make_withdrawal(self):
    #     self.account.withdraw()
    #     return self
    # def display_user_balance(self):
    #     print(f"{self.name} - balance: {self.account}")
    #     return self
    # def transfer_money(self, name, amount):
    #     self.account -= amount
    #     name.account += amount
    #     print(f"{self.name} transferred {amount}$ to {name.name}'s account")
    #     return self

michael = User("Michael")

michael.account['Savings'].deposit(100)
michael.account['Savings'].withdraw(50) 
michael.account['Savings'].transfer_moolah(michael.name, 10, michael.account['Checking'])
michael.account['Savings'].display_account_info()
michael.account['Checking'].display_account_info()





# self_account = {'Checking' : 'fdas' , 'Savings' : 'asdf'}
# print(self_account[1][1])