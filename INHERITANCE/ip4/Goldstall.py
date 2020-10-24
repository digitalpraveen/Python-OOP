from Stall import Stall
class Goldstall(Stall):
    def __init__(self,extraamount,name,detail,contact,ownername,basicprice):
        self.extraamount=extraamount
        Stall.__init__(self,name,detail,contact,ownername,basicprice)

    def display(self):

        super(Goldstall, self).display()
        print("Stall price per day:",self.basicprice+self.extraamount)


