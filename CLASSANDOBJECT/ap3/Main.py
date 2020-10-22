
from User import User
li = []
for i in range(1 , 3):
    print("Enter the details of user %d"%i)
    fname = input("Enter your first name\n")
    lname = input("Enter your last name\n")
    dob = input("Enter your DOB\n")
    age = input("Enter your age\n")
    contact = input("Enter your contact number\n")
    email = input("Enter your email\n")
    uname = input("Enter your username\n")
    pwd = input("Enter your password\n")
    role = input("Enter your role\n")
    address = input("Enter your address\n")
    p=User(fname,lname,dob,age,contact,email,uname,pwd,role,address)
    li.append(p)
len()==li.count(p)

