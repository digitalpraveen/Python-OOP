from Event import Event
class Exhibition(Event):

    def __init__(self,name,ownername,noofdays,costperday):
        Event.__init__(self,name,ownername,noofdays,costperday)

    def Calculate(self):
        print("Gross amuont %.1f"%(self.noofdays*self.costperday))
        print("Gst: %.1f"%((self.noofdays*self.costperday)*5/100))
        print("Net amount: %.1f"%((self.noofdays*self.costperday)+((self.noofdays*self.costperday)*5/100)))

