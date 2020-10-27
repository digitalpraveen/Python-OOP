from abc import ABCMeta
class HotelTraif():
    def showTraiff(self, c):
        pass
# fill your code
class MakeMyTrip(HotelTraif):
    def __init__(self):
        super().__init__()
        self.f = {'Mysore': ['Sugamya corner--1500 per day','Mysorepalace--2050 per day'],
                  'Bangalore': ['Jigar corner--1500 per day', 'Marshpalace--2050 per day'],
                  'Mangalore': ['Karawali corner--1500 per day', 'Mangalorepalace--2050 per day']}

    def showTraiff(self, c):
        self.c=c
        if self.c in self.f:
            for i in self.f[self.c]:
                 print(i)
        else:
             print("No results found")




class Trivago(HotelTraif):
    def __init__(self):
        super().__init__()
        self.f = {'Bangalore': ['Kanakazana corner--1250 per day', 'Bangalorepalace--2150 per day'],
                  'Mysore': ['Sugamya corner--1500 per day', 'Mysorepalace--2050 per day']}

    def showTraiff(self, c):
        self.c = c
        if self.c in self.f:
            for i in self.f[self.c]:
                 print(i)
        else:
            print("No results found")


class ClearTrip(HotelTraif):
    def __init__(self):
        super().__init__()
        self.f = {'Mysore': ['Sugamya corner--1250 per day', 'Mysorepalace--2250 per day'],
                  'Shivmogha': ['Jog jalapatha--1500 per day', 'Murdashwara mata--2050 per day']}

    def showTraiff(self, c):
        self.c = c
        if self.c in self.f:
            for i in self.f[self.c]:
                print(i)
        else:
            print("No results found")


print("Menu\n1.MakeMyTrip\n2.Trivago\n3.ClearTrip")
n = int(input("Enter your choice\n"))
if n==1:
    c=input("Enter city to be searched\n")
    make=MakeMyTrip()
    make.showTraiff(c)
elif n==2:
    c = input("Enter city to be searched\n")
    triv=Trivago()
    triv.showTraiff(c)
elif n==3:
    c = input("Enter city to be searched\n")
    clear=ClearTrip()
    clear.showTraiff(c)

