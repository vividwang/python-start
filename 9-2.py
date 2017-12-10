class Restaurant():
    def __init__(self,restaurantName,cuisineType):
        self.name = restaurantName
        self.cuisineType = cuisineType

    def describeRestaurant(self):
        print("The restaurant name is " + self.name.title())
        print("The cuisine type is " + self.cuisineType)

    def openRestaurant(self):
        print("The restaurant is open!")

myRestaurant = Restaurant('William Restaurant','West')
myRestaurant.describeRestaurant()
myRestaurant.openRestaurant()

newRestaurant = Restaurant('Hange Home','Chinese')
newRestaurant.describeRestaurant()
newRestaurant.describeRestaurant()

nextRestaurant = Restaurant('panda','Chinese')
nextRestaurant.describeRestaurant()
nextRestaurant.describeRestaurant()