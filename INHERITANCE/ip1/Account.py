class Account:
    def __init__(self,accname,accno,bankname):
         self._accname=accname
         self._accno=accno
         self._bankname=bankname

    def display(self):
         print("Account Name:", self._accname)
         print("Account Number:", self._accno)
         print("Bank Name:",self._bankname)
