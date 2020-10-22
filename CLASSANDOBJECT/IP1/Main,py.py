from Hall import Hall
li=[]
n = int(input("Enter the number of Entries\n"))
for i in range(0, n):
    print("Enter details of Hall %d" % (i + 1))
    name = input("Enter Hall name\n")
    phno = int(input("Enter Phone\n"))
    addr = input("Enter Address\n")
    date = input("Enter Date of booking\n")
    cost = float(input("Enter cost\n"))
    oname = input("Enter owner name\n")
    p = Hall(name, phno, addr, date, cost, oname)
    li.append(p)