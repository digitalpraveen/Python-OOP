from Contact import Contact
from Address import Address
print("You want to search by,\n1.Contact\n2.Address\n")
n=int(input())
name=input("Enter Name\n")
phno=input("Enter Phone Number\n")
email=input("Enter Email id\n")
print("Enter Address")
door,street,city,state,pin=map(input("Enter Address").split(","))
cont=Contact(name,phno,email,Address)
addr=Address(cont,door,street,city,state,pin)
cont=Contact(name,phno,email,addr)
if(n==1):
    print(cont)
elif(n==2):
    print(addr)




