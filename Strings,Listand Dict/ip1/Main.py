import datetime
import re
from User import User
n=int(input("Enter the number of user's to be added"))
use=[]
for i in range(n):
    print("Enter the details of User",i+1)
    fname=input("Enter the first name\n")
    lname=input("Enter the last name\n")
    birth=datetime.datetime.strptime(input("Enter the date of birth(dd-mm-yyyy)\n"),'%d-%m-%Y')
    age=int(input("Enter the age\n"))
    regex = "[7-9][0-9]{9}"
    contact=input("Enter the contact number\n")
    for a in contact:
        if re.search(regex,contact) and len(contact)==10:
            break
        else:
            print("Invalid contact number")
            contact=input("Enter the contact number\n")
    uname = input("Enter the user name\n")
    passw=input("Enter the password\n")
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    email = input("Enter the email\n")
    for s in email:
        if (re.search(regex, email)):
            break
        else:
            print("Invalid email. try again!")
            email=input("Enter the email\n")
    print("Address details:")
    street = input("Enter the street\n")
    city = input("Enter the city\n")
    state = input("Enter the state\n")
    country = input("Enter the country\n")
    pin = int(input("Enter the pincode\n"))
    user = User(fname, lname, birth, age, contact, uname, passw, email, street, city, state, country, pin)
    use.append(user)

for User in use:
    user.display()






