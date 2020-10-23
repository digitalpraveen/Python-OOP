class Hall:
    def __init__(self,name,cosrperday,ownerName):
        self.name=name
        self.costperday=cosrperday
        self.ownername=ownerName

    # Fill your code here

    def display(self):
        print("Owner Name : ",self.ownername)
        print("Hall :",self.name)
        print("Costperday : ",self.costperday)