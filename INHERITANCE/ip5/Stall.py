class Stall:
    def __init__(self,name,detail,owner):
        self.name=name
        self.detail=detail
        self.owner=owner
    def computeCost(self,stallType, squareFeet,numberOfTV):
         plat = 200
         diamond = 150
         gold = 100
         tv = 10000
         self.type=stallType
         self.sqft=squareFeet
         self.tv=numberOfTV

         if self.type == "Platinum":
            total= plat * self.sqft
         elif self.type == "Diamond":
             total= diamond * self.sqft
         elif self.type == "Gold":
             total= gold * self.sqft
         if self.tv != 0:
             print("The cost of the stall is %.1f"%(total+(self.tv*tv)))
         elif self.tv ==0:
             print("The cost of the stall is %.1f"%total)

















