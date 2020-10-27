from abc import ABC,abstractmethod
import math
class Shape(ABC):
    #abstract method
    def calperimeter(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def calperimeter(self):
        p=2*math.pi*self.radius
        print("The perimeter is %.2f" %p)

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def calperimeter(self):
        p=float(2*(self.length+self.breadth))
        print("The perimeter is %.2f" % p)
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def calperimeter(self):
        p=4*(self.side)
        print("The perimeter is %.2f" %p)
print("List of shapes")
print("1.circle")
print("2.rectangle")
print("3.square")
ch=int(input("Enter your choice\n"))
if ch==1:
    rad=float(input("Enter the radius\n"))
    cir=Circle(rad)
    per=cir.calperimeter()
elif ch==2:
    len=int(input("Enter the length\n"))
    bred=int(input("Enter the breadth\n"))
    rec=Rectangle(len,bred)
    per=rec.calperimeter()

elif ch==3:
    side=int(input("Enter the side\n"))
    sq=Square(side)
    per=sq.calperimeter()
