from VisaCard import VISCard
class HPVISACard(VISCard):

    def __init__(self, holdername, cvv):
        super().__init__(holdername, cvv)
        self.holdername = holdername
        self.cvv = cvv

    def computeRewardPoints(self, type, amount):
        self.reward=10
        print("Holder name:",self.holdername)
        print("CVV:",self.cvv)
        if type == "Fuel":
            print("Reward points:%.1f"%float((amount*0.01)+self.reward ))
        else:
            print("Reward points:%.1f"%float(amount * 0.01))

