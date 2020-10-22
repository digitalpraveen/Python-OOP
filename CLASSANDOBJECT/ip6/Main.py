from Student import Student

id=int(input("Enter the student id\n"))
uname=input("Enter the  student's username")
pwd=input("Enter the password\n")
name=input("Enter the name of the student\n")
addr=input("Enter the address\n")
city=input("Enter the city\n")
pin=int(input("Enter the pincode\n"))
phno=int(input("Enter the contact number\n"))
email=input("Enter the email id")

stu=Student(id,uname,pwd,name,addr,city,pin,phno,email)
print(stu)