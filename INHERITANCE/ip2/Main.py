from Stageevent import Stageevent
from Exhibition import Exhibition
print("Menu")
print("1.Exhibition")
print("2.Stage Event type")
print("Enter event type")
n=int(input(""))

if (n == 1):
    name = input("Enter Event name\n")
    addr = input("Enter Event address\n")
    date = input("Enter Event date\n")
    sttime = input("Enter Event Start time\n")
    enddate = input("Enter Event Closing Date\n")
    exb = Exhibition(name, addr, date, sttime,enddate)
    exb.display()

elif (n == 2):
    name = input("Enter Event name\n")
    addr = input("Enter Event address\n")
    date = input("Enter Event date\n")
    sttime = input("Enter Event Start time\n")
    endtime = input("Enter End Time\n")
    stage = Stageevent(endtime,name,addr,date,sttime)
    stage.display()
