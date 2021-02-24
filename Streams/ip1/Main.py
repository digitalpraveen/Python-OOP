class User:
    def __init__(self,name,contactNumber,email):
        self.name=name
        self.contact=contactNumber
        self.email=email
    def addToList(fname):
        f=open("user.txt")
        eventlist=[]
        templist=f.readlines()
        for i in templist:
            tl=i[:-1].split(",")
            user=User(tl[0],tl[1],tl[2])
            eventlist.append(user)
        f.close()
        return eventlist
    def display(self):
        print("Name:",self.name)
        print("Contact:",self.contact)
        print("Email:",self.email)
eventlist=User.addToList("user.txt")
print("User details are as follows:")
for i in eventlist:
    i.display()
    print("\n")