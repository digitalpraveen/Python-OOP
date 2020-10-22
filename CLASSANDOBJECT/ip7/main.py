from Book import Stall

nam=input("Enter book name\n")
detail=input("Enter book details\n")
p=Stall(nam,detail)
p.display()
n=int(input())
if (n==1):
    print(p)
elif(n==2):
    print("Initializing and printing using Setters and Getters")
    print("Details of the stall category:")
    p.set_detail(a=input(""))
    print(p.get_detail())