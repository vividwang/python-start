inviters = ['Lordy','Glory','Flandre','Sand']

print('I have found a bigger board.')

inviters.insert(0,'Westwood')
inviters.insert(2,'Tony')
inviters.append('Xean')

print('I could only get two inviters to have dinner.')

inviters.pop()
inviters.pop()
inviters.pop()
inviters.pop()
inviters.pop()

for item in inviters:
    print('Welcome to join dinner, ' + item.title() + '.')

del inviters[0]
del inviters[0]

print(inviters)