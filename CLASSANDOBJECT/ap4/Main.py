
from Product import Product
n = int(input("Enter the number of product detials to be displayed\n"))
lis=[]
for i in range(n):
    print("Enter the details of product %d"%(i+1))
    name = input("Enter product name\n")
    brand = input("Enter product brand\n")
    ptype = input("Enter product type\n")
    pcat = input("Enter product category\n")
    pcatsec = input("Enter catalog service sector\n")
    pcatarea = input("Enter catalog service area\n")
    color = input("Enter product color\n")
    mat = input("Enter product material\n")
    dim = input("Enter product dimensions\n")
    prate = input("Enter product rate\n")
    city = input("Enter city\n")
    product=Product(name,brand,ptype,pcat,pcatsec,pcatarea,color,mat,dim,prate,city)
    lis.append(product)
print("Product Details")
print("%-15s%-15s%-15s%-15s%-15s%-15s%-15s%-15s%-15s%-15s%-15s"%("Name","Brand","Type","Category","Service Sector","Service Area","Color" , "Material" , "Dimension" , "Rate" , "City"))
for i in lis:
    print(i)