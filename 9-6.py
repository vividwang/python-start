class Restaurant():
    def __init__(self,restaurantName,cuisineType):
        self.name = restaurantName
        self.cuisineType = cuisineType
        self.numberServed = 0

    def describeRestaurant(self):
        print("The restaurant name is " + self.name.title())
        print("The cuisine type is " + self.cuisineType)

    def openRestaurant(self):
        print("The restaurant is open!")

    def setNumberServed(self,number):
        self.numberServed = number

    def incrementNumberServed(self,number):
        self.numberServed += number

class IceCreamStand(Restaurant):
    def __init__(self,restaurantName,cuisineType):
        super().__init__(restaurantName,cuisineType)
        self.flavors = ['orange','pineapple','apple']

    def showFlavors(self):
        for item in self.flavors:
            print(item)

myIceCream = IceCreamStand('Panda','Chinese')
myIceCream.showFlavors()