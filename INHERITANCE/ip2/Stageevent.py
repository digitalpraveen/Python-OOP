from Event import Event
class Stageevent(Event):

    def __init__(self,endingtime,name,address,startingdate,startingtime):
        self.__eventtype="Stage Event"
        self.__endingtime=endingtime
        super(Stageevent,self).__init__(name,address,startingdate,startingtime)
    def display(self):
        print("Event type:",self.__eventtype)
        print("Event Name:",self.name)
        print("Event Address:",self.address)
        print("Event Date:",self.startdate)
        print("Event Start Time:",self.starttime)
        print("Event End Time:",self.__endingtime)