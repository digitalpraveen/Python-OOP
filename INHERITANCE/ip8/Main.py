from VisaCard import VISCard
from HPVISACard import HPVISACard

name=input("Enter the holder name\n")
cvv=input("Enter the CVV number\n")
amount=int(input("Enter the bill amount\n"))
type=input("Mention the type of spending\n")
print("Choose card type\n1.VISA card\n2.HP VISA card")
n=int(input(""))
if n==1:
    vis=VISCard(name,cvv)
    vis.computeRewardPoints(type,amount)
elif n==2:
    hp=HPVISACard(name,cvv)
    hp.computeRewardPoints(type,amount)
else:
    print("Invalid choice")
for i in range(10):
    c = input("Do you want to continue?(Y/N)\n")
    if c == "Y":
        name = input("Enter the holder name\n")
        cvv = input("Enter the CVV number\n")
        amount = int(input("Enter the bill amount\n"))
        type = input("Mention the type of spending\n")
        print("Choose card type\n1.VISA card\n2.HP VISA card")
        n = int(input(""))
        if n == 1:
            vis = VISCard(name, cvv)
            vis.computeRewardPoints(type, amount)
        elif n == 2:
            hp = HPVISACard(name, cvv)
            hp.computeRewardPoints(type, amount)
        else:
            print("Invalid choice")
    elif c == "N":
        break
