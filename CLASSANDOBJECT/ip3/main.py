from Item import Item
iid=input("\n")
itemname=input("\n")
companyname=input("\n")
price=int(input())

# fill your code
p=Item(iid,itemname,companyname,price)
p.display()