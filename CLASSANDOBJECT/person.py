class Person:
    def __init__(self,name,age,qual):
        self.name=name
        self._age=age
        self.__qual=qual

    def display(self):
        print("name",self.name)
        print("age",self._age)
        print("qual",self.__qual)

    def __str__(self):
        s="name="+self.name +"\nself.age=" +str(self._age)+"\nqual" + self.__qual
        return s


    def getqual(self):
        return self.__qual



    def setqual(self,newqual):
        print("inside")
        self.__qual=newqual


