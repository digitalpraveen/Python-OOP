from Account import Account
class CurrentAccount(Account):
    def __init__(self,tinnumber,accname,accno,bankname):
         self.tinnumber = tinnumber
         Account.__init__(self,accname,accno,bankname)
    def display(self):
         print("Account Name:", self._accname)
         print("Account Number:", self._accno)
         print("Bank Name:", self._bankname)
         print("TIN Number:", self.tinnumber)