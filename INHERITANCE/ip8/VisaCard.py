class VISCard:

    def __init__(self,holdername,cvv):
        self.holdername=holdername
        self.cvv=cvv

    def computeRewardPoints(self,type,amount):
        self.reward=10
        print("Holder name:",self.holdername)
        print("CVV:",self.cvv)
        print("Reward points:%.1f"%float(amount*0.01))





