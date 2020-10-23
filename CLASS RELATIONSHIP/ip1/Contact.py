class Contact:
    def __init__(self, pho, email,addr,User):
        self.pho=pho
        self.email=email
        self.addr=addr
        self.User=User
    # Fill your code here

    def __str__(self):
           return str(self.User) +"\n" +"Phone Number:"+self.pho+"\n"+"Email id:"+self.email+"\n"+"Address:"+self.addr