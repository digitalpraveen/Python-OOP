from Circle import Circle
from Rectangle import Rectangle
from Triangle import Triangle
print("Enter the shape\n 1.Circle\n 2.Rectangle\n 3.Triangle")
n=int(input(""))
if n==1:
    rad=float(input("Enter the radius:\n"))
    cir=Circle(rad,area=0)
    cir.computeArea()
elif n==2:
    print("Enter the length and bradth:")
    len=float(input(""))
    bre=float(input(""))
    rec=Rectangle(len,bre,area=0)
    rec.computeArea()
elif n==3:
    print("Enter the base and height:")
    base=float(input(""))
    height=float(input(""))
    tri=Triangle(base,height,area=0)
    tri.computeArea()
else:
    print("Invalid choice ")