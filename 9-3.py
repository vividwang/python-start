class User():
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName

    def describeUser(self):
        print("User name was " + self.firstName.title() + ' ' + self.lastName.title() + ".")

    def greetUser(self):
        print("Hi " + self.firstName.title() +  ' ' + self.lastName.title() + ".")

user1 = User('Jim','Harry')
user1.describeUser()
user1.greetUser()

user2 = User('Tom','Mkinson')
user2.describeUser()
user2.describeUser()

user3 = User('mike','pating')
user3.describeUser()
user3.greetUser()