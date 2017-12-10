class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometerReading = 0

    def getDescriptiveName(self):
        longName = str(self.year) + ' ' + self.make + ' ' + self.model
        return longName.title()
    def readOdometerReading(self,mileage):
        if mileage >= self.odometerReading:
            self.odometerReading = mileage
        else:
            print("You can't roll back an odometer!")
    def incrementOdometer(self,miles):
        self.odometerReading += miles

class Battery():
    def __init__(self,batterySize = 70):
        self.batterySize = batterySize

    def upgradeBattery(self):
        if self.batterySize  != 85:
            self.batterySize = 85

    def getRange(self):
        if self.batterySize == 70:
            range = 240
        elif self.batterySize == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

class EletricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery(80)

myTesla = EletricCar('tesla','model s',2016)
print(myTesla.getDescriptiveName())
myTesla.battery.upgradeBattery()
myTesla.battery.getRange()