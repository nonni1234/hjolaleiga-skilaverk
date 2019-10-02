# Hjólaleiga Skilaverkefni
# Jón og Sesselja
from time import sleep as wait
class Bike:
    def __init__(self, hourly_price, daily_price, weekly_price):
        self.hourly_price = hourly_price
        self.daily_price = daily_price
        self.weekly_price = weekly_price

class MountainBike(Bike):
    def __init__(self, hourly_price, daily_price, weekly_price, shock_absorber):
        Bike.__init__(self,hourly_price,daily_price,weekly_price)
        self.shock_absorber = shock_absorber

class RoadBike(Bike):
    def __init__(self,hourly_price, daily_price, weekly_price, avgSpeed, tireQuality):
        Bike.__init__(self,hourly_price, daily_price, weekly_price)
        self.avgSpeed = avgSpeed
        self.tireQuality = tireQuality

class BMXBike(Bike):
    def __init__(self, hourly_price, daily_price, weekly_price, tireSize, pegs):
        Bike.__init__(self, hourly_price, daily_price, weekly_price)
        self.tireSize = tireSize
        self.pegs = pegs

class Customer:
    def __init__(self, name, email, cardnumber):
        self.name = name
        self.email = email
        self.cardnumber = int(cardnumber)
        self.bikeRented = None
    def rentBike(self,time, bike):
        if self.bikeRented != None:
            print("Customer already rented a bike")
            return False
        else:
            if bikes[bike] > 0:
                customer.bikeRented = bike
                return True
            else:
                print("This bike does not exist or is sold out")
                return False
    def returnBike(self):
        if self.bikeRented == None:
            print("Customer does not have a bike rented")
        else:
            for k,v in bikes.items():
                if k == self.bikeRented:
                    v += 1

bikes = {"Mountain Bike":4,"BMX Bike": 1,"Road Bike": 2}
customer = Customer(input("Your name:"),input("Your Email: "), input("Your Card Number: "))
while True:
    print("""
    ====== Bike Rental Shop =======
    1. Display available bikes
    2. Request a bike on hourly basis $5
    3. Request a bike on daily basis $20
    4. Request a bike on weekly basis $60
    5. Return a bike
    6. Exit """)
    choice = input("Choose an action: ")
    if choice == "1":
        for k,v in bikes.items():
            print(v,k+"s")
    elif choice == "2":
        bike = input("What type of bike do you want to rent?: ")
        time = input("How many hours do you want it for?")
        time = time+" Hours"
        rented = customer.rentBike(time,bike)
        if rented == True:
            print("Bike has been rented")

    elif choice == "3":
        bike = input("What type of bike do you want to rent?: ")
        time = input("How many days do you want it for?")
        time = time + " Days"
        rented = customer.rentBike(time, bike)
        if rented == True:
            print("Bike has been rented")
    elif choice == "4":
        bike = input("What type of bike do you want to rent?: ")
        time = input("How many hours do you want it for?")
        time = time + " Weeks"
        rented = customer.rentBike(time, bike)
        if rented == True:
            print("Bike has been rented")
    elif choice == "5":
        customer.returnBike()
    else:
        print("Thats not a valid action")
    wait(1.5)

