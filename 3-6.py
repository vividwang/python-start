inviters = ['Lordy','Glory','Flandre','Sand']

print('I have found a bigger board.')

inviters.insert(0,'Westwood')
inviters.insert(2,'Tony')
inviters.append('Xean')

for item in inviters:
    print('Welcome to join dinner, ' + item.title() + '.')