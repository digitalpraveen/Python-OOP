from User import User
name=input("Enter User name\n")
try:
   deposit =input("Enter Deposit amount\n")
   cost = input("Enter Cost per day\n")
   s=float(deposit)
   n=float(cost)
   user = User(name,s,n)
   user.display()
except:
    print("Invalid Input")


