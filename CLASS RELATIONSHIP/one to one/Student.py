class Student:
    def __init__(self,name,idcard):
        self.name=name
        self.idcard=idcard

    def __str__(self):
        s=self.name+"-"+ str(self.idcard)
        return s
