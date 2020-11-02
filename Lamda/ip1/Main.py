
print("1. Admin\n2. Teacher\n3. Student\nEnter your choice:")
n=int(input(""))
s=(lambda n:"- Login\n- Logout\n- resetPassword\n- createUser"if n==1 else("-  Login\n- Logout\n- postResults\n- attendanceReport" if n==2  else("- Login\n- Logout\n- takeTest"if(n==3) else "Wrong choice")))(n)
print(s)