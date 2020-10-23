from Hall import Hall
from User import User
n=int(input("Enter the number of user's\n"))
hall=[]
for i in range(n):
    name=input("Enter user name")
    contact = input("Enter contact number")
halls = int(input("Enter the number of halls"))
for i in range(halls):
    hallnam = input("Enter hall name")
    cost = input("Enter cost per day")
    owner = input("Enter owner name")
    hal=Hall(hallnam,cost,owner)
    hall.append(hal)

user=User(name,contact,hall)
print(user.addHallList(hal))

