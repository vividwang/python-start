class User():
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName

    def describeUser(self):
        print("User name was " + self.firstName.title() + ' ' + self.lastName.title() + ".")

    def greetUser(self):
        print("Hi " + self.firstName.title() +  ' ' + self.lastName.title() + ".")


class Admin(User):
    def __init__(self,firstName,lastName):
        super().__init__(firstName,lastName)
        self.privileges =  ["can add post","can delete post","can be user"]

    def showPrivileges(self):
        for item in self.privileges:
            print(item)

admin = Admin('Henry','Lee')
admin.showPrivileges()