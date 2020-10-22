class Hall:
    def __init__(self, name, phone, addr, date, cost, owner):
        self.name = name
        self.phone = phone
        self.addr = addr
        self.date = date
        self.cost = cost
        self.owner = owner

    def __eq__(self, obj):
        # fill your code
        return self.name == obj.name and self.phone == obj.phone

    def display(self):
        # fill your code
        print("Hall name :" + self.name)
        print("Phone No :", self.phone)
        print("Address :" + self.addr)
        print("Cost :", self.cost)
        print("Enter owner name"+ self.owner)


