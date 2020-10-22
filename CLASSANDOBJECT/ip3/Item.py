class Item:
    def __init__(self, iid, name, cname, price):
        self.itemid = iid
        self.itemname = name
        self.cname = cname
        self.price = price

    def display(self):
# fill your code
        print("Item Id:",self.itemid)
        print("Item Name:",self.itemname)
        print("Company Name:",self.cname)
        print("Price of Item:%d RS"%self.price)