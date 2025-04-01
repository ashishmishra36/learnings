class Account:
#As an added requirement, withdrawals may not exceed the available balance.
# Instantiate your class, make several deposits and withdrawals, and test to make sure the
# account can't be overdrawn.

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        print(f'Account owner:  {owner}')
        print(f'Account balance:  ${balance}')


    def deposit(self, d):
        self.balance = self.balance + d
        print('Deposit Accepted')


    def withdraw(self, wd):
        if wd<self.balance:
            self.balance = self.balance - wd
        else:
            print('Funds Unavailable!')


# 1. Instantiate the class
acct1 = Account('Jose', 100)
print(acct1.owner)
print(acct1.balance)

# 5. Make a series of deposits and withdrawals
acct1.deposit(50)

#6. withdraw
acct1.withdraw(75)

# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)

print(acct1.balance)