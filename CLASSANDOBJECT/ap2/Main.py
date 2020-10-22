
from Product import Product
pro=[]
for i in range(1 , 3):
    print("Enter the details of product %d"%i)
    name = input("Enter product name\n")
    brand = input("Enter product brand\n")
    typ =  input("Enter product type\n")
    color = input("Enter product color\n")
    mat = input("Enter product material\n")
    dim = input("Enter product dimensions\n")
    prate = input("Enter product rate\n")
    product=Product(name,brand,typ,color,mat,dim,prate)
    pro.append(product)
print("Product Details")
product.set_value()
for product in pro:
    product.getvalue()
