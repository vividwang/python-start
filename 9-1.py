class Restaurant():
    def __init__(self,restaurantName,cuisineType):
        self.name = restaurantName
        self.cuisineType = cuisineType

    def describeRestaurant(self):
        print("The restaurant name is " + self.name.title())
        print("The cuisine type is " + self.cuisineType)

    def openRestaurant(self):
        print("The restaurant is open!")

myRestaurant = Restaurant('New era','Chinese')
myRestaurant.describeRestaurant()
myRestaurant.openRestaurant()