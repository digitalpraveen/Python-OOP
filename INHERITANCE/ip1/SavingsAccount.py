from Account import Account
class SavingsAccount(Account):
    def __init__(self, orgname, accname,accno,bankname):
         self.orgname = orgname
         Account.__init__(self,accname,accno,bankname)

    def display(self):
         print("Account Name:",self._accname)
         print("Account Number:",self._accno)
         print("Bank Name",self._bankname)
         print("Organisation Name:",self.orgname)
