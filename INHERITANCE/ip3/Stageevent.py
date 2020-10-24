from Event import Event


class StageEvent(Event):

    def __init__(self,name,ownername,noofdays,costperday):
        Event.__init__(self,name,ownername,noofdays,costperday)


    def Calculate(self):
        print("Gross amuont", self.noofdays * self.costperday)
        print("Gst:", (self.noofdays * self.costperday) * 15 / 100)
        print("Net amount:", (self.noofdays * self.costperday) + ((self.noofdays * self.costperday) * 15 / 100))



