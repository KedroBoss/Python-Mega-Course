class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        if ammount <= account.balance:
            self.balance -= amount
        else:
            print('No')

    def deposit(self, amount):
        self.balance +=amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))




class Checking(Account):
    """Doc String: Generates Checking account"""
    type = 'Checking' # Class Variable

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance=self.balance - amount - self.fee

checking_acc = Checking('balance.txt', 1)
print(checking_acc.balance)
checking_acc.deposit(100)
print(checking_acc.balance)
checking_acc.commit()
print(checking_acc.type)

print(checking_acc.__doc__)
