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

myRestaurant = Restaurant('My Restaurant','Chinese')
print(myRestaurant.numberServed)
myRestaurant.numberServed = 10
print(myRestaurant.numberServed)
myRestaurant.setNumberServed(16)
print(myRestaurant.numberServed)
myRestaurant.incrementNumberServed(16)
print(myRestaurant.numberServed)
