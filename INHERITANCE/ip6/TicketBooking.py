class TicketBooking:
    def __init__(self, stageevent, customer, noofseats):
        self.__stageevent = stageevent
        self.__customer = customer
        self.__noofseats = noofseats

    def makePayment(self):
        n = int(input(""))
        if n == 1:
            amount = float(input("Enter the amount\n"))

            print("Stage event:", self.__stageevent)
            print("Customer:", self.__customer)
            print("Number of seats:", self.__noofseats)
            print("Amount %.1f paid in cash" % amount)

        elif n == 2:
            amount = float(input("Enter the amount\n"))
            walletnumber = input("Enter the wallet number\n")
            print("Stage event:", self.__stageevent)
            print("Customer:", self.__customer)
            print("Number of seats:", self.__noofseats)
            print("Amount %.1f paid using wallet number %s" % (amount, walletnumber))

        elif n == 3:
            name = input("Enter cardholder name\n")
            amount = float(input("Enter the amount\n"))
            creditcard = input("Enter the credit card type\n")
            cvv = input("Enter the CVV number\n")
            print("Stage event:", self.__stageevent)
            print("Customer:", self.__customer)
            print("Number of seats:", self.__noofseats)
            print("Holder name:", name)
            print("Amount %.1f paid using %s" % (amount, creditcard))
            print("CVV:%s" % cvv)
        else:
            print("Invalid Choice")


