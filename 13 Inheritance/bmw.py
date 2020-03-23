class BMW:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):                            # Can be called by object of any of it's child class
        print("Car is Starting")

    def stop(self):                             # Can be called by object of any of it's child class
        print("Car is stopped")


class ThreeSeries(BMW):
    def __init__(self, cruiseControlEnabled, make, model, year):
        BMW.__init__(self, make, model, year)
        self.cruiseControlEnabled = cruiseControlEnabled

    def display(self):
        print(self.cruiseControlEnabled)


class FiveSeries(BMW):
    def __init__(self, parkingAssistEnabled, make, model, year):
        BMW.__init__(self, make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled


t = ThreeSeries(True, 'GTR', '15x', 2018)
print(t.cruiseControlEnabled)
print(t.make)
print(t.model)
print(t.year)
t.start()                   # Inheriting the function of parent class
t.stop()                    # Inheriting the function of parent class
t.display()                 # Called it's own function

f = FiveSeries(False, 'GTX', '19y', 2019)
print(f.parkingAssistEnabled)
print(f.make)
print(f.model)
print(f.year)