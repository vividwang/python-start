currentUsers = ['Eric','Jamme','Sonde','Vanke','Loude']
newUsers = ['Eric','James','Mark','Vanke','kerry']

for newUser in newUsers:
    for currentUser in currentUsers:
        if newUser.lower() == currentUser.lower():
            print('You need find another name!')
        else:
            print('You can use this name!')