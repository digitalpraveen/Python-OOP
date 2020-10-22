import datetime
from Event import Event
name=input("Enter the name")
d1=input("Enter the date")
datecheck=datetime.datetime.strptime(d1,"%d/%m/%Y").date()

p=Event(name,datecheck)
p.checkDate()


