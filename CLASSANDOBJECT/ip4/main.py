from operator import attrgetter
from User import User
n=int(input("Enter the number of User:\n"))
use=[]
for i in range(0,n):
    print("Enter the details of User %d"%(i+1))
    name=input("Enter the name of the user:\n")
    mno=int(input("Enter the mobile number of the user:\n"))
    uname=input("Enter the username of the user:\n")
    pswd=input("Enter the password of the user:\n")
    p = User(name, mno, uname, pswd)
    use.append(p)
for i in use:
    print(i)
print("After sorting***")
use=sorted(use,key=attrgetter("name"))
for i in use:
    print(i)
un=input("Enter elements to deleted")
for p in use:
    if uname==un in use:
        use.remove(uname)
        print()
    else:
        print("no vlaue")
