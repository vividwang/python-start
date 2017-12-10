class User():
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.loginAttempts = 0

    def incrementLoginAttempts(self):
        self.loginAttempts += 1
    def resetLoginAttempts(self):
        self.loginAttempts = 0

    def describeUser(self):
        print("User name was " + self.firstName.title() + ' ' + self.lastName.title() + ".")

    def greetUser(self):
        print("Hi " + self.firstName.title() +  ' ' + self.lastName.title() + ".")

newUser = User('Tom','Jerrson')
newUser.incrementLoginAttempts()
newUser.incrementLoginAttempts()
newUser.incrementLoginAttempts()
print(newUser.loginAttempts)
newUser.resetLoginAttempts()
print(newUser.loginAttempts)
