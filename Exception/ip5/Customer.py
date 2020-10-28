class Customer:

    def __init__(self,name,id,place):
        self.name=name
        self.id=id
        self.place=place



    def display(self):
        print("Name: ",self.name)
        print("Id: ",self.id)
        print("Place: ",self.place)
