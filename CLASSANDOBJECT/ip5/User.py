class User:
    def __init__(self,name,username,password,mobileNumber):
        self.name=name
        self.username=username
        self.password=password
        self.mobileNumber=mobileNumber

    def __eq__(self,obj):
        # fill your code
               return self.mobileNumber==obj.mobileNumber