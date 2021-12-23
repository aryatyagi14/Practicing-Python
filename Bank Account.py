class BankAccount:
    def __init__(self, name, accountNumber,totalBalance):
        self.name = name
        self.an = accountNumber
        self.tb = totalBalance
        print(self.name, self.an, self.tb)

    def deposit(self, amountD):
        self.amountD = amountD
        self.tb += self.amountD

    def withdraw(self, amountW):
        self.amountW = amountW
        if(self.tb - amountW >= 0):
            self.tb -= amountW
        else:
            print("insufficient funds")

    def printBalance(self):
        print(self.tb)

arya = BankAccount("Arya", 1, 100)
arya.deposit(100)
arya.printBalance()
arya.withdraw(300)
arya.printBalance()
    
