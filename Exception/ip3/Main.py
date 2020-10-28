from User import User
import re
try:
   regex='([A-Za-z0-9])([\W]){10-20}'
   name,mob,Username,passw=input("Enter the user details").split(",")
   x=re.search(regex,passw)
   user=User(name,mob,Username,passw)
   user.display()
except:
   print("week password")

