from Shape import Shape

class Rectangle(Shape):
    def __init__(self, length, breadth, area):
        super().__init__(area)
        self.length=length
        self.breadth=breadth

    def computeArea(self):
        self.area=print("Area of the rectangle is %.2f"%float((self.length*self.breadth)))