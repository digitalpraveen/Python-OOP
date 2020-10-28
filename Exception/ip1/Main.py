try:
    c=int(input("Enter the cost of the item for n days"))
    n=int(input("Enter the value of n"))
    cpd=c/n
    print("Cost per day of the item is %d"%cpd)
    if n==0:
        print("Exception occur")

except:
    print("Division by Zero")


