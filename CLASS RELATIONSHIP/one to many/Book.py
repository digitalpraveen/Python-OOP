class Book:
    def __init__(self,name,author):
        self.name=name
        self.author=author

    def __str__(self):
        return self.name+"-" +self.author

    def __eq__(self,book):
        if self.name==book.name:
            return True
        else:
            return False

