class Library:
    def __init__(self,name,book=[]):
       self.name=name
       self.book=book

    def __str__(self):
        s=self.name
        for i in self.book:
            s+= str(i) +"\n"
            return s



