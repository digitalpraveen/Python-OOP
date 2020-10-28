class User:

    def __init__(self,name,deposit,costperday):
        self.name=name
        self.deposit=deposit
        self.costperday=costperday


    def display(self):
        print("Name:%s"%self.name)
        print("Deposite:%2d"%self.deposit)
        print("Cost per day:%2d"%self.costperday)


