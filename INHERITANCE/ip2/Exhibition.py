from Event import Event
class Exhibition(Event):

    def __init__(self,name,address,startingdate,startingtime,enddate):
        self.__eventtype="Exhibition"
        self.__enddate=enddate
        super(Exhibition, self).__init__(name, address, startingdate, startingtime)

    def display(self):
        print("Event type:",self.__eventtype)
        print("Event Name: ",self.name)
        print("Event Address: ",self.address)
        print("Event Date: ",self.startdate)
        print("Event Endtime:",self.__enddate)
        print("Event Start Time: ",self.starttime)
