from Stall import Stall

name=input("Enter the name of the stall\n")
detail=input("Enter the detail of the stall:\n")
owner=input("Enter the owner of the stall:\n")
type=input("Enter the type of the stall:\n")
size=int(input("Enter the size of the stall in square feet:\n"))
ch=input("Does the hall have TV?(y/n)\n")
stall = Stall(name, detail, owner)
if ch=="y":
    tv = int(input("Enter the number of TV:"))
    stall.computeCost(type, size, tv)
elif ch=="n":
    tv=0
    stall.computeCost(type, size,tv)






