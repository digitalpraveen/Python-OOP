from TicketBooking import TicketBooking
Stageevent,Customer,Number_of_seats=input("Enter the booking detail").split(",")
print("Payment mode")
print("1.Cash payment")
print("2.Wallet payment")
print("3.Card payment")
Ticket=TicketBooking(Stageevent,Customer,Number_of_seats)

Ticket.makePayment()
