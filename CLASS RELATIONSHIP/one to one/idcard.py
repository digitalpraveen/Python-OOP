class Idcard:
    def __init__(self,rno,isbarcodepresent):
        self.rno=rno
        self.isbarcodepresent=isbarcodepresent

    def __str__(self):
        return str(self.rno) + '-'+ str(self.isbarcodepresent)
