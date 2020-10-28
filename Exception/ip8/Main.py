class Hall:
    def __init__(self,hallname,eventname,date,price):
        self.hall=hallname
        self.event=eventname
        self.date=date
        self.price=price



    def display(self):
        print(self.hall, '{:>14}'.format(self.event), '{:>12}'.format(self.date), '{:>10}'.format(self.price))


try:
    lis = []
    for i in range(1, 3):
        print("Enter the booking details:")
        hallname, event, date, price = input("").split(",")
        hall = Hall(hallname, event, date, price)
        lis.append(hall)
    for hall in lis:

            raise Exception
        else:
            print("Hall Name", '{:>14}'.format('Event Name'), '{:>12}'.format('Event Date'), '{:>10}'.format("Price"))
            hall.display()
except:
    print("Hall Not Available, Hall Already Booked")



