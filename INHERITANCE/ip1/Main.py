from SavingsAccount import SavingsAccount
from CurrentAccount import CurrentAccount
print("Choose Account Type")
print("1.Savings Account")
print("2.Current Account")
n=int(input(""))
if n==1:
    accname,accno,bankname,orgname = input("Enter Account details in comma separated(Account Name,Account Number,Bank Name,Organisation Name)").split(",")
    save=SavingsAccount(accname,accno,bankname,orgname)
    save.display()
elif n==2:
    accname,accno,bankname,tinno=input("Enter Account details in comma separated(Account Name,Account Number,Bank_Name,TIN Number)").split(",")
    current=CurrentAccount(accname,accno,bankname,tinno)
    current.display()

