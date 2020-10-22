from User import User

print("Enter the details of User 1")
name1=input("Name :\n")
uname1=input("Username :\n")
pwd1=input("Password :\n")
mbno1=input("Mobile Number :\n")

print("Enter the details of User 2")
name2=input("Name :\n")
uname2=input("Username :\n")
pwd2=input("Password :\n")
mbno2=input("Mobile Number :\n")

# fill your code
user1=User(name1,uname1,pwd1,mbno1)
user2=User(name2,uname2,pwd2,mbno2)
if(user1==user2):
    print("User1 and User2 are equal")
else:
    print("User1 and User2 are not equal")