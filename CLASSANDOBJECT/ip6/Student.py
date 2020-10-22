class Student:

    def __init__(self,id,uname,pwd,name,addr,city,pin,phno,email):
        self.id=id
        self.uname=uname
        self.pwd=pwd
        self.name=name
        self.addr=addr
        self.city=city
        self.pin=pin
        self.phno=phno
        self.email=email

    def __str__(self):
        return "id"+str(self.id)+"\n"+"User Name:"+self.uname+"\n"+"Password:"+self.pwd+"\n"+"Name"+self.name+"\n"+"Address:"+self.addr+"\n"+"city:"+self.city+"\n"+"pincode"+str(self.pin)+"\n"+"Contact Number"+str(self.phno)+"\n"+"email:"+self.email
