
from abc import ABCMeta
class Event(metaclass=ABCMeta):

    def calTotalSpent(self):
        pass

    def calTotalRevenue(self):
        pass

    def profitOrLoss(self):
        pass


class Exhibition(Event):
    def __init__(self,noofstalls,costperstall,noofentries,costperentry):
        self.noofstalls=noofstalls
        self.costperstall=costperstall
        self.noofentries=noofentries
        self.costperentry=costperentry

    def calTotalSpent(self):
        p=self.noofstalls*self.costperstall
        return p

    def calTotalRevenue(self):
        s=self.noofentries*self.costperentry
        return s

    def profitOrLoss(self):
        if self.noofstalls*self.costperstall > self.noofentries*self.costperentry:
            print("LOSS")
        elif self.noofstalls*self.costperstall < self.noofentries*self.costperentry:
            print("PROFIT")
        elif self.noofstalls*self.costperstall == self.noofentries*self.costperentry:
            print("NO PROFIT NO LOSS")

    def display(self):
        print("Number of stall is ",self.noofstalls)
        print("Total cost spent is",self.noofstalls*self.costperstall)
        print("Total revenue is",self.noofentries*self.costperentry)


class StageEvent(Event):
    def __init__(self ,noofevents,costperevent,noofentries,costperentry,sum):
        self.noofevents = noofevents
        self.costperevent =costperevent
        self.noofentries = noofentries
        self.costperday = costperentry
        self.sum=sum
    def calTotalSpent(self):
        return self.noofevents*self.costperevent

    def calTotalRevenue(self):
        return self.noofentries*self.costperday

    def profitOrLoss(self):
        if self.noofevents*self.costperevent > self.noofentries*self.costperday:
            print("LOSS")
        elif self.noofevents*self.costperevent < self.noofentries*self.costperday:
            print("PROFIT")
        elif self.noofevents*self.costperevent == self.noofentries*self.costperday:
            print("NO PROFIT NO LOSS")

    def display(self):
        print("Number of stall is ", self.noofevents)
        print("Total cost spent is", self.noofevents * self.costperevent)
        print("Total revenue is", self.sum)


# Main
print("Menu\n1.Exhibition\n2.stage Event\n")
n=int(input(""))
if n==1:
    num = int(input("Enter number of stalls\n"))
    cost = float(input("Enter cost per stalls\n"))
    entries = int(input("Enter number of entries to exhibition\n"))
    fee=float(input("Enter the entry fee\n"))
    exhi=Exhibition(num,cost,entries,fee)
    exhi.display()
    exhi.profitOrLoss()
elif n==2:
    s=int(input("Enter number of Events\n"))
    cost = float(input("Enter cost per events\n"))
    sum=0
    for i in range(s):
        print("Enter number of entries for {} event".format(i+1))
        entries=int(input(""))
        fee= float(input("Enter the entry fee\n"))
        sum+=entries*fee
    stage=StageEvent(s,cost,entries,fee,sum)
    stage.display()
    stage.profitOrLoss()

