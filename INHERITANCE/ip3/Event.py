
class Event:
    def __init__(self,name,ownername,noofdays,costperday):
        self.name=name
        self.ownername=ownername
        self.noofdays=noofdays
        self.costperday=costperday

    def __str__(self):
              return "Event Name:"+self.name+"\n"+"Event owner"+self.ownername+"\n"+"No of days"+str(self.noofdays)+":\n"+"Cost Per day"+str(self.costperday)



