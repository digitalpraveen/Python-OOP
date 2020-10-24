from Goldstall import Goldstall
from Platinumstall import Platinumstall
print("Menu")
print("1.Gold stall")
print("2.Platinum stall")
n=int(input(""))
name=input("Enter Stall name")
detail=input("Enter Stall Detaila")
contact=int(input("Enter contact Number"))
owner=input("Enter Owner name")
basic=int(input("Enter Basic Price"))
extra=int(input("Enter the Extra amount Goldstall"))
gold=Goldstall(extra,name,detail,contact,owner,basic)
platinum=Platinumstall(extra,name,detail,contact,owner,basic)
if(n==1):
    gold.display()

elif(n==2):
    platinum.display()


