class BankAccount (object):
    accounts = {}

    def __init__(self, name):
        self.name = name
        BankAccount.accounts[self.name] = 0

    def deposit(self, amount):
        BankAccount.accounts[self.name] += amount
        print(f'{amount} SAR has been deposited to your bank balance on Thursday, June 10, 2021, at 4:45am')

    def withdraw(self, amount):
        BankAccount.accounts[self.name] -= amount
        print(f'{amount} SAR were deducted from your bank balance on Tuesday, February 9, 2021, at 9:15pm')

    def transfer(self, receiver, amount):
        self.withdraw(amount)
        receiver.deposit(amount)


account1 = BankAccount('Faisal')
account2 = BankAccount('Marwan')
account3 = BankAccount('Ftoon')

print(BankAccount.accounts)

account1.deposit(500)
account2.deposit(1400)
account3.deposit(1700)
print(BankAccount.accounts)

account1.withdraw(200)
account2.withdraw(700)
account3.withdraw(1000)
print(BankAccount.accounts)

account1.transfer(account2, 250)
print(BankAccount.accounts)