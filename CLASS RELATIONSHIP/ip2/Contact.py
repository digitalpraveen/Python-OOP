from Address import Address
class Contact:
    def __init__(self, name, phn, email,addr):
        self.name=name
        self.phn=phn
        self.email=email
        self.addr=addr

    def display(self):
        print("Enter Name",self.name)
        print("Phone Number",self.phn)
        print("Email id:",self.email)
        print(self.addr)
