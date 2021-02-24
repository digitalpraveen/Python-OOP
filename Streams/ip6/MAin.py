from EventBO import EventBO
n=int(input("Enter the number of Events to be added to the list"))
ebo=EventBO()
for i in range(n):
    s=input()
    ebo.listforLead("Event.txt",s+"\n")

eventList=ebo.createListofEvent("Event.txt")
for i in eventList:
    i.display()
    print("\n")