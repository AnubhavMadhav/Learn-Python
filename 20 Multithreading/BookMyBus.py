from threading import *

class BookMyBus:

    def __init__(self, availableSeats):
        self.availableSeats = availableSeats

    def buy(self, seatsRequested):
        print(current_thread().getName())
        print("Seats Requested by you:", seatsRequested)
        print("Total Seats Available:", self.availableSeats)
        if self.availableSeats>=seatsRequested:
            print("Confirming a Seat")
            print("Processing the Payment")
            print("Printing the Ticket")
            self.availableSeats-=seatsRequested
        else:
            print("Sorry. Not enough seats are available")


obj = BookMyBus(10)

t1 = Thread(target = obj.buy, args = (3,))          # We need to pass arguments as a list cause thread class expects arguments to be a list
t2 = Thread(target = obj.buy, args = (4,))
t3 = Thread(target = obj.buy, args = (4,))


t1.start()
t2.start()
t3.start()

'''This program helps us to book the tickets one by one, so there is no discrepancy or ambiguity if more than 1 person books the seat at same time or simultaneously'''