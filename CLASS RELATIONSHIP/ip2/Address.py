from Contact import Contact
class Address:
    def __init__(self,door,street,city,state,pin,Contact):
        self.contact=Contact
        self.address=Address
        self.door=door
        self.street=street
        self.city=city
        self.state=state
        self.pin=pin
    def display(self):
        print("Address:")
        print("Door No:",self.door)
        print("Street:",self.street)
        print("City:",self.city)
        print("State:",self.state)
        print("Pincode:",self.pin)
        print(self.contact)




