
class user:
    def __init__(self,name,detail,owner,event):
        self.name=name
        self.detail=detail
        self.owner=owner
        self.event=event

    def display(self):
        print(self.name,'{:>14}'.format(self.detail),'{:>12}'.format(self.owner),'{:>10}'.format(self.event))
n=int(input("Enter the number of the events:"))
lis=[]
try:
  for i in range(n):
      print("Enter the details of event",i+1)
      name,details,owner,eventid=input("").split(",")
      event=int(eventid)
      if event in range(1, 4):
          pass
      else:
          raise Exception("No event type available with the given id")
      s = user(name, details, owner, event)
      lis.append(s)
  print("The events entered are:")
  print("Name",'{:>14}'.format('Details'),'{:>12}'.format('Owner name'),'{:>10}'.format('Eventtypeid'))
  for s in lis:
      print()
except Exception:
    print("No event type available with the given id")