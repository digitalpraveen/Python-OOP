class Hall:
    def __init__(self, startDate, endDate, costPerDay):
        self.startDate = startDate
        self.endDate = endDate
        self.costPerDay = costPerDay

    def noDays(self):
          n=(self.endDate-self.startDate).days
          print("Total numer of date",n)
    def cost(self,d):
          self.d=d
          result=int(self.d*((self.endDate-self.startDate).days))
          print("Total cost",result)
