'''Create a Thread using function'''

from threading import Thread

def displayNumbers():
    i = 0
    while i<=10:
        print(i)
        i+=1

t = Thread(target=displayNumbers)

t.start()

