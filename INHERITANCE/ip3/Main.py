from Exhibition import Exhibition
from Stageevent import StageEvent
name=input("Enter Stall Name\n")
owner=input("Enter the Stall Owner\n")
days=int(input("Enter the number of days booked\n"))
amount=float(input("Enter amount per day\n"))
print("Menu")
print("1Exhibition")
print("2.Stage Event")
Exhibitio=Exhibition(name,owner,days,amount)
Stage=StageEvent(name,owner,days,amount)
n=int(input(""))
if n==1:
    print(Exhibitio)
    Exhibitio.Calculate()
elif n==2:
    print(Stage)
    Stage.Calculate()
