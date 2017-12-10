stopFlag = False
data = {}

while not stopFlag:
    name = input("what's your name?")
    place = input("If you could visit one place in the world,where would you go?")
    data[name] = place

    repeat = input("Would you like to let another person respond?(yes/no)")
    if repeat == 'no':
        stopFlag  = True

for name,place in data.items():
    print(name.title() + ' would go to ' + place + '.')