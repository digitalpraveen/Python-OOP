class Faculty:
    def __init__(self,name,sub):
        self.name=name
        self.sub=sub

    def __str__(self):
        return self.name +"-"+ self.sub

