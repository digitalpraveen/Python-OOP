from abc import ABCMeta, abstractmethod


class AbstractStall():
    @abstractmethod
    def display(self):
        pass

class Stall(AbstractStall):
    def __init__(self,name,details,cost,ownername):
        self.__name=name
        self.__details=details
        self.__cost=cost
        self.__owner=ownername
    def display(self):
        print("Stall name:%s"%self.__name)
        print("Details:%s"%self.__details)
        print("Cost:%.2f"%self.__cost)
        print("Owner:%s"%self.__owner)


class ExecutiveStall(AbstractStall):
    def __init__(self,name,detail,cost,owner,tv):
        self.__name=name
        self.__detail=detail
        self.__cost=cost
        self.__owner=owner
        self.__tv=tv
    def display(self):
        print("Stall name:", self.__name)
        print("Details:", self.__detail)
        print("Cost:%.2f"%self.__cost)
        print("Owner:", self.__owner)
        print("Number of TV set:",self.__tv)


# fill your code

class PremiumStall(AbstractStall):
    def __init__(self,name,detail,cost,owner,projector):
        self.__name=name
        self.__detail=detail
        self.__cost=cost
        self.__owner=owner
        self.__projector=projector

    def display(self):
        print("Stall name:", self.__name)
        print("Details:", self.__detail)
        print("Cost:%.2f"%self.__cost)
        print("Owner:", self.__owner)
        print("Number of Projector:", self.__projector)


# fill your code

# Main
print("Stall Type")
print("1.Stall")
print("2.Executive Stall")
print("3.Premium Stall")
ch = int(input(""))
if ch==1:
    name = input("Enter the Stall name\n")
    detail = input("Enter the details\n")
    cost = float(input("Enter the cost\n"))
    owner = input("Enter the Owner name\n")
    stall=Stall(name,detail,cost,owner)
    stall.display()
elif ch==2:# fill your code
    name = input("Enter the Stall name\n")
    detail = input("Enter the details\n")
    cost = float(input("Enter the cost\n"))
    owner = input("Enter the Owner name\n")
    tv=int(input("Enter the number of TV set\n"))
    exe=ExecutiveStall(name, detail, cost, owner,tv)
    exe.display()
elif ch==3:
    name = input("Enter the Stall name\n")
    detail = input("Enter the details\n")
    cost = float(input("Enter the cost\n"))
    owner = input("Enter the Owner name\n")
    projector = int(input("Enter the number of Projectors\n"))
    premium=PremiumStall(name,detail,cost,owner,projector)
    premium.display()
else:
    print("Ivalid Input")

