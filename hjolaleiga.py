# Hjólaleiga Skilaverkefni
# Jón og Sesselja
from time import sleep as wait
from random import randint as rand

class Bike:
    def __init__(self, hourly_price, daily_price, weekly_price, nr):
        self.hourly_price = hourly_price
        self.daily_price = daily_price
        self.weekly_price = weekly_price
        self.nr = nr

bikes = {"mountain bike":Bike(6, 20, 60, 4), "road bike":Bike(3, 15, 50, 2), "bmx bike":Bike(4, 12, 40, 1)}
'''bikes.append(Bike("Mountain bike", 6, 20, 60, 4))
bikes.append(Bike("Road bike", 3, 15, 50, 2))
bikes.append(Bike("Bmx bike", 4, 12, 40, 1))'''

'''class MountainBike(Bike):
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
        self.pegs = pegs'''

class Customer:
    def __init__(self, name, email, cardnumber):
        self.name = name
        self.email = email
        self.cardnumber = int(cardnumber)
        self.bikeRented = None
        self.rentTime = None
    def rentBike(self,time, bike):
        if self.bikeRented != None:
            print("Customer already rented a bike")
            return False
        else:
            if bikes[bike.lower()].nr > 0:
                self.bikeRented = bike
                self.rentTime = time
                bikes[bike.lower()].nr -= 1
                return True
            else:
                print("This bike does not exist or is sold out")
                return False
    def returnBike(self):
        if self.bikeRented == None:
            print("Customer does not have a bike rented")
        else:
            bikes[bike.lower()].nr += 1
            self.bikeRented = None
            self.rentTime = None
            print("Bike returned, thank you", self.name + "!")

'''mtbikes = [MountainBike(rand(3,20), rand(15,40), rand(30,55), bool(rand(0,1))) for i in range(4)]
bmxbikes = [BMXBike(rand(3,20), rand(15,40), rand(30,55), rand(20, 30), bool(rand(0,1))) for i in range(1)]
rdbikes = [RoadBike(rand(3,20), rand(15,40), rand(30,55), rand(10,20), rand(1,10)) for i in range(2)]'''

#bikes = {"Mountain Bike":len(mtbikes),"BMX Bike": len(bmxbikes),"Road Bike": len(rdbikes)}
customer = Customer(input("Your name:"),input("Your Email: "), input("Your Card Number: "))
while True:
    print("""
    ====== Bike Rental Shop =======
    1. Display available bikes
    2. Request a bike on hourly basis
    3. Request a bike on daily basis
    4. Request a bike on weekly basis
    5. Return a bike
    6. Rented bike information
    7. Exit """)
    choice = input("Choose an action: ")
    if choice == "1":
        for k,v in bikes.items():
            print(v.nr,k+"s")
    elif choice == "2":
        for k,v in bikes.items():
            print("%s: $%s per hour" % (k, v.hourly_price))
        bike = input("What type of bike do you want to rent?: ")
        time = input("How many hours do you want it for?")
        time2 = time+" Hours"
        rented = customer.rentBike(time2,bike)
        if rented == True:
            print("Total price: $%s" % (int(bikes[bike.lower()].hourly_price) * int(time)))
            print("Bike has been rented")

    elif choice == "3":
        for k,v in bikes.items():
            print("%s: $%s per day" % (k, v.daily_price))
        bike = input("What type of bike do you want to rent?: ")
        time = input("How many days do you want it for?")
        time2 = time + " Days"
        rented = customer.rentBike(time2, bike)
        if rented == True:
            print("Total price: $%s" % (int(bikes[ bike.lower() ].daily_price) * int(time)))
            print("Bike has been rented")
    elif choice == "4":
        for k,v in bikes.items():
            print("%s: $%s per week" % (k, v.weekly_price))
        bike = input("What type of bike do you want to rent?: ")
        time = input("How many weeks do you want it for?")
        time2 = time + " Weeks"
        rented = customer.rentBike(time2, bike)
        if rented == True:
            print("Total price: $%s" % (int(bikes[ bike.lower() ].weekly_price) * int(time)))
            print("Bike has been rented")
    elif choice == "5":
        customer.returnBike()

    elif choice == "6":
        if customer.bikeRented != None:
            print(f"{customer.name} has a {customer.bikeRented} with {customer.rentTime} left ")
        else:
            print("Customer does not have a bike rented")

    elif choice == "7":
        print("Takk fyrir að versla hjá okkur!")
        break
    else:
        print("Thats not a valid action")
    wait(1.5)

