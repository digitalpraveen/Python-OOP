class Stall:
    def __init__(self,name,detail,contact,ownername,basicprice):
        self.name=name
        self.detail=detail
        self.contact=contact
        self.ownername=ownername
        self.basicprice=basicprice

    def display(self):
        print("Name:",self.name)
        print("Details:",self.detail)
        print("Contact Number:",self.contact)
        print("Owner Name",self.ownername)
