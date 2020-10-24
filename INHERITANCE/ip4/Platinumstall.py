from Stall import Stall
class Platinumstall(Stall):
    def __init__(self,extraamount,name,detail,contact,ownername,basicprice):
        self.extraamount=extraamount
        super(Platinumstall, self).__init__(name,detail,contact,ownername,basicprice)

    def display(self):
        super(Platinumstall, self).display()
        print("Stall price per day:", self.basicprice + self.extraamount)


