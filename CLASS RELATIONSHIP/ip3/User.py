class User:
    def __init__(self, name,contactNumber,hallist=[]):
        self.__name=name
        self.__contactNumber=contactNumber
        self.__hallist=hallist

    def addHallList(self, h):
        s=self.__name
        a=self.__contactNumber
        for i in self.__hallist:
            s+=str(i)+"\n"
            return s,a

