class Privileges():
    def __init__(self):
        self.privileges = ["can add post","can delete post","can be user"]
    def showPrivileges(self):
        for item in self.privileges:
            print(item)

class Admin():
    def __init__(self):
        self.privileges = Privileges()

admin = Admin()
admin.privileges.showPrivileges()

