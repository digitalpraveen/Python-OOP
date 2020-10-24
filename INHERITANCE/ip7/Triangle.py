from Shape import Shape

class Triangle(Shape):
    def __init__(self, base, height, area):
        super().__init__(area)
        self.base=base
        self.heigth=height

    def computeArea(self):
        self.area=print("Area of the trianglr=%.2f"%float((1/2)*(self.base*self.heigth)))

