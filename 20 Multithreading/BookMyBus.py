from threading import *

class BookMyBus:

    def buy(self):
        print("Confirming a Seat")
        print("Processing the Payment")
        print("Printing the Ticket")


obj = BookMyBus()

t1 = Thread(target = obj.buy)
t2 = Thread(target = obj.buy)
t3 = Thread(target = obj.buy)


t1.start()
t2.start()
t3.start()

'''This program helps us to book the tickets one by one, so there is no discrepancy or ambiguity if more than 1 person books the seat at same time or simultaneously'''