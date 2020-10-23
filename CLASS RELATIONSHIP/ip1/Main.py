from User import User
from Contact import Contact
name=input("Enter Name\n")
age=input("Enter Age\n")
gender=input("Enter Gender\n")
phno=input("Enter Phone Number\n")
email=input("Enter Email id\n")
addr=input("Enter Address\n")
#Fill your code here
user=User(name,age,gender)
cont=Contact(phno,email,addr,user)
print(cont)