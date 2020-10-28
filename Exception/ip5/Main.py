from Customer import Customer
n=int(input("Enter the number of Customers\n"))
list=[]
print("Enter the Customer Details")
try:
    for i in range(n):
        name,id,place = input("").split(",")
        customer = Customer(name, id, place)
        list.append(customer)
    indx=int(input("Enter the customer number to be displayed\n"))
    if customer in list:
        list[indx].display()

except:
    print("Array index out of bond")