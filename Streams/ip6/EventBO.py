from Event import Event
class EventBO:
    def createListofEvent(self,fname):
        f=open(fname)
        eventList=[]
        templist=f.readlines()
        for i in templist:
            tl=i[:-1].split(",")
            event=Event(tl[0],tl[1],tl[2],tl[3],tl[4])
            eventList.append(event)
        f.close()
        return eventList
    def listforLead(self,fname,eventstr):
        f=open(fname,"a")
        f.write(eventstr)
        f.close()
