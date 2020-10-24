from Shape import Shape
import math
class Circle(Shape):
    def __init__(self, radius, area):
        super().__init__(area)
        self.radius=radius


    def computeArea(self):
        self.area=print("Area of circle is %.2f"%float(math.pi*(self.radius*self.radius)))



